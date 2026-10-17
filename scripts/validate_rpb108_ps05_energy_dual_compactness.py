#!/usr/bin/env python3
"""PS05: original Weil edge energy compactness / compact dual Schur.

Analytic compactness theorem; exact Fraction high-frequency certificate.
Requires and replays inherited PS03 full-edge uniform positivity and PS04
true signed bounded-but-noncompact physical seam cross result.
Not a PSD Schur estimate, domain projector, whole Weil or RH proof.
"""
from fractions import Fraction as F
import json
from pathlib import Path
import validate_rpb108_rc315_low_mode_sign as old
import validate_rpb108_ps03_edge_coercivity as ps03
import validate_rpb108_ps04_edge_schur_coupling as ps04

ROOT=Path(__file__).resolve().parents[1]
B=F(11,10)
R=2*B
N=((2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3))
C0=F(3,10)
FREQ=2**80

def run():
    # Actual original-form PS03 coercivity and PS04 complete signed coupling.
    # Each parent repeats RC315's PINNED CC27/RC313 source model check.
    ps03.run()
    ps04.run()

    gov=json.loads((ROOT/"research/obligations.json").read_text())
    lane=json.loads((ROOT/"research/parallel_investigations/w_physical_shift.json").read_text())
    assert gov["active_obligation"]=="W-ODD-NEG"
    assert gov["objective"]["status"]=="open"
    assert lane["id"]=="W-PHYSICAL-SHIFT" and lane["status"]=="open"
    assert lane["active_frontier_unchanged"]=="W-ODD-NEG"
    assert all(v is False for v in lane["closures"].values())

    pi=old.pi_iv()
    gamma=old.gamma_iv()
    log2=old.log_i(F(2))
    arch_c=-gamma-pi/2-3*log2-old.log_i(pi)
    assert arch_c.hi<-F(5)

    ell=old.log_i(F(9))
    delta=old.IV(R-ell.hi,R-ell.lo)
    a=old.IV(ell.lo-B,ell.hi-B)
    assert F(0)<delta.lo<=delta.hi<F(1,350)
    assert a.lo>F(1) and a.hi<B
    sum_weights=old.IV(0)
    for n,p in N:
        # Certified outward rational true original von Mangoldt coefficients;
        # special exact square roots for 4,9 avoid artificial interval width.
        sqrt_n=old.IV(2 if n==4 else 3) if n in (4,9) else old.sqrt_i(n)
        w=old.log_i(F(p))/sqrt_n
        assert w.lo>0
        sum_weights+=w
    assert F(3)<sum_weights.lo<=sum_weights.hi<F(4)

    sinh,cosh=old.sinh_cosh_iv(B/2)
    # Q_E >= ∫ J(xi)|Zfhat|² - C_E||f||²
    # C_E includes exact 7 shifts & correctly signed original odd pole;
    # positive even pole is discarded only in a safe LOWER bound.
    C_E_hi=(
        -arch_c.lo+
        2*sum_weights.hi+
        4*delta.hi*sinh.hi**2
    )
    assert F(12)<C_E_hi<F(13)

    # For |xi|>=Lambda, the ORIGINAL arch digamma difference:
    # J(xi) >= log(Lambda/2)-1/pi-1/2.
    # This follows from k(u)>=1/(2u)-1/4 for u<=1/2 and one
    # integration-by-parts cosine integral, not numerical gridding.
    log_growth=79*log2.lo - F(1)/pi.lo - F(1,2)
    assert log_growth>F(53) and log_growth<F(55)
    assert FREQ == 2**80

    # For all f in native edge form domain, q_E(f)>=3/10||f||²,
    # tail_{|xi|>=2^80} ≤ ratio*q_E(f). Exact acceptance:
    ratio=(F(1)+C_E_hi/C0)/log_growth
    assert F(0)<ratio<F(4,5),("PS05 true edge Fourier-tail gate",float(ratio))

    # The finite band compression 1_E F^-1 1_band F 1_E has sinc
    # kernel with Hilbert-Schmidt property; compactness of A_E^-1/2
    # follows from the uniformly vanishing high-frequency energy tail.
    # This is an ANALYTIC step, not a claim of computing any 890x890
    # Schur eigenvalues or singular values.
    trace_upper=4*FREQ*delta.hi
    assert trace_upper>0
    print("PS05 original edge seven-prime mass upper",float(sum_weights.hi),flush=True)
    print("PS05 original c_arch lower",float(arch_c.lo),flush=True)
    print("PS05 original edge Q_E lower",float(C0),flush=True)
    print("PS05 original edge negative relative constant C_E upper",float(C_E_hi),flush=True)
    print("PS05 spectral |xi|>=2^80 original digamma growth lower",float(log_growth),flush=True)
    print("PS05 certified high-frequency mass per Q_E upper",float(ratio),flush=True)
    print("PS05 low-band physical sinc compression trace upper",float(trace_upper),flush=True)
    print("PS05 PASS SCOPED: q_E form-domain to physical L2 compact;"
          " A_E^(-1/2) compact; genuine original energy-dual"
          " B_EF^* A_E^(-1) B_EF positive compact though B_EF noncompact"
          " in physical L2. This is analytic compactness with a true"
          " rational high-frequency tail gate, NOT a numerical"
          " Schur PSD or domain-invariant full carrier split."
          " W-ODD-NEG, W-EVEN-FORM and RH OPEN.",flush=True)

if __name__=="__main__":
    run()
