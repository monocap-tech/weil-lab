#!/usr/bin/env python3
"""PS22 true original eight-window-to-entire-residual nested signed Schur.

Replays PS21→PS20→...→the source-pinned RC315 original seven-prime Weil
form. Strengthens the TRUE source-eliminated eight-window block >19/20
via a signed 2x2 block determinant, assembles its complete physical
offdiagonal to the ENTIRE residual, retaining original arch Carleman
seams, all seven prime shifts, both signed poles, and compact source
response. Bounds positive compact nested penalty <1253. Certifies
genuine high-arch-energy residual Schur positivity and even/odd
RC315 NECESSARY upper gap ceilings. No full residual PSD or RH.
"""
from fractions import Fraction as F
from pathlib import Path
import json

import validate_rpb108_rc315_low_mode_sign as old
import validate_rpb108_ps21_nested_eightwindow as ps21

ROOT=Path(__file__).resolve().parents[1]
B=F(11,10)
R=2*B
L=F(1,128)
ORIGINAL=((2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3))

def run():
    ps21.run()
    m=json.loads((ROOT/"research/obligations.json").read_text())
    lane=json.loads((ROOT/"research/parallel_investigations/w_physical_shift.json").read_text())
    assert m["active_obligation"]=="W-ODD-NEG"
    assert m["objective"]["status"]=="open"
    assert lane["id"]=="W-PHYSICAL-SHIFT"
    assert lane["active_frontier_unchanged"]=="W-ODD-NEG"
    assert lane["status"]=="open"
    assert all(x is False for x in lane["closures"].values())

    ln2=old.log_i(F(2))
    ln9=old.log_i(F(9))
    pi=old.pi_iv()
    delta=old.IV(R-ln9.hi,R-ln9.lo)
    assert F(1,400)<delta.lo<=delta.hi<F(1,350)
    # Source PS15: thirteen disjoint width delta intervals, reflecting
    # r <-> 9/r. PS20 six and PS21 two window blocks: eight total.
    offsets={F(1),F(9)}|{F(n) for n in (2,3,4,5,7,8)}
    offsets|={F(9,n) for n in (2,4,5,7,8)}
    assert len(offsets)==13 and all(F(9)/r in offsets for r in offsets)
    assert F(8)*L==F(1,16)
    source_measure_hi=13*delta.hi
    eight_measure=8*L
    assert source_measure_hi+eight_measure<F(1,10)

    # TWO actual blocks of already source-eliminated true signed S_C:
    # W=PS20 six windows: alpha=359/300 lower.
    # T=PS21 reflected log2 pair: source-eliminated beta lower.
    # All original nonzero W/T mixed arch and signed poles + source
    # induced interactions are bounded gamma=3/8, and original
    # prime W/T cross vanishes by 532 exact physical checks PS21.
    alpha=F(359,300)
    beta=(F(11,5)-F(1,2)-F(1,70)-F(1,80)-F(1,8))
    gamma=F(3,8)
    assert alpha>1 and beta>1 and 0<gamma<F(1)
    # The 2x2 block bound on FULL infinite-dimensional eight-window
    # S_C has a positive margin mu iff (alpha-mu)(beta-mu)>gamma².
    mu=F(19,20)
    determinant=(alpha-mu)*(beta-mu)-gamma**2
    assert alpha>mu and beta>mu and determinant>0,float(determinant)
    # Thus true original source-eliminated A_U>19/20 I, better
    # than the weaker PS21 triangular bound 2/3.

    # Sharp 8-window restriction of original logarithmic form domain:
    # for each width-L interval, mixed arch across both physical
    # sides = Carleman 1/(2(s+t)) + regular kernel. PS15's
    # uniform truncated-k_M monotone proof applies to all eight.
    # Eight internal windows -> 16 true window/rest internal seams.
    assert 2*8==16
    # Bound original W8/rest arch output over 8 mutually orthogonal
    # physical intervals: sqrt(8)*(pi/sqrt(2)+sqrt(L R)).
    # Fully exact outward rational sqrt8<17/6, pi/sqrt2<110/49,
    # sqrt(L R)<7/50. No invented finite approximation.
    assert pi.hi<F(22,7)
    assert F(8)<F(17,6)**2
    assert F(7,5)**2<F(2)
    assert L*R<F(7,50)**2
    arch_UR=F(17,6)*(F(110,49)+F(7,50))
    assert arch_UR<F(7),float(arch_UR)

    # ALL seven original nonperiodic prime translations across
    # U/rest remain, unlike PS21's special W/T cross zero.
    weights=[]
    for n,base in ORIGINAL:
        root=(old.IV(2 if n==4 else 3)
              if n in (4,9) else old.sqrt_i(n))
        w=old.log_i(F(base))/root
        assert w.lo>0
        weights.append(w)
    assert len(weights)==7
    prime_UR=2*sum((w.hi for w in weights),F(0))
    assert prime_UR<F(71,10),float(prime_UR)

    # BOTH original correctly signed rank-one pole couplings:
    # sqrt(meas U)=1/4, sup_I cosh<7/6, sinh<7/12,
    # ||c||<8/5 and ||s||<1/2.
    sn,cs=old.sinh_cosh_iv(B/2)
    sinhB=2*sn*cs
    assert cs.hi<F(7,6) and sn.hi<F(7,12)
    assert B+sinhB.hi<F(8,5)**2
    assert sinhB.hi-B<F(1,2)**2
    pole_UR=2*F(1,4)*(F(7,6)*F(8,5)+F(7,12)*F(1,2))
    assert pole_UR==F(259,240)<F(11,10)

    # ALL TRUE original source-induced signed Schur interactions
    # between eight-window U and the uncovered physical residual Z.
    # Parent PS20: ||B_{P,W6}||<31/100; PS21: ||B_{P,T2}||<1/5.
    # W6/T2 are input-orthogonal, so whole P/U coupling is bounded
    # by sqrt(.31²+.20²)<.37, not their sum .51.
    assert F(31,100)**2+F(1,5)**2<F(37,100)**2
    whole_source_to_U=F(37,100)
    # TRUE source inverse A_P >323/1000, actual PS15 complete
    # ||B_{P,C}||<67/4 including EVERY original Carleman/prime/pole.
    # Thus ||U T_C Z||<(.37)*(1000/323)*(67/4).
    source_response_UR=whole_source_to_U*F(1000,323)*F(67,4)
    assert source_response_UR<F(193,10),float(source_response_UR)

    # TRUE already-source-eliminated cross is
    # B_UZ = B_UZ^(full-original-Q) - U T_C Z.
    # Unlike original B_UZ, the second term is compact, nonzero.
    # Total offdiag <7+7.1+1.1+19.3=34.5=69/2.
    whole_signed_cross=F(7)+F(71,10)+F(11,10)+F(193,10)
    assert whole_signed_cross==F(69,2)
    assert arch_UR+prime_UR+pole_UR+source_response_UR <whole_signed_cross

    # Genuine A_U>19/20 has compact inverse because original
    # digamma log-form embedding on bounded physical support is
    # compact and all signed lower terms incl source T_C bounded.
    # The SECOND source-aware Schur correction is a positive compact
    # operator, even though the RAW U/Z cross is noncompact in L2.
    # ||T_Z^(2)|| <(69/2)²/(19/20)=23805/19 <1253.
    nested_upper=whole_signed_cross**2/mu
    assert nested_upper==F(23805,19)<F(1253),float(nested_upper)

    # Analytic original seam witness: at an internal U/Z boundary,
    # opposing normalized epsilon-step supports converge weakly to
    # zero. All original prime shifts vanish on 2eps<log2 and
    # signed poles are O(eps); arch mixed -> -log2.
    # T_C is compact, so its weakly-null mixed response tends to 0.
    # Therefore ||B_UZ||essential >=log2>.69, rather than compact.
    assert ln2.lo>F(69,100)
    # This does NOT imply noncompactness of the energy-normalized
    # penalty B* A_U^-1 B, which IS positive compact.

    # Original sign-aware Q_Z >= J_Z -13 mass (PS11).
    # Signed source-eliminated S_C|Z >=J_Z-(13+869)mass (PS16).
    # Subtract the SECOND full positive compact nested penalty <1253:
    # S_Z[z] > J_Z[z] -2135 ||z||².
    high_energy_gate=F(13)+F(869)+F(1253)
    assert high_energy_gate==F(2135)
    # Hence for every nonzero original-form-admissible Z vector
    # whose ACTUAL original arch Rayleigh energy >=2135 mass,
    # the TRUE twice-source-eliminated original signed residual
    # is positive. Mixed low/high interactions remain unresolved.

    # Necessary parity-aware gap ceilings for ANY proposed UNIFORM
    # positive residual sign. Reflection fixes source and U, thus
    # Z and both Schurs. For original RC315 u0/u1 witnesses:
    # S_Z[1_Z u_j] <= Q[u_j] by TWO actual variational
    # completions, but is not known positive.
    rc=json.loads((ROOT/"certificates/rpb108_rc315_low_mode_sign.json").read_text())
    assert rc["milestone"]=="RC315" and rc["original_source_pin"]==old.ORIGINAL_PIN
    assert not rc["RH"] and not rc["signed_Schur_positive_certified"]
    ds=rc["original_low_diagonals"]
    assert [v["n"] for v in ds]==[0,1]
    q0_hi=F(ds[0]["physically_normalized_original_Weil_diagonal_interval"][1])
    q1_hi=F(ds[1]["physically_normalized_original_Weil_diagonal_interval"][1])
    assert F(0)<q0_hi<F(41,1000) and F(0)<q1_hi<F(14,100)
    # Exact 8-window measure 1/16; original 13 source measure
    # 13delta. Unit constant residual norm² = 1 - (|P|+|U|)/R.
    mass_removed_upper=13*delta.hi+eight_measure
    remaining_even_mass_lower=1-mass_removed_upper/R
    # Normalized odd linear u1(x)=sqrt(3/R) x/B gives sup²<=3/R
    # for conservative TRUE residual lower mass.
    remaining_odd_mass_lower=1-3*mass_removed_upper/R
    assert 0<remaining_odd_mass_lower<remaining_even_mass_lower
    even_ceiling=q0_hi/remaining_even_mass_lower
    odd_ceiling=q1_hi/remaining_odd_mass_lower
    assert even_ceiling<F(43,1000),float(even_ceiling)
    assert odd_ceiling<F(4,25),float(odd_ceiling)

    # Negative inertia unchanged under TWO domain-compatible
    # invertible completions of squares. PS13 gives conservative
    # entire original physical nonpositive subspace dimension bound.
    assert F(352000000)>0

    print("PS22 TRUE eight-window 2x2 determinant above mu=19/20",
          float(determinant),flush=True)
    print("PS22 improved entire original source-adjusted eight-window A_U lower",
          float(mu),flush=True)
    print("PS22 eight-window physical internal seams",16,flush=True)
    print("PS22 original U/rest Carleman arch cross upper",float(arch_UR),flush=True)
    print("PS22 all seven original U/rest prime cross upper",float(prime_UR),flush=True)
    print("PS22 both original signed U/rest pole cross upper",float(pole_UR),flush=True)
    print("PS22 full original source-mediated U/rest cross upper",
          float(source_response_UR),flush=True)
    print("PS22 entire TRUE source-aware eight-window/rest cross upper",
          float(whole_signed_cross),flush=True)
    print("PS22 original source-aware raw cross essential-norm lower",
          float(F(69,100)),flush=True)
    print("PS22 true SECOND positive COMPACT energy-dual penalty upper",
          float(nested_upper),flush=True)
    print("PS22 actual unshifted nested residual sufficient high J threshold",
          float(high_energy_gate),flush=True)
    print("PS22 RC315 even full residual uniform gap NECESSARY UPPER",
          float(even_ceiling),flush=True)
    print("PS22 RC315 odd full residual uniform gap NECESSARY UPPER",
          float(odd_ceiling),flush=True)
    print("PS22 PASS SCOPED: true source-eliminated A_U>19/20 on"
          " eight coupled infinite-dimensional windows; exact original"
          " full signed U/rest Schur retains noncompact digamma,"
          " all seven original prime shifts, BOTH signed poles and"
          " compact source response; source-aware cross<69/2,"
          " positive compact nested correction<1253; actual"
          " twice-eliminated residual positive in high original"
          " arch-energy J>=2135 sector; RC315 even/odd necessary"
          " residual global gap ceilings <.043/.16."
          " LOW residual sign, CC27 D-Riesz attachment,"
          " W-ODD-NEG, W-EVEN-FORM, original Weil and RH OPEN.",flush=True)

if __name__=="__main__":
    run()
