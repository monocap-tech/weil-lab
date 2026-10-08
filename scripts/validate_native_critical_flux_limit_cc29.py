"""CC29 exact critical projection/flux lower-bound controls.
Infinite source exhaustion and actual no-flatness are analytic inputs.
No actual zeta contact, covariance upper bound or RH proof is evaluated.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
from validate_native_forced_source_cc20 import mm,tr,eye,sub
from validate_native_stationary_extension_cc28 import run as inherited_run
ROOT=Path(__file__).resolve().parents[1]
def scale(c,A):return [[c*x for x in row] for row in A]
def add(A,B):return [[x+y for x,y in zip(a,b)] for a,b in zip(A,B)]
def psd(A):return A[0][0]>=0 and A[1][1]>=0 and A[0][0]*A[1][1]>=A[0][1]*A[1][0]
def trace(A):return A[0][0]+A[1][1]
def family(d):
 P=[[1/(1+d*d),d/(1+d*d)],[d/(1+d*d),d*d/(1+d*d)]]
 return add(scale(F(1,2)-d,eye(2)),scale(F(1,2),P)),P
def run():
 counts={k:0 for k in ('critical_limit','noncommuting_order','power_divergence','genuine_crossing','full_mass')}
 def check(v,k):assert v,k;counts[k]+=1
 AA=[[F(1),F(0)],[F(0),F(1,2)]];gamma=F(1,8)
 AT=add(AA,scale(gamma,[[F(1),F(1)],[F(1),F(1)]]));y=[[F(1)],[F(0)]]
 rows=[]
 for j in (2,4,8,16,24,40):
  d=F(1,2**(2*j));AS,E=family(d);Ds=sub(eye(2),AS)
  check(mm(E,E)==E and E==tr(E),'critical_limit')
  check(mm(AS,E)==scale(1-d,E),'critical_limit')
  check(psd(Ds) and psd(sub(AA,AS)) and psd(sub(AT,AS)),'critical_limit')
  check(mm(AA,y)==y,'critical_limit')
  ys=mm(E,y);error=sub(y,ys)
  expected=mm(mm(tr(y),Ds),y)[0][0]
  den=mm(mm(tr(ys),Ds),ys)[0][0]
  check(expected==d+F(1,2)*d*d/(1+d*d),'critical_limit')
  check(mm(tr(error),error)[0][0]<=expected/F(1,4),'critical_limit')
  check(den==d/(1+d*d)<=expected,'critical_limit')
  Delta=sub(AT,AS);num=mm(mm(tr(ys),Delta),ys)[0][0]
  check(num>=gamma/2,'critical_limit')
  check(mm(mm(tr(y),sub(AT,AA)),y)[0][0]==gamma,'critical_limit')
  leakage=mm(mm(E,Delta),E);scalar=trace(leakage)
  check(mm(leakage,ys)==scale(scalar,ys),'critical_limit')
  check(scalar/d>=num/den>=gamma/(2*expected),'power_divergence')
  for power in (d,F(1,2**j),d*d):
   check(scalar/power>=gamma/(2*power),'power_divergence')
  nextA,nextE=family(d/4)
  check(psd(sub(nextA,AS)),'noncommuting_order')
  check(mm(E,nextE)!=mm(nextE,E),'noncommuting_order')
  rows.append({'old_defect_eigenvalue':str(d),'expected_contact_vector_defect':str(expected),
   'contact_flux':'1/8','critical_cost':str(scalar/d),
   'scope':'finite monotone rotating critical chart, not actual zeta'})
 # Genuine differential shell: fixed target v=1+h, not restricted positive.
 h=F(1,16);v=1+h
 for j in (8,16,32,48,64):
  u=1-F(1,2**j);gap=1-u*u;leak=2*u*(v-u)
  check(leak>h>0,'genuine_crossing')
  check(leak/gap>F(2)**(j-6),'genuine_crossing')
  check(leak*leak/gap>F(2)**(j-10),'genuine_crossing')
  check(leak/(gap*gap)>F(2)**(2*j-8),'genuine_crossing')
  # Restricting targets to contact permits bounded critical cost, while
  # its admissible width collapses; that is not the fixed-step property.
  check(2*u*(1-u)/gap==2*u/(1+u)<1,'genuine_crossing')
 a,k,mu=F(9,25),F(12,25),F(16,25)
 lam=a*a+mu;gap=1-lam
 critical=a*a*k*k/(lam*gap);low=k*k+mu-a*a*k*k/lam
 check(k*k/(1-a*a)==F(9,34)<1,'full_mass')
 check(critical+low==1 and low>0,'full_mass')
 check(lam==F(481,625) and gap==F(144,625),'full_mass')
 inherited=inherited_run();assert inherited['all_passed'] and inherited['total_exact_checks']==24748
 return {'stage':'CC29 critical flux limit / weaker sufficient target',
  'all_passed':True,'new_counts':counts,'new_exact_checks':sum(counts.values()),
  'inherited_cc28_checks':24748,'total_exact_checks':24748+sum(counts.values()),
  'conditional_actual_lower_bound':'critical defect-relative reaction >= gamma_t/(2 d_s) near hypothetical first contact at fixed t>a',
  'sufficiency':'cap-only fixed band and positive steps with any bounded vanishing modulus imply no first contact',
  'no_low_budget_required_for_endpoint_argument':True,
  'low_budget_still_required_for_finite_step_product_argument':True,
  'finite_operator_examples':rows,'actual_contact_exists_claimed':False,
  'actual_arithmetic_modulus_established':False,'RH_proved':False,
  'actual_critical_covariance_evaluated':False,'new_aperture':False,'lean_certified':False,
  'input_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in [
   'scripts/validate_native_stationary_extension_cc28.py',
   'notes/data/RPB108_STATIONARY_EXTENSION_CC28_VALIDATION_20261008.json',
   'notes/REFLECTED_PACKET_BRIDGE_108_SOURCE_SHELL_GAIN_20261008.md',
   'notes/REFLECTED_PACKET_BRIDGE_108_STATIONARY_EXTENSION_CC28_20261008.md']},
  'constructor_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
if __name__=='__main__':
 out=run();(ROOT/'notes/data/RPB108_CRITICAL_FLUX_LIMIT_CC29_VALIDATION_20261008.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:out[k] for k in ('all_passed','new_counts','total_exact_checks')},indent=2))
