"""Independent custody of the final aggregate producer, not a second Lean compilation."""
import argparse,hashlib,json,os,re,subprocess,tempfile,urllib.request,zipfile
from pathlib import Path,PurePosixPath
HERE=Path(__file__).resolve().parent
REPO='monocap-tech/weil-lab'
WORKFLOW='.github/workflows/f41-aggregation-authenticated-replay.yml'
SOURCE='f41-aggregate-complete-authenticated-replay-sources'
FINAL='f41-aggregate-original-242-row-kernel-evidence'
NAMES=('f41OriginalAllRows','f41OriginalEntryCheck','f41OriginalEnclosures_of_moment_soundness')
ALLOWED={'propext','Classical.choice','Quot.sound'}
SUFFIX=('.olean','.olean.private','.olean.server','.ilean','.ir')
def sha(b):return hashlib.sha256(b).hexdigest()
def stream_sha(f):
    h=hashlib.sha256()
    for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
    return h.hexdigest()
def file_sha(p):
    with p.open('rb') as f:return stream_sha(f)
def read(z,n):return json.loads(z.read(n))
def ranges():return [(i,min(i+15,241)) for i in range(0,242,16)]
def route(i):
    rr=f'{i:03d}';k=f'{2*i-93:03d}'
    if i<8:return f'WeilDefect.Generated.NF695.Row{rr}',f'WeilDefect.Generated.NF702Inputs.Attach{rr}',f'nf702Attach{rr}ActualPayment'
    if i<48:
        stage='NF698Physical' if i<24 else 'NF701Physical'
        return f'WeilDefect.Generated.{stage}.Row{rr}',f'WeilDefect.Generated.NF707.Attach{rr}',f'nf707Attach{rr}ActualPayment'
    return f'WeilDefect.Generated.F41{k}.Row{rr}',f'WeilDefect.Generated.F41{k}.Attach{rr}',f'f41{k}Attach{rr}ActualPayment'
def axiom_log(s,expected):
    found={}
    for line in s.splitlines():
        assert not re.search(r'error:|sorryAx|uses sorry',line,re.I),line
        m=re.fullmatch(r"'WeilDefect\.(\w+)' depends on axioms: \[([^\]]*)\]",line)
        n=re.fullmatch(r"'WeilDefect\.(\w+)' does not depend on any axioms",line)
        if m or n:
            name=(m or n)[1]
            assert name in expected and name not in found
            values=[v.strip() for v in m[2].split(',') if v.strip()] if m else []
            assert len(values)==len(set(values)) and set(values)<=ALLOWED
            found[name]=sorted(values)
    assert set(found)==set(expected)
    return found
def zip_members(z):
    ns=z.namelist()
    assert ns and len(ns)==len(set(ns))
    for name in ns:
        p=PurePosixPath(name)
        assert not p.is_absolute() and '..' not in p.parts and '\\' not in name
        assert not z.getinfo(name).is_dir()
    assert z.testzip() is None
    return set(ns)
def check_hashes(z,files,prefix=''):
    assert isinstance(files,dict) and files
    for name,d in files.items():
        p=PurePosixPath(name)
        assert not p.is_absolute() and '..' not in p.parts and re.fullmatch(r'[0-9a-f]{64}',d)
        with z.open(prefix+name) as f:assert stream_sha(f)==d,name
def validate_run(d,run,head):
    assert d['id']==run and d['status']=='completed' and d['conclusion']=='success'
    assert d['name']=='F41 aggregation authenticated source replay' and d['path'].split('@')[0]==WORKFLOW
    assert d['head_sha']==head and d['head_branch']=='main' and d['head_repository']['full_name']==REPO
    assert d['event'] in ('workflow_run','workflow_dispatch')
def api(path):
    url=os.environ['GITHUB_API_URL']+'/repos/'+REPO+path
    req=urllib.request.Request(url,headers={'Authorization':'Bearer '+os.environ['GH_TOKEN'],'Accept':'application/vnd.github+json'})
    with urllib.request.urlopen(req,timeout=45) as f:return json.load(f)
def names():
    return {SOURCE,FINAL}|{f'f41-aggregate-objects-{lo}-{hi}' for lo,hi in ranges()}
