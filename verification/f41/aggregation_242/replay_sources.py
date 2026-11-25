"""Authenticate original proof archives and materialize their Lean source closure.
No Lean kernel work or frontier promotion is performed here.
"""
import argparse,hashlib,json,os,re,subprocess,sys,tempfile,urllib.request,zipfile
from pathlib import Path,PurePosixPath
ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve().parent
REPO='monocap-tech/weil-lab'
PRODUCER=45526535048
PRODUCER_HEAD='1efb451b3433548ec3c24bf09d5e11d9ed41ec24'
HISTORICAL={
 'nf691':(14562899400,'c0d513078ecb64e1d6ff718fa0163f0e4af229034a11172eaea7d05d17398844',None),
 'nf695':(14569367307,'68a5fafe7ba038639ae628ab87baed86f7e68a07e90a07976633a4dede681015','NF695'),
 'nf702':(14582437652,'258637da71e96468ed7c6ac5b0a4480ce06cdee9989aef8e71a4cd09059789e0','NF702Inputs'),
 'nf707':(14589561404,'46eef0146bd479ca8991b9630581b21c0a37fe1f662dac4fc8c8befbe2660cbe','NF707'),
 'nf698':(14577476562,'98f124f794b15def1b2dd51957cac47eae44362640f2911332b334da93374bf0','NF698Physical'),
 'nf701':(14583015625,'2979f409f4179499e7f5cd499b402d678f507cf1188d88ef373a34843ef915c3','NF701Physical'),
}
BINDINGS=('nf702_input_manifest_sha256','source_original_commit','research_replay_commit','original_nf631_entries_archive_sha256','original_nf631_entries_gzip_sha256','nf702_original_input_archive_sha256','nf702_original_payment_payload_sha256','original_bank','original_payment')
def sha(b):return hashlib.sha256(b).hexdigest()
def api(path):
    req=urllib.request.Request(os.environ['GITHUB_API_URL']+'/repos/'+REPO+path,headers={'Authorization':'Bearer '+os.environ['GH_TOKEN'],'Accept':'application/vnd.github+json'})
    with urllib.request.urlopen(req,timeout=45) as f:return json.load(f)
def success(run_id):
    d=api(f'/actions/runs/{run_id}')
    assert d['id']==run_id and d['status']=='completed' and d['conclusion']=='success'
    assert d['head_repository']['full_name']==REPO
    return d
def artifact_list(run):
    out=[]
    for page in range(1,5):
        a=api(f'/actions/runs/{run}/artifacts?per_page=100&page={page}')['artifacts']
        out.extend(a)
        if len(a)<100:break
    assert len({x['id'] for x in out})==len(out)
    assert len({x['name'] for x in out})==len(out)
    return {x['name']:x for x in out}
def download(artifact_id,digest,dest,run_id=None,name=None,head=None):
    a=api(f'/actions/artifacts/{artifact_id}')
    assert a['id']==artifact_id and not a['expired'] and a['size_in_bytes']>0
    assert re.fullmatch(r'[0-9a-f]{64}',digest) and a['digest']=='sha256:'+digest
    run=a['workflow_run']['id']
    d=success(run)
    if run_id is not None:assert run==run_id
    if name is not None:assert a['name']==name
    if head is not None:assert a['workflow_run']['head_sha']==head==d['head_sha']
    url=os.environ['GITHUB_API_URL']+f'/repos/{REPO}/actions/artifacts/{artifact_id}/zip'
    subprocess.run(['curl','-fsSL','--retry','3','-H','Authorization: Bearer '+os.environ['GH_TOKEN'],url,'-o',str(dest)],check=True)
    assert sha(dest.read_bytes())==digest
    with zipfile.ZipFile(dest) as z:
        ns=z.namelist()
        assert ns and len(ns)==len(set(ns)) and z.testzip() is None
    return {'run_id':run,'artifact_id':artifact_id,'head':d['head_sha'],'zip_sha256':digest,'name':a['name']}
def row_names(i):
    rr=f'{i:03d}';k=f'{2*i-93:03d}';v=f'{2*i-92:03d}'
    return rr,k,v,f'f41-{k}-original-full-payment-row{rr}-kernel-evidence',f'f41-{v}-original-physical-row{rr}-independent-audit'
def historical_pin(i):
    rr,k,v,name,_=row_names(i)
    if i<=72:f=f'f41-{v}-independent-row{rr}-archive-custody.yml'
    elif i<=74:f='f41-shared-independent-audit-073-074.yml'
    else:f='f41-shared-independent-audit-075-078.yml'
    s=(ROOT/'.github/workflows'/f).read_text()
    # Limit extraction to the exact named row job.
    m=re.search(rf'^  independent-original-row{rr}:\n(.*?)(?=^  independent-original-row\d{{3}}:|\Z)',s,re.M|re.S)
    assert m, f
    return parse_pin(m.group(1),name)
