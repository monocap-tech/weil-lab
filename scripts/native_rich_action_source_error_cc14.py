"""Factored error payment for the unchanged ORIGINAL source polynomials.

The gamma/log constant is one shared scalar multiplying p, not independent
monomial errors. Nonconstant interval/decimal errors are separately paid.
"""
from certify_native_coupled_trial_cc3 import F,I,D,log,sqrt_rational,bernoulli
from math import factorial
def constant_radius(pi):
 B=bernoulli(362)
 gamma=I(sum((F(1,k) for k in range(1,101)),F(0))-F(1,200))-log(F(100))
 gamma+=sum((B[2*k]/F(2*k*100**(2*k)) for k in range(1,57)),F(0))
 ge=abs(B[114])/F(114*100**114);gamma+=I(-ge,ge)
 constant=-gamma-log(F(2))-I(log(pi.lo).lo,log(pi.hi).hi)-log(D)
 radius=(constant.hi-constant.lo)/2
 assert radius<F(1,10**130)
 return radius
def factored_error(p,M0,M1,regs,radius):
 degree=len(p)-1
 assert 0<=degree<=142 and 0<M0<100 and all(len(row)<1000 for row in regs)
 assert sum(map(abs,p),F(0))<=M0*8**degree
 assert M1<=142*143*M0 and I.grid==10**800
 # Fixed-grid interval errors in twelve translations and the other source
 # arithmetic and their scalar sensitivity factors are bounded by10^30
 # at these fixed finite orders. |shift|<=1; translated coefficient L1
 # amplification is <=2^degree. This deliberately loose bound also pays
 # the midpoint constant's grid rounding after factoring its uncertainty.
 assert log(F(8)).hi<D
 operations=10**30*M0*16**degree/I.grid
 # Each of <1000 chosen coefficients is floored on the ABSOLUTE grid10^-250.
 coefficient_rounding=F(1000,10**250)
 remainder=operations+coefficient_rounding
 assert remainder<F(1,10**200)
 N,K=140,180
 ce=F(23,10)*(D/2)**(N+1)/factorial(N+1)
 cb=4*(D/3)**(2*K+2)/(1-(D/3)**2)
 he=ce/(N+1)+cb/(2*K+2);ae=ce/(N+2)+cb/(2*K+3)
 exp_error=2*(D/4)**(N+1)/factorial(N+1)
 # Same original kernel/pole truncations; no source term is omitted.
 uniform=2*M0*he+2*M1*ae+100*D*M0*exp_error+M0*radius+F(1,10**200)
 return sqrt_rational(D).hi*uniform
