#!/usr/bin/env python3
"""NF383 independent exact-rational original n512 residual information audit.

Native original n512 is SHA-pinned. This does not compute original n513,
the missing exterior remainder, or the original whole Weil sign.
"""
import argparse
import hashlib
import json
import sys
from fractions import Fraction as F
from math import isqrt
from pathlib import Path

sys.set_int_max_str_digits(0)
ORIGINAL_SHA = '9d4b07fb2ca42c14ed995ddcd69811201eacb6f13f9f795a70c4b64889e9f83b'
D = F(2401, 2 * 10**28)
SHARE_LO, SHARE_HI = F(145133,10**6), F(145134,10**6)
TAIL_LO, TAIL_HI = F(854866,10**6), F(854867,10**6)

def sqrt_floor_ceil(x, scale=10**32):
    assert x>0
    y=x*scale*scale
    k=isqrt(y.numerator//y.denominator)
    lo,hi=F(k,scale),F(k+1,scale)
    assert lo*lo<=x<hi*hi
    return lo,hi

def test_abstract_nonidentifiability():
    # Pure Hilbert-space fixtures; not original signed Weil measurements.
    for x,y in [(F(1,3),F(2,5)),(F(0),F(7,4)),(F(9,8),F(0))]:
        b1,b2=x,y
        last=None
        for z in [F(0),F(1),F(100),F(10**12)]:
            assert (b1,b2)==(x,y)  # unchanged projected observations
            norm=x*x+y*y+z*z
            assert norm>=x*x+y*y
            if last is not None:assert norm>=last
            last=norm
    print('NF383 abstract finite-information counterexamples PASS (not original-object evidence)')

def evaluate(path):
    raw=Path(path).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==ORIGINAL_SHA
    j=json.loads(raw)
    assert j['unfitted_n']==512 and j['selected_rank']==242 and j['critical_count']==4
    assert j['original_physical_16_Gram_overlaps'] is True
    assert j['original_signed_32_CE_BP_overlaps'] is True
    assert j['original_WJJ_WJF_archived_cells_reused']==30371
    assert j['original_lowband_integral_computed'] is False
    assert j['entire_exterior_inverse_computed'] is False
    assert j['W_ODD_NEG']==j['RH']=='OPEN'
    assert F(j['original_direction_four_squared_residual_budget'])==D
    g_lo,g_hi=[F(v) for v in j['outside_E4_norm2_interval']]
    b_lo,b_hi=[F(v) for v in j['complete_original_signed_u4_qperp_interval']]
    assert 0<g_lo<=g_hi<F(11,10) and 0<b_lo<=b_hi
    d_lo=b_lo*b_lo/g_hi
    d_hi=b_hi*b_hi/g_lo
    assert SHARE_LO*D<d_lo<=d_hi<SHARE_HI*D
    # The unmeasured one-witness orthogonal remainder must satisfy this
    # NECESSARY budget IF the NF370 sufficient method is to pass.
    tail_budget_lo,tail_budget_hi=D-d_hi,D-d_lo
    assert TAIL_LO*D<tail_budget_lo<=tail_budget_hi<TAIL_HI*D
    root_lo,_=sqrt_floor_ceil(TAIL_LO*D)
    _,root_hi=sqrt_floor_ceil(TAIL_HI*D)
    assert root_lo*root_lo<TAIL_LO*D and root_hi*root_hi>TAIL_HI*D
    return dict(
      standing='NF383 EXACT ORIGINAL N512 FINITE-INFORMATION BUDGET; NO ORIGINAL N513 OR RESIDUAL UPPER',
      original_512_native_sha256=ORIGINAL_SHA,
      original_nf370_fourth_squared_residual_budget=str(D),
      strict_original_n512_dual_share_lower=str(SHARE_LO),
      strict_original_n512_dual_share_upper=str(SHARE_HI),
      strict_remaining_unmeasured_budget_fraction_lower=str(TAIL_LO),
      strict_remaining_unmeasured_budget_fraction_upper=str(TAIL_HI),
      strict_necessary_second_orthogonalized_amplitude_lower=str(root_lo),
      strict_necessary_second_orthogonalized_amplitude_upper=str(root_hi),
      necessary_second_amplitude_interpretation='The true needed signal sqrt(D-d1) is between the two bounds; no original second signal measured.',
      information_boundary='Finite observed pairings specify P_E r only; without an independent bound on ||(I-P_E)r|| they cannot certify a full strong residual upper.',
      original_n513_measured=False,
      whole_strong_residual_upper=False,
      original_operator_domain_audit='OPEN',W_ODD_NEG='OPEN',RH='OPEN')

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--self-test',action='store_true')
    p.add_argument('--original-512')
    p.add_argument('--output')
    args=p.parse_args()
    if args.self_test:test_abstract_nonidentifiability()
    if args.original_512:
        result=evaluate(args.original_512)
        if args.output:
            target=Path(args.output)
            target.parent.mkdir(parents=True,exist_ok=True)
            target.write_text(json.dumps(result,indent=2)+'\n')
        print('NF383 native pinned original n512 share: (145133/10^6,145134/10^6)')
        print('NF383 remaining unmeasured budget fraction: (854866/10^6,854867/10^6)')
        print('NF383 original n513, full residual upper, domain, W-ODD-NEG, RH OPEN')
    elif args.output:
        p.error('--output requires --original-512')
    elif not args.self_test:
        p.error('provide --original-512, optionally with --self-test')
if __name__=='__main__':main()
