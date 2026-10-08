"""Independent odd matrix consumer and complete higher-precision Gram replay.

Source caches can be reconstructed by the fixed precache producer. This
consumer replays their error/binding checks, then integrates ALL72-source
Gram pairs at grid600 through a separately written panel evaluator.
The even closure is explicitly inherited from CC16, not freshly replayed.
"""
import json,gzip,hashlib,time
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import get_context
from fractions import Fraction as F
from certify_native_inverse_correlation_cc13 import I as SI,read as sread,solve
from validate_native_even_block_cc16 import ldl
from validate_native_defect_envelope_cc15 import controls as envelope_controls
from validate_native_inverse_correlation_cc13 import run as inverse_controls
from certify_native_odd_frame_cc18 import I,D,ROOT,BASE,FRAME,RETAINED,ACTIONS,read_inputs
from certify_native_rich_action_cc14 import ints,applied,bil,primitives,original_source_function_sha256
from certify_native_coupled_trial_cc3 import dot
from native_odd_frame_source_cc18 import controls,original,sqrt_rational,mid
_VERIFY=None

def convert_application(rc,den,moments,size):
 a,b=applied(rc,moments,size)
 return [I(F(x-y,2*I.grid*den),F(x+y,2*I.grid*den)) for x,y in zip(a,b)]

def independent_panel(panel):
 primitive,rs,ds,ps,ts,size,high,degree=_VERIFY;n=len(ps);a,b=primitive[panel],primitive[panel+1]
 power=[(b[0][k+1]-a[0][k+1])/F(k+1) for k in range(degree+1)]
 logarithm=[b[1][k]-a[1][k] for k in range(degree+1)]
 power=[I(max(F(0),x.lo),x.hi) for x in power];logarithm=[I(max(F(0),x.lo),x.hi) for x in logarithm]
 rp=[applied(r[panel],power,high) for r in rs];rl=[applied(r[panel],logarithm,size) for r in rs]
 moments=[convert_application(rs[i][panel],ds[i][panel],power,size) for i in range(n)]
 matrix=[[I(0) for _ in range(n)] for _ in range(n)]
 for j in range(n):
  for i in range(j+1):
   # Both different log cross terms are explicit. The pure log-square
   # term is attached once outside the piecewise regular panel loop.
   matrix[i][j]=bil(rs[i][panel],rp[j],ds[i][panel]*ds[j][panel])+bil(ps[i],rl[j],ts[i]*ds[j][panel])+bil(ps[j],rl[i],ts[j]*ds[i][panel])
 return panel,moments,matrix

def replay(sources):
 I.grid=10**600;polys=[list(map(F,s['polynomial'])) for s in sources];regs=[[[F(x) for x in r] for r in s['regular_polynomials']] for s in sources]
 cuts=[I(*map(F,x)) for x in sources[0]['cuts']];pi=I(*map(F,sources[0]['pi']));n=len(polys);size=max(map(len,polys));high=max(len(r) for rows in regs for r in rows);degree=2*high-2
 print('CC18 independent Gram72 grid600 primitive degree',degree,flush=True)
 primitive=[primitives(t,degree) for t in cuts];ps,ts=zip(*(ints(p) for p in polys));rs=[];ds=[]
 for rows in regs:r,d=zip(*(ints(row) for row in rows));rs.append(r);ds.append(d)
 H=F(0);H2=F(0);log=[];square=[]
 for k in range(2*size-1):
  h=k+1;H+=F(1,h);H2+=F(1,h*h);log.append(I((F(1,h*h)+H/h)/2))
  value=I((F(2,h**3)+(H*H+H2)/h+2*H/h**2+2*H2/h)/4)-pi*pi/(12*h);square.append(I(max(F(0),value.lo),value.hi))
 moments=[convert_application(ps[i],ts[i],log,size) for i in range(n)];matrix=[[I(0) for _ in range(n)] for _ in range(n)]
 for i in range(n):
  application=applied(ps[i],square,size)
  for j in range(i,n):matrix[i][j]=bil(ps[j],application,ts[i]*ts[j])
 global _VERIFY
 _VERIFY=(primitive,rs,ds,ps,ts,size,high,degree)
 with ProcessPoolExecutor(max_workers=4,mp_context=get_context('fork')) as pool:
  for panel,pm,pg in pool.map(independent_panel,range(13)):
   for i in range(n):
    for k in range(size):moments[i][k]+=pm[i][k]
    for j in range(i,n):matrix[i][j]+=pg[i][j]
   print('CC18 independent ALL72-source Gram panel',panel,flush=True)
 for i in range(n):
  for j in range(i,n):matrix[i][j]=matrix[j][i]=D*matrix[i][j]
 return moments,matrix

