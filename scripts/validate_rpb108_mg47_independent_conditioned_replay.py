#!/usr/bin/env python3
"""MG47 independent exact original measured/whole/missing G/S covariance audit.

No import of MG47 implementation. Rebuild original MG29 16/32-cell
unpoled physical moments from the accepted original Fourier source
algorithm and replay its accepted pole-corrected MG29 artifact.
Rebuild every MG47 24x24 conditioned remainder/whole-upper trial
independently and verify exact signs and selected full-source inertia.
"""
import argparse,json,sys
from fractions import Fraction as Q
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
import validate_rpb108_mg32_joint_fourier_residual as mg32
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import ROOT
from validate_rpb108_mg25_original24_robust_trial import (
    deserialize,original_H24_from_physical_source)
from validate_rpb108_mg25_robust_source_aware_residual import (
    Id,T,mm,plus,sub,mul,shift,gersh_lower,psd)
from validate_rpb108_mg26_contiguous_prefix_mass_closure import original_partition_preparation
from validate_rpb108_mg29_adapted_third_curvature import (
    calculate_mesh, original_scenarios)
from validate_rpb108_mg23_physical_metric_matrix_envelope import KAPPA
N=24;P=23
def read(A):
    A=deserialize(A)
    assert len(A)==N and all(len(r)==N for r in A)
    return A
def sr(A):return [[str(x) for x in row] for row in A]
def trace(A):return sum((A[i][i] for i in range(N)),Q(0))
def qf(z,A):return sum((z[i]*A[i][j]*z[j] for i in range(N)
                       for j in range(N)),Q(0))
def diag(ds):
    A=[[Q(0)]*N for _ in range(N)]
    for i in range(N):A[i][i]=ds[i]
    return A
def exact_ldl(A):
    assert A==T(A)
    W=[list(r) for r in A];p=[]
    for k in range(N):
        d=W[k][k]
        if d<=0:return None
        p.append(d)
        for i in range(k+1,N):
            for j in range(i,N):
                W[j][i]-=W[i][k]*W[j][k]/d
                W[i][j]=W[j][i]
    return p
def candidate_groups(Hlo,Hup,HClo,HCup,Lc,Uc,Sc,m24,original29,k,mesh):
    cut=next(x for x in m24["cases"] if x["cutoff_k"]==k)
    full=next(x for x in original29[mesh] if x["cutoff_k"]==k)
    remup=sub(Hup,HClo)
    assert psd(remup)
    M=Q(17)+Q(347*k,500)
    tau1=Q(cut["complete_original_form_tail_rational"])
    tau2=Q(cut["complete_original_strong_tail_rational"])
    L={
       "mass_kappa":mul(KAPPA,sub(Hlo,HCup)),
       "MG24_whole_minus_measured":sub(read(cut["MG19_selected_Go_lower"]),Uc),
       "MG29_whole_minus_measured":sub(read(full["whole_Go_lower"]),Uc)}
    U={
       "mass_majorant":shift(mul(M,remup),tau1),
       "MG24_whole_minus_measured":sub(read(cut["complete_original_Go_upper"]),Lc),
       "MG29_whole_minus_measured":sub(read(full["whole_Go_upper"]),Lc)}
    S={
       "mass_majorant":shift(mul(M*M,remup),tau2),
       "MG24_whole_minus_measured":sub(read(cut["complete_original_So_upper"]),Sc),
       "MG29_whole_minus_measured":sub(read(full["whole_So_upper"]),Sc)}
    for lo in L.values():
        for up in U.values():assert psd(sub(up,lo))
    for up in S.values():assert psd(up)
    return remup,L,U,S
