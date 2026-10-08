"""One complete sixteen-column ORIGINAL even inverse-action audit.

Sources are constructed afresh. Exact integer Hankel products retain every
mixed action entry. No full retained source Gram or full inverse is asserted.
"""
import sys,json,gzip,hashlib,time
from functools import lru_cache
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import get_context
from pathlib import Path
from certify_native_coupled_trial_cc3 import F,I,D,ROOT,source,shifted_legendre,sqrt_rational,primitives,dot,bracket
from certify_native_exact_hankel import moment_apply,bilinear_bounds
from certify_native_inverse_correlation_cc13 import solve,pivots
from native_rich_action_fast_source_cc14 import fast_source,controls,original_source_function_sha256
from native_rich_action_source_error_cc14 import constant_radius,factored_error
sys.set_int_max_str_digits(0)
I.grid=10**800
_atan=fast_source.__globals__['atan']
@lru_cache(None)
def _cached_atan(x,n,grid):
 assert I.grid==grid
 return _atan(x,n)
fast_source.__globals__['atan']=lambda x,n:_cached_atan(x,n,I.grid)
fast_source.__globals__['bernoulli']=lru_cache(None)(fast_source.__globals__['bernoulli'])
DEGREES=list(range(112,144,2))
def mid(x):return (x.lo+x.hi)/2
def compact(x):
 g=10**100
 return [str(F((x.lo*g).__floor__(),g)),str(F((x.hi*g).__ceil__(),g))]
def ints(p):
 from math import lcm
 den=lcm(*(x.denominator for x in p));return [int(x*den) for x in p],den
def applied(p,m,count):return moment_apply(p,[(int(x.lo*I.grid),int(x.hi*I.grid)) for x in m],count)
def bil(p,am,den):
 lo,hi=bilinear_bounds(p,am);return I(F(lo,2*I.grid*den),F(hi,2*I.grid*den))
def quad(A,t):return sum((t[i]*A[i][j]*t[j] for i in range(len(t)) for j in range(len(t))),I(0))
_BATCH=None
def panel_worker(panel):
 prim,regs,rc,rden,pints,pden,count,plen,slen,degree=_BATCH
 a,b=prim[panel:panel+2]
 mm=[(b[0][k+1]-a[0][k+1])/(k+1) for k in range(degree+1)]
 lm=[b[1][k]-a[1][k] for k in range(degree+1)]
 mm=[I(max(F(0),x.lo),x.hi) for x in mm];lm=[I(max(F(0),x.lo),x.hi) for x in lm]
 apps=[applied(rc[j][panel],mm,slen) for j in range(count)]
 logapps=[applied(rc[j][panel],lm,plen) for j in range(count)]
 moments=[[I(0) for _ in range(plen)] for _ in range(count)]
 gram=[[I(0) for _ in range(count)] for _ in range(count)]
 for i in range(count):
  for k in range(plen):moments[i][k]+=dot(regs[i][panel],mm[k:])
  for j in range(i,count):
   gram[i][j]+=bil(rc[i][panel],apps[j],rden[i][panel]*rden[j][panel])
   gram[i][j]+=bil(pints[i],logapps[j],pden[i]*rden[j][panel])
   gram[i][j]+=bil(pints[j],logapps[i],pden[j]*rden[i][panel])
 return panel,moments,gram
