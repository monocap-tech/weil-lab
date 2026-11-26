import hashlib,io,json,sys,tarfile,zipfile
from pathlib import Path,PurePosixPath
H=lambda b:hashlib.sha256(b).hexdigest()
p=Path(sys.argv[1])
assert H(p.read_bytes())=='d479b8bb33d30b357ef8880245dc0401a87b0d8d82465419bcf242934942630f'
prefix='nf618-checkpoints/common/'
with zipfile.ZipFile(p) as z:
    assert set(z.namelist())=={prefix+'compiled.tar.gz',prefix+'checkpoint.json','nf697-bank-binding.json','nf618-native-batch02-audit.json','WeilDefect/Generated/NF618HybridPilot/manifest.json'}
    assert z.testzip() is None
    raw=z.read(prefix+'checkpoint.json')
    assert H(raw)=='d7cb931b8335bda537274f21aaf679afe8e136a2966d530766be05f219bad179'
    r=json.loads(raw);binding=z.read('nf697-bank-binding.json')
    assert H(binding)==r['base_binding_sha256'] and binding==Path('nf697-bank-binding.json').read_bytes()
    b=json.loads(binding);fp=b.pop('fingerprint')
    assert fp==r['base_fingerprint']==H(json.dumps(b,sort_keys=True,separators=(',',':')).encode())
    a=z.read('nf618-native-batch02-audit.json');m=z.read('WeilDefect/Generated/NF618HybridPilot/manifest.json')
    assert H(a)==r['audit_sha256'] and H(m)==r['manifest_sha256']
    a=json.loads(a);m=json.loads(m)
    assert a['manifest_sha256']==r['manifest_sha256'] and (a['tables'],a['rows'])==(117,590)
    assert len(a['theorems'])==620 and set(a['theorems'])==set(m['theorems'])
    assert all(set(v)<={'propext','Classical.choice','Quot.sound'} for v in a['theorems'].values())
    g=Path('WeilDefect/Generated');common=list((g/'NF632').glob('*.lean'))+list((g/'NF703').glob('Real0001*.lean'))+list((g/'NF703').glob('Real0003*.lean'))+[g/'NF618HybridPilot/Amplitude.lean',Path('WeilDefect/Arithmetic/ActualZetaOriginalPhysicalSemanticEndpointCache.lean'),Path('WeilDefect/Arithmetic/ActualZetaOriginalPhysicalHybridEndpoint.lean')]
    assert len(common)==144 and set(map(str,common))==set(r['sources'])
    assert all(H(q.read_bytes())==r['sources'][str(q)] for q in common)
    data=z.read(prefix+'compiled.tar.gz');assert H(data)==r['archive_sha256']
stems={str(q.with_suffix('')) for q in common};seen=set()
with tarfile.open(fileobj=io.BytesIO(data),mode='r:gz') as t:
    for x in t:
        q=PurePosixPath(x.name)
        assert x.isfile() and not q.is_absolute() and '..' not in q.parts and x.name.startswith('.lake/build/') and '/WeilDefect/' in x.name and x.name not in seen
        assert ('WeilDefect/'+x.name.split('/WeilDefect/',1)[1]).split('.',1)[0] in stems
        assert H(t.extractfile(x).read())==r['objects'][x.name]
        seen.add(x.name)
    assert len(seen)==1152 and seen==set(r['objects'])
with tarfile.open(fileobj=io.BytesIO(data),mode='r:gz') as t:
    for x in t:
        q=Path(x.name);q.parent.mkdir(parents=True,exist_ok=True)
        assert not q.is_symlink() and all(not v.is_symlink() for v in q.parents)
        q.write_bytes(t.extractfile(x).read())
assert all((Path('.lake/build/lib/lean')/q.with_suffix('.olean')).is_file() for q in common)
print('NF618 common compiled checkpoint source/environment/object binding PASS',len(common),len(seen),fp)
