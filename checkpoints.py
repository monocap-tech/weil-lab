#!/usr/bin/env python3
"""G3 second tranche: special receipts and incremental compiled checkpoint custody."""
import hashlib, json, os, re, subprocess, sys, zipfile, importlib.util, time
from pathlib import Path, PurePosixPath
from fractions import Fraction
H=lambda b:hashlib.sha256(b).hexdigest()
def need(x,msg):
    if not x: raise ValueError(msg)
def run(*a,**kw): return subprocess.check_output(a,**kw)
def api(path): return json.loads(run('gh','api',path))
def write(p,x): p.write_text(json.dumps(x,indent=2)+'\n')
def safezip(p):
    with zipfile.ZipFile(p) as z:
        names=z.namelist()
        need(len(names)==len(set(names)) and all(not PurePosixPath(n).is_absolute() and '..' not in PurePosixPath(n).parts for n in names),'unsafe/duplicate ZIP paths')
        need(z.testzip() is None,'ZIP CRC')
def unique(z,n):
    ns=[p for p in z.namelist() if p==n or p.endswith('/'+n)]
    need(len(ns)==1,'unique ZIP member '+n);return z.read(ns[0])
repo=os.environ['GITHUB_REPOSITORY']; branch='custody/nf618-w02-historical-recovery'
root=Path('research'); old=Path('custody/run_46076027949-attempt_1')
dest=Path('custody/checkpoints');dest.mkdir(exist_ok=True)
tmp=Path(os.environ['RUNNER_TEMP'])/'nf618-checkpoint-work';tmp.mkdir(exist_ok=True)
need(run('git','-C',str(root),'rev-parse','HEAD',text=True).strip()=='5801507d416e4a699c002920b2441f5aa0c19aef','research pin')
need(run('git','hash-object','census.json',text=True).strip()=='a8be4e13de5d384c8056928abbafa65d18103cd5','census pin')
c=json.loads(Path('census.json').read_text()); lp=root/'notes/provisional/NF618CertifiedSlotLedgerBatch24R1.json'
need(run('git','hash-object',str(lp),text=True).strip()==c['ledger_blob'],'ledger pin')
l=json.loads(lp.read_text()); groups={g['group']:g for g in l['groups']}
oldrec={x['name']:x for x in json.loads((old/'recovery.json').read_text())['records']}
need(len(oldrec)==56 and all(x['status']=='BYTE_PASS' for x in oldrec.values()),'historical source/evidence receipts')
def restore(name):
    r=oldrec[name];p=tmp/(name if name.endswith('.zip') else name+'.zip')
    if not p.exists():
        with p.open('wb') as f:
            for ch in r['chunks']:
                data=(old/ch['file']).read_bytes()
                need(len(data)==ch['bytes'] and H(data)==ch['sha256'],'stored chunk '+name);f.write(data)
    need(H(p.read_bytes())==r['sha256']==l['archives'][name],'historical archive digest '+name)
    return p
def commit_paths(paths,message):
    head=run('git','rev-parse','HEAD',text=True).strip()
    subprocess.run(['git','fetch','--no-tags','origin',branch],check=True)
    need(run('git','rev-parse','FETCH_HEAD',text=True).strip()==head,'branch changed')
    subprocess.run(['git','add','--']+[str(p) for p in paths],check=True)
    subprocess.run(['git','commit','-m',message+' [skip ci]'],check=True)
    subprocess.run(['git','push','origin','HEAD:refs/heads/'+branch],check=True)
    subprocess.run(['git','fetch','--no-tags','origin',branch],check=True)
    need(run('git','rev-parse','HEAD',text=True).strip()==run('git','rev-parse','FETCH_HEAD',text=True).strip(),'remote head')
def remote_bytes(p): return run('git','show','FETCH_HEAD:'+str(p))
def check_log(z,logname,expected,report):
    found={}
    for m in re.finditer(r"'WeilDefect\.(\w+)' (?:depends on axioms:\s*\[([^\]]*)\]|does not depend on any axioms)",unique(z,logname).decode()):
        n=m.group(1)
        if n not in expected:continue
        need(n not in found,'duplicate axiom '+n)
        found[n]=[v.strip() for v in (m.group(2) or '').split(',') if v.strip()]
    need(set(found)==set(expected) and found==report,'named audit binding')
    need(all(set(v)<={'propext','Classical.choice','Quot.sound'} for v in found.values()),'axiom whitelist')
