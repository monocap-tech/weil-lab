"""Exact algebra controls for NF55; no actual divisor or analytic certification."""
from fractions import Fraction as F
import json

checks = 0
def check(statement):
    global checks
    assert statement
    checks += 1

# Complete positive channel is identity in this finite control. The original
# form is positive; subtracting its lowest physical level changes the gain.
n2 = [F(9,25), F(16,25)]
q = [1-x for x in n2]
mu = min(q)
check(max(n2) < 1)
check(mu == F(9,25))
check(max(x+mu for x in n2) == 1)
check(n2[1] == 1-mu)
check(q[1]-mu == 0)

# Quantitative coercivity/gain dictionary in a second scalar model.
p2, neg2, canonical2 = F(4), F(1), F(1)
c2 = C2 = p2/canonical2
gain2 = neg2/p2
delta = (p2-neg2)/canonical2
check(delta == (1-gain2)*c2)
check(gain2 == 1-delta/C2)

# A truncated negative observation can miss the maximizing direction.
prefix_n2 = [n2[0], F(0)]
check(max(prefix_n2) < max(n2))

if __name__ == '__main__':
    print(json.dumps({'checks': checks, 'passed': True,
        'scope': 'finite rational algebra only; no actual gain estimate'}, indent=2))
