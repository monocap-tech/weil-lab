"""Exact controls for the global F4 implication audit; no actual zeta data."""
from fractions import Fraction as F
import json

def check(t):
    p, n, r, s, g, comp = F(1), t, t, F(1), F(1), -t
    a = p*p-n*n
    response = 1-r*r/g
    assert a == g-r*r == s*s*(1-comp*comp) == response
    return {"t": str(t), "native": str(a), "response": str(response)}

points = [F(1, 2), F(3, 4), F(1), F(5, 4), F(3, 2)]
rows = [check(t) for t in points]
assert all(1-x*x > 1-y*y for x, y in zip(points, points[1:]))
h, u, comp, r = F(1), F(-1), F(-1), F(1)
assert comp*u == h
assert comp*comp*u == u
assert -r*u == h
assert 1-r*r == 0  # actual zero in the strictly decreasing control
# A=diag(0,1); prescribed R=(0,1) misses its kernel.
blind_covariance = (F(0), F(2))
separating_covariance = (F(1), F(1))  # fresh R=(1,0)
assert min(blind_covariance) == 0
assert min(separating_covariance) > 0
rejected = []
for name, claim in [
    ("strict_monotonicity_excludes_contact", all(1-t*t != 0 for t in points)),
    ("existential_selection_certifies_prescribed_selection", min(blind_covariance) > 0),
]:
    assert not claim, name
    rejected.append(name)
print(json.dumps({
    "scope": "algebraic controls only; not actual zeta or nested support models",
    "response_crossing": rows,
    "endpoint_equations": "PASS",
    "blind_prescribed_covariance": [str(x) for x in blind_covariance],
    "fresh_separating_covariance": [str(x) for x in separating_covariance],
    "rejected_invalid_implications": rejected,
}, indent=2, sort_keys=True))
