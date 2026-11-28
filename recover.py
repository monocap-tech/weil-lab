import hashlib,json,os,re,subprocess,sys,zipfile,time
from pathlib import Path,PurePosixPath
H=lambda b:hashlib.sha256(b).hexdigest()
def need(x,msg):
    if not x:raise ValueError(msg)
def run(*a,**kw):return subprocess.check_output(a,**kw)
def api(path):return json.loads(run('gh','api',path))
repo=os.environ['GITHUB_REPOSITORY'];branch='custody/nf618-w02-producer-dependencies'
c=json.loads(Path('dependency-census.json').read_text());targets=[x for x in c['inputs'] if x['id']!=14558233793]
need(len({x['id'] for x in targets})==len(targets),'unique input IDs')
dest=Path('archives');dest.mkdir(exist_ok=True)
tmp=Path(os.environ['RUNNER_TEMP'])/'nf618-input.zip'
def commit(paths,msg):
    head=run('git','rev-parse','HEAD',text=True).strip()
    subprocess.run(['git','fetch','--no-tags','origin',branch],check=True)
    need(run('git','rev-parse','FETCH_HEAD',text=True).strip()==head,'branch lease')
    subprocess.run(['git','add','--']+[str(x) for x in paths],check=True)
    subprocess.run(['git','commit','-m',msg+' [skip ci]'],check=True)
    subprocess.run(['git','push','origin','HEAD:refs/heads/'+branch],check=True)
    subprocess.run(['git','fetch','--no-tags','origin',branch],check=True)
    need(run('git','rev-parse','HEAD',text=True).strip()==run('git','rev-parse','FETCH_HEAD',text=True).strip(),'remote head')
def write(p,v):p.write_text(json.dumps(v,indent=2)+'\n')
# Preserve each independently. Bound disk and network to one archive at a time.
for x in targets:
    d=dest/str(x['id']);need(not d.exists(),'existing input, explicit review required');d.mkdir()
    r=dict(x)
    try:
        m=api(f"repos/{repo}/actions/artifacts/{x['id']}")
        need(m['id']==x['id'] and not m['expired'] and m['digest']=='sha256:'+x['sha256'],'metadata binding')
        need(m['size_in_bytes']<=1024**3,'per-archive size limit 1 GiB')
        prod=api(f"repos/{repo}/actions/runs/{m['workflow_run']['id']}")
        r.update(producer_run=prod['id'],producer_conclusion=prod['conclusion'],bytes=m['size_in_bytes'])
        # Historical input archive may predate terminal producer success; retain and report status rather than silently discard.
        for attempt in range(3):
            try:
                with tmp.open('wb') as f:subprocess.run(['gh','api',f"repos/{repo}/actions/artifacts/{x['id']}/zip"],stdout=f,check=True)
                need(tmp.stat().st_size==m['size_in_bytes'] and H(tmp.read_bytes())==x['sha256'],'download identity')
                with zipfile.ZipFile(tmp) as z:
                    ns=z.namelist()
                    need(len(ns)==len(set(ns)) and all(not PurePosixPath(n).is_absolute() and '..' not in PurePosixPath(n).parts for n in ns),'unsafe ZIP')
                    need(z.testzip() is None,'ZIP CRC')
                break
            except Exception:
                if attempt==2:raise
                time.sleep(2**attempt)
        chunks=[]
        with tmp.open('rb') as f:
            i=0
            while data:=f.read(16*1024**2):
                p=d/f'part{i:04d}.bin';p.write_bytes(data);chunks.append({'file':p.name,'sha256':H(data),'bytes':len(data)});i+=1
        write(d/'metadata.json',m);r.update(status='BYTE_PASS',chunks=chunks)
    except Exception as ex:r.update(status='BLOCKED',error=str(ex))
    finally:tmp.unlink(missing_ok=True)
    write(d/'receipt.json',r)
    commit([d],f"NF618 preserve producer input {x['id']}")
    need(run('git','show','FETCH_HEAD:'+str(d/'receipt.json'))==(d/'receipt.json').read_bytes(),'remote receipt')
    if r['status']=='BYTE_PASS':
        h=hashlib.sha256()
        for p in r['chunks']:
            data=run('git','show','FETCH_HEAD:'+str(d/p['file']))
            need(H(data)==p['sha256'] and len(data)==p['bytes'],'remote chunk')
            h.update(data)
        need(h.hexdigest()==r['sha256'],'remote digest')
    print(r['id'],r['name'],r['status'],flush=True)
rows=[json.loads(p.read_text()) for p in sorted(dest.glob('*/receipt.json'))]
summary={'target':len(targets),'byte_pass':sum(r['status']=='BYTE_PASS' for r in rows),'source':'direct input census only','semantic_replay':'not performed','recursive_dependency_closure':'not established','hold':'unchanged','new_admissions':0}
write(dest/'summary.json',summary);commit([dest/'summary.json'],'NF618 direct dependency recovery summary')
need(run('git','show','FETCH_HEAD:archives/summary.json')==(dest/'summary.json').read_bytes(),'remote summary')
print(summary)
need(summary['target']==summary['byte_pass'],'incomplete byte recovery')