def group_slots(group):return sorted(s['index'] for s in l['slots'] if s['certified_group']==group)
# Three special groups: replay their actual historical source/evidence interfaces, not the regular batch format.
special=[]
with zipfile.ZipFile(restore('nf690-payload')) as payload:
    bankraw=payload.read('manifest.json');need(H(bankraw)==l['original_manifest_sha256'],'original bank manifest')
    bm=json.loads(bankraw); slots={s['index']:s for s in bm['slots']}
    def literal(i):
        s=slots[i];raw=payload.read(s['chunk']+'.lean').decode()
        return re.findall(r'#\[\n    (.*?)\n  \]',raw,re.S)[s['offset']]
    for group,srcname,evname,manifest,audit,log in [
        ('combined','nf690-combined-receiver-source','nf690-combined-receiver-evidence','nf690-combined-manifest.json','nf690-combined-audit.json','combined-axioms.log'),
        ('mixed','nf618-mixed-fourth-root-expansion-source','nf618-mixed-fourth-root-expansion-evidence','nf618-mixed-fourth-root-manifest.json','nf618-mixed-fourth-root-audit.json','nf618-mixed-fourth-root-axioms.log'),
        ('real','nf618-real-terminal-slot-evidence','nf618-real-terminal-slot-evidence','nf618-real-slot-manifest.json','nf618-real-slot-audit.json','nf618-real-slot-axioms.log')]:
        try:
            with zipfile.ZipFile(restore(srcname)) as s, zipfile.ZipFile(restore(evname)) as e:
                raw=unique(s,manifest);m=json.loads(raw);a=json.loads(unique(e,audit));g=groups[group]
                need(raw==unique(e,manifest) and H(raw)==g['manifest_sha256'],'manifest binding')
                if group=='combined':
                    ids=sorted(m['slots']);names=m['audit_names']
                    need(m['bank_manifest_sha256']==H(bankraw),'combined bank binding')
                    flat=[i for v in m['banks'].values() for i in v]
                    need(sorted(flat)==ids,'combined disjoint constituent slot inventory')
                elif group=='mixed':
                    ids=sorted(r[0] for r in m['records']);names=m['theorems']
                    for i,h,f,n,ch,o,sha in m['records']:
                        t=slots[i]
                        need(tuple(map(Fraction,t['key']))==(Fraction(h),Fraction(f)) and (n,ch,o)==(t['rows'],t['chunk'],t['offset']),'mixed literal metadata')
                        need(H(literal(i).encode())==sha,'mixed literal digest')
                else:
                    ids=[7834];names=['nf618RealTerminalHalfPos','nf618RealTerminalHalfNeg','nf618RealTerminalCacheSound','nf618RealTerminalRowsCheck','nf618RealTerminalSound','nf618RealTerminalConcrete']
                    need(m==slots[7834] and a['slot']==7834,'real slot identity')
                    need(H(literal(7834).encode())=='7e9c87d3187b4bff1bbedbc4de22d9d6040e04118ada863917b27bd053a10477','real literal digest')
                    need(H(unique(s,'Slot.lean'))==a['source_sha256'],'real proof source')
                if group!='real':
                    need(a['manifest_sha256']==H(raw),'audit manifest binding')
                    for p,sha in m['source_sha256'].items():
                        # Upload root may be stripped to a common ancestor; require one matching source.
                        candidates=[n for n in s.namelist() if n==p or n.endswith('/'+p) or p.endswith('/'+n)]
                        if not candidates: candidates=[n for n in s.namelist() if Path(n).name==Path(p).name]
                        need(len(candidates)==1 and H(s.read(candidates[0]))==sha,'source hash '+p)
                    need((a['tables'],a['rows'])==(g['tables'],g['rows']),'audit coverage')
                need(ids==group_slots(group) and (len(ids),sum(slots[i]['rows'] for i in ids),len(names))==(g['tables'],g['rows'],g['audit_targets']),'ledger group counts/slots')
                check_log(e,log,names,a['theorems'])
                special.append({'group':group,'status':'REPLAY_PASS','tables':g['tables'],'rows':g['rows'],'audit_targets':len(names),'manifest_sha256':H(raw)})
        except Exception as ex:special.append({'group':group,'status':'BLOCKED','error':str(ex)})
        print(special[-1],flush=True)
sp=dest/'special-replay.json'
write(sp,{'scope':'special historical source, literal/slot and named audit replay; no new admissions','records':special})
commit_paths([sp],'NF618 preserve three special historical receipt replays')
need(remote_bytes(sp)==sp.read_bytes(),'remote special replay')
# Restore frozen bank and original verifier from immutable research pin.
mp=root/'notes/provisional/NF618ReflexiveDeploymentBank.manifest.json'
need(run('git','hash-object',str(mp),text=True).strip()=='bc7e2725deae2db936a6b2e66150e199e0778b00','bank manifest')
m=json.loads(mp.read_text());bank=tmp/'frozen-bank.zip'
with bank.open('wb') as f:
    for x in m['chunks']:
        p=root/x['path'];data=p.read_bytes()
        need(len(data)==x['bytes'] and run('git','hash-object',str(p),text=True).strip()==x['git_blob'],'bank chunk');f.write(data)
