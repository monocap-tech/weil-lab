#!/usr/bin/env python3
"""MG47 true original omitted-frequency G/S via independently accepted whole-minus-measured moments.

Never take entrywise or fictitious Loewner minima. For the same genuine
24D SI10/MG11 source, MG24 and MG29 enclose unpoled whole-real moments:
 L_j <= G_whole <= U_j, S_whole <= V_j.
The MG29 32-cell actual original [0,4] prefix encloses independently
 G_C in [LC,UC], S_C >= LSC.
Therefore independently valid OMITTED bounds are
    G_D >= L_j-UC, G_D <= U_j-LC, S_D <= V_j-LSC.
Also retain MG46's positive-multiplier mass bounds
    G_D >= kappa(Hlo-HCupper),
    G_D <= M(Hup-HClower)+tau1 I,
    S_D <= M^2(Hup-HClower)+tau2 I.
Each pairing of a valid lower G, upper G and upper S, with a PSD
G uncertainty E=(U-L)/2, permits the exact original MG40-style
coupled source residual upper, including physical sinh-pole error.

This does not invent a Loewner supremum or use a source-ray scalar
as a simultaneous matrix. Each candidate U_D is separately valid.
The accepted MG32 measured direct residual U_C is summed ONCE.
Also compare a *valid convex interpolation of whole matrices*
 U(theta)=(1-theta)U_MG43 + theta(U_C+U_D)
(the two endpoints independently bound the SAME whole residual).
A convex mixture may improve a signed Gersh or true inertia but cannot
be assumed to without exact rational acceptance.

No all-470 inverse or original signed 51/56 Weil/RH promotion.
"""
import argparse,json,sys
from fractions import Fraction as Q
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
import validate_rpb108_mg32_joint_fourier_residual as m32
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import ROOT
from validate_rpb108_mg25_original24_robust_trial import (
    deserialize, original_H24_from_physical_source)
from validate_rpb108_mg25_robust_source_aware_residual import (
    Id,T,mm,plus,sub,mul,shift,gersh_lower,psd)
from validate_rpb108_mg41_ideal_cross_error_feasibility import classify_ideal
from validate_rpb108_mg23_physical_metric_matrix_envelope import KAPPA
from validate_rpb108_mg26_contiguous_prefix_mass_closure import original_partition_preparation
from validate_rpb108_mg29_adapted_third_curvature import calculate_mesh,original_scenarios
N=24;P=23
ETAS=(Q(1,4),Q(1))
GAMMAS=(Q(1,4),Q(1))
THETAS=(Q(0),Q(1,32),Q(1,16),Q(1,8),Q(1,4),Q(1,2),Q(1))
def mat(A):
    A=deserialize(A)
    assert len(A)==N and all(len(r)==N for r in A)
    return A
def enc(A):return [[str(x) for x in r] for r in A]
def tr(A):return sum((A[i][i] for i in range(N)),Q(0))
def qf(v,A):return sum((v[i]*A[i][j]*v[j] for i in range(N)
                        for j in range(N)),Q(0))
def diag(ds):
    R=[[Q(0)]*N for _ in range(N)]
    for i in range(N):R[i][i]=ds[i]
    return R
