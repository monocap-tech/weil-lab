"""RC67: recentered actual 64-mode metric and 22 native Riesz enrichment.

Replay integrates convolution polynomials by beta/log moments instead of
expanding their displacement polynomials. Residual refinement uses exact
canonical trial differences and the previously certified error Gram.
"""
from fractions import Fraction as F
from math import factorial,comb
from pathlib import Path
import hashlib,json,sys
from validate_rpb108_rc30_interval_metric import I,PI,loctx,hictx
from validate_rpb108_rc29_atom_reduction import legendre,overlap
from validate_rpb108_rc31_trial_riesz import mm,tr,inverse,psd
from validate_rpb108_rc47_correlated_native_transport import matrix,serialize,entries,rows
from validate_rpb108_rc57_uniform_low_head_floor import rounded_bound
from validate_rpb108_rc59_twenty_two_native_projection import nearest
DIM=64;NATIVE=22;ORDER=192;R=F(11,5)

def add(A,B,s=F(1)):return [[x+s*y for x,y in zip(a,b)] for a,b in zip(A,B)]
def scale(A,s):return [[s*x for x in row] for row in A]
def shifted(n):return [F((-1)**(n-k)*comb(n,k)*comb(n+k,k)) for k in range(n+1)]
def convolution(a,b):
 c=[F(0)]*(len(a)+len(b))
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j+1]+=x*y*factorial(i)*factorial(j)
 return [x/factorial(k) for k,x in enumerate(c)]
def displacement(c,parity):
 return [R*2*(-1)**parity*(-1/R)**k*sum((c[d]*comb(d,k) for d in range(k,len(c))),F(0)) for k in range(len(c))]
def bounds(x,den=10**30):
 lo=F(int(loctx.multiply(x.l,I(den).l).to_integral_value(rounding='ROUND_FLOOR')),den)
 hi=F(int(hictx.multiply(x.h,I(den).h).to_integral_value(rounding='ROUND_CEILING')),den)
 return lo,hi

