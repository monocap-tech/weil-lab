import hashlib,json,sys,tarfile
from pathlib import Path

def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
    return h.hexdigest()

def main():
    audit=Path(sys.argv[1]);root=Path('WeilDefect/Generated/NF618HybridPilot');manifest=root/'manifest.json'
    a=json.loads(audit.read_text());m=json.loads(manifest.read_text());binding=Path('nf697-bank-binding.json');b=json.loads(binding.read_text());finger=b.pop('fingerprint')
    assert hashlib.sha256(json.dumps(b,sort_keys=True,separators=(',',':')).encode()).hexdigest()==finger
    assert a['manifest_sha256']==sha(manifest) and set(a['theorems'])==set(m['theorems']) and all(set(v)<={'propext','Classical.choice','Quot.sound'} for v in a['theorems'].values())
    assert a['tables']==len(m['tables']) and a['rows']==sum(t['rows'] for t in m['tables'])
    assert all(sha(root/n)==h for n,h in m['files'].items())
    g=Path('WeilDefect/Generated');common=list((g/'NF632').glob('*.lean'))+list((g/'NF703').glob('Real0001*.lean'))+list((g/'NF703').glob('Real0003*.lean'))+[root/'Amplitude.lean',Path('WeilDefect/Arithmetic/ActualZetaOriginalPhysicalSemanticEndpointCache.lean'),Path('WeilDefect/Arithmetic/ActualZetaOriginalPhysicalHybridEndpoint.lean')]
    assert len(common)==144 and all(p.is_file() for p in common)
    batch=[root/n for n in m['files'] if n!='Amplitude.lean'];build=Path('.lake/build');paths=[p for p in build.rglob('*') if p.is_file() and not p.is_symlink() and 'WeilDefect' in p.parts]
    seen=set()
    for label,sources in [('common',common),('batch',batch)]:
        stems={str(p.with_suffix('')) for p in sources}; objects=[]
        for p in paths:
            k='WeilDefect/'+str(p).split('/WeilDefect/',1)[1];stem=k.split('.',1)[0]
            if stem in stems:objects.append(p)
        assert objects and not seen.intersection(objects);seen.update(objects)
        assert all((build/'lib/lean'/p.with_suffix('.olean')).is_file() for p in sources)
        out=Path('nf618-checkpoints')/label;out.mkdir(parents=True,exist_ok=True);tar=out/'compiled.tar.gz'
        with tarfile.open(tar,'w:gz',compresslevel=3) as t:
            for p in sorted(objects):t.add(p,arcname=str(p),recursive=False)
        receipt={'scope':'Compiled cache candidate; requires producer audit, source/environment binding and Lake revalidation before reuse','base_binding_sha256':sha(binding),'base_fingerprint':finger,'manifest_sha256':sha(manifest),'audit_sha256':sha(audit),'sources':{str(p):sha(p) for p in sorted(sources)},'objects':{str(p):sha(p) for p in sorted(objects)},'archive_sha256':sha(tar)}
        (out/'checkpoint.json').write_text(json.dumps(receipt,sort_keys=True,indent=2)+'\n');print(label,len(sources),len(objects),tar.stat().st_size,receipt['archive_sha256'])
if __name__=='__main__':main()
