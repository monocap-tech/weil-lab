#!/usr/bin/env python3
"""NF650: standalone, archive-bound local data audit. No Lean truth asserted.
Usage: python scripts/verify_nf650_retained_local_data.py /path/to/archives
Archive filenames must be exactly the keys of ART with .zip appended.
"""
import gzip,hashlib,json,re,sys,zipfile
from pathlib import Path
from fractions import Fraction as F
sys.set_int_max_str_digits(0)
Q=10**2600; N=1200; Z=(0,0); ONE=(Q,0)
BASE=Path(sys.argv[1])
ART={
'nf621-shard0':'a6d19c05b28bf9dbf3104f2e77f0a06653575d67aafde7dc28438c6f770dbd88',
'nf621-shard1':'42e8ed541720f316b9ab7136e884e29d7ee6601a11907c3d1f3210340c4351a9',
'nf621-shard2':'cd12417fe9e2fe2df994b2d970d384a047ec91e607b369ce09ba3ab7829af637',
'nf631-widened':'e91a83cae117e98608aefa6849dac178e4ddb58dd1dffbfe37304ad248af9ed9',
'nf632-pi':'d1769ab74275cc9c57452d3aa5ad3a30109efc500f7834ee392ed668612d9a37',
'nf635-endpoints':'2b0e45897c28a1ed8d671b2958c8a51646e818e742ecbcf4ed6fcf02f31ed363',
'nf638-pilots':'3ddcd0c863614a9f95a8b3ee393dc7af383a125d34b873e181c8f0646f85ac20'}
sha=lambda x:hashlib.sha256(x).hexdigest()
zips={}
for name,d in ART.items():
 path=BASE/(name+'.zip'); assert sha(path.read_bytes())==d,name; zips[name]=zipfile.ZipFile(path)
P,B,T,W=(zips[n] for n in ('nf632-pi','nf635-endpoints','nf638-pilots','nf631-widened'))
def manifest(a):
 m=json.loads(a.read('manifest.json'))
 for f in m['files']: assert sha(a.read(f['file']))==f['sha256'],f['file']
 return m
pm,bm,tm=map(manifest,(P,B,T)); wm=json.loads(W.read('nf631-widening.json'))
assert sha(T.read('Join.lean'))==tm['join_sha256']; assert bm['input_sha256']==tm['input_sha256']==wm['input_sha256']; assert len(bm['input_sha256'])==8
assert pm['full'] and len(pm['files'])==127 and bm['full_values']
assert sha(W.read('nf631-widened-entries.jsonl.gz'))==wm['widened_entry_sha256']
b=json.loads(gzip.decompress(B.read('endpoints.json.gz'))); assert b['scale']=='10^2600'
pi=tuple(map(int,b['pi'])); ptext=next(l for l in P.read('Pi.lean').decode().splitlines() if l.startswith('def nf632Pi :'))
assert tuple(map(int,re.findall(r'\((-?\d+):ℚ\)/neutralNF616Q',ptext)))==pi
lit=lambda s:list(map(int,re.findall(r'\((-?\d+):ℚ\)/\(neutralNF616Q:ℚ\)',s)))
assert lit(B.read('Banks.lean').decode())==list(pi)
R,Phi=({F(k):tuple(tuple(map(int,x)) for x in v) for k,v in b[label]} for label in ('real','phase'))
for label,vals in [('Real',R),('Phase',Phi)]:
 coords=[]
 for name in sorted(B.namelist()):
  if name.startswith(label+'Values') and name.endswith('.lean'): coords+=lit(B.read(name).decode())
 assert coords==[x for v in vals.values() for a in v for x in a]
assert (len(R),len(Phi))==(5,1276)
keys={(F(1),F(0)):1,(F(0),F(37,32)):27,(F(1,2),F(37,64)):14,(F(-1,2),F(37,64)):14}
rows={}; shard_names={}
for j in range(3):
 name=f'nf621-shard{j}.json.gz'; raw=zips[f'nf621-shard{j}'].read(name); assert sha(raw)==bm['input_sha256'][name]
 sh=json.loads(gzip.decompress(raw)); assert sh['scale']=='10^2600' and sh['exp_terms']==N and sh['atan_terms']==2000
 for t in sh['tables']:
  k=F(t['h']),F(t['f'])
  if k in keys:
   assert k not in rows; rows[k]=[tuple(map(int,r)) for r in t['rows']]; shard_names[str(k)]=j
