#!/usr/bin/env python3
"""UOI048: exact rational verification of constants; not a Lean or analytic proof."""
from fractions import Fraction as Q
from pathlib import Path
import json, hashlib

delta = Q(1, 1000)
# e^u <= 1/(1-u) for 0<=u<1, applied to 5delta and 4delta.
C = 2 / (1-5*delta) / (1-1/(1-4*delta)/64)
assert C == Q(3187200, 1560757)
assert C < Q(21, 10)
majorant = Q(21, 10)
row_coeff = majorant * Q(8, 511)
col_coeff = majorant / 63
assert row_coeff < Q(1, 30)
assert col_coeff == Q(1, 30)
# Full off-diagonal (two triangles) Hilbert-Schmidt squared bound.
hs2_bound = 2 * majorant**2 * delta**2 * Q(64, 63) / (8**6-1)
assert hs2_bound < Q(4, 10**11)
# Gamma mass lower G3 > 1099/1000 -> relative cross estimate.
normalized_base = delta / (30 * Q(1099, 1000))
assert normalized_base == Q(1, 32970)
# Spot-check exact finite row/column sums against uniform closed form.
checks = []
for M in [1,2,3,5,10,15]:
    row_sup = max(
        sum(majorant*delta*Q(1,8**j)*Q(1,8**(3*(k-j)))
            for k in range(M,M+100))
        for j in range(M)
    )
    col_sup = max(
        sum(majorant*delta*Q(1,8**j)*Q(1,8**(3*(k-j)))
            for j in range(M))
        for k in range(M,M+3)
    )
    closed = delta*Q(1,8**M)/30
    assert row_sup < closed and col_sup <= closed
    checks.append({'M': M, 'relative_kappa_upper': float(Q(1,8**M)/32970),
                   'L2_mixed_upper':str(closed)})
report = Path(__file__).resolve().parents[2]/'research/unified/receipts'/'UOI048_exact_constant_receipt.json'
proof = {'schema':'uoi048-elementary-constants-v1',
         'status':'exact rational constants only; no gamma digamma identity, analytic spectral, Lean or source-to-native proof',
         'exp_coefficient_upper':str(C),
         'row_coefficient':str(row_coeff),
         'column_coefficient':str(col_coeff),
         'HS_norm_squared_upper':str(hs2_bound),
         'normalized_kappa_upper_coefficient':str(normalized_base),
         'index_checks': checks,
         'verified_Lean_kernel':False,
         'verified_original_native_form':False}
report.write_text(json.dumps(proof,indent=2,sort_keys=True)+'\n')
print('PASS: exact digamma-kernel majorant and row/column Schur arithmetic')
print('C =', C, '; max row/col coefficient =', max(row_coeff,col_coeff))
print('HS^2 bound =', hs2_bound, '≈',float(hs2_bound))
print('kappa_M < 8^(-M)/32970')
