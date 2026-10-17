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

    # All seven prime correlations vanish on support diameter <=1/16.
    # True digamma k(u)=sum exp(-(2k+1/2)*u). Integrate u>=L,
    # lower bound exponential by (1-x/32)**32, entirely rational.
    T=F(0)
    for k in range(32):
        a=F(4*k+1,2)
        x=a*L
        assert 0<x<32
        T+=2*(1-x/32)**32/a
    assert T>F(568035,100000)
    # Correct original pole signs: +2|<f,c>|² is safely dropped;
    # -2|<f,s>|² >= -2*L*sinh(B/2)²*||f||².
    q_local=arch_c.lo+T-2*L*si.hi**2
    assert q_local>F(1,4),float(q_local)

    # Original sign-aware bound Q>=J-13||f||² is inherited from PS11.
    # For |xi|>=Lambda=2**22, j(xi)>21 log(2)-1/pi-1/2.
    # Log and pi rational source enclosures prove the strict gate.
    assert ln2.lo>F(693,1000) and pi.lo>F(3)
    Lambda=2**22
    spectral_floor=21*F(693,1000)-F(1,3)-F(1,2)
    assert spectral_floor==F(41159,3000)
    assert spectral_floor>F(13)
    true_floor=21*ln2.lo-F(1)/pi.lo-F(1,2)
    assert true_floor>spectral_floor
    mass_floor=1-F(13)/spectral_floor
    assert F(0)<mass_floor<F(1)
    # Any L2-orthonormal family in a nonpositive linear subspace V
    # has >=mass_floor low-band mass per vector by the original arch
    # Fourier tail. Bessel gives sum low-band <=2 Lambda |I|.
    index_upper=2*Lambda*R/mass_floor
    assert index_upper<F(352_000_000)
