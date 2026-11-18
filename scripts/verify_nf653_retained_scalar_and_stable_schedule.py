#!/usr/bin/env python3
"""Audit retained scalar proposals and the whole stable-tail schedule; no Lean execution."""
import hashlib,json,zipfile,gzip,re,sys
from pathlib import Path
from fractions import Fraction as F
sys.set_int_max_str_digits(0)
base=Path(sys.argv[1]); out=Path(sys.argv[2]);out.mkdir(parents=True,exist_ok=True)
sha=lambda b:hashlib.sha256(b).hexdigest()
expected={'nf643-stable-survey':'844e7ccd2a09e60b032fee8c7f4c32f4f18d2d10e9b5f119f8c8212c4ed16ab7','nf639-scalar-proposals':'7c4e6f03364ed0290a54683c5b52688a0478a32ae00625b3e5f6f4231ad54582','nf645-attachments':'af571ab52e962b720c92c5539abbfd4735dd2f70ecb9725f1f53e8386bb9f661','nf631-payments':'8cbae72a7714dc555c0183edfbbda077096ef910b1e284d4abc91c4960d95e6e','nf635-endpoints':'2b0e45897c28a1ed8d671b2958c8a51646e818e742ecbcf4ed6fcf02f31ed363','nf632-pi':'d1769ab74275cc9c57452d3aa5ad3a30109efc500f7834ee392ed668612d9a37'}
zs={}
for n,d in expected.items():
 p=base/(n+'.zip'); assert sha(p.read_bytes())==d;zs[n]=zipfile.ZipFile(p)
a,b,c,d,e,f=[zs[n] for n in expected]
plans=json.loads(a.read('plan.json'));sm=json.loads(b.read('manifest.json'));am=json.loads(c.read('manifest.json'));bm=json.loads(e.read('manifest.json'));pm=json.loads(f.read('manifest.json'))
for z,m in [(a,plans),(b,sm),(c,am),(e,bm),(f,pm)]:
 for rec in m['files']:assert sha(z.read(rec['file']))==rec['sha256']
