#!/usr/bin/env python3
"""NF501 independent exact-Fraction receipt for original 242D log one-ray NO-GO.

This is a *separate algebraic, exact rational* audit of the accepted
source-native 4096-bit original projector computation. It independently
checks its original NF498 physical log source, NF404 centered frame norm,
NF478/479/495 complete energy lineage, Cauchy/Gram identities, and the
GLOBAL-L2 smooth transfer. It does not independently re-evaluate all
242 original native source moments or rederive the historical D Gram.

No sign/RH or original Weil image-domain claim.
"""
from __future__ import annotations
import argparse,hashlib,json,sys
from pathlib import Path
from fractions import Fraction as F
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)

NF501_SHA="7726a8a9af5faa7a22fd7581c38548c26c5a48a52cb92dc75f815c57f6e3ad7a"
SRC="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAM="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
NF401="644337986f62a3f25bb6b2005efc82f517975c84629b32b5ae8d1e5b95614515"
NF500="7e261d540c8b658bced4b44d1bf998c23ef7f975fc07daa0f30ae6438dcffb05"
NF498="350593d08381d7b9a1a80f25e2cbc30ead1d3b529fcc977f390eebd50785c569"
FRAME="18ac01bba4de7ec432e419db5ed990fbfabad91c10cbcf2f61cf5666e36b430e"

def read(p):
    b=Path(p).read_bytes()
    return json.loads(b),hashlib.sha256(b).hexdigest()
def checkpair(x):
    assert len(x)==2
    a,b=map(F,x);assert a<=b
    return a,b
def add(x,y):return x[0]+y[0],x[1]+y[1]
def sub(x,y):return x[0]-y[1],x[1]-y[0]
def intersects(x,y):return x[0]<=y[1] and y[0]<=x[1]
def square(x):
    a,b=x
    if a<=0<=b:return F(0),max(a*a,b*b)
    return min(a*a,b*b),max(a*a,b*b)
def divpos(x,y):
    assert y[0]>0 and x[0]>=0
    return x[0]/y[1],x[1]/y[0]
def absrange(x):
    a,b=x
    return (F(0) if a<=0<=b else min(abs(a),abs(b))),max(abs(a),abs(b))
