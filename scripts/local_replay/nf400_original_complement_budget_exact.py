#!/usr/bin/env python3
"""NF400 exact original J242 complement-only lowband sufficient gate.

Only proves a conditional algebraic acceptance: selected full-response
projection plus genuine lowband complement < sigma implies lowband < tau.
No complement upper measured.
"""
from fractions import Fraction as F
import hashlib,json
from pathlib import Path

NATIVE='notes/data/provisional/NF398_original_j387_selected_signed_native.json'
PIN='bae006e4fb542c4b0c6d184ae8cfbc2e7c924d45c89092ebda89cf0c6057c877'
SIGMA=F(11,40000000000000)   # 2.75e-13

def main():
    raw=Path(NATIVE).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==PIN
    x=json.loads(raw)
    assert x['original_NF375_fourth_cutoff']==2**24
    H=F(x['original_NF375_fourth_highband_action_norm_upper'])
    tau=F(x['original_NF375_fourth_lowband_future_target'])
    assert tau==F(7,25000000000000)
    assert 0<H<tau and 0<SIGMA<tau
    assert SIGMA**2+H**2 < tau**2
    assert x['W_ODD_NEG']==x['RH']=='OPEN'
    print('NF400 ORIGINAL COMPLETE SELECTED PROJECTION COMPLEMENT GATE PASS')
    print('Conditional: if ||(I-P_J) t_L|| <= 11/40000000000000,')
    print('then j*=P_J m(D)u4 has ||t_L-j*|| < 7/25000000000000.')
    print('No original J-perpendicular norm upper measured; W-ODD-NEG/RH OPEN.')

if __name__=='__main__':
    main()
