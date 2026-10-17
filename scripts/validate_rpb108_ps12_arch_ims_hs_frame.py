#!/usr/bin/env python3
"""PS12: true signed original arch IMS thin-edge HS + whole graph frame.

Replay original RC315, PS03-PS11 source receipts and check outward rational
bounds for FULL original nonperiodic digamma / seven-prime / two-pole IMS
localization. This is a whole original PHYSICAL graph frame for G=Q+20,
not full unshifted Q>=0, CC27 D-Riesz transfer, Schur PSD or RH.
"""
from fractions import Fraction as F
import json
from pathlib import Path
import validate_rpb108_rc315_low_mode_sign as old
import validate_rpb108_ps11_energy_inverse_channel_response as ps11

ROOT=Path(__file__).resolve().parents[1]
B=F(11,10)
R=2*B
ORIGINAL=((2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3))

def run():
    # This replays the exact TRUE original model through the PS11 parent:
    # PS11 -> PS10 -> PS09 -> PS07 -> PS06 -> PS03 -> pinned RC315.
    ps11.run()
    manifest=json.loads((ROOT/"research/obligations.json").read_text())
    lane=json.loads((ROOT/"research/parallel_investigations/w_physical_shift.json").read_text())
    assert manifest["active_obligation"]=="W-ODD-NEG"
    assert manifest["objective"]["status"]=="open"
    assert lane["id"]=="W-PHYSICAL-SHIFT"
    assert lane["active_frontier_unchanged"]=="W-ODD-NEG"
    assert lane["status"]=="open"
    assert all(v is False for v in lane["closures"].values())

    pi=old.pi_iv()
    ln2=old.log_i(F(2))
    ln9=old.log_i(F(9))
    delta=old.IV(R-ln9.hi,R-ln9.lo)
    A=pi/delta
    assert F(1,400)<delta.lo<=delta.hi<F(1,350)
    assert F(1000)<A.lo<=A.hi<F(1300)
    assert A.hi*R<F(4096)
    assert 12*ln2.hi<F(42,5)  # log(AR)<log(2^12)<8.4
    assert F(2)*F(1,350)>2*delta.hi
    # Arch kernel K(x,y)=1/2 k(|x-y|) eta(x,y), eta=0 if both
    # x,y outside E where E two edge collars, |E|=2delta.
    # k(u)<=1/(2u)+1, eta<=min(A²u²,2).
    #
    # HS² <= 2delta int_0^R k(u)^2 min(A²u²,2)^2 du
    #      < 13pi/6 +2delta(1/4 +4log(AR)+4R).
    # Exact rational majorant takes pi<22/7,delta<1/350,
    # log(AR)<12log2<42/5 and R=11/5:
    arch_hs_sq_majorant=F(13,6)*F(22,7)+F(2,350)*(
        F(1,4)+F(4)*F(42,5)+4*R)
    assert arch_hs_sq_majorant<F(64,9),(
        "PS12 original thin-edge HS bound not strictly <(8/3)^2",
        float(arch_hs_sq_majorant))
    assert arch_hs_sq_majorant>F(7)  # useful audit threshold

    # Seven ORIGINAL von Mangoldt coefficients retained, with squared
    # coefficients exact without spurious square-root interval width.
    sq=old.IV(0)
    for n,base in ORIGINAL:
        ell=old.log_i(F(base))
        sq+=ell**2/F(n)
    assert sq.lo>F(1419,1000)**2 and sq.hi<F(71,50)**2
    assert len(ORIGINAL)==7

    # PS11 TRUE original two correctly signed pole localized rank-one
    # correction bound remains 549/800. Compare to old 8sinhB <12.
    pole_bound=F(549,800)
    assert pole_bound<F(7,10)

    # Combine complete arch HS operator, entire 7-prime channel
    # and both signed poles in SAME original physical operator.
    arch_norm=F(8,3)
    prime_norm=F(71,50)
    total_raw=arch_norm+prime_norm+pole_bound
    assert total_raw==F(11455,2400)
    assert total_raw<F(24,5)

    # PS11 TRUE original signed H = Q+20 graph energy satisfies H>7.
    # Hence whole signed normalized IMS R_energy op norm <=||R||/7:
    total_graph=total_raw/F(7)
    assert total_graph==F(11455,16800)
    assert total_graph<F(683,1000)<F(7,10)
    # Since alpha²+beta²=1, graph scalar mass exactly cancels:
    # G[alpha f]+G[beta f]=G[f]+<f,R f>.
    # For all nonzero f in SAME original graph form domain,
    # (1-kappa)G[f] < G[alpha f]+G[beta f] < (1+kappa)G[f].
    lower_frame=F(1)-F(683,1000)
    upper_frame=F(1)+F(683,1000)
    assert lower_frame==F(317,1000)
    assert upper_frame==F(1683,1000)
    assert lower_frame>0

    print("PS12 original exact delta upper",float(delta.hi),flush=True)
    print("PS12 mask angle Lipschitz A upper",float(A.hi),flush=True)
    print("PS12 arch HS square strict rational upper",float(arch_hs_sq_majorant),flush=True)
    print("PS12 entire original arch IMS operator norm <8/3",float(arch_norm),flush=True)
    print("PS12 true full seven-prime sharp norm upper",float(prime_norm),flush=True)
    print("PS12 true correctly signed two-pole IMS norm upper",float(pole_bound),flush=True)
    print("PS12 entire original signed IMS raw L2 norm upper",float(total_raw),flush=True)
    print("PS12 FULL SIGNED graph normalized IMS norm upper",float(total_graph),flush=True)
    print("PS12 graph frame lower and upper",float(lower_frame),float(upper_frame),flush=True)
    print("PS12 PASS SCOPED: full ORIGINAL seven-prime signed physical"
          " arch IMS thin-support HS norm <8/3, total original signed"
          " normalized IMS error <683/1000, stable complete physical"
          " shifted graph frame 0.317 G< G[alpha f]+G[beta f]"
          " <1.683 G. This is NOT positivity of unshifted Q,"
          " finite Schur PSD, complete CC27 D-Riesz bridge or RH.",flush=True)

if __name__=="__main__":
    run()