def compute():
 start=time.monotonic();base=ROOT/'notes/data'
 convolution_checks=controls();assert convolution_checks==20
 paths={k:base/v for k,v in {
 'saved':'RPB108_PRIME8_SCHUR112_105_CERTIFICATE_20261008.json',
 'cc9':'RPB108_TWO_RETAINED_BLOCK_CC9_CERTIFICATE_20261008.json',
 'cc11':'RPB108_ODD_BATCH_CC11_CERTIFICATE_20261008.json',
 'nf71':'RPB108_CORRELATED_WEAK_ROW_NF71_CERTIFICATE_20261008.json',
 'cc13':'RPB108_INVERSE_CORRELATION_CC13_CERTIFICATE_20261008.json'}.items()}
 rawin={k:p.read_bytes() for k,p in paths.items()};dat={k:json.loads(b) for k,b in rawin.items()}
 saved,old,nf=dat['saved'],dat['cc9'],dat['nf71'];v=list(map(F,saved['rational_coefficient_witness']))
 raw=gzip.decompress((base/'RPB108_PRIME8_MATRIX112_105_COMPACT80_20261008.json.gz').read_bytes())
 assert hashlib.sha256(raw).hexdigest()==saved['input_sha256']['native'];nat=json.loads(raw)
 Q=[[None]*112 for _ in range(112)];pos=0
 for i in range(112):
  for j in range(i+1):
   Q[i][j]=Q[j][i]=I(*(F(int(x),10**80) for x in nat['lower_triangle_row_major'][pos]));pos+=1
 P=shifted_legendre(DEGREES[-1]);norms=[sqrt_rational(F(2*j+1)/D) for j in range(DEGREES[-1]+1)]
 weights=[v[j]*mid(norms[j]) if j%2==0 else F(0) for j in range(112)]
 ph=[sum((weights[j]*(P[j][k] if k<=j else 0) for j in range(112)),F(0)) for k in range(111)]
 nu=mid(norms[0]);nz=[mid(norms[n]) for n in DEGREES]
 polys=[ph,[nu]]+[[nz[i]*x for x in P[n]] for i,n in enumerate(DEGREES)]
 M0=[sum(map(abs,weights),F(0)),abs(nu)]+list(map(abs,nz))
 M1=[sum((abs(weights[j])*j*(j+1) for j in range(112)),F(0)),F(0)]+[abs(nz[i])*n*(n+1) for i,n in enumerate(DEGREES)]
 regs=[];errs=[]
 for i,p in enumerate(polys):
  print('CC14 original source',i,'of',len(polys),file=sys.stderr,flush=True)
  bind=hashlib.sha256(json.dumps([original_source_function_sha256,hashlib.sha256((ROOT/'scripts/native_rich_action_fast_source_cc14.py').read_bytes()).hexdigest(),list(map(str,p)),str(M0[i]),str(M1[i]),str(I.grid)]).encode()).hexdigest()
  cache=base/f'RPB108_RICH_ACTION_CC14_SOURCE_CACHE_{i}.json.gz'
  if cache.exists():
   cached=json.loads(gzip.decompress(cache.read_bytes()));assert cached['binding']==bind
   r=[[F(x) for x in row] for row in cached['regular_polynomials']];e=F(cached['source_error']);pi=I(*map(F,cached['pi']))
   geom={'cuts':[I(*map(F,x)) for x in cached['cuts']],'active':cached['active']}
  else:
   r,e,pi,geom=fast_source(p,M0[i],M1[i])
   cache.write_bytes(gzip.compress(json.dumps({'binding':bind,'regular_polynomials':[[str(x) for x in row] for row in r],'source_error':str(e),'pi':bracket(pi),'cuts':[bracket(x) for x in geom['cuts']],'active':geom['active']}).encode(),mtime=0))
  regs.append(r);errs.append(e)
 original_errors=list(errs);scalar_radius=constant_radius(pi)
 errs=[factored_error(p,M0[i],M1[i],regs[i],scalar_radius) for i,p in enumerate(polys)]
 errs[0]+=2*F(10**7)*sum((abs(v[j])*sqrt_rational(D/F(2*j+1)).hi/(2*I.grid) for j in range(0,112,2)),F(0))
 assert max(errs)<F(1,10**43) and len(geom['cuts'])==14
 count=len(polys);plen=max(map(len,polys));slen=max(len(row) for rows in regs for row in rows);degree=2*slen-2
 print('CC14 exact primitives',degree,file=sys.stderr,flush=True)
 prim=[primitives(t,degree) for t in geom['cuts']]
 pints,pden=zip(*(ints(p) for p in polys))
 rc=[];rden=[]
 for rows in regs:
  a,b=zip(*(ints(row) for row in rows));rc.append(a);rden.append(b)
 moments=[[I(0) for _ in range(plen)] for _ in polys]
 gram=[[I(0) for _ in polys] for _ in polys]
 h1=[];h2=[];harm=F(0);harm2=F(0)
 for k in range(2*plen-1):
  n=k+1;harm+=F(1,n);harm2+=F(1,n*n)
  h1.append(I((F(1,n*n)+harm/n)/2))
  h2.append(I((F(2,n**3)+(harm*harm+harm2)/n+2*harm/n**2+2*harm2/n)/4)-pi*pi/(12*n))
 h2=[I(max(F(0),x.lo),x.hi) for x in h2]
 for j in range(count):
  am=applied(pints[j],h2,plen)
  for i in range(j+1):gram[i][j]+=bil(pints[i],am,pden[i]*pden[j])
 global _BATCH
 _BATCH=(prim,regs,rc,rden,pints,pden,count,plen,slen,degree)
 with ProcessPoolExecutor(max_workers=4,mp_context=get_context('fork')) as pool:
  for panel,pm,pg in pool.map(panel_worker,range(13)):
   print('CC14 complete mixed panel',panel,'elapsed',round(time.monotonic()-start),file=sys.stderr,flush=True)
   for i in range(count):
    for k in range(plen):moments[i][k]+=pm[i][k]
    for j in range(i,count):gram[i][j]+=pg[i][j]
   checkpoint={'completed_panels':panel+1,'source_count':count,'degrees':DEGREES,'elapsed_seconds':time.monotonic()-start}
   (base/'RPB108_RICH_ACTION_CC14_PROGRESS.json').write_text(json.dumps(checkpoint)+'\n')
 for i in range(count):
  for k in range(plen):moments[i][k]+=dot(polys[i],h1[k:])
 coarse=[F(10**8)*(1+x) for x in M0]
 for i in range(count):
  for j in range(i,count):
   e=errs[i]*coarse[j]+errs[j]*coarse[i]+errs[i]*errs[j]
   gram[i][j]=gram[j][i]=D*gram[i][j]+I(-e,e)
 rows=[];audits=0;ucoeff=nu*sqrt_rational(D)
 for i in range(count):
  row=[]
  for k in range(112):
   x=I(0) if k%2 else D*norms[k]*dot(P[k],moments[i])+I(-errs[i],errs[i]);row.append(x)
   if i<2 and k%2==0:
    y=sum((v[j]*Q[k][j] for j in range(0,112,2)),I(0)) if i==0 else ucoeff*Q[k][0]
    assert max(x.lo,y.lo)<=min(x.hi,y.hi),('retained-native',i,k);audits+=1
  rows.append(row)
 for i in range(count):
  for j in range(i,count):gram[i][j]=gram[j][i]=gram[i][j]-sum((rows[i][k]*rows[j][k] for k in range(112)),I(0))
 # Complete compatibility with CC9's ORIGINAL mixed action data.
 overlaps=0
 for i in range(4):
  for j in range(i,4):
   prior=old['actual_retained_source_gram'][i][j] if j<2 else (old['mixed_trial_action'][j-2][i] if i<2 else old['trial_action_gram'][i-2][j-2])
   y=I(*map(F,prior));x=gram[i][j]
   if i==j==0:y-=I(0,64*F(old['odd_original_witness_mass']))
   assert max(x.lo,y.lo)<=min(x.hi,y.hi),('CC9-action-overlap',i,j);overlaps+=1
 QZ=[[I(0) for _ in DEGREES] for _ in DEGREES]
 for i,n in enumerate(DEGREES):
  mass=D*nz[i]*nz[i]/(2*n+1)
  for j in range(len(DEGREES)):
   QZ[i][j]=D*nz[i]*dot(P[n],moments[j+2])+I(-errs[j+2]*sqrt_rational(mass).hi,errs[j+2]*sqrt_rational(mass).hi)
 for i in range(len(DEGREES)):
  for j in range(i+1,len(DEGREES)):
   a,b=QZ[i][j],QZ[j][i];assert max(a.lo,b.lo)<=min(a.hi,b.hi)
   QZ[i][j]=QZ[j][i]=I(min(a.lo,b.lo),max(a.hi,b.hi))
 plane=[[F(x) for x in row] for row in nf['even_plane_deterministic_lower']];rho=plane[0][1]/plane[1][1];ell=F(nf['even_weak_margin'])
 weak=quad([row[:2] for row in gram[:2]],[F(1),-rho])
 GZ=[row[2:] for row in gram[2:]];V=[gram[i+2][0]-rho*gram[i+2][1] for i in range(len(DEGREES))]
 # Deterministic Loewner lower of the WHOLE action Gram; radius is paid once.
 center=[[mid(x) for x in row] for row in GZ]
 radius=max(sum(((x.hi-x.lo)/2 for x in row),F(0)) for row in GZ)
 actionlower=[[center[i][j]-(radius if i==j else 0) for j in range(len(DEGREES))] for i in range(len(DEGREES))]
 # Round to100 digits and pay all rounding error in a second row allowance.
 g=10**100;rounded=[[F((x*g).__floor__(),g) for x in row] for row in actionlower]
 rounding=max(sum((abs(rounded[i][j]-actionlower[i][j]) for j in range(len(DEGREES))),F(0)) for i in range(len(DEGREES)))
 actionlower=[[rounded[i][j]-(rounding if i==j else 0) for j in range(len(DEGREES))] for i in range(len(DEGREES))]
 lp=pivots(actionlower)
 vc=[mid(x) for x in V];vr=[(x.hi-x.lo)/2 for x in V]
 invcols=[solve(actionlower,[F(j==i) for j in range(len(DEGREES))]) for i in range(len(DEGREES))]
 nominal=sum((vc[i]*invcols[j][i]*vc[j] for i in range(len(DEGREES)) for j in range(len(DEGREES))),F(0))
 allowance=sum((abs(invcols[j][i])*(abs(vc[i])*vr[j]+vr[i]*abs(vc[j])+vr[i]*vr[j]) for i in range(len(DEGREES)) for j in range(len(DEGREES))),F(0))
 residualfloor=weak.lo-nominal-allowance
 t0=solve(center,vc);t=[F((x*g).__floor__(),g) for x in t0]
 residual=weak-2*sum((t[i]*V[i] for i in range(len(DEGREES))),I(0))+quad(GZ,t)
 assert residual.hi>=residualfloor>0
 c=F(699,1000);M=F(saved['surrogate_map_norm_upper'])+F(saved['complete_source_map_allowance'])
 coeff=[I(x) if k%2==0 else I(0) for k,x in enumerate(v)];coeff[0]-=rho*ucoeff
 head=[sum((Q[k][j]*coeff[j] for j in range(112)),I(0))-sum((t[i]*rows[i+2][k] for i in range(len(DEGREES))),I(0)) for k in range(112)]
 # Physical even quotient projection: remove constant and h_even_tail.
 tail=[v[j] if j>=2 and j%2==0 else F(0) for j in range(112)];tm=sum((x*x for x in tail),F(0))
 head[0]=I(0);alpha=sum((head[j]*tail[j] for j in range(112)),I(0))/tm
 head=[head[j]-alpha*tail[j] for j in range(112)]
 hn=sqrt_rational(sum((max(abs(x.lo),abs(x.hi))**2 for x in head),F(0))).hi
 rn=sqrt_rational(residual.hi).hi;bound=hn+M*rn/c;budget=bound*bound/ell
 r=list(map(F,dat['cc13']['even_test_vector_orthogonal_to_all_cc11_five']));rm=sum((x*x for x in r),F(0));qr=quad(Q,r)/rm
 uniformfloor=M*M*residualfloor/(c*c*ell)
 floor_ideal=M*M*residualfloor/(4*c*c*ell)
 assert uniformfloor>qr.hi and floor_ideal>qr.hi
 out={'stage':'CC14 complete sixteen-column original rich action','classification':'C',
 'shared_scalar_constant_radius':str(scalar_radius),'original_independent_coefficient_source_errors':list(map(str,original_errors)),
 'shared_constant_error_paid_against_actual_polynomial_sup_norm':True,'other_source_coefficient_error_strict_upper':'1/10^200',
 'exact_kernel_difference_convolution_controls':convolution_checks,'original_source_function_sha256':original_source_function_sha256,
 'aperture':'21/20','action_degrees':DEGREES,'actual_sources_reconstructed':count,
 'integration_degree':degree,'panels':13,'all_prime_powers':[2,3,4,5,7,8],'both_signed_poles':True,
 'native_retained_overlap_checks':audits,'independent_cc9_mixed_action_overlaps':overlaps,
 'action_native_symmetry_checks':len(DEGREES)*(len(DEGREES)-1)//2,
 'complete_action_gram':[[compact(x) for x in row] for row in GZ],
 'complete_trial_native_gram':[[compact(x) for x in row] for row in QZ],
 'whole_weak_trial_action_cross':list(map(compact,V)),'weak_source_norm_squared':compact(weak),
 'complete_trial_native_rows':[[compact(x) for x in row] for row in rows[2:]],
 'entire_action_loewner_lower':[[str(x) for x in row] for row in actionlower],
 'entire_action_lower_ldl_pivots':list(map(str,lp)),
 'source_and_action_interval_row_payment':str(radius),'rounding_row_payment':str(rounding),
 'maximum_inverse_credit_upper':str(nominal+allowance),'all_sixteen_action_span_residual_squared_lower':str(residualfloor),
 'proposed_lift_coefficients':list(map(str,t)),'entire_proposed_residual_norm_squared':compact(residual),
 'whole_even54_correlated_native_row':list(map(compact,head)),
 'whole_even54_native_head_norm_upper':str(hn),'whole_even54_completed_row_norm_upper':str(bound),
 'whole_even54_weak_reaction_upper':str(budget),'uniform_absolute_estimator_floor':str(uniformfloor),
 'perfect_centered_inverse_interval_estimator_floor':str(floor_ideal),
 'explicit_even_quotient_native_rayleigh_upper':compact(qr),
 'source_errors':list(map(str,errs)),'full_remaining_lower_form_evaluated':False,
 'actual_inverse_correlation_evaluated':False,'full_source112_gram_replayed':False,
 'whole_even_positive':False,'whole_odd_positive':False,'cc12_obstruction_overcome':False,
 'protected_codimension_preserved':107,'certified_aperture_preserved':'1','global_nonstalling':False,'lean_certified':False,
 'input_sha256':{**{k:hashlib.sha256(v).hexdigest() for k,v in rawin.items()},'native':hashlib.sha256(raw).hexdigest()},
 'producer_seconds':time.monotonic()-start,
 'displays':{'residual_squared_floor':float(residualfloor),'residual_norm_upper':float(rn),
 'whole_correlated_native_head_norm':float(hn),'completed_row_norm_upper':float(bound),'weak_reaction_upper':float(budget),
 'absolute_estimator_floor':float(uniformfloor),'ideal_inverse_interval_floor':float(floor_ideal),'quotient_rayleigh_upper':float(qr.hi)}}
 raw_certificate=(json.dumps(out,indent=2)+'\n').encode()
 (base/'RPB108_RICH_ACTION_CC14_CERTIFICATE_20261008.json').write_bytes(raw_certificate)
 (base/'RPB108_RICH_ACTION_CC14_CERTIFICATE_20261008.json.gz').write_bytes(gzip.compress(raw_certificate,mtime=0))
 print(json.dumps(out['displays'],indent=2));return out
if __name__=='__main__':compute()
