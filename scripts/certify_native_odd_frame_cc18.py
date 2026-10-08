"""Entire original odd56 matrix envelope, fixed odd Z16, fresh frame72.

The chart uses odd3..111 and CC17's precise weak source; the degree-one
weak coefficient is nonzero. Every raw/source/action mixed product and
every source error is retained. The original even closure is inherited.
"""
import json,gzip,hashlib,time,sys
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import get_context
from native_odd_frame_source_cc18 import I,F,D,frame_error,controls,original,mid,sqrt_rational
from precache_native_odd_frame_cc18 import binding
from certify_native_rich_action_cc14 import ints,applied,bil,compact,dot,primitives,quad
from certify_native_even_block_cc16 import interval_ldl
from certify_native_inverse_correlation_cc13 import solve
from native_rich_action_source_error_cc14 import constant_radius
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT/'notes/data';I.grid=10**400
RETAINED=list(range(3,112,2));ACTIONS=list(range(113,144,2));FRAME=RETAINED+['weak']+ACTIONS
_JOB=None
_RADII={}
def scalar_radius(pi):
 key=(pi.lo,pi.hi,I.grid)
 if key not in _RADII:_RADII[key]=constant_radius(pi)
 return _RADII[key]

def value_apply(coeff,den,mom,count):
 c,r=applied(coeff,mom,count)
 return [I(F(a-b,2*I.grid*den),F(a+b,2*I.grid*den)) for a,b in zip(c,r)]

def panel_worker(panel):
 prim,rc,rd,pc,pd,plen,slen,degree=_JOB;n=len(pc);a,b=prim[panel:panel+2]
 mm=[(b[0][k+1]-a[0][k+1])/(k+1) for k in range(degree+1)];lm=[b[1][k]-a[1][k] for k in range(degree+1)]
 mm=[I(max(F(0),x.lo),x.hi) for x in mm];lm=[I(max(F(0),x.lo),x.hi) for x in lm]
 regular=[applied(rc[j][panel],mm,slen) for j in range(n)];logs=[applied(rc[j][panel],lm,plen) for j in range(n)]
 moments=[value_apply(rc[j][panel],rd[j][panel],mm,plen) for j in range(n)]
 gram=[[I(0) for _ in range(n)] for _ in range(n)]
 for i in range(n):
  for j in range(i,n):
   gram[i][j]=bil(rc[i][panel],regular[j],rd[i][panel]*rd[j][panel])+bil(pc[i],logs[j],pd[i]*rd[j][panel])+bil(pc[j],logs[i],pd[j]*rd[i][panel])
 return panel,moments,gram

def read_inputs():
 paths={'native':'RPB108_PRIME8_MATRIX112_105_COMPACT80_20261008.json.gz','weak':'RPB108_TERMINAL_ODD_CC17_SOURCE_20261008.json.gz','cc17':'RPB108_TERMINAL_ODD_CC17_CERTIFICATE_20261008.json','cc16':'RPB108_JOINED_CC16_SUMMARY_20261008.json','cc16_validation':'RPB108_EVEN_BLOCK_CC16_VALIDATION_20261008.json'}
 raw={k:(BASE/v).read_bytes() for k,v in paths.items()};data={k:json.loads(gzip.decompress(b) if paths[k].endswith('.gz') else b) for k,b in raw.items()}
 assert hashlib.sha256(raw['weak']).hexdigest()==data['cc17']['source_archive_sha256'] and hashlib.sha256(raw['native']).hexdigest()==data['cc17']['input_sha256'][paths['native']]
 Q=[[None]*112 for _ in range(112)];pos=0
 for i in range(112):
  for j in range(i+1):Q[i][j]=Q[j][i]=I(*(F(int(x),10**80) for x in data['native']['lower_triangle_row_major'][pos]));pos+=1
 w=list(map(F,data['weak']['scaled_physical_coefficients']));assert w[0]!=0
 sources=[];pins={};errs=[]
 for key in FRAME:
  if key=='weak':s=data['weak'];name=paths['weak'];blob=raw['weak'];error=F(s['source_error'])
  else:
   name=f'RPB108_ODD_FRAME_CC18_SOURCE_CACHE_{key}.json.gz';blob=(BASE/name).read_bytes();s=json.loads(gzip.decompress(blob));assert s['binding']==binding(key)
   norm=sqrt_rational(F(2*key+1)/D);p=[mid(norm)*x for x in original.shifted_legendre(key)[key]]
   assert list(map(F,s['polynomial']))==p
   regs=[[F(x) for x in row] for row in s['regular_polynomials']];pi=I(*map(F,s['pi']))
   error=frame_error(p,F(s['M0']),F(s['M1']),regs,scalar_radius(pi))+F(10**8)*(1+F(s['M0']))*(norm.hi-norm.lo)/(2*mid(norm))
   assert error==F(s['source_error'])
  sources.append(s);errs.append(error);pins[name]=hashlib.sha256(blob).hexdigest()
 return data,Q,w,sources,errs,pins,{k:hashlib.sha256(b).hexdigest() for k,b in raw.items()}

