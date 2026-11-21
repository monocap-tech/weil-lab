#!/usr/bin/env python3
"""UOI007: offline, no-execution control-plane candidate validation.

No GitHub API, shell, source checkout, file writes, command/job selection,
workflow dispatch, status promotion, or approval issuance. An allowlist match
only confirms consistency with previously pinned *records*; NOT that a fresh
GitHub API lookup, protected-environment review or CI fan-out audit occurred.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path
from uoi_validate import validate as validate_obligations, ManifestError

REPOSITORY = 'monocap-tech/weil-lab'
DEFAULT_BRANCH = 'main'
ALLOWED_MODE = 'inspect_only'
SOURCE_PINS = {
    'NF768': ('research/nf768-original-indexzero-104-111-controlled-kernel',
              'b477d9a8eb6c33781a8eee7c1208de93c705f307'),
    'IV025': ('research/iv025-original-manifest-preflight-recovery',
              'f89952aebfbb1e9775a9fb0dbbe71995ae636b04'),
}
SHA = re.compile(r'^[0-9a-f]{40}$')


class PreflightError(ValueError):
    """Refuse unknown, ambiguous, mutable, or purportedly authorized inputs."""


def _exact_keys(obj: dict, fields: set[str], what: str) -> None:
    if not isinstance(obj, dict) or set(obj) != fields:
        raise PreflightError(f'{what}: unexpected or missing fields')


def inspect(manifest: dict, catalog: dict, *, source_key: str,
            obligation_id: str, mode: str,
            event: str | None = None, github_ref: str | None = None,
            github_repository: str | None = None,
            enforce_ci_context: bool = False) -> dict:
    """Inspect frozen records. NEVER return dispatch or review approval."""
    try:
        nodes = validate_obligations(manifest)
    except (ManifestError, KeyError, TypeError) as ex:
        raise PreflightError('UOI manifest not independently valid: ' + str(ex)) from ex

    if mode != ALLOWED_MODE:
        raise PreflightError('only inspect_only is supported')
    if not isinstance(source_key, str) or source_key not in SOURCE_PINS:
        raise PreflightError('source key is not on the immutable two-snapshot allowlist')
    if obligation_id != 'CI-FANOUT':
        raise PreflightError('only CI-FANOUT is eligible for this inspection-only prototype')
    if nodes['CI-FANOUT']['standing'] != 'open' or nodes['UOI-INTAKE']['standing'] != 'open':
        raise PreflightError('expected unfinished intake/CI obligations')
    if (manifest['authority']['operational_cursor'] != 'UOI-INTAKE'
            or manifest['authority']['execution_policy'] != 'consolidation_hold'):
        raise PreflightError('UOI hold or cursor is no longer the studied revision')
    if enforce_ci_context or event is not None or github_ref is not None or github_repository is not None:
        if (event != 'workflow_dispatch' or github_ref != 'refs/heads/main'
                or github_repository != REPOSITORY):
            raise PreflightError('wrong GitHub event, controller ref, or repository')

    _exact_keys(catalog, {'schema_version', 'source', 'mode', 'sources',
                          'candidate_controller_location', 'security_state'}, 'catalog')
    if catalog['schema_version'] != 1 or catalog['source'] != 'UOI006':
        raise PreflightError('unknown source provenance')
    if catalog['mode'] != ALLOWED_MODE:
        raise PreflightError('catalog cannot authorize execution')
    if catalog['candidate_controller_location'] != 'main':
        raise PreflightError('controller must be reviewed for default branch')
    _exact_keys(catalog['security_state'],
                {'required_checks_authenticated', 'research_execution_enabled',
                 'external_operator_approval_authenticated'}, 'security_state')
    if any(catalog['security_state'][x] is not False for x in
           ('required_checks_authenticated', 'research_execution_enabled',
            'external_operator_approval_authenticated')):
        raise PreflightError('self-asserted approval or protection claim')

    sources = catalog['sources']
    if not isinstance(sources, dict) or set(sources) != set(SOURCE_PINS):
        raise PreflightError('source catalog must contain exactly the frozen pair')
    for key, (branch, sha) in SOURCE_PINS.items():
        row = sources[key]
        _exact_keys(row, {'repository', 'branch', 'commit_sha',
                          'source_issue', 'purpose'}, key)
        if (row['repository'] != REPOSITORY or row['branch'] != branch
                or row['commit_sha'] != sha or not SHA.fullmatch(row['commit_sha'])
                or row['source_issue'] !=
                'https://github.com/monocap-tech/weil-lab/issues/867'
                or row['purpose'] != 'historical_ci_source_inspection'):
            raise PreflightError(key + ': source pin drift or changed scope')

    target_branch, target_sha = SOURCE_PINS[source_key]
    return {
        'schema': 'UOI007-preflight-inspection-v1',
        'preflight_inspection_valid': True,
        'obligation_id': obligation_id,
        'source_key': source_key,
        'source_branch': target_branch,
        'source_commit_sha': target_sha,
        'snapshot_matches_frozen_UOI006_record': True,
        'fresh_remote_commit_attestation': False,
        'required_checks_authenticated': False,
        'external_operator_approval_authenticated': False,
        'source_workflows_fully_audited': False,
        'heavy_runner_lease_issued': False,
        'dispatch_authorized': False,
        'mathematical_promotion_authorized': False,
        'execution_permitted': False,
        'reason': 'inspection-only candidate; active consolidation hold',
    }


def main(argv: list[str] | None = None, environ: dict[str, str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest', type=Path, required=True)
    parser.add_argument('--catalog', type=Path, required=True)
    parser.add_argument('--source-key', choices=sorted(SOURCE_PINS))
    parser.add_argument('--obligation-id', default='CI-FANOUT')
    parser.add_argument('--mode', default=ALLOWED_MODE)
    parser.add_argument('--from-env', action='store_true')
    args = parser.parse_args(argv)
    env = os.environ if environ is None else environ
    try:
        if args.from_env:
            if (args.source_key is not None or args.mode != ALLOWED_MODE
                    or args.obligation_id != 'CI-FANOUT'):
                raise PreflightError('ambiguous env and CLI selectors')
            event = env.get('GITHUB_EVENT_NAME')
            github_ref = env.get('GITHUB_REF')
            repo = env.get('GITHUB_REPOSITORY')
            source_key = env.get('UOI_SOURCE_KEY')
            mode = env.get('UOI_MODE')
            obligation_id = env.get('UOI_OBLIGATION_ID')
        else:
            if args.source_key is None:
                raise PreflightError('offline inspection needs --source-key')
            event = github_ref = repo = None
            source_key = args.source_key
            mode = args.mode
            obligation_id = args.obligation_id
        m = json.loads(args.manifest.read_text(encoding='utf-8'))
        c = json.loads(args.catalog.read_text(encoding='utf-8'))
        result = inspect(m, c, source_key=source_key, obligation_id=obligation_id,
                         mode=mode, event=event, github_ref=github_ref,
                         github_repository=repo,
                         enforce_ci_context=args.from_env)
        print(json.dumps(result, indent=2, sort_keys=True))
        return 0
    except (OSError, ValueError, TypeError, KeyError) as e:
        print('UOI007 preflight FAIL: ' + str(e), file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
