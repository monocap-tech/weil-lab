#!/usr/bin/env python3
"""PS08: explicit physical Galerkin rank/error for ORIGINAL signed IMS graph.

Rigorous abstract finite-rank approximation K_N=P_N H^-1/2 R H^-1/2 P_N
for complete original seven-prime Weil IMS remainder with all poles.
The gigantic 2**8206 x 2**8206 matrix is NOT built or evaluated.
This is a quantitative approximate-compactness/method-cost theorem,
NOT a computed PSD, source inverse or whole odd/even Weil/RH proof.
"""
from fractions import Fraction as F
import json
from pathlib import Path
import validate_rpb108_rc315_low_mode_sign as old
import validate_rpb108_ps07_ims_localization as ps07

ROOT=Path(__file__).resolve().parents[1]
B=F(11,10)
R=2*B
N_ORIG=((2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3))
LAMBDA_EXP=8192
RANK_EXP=8206

def run():
    # Original PS07 IMS/PS06 graph/PS03 supported positivity and
    # CC27/RC313/315 source/pole receipts are all replayed.
    ps07.run()
    gov=json.loads((ROOT/"research/obligations.json").read_text())
    lane=json.loads((ROOT/"research/parallel_investigations/w_physical_shift.json").read_text())
    assert gov["active_obligation"]=="W-ODD-NEG"
    assert gov["objective"]["status"]=="open"
    assert lane["id"]=="W-PHYSICAL-SHIFT"
    assert lane["active_frontier_unchanged"]=="W-ODD-NEG"
    assert lane["status"]=="open"
    assert all(v is False for v in lane["closures"].values())

    ln2=old.log_i(F(2))
    pi=old.pi_iv()
    assert F(69,100)<ln2.lo<=ln2.hi<F(7,10)
    assert F(3)<pi.lo<=pi.hi<F(22,7)
    gamma=old.gamma_iv()
    arch_c=-gamma-pi/2-3*ln2-old.log_i(pi)
    assert arch_c.hi<0
    weights=[]
    for n,p in N_ORIG:
        root=old.IV(2 if n==4 else 3) if n in (4,9) else old.sqrt_i(n)
        w=old.log_i(F(p))/root
        assert w.lo>0
        weights.append(w)
    assert len(weights)==7
    W=sum(weights,old.IV(0))
    assert F(3)<W.lo<=W.hi<F(4)
    si,co=old.sinh_cosh_iv(B/2)
    sinh_B=2*si*co
    assert sinh_B.lo>0 and sinh_B.hi<F(3,2)

    # Same exact ORIGINAL Q vs arch J, all seven prime shifts and both poles.
    Cstar=(-arch_c).hi+2*W.hi+4*sinh_B.hi
    gamma_lower=F(20)-Cstar
    assert Cstar<F(179,10)
    assert gamma_lower>F(21,10)>F(100,49)
    # Thus ||H^-1/2||<7/10, no numerical inverse was constructed.

    # PS07 exact signed IMS uniform original physical L2 error operator.
    arch_R_upper=F(11)+11*ln2.hi
    prime_R_upper=2*W.hi
    pole_R_upper=8*sinh_B.hi
    total_R_upper=arch_R_upper+prime_R_upper+pole_R_upper
    assert total_R_upper<F(37),float(total_R_upper)

    # Fourier logarithmic tail for ORIGINAL J, on complete physical graph G.
    # L(2^8192)=8191 log 2−1/pi−1/2>75².
    lam_exponent=LAMBDA_EXP
    rank_exponent=RANK_EXP
    assert lam_exponent==8192 and rank_exponent==8206
    log_growth_lower=F(lam_exponent-1)*ln2.lo-F(1)/pi.lo-F(1,2)
    assert F(8191)*F(69,100)-F(5,6)>F(75**2)
    assert log_growth_lower>F(75**2)
    assert log_growth_lower<F(5700)
    assert rank_exponent-lam_exponent==14
    actual_Lambda_over_N=F(1,2**14)

    # P_N = orthogonal cell-mean projection on the original physical I,
    # N=2^8206 equal cells (no explicit basis or matrix allocation).
    # ||(I-P_N)H^-1/2|| <= 1/sqrt(loggrowth)
    #                 + (7/10)*2pi*Lambda*(2B)/N.
    # ||K-P_NKP_N|| <= 2||R|| ||H^-1/2|| ||(I-P_N)H^-1/2||.
    # The strict Fraction majorant is completely exact:
    hi_tail=F(1,75)
    hi_cell=F(7,10)*2*F(22,7)*R*actual_Lambda_over_N
    hi_residual=2*F(37)*F(7,10)*(hi_tail+hi_cell)
    assert hi_residual==F(443149,614400)
    assert hi_residual<F(3,4)
    assert hi_residual>F(7,10)

    # Limitation of THIS PARTICULAR UNIFORM sufficient-error formula:
    # For Lambda <= 2^6000, loggrowth < 5999*0.7 < 4700, while
    # (2*37*0.7 /0.75)^2 >4700. Thus even N->infinity will not
    # let THIS conservative sufficient bound certify <0.75.
    # This is emphatically NOT a mathematical lower rank/eigenvalue bound.
    low_freq_growth_upper=F(5999)*ln2.hi
    impossible_gate=(2*F(37)*F(7,10)/F(3,4))**2
    assert low_freq_growth_upper < F(4700) < impossible_gate
    assert hi_cell>0

    # The true original Q and real-even IMS masks commute with parity;
    # the N even-cell Galerkin projector therefore has exactly N/2
    # parity-adapted directions for each sign.
    N=1<<rank_exponent
    Lambda=1<<lam_exponent
    assert N.bit_length()==rank_exponent+1
    assert Lambda.bit_length()==lam_exponent+1
    assert N//Lambda==2**14
    assert N%2==0
    assert (N//2).bit_length()==rank_exponent

    print("PS08 original full signed Cstar bound",float(Cstar),flush=True)
    print("PS08 original G positive gap bound",float(gamma_lower),flush=True)
    print("PS08 original actual signed IMS R norm upper",float(total_R_upper),flush=True)
    print("PS08 rigorous true 2^8192 high-freq log-growth lower",float(log_growth_lower),flush=True)
    print("PS08 explicit Galerkin rank 2**",rank_exponent," (NOT ALLOCATED)",sep="",flush=True)
    print("PS08 exact norm residual majorant rational",str(hi_residual),flush=True)
    print("PS08 exact norm residual majorant decimal",float(hi_residual),flush=True)
    print("PS08 each parity projection rank 2**",rank_exponent-1," (NOT ALLOCATED)",sep="",flush=True)
    print("PS08 coarse uniform source-envelope 3/4 threshold"
          " IMPOSSIBLE within this method when Lambda<=2^6000",flush=True)
    print("PS08 PASS SCOPED: genuine complete original signed"
          " energy-normalized IMS compact operator admits explicit"
          " finite-rank spatial Galerkin compression with rigorous"
          " ||K-P_NKP_N||<3/4, but rank 2^8206 is computationally"
          " uncompetitive, matrix entries absent, and no positive"
          " Schur PSD, CC27 transfer, full Weil or RH.",flush=True)

if __name__=="__main__":
    run()
