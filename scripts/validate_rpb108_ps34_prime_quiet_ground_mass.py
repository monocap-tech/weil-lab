#!/usr/bin/env python3
"""PS34: TRUE original pole-free even Schur positive on a reflected
prime-quiet physical window and quantitative genuine ground mass OUTSIDE.

ANALYTIC original-source inputs awaiting independent proof review:
* PS18 complete 13-source original quiet geometry, Qlocal>133/500
  on any profile supported in Jquiet of length 1/16, original
  source/quiet arch HS <7/40, every genuine prime-source quiet
  coupling zero.
* PS27 A0>1997/9000, full original pole-free B0<1403/80,
  full original signed lower order V_C norm<13, true source-first
  original L=J_C+V0_C−B0* A0^-1 B0.
* PS29 actual even ground phi0 of L normalized, lambda0<-4.359740
  by RC315/PS27 original auxiliary negative constant witness.
* Four original new sharp E cut interfaces preserve the logarithmic
  form domain via bounded Carleman mixed terms (audit required).

NEW analytical implications on E=+/-[9/100,9/100+1/256]:
L_EE>1/5; ||L_{E,C\\E}||<31; mu(C+\\H)>81/3925.
All checks here are exact Fraction constants, source geometry and
a finite algebra test; not a numerical original eigenfunction, lambda1,
pole angle Delta, W-EVEN-FORM/W-ODD-NEG, original full Weil or RH.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import validate_rpb108_ps33_optimized_original_ground_pole_overlap as ps33
import validate_rpb108_ps18_spectral_rank_obstruction as ps18

ROOT=Path(__file__).resolve().parents[1]
B=F(11,10)
R=2*B
H_LO=F(9,100)
H_WIDTH=F(1,256)
H_HI=H_LO+H_WIDTH
E_MASS_LENGTH=2*H_WIDTH
QLO=F(269,5000)
QHI=F(1163,10000)
LAMBDA_ABS_LO=F(4359740,10**6)


def quiet_geometry_original():
    old=ps18.old
    assert QLO<=H_LO<H_HI<=QHI
    assert QHI-QLO==F(1,16)
    assert E_MASS_LENGTH==F(1,128)
    assert 2*H_HI<F(1,5)
    l2=old.log_i(F(2))
    assert F(1,5)<l2.lo
    labels={F(1),F(9)}|{F(n) for n in (2,3,4,5,7,8)}
    labels|={F(9,n) for n in (2,4,5,7,8)}
    assert len(labels)==13
    ln9=old.log_i(F(9))
    delta=old.IV(R-ln9.hi,R-ln9.lo)
    assert F(0)<delta.lo<=delta.hi<F(1,350)

    # PS18's original thirteen-source d_r source/quiet separation
    # checker, with ALL seven prime shifts, both signs.
    sources=sorted(labels)
    src_log={t:(old.IV(0) if t==1 else old.log_i(t)) for t in sources}
    shifts={n:old.log_i(F(n)) for n,_ in ps18.SOURCE}
    assert set(shifts)=={2,3,4,5,7,8,9}
    dmin=None
    for t in sources:
        src_start_lo=src_log[t].lo-B
        src_end_hi=src_log[t].hi-B+delta.hi
        d=max(QLO-src_end_hi,src_start_lo-QHI)
        assert d>0
        dmin=d if dmin is None else min(d,dmin)
        for n,shift in shifts.items():
            for sign in (-1,1):
                if sign==1:
                    shifted_lo=QLO+shift.lo
                    shifted_hi=QHI+shift.hi
                else:
                    shifted_lo=QLO-shift.hi
                    shifted_hi=QHI-shift.lo
                gap=max(src_start_lo-shifted_hi,
                        shifted_lo-src_end_hi)
                assert gap>F(1,20000),("source-quiet cross prime",t,n,sign)
    assert dmin>0

    # Directly replay original PS18 source cross HS uniform
    # per original 13 interval d_r formula; this allows **true
    # physical restriction** of the HS² to E by linear length.
    hs_full=F(0)
    for t in sources:
        src_lo=src_log[t].lo-B
        src_hi=src_log[t].hi-B+delta.hi
        d=max(QLO-src_hi,src_lo-QHI)
        assert d>0
        hs_full+=delta.hi*(QHI-QLO)*(1+F(1)/(2*d))**2
    assert hs_full<F(7,40)**2
    # Two reflected H strips; every original reflected source
    # interval has the same total uniform source-separation sum
    # by reflection. Ratio |E| / |Jquiet| =1/8.
    hs_E_sq=(E_MASS_LENGTH/(QHI-QLO))*hs_full
    qE=F(1,8)*F(7,40)**2
    assert hs_E_sq<qE
    return qE,hs_E_sq


def replay_original_PS18_local_Q_lower():
    # A strict inherited ORIGINAL signed Q lower on every function
    # supported in Jquiet, including all original seven prime and
    # two poles; use PS18's exact 32-factor rational arch estimate.
    old=ps18.old
    pi=old.pi_iv()
    ln2=old.log_i(F(2))
    assert pi.lo>3
    sn,cs=old.sinh_cosh_iv(B/2)
    carch=-old.gamma_iv()-pi/2-3*ln2-old.log_i(pi)
    tail32=F(0)
    for m in range(32):
        nu=F(4*m+1,2)
        x=nu*F(1,16)
        assert 0<x<32
        tail32+=2*(1-x/32)**32/nu
    original_Q_local_lower=carch.lo+tail32-2*F(1,16)*sn.hi**2
    assert original_Q_local_lower>F(133,500)
    return original_Q_local_lower


def original_polefree_even_local_margin(qE):
    # Original arch cross between +H and -H: separation >=9/50,
    # k(u)<=1/(2u)+1; true bound by HS/Schur integral length.
    min_dist=2*H_LO
    assert min_dist==F(9,50)
    arch_mirror_cross=H_WIDTH*(1+F(1)/(2*min_dist))
    assert arch_mirror_cross==F(17,1152)

    # Original +even pole cross and -odd pole cross are both
    # NONNEGATIVE when h- is mirror reflection of h+.
    # So sum of original full-pole local Q's minus arch cross
    # lower-bounds Q on E, before remove original even pole.
    # Q0=Q−2|<c,h>|²; true c norm on E use cosh(B/2)<7/6.
    even_pole_cost=2*E_MASS_LENGTH*F(7,6)**2
    assert even_pole_cost==F(49,2304)

    # True pre-pole source response A0^-1, B0 even only arch cross.
    source_penalty=qE/F(1997,9000)
    local_margin=(F(133,500)-arch_mirror_cross
                  -even_pole_cost-source_penalty)
    assert local_margin>F(1,5)
    return arch_mirror_cross,even_pole_cost,source_penalty,local_margin


def cross_bound_original(qE):
    # Four sharp original internal cut faces; Carleman norm pi
    # on each 1/(s+t), coefficient 1/2 => at most 2pi total.
    # The everywhere <=1 remainder has HS norm sqrt(|E|*|I|).
    hs_regular_sq=E_MASS_LENGTH*R
    assert hs_regular_sq==F(11,640)
    assert hs_regular_sq<F(1,7)**2

    # Full original signed V_C<13 includes positive even and
    # negative odd poles; removing even pole only changes by
    # -2|c_C><c_C|, norm <539/90.
    v0_upper=F(13)+F(539,90)
    assert v0_upper<F(19)

    # True source response bound with tiny E-to-source HS and
    # FULL original B0 on C\\E, not simply <1400.
    source_cross_squared=qE*(F(9000,1997)*F(1403,80))**2
    assert source_cross_squared<F(25)
    K_envelope=F(44,7)+F(1,7)+F(19)+F(5)
    assert K_envelope==F(213,7) and K_envelope<F(31)
    return hs_regular_sq,v0_upper,source_cross_squared,K_envelope


def toy_negative_eigen_ground_test():
    # Exact TWO-BLOCK arithmetic verifying the nonconcentration
    # eigen-test, no false original 2-dimensional eigenfunction.
    # L=[[1/4,-2],[-2,13/4]], ground eig (-3/4), phi~(2,1).
    L=[[F(1,4),F(-2)],[F(-2),F(13,4)]]
    phi=[F(2),F(1)]
    lam=F(-3,4)
    assert [sum((L[i][j]*phi[j] for j in range(2)),F(0))
            for i in range(2)]==[lam*v for v in phi]
    assert (L[0][0]-lam)*phi[0]==-L[0][1]*phi[1]
    assert F(1,4)-lam==F(1)
    assert phi[1]**2/sum((v*v for v in phi),F(0))==F(1,5)
    assert (F(1)/(F(2)**2+F(1)))==F(1,5)


def run():
    # Prior original source validation is always replayed; do not
    # invoke ancestor terminal-checkpoint validators as their
    # fail-closed PS33 assertion would reject valid PS34.
    ps33.ps32.ps31.ps30.ps29.ps28.run()
    assert all(v>0 for v in ps33.ps32.ps31.ps30.regression())
    T,M,jsym=ps33.ps32.exact_original_analytic_constants()
    assert T>0 and M>0 and jsym>0
    p24,p25,p26,overlap,optimized,improvement=ps33.optimize_dyadic(M)
    assert optimized>0 and improvement>1 and p25>p24
    gov=json.loads((ROOT/"research/obligations.json").read_text())
    lane=json.loads(
        (ROOT/"research/parallel_investigations/w_physical_shift.json").read_text())
    assert gov["active_obligation"]=="W-ODD-NEG"
    assert gov["objective"]["status"]=="open"
    assert gov["governance"]["no_automatic_promotion"] is True
    assert lane["id"]=="W-PHYSICAL-SHIFT"
    assert lane["active_frontier_unchanged"]=="W-ODD-NEG"
    assert lane["status"]=="open"
    assert lane["checkpoints"][-1]["id"]=="PS34"
    assert all(x is False for x in lane["closures"].values())

    qE,hs2=quiet_geometry_original()
    q_original=replay_original_PS18_local_Q_lower()
    mirror,pole,source,local=original_polefree_even_local_margin(qE)
    regular_sq,v0,source_cross_sq,K=cross_bound_original(qE)
    toy_negative_eigen_ground_test()

    # For normalized actual original L-ground:
    # local positive >1/5, lam0< -4.359740.
    # p=1_E phi0, z=1_(C\\E)phi0; (L_EE-lam0)p= -L_EQ z.
    # So ||p|| <(31/(1/5+|lam0|))||z|| <(62/9)||z||,
    # implying true z²>81/(3844+81)=81/3925.
    required=F(1,5)+F(4359740,10**6)
    assert required>F(9,2)
    Kcrude=F(31)
    assert K<Kcrude
    outside_mass=F(9,2)**2/(F(31)**2+F(9,2)**2)
    assert outside_mass==F(81,3925)
    assert outside_mass>F(1,50) # >2% genuine macroscopic
    assert 1-outside_mass==F(3844,3925)

    print("PS34 original thirteen-source mirror quiet H:",
          H_LO,H_HI,"width",H_WIDTH,flush=True)
    print("PS34 ORIGINAL per-source quiet arch HS² E strict upper",
          float(qE),"direct rational",float(hs2),flush=True)
    print("PS34 original Jquiet Q signed local lower",
          float(q_original),">133/500",flush=True)
    print("PS34 original even mirror arch cross upper",
          float(mirror),flush=True)
    print("PS34 removed true positive-even-pole cost upper",
          float(pole),flush=True)
    print("PS34 full A0^-1 source E correction upper",
          float(source),flush=True)
    print("PS34 ORIGINAL E-supported even pole-free Schur margin >",
          float(local),">1/5",flush=True)
    print("PS34 four-interface full original arch bounded cross regular HS²",
          float(regular_sq),flush=True)
    print("PS34 true original B0* A0^-1 B0 E-to-complement cross squared <",
          float(source_cross_sq),"<25",flush=True)
    print("PS34 true FULL original pole-free mixed cross <",
          float(K),"<31",flush=True)
    print("PS34 TRUE ORIGINAL ground-mass outside reflected physical H >",
          outside_mass,">2%",flush=True)
    print("PS34 PASS SCOPED: original mirrored prime-quiet"
          " pole-free EVEN local Schur >1/5, 4-interface actual arch"
          " Carleman plus signed 7-prime and full original source"
          " response cross <31, true normalized negative ground"
          " carries >81/3925 mass OUTSIDE physical H width 1/256."
          " No actual ground profile in individual cells, second"
          " eigenvalue lambda1, effective-pole Delta, odd/even"
          " global Weil positivity, native CC27 D-Riesz or RH."
          " Independent infinite-dimensional and sharp-cut audit"
          " remains necessary.",flush=True)


if __name__=="__main__":
    run()
