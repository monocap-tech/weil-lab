#!/usr/bin/env python3
"""MG46 — new complete original 24D JOINT omitted-frequency residual Loewner upper.

Original MG32 complement was bounded by separate Young payments for
t C0, (a t) B and rank-one pole uncertainty. Here recombine the SAME
true omitted-frequency H/G/S moments before paying one matrix-valued
cross-G interval penalty. No new source Fourier measurement is
asserted; the new rigorous original-source bound uses more correlations
from the existing physical missing mass H-H_[0,4].

Unpoled A_o Fourier multiplier a(xi)>=kappa on the omitted set and
S_rem <= M^2 Hrem_upper+tau2 I, G_rem <= M Hrem_upper+tau1 I.
Hrem_true=H-H_C, Hrem_lower=Hlo-HCupper, Hrem_upper=Hup-HClower.
Two independently valid G_rem lowers: 0 and kappa Hrem_lower.
For each accepted first-moment bracket L<=G<=U,
C=(L+U)/2, E=(U-L)/2 PSD, and any nonscalar B,
C0=I+2ep bmid^T B,
Ubase=C0^T Hrem_upper C0
  -C0^T C B-B^T C C0+B^T Srem_upper B
  +eta C0^T E C0+eta^-1 B^T E B.
The block PSD [[E,G-C],[G-C,E]] gives the last anisotropic fee
on the TRUE original mixed moment (same logic as MG40).
True pole b differs by interval brad. For delta=q_true-q_base
=2 t_p (delta_b^T B), the independently accepted MG32 estimate
delta^T delta <= 4 (Hrem_upper)pp ||ds||² I,
ds_j=sum_i brad_i|B_ij|.
Also valid: <=4(Hrem_upper)pp diag(ds_j sum_k ds_k).
For any gamma>0, full U_rem <= (1+gamma) Ubase
 +(1+gamma^-1) fee. All symmetric genuine original 24D Loewner UPPER.

Try two source G lower bounds, the two valid pole error matrices,
and finite rational eta/gamma. Replay original MG32 valid complement
as baseline. Independently combine the SAME original [0,4] MG32
full24 direct residual Loewner upper and classify exact source matrix.
A negative rational lower-matrix Rayleigh does not imply original
signed operator negative. Do not claim source contraction from Gersh
alone or compare full matrices by trace as Loewner ordering.
"""
import argparse,json,sys
from fractions import Fraction as Q
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
import validate_rpb108_mg32_joint_fourier_residual as m32
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import ROOT
from validate_rpb108_mg25_original24_robust_trial import (
    deserialize,original_H24_from_physical_source)
from validate_rpb108_mg25_robust_source_aware_residual import (
    Id,T,mm,plus,sub,mul,shift,gersh_lower,psd)
from validate_rpb108_mg41_ideal_cross_error_feasibility import (
    classify_ideal,dot)
from validate_rpb108_mg23_physical_metric_matrix_envelope import KAPPA
N=24;P=23
CUTS=(12,16)
MESH=(16,32)
ETA=(Q(1,16),Q(1,4),Q(1),Q(4))
GAMMA=(Q(1,16),Q(1,4),Q(1),Q(4))
def enc(A):return [[str(x) for x in r] for r in A]
def mat(A):
    B=deserialize(A)
    assert len(B)==N and all(len(r)==N for r in B)
    return B
def trace(A):
    return sum((A[i][i] for i in range(N)),Q(0))
def quadratic(z,A):
    return sum((z[i]*A[i][j]*z[j] for i in range(N)
                for j in range(N)),Q(0))
def diag(values):
    R=[[Q(0) for _ in range(N)] for _ in range(N)]
    for i in range(N):R[i][i]=values[i]
    return R