def parse_pin(s,name):
    def one(pattern):
        xs=re.findall(pattern,s,re.M)
        assert len(xs)==1,pattern
        return xs[0]
    return {'run_id':int(one(r"^\s+F41_RUN_ID: '(\d+)'$")),
            'artifact_id':int(one(r"^\s+F41_ARTIFACT_ID: '(\d+)'$")),
            'zip_sha256':one(r"^\s+F41_ZIP_SHA256: '([0-9a-f]{64})'$"),
            'head':one(r"assert run\['head_sha'\]=='([0-9a-f]{40})'"),
            'name':name}
def complete_pins(audit_run,work):
    d=success(PRODUCER)
    assert d['head_sha']==PRODUCER_HEAD and d['head_branch']=='main' and d['name']=='F41 completion producer rows079-241'
    a=success(audit_run)
    assert a['name']=='F41 completion independent custody rows079-241'
    assert a['event']=='workflow_run'
    assert a['path'].split('@')[0]=='.github/workflows/f41-completion-audit-079-241.yml'
    producer=artifact_list(PRODUCER); audit=artifact_list(audit_run)
    assert set(producer)=={row_names(i)[3] for i in range(79,242)}
    assert set(audit)=={'f41-completion-external-pins'}|{row_names(i)[4] for i in range(79,242)}
    ext=audit['f41-completion-external-pins'];p=work/'external-pins.zip'
    download(ext['id'],ext['digest'][7:],p,audit_run,ext['name'])
    with zipfile.ZipFile(p) as z:
        x=json.loads(z.read('f41-completion-pins.json'))
    assert x['producer_run']==PRODUCER and x['producer_head']==PRODUCER_HEAD
    assert [r['row'] for r in x['rows']]==list(range(79,242))
    out={}
    for r in x['rows']:
        i=r['row'];rr,k,v,name,receipt=row_names(i);p=producer[name]
        assert r['artifact']==name and r['receipt']==receipt and r['run_id']==PRODUCER and r['head']==PRODUCER_HEAD
        assert r['artifact_id']==p['id'] and 'sha256:'+r['zip_sha256']==p['digest']
        out[i]={'run_id':PRODUCER,'artifact_id':p['id'],'head':PRODUCER_HEAD,'zip_sha256':r['zip_sha256'],'name':name,'receipt':audit[receipt]}
    return out
def install(z,prefix,dest,files):
    for n in z.namelist():
        if not n.startswith(prefix):continue
        rel=n[len(prefix):]
        if not rel.endswith(('.lean','.json')):continue
        # Only flat generated source modules and their manifests; no executable or object extraction.
        assert PurePosixPath(rel).name==rel and rel not in ('.','..')
        p=dest/prefix/rel
        assert not p.exists(),p
        p.parent.mkdir(parents=True,exist_ok=True)
        data=z.read(n);p.write_bytes(data)
        files[p.relative_to(dest).as_posix()]=sha(data)
def check_routes(plan,dest,last):
    for r in plan['rows'][:last+1]:
        p=dest/Path(r['module'].replace('.','/')+'.lean')
        assert p.is_file(),p
        s=p.read_text()
        assert 'theorem '+r['theorem']+' :' in s
        assert 'neutralNF674OriginalRowCheck' in s and 'nf702OriginalInputs.payment' in s
        assert re.search(r'\(\s*'+str(r['row'])+r'\s*:\s*Fin 242\s*\)',s)
