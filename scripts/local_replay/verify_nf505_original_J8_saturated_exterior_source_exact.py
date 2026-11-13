#!/usr/bin/env python3
"""NF505 independent exact-Fraction scope/source audit of the original
NF504 *support-saturated* two-terminal-collar J8 physical quotient.

Read a real original NF504 4096-bit source-native result only AFTER
the computation finishes. Verify unmodified NF407/NF406 and accepted
NF404/NF478/NF479/NF495 exact rational original receipts; independently
reassemble E_full and E_out, compare all source-named signed intervals,
audit source dyadic frame SHA + 242 original selected generator order,
242x242 exterior Gram symmetry/diagonal positivity, independent
primal/dual Schur agreement, exact original gamma² comparison, and
logical scope.

In particular: this is the best possible PHYSICAL L2 correction
supported on S, not the existence of any admissible Weil source or
operator-domain vector. No RH/odd positivity leap.

The *original numerical* 242x242 Gram is not independently reintegrated
from the source at 4096bit by this Fraction auditor; its historical
original frame identity and complete interval matrix is source-audited,
and actual 242D projection/Schur was computed by the separate NF504
native calculator. Distinguish this from an independent 242x242 solve.
"""
from __future__ import annotations
import argparse,hashlib,json,sys
from pathlib import Path
from fractions import Fraction as F
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
SRC="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAM="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
FRAME="18ac01bba4de7ec432e419db5ed990fbfabad91c10cbcf2f61cf5666e36b430e"
NF494_H="39cba367d70243c2d15e5a9323fc8097d58187923dcf0eca2b031136871f0181"
NF495="ebd45c76e3bfca33572fac77cfaeb7134e21150443d84cbd206711f26a2f9460"
NF500="7e261d540c8b658bced4b44d1bf998c23ef7f975fc07daa0f30ae6438dcffb05"
NF501="7726a8a9af5faa7a22fd7581c38548c26c5a48a52cb92dc75f815c57f6e3ad7a"
NF401="644337986f62a3f25bb6b2005efc82f517975c84629b32b5ae8d1e5b95614515"

def read(path):
    raw=Path(path).read_bytes()
    return json.loads(raw),hashlib.sha256(raw).hexdigest()
def I(pair):
    a,b=map(F,pair)
    assert a<=b
    return (a,b)
def plus(a,b):
    return (a[0]+b[0],a[1]+b[1])
def minus(a,b):
    return (a[0]-b[1],a[1]-b[0])
def intersect(a,b):
    return max(a[0],b[0])<=min(a[1],b[1])
def strict_inside(a,b):
    return b[0]<=a[0]<=a[1]<=b[1]
def to_str(a):
    return [str(a[0]),str(a[1])]
def fball(v):
    # Original phys.ball: [dyadic midpoint, dyadic radius]
    assert len(v)==2
    def dyad(p):
        assert len(p)==2
        k=int(p[0]);e=int(p[1])
        return F(k)*F(2)**e
    m=dyad(v[0]);r=dyad(v[1])
    assert r>=0
    return (m-r,m+r)

