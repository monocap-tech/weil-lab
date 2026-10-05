"""Compare precomputed exact integration with full convolution on actual entries."""
import json
from math import factorial
from certify_native_legendre_small_window import F,bernoulli,legendre,add
from certify_native_exact_polynomial import correlation,mul
from certify_native_exact_kernel_integral import make_kernel_integrator,make_archimedean_integrator

a=F(81,100);L=4*a;N=260;K=230
B=bernoulli(2*K+2);kernel=[F(0)]*(2*K+1);kernel[0],kernel[1]=F(1),L/2
for k in range(1,K+1):kernel[2*k]=B[2*k]*L**(2*k)/factorial(2*k)
integrate=make_kernel_integrator(kernel,N+167)
p=legendre(83);exp1=[(-L)**k/factorial(k) for k in range(N+1)];expquarter=[(-L/4)**k/factorial(k) for k in range(N+1)]
arch=make_archimedean_integrator(kernel,expquarter,168)
checks=[]
for i,j in [(0,0),(80,82),(83,83)]:
    c=[a*x*2**k for k,x in enumerate(correlation(p[i],p[j]))]
    delta=F(2*a,2*i+1) if i==j else F(0)
    numerator=add([delta*x for x in exp1],[-x for x in mul(expquarter,c)])
    assert numerator[0]==0
    full=mul(numerator[1:],kernel)
    original=sum((x/F(k+1) for k,x in enumerate(full)),F(0))
    assert integrate(numerator[1:])==original,(i,j)
    assert arch(c,delta)==original,(i,j)
    checks.append([i,j])
print(json.dumps(dict(exact_actual_entry_integral_checks=checks,original_full_convolution_agreement=True),indent=2))
