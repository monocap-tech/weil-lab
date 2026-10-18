#!/usr/bin/env python3
"""PS33: actual original ground/effective even-pole overlap, dyadic optimized.

NEW exact-rational quantitative result, CONDITIONAL on inherited original
functional-analysis proofs, NOT on toy eigenfunctions:
 Original PS32 bound J[phi0] < M = T-4.359740 < 1401; original
 digamma symbol j(xi) > (e-1)*693/1000-5/6 on |xi|>=2**e.
 Nonnegative original even ground, original PS28 d>=1 imply
 <d,phi0>² > (1-M/s_e)/2**(e+1), for s_e > M.
 Exactly e=2025 maximizes this particular dyadic lower for integer
 e, improving PS32 e=8096 by >2**6071/1000.
 No original spectral gap, Delta, restored W-EVEN-FORM, odd, Weil, RH.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import validate_rpb108_ps32_original_ground_fourier_mass as ps32

ROOT=Path(__file__).resolve().parents[1]
LOG2_LO=F(693,1000)
PI_SUB=F(5,6)
P_LO=F(3,4000)
OPT_E=2025


def s(e):
    assert isinstance(e,int) and e>=2
    return F(e-1)*LOG2_LO-PI_SUB


def p(e,original_energy_upper):
    assert s(e)>original_energy_upper
    return F(1)-original_energy_upper/s(e)


def optimize_dyadic(original_energy_upper):
    M=original_energy_upper
    assert F(0)<M<F(1401)
    assert s(2023)<=M<s(2024)
    p24=p(2024,M)
    p25=p(2025,M)
    p26=p(2026,M)
    assert F(0)<p24<p25<p26<F(1)
    assert p25>2*p24
    assert p26<2*p25
    # For e>=2025, exact difference:
    #   p(e+1)-p(e)=M*log2lo/(s(e)*s(e+1)),
    # so positive increments STRICTLY decrease in e. Since
    # p26-p25 < p25 and p(e)>=p25, for every integer e>=2025,
    # p(e+1)<2p(e). Thus p(e)/2**(e+1) decreases.
    assert p26-p25==M*LOG2_LO/(s(2025)*s(2026))
    assert p26-p25<p25
    for e in range(2025,2040):
        assert p(e+1,M)-p(e,M)==M*LOG2_LO/(s(e)*s(e+1))
        assert p(e+1,M)<2*p(e,M)
    # No e <= 2023 is admissible (s_e<=M);
    # 2024 has strictly smaller objective than 2025.
    assert p25/F(2)**(2026)>p24/F(2)**2025
    assert p25>P_LO
    overlap=p25/F(2)**2026
    overlap_simple=P_LO/F(2)**2026
    assert overlap>overlap_simple==F(3,8000*2**2025)
    old_overlap=F(3,8*2**8096)
    assert overlap_simple>old_overlap
    # Exact multiplicative improvement guarantee:
    #  (3/(8000*2**2025))/(3/(8*2**8096))
    #    = 2**6071/1000. Avoid enormous decimal output.
    improvement=overlap_simple/old_overlap
    assert improvement==F(2**6071,1000)
    assert improvement>1
    return p24,p25,p26,overlap,overlap_simple,improvement


def run():
    # Inherited true-source exact rational arithmetic without rerunning
    # earlier checkpoint-terminal assertions on this descendant.
    ps32.ps31.ps30.ps29.ps28.run()
    ps32.ps31.ps30.regression()
    ps32.ps31.even_reflection_demo()
    # This invokes original-operator source bounds, and PS18's true
    # Fourier lower at older concentration cutoff as regression.
    T,M,jold=ps32.exact_original_analytic_constants()
    assert M==T-F(4359740,10**6)
    assert M<F(1401)
    assert ps32.X_EXP==8096
    assert jold>F(5604)
    assert F(3994,2907)==ps32.ALPHA_LO
    p24,p25,p26,overlap,simple,improvement=optimize_dyadic(M)

    gov=json.loads((ROOT/"research/obligations.json").read_text())
    lane=json.loads((ROOT/"research/parallel_investigations/w_physical_shift.json").read_text())
    assert gov["active_obligation"]=="W-ODD-NEG"
    assert gov["objective"]["status"]=="open"
    assert gov["governance"]["no_automatic_promotion"] is True
    assert lane["id"]=="W-PHYSICAL-SHIFT"
    assert lane["active_frontier_unchanged"]=="W-ODD-NEG"
    assert lane["status"]=="open"
    assert lane["checkpoints"][-1]["id"]=="PS33"
    assert all(v is False for v in lane["closures"].values())

    # Distinguish the new *overlap* cutoff (tiny low Fourier mass)
    # from the previous valid *physical nonconcentration* cutoff.
    assert p25<F(1,100)  # 0.00075; definitely not 75%.
    assert F(1)-p25>F(99,100)
    # TRUE original ground qualitative d>=1 and phi0>=0 imply
    #   a² > overlap > simple; never assert pole angle Delta.
    alpha=ps32.ALPHA_LO
    alpha_bound=alpha*simple
    assert alpha_bound>simple>0

    print("PS33 source-true J[phi0] strict upper",float(M),flush=True)
    print("PS33 true dyadic j lower at 2**2025",float(s(2025)),flush=True)
    print("PS33 low Fourier fraction lower at e 2024,2025,2026",
          float(p24),float(p25),float(p26),flush=True)
    print("PS33 unique admissible dyadic overlap-optimal exponent",OPT_E,
          flush=True)
    print("PS33 true original <d,phi0>² strictly exceeds"
          " 3/(8000*2**2025)",flush=True)
    print("PS33 true original alpha<d,phi0>² strictly exceeds"
          " (3994/2907)*3/(8000*2**2025)",flush=True)
    print("PS33 rigorous improvement vs PS32 old actual pole overlap:"
          " >2**6071/1000 times; integer dyadic optimization",flush=True)
    print("PS33 NOTE original low Fourier mass at new cutoff only",
          float(p25),"not PS32 >3/4 low-mass condition",flush=True)
    print("PS33 PASS SCOPED: optimized ORIGINAL physical first"
          " even ground/effective source-renormalized pole overlap"
          " lower from full frequency arch bound; no true phi0"
          " pointwise data or macroscopic PS31 graph, lambda1,"
          " effective Delta, signed W-EVEN-FORM/W-ODD-NEG,"
          " original Weil, CC27 D-Riesz or RH closure."
          " Original infinite-dimensional premises still need review.",
          flush=True)


if __name__=="__main__":
    run()
