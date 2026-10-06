"""Exact algebra controls only; the analytic budget proof is in the note."""
from fractions import Fraction as F
import json

samples=0
for n in range(1,65):
    for j in range(33):
        theta=F(j,32)
        assert theta*theta/n<=1
        samples+=1
blocks=[]
for k in range(1,13):
    lo,hi=2**k,2**(k+1)
    # e<3 implies e+n<3+n; log(2)<1 is used analytically.
    assert all(3+n<=2**(k+3) for n in range(lo,hi))
    rational_budget=sum((F(n,1+n*n)/F(k+3) for n in range(lo,hi)),F(0))
    floor=F(1,4*(k+3))
    assert rational_budget>=floor
    blocks.append({"k":k,"lower_bound":str(floor)})
# log(1+n)<=k+2 on this dyadic block; n^2>=4^k.
# These block ceilings sum to 4 over all k>=1.
polynomial_partial=sum((F(k+2,2**k) for k in range(1,65)),F(0))
assert polynomial_partial<4
rejected=[]
for name,claim in [
    ("gaussian_exponent_at_least_one_throughout_window",F(0)>=F(1)),
    ("polynomial_log_budget_has_harmonic_block_floor",F(66,2**64)>=F(1,4*67)),
]:
    assert not claim
    rejected.append(name)
print(json.dumps({
 "scope":"rational comparisons only; no actual zeta vector or analytic certification",
 "gaussian_exponent_controls":samples,
 "dyadic_blocks_checked":12,
 "divergent_profile_block_lower_bounds":[b["lower_bound"] for b in blocks],
 "polynomial_block_sum_upper_bound":"4",
 "invalid_comparisons_rejected":rejected,
 "f4_closed":False,"full_transport_closed":False
},indent=2,sort_keys=True))