def extrapolate(Hlo,Hup,HClo,HCup,GCL,GCU,SCL,m24,whole29,k,mesh):
    mass=sub(Hup,HClo)
    assert mass==T(mass) and psd(mass)
    M=Q(17)+Q(347*k,500)
    row24=next(x for x in m24["cases"] if x["cutoff_k"]==k)
    tau1=Q(row24["complete_original_form_tail_rational"])
    tau2=Q(row24["complete_original_strong_tail_rational"])
    Glo={
        "mass_kappa":mul(KAPPA,sub(Hlo,HCup)),
        "MG24_whole_minus_measured":sub(
            mat(row24["MG19_selected_Go_lower"]),GCU),
    }
    Gup={
        "mass_majorant":shift(mul(M,mass),tau1),
        "MG24_whole_minus_measured":sub(
            mat(row24["complete_original_Go_upper"]),GCL),
    }
    Sup={
        "mass_majorant":shift(mul(M*M,mass),tau2),
        "MG24_whole_minus_measured":sub(
            mat(row24["complete_original_So_upper"]),SCL),
    }
    row29=next(x for x in whole29[mesh] if x["cutoff_k"]==k)
    Glo["MG29_whole_minus_measured"]=sub(mat(row29["whole_Go_lower"]),GCU)
    Gup["MG29_whole_minus_measured"]=sub(mat(row29["whole_Go_upper"]),GCL)
    Sup["MG29_whole_minus_measured"]=sub(mat(row29["whole_So_upper"]),SCL)
    for x in list(Glo.values())+list(Gup.values())+list(Sup.values()):
        assert x==T(x)
    # Every pair is a proven enclosure on exactly the same true G_D.
    for L in Glo.values():
        for U in Gup.values():assert psd(sub(U,L))
    for V in Sup.values():assert psd(V)
    return mass,Glo,Gup,Sup
def make_uppers(mass,Glo,Gup,Sup,B,bmid,brad):
    coeff=[sum((bmid[i]*B[i][j] for i in range(N)),Q(0))
            for j in range(N)]
    C0=[[Q(i==j)+(2*coeff[j] if i==P else Q(0))
         for j in range(N)] for i in range(N)]
    Hpart=mm(mm(T(C0),mass),C0)
    ds=[sum((brad[i]*abs(B[i][j]) for i in range(N)),Q(0))
        for j in range(N)]
    pp=mass[P][P];D=sum(ds,Q(0))
    assert pp>=0
    Wiso=mul(4*pp*sum((x*x for x in ds),Q(0)),Id(N))
    Wdiag=diag([4*pp*D*x for x in ds])
    assert psd(Wiso) and psd(Wdiag)
    pole=(("isotropic",Wiso),("diagonal",Wdiag))
    candidates=[]
    for lname,L in Glo.items():
        for uname,U in Gup.items():
            C=mul(Q(1,2),plus(U,L))
            E=mul(Q(1,2),sub(U,L))
            assert psd(E)
            X=mm(mm(T(C0),E),C0)
            Y=mm(mm(T(B),E),B)
            assert psd(X) and psd(Y)
            base=sub(Hpart,plus(mm(mm(T(C0),C),B),
                                mm(mm(T(B),C),C0)))
            for sname,S in Sup.items():
                core=plus(base,mm(mm(T(B),S),B))
                for eta in ETAS:
                    Qbase=plus(core,plus(mul(eta,X),mul(1/eta,Y)))
                    for gamma in GAMMAS:
                        for pname,W in pole:
                            M=plus(mul(1+gamma,Qbase),mul(1+1/gamma,W))
                            assert M==T(M)
                            candidates.append((lname,uname,sname,eta,gamma,pname,M))
    assert len(candidates)==3*3*3*len(ETAS)*len(GAMMAS)*2==216
    return candidates,ds
