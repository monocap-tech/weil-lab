#!/usr/bin/env python3
"""SM48: original signed 25-source full-coupling test of SM47 lower reference.

CERTIFIED, conditional on the retained genuine original SI06/SM04/SM12/
SM42/SM46 physical-Fourier identities and whole-real band estimates:

L47 = kappa H_q + P_17 - eps47 I  <= A_original_positive_low,25.

On the 15 original SM04 whole-real NEGATIVE windows, m(xi)<-Delta,
the complete true ORIGINAL K_neg,25 is bounded BELOW by
    N15 - epsN I, N15 = (4*r*Delta)*sum_j vneg_j*vneg_j^T,
where vneg_j are rational physical Fourier midpoint vectors for ALL
25 actual sin/xcos/sinh odd sources. Each true frequency mean error is
paid using local T''/T''' intervals (first moment cancels EXACTLY),
full 25x25 source cross retained. Thus if for exact rational z
   z^T (N15-epsN I-L47) z > 0
then L47 cannot dominate the ACTUAL full K_neg,25 (since full Kneg
dominates its 15-band certified lower). This is a METHOD-CLASS NO-GO,
**NOT** a negative witness to the actual odd Weil form. In particular,
a lower bound L47 does not furnish any upper bound on actual A_o.

Additionally original physical sinh pole vector p=H[:,pole] satisfies
  2pp* <= 2qq*+eps_pole I, q=Hq[:,pole] (full interval Gram error).
Thus L47-2qq* -eps_pole I is a lower reference for pole-corrected
A_original_positive_low -2ss*. A separate complete odd O1/O2 Schur
and all 470 sources remain OPEN; no negative index is inferred.

Fail closed: only declare reference insufficiency after an actual
positive exact rational Rayleigh gap is found. Candidate selection uses
finite exact rational standard basis and two-coordinate +/- vectors,
without numerical eigenspectra.
"""
import argparse
import json
from fractions import Fraction as F

from validate_rpb108_si06_negative_band import B
from validate_rpb108_si10_complement_positivity import KAPPA
from validate_rpb108_sm04_negative_packet_rank import (
    CENTERS as NEG_CENTERS, RADIUS as NEG_RADIUS,
    DELTA as NEG_DELTA, original_negative_certificates
)
from validate_rpb108_sm42_original_physical_gram_and_low_gate import (
    original_full_25_physical_interval_gram, hyperbolic_interval
)
from validate_rpb108_sm43_positive_cell_envelope import (
    ROOT, original_source_centered_windows, ceil_rat, floor_rat
)
from validate_rpb108_sm44_physical_fourier_cell_gram import (
    sqrt_upper, original_exact_physical_fourier_midpoint,
    original_full_second_derivative_upper
)
from validate_rpb108_sm46_affine_physical_fourier_source import (
    original_midpoint_derivative_intervals, original_third_spatial_moment
)
from validate_rpb108_sm47_original_full_low_jensen import (
    full_original_rational_gram, build_original_positive_jensen,
    E, L, TAIL
)

DEN=10**12
N=25
def qceil(a): return ceil_rat(a,DEN)


def original_15_negative_source_lower(centers,sources):
    """Original true SM04 negative whole-real window Jensen source lower.

    On each real I_j of radius r, 2*integral_I (kappa-m)_+
      T T* >= 2*DELTA*(2r) u_j u_j*= gamma*u_j u_j*.
    Use Delta, not kappa+Delta, to preserve the simpler inherited
    exact SM04 multiplier margin.
    """
    assert len(NEG_CENTERS)==15 and len(sources)==N
    assert NEG_RADIUS==F(1,100) and NEG_DELTA==F(2,5)
    assert all(0<c-NEG_RADIUS<c+NEG_RADIUS<L for c in NEG_CENTERS)
    assert all(NEG_CENTERS[i]+NEG_RADIUS <
               NEG_CENTERS[i+1]-NEG_RADIUS
               for i in range(14))
    orig_upper=original_negative_certificates()
    assert orig_upper < -NEG_DELTA
    gamma=4*NEG_RADIUS*NEG_DELTA
    assert gamma==F(2,125)
    sh=hyperbolic_interval(B/2,"sinh")
    ch=hyperbolic_interval(B/2,"cosh")
    Kglobal=original_full_second_derivative_upper(sources)
    M3=original_third_spatial_moment(sources)
    matrix=[[F(0) for j in range(N)] for i in range(N)]
    eps=F(0)
    used_local=0
    witnesses=[]
    for c in NEG_CENTERS:
        q=original_exact_physical_fourier_midpoint(
            c,centers,sources,(sh,ch))
        v=[x for x,rad in q]
        rad0=[rad for x,rad in q]
        _,T2=original_midpoint_derivative_intervals(
            c,centers,sources,(sh,ch))
        K=[]
        for t2,g,m in zip(T2,Kglobal,M3):
            kk=g if t2 is None else min(g,max(abs(t2.l),abs(t2.h))+m*NEG_RADIUS)
            assert F(0)<=kk<=g
            used_local+=int(kk<g)
            K.append(kk)
        # Whole real frequency mean linear term integrates to zero.
        rr=[rad+kk*NEG_RADIUS**2/6 for rad,kk in zip(rad0,K)]
        V2=sum((x*x for x in v),F(0))
        R2=sum((x*x for x in rr),F(0))
        eps+=gamma*(2*sqrt_upper(V2*R2)+R2)
        for i in range(N):
            for j in range(i,N):
                matrix[i][j]+=gamma*v[i]*v[j]
        witnesses.append((str(c),str(qceil(gamma*(2*sqrt_upper(V2*R2)+R2)))))
    for i in range(N):
        for j in range(i): matrix[i][j]=matrix[j][i]
    assert all(matrix[i][i]>=0 for i in range(N))
    assert all(matrix[i][j]==matrix[j][i] for i in range(N) for j in range(N))
    return matrix,qceil(eps),floor_rat(-orig_upper,DEN),used_local,witnesses