need(H(bank.read_bytes())==m['sha256']==l['archives']['NF618ReflexiveDeploymentBank'],'frozen bank digest');safezip(bank)
v=root/'scripts/local_replay/NF618AdmitNativeBatch.py'
need(run('git','hash-object',str(v),text=True).strip()=='d27ba77ad9d08b657ad092f4fee1b1c082e1504f','verifier')
spec=importlib.util.spec_from_file_location('admit',v);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
targets=sorted([x for x in c['archives'] if 'checkpoint' in x['name']],key=lambda x:int(re.search(r'batch(\d+)',x['name']).group(1)))
need(len(targets)==21,'checkpoint count')
for x in targets:
    name=x['name'];b=int(re.search(r'batch(\d+)',name).group(1));d=dest/f'batch{b:02d}'
    need(not d.exists(),'existing checkpoint directory: resume only by explicit review')
    d.mkdir();p=tmp/'checkpoint.zip';r={'batch':b,'name':name,'artifact_id':x['artifact_id'],'sha256':x['sha256']}
    try:
        need(l['archives'][name]==x['sha256'],'ledger digest')
        meta=api(f"repos/{repo}/actions/artifacts/{x['artifact_id']}")
        need(meta['id']==x['artifact_id'] and not meta['expired'] and meta['digest']=='sha256:'+x['sha256'] and meta['size_in_bytes']==x['bytes'] and meta['workflow_run']['id']==x['producer_run'],'artifact binding')
        prod=api(f"repos/{repo}/actions/runs/{x['producer_run']}")
        need(prod['status']=='completed' and prod['conclusion']=='success','producer status')
        for attempt in range(3):
            try:
                with p.open('wb') as f:subprocess.run(['gh','api',f"repos/{repo}/actions/artifacts/{x['artifact_id']}/zip"],stdout=f,check=True)
                need(p.stat().st_size==x['bytes'] and H(p.read_bytes())==x['sha256'],'download identity');safezip(p);break
            except Exception:
                if attempt==2:raise
                time.sleep(2**attempt)
        chunks=[]
        with p.open('rb') as f:
            i=0
            while data:=f.read(16*1024*1024):
                part=d/f'part{i:04d}.bin';part.write_bytes(data);chunks.append({'file':part.name,'sha256':H(data),'bytes':len(data)});i+=1
        write(d/'metadata.json',meta)
        r.update(byte_status='PASS',chunks=chunks)
        try:
            sn=f'nf618-batch{b:02d}-source'+('.zip' if b==3 else '')
            en=f'nf618-batch{b:02d}-evidence'+('.zip' if b==3 else '')
            a=mod.admit(bank,b,restore(sn),l['archives'][sn],restore(en),l['archives'][en],p,x['sha256'])
            g=groups[f'batch{b:02d}'];need(a['slots']==group_slots(g['group']) and a['manifest_sha256']==g['manifest_sha256'] and a['checkpoint_gate']=='PASS','checkpoint replay binding')
            r.update(replay_status='PASS',receipt=a)
        except Exception as ex:r.update(replay_status='BLOCKED',error=str(ex))
    except Exception as ex:r.update(byte_status='BLOCKED',error=str(ex))
    finally:p.unlink(missing_ok=True)
    write(d/'receipt.json',r)
    commit_paths([d],f'NF618 preserve historical checkpoint batch {b:02d}')
    need(remote_bytes(d/'receipt.json')==(d/'receipt.json').read_bytes(),'remote receipt')
    if r['byte_status']=='PASS':
        h=hashlib.sha256()
        for ch in r['chunks']:
            data=remote_bytes(d/ch['file']);need(H(data)==ch['sha256'] and len(data)==ch['bytes'],'remote checkpoint chunk');h.update(data)
        need(h.hexdigest()==r['sha256'],'remote checkpoint digest')
    print('CHECKPOINT',b,r['byte_status'],r.get('replay_status'),flush=True)
receipts=[json.loads(p.read_text()) for p in sorted(dest.glob('batch*/receipt.json'))]
summary={'checkpoint_target':21,'byte_pass':sum(r['byte_status']=='PASS' for r in receipts),'checkpoint_replay_pass':sum(r.get('replay_status')=='PASS' for r in receipts),'special_replay_pass':sum(r['status']=='REPLAY_PASS' for r in special),'special_target':3,'head':'Batch24R1','hold':'unchanged','new_admissions':0}
out=dest/'summary.json';write(out,summary);commit_paths([out],'NF618 historical checkpoint and special replay summary');need(remote_bytes(out)==out.read_bytes(),'remote summary')
print(summary)
need(summary['byte_pass']==summary['checkpoint_replay_pass']==21 and summary['special_replay_pass']==3,'bounded scope incomplete')