def pins(items,run,head):
    assert len(items)==18 and {x['name'] for x in items}==names()
    assert len({x['id'] for x in items})==18
    for a in items:
        assert a['workflow_run']['id']==run and a['workflow_run']['head_sha']==head
        assert isinstance(a['id'],int) and a['id']>0 and not a['expired'] and a['size_in_bytes']>0
        assert re.fullmatch(r'sha256:[0-9a-f]{64}',a['digest'])
    return {x['name']:x for x in items}
def fetch(a,path,run,head):
    b=api(f'/actions/artifacts/{a["id"]}')
    for key in ('id','name','digest','size_in_bytes','expired'):
        assert b[key]==a[key],key
    assert b['workflow_run']['id']==run and b['workflow_run']['head_sha']==head
    url=os.environ['GITHUB_API_URL']+f'/repos/{REPO}/actions/artifacts/{a["id"]}/zip'
    subprocess.run(['curl','-fsSL','--retry','3','-H','Authorization: Bearer '+os.environ['GH_TOKEN'],url,'-o',str(path)],check=True)
    assert file_sha(path)==a['digest'][7:]
def check_object_set(obj,mods):
    allowed={m.replace('.','/')+s for m in mods for s in SUFFIX}
    required={m.replace('.','/')+'.olean' for m in mods}
    assert required<=set(obj)<=allowed
def audit(run,head,out):
    validate_run(api(f'/actions/runs/{run}'),run,head)
    p=pins(api(f'/actions/runs/{run}/artifacts?per_page=100')['artifacts'],run,head)
    plan=json.loads((HERE/'plan.json').read_text())
    assert [r['row'] for r in plan['rows']]==list(range(242))
    assert [(r['module'],r['theorem']) for r in plan['rows']]==[route(i)[1:] for i in range(242)]
    source=(HERE/'AllRows.lean.in').read_bytes()
    with tempfile.TemporaryDirectory() as t:
        t=Path(t)
        final=t/'final.zip';fetch(p[FINAL],final,run,head)
        with zipfile.ZipFile(final) as z:
            assert zip_members(z)=={'manifest.json','AllRows.lean','aggregate-axioms.log','object-baseline.json','source-replay-manifest.json'}
            m=read(z,'manifest.json')
            raw=z.read('source-replay-manifest.json');base=z.read('object-baseline.json')
            sm=json.loads(raw);baseline=json.loads(base)
            assert m['schema']=='F41-aggregate-kernel-producer-v1' and m['rows']==list(range(242))
            assert z.read('AllRows.lean')==source and m['source_sha256']==sha(source)
            assert m['source_manifest_sha256']==sha(raw) and m['object_baseline_sha256']==sha(base)
            assert m['axioms']==axiom_log(z.read('aggregate-axioms.log').decode(),NAMES)
            assert m['new_Lean_compilation_performed'] is True and m['original_global_boolean_Lean_passed'] is True
            assert m['physical_enclosure_requires_moment_soundness'] is True
            for key in ('analytic_bank_hbank_certified','full_F41_certified','F42_positive','RH_proved'):
                assert m[key] is False
        assert baseline['schema']=='F41-replay-object-baseline-v1' and baseline['source_manifest_sha256']==sha(raw)
        assert all(re.fullmatch(r'[0-9a-f]{64}',baseline[k]) for k in ('bank_binding_sha256','input_binding_sha256'))
        assert baseline['objects'] and all(re.fullmatch(r'[0-9a-f]{64}',x) for x in baseline['objects'].values())
        assert not set(baseline['objects'])&set(m['shard_objects'])
        sp=t/'source.zip';fetch(p[SOURCE],sp,run,head)
        with zipfile.ZipFile(sp) as z:
            assert zip_members(z)==set(sm['files'])|{'replay-manifest.json','historical-custody.json'}
            assert z.read('replay-manifest.json')==raw
            assert sm['schema']=='F41-aggregate-replay-sources-v1' and sm['row_range']==[0,241]
            assert sm['source_only'] is True and sm['new_Lean_compilation_performed'] is False and sm['RH_proved'] is False
            e=[x for x in sm['evidence'] if 'row' in x]
            assert [x['row'] for x in e]==list(range(48,242))
            assert all('independent_receipt' in x for x in e if x['row']>=79)
            assert len({x['artifact_id'] for x in e})==194
            check_hashes(z,sm['files'])
            assert z.read('WeilDefect/Generated/F41Aggregate/AllRows.lean')==source
            for i in range(242):
                for mod in route(i)[:2]:assert mod.replace('.','/')+'.lean' in sm['files']
        sp.unlink()
        objects={};covered=[];terminal={}
        for lo,hi in ranges():
            name=f'f41-aggregate-objects-{lo}-{hi}';path=t/'shard.zip'
            fetch(p[name],path,run,head)
            with zipfile.ZipFile(path) as z:
                ns=zip_members(z);s=read(z,'manifest.json')
                assert s['schema']=='F41-replay-shard-objects-v1' and s['row_range']==[lo,hi]
                assert s['run_id']==str(run) and s['head']==head
                assert s['baseline_sha256']==sha(base) and s['source_manifest_sha256']==sha(raw)
                assert s['new_Lean_compilation_performed'] is True and s['aggregate_certified'] is False
                mods=[mod for i in range(lo,hi+1) for mod in route(i)[:2]]
                expected=[route(i)[2] for i in range(lo,hi+1)]
                assert s['modules']==mods
                check_object_set(s['objects'],mods)
                assert ns=={'manifest.json','terminal-axioms.log'}|{f'row{i:03d}-build.log' for i in range(lo,hi+1)}|{'objects/'+x for x in s['objects']}
                assert s['axioms']==axiom_log(z.read('terminal-axioms.log').decode(),expected)
                assert not set(terminal)&set(s['axioms'])
                assert not set(objects)&set(s['objects'])
                check_hashes(z,s['objects'],'objects/')
                objects.update(s['objects']);terminal.update(s['axioms']);covered.extend(range(lo,hi+1))
            path.unlink()
        assert covered==list(range(242)) and len(terminal)==242
        assert objects==m['shard_objects']
        check_object_set(objects,[mod for i in covered for mod in route(i)[:2]])
    receipt={'schema':'F41-aggregate-independent-custody-v1','producer_run':run,'producer_head':head,
        'artifact_pins':{n:{k:a[k] for k in ('id','digest','size_in_bytes')} for n,a in sorted(p.items())},
        'rows':covered,'terminal_axioms':terminal,'aggregate_axioms':m['axioms'],
        'source_sha256':sha(source),'source_manifest_sha256':sha(raw),'object_baseline_sha256':sha(base),
        'verified_shard_objects':len(objects),'independent_archive_audit_passed':True,
        'original_global_boolean_producer_custody_passed':True,'new_Lean_compilation_performed_by_audit':False,
        'physical_enclosure_requires_moment_soundness':True,'analytic_bank_hbank_certified':False,
        'full_F41_certified':False,'F42_positive':False,'RH_proved':False}
    out.write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n')
