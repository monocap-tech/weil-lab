#!/usr/bin/env python3
"""Independent source/audit/checkpoint admission for single-batch and session artifacts.
Producer-run success must be checked independently; this script never asserts it.
"""
import argparse, hashlib, io, json, re, tarfile, zipfile
from pathlib import Path, PurePosixPath
H=lambda b:hashlib.sha256(b).hexdigest()
BANK='5c93d86fd9461aff82834cc264c522544f3b2205fc56171886de18623ca31b82'
ALLOWED={'propext','Classical.choice','Quot.sound'}
ROOT='WeilDefect/Generated/NF618HybridPilot/'
def need(x,why):
    if not x:raise ValueError(why)
def opened(path,digest):
    need(H(path.read_bytes())==digest,f'archive digest: {path}')
    z=zipfile.ZipFile(path);ns=z.namelist()
    need(len(ns)==len(set(ns)) and z.testzip() is None,'ZIP integrity')
    need(all(not PurePosixPath(n).is_absolute() and '..' not in PurePosixPath(n).parts for n in ns),'unsafe ZIP path')
    return z
def unique(z,suffix):
    ns=[n for n in z.namelist() if n==suffix or n.endswith('/'+suffix)]
    need(len(ns)==1,'unique member: '+suffix);return z.read(ns[0])
def audit_name(z):
    ns=[n for n in z.namelist() if n.endswith('-audit.json')];need(len(ns)==1,'unique audit');return ns[0]
def table_identity(t):return tuple(t[k] if k!='key' else tuple(t[k]) for k in ('slot','key','rows','source_row_sha256','module'))
def admit(bank,batch,source,sd,evidence,ed,checkpoint=None,cd=None):
    need(0<=batch<40,'batch number')
    with opened(bank,BANK) as bz:
        with zipfile.ZipFile(io.BytesIO(bz.read(f'batches/Batch{batch:02}.zip'))) as q:
            expected=json.loads(q.read('manifest.json'));need(q.testzip() is None,'candidate integrity')
    with opened(source,sd) as s,opened(evidence,ed) as e:
        raw=unique(s,'manifest.json');m=json.loads(raw);need(raw==unique(e,'manifest.json'),'source/evidence manifest mismatch')
        files=m['files'];need(files==expected['files'],'source inventory differs from frozen candidate')
        need(set(s.namelist())==set(files)|{'manifest.json'},'unexpected source archive layout or contents')
        need(all(H(s.read(n))==h for n,h in files.items()),'source hash mismatch')
        fp=H('\n'.join(f'{n}:{h}' for n,h in sorted(files.items())).encode());need(fp==m['source_fingerprint']==expected['source_fingerprint'],'source fingerprint')
        ids={table_identity(t) for t in m['tables']};need(len(ids)==len(m['tables']) and ids=={table_identity(t) for t in expected['tables']},'original table identity')
        targets=set(m['theorems']);need(len(targets)==len(m['theorems']) and targets==set(expected['theorems']),'audit target inventory')
        raw_a=e.read(audit_name(e));a=json.loads(raw_a)
        need(a['manifest_sha256']==H(raw) and set(a['theorems'])==targets,'audit binding')
        need(all(isinstance(v,list) and len(set(v))==len(v) and set(v)<=ALLOWED for v in a['theorems'].values()),'unapproved axiom')
        need((a['tables'],a['rows'])==(len(ids),sum(t[2] for t in ids)),'audit coverage')
        # Cross-check actual printed axiom lines, not just the audit JSON.
        logs=[n for n in e.namelist() if n.endswith('-axioms.log')];need(len(logs)==1,'unique axiom log');log=e.read(logs[0]).decode();found={}
        for n,x in re.findall(r"'WeilDefect\.(\w+)' depends on axioms: \[([^\]]*)\]",log):
            if n in targets:need(n not in found,'duplicate axiom line');found[n]=[v.strip() for v in x.split(',') if v.strip()]
        for n in re.findall(r"'WeilDefect\.(\w+)' does not depend on any axioms",log):
            if n in targets:need(n not in found,'duplicate axiom line');found[n]=[]
        need(found==a['theorems'],'printed axiom report mismatch')
    out={'batch':batch,'tables':a['tables'],'rows':a['rows'],'audit_targets':len(targets),'source_modules':len(files),'slots':sorted(t[0] for t in ids),'source_sha256':sd,'evidence_sha256':ed,'manifest_sha256':H(raw),'source_fingerprint':fp,'source_audit_gate':'PASS','native_acceptance':'REQUIRES VERIFIED PRODUCER SUCCESS'}
    if checkpoint:
        need(cd is not None,'checkpoint digest required')
        with opened(checkpoint,cd) as z:
            need(len(z.namelist())==5,'checkpoint archive member count')
            r=json.loads(unique(z,'checkpoint.json'));binding=unique(z,'nf697-bank-binding.json');b=json.loads(binding);f=b.pop('fingerprint');need(H(binding)==r['base_binding_sha256'] and f==r['base_fingerprint']==H(json.dumps(b,sort_keys=True,separators=(',',':')).encode()),'base binding')
            need(unique(z,'manifest.json')==raw and z.read(audit_name(z))==raw_a and r['manifest_sha256']==H(raw) and r['audit_sha256']==H(raw_a),'checkpoint manifest/audit binding')
            src={ROOT+n:h for n,h in files.items() if n!='Amplitude.lean'};need(r['sources']==src,'checkpoint source closure')
            data=unique(z,'compiled.tar.gz');need(H(data)==r['archive_sha256'],'compiled archive hash')
            seen=set();stems={p.removesuffix('.lean') for p in src}
            with tarfile.open(fileobj=io.BytesIO(data),mode='r:gz') as t:
                for x in t:
                    p=PurePosixPath(x.name);need(x.isfile() and not p.is_absolute() and '..' not in p.parts and x.name.startswith('.lake/build/') and '/WeilDefect/' in x.name and x.name not in seen,'unsafe/duplicate compiled member')
                    stem=('WeilDefect/'+x.name.split('/WeilDefect/',1)[1]).split('.',1)[0];need(stem in stems,'foreign compiled object')
                    need(H(t.extractfile(x).read())==r['objects'].get(x.name),'compiled object hash');seen.add(x.name)
            need(seen==set(r['objects']),'compiled object inventory')
            need(all('.lake/build/lib/lean/'+p+'.olean' in seen for p in stems),'missing olean')
        out.update(checkpoint_gate='PASS',checkpoint_sha256=cd,checkpoint_sources=len(src),checkpoint_objects=len(seen),base_fingerprint=f)
    return out
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--bank',type=Path,required=True);p.add_argument('--batch',type=int,required=True);p.add_argument('--source',type=Path,required=True);p.add_argument('--source-digest',required=True);p.add_argument('--evidence',type=Path,required=True);p.add_argument('--evidence-digest',required=True);p.add_argument('--checkpoint',type=Path);p.add_argument('--checkpoint-digest');a=p.parse_args();print(json.dumps(admit(a.bank,a.batch,a.source,a.source_digest,a.evidence,a.evidence_digest,a.checkpoint,a.checkpoint_digest),indent=2))
