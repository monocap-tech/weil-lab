#!/usr/bin/env python3
"""PS17 — actual original signed complementary low/high Feshbach proof gates.

Replay PS16→PS15→PS14→PS13→...→RC315 original seven-prime sources.
Certify rational sign-aware V_C, true source Schur response T_C,
positive J_C high block and all-high-interaction Feshbach norms.
This NEVER computes the real finite low D_LL eigenvalues, high inverse,
physical CC27 D-Riesz bridge, whole original Weil positivity or RH.
"""
from fractions import Fraction as F
from pathlib import Path
import json

import validate_rpb108_rc315_low_mode_sign as old
import validate_rpb108_ps16_schur_gap_calibration as ps16

ROOT=Path(__file__).resolve().parents[1]
B=F(11,10)
R=2*B
SOURCE=((2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3))

def run():
    # Full original source/CI replay. PS16 includes the actual original
    # sign-aware 13-source Schur with 24 Carleman seams and RC315 originals.
    ps16.run()
    gov=json.loads((ROOT/"research/obligations.json").read_text())
    lane=json.loads((ROOT/"research/parallel_investigations/w_physical_shift.json").read_text())
    assert gov["active_obligation"]=="W-ODD-NEG"
    assert gov["objective"]["status"]=="open"
    assert lane["id"]=="W-PHYSICAL-SHIFT"
    assert lane["active_frontier_unchanged"]=="W-ODD-NEG"
    assert lane["status"]=="open"
    assert all(value is False for value in lane["closures"].values())

    # Recompute true original sign-aware whole physical bounded operator:
    # V = carch I -2 sum w_n Re C(log n)
    #   +2|cosh(x/2)><cosh(x/2)|
    #   -2|sinh(x/2)><sinh(x/2)|.
    # The upper and lower poles cost DISTINCT true signed L2 masses.
    pi=old.pi_iv()
    ln2=old.log_i(F(2))
    carch=-old.gamma_iv()-pi/2-3*ln2-old.log_i(pi)
    weights=[]
    for n,base in SOURCE:
        root=old.IV(2 if n==4 else 3) if n in (4,9) else old.sqrt_i(n)
        w=old.log_i(F(base))/root
        assert w.lo>0
        weights.append(w)
    assert len(weights)==7
    mass=sum(weights,old.IV(0))
    sn,cs=old.sinh_cosh_iv(B/2)
    sinhB=2*sn*cs
    original_lower=carch.lo-2*mass.hi-2*(sinhB.hi-B)
    original_upper=carch.hi+2*mass.hi+2*(B+sinhB.hi)
    assert -F(13)<original_lower<-F(12)
    assert F(6)<original_upper<F(7)
    assert -original_lower>original_upper
    # P_C V P_C compresses unchanged original V: -13<V_C<7.
    # True source penalty T_C=B_PC* A_P^-1 B_PC has norm <869
    # by the checked original PS16 certificate.
    source_gap=F(323,1000)
    cross_bound=F(67,4)
    schur_penalty_bound=cross_bound**2/source_gap
    assert schur_penalty_bound==F(4489000,5168)
    assert schur_penalty_bound<F(869)
    bounded_signed_remainder=F(13)+F(869)
    assert bounded_signed_remainder==F(882)
    # Actual complement Schur S_C=J_C +M_C, M_C=V_C-T_C.
    # Spectral J_C low/high decomposition has no unbounded cross.
    # Thus all cross K_LH=L M_C R is bounded by 882, and the
    # high positive form D_HH>=Lambda-882 whenever Lambda>882.

    def validate_cutoff(exp, den):
        cutoff=F(2**exp)
        high_gap=cutoff-bounded_signed_remainder
        assert high_gap>0
        response=bounded_signed_remainder**2/high_gap
        assert response<F(1,den)
        # Full signed low/high correction is POSITIVE, subtracted:
        # 0<=K_LH D_HH^-1 K_HL <response I.
        # If independent REAL source matrix D_LL>=1/den I, then
        # its complete true Feshbach F= D_LL-C_hh is PSD.
        # That low-block margin is *not* checked here.
        return cutoff,high_gap,response

    cutoff26,gap26,response26=validate_cutoff(26,80)
    cutoff30,gap30,response30=validate_cutoff(30,1000)
    assert F(882)**2==F(777924)
    assert F(2**25)-F(882)>0
    assert bounded_signed_remainder**2/(F(2**25)-882)>F(1,80)
    assert response26>F(1,100)
    assert response30>F(1,2000)

    # Source-preserving reflection/parity: r<->9/r. Thus P and C,
    # both original operators Q and J, and bounded T_C commute with
    # reflection. The low spectral projector on J_C does too.
    labels={F(1),F(9)}|{F(n) for n in (2,3,4,5,7,8)}
    labels|={F(9,n) for n in (2,4,5,7,8)}
    assert len(labels)==13 and all(F(9)/x in labels for x in labels)

    # Pinned real RC315 even/odd upper Rayleigh ceilings.
    receipt=json.loads((ROOT/"certificates/rpb108_rc315_low_mode_sign.json").read_text())
    assert receipt["milestone"]=="RC315"
    assert receipt["original_source_pin"]==old.ORIGINAL_PIN
    assert receipt["original_CC27_native_source_from_RC313"]
    assert not receipt["RH"] and not receipt["signed_Schur_positive_certified"]
    diag=receipt["original_low_diagonals"]
    q0_upper=F(diag[0]["physically_normalized_original_Weil_diagonal_interval"][1])
    q1_upper=F(diag[1]["physically_normalized_original_Weil_diagonal_interval"][1])
    ell9=old.log_i(F(9))
    delta=old.IV(R-ell9.hi,R-ell9.lo)
    even_complement_mass=1-13*delta.hi/R
    odd_complement_mass=1-39*delta.hi/R
    assert F(0)<odd_complement_mass<even_complement_mass
    even_gap_upper=q0_upper/even_complement_mass
    odd_gap_upper=q1_upper/odd_complement_mass
    assert even_gap_upper<F(41,1000)
    assert odd_gap_upper<F(7,50)

    # These are CONDITIONAL low-block margins, NOT established by CI.
    # M_C norm <882, and J_C compact resolvent, imply finite-rank
    # low projection E_[0,Lambda). Mixed high block is eliminated
    # with the exact original D_HH inverse (uncomputed).
    # A TRUE numerical low eigenvalue lower >response would imply
    # Feshbach positivity; no such eigenvalue was evaluated here.
    # Full Q and low Feshbach negative inertia are equal analytically
    # by two successive domain-compatible completions of squares.
    assert response26<F(1,80)<even_gap_upper
    assert response30<F(1,1000)<even_gap_upper

    print("PS17 original signed whole physical V lower/upper",float(original_lower),float(original_upper),flush=True)
    print("PS17 true source response T_C crude norm upper",float(schur_penalty_bound),flush=True)
    print("PS17 entire ORIGINAL complementary bounded M_C norm upper",float(bounded_signed_remainder),flush=True)
    print("PS17 cutoff 2**26 high original Schur spectral gap at least",float(gap26),flush=True)
    print("PS17 cutoff 2**26 complete signed high-response error upper",float(response26),flush=True)
    print("PS17 cutoff 2**30 high original Schur spectral gap at least",float(gap30),flush=True)
    print("PS17 cutoff 2**30 complete signed high-response error upper",float(response30),flush=True)
    print("PS17 actual RC315 necessary even gap ceiling",float(even_gap_upper),flush=True)
    print("PS17 actual RC315 necessary odd gap ceiling",float(odd_gap_upper),flush=True)
    print("PS17 PASS SCOPED: exact original signed source/complement Schur"
          " reduces, using native restricted J_C spectral projection,"
          " to a TRUE finite low-energy Feshbach matrix, with rigorously"
          " POSITIVE and SUBTRACTED complete high response <1/80 at"
          " cutoff 2**26 and <1/1000 at cutoff 2**30."
          " LOW MATRIX NOT COMPUTED OR SIGN-CERTIFIED."
          " Native CC27 D-Riesz transfer, complete Weil positivity,"
          " W-ODD-NEG, W-EVEN-FORM and RH OPEN.",flush=True)

if __name__=="__main__":
    run()
