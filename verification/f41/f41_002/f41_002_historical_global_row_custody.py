#!/usr/bin/env python3
"""F41-002 reproducible archived ORIGINAL global physical row custody.
Only reauthenticates earlier actual hosted Lean results. NO NEW LEAN or F41 matrix.
"""
import argparse
import hashlib
import json
import re
import zipfile
from pathlib import Path

ZIP = {
  'nf691':('nf691.zip','c0d513078ecb64e1d6ff718fa0163f0e4af229034a11172eaea7d05d17398844'),
  'nf695':('nf695.zip','68a5fafe7ba038639ae628ab87baed86f7e68a07e90a07976633a4dede681015'),
  'nf702':('nf702.zip','258637da71e96468ed7c6ac5b0a4480ce06cdee9989aef8e71a4cd09059789e0'),
  'nf707':('nf707.zip','46eef0146bd479ca8991b9630581b21c0a37fe1f662dac4fc8c8befbe2660cbe'),
}
H_ORIGINAL='9e76e2dea4f46ed5fc3ff8875f804c186cd0cacb86c47295f0cd93d189b9f7e6'
PAY_ORIGINAL='e6eac42fde8404c5198c78eebe56fdd3fb543549079695a641c9cc60acca9b03'
ALLOWED={'propext','Classical.choice','Quot.sound'}
def digest(b):return hashlib.sha256(b).hexdigest()
def unpack(base,name):
    filename,sha=ZIP[name]
    b=(base/filename).read_bytes()
    assert digest(b)==sha,(name,'outer ZIP hash')
    z=zipfile.ZipFile(base/filename)
    ns=z.namelist()
    assert len(ns)==len(set(ns)),(name,'duplicate ZIP member')
    assert ns and z.testzip() is None,(name,'CRC')
    assert all(z.getinfo(x).file_size>0 for x in ns),(name,'empty member')
    return z
def logaudit(contents,expected):
    found={}
    lines=contents.splitlines()
    assert len(lines)==len(expected),('wrong axiom count',len(lines),len(expected))
    for line in lines:
        match=re.fullmatch(r"'WeilDefect\.([^']+)' depends on axioms: \[([^\]]*)\]",line)
        assert match,('unrecognized printed axiom',line)
        name=match[1]
        assert name not in found,('duplicated proof name',name)
        found[name]={s.strip() for s in match[2].split(',') if s.strip()}
        assert found[name]<=ALLOWED,('nonstandard axiom',name,found[name])
    assert set(found)==set(expected),('missing/extra declaration',set(expected)^set(found))
    return found
def selftest():
    base="'WeilDefect.trial' depends on axioms: [propext, Classical.choice, Quot.sound]"
    assert 'trial' in logaudit(base,{'trial'})
    for label,test in [
       ('nonstandard',lambda: logaudit(base.replace('propext','sorryAx'),{'trial'})),
       ('missing-name',lambda: logaudit(base,{'not_trial'})),
       ('duplicate',lambda: logaudit(base+'\n'+base,{'trial'})),
    ]:
        try:test()
        except AssertionError:pass
        else:raise AssertionError(('synthetic refusal failed',label))
    print('F41-002 source receipt selftest: 3/3 changed-axiom/name controls REJECTED; no Lean')
