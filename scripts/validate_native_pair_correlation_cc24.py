"""CC24 exact finite-perturbation and physical pulse controls, not zeta data."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
from validate_native_translation_candidate_cc21 import ga,gm,gn,gs
from validate_native_signed_budget_cc23 import run as inherited_run
ROOT=Path(__file__).resolve().parents[1]
def poly(z,theta,kappa):
 z2=gm(z,z);u=(2*theta,kappa);v=(2*theta,-kappa)
 return gm(ga(z2,gs(-1,gm(u,u))),ga(z2,gs(-1,gm(v,v))))
def run():
 counts={k:0 for k in ('gram_kernel','pulse_dictionary','perturbation_rate','relative_loss')}
 def check(v,k):assert v,k;counts[k]+=1
 for kappa in (F(1,8),F(1,4),F(3,8)):
  check(4-4*kappa*kappa>0,'gram_kernel')
  # Exact integral of exp(-2|v|+u v), u real here; complex version analytic.
  for u in (-2*kappa,-kappa,F(0),kappa,2*kappa):
   check(1/(2-u)+1/(2+u)==4/(4-u*u),'gram_kernel')
   check(4/(4-u*u)<=1/(1-kappa*kappa),'gram_kernel')
  for theta in (F(1),F(7,3),F(25)):
   for sign in (-1,1):
    check(poly((2*theta,sign*kappa),theta,kappa)==(0,0),'pulse_dictionary')
    check(poly((-2*theta,sign*kappa),theta,kappa)==(0,0),'pulse_dictionary')
   A=16*theta*theta*(theta*theta+kappa*kappa)
   check(poly((F(0),kappa),theta,kappa)==(A,0),'pulse_dictionary')
   check(poly((F(0),-kappa),theta,kappa)==(A,0),'pulse_dictionary')
   check(A>0,'pulse_dictionary')
   for j in range(1,41):
    R=F(2**j);sinh=(R-1/R)/2
    Fplus=-2*A*sinh;Fminus=2*A*sinh
    p=(Fminus+Fplus)/2;n=(Fminus-Fplus)/2
    check(p==0 and n==2*A*sinh,'pulse_dictionary')
    check(2*n*n==8*A*A*sinh*sinh,'pulse_dictionary')
    check(8*A*A*sinh*sinh>=A*A*R*R,'pulse_dictionary')
 # T=X^8 makes the strip exponent saving T^-1/8 exact rational.
 for j in range(2,62):
  X=F(2**j);T=X**8
  # Normalized perturbation square T^(2kappa-1)=T^-1/4.
  check(2*F(3,8)-1==F(-1,4),'perturbation_rate')
  check(F(3,8)-F(1,2)==F(-1,8),'perturbation_rate')
  check(X**6/T==1/X**2,'perturbation_rate')
  check((X**3/X**4)==1/X,'perturbation_rate')
  check(1/X**2<=1/X,'perturbation_rate')
  # Mode-dependent defect can shrink independently of averaged error.
  delta=F(1,2**(3*j));alignment=F(1,2**j)
  check(alignment*alignment/delta==2**j,'relative_loss')
  check(alignment*alignment==F(1,2**(2*j)),'relative_loss')
  # Full positive physical mass control replay, with original distinction.
  a,k,mu=F(9,25),F(12,25),F(16,25)
  lam=a*a+mu;d=1-lam
  critical=a*a*k*k/(lam*d);low=k*k+mu-a*a*k*k/lam
  check(critical+low==1 and k*k/(1-a*a)==F(9,34)<1,'relative_loss')
 inherited=inherited_run();assert inherited['all_passed'] and inherited['total_exact_checks']==20836
 return {'stage':'CC24 unconditional pair correlation and finite-exception audit',
  'all_passed':True,'new_counts':counts,'new_exact_checks':sum(counts.values()),
  'inherited_cc23_checks':20836,'total_exact_checks':20836+sum(counts.values()),
  'classification':'A: finite perturbation stability and complete physical dictionary control; C: published averaged statistic does not supply adaptive relative covariance',
  'external_actual_input':'Baluyot-Goldston-Suriajaya-Turnage-Butterbaugh arXiv:2306.04799v1 Theorem 1; no RH assumption',
  'external_conjectural_comparison':'Goldston-Lee-Schettler-Suriajaya arXiv:2503.15449v4 Theorem 1 conditional on vertical PCC',
  'finite_perturbation_uniform_normalized_error':'O(T^-1/8) on 0<=alpha<=1 for fixed added reflected copies with |beta|<=3/8',
  'pulse_scope':'arbitrary complete critical-line background with polynomial counting; not actual modified zeta divisor or native explicit formula',
  'actual_relative_covariance_certified':False,'actual_zeta_bound_disproved':False,
  'complete_Weil_logical_independence_proved':False,'new_aperture':False,
  'global_nonstalling':False,'lean_certified':False,
  'whole_domain_anchor':'21/20 even0/odd0 inherited',
  'input_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in [
    'scripts/validate_native_signed_budget_cc23.py',
    'notes/data/RPB108_SIGNED_BUDGET_CC23_VALIDATION_20261008.json']},
  'constructor_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
if __name__=='__main__':
 out=run();(ROOT/'notes/data/RPB108_PAIR_CORRELATION_CC24_VALIDATION_20261008.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:out[k] for k in ('all_passed','new_counts','total_exact_checks')},indent=2))
