"""Exact abstract controls for RC2; no zeta/source certificate is tested."""
from fractions import Fraction as F
import json

checks = 0
def check(value):
    global checks
    if not value:
        raise AssertionError(checks + 1)
    checks += 1

# Two-dimensional high block; first coordinate is the paid trial frame.
# Exercise strict, semidefinite, and negative true Schur values, and
# optimal/nonoptimal coefficient choices, with a nonzero unresolved defect.
for k, c0, c1 in [(F(1), F(2), F(3)), (F(2), F(5), F(7))]:
    for b0, b1 in [(F(1), F(1)), (F(-2), F(3, 2))]:
        n = c0 * (c0-k) / k
        w = b0 * (c0-k)
        optimal = w / n
        defect = b1*b1 * (1/k - 1/c1)
        check(n > 0 and defect > 0)
        for schur in [F(-1), F(0), F(1, 100)]:
            q = b0*b0/c0 + b1*b1/c1 + schur
            for offset in [F(0), F(1, 3), F(-2)]:
                h = optimal + offset
                lower = q-(b0*b0+b1*b1)/k+(2*w*h-n*h*h)/(k*k)
                check(schur-lower == defect+n*offset*offset/(k*k))
                check(lower <= schur)

# Full response coverage does not prevent a smooth future first contact.
# C=2, B=1, k=1, Y=1, N=2, W=1, H=1/2.
k, c, b, n, w, h = F(1), F(2), F(1), F(2), F(1), F(1, 2)
for a in [F(53, 50), F(3, 2), F(2), F(5, 2)]:
    q = F(5, 2)-a
    schur = q-b*b/c
    lower = q-b*b/k+(2*w*h-n*h*h)/(k*k)
    check(lower == schur == F(2)-a)
check(F(2)-F(53, 50) > 0)
# At contact, v=(1,-1/2) is a genuine full-block null.
q, x, y = F(1, 2), F(1), F(-1, 2)
check(q*x+b*y == 0 and b*x+c*y == 0)
check(q*x*x+2*b*x*y+c*y*y == 0)
# Positive eigenlevel control: [[2,1],[1,2]] (1,-1)=1*(1,-1).
q, x, y, level = F(2), F(1), F(-1), F(1)
check(q*x+b*y == level*x and b*x+c*y == level*y)
check(q*x+b*y != 0 and b*x+c*y != 0)
check(q*x*x+2*b*x*y+c*y*y == level*(x*x+y*y) > 0)
print(json.dumps({'milestone': 'RC2', 'status': 'PASS',
                  'exact_rational_checks': checks,
                  'scope': 'abstract response identities and countercontrols',
                  'new_original_zeta_estimate': False,
                  'RH': False, 'F4': False, 'Lean': False}, indent=2))
