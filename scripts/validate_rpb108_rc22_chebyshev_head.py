"""RC22 contour/Chebyshev low-band residual and explicit head budgets."""
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
B=F(11,10); n=8600
check(eb(F(7))[1]<1100)
check(eb(F(2,3))[1]<2) # log2>2/3
check(eb(F(1))[0]>2)
rho=F(2)
ellipse_height=(rho-1/rho)/2
check(ellipse_height==F(3,4))
BT_upper=B*1100
z_upper=2*F(22,7)*BT_upper
exponent_margin=F(2,3)*n-ellipse_height*z_upper
check(exponent_margin==F(610,21)>16)
check(4*BT_upper<70**2)
check(4/F(2**16)==F(1,16384))
check(F(70,16384)<F(1,100))
eta=F(1,100)
tail_floor=F(1,10)-12*eta**2
check(tail_floor==F(247,2500)>F(1,11))
m=F(1,4000); beta=F(1,300)
cost=beta**2/tail_floor
check(cost==F(1,8892))
check(m-cost==F(1223,8892000)>0)
check(F(23000,n)==F(115,43)>F(5,2))
# Finite exact controls of the Laurent/Chebyshev recurrence identity.
def cheb(k,x):
    if k==0: return F(1)
    a,b=F(1),x
    for _ in range(1,k): a,b=b,2*x*b-a
    return b
for w in [F(2),F(3,2)]:
    x=(w+1/w)/2
    for k in range(1,9):
        check(cheb(k,x)==(w**k+w**(-k))/2)
# Geometric-series tail factor: 2*sum_{k>=n}rho^-k=4*2^-n.
check(2/(1-1/rho)==4)
# Each bounded Chebyshev moment has squared dual norm <=2B.
check(2*B==F(11,5))
check(m*tail_floor-F(1,100)**2<0)
# Nonorthonormal finite source control: M is the canonical feature Gram.
M=[[F(4),F(2)],[F(2),F(2)]]
Minv=[[F(1,2),F(-1,2)],[F(-1,2),F(1)]]
def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
check(mm(M,Minv)==[[1,0],[0,1]])
a=F(1,2)
source_head=[[a*v for v in row] for row in M]
paid=mm(mm(source_head,Minv),source_head)
check(paid==[[a*a*v for v in row] for row in M])
residual=[[beta**2*v for v in row] for row in [[4,2],[2,1]]]
source_gram=[[paid[i][j]+residual[i][j] for j in range(2)] for i in range(2)]
check([[source_gram[i][j]-paid[i][j] for j in range(2)] for i in range(2)]==residual)
check([[beta**2*M[i][j]-residual[i][j] for j in range(2)] for i in range(2)]==[[0,0],[0,beta**2]])
print(json.dumps({'milestone':'RC22','status':'PASS','exact_rational_checks':checks,
 'cap':'11/10','frequency_cutoff':'exp(7)','canonical_chebyshev_moment_head_rank_upper':n,
 'contour_radius':str(rho),'contour_exponent_margin_lower':str(exponent_margin),
 'whole_low_band_tail_norm_upper':str(eta),'original_whole_tail_floor':str(tail_floor),
 'conditional_actual_head_floor':str(m),'conditional_source_cross_norm_upper':str(beta),
 'conditional_schur_reserve':str(m-cost),'canonical_projection_constructed':False,
 'actual_head_certified':False,'source_residual_certified':False,
 'whole_centered_aperture_extended':False,'RH':False,'F4':False,'Lean':False},indent=2))
