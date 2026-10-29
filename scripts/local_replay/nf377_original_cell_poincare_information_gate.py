#!/usr/bin/env python3
"""NF377 informal exact-rational entry for the 492-cell Poincare information gate.

The Hilbert-space inequality is proved in the companion note; this checks
only exact rational thresholds. No signed original integral is measured.
"""
from fractions import Fraction as F
import json
from pathlib import Path
import argparse

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--report',required=True)
    args=p.parse_args()
    n=492
    d=246
    B=F(11,10)
    h=B/n
    h4=F(3,2*10**13)
    assert n==2*d
    assert h==F(11,4920)
    assert h4==F(3,20_000_000_000_000)
    # Exact rational conservative Poincare-Wirtinger (pi>3).
    coefficient=h*h/9
    derivative_only_threshold=3*h4/h
    assert derivative_only_threshold==F(1107,5_500_000_000_000)
    assert coefficient*derivative_only_threshold**2==h4**2
    assert h4*h4==F(9,4*10**26)
    report={
      'standing':'EXACT_RATIONAL_PRECONDITION_FOR_TWO_SIDED_CELL_REGULARITY_GATE',
      'method':'492 normalized odd annuli with Poincare-Wirtinger H1 remainder',
      'B':str(B),'annuli':n,'selected_plus_fitted_dimension_upper':d,
      'annulus_spacing':str(h),'lowband_direction_four_target':str(h4),
      'cell_energy':'A=sum_i |<g_low,q_i>|^2/h, q_i=(I-P_(J+E))delta_i',
      'unfitted_residual_lower':'A<=||r||^2',
      'unfitted_residual_upper':'||r||^2<=A+(h^2/pi^2)||r_prime||^2<=A+(h^2/9)||r_prime||^2',
      'fitted_component_payment_required':'inf_j H4(j)^2=||P_E Qg_low||^2+||r||^2',
      'conservative_derivative_square_coefficient':str(coefficient),
      'conservative_derivative_only_threshold':str(derivative_only_threshold),
      'threshold_only_preflight':True,
      'original_signed_cell_pairs_computed':False,
      'original_r_prime_norm_computed':False,
      'fitted_four_lowband_component_computed':False,
      'specific_annulus_native_certified':False,
      'NF375_lowband_budget_accepted':False,
      'external_method_promoted':False,
      'W_ODD_NEG':'OPEN','RH':'OPEN'
    }
    out=Path(args.report);out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(report,sort_keys=True,indent=2)+'\n')
    print('PASS exact Fraction cell-regularity threshold; actual signed response OPEN')

if __name__=='__main__':main()
