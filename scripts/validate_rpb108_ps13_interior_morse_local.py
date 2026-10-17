#!/usr/bin/env python3
"""PS13 scoped source-rational form analysis."""

from fractions import Fraction as F
from pathlib import Path
import json
import validate_rpb108_rc315_low_mode_sign as old
import validate_rpb108_ps12_arch_ims_hs_frame as ps12

ROOT=Path(__file__).resolve().parents[1]
B=F(11,10)
R=2*B
ORIGINAL=((2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3))

def run():
    ps12.run()
    m=json.loads((ROOT/"research/obligations.json").read_text())
    p=json.loads((ROOT/"research/parallel_investigations/w_physical_shift.json").read_text())
    assert m["active_obligation"]=="W-ODD-NEG"
    assert m["objective"]["status"]=="open"
    assert p["id"]=="W-PHYSICAL-SHIFT" and p["status"]=="open"
    assert p["active_frontier_unchanged"]=="W-ODD-NEG"
    assert all(not x for x in p["closures"].values())

    pi=old.pi_iv()
    gamma=old.gamma_iv()
    ln2=old.log_i(F(2))
    arch_c=-gamma-pi/2-3*ln2-old.log_i(pi)
    assert -F(6)<arch_c.lo<=arch_c.hi<-F(5)
    si,co=old.sinh_cosh_iv(B/2)
    L=F(1,16)
    assert 0<L<ln2.lo and len(ORIGINAL)==7
    for n,base in ORIGINAL:
        assert old.log_i(F(n)).lo>L
