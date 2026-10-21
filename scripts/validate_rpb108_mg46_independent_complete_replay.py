#!/usr/bin/env python3
"""Independent MG46 verification: NO import of MG46 candidate constructor.

Recalculate actual original [0,4] physical 24D joint-source residual
and all 256 new complete original frequency remainder matrix candidates.
Use independent matrix formula from original true H/G/S source moments,
including original pole-error scalar/diagonal PSD Young bound. Check
entire selected lower matrix inertia by exact Fraction rational LDL/ray.
"""
import argparse,json,sys
from fractions import Fraction as Q
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
import validate_rpb108_mg32_joint_fourier_residual as mg32
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import ROOT
from validate_rpb108_mg25_original24_robust_trial import (
    deserialize, original_H24_from_physical_source)
from validate_rpb108_mg25_robust_source_aware_residual import (
    Id,T,mm,plus,sub,mul,shift,gersh_lower,psd)
from validate_rpb108_mg23_physical_metric_matrix_envelope import KAPPA
N=24
def read(A):
    B=deserialize(A)
    assert len(B)==N and all(len(r)==N for r in B)
    return B
def tr(A):
    return sum((A[i][i] for i in range(N)),Q(0))
def qf(z,A):
    return sum((z[i]*A[i][j]*z[j] for i in range(N)
                for j in range(N)),Q(0))
def identity_diagonal(values):
    A=[[Q(0)]*N for _ in range(N)]
    for i in range(N):A[i][i]=values[i]
    return A
def exact_ldl(A):
    assert A==T(A)
    W=[list(r) for r in A];pivots=[]
    for k in range(N):
        d=W[k][k]
        if d<=0:return None
        pivots.append(d)
        for i in range(k+1,N):
            for j in range(i,N):
                W[j][i]-=W[i][k]*W[j][k]/d
                W[i][j]=W[j][i]
    return pivots
