#!/usr/bin/env python3
"""NF401 dependency-free exact regression for original Arb ball serialization.

Proves parser conservatively takes midpoint+radius, never point estimate.
"""
from fractions import Fraction as F
from nf400_original_selected_column_exact_receipt import exact_arb_upper

def check():
    assert exact_arb_upper('1/3')==F(1,3)
    assert exact_arb_upper('[1.25e-299 +/- 7.50e-1532]') == F('1.25e-299')+F('7.50e-1532')
    assert exact_arb_upper('[1.25e-299 +/- 7.50e-1532]')>F('1.25e-299')
    assert exact_arb_upper('[-1e-5 +/- 1e-6]')==F(-9,1000000)
    for bad in ('[1.25e-299 +/- -7.5e-1532]','1.25 +/- 7.5','[NaN +/- 1]'):
        try: exact_arb_upper(bad)
        except (AssertionError, ValueError,ArithmeticError): pass
        else:raise AssertionError('unbounded/invalid error paid: '+bad)
    print('NF401 exact original interval midpoint+radius parsing regression PASS')

if __name__=='__main__':check()
