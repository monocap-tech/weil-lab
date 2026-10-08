"""Exact CC22 weight-transfer controls; not actual zero or covariance data."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
from validate_native_translation_candidate_cc21 import run as inherited_run
ROOT=Path(__file__).resolve().parents[1]
def run():
 counts={k:0 for k in ('dyadic_split','weight_transfer','genuine_crossing','positive_level')}
 def check(v,k):
  assert v,k
  counts[k]+=1
 examples=[]
 # Rational proxies for height weight and phase min bound, no numerical logs.
 for m in range(3,35):
  r=F(1,2**m)
  for j in range(1,2*m+1):
   lo,hi=2**j,2**(j+1)
   W=F(lo)*j*j
   phase_bound=min(F(4),hi*hi*r*r)
   check(phase_bound/W<=hi*hi*r*r/W,'dyadic_split')
   check(phase_bound/W<=4/W,'dyadic_split')
   if j<=m:
    check(hi*hi*r*r/W==F(4)*r*r*lo/(j*j),'dyadic_split')
   else:
    check(phase_bound/W==F(4,lo*j*j),'dyadic_split')
  for k in (F(1,8),F(1,2),F(1)):
   delta=F(1,2**m);W=F(2**(3*m))
   weighted=k*k/W;dual=W/delta;cost=k*k/delta
   check(weighted*dual==cost,'weight_transfer')
   check(dual>=1/delta,'weight_transfer')
   check(weighted<=k*k*delta**3,'weight_transfer')
   check(cost>=k*k*2**m,'weight_transfer')
   # Uniformly protected positive Gram, actual signed Schur obstruction.
   lam=1-delta;M=[[F(1),F(0)],[F(0),F(1)]]
   # Negative row (sqrt(lam), k); no rational square root needed.
   Qold=delta;Qnew=1-k*k;cross_squared=lam*k*k
   check(Qnew-cross_squared/Qold==1-cost,'weight_transfer')
  if m in (3,12,24,34):
   examples.append({'m':m,'delta':str(F(1,2**m)),
     'height_weight_proxy':str(2**(3*m)),
     'weighted_phase_squared_at_k_1_2':str(F(1,4*2**(3*m))),
     'original_relative_cost_at_k_1_2':str(F(2**m,4)),
     'scope':'rank-one weight-transfer control, not actual zeta'})
 # Genuine H01 differential form: u=2s/pi, v=2t/pi.
 for j in range(2,82):
  u=1-F(1,2**j);delta=1-u*u
  leak=2*u*(1-u)
  check(leak/delta==2*u/(1+u)<1,'genuine_crossing')
  check(1-leak/delta==(1-u)/(1+u),'genuine_crossing')
  v=F(9,8);beyond=2*u*(v-u)/delta
  check(beyond>1,'genuine_crossing')
  check(beyond>=u/(4*delta),'genuine_crossing')
 # Genuine positive level and complete physical mass channel retained.
 a,k,mu=F(9,25),F(12,25),F(16,25)
 lam=a*a+mu;delta=1-lam
 critical=a*a*k*k/(lam*delta)
 low=k*k+mu-a*a*k*k/lam
 check(k*k/(1-a*a)==F(9,34)<1,'positive_level')
 check(critical+low==1,'positive_level')
 check(1-k*k-mu-a*a*k*k/delta==0,'positive_level')
 check(a*a+k*k+mu==1,'positive_level')
 inherited=inherited_run()
 assert inherited['all_passed'] and inherited['total_exact_checks']==13996
 out={'stage':'CC22 actual density phase modulus and weight-transfer audit',
  'all_passed':True,'new_counts':counts,'new_exact_checks':sum(counts.values()),
  'inherited_cc21_checks':13996,'total_exact_checks':13996+sum(counts.values()),
  'classification':'A: actual weighted negative phase modulus; C: separated weight-transfer closure rejected',
  'finite_controls':examples,
  'actual_weighted_phase_rate':'squared HS O_B,eta((log log(1/|r|))^2/(log(1/|r|))^eta), eta>0',
  'proof_scope':'analytic rate proved in note; exact rational controls do not validate actual zero data',
  'unweighted_relative_covariance_certified':False,
  'actual_zeta_desired_bound_disproved':False,
  'complete_Weil_logical_independence_proved':False,
  'new_aperture':False,'global_nonstalling':False,'lean_certified':False,
  'whole_domain_anchor':'21/20 inherited CC18, even0/odd0',
  'input_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in [
    'scripts/validate_native_translation_candidate_cc21.py',
    'notes/data/RPB108_TRANSLATION_CANDIDATE_CC21_VALIDATION_20261008.json',
    'notes/REFLECTED_PACKET_BRIDGE_108_TRANSVERSE_DENSITY_SAMPLING_20261007.md']},
  'constructor_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
 return out
if __name__=='__main__':
 out=run()
 (ROOT/'notes/data/RPB108_DENSITY_PHASE_CC22_VALIDATION_20261008.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:out[k] for k in ('all_passed','new_counts','total_exact_checks')},indent=2))