def source_inner_rows(a,b):
 # All physical112 projection products, with one outward rounding after
 # the complete integer endpoint sum. This differs from the producer's
 # termwise rational interval sum and retains every mixed product.
 lower=upper=0
 for x,y in zip(a[:112],b[:112]):
  aa,bb=int(x.lo*I.grid),int(x.hi*I.grid);cc,dd=int(y.lo*I.grid),int(y.hi*I.grid)
  values=(aa*cc,aa*dd,bb*cc,bb*dd);lower+=min(values);upper+=max(values)
 return I(F(lower,I.grid**2),F(upper,I.grid**2))

def load_certificate():
 p=BASE/'RPB108_ODD_FRAME_CC18_CERTIFICATE_20261008.json';d=json.loads(p.read_bytes())
 for key,record in d.get('matrix_archives',{}).items():
  rows=[]
  for part in record['parts']:
   raw=(BASE/part['path']).read_bytes();assert hashlib.sha256(raw).hexdigest()==part['gzip_sha256'];decoded=gzip.decompress(raw);assert hashlib.sha256(decoded).hexdigest()==part['decoded_sha256'];more=json.loads(decoded)
   assert part['row_start']==len(rows) and part['row_count']==len(more);rows+=more
  assert len(rows)==record['row_count'] and all(len(row)==record['column_count'] for row in rows);d[key]=rows
 return d

def attachments(K,w,old,weak_native,T,N):
 # Congruence from chart(odd3..111,weak) to physical odd1..111.
 # The weak degree-one coefficient, rather than its tiny degree111
 # coefficient, supplies the invertible chart. All coefficients are exact.
 n=56;v=[-w[j+1]/w[0] for j in range(55)]+[1/w[0]]
 P=[[F(0) for _ in range(n)] for _ in range(n)]
 P[0][0]=sum((v[i]*K[i][j]*v[j] for i in range(n) for j in range(n)),F(0))
 for j in range(55):
  P[0][j+1]=P[j+1][0]=sum((v[i]*K[i][j] for i in range(n)),F(0))
  for k in range(55):P[j+1][k+1]=K[j][k]
 p,L,failed=ldl(P)
 # This consumer separately encloses the actual lower terminal Schur
 # scalar only when its physical e111-perpendicular lower is positive.
 result={'physical_lower_positive_pivots':len(p),'physical_lower_failed_pivot_index':failed}
 a=[[SI(x) for x in row] for row in P]
 for k in range(55):
  pivot=a[k][k]
  if pivot.lo<=0:return result
  for i in range(k+1,56):
   for j in range(i,56):a[i][j]=a[j][i]=a[i][j]-a[i][k]*a[k][j]/pivot
 scalar_lower=a[55][55].lo
 # Native Z16 gives a genuine ORIGINAL compression inverse-reaction
 # lower through the variational principle. It does not use CZ norm/c.
 center=[[(x.lo+x.hi)/2 for x in row] for row in T];b=[(N[i][55].lo+N[i][55].hi)/2 for i in range(16)];t=solve(center,b)
 grid=10**100;t=[F((x*grid).__floor__(),grid) for x in t]
 reaction=2*sum((t[i]*N[i][55] for i in range(16)),SI(0))-sum((t[i]*T[i][j]*t[j] for i in range(16) for j in range(16)),SI(0))
 scale=F(1,10**14);reaction_lower=max(F(0),reaction.lo);sigma_upper=min(F(old['actual_terminal_scalar_enclosure'][1]),(weak_native.hi-reaction_lower)/scale**2)
 reaction_upper=weak_native.hi-scale**2*scalar_lower
 assert scalar_lower<=sigma_upper and reaction_lower<=reaction_upper
 result.update({'actual_terminal_scalar_enclosure':[str(scalar_lower),str(sigma_upper)],'actual_scaled_compression_inverse_reaction_enclosure':[str(reaction_lower),str(reaction_upper)],'genuine_native_Z16_inverse_reaction_lower':str(reaction_lower),'physical_terminal_lower_pivot_interval':[str(a[55][55].lo),str(a[55][55].hi)],'actual_terminal_scalar_positive':scalar_lower>0,'actual_inverse_evaluated':False})
 return result