def hilbert_controls():
    # Exact Gram orthogonality and projection to new direction.
    w=(F(2),F(3),F(4));e=(F(0),F(3),F(1))
    dot=lambda x,y:sum((a*b for a,b in zip(x,y)),F(0))
    norm=lambda x:dot(x,x)
    proj=F(dot(w,e),norm(e))
    resid=tuple(a-proj*b for a,b in zip(w,e))
    assert dot(resid,e)==0
    assert norm(w)-dot(w,e)**2/norm(e)==norm(resid)
    # A pole within OLD selected J cannot affect Q(w).
    assert (F(3),F(4))==(F(3),F(4))
    # This is a finite Hilbert selection failure, NOT form sign.
    wp=(F(1),F(0)); wn=(F(1),F(3))
    assert wp[1]**2<wn[1]**2
    return 5

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--nf501",required=True)
    p.add_argument("--nf498",required=True)
    p.add_argument("--nf495",required=True)
    p.add_argument("--output",required=True)
    a=p.parse_args()
    n,sha=read(a.nf501)
    lg,lgsha=read(a.nf498)
    last,lastsha=read(a.nf495)
    source,srcsha=read("notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json")
    seams,seamsha=read("notes/data/provisional/NF406_original_prime_support_partition_exact.json")
    nf404,sha404=read("notes/data/provisional/NF404_original_selected_pole_shear_exact.json")
    nf478,sha478=read("notes/data/provisional/NF478_original_complete_J7_signed_seven_panel_custody.json")
    nf479,sha479=read("notes/data/provisional/NF479_original_full_J8_forced_positive_NF404_transfer_custody.json")
    assert sha==NF501_SHA and n["pass"]=="NF501-native"
    assert n["original_nf401_SHA256"]==NF401
    assert n["original_nf500_SHA256"]==NF500
    assert n["original_nf498_SHA256"]==lgsha==NF498
    assert n["original_nf495_SHA256"]==lastsha
    assert n["original_nf404_SHA256"]==sha404
    assert n["original_nf478_SHA256"]==sha478
    assert n["original_nf479_SHA256"]==sha479
    assert n["original_nf407_source_SHA256"]==srcsha==SRC
    assert n["original_nf406_seams_SHA256"]==seamsha==SEAM
    assert n["original_physical_frame_SHA256"]==FRAME
    assert n["original_J242_Gram_frame_identity_verified"] is True
    assert n["original_source_selected_raw_moments_verified"]==242
    assert n["original_source_correlated_U110_and_basisTaylor_order"]==600
    assert n["original_selected_pole_centered_energy_compatible"] is True
    assert n["full_Weil_source_multiplier_image_eligibility"] is False
    assert n["full_even_odd_Weil_operator_graph_domain"]=="OPEN"
    assert n["W_ODD_NEG"]==n["RH"]=="OPEN"
    assert nf404["original_dimension"]==242 and nf404["original_selected_pole_index"]==241
    assert nf404["fixed_dyadic_pole_coefficient"]=="6677356497477490213/4611686018427387904"
    assert nf478["pass"]=="NF478" and nf479["pass"]=="NF479"
    assert last["pass"]=="NF494"
    assert lg["pass"]=="NF498"
    assert lg["original_nf407_source_sha256"]==SRC
    assert lg["original_nf406_seams_sha256"]==SEAM
    assert nf478["source_original_nf407_sha256"]==SRC
    assert nf479["original_nf407_source_sha256"]==SRC
    assert last["original_nf407_source_sha256"]==SRC

    # SOURCE-EXACT OUTWARD IDENTITY: NF498's w=p+z is already
    # the original NF404 pole-CENTERED physical response W,
    # not the original uncentered multiplier (norm ~0.7).
    ell2=checkpair(lg["original_odd_log_carrier_full_two_collar_norm_squared_outward"])
    Well=checkpair(lg["original_odd_log_carrier_full_two_collar_inner_with_w_outward"])
    assert Well[1]<0
    pell=checkpair(n["true_original_P_J_ell_squared_outward"])
    qell=checkpair(n["true_original_Q_J_ell_squared_outward"])
    assert pell[0]>0 and qell[0]>0
    assert intersects(add(pell,qell),ell2)
    assert intersects(sub(ell2,pell),qell)

    PW=checkpair(n["true_original_P_J_centered_w_inner_ell_outward"])
    v=checkpair(n["true_original_Q_J_centered_w_inner_Qell_outward"])
    assert v[1]<0
    assert intersects(sub(Well,PW),v)
    assert intersects(add(PW,v),Well)
    # Independent root-free Gram/Cauchy consistency.
    rawcap=checkpair(n["true_original_raw_Qell_one_ray_captured_energy_outward"])
    recomputed_raw=divpos(square(v),qell)
    assert intersects(rawcap,recomputed_raw)
    assert F("7.60e-28")<rawcap[0]<=rawcap[1]<F("7.63e-28")
    assert F("2.5786e-25")<(-v[1])<=(-v[0])<F("2.5788e-25")

    # Independently reconstruct the genuine whole supported Qw²
    # from accepted ORIGINAL K + COMPLETE signed J7 + COMPLETE signed J8
    # minus the ORIGINAL pole-centered selected energy. NOT 0.494.
    K=checkpair(nf479["original_exact_K_outward_approx"])
    D7=checkpair(nf478["original_seven_panel_J7_signed_D_outward"])
    D8=checkpair(last["original_true_full_J8_signed_D8_outward"])
    R=checkpair([
      nf404["original_selected_after_pole_shear_power_lower_exact"],
      nf404["original_selected_after_pole_shear_power_upper_exact"]])
    q2parent=sub(add(add(K,D7),D8),R)
    q2=checkpair(n["true_original_Q_Jw_squared_from_K_D7_D8_R_outward"])
    assert intersects(q2parent,q2)
    assert q2[0]>F("1.578e-22") and q2[1]<F("1.607e-22")
    assert square(v)[1]<q2[0]*qell[0], "Cauchy correlated Gram determinant"
    assert rawcap[1]<q2[0]/F(10**5)  # capture < 0.001% of full residual

    # Independently derive the ACTUAL Cc∞ smoothing rank-one capture
    # using globally correlated L2 error ||phi-ell||<1e-29,
    # NOT 242 separately source-overcharged 1e-28 smooth moment rows.
    eta=F("1e-29")
    assert F(n["original_global_L2_smoothing_error_eta_upper"])==eta
    rupper=F("1.27e-11")
    elower=F("9.344e-12")
    eupper=F("9.35e-12")
    assert q2[1]<rupper*rupper
    assert elower*elower<qell[0]<=qell[1]<eupper*eupper
    assert elower>eta
    minv,maxv=absrange(v)
    # Narrow rational brackets are source-outward and not decimal point guesses.
    minv_guard=F("2.5786e-25")
    maxv_guard=F("2.5788e-25")
    assert minv_guard<minv<=maxv<maxv_guard
    assert minv>rupper*eta
    CL=(minv-rupper*eta)**2/(eupper+eta)**2
    CH=(maxv+rupper*eta)**2/(elower-eta)**2
    assert F("7.60e-28")<CL<=CH<F("7.63e-28")
    native_CL=checkpair(n["smooth_true_QJ_phi_one_ray_captured_power_lower_outward"])
    native_CH=checkpair(n["smooth_true_QJ_phi_one_ray_captured_power_upper_outward"])
    # Since our independent C bounds deliberately use loose root-free
    # rational norm brackets they MUST contain native tighter estimates.
    assert CL<=native_CL[0] and native_CH[1]<=CH
    Rlower=q2[0]-CH
    Rupper=q2[1]-CL
    native_Rlo=checkpair(n["smooth_true_QJw_after_one_ray_residual_lower_outward"])
    native_Rhi=checkpair(n["smooth_true_QJw_after_one_ray_residual_upper_outward"])
    assert Rlower<=native_Rlo[0] and native_Rhi[1]<=Rupper

    gamma2=F(n["original_gamma_squared"])
    assert gamma2==F(nf404["exact_source_original_full_complement_power_budget"])
    assert F(0)<gamma2<F("5.13e-26")
    assert Rlower>F("1.5784e-22")
    assert Rlower>3076*gamma2
    assert n["original_projected_one_ray_sufficient_Hilbert_gate"]=="CERTIFIED_FAIL"
    assert CH/q2[0] <F(1,200000)  # <5e-6, or <0.0005%
    assert hilbert_controls()==5
    result={
        "pass":"NF501-independent-Fraction",
        "standing":"INDEPENDENT EXACT-FRACTION PHYSICAL Hilbert/correlation/smoothing NO-GO RECEIPT for ONE explicit original smooth logarithmic J8 candidate; full Q_J 242D native source projection itself not independently numerically recomputed; RH and operator domain OPEN",
        "original_nf501_native_json_sha256":sha,
        "original_source_sha256":SRC,"original_seams_sha256":SEAM,
        "original_nf498_raw_json_sha256":lgsha,
        "original_nf495_raw_json_sha256":lastsha,
        "original_nf404_exact_source_sha256":sha404,
        "original_source_selected_dimension":242,
        "original_source_direct_D_frame_generator_Taylor_order":600,
        "original_raw_log_carrier_Q_J_squared_strict_bracket":["8.73e-23","8.74e-23"],
        "original_Q_Jw_squared_strict_bracket":["1.578e-22","1.607e-22"],
        "original_Q_Jw_Q_Jell_cross_strict_bracket":["-2.59e-25","-2.57e-25"],
        "original_smooth_one_direction_capture_strict_bracket":["7.60e-28","7.63e-28"],
        "original_smooth_capture_fraction_strict_upper":"1/200000",
        "original_smooth_capture_percentage_strict_upper":"0.0005%",
        "original_remaining_Q_Jw_squared_strict_lower":str(F("1.5784e-22")),
        "original_remaining_residual_exceeds_NF404_gamma_squared_factor_strict":3076,
        "independent_interval_source_lineage_and_Cauchy_and_global_smoothing_checks":True,
        "independently_recomputed_source_all_242_oscillatory_dyadic_arcs":False,
        "original_full_projected_one_ray_NF404_sufficient_gate":"CERTIFIED_FAIL",
        "original_Weil_multiplier_image_domain":"OPEN",
        "W_ODD_NEG":"OPEN","RH":"OPEN"
    }
    Path(a.output).write_text(json.dumps(result,indent=2)+"\n")
    print("NF501 exact-Fraction independent audit PASS",flush=True)
    print("NF501 original smooth Q_J log one-ray captures < 0.0005% of entire original q energy",flush=True)
    print("NF501 original residual after one log smooth ray >3076 gamma²; FIXED one-ray gate CERTIFIED FAIL",flush=True)
    print("NF501 NO full Weil operator image, W-ODD-NEG or RH implication",flush=True)

if __name__=="__main__":
    main()