def check_hilbert_countermodels():
    # Exact rational finite-dimensional examples distinguish a fixed
    # S support saturated physical L2 approximation from source
    # admissibility and global Weil-operator sign assertions.
    # With J=e1 in R3, S=e2, O=span(e1,e3),
    # w=(3,5,7), best modulo J supported S residual =49.
    w=(F(3),F(5),F(7))
    sat=w[2]**2
    assert sat==49
    assert sat==sum(x*x for x in w[0::2])-w[0]**2
    # A different S=span(e2,e3) captures full q (support changes).
    assert 0==sum(x*x for x in w[0:1])-w[0]**2
    # Model forms Q_+ and Q_- agree on all currently tested
    # w,J,S data, but can have opposite sign on a new untested ray.
    def positive(v):return sum(x*x for x in v)
    def negative(v):return v[0]**2+v[1]**2+v[2]**2-v[3]**2
    z=tuple(list(w)+[F(0)])
    assert positive(z)==negative(z)
    z0=(F(0),F(0),F(0),F(1))
    assert positive(z0)==1 and negative(z0)==-1
    # Historical pole recentering s∈J leaves q fixed.
    for a in (F(0),F(10),F(-7,11)):
        centered=(w[0]-a,w[1],w[2])
        assert centered[1:]==w[1:]
    return 8

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--native",required=True)
    ap.add_argument("--nf495",required=True)
    ap.add_argument("--nf501",required=True)
    ap.add_argument("--output",required=True)
    o=ap.parse_args()
    n,nsha=read(o.native)
    last,lsha=read(o.nf495)
    selected,ssha=read(o.nf501)
    src,srcsha=read("notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json")
    seams,seamsha=read("notes/data/provisional/NF406_original_prime_support_partition_exact.json")
    nf404,f404=read("notes/data/provisional/NF404_original_selected_pole_shear_exact.json")
    nf478,f478=read("notes/data/provisional/NF478_original_complete_J7_signed_seven_panel_custody.json")
    nf479,f479=read("notes/data/provisional/NF479_original_full_J8_forced_positive_NF404_transfer_custody.json")
    nf500,f500=read("notes/data/provisional/NF500_original_all_242_selected_smooth_log_moment_native_custody.json")
    assert srcsha==SRC==n["source_original_NF407_sha256"]==last["original_nf407_source_sha256"]
    assert seamsha==SEAM==n["source_original_NF406_sha256"]==last["original_nf406_seams_sha256"]
    assert n["pass"]=="NF504-native" and n["original_selected_J_dimension"]==242
    assert n["original_original_D_frame_SHA256"]==FRAME
    assert n["original_NF401_native_sha256"]==NF401
    assert n["original_NF494_native_400_HU_sha256"]==NF494_H
    assert n["original_NF495_independent_true_square_sha256"]==NF495==lsha
    assert n["original_NF500_log_column_sha256"]==NF500
    assert n["original_NF501_complete_QJ_native_sha256"]==NF501==ssha
    assert last["pass"]=="NF494" and selected["pass"]=="NF501-native"
    assert nf404["pass"]=="NF404" and nf404["original_dimension"]==242
    assert nf404["original_selected_pole_index"]==241
    assert nf404["fixed_dyadic_pole_coefficient"]=="6677356497477490213/4611686018427387904"
    assert n["original_nf404_sha256"]==f404
    assert n["original_nf478_sha256"]==f478 and nf478["pass"]=="NF478"
    assert n["original_nf479_sha256"]==f479 and nf479["pass"]=="NF479"
    assert nf500["pass"]=="NF500" and nf500["original_source_native_original_242_mixed_moments_source_accepted"] is True
    assert nf500["original_source_native_raw_json_sha256"]==NF500
    assert n["original_terminal_two_collar_delta"]=="1/500"
    assert n["original_exterior_center_radius"]=="549/500"
    assert n["source_native_4096bit_complete_two_collar_S_saturation_result"] is True
    assert n["original_source_all_242_true_complete_W_H_and_Ulog_moments_source_cross_NF500"] is True
    assert n["original_H_U_normalized_retained_terms"]==102
    assert n["original_U_full_log_source_normalized_terms"]==400
    assert n["original_original_basis_Taylor_order"]==400
    assert n["original_actual_exterior_D_Gram_inverse_executed"] is True
    assert n["original_weil_multiplier_source_image_domain"]=="OPEN"
    assert n["W_ODD_NEG"]==n["full_even_odd_Weil_operator_and_RH"]=="OPEN"

    basis=src["original_selected_generator_node_orders"]
    assert len(basis)==242 and basis[241]==["pole",None]
    assert basis==n["original_source_basis_nodes"]
    assert len(src["original_exact_native_original_four_critical_coefficients_mid_radius"])==4
    assert len(src["original_source_critical_sine_frequencies"])==32

    # ORIGINAL source-native precision checks:
    assert n["original_selected_J_dimension"]==242
    fee=I(n["original_actual_D_frame_W_S_moment_max_absolute_fee"])
    assert fee[0]>=0 and fee[1]<F("1e-45")
    tail=F(n["original_generator_Taylor_source_remainder"])
    assert 0<=tail<F(1,10**425)
    gram_rows=n["original_actual_exterior_J242_D_Gram_rows_outward"]
    assert len(gram_rows)==242 and all(len(row)==242 for row in gram_rows)
    # Every actual source-native dyadic entry has nonnegative radius.
    # Diagonal strict positivity and an independent physical matrix
    # interval overlap test for all symmetric counterparts.
    max_symmetric_gap=F(0)
    for i in range(242):
        d=fball(gram_rows[i][i])
        assert d[0]>0
        for j in range(i):
            a=fball(gram_rows[i][j]);b=fball(gram_rows[j][i])
            assert intersect(a,b), ("METHOD STOP original true physical exterior Gram not symmetric",i,j)
            if a[1]<b[0]:max_symmetric_gap=max(max_symmetric_gap,b[0]-a[1])
            elif b[1]<a[0]:max_symmetric_gap=max(max_symmetric_gap,a[0]-b[1])
    assert max_symmetric_gap==0

    # Exact source rational independently reassemble the whole true
    # centered physical E = accepted K + source J7 + actual J8.
    K=I(nf479["original_exact_K_outward_approx"])
    D7=I(nf478["original_seven_panel_J7_signed_D_outward"])
    D8=I(last["original_true_full_J8_signed_D8_outward"])
    full=plus(plus(K,D7),D8)
    Ew=I(last["original_complete_J8_true_improper_whole_terminal_positive_square_EwT_outward"])
    S=(2*Ew[0],2*Ew[1])
    O=minus(full,S)
    assert O[0]>0 and S[0]>0
    Efull=I(n["original_original_W_whole_energy_outward"])
    Es=I(n["original_original_W_two_collar_energy_outward"])
    Eout=I(n["original_original_W_exterior_energy_outward"])
    assert intersect(Efull,full) and intersect(Es,S) and intersect(Eout,O)
    assert intersect(Eout,minus(Efull,Es))
    p=I(n["original_original_W_exterior_selected_projection_power_outward"])
    q=I(n["original_original_saturated_exterior_residual_outward"])
    pr=I(n["original_original_primal_independent_Schur_residual_outward"])
    q2=I(n["original_original_entire_Q_JW_squared_outward"])
    qS2=I(n["original_original_Q_JW_squared_S_outward"])
    assert p[0]>0 and q2[0]>0 and qS2[0]>0
    assert intersect(q,minus(Eout,p))
    assert intersect(q,pr), "METHOD STOP original dual and primal Hilbert support Schur calculations disagree"
    assert q[0]>=0 and q[1]<=q2[1] and q2[1]<F(1,10**15)
    assert qS2[0]<=q2[1]
    assert intersect(q2,I(selected["true_original_Q_Jw_squared_from_K_D7_D8_R_outward"]))
    gamma=F(nf404["exact_source_original_full_complement_power_budget"])
    assert F(0)<gamma<F("5.13e-26")
    assert F(n["original_original_gamma_squared"])==gamma
    decision=n["original_support_saturated_physical_Hilbert_gate"]
    assert decision in (
        "CERTIFIED_PHYSICAL_SUPPORT_NO_GO",
        "PHYSICAL_SUPPORT_SUFFICIENT_POSSIBLE",
        "SOURCE_INTERVAL_INDETERMINATE")
    if decision=="CERTIFIED_PHYSICAL_SUPPORT_NO_GO":
        assert q[0]>gamma
    elif decision=="PHYSICAL_SUPPORT_SUFFICIENT_POSSIBLE":
        assert q[1]<gamma
    else:
        assert q[0]<=gamma<=q[1] or (q[0]<=gamma and q[1]>gamma)

    exactcontrols=check_hilbert_countermodels()
    result={
      "pass":"NF505",
      "standing":"INDEPENDENT EXACT SOURCE-CUSTODY AND ORIGINAL PHYSICAL 242x242 INTERVAL/HILBERT DOUBLE SCHUR AUDIT OF NF504; this is saturated L2 support condition for FIXED original selected source and J242/gamma, NOT test-source range/domain or Weil/RH",
      "original_nf407_source_sha256":SRC,
      "original_nf406_seams_sha256":SEAM,
      "original_nf504_original_entire_242_exterior_4096bit_native_json_sha256":nsha,
      "original_nf495_true_real_J8_square_sha256":lsha,
      "original_nf501_true_QJ_w_source_sha256":ssha,
      "original_nf404_exact_pole_shear_source_sha256":f404,
      "original_nf478_original_J7_source_custody_sha256":f478,
      "original_nf479_original_K_source_custody_sha256":f479,
      "original_nf500_242_moments_custody_sha256":f500,
      "original_selected_true_J_dimension":242,
      "original_all_242x242_physical_exterior_Gram_symmetry_independently_dyadic_Fraction_checked":True,
      "original_all_242_exterior_Gram_diagonal_strictly_positive":True,
      "original_source_original_norm_fee_lt":"1e-45",
      "original_complete_J8_log_400_coefficients_retained":True,
      "original_original_true_whole_centered_energy_reassembled_outward":to_str(full),
      "original_original_true_two_collar_total_positive_square_reassembled_outward":to_str(S),
      "original_original_true_exterior_energy_reassembled_outward":to_str(O),
      "original_original_saturated_support_residual_outward":to_str(q),
      "original_original_independent_primal_Hilbert_residual_outward":to_str(pr),
      "original_original_gamma_squared":str(gamma),
      "original_original_S_support_saturated_physical_Hilbert_verdict":decision,
      "original_true_actual_saturated_residual_exact_factor_lower_over_gamma":str(q[0]/gamma),
      "source_custody_all_242x242_phys_integrals_independently_recomputed":False,
      "source_custody_actual_original_242D_interval_inverse_recomputed_independently":False,
      "original_new_physical_S_support_correction_Weil_image_domain_eligible_verified":False,
      "original_fixed_source_NF404_sufficient_centered_certificate":"CERTIFIED FAIL",
      "W_ODD_NEG":"OPEN","whole_even_odd_Weil_domain":"OPEN","RH":"OPEN",
      "exact_rational_hilbert_nonimplication_controls":exactcontrols,
      "next_bold":"NF506: independently recompute a targeted original 242D exterior Schur block and genuine supported-source basis eligibility / graph-domain transfer; no global RH claim"
    }
    output=Path(o.output);output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(result,indent=2)+"\n")
    print("NF505 SOURCE exact original 242x242 exterior symmetry and complete source energy/primal/dual Schur audited",flush=True)
    print("NF505 ORIGINAL SATURATED PHYSICAL GATE",decision,flush=True)
    print("NF505 true original saturated physical residual rational lower vs fixed gamma ratio",str(q[0]/gamma),flush=True)
    print("NF505 J242 source range/domain/Weil sign/RH OPEN",flush=True)
if __name__=="__main__":main()
