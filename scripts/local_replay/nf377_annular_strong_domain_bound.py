#!/usr/bin/env python3
"""Exact-rational arithmetic for original odd annulus multiplier-domain scope.

Fourier identity and BV domain argument are analytic proof obligations described
in the companion note. This script verifies only their elementary rational caps.
"""
import json
from fractions import Fraction as F
from pathlib import Path
import argparse

def check():
    B=F(11,10); n=492; d=246; step=B/n; cutoff=2**20
    assert step == F(11,4920)
    assert n == 2*d
    assert F(n-d,n) == F(1,2) > F(49,100)
    # ||delta_i||^2=step, |hat(delta_i)(xi)|<=sqrt(2)/(pi |xi|)
    # for xi!=0. With pi>3, the unweighted whole-line high tail is
    # strictly below 4/(9 cutoff).
    unweighted=F(4,9*cutoff)
    assert unweighted < F(1,2_000_000)
    # Inherited original |m(xi)|<=17+log |xi| at |xi|>=1.
    # log(2)<7/10 implies A=17+log(2^20)<31.
    # int_cutoff^inf (17+log t)^2/t^2 dt=
    #  (A^2+2A+2)/cutoff. Hence <=1025/cutoff.
    squared_action=F(4*1025,9*cutoff)
    assert squared_action < F(1,2000)
    assert unweighted/step < F(1,5000)
    return {
      'standing':'EXACT_RATIONAL_DOMAIN_TAIL_UPPER_FOR_RAW_ANNULUS_ONLY',
      'scope':'Fourier BV tail for normalized raw odd annular box; projected q_i domain via finite BV combination, but NO quantified projected q_i tail',
      'B':str(B),'n':n,'subspace_dimension_upper':d,'step':str(step),
      'theoretical_some_unfitted_squared_mass_fraction_lower':'1/2',
      'native_strict_witness_fraction_target':'49/100',
      'cutoff':cutoff,
      'raw_annulus_unweighted_Fourier_tail_sq_strict_upper':str(unweighted),
      'raw_annulus_signed_multiplier_action_tail_sq_strict_upper':str(squared_action),
      'uses':'pi>3,log2<7/10,|m(xi)|<=17+log|xi| for |xi|>=1',
      'domain_conditional':'original multiplier bounded locally on |xi|<=1; original supported J/F are compact piecewise C1/BV',
      'selected_annulus_physical_certificate_passed':False,
      'projected_annulus_tail_quantified':False,
      'signed_lowband_integral_measured':False,
      'signed_fullband_pairing_measured':False,
      'original_Suzuki_normalization_transfer_proved':False,
      'W_ODD_NEG':'OPEN','RH':'OPEN'
    }

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--report',required=True)
    args=p.parse_args();data=check(); path=Path(args.report);path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
    print('PASS original raw annulus rational BV/log multiplier tail; projected signed response OPEN')
