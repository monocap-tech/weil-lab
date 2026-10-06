"""Finite polynomial iteration of the proved Bessel logarithmic derivative."""
from math import prod,factorial
from certify_native_legendre_small_window import F,I,atan
from certify_native_larger_aperture_complement import integrated_mass


def derivative_coefficients(n,depth):
    if type(n) is not int or n<1 or type(depth) is not int or not 0<=depth<=3:
        raise ValueError('Unsupported logarithmic derivative iteration')
    coefficients=[F(1,2*n+3)]
    for _ in range(depth):
        squared=[F(0)]*(2*len(coefficients)-1)
        for i,a in enumerate(coefficients):
            for j,b in enumerate(coefficients):squared[i+j]+=a*b
        coefficients=[F(1,2*n+3)]+[value/F(2*n+2*j+5) for j,value in enumerate(squared)]
    return coefficients


def integrated_iterated_mass(a,k,T,N=48,depth=2):
    if not a>0 or type(k) is not int or k<1 or not T>0 or type(N) is not int or N<1:
        raise ValueError('Invalid iterated mass arguments')
    derivative_coefficients(k,depth)
    pi=16*atan(F(1,5))-4*atan(F(1,239));low=2*a*pi.lo*T;high=2*a*pi.hi*T
    if high*high>=k*(k+1):raise ValueError('Outside proved positive Bessel region')
    total=I(0);terms=[];rates=[];exponents=[]
    for n in range(k,k+N):
        coefficients=derivative_coefficients(n,depth)
        exponent=I(sum((v*low**(2*j+2)/F(j+1) for j,v in enumerate(coefficients)),F(0))).lo
        rate=I(F(2*n+1)-2*sum((v*high**(2*j+2) for j,v in enumerate(coefficients)),F(0))).lo
        if rate<=0:raise ValueError('Nonpositive iterated integrated rate')
        attenuation=I(1/sum((exponent**j/factorial(j) for j in range(101)),F(0))).hi
        D=prod(range(1,2*n+2,2))
        term=I(4*a*T*(2*n+1)*high**(2*n)*attenuation/(rate*D*D)).hi
        total+=term;terms.append(str(term));rates.append(str(rate));exponents.append(str(exponent))
    tail=I(integrated_mass(a,k+N,T)).hi;total+=tail
    return total.hi,dict(degrees=list(range(k,k+N)),iteration_depth=depth,
        individual_integrated_term_upper=terms,infinite_undamped_tail_upper=str(tail),
        integrated_rate_lower=rates,squared_damping_exponent_lower=exponents,
        positive_region_argument_squared_upper=str(high*high),exponential_lower_terms=101,
        interval_grid_digits=len(str(I.grid))-1)
