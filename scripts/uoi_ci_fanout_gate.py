#!/usr/bin/env python3
"""Fail-closed, read-only UOI source-branch PR fan-out triage.

Never claims to emulate GitHub's complete YAML/path/branch event semantics. Any
unrecognized syntax stays UNKNOWN and blocks unattended work. No GitHub API,
workflow dispatch, branch changes, shell execution, or accepted-theorem promotion.
"""
from __future__ import annotations

import argparse
import fnmatch
import json
from pathlib import Path
import re
import sys

class GateError(ValueError):
    pass


def _strip_scalar(s: str) -> str:
    s = s.strip()
    if len(s) >= 2 and s[0] == s[-1] and s[0] in "'\"":
        return s[1:-1]
    return s


def _events_from_yaml(source: str) -> dict:
    lines = source.splitlines()
    found = [i for i, line in enumerate(lines) if re.fullmatch(r'on:\s*(?:#.*)?', line)]
    if len(found) != 1:
        raise GateError("expected exactly one literal top-level 'on:' mapping")
    a = found[0] + 1
    out: dict[str, list[str]] = {}
    name = None
    for line in lines[a:]:
        if line and not line[0].isspace() and not line.lstrip().startswith('#'):
            break
        if not line.strip() or line.lstrip().startswith('#'):
            continue
        match = re.fullmatch(r'  ([A-Za-z_]+):\s*(?:#.*)?', line)
        if match:
            name = match.group(1)
            if name in out:
                raise GateError("duplicate event")
            out[name] = []
        elif name is not None and (line.startswith('    ') or line.lstrip().startswith('#')):
            out[name].append(line)
        else:
            raise GateError("unrecognized event-indentation/flow mapping")
    if not out:
        raise GateError("missing events")
    return out


def _event_config(lines: list[str]) -> dict:
    # Only inspect literal paths/types/branches; exotic YAML never passes clean.
    config = {}
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip() or line.lstrip().startswith('#'):
            i += 1
            continue
        m = re.fullmatch(r'    ([a-zA-Z_-]+):\s*(.*)', line)
        if not m:
            raise GateError("unsupported event configuration indentation")
        key, scalar = m.groups()
        if key in config:
            raise GateError("duplicate event config key")
        if scalar.startswith('#'):
            scalar = ''
        if scalar:
            if not (scalar.startswith('[') and scalar.endswith(']')):
                raise GateError("unsupported event configuration scalar")
            config[key] = [_strip_scalar(v) for v in scalar[1:-1].split(',') if v.strip()]
            i += 1
        else:
            vals = []
            i += 1
            while i < len(lines):
                nxt = lines[i]
                if not nxt.strip() or nxt.lstrip().startswith('#'):
                    i += 1
                    continue
                if not nxt.startswith('      '):
                    break
                m2 = re.fullmatch(r'      -\s+(.+?)\s*', nxt)
                if not m2:
                    raise GateError("unsupported multiline event list")
                vals.append(_strip_scalar(m2.group(1)))
                i += 1
            config[key] = vals
    return config


def _trigger_witness(pattern: str, path: str) -> str:
    """Exact, one-prefix '/**', or conservative UNKNOWN for exotic globs."""
    # Pattern negations are order-dependent; never conclude that an unknown glob excludes a change.
    if pattern.startswith('!'):
        return 'unknown'
    if pattern.endswith('/**') and not re.search(r'[?\[\]{}+]', pattern):
        prefix = pattern[:-3]
        if not re.search(r'\*', prefix):
            return 'match' if path.startswith(prefix + '/') else 'no_match'
    if not re.search(r'[?\*\[\]{}+]', pattern):
        return 'match' if pattern == path else 'no_match'
    return 'unknown'


