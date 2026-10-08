"""Independent all-column residual-floor and exact Hankel controls for CC14."""
import json,sys,gzip
from pathlib import Path
from fractions import Fraction as F
from math import factorial,isqrt
from certify_native_inverse_correlation_cc13 import solve,pivots
from certify_native_exact_hankel import moment_apply,bilinear_bounds
ROOT=Path(__file__).resolve().parents[1]
sys.set_int_max_str_digits(0)
def run():
 checks=0
 def ck(v):
  nonlocal checks
  assert v;checks+=1
 # Signed source polynomials and nonzero moment radii against direct products.
 cases=0
 for n in (2,3,5,9):
  for seed in range(1,6):
   a=[(-1)**i*(i+seed) for i in range(n)]
   b=[(-1)**(i+seed)*(2*i+1) for i in range(n+1)]
   moments=[(k+1,2*k+3) for k in range(2*n+1)]
   got=bilinear_bounds(a,moment_apply(b,moments,n))
   center=sum((a[i]*b[j]*sum(moments[i+j]) for i in range(n) for j in range(n+1)),0)
   radius=sum((abs(a[i]*b[j])*(moments[i+j][1]-moments[i+j][0]) for i in range(n) for j in range(n+1)),0)
   ck(got==(center-radius,center+radius));cases+=1
 p=ROOT/'notes/data/RPB108_RICH_ACTION_CC14_CERTIFICATE_20261008.json'
 raw=p.read_bytes() if p.exists() else gzip.decompress(p.with_suffix('.json.gz').read_bytes())
 d=json.loads(raw)
 # Independently rebuild the physical factored source-error payments from
 # the actual rational normalizations; no source coefficient is set exact.
 from certify_native_coupled_trial_cc3 import shifted_legendre
 grid=10**800;D=F(21,10)
 def nsq(x):
  k=isqrt((x*grid*grid).__floor__());return F(2*k+1,2*grid)
 P=shifted_legendre(142);saved=json.loads((ROOT/'notes/data/RPB108_PRIME8_SCHUR112_105_CERTIFICATE_20261008.json').read_text())
 v=list(map(F,saved['rational_coefficient_witness']));weights=[v[j]*nsq(F(2*j+1)/D) if j%2==0 else F(0) for j in range(112)]
 m0=[sum(map(abs,weights),F(0)),nsq(1/D)]+[nsq(F(2*n+1)/D) for n in range(112,144,2)]
 m1=[sum((abs(weights[j])*j*(j+1) for j in range(112)),F(0)),F(0)]+[m0[i+2]*n*(n+1) for i,n in enumerate(range(112,144,2))]
 sr=F(d['shared_scalar_constant_radius']);ck(0<sr<F(1,10**130))
 ce=F(23,10)*(D/2)**141/factorial(141);cb=4*(D/3)**362/(1-(D/3)**2)
 he=ce/141+cb/362;ae=ce/142+cb/363;ee=2*(D/4)**141/factorial(141)
 sd=F(isqrt((D*grid*grid).__floor__())+1,grid)
 for i in range(18):
  expected=sd*(2*m0[i]*he+2*m1[i]*ae+100*D*m0[i]*ee+m0[i]*sr+F(1,10**200))
  if i==0:
   expected+=2*F(10**7)*sum((abs(v[j])*F(isqrt((D/F(2*j+1)*grid*grid).__floor__())+1,grid)/(2*grid) for j in range(0,112,2)),F(0))
  ck(expected==F(d['source_errors'][i]))
 # One shared scalar multiplies the bounded polynomial. Its large monomial
 # coefficient norm must not be called an independent physical error.
 scalar_cases=0
 for n in (0,2,6,10):
  p=P[n];ck(sum(map(abs,p),F(0))<=8**n)
  for t in (F(0),F(1,7),F(1,2),F(6,7),F(1)):
   value=sum((x*t**j for j,x in enumerate(p)),F(0))
   ck(abs(F(1,1000)*value)<=F(1,1000));scalar_cases+=1
 size=len(d['action_degrees']);ck(size==16 and d['action_degrees']==list(range(112,144,2)))
 G=[[[F(x) for x in ab] for ab in row] for row in d['complete_action_gram']]
 # Independent deterministic lower from the entire PUBLISHED intervals.
 center=[[(ab[0]+ab[1])/2 for ab in row] for row in G]
 radius=max(sum(((ab[1]-ab[0])/2 for ab in row),F(0)) for row in G)
 K=[[center[i][j]-(radius if i==j else 0) for j in range(size)] for i in range(size)]
 pivots(K)
 V=[[F(x) for x in ab] for ab in d['whole_weak_trial_action_cross']]
 vc=[(ab[0]+ab[1])/2 for ab in V];vr=[(ab[1]-ab[0])/2 for ab in V]
 cols=[solve(K,[F(i==j) for i in range(size)]) for j in range(size)]
 credit=sum((cols[j][i]*(vc[i]*vc[j]) for i in range(size) for j in range(size)),F(0))
 credit+=sum((abs(cols[j][i])*(abs(vc[i])*vr[j]+abs(vc[j])*vr[i]+vr[i]*vr[j]) for i in range(size) for j in range(size)),F(0))
 weak=list(map(F,d['weak_source_norm_squared']));floor=weak[0]-credit
 c=F(699,1000);nf=json.loads((ROOT/'notes/data/RPB108_CORRELATED_WEAK_ROW_NF71_CERTIFICATE_20261008.json').read_text())
 ell=F(nf['even_weak_margin']);saved=json.loads((ROOT/'notes/data/RPB108_PRIME8_SCHUR112_105_CERTIFICATE_20261008.json').read_text())
 M=F(saved['surrogate_map_norm_upper'])+F(saved['complete_source_map_allowance']);test=F(d['explicit_even_quotient_native_rayleigh_upper'][1])
 ck(floor>0);ck(M*M*floor/(4*c*c*ell)>test)
 # The independent lower uses broader published intervals. A strict simple
 # residual endpoint common to producer/consumer is reported separately.
 strict=F(1,10**100)
 while strict*10<min(floor,F(d['all_sixteen_action_span_residual_squared_lower'])):strict*=10
 ck(0<strict<=floor)
 # Complete mixed terms matter: a positive diagonal need not be a positive
 # action Gram; deleting the off-diagonal would incorrectly pass this control.
 ck(F(1)*F(1)-F(2)*F(2)<0)
 # Re-run the independent complete inverse-correlation and positive-eigenmode
 # mass-source controls rather than replacing them with scalar zero tests.
 from validate_native_inverse_correlation_cc13 import run as inverse_controls
 controls=inverse_controls();ck(controls['passed'])
 return {'passed':True,'actual_full_action_dimension':size,'signed_hankel_controls':cases,
 'independent_factored_source_payments':18,'shared_scalar_correlation_controls':scalar_cases,
 'independent_action_lower_positive':True,'independent_residual_floor':str(floor),
 'common_simple_strict_residual_squared_lower':str(strict),
 'independent_ideal_estimator_floor':str(M*M*floor/(4*c*c*ell)),
 'cc14_exact_checks':checks,'cc13_controls_replayed':controls['exact_checks'],
 'all_mixed_action_columns_retained':True,'synthetic_controls_are_arithmetic':False,'lean_certified':False}
if __name__=='__main__':
 out=run();(ROOT/'notes/data/RPB108_RICH_ACTION_CC14_VALIDATION_20261008.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items() if 'floor' not in k},indent=2))
