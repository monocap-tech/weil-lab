"""Complete integrated mass with proved quartic Bessel damping."""
from math import prod,factorial
from certify_native_legendre_small_window import F,I,atan
from certify_native_larger_aperture_complement import integrated_mass


def quartic_exponent(n,x):
    return x*x/F(2*n+3)+x**4/F(2*(2*n+3)**2*(2*n+5))


def integrated_quartic_mass(a,k,T,N=48):
    if not a>0 or k<1 or not T>0 or N<1:raise ValueError('Invalid quartic mass arguments')
    pi=16*atan(F(1,5))-4*atan(F(1,239))
    low=2*a*pi.lo*T;high=2*a*pi.hi*T
    if high*high>=k*(k+1):raise ValueError('Outside proved positive Bessel region')
    total=I(0);terms=[];rates=[];exponents=[]
    for n in range(k,k+N):
        z=high*high/F(2*n+3);w=high**4/F(2*(2*n+3)**2*(2*n+5))
        rate=F(2*n+1)-2*z-4*w
        if rate<=0:raise ValueError('Nonpositive integrated quartic rate')
        exponent=quartic_exponent(n,low)
        attenuation=I(1/sum((exponent**j/factorial(j) for j in range(81)),F(0))).hi
        D=prod(range(1,2*n+2,2))
        term=I(4*a*T*(2*n+1)*high**(2*n)*attenuation/(rate*D*D)).hi
        total+=term;terms.append(str(term));rates.append(str(rate));exponents.append(str(exponent))
    tail=I(integrated_mass(a,k+N,T)).hi;total+=tail
    return total.hi,dict(degrees=list(range(k,k+N)),individual_integrated_term_upper=terms,
        infinite_undamped_tail_upper=str(tail),integrated_rate_lower=rates,
        squared_damping_exponent_lower=exponents,positive_region_argument_squared_upper=str(high*high),
        exponential_lower_terms=81,interval_grid_digits=len(str(I.grid))-1)