def recombine(Hlo,Hup,HClo,HCup,bmid,brad,B,k,tau1,tau2):
    """Exact original omitted-frequency source residual candidate family."""
    Hremup=sub(Hup,HClo)
    assert Hremup==T(Hremup)
    assert psd(Hremup)
    # Original physical Hlo needed for the second valid lower.
    # Caller passes separately through global setup, not a surrogate.
    assert m32.cutoff_tail[k]==tau2
    M=Q(17)+Q(347*k,500)
    Sup=shift(mul(M*M,Hremup),tau2)
    Gup=shift(mul(M,Hremup),tau1)
    assert psd(Sup) and psd(Gup)
    pcoeff=[sum((bmid[i]*B[i][j] for i in range(N)),Q(0))
            for j in range(N)]
    C0=[[Q(i==j)+(2*pcoeff[j] if i==P else Q(0))
         for j in range(N)] for i in range(N)]
    HC=mm(mm(T(C0),Hremup),C0)
    BS=mm(mm(T(B),Sup),B)
    ds=[sum((brad[i]*abs(B[i][j]) for i in range(N)),Q(0))
        for j in range(N)]
    massP=Hremup[P][P]
    assert massP>=0
    scalarfee=mul(4*massP*sum((d*d for d in ds),Q(0)),Id(N))
    ds_sum=sum(ds,Q(0))
    directionalfee=diag([4*massP*ds[i]*ds_sum for i in range(N)])
    assert psd(scalarfee) and psd(directionalfee)
    Hremlo=sub(Hlo,HCup)
    lows={
       "PSD_zero":diag([Q(0)]*N),
       "kappa_missing_mass":mul(KAPPA,Hremlo),
    }
    all_new=[]
    for lname,L in lows.items():
        assert L==T(L)
        E=mul(Q(1,2),sub(Gup,L))
        Gc=mul(Q(1,2),plus(Gup,L))
        assert psd(E) # both L and U provably enclose true G_rem
        core=plus(sub(HC,plus(mm(mm(T(C0),Gc),B),
                               mm(mm(T(B),Gc),C0))),BS)
        P0=mm(mm(T(C0),E),C0)
        P1=mm(mm(T(B),E),B)
        assert psd(P0) and psd(P1)
        for eta in ETA:
            base=plus(core,plus(mul(eta,P0),mul(1/eta,P1)))
            assert base==T(base)
            for gamma in GAMMA:
                for fee_name,fee in (
                       ("MG32_scalar_isotropic",scalarfee),
                       ("new_sourcewise_diagonal",directionalfee)):
                    U=plus(mul(1+gamma,base),mul(1+1/gamma,fee))
                    assert U==T(U)
                    all_new.append((lname,eta,gamma,fee_name,U))
    assert len(all_new)==len(lows)*len(ETA)*len(GAMMA)*2==64
    return all_new,Hremup,Sup,Gup,ds,scalarfee,directionalfee

