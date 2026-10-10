"""RC6 small-step, signed-block and genuine shell controls."""
from fractions import Fraction as F
import json
checks=0
def check(v):
    global checks
    if not v: raise AssertionError(checks+1)
    checks+=1

# Old positivity plus an arbitrarily small mixed row permits target negativity.
for n in [2,4,8,16,32,64]:
    width=F(1,n)
    old=width**4
    outgoing=width
    new_diag=F(1)
    check(old>0 and outgoing<=F(1,2))
    check(old*new_diag-outgoing*outgoing<0)
    check(outgoing*outgoing/old==n*n)

# Exact scalar factorization O=R sqrt(H), tested in squared quantities.
for old in [F(1,2),F(1,100),F(1,10000)]:
    for o2 in [old/F(3),old,3*old]:
        ratio=o2/old
        check(o2==ratio*old)
        check((o2<=2*old)==(ratio<=2))

# Genuine differential source-shell formula from CC19 in rational u,v.
# A fixed reserve forces permitted steps to vanish with the old defect.
rho=F(1,2)
for u in [F(1,2),F(3,4),F(15,16),F(255,256)]:
    defect=1-u*u
    maximal_width=rho*defect/(2*u)
    check(2*u*maximal_width/defect==rho)
    check(maximal_width < 1-u)
    fixed_target=F(9,8)
    leak=2*u*(fixed_target-u)
    check(leak>0 and leak/defect>rho)

# Target signed positivity does imply the linear mixed bound, but is its premise.
for old,diag,mixed in [(F(1),F(2),F(1)),(F(1,4),F(1),F(1,2)),(F(1,16),F(1),F(1,2))]:
    determinant=old*diag-mixed*mixed
    check((determinant>=0)==(mixed*mixed<=diag*old))

print(json.dumps({'milestone':'RC6','status':'PASS','exact_rational_checks':checks,
 'scope':'native factorization, small-step failure and genuine differential budgets',
 'actual_native_decay_bound_proved':False,'RH':False,'F4':False,'Lean':False},indent=2))
