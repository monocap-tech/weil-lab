#!/usr/bin/env python3
"""SM57: TRUE original 25-source complete negative upper / signed lower.

Unlike preceding physical 2D/3D trial-source signed proofs, this
certificate covers ALL 25 genuine original selected supported odd
SI10 sources: 16 sin, 8 xcos, and actual sinh(x/2).

The entire true original negative multiplier r=(kappa-m)_+ is
supported on the 973 real SI10 leaf cells (107 disjoint clusters)
with original all-seven-prime/digamma whole-real upper r<=h_I+kappa.
For each leaf I and every real xi in I, the original source
sine-transform modulus is bounded by the full 25-component SM43
whole-real envelope s_i(I). Let z be arbitrary real source coefficients.
Then
   |sum_i z_i T_i(xi)|²
   <= (sum_i |z_i| s_i)^2
   <= (sum_j s_j) * sum_i (s_i z_i²).
Consequently the *complete* original negative-frequency source
operator is bounded from ABOVE in 25x25 Loewner order by the
nonnegative diagonal D_i =
      2*sum_{I in SI10 973} |I| (h_I+kappa) s_i sum_j s_j.
Outward rounding of BOTH each real-cell r and each true Fourier
source cap is performed BEFORE the sum. This charges all negative
frequencies and all mixed original source coefficients, without
pretending that original source directions are orthogonal.

Combine with the already certified complete 25x25 original
SM47+SM49 positive LOW source lower, and the true SM42 physical
sinh pole rank-one UPPER via a certified Gram interval vector p.
Then Wodd on the actual ORIGINAL physical 25-source span satisfies
the complete true source Loewner lower
    W_25 >= Lpos_25 - diag(D_i) - 2 p p^T.
The output is a compact rational 25x25 lower matrix after entire
max-row-sum quantization error is PAID on its diagonal.

This is deliberately an acceptance-grade complete source
representation but NOT a proof of original 25x25 signed PSD or
negative index. Negative lower entries/determinants imply no actual
negative mode. Orthogonal remainder, all 470 source inverse, O1/O2,
even/Weil/CC27/RH remain OPEN. Use new 25-source lower to identify
which SOURCE-vs-TRUE-OPERATOR bounds must be refined, rather than
promote a three-dimensional positivity argument.
"""
import argparse,json
from fractions import Fraction as F
from validate_rpb108_si10_complement_positivity import KAPPA
from validate_rpb108_sm10_explicit_odd_cap_moments import full_upper_leaves
from validate_rpb108_sm43_positive_cell_envelope import (
    ROOT,original_source_centered_windows,source_window_support_envelopes,
    ceil_rat,floor_rat)
from validate_rpb108_sm42_original_physical_gram_and_low_gate import (
    original_full_25_physical_interval_gram)
from validate_rpb108_sm44_physical_fourier_cell_gram import (
    quantize,sqrt_upper)
from validate_rpb108_sm47_original_full_low_jensen import (
    TAIL,full_original_rational_gram,build_original_positive_jensen)
from validate_rpb108_sm49_adaptive_positive_jensen import (
    original_adaptive_candidate_cells,
    original_additional_positive_source_matrix)

N=25
PREC=10**9
OUTPUT_DEN=10**12

def up(x):return ceil_rat(x,OUTPUT_DEN)
def down(x):return floor_rat(x,OUTPUT_DEN)