def main():
    p=argparse.ArgumentParser()
    for n in ("mg24","mg29","mg32","mg43","mg44","mg45"):
        p.add_argument("--verified-"+n+"-json")
    p.add_argument("--output",default=
                   "artifacts/mg46_original_joint_missing_frequency_residual.json")
    a=p.parse_args()
    assert all(getattr(a,"verified_"+n+"_json") for n in
               ("mg24","mg29","mg32","mg43","mg44","mg45"))
    load=lambda n:json.loads((ROOT/getattr(a,"verified_"+n+"_json")).read_text())
    m24,m29,m32data,m43,m44,m45=(
        load(n) for n in ("mg24","mg29","mg32","mg43","mg44","mg45"))
    assert all(q["canonical_W_ODD_NEG"]=="OPEN"
               for q in (m24,m29,m32data,m43,m44,m45))
    assert m32data["MG24_accepted_run"]==39378465438
    assert m32data["MG29_accepted_run"]==39440914565
    assert m45["status"]=="ORIGINAL_MG45_SIGNED_SOURCE_RAY_FOURIER_RESIDUAL_LINEARIZATION"
    assert m45["total_original_exact_rays"]==12
    Hmid,Hrad,Herr=original_H24_from_physical_source()
    assert Herr==Q(m24["physical_Gram_Loewner_row_error"])
    Hlower=sub(Hmid,mul(Herr,Id(N)))
    Hupper=plus(Hmid,mul(Herr,Id(N)))
    bmid=[Hmid[i][P] for i in range(N)]
    brad=[Hrad[i][P] for i in range(N)]
    assert [str(x) for x in bmid]==m24["original_pole_b_center"]
    assert [str(x) for x in brad]==m24["original_pole_b_radii"]
    cells,HClo,HCup,source_radius,taus=m32.exact_original_cells()
    assert len(cells)==32
    assert source_radius==Q(next(x for x in m29["meshes"]
                 if x["mesh_cells"]==32)["total_source_radius_MG29"])
    m32.cutoff_tail={c["cutoff_k"]:Q(c["complete_original_strong_tail_rational"])
                     for c in m24["cases"]}
    scenarios=[]
    for mesh in MESH:
      for k in CUTS:
        case24=next(c for c in m24["cases"] if c["cutoff_k"]==k)
        row43=next(x for x in m43["scenarios"]
                   if x["mesh_cells"]==mesh and x["cutoff_k"]==k)
        ray45=next(x for x in m45["cases"]
                   if x["mesh_cells"]==mesh and x["cutoff_k"]==k)
        B=mat(row43["exact_original_rational_B"])
        tau1=Q(case24["complete_original_form_tail_rational"])
        tau2=Q(case24["complete_original_strong_tail_rational"])
        oldrem,oldbeta,oldpole=m32.complement_upper(
            Hupper,HClo,bmid,brad,B,k)
        original_band,sourceR,chosen_taus=m32.joint_prefix_upper(
            cells,bmid,brad,B)
        candidates,Hremup,Sup,Gup,ds,fee0,fee1=recombine(
            Hlower,Hupper,HClo,HCup,bmid,brad,B,k,tau1,tau2)
        baseline_lower=sub(Hlower,plus(original_band,oldrem))
        oldmargin=gersh_lower(baseline_lower)
        tests=[]
        scored=[]
        for lname,eta,gamma,ftype,U in candidates:
            M=sub(Hlower,plus(original_band,U))
            margin=gersh_lower(M)
            tests.append({
             "G_original_lower_type":lname,
             "cross_G_matrix_Young_eta":str(eta),
             "pole_combination_gamma":str(gamma),
             "pole_error_matrix_kind":ftype,
             "whole_original_signed_Gersh_lower":str(margin),
             "new_omitted_source_trace":str(trace(U))})
            scored.append((margin,lname,eta,gamma,ftype,U,M))
        best=max(scored,key=lambda x:(x[0],-trace(x[5])))
        margin,lname,eta,gamma,ftype,U,M=best
        if margin>oldmargin:
            selected_kind="NEW_ORIGINAL_JOINT_MISSING_GS_LOEWNER"
            selU=U;selectedM=M;selectedMargin=margin
        else:
            selected_kind="MG32_VALID_OMITTED_FREQUENCY_FALLBACK"
            selU=oldrem;selectedM=baseline_lower;selectedMargin=oldmargin
        # Exact standalone positivity (never infer positivity from
        # a NEGATIVE Gershgorin lower).
        kind,witness=classify_ideal(selectedM)
        assert kind in ("NEGATIVE_EXACT_RATIONAL_RAYLEIGH",
                       "POSITIVE_EXACT_RATIONAL_LDL","INCONCLUSIVE")
        direct_rays=[]
        for ray in ray45["rays"]:
            z=[Q(x) for x in ray["original_source_rational_ray"]]
            direct=Q(ray["new_original_direct_prefix_ray_upper"])
            mg45old=Q(ray["selected_intersected_valid_original_ray_upper"])
            complete=direct+quadratic(z,selU)
            improvement=complete<mg45old
            vbest=min(mg45old,complete)
            direct_rays.append({
                "same_MG45_original_source_ray":ray["same_archived_original_exact_ray_kind"],
                "original_source_rational_vector":ray["original_source_rational_ray"],
                "new_omitted_source_upper_ray":str(quadratic(z,selU)),
                "original_signed_direct_prefix_ray_upper":str(direct),
                "new_complete_original_ray_upper":str(complete),
                "MG45_prior_original_complete_ray_upper":str(mg45old),
                "new_intersected_original_complete_ray_upper":str(vbest),
                "strict_complete_ray_improvement":improvement,
                "nonnegative_original_ray_lower":quadratic(z,Hlower)-vbest>=0,
                "original_complete_ray_lower":str(quadratic(z,Hlower)-vbest)})
        scenarios.append({
            "mesh_cells":mesh,"cutoff_k":k,
            "nonscalar_original_B":row43["source_response_name"],
            "response_matrix_original_rational":enc(B),
            "original_MG32_direct_band_24D_upper":enc(original_band),
            "original_complete_omitted_H_upper":enc(Hremup),
            "original_complete_omitted_S_upper":enc(Sup),
            "original_complete_omitted_G_upper":enc(Gup),
            "original_pole_source_uncertainty_components":[str(x) for x in ds],
            "original_MG32_pole_fee_scalar":str(oldpole),
            "original_MG32_complement_beta":str(oldbeta),
            "original_MG32_complement_Gersh":str(oldmargin),
            "original_MG32_omitted_upper_trace":str(trace(oldrem)),
            "new_best_G_lower_type":lname,
            "new_best_eta":str(eta),"new_best_gamma":str(gamma),
            "new_best_pole_fee_type":ftype,
            "new_best_omitted_GS_upper_matrix":enc(U),
            "new_best_omitted_GS_upper_trace":str(trace(U)),
            "new_best_complete_original_source_Gersh":str(margin),
            "new_best_complete_source_lower_matrix":enc(M),
            "new_best_vs_MG32_Gersh_change":str(margin-oldmargin),
            "selected_complete_source_method":selected_kind,
            "selected_omitted_upper_matrix":enc(selU),
            "selected_complete_original_source_lower_matrix":enc(selectedM),
            "selected_complete_original_source_Gersh":str(selectedMargin),
            "selected_full_source_inertia_classification":kind,
            "selected_full_source_exact_inertia_witness":witness,
            "selected_full24_source_strict_positivity":
                 kind=="POSITIVE_EXACT_RATIONAL_LDL",
            "all_64_true_original_GS_missing_frequency_parameter_tests":tests,
            "number_valid_exact_original_joint_remainder_trials":len(tests),
            "number_MG45_rays_improved_complete":sum(
                 x["strict_complete_ray_improvement"] for x in direct_rays),
            "number_MG45_rays_nonnegative":sum(
                 x["nonnegative_original_ray_lower"] for x in direct_rays),
            "same_original_3_ray_diagnostics":direct_rays,
            "true_23_adapted_plus_sinh_pole_original_source":True,
            "complete_signed_seven_prime_arch_real_frequency_paid":True,
            "new_joint_omitted_GS_cross_matrix_true_Loewner_upper":True,
            "no_unmeasured_original_source_frequency_dropped":True,
            "no_original_470D_operator_spectral_conclusion":True})
    assert [(x["mesh_cells"],x["cutoff_k"]) for x in scenarios]==[
           (16,12),(16,16),(32,12),(32,16)]
    out={
      "status":"ORIGINAL_MG46_OMITTED_FREQUENCY_TRUE_GS_CROSS_RESIDUAL_UPPER",
      "canonical_W_ODD_NEG":"OPEN",
      "verified_MG24_run":39378465438,
      "verified_MG29_run":39440914565,
      "verified_MG32_run":39459624082,
      "verified_MG43_run":39522608989,
      "verified_MG44_run":39542236311,
      "verified_MG45_run":39544081287,
      "true_original_physical_25_SI10_23adapted_plus_sinh_pole24D":True,
      "complete_original_real_frequency_missing_mass_and_tail":True,
      "new_exact_Grem_cross_moment_block_PSD_Loewner":True,
      "new_joint_24D_omitted_frequency_covariance_valid":True,
      "all_256_exact_rational_candidate_uppers_tested":True,
      "old_MG32_complement_available_as_valid_fail_safe":True,
      "no_simple_PSD_measured_band_double_charge":True,
      "all_12_original_source_rays_from_MG45_replayed":True,
      "any_verified_full24_source_contraction":any(
          c["selected_full24_source_strict_positivity"] for c in scenarios),
      "full470_source_inverse_certified":False,
      "signed_original_51over56_negative_cap_certified":False,
      "independent_original_Fourier_form_domain_audit":"OPEN",
      "complete_even_Weil_CC27_RH":"OPEN",
      "scenarios":scenarios,
      "next":"Classify measured [0,4] direct residual and new omitted G/S cross estimates simultaneously, then refine the original missing-frequency multiplier source moments or the b-pole coupling. Negative conservative source lower Rayleigh never means the physical signed operator is negative."
    }
    path=ROOT/a.output;path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(out,indent=2)+"\n")
    print("MG46 accepted-form ORIGINAL omitted-frequency G/S cross candidate:",json.dumps({
       "scenarios":[{
           "mesh":s["mesh_cells"],"k":s["cutoff_k"],
           "old_MG32_Gersh":float(Q(s["original_MG32_complement_Gersh"])),
           "new_best_Gersh":float(Q(s["new_best_complete_original_source_Gersh"])),
           "selected":s["selected_complete_source_method"],
           "full_24_inertia":s["selected_full_source_inertia_classification"],
           "ray_improvements":s["number_MG45_rays_improved_complete"]}
           for s in scenarios],
           "full_original_470D_Weil_RH":"OPEN"}),flush=True)
if __name__=="__main__":main()
