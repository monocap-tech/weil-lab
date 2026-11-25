"""Rebuild authenticated original row sources in bounded shards; no evidence is accepted on failure."""
import hashlib,json,os,re,shutil,subprocess,sys,tempfile
from pathlib import Path,PurePosixPath
HERE=Path(__file__).resolve().parent
REPLAY=Path('../replay')
LIB=Path('.lake/build/lib/lean')
BASE=Path('f41-object-baseline.json')
ALLOWED={'propext','Classical.choice','Quot.sound'}
FINAL=('f41OriginalAllRows','f41OriginalEntryCheck','f41OriginalEnclosures_of_moment_soundness')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text())
def write(p,x):
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(x,indent=2,sort_keys=True)+'\n')
def rows():return read(HERE/'plan.json')['rows']
def ranges():return [(i,min(i+15,241)) for i in range(0,242,16)]
def modules(lo,hi):
    out=[]
    for i in range(lo,hi+1):
        r=rows()[i]
        rr=f'{i:03d}'
        local=(f'WeilDefect.Generated.NF695.Row{rr}' if i<8 else
               f'WeilDefect.Generated.NF698Physical.Row{rr}' if i<24 else
               f'WeilDefect.Generated.NF701Physical.Row{rr}' if i<48 else
               r['module'].replace('.Attach','.Row'))
        out.extend([local,r['module']])
    assert len(out)==len(set(out))==2*(hi-lo+1)
    return out
def source_manifest():
    x=read(REPLAY/'replay-manifest.json')
    assert x['schema']=='F41-aggregate-replay-sources-v1' and x['row_range']==[0,241]
    assert x['source_only'] and not x['new_Lean_compilation_performed']
    assert len([e for e in x['evidence'] if 'row' in e])==194
    for name,digest in x['files'].items():
        p=PurePosixPath(name)
        assert not p.is_absolute() and '..' not in p.parts and p.parts[:2]==('WeilDefect','Generated')
        assert sha(REPLAY/name)==digest
    assert (REPLAY/'WeilDefect/Generated/F41Aggregate/AllRows.lean').read_bytes()==(HERE/'AllRows.lean.in').read_bytes()
    return x
def install_sources():
    x=source_manifest()
    for name,digest in x['files'].items():
        p=Path(name)
        assert not p.exists(),p
        p.parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(REPLAY/name,p)
        assert sha(p)==digest
def object_files(module):
    p=LIB/Path(module.replace('.','/'))
    assert p.with_suffix('.olean').is_file(),module
    files=[p.with_suffix('.olean')]
    for suffix in ('.olean.private','.olean.server','.ilean','.ir'):
        q=p.with_suffix(suffix)
        if q.is_file():files.append(q)
    return files
def all_objects():
    return {p.relative_to(LIB).as_posix():sha(p) for p in sorted((LIB/'WeilDefect').rglob('*')) if p.is_file() and any(p.name.endswith(s) for s in ('.olean','.olean.private','.olean.server','.ilean','.ir'))}
def baseline():
    for m in ('WeilDefect.Generated.NF691.OriginalLookup','WeilDefect.Generated.NF702Inputs.Data','WeilDefect.Arithmetic.ActualZetaOriginalPhysicalLiteralRowProjection','WeilDefect.Arithmetic.ActualZetaOriginalPhysicalShardedEntryCustody'):
        object_files(m)
    x={'schema':'F41-replay-object-baseline-v1','source_manifest_sha256':sha(REPLAY/'replay-manifest.json'),
       'bank_binding_sha256':sha(Path('nf697-bank-binding.json')),
       'input_binding_sha256':sha(Path('compiled-input/nf707-input-binding.json')),
       'objects':all_objects()}
    # The baseline must not already contain the row proofs to be rebuilt.
    for m in modules(0,241):
        assert (Path(m.replace('.','/')).as_posix()+'.olean') not in x['objects'],m
    write(BASE,x)
def audit_log(log,expected):
    found={}
    for line in log.splitlines():
        m=re.fullmatch(r"'WeilDefect\.(\w+)' depends on axioms: \[([^\]]*)\]",line)
        n=re.fullmatch(r"'WeilDefect\.(\w+)' does not depend on any axioms",line)
        if m or n:
            name=(m or n)[1]
            assert name in expected and name not in found,name
            a=set(s.strip() for s in m[2].split(',') if s.strip()) if m else set()
            assert a<=ALLOWED,(name,a)
            found[name]=sorted(a)
        assert not re.search(r'\b(error:|sorryAx|uses sorry)\b',line),line
    assert set(found)==set(expected),set(expected)^set(found)
    return found