def integrate(sources):
 start=time.monotonic();polys=[list(map(F,s['polynomial'])) for s in sources];regs=[[[F(x) for x in row] for row in s['regular_polynomials']] for s in sources]
 cuts=[I(*map(F,x)) for x in sources[0]['cuts']];pi=I(*map(F,sources[0]['pi']));n=len(sources);plen=max(map(len,polys));slen=max(len(r) for rows in regs for r in rows);degree=2*slen-2
 assert len(cuts)==14 and all(len(rows)==13 for rows in regs)
 print('CC18 frame72 primitives',degree,'grid digits',len(str(I.grid))-1,flush=True);prim=[primitives(t,degree) for t in cuts]
 pc,pd=zip(*(ints(p) for p in polys));rc=[];rd=[]
 for rows in regs:a,b=zip(*(ints(row) for row in rows));rc.append(a);rd.append(b)
 h1=[];h2=[];h=F(0);h2sum=F(0)
 for k in range(2*plen-1):
  m=k+1;h+=F(1,m);h2sum+=F(1,m*m);h1.append(I((F(1,m*m)+h/m)/2))
  x=I((F(2,m**3)+(h*h+h2sum)/m+2*h/m**2+2*h2sum/m)/4)-pi*pi/(12*m);h2.append(I(max(F(0),x.lo),x.hi))
 moments=[value_apply(pc[i],pd[i],h1,plen) for i in range(n)];gram=[[I(0) for _ in range(n)] for _ in range(n)]
 for j in range(n):
  app=applied(pc[j],h2,plen)
  for i in range(j+1):gram[i][j]+=bil(pc[i],app,pd[i]*pd[j])
 global _JOB
 _JOB=(prim,rc,rd,pc,pd,plen,slen,degree)
 with ProcessPoolExecutor(max_workers=4,mp_context=get_context('fork')) as pool:
  for panel,pm,pg in pool.map(panel_worker,range(13)):
   for i in range(n):
    for k in range(plen):moments[i][k]+=pm[i][k]
    for j in range(i,n):gram[i][j]+=pg[i][j]
   print('CC18 complete frame72 panel',panel,'seconds',round(time.monotonic()-start),flush=True)
 for i in range(n):
  for j in range(i,n):gram[i][j]=gram[j][i]=D*gram[i][j]
 return polys,moments,gram,degree

