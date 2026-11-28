import hashlib,json,os,zipfile
from pathlib import Path
H=lambda b:hashlib.sha256(b).hexdigest()
root=Path.cwd();out=Path(os.environ['RUNNER_TEMP'])/'nf618-inputs';out.mkdir()
def need(x,msg):
    if not x:raise ValueError(msg)
def recover(receipt,base,expected):
    need(receipt['status']=='BYTE_PASS' and receipt['sha256']==expected,'receipt digest')
    dest=out/(str(receipt.get('id',receipt.get('artifact_id')))+'.zip')
    h=hashlib.sha256();n=0
    with dest.open('wb') as f:
        for c in receipt['chunks']:
            b=(base/c['file']).read_bytes()
            need(H(b)==c['sha256'] and len(b)==c['bytes'],'chunk identity')
            h.update(b);n+=len(b);f.write(b)
    need(h.hexdigest()==expected and n==receipt['bytes'],'archive identity')
    with zipfile.ZipFile(dest) as z:need(z.testzip() is None,'CRC')
    print('Recovered from repository only',dest.name,n,flush=True)
    return dest
pins={14551493244:'37be910efa7d204c9db35f62bf9d5f818ece77c7026d94d9c84e4ddba0df41a5',14571810925:'77111b4957562eac2d24f47ffea3b7028c530a165516cbba86852f86540408a5',15136694468:'e324a64d4a1a8f6c537e3d8040a335333973a2df63dc5b1f39f3bb49b246811f',14580099864:'fba35eada4a0614260109add6e3762b90447bf047541817c7529348121f33ab3',15084125240:'5ecdd6e9cccf16359cdc1bdcffbe415256b3b03b5a3066009fa0a44fcffc2513',15149930460:'96bd3e816d227a41ce60ee643fae020c05107384e770ff26043db521713b1918',15154802905:'d479b8bb33d30b357ef8880245dc0401a87b0d8d82465419bcf242934942630f'}
for id,digest in pins.items():
    d=root/'direct/archives'/str(id);r=json.loads((d/'receipt.json').read_text());need(r['id']==id,'receipt ID');recover(r,d,digest)
d=root/'historical/custody/run_46076027949-attempt_1';rs=json.loads((d/'recovery.json').read_text())['records']
for id,digest in [(14558233793,'2327fbf952d4894c9f28f81cad9e94d226c93131d9ef2fafa14c35f482211b70'),(15154611293,'6b27144e8b723d476f992a888ea0bb7fef48a302d4b7ad9003fce737734f8532')]:
    r=[x for x in rs if x['artifact_id']==id];need(len(r)==1,'historical receipt ID');recover(r[0],d,digest)
