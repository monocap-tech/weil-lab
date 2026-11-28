#!/usr/bin/env python3
"""Replay the Batch26 ledger mutation using authenticated parent and admission receipt.
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
raw=(p/'NF618CertifiedSlotLedgerBatch25.json').read_bytes()
r=json.loads((p/'NF618W02Batch26Admission.json').read_bytes())
need(sha(raw)==r['parent']['sha256']=='65d3a7ca4aff2ad04ffab9f5a08d6f85160e4f7c34a5320ff5a1c20c2e7441ff','parent')
need(r['producer']['native_acceptance']==r['independent']['source_regeneration']==r['independent']['source_audit_gate']==r['admission']=='PASS','receipt')
need(r['producer']['sha256']=='00e5112731e9e3096318416bf96c27783476d1e1a97fb0d2e8da378e9b4c580f' and r['independent']['sha256']=='28b39e3295f5c095af95ee93e43631891b03a318db273b2de186255b386c4292','evidence pins')
need(r['checkpoint_gate']=='NOT_APPLICABLE_TO_NEW_SOURCE_REPLAY_CONTRACT' and r['universal_dispatch']=='HELD','scope')
l=json.loads(raw);need(census(l)==[6217,29890,1618,8104],'prior')
ids=r['slots'];need(ids==[s['index'] for s in l['slots'] if s['scheduled_batch']==26 and s['certified_group'] is None] and len(ids)==len(set(ids))==120 and sum(l['slots'][i]['rows'] for i in ids)==537,'partition')
l['archives']['nf618-batch26-native-source-evidence']=r['producer']['sha256']
l['archives']['nf618-batch26-independent-replay']=r['independent']['sha256']
l['groups'].append(dict(group='batch26',run=r['producer']['run'],tables=120,rows=537,audit_targets=1243,manifest_sha256=r['manifest_sha256'],evidence_sha256=r['producer']['sha256'],custody_contract='W02-source-replay-v1',independent_replay_sha256=r['independent']['sha256']))
for i in ids:l['slots'][i]['certified_group']='batch26'
l['certified_tables']+=120;l['certified_rows']+=537;l['residual_tables']-=120;l['residual_rows']-=537
need(census(l)==[6337,30427,1498,7567],'new census')
out=(json.dumps(l,indent=2)+'\n').encode()
need(sha(out)==r['result']['sha256']=='52c53dae7339950755b094be4534f8d27e83ac6e80b79472dc53e9e994e01dee' and out==(p/'NF618CertifiedSlotLedgerBatch26.json').read_bytes(),'ledger bytes')
print(json.dumps({'ledger_replay':'PASS','sha256':sha(out),'census':census(l)}))