def assemble(data,Q,w,sources,errs,moments,proxy_gram):
 n=72;P=original.shifted_legendre(143);norms=[sqrt_rational(F(2*k+1)/D) for k in range(144)]
 # Every true source Gram pair has its complete physical source-error
 # allowance. No old delta is silently dropped: this is a NEW full frame.
 proxy_norm=[sqrt_rational(max(F(0),proxy_gram[i][i].hi)).hi for i in range(n)]
 gram=[[proxy_gram[i][j]+I(-(errs[i]*proxy_norm[j]+errs[j]*proxy_norm[i]+errs[i]*errs[j]),errs[i]*proxy_norm[j]+errs[j]*proxy_norm[i]+errs[i]*errs[j]) for j in range(n)] for i in range(n)]
 rows=[];native_overlaps=0;odd=list(range(1,112,2))
 for i,key in enumerate(FRAME):
  row=[]
  for k in range(144):
   x=I(0) if k%2==0 else D*norms[k]*dot(P[k],moments[i])+I(-errs[i],errs[i])
   if k<112 and key in RETAINED+['weak'] and k%2:
    y=Q[k][key] if key!='weak' else sum((w[j]*Q[k][l] for j,l in enumerate(odd)),I(0))
    assert max(x.lo,y.lo)<=min(x.hi,y.hi),('retained original overlap',key,k)
    x=I(max(x.lo,y.lo),min(x.hi,y.hi));native_overlaps+=1
   row.append(x)
  rows.append(row)
 residual=[[gram[i][j]-sum((rows[i][k]*rows[j][k] for k in range(112)),I(0)) for j in range(n)] for i in range(n)]
 # Original physical native56 chart; use the sharper fresh weak source
 # self pairing as a SECOND enclosure of the SAME original native value.
 A=[[I(0) for _ in range(56)] for _ in range(56)]
 for i,k in enumerate(RETAINED):
  for j,l in enumerate(RETAINED):A[i][j]=Q[k][l]
  A[i][55]=A[55][i]=rows[55][k]
 weaknative=sum((w[j]*rows[55][l] for j,l in enumerate(odd)),I(0));stored=I(*map(F,data['cc17']['native_finite_trial_value']))*F(data['cc17']['source_physical_scale'])**2
 assert max(weaknative.lo,stored.lo)<=min(weaknative.hi,stored.hi)
 A[55][55]=I(max(weaknative.lo,stored.lo),min(weaknative.hi,stored.hi))
 T=[[I(0) for _ in ACTIONS] for _ in ACTIONS];N=[[I(0) for _ in range(56)] for _ in ACTIONS]
 for i,k in enumerate(ACTIONS):
  for j,l in enumerate(ACTIONS):
   x,y=rows[56+i][l],rows[56+j][k];assert max(x.lo,y.lo)<=min(x.hi,y.hi)
   T[i][j]=I(max(x.lo,y.lo),min(x.hi,y.hi))
  for j,l in enumerate(RETAINED):N[i][j]=rows[56+i][l]
  x=sum((w[j]*rows[56+i][l] for j,l in enumerate(odd)),I(0));y=rows[55][k]
  assert max(x.lo,y.lo)<=min(x.hi,y.hi);N[i][55]=I(max(x.lo,y.lo),min(x.hi,y.hi))
 c=F(699,1000);G=residual
 J=[[G[56+i][56+j]/c-T[i][j] for j in range(16)] for i in range(16)]
 H=[[G[56+i][j]/c-N[i][j] for j in range(56)] for i in range(16)]
 jp,_,jf,jbad=interval_ldl(J);assert jf is None and len(jp)==16
 center=[[mid(x) for x in row] for row in J];columns=[solve(center,[F(i==j) for i in range(16)]) for j in range(16)];grid=10**100
 L=[[F((sum((columns[k][i]*mid(H[k][j]) for k in range(16)),F(0))*grid).__floor__(),grid) for j in range(56)] for i in range(16)]
 JL=[[sum((J[i][k]*L[k][j] for k in range(16)),I(0)) for j in range(56)] for i in range(16)]
 S=[[A[i][j]-G[i][j]/c+sum((H[k][i]*L[k][j]+L[k][i]*H[k][j]-L[k][i]*JL[k][j] for k in range(16)),I(0)) for j in range(56)] for i in range(56)]
 for i in range(56):
  for j in range(i+1,56):
   x,y=S[i][j],S[j][i];S[i][j]=S[j][i]=I(min(x.lo,y.lo),max(x.hi,y.hi))
 return A,rows,gram,G,T,N,J,H,L,S,native_overlaps

def finish(d):
 # Consumer format pays endpoint100 rounding before its entire LDL test.
 mat=lambda name:[[I(*map(F,x)) for x in row] for row in d[name]]
 A=mat('whole_odd_native_chart');G=mat('full_actual_F112_residual_gram');J=mat('whole_defect_matrix');H=mat('whole_defect_source_cross');c=F(699,1000)
 lift=[[F(x) for x in row] for row in d['rational_full_matrix_lift']]
 JL=[[sum((J[i][k]*lift[k][j] for k in range(16)),I(0)) for j in range(56)] for i in range(16)]
 S=[[A[i][j]-G[i][j]/c+sum((H[k][i]*lift[k][j]+lift[k][i]*H[k][j]-lift[k][i]*JL[k][j] for k in range(16)),I(0)) for j in range(56)] for i in range(56)]
 for i in range(56):
  for j in range(i+1,56):
   a,b=S[i][j],S[j][i];S[i][j]=S[j][i]=I(min(a.lo,b.lo),max(a.hi,b.hi))
 d['whole_odd_schur_lower']=[[compact(x) for x in row] for row in S]
 S=[[I(*map(F,x)) for x in row] for row in d['whole_odd_schur_lower']];grid=10**100
 # Small weak-row errors are paid with a complete weighted diagonal.
 weights=[F(1)]*55+[F(1,10**14)]
 payments=[sum(((S[i][j].hi-S[i][j].lo)/2*weights[j]/weights[i] for j in range(56)),F(0)) for i in range(56)]
 payments=[F((p*grid).__ceil__()+56,grid) for p in payments]
 K=[[F((mid(S[i][j])*grid).__floor__(),grid)-(payments[i] if i==j else 0) for j in range(56)] for i in range(56)]
 ps,L,failed,bad=interval_ldl(K)
 d.update({'interval_row_weights':list(map(str,weights)),'weighted_error_diagonal':list(map(str,payments)),'whole_odd_deterministic_lower':[[str(x) for x in row] for row in K],'whole_odd_ldl_pivots':list(map(compact,ps)),'whole_odd_positive':failed is None,'failed_pivot_index':failed,'failed_pivot_interval':None if bad is None else compact(bad),'actual_terminal_scalar_sign_certified':failed is None,'whole_domain_aperture_105_certified':failed is None,'actual_infinite_inverse_evaluated':False,'nonstalling':False,'lean_certified':False})
 return d

