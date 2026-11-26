"""Independent exponential-series audit of the AM signed shift/weight caps."""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import hashlib,json,sys
raw=Path(sys.argv[1]).read_bytes()
assert hashlib.sha256(raw).hexdigest()=='2b149c79f469b594ce7c308e44c278da00e9e41fbd9da1436cad0b0dca9d294a'
d=json.loads(raw); M,W,h,shifts=(d[k] for k in ('M','W','h','shifts'))
pp={}
for p in range(2,55):
    if all(p%k for k in range(2,isqrt(p)+1)):
        n=p
        while n<=54: pp[n]=p; n*=p
# For 0 <= x <= 4, all terms nonnegative; tail after term 40
# is at most term 41 / (1-x/42).
def exp_bounds(x):
    assert 0<=x<=4
    t=s=F(1)
    for k in range(1,41): t=t*x/k; s+=t
    return s,s+(t*x/41)/(1-x/42)
assert len(pp)==24 and len(shifts)==48
rows=[]
for (n,p),((j,u),(jj,uu)) in zip(sorted(pp.items()),zip(shifts[::2],shifts[1::2])):
    assert jj==-j-1 and uu==u
    assert exp_bounds(F(4*j,M))[1]<n<exp_bounds(F(4*(j+1),M))[0]
    root=isqrt(n*10**40); assert root**2<=n*10**40<(root+1)**2
    q=F(u*root,W*10**20)
    assert exp_bounds(q)[0]>p
    rows.append(dict(n=n,p=p,j=j,u=u,sqrt_lower_num=root))
assert all(0<x<=10**8 for x in h)
v=lambda i:h[i] if 0<=i<M else 0
slacks=[7979648*W*x-1000000*sum(u*max(v(i+j),v(i+j+1)) for j,u in shifts) for i,x in enumerate(h)]
assert min(slacks)==18510382530000000
print(json.dumps({'shift_pairs':len(rows),'strict_shift_endpoint_comparisons':2*len(rows),'strict_weight_comparisons':len(rows),'integer_sqrt_checks':len(rows),'rows':len(slacks),'min_strong_slack':min(slacks),'worst_cell':slacks.index(min(slacks))},indent=2))
if len(sys.argv)>2: Path(sys.argv[2]).write_text(json.dumps(rows,indent=2)+'\n')