def main():
    p=argparse.ArgumentParser()
    for n in ("mg24","mg29","mg32","mg43","mg45","mg46","mg47"):
        p.add_argument("--verified-"+n+"-json",required=True)
    args=p.parse_args()
    source={n:json.loads((ROOT/getattr(args,"verified_"+n+"_json")).read_text())
            for n in ("mg24","mg29","mg32","mg43","mg45","mg46","mg47")}
    m24,m29,m32,m43,m45,m46,d=(source[n] for n in
                               ("mg24","mg29","mg32","mg43","mg45","mg46","mg47"))
    assert d["status"]=="ORIGINAL_MG47_WHOLE_MINUS_MEASURED_CONDITIONED_GS_REMAINDER"
    assert d["canonical_W_ODD_NEG"]=="OPEN"
    assert [d[n] for n in ("MG24_accepted_run","MG29_accepted_run",
       "MG32_accepted_run","MG43_accepted_run","MG45_accepted_run",
       "MG46_accepted_run")]==[
       39378465438,39440914565,39459624082,
       39522608989,39544081287,39638393721]
    for flag in ("original_actual_unpoled_whole_G_and_S_minus_same_measured_band",
       "new_multiple_true_complete_frequency_missing_GS_Loewner_enclosures",
       "all_original_864_complete_source_candidates_exact_rational",
       "valid_whole_matrix_convex_mixes_only_not_Loewner_minima"):
        assert d[flag],flag
    Hmid,Hrad,Herr=original_H24_from_physical_source()
    assert Herr==Q(m24["physical_Gram_Loewner_row_error"])
    Hlo=sub(Hmid,mul(Herr,Id(N)))
    Hup=plus(Hmid,mul(Herr,Id(N)))
    b=[Hmid[i][P] for i in range(N)]
    rad=[Hrad[i][P] for i in range(N)]
    assert [str(x) for x in b]==m24["original_pole_b_center"]
    assert [str(x) for x in rad]==m24["original_pole_b_radii"]
    cells,HClo,HCup,radius,ta=mg32.exact_original_cells()
    assert len(cells)==32
    assert radius==Q(next(x for x in m29["meshes"]
         if x["mesh_cells"]==32)["total_source_radius_MG29"])
    mg32.cutoff_tail={x["cutoff_k"]:Q(x["complete_original_strong_tail_rational"])
                      for x in m24["cases"]}
    prep=original_partition_preparation()
    parts={};original29={}
    for mesh in (16,32):
        part=calculate_mesh(mesh,prep)
        archive=next(x for x in m29["meshes"] if x["mesh_cells"]==mesh)
        assert Q(part["sum_29_radii"])==Q(archive["total_source_radius_MG29"])
        for label in ("mass","one","two"):
            assert part["matrices"]["mg29_third"][label]["trace_width"]==Q(
               archive["prefix_widths"][label]["mg29_direct_third_trace_width"])
        scenarios=original_scenarios(part,m24,Hmid,Herr,b,rad,b[P],rad[P])["mg29_third"]
        for row in scenarios:
            arch=next(x for x in archive["full_original_frequency_scenarios"]
                     if x["cutoff_k"]==row["cutoff_k"])
            for kind in ("Gstar","Sstar"):
                assert sr(row["whole_"+kind+"_lower"])==arch[
                  "full_original_"+kind+"_lower"]
                assert sr(row["whole_"+kind+"_upper"])==arch[
                  "full_original_"+kind+"_upper"]
        parts[mesh]=part;original29[mesh]=scenarios
    prefix=parts[32]["matrices"]["mg29_third"]
    Lc=read(prefix["one"]["lower_matrix"])
    Uc=read(prefix["one"]["upper_matrix"])
    Sc=read(prefix["two"]["lower_matrix"])
    assert psd(sub(Uc,Lc))
    assert [(c["mesh_cells"],c["cutoff_k"]) for c in d["scenarios"]]==[
       (16,12),(16,16),(32,12),(32,16)]
    count=0;positive=0;raycount=0
    for row in d["scenarios"]:
        mesh,k=row["mesh_cells"],row["cutoff_k"]
        old43=next(c for c in m43["scenarios"]
                   if c["mesh_cells"]==mesh and c["cutoff_k"]==k)
        old46=next(c for c in m46["scenarios"]
                   if c["mesh_cells"]==mesh and c["cutoff_k"]==k)
        old45=next(c for c in m45["cases"]
                   if c["mesh_cells"]==mesh and c["cutoff_k"]==k)
        B=read(old43["exact_original_rational_B"])
        assert row["original_response_name"]==old43["source_response_name"]
        assert B==read(row["full_original_rational_response_B"])
        assert (Lc==read(row["measured_original_G_lower"]) and
                Uc==read(row["measured_original_G_upper"]) and
                Sc==read(row["measured_original_S_lower"]))
        rem,L,U,S=candidate_groups(Hlo,Hup,HClo,HCup,Lc,Uc,Sc,
                                   m24,original29,k,mesh)
        for label,mats in (("original_G_lower_candidate_matrices",L),
                           ("original_G_upper_candidate_matrices",U),
                           ("original_S_upper_candidate_matrices",S)):
            assert set(row[label])==set(mats)
            for name,M in mats.items():assert M==read(row[label][name])
        coeff=[sum((b[i]*B[i][j] for i in range(N)),Q(0))
               for j in range(N)]
        C0=[[Q(i==j)+(2*coeff[j] if i==P else Q(0))
             for j in range(N)] for i in range(N)]
        Hp=mm(mm(T(C0),rem),C0)
        Ds=[sum((rad[i]*abs(B[i][j]) for i in range(N)),Q(0))
            for j in range(N)]
        assert [str(x) for x in Ds]==row["exact_sourcewise_pole_error_components"]
        pole=[("isotropic",mul(4*rem[P][P]*
               sum((x*x for x in Ds),Q(0)),Id(N))),
              ("diagonal",diag([4*rem[P][P]*sum(Ds,Q(0))*x
                               for x in Ds]))]
        for name,W in pole:assert psd(W)
        direct,_,_=mg32.joint_prefix_upper(cells,b,rad,B)
        U43=read(old43["original_24D_new_upper_matrix"])
        U46=plus(direct,read(old46["selected_omitted_upper_matrix"]))
        entries=[]
        for lname,l in L.items():
            for uname,u in U.items():
                E=mul(Q(1,2),sub(u,l))
                C=mul(Q(1,2),plus(u,l))
                assert psd(E)
                X=mm(mm(T(C0),E),C0)
                Y=mm(mm(T(B),E),B)
                assert psd(X) and psd(Y)
                cross=plus(mm(mm(T(C0),C),B),mm(mm(T(B),C),C0))
                for sname,ss in S.items():
                    core=plus(sub(Hp,cross),mm(mm(T(B),ss),B))
                    for eta in (Q(1,4),Q(1)):
                        mid=plus(core,plus(mul(eta,X),mul(1/eta,Y)))
                        for gamma in (Q(1,4),Q(1)):
                            for pname,W in pole:
                                upper=plus(mul(1+gamma,mid),
                                           mul(1+1/gamma,W))
                                assert upper==T(upper)
                                A=sub(Hlo,plus(direct,upper))
                                margin=gersh_lower(A)
                                entries.append((margin,-trace(upper),
                                     lname,uname,sname,eta,gamma,pname,upper))
                                count+=1
        assert len(entries)==row["number_exact_full_source_conditioned_candidates"]==216
        archived=row["all_exact_true_original_conditioned_remainder_tests"]
        assert len(archived)==216
        for cur,old in zip(entries,archived):
            margin,negtr,lname,uname,sname,eta,gamma,pname,Unew=cur
            assert old=={
              "original_omitted_G_lower_origin":lname,
              "original_omitted_G_upper_origin":uname,
              "original_omitted_S_upper_origin":sname,
              "matrix_cross_eta":str(eta),
              "true_pole_outer_gamma":str(gamma),
              "true_pole_fee_kind":pname,
              "new_complete_24D_Gersh_lower":str(margin),
              "new_omitted_residual_trace":str(trace(Unew))}
        winner=max(entries,key=lambda x:x[:2])
        g,_,lo,up,ss,eta,gamma,polekind,Unew=winner
        assert row["new_best_source_method"]=={
            "lower":lo,"upper":up,"second":ss,
            "eta":str(eta),"gamma":str(gamma),"pole_fee":polekind}
        assert Unew==read(row["new_best_omitted_upper"])
        Uwhole=plus(direct,Unew)
        assert Uwhole==read(row["new_best_complete_24D_upper"])
        assert g==Q(row["new_best_complete_Gersh_lower"])
        assert gersh_lower(sub(Hlo,U43))==Q(row["MG43_accepted_whole_Gersh_lower"])
        assert gersh_lower(sub(Hlo,U46))==Q(row["MG46_accepted_whole_Gersh_lower"])
        weights=(Q(0),Q(1,32),Q(1,16),Q(1,8),Q(1,4),Q(1,2),Q(1))
        comp=[]
        for theta in weights:
            UU=plus(mul(1-theta,U43),mul(theta,Uwhole))
            comp.append({
              "valid_whole_matrix_convex_weight_new":str(theta),
              "whole_24D_exact_Gersh_lower":str(
                  gersh_lower(sub(Hlo,UU))),
              "whole_24D_upper_trace":str(trace(UU))})
        assert comp==row["whole_original_moment_convex_certificate_trials"]
        chosen=max(comp,key=lambda x:Q(x["whole_24D_exact_Gersh_lower"]))
        theta=Q(chosen["valid_whole_matrix_convex_weight_new"])
        assert theta==Q(row["selected_valid_convex_weight"])
        mixture=plus(mul(1-theta,U43),mul(theta,Uwhole))
        competitors=(("MG43_whole",U43),
                     ("MG46_measured_plus_remainder",U46),
                     ("MG47_new_measured_plus_conditioned_remainder",Uwhole),
                     ("MG43_MG47_valid_whole_convex_mix",mixture))
        name,final=max(competitors,key=lambda x:(
            gersh_lower(sub(Hlo,x[1])),-trace(x[1])))
        assert name==row["selected_strongest_valid_whole_method"]
        A=sub(Hlo,final)
        assert A==read(row["selected_complete_24D_source_lower"])
        assert final==read(row["selected_complete_24D_source_upper"])
        assert gersh_lower(A)==Q(row["selected_exact_Gersh_lower"])
        sign=row["selected_full24_source_inertia"]
        wit=row["selected_exact_inertia_witness"]
        if sign=="POSITIVE_EXACT_RATIONAL_LDL":
            piv=exact_ldl(A)
            assert piv is not None and piv==[Q(x) for x in wit[
                "exact_positive_schur_pivots"]]
            positive+=1
        elif sign=="NEGATIVE_EXACT_RATIONAL_RAYLEIGH":
            v=[Q(x) for x in wit["rational_vector"]]
            assert len(v)==N and any(v)
            assert qf(v,A)==Q(wit["exact_negative_quadratic"])<0
        else:
            assert sign=="INCONCLUSIVE" and wit=={}
        assert row["certified_strict_original_full24_source_positivity"]==(
            sign=="POSITIVE_EXACT_RATIONAL_LDL")
        assert len(row["original_MG45_ray_results"])==3
        for current,old in zip(row["original_MG45_ray_results"],old45["rays"]):
            raycount+=1
            v=[Q(x) for x in old["original_source_rational_ray"]]
            assert v==[Q(x) for x in current["rational_source"]]
            oldbound=Q(old["selected_intersected_valid_original_ray_upper"])
            old46ray=Q(old["new_original_direct_prefix_ray_upper"])+qf(
                v,read(old46["selected_omitted_upper_matrix"]))
            newray=Q(old["new_original_direct_prefix_ray_upper"])+qf(v,Unew)
            scalar=min(oldbound,old46ray,newray)
            assert [Q(current[x]) for x in (
              "original_MG45_whole_ray_upper",
              "original_MG46_omitted_plus_direct_ray_upper",
              "new_conditioned_omitted_plus_direct_ray_upper",
              "new_valid_scalar_intersection_ray_upper")]==[
                oldbound,old46ray,newray,scalar]
            assert current["strict_improvement_vs_MG45"]==(scalar<oldbound)
            assert current["nonnegative_valid_source_ray_lower"]==(
                qf(v,Hlo)-scalar>=0)
        assert row["original_source_23adapted_plus_true_sinh_pole"]
        assert row["same_complete_original_seven_prime_arch_source_operator"]
        assert row["no_double_count_original_measured_missing_source_mass"]
        assert row["no_invalid_matrix_Loewner_minimum"]
        assert row["no_true_470D_odd_spectral_promotion"]
    assert count==864 and raycount==12
    assert d["any_original_full24_source_contraction"]==(positive>0)
    assert not d["original_470D_strong_inverse_certified"]
    assert not d["signed_original_51over56_negative_cap_certified"]
    assert d["independent_original_Fourier_form_domain_audit"]=="OPEN"
    assert d["complete_even_Weil_CC27_RH"]=="OPEN"
    print("MG47 INDEPENDENT exact original whole-minus-measured source covariance PASS",{
       "full24_candidates":count,"source_rays":raycount,
       "positive_exact_LDL":positive,"original_470D_RH":"OPEN"})
if __name__=="__main__":main()
