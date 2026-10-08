"""CC26 exact cap-step/product-budget controls; no arithmetic budget proof."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
from validate_native_forced_source_cc20 import mm,tr,eye,sub,inv
from validate_native_finite_identity_cc25 import run as inherited_run
ROOT=Path(__file__).resolve().parents[1]
def scale(c,A):return [[c*x for x in row] for row in A]
def psd(A):return A[0][0]>=0 and A[1][1]>=0 and A[0][0]*A[1][1]>=A[0][1]*A[1][0]
def run():
 counts={k:0 for k in ('product_budget','cap_partition','crossing_nonstalling','physical_vs_source','full_positive_level')}
 def check(v,k):assert v,k;counts[k]+=1
 I=eye(2);rho=F(9,25);reserve=1-rho;examples=[]
 units=[[[F(1)],[F(0)]],[[F(0)],[F(1)]],[[F(3,5)],[F(4,5)]],[[-F(4,5)],[F(3,5)]]]
 for j in (1,4,16,32,64):
  L=[[F(1,2**j),F(0)],[F(0),F(1,2)]];delta0=F(1,2**(2*j))
  for n in range(1,25):
   u=units[(n-1)%len(units)];D=mm(L,tr(L));K=scale(F(3,5),mm(L,u))
   R=sub(I,scale(F(1,5),mm(u,tr(u))))
   check(mm(tr(K),mm(inv(D),K))==[[rho]],'product_budget')
   check(mm(R,tr(R))==sub(I,scale(rho,mm(u,tr(u)))),'product_budget')
   Ln=mm(L,R);Dn=mm(Ln,tr(Ln))
   check(Dn==sub(D,mm(K,tr(K))),'product_budget')
   check(psd(sub(Dn,scale(reserve,D))),'product_budget')
   check(psd(sub(Dn,scale(delta0*reserve**n,I))),'product_budget')
   check(psd(sub(I,Dn)),'product_budget')
   L=Ln
  examples.append({'anchor_source_defect_lower':str(delta0),'steps':24,
    'relative_budget':'9/25','product_defect_lower':str(delta0*reserve**24),
    'scope':'noncommuting finite source-chart control, not actual zeta'})
 a0=F(21,20)
 for B in (F(11,10),F(3,2),F(2),F(10),F(100)):
  for h in (F(1,20),F(1,4),F(1,2)):
   length=B-a0;ratio=length/h;N=(ratio.numerator+ratio.denominator-1)//ratio.denominator
   step=length/N
   check(N>=1 and 0<step<=h,'cap_partition')
   check(a0+N*step==B,'cap_partition')
   check(reserve**N>0,'cap_partition')
 # Genuine differential crossing, fixed positive cap-step must fail near contact.
 for j in range(8,65):
  u=1-F(1,2**j);gap=1-u*u;h=F(1,16);v=u+h
  check(v>1 and v<F(9,8),'crossing_nonstalling')
  check(2*u*h/gap>1>rho,'crossing_nonstalling')
  step=rho*gap/(2*u);vsmall=u+step
  check(2*u*(vsmall-u)/gap==rho,'crossing_nonstalling')
  check(u<vsmall<1,'crossing_nonstalling')
  check(0<(1-vsmall)/(1-u)<1-rho/2,'crossing_nonstalling')
  # Tiny original physical margin with exactly zero negative source gain.
  eps=F(1,2**j);P=[[eps,F(0)],[F(0),F(1)]];N=[[F(0),F(0)],[F(0),F(0)]]
  Q=mm(tr(P),P);T=mm(N,inv(P))
  check(Q[0][0]==eps*eps>0,'physical_vs_source')
  check(T==[[F(0),F(0)],[F(0),F(0)]],'physical_vs_source')
  check(sub(I,mm(T,tr(T)))==I,'physical_vs_source')
 # Full shifted physical mass remains separate from the original source budget.
 a,k,mu=F(9,25),F(12,25),F(16,25)
 lam=a*a+mu;gap=1-lam;critical=a*a*k*k/(lam*gap)
 low=k*k+mu-a*a*k*k/lam
 check(critical+low==1,'full_positive_level')
 check(k*k/(1-a*a)==F(9,34)<1,'full_positive_level')
 check(1-k*k-mu-a*a*k*k/gap==0,'full_positive_level')
 inherited=inherited_run();assert inherited['all_passed'] and inherited['total_exact_checks']==23330
 return {'stage':'CC26 quantifier and RH-strength audit of uniform continuation',
  'all_passed':True,'new_counts':counts,'new_exact_checks':sum(counts.values()),
  'inherited_cc25_checks':23330,'total_exact_checks':23330+sum(counts.values()),
  'finite_chain_examples':examples,
  'proved_reduction':'uniform whole strict budgets with positive cap-only steps imply all-cap original Weil positivity; RH gives N=0 and zero budgets',
  'reduction_dependencies':'inherited complete actual canonical identity, strict source anchor and positive observability; classical compact-test Weil criterion',
  'uniform_exit_property_proved_for_actual_zeta':False,'RH_proved':False,
  'critical_bound_without_low_or_nonstalling_equated_to_RH':False,
  'actual_zeta_bound_disproved':False,'new_aperture':False,'lean_certified':False,
  'whole_domain_anchor':'21/20 even0/odd0 inherited; source defect constant not numerically inferred from physical margin',
  'input_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in [
    'scripts/validate_native_finite_identity_cc25.py',
    'notes/data/RPB108_FINITE_IDENTITY_CC25_VALIDATION_20261008.json',
    'notes/REFLECTED_PACKET_BRIDGE_108_SHELL_LEAKAGE_CC19_20261008.md']},
  'constructor_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
if __name__=='__main__':
 out=run();(ROOT/'notes/data/RPB108_UNIFORM_EXIT_CC26_VALIDATION_20261008.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:out[k] for k in ('all_passed','new_counts','total_exact_checks')},indent=2))
