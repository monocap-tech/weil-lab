"""Independent binomial amplification and Akiyama Bernoulli constant audit at a=1."""
import hashlib,json
from pathlib import Path
from math import comb,isqrt
from fractions import Fraction as F
from certify_native_legendre_small_window import I
from certify_native_exact_logarithm import log_rational

def certificate(path):
    raw=Path(path).read_bytes();c=json.loads(raw);assert c['aperture']=='1'
    amp=sum((F(2*n+1)*sum(comb(n,k)*comb(n+k,k) for k in range(n+1))**2 for n in range(112)),F(0))
    assert amp==F(c['squared_physical_amplification'])
    A=[];B=[]
    for m in range(115):
        A.append(F(1,m+1))
        for j in range(m,0,-1):A[j-1]=j*(A[j-1]-A[j])
        B.append(A[0])
    checks=0
    for order in (50,56):
        e=abs(B[2*order+2])/((2*order+2)*100**(2*order+2));entry=c['constant_budgets']['gamma'+str(order)]
        assert e==F(entry['remainder'])
        assert F(entry['propagated_map_allowance'])**2>=e*e*amp;checks+=1
    saved=I.grid;I.grid=10**500
    try:
        def arctan(x,terms):
            s=sum(((-1)**k*x**(2*k+1)/F(2*k+1) for k in range(terms)),F(0))
            next_term=(-1)**terms*x**(2*terms+1)/F(2*terms+1)
            return I(min(s,s+next_term),max(s,s+next_term))
        pi=16*arctan(F(1,5),240)-4*arctan(F(1,239),240)
        for terms in (80,160):
            # Independent one-sided alternating endpoints refine the published symmetric enclosure.
            oldpi=16*arctan(F(1,5),terms)-4*arctan(F(1,239),terms)
            assert oldpi.lo<=pi.lo<=pi.hi<=oldpi.hi
            lp=I(log_rational(oldpi.lo,300).lo,log_rational(oldpi.hi,300).hi)
            radius=(lp.hi-lp.lo)/2;entry=c['constant_budgets']['pi'+str(terms)]
            assert radius<=F(entry['logarithm_radius'])
            assert F(entry['propagated_map_allowance'])**2>=F(entry['logarithm_radius'])**2*amp;checks+=1
        assert log_rational(F(3),450).lo>1
    finally:I.grid=saved
    return dict(aperture='1',certificate_sha256=hashlib.sha256(raw).hexdigest(),independent_binomial_amplification_checks=112,
        independent_akiyama_bernoulli_remainders=2,independent_one_sided_machin_checks=2,
        finer_machin_terms=240,log_terms=300,all_propagated_constant_allowances_verified=True,
        exponential_one_strictly_below_three=True,whole_domain_positivity=False,f4_entry_closed=False)

if __name__=='__main__':
    import sys
    print(json.dumps(certificate(sys.argv[1]),indent=2))