def complete_original_negative_upper_diagonal(centers,sources):
    """Exhaust full continuous negative frequency with rigorous 25 caps.

    For all z, 2int r |sum z_i*T_i|² <= sum_i D_i z_i².
    Every D_i uses exact rational outward original signed weight
    and TRUE source transform envelope on ALL real xi in a leaf.
    """
    clusters,W,Mneg,total_mass=full_upper_leaves()
    assert len(clusters)==107 and W==F(973,32)
    leaves=[(l,r,w) for cluster in clusters for l,r,w in cluster]
    assert len(leaves)==973 and len(sources)==N
    D=[F(0) for _ in range(N)]
    maxcap=[F(0) for _ in range(N)]
    mass=F(0)
    width=F(0)
    maxweight=F(0)
    strict_positive_cells=0
    for left,right,h in leaves:
        assert F(0)<=left<right<=F(896)
        # The original SI10 all-real negative weight cap is
        # h+kappa. Round UP to a small exact rational BEFORE use.
        real_weight=h+KAPPA
        weight=ceil_rat(real_weight,PREC)
        assert weight>=real_weight and weight>0
        rawcaps=source_window_support_envelopes(
            left,right,centers,sources)
        assert len(rawcaps)==N
        caps=[ceil_rat(x,PREC) for x in rawcaps]
        assert all(caps[i]>=rawcaps[i]>0 for i in range(N))
        size=right-left
        sumcaps=sum(caps,F(0))
        coeff=2*size*weight*sumcaps
        for i in range(N):
            D[i]+=coeff*caps[i]
            maxcap[i]=max(maxcap[i],caps[i])
        mass+=2*size*weight
        width+=size
        maxweight=max(maxweight,weight)
        strict_positive_cells+=1
    assert strict_positive_cells==973
    # SI10 W counts BOTH signed-frequency halves; our integral is
    # twice the positive real half, but width itself is one-sided.
    assert 2*width==W and width==F(973,64)
    assert mass>=total_mass
    assert len(D)==N and all(x>0 for x in D)
    # Source2 diagonal bound cannot be smaller than the actual
    # single-source cap in general; we do NOT demand it be sharp.
    return [up(x) for x in D],{
       "original_negative_real_half_support":"[0,896], exhaustive SI10 leaves",
       "original_negative_true_whole_real_cover_clusters":len(clusters),
       "original_negative_true_whole_real_cover_leaves":len(leaves),
       "original_negative_full_supported_source_count":len(sources),
       "original_negative_total_width_exact":str(width),
       "original_negative_total_weight_mass_up":str(up(mass)),
       "original_negative_max_true_cell_weight_outward":str(up(maxweight)),
       "original_negative_max_per_source_sinc_envelope_outward":[
           str(up(x)) for x in maxcap],
       "original_negative_all25_complete_Cauchy_row_majorant":True,
       "original_negative_full25_Loewner_upper_diagonal":[str(up(x)) for x in D]
    }

def pole_outer_upper(gram):
    """Entire true original sinh pole rank-one upper on all 25 sources.

    p_i=<g_i,s>, s=g_24. Original H_i24 is a genuine closed
    interval via SM42 exact physical analytic integral.
    For q_i midpoint rational and |p_i-q_i|<=e_i, 2 ppT
    <= 2 qqT + 2(2||q||||e||+||e||²) I25.
    """
    q=[];e=[]
    for i in range(N):
        iv=gram[i][24]
        qi=quantize(iv.mid())
        radius=max(abs(iv.l-qi),abs(iv.h-qi))
        assert radius>=0
        q.append(qi);e.append(radius)
    q2=sum((x*x for x in q),F(0))
    e2=sum((x*x for x in e),F(0))
    scalar=up(2*(2*sqrt_upper(q2*e2)+e2))
    assert scalar>=0
    mat=[[2*q[i]*q[j] for j in range(N)] for i in range(N)]
    for i in range(N):mat[i][i]+=scalar
    assert all(mat[i][j]==mat[j][i] for i in range(N) for j in range(N))
    return mat,scalar

def original_positive_low_25(centers,sources,gram):
    """Re-run rather than guess the SM47/SM49 entire positive source lower."""
    Hq,epsH=full_original_rational_gram(gram)
    P47,eps47,_,_,b47,_=build_original_positive_jensen(centers,sources)
    chosen,available,_,_=original_adaptive_candidate_cells(centers,sources)
    assert len(b47)==17 and len(chosen)==32
    P49,eps49,_,_,_=original_additional_positive_source_matrix(
        centers,sources,chosen)
    eps=KAPPA*(TAIL+up(epsH))+up(eps47)+up(eps49)
    A=[[KAPPA*Hq[i][j]+P47[i][j]+P49[i][j]
        -(eps if i==j else F(0)) for j in range(N)]
        for i in range(N)]
    assert all(A[i][j]==A[j][i] for i in range(N) for j in range(N))
    return A,{
      "original_positive_low_real_support":"[0,4096] (high remainder discarded only when nonnegative)",
      "original_positive_inherited_strict_real_signed_windows":17+32,
      "complete_25_positive_source_Gram_and_Jensen_Loewner_error":str(up(eps)),
      "original_positive_full25_source2_diagonal_lower":str(down(A[2][2]))
    }