assert plans['bank_manifest_sha256']==am['bank_manifest_sha256']==sha(e.read('manifest.json'))
assert plans['endpoint_bytes_sha256']==sha(e.read('endpoints.json.gz')) and am['pi_manifest_sha256']==sha(f.read('manifest.json'))
end=json.loads(gzip.decompress(e.read('endpoints.json.gz')));Q=10**2600;pi=tuple(map(int,end['pi']))
ceil=lambda a,b:-((-a)//b)
def ex(q):
 q=F(q);m,r=divmod(q.numerator*Q,q.denominator);return m,int(r!=0)
def mul(a,b):
 m,r=a;n,s=b;return m*n//Q,ceil(abs(m)*s+abs(n)*r+r*s,Q)+1
def add(a,b):return a[0]+b[0],a[1]+b[1]
def neg(a):return -a[0],a[1]
def zm(a,b):return add(mul(a[0],b[0]),neg(mul(a[1],b[1]))),add(mul(a[0],b[1]),mul(a[1],b[0]))
slots=plans['slots'];assert len(slots)==1281 and plans['audited_slots']==1281
counts={};fixed=((0,2),(0,2));saved=segments=0
for label in ['Real','Phase']:
 rows=[s for s in slots if s['bank']==label]
 assert len(rows)==len(end[label.lower()]); cuts=[]
 for i,(s,(k,_)) in enumerate(zip(rows,end[label.lower()])):
  q=F(k);assert (s['index'],F(s['parameter']))==(i,q)
  arg=(ex(q*F(11,20)),(0,0)) if label=='Real' else ((0,0),mul(pi,ex(q/2)))
  prod=zm(fixed,arg);r=max(x[1] for x in prod)
  assert r==s['fixed_product_max_radius'] and all(m==0 and 0<t<=s['cutoff']+1 for m,t in prod)
  assert s['skipped_terms']==1200-s['cutoff'] and s['prefix_segments']==ceil(s['cutoff'],32)
  assert 0<=s['cutoff']<1200 and s['segments']==38
  saved+=s['skipped_terms'];segments+=s['prefix_segments'];cuts.append(s['cutoff'])
 counts[label]={'slots':len(rows),'min_cutoff':min(cuts),'max_cutoff':max(cuts)}
assert saved==plans['skipped_terms_audited']==427914 and segments==plans['prefix_segments_audited']==35277
raw=d.read('nf631-widened-payments.json');pay=json.loads(raw);rat=lambda a:F(int(a[0]),int(a[1]))
assert sha(raw)==sm['payment_sha256'] and pay['entry_sha256']==sm['entry_sha256'] and pay['all_pass']
p=b.read('Params.lean').decode();ns={k:int(v) for k,v in re.findall(r'def nf639([SQTU]) : ℕ := (\d+)',p)};S,q,T,U=[ns[k] for k in 'SQTU'];assert q==Q and min(S,T,U)>0
vals={k:F(int(n),int(d)) for k,n,d in re.findall(r'def nf639(EH|EV|R) : ℚ := \((-?\d+):ℚ\)/(\d+)',p)};eh,ev,r=[vals[k] for k in ('EH','EV','R')];assert (eh,ev,r)==tuple(rat(pay[k]) for k in ('uniform_H_radius','uniform_V_radius','r'))
assert all(v>=0 for v in (eh,ev,r));cols=[];mass=[];shared=set();maxrow=F(0)
for i,pr in enumerate(pay['rows']):
 text=b.read(f'Row{i:03}.lean').decode();vs=list(map(int,re.findall(r'\((-?\d+):ℤ\)',text)));assert len(vs)==9 and pr['i']==i and pr['pass']
 de,co,to,wm,ym,ma,bb,ay,dy=vs;assert min(de,co,to,wm,ym,ma)>=0
 row=F(de,Q*S*S)+F(co*to,S*S)*eh
 res=abs(F(bb,Q*S*T)-F(ay,Q*S*S*U))+F(co*wm,S*T)*ev+F(co*ym,S*S*U)*eh
 assert row==rat(pr['defect_upper'])<=F(1,100) and res==rat(pr['residual_upper'])<=r
 selected=rat(pr['selected_payment']);rad=rat(pr['selected_radius']);assert F(ma,S)*2*r<=selected<=rad
 # Selected displacement is not independently recomputed: frozen midpoint is external to these archives.
 maxrow=max(maxrow,row)
 cols.append(co);mass.append(ma);shared.add((to,wm,ym))
 assert f'nf639R {i}=true' in text
assert len(cols)==242 and len(shared)==1 and sum(cols)==sum(mass)==next(iter(shared))[0]
assert maxrow==rat(pay['row_defect_max'])
# Derive a literal-only input set: modify JUST Params import, retain all 242 rows byte-identical.
old=b'import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalScalarPaymentReceipts\n';new=b'import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalScalarPaymentCore\n';assert b.read('Params.lean').count(old)==1
files=[]
for rec in sm['files']:
 name=rec['file'];raw=b.read(name);data=raw.replace(old,new) if name=='Params.lean' else raw
 (out/name).write_bytes(data);files.append({'file':name,'sha256':sha(data),'original_sha256':rec['sha256']})
report={'schema':'NF653-literal-gate-isolation-v1','archive_sha256':expected,'manifest_file_checks':sum(len(m['files']) for m in (plans,sm,am,bm,pm)),'stable_schedule_slots':len(slots),'stable_product_bounds_checked':len(slots),'tail_steps_saved':saved,'prefix_segments':segments,'cutoffs':counts,'scalar_row_payments_recomputed':242,'scalar_residual_payments_recomputed':242,'selected_payment_allowances_checked':242,'common_mass_totals_match':True,'selected_displacement_scope':'not independently recomputed, original NF639 emitter did so using frozen midpoints','derived_files':files,'scope':'actual retained data/exact arithmetic; no Lean compilation and no full endpoint prefix replay'}
(out/'manifest.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items() if k not in ('derived_files','archive_sha256')},indent=2))