def compute():
 start=time.monotonic();assert controls()==204
 data,Q,w,sources,errs,pins,inputpins=read_inputs()
 checkpoint=BASE/'RPB108_ODD_FRAME_CC18_INTEGRATION_CHECKPOINT_20261008.json.gz'
 if '--resume' in sys.argv:
  saved=json.loads(gzip.decompress(checkpoint.read_bytes()));assert saved['source_cache_sha256']==pins
  polys=[list(map(F,s['polynomial'])) for s in sources];moments=[[I(*map(F,x)) for x in row] for row in saved['moments']];proxy=[[I(*map(F,x)) for x in row] for row in saved['proxy_gram']];degree=saved['integration_degree']
 else:
  polys,moments,proxy,degree=integrate(sources)
  saved={'source_cache_sha256':pins,'integration_degree':degree,'moments':[[[str(x.lo),str(x.hi)] for x in row] for row in moments],'proxy_gram':[[compact(x) for x in row] for row in proxy]};checkpoint.write_bytes(gzip.compress(json.dumps(saved).encode(),mtime=0))
 A,rows,gram,G,T,N,J,H,L,S,overlaps=assemble(data,Q,w,sources,errs,moments,proxy)
 matrices={'whole_odd_native_chart':A,'full_original_native_projection_rows':rows,'full_source_proxy_gram':proxy,'full_actual_source_gram_enclosure':gram,'full_actual_F112_residual_gram':G,'whole_trial_native_matrix':T,'whole_trial_retained_native_cross':N,'whole_defect_matrix':J,'whole_defect_source_cross':H,'whole_odd_schur_lower':S}
 d={'milestone':'CC18','base_commit':'8bf67e1bb474d2b9e836b100d5fbaf2b8e93d892','aperture':'21/20','complement_lower':'699/1000','frame_labels':FRAME,'retained_regular_degrees':RETAINED,'action_degrees':ACTIONS,'weak_physical_coefficients':list(map(str,w)),'source_errors':list(map(str,errs)),'source_proxy_norm_uppers':list(map(str,[sqrt_rational(max(F(0),proxy[i][i].hi)).hi for i in range(72)])),'rational_full_matrix_lift':[[str(x) for x in row] for row in L],'all_original_panels':13,'all_prime_powers':[2,3,4,5,7,8],'both_signed_poles':True,'fresh_original_sources':71,'precise_original_CC17_source_reused':True,'full_source_gram_dimension':72,'complete_mixed_action_retained_crosses':896,'fresh_retained_native_overlaps':overlaps,'integration_degree':degree,'integration_grid_digits':400,'source_cache_sha256':pins,'input_sha256':inputpins,'source_controls':204,'source_operator_errors_in_every_gram_entry':True,'archived_full112_gram_replayed':False,'whole_even_closure_inherited_from_CC16':True}
 d.update({name:[[compact(x) for x in row] for row in M] for name,M in matrices.items()});d=finish(d);d['producer_seconds']=time.monotonic()-start
 raw=(json.dumps(d,indent=2)+'\n').encode();p=BASE/'RPB108_ODD_FRAME_CC18_CERTIFICATE_20261008.json';p.write_bytes(raw);p.with_suffix('.json.gz').write_bytes(gzip.compress(raw,mtime=0))
 from pack_native_odd_frame_cc18 import pack
 pack(d)
 print(json.dumps({'whole_odd_positive':d['whole_odd_positive'],'failed_pivot_index':d['failed_pivot_index'],'failed_pivot_interval':None if d['failed_pivot_interval'] is None else list(map(lambda x:float(F(x)),d['failed_pivot_interval'])),'last_positive_pivot':float(F(d['whole_odd_ldl_pivots'][-1][0])),'seconds':d['producer_seconds']},indent=2));return d

if __name__=='__main__':compute()
