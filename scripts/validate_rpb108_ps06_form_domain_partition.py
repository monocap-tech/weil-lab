#!/usr/bin/env python3
"""PS06: original Weil spectral-form-domain Lipschitz partition.

The ORIGINAL full seven-prime, digamma difference-energy and both signed
poles are retained. Exact rational acceptance establishes
  C_* <18, I_L<9, 20-C_*>2, and graph-norm multiplier <30.
This is a domain theorem for the physical form, NOT a sharp support
projector theorem, orthogonal Schur split, 890-gate or RH proof.
"""
from fractions import Fraction as F
import json
from pathlib import Path
import validate_rpb108_rc315_low_mode_sign as old

ROOT=Path(__file__).resolve().parents[1]
B=F(11,10)
R=2*B
N=((2,2),(3,3),(4,2),(5,5),(7,7),(8,9))
# NOTE N must enumerate the actual seven prime powers independently.
ORIGINAL=((2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3))

def run():
    source=old.run()
    assert source["original_CC27_native_source_from_RC313"]
    assert source["reg_source_verified"]
    assert source["offdiagonal_P0_P1_exactly_zero_by_parity"]
    manifest=json.loads((ROOT/"research/obligations.json").read_text())
    lane=json.loads((ROOT/"research/parallel_investigations/w_physical_shift.json").read_text())
    assert manifest["active_obligation"]=="W-ODD-NEG"
    assert manifest["objective"]["status"]=="open"
    assert lane["id"]=="W-PHYSICAL-SHIFT"
    assert lane["active_frontier_unchanged"]=="W-ODD-NEG"
    assert all(value is False for value in lane["closures"].values())
    assert len(ORIGINAL)==7 and {n for n,p in ORIGINAL}=={2,3,4,5,7,8,9}

    log2=old.log_i(F(2))
    log5=old.log_i(F(5))
    log9=old.log_i(F(9))
    delta=old.IV(R-log9.hi,R-log9.lo)
    a=old.IV(log9.lo-B,log9.hi-B)
    assert F(1,400)<delta.lo<delta.hi<F(1,350)
    assert F(1)<a.lo<a.hi<B
    L_lo=2/delta.hi
    L_hi=2/delta.lo
    assert F(700)<L_lo<L_hi<F(800)

    pi=old.pi_iv()
    gamma=old.gamma_iv()
    arch_const=-gamma-pi/2-3*log2-old.log_i(pi)
    weights=[]
    for n,p in ORIGINAL:
        root=old.IV(2 if n==4 else 3) if n in (4,9) else old.sqrt_i(n)
        w=old.log_i(F(p))/root
        assert w.lo>0
        weights.append(w)
    sum_w=sum(weights,old.IV(0))
    sinh,cosh=old.sinh_cosh_iv(B/2)
    sinh_B=2*sinh*cosh
    assert sinh_B.lo>1 and sinh_B.hi<F(3,2)
    # Original signed seven-prime cos correlations and both poles
    # are norm-bounded in q, with the positivity of the even pole
    # retained when proving a LOWER bound.
    Cstar_hi=(-arch_const).hi+2*sum_w.hi+4*sinh_B.hi
    assert F(0)<Cstar_hi<F(18),(
        "full original signed q-vs-J envelope",float(Cstar_hi))

    # Exact Lipschitz cutoff χ: 0 for |x|<=a+δ/4,
    # 1 for |x|>=a+3δ/4, linear on width δ/2.
    # ψ=1-χ. Both globally Lipschitz, 0<=χ,ψ<=1.
    # L=2/δ, and 700<L<800.
    #
    # For 0<u<=1, k(u)<=1/(2u)+1;
    # for u>=1, k(u)<=2 exp(-u/2), whose total integral <=4.
    # Integral I_L <=.25+1/(3L)+.5log L+1-1/L+4
    #              <.5log800+21/4 <9.
    log800_hi=5*log2.hi+2*log5.hi
    assert log800_hi<F(7)
    I_hi=log800_hi/F(2)+F(21,4)
    assert F(0)<I_hi<F(9)

    # G=q+20 mass; G>=J+(20-Cstar) mass.
    # J[θf]<=2J[f]+2 I_L mass for each θ in {χ,ψ}.
    gap=F(20)-Cstar_hi
    assert gap>2
    upper_mult=2+(2*I_hi+20+Cstar_hi)/gap
    assert F(0)<upper_mult<F(30),(
        "PS06 original graph multiplier bound not certified",
        float(upper_mult))

    # The two collars overlap! For f=1_I, ∫χψ=δ/6.
    # For normalized original u0=1/sqrt(R),
    # <χu0,ψu0>=δ/(6R)>0: do not model these as orthogonal
    # edge/interior variables or insert PS05's DISJOINT B_EF.
    collar_overlap=old.IV(delta.lo/(6*R),delta.hi/(6*R))
    assert collar_overlap.lo>0
    assert collar_overlap.hi<F(1,1000)

    print("PS06 original log9 edge width interval",float(delta.lo),float(delta.hi),flush=True)
    print("PS06 exact cut-off Lipschitz L interval",float(L_lo),float(L_hi),flush=True)
    print("PS06 original seven-prime total mass upper",float(sum_w.hi),flush=True)
    print("PS06 full signed graph comparison Cstar upper",float(Cstar_hi),flush=True)
    print("PS06 kernel Lipschitz commutator integral upper",float(I_hi),flush=True)
    print("PS06 G=q+20 mass positive gap lower",float(gap),flush=True)
    print("PS06 each additive multiplier original G factor upper",float(upper_mult),flush=True)
    print("PS06 normalized P0 collar L2 overlap interval",
          float(collar_overlap.lo),float(collar_overlap.hi),flush=True)
    print("PS06 PASS SCOPED: χ and 1-χ preserve the exact original"
          " physical Weil logarithmic spectral form domain;"
          " both support-preserving additive multipliers are G-bounded"
          " by <30, with genuine nonorthogonal overlap constraint."
          " Sharp projector and complete CC27 D-Riesz bridge OPEN;"
          " no actual unconstrained edge Schur PSD, W-ODD-NEG,"
          " W-EVEN-FORM or RH.",flush=True)

if __name__=="__main__":
    run()
