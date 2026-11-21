"""Static regression tests, no network/Actions/checkout of research source."""
from __future__ import annotations
import json
import tempfile
import unittest
from pathlib import Path
from uoi_ci_fanout_gate import GateError, audit, classify

BARE='name: old\non:\n  pull_request:\n  workflow_dispatch:\njobs:\n  noop:\n    runs-on: ubuntu-latest\n'
SCOPED='name: test\non:\n  pull_request:\n    paths:\n      - "scripts/source.py"\n      - "WeilDefect/**"\n  workflow_dispatch:\njobs:\n  noop:\n    runs-on: ubuntu-latest\n'
LABELED='name: labeled\non:\n  workflow_dispatch:\n  pull_request:\n    types: [labeled]\njobs:\n  noop:\n    runs-on: ubuntu-latest\n'

class TestFanout(unittest.TestCase):
    def test_unrestricted_detected(self):
        self.assertEqual(classify(BARE,['docs/notes.md'])['status'],'unrestricted')
    def test_literal_source_match(self):
        self.assertEqual(classify(SCOPED,['scripts/source.py'])['status'],'matched_scoped')
    def test_prefix_source_match(self):
        self.assertEqual(classify(SCOPED,['WeilDefect/Arithmetic/Proof.lean'])['status'],'matched_scoped')
    def test_unrelated_path_excluded(self):
        self.assertEqual(classify(SCOPED,['docs/notes.md'])['status'],'inactive_for_pr_event')
    def test_labeled_only_excluded_from_sync(self):
        self.assertEqual(classify(LABELED,['docs/notes.md'])['status'],'inactive_for_pr_event')
    def test_branches_only_is_not_source_scoping(self):
        s='name: b\non:\n  pull_request:\n    branches: [main]\njobs:\n  x:\n    runs-on: ubuntu-latest\n'
        self.assertEqual(classify(s,['docs/notes.md'],base_branch='main')['status'],'unrestricted')
    def test_branches_nonmatching_is_inactive(self):
        s='name: b\non:\n  pull_request:\n    branches: [main]\njobs:\n  x:\n    runs-on: ubuntu-latest\n'
        self.assertEqual(classify(s,['docs/notes.md'],base_branch='research/x')['status'],'inactive_for_pr_event')
    def test_unknown_yaml_event_blocks(self):
        self.assertRaises(GateError,classify,'name: bad\n"on":\n  pull_request:\n',['foo'])
    def test_sensitive_events_unknown(self):
        s='on:\n  pull_request_target:\njobs:\n  noop:\n    runs-on: ubuntu-latest\n'
        self.assertEqual(classify(s,['docs/foo'])['status'],'unknown')
    def test_exotic_glob_unknown(self):
        s='on:\n  pull_request:\n    paths:\n      - "src/[ab]*/**"\n'
        self.assertEqual(classify(s,['docs/foo'])['status'],'unknown')
    def test_unknown_config_avoids_approval(self):
        s='on:\n  pull_request:\n    completely_custom: [x]\n'
        self.assertEqual(classify(s,['foo'])['status'],'unknown')
    def test_missing_change_list_unknown(self):
        self.assertEqual(classify(BARE,[])['status'],'unknown')
    def test_dual_tree_catches_unrepaired_base(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            base=root/'base'/'.github/workflows';head=root/'head'/'.github/workflows'
            base.mkdir(parents=True);head.mkdir(parents=True)
            (base/'old.yml').write_text(BARE)
            (head/'old.yml').write_text(SCOPED)
            p=audit(root/'head',root/'base',['docs/x.md'],'synchronize','research/prev',1)
            self.assertFalse(p['static_negative_controls_cleared'])
            self.assertEqual(p['branches']['base']['unsafe_or_unknown_count'],1)
            self.assertFalse(p['dispatch_authorized'])
    def test_two_scoped_trees_still_no_auto_dispatch(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            for n in ('base','head'):
                dest=root/n/'.github/workflows';dest.mkdir(parents=True)
                (dest/'new.yml').write_text(SCOPED)
            p=audit(root/'head',root/'base',['scripts/source.py'],'synchronize','main',1)
            self.assertTrue(p['static_negative_controls_cleared'])
            self.assertFalse(p['dispatch_authorized'])
            self.assertFalse(p['required_checks_verified'])
    def test_workflow_count_minimum_blocks(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            for n in ('base','head'):
                dest=root/n/'.github/workflows';dest.mkdir(parents=True)
                (dest/'old.yml').write_text(BARE)
            self.assertRaises(GateError,audit,root/'head',root/'base',['README.md'],'synchronize','main',600)
    def test_path_ignore_refuses_false_safety(self):
        s='on:\n  pull_request:\n    paths-ignore:\n      - "docs/**"\n'
        self.assertEqual(classify(s,['docs/foo'])['status'],'unknown')

if __name__=='__main__': unittest.main()
