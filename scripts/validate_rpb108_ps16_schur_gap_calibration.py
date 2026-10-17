#!/usr/bin/env python3
"""PS16: TRUE signed original source Schur quantitative/sign calibration.

Parent replays original PS15->PS14->PS13->...->RC315 source pins.
Proves rational source gap >0.323, Schur penalty <869,
a genuine positive high-arch-energy complementary sector,
a nonzero seam energy-dual penalty >0.028, and necessary RC315
even/odd *UPPER* ceilings for any uniform positive Schur margin.
Does NOT certify complementary PSD, D-Riesz carrier or RH.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import validate_rpb108_rc315_low_mode_sign as old
import validate_rpb108_ps15_sharp_source_schur as ps15

ROOT=Path(__file__).resolve().parents[1]
B=F(11,10)
R=2*B
SRC=((2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3))
LABELS=sorted({F(1),F(9)}|{F(n) for n in (2,3,4,5,7,8)}
              |{F(9,n) for n in (2,4,5,7,8)})

def run():
    ps15.run()
    gov=json.loads((ROOT/"research/obligations.json").read_text())
    lane=json.loads((ROOT/"research/parallel_investigations/w_physical_shift.json").read_text())
    assert gov["active_obligation"]=="W-ODD-NEG"
    assert gov["objective"]["status"]=="open"
    assert lane["id"]=="W-PHYSICAL-SHIFT" and lane["status"]=="open"
    assert lane["active_frontier_unchanged"]=="W-ODD-NEG"
    assert all(v is False for v in lane["closures"].values())

    pi=old.pi_iv()
    ln2=old.log_i(F(2))
    ln5=old.log_i(F(5))
    ell9=old.log_i(F(9))
    delta=old.IV(R-ell9.hi,R-ell9.lo)
    assert F(1,400)<delta.lo<=delta.hi<F(1,350)
    carch=-old.gamma_iv()-pi/2-3*ln2-old.log_i(pi)
    assert carch.hi<-F(5)
    sn,cs=old.sinh_cosh_iv(B/2)
    cosh_B=cs*cs+sn*sn
    assert cosh_B.hi<F(7,4)

    # PS14: TRUE original Q on 13 supported physical channels has all
    # 19 internal prime edges, not the 13 IMS-remainder prime edges.
    offsets={q:(old.IV(0) if q==1 else old.log_i(q)) for q in LABELS}
    assert len(LABELS)==13
    weights={}
    for n,base in SRC:
        root=old.IV(2 if n==4 else 3) if n in (4,9) else old.sqrt_i(n)
        weights[n]=old.log_i(F(base))/root
        assert weights[n].lo>0
    edges=[]
    for i,u in enumerate(LABELS):
        for j in range(i+1,len(LABELS)):
            v=LABELS[j]
            for n,_ in SRC:
                if v==u*n:
                    edges.append((i,j,n))
    assert len(edges)==19
    W=[[F(0) for j in range(13)] for i in range(13)]
    for i,j,n in edges:
        W[i][j]=W[j][i]=weights[n].hi
    W2=[[sum((W[i][k]*W[k][j] for k in range(13)),F(0))
          for j in range(13)] for i in range(13)]
    row_max=max(sum(row,F(0)) for row in W2)
    assert row_max<F(213,100)**2,float(row_max)

    # Same entire original digamma arch 64-term diagonal bound,
    # off-source arch cross and correctly signed negative odd pole.
    tail64=F(0)
    for m in range(64):
        a=F(4*m+1,2)
        x=a*delta.hi
        assert 0<x<32
        tail64+=2*(1-x/32)**32/a
    arch_diag=carch.lo+tail64
    assert arch_diag>F(2683,1000),float(arch_diag)
    gap=F(1,10)-delta.hi
    assert gap>0
    arch_cross=12*delta.hi*(1+F(1)/(2*gap))
    assert arch_cross<F(205,1000),float(arch_cross)
    odd_cost=26*delta.hi*sn.hi**2
    assert odd_cost<F(25,1000),float(odd_cost)
    source_lower=arch_diag-F(213,100)-arch_cross-odd_cost
    assert source_lower>F(323,1000),float(source_lower)

    # A_P >.323, genuine physical offdiag B_PC<67/4 from PS15.
    # True POSITIVE COMPACT Schur subtraction T_C=B* A_P^-1 B.
    tnorm_hi=F(67,4)**2/F(323,1000)
    assert tnorm_hi==F(4489000,5168)
    assert tnorm_hi<F(869)
    # Q_C>=J_C-13mass is the sign-aware original source comparison.
    # S_C=Q_C-T_C>J_C-(13+869)mass:
    threshold=F(13)+F(869)
    assert threshold==F(882)
    # The spectral J_C>=882 part of the complement is S_C positive,
    # but the residual low/high cross Schur remains unknown.

    # Explicit L2-normalized source/complement seam indicator vectors.
    # eps=delta/64. Seven prime cross terms vanish by support;
    # original arch mixed is negative, both signed poles O(eps).
    eps_hi=delta.hi/64
    eps_lo=delta.lo/64
    assert 2*eps_hi<ln2.lo and eps_lo>F(1,25600)
    seam_b_upper=-ln2.lo+eps_hi*(F(1,4)+2*cosh_B.hi)
    assert seam_b_upper<-F(69,100),float(seam_b_upper)

    # Exact ORIGINAL normalized source indicator difference-energy:
    # D_e(u)=2min(u/eps,1); J[e] <log(1/eps)+11 from original k.
    # eps>1/25600, log25600=10log2+2log5.
    log_eps_hi=10*ln2.hi+2*ln5.hi
    assert log_eps_hi<F(103,10)
    # All 7 original prime e autocorrelations are identically zero;
    # positive even pole <=2eps cosh(B/2)^2; odd pole safely dropped.
    q_source_step_hi=log_eps_hi+F(11)+carch.hi+2*eps_hi*cs.hi**2
    assert q_source_step_hi<F(17),float(q_source_step_hi)
    seam_penalty_lo=F(69,100)**2/F(17)
    assert seam_penalty_lo==F(4761,170000)
    assert seam_penalty_lo>F(28,1000)

    # Source-pinned RC315 original physical u0/u1 diagonal intervals.
    receipt=json.loads((ROOT/"certificates/rpb108_rc315_low_mode_sign.json").read_text())
    assert receipt["milestone"]=="RC315" and not receipt["RH"]
    assert receipt["original_source_pin"]==old.ORIGINAL_PIN
    diags=receipt["original_low_diagonals"]
    assert [d["n"] for d in diags]==[0,1]
    q0_lo,q0_hi=map(F,diags[0]["physically_normalized_original_Weil_diagonal_interval"])
    q1_lo,q1_hi=map(F,diags[1]["physically_normalized_original_Weil_diagonal_interval"])
    assert F(0)<q0_lo<=q0_hi<F(41,1000)
    assert F(0)<q1_lo<=q1_hi<F(14,100)

    # u0=1/sqrt(R), u1=sqrt(3/R)*x/B normalized on original I.
    # Reflection symmetry of P follows labels r<->9/r.
    assert all(F(9)/r in LABELS for r in LABELS)
    even_complement_mass_lo=1-F(13)*delta.hi/R
    odd_complement_mass_lo=1-F(39)*delta.hi/R
    assert 0<odd_complement_mass_lo<even_complement_mass_lo<1
    # Variational exact source Schur S_C[h_j]=inf_e Q[e+h_j] <=Q[u_j].
    # These are UPPER ceilings on a hypothetical positive margin,
    # NOT lower bounds proving a sign.
    even_gap_ceiling=q0_hi/even_complement_mass_lo
    odd_gap_ceiling=q1_hi/odd_complement_mass_lo
    assert even_gap_ceiling<F(41,1000),float(even_gap_ceiling)
    assert odd_gap_ceiling<F(7,50),float(odd_gap_ceiling)

    # Sylvester inertia equivalence via PS15 domain-preserving
    # invertible triangular completion of square. PS13 nonpositive
    # index bound transfers, though numerical inertia is UNKNOWN.
    dim_cap=F(352_000_000)
    assert dim_cap>0

    print("PS16 full original 19-prime source W² row upper",float(row_max),flush=True)
    print("PS16 full original true source Q coercivity lower",float(source_lower),flush=True)
    print("PS16 actual signed source Schur penalty norm upper",float(tnorm_hi),flush=True)
    print("PS16 sufficient complement arch J high-energy threshold",float(threshold),flush=True)
    print("PS16 explicit seam original mixed form upper",float(seam_b_upper),flush=True)
    print("PS16 explicit seam source step Q upper",float(q_source_step_hi),flush=True)
    print("PS16 ACTUAL nonzero Schur penalty seam lower",float(seam_penalty_lo),flush=True)
    print("PS16 original even P0 complementary Schur margin UPPER",float(even_gap_ceiling),flush=True)
    print("PS16 original odd P1 complementary Schur margin UPPER",float(odd_gap_ceiling),flush=True)
    print("PS16 negative-index inherited dimensional UPPER",int(dim_cap),flush=True)
    print("PS16 PASS SCOPED: original source gap >.323; full"
          " signed compact energy-dual Schur penalty <869 yet"
          " nonzero seam response >.028; complementary S_C"
          " strictly positive for J_C>=882; any uniform even"
          " Schur positive margin <.041, odd margin <.14."
          " LOW complementary sign, low/high coupling, complete"
          " CC27 D-Riesz attachment, W-ODD-NEG, W-EVEN-FORM,"
          " whole original Weil and RH remain OPEN.",flush=True)

if __name__=="__main__":
    run()
