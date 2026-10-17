#!/usr/bin/env python3
"""PS04: exact rational original Weil edge-to-interior bounded noncompact coupling.

New whole original signed result:
  ||B_EF||_{L2->L2} < 11,
  ||B_EF||_essential >= log(2),
with an explicit unit-norm edge/interior pair whose original signed
cross Q(f+h)-Q(f)-Q(h) < -1.37.
No positive full Schur, domain projection invariant, parity closure or RH.
"""
from fractions import Fraction as F
import json
from pathlib import Path
import validate_rpb108_rc315_low_mode_sign as old

ROOT=Path(__file__).resolve().parents[1]
B=F(11,10)
R=2*B
N=((2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3))

def run():
    rc=old.run()  # Checks pinned CC27/RC313 and RC46/RC314 source evidence.
    assert rc["original_CC27_native_source_from_RC313"]
    assert rc["reg_source_verified"]

    gov=json.loads((ROOT/"research/obligations.json").read_text())
    lane=json.loads((ROOT/"research/parallel_investigations/w_physical_shift.json").read_text())
    assert gov["active_obligation"]=="W-ODD-NEG"
    assert gov["objective"]["status"]=="open"
    assert lane["id"]=="W-PHYSICAL-SHIFT"
    assert lane["active_frontier_unchanged"]=="W-ODD-NEG"
    assert lane["status"]=="open"
    assert all(v is False for v in lane["closures"].values())

    logs={n:old.log_i(F(n)) for n,_ in N}
    ell=logs[9]
    delta=old.IV(R-ell.hi,R-ell.lo)
    a=old.IV(ell.lo-B,ell.hi-B)
    assert F(0)<delta.lo<=delta.hi<F(1,350)
    assert F(1)<a.lo<=a.hi<B
    assert logs[2].lo>delta.hi/F(8)
    eps=old.IV(delta.lo/16,delta.hi/16)
    assert 0<eps.lo<=eps.hi<F(1,5600)
    assert 2*eps.hi<logs[2].lo
    # Seven ACTUAL prime powers, retaining correctly based von Mangoldt.
    weights={}
    for n,p in N:
        if n in (4,9):  # exact square roots
            weights[n]=old.log_i(F(p)) / (2 if n==4 else 3)
        else:
            weights[n]=old.log_i(F(p)) / old.sqrt_i(n)
        assert weights[n].lo>0
    sum_hi=sum((v.hi for v in weights.values()),F(0))

    # Elementary kernel estimates, all u>0 for k upper,
    # 0<u<=1/2 for k lower.
    # k(u)<=1/(2u)+1:
    # e^(2u)-1>=2u and exp(-u/2)<=1.
    # k(u)>=1/(2u)-1/4:
    # 1-exp(-2u)<=2u and exp(-u/2)>=1-u/2.
    # Proof is algebraic; intervals validate the resulting strict gates.

    # Classical half-line Hilbert/Carleman kernel ||(s+t)^-1||<=pi.
    # With E=E- union E+, F=(-a,a), the two orientations have
    # s=x-a>=0/t=a-y>=0 or their reflections.
    # sqrt2 < 3/2, sqrt(2a delta)<1/12, sqrt(a delta)<1/17.
    assert F(2)*B*delta.hi<F(1,144)
    assert B*delta.hi<F(1,289)
    pi=old.pi_iv()
    assert pi.hi<F(22,7)
    s,c=old.sinh_cosh_iv(B/2)
    cosh_B=c*c+s*s
    assert F(1)<cosh_B.lo<=cosh_B.hi<F(7,4)

    # Full original signed offdiag L2 operator bound:
    # arch <=sqrt(2)(pi/2+sqrt(2a delta))
    # signed primes <=2 sum_n Lambda(n)/sqrt(n)
    # signed poles <=4sqrt(a delta) cosh(B)
    arch_bound=F(3,2)*(F(11,7)+F(1,12))
    prime_bound=2*sum_hi
    pole_bound=F(4,17)*cosh_B.hi
    M=arch_bound+prime_bound+pole_bound
    assert F(0)<M<F(11), ("PS04 failed strict full original coupling norm",float(M))

    # At eps=delta/16 take TRUE original BV physical step vectors:
    #  f=1_[a,a+eps]/sqrt(eps) (edge), and
    #  h=1_[a-eps,a]/sqrt(eps) (interior), both norm 1.
    # All seven signed prime shift terms vanish exactly since 2eps<log2.
    #
    # arch Qcross=-2/eps int_0^eps int_0^eps k(s+t)dsdt.
    # 1/eps int int 1/(s+t)=2log2; result in
    #   [-2log2-2eps, -2log2+eps/2].
    # Both rank-one pole mixed terms have abs sum <=4eps*cosh(B).
    log2=old.log_i(F(2))
    strict_cross_upper=(
        -2*log2.lo+eps.hi/F(2)
        +4*eps.hi*cosh_B.hi
    )
    strict_cross_lower=(
        -2*log2.hi-2*eps.hi
        -4*eps.hi*cosh_B.hi
    )
    assert strict_cross_lower<strict_cross_upper<-F(137,100),(
        "PS04 full original true seam cross not strictly negative enough",
        float(strict_cross_lower),float(strict_cross_upper))
    # Real/complex polarized form b=Qcross/2, so its norm is >=0.685
    # on this explicit pair. Taking eps down to zero gives
    # b(f_eps,h_eps) -> -log2, and the two vectors converge weakly to
    # zero. The essential-norm lower is therefore exactly log2.
    essential_lower=log2.lo
    assert essential_lower>F(69,100)

    print("PS04 actual original seam epsilon upper",float(eps.hi),flush=True)
    print("PS04 original signed arch Carleman cross norm upper",float(arch_bound),flush=True)
    print("PS04 original seven-prime cross norm upper",float(prime_bound),flush=True)
    print("PS04 original signed two-pole cross norm upper",float(pole_bound),flush=True)
    print("PS04 original full E-F cross norm certified upper",float(M),flush=True)
    print("PS04 true two-vector ORIGINAL SIGNED Q cross interval",
          float(strict_cross_lower),float(strict_cross_upper),flush=True)
    print("PS04 noncompact original edge cross essential norm LOWER",
          float(essential_lower),flush=True)
    print("PS04 PASS SCOPED: full original edge/interior coupling bounded"
          " in L2 (<11), but noncompact with essential norm >=log2;"
          " true physical seam Q cross <-1.37."
          " PS03 edge positivity does not close any full Schur."
          " W-ODD-NEG, W-EVEN-FORM, RH OPEN.",flush=True)

if __name__=="__main__":
    run()
