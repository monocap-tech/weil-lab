#!/usr/bin/env python3
"""NF501: actual original 242D Hilbert projector coupling for J8 log carrier.

SCOPED numerical experiment: unchanged original source, old physical
Gram/frame, old NF401 signed+pole multiplier column, NF404 pole shear,
NF500 242 actual raw ell mixed moments, NF498 same-source true whole
terminal W/ell and ell norm. Independent CI required; not a Weil
domain/range assertion, RH theorem, or promotion of NF404.

IMPORTANT: smooth phi differs from raw ell by GLOBAL L2 norm <1e-29.
Do NOT transport NF500's loose 1e-28 independent raw-row smoothing
intervals through near-singular raw Gram. First project raw ell with its
1e-75 source intervals, then use contraction ||Q(phi-ell)||<=1e-29
to bound normalized genuine smooth capture. This is condition invariant.
"""
from __future__ import annotations
import argparse,hashlib,json,sys,time
from fractions import Fraction as F
from pathlib import Path
if hasattr(sys,"set_int_max_str_digits"): sys.set_int_max_str_digits(0)
import flint
from flint import arb,arb_mat,ctx
import verify_rpb108_si29_full_J_L2_normalization as phys
from verify_rpb108_original_signed_frame_transport import candidate
from verify_nf374_original_matched_curvature import load,RANK_SHA,PR355_SHA
from verify_nf380_original_archived_signed_dual import interval,FRAME_SHA

NF401_SHA="644337986f62a3f25bb6b2005efc82f517975c84629b32b5ae8d1e5b95614515"
NF500_SHA="7e261d540c8b658bced4b44d1bf998c23ef7f975fc07daa0f30ae6438dcffb05"
NF498_SHA="350593d08381d7b9a1a80f25e2cbc30ead1d3b529fcc977f390eebd50785c569"
SRC="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAM="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"

def read(p):
    b=Path(p).read_bytes()
    return json.loads(b),hashlib.sha256(b).hexdigest()
def ball(pair):
    lo,hi=map(F,pair)
    assert lo<=hi
    return arb(phys.a((lo+hi)/2),phys.a((hi-lo)/2))
def column(items):
    return arb_mat([[x] for x in items])
def report_interval(x):
    return interval(x)

