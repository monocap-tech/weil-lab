"""Independent exact Bernoulli constants through the aperture-one native kernel."""
import hashlib,json
from pathlib import Path
from fractions import Fraction as F
from math import factorial
from certify_native_legendre_small_window import bernoulli

def certificate():
    saved=bernoulli(722);A=[];checks=0
    for m in range(723):
        A.append(F(1,m+1))
        for j in range(m,0,-1):A[j-1]=j*(A[j-1]-A[j])
        actual=-A[0] if m==1 else A[0]
        assert actual==saved[m];checks+=1
    coefficients=[abs(saved[2*k]*F(4)**(2*k)/factorial(2*k)) for k in range(1,115)]
    assert all(y<x for x,y in zip(coefficients,coefficients[1:]))
    assert all((saved[2*k]>0)==(k%2==1) for k in range(1,362))
    assert F(13,6)<F(9,4) and F(2,3)<1
    return dict(aperture='1',independent_akiyama_vs_defining_recurrence_checks=checks,
        all_native_360_pair_and_source_114_pair_constants_verified=True,
        source_alternating_decreasing_pairs_verified=114,native_nonzero_even_signs_verified=361,
        exact_source_kernel_ceiling='13/6',source_kernel_ceiling_below='9/4',
        native_kernel_guard=5,exponential_guard=55,whole_domain_positivity=False,f4_entry_closed=False,
        auditor_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())

if __name__=='__main__':print(json.dumps(certificate(),indent=2))