def command(args,log):
    log.parent.mkdir(parents=True,exist_ok=True)
    with log.open('wb') as f:
        p=subprocess.Popen(args,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        for line in iter(p.stdout.readline,b''):
            f.write(line);sys.stdout.buffer.write(line);sys.stdout.buffer.flush()
        assert p.wait()==0,args
def check_baseline(base,actual,expected_extra):
    assert all(actual.get(k)==v for k,v in base.items()),'common compiled dependency mismatch'
    assert set(actual)-set(base)==set(expected_extra),'unexpected compiled module closure'
def compile_shard():
    lo=int(os.environ['FIRST']);hi=int(os.environ['LAST'])
    assert (lo,hi) in ranges()
    b=read(BASE);out=Path('shard-evidence');out.mkdir()
    for r in rows()[lo:hi+1]:
        command(['lake','build',r['module']],out/f'row{r["row"]:03d}-build.log')
    targets=modules(lo,hi)
    objects={p.relative_to(LIB).as_posix():sha(p) for m in targets for p in object_files(m)}
    check_baseline(b['objects'],all_objects(),objects)
    with tempfile.TemporaryDirectory() as t:
        probe=Path(t)/'Audit.lean'
        probe.write_text(''.join('import '+r['module']+'\n' for r in rows()[lo:hi+1])+''.join('#print axioms WeilDefect.'+r['theorem']+'\n' for r in rows()[lo:hi+1]))
        command(['lake','env','lean',str(probe)],out/'terminal-axioms.log')
    axioms=audit_log((out/'terminal-axioms.log').read_text(),[r['theorem'] for r in rows()[lo:hi+1]])
    for name,digest in objects.items():
        p=out/'objects'/name;p.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(LIB/name,p)
        assert sha(p)==digest
    write(out/'manifest.json',{'schema':'F41-replay-shard-objects-v1','row_range':[lo,hi],
        'run_id':os.environ['GITHUB_RUN_ID'],'head':os.environ['GITHUB_SHA'],
        'baseline_sha256':sha(BASE),'source_manifest_sha256':b['source_manifest_sha256'],
        'modules':targets,'objects':objects,'axioms':axioms,'new_Lean_compilation_performed':True,
        'aggregate_certified':False})
def aggregate():
    b=read(BASE);objects={};covered=[]
    for lo,hi in ranges():
        root=Path('../shards')/f'f41-aggregate-objects-{lo}-{hi}'
        m=read(root/'manifest.json')
        assert m['schema']=='F41-replay-shard-objects-v1' and m['row_range']==[lo,hi]
        assert m['run_id']==os.environ['GITHUB_RUN_ID'] and m['head']==os.environ['GITHUB_SHA']
        assert m['baseline_sha256']==sha(BASE) and m['source_manifest_sha256']==b['source_manifest_sha256']
        assert m['modules']==modules(lo,hi) and m['new_Lean_compilation_performed'] and not m['aggregate_certified']
        assert audit_log((root/'terminal-axioms.log').read_text(),[r['theorem'] for r in rows()[lo:hi+1]])==m['axioms']
        allowed={Path(x.replace('.','/')).as_posix()+s for x in m['modules'] for s in ('.olean','.olean.private','.olean.server','.ilean','.ir')}
        assert set(m['objects'])<=allowed
        assert all(Path(x.replace('.','/')).as_posix()+'.olean' in m['objects'] for x in m['modules'])
        assert not set(objects)&set(m['objects'])
        for name,digest in m['objects'].items():
            p=root/'objects'/name
            assert p.is_file() and sha(p)==digest
            dst=LIB/name
            assert not dst.exists(),dst
            dst.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,dst)
            assert sha(dst)==digest
        objects.update(m['objects']);covered.extend(range(lo,hi+1))
    assert covered==list(range(242))
    check_baseline(b['objects'],all_objects(),objects)
    out=Path('aggregate-evidence');out.mkdir()
    source=Path('WeilDefect/Generated/F41Aggregate/AllRows.lean')
    assert sha(source)==source_manifest()['files'][source.as_posix()]
    # Direct Lean invocation, not Lake rebuild of the imported shard modules.
    command(['lake','env','lean',str(source)],out/'aggregate-axioms.log')
    axioms=audit_log((out/'aggregate-axioms.log').read_text(),FINAL)
    shutil.copyfile(source,out/'AllRows.lean')
    shutil.copyfile(REPLAY/'replay-manifest.json',out/'source-replay-manifest.json')
    shutil.copyfile(BASE,out/'object-baseline.json')
    write(out/'manifest.json',{'schema':'F41-aggregate-kernel-producer-v1','rows':covered,
        'source_sha256':sha(source),'source_manifest_sha256':b['source_manifest_sha256'],
        'object_baseline_sha256':sha(BASE),'shard_objects':objects,'axioms':axioms,
        'new_Lean_compilation_performed':True,'original_global_boolean_Lean_passed':True,
        'physical_enclosure_requires_moment_soundness':True,'analytic_bank_hbank_certified':False,
        'full_F41_certified':False,'F42_positive':False,'RH_proved':False})
def selftest():
    assert [i for lo,hi in ranges() for i in range(lo,hi+1)]==list(range(242))
    assert len(set(modules(0,241)))==484
    assert modules(7,8)==['WeilDefect.Generated.NF695.Row007','WeilDefect.Generated.NF702Inputs.Attach007','WeilDefect.Generated.NF698Physical.Row008','WeilDefect.Generated.NF707.Attach008']
    assert modules(47,48)[2:]==['WeilDefect.Generated.F41003.Row048','WeilDefect.Generated.F41003.Attach048']
    line="'WeilDefect.t' depends on axioms: [propext, Classical.choice, Quot.sound]"
    assert set(audit_log(line,['t']))=={'t'}
    tests=[lambda:audit_log(line.replace('propext','sorryAx'),['t']),lambda:audit_log(line,['u']),
           lambda:audit_log(line+'\n'+line,['t']),lambda:check_baseline({'a':'1'},{'a':'2'},[]),
           lambda:check_baseline({'a':'1'},{'a':'1','b':'2'},[])]
    for f in tests:
        try:f()
        except AssertionError:pass
        else:raise AssertionError('negative control accepted')
    print('16 shards, 242 terminal routes, 484 row module routes; five negative controls rejected. NO Lean.')
if __name__=='__main__':
    modes={'install-sources':install_sources,'baseline':baseline,'compile-shard':compile_shard,'aggregate':aggregate,'selftest':selftest}
    modes[sys.argv[1]]()