def main():
    a=argparse.ArgumentParser()
    for name in ("mg24","mg29","mg32","mg43","mg45","mg46"):
        a.add_argument("--verified-"+name+"-json")
    a.add_argument("--output",default="artifacts/mg47_original_conditioned_missing_moments.json")
    args=a.parse_args()
    assert all(getattr(args,"verified_"+n+"_json") for n in
               ("mg24","mg29","mg32","mg43","mg45","mg46"))
    load=lambda n:json.loads((ROOT/getattr(args,"verified_"+n+"_json")).read_text())
    m24,m29,m32data,m43,m45,m46=(load(n) for n in
                                 ("mg24","mg29","mg32","mg43","mg45","mg46"))
    assert all(x["canonical_W_ODD_NEG"]=="OPEN" for x in
               (m24,m29,m32data,m43,m45,m46))
    assert m46["status"]=="ORIGINAL_MG46_OMITTED_FREQUENCY_TRUE_GS_CROSS_RESIDUAL_UPPER"
    assert m45["status"]=="ORIGINAL_MG45_SIGNED_SOURCE_RAY_FOURIER_RESIDUAL_LINEARIZATION"
    Hmid,Hrad,Herr=original_H24_from_physical_source()
    assert Herr==Q(m24["physical_Gram_Loewner_row_error"])
    Hlo=sub(Hmid,mul(Herr,Id(N)))
    Hup=plus(Hmid,mul(Herr,Id(N)))
    bmid=[Hmid[i][P] for i in range(N)]
    brad=[Hrad[i][P] for i in range(N)]
    assert [str(x) for x in bmid]==m24["original_pole_b_center"]
    assert [str(x) for x in brad]==m24["original_pole_b_radii"]
    cells,HClo,HCup,radius,oldtau=m32.exact_original_cells()
    assert len(cells)==32
    # Reconstruct MG29's original unpoled prefix and whole G/S
    # matrices, which MG29's accepted compact artifact did not store.
    prep=original_partition_preparation()
    meshparts={};whole29={}
    for mesh in (16,32):
        part=calculate_mesh(mesh,prep)
        meshparts[mesh]=part
        archive=next(x for x in m29["meshes"] if x["mesh_cells"]==mesh)
        assert part["sum_29_radii"]==Q(archive["total_source_radius_MG29"])
        for key in ("mass","one","two"):
            actual=part["matrices"]["mg29_third"][key]["trace_width"]
            assert actual==Q(archive["prefix_widths"][key]["mg29_direct_third_trace_width"])
        recon=original_scenarios(part,m24,Hmid,Herr,bmid,brad,
                                 bmid[P],brad[P])["mg29_third"]
        assert len(recon)==2
        for row in recon:
            old=next(x for x in archive["full_original_frequency_scenarios"]
                     if x["cutoff_k"]==row["cutoff_k"])
            for key in ("Gstar","Sstar"):
                assert enc(row["whole_"+key+"_lower"])==old[
                    "full_original_"+key+"_lower"]
                assert enc(row["whole_"+key+"_upper"])==old[
                    "full_original_"+key+"_upper"]
        whole29[mesh]=recon
    measured=meshparts[32]["matrices"]["mg29_third"]
    GCL=mat(measured["one"]["lower_matrix"])
    GCU=mat(measured["one"]["upper_matrix"])
    SCL=mat(measured["two"]["lower_matrix"])
    assert psd(sub(GCU,GCL))
    assert SCL==T(SCL) # A Loewner lower need not be PSD.
    m32.cutoff_tail={x["cutoff_k"]:Q(x["complete_original_strong_tail_rational"])
                     for x in m24["cases"]}
    scenarios=[]
    for mesh in (16,32):
      for k in (12,16):
        r43=next(x for x in m43["scenarios"]
                 if x["mesh_cells"]==mesh and x["cutoff_k"]==k)
        r46=next(x for x in m46["scenarios"]
                 if x["mesh_cells"]==mesh and x["cutoff_k"]==k)
        r45=next(x for x in m45["cases"]
                 if x["mesh_cells"]==mesh and x["cutoff_k"]==k)
        assert r43["source_response_name"]==r46["nonscalar_original_B"]
        B=mat(r43["exact_original_rational_B"])
        direct,sourceR,choices=m32.joint_prefix_upper(cells,bmid,brad,B)
        assert direct==mat(r46["original_MG32_direct_band_24D_upper"])
        mass,Ls,Us,Ss=extrapolate(
            Hlo,Hup,HClo,HCup,GCL,GCU,SCL,m24,whole29,k,mesh)
        candidates,ds=make_uppers(mass,Ls,Us,Ss,B,bmid,brad)
        alltests=[];scored=[]
        for lname,uname,sname,eta,gamma,pname,upper in candidates:
            complete=plus(direct,upper)
            M=sub(Hlo,complete)
            g=gersh_lower(M)
            row={
              "original_omitted_G_lower_origin":lname,
              "original_omitted_G_upper_origin":uname,
              "original_omitted_S_upper_origin":sname,
              "matrix_cross_eta":str(eta),
              "true_pole_outer_gamma":str(gamma),
              "true_pole_fee_kind":pname,
              "new_complete_24D_Gersh_lower":str(g),
              "new_omitted_residual_trace":str(tr(upper))}
            alltests.append(row)
            scored.append((g,-tr(upper),lname,uname,sname,eta,gamma,pname,upper))
        best=max(scored,key=lambda q:q[:2])
        val,negtrace,lname,uname,sname,eta,gamma,pname,newrem=best
        newwhole=plus(direct,newrem)
        U43=mat(r43["original_24D_new_upper_matrix"])
        U46=mat(r46["selected_omitted_upper_matrix"])
        old46=plus(direct,U46)
        assert val==gersh_lower(sub(Hlo,newwhole))
        comparators=[]
        # Each is a genuinely valid whole-source residual Loewner upper.
        for theta in THETAS:
            M=plus(mul(1-theta,U43),mul(theta,newwhole))
            m=gersh_lower(sub(Hlo,M))
            comparators.append({
               "valid_whole_matrix_convex_weight_new":str(theta),
               "whole_24D_exact_Gersh_lower":str(m),
               "whole_24D_upper_trace":str(tr(M))})
        mixed=max(comparators,key=lambda x:Q(x["whole_24D_exact_Gersh_lower"]))
        theta=Q(mixed["valid_whole_matrix_convex_weight_new"])
        mixedU=plus(mul(1-theta,U43),mul(theta,newwhole))
        chosen=(
            ("MG43_whole",U43),
            ("MG46_measured_plus_remainder",old46),
            ("MG47_new_measured_plus_conditioned_remainder",newwhole),
            ("MG43_MG47_valid_whole_convex_mix",mixedU))
        resolved=max(chosen,key=lambda q:(gersh_lower(sub(Hlo,q[1])),-tr(q[1])))
        bestname,finalU=resolved
        finalM=sub(Hlo,finalU)
        sign,wit=classify_ideal(finalM)
        assert sign in ("POSITIVE_EXACT_RATIONAL_LDL",
                        "NEGATIVE_EXACT_RATIONAL_RAYLEIGH","INCONCLUSIVE")
        results=[]
        for ray in r45["rays"]:
            v=[Q(x) for x in ray["original_source_rational_ray"]]
            prior=Q(ray["selected_intersected_valid_original_ray_upper"])
            directray=Q(ray["new_original_direct_prefix_ray_upper"])
            newray=directray+qf(v,newrem)
            old46ray=directray+qf(v,U46)
            selected=min(prior,newray,old46ray)
            results.append({
              "original_ray":ray["same_archived_original_exact_ray_kind"],
              "rational_source":[str(x) for x in v],
              "original_MG45_whole_ray_upper":str(prior),
              "original_MG46_omitted_plus_direct_ray_upper":str(old46ray),
              "new_conditioned_omitted_plus_direct_ray_upper":str(newray),
              "new_valid_scalar_intersection_ray_upper":str(selected),
              "strict_improvement_vs_MG45":selected<prior,
              "nonnegative_valid_source_ray_lower":qf(v,Hlo)-selected>=0})
        scenarios.append({
          "mesh_cells":mesh,"cutoff_k":k,
          "original_response_name":r43["source_response_name"],
          "full_original_rational_response_B":enc(B),
          "measured_original_G_lower":enc(GCL),
          "measured_original_G_upper":enc(GCU),
          "measured_original_S_lower":enc(SCL),
          "original_G_lower_candidate_matrices":{x:enc(y) for x,y in Ls.items()},
          "original_G_upper_candidate_matrices":{x:enc(y) for x,y in Us.items()},
          "original_S_upper_candidate_matrices":{x:enc(y) for x,y in Ss.items()},
          "exact_sourcewise_pole_error_components":[str(x) for x in ds],
          "all_exact_true_original_conditioned_remainder_tests":alltests,
          "number_exact_full_source_conditioned_candidates":len(alltests),
          "new_best_source_method":{
             "lower":lname,"upper":uname,"second":sname,
             "eta":str(eta),"gamma":str(gamma),"pole_fee":pname},
          "new_best_omitted_upper":enc(newrem),
          "new_best_complete_24D_upper":enc(newwhole),
          "new_best_complete_Gersh_lower":str(val),
          "MG43_accepted_whole_Gersh_lower":str(gersh_lower(sub(Hlo,U43))),
          "MG46_accepted_whole_Gersh_lower":str(gersh_lower(sub(Hlo,old46))),
          "whole_original_moment_convex_certificate_trials":comparators,
          "selected_valid_convex_weight":str(theta),
          "selected_strongest_valid_whole_method":bestname,
          "selected_complete_24D_source_upper":enc(finalU),
          "selected_complete_24D_source_lower":enc(finalM),
          "selected_exact_Gersh_lower":str(gersh_lower(finalM)),
          "selected_full24_source_inertia":sign,
          "selected_exact_inertia_witness":wit,
          "certified_strict_original_full24_source_positivity":
                sign=="POSITIVE_EXACT_RATIONAL_LDL",
          "original_MG45_ray_results":results,
          "original_source_23adapted_plus_true_sinh_pole":True,
          "same_complete_original_seven_prime_arch_source_operator":True,
          "no_double_count_original_measured_missing_source_mass":True,
          "no_invalid_matrix_Loewner_minimum":True,
          "no_true_470D_odd_spectral_promotion":True})
    assert len(scenarios)==4
    out={
      "status":"ORIGINAL_MG47_WHOLE_MINUS_MEASURED_CONDITIONED_GS_REMAINDER",
      "canonical_W_ODD_NEG":"OPEN",
      "MG24_accepted_run":39378465438,
      "MG29_accepted_run":39440914565,
      "MG32_accepted_run":39459624082,
      "MG43_accepted_run":39522608989,
      "MG45_accepted_run":39544081287,
      "MG46_accepted_run":39638393721,
      "original_actual_unpoled_whole_G_and_S_minus_same_measured_band":True,
      "new_multiple_true_complete_frequency_missing_GS_Loewner_enclosures":True,
      "all_original_864_complete_source_candidates_exact_rational":True,
      "valid_whole_matrix_convex_mixes_only_not_Loewner_minima":True,
      "original_470D_strong_inverse_certified":False,
      "signed_original_51over56_negative_cap_certified":False,
      "independent_original_Fourier_form_domain_audit":"OPEN",
      "complete_even_Weil_CC27_RH":"OPEN",
      "any_original_full24_source_contraction":any(
         x["certified_strict_original_full24_source_positivity"] for x in scenarios),
      "scenarios":scenarios,
      "next":"If previously certified global first/second original source moment enclosures plus actual measured G/S subtraction cannot produce a positive 24D lower, derive new jointly integrated frequency moment inequalities for the original signed source, or a new nonscalar response. No full470/even/Weil promotion."
    }
    path=ROOT/args.output;path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(out,indent=2)+"\n")
    print("MG47 whole-minus-measured original 24D conditioned source covariance:",
        json.dumps({"cases":[{
         "mesh":x["mesh_cells"],"k":x["cutoff_k"],
         "MG43_Gersh":float(Q(x["MG43_accepted_whole_Gersh_lower"])),
         "MG46_Gersh":float(Q(x["MG46_accepted_whole_Gersh_lower"])),
         "new_Gersh":float(Q(x["new_best_complete_Gersh_lower"])),
         "selected_method":x["selected_strongest_valid_whole_method"],
         "certified_sign":x["selected_full24_source_inertia"]}
        for x in scenarios],"true_full470_and_Weil_RH":"OPEN"}),flush=True)
if __name__=="__main__":main()
