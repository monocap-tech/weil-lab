#!/usr/bin/env python3
"""NF381 exact remaining source-adapted orthogonal signal after original NF380.

NF380 independent exact-rational original interval gave 1/7 < d1/D < 3/20.
The exact 2x2 Schur identity quantifies the missing conditional response.
This is an acceptance-condition theorem, NOT a new original n513 datum.
"""
import argparse,json
from fractions import Fraction as F
from pathlib import Path
from math import isqrt
D=F(2401,2*10**28)

def truncsqrt(x,scale=10**31):
    n=x*scale*scale
    k=isqrt(n.numerator//n.denominator)
    return F(k,scale),F(k+1,scale)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);args=ap.parse_args()
    lo=F(1,7)*D;hi=F(3,20)*D
    gaplo=D-hi;gaphi=D-lo
    assert gaplo==F(17,20)*D and gaphi==F(6,7)*D
    lower,upper=truncsqrt(gaplo)
    assert lower**2<gaplo<upper**2
    # D=fixed original fourth residual budget. NF380's *actual* d1 is
    # strictly inside bounds, so its unobserved orthogonal complement needs
    # stronger normalized response than sqrt(gaplo) to force a no-go.
    out={
      'standing':'EXACT ANALYTIC NF381 TWO-WITNESS NECESSARY SIGNAL BUDGET, NOT NEW WEIL PAIRING',
      'original_nf370_direction_four_squared_budget':str(D),
      'nf380_single_n512_squared_dual_ratio_strictly_above':'1/7',
      'nf380_single_n512_squared_dual_ratio_strictly_below':'3/20',
      'necessary_new_orthogonalized_squared_response_strictly_greater_than':str(gaplo),
      'missing_squared_fraction_of_original_budget_strictly_above':'17/20',
      'missing_squared_fraction_of_original_budget_strictly_below':'6/7',
      'outward_rational_lower_on_necessary_amplitude':str(lower),
      'outward_rational_upper_on_necessary_amplitude':str(upper),
      'joint_schur_formula':'d12=b1^2/g1+(b2-c*b1/g1)^2/(g2-c^2/g1)',
      'actual_original_b2_or_cross_Gram_measured':False,
      'complete_original_strong_residual_upper_computed':False,
      'operator_domain_review':'OPEN', 'W_ODD_NEG':'OPEN','RH':'OPEN'}
    Path(args.output).parent.mkdir(parents=True,exist_ok=True)
    Path(args.output).write_text(json.dumps(out,indent=2)+'\n')
    print('NF381 exact remaining response threshold:',str(lower),' < sqrt(gap) < ',str(upper))

if __name__=='__main__':main()
