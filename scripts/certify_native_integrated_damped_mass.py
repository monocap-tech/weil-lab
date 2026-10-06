"""Integrated Bessel damping on each retained degree, with a complete tail."""
from math import prod,factorial
from certify_native_legendre_small_window import F,I,atan
from certify_native_larger_aperture_complement import integrated_mass


def integrated_damped_mass(a,k,T,N=48):
    if not a>0 or k<1 or not T>0 or N<1:raise ValueError('Invalid damped mass arguments')
    pi=16*atan(F(1,5))-4*atan(F(1,239))
    low=2*a*pi.lo*T;high=2*a*pi.hi*T
    if high*high>=k*(k+1):raise ValueError('Outside proved positive Bessel region')
    total=I(0);terms=[]
    for n in range(k,k+N):
        z=low*low/F(2*n+3)
        rate=F(2*n+1)-2*high*high/F(2*n+3)
        assert rate>0
        attenuation=I(1/sum((z**j/factorial(j) for j in range(61)),F(0))).hi
        D=prod(range(1,2*n+2,2))
        term=I(4*a*T*(2*n+1)*high**(2*n)*attenuation/(rate*D*D)).hi
        total+=term;terms.append(str(term))
    tail=I(integrated_mass(a,k+N,T)).hi
    total+=tail
    return total.hi,dict(degrees=list(range(k,k+N)),individual_integrated_term_upper=terms,
        infinite_undamped_tail_upper=str(tail),positive_region_argument_squared_upper=str(high*high),
        exponential_lower_terms=61,interval_grid_digits=len(str(I.grid))-1)