def run(paths,replay=False,saved=None):
 raw=[Path(p).read_bytes() for p in paths];metric,native,residual,precision=[json.loads(x) for x in raw]
 hashes=[hashlib.sha256(x).hexdigest() for x in raw]
 assert residual['input_sha256']==[hashes[i] for i in [0,3,1]]
 assert native['input_sha256'][0]==hashes[0] and native['input_sha256'][2]==hashes[3]
 C=matrix(native['chebyshev_to_legendre']);Vold=matrix(native['native_trial_coefficients'])
 cmid=F(precision['constant_midpoint']);crad=F(precision['constant_radius'])
 H=[sum((F(1,k) for k in range(1,n+1)),F(0)) for n in range(ORDER+2*DIM+2)]
 Z=I(1).exp()*2*PI*I(R);assert Z.h<42
 q=[];l=[];power=I(1)
 for n in range(1,ORDER+1):
  power=power*Z/n
  if n%2==0:q.append((-1)**(n//2+1)*power/2);l.append(I(0))
  else:
   sign=(-1)**((n-1)//2);q.append(sign*power*I(H[n]+cmid-1)/PI);l.append(-sign*power/PI)
 # Precompute generic kernel moment families once, independently on replay.
 moments=[]
 for d in range(2*DIM):
  if replay:
   value=sum(((q[p]+l[p]*I(H[p]-H[p+d+1]))*I(F(factorial(p)*factorial(d),factorial(p+d+1))) for p in range(ORDER)),I(0))
  else:value=sum((q[p]/F(p+d+1)-l[p]/F((p+d+1)**2) for p in range(ORDER)),I(0))
  moments.append(value)
 polys=[shifted(i) for i in range(DIM)];mass=[R/F(2*i+1) for i in range(DIM)]
 G=[[F(0)]*DIM for _ in range(DIM)];intervals={};maxhalf=F(0)
 old={} if saved is None else entries(saved['recentered_nominal_metric_entry_enclosures'])
 for i in range(DIM):
  for j in range(i,DIM):
   if (i-j)%2:intervals[i,j]=(F(0),F(0));continue
   cv=convolution(polys[i],polys[j])
   if replay:value=R*2*(-1)**i*sum((I(x)*moments[d] for d,x in enumerate(cv)),I(0))
   else:
    op=displacement(cv,i%2)
    if j<8:assert op==overlap(i,j)
    value=sum((I(x*R**d)*moments[d] for d,x in enumerate(op)),I(0))
   endpoint=R*sum((x*y/F(a+b+1)**2 for a,x in enumerate(polys[i]) for b,y in enumerate(polys[j])),F(0))
   value+=endpoint
   if i==j:value+=(H[i]+cmid)*mass[i]
   if saved is None:a,b=bounds(value)
   else:
    a,b=old[i,j];assert I(a).l<=value.l<=value.h<=I(b).h
   intervals[i,j]=(a,b);G[i][j]=G[j][i]=(a+b)/2;maxhalf=max(maxhalf,(b-a)/2)
  print('metric row',i,'verified',file=sys.stderr,flush=True)
 epskernel=F(4,3)*(ORDER+DIM)*F(42)**(ORDER+1)/factorial(ORDER+1)
 delta=2*crad+epskernel+DIM*maxhalf/min(mass)
 # Rational outward budget also removes enormous factorial denominators.
 delta=F(-(-(delta*10**30).numerator//(delta*10**30).denominator),10**30)
 assert 0<delta<F(1,10**25)
 D=[[mass[i]*(i==j) for j in range(DIM)] for i in range(DIM)]
 Glo=add(G,D,-delta);Gup=add(G,D,delta);assert psd(Glo) and psd(add(Glo,D,-1))
 X=[[mass[i]*C[i][j] if i<NATIVE else F(0) for j in range(NATIVE)] for i in range(DIM)]
 GI=inverse(G);exact=mm(GI,X)
 V=[[nearest(x,10**40) for x in row] for row in exact]
 assert all(V[i][j]==0 for i in range(DIM) for j in range(NATIVE) if (i-j)%2)
 ML,mlround=rounded_bound(mm(mm(tr(X),inverse(Gup)),X),-1,10**30)
 priorML=matrix(native['actual_canonical_native_Gram_Loewner_lower'])
 assert psd(add(ML,priorML,-1))
 oldpad=Vold+[[F(0)]*NATIVE for _ in range(DIM-32)];W=add(V,oldpad,-1)
 J=mm(tr(X),W);cross=mm(mm(tr(oldpad),G),W)
 WT=mm(mm(tr(W),D),W);WG=mm(mm(tr(W),G),W);Told=matrix(native['physical_native_trial_Gram'])
 Ecold=matrix(residual['actual_canonical_Riesz_error_Gram_Loewner_upper'])
 # Exact identity Enew=Eold-W. <Eold,W>=X*W-Vold*Gactual W.
 # Metric perturbation: 2|<Vold,Delta W>|+<W,Delta W>
 # <=delta*(Told+2 WT), in quadratic-form order.
 allowance=scale(add(Told,WT,2),delta)
 Ecraw=add(add(add(add(Ecold,J,-1),tr(J),-1),cross),tr(cross))
 Ecraw=add(add(Ecraw,WG),allowance)
 Ec=rounded_bound(Ecraw,1,10**30)[0];rho=F(252,257);Ep=scale(Ec,rho)
 assert psd(Ec)
 improvement=add(Ecold,Ec,-1);whole=psd(improvement)
 if replay:
  # Independent expanded trial error identity, with old-minus-new trials.
  GTold=mm(mm(tr(oldpad),G),oldpad);GTnew=mm(mm(tr(V),G),V)
  JVold=mm(tr(X),oldpad);JVnew=mm(tr(X),V)
  alternate=add(add(add(add(Ecold,GTnew),GTold,-1),JVold),tr(JVold))
  alternate=add(add(alternate,JVnew,-1),tr(JVnew),-1)
  assert add(alternate,allowance)==Ecraw
  assert psd(add(Ec,Ecraw,-1))
 diagnostics=[]
 for j in range(NATIVE):
  diagnostics.append(dict(feature=j,prior_canonical_Riesz_error_squared_upper=str(Ecold[j][j]),enriched_canonical_Riesz_error_squared_upper=str(Ec[j][j]),diagonal_upper_bound_improvement_factor=str(Ecold[j][j]/Ec[j][j])))
 return dict(milestone='RC67',status='PASS',input_sha256=hashes,trial_dimension=DIM,native_features_certified=list(range(NATIVE)),
  kernel_degree=ORDER,recentered_metric_constant_midpoint=str(cmid),actual_recentered_metric_mass_error_upper=str(delta),
  recentered_nominal_metric_entry_enclosures=rows(intervals),recentered_nominal_metric_center=serialize(G),physical_mass=list(map(str,mass)),
  enriched_native_trial_coefficients=serialize(V),
  enriched_actual_native_Gram_Loewner_lower=serialize(ML),actual_native_Gram_lower_Loewner_improvement_certified=True,
  finite_trial_difference_physical_Gram=serialize(WT),
  actual_metric_trial_difference_allowance=serialize(allowance),
  enriched_actual_canonical_Riesz_error_Gram_Loewner_upper=serialize(Ec),enriched_actual_physical_Riesz_error_Gram_Loewner_upper=serialize(Ep),
  whole_Riesz_error_Gram_Loewner_improvement_certified=whole,diagonal_error_bound_comparisons=diagnostics,
  all_native_diagonal_Riesz_error_upper_bounds_improved=all(Ec[j][j]<Ecold[j][j] for j in range(NATIVE)),
  enriched_original_source_covariance_evaluated=False,enriched_projected_source_residual_bound_certified=False,
  prior_actual_projection_and_source_bounds_remain_valid=True,uniform_twenty_two_positive_Weil_floor_certified=False,
  whole_aperture_positivity_extended=False,RH=False,F4=False)
if __name__=='__main__':
 base=Path(__file__).parent.parent/'certificates'
 defaults=[base/n for n in ['rpb108_rc38_thirty_two_metric.json','rpb108_rc59_twenty_two_native_projection.json','rpb108_rc60_twenty_two_mixed_residuals.json','rpb108_rc56_precision_attached_head.json']]
 if len(sys.argv)>1 and sys.argv[1]=='--replay':
  saved=json.loads(Path(sys.argv[2]).read_text());assert run(sys.argv[3:] or defaults,True,saved)==saved
  print('PASS: independent beta/log kernel integration and expanded canonical trial-difference error replay')
 else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))