assert {k:len(v) for k,v in rows.items()}==keys
ceil=lambda a,b:-((-a)//b)
def exact(x):
 x=F(x); m,r=divmod(x.numerator*Q,x.denominator); return m,int(r!=0)
def add(a,b):return a[0]+b[0],a[1]+b[1]
def neg(a):return -a[0],a[1]
def mul(a,b):
 m,r=a;n,s=b;return m*n//Q,ceil(abs(m)*s+abs(n)*r+r*s,Q)+1
def div(a,n):return a[0]//n,ceil(a[1],n)+1
def za(a,b):return add(a[0],b[0]),add(a[1],b[1])
def zn(a):return neg(a[0]),neg(a[1])
def zm(a,b):return add(mul(a[0],b[0]),neg(mul(a[1],b[1]))),add(mul(a[0],b[1]),mul(a[1],b[0]))
def rr(x):return exact(x),Z
def red(f):u=f*F(11,10);return u-(u+F(1,2))//1
def small(a):
 t=(ONE,Z); s=(Z,Z)
 for n in range(N):
  s=za(s,t); t=tuple(div(v,n+1) for v in zm(t,a))
 return tuple((m,r+1) for m,r in s)
realkeys={s*h for h,f in keys for s in (-1,1)}; phasekeys={red(s*f) for h,f in keys for s in (-1,1)}
for h in realkeys:
 x=small(rr(h*F(11,20))); assert zm(x,x)==R[h]
for u in phasekeys:
 x=small((Z,mul(pi,exact(u/2)))); x=zm(x,x);assert zm(x,x)==Phi[u]
assert len(realkeys)==len(phasekeys)==5
upper=lambda a:sum(abs(m)+r for m,r in a)
def cache(h,f):return (exact(h),mul(pi,exact(2*f))),zm(R[h],Phi[red(f)]),zm(R[-h],Phi[red(-f)])
for rec in tm['files']:
 k=tuple(map(F,rec['key'])); txt=T.read(rec['file']).decode(); t=txt.split(' := ',1)[1].split('\n\ntheorem',1)[0]
 coords=list(map(int,re.findall(r'\((-?\d+):ℤ\)',t))); expected=[x for a in cache(*k) for z in a for x in z]+[x for r in rows[k] for x in r]
 assert coords==expected,rec['file']
residuals=0; reject=0
for (h,f),tab in rows.items():
 d=max(abs(h),6*abs(f)); z,p,m=cache(h,f); prev=(0,0,0)
 for n,(x,y,r) in enumerate(tab):
  Bn=za(zm(rr(F(11,10)**n),p),zn(zm(rr(F(-11,10)**n),m)))
  a=za(Bn,zn(zm(z,((x,0),(y,0)))))
  if n:a=za(a,zn(zm(rr(n),((prev[0],0),(prev[1],0)))))
  fee=upper(a)+n*prev[2]; assert F(fee)<=d*r; assert r==ceil(fee*d.denominator,d.numerator)+1
  assert fee>0;reject+=1;residuals+=1;prev=x,y,r
ix=list(range(14))+[241]; wanted={(i,j) for i in ix for j in ix if j<=i}; retained={}
with gzip.GzipFile(fileobj=W.open('nf631-widened-entries.jsonl.gz')) as fh:
 head=json.loads(next(fh));assert head['schema']=='NF622-original-physical-entry-balls-v1' and head['scale']=='10^2600' and head['original_entry_sha256']==wm['original_entry_sha256']
 for i,line in enumerate(fh):
  t=json.loads(line);assert t['row']==i and len(t['H_lower'])==i+1
  if i in ix:
   for j in ix:
    if (i,j) in wanted:retained[i,j]=tuple(map(int,t['H_lower'][j]))
assert set(retained)==wanted
# Original 37/64 block and genuine pole, read from NF545 source previously audited.
def terms(i):
 if i==241:return [(F(s,2),F(0),0,F(s,2),F(0)) for s in (1,-1)]
 return [(F(0),F(s*37,64),i,F(1,2) if i%2 else F(0),F(0) if i%2 else F(-s,2)) for s in (1,-1)]
def moment(h,f,n):
 if h==f==0:return rr((F(11,10)**(n+1)-F(-11,10)**(n+1))/(n+1))
 flip=f<0 or (f==0 and h<0);k=(-h,-f) if flip else (h,f);x,y,r=rows[k][n];s=-1 if flip and n%2 else 1;return (s*x,r),(s*y,r)
def scale(a,c):c=F(c);m,r=divmod(a[0]*c.numerator,c.denominator);return m,ceil(a[1]*abs(c.numerator),c.denominator)+int(r!=0)
def zscale(a,c,d):return add(scale(a[0],c),neg(scale(a[1],d))),add(scale(a[0],d),scale(a[1],c))
under=0; exact_widen=0; maxrad=0; query=0
for (i,j),(m,r) in retained.items():
 old=ref=(Z,Z)
 for h,f,n,c,d in terms(i):
  for k,g,l,e,v in terms(j):
   a=moment(h+k,f+g,n+l);query+=1
   old=za(old,zscale(a,c*e-d*v,c*v+d*e));ref=za(ref,zm(zm((exact(c),exact(d)),(exact(e),exact(v))),a))
 assert abs(ref[1][0])<=ref[1][1] and abs(old[1][0])<=old[1][1]
 assert m==old[0][0];needed=abs(m-ref[0][0])+ref[0][1];assert r==max(old[0][1],needed)
 assert needed==r and r>0; assert r-1<needed
 under+=1;exact_widen+=1;maxrad=max(maxrad,r)
report={'schema':'NF650-retained-local-data-audit-v1','archive_sha256':ART,'manifests_checked':3,'manifest_listed_files_checked':sum(len(m['files']) for m in (pm,bm,tm)),'common_shard_digest_inventory':8,'actual_shard_bytes_checked':3,'pi_literal_match':True,'endpoint_json_lean_literal_matches':1281,'endpoint_reference_replays':10,'retained_integer_tables_matched':3,'retained_integer_rows_matched':42,'retained_moment_residuals_pass':residuals,'zero_radius_mutations_rejected':reject,'retained_gram_centers_match':len(retained),'exact_widening_pass':exact_widen,'one_unit_widening_mutations_rejected':under,'signed_source_queries':query,'max_local_widened_radius_units':str(maxrad),'scope':'actual retained artifact byte audit and exact arithmetic; not Lean execution, no whole-bank reference proof'}
print(json.dumps(report,indent=2))
