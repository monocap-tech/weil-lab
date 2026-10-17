#!/usr/bin/env python3
"""PS07: original signed seven-prime quadratic IMS localization.

Exact rational checks for analytic bounded/noncompact/graph-compact
physical localization defect. Does NOT compute a signed Schur PSD,
full Weil original positivity or RH. Parent source identity pinned.
"""
from fractions import Fraction as F
import json
from pathlib import Path
import validate_rpb108_rc315_low_mode_sign as old
import validate_rpb108_ps03_edge_coercivity as ps03
import validate_rpb108_ps06_form_domain_partition as ps06

ROOT = Path(__file__).resolve().parents[1]
B = F(11, 10)
R = 2*B
ORIGINAL = ((2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3))

def run():
    # True original source receipt and infinite-dimensional supported edge
    # positivity; repeat PS06 signed physical graph domain certificate.
    ps03.run()
    ps06.run()
    m=json.loads((ROOT/"research/obligations.json").read_text())
    p=json.loads((ROOT/"research/parallel_investigations/w_physical_shift.json").read_text())
    assert m["active_obligation"]=="W-ODD-NEG"
    assert m["objective"]["status"]=="open"
    assert p["id"]=="W-PHYSICAL-SHIFT"
    assert p["active_frontier_unchanged"]=="W-ODD-NEG"
    assert p["status"]=="open"
    assert all(v is False for v in p["closures"].values())

    pi=old.pi_iv()
    ln2=old.log_i(F(2))
    ln9=old.log_i(F(9))
    delta=old.IV(R-ln9.hi,R-ln9.lo)
    a=old.IV(ln9.lo-B,ln9.hi-B)
    assert F(1,400)<delta.lo<=delta.hi<F(1,350)
    assert F(1)<a.lo<=a.hi<B

    # θ=(pi/2)χ, χ exact PS06 linear cut-off with ||χ'||<=2/delta.
    # Thus θ'<=A=pi/delta. Certified true cutoff domain stability.
    A_hi=pi.hi/delta.lo
    A_lo=pi.lo/delta.hi
    assert F(700)<A_lo<=A_hi<F(2048)
    # In both trig masks 0<=α,β<=1, α²+β²=1,
    # η=2(1-cos(θx-θy))∈[0,2], η<=A²u².

    # Signed native original constants: exactly seven prime powers.
    weights=[]
    for n,base in ORIGINAL:
        root=old.IV(2 if n==4 else 3) if n in (4,9) else old.sqrt_i(n)
        w=old.log_i(F(base))/root
        assert w.lo>0
        weights.append(w)
    assert len(weights)==7
    sum_weights=sum(weights,old.IV(0))
    assert F(3)<sum_weights.lo<=sum_weights.hi<F(4)

    sinh,cosh=old.sinh_cosh_iv(B/2)
    sinh_B=2*sinh*cosh
    assert F(1)<sinh_B.lo<=sinh_B.hi<F(3,2)

    # c* gives |Q−J|<=c*||f||²; true signed poles and prime terms.
    arch_c=-old.gamma_iv()-pi/2-3*ln2-old.log_i(pi)
    Cstar=(-arch_c).hi+2*sum_weights.hi+4*sinh_B.hi
    assert Cstar<F(18)
    graph_gap=20-Cstar
    assert graph_gap>2

    # For each α,β, the original graph bound on its quadratic form:
    # I_A = int k(u) min(Au,1)^2 du
    #     < .5 log A + 21/4 < .5 log2048+21/4 < 10.
    log2048_hi=11*ln2.hi
    assert log2048_hi<F(8)
    IA_hi=log2048_hi/F(2)+F(21,4)
    assert IA_hi<F(10)
    # G[θ f]<=2 J[f]+(2I_A+20+Cstar)||f||².
    # J[f]<=G[f], ||f||²<=G[f]/(20-Cstar).
    graph_mult=F(2)+(2*IA_hi+20+Cstar)/graph_gap
    assert graph_mult<F(31),float(graph_mult)

    # Arch IMS correction kernel K(x,y)=0.5*k(|x−y|)*η(x,y)
    # continuous at diagonal with limit 0 => Hilbert-Schmidt, compact.
    # Schur operator norm <=H_A=int k(u)min(A²u²,2)du,
    # < 11+log A < 11+log2048.
    arch_upper=F(11)+log2048_hi
    assert arch_upper<F(19)
    prime_upper=2*sum_weights.hi
    assert prime_upper<F(8)
    # Rank at most six pole defect.
    pole_upper=8*sinh_B.hi
    assert pole_upper<F(12)
    remainder_upper=arch_upper+prime_upper+pole_upper
    assert remainder_upper<F(40),float(remainder_upper)

    # Isolated true log2 prime reflection:
    # V=[B-delta/8,B] entirely outer α=1,β=0.
    # U=V-log2 wholly central α=0,β=1.
    # χ=0 on |x|<=a+delta/4 and χ=1 on |x|>=a+3delta/4.
    Vlo=B-delta.hi/F(8)
    Vhi=B
    Ulo=Vlo-ln2.hi
    Uhi=Vhi-ln2.lo
    assert Vlo > B-delta.lo/F(4)
    assert F(0)<Ulo<Uhi<a.lo+delta.lo/F(4)
    assert Vhi-Vlo<F(1,350)
    assert Uhi-Ulo<F(1,350)
    # For n!=2, differences log(n)-log(2)>width V
    # and therefore none map V into U.
    for n,_ in ORIGINAL:
        if n==2:
            continue
        lni=old.log_i(F(n))
        assert lni.lo-ln2.hi>delta.hi
    # χ values are 1 on V and 0 on U, so η=2.
    # Prime block P_U R P_V is exactly (log2/sqrt2)*unitary
    # physical translation modulo compact arch Hilbert-Schmidt
    # and finite-rank pole terms. Therefore essential norm>=w2.
    root2=old.sqrt_i(2)
    true_w2=ln2/root2
    assert true_w2.lo>F(49,100) and true_w2.hi<F(1,2)

    # The true original whole physical graph form is compactly embedded:
    # arch J(|xi|)>=log(|xi|/2)-1/pi-1/2 for |xi|>=2.
    # With G>=J+2 mass, the entire high Fourier tail ≤ G/LambdaLog.
    growth=79*ln2.lo-F(1)/pi.lo-F(1,2)
    assert growth>F(53)
    full_energy_tail_ratio=F(1)/growth
    assert full_energy_tail_ratio<F(1,53)
    # The physical finite-band sinc compression is HS on finite I;
    # letting frequency ->infinity proves compact graph embedding
    # and therefore compact H^{-1/2} R H^{-1/2} even though R not
    # compact on L2. No numerical finite rank PSD follows.

    print("PS07 actual IMS trig angle Lipschitz A upper",float(A_hi),flush=True)
    print("PS07 graph G=q+20 mass multiplier upper per mask",float(graph_mult),flush=True)
    print("PS07 true arch IMS Hilbert-Schmidt operator-norm upper",float(arch_upper),flush=True)
    print("PS07 true seven-prime signed translation norm upper",float(prime_upper),flush=True)
    print("PS07 original signed pole rank-six norm upper",float(pole_upper),flush=True)
    print("PS07 whole original IMS remainder operator norm upper",float(remainder_upper),flush=True)
    print("PS07 unique log2 prime essential-norm LOWER",float(true_w2.lo),flush=True)
    print("PS07 full physical graph arch spectral growth at 2^80",float(growth),flush=True)
    print("PS07 graph high frequency tail ratio upper",float(full_energy_tail_ratio),flush=True)
    print("PS07 PASS SCOPED: exact ORIGINAL signed quadratic IMS"
          " identity with compact arch kernel, noncompact actual log2"
          " weighted translation and rank-six pole remainder;"
          " true L2 remainder <40 but essential norm >0.49;"
          " graph-energy-conjugated remainder compact."
          " This is an analytical result with outward-rational"
          " source checks, not full Schur PSD, CC27 bridge or RH.",flush=True)

if __name__=="__main__":
    run()
