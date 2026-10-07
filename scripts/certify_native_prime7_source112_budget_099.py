"""Analytic truncation preflight only; excludes source rounding and Gram."""
import json
from math import factorial
from certify_native_legendre_small_window import F,I,bernoulli,sqrt_rational

def certificate():
    a=F(99,100);d=2*a;N=90;old=I.grid;I.grid=10**140
    try:
        budgets={}
        for K in (106,108,110):
            B=bernoulli(2*K+2)
            coefficients=[abs(B[2*k]*(2*d)**(2*k)/factorial(2*k)) for k in range(1,K+1)]
            assert all(y<x for x,y in zip(coefficients,coefficients[1:]))
            assert all((B[2*k]>0)==(k%2==1) for k in range(1,K+1))
            assert (1+d+d*d/3)/2<F(9,4)
            ce=F(9,4)*(d/2)**(N+1)/factorial(N+1)
            cb=4*(d/3)**(2*K+2)/(1-(d/3)**2)
            he=ce/(N+1)+cb/(2*K+2);ae=ce/(N+2)+cb/(2*K+3)
            ep=2*(d/4)**(N+1)/factorial(N+1)
            squared=sum(((2*n+1)*(2*he+2*n*(n+1)*ae+10*d*ep)**2 for n in range(112)),F(0))
            eta=sqrt_rational(squared).hi
            budgets[str(K)]=dict(squared_analytic_map_budget=str(squared),analytic_map_upper=str(eta),display=float(eta))
        assert F(budgets['106']['analytic_map_upper'])>F(1,10**34)
        assert F(budgets['110']['analytic_map_upper'])<F(1,10**35)
        return dict(aperture='99/100',exponential_order=N,proposed_bernoulli_pairs=110,
                    budgets=budgets,old_106_pair_analytic_budget_exceeds_1e_minus34=True,
                    excludes_interval_and_quantization_errors=True,
                    source_map_complete=False,gram_complete=False,whole_domain_positivity=False)
    finally:I.grid=old

if __name__=='__main__':print(json.dumps(certificate(),indent=2))
