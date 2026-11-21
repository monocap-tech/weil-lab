"""UOI007 negative-control tests; absolutely no network or GitHub Actions."""
from __future__ import annotations

import copy
import io
import json
import pathlib
import tempfile
import unittest
from contextlib import redirect_stdout, redirect_stderr

from uoi007_preflight import (ALLOWED_MODE, PreflightError, SOURCE_PINS,
                               inspect, main)

ROOT = pathlib.Path(__file__).resolve().parents[1]
MANIFEST = json.loads((ROOT/'research/unified/obligations.json').read_text())
CATALOG = json.loads((ROOT/'research/unified/controller/UOI007_frozen_sources.json').read_text())
VALID_ENV = {
    'GITHUB_EVENT_NAME': 'workflow_dispatch',
    'GITHUB_REF': 'refs/heads/main',
    'GITHUB_REPOSITORY': 'monocap-tech/weil-lab',
    'UOI_SOURCE_KEY': 'NF768',
    'UOI_MODE': 'inspect_only',
    'UOI_OBLIGATION_ID': 'CI-FANOUT',
}


class TestUOI007Preflight(unittest.TestCase):
    def probe(self, manifest=None, catalog=None, **kwargs):
        return inspect(copy.deepcopy(MANIFEST if manifest is None else manifest),
                       copy.deepcopy(CATALOG if catalog is None else catalog),
                       source_key='NF768', obligation_id='CI-FANOUT',
                       mode='inspect_only', **kwargs)

    def test_nf768_pinned_dry_run(self):
        r=self.probe()
        self.assertEqual(r['source_commit_sha'],SOURCE_PINS['NF768'][1])
        self.assertTrue(r['preflight_inspection_valid'])
        self.assertFalse(r['execution_permitted'])

    def test_iv025_pinned_dry_run(self):
        r=inspect(MANIFEST,CATALOG,source_key='IV025',obligation_id='CI-FANOUT',mode='inspect_only')
        self.assertEqual(r['source_commit_sha'],SOURCE_PINS['IV025'][1])
        self.assertFalse(r['dispatch_authorized'])

    def test_valid_ci_context(self):
        r=self.probe(enforce_ci_context=True,event='workflow_dispatch',github_ref='refs/heads/main',github_repository='monocap-tech/weil-lab')
        self.assertTrue(r['preflight_inspection_valid'])

    def test_no_ci_context_is_not_a_valid_event(self):
        with self.assertRaises(PreflightError): self.probe(enforce_ci_context=True)

    def test_wrong_event_rejected(self):
        with self.assertRaises(PreflightError): self.probe(enforce_ci_context=True,event='pull_request',github_ref='refs/heads/main',github_repository='monocap-tech/weil-lab')

    def test_non_main_ref_rejected(self):
        with self.assertRaises(PreflightError): self.probe(enforce_ci_context=True,event='workflow_dispatch',github_ref='refs/heads/research/nf768',github_repository='monocap-tech/weil-lab')

    def test_wrong_repository_rejected(self):
        with self.assertRaises(PreflightError): self.probe(enforce_ci_context=True,event='workflow_dispatch',github_ref='refs/heads/main',github_repository='attacker/fork')

    def test_execute_mode_rejected(self):
        with self.assertRaises(PreflightError): inspect(MANIFEST,CATALOG,source_key='NF768',obligation_id='CI-FANOUT',mode='execute')

    def test_invented_source_key_rejected(self):
        with self.assertRaises(PreflightError): inspect(MANIFEST,CATALOG,source_key='NF999',obligation_id='CI-FANOUT',mode='inspect_only')

    def test_injection_source_key_rejected(self):
        with self.assertRaises(PreflightError): inspect(MANIFEST,CATALOG,source_key='NF768; echo hacked',obligation_id='CI-FANOUT',mode='inspect_only')

    def test_wrong_obligation_rejected(self):
        with self.assertRaises(PreflightError): inspect(MANIFEST,CATALOG,source_key='NF768',obligation_id='RD-ARITH-ESTIMATE',mode='inspect_only')

    def test_changed_sha_rejected(self):
        c=copy.deepcopy(CATALOG); c['sources']['NF768']['commit_sha']='0'*40
        with self.assertRaises(PreflightError): self.probe(catalog=c)

    def test_mutable_branch_rejected(self):
        c=copy.deepcopy(CATALOG);c['sources']['IV025']['branch']='main'
        with self.assertRaises(PreflightError):self.probe(catalog=c)

    def test_malicious_new_catalog_source_rejected(self):
        c=copy.deepcopy(CATALOG); c['sources']['NF000']=copy.deepcopy(c['sources']['NF768'])
        with self.assertRaises(PreflightError):self.probe(catalog=c)

    def test_wrong_repo_in_catalog_rejected(self):
        c=copy.deepcopy(CATALOG);c['sources']['NF768']['repository']='attacker/fork'
        with self.assertRaises(PreflightError):self.probe(catalog=c)

    def test_extra_authorization_flag_rejected(self):
        c=copy.deepcopy(CATALOG);c['approved_to_dispatch']=True
        with self.assertRaises(PreflightError):self.probe(catalog=c)

    def test_approval_self_assertion_rejected(self):
        c=copy.deepcopy(CATALOG);c['security_state']['external_operator_approval_authenticated']=True
        with self.assertRaises(PreflightError):self.probe(catalog=c)

    def test_required_checks_self_assertion_rejected(self):
        c=copy.deepcopy(CATALOG);c['security_state']['required_checks_authenticated']=True
        with self.assertRaises(PreflightError):self.probe(catalog=c)

    def test_catalog_execution_enable_rejected(self):
        c=copy.deepcopy(CATALOG);c['security_state']['research_execution_enabled']=True
        with self.assertRaises(PreflightError):self.probe(catalog=c)

    def test_hold_lift_rejected(self):
        m=copy.deepcopy(MANIFEST);m['authority']['execution_policy']='dispatch'
        with self.assertRaises(PreflightError):self.probe(manifest=m)

    def test_manifest_automatic_dispatch_rejected(self):
        m=copy.deepcopy(MANIFEST);m['authority']['automatic_dispatch']=True
        with self.assertRaises(PreflightError):self.probe(manifest=m)

    def test_fake_math_acceptance_rejected(self):
        m=copy.deepcopy(MANIFEST);m['obligations'][1]['standing']='accepted'
        with self.assertRaises(PreflightError):self.probe(manifest=m)

    def test_unknown_schema_rejected(self):
        c=copy.deepcopy(CATALOG);c['schema_version']=2
        with self.assertRaises(PreflightError):self.probe(catalog=c)

    def test_default_branch_missing_rejected(self):
        c=copy.deepcopy(CATALOG);c['candidate_controller_location']='governance/uoi000'
        with self.assertRaises(PreflightError):self.probe(catalog=c)

    def test_report_never_grants_authority(self):
        for name in SOURCE_PINS:
            r=inspect(MANIFEST,CATALOG,source_key=name,obligation_id='CI-FANOUT',mode=ALLOWED_MODE)
            self.assertFalse(r['dispatch_authorized'])
            self.assertFalse(r['execution_permitted'])
            self.assertFalse(r['mathematical_promotion_authorized'])
            self.assertFalse(r['external_operator_approval_authenticated'])
            self.assertFalse(r['fresh_remote_commit_attestation'])

    def test_valid_cli_offline(self):
        with io.StringIO() as output,redirect_stdout(output):
            code=main(['--manifest',str(ROOT/'research/unified/obligations.json'), '--catalog',str(ROOT/'research/unified/controller/UOI007_frozen_sources.json'),'--source-key','NF768'])
            r=json.loads(output.getvalue())
        self.assertEqual(code,0)
        self.assertEqual(r['source_key'],'NF768')

    def test_valid_env_cli(self):
        with io.StringIO() as output,redirect_stdout(output):
            code=main(['--manifest',str(ROOT/'research/unified/obligations.json'),'--catalog',str(ROOT/'research/unified/controller/UOI007_frozen_sources.json'),'--from-env'],environ=VALID_ENV)
            r=json.loads(output.getvalue())
        self.assertEqual(code,0)
        self.assertFalse(r['execution_permitted'])

    def test_missing_env_cli_rejected(self):
        with io.StringIO() as err,redirect_stderr(err):
            code=main(['--manifest',str(ROOT/'research/unified/obligations.json'),'--catalog',str(ROOT/'research/unified/controller/UOI007_frozen_sources.json'),'--from-env'],environ={})
        self.assertEqual(code,1)

    def test_cli_env_conflict_rejected(self):
        with io.StringIO() as err,redirect_stderr(err):
            code=main(['--manifest',str(ROOT/'research/unified/obligations.json'),'--catalog',str(ROOT/'research/unified/controller/UOI007_frozen_sources.json'),'--from-env','--source-key','NF768'],environ=VALID_ENV)
        self.assertEqual(code,1)

    def test_script_does_not_mutate_sources(self):
        paths=[ROOT/'research/unified/obligations.json',ROOT/'research/unified/controller/UOI007_frozen_sources.json']
        before=[p.read_bytes() for p in paths]
        self.probe()
        self.assertEqual(before,[p.read_bytes() for p in paths])


if __name__=='__main__':unittest.main()
