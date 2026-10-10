"""RC17 direct native Schur bounds; exact rational controls, no head computed."""
from fractions import Fraction as F
from math import factorial
import json
checks=0
def check(v):
    global checks
    assert v, checks+1
    checks+=1
def eb(x,n=64):
    p=sum((x**j/F(factorial(j)) for j in range(n+1)),F(0))
    return p,p+x**(n+1)/F(factorial(n+1))/(1-x/F(n+2))
B=F(11,10)
check(eb(B)[1]<F(31,10))
check(eb(B)[0]>3)
check(9<eb(2*B)[0]<eb(2*B)[1]<10)
prime_sum=F(12093,3740)+F(11,30)
twosinh_upper=F(31,10)-F(10,31)
pole_negative_upper=twosinh_upper-2*B
pole_norm_upper=twosinh_upper+2*B
check(twosinh_upper==F(861,310))
check(pole_negative_upper==F(179,310)>0)
check(pole_norm_upper==F(1543,310))
check(8+2*prime_sum+pole_negative_upper<16)
check(8+2*prime_sum+pole_norm_upper<21)
M=F(21); N=F(16); delta=F(1,2000); m=F(1,4000)
tau=N*delta**2
rho_sq=M**2*delta**2
cost=rho_sq/(1-tau)
reserve=m-cost
check(tau==F(1,250000))
check(rho_sq==F(441,4000000))
check(cost==F(147,1333328))
check(reserve==F(46583,333332000)>0)
check(delta**2<m/(M**2+N*m))
check(m/(M**2+N*m)==F(1,1764016))
cutoff_exponent=4/delta**2
check(cutoff_exponent==16000000)
check(F(4*10**12)/cutoff_exponent==250000)
# Exact signed pole spectral identity: even/odd representers are orthogonal
# for a symmetric interval. Rational sinh surrogate only tests the algebra.
for s in [F(3,2),F(2),F(5)]:
    gram=[[2*s,2*B],[2*B,2*s]]
    swap=[[0,1],[1,0]]
    # Pole coefficient matrix in moment coordinates is swap.
    product=[[sum(swap[i][k]*gram[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
    for vec,eigen in [([1,1],2*s+2*B),([1,-1],2*B-2*s)]:
        check([sum(product[i][j]*vec[j] for j in range(2)) for i in range(2)]==[eigen*v for v in vec])
# A positive head and tail without the cross gate do not imply positivity.
check(F(1,100)*F(1,2)-F(1,10)**2<0)
print(json.dumps({'milestone':'RC17','status':'PASS','exact_rational_checks':checks,
 'cap':'11/10','native_remainder_norm_upper':str(M),
 'native_remainder_lower_bound':str(-N),'physical_tail_upper':str(delta),
 'whole_tail_floor':str(1-tau),'cross_norm_squared_upper':str(rho_sq),
 'conditional_actual_canonical_head_floor':str(m),'schur_cost_upper':str(cost),
 'conditional_schur_reserve':str(reserve),'generic_log_cutoff':str(cutoff_exponent),
 'actual_head_certified':False,'finite_space_numerically_constructed':False,
 'whole_centered_aperture_extended':False,'RH':False,'F4':False,'Lean':False},indent=2))