def pole_outer_majorant(physical_gram,Hq):
    """Rational full 25-source original pole rank-one form majorant."""
    pole_col=N-1
    q=[Hq[i][pole_col] for i in range(N)]
    r=[max(abs(physical_gram[i][pole_col].l-q[i]),
           abs(physical_gram[i][pole_col].h-q[i])) for i in range(N)]
    q2=sum((x*x for x in q),F(0))
    r2=sum((x*x for x in r),F(0))
    # Actual rank-one 2ppT differs from 2qqT by at most epspole I.
    ep=qceil(2*(2*sqrt_upper(q2*r2)+r2))
    return q,ep


def quadratic(A,vec):
    ix=[(i,x) for i,x in enumerate(vec) if x]
    return sum((a*b*A[i][j] for i,a in ix for j,b in ix),F(0))


def signed_reference_gap_witnesses(Lref,Nref,epsN,polevec,epsPole):
    """Exact rational search in 25 physical coordinate directions and pairs.

    Floating values appear ONLY in diagnostics, not in comparisons.
    """
    def candidates():
        for i in range(N):
            z=[F(0)]*N;z[i]=F(1)
            yield "basis",i,None,1,z
        for i in range(N):
            for j in range(i+1,N):
                for sign in (-1,1):
                    z=[F(0)]*N;z[i]=F(1);z[j]=F(sign)
                    yield "two-source",i,j,sign,z
    best_pos=None
    best_star=None
    examined=0
    for kind,i,j,sg,z in candidates():
        examined+=1
        nz2=sum((t*t for t in z),F(0))
        neg_lower=quadratic(Nref,z)-epsN*nz2
        pos_lower=quadratic(Lref,z)
        pole_sub=2*(sum((polevec[k]*z[k] for k in range(N)),F(0)))**2
        signed_lower=pos_lower-pole_sub-epsPole*nz2
        gap_no_pole=neg_lower-pos_lower
        gap_with_pole=neg_lower-signed_lower
        desc={"kind":kind,"first":i,"second":j,"sign":sg,
              "squared_coefficient_norm":str(nz2),
              "negative_15_band_certified_lower":str(qceil(neg_lower)),
              "SM47_positive_low_reference_lower":str(qceil(pos_lower)),
              "pole_conditioned_reference_lower":str(qceil(signed_lower))}
        # Comparison is EXACT before outward summary.
        if best_pos is None or gap_no_pole/nz2 > best_pos[0]:
            best_pos=(gap_no_pole/nz2,desc)
        if best_star is None or gap_with_pole/nz2 > best_star[0]:
            best_star=(gap_with_pole/nz2,desc)
    assert examined==N+2*N*(N-1)//2
    assert best_pos is not None and best_star is not None
    return examined,best_pos,best_star


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output",default="artifacts/sm48_original_25source_signed_jensen_deficit.json")
    args=p.parse_args()
    manifest=json.loads((ROOT/"research/obligations.json").read_text())
    odd=next(z for z in manifest["obligations"] if z["id"]=="W-ODD-NEG")
    assert manifest["active_obligation"]=="W-ODD-NEG"
    assert manifest["objective"]["status"]=="open" and odd["status"]=="open"
    assert manifest["governance"]["no_automatic_promotion"] is True
    assert "SM47" in odd["evidence"] and "SM47" in manifest["evidence"]
    centers,sources,_=original_source_centered_windows()
    gram,source_check,pole=original_full_25_physical_interval_gram()
    assert sources==source_check
    Hq,errH=full_original_rational_gram(gram)
    P,errP,local_pos,maxrad_pos,bands_pos,mpositive=build_original_positive_jensen(
        centers,sources)
    Nmat,errN,negative_margin,local_neg,bands_neg=original_15_negative_source_lower(
        centers,sources)
    errH=qceil(errH);errP=qceil(errP)
    fullSM47Fee=errP+KAPPA*(TAIL+errH)
    q,errPole=pole_outer_majorant(gram,Hq)
    Lref=[[KAPPA*Hq[i][j]+P[i][j]-
          (fullSM47Fee if i==j else 0)
          for j in range(N)] for i in range(N)]
    assert all(Lref[i][j]==Lref[j][i] for i in range(N) for j in range(N))
    examined,best_pos,best_star=signed_reference_gap_witnesses(
        Lref,Nmat,errN,q,errPole)
    # Fail-closed strong METHOD-NOGO gate. We do NOT call this an
    # original full-form negative witness: no original positive upper.
    assert best_pos[0]>0, (
        "SM48 did not find a certified source Rayleigh deficit of SM47",
        float(best_pos[0]))
    assert best_star[0]>=best_pos[0] or best_star[0]>0
    result={
      "status":"CERTIFIED_ORIGINAL_25SOURCE_SM47_LOWER_REFERENCE_SIGNED_NEGATIVE_DEFICIT_ONLY",
      "canonical_W_ODD_NEG":"OPEN",
      "original_positive_window_count":17,
      "original_negative_real_window_count":15,
      "original_source_dimension":N,
      "original_pole_source_index":N-1,
      "original_true_supported_source_coordinate_descriptors":[
          {"index":i,"source_type":kind,"source_cluster_index":j,
           "source_degree":k,
           "original_signed_frequency_center":str(centers[j]) if j>=0 else None}
          for i,(kind,j,k) in enumerate(sources)],
      "original_positive_low_0_to_4096_complete_one_sided_lower":True,
      "actual_complete_original_negative_frequency_upper_certified":False,
      "true_original_signed_negative_15band_lower_certified":True,
      "original_15_negative_window_original_m_upper_below_minus_two_fifths":True,
      "original_negative_multiplier_margin_rational_lower":str(negative_margin),
      "SM47_positive_low_reference_error_exact_outward":str(fullSM47Fee),
      "negative_15band_mean_Loewner_error_exact_outward":str(errN),
      "true_pole_rank_one_rational_majorant_error_exact_outward":str(errPole),
      "original_local_true_Tsecond_source_improvements_positive":local_pos,
      "original_local_true_Tsecond_source_improvements_negative":local_neg,
      "exact_original_25source_rayleigh_tests":examined,
      "nonpole_reference_best_signed_deficit_per_source_norm2_rational_lower":
         str(qceil(best_pos[0] - F(1,DEN))),
      "nonpole_reference_witness":best_pos[1],
      "pole_conditioned_reference_best_signed_deficit_per_source_norm2_rational_lower":
         str(qceil(best_star[0] - F(1,DEN))),
      "pole_conditioned_reference_witness":best_star[1],
      "meaning":"SM47 computed one-sided positive lower matrix, even BEFORE pole subtraction, does not dominate a genuine original 15-band negative-frequency lower suboperator on the actual 25-source physical trial carrier. A weaker lower is not an upper bound on actual positive A_o, so this is only a proof-reference obstruction, not actual signed Weil negativity.",
      "source_windows_positive_error":"SM47 original 17 bands",
      "source_windows_negative_error":"SM04 true original 15 bands",
      "full_25x25_rational_positive_reference_matrix":[
          [str(x) for x in row] for row in P],
      "full_25x25_rational_negative_15band_reference_matrix":[
          [str(x) for x in row] for row in Nmat],
      "full_25x25_rational_positive_low_lower_matrix":[
          [str(x) for x in row] for row in Lref],
      "negative_window_error_breakdown":bands_neg,
      "remaining":[
         "Original stronger/more complete positive-frequency lower response not yet included by 17 Jensen bands",
         "Original complete negative-frequency cap 890 and complete 470 physical source inverse with strong residual",
         "True full original odd O1/O2 or exact pole-corrected Schur and even E1–E4",
         "Original signed Weil/CC27/RH and independent Fourier/domain audit"
      ]
    }
    out=ROOT/args.output;out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2)+"\n")
    print("SM48 original signed 25-source full cross:",json.dumps({
        "negative_bands":15,
        "positive_bands":17,
        "SM47_lower_error":str(fullSM47Fee),
        "negative_mean_error":str(errN),
        "pole_majorant_error":str(errPole),
        "best_nonpole_deficit_per_norm2":float(best_pos[0]),
        "best_pole_conditioned_deficit_per_norm2":float(best_star[0]),
        "best_nonpole_witness":best_pos[1],
        "best_pole_witness":best_star[1],
        "whole_original_odd_O1_O2_Weil_RH":"OPEN"
    },sort_keys=True),flush=True)
    print("SM48 CERTIFIED PROOF-REFERENCE LIMITATION, not an original signed odd counterexample. Full original 470 source and all-operator negative cap remain OPEN.",flush=True)

if __name__=="__main__":
    main()
