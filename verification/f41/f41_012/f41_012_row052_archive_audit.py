#!/usr/bin/env python3
"""F41-012: independent, source-only archive custody of a successful F41-011 row52 run.

This program never runs Lean, certifies the complete 242-row matrix, or promotes
analytic moment-bank/cache/payment proof obligations. Only original SHA-pinned
compiler receipt evidence is inspected. Requires independently recorded outer
ZIP SHA256; accepting the payload's own hash as authority is prohibited.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import re
import zipfile
from pathlib import Path

SCHEMA = 'F41-012-independent-original-row052-archive-custody-v1'
ORIGINAL = 'a431f903254000bb5ad8edbc276ccc8599da98f5'
NF707 = '3d3fa66956bef3a63f90ed9b5325141afaf43cb5'
NF631_ZIP = 'e91a83cae117e98608aefa6849dac178e4ddb58dd1dffbfe37304ad248af9ed9'
NF631_INNER = '9e76e2dea4f46ed5fc3ff8875f804c186cd0cacb86c47295f0cd93d189b9f7e6'
NF702_ZIP = '258637da71e96468ed7c6ac5b0a4480ce06cdee9989aef8e71a4cd09059789e0'
NF631_PAY = 'e6eac42fde8404c5198c78eebe56fdd3fb543549079695a641c9cc60acca9b03'
ALLOWED = {'propext','Classical.choice','Quot.sound'}
ROW = 52
N = 242
PREV_ACCEPTED = 52
EXPECTED = [f'f41011Row052{x}' for x in ('Fast','ActualBank','PaymentTransport')] + [f'f41011Attach052{x}' for x in ('HRowGate','HColGate','VGate','EH','EV','ActualPayment')]
PATH = 'WeilDefect/Generated/F41011/'


def sha(b:bytes)->str: return hashlib.sha256(b).hexdigest()


def axiom_lines(log:str):
    found = {}
    # Rely on exact Lean stdout, not a generated report declaring success.
    for line in log.splitlines():
        line=line.strip()
        m=re.fullmatch(r"'WeilDefect\.(\w+)' depends on axioms: \[([^\]]*)\]",line)
        if m:
            name=m[1]
            assert name not in found,('duplicate axiom declaration',name)
            found[name]={s.strip() for s in m[2].split(',') if s.strip()}
            continue
        m=re.fullmatch(r"'WeilDefect\.(\w+)' does not depend on any axioms",line)
        if m:
            name=m[1]
            assert name not in found,('duplicate axiom declaration',name)
            found[name]=set()
            continue
        # There must be no nonaxiom stdout, so any compiler error also fails.
        assert not line,('unexpected Lean axiom-check output',line)
    assert set(found)==set(EXPECTED),('missing or extra theorem declaration',set(found)^set(EXPECTED))
    assert all(s<=ALLOWED for s in found.values()),('unsafe Lean axioms',found)
    return found


def verify_archive(z:zipfile.ZipFile):
    members=z.namelist()
    assert members and len(members)==len(set(members)), 'missing or duplicate ZIP members'
    assert z.testzip() is None, 'CRC invalid'
    assert all(not (m.startswith('/') or '..' in Path(m).parts) for m in members),'unsafe path member'
    roots={x for x in members if not x.endswith('/')}
    assert all(z.getinfo(x).file_size>0 for x in roots), 'empty archive file'
    required={PATH+'manifest.json',PATH+'Row052.lean',PATH+'Attach052.lean',PATH+'f41-011-kernel-audit.json',
             'f41-011-axioms.log','f41-011-local-row.log','f41-011-full-attach.log','f41-011-original-source.json'}
    assert required<=roots,('missing required files',required-roots)
    manifest=json.loads(z.read(PATH+'manifest.json'))
    audit=json.loads(z.read(PATH+'f41-011-kernel-audit.json'))
    assert manifest['schema']==audit['schema']=='F41-011-original-physical-row052-proposal-v1'
    assert manifest['row']==audit['row']==ROW
    assert manifest['source_original_commit']==audit['source_original_commit']==ORIGINAL
    assert manifest['research_replay_commit']==audit['research_replay_commit']==NF707
    assert manifest['original_nf631_entries_archive_sha256']==audit['original_nf631_entries_archive_sha256']==NF631_ZIP
    assert manifest['original_nf631_entries_gzip_sha256']==audit['original_nf631_entries_gzip_sha256']==NF631_INNER
    assert manifest['nf702_original_input_archive_sha256']==audit['nf702_original_input_archive_sha256']==NF702_ZIP
    assert manifest['nf702_original_payment_payload_sha256']==audit['nf702_original_payment_payload_sha256']==NF631_PAY
    assert (manifest['H_lower_comparisons'],manifest['V_mixed_comparisons'],manifest['center_symmetry_comparisons'])==(53,4,242)
    assert manifest['original_bank']=='neutralNF624Lookup nf690OriginalBank (neutralNF624Index nf690OriginalBank)'
    assert manifest['original_payment']=='nf702OriginalInputs.payment'
    assert manifest['axiom_names']==audit['axiom_names']==EXPECTED
    assert manifest['actual_payment_Lean_passed'] is False
    assert audit['actual_payment_Lean_passed'] is True
    for flag in ['full_F41_matrix_certified','F42_positive','RH_proved']:
        assert manifest[flag] is False and audit[flag] is False,('overpromotion',flag)
    assert audit['source_sha256_links_reverified'] is True
    assert set(manifest['generated_files'])=={'Row052.lean','Attach052.lean'}
    assert manifest['generated_files']==audit['generated_files']
    for name,digest in manifest['generated_files'].items():
        assert sha(z.read(PATH+name))==digest,('source digest mismatch',name)
    printed=axiom_lines(z.read('f41-011-axioms.log').decode())
    assert audit['axiom_report']=={n:sorted(printed[n]) for n in sorted(printed)}
    original=json.loads(z.read('f41-011-original-source.json'))
    assert original['historical_original_immutable_source_commit']==ORIGINAL
    assert original['source_anchor_checks']==42
    assert len(original['source_sha256'])==7
    assert original['data_dependent_full_HV_entry_check_proved'] is False
    assert original['physical_full_matrix_certified'] is False
    # Require concrete original inputs, exact rule, and five proof gate names in source;
    # the generated manifest alone must not be sufficient to pass.
    row=z.read(PATH+'Row052.lean').decode()
    attach=z.read(PATH+'Attach052.lean').decode()
    row_checks=(
      'def f41011Row052Payment : NF625PaymentData',
      'theorem f41011Row052Fast : neutralNF674OriginalRowCheck',
      'nf691OriginalLookup',
      '(neutralNF624Lookup nf690OriginalBank (neutralNF624Index nf690OriginalBank))',
      'theorem f41011Row052ActualBank : neutralNF674OriginalRowCheck',
      'theorem f41011Row052PaymentTransport (p : NF625PaymentData)',
      'neutralNF675OriginalRow_true_of_projection',
      'decide +kernel',
    )
    attach_checks=(
      'import WeilDefect.Generated.NF702Inputs.Data',
      'import WeilDefect.Generated.F41011.Row052',
      'nf702OriginalInputs.payment',
      'theorem f41011Attach052HRowGate :',
      'theorem f41011Attach052HColGate :',
      'theorem f41011Attach052VGate :',
      'theorem f41011Attach052EH :',
      'theorem f41011Attach052EV :',
      'theorem f41011Attach052ActualPayment :',
      'apply f41011Row052PaymentTransport',
      'neutralNF674OriginalRowCheck',
    )
    # Refuse a changed local/full-payment index even if theorem names and manifest survive.
    assert '(52:Fin 242)' in row, 'local theorem literal row index changed'
    assert '(52:Fin 242)' in attach, 'attached theorem literal row index changed'
    for item in row_checks: assert item in row,('local source anchor missing',item)
    for item in attach_checks: assert item in attach,('actual payment anchor missing',item)
    for name in EXPECTED: assert sum(name in s for s in (row,attach))>=1,name
    for name in ['f41-011-local-row.log','f41-011-full-attach.log']:
        log=z.read(name).decode()
        assert log.strip(),('missing compilation evidence',name)
        assert not re.search(r'(^|\n).*?error:',log,re.I),('compiler error',name)
    return {'schema':SCHEMA,'row':ROW,'accepted_previous_original_full_payment_rows':PREV_ACCEPTED,
            'rows_covered_if_independently_verified':PREV_ACCEPTED+1,
            'remaining_original_full_payment_rows':N-PREV_ACCEPTED-1,
            'original_H_lower_comparisons':53,'original_V_mixed_comparisons':4,
            'original_H_symmetry_comparisons':242,
            'original_bank':'NF690 original source-bound lookup','original_payment':'NF702 original global payment',
            'source_file_SHA_links_checked':len(manifest['generated_files'])+len(original['source_sha256']),
            'named_original_Lean_axiom_reports':len(EXPECTED),
            'axiom_names':EXPECTED,'only_standard_axioms_reported':True,
            'physical_full_matrix_certified':False,'analytic_bank_hbank_certified':False,
            'complete_integer_cache_hcache_certified':False,'full_payment_hpay_certified':False,
            'F42_signed_Weil_positivity_certified':False,'RH_proved':False}


def audit(archive:Path,expected_sha:str,run_url:str,run_status:str):
    assert re.fullmatch('[0-9a-f]{64}',expected_sha), 'trusted 64-character ZIP digest required'
    assert sha(archive.read_bytes())==expected_sha,'artifact ZIP SHA does not match independent expected digest'
    assert run_status=='success','hosted run must be independently confirmed successful'
    assert re.fullmatch(r'https://github\.com/monocap-tech/weil-lab/actions/runs/\d+',run_url)
    with zipfile.ZipFile(archive) as z: receipt=verify_archive(z)
    receipt.update({'successful_compiler_run_url':run_url,'artifact_external_SHA256':expected_sha,
                    'independent_archive_audit_passed':True,'F41_row052_archive_custody_complete':True})
    return receipt


def selftest():
    good="'WeilDefect.%s' depends on axioms: [propext, Classical.choice, Quot.sound]" %EXPECTED[0]
    valid='\n'.join("'WeilDefect.%s' depends on axioms: [propext, Classical.choice, Quot.sound]" %n for n in EXPECTED)
    assert len(axiom_lines(valid))==9
    bad=[('unsafe-axiom',valid.replace('propext','sorryAx')),
         ('missing-name',valid.replace(EXPECTED[-1],'f41011Attach047ActualPayment')),
         ('duplicate-name',valid+'\n'+good),
         ('compiler-stdout',valid+'\nerror: elaboration failed')]
    for name,v in bad:
        try:axiom_lines(v)
        except AssertionError:pass
        else:raise AssertionError(('negative control admitted',name))
    print('F41-012 independent receipt checker: 4/4 adversarial axiom controls rejected; no Lean')


def main():
    p=argparse.ArgumentParser()
    sub=p.add_subparsers(dest='mode',required=True)
    sub.add_parser('selftest')
    a=sub.add_parser('audit')
    a.add_argument('--zip',type=Path,required=True)
    a.add_argument('--expected-zip-sha256',required=True)
    a.add_argument('--run-url',required=True)
    a.add_argument('--run-status',required=True,choices=['success','failure','pending'])
    a.add_argument('--output',type=Path,required=True)
    x=p.parse_args()
    if x.mode=='selftest':selftest();return
    result=audit(x.zip,x.expected_zip_sha256,x.run_url,x.run_status)
    x.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print('F41-012 independently verified original physical row52 full-payment Lean archive; ONLY 53/242 rows, no global F41 or RH')

if __name__=='__main__':main()