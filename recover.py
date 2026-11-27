#!/usr/bin/env python3
"""G3 bounded byte recovery, not new mathematical admission."""
import hashlib, json, os, re, subprocess, sys, zipfile, time, importlib.util
from pathlib import Path, PurePosixPath
H=lambda b:hashlib.sha256(b).hexdigest()
def need(x,msg):
    if not x: raise ValueError(msg)
def run(*a,**kw): return subprocess.check_output(a,**kw)
def api(path): return json.loads(run('gh','api',path))
def safezip(p):
    with zipfile.ZipFile(p) as z:
        names=z.namelist()
        need(len(names)==len(set(names)),'duplicate zip path')
        need(all(not PurePosixPath(n).is_absolute() and '..' not in PurePosixPath(n).parts for n in names),'unsafe zip path')
        need(z.testzip() is None,'CRC')
def write(p,x): p.write_text(json.dumps(x,indent=2)+'\n')
repo=os.environ['GITHUB_REPOSITORY']; root=Path(sys.argv[1]).resolve(); dest=Path(sys.argv[2]).resolve()
dest.mkdir(parents=True,exist_ok=False); tmp=Path(os.environ['RUNNER_TEMP'])/'nf618-archives';tmp.mkdir(exist_ok=False)
c=json.loads(Path('census.json').read_text())
need(run('git','hash-object','census.json',text=True).strip()=='a8be4e13de5d384c8056928abbafa65d18103cd5','census blob')
need(run('git','-C',str(root),'rev-parse','HEAD',text=True).strip()=='5801507d416e4a699c002920b2441f5aa0c19aef','research pin')
lp=root/'notes/provisional/NF618CertifiedSlotLedgerBatch24R1.json'
need(run('git','hash-object',str(lp),text=True).strip()==c['ledger_blob'],'ledger blob')
l=json.loads(lp.read_text())
groups={g['group']:g for g in l['groups']}
need(len(groups)==28 and len(c['archives'])==76,'inventory')
need(len({x['name'] for x in c['archives']})==76,'unique archive names')
for x in c['archives']: need(l['archives'][x['name']]==x['sha256'],'ledger digest')
targets=[x for x in c['archives'] if 'checkpoint' not in x['name']]
need(len(targets)==55,'source/evidence scope')
payload=c['other_ledger_entries'][0];need(payload['name']=='nf690-payload' and payload['sha256']==l['archives'][payload['name']],'payload identity')
targets.append(payload)
checks=[]; paths={}; runmeta={}
for x in targets:
    name=x['name']; ident=x['artifact_id']; p=tmp/(name+'.zip' if not name.endswith('.zip') else name)
    rec={'name':name,'artifact_id':ident,'sha256':x['sha256']}
    try:
        need(re.fullmatch(r'[A-Za-z0-9_.-]+',name),'artifact name')
        meta=api(f'repos/{repo}/actions/artifacts/{ident}')
        need(meta['id']==ident and not meta['expired'],'artifact identity/expiry')
        need(meta['digest']=='sha256:'+x['sha256'],'reported digest')
        producer=meta['workflow_run']['id']
        need(producer==x.get('producer_run',producer),'producer run identity')
        if producer not in runmeta: runmeta[producer]=api(f'repos/{repo}/actions/runs/{producer}')
        need(runmeta[producer]['status']=='completed' and runmeta[producer]['conclusion']=='success','producer success')
        rec['producer_run']=producer
        need(meta['size_in_bytes']==x.get('bytes',meta['size_in_bytes']),'reported size')
        for attempt in range(3):
            try:
                with p.open('wb') as f: subprocess.run(['gh','api',f'repos/{repo}/actions/artifacts/{ident}/zip'],stdout=f,check=True)
                need(p.stat().st_size==meta['size_in_bytes'],'download size')
                need(H(p.read_bytes())==x['sha256'],'download digest')
                safezip(p)
                break
            except Exception:
                if attempt==2: raise
                time.sleep(2**attempt)
        # Preserve exact original bytes in individually Git-safe chunks.
        d=dest/name;d.mkdir()
        chunks=[]
        with p.open('rb') as f:
            i=0
            while data:=f.read(16*1024*1024):
                part=d/f'part{i:04d}.bin';part.write_bytes(data)
                chunks.append({'file':str(part.relative_to(dest)),'bytes':len(data),'sha256':H(data)})
                i+=1
        write(d/'metadata.json',meta)
        rec.update(bytes=p.stat().st_size,chunks=chunks,status='BYTE_PASS')
        paths[name]=p
    except Exception as ex: rec.update(status='BLOCKED',error=str(ex))
    checks.append(rec)
    print(name,rec['status'],flush=True)
    write(dest/'recovery.json',{'scope':'byte recovery, producer status, not new admissions','records':checks,'target_count':len(targets)})
# Recover bank from already authenticated Git chunks, without historical ledger search.
replays=[]
try:
    mp=root/'notes/provisional/NF618ReflexiveDeploymentBank.manifest.json'
    need(run('git','hash-object',str(mp),text=True).strip()=='bc7e2725deae2db936a6b2e66150e199e0778b00','bank manifest')
    m=json.loads(mp.read_text());bank=tmp/'frozen-bank.zip'
    need(len(m['chunks'])==101,'bank chunks')
    with bank.open('wb') as f:
        for x in m['chunks']:
            p=root/x['path'];data=p.read_bytes()
            need(len(data)==x['bytes'] and run('git','hash-object',str(p),text=True).strip()==x['git_blob'],'bank chunk')
            f.write(data)
    need(bank.stat().st_size==m['bytes'] and H(bank.read_bytes())==m['sha256']==l['archives']['NF618ReflexiveDeploymentBank'],'bank digest')
    safezip(bank)
    verifier=root/'scripts/local_replay/NF618AdmitNativeBatch.py'
    need(run('git','hash-object',str(verifier),text=True).strip()=='d27ba77ad9d08b657ad092f4fee1b1c082e1504f','admission verifier')
    spec=importlib.util.spec_from_file_location('admit',verifier);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    def name_for(b,kind):
        if b==0:return 'nf618-repaired-pilot-'+kind
        return f'nf618-batch{b:02d}-{kind}'+('.zip' if b==3 else '')
    for b in range(25):
        g=groups[f'batch{b:02d}']; sn=name_for(b,'source');en=name_for(b,'evidence')
        try:
            r=mod.admit(bank,b,paths[sn],l['archives'][sn],paths[en],l['archives'][en])
            need(r['tables']==g['tables'] and r['rows']==g['rows'] and r['audit_targets']==g['audit_targets'] and r['manifest_sha256']==g['manifest_sha256'],'ledger group binding')
            expected=sorted(s['index'] for s in l['slots'] if s['certified_group']==g['group'])
            need(r['slots']==expected,'ledger slot set')
            replays.append({'batch':b,'status':'SOURCE_EVIDENCE_REPLAY_PASS','receipt':r})
        except Exception as ex: replays.append({'batch':b,'status':'BLOCKED','error':str(ex)})
        print('batch',b,replays[-1]['status'],flush=True)
except Exception as ex:
    replays.append({'status':'BANK_OR_VERIFIER_BLOCKED','error':str(ex)})
write(dest/'replay.json',{'scope':'historical source/evidence replay only; no compiled checkpoint validation, no new slot admissions','records':replays})
passed=sum(x['status']=='BYTE_PASS' for x in checks)
replayed=sum(x['status']=='SOURCE_EVIDENCE_REPLAY_PASS' for x in replays)
write(dest/'summary.json',{'archives_target':56,'archives_byte_pass':passed,'batch_replay_target':25,'batch_source_evidence_replay_pass':replayed,'checkpoint_target_deferred':21,'special_groups_replay_deferred':['combined','mixed','real'],'mathematical_head':'Batch24R1','new_admissions':0,'hold':'unchanged'})
# Return status separately so workflow can preserve partial successes before failing.
print(f'BYTE_PASS {passed}/56; SOURCE_EVIDENCE_REPLAY_PASS {replayed}/25',flush=True)