def selftest():
    assert len(names())==18 and len({route(i)[2] for i in range(242)})==242
    assert len({m for i in range(242) for m in route(i)[:2]})==484
    assert [i for lo,hi in ranges() for i in range(lo,hi+1)]==list(range(242))
    line="'WeilDefect.t' depends on axioms: [propext, Classical.choice, Quot.sound]"
    assert set(axiom_log(line,['t']))=={'t'}
    run=1;head='a'*40
    a=[{'name':n,'id':i+1,'workflow_run':{'id':run,'head_sha':head},'expired':False,'size_in_bytes':1,'digest':'sha256:'+'b'*64} for i,n in enumerate(sorted(names()))]
    assert len(pins(a,run,head))==18
    mods=['WeilDefect.Test'];obj={'WeilDefect/Test.olean':'c'*64}
    check_object_set(obj,mods)
    bad=[lambda:axiom_log(line.replace('propext','sorryAx'),['t']),lambda:axiom_log(line,['u']),lambda:axiom_log(line+'\n'+line,['t']),
         lambda:pins(a[:-1],run,head),lambda:pins([dict(a[0],expired=True)]+a[1:],run,head),
         lambda:pins([dict(a[0],workflow_run={'id':2,'head_sha':head})]+a[1:],run,head),
         lambda:check_object_set({},mods),lambda:check_object_set(dict(obj,extra='d'*64),mods)]
    for f in bad:
        try:f()
        except AssertionError:pass
        else:raise AssertionError('negative control accepted')
    print('242 terminal routes, 484 modules, 18 artifact slots; eight independent negative controls rejected. NO Lean.')
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['selftest','audit']);ap.add_argument('--run',type=int);ap.add_argument('--head');ap.add_argument('--output',type=Path)
    a=ap.parse_args()
    if a.mode=='selftest':selftest()
    else:
        assert a.run and a.output and re.fullmatch(r'[0-9a-f]{40}',a.head)
        audit(a.run,a.head,a.output)
