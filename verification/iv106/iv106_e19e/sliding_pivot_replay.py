"""E19E: exact eligibility census and synthetic rational Cramer tests.
Synthetic systems are not evaluations of the IV105C response.
"""
from math import comb
import sympy as S

excluded={35,36,76,177,178,245,332,454,455}
eligible=set(range(1,664))-excluded
k=34
starts=[s for s in sorted(eligible) if all(s+j in eligible for j in range(k+1))]
assert len(eligible)==654 and len(starts)==416
assert starts[0]==37 and starts[-1]==629
assert len(set(starts))==len(starts)
assert sum(comb(k,j+1) for j in range(k))==2**k-1
assert max(comb(k,j+1) for j in range(k))==2333606220
print("eligible cells",len(eligible),"sliding starts",len(starts))
# Exact rational synthetic moment systems:
# X_n=n, Y_n=1/n, W_n=(n-1)n^k, n=2,...,N+1.
# These choices make both A and b integral; inverse and solve are exact.
for k,N in [(2,4),(5,8),(12,16),(34,35),(34,42)]:
    nodes=list(range(2,N+2))
    A=S.Matrix(k,k,lambda i,j: sum((n-1)*n**(k+j-i) for n in nodes))
    b=S.Matrix([sum((n-1)*n**(k-i-1) for n in nodes) for i in range(k)])
    c=A.inv(method="DM")*b
    assert A*c==b
    assert all(0<=(-1)**j*c[j]<=comb(k,j+1) for j in range(k))
    print(k,N,"PASS","max abs",float(max(map(abs,c))),"l1",float(sum(map(abs,c))))
# Independence of the actual corrected bank, conditional on nonzero
# disjoint-cell representatives and exact response cancellation:
# in a nonzero linear combination choose the smallest start s
# with nonzero coefficient; its own cell survives, all later starts
# have support strictly to the right of the interior of that cell.
