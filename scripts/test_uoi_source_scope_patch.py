"""UOI005 staged workflow repair source-integrity regression tests; no network/CI."""
from __future__ import annotations

import copy
import tempfile
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from uoi_source_scope_patch import RepairError, git_blob_sha, patch_yaml, preview, run, check_plan

B = (b"name: NFtest\non:\n  pull_request:\n  workflow_dispatch:\n"
     b"jobs:\n  exact:\n    runs-on: ubuntu-latest\n    steps:\n"
     b"      - run: python scripts/testsource.py\n")
SRC = b"print('audit')\n"
SRC_NAME = 'scripts/testsource.py'
WF = '.github/workflows/test.yml'


def mkplan():
    return {'schema': 'UOI005-proposed-NF768-scoped-PR-repair-v1',
        'research_branch_sha': 'b477d9a8eb6c33781a8eee7c1208de93c705f307',
        'status': 'source-verified-dry-run-proposal-NOT-APPLIED',
        'approved_for_push': False, 'approved_for_pr': False,
        'dispatch_authorized': False, 'accepted_theorems_modified': False,
        'workflows': [
            {'workflow': '.github/workflows/test%d.yml' % i,
             'git_blob_sha': git_blob_sha(B),
             'source_blobs': {SRC_NAME: git_blob_sha(SRC)},
             'pr_paths': ['.github/workflows/test%d.yml'%i, SRC_NAME]}
            for i in range(4)]}


class TestUOI005(unittest.TestCase):
    def make(self, tmp):
        root = Path(tmp) / 'source'
        for i in range(4):
            f = root/'.github/workflows'/('test%d.yml'%i)
            f.parent.mkdir(parents=True, exist_ok=True)
            f.write_bytes(B)
        script = root/SRC_NAME
        script.parent.mkdir(parents=True, exist_ok=True)
        script.write_bytes(SRC)
        return root

    def test_git_blob_identity(self):
        self.assertEqual(git_blob_sha(b''), 'e69de29bb2d1d6434b8b29ae775ad8c2e48c5391')
    def test_manifest_valid(self):
        check_plan(mkplan())
    def test_all_four_staged(self):
        with tempfile.TemporaryDirectory() as td:
            src=self.make(td)
            r=run(src,mkplan())
            self.assertEqual(len(r['files']),4)
            self.assertFalse(r['dispatch_authorized'])
            self.assertFalse(r['entire_workflow_tree_audited'])
    def test_dry_run_does_not_modify_inputs(self):
        with tempfile.TemporaryDirectory() as td:
            src=self.make(td)
            before=(src/'.github/workflows/test0.yml').read_bytes()
            run(src,mkplan())
            self.assertEqual(before,(src/'.github/workflows/test0.yml').read_bytes())
            self.assertFalse((Path(td)/'preview').exists())
    def test_preview_writes_only_separate_dir(self):
        with tempfile.TemporaryDirectory() as td:
            src=self.make(td)
            dst=Path(td)/'preview'
            r=run(src,mkplan(),dst)
            self.assertEqual(len(r['files']),4)
            self.assertIn(b"    paths:\n",(dst/'.github/workflows/test0.yml').read_bytes())
            self.assertEqual(B,(src/'.github/workflows/test0.yml').read_bytes())
    def test_overwrite_guard(self):
        with tempfile.TemporaryDirectory() as td:
            src=self.make(td)
            dst=Path(td)/'preview'
            run(src,mkplan(),dst)
            with self.assertRaises(RepairError):run(src,mkplan(),dst)
    def test_same_root_guard(self):
        with tempfile.TemporaryDirectory() as td:
            src=self.make(td)
            with self.assertRaises(RepairError):run(src,mkplan(),src)
    def test_parent_root_guard(self):
        with tempfile.TemporaryDirectory() as td:
            src=self.make(td)
            with self.assertRaises(RepairError):run(src,mkplan(),Path(td))
    def test_nested_output_guard(self):
        with tempfile.TemporaryDirectory() as td:
            src=self.make(td)
            with self.assertRaises(RepairError):run(src,mkplan(),src/'preview')
    def test_changed_workflow_source_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            src=self.make(td)
            (src/'.github/workflows/test2.yml').write_bytes(B+b'\n')
            with self.assertRaises(RepairError):run(src,mkplan())
    def test_changed_dependency_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            src=self.make(td)
            (src/SRC_NAME).write_bytes(SRC+b'\n')
            with self.assertRaises(RepairError):run(src,mkplan())
    def test_missing_dependency_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            src=self.make(td)
            (src/SRC_NAME).unlink()
            with self.assertRaises(FileNotFoundError):run(src,mkplan())
    def test_jobs_bit_for_bit_preserved(self):
        p=patch_yaml(B,[WF,SRC_NAME]); self.assertEqual(p.split(b'jobs:\n')[1], B.split(b'jobs:\n')[1])
    def test_manual_dispatch_bit_for_bit_preserved(self):
        p=patch_yaml(B,[WF,SRC_NAME]); self.assertEqual(p.count(b'  workflow_dispatch:\n'),1)
    def test_pr_scope_contains_expected_inputs(self):
        p=patch_yaml(B,[WF,SRC_NAME]); self.assertIn(b"      - 'scripts/testsource.py'\n",p)
    def test_repair_of_already_scoped_rejected(self):
        p=patch_yaml(B,[WF,SRC_NAME]); self.assertRaises(RepairError,patch_yaml,p,[WF,SRC_NAME])
    def test_unknown_on_rejected(self):
        self.assertRaises(RepairError,patch_yaml,B.replace(b'on:\n',b"'on':\n"),[WF,SRC_NAME])
    def test_push_trigger_rejected(self):
        self.assertRaises(RepairError,patch_yaml,B.replace(b'  workflow_dispatch:\n',b'  push:\n  workflow_dispatch:\n'),[WF,SRC_NAME])
    def test_false_approval_rejected(self):
        m=mkplan();m['approved_for_pr']=True
        self.assertRaises(RepairError,check_plan,m)
    def test_duplicate_input_rejected(self):
        m=mkplan();m['workflows'][0]['pr_paths'].append(SRC_NAME)
        self.assertRaises(RepairError,check_plan,m)
    def test_missing_source_mapping_rejected(self):
        m=mkplan();m['workflows'][0]['pr_paths']=[m['workflows'][0]['workflow']]
        self.assertRaises(RepairError,check_plan,m)
    def test_path_traversal_rejected(self):
        m=mkplan();m['workflows'][0]['source_blobs']={'../secrets.txt':git_blob_sha(SRC)}
        self.assertRaises(RepairError,check_plan,m)
    def test_duplicate_workflow_rejected(self):
        m=mkplan();m['workflows'][1]=copy.deepcopy(m['workflows'][0])
        self.assertRaises(RepairError,check_plan,m)


if __name__=='__main__':unittest.main()
