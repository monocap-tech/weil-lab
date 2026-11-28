#!/usr/bin/env python3
"""Independent W02 Batch26 admission preflight. Does NOT promote the ledger.

Inputs: immutable producer evidence ZIP, original NF690 payload ZIP, pinned
Batch25 ledger, frozen Batch26 plan, release, GitHub run/jobs/metadata JSON
retrieved independently, and exact pinned generator bytes. A successful
producer plus this check is necessary; durable source/environment replay
and explicit verified ledger commit remain separate.
"""
import argparse,hashlib,json,re,zipfile
from pathlib import Path,PurePosixPath
from collections import Counter
from fractions import Fraction
H=lambda b:hashlib.sha256(b).hexdigest()
B=lambda b:hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def need(ok,msg):
    if not ok:raise ValueError(msg)
def read(path,digest,git=False):
    raw=Path(path).read_bytes()
    need((B if git else H)(raw)==digest,'identity '+str(path))
    return raw
def opened(path,digest):
    z=zipfile.ZipFile(path)
    need(H(Path(path).read_bytes())==digest,'ZIP digest')
    ns=z.namelist()
    need(len(ns)==len(set(ns)) and z.testzip() is None,'ZIP integrity')
    need(all(not PurePosixPath(n).is_absolute() and '..' not in PurePosixPath(n).parts for n in ns),'ZIP path')
    return z
def census(l):
    slots=l['slots']
    need(len(slots)==7835 and all(s['index']==i and type(s['rows']) is int and s['rows']>0 for i,s in enumerate(slots)),'slot universe')
    a=[s for s in slots if s['certified_group'] is not None]; b=[s for s in slots if s['certified_group'] is None]
    result=[len(a),sum(s['rows'] for s in a),len(b),sum(s['rows'] for s in b)]
    need(result==[l[k] for k in ('certified_tables','certified_rows','residual_tables','residual_rows')],'ledger census')
    c=Counter(s['certified_group'] for s in a); r=Counter()
    for s in a:r[s['certified_group']]+=s['rows']
    need(len(l['groups'])==len(c) and len({g['group'] for g in l['groups']})==len(c),'group universe')
    need(all((c[g['group']],r[g['group']])==(g['tables'],g['rows']) for g in l['groups']),'group census')
    return result