def run():
 start=time.monotonic();I.grid=10**400;d=load_certificate();data,Q,w,sources,errs,pins,inputpins=read_inputs();checks=0
 assert d['source_cache_sha256']==pins and d['input_sha256']==inputpins;checks+=2
 assert d['source_errors']==list(map(str,errs)) and d['weak_physical_coefficients']==list(map(str,w));checks+=73
 assert w[0]!=0 and d['frame_labels']==FRAME and d['source_controls']==204;checks+=1
 checks+=controls()+envelope_controls();prior=inverse_controls();assert prior['passed'];checks+=prior['exact_checks']
 moments,proxy=replay(sources)
 def ck(value):
  nonlocal checks
  assert value;checks+=1
 def enclosed(x,y):return F(y[0])<=x.lo<=x.hi<=F(y[1])
 for i in range(72):
  for j in range(72):ck(enclosed(proxy[i][j],d['full_source_proxy_gram'][i][j]))
 # Proxy norms are checked at HIGHER integration precision; their original
 # recorded outward bounds pay every pair's full source error again.
 bounds=list(map(F,d['source_proxy_norm_uppers']))
 for i in range(72):ck(bounds[i]>=sqrt_rational(max(F(0),proxy[i][i].hi)).hi)
 Gactual=[[proxy[i][j]+I(-(errs[i]*bounds[j]+errs[j]*bounds[i]+errs[i]*errs[j]),errs[i]*bounds[j]+errs[j]*bounds[i]+errs[i]*errs[j]) for j in range(72)] for i in range(72)]
 P=original.shifted_legendre(143);norms=[sqrt_rational(F(2*k+1)/D) for k in range(144)];rows=[];odd=list(range(1,112,2))
 for i,key in enumerate(FRAME):
  row=[]
  for k in range(144):
   x=I(0) if k%2==0 else D*norms[k]*dot(P[k],moments[i])+I(-errs[i],errs[i])
   if k<112 and key in RETAINED+['weak'] and k%2:
    y=Q[k][key] if key!='weak' else sum((w[j]*Q[k][l] for j,l in enumerate(odd)),I(0))
    ck(max(x.lo,y.lo)<=min(x.hi,y.hi));x=I(max(x.lo,y.lo),min(x.hi,y.hi))
   ck(enclosed(x,d['full_original_native_projection_rows'][i][k]));row.append(x)
  rows.append(row)
 G=[[Gactual[i][j]-source_inner_rows(rows[i],rows[j]) for j in range(72)] for i in range(72)]
 for i in range(72):
  for j in range(72):ck(enclosed(Gactual[i][j],d['full_actual_source_gram_enclosure'][i][j]));ck(enclosed(G[i][j],d['full_actual_F112_residual_gram'][i][j]))
 # Verify every original native chart/trial entry against freshly replayed
 # sources. The following positive envelope uses their published compact
 # enclosures only AFTER these physical pairing checks.
 expectedA=[[I(0) for _ in range(56)] for _ in range(56)]
 for i,k in enumerate(RETAINED):
  for j,l in enumerate(RETAINED):expectedA[i][j]=Q[k][l]
  expectedA[i][55]=expectedA[55][i]=rows[55][k]
 weak=sum((w[j]*rows[55][l] for j,l in enumerate(odd)),I(0));stored=I(*map(F,data['cc17']['native_finite_trial_value']))*F(1,10**28)
 ck(max(weak.lo,stored.lo)<=min(weak.hi,stored.hi));expectedA[55][55]=I(max(weak.lo,stored.lo),min(weak.hi,stored.hi))
 expectedT=[[I(0) for _ in ACTIONS] for _ in ACTIONS];expectedN=[[I(0) for _ in range(56)] for _ in ACTIONS]
 for i,k in enumerate(ACTIONS):
  for j,l in enumerate(ACTIONS):
   a,b=rows[56+i][l],rows[56+j][k];ck(max(a.lo,b.lo)<=min(a.hi,b.hi));expectedT[i][j]=I(max(a.lo,b.lo),min(a.hi,b.hi))
  for j,l in enumerate(RETAINED):expectedN[i][j]=rows[56+i][l]
  a=sum((w[j]*rows[56+i][l] for j,l in enumerate(odd)),I(0));b=rows[55][k];ck(max(a.lo,b.lo)<=min(a.hi,b.hi));expectedN[i][55]=I(max(a.lo,b.lo),min(a.hi,b.hi))
 for name,expected in [('whole_odd_native_chart',expectedA),('whole_trial_native_matrix',expectedT),('whole_trial_retained_native_cross',expectedN)]:
  for i,row in enumerate(expected):
   for j,x in enumerate(row):ck(enclosed(x,d[name][i][j]))
 c=F(699,1000)
 expectedJ=[[G[56+i][56+j]/c-expectedT[i][j] for j in range(16)] for i in range(16)]
 expectedH=[[G[56+i][j]/c-expectedN[i][j] for j in range(56)] for i in range(16)]
 for i in range(16):
  for j in range(16):ck(enclosed(expectedJ[i][j],d['whole_defect_matrix'][i][j]))
  for j in range(56):ck(enclosed(expectedH[i][j],d['whole_defect_source_cross'][i][j]))
 matrix=lambda name:[[I(*map(F,x)) for x in row] for row in d[name]]
 A=matrix('whole_odd_native_chart');T=matrix('whole_trial_native_matrix');N=matrix('whole_trial_retained_native_cross');GP=matrix('full_actual_F112_residual_gram');J=matrix('whole_defect_matrix');H=matrix('whole_defect_source_cross')
 jp,_,jf=ldl([[SI(x.lo,x.hi) for x in row] for row in J]);ck(jf is None and len(jp)==16)
 L=[[F(x) for x in row] for row in d['rational_full_matrix_lift']];JL=[[sum((J[i][k]*L[k][j] for k in range(16)),I(0)) for j in range(56)] for i in range(16)]
 S=[[A[i][j]-GP[i][j]/c+sum((H[k][i]*L[k][j]+L[k][i]*H[k][j]-L[k][i]*JL[k][j] for k in range(16)),I(0)) for j in range(56)] for i in range(56)]
 for i in range(56):
  for j in range(i+1,56):a,b=S[i][j],S[j][i];S[i][j]=S[j][i]=I(min(a.lo,b.lo),max(a.hi,b.hi))
 for i in range(56):
  for j in range(56):ck(enclosed(S[i][j],d['whole_odd_schur_lower'][i][j]))
 # Independently prove that the entire rational K is a lower matrix via
 # weighted Young diagonal bounds. All endpoint100 roundings are paid.
 SS=matrix('whole_odd_schur_lower');weights=list(map(F,d['interval_row_weights']));K=[[F(x) for x in row] for row in d['whole_odd_deterministic_lower']]
 ck(weights==[F(1)]*55+[F(1,10**14)])
 for i in range(56):
  payment=sum(((SS[i][j].hi-SS[i][j].lo)/2*weights[j]/weights[i] for j in range(56)),F(0))
  ck(F(d['weighted_error_diagonal'][i])>=payment+F(56,10**100))
  for j in range(56):
   center=(SS[i][j].lo+SS[i][j].hi)/2;entry=K[i][j]+(F(d['weighted_error_diagonal'][i]) if i==j else 0)
   ck(0<=center-entry<F(1,10**100))
 ps,lower,failed=ldl(K);ck((failed is None)==d['whole_odd_positive'])
 attachment=attachments(K,w,data['cc17'],SI(A[55][55].lo,A[55][55].hi),[[SI(x.lo,x.hi) for x in row] for row in T],[[SI(x.lo,x.hi) for x in row] for row in N])
 out={'passed':True,'exact_checks':checks,'independent_odd_positive_pivots':len(ps),'whole_odd_positive':failed is None,'failed_pivot_index':failed,'complete_source_Gram_pairs_reintegrated':72**2,'independent_integration_grid_digits':600,'all13_panels_replayed':True,'all72_source_error_bindings_replayed':True,'original_source_constructors_freshly_replayed_again':False,'all_original_native_projection_checks':72*144,'complete_action_retained_crosses':896,'cc13_controls_replayed':prior['exact_checks'],'synthetic_controls_are_arithmetic':False,'whole_even_inherited_from_CC16':True,'whole_CC16_even_archive_replayed':False,'actual_inverse_evaluated':False,'nonstalling':False,'lean_certified':False}
 out.update(attachment)
 if failed is None:
  inv=[[SI(0) for _ in range(56)] for _ in range(56)]
  for j in range(56):
   for i in range(j,56):inv[i][j]=SI(int(i==j))-sum((lower[i][k]*inv[k][j] for k in range(j,i)),SI(0))
  trace=sum((max(abs(inv[i][j].lo),abs(inv[i][j].hi))**2/ps[i].lo for i in range(56) for j in range(i+1)),F(0));tb=1
  while tb<trace:tb*=10
  mass=55+sum((x*x for x in w),F(0));mb=mass.__ceil__();tau=F(1,tb*mb)
  # Recover the COMPLETE source norm on the physically orthonormal odd
  # basis, including degree1, from this invertible source chart.
  v=[-w[j+1]/w[0] for j in range(55)]+[1/w[0]]
  first=sum((v[i]*GP[i][j]*v[j] for i in range(56) for j in range(56)),I(0))
  physical_trace=first+sum((GP[i][i] for i in range(55)),I(0));ck(physical_trace.hi>=0)
  factor=(1+2*physical_trace.hi/c**2).__ceil__()+1;mu=min(tau/factor,c/2)
  even=F(1,3*10**63);joined=min(mu,even);kap=joined/(10*(joined+26))
  out.update({'retained_chart_inverse_trace_upper':str(tb),'physical_chart_mass_trace_upper':str(mb),'whole_odd_retained_physical_margin_lower':str(tau),'full_original_odd_source_map_norm_squared_upper':str(physical_trace.hi),'physical_norm_completion_factor':factor,'whole_infinite_odd_physical_margin_lower':str(mu),'inherited_whole_even_physical_margin_lower':str(even),'whole_domain_aperture_105_certified':True,'whole_domain_physical_margin_lower':str(joined),'whole_domain_canonical_margin_lower':str(kap),'remaining_even_retained_dimension':0,'remaining_odd_retained_dimension':0,'original_nonpositive_spectral_dimension_upper':0,'positive_slice_codimension':0})
  ck(attachment.get('actual_terminal_scalar_positive',False))
 else:out.update({'whole_domain_aperture_105_certified':False,'certified_whole_domain_aperture':'1','remaining_even_retained_dimension':0,'remaining_odd_retained_dimension':1,'positive_slice_codimension':1})
 out['exact_checks']=checks;out['validation_seconds']=time.monotonic()-start
 (BASE/'RPB108_ODD_FRAME_CC18_VALIDATION_20261008.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if 'enclosure' not in k},indent=2));return out

if __name__=='__main__':run()