def audit(base):
    with unpack(base,'nf691') as z:
        b=json.loads(z.read('nf691-complete-audit.json'))
        assert b['schema']=='NF691-full-shaped-bank-coverage-audit-v1'
        assert (b['keys'],b['rows'],b['chunks'])==(7835,37994,490)
    with unpack(base,'nf695') as z:
        p=json.loads(z.read('nf695-complete-audit.json'))
        assert p['schema']=='NF695-concrete-bank-original-entry-row-proposals-v1'
        assert p['nf691_accepted_zip_sha256']==ZIP['nf691'][1]
        assert p['widened_digest']==H_ORIGINAL
        assert [x['row'] for x in p['rows']]==list(range(8))
        assert 'full payment attachment remains conditional' in p['scope']
    with unpack(base,'nf702') as z:
        root='WeilDefect/Generated/NF702Inputs/'
        manraw=z.read(root+'manifest.json')
        man=json.loads(manraw)
        auditraw=z.read('nf702-input-complete-audit.json')
        a=json.loads(auditraw)
        assert man['schema']==a['schema']=='NF702-original-global-input-projection-v1'
        assert man['projection_rows']==a['projection_rows']
        assert [x['row'] for x in man['projection_rows']]==list(range(8))
        assert man['rows']==242 and man['entries_sha256']==H_ORIGINAL
        assert man['payment_sha256']==PAY_ORIGINAL
        assert a['manifest_sha256']==digest(manraw)
        for f in man['files']:
            assert digest(z.read(root+f['file']))==f['sha256'],('NF702 source mismatch',f['file'])
        expected={'nf702InputH_symm','nf702OriginalW'}
        for r in man['projection_rows']:
            i=r['row']; stem=f'nf702Attach{i:03d}'
            assert r['theorems']==[stem+s for s in ('HRowGate','HColGate','VGate','EH','EV','ActualPayment')]
            source=z.read(root+r['module']+'.lean').decode()
            for term in (f'theorem {stem}ActualPayment',
                         'neutralNF674OriginalRowCheck',
                         'nf702OriginalInputs.payment',
                         f'nf695Row{i:03d}PaymentTransport'):
                assert term in source,(i,term)
            expected.update(r['theorems'])
        printed=logaudit(z.read('nf702-input-axioms.log').decode(),expected)
        assert set(a['axioms'])==set(printed)
        nf702_files=len(man['files'])
    with unpack(base,'nf707') as z:
        root='WeilDefect/Generated/NF707/'
        man=json.loads(z.read(root+'manifest.json'))
        a=json.loads(z.read('nf707-complete-audit.json'))
        assert man['schema']==a['schema']=='NF707-full-original-payment-row-attachments-v1'
        assert man['records']==a['records']
        assert man['input_manifest_sha256']==digest(manraw)
        assert man['input_audit_sha256']==digest(auditraw)
        assert [x['row'] for x in man['records']]==list(range(8,48))
        assert 'analytical bank validity still separate' in man['scope']
        expected=set()
        for row in man['records']:
            i=row['row'];stem=f'nf707Attach{i:03d}'
            assert row['theorems']==[stem+s for s in ('HRowGate','HColGate','VGate','EH','EV','ActualPayment')]
            source=z.read(root+row['module']+'.lean').decode()
            origin={'NF698Physical':'nf698','NF701Physical':'nf701'}[row['source_stage']]
            for term in (f'theorem {stem}ActualPayment','neutralNF674OriginalRowCheck',
                         'neutralNF624Lookup nf690OriginalBank','nf702OriginalInputs.payment',
                         f'{origin}PhysicalRow{i:03d}PaymentTransport'):
                assert term in source,(i,term)
            expected.update(row['theorems'])
        for f in man['files']:
            assert digest(z.read(root+f['file']))==f['sha256'],('NF707 source mismatch',f['file'])
        printed=logaudit(z.read('nf707-axioms.log').decode(),expected)
        assert set(a['axioms'])==set(printed)
        nf707_files=len(man['files'])
    return {
      'schema':'F41-002-independent-historical-original-global-row000-047-custody-v1',
      'archive_full_sha256':{k:ZIP[k][1] for k in ZIP},
      'original_NF631_HV_widened_gzip_sha256':H_ORIGINAL,
      'original_NF631_payment_payload_sha256':PAY_ORIGINAL,
      'NF691_full_bank_keys':7835,'NF691_degrees':37994,
      'NF702_original_global_HV_rows_Lean_passed':list(range(8)),
      'NF707_original_global_HV_rows_Lean_passed':list(range(8,48)),
      'recovered_unique_original_full_payment_row_checks':48,
      'remaining_original_HV_rows':194,
      'strict_NF702_named_axiom_reports':50,
      'strict_NF707_named_axiom_reports':240,
      'all_reported_axioms_in_standard_whitelist':True,
      'source_member_sha256_links_checked':nf702_files+nf707_files,
      'hosted_successful_original_Lean_runs':[44582623958,44592096206,44626165661,44633937710],
      'new_Lean_compilation_performed':False,
      'physical_analytic_bank_soundness_certified_by_this_recovery':False,
      'complete_original_entry_triangle_certified':False,
      'original_full_cache_and_payment_certified':False,
      'F41_full_physical_matrix_complete':False,
      'F42_signed_Weil_positive':False,
      'RH_proved':False,
      'next_exact_proof_target':'original H/V row48 attached to nf702OriginalInputs.payment, NF690 bank and NF631 original interval radii',
    }
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('mode',choices=['selftest','audit'])
    ap.add_argument('--archive-dir',type=Path,default=Path('.'))
    ap.add_argument('--output',type=Path,default=Path('f41-002-audit.json'))
    a=ap.parse_args()
    if a.mode=='selftest':selftest()
    else:
        j=audit(a.archive_dir)
        a.output.write_text(json.dumps(j,indent=2,sort_keys=True)+'\n')
        print('F41-002 archival recovery PASS: original full-payment row predicates 0–47 previously genuine Lean PASS; 194 remain; no new F41 matrix theorem')
if __name__=='__main__':main()
