"""RC21 exact support-chain prime norm and explicit-head budgets."""
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
B=F(11,10)
check(9<eb(2*B)[0]<eb(2*B)[1]<10)
check(eb(F(7,10))[0]>2)
check(eb(F(11,10))[0]>3)
check(eb(F(161,100))[0]>5)
check(eb(F(39,20))[0]>7)
for square,root_lower in [(2,F(7,5)),(3,F(17,10)),(5,F(11,5)),(7,F(13,5)),(8,F(14,5))]:
    check(root_lower**2<square)
phi_upper=F(13,8); sqrt2_upper=F(17,12)
check(phi_upper>1 and phi_upper**2-phi_upper-1>0)
check(sqrt2_upper**2>2)
coefficients={2:F(1,2),3:F(11,17),4:F(7,20),5:F(161,220),7:F(3,4),8:F(1,4),9:F(11,30)}
chain_norm={2:phi_upper,3:sqrt2_upper,4:F(1),5:F(1),7:F(1),8:F(1),9:F(1)}
prime_upper=sum((coefficients[k]*chain_norm[k] for k in coefficients),F(0))
check(prime_upper==F(11029,2640))
negative_pole=F(179,310)
check(prime_upper+negative_pole==F(77831,16368)<5)
check(8+prime_upper+negative_pole<13)
check(8+prime_upper+F(1543,310)<18)
check(eb(F(7))[1]<1100)
check(eb(F(1))[1]<F(11,4))
alpha=F(1,10); ell=F(7); nonarch=F(5)
check((1-alpha)*ell-nonarch-(1+3*alpha)/2>0)
penalty=alpha*8+F(31,5)+nonarch
check(penalty==12)
n=23000; BT_upper=B*1100
check(n>6*F(22,7)*BT_upper)
check(n>=128)
check(F(11,12)**128<F(1,40000))
check(4*BT_upper<70**2)
check(F(70,40000)<F(1,100))
tail_floor=alpha-penalty*F(1,100)**2
check(tail_floor==F(247,2500)>F(1,11))
m=F(1,4000); beta=F(1,300)
cost=beta**2/tail_floor
check(cost==F(1,8892))
check(m-cost==F(1223,8892000)>0)
check(460000//n==20 and 460000%n==0)
check(m*tail_floor-F(1,100)**2<0)
print(json.dumps({'milestone':'RC21','status':'PASS','exact_rational_checks':checks,
 'cap':'11/10','prime_support_chain_norm_upper':str(prime_upper),
 'nonarch_negative_allowance':5,'native_remainder_norm_upper':18,
 'frequency_cutoff':'exp(7)','explicit_canonical_moment_head_rank_upper':n,
 'original_whole_tail_floor':str(tail_floor),'conditional_actual_head_floor':str(m),
 'conditional_source_cross_norm_upper':str(beta),'conditional_schur_reserve':str(m-cost),
 'head_constructed':False,'actual_head_certified':False,'source_residual_certified':False,
 'whole_centered_aperture_extended':False,'RH':False,'F4':False,'Lean':False},indent=2))
