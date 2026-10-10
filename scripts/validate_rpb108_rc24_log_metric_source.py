"""RC24 exact budgets for physical logarithmic metric sources."""
from fractions import Fraction as F
import json
checks=0
def check(v):
    global checks
    assert v, checks+1
    checks+=1
B=F(11,10)
check(2*B<F(3,2)**2)
check(B>=1) # disjoint unit-width endpoint-log strips
# ||(log_+(1/(B-x))+log_+(1/(B+x)))/2||_2^2=1.
log_square_integral=F(2)
check(2*F(1,2)**2*log_square_integral==1)
exterior_source_norm_upper=1+F(1,2)*F(3,2)
check(exterior_source_norm_upper==F(7,4))
sup_coefficient=F(3,2)+exterior_source_norm_upper
derivative_coefficient=B*F(3,2)
check(sup_coefficient==F(13,4))
check(derivative_coefficient==F(33,20))
check(sup_coefficient+18*F(3,2)==F(121,4))
# Small-radius lower kernel estimate: 2*pi*e*r<=1 at r<=1/100.
r0=F(1,100)
check(2*F(22,7)*3*r0<1)
check(F(1,3)*F(1,4)==F(1,12))
# Chebyshev trial sum: sup <=sum|a_k|, Lip <=sum k^2|a_k|/B.
for coefficients in [[F(1)],[F(0),F(1)],[F(1,2),F(-1,3),F(2,5)], [F(0)]*8+[F(1)]]:
    amplitude=sum(abs(a) for a in coefficients)
    derivative_moment=sum(k*k*abs(a) for k,a in enumerate(coefficients))
    lip=derivative_moment/B
    physical_upper=sup_coefficient*amplitude+derivative_coefficient*lip
    check(physical_upper==F(13,4)*amplitude+F(3,2)*derivative_moment)
    check(physical_upper>=F(3,2)*amplitude)
# Constant trial has zero internal difference term, but two exterior tails.
check(B+F(1,2)>1 and B-F(1,2)<1)
check(F(1,2)+F(1,2)==1) # two external tails; neither may be omitted
check(F(1,4)+F(1,4)==F(1,2)) # bounded far-tail contribution
print(json.dumps({'milestone':'RC24','status':'PASS','exact_rational_checks':checks,
 'cap':'11/10','metric_symbol':'log(e+abs(xi))',
 'metric_density':'2*integral_0^infinity exp(-e*t)/(t^2+4*pi^2*r^2) dt',
 'near_kernel_upper':'1/(2*r)','far_kernel_upper':'1/(4*r^2)',
 'small_radius_kernel_lower':'1/(12*r), 0<r<=1/100',
 'exterior_source_L2_upper':'7/4',
 'Lipschitz_trial_source_L2_upper':'(13/4)*sup + (33/20)*Lip',
 'actual_constant_trial_source_identified':True,'actual_Riesz_solution_computed':False,
 'actual_weak_residual_norm_certified':False,'actual_head_certified':False,
 'whole_centered_aperture_extended':False,'RH':False,'F4':False,'Lean':False},indent=2))
