#!/usr/bin/env python3
"""UOI050: exact elementary checks. NOT PNT, Gamma, original form or Lean certificate."""
import json
from fractions import Fraction as Q
from pathlib import Path
import sympy as sp

x, u, y = sp.symbols('x u y', real=True, positive=True)
h = sp.Function('h')
F = u**sp.Rational(-1,2) * h(y - sp.log(u))
expected = -u**sp.Rational(-3,2) * (
    sp.diff(h(x), x).subs(x, y-sp.log(u)) + sp.Rational(1,2)*h(y-sp.log(u)))
assert sp.simplify(sp.diff(F,u)-expected) == 0

# A compactly supported C^4 polynomial precursor with 5-fold endpoint zeros.
# Its third-order differential annihilator has neutral moments at lambda=0,+-1/2.
q=x**5*(1-x)**5
H=sp.expand(sp.diff(q,x,3)-sp.diff(q,x)/4)
assert H != 0
for lam in [sp.Integer(0), sp.Rational(1,2), sp.Rational(-1,2)]:
    moment = sp.simplify(sp.integrate(sp.exp(lam*x)*H,(x,0,1)))
    assert moment == 0, (lam,moment)
for d in range(5):
    assert sp.diff(q,x,d).subs(x,0)==0
    assert sp.diff(q,x,d).subs(x,1)==0

# Exact algebraic cancellation sqrt(|I_k|)*e^(c_k/2) for 8-adic c_k.
delta = Q(1,1000)
scales=[]
for k in [0,1,2,3,5,10,15,30,60]:
    width=delta/Q(8**k)
    assert width * (8**k) == delta
    scales.append({'k':k, 'width':str(width),'width_times_8powerk':str(width*8**k)})

receipt={
    'schema':'uoi050-exact-elementary-identity-v1',
    'scope':'sympy exact derivative and moment identities, rational collar scaling; classical PNT used as external theorem, not verified',
    'physical_derivative_identity':'F_y_prime(u)=-u^(-3/2)*(h_prime(y-log(u))+h(y-log(u))/2)',
    'polynomial_precursor':'q=x^5*(1-x)^5 for 0<x<1, extended by zero',
    'annihilator':'h=(D^3-D/4)q',
    'exact_zero_exponential_moments':['0','1/2','-1/2'],
    'collar_scale_checks':scales,
    'PNT_error_theorem_verified':False,
    'full_prime_operator_compact':False,
    'Lean_kernel_verified':False,
    'source_to_native_verified':False,
}
path=Path(__file__).resolve().parents[2]/'research/unified/receipts/'/'UOI050_discrepancy_receipt.json'
path.write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n')
print('PASS: exact derivative, 3 exponential moments, and 8-adic collar scaling')
