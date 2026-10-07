"""Closed moment-sum audit of the 112-column analytic source budget."""
import hashlib,json
from pathlib import Path
from fractions import Fraction as F
from math import factorial

def certificate(path):
    raw=Path(path).read_bytes();c=json.loads(raw)
    assert c['aperture']=='1' and c['exponential_order']==90
    assert c['proposed_bernoulli_pairs']==114
    d=F(2);N=90;k=112
    ce=F(9,4)*(d/2)**(N+1)/factorial(N+1)
    ep=2*(d/4)**(N+1)/factorial(N+1)
    for key,entry in c['budgets'].items():
        K=int(key);cb=4*(d/3)**(2*K+2)/(1-(d/3)**2)
        H=2*(ce/(N+1)+cb/(2*K+2))+10*d*ep
        A=2*(ce/(N+2)+cb/(2*K+3))
        squared=k*k*H*H+k*k*(k*k-1)*H*A+F(k*k*(k*k-1)**2,3)*A*A
        assert squared==F(entry['squared_analytic_map_budget'])
        assert F(entry['analytic_map_upper'])**2>=squared
    assert F(c['budgets']['110']['analytic_map_upper'])>F(1,10**35)
    assert F(c['budgets']['114']['analytic_map_upper'])<F(1,10**35)
    return dict(certificate_sha256=hashlib.sha256(raw).hexdigest(),aperture='1',
        source_columns=112,independent_closed_weighted_moment_sums_checked=3,
        analytic_114_pair_allowance=c['budgets']['114']['analytic_map_upper'],
        excludes_interval_and_quantization_errors=True,complete_source_map_certified=False,
        whole_domain_positivity=False,whole_domain_frontier='399/400',f4_entry_closed=False)

if __name__=='__main__':
    import sys
    print(json.dumps(certificate(sys.argv[1]),indent=2))