def main():
    ap=argparse.ArgumentParser()
    for n in ("mg24","mg29","mg32","mg43","mg44","mg45","mg46"):
        ap.add_argument("--verified-"+n+"-json",required=True)
    args=ap.parse_args()
    src={n:json.loads((ROOT/getattr(args,"verified_"+n+"_json")).read_text())
         for n in ("mg24","mg29","mg32","mg43","mg44","mg45","mg46")}
    d=src["mg46"]
    assert d["status"]=="ORIGINAL_MG46_OMITTED_FREQUENCY_TRUE_GS_CROSS_RESIDUAL_UPPER"
    assert d["canonical_W_ODD_NEG"]=="OPEN"
    assert [d[k] for k in (
        "verified_MG24_run","verified_MG29_run","verified_MG32_run",
        "verified_MG43_run","verified_MG44_run","verified_MG45_run")]==[
          39378465438,39440914565,39459624082,
          39522608989,39542236311,39544081287]
    for key in (
       "true_original_physical_25_SI10_23adapted_plus_sinh_pole24D",
       "complete_original_real_frequency_missing_mass_and_tail",
       "new_exact_Grem_cross_moment_block_PSD_Loewner",
       "new_joint_24D_omitted_frequency_covariance_valid",
       "all_256_exact_rational_candidate_uppers_tested",
       "old_MG32_complement_available_as_valid_fail_safe",
       "no_simple_PSD_measured_band_double_charge",
       "all_12_original_source_rays_from_MG45_replayed"):
        assert d[key],key
    Hmid,Hrad,Herr=original_H24_from_physical_source()
    assert Herr==Q(src["mg24"]["physical_Gram_Loewner_row_error"])
    Hlo=sub(Hmid,mul(Herr,Id(N)))
    Hup=plus(Hmid,mul(Herr,Id(N)))
    b=[Hmid[i][23] for i in range(N)]
    brad=[Hrad[i][23] for i in range(N)]
    assert [str(t) for t in b]==src["mg24"]["original_pole_b_center"]
    assert [str(t) for t in brad]==src["mg24"]["original_pole_b_radii"]
    cells,HClo,HCup,rad,choices=mg32.exact_original_cells()
    assert len(cells)==32
    assert rad==Q(next(x for x in src["mg29"]["meshes"]
        if x["mesh_cells"]==32)["total_source_radius_MG29"])
    mg32.cutoff_tail={
        x["cutoff_k"]:Q(x["complete_original_strong_tail_rational"])
        for x in src["mg24"]["cases"]}
    assert [(x["mesh_cells"],x["cutoff_k"]) for x in d["scenarios"]]==[
        (16,12),(16,16),(32,12),(32,16)]
    count=0;rays=0; positives=0
    for sc in d["scenarios"]:
        k=sc["cutoff_k"];mesh=sc["mesh_cells"]
        c24=next(x for x in src["mg24"]["cases"] if x["cutoff_k"]==k)
        c43=next(x for x in src["mg43"]["scenarios"]
                 if x["mesh_cells"]==mesh and x["cutoff_k"]==k)
        c45=next(x for x in src["mg45"]["cases"]
                 if x["mesh_cells"]==mesh and x["cutoff_k"]==k)
        assert sc["nonscalar_original_B"]==c43["source_response_name"]
        B=read(c43["exact_original_rational_B"])
        assert B==read(sc["response_matrix_original_rational"])
        # original independently pinned physical [0,4] direct
        direct,rl,ta=mg32.joint_prefix_upper(cells,b,brad,B)
        assert direct==read(sc["original_MG32_direct_band_24D_upper"])
        old,beta,fee_old=mg32.complement_upper(Hup,HClo,b,brad,B,k)
        assert sc["original_MG32_complement_beta"]==str(beta)
        assert sc["original_MG32_pole_fee_scalar"]==str(fee_old)
        orig=gersh_lower(sub(Hlo,plus(direct,old)))
        assert orig==Q(sc["original_MG32_complement_Gersh"])
        assert tr(old)==Q(sc["original_MG32_omitted_upper_trace"])
        hrem=sub(Hup,HClo)
        assert hrem==T(hrem) and psd(hrem)
        assert hrem==read(sc["original_complete_omitted_H_upper"])
        M=Q(17)+Q(347*k,500)
        t1=Q(c24["complete_original_form_tail_rational"])
        t2=Q(c24["complete_original_strong_tail_rational"])
        assert t1>=0 and t2>=0
        Sm=shift(mul(M*M,hrem),t2)
        Gu=shift(mul(M,hrem),t1)
        assert Sm==read(sc["original_complete_omitted_S_upper"])
        assert Gu==read(sc["original_complete_omitted_G_upper"])
        assert psd(Sm) and psd(Gu)
        coefs=[sum((b[i]*B[i][j] for i in range(N)),Q(0))
               for j in range(N)]
        C0=[[Q(i==j)+(2*coefs[j] if i==23 else Q(0))
             for j in range(N)] for i in range(N)]
        CHTC=mm(mm(T(C0),hrem),C0)
        BTB=mm(mm(T(B),Sm),B)
        ds=[sum((brad[i]*abs(B[i][j]) for i in range(N)),Q(0))
            for j in range(N)]
        assert [str(x) for x in ds]==sc["original_pole_source_uncertainty_components"]
        pp=hrem[23][23]
        assert pp>=0
        scalar=mul(4*pp*sum((t*t for t in ds),Q(0)),Id(N))
        diag=identity_diagonal([4*pp*ds[i]*sum(ds,Q(0)) for i in range(N)])
        assert psd(scalar) and psd(diag)
        lower_mass=sub(Hlo,HCup)
        lower_choice={
          "PSD_zero":identity_diagonal([Q(0)]*N),
          "kappa_missing_mass":mul(KAPPA,lower_mass)}
        results=[]
        for lname,L in lower_choice.items():
            Gc=mul(Q(1,2),plus(L,Gu))
            E=mul(Q(1,2),sub(Gu,L))
            assert psd(E)
            middle=plus(sub(CHTC,
                       plus(mm(mm(T(C0),Gc),B),
                            mm(mm(T(B),Gc),C0))),BTB)
            feeA=mm(mm(T(C0),E),C0)
            feeB=mm(mm(T(B),E),B)
            assert psd(feeA) and psd(feeB)
            for eta in (Q(1,16),Q(1,4),Q(1),Q(4)):
                raw=plus(middle,plus(mul(eta,feeA),mul(1/eta,feeB)))
                for gamma in (Q(1,16),Q(1,4),Q(1),Q(4)):
                    for ftype,polefee in (
                        ("MG32_scalar_isotropic",scalar),
                        ("new_sourcewise_diagonal",diag)):
                        U=plus(mul(1+gamma,raw),
                               mul(1+1/gamma,polefee))
                        lower=sub(Hlo,plus(direct,U))
                        margin=gersh_lower(lower)
                        results.append((margin,lname,eta,gamma,ftype,U,lower))
        assert len(results)==64
        assert len(sc["all_64_true_original_GS_missing_frequency_parameter_tests"])==64
        for result,archive in zip(results,sc[
                 "all_64_true_original_GS_missing_frequency_parameter_tests"]):
            margin,lname,eta,gamma,ftype,U,lower=result
            assert archive=={
             "G_original_lower_type":lname,
             "cross_G_matrix_Young_eta":str(eta),
             "pole_combination_gamma":str(gamma),
             "pole_error_matrix_kind":ftype,
             "whole_original_signed_Gersh_lower":str(margin),
             "new_omitted_source_trace":str(tr(U))}
            count+=1
        best=max(results,key=lambda r:(r[0],-tr(r[5])))
        margin,lname,eta,gamma,ftype,U,lower=best
        assert (lname,str(eta),str(gamma),ftype)==(
            sc["new_best_G_lower_type"],sc["new_best_eta"],
            sc["new_best_gamma"],sc["new_best_pole_fee_type"])
        assert U==read(sc["new_best_omitted_GS_upper_matrix"])
        assert lower==read(sc["new_best_complete_source_lower_matrix"])
        assert tr(U)==Q(sc["new_best_omitted_GS_upper_trace"])
        assert margin==Q(sc["new_best_complete_original_source_Gersh"])
        assert margin-orig==Q(sc["new_best_vs_MG32_Gersh_change"])
        if margin>orig:
            selectedU=U;selectedlower=lower;selectedM=margin
            name="NEW_ORIGINAL_JOINT_MISSING_GS_LOEWNER"
        else:
            selectedU=old
            selectedlower=sub(Hlo,plus(direct,old))
            selectedM=orig
            name="MG32_VALID_OMITTED_FREQUENCY_FALLBACK"
        assert name==sc["selected_complete_source_method"]
        assert selectedU==read(sc["selected_omitted_upper_matrix"])
        assert selectedlower==read(sc["selected_complete_original_source_lower_matrix"])
        assert selectedM==Q(sc["selected_complete_original_source_Gersh"])
        status=sc["selected_full_source_inertia_classification"]
        wit=sc["selected_full_source_exact_inertia_witness"]
        if status=="NEGATIVE_EXACT_RATIONAL_RAYLEIGH":
            v=[Q(x) for x in wit["rational_vector"]]
            assert len(v)==N and any(v)
            assert qf(v,selectedlower)==Q(wit["exact_negative_quadratic"])<0
        elif status=="POSITIVE_EXACT_RATIONAL_LDL":
            p=exact_ldl(selectedlower)
            assert p is not None and p==[Q(x) for x in
                wit["exact_positive_schur_pivots"]]
            positives+=1
        else:
            assert status=="INCONCLUSIVE" and wit=={}
        assert sc["selected_full24_source_strict_positivity"]==(
            status=="POSITIVE_EXACT_RATIONAL_LDL")
        assert sc["number_valid_exact_original_joint_remainder_trials"]==64
        assert len(sc["same_original_3_ray_diagnostics"])==3
        rimproved=cleared=0
        for row,oldray in zip(sc["same_original_3_ray_diagnostics"],
                              c45["rays"]):
            rays+=1
            v=[Q(x) for x in oldray["original_source_rational_ray"]]
            assert row["same_MG45_original_source_ray"]==oldray[
                "same_archived_original_exact_ray_kind"]
            assert v==[Q(x) for x in row["original_source_rational_vector"]]
            directed=Q(oldray["new_original_direct_prefix_ray_upper"])
            rem=qf(v,selectedU)
            whole=directed+rem
            past=Q(oldray["selected_intersected_valid_original_ray_upper"])
            selected=min(whole,past)
            marginray=qf(v,Hlo)-selected
            assert [Q(row[x]) for x in (
                "new_omitted_source_upper_ray",
                "original_signed_direct_prefix_ray_upper",
                "new_complete_original_ray_upper",
                "MG45_prior_original_complete_ray_upper",
                "new_intersected_original_complete_ray_upper",
                "original_complete_ray_lower")]==[
                rem,directed,whole,past,selected,marginray]
            assert row["strict_complete_ray_improvement"]==(whole<past)
            assert row["nonnegative_original_ray_lower"]==(marginray>=0)
            rimproved+=whole<past;cleared+=marginray>=0
        assert rimproved==sc["number_MG45_rays_improved_complete"]
        assert cleared==sc["number_MG45_rays_nonnegative"]
        assert sc["true_23_adapted_plus_sinh_pole_original_source"]
        assert sc["complete_signed_seven_prime_arch_real_frequency_paid"]
        assert sc["new_joint_omitted_GS_cross_matrix_true_Loewner_upper"]
        assert sc["no_unmeasured_original_source_frequency_dropped"]
        assert sc["no_original_470D_operator_spectral_conclusion"]
    assert count==256 and rays==12
    assert d["any_verified_full24_source_contraction"]==(positives>0)
    assert not d["full470_source_inverse_certified"]
    assert not d["signed_original_51over56_negative_cap_certified"]
    assert d["independent_original_Fourier_form_domain_audit"]=="OPEN"
    assert d["complete_even_Weil_CC27_RH"]=="OPEN"
    print("MG46 INDEPENDENT exact original complete missing-frequency joint matrix audit PASS",{
       "full24_candidates":count,"ray_replays":rays,
       "selected_exact_source_LDL_positive":positives,
       "full470_and_Weil_RH":"OPEN"})
if __name__=="__main__":main()