def main(opt):
    t=time.monotonic()
    assert flint.__version__=="0.8.0"
    assert opt.bits>=4096
    ctx.prec=opt.bits
    source,sh=read("notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json")
    seams,ss=read("notes/data/provisional/NF406_original_prime_support_partition_exact.json")
    assert sh==SRC and ss==SEAM
    rank=load(opt.rank,RANK_SHA)
    _=load(opt.source,PR355_SHA)
    old,oldsha=read("notes/data/provisional/NF401_original_242D_selected_column_source_native.json")
    oldreceipt,rcsha=read("notes/data/provisional/NF401_original_242D_execution_receipt.json")
    new,newsha=read(opt.nf500)
    log,logsha=read(opt.nf498)
    last,lastsha=read(opt.nf495)
    nf404,f404=read("notes/data/provisional/NF404_original_selected_pole_shear_exact.json")
    nf478,f478=read("notes/data/provisional/NF478_original_complete_J7_signed_seven_panel_custody.json")
    nf479,f479=read("notes/data/provisional/NF479_original_full_J8_forced_positive_NF404_transfer_custody.json")
    assert oldsha==NF401_SHA==oldreceipt["original_native_json_sha256"]
    assert oldreceipt["native_column_accepted"] is True
    assert old["original_frame_sha256"]==FRAME_SHA and old["original_rank_sha256"]==RANK_SHA
    assert old["original_dimension"]==242 and old["original_pole_restored"] is True
    assert newsha==NF500_SHA and new["pass"]=="NF500-native"
    assert new["original_nf407_source_sha256"]==SRC
    assert new["original_nf406_seams_sha256"]==SEAM
    assert logsha==NF498_SHA and log["pass"]=="NF498"
    assert log["original_nf407_source_sha256"]==SRC
    assert log["original_nf406_seams_sha256"]==SEAM
    assert last["pass"]=="NF494" and last["original_nf407_source_sha256"]==SRC
    assert last["original_nf406_seams_sha256"]==SEAM
    assert nf404["original_selected_pole_index"]==241 and nf404["original_dimension"]==242
    assert nf478["pass"]=="NF478" and nf479["pass"]=="NF479"
    assert nf479["original_nf407_source_sha256"]==SRC
    assert nf478["source_original_nf407_sha256"]==SRC
    assert source["original_dimension"]==242
    assert new["original_242_selected_mixed_moments_computed"] is True
    assert new["original_full_original_selected_242_Gram_inverse_computed"] is False
    assert nf404["fixed_dyadic_pole_coefficient"]=="6677356497477490213/4611686018427387904"

    nodes=[]
    for (freq,maxk),count in zip(rank["original_nodes"],rank["selected_multiplicities"]):
        assert 0<=count<=maxk
        for k in range(count): nodes.append((F(freq),k))
    assert len(nodes)==241 and rank["retained_original_pole"]
    nodes.append((None,None))
    original_basis=[["pole",None] if freq is None else [str(freq),k] for freq,k in nodes]
    assert original_basis==new["original_selected_basis_242_raw_index_order"]
    moments=new["original_selected_242_odd_source_full_two_collar_basis_moments_outward"]
    assert len(moments)==242
    for i,(r,(freq,k)) in enumerate(zip(moments,nodes)):
        assert r["raw_selected_index"]==i
        assert r["original_monomial_order"]==k
        assert r["original_generator"]==("pole" if freq is None else str(freq))
    assert F(new["original_each_raw_selected_moment_analytic_plus_original_dyadic_overcharge"])==F(1,10**75)
    print("NF501 source-custody 242 original moments and old column verified",flush=True)

    J=[phys.pole_terms() if c is None else phys.source_terms(c,k) for c,k in nodes]
    kern=phys.Integrals()
    H=arb_mat(242,242)
    for i in range(242):
        for j in range(i+1):
            H[i,j]=H[j,i]=phys.gram(J[i],J[j],kern)
    D=candidate(H)
    N=D.transpose()*H*D
    row=max(sum((abs(N[i,j]-int(i==j)) for j in range(242)),arb(0)) for i in range(242))
    assert row<arb("0.01")
    digest=hashlib.sha256()
    for i in range(242):
        for j in range(242):
            digest.update((json.dumps(phys.dyadic(D[i,j]),separators=(",",":"))+"\n").encode())
    assert digest.hexdigest()==FRAME_SHA, "METHOD STOP: original 242D physical frame changed"
    print("NF501 source original 242 Gram, dyadic frame SHA verified",flush=True)

    d_old=column([ball(pair) for pair in old["original_selected_D_frame_moment_column_outward"]])
    raw_ell=column([ball(r["original_true_raw_log_source_moment_outward"]) for r in moments])
    d_ell=D.transpose()*raw_ell
    x_ell=N.solve(d_ell,algorithm="lu")
    Pell2=(d_ell.transpose()*x_ell)[0,0]
    assert Pell2.lower()>=0, "METHOD STOP: projector source numerical precision"
    restored=H*D*N.solve(d_old,algorithm="lu")
    for i,(lo,hi) in enumerate(old["original_selected_raw_J_basis_moment_column_outward"]):
        a,b=map(F,(lo,hi))
        assert restored[i,0].lower()<=phys.a(b) and restored[i,0].upper()>=phys.a(a),("METHOD STOP NF401 old raw source",i)
    a=phys.a(F(nf404["fixed_dyadic_pole_coefficient"]))
    es=column([int(i==241) for i in range(242)])
    d_center=d_old-a*D.transpose()*H*es
    centered_selected_norm=(d_center.transpose()*N.solve(d_center,algorithm="lu"))[0,0]
    Rlo=F(nf404["original_selected_after_pole_shear_power_lower_exact"])
    Rhi=F(nf404["original_selected_after_pole_shear_power_upper_exact"])
    assert centered_selected_norm.lower()<=phys.a(Rhi)
    assert centered_selected_norm.upper()>=phys.a(Rlo)
    PW_ell=(d_center.transpose()*x_ell)[0,0]
    ell2=ball(log["original_odd_log_carrier_full_two_collar_norm_squared_outward"])
    Well=ball(log["original_odd_log_carrier_full_two_collar_inner_with_w_outward"])
    assert ell2.lower()>0 and Well.upper()<0
    e2=ell2-Pell2
    assert e2.lower()>0, "METHOD STOP: raw orthogonal log carrier norm unresolved"
    qell=Well-PW_ell
    rawcapt=(qell*qell)/e2

    # The SAME original pole-centered W has source-accepted squared
    # power Ecent=K+D7+D8, and the original selected R_a² is exact.
    # Do not silently replace those with detached 18k-image Gram data.
    Klo,Khi=map(F,nf479["original_exact_K_outward_approx"])
    D7lo,D7hi=map(F,nf478["original_seven_panel_J7_signed_D_outward"])
    D8lo,D8hi=map(F,last["original_true_full_J8_signed_D8_outward"])
    q2=ball([Klo+D7lo+D8lo-Rhi,Khi+D7hi+D8hi-Rlo])
    assert q2.lower()>0, "METHOD STOP: source Qw squared norm enclosure"
    gamma2=phys.a(F(nf404["exact_source_original_full_complement_power_budget"]))
    assert 0<gamma2.lower()<gamma2.upper()+arb("1e-200")
    # Use global Hilbert contraction, NOT the dangerous individually
    # padded 1e-28 raw-row phi intervals through this ill-conditioned frame.
    eta=phys.a(F(1,10**29))
    norm_q_upper=q2.sqrt().upper()
    norm_e=e2.sqrt()
    assert norm_e.lower()>eta, "METHOD STOP: smooth Q carrier denominator unresolved"
    absinner=abs(qell)
    lower=absinner.lower()-norm_q_upper*eta
    if lower<0:lower=arb(0)
    upper=absinner.upper()+norm_q_upper*eta
    smoothcap_lo=(lower/(norm_e.upper()+eta))**2
    smoothcap_hi=(upper/(norm_e.lower()-eta))**2
    assert smoothcap_lo.lower()>=0 and smoothcap_lo.lower()<=smoothcap_hi.upper()
    res_lo=q2.lower()-smoothcap_hi.upper()
    res_hi=q2.upper()-smoothcap_lo.lower()
    decision=("CERTIFIED_FAIL" if res_lo>gamma2.upper()
              else "CERTIFIED_PASS_SUFFICIENT_HILBERT_GATE" if res_hi<gamma2.lower()
              else "INDETERMINATE_WITH_CURRENT_CORRELATED_SOURCE_INTERVALS")
    print("NF501 actual original Q_J ell squared:",interval(e2),flush=True)
    print("NF501 actual original <Q_Jw,Q_Jell>:",interval(qell),flush=True)
    print("NF501 actual smooth projected one-ray energy lower:",interval(smoothcap_lo),flush=True)
    print("NF501 actual smooth projected one-ray energy upper:",interval(smoothcap_hi),flush=True)
    print("NF501 source-dependent original residual sufficient gate:",decision,flush=True)
    out={
        "pass":"NF501-native","standing":"AUTHENTIC original 242D physical frame all original 242 log cross moments plus original NF401 old w, source terminal log raw and smooth global L2 transport; operator/image/domain and RH OPEN",
        "original_nf401_SHA256":oldsha,"original_nf500_SHA256":newsha,
        "original_nf498_SHA256":logsha,"original_nf495_SHA256":lastsha,
        "original_nf404_SHA256":f404,"original_nf478_SHA256":f478,"original_nf479_SHA256":f479,
        "original_nf407_source_SHA256":SRC,"original_nf406_seams_SHA256":SEAM,
        "original_physical_frame_SHA256":FRAME_SHA,
        "original_J242_Gram_frame_identity_verified":True,
        "original_source_selected_raw_moments_verified":242,
        "original_selected_pole_centered_energy_compatible":True,
        "true_original_P_J_ell_squared_outward":report_interval(Pell2),
        "true_original_Q_J_ell_squared_outward":report_interval(e2),
        "true_original_P_J_centered_w_inner_ell_outward":report_interval(PW_ell),
        "true_original_Q_J_centered_w_inner_Qell_outward":report_interval(qell),
        "true_original_raw_Qell_one_ray_captured_energy_outward":report_interval(rawcapt),
        "true_original_Q_Jw_squared_from_K_D7_D8_R_outward":report_interval(q2),
        "original_global_L2_smoothing_error_eta_upper":"1e-29",
        "smooth_true_QJ_phi_one_ray_captured_power_lower_outward":report_interval(smoothcap_lo),
        "smooth_true_QJ_phi_one_ray_captured_power_upper_outward":report_interval(smoothcap_hi),
        "smooth_true_QJw_after_one_ray_residual_lower_outward":report_interval(res_lo),
        "smooth_true_QJw_after_one_ray_residual_upper_outward":report_interval(res_hi),
        "original_gamma_squared":str(F(nf404["exact_source_original_full_complement_power_budget"])),
        "original_projected_one_ray_sufficient_Hilbert_gate":decision,
        "full_Weil_source_multiplier_image_eligibility":False,
        "full_even_odd_Weil_operator_graph_domain":"OPEN",
        "W_ODD_NEG":"OPEN","RH":"OPEN",
        "duration_seconds":round(time.monotonic()-t,3)
    }
    Path(opt.output).write_text(json.dumps(out,indent=2)+"\n")
if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--nf500",required=True)
    ap.add_argument("--nf498",required=True)
    ap.add_argument("--nf495",required=True)
    ap.add_argument("--rank",default="notes/data/provisional/parents/pr350_original_BS_pruned_rank_bound.json")
    ap.add_argument("--source",default="notes/data/provisional/nf372_pr355_fields.json")
    ap.add_argument("--bits",type=int,default=4096)
    ap.add_argument("--output",required=True)
    main(ap.parse_args())
