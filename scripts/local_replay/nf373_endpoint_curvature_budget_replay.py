#!/usr/bin/env python3
"""NF373 exact-rational directional-four endpoint/curvature conditional budget.

Audit the pinned native outward-bound display and NF372 exact raw-source tail.
Conditional curvature ceiling is NOT measured and NOT original residual closure.
"""
from fractions import Fraction as F
from decimal import Decimal
from pathlib import Path
import hashlib, json, re

S372='11f1b83d8a4920bb606a5a6e7b41db317bedbcd611e9abae4126eaf54e6df551'
S373='869e44ee2c7ff2547c163bc563864ad8ebf65c8d52e4199ba8e5a06979bed87e'

def load(p,sha):
    b=Path(p).read_bytes()
    assert hashlib.sha256(b).hexdigest()==sha,(p,'sha mismatch')
    return json.loads(b)

def decimal_ball_upper(s):
    m=re.fullmatch(r'\[([^\[\]]+) \+/- ([^\[\]]+)\]',s)
    assert m, ('unexpected native Arb outward interval',s[:100])
    return F(Decimal(m[1]))+F(Decimal(m[2]))

def main():
    p372=load('notes/data/provisional/NF372_replay.json',S372)
    p373=load('notes/data/provisional/NF373_native_accepted_endpoint_jets.json',S373)
    assert p373['native_parent_physical_quotient_overlap_pass']
    assert p373['working_precision_bits']==4096
    assert p373['W_ODD_NEG']==p373['RH']=='OPEN'
    assert not p373['full_exterior_residual_certified']
    assert not p373['complete_original_multiplier_high_tail_certified']
    caps=[(F(81,10**12),F(224,10**8)),
          (F(44,10**13),F(13,10**8)),
          (F(102,10**14),F(27,10**9)),
          (F(78,10**14),F(21,10**9))]
    for i,jet in enumerate(p373['boundary_jets']):
        assert jet['direction']==i+1
        assert F(jet['strict_rational_endpoint_cap'])==caps[i][0]
        assert F(jet['strict_rational_derivative_cap'])==caps[i][1]
        assert decimal_ball_upper(jet['w_endpoint_abs_upper'])<caps[i][0]
        assert decimal_ball_upper(jet['w_derivative_abs_upper'])<caps[i][1]
    d4=p372['directions'][3]
    assert d4['direction']==4
    raw_source_tail=F(d4['complete_raw_source_log_tail_strict_upper'])
    assert raw_source_tail<F(5011,10**17)
    # Elementary upper calculation from pi>3 and L=17+ln(2^24)<34.
    # ln(2)<7/10 follows from the first 4 terms of exp(7/10)>2.
    lam=2**24; L=F(34)
    J2=F(2,lam)*(L*L+2*L+2)
    J4=F(2,lam**3)*(L*L/3+2*L/9+F(2,27))
    C0=F(1,240)
    C1=F(1,4*10**10)
    assert J2/9<C0*C0
    assert J4/(4*3**4)<C1*C1
    # Deliberately unmeasured conditional bulk curvature integral.
    curvature_hypothesis=F(1,100)
    wB,wDB=caps[3]
    strict_conditional_highband_upper=raw_source_tail+C0*wB+C1*(wDB+curvature_hypothesis)
    budget_squared=F(49,50000)*F(49,10**23)/4
    assert strict_conditional_highband_upper < F(304,10**15)
    assert strict_conditional_highband_upper**2 < budget_squared
    # There is a positive low-band allowance only if the curvature hypothesis holds.
    print('PASS: NF373 SHA-pinned native endpoint outward balls fit 4 exact rational caps')
    print('PASS: certified direction-four endpoint-only high-tail constants')
    print('PASS: CONDITIONAL if integral_0^B |w4_doubleprime| <= 1/100,')
    print('      ||1_high m u4_hat||_2 < 3.04e-13, below NF370 individual 3.465e-13 ceiling')
    print('UNMEASURED: curvature hypothesis; selected low-band residual; full signed exterior Schur')
    return strict_conditional_highband_upper

if __name__=='__main__':main()