def classify(text: str, changed: list[str], event: str = 'synchronize', base_branch: str = 'main') -> dict:
    events = _events_from_yaml(text)
    unexpected = sorted(set(events) & {'pull_request_target', 'workflow_run', 'issue_comment', 'repository_dispatch'})
    if unexpected:
        return {'status': 'unknown', 'reason': 'sensitive_or_indirect_events:' + ','.join(unexpected)}
    if 'pull_request' not in events:
        return {'status': 'inactive_for_pr_event', 'reason': 'no_pull_request'}
    cfg = _event_config(events['pull_request'])
    if not set(cfg).issubset({'paths', 'paths-ignore', 'branches', 'branches-ignore', 'types'}):
        return {'status': 'unknown', 'reason': 'unsupported_pull_request_config'}
    # GitHub defaults to opened/reopened/synchronize. Labeled-only events are not ordinary synchronization.
    types = cfg.get('types', ['opened', 'reopened', 'synchronize'])
    if event not in types:
        return {'status': 'inactive_for_pr_event', 'reason': 'event_type_excluded'}
    if 'paths' in cfg and 'paths-ignore' in cfg:
        return {'status': 'unknown', 'reason': 'paths_and_paths-ignore_combined'}
    for key in ('branches', 'branches-ignore'):
        if key in cfg:
            results = [_trigger_witness(x, base_branch) for x in cfg[key]]
            if 'unknown' in results:
                return {'status': 'unknown', 'reason': 'branch_pattern_undecidable'}
            positive = 'match' in results
            if key == 'branches' and not positive:
                return {'status': 'inactive_for_pr_event', 'reason': 'base_branch_excluded'}
            if key == 'branches-ignore' and positive:
                return {'status': 'inactive_for_pr_event', 'reason': 'base_branch_ignored'}
    if not changed:
        return {'status': 'unknown', 'reason': 'changed_paths_not_provided'}
    if 'paths' not in cfg and 'paths-ignore' not in cfg:
        return {'status': 'unrestricted', 'reason': 'ordinary_PR_trigger_without_path_filter'}
    if 'paths-ignore' in cfg:
        return {'status': 'unknown', 'reason': 'paths-ignore_requires_full_git_semantics'}
    patterns = cfg['paths']
    if not patterns:
        return {'status': 'unknown', 'reason': 'empty_paths_filter'}
    vals = [_trigger_witness(p, f) for p in patterns for f in changed]
    if 'unknown' in vals:
        return {'status': 'unknown', 'reason': 'glob_not_fully_supported'}
    if 'match' in vals:
        return {'status': 'matched_scoped', 'reason': 'changed_file_matches_literal_or_prefix'}
    return {'status': 'inactive_for_pr_event', 'reason': 'paths_excluded'}


def audit(head: Path, base: Path, changed: list[str], event: str, base_branch: str, min_workflows: int = 0) -> dict:
    result = {'input_kind': 'two_explicit_local_source_checkouts',
              'event': event, 'base_branch': base_branch,
              'changed_files': changed, 'expected_ci_fanout_bounded': False,
              'required_checks_verified': False, 'dispatch_authorized': False,
              'mathematical_promotion_authorized': False, 'branches': {}}
    for name, directory in [('base', base), ('head', head)]:
        wfs = sorted((directory / '.github/workflows').glob('*.yml')) + sorted((directory / '.github/workflows').glob('*.yaml'))
        if len(wfs) < max(1, min_workflows):
            raise GateError(f'{name}: incomplete workflow directory, {len(wfs)}')
        rows = []
        for f in wfs:
            try:
                row = classify(f.read_text(encoding='utf-8'), changed, event, base_branch)
            except (ValueError, UnicodeError) as ex:
                row = {'status': 'unknown', 'reason': str(ex)}
            rows.append({'workflow': f.name, **row})
        risk = [x for x in rows if x['status'] in ('unrestricted', 'unknown')]
        matches = [x for x in rows if x['status'] == 'matched_scoped']
        result['branches'][name] = {'workflow_count': len(rows), 'unsafe_or_unknown': risk,
                                    'matched_scoped': matches, 'unsafe_or_unknown_count': len(risk),
                                    'matched_scoped_count': len(matches)}
    # Even empty risk is not approval: check GitHub's actual event behavior, required checks, and runner budget.
    result['static_negative_controls_cleared'] = not any(
        result['branches'][x]['unsafe_or_unknown'] for x in ('base', 'head'))
    result['next_gate'] = 'operator_verify_branch_rules_required_checks_manifest_order_then_manual_one_job_lease'
    return result


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--head', type=Path, required=True)
    p.add_argument('--base', type=Path, required=True)
    p.add_argument('--changed-files-json', type=Path, required=True)
    p.add_argument('--base-branch', required=True)
    p.add_argument('--event', choices=('opened', 'reopened', 'synchronize'), default='synchronize')
    p.add_argument('--min-workflows', type=int, default=0)
    args = p.parse_args()
    try:
        files = json.loads(args.changed_files_json.read_text())
        if not isinstance(files, list) or not files or any(not isinstance(f,str) or f.startswith('/') or '..' in Path(f).parts for f in files):
            raise GateError('invalid changed path list')
        result = audit(args.head, args.base, files, args.event, args.base_branch, args.min_workflows)
        print(json.dumps(result, indent=2))
        return 0 if result['static_negative_controls_cleared'] else 2
    except (OSError, ValueError) as e:
        print('UOI CI GATE FAIL CLOSED:', e, file=sys.stderr)
        return 3

if __name__ == '__main__':
    raise SystemExit(main())