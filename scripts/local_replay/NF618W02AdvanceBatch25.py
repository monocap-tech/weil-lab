#!/usr/bin/env python3
"""Replay the Batch25 ledger mutation using authenticated parent and admission receipt.
This is a ledger-only check; native and independent evidence gates are separately recorded.
"""
import hashlib,json,sys
from pathlib import Path
from collections import Counter
def sha(x):return hashlib.sha256(x).hexdigest()
def need(ok,msg):
    if not ok:raise ValueError(msg)
def census(l):
    a=[s for s in l['slots'] if s['certified_group'] is not None]
    b=[s for s in l['slots'] if s['certified_group'] is None]
    need(len(l['slots'])==7835 and all(s['index']==i and type(s['rows']) is int and s['rows']>0 for i,s in enumerate(l['slots'])),'universe')
    c=Counter(s['certified_group'] for s in a);r=Counter()
    for s in a:r[s['certified_group']]+=s['rows']
    need(len(c)==len(l['groups'])==len({g['group'] for g in l['groups']}) and all((c[g['group']],r[g['group']])==(g['tables'],g['rows']) for g in l['groups']),'groups')
    v=[len(a),sum(s['rows'] for s in a),len(b),sum(s['rows'] for s in b)]
    need(v==[l[k] for k in ('certified_tables','certified_rows','residual_tables','residual_rows')],'census')
    return v
p=Path(__file__).resolve().parents[2]/'notes/provisional'
raw=(p/'NF618CertifiedSlotLedgerBatch24R1.json').read_bytes()
r=json.loads((p/'NF618W02Batch25Admission.json').read_bytes())
need(sha(raw)==r['parent']['sha256']=='7910b438110d0ecb1a2ab8caf14646d0ac62440c4893dc80bbcce077bf51ddcf','parent')
need(r['producer']['native_acceptance']==r['independent']['source_regeneration']==r['independent']['source_audit_gate']==r['admission']=='PASS','receipt')
need(r['producer']['sha256']=='e2b088fd8602ae70ed74c4939646b979a6c4c0a190713512831e2db9d58b5b6a' and r['independent']['sha256']=='986eab16adb1aa2d08967cd89088727f54eb216bbb71f3de65a0aaf4bac7322c','evidence pins')
need(r['checkpoint_gate']=='NOT_APPLICABLE_TO_NEW_SOURCE_REPLAY_CONTRACT' and r['universal_dispatch']=='HELD','scope')
l=json.loads(raw);need(census(l)==[6097,29336,1738,8658],'prior')
ids=r['slots'];need(ids==[s['index'] for s in l['slots'] if s['scheduled_batch']==25 and s['certified_group'] is None] and len(ids)==len(set(ids))==120 and sum(l['slots'][i]['rows'] for i in ids)==554,'partition')
l['archives']['nf618-batch25-native-source-evidence']=r['producer']['sha256']
l['archives']['nf618-batch25-independent-replay']=r['independent']['sha256']
l['groups'].append(dict(group='batch25',run=r['producer']['run'],tables=120,rows=554,audit_targets=1260,manifest_sha256=r['manifest_sha256'],evidence_sha256=r['producer']['sha256'],custody_contract='W02-source-replay-v1',independent_replay_sha256=r['independent']['sha256']))
for i in ids:l['slots'][i]['certified_group']='batch25'
l['certified_tables']+=120;l['certified_rows']+=554;l['residual_tables']-=120;l['residual_rows']-=554
need(census(l)==[6217,29890,1618,8104],'new census')
out=(json.dumps(l,indent=2)+'\n').encode()
need(sha(out)==r['result']['sha256']=='65d3a7ca4aff2ad04ffab9f5a08d6f85160e4f7c34a5320ff5a1c20c2e7441ff' and out==(p/'NF618CertifiedSlotLedgerBatch25.json').read_bytes(),'ledger bytes')
print(json.dumps({'ledger_replay':'PASS','sha256':sha(out),'census':census(l)}))
