"""RC20 explicit canonical moment-head rank and full low-band residual."""
from fractions import Fraction as F
from math import factorial
import json
checks=0
def check(v):
    global checks
    assert v, checks+1
    checks+=1
def eb(x,n=96):
    p=sum((x**j/F(factorial(j)) for j in range(n+1)),F(0))
    return p,p+x**(n+1)/F(factorial(n+1))/(1-x/F(n+2))
B=F(11,10); T_upper=F(22100); n=460000
check(eb(F(10))[1]<T_upper)
check(eb(F(1))[1]<F(11,4))
BT_upper=B*T_upper
z_upper=2*F(22,7)*BT_upper
check(BT_upper==24310)
check(n>3*z_upper)
check(n>=128)
check(F(11,4)*z_upper/n<F(11,12))
check(F(11,12)**128<F(1,40000))
check(4*BT_upper<312**2)
eta=F(1,100)
check(F(312,40000)<eta)
alpha=F(1,10); penalty=F(153,10)
tail_floor=alpha-penalty*eta**2
check(tail_floor==F(9847,100000)>F(1,11))
m=F(1,4000); beta=F(1,300)
cost=beta**2/tail_floor
reserve=m-cost
check(cost==F(10,88623))
check(reserve==F(48623,354492000)>0)
check(F(30000000)/n>65)
# Orthogonality to X* enforces XH=0: exact finite feature-map control.
X=[[F(1),F(2),F(0)],[F(0),F(0),F(3)]]
h=[F(2),F(-1),F(0)]
check([sum(row[j]*h[j] for j in range(3)) for row in X]==[0,0])
check(sum(X[0][j]*h[j] for j in range(3))==0)
check(sum(X[1][j]*h[j] for j in range(3))==0)
# Small low-band residual alone pays the tail, not the cross budget.
generic_physical_tail_sq=eta**2+F(1,10)
check(21**2*generic_physical_tail_sq/tail_floor>m)
check(m*tail_floor-F(1,100)**2<0)
print(json.dumps({'milestone':'RC20','status':'PASS','exact_rational_checks':checks,
 'cap':'11/10','frequency_cutoff':'exp(10)','canonical_moment_head_rank_upper':n,
 'head_features':'canonical Riesz representatives of physical moments 0,...,459999',
 'whole_low_band_tail_norm_upper':str(eta),'original_whole_tail_floor':str(tail_floor),
 'conditional_actual_head_floor':str(m),'conditional_source_cross_norm_upper':str(beta),
 'conditional_schur_reserve':str(reserve),'projection_numerically_constructed':False,
 'actual_head_certified':False,'source_residual_certified':False,
 'whole_centered_aperture_extended':False,'RH':False,'F4':False,'Lean':False},indent=2))