def replay(args):
    dest=args.output.resolve()
    assert not dest.exists(),'output must be a fresh directory'
    dest.mkdir(parents=True)
    plan=json.loads((HERE/'plan.json').read_text())
    files={};evidence=[];common=None
    last=78 if args.historical_only else 241
    with tempfile.TemporaryDirectory() as t:
        work=Path(t)
        future={} if args.historical_only else complete_pins(args.audit_run,work)
        for key,(aid,digest,stage) in HISTORICAL.items():
            zpath=work/(key+'.zip')
            ev=download(aid,digest,zpath);evidence.append(ev)
            if stage:
                with zipfile.ZipFile(zpath) as z:install(z,f'WeilDefect/Generated/{stage}/',dest,files)
        subprocess.run([sys.executable,str(ROOT/'verification/f41/f41_002/f41_002_historical_global_row_custody.py'),'audit','--archive-dir',str(work),'--output',str(dest/'historical-custody.json')],check=True)
        for i in range(48,last+1):
            rr,k,v,name,receipt=row_names(i)
            pin=historical_pin(i) if i<=78 else future[i]
            zpath=work/f'row{rr}.zip'
            ev=download(pin['artifact_id'],pin['zip_sha256'],zpath,pin['run_id'],name,pin['head'])
            auditor=ROOT/f'verification/f41/f41_{v}/f41_{v}_row{rr}_archive_audit.py'
            local=work/f'row{rr}-audit.json'
            subprocess.run([sys.executable,str(auditor),'audit','--zip',str(zpath),'--expected-zip-sha256',pin['zip_sha256'],'--run-url',f'https://github.com/{REPO}/actions/runs/{pin["run_id"]}','--run-status','success','--output',str(local)],check=True)
            receipt_data=json.loads(local.read_text())
            assert receipt_data['row']==i and receipt_data['independent_archive_audit_passed']
            if i>=79:
                a=pin['receipt'];rp=work/f'receipt{rr}.zip'
                audit_ev=download(a['id'],a['digest'][7:],rp,args.audit_run,receipt)
                with zipfile.ZipFile(rp) as z:
                    saved=json.loads(z.read('independent-custody.json'))
                    validated=json.loads(z.read('validated-producer.json'))
                assert saved==receipt_data
                assert validated['row']==i and validated['run_id']==pin['run_id'] and validated['head']==pin['head']
                assert validated['artifact_id']==pin['artifact_id'] and validated['zip_sha256']==pin['zip_sha256']
                ev['independent_receipt']=audit_ev
            prefix=f'WeilDefect/Generated/F41{k}/'
            with zipfile.ZipFile(zpath) as z:
                man=json.loads(z.read(prefix+'manifest.json'))
                bindings={key:man[key] for key in BINDINGS}
                if common is None:common=bindings
                assert common==bindings
                install(z,prefix,dest,files)
            evidence.append(dict(ev,row=i));zpath.unlink()
        check_routes(plan,dest,last)
    assert len([e for e in evidence if 'row' in e])==last-47
    if not args.historical_only:
        p=dest/'WeilDefect/Generated/F41Aggregate/AllRows.lean'
        p.parent.mkdir(parents=True,exist_ok=True)
        data=(HERE/'AllRows.lean.in').read_bytes();p.write_bytes(data);files[p.relative_to(dest).as_posix()]=sha(data)
    manifest={'schema':'F41-aggregate-replay-sources-v1','source_only':True,'new_Lean_compilation_performed':False,'row_range':[0,last],'common_bindings':common,'evidence':evidence,'files':files,'F41_global_boolean_Lean_passed':False,'RH_proved':False}
    (dest/'replay-manifest.json').write_text(json.dumps(manifest,indent=2,sort_keys=True)+'\n')
    print(f'Authenticated replay sources for rows0–{last}; {len(files)} files. NO Lean.')
def selftest():
    pins=[historical_pin(i) for i in range(48,79)]
    assert len({p['artifact_id'] for p in pins})==31
    assert len({p['name'] for p in pins})==31
    with tempfile.TemporaryDirectory() as t:
        p=Path(t);f=p/'test.zip';out=p/'out'
        with zipfile.ZipFile(f,'w') as z:
            z.writestr('WeilDefect/Generated/Test/Row.lean','def test := 1')
            z.writestr('WeilDefect/Generated/Test/manifest.json','{}')
        files={}
        with zipfile.ZipFile(f) as z:install(z,'WeilDefect/Generated/Test/',out,files)
        assert len(files)==2
        with zipfile.ZipFile(f) as z:
            try:install(z,'WeilDefect/Generated/Test/',out,files)
            except AssertionError:pass
            else:raise AssertionError('duplicate destination accepted')
        with zipfile.ZipFile(f,'w') as z:z.writestr('WeilDefect/Generated/Test/../escape.lean','bad')
        with zipfile.ZipFile(f) as z:
            try:install(z,'WeilDefect/Generated/Test/',out,files)
            except AssertionError:pass
            else:raise AssertionError('traversal accepted')
    print('31 historical producer pins parsed; replay extraction controls passed. NO Lean.')
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('mode',choices=['selftest','replay']);p.add_argument('--historical-only',action='store_true');p.add_argument('--audit-run',type=int);p.add_argument('--output',type=Path)
    a=p.parse_args()
    if a.mode=='selftest':selftest()
    else:
        assert a.output and (a.historical_only != bool(a.audit_run))
        replay(a)