def outward_compact_matrix(A,den=OUTPUT_DEN):
    """Exact proof first, then full symmetric rational Loewner lower export."""
    assert len(A)==N and all(len(row)==N for row in A)
    assert all(A[i][j]==A[j][i] for i in range(N) for j in range(N))
    q=[[F(round(A[i][j]*den),den) for j in range(N)] for i in range(N)]
    assert all(q[i][j]==q[j][i] for i in range(N) for j in range(N))
    row_errors=[sum(abs(A[i][j]-q[i][j]) for j in range(N))
                for i in range(N)]
    err=up(max(row_errors))
    out=[[q[i][j]-(err if i==j else F(0)) for j in range(N)]
         for i in range(N)]
    assert all(out[i][j]==out[j][i] for i in range(N) for j in range(N))
    assert err>=max(row_errors)
    return out,err

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output",
       default="artifacts/sm57_original_complete_negative_25source_signed_lower.json")
    args=p.parse_args()
    manifest=json.loads((ROOT/"research/obligations.json").read_text())
    odd=next(x for x in manifest["obligations"] if x["id"]=="W-ODD-NEG")
    assert manifest["active_obligation"]=="W-ODD-NEG"
    assert odd["status"]==manifest["objective"]["status"]=="open"
    assert manifest["governance"]["no_automatic_promotion"] is True
    assert all(x in odd["evidence"] for x in ("SM49","SM56","SM57"))
    centers,sources,_=original_source_centered_windows()
    assert len(sources)==N and sources[24][0]=="pole"
    assert sum(x[0]=="cluster" and x[2]==0 for x in sources)==16
    assert sum(x[0]=="cluster" and x[2]==1 for x in sources)==8
    gram,actual,pole=original_full_25_physical_interval_gram()
    assert sources==actual
    neg,negative_stats=complete_original_negative_upper_diagonal(
        centers,sources)
    positive,positive_stats=original_positive_low_25(
        centers,sources,gram)
    polemat,pole_err=pole_outer_upper(gram)
    Lexact=[[positive[i][j]-polemat[i][j]-
              (neg[i] if i==j else F(0))
             for j in range(N)] for i in range(N)]
    L,fee=outward_compact_matrix(Lexact)
    assert all(L[i][j]==L[j][i] for i in range(N) for j in range(N))
    # Do NOT call negative diagonal of this LOWER an actual negative vector!
    diag=[L[i][i] for i in range(N)]
    count_positive=sum(x>0 for x in diag)
    # Source2/17 are already positively classified by SM52 on a much
    # sharper 2D signed real source basis; the full-25 envelope may
    # be far weaker. This is explicitly diagnostic, NOT a regression
    # of the stronger restricted source certificate.
    d={
       "status":"SCOPED_TRUE_ORIGINAL_COMPLETE_25SOURCE_SIGNED_LOEWNER_LOWER_AND_NEGATIVE_UPPER",
       "canonical_W_ODD_NEG":"OPEN",
       "original_actual_supported_source_count":N,
       "original_sources_include":"16 sin, 8 xcos, 1 genuine sinh pole",
       "all_original_25x25_mixed_source_coefficients_paid":True,
       "full_original_negative_frequency_operator_upper_on_all_25":True,
       **negative_stats,**positive_stats,
       "original_true_physical_sinh_pole_rankone_full25_upper":True,
       "original_pole_full25_Loewner_upper_rounding_fee":str(pole_err),
       "complete_original_signed_25x25_matrix_outward_export_fee":str(fee),
       "original_complete_25source_signed_lower_matrix":[
          [str(x) for x in row] for row in L],
       "original_signed_25source_lower_diagonal":[str(down(x)) for x in diag],
       "signed_lower_diagonal_positive_entry_count_not_a_PSD_claim":count_positive,
       "original_true_negative_index_exactly_known":False,
       "original_25source_signed_PSD_certified":False,
       "complete_original_odd_orthogonal_complement_classified":False,
       "original_470source_Astar_inverse_and_O1O2_closed":False,
       "even_Weil_CC27_RH_closed":False,
       "independent_physical_Fourier_form_domain_audit":"OPEN",
       "interpretation":"Real exact 25x25 original supported signed-source Wodd lower from original positive LOW lower, entire true negative-frequency upper and physical exceptional pole. Its negative eigenspaces, if any, belong ONLY to a LOWER reference and do not establish true negative index. Full original odd/even/Weil/RH OPEN."
    }
    target=ROOT/args.output
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps(d,indent=2)+"\n")
    print("SM57 original full 25-source complete negative-spectrum upper and true signed lower:",json.dumps({
       "negative_real_leaves":negative_stats["original_negative_true_whole_real_cover_leaves"],
       "source_count":N,
       "negative_diagonal_source2_up":str(neg[2]),
       "positive_low_source2_lower":str(down(positive[2][2])),
       "true_signed_full25_lower_source2":str(down(L[2][2])),
       "signed_lower_positive_diagonal_count":count_positive,
       "actual_entire_odd_index":"OPEN",
       "even_Weil_RH":"OPEN"
    }),flush=True)

if __name__=="__main__":main()
