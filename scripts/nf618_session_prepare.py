import hashlib,json,shutil,subprocess,sys,tempfile
from pathlib import Path
H=lambda b:hashlib.sha256(b).hexdigest()
REL=Path('WeilDefect/Generated/NF618HybridPilot')
def merge(src,dest,record):
    raw=(src/'manifest.json').read_bytes();m=json.loads(raw)
    files=m['files'];assert set(p.name for p in src.glob('*.lean'))==set(files)
    assert all(H((src/n).read_bytes())==h for n,h in files.items())
    # Validate the entire batch before writing anything.
    shared=[]
    for n,h in files.items():
        assert Path(n).name==n and n.endswith('.lean')
        q=dest/n
        if q.exists():
            assert n=='Amplitude.lean' and H(q.read_bytes())==h,n
            shared.append(n)
    assert not record.exists(),record
    dest.mkdir(parents=True,exist_ok=True);record.mkdir(parents=True)
    for n in files:
        q=dest/n
        if not q.exists():shutil.copyfile(src/n,q)
    shutil.copytree(src,record/'source')
    return {'modules':len(files),'shared':shared,'manifest_sha256':H(raw)}
def prepare(plan):
    project=Path.cwd();plan=plan.resolve();p=json.loads(plan.read_bytes());n=f"{p['batch']:02d}"
    scripts=project/'scripts';dest=project/REL;record=project/'nf618-session'/f'Batch{n}'
    with tempfile.TemporaryDirectory(prefix='nf618-session-') as temp:
        tmp=Path(temp);g=tmp/'WeilDefect/Generated';g.mkdir(parents=True)
        (g/'NF690').symlink_to(project/'WeilDefect/Generated/NF690',target_is_directory=True)
        for script,args in [('nf618_native_multi.py',[str(plan)]),('nf618_repair_bool_branch.py',[str(REL),str(p['repair_count']),p['normalized_fingerprint']]),('nf618_repair_reflexivity.py',[str(REL),str(p['reflexivity_count']),p['reflexive_fingerprint']])]:
            subprocess.run([sys.executable,str(scripts/script),*args],cwd=tmp,check=True)
        m=json.loads((tmp/REL/'manifest.json').read_bytes());assert m['source_fingerprint']==p['reflexive_fingerprint']
        print('NF618 session prepare',n,merge(tmp/REL,dest,record),flush=True)
if __name__=='__main__':
    for arg in sys.argv[1:]:prepare(Path(arg))