def main():
    p=argparse.ArgumentParser()
    for k in ('evidence','payload','ledger','plan','release','run','jobs','metadata','generator','out'):
        p.add_argument('--'+k,type=Path,required=True)
    a=p.parse_args()
    parent=read(a.ledger,'65d3a7ca4aff2ad04ffab9f5a08d6f85160e4f7c34a5320ff5a1c20c2e7441ff')
    l=json.loads(parent);need(census(l)==[6217,29890,1618,8104],'parent standing')
    plan=read(a.plan,'26aef7a4b21aa2985fbbd72675f16be131202a99',True)
    release=json.loads(read(a.release,'cae9fe7d42c32ad7269348b8f0176863c9149986',True))
    need(release['allow_native_batches_25_39'] and not release['allow_dependent_universal_dispatch'],'scope')
    need(release['current_ledger']['sha256']==H(parent),'released parent ledger')
    plan=json.loads(plan);need(plan['batch']==26,'batch identity');ids=sorted(i for g in plan['groups'] for i,_ in g['slots'])
    need(len(ids)==len(set(ids))==120 and plan['rows']==537,'frozen demand')
    need(ids==[s['index'] for s in l['slots'] if s['scheduled_batch']==26 and s['certified_group'] is None],'parent slot partition')
    run=json.loads(a.run.read_bytes());jobs=json.loads(a.jobs.read_bytes());md=json.loads(a.metadata.read_bytes())
    need(run['id']==46102328502 and run['head_sha']=='78a2b73b2806bf3e7d9ed5434ab3eb1100a95519' and run['status']=='completed' and run['conclusion']=='success','producer result')
    need(run['head_branch']=='formalization/nf618-w02-batch26','producer branch')
    need({j['name']:j['conclusion'] for j in jobs['jobs']}=={'replay':'success','custody':'success'},'producer and custody jobs')
    need(md['workflow_run']['id']==run['id'] and md['workflow_run']['head_sha']==run['head_sha'] and md['name']=='nf618-w02-batch26','artifact association')
    ed=md['digest'].removeprefix('sha256:');need(len(ed)==64,'artifact digest')
    need(a.evidence.stat().st_size==md['size_in_bytes'],'artifact size')
    gen=read(a.generator,'ab57f0cf9cf1dd104ed10bf37e7d644aad5801c5',True)
    with opened(a.evidence,ed) as e,opened(a.payload,'2327fbf952d4894c9f28f81cad9e94d226c93131d9ef2fafa14c35f482211b70') as z:
        need(e.read('generate.py')==gen,'producer generator binding')
        raw=z.read('manifest.json');need(H(raw)=='8d064584205c62907a397ebc854630a5481a675923648dcdcb7c4051af218bf7','original manifest')
        bank=json.loads(raw);chashes={f['file']:f['sha256'] for f in bank['files']}
        raw=e.read('manifest.json');m=json.loads(raw);audit=json.loads(e.read('batch26-audit.json'))
        need(m['plan_blob']=='26aef7a4b21aa2985fbbd72675f16be131202a99','new manifest demand binding')
        need(sorted(t['slot'] for t in m['tables'])==ids,'exact new slot set')
        files=m['files'];need(len(files)==170 and all(H(e.read(n))==v for n,v in files.items()),'new source inventory')
        fp=H('\n'.join(f'{n}:{h}' for n,h in sorted(files.items())).encode())
        need(fp==m['source_fingerprint'] and fp!=plan['reflexive_fingerprint'],'new fingerprint, not historical')
        targets=set(m['theorems']);need(len(targets)==len(m['theorems'])==1243,'strict targets')
        need(audit['manifest_sha256']==H(raw) and set(audit['theorems'])==targets and (audit['tables'],audit['rows'])==(120,537),'audit binding')
        found={}
        log=e.read('batch26-axioms.log').decode()
        for n,ax in re.findall(r"'WeilDefect\.(\w+)' depends on axioms: \[([^\]]*)\]",log):
            if n in targets:
                need(n not in found,'duplicate audit');found[n]=[x.strip() for x in ax.split(',') if x.strip()]
        for n in re.findall(r"'WeilDefect\.(\w+)' does not depend on any axioms",log):
            if n in targets:
                need(n not in found,'duplicate audit');found[n]=[]
        need(found==audit['theorems'] and all(set(v)<={'propext','Classical.choice','Quot.sound'} and len(v)==len(set(v)) for v in found.values()),'printed axioms')
        actual=set()
        for t in m['tables']:
            i=t['slot'];s=bank['slots'][i];old=l['slots'][i]
            need(s['index']==i and t['key']==s['key'] and t['rows']==s['rows']==old['rows'],'row count/key')
            need(t['chunk']==s['chunk'] and t['offset']==s['offset'],'chunk locator')
            name=s['chunk']+'.lean';b=z.read(name)
            need(H(b)==chashes[name]==t['chunk_sha256'],'original chunk hash')
            literal=re.findall(r'#\[\n    (.*?)\n  \]',b.decode(),re.S)[s['offset']]
            need(H(literal.encode())==t['source_row_sha256'],'actual frozen row hash')
            n=f'nf618B26Slot{i:05d}';need(t['module']==f'Slot{i:05d}.lean' and t['concrete']==n+'Concrete','exact theorem mapping')
            src=e.read(t['module']).decode();f=Fraction(s['key'][1])
            table=f'def {n}Table : NF624KeyTable := ⟨⟨0,({f.numerator}/{f.denominator}:ℚ)⟩, (nf690{s["chunk"]}[{s["offset"]}]?).getD #[]⟩'
            concrete=f'theorem {n}Concrete : neutralNF690TableSound (neutralNF624BankRead nf690OriginalBank {i}) := by'
            need(table in src and concrete in src,'actual bank-read theorem statement and payload reference')
            wanted={n+x for x in ('CacheEq','CacheSound','RowsCheck','Sound','Concrete')}|{n+f'Row{j}' for j in range(t['rows'])}
            need(set(t['targets'])==wanted and wanted<=targets and not actual&wanted,'per-slot named audit')
            actual|=wanted
        need(len(actual)==1137,'slot audit coverage')
        need(sum(t['rows'] for t in m['tables'])==537,'row census')
        # Check preserved original compiled-bank binding and source equality,
        # including canonical fingerprint and the exact independently recomputed bytes.
        pb=e.read('producer-bank-binding.json');rb=e.read('recomputed-bank-binding.json')
        x,y=json.loads(pb),json.loads(rb)
        ff=x.pop('fingerprint');rf=y.pop('fingerprint')
        for b,h in ((x,ff),(y,rf)):
            need(h==H(json.dumps(b,sort_keys=True,separators=(',',':')).encode()),'base fingerprint')
        need(x['schema']==y['schema'] and x['environment']==y['environment'],'base environment')
        need(all(y['files'].get(k)==v for k,v in x['files'].items()),'all original source identities')
        need(set(y['files'])-set(x['files'])=={'WeilDefect/Arithmetic/ActualZetaOriginalPhysicalTriangularCacheAssembly.lean'},'one allowed extra source')
        # The producer verified non-import of the additional independent module.
        need(e.read('bank-status.txt').strip()==b'BANK_BINDING_PASS','producer bank binding gate')
        hist=json.loads(e.read('nf691-complete-audit.json'))
        need((hist['keys'],hist['rows'],hist['chunks'])==(7835,37994,490) and len(hist['theorems'])==14 and {'nf691OriginalCoverage','nf691OriginalLookup_eq'}<=set(hist['theorems']) and all(set(v)<={'propext','Classical.choice','Quot.sound'} for v in hist['theorems'].values()),'historical bank audit')
        need(e.read('lean-toolchain').strip()==b'leanprover/lean4:v4.34.0','toolchain')
        manifest_sha=H(raw)
    result={'scope':'independent evidence/identity preflight; no ledger promotion; fresh replay of source/environment required before admission','batch':26,'producer_run':run['id'],'producer_head':run['head_sha'],'parent_sha256':H(parent),'tables':120,'rows':537,'slots':ids,'audit_targets':len(targets),'source_modules':len(files),'source_fingerprint':fp,'manifest_sha256':manifest_sha,'evidence_sha256':ed,'base_fingerprint':ff,'source_audit_gate':'PASS','new_admissions':0}
    a.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
