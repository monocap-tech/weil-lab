#!/usr/bin/env python3
"""MG51 independent original complete 24D matched-band matrix replay.

No import of MG51 producer: independently reconstruct ungrouped full
original residual for both established valid MG48 and MG50 sources,
then every exact rational difference component, sign witness and ray.
No new Loewner order or spectral result is inferred from this diagnostic.
"""
import argparse,json,sys
from fractions import Fraction as Q
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import ROOT
from validate_rpb108_mg25_original24_robust_trial import original_H24_from_physical_source
from validate_rpb108_mg23_physical_metric_matrix_envelope import KAPPA
N=24;P=23
def read(v):return [[Q(x) for x in row] for row in v]
def trans(a):return [list(c) for c in zip(*a)]
def mult(a,b):
    bt=trans(b)
    return [[sum((x*y for x,y in zip(row,col)),Q(0)) for col in bt] for row in a]
def add(a,b):return [[x+y for x,y in zip(u,v)] for u,v in zip(a,b)]
def scl(c,a):return [[c*x for x in row] for row in a]
def sub(a,b):return add(a,scl(-1,b))
def ident():return [[Q(i==j) for j in range(N)] for i in range(N)]
def conj(a,x):return mult(mult(trans(x),a),x)
def diag(values):
    a=scl(0,ident())
    for i,v in enumerate(values):a[i][i]=v
    return a
def quad(v,a):return sum((v[i]*a[i][j]*v[j] for i in range(N) for j in range(N)),Q(0))
def gersh(a):return min((a[i][i]-sum((abs(a[i][j]) for j in range(N) if j!=i),Q(0)) for i in range(N)))
def combine(items):
    out=scl(0,ident())
    for x in items:out=add(out,x)
    return out
def core(C,B,Hup,Hlo,Gmid,Ghalf,eta,m,tau):
    # UNGROUPED original polynomial, not centered P0 G core.
    base=conj(Hup,C)
    base=sub(base,mult(mult(trans(C),Gmid),B))
    base=sub(base,mult(mult(trans(B),Gmid),C))
    base=add(base,scl(KAPPA+m,conj(Gmid,B)))
    base=sub(base,scl(KAPPA*m,conj(Hlo,B)))
    base=add(base,scl(tau,mult(trans(B),B)))
    p=sub(C,scl((KAPPA+m)/2,B))
    base=add(base,scl(eta,conj(Ghalf,p)))
    base=add(base,scl(1/eta,conj(Ghalf,B)))
    return base,p
def main():
    parser=argparse.ArgumentParser()
    for n in ("mg24","mg46","mg47","mg48","mg50","mg51"):
        parser.add_argument("--verified-"+n+"-json",required=True)
    a=parser.parse_args()
    load=lambda n:json.loads((ROOT/getattr(a,"verified_"+n+"_json")).read_text())
    d={n:load(n) for n in ("mg24","mg46","mg47","mg48","mg50","mg51")}
    result=d["mg51"]
    assert result["status"]=="ORIGINAL_MG51_MATCHED_PARAM_4TO8_MATRIX_DIFFERENCE_AUDIT"
    assert all(x["canonical_W_ODD_NEG"]=="OPEN" for x in d.values())
    hm,hr,he=original_H24_from_physical_source()
    assert he==Q(d["mg24"]["physical_Gram_Loewner_row_error"])
    Hlo=sub(hm,scl(he,ident()))
    b=[hm[i][P] for i in range(N)];br=[hr[i][P] for i in range(N)]
    hL=read(d["mg50"]["new_band_original_mass_lower"])
    hU=read(d["mg50"]["new_band_original_mass_upper"])
    gL=read(d["mg50"]["new_band_original_G_lower"])
    gU=read(d["mg50"]["new_band_original_G_upper"])
    gMid=scl(Q(1,2),add(gL,gU))
    gWidth=scl(Q(1,2),sub(gU,gL))
    assert gWidth==trans(gWidth)
    count=0
    for c46,c47,c48,c50,c51 in zip(d["mg46"]["scenarios"],d["mg47"]["scenarios"],
                                   d["mg48"]["scenarios"],d["mg50"]["cases"],result["cases"]):
        mesh,k=c51["mesh_cells"],c51["cutoff_k"]
        assert (mesh,k)==(c47["mesh_cells"],c47["cutoff_k"])==(c50["mesh_cells"],c50["cutoff_k"])
        B=read(c47["full_original_rational_response_B"])
        m=Q(17)+Q(347*k,500)
        tau=Q(next(x for x in d["mg24"]["cases"] if x["cutoff_k"]==k)["complete_original_strong_tail_rational"])
        C=[[Q(i==j)+(2*sum((b[t]*B[t][j] for t in range(N)),Q(0)) if i==P else Q(0))
            for j in range(N)] for i in range(N)]
        originalH=read(c46["original_complete_omitted_H_upper"])
        lowerH=scl(1/KAPPA,read(c47["original_G_lower_candidate_matrices"]["mass_kappa"]))
        newH=sub(originalH,hL)
        newlowerH=sub(lowerH,hU)
        originalDirect=read(c46["original_MG32_direct_band_24D_upper"])
        newDirect=read(c50["actual_4to8_original_direct_24D_upper"])
        ray=[Q(x) for x in c51["same_original_MG43_certified_rational_ray"]]
        assert ray==[Q(x) for x in c47["selected_exact_inertia_witness"]["rational_vector"]]
        assert len(c51["matched_parameter_comparisons"])==2
        for comparison in c51["matched_parameter_comparisons"]:
            p=comparison["parameters"]
            eta=Q(p["eta"]);gamma=Q(p["gamma"])
            low=read(c47["original_G_lower_candidate_matrices"][p["G_lower"]])
            high=read(c47["original_G_upper_candidate_matrices"][p["G_upper"]])
            Gc=scl(Q(1,2),add(low,high))
            E=scl(Q(1,2),sub(high,low))
            Gnew=sub(Gc,gMid)
            Enew=add(E,gWidth)
            ds=[sum((br[i]*abs(B[i][j]) for i in range(N)),Q(0)) for j in range(N)]
            Wbase=(scl(4*sum((z*z for z in ds),Q(0)),ident())
                 if p["pole_fee"]=="isotropic" else
                 diag([4*sum(ds,Q(0))*z for z in ds]))
            oldbase,P0=core(C,B,originalH,lowerH,Gc,E,eta,m,tau)
            newbase,Pcheck=core(C,B,newH,newlowerH,Gnew,Enew,eta,m,tau)
            assert Pcheck==P0
            old=combine([originalDirect,scl(1+gamma,oldbase),
                         scl((1+1/gamma)*originalH[P][P],Wbase)])
            new=combine([originalDirect,newDirect,scl(1+gamma,newbase),
                         scl((1+1/gamma)*newH[P][P],Wbase)])
            assert old==read(comparison["MG48_24D_upper"])
            assert new==read(comparison["MG50_24D_upper"])
            change=sub(new,old)
            assert change==read(comparison["MG50_minus_MG48_exact_24D_matrix"])
            if comparison["matched_parameter_origin"]=="MG48_best":
                assert old==read(c48["best_joint_complete_24D_upper"])
                assert p==c48["best_joint_parameters"]
            else:
                assert comparison["matched_parameter_origin"]=="MG50_best"
                assert new==read(c50["best_new_whole_24D_upper"])
                assert p==c50["best_new_joint_parameters"]
            expected={
               "new_direct_band":newDirect,
               "removed_tail_H_upper":scl(-(1+gamma),conj(hL,C)),
               "lost_tail_H_lower_credit":scl((1+gamma)*KAPPA*m,conj(hU,B)),
               "new_G_center_cross":scl(1+gamma,add(
                  mult(mult(trans(P0),gMid),B),
                  mult(mult(trans(B),gMid),P0))),
               "added_G_uncertainty_P0":scl((1+gamma)*eta,conj(gWidth,P0)),
               "added_G_uncertainty_B":scl((1+gamma)/eta,conj(gWidth,B)),
               "changed_pole_uncertainty":scl(-(1+1/gamma)*hL[P][P],Wbase)}
            assert tuple(expected)==tuple(comparison["exact_diagnostic_matrix_components"])
            for name,value in expected.items():
                assert value==read(comparison["exact_diagnostic_matrix_components"][name])
            assert combine(expected.values())==change
            aRay=comparison["on_original_MG43_negative_rational_ray"]
            assert Q(aRay["MG48_source_lower"])==quad(ray,sub(Hlo,old))
            assert Q(aRay["MG50_source_lower"])==quad(ray,sub(Hlo,new))
            assert Q(aRay["MG50_minus_MG48_upper"])==quad(ray,change)
            assert sum((quad(ray,x) for x in expected.values()),Q(0))==quad(ray,change)
            assert aRay["signed_seven_component_ray_differences"]=={
                 k:str(quad(ray,x)) for k,x in expected.items()}
            assert Q(comparison["matched_MG48_Gersh"])==gersh(sub(Hlo,old))
            assert Q(comparison["matched_MG50_Gersh"])==gersh(sub(Hlo,new))
            signs=comparison["exact_24D_difference_sign_witness_scan"]
            for kind,expectedSign in (("positive_rational_witness",1),("negative_rational_witness",-1)):
                cert=signs[kind]
                if cert is not None:
                    v=[Q(x) for x in cert["vector"]]
                    actual=quad(v,change)
                    assert actual==Q(cert["exact_quadratic"]) and actual*expectedSign>0
            assert signs["definitely_indefinite"]==(
                signs["positive_rational_witness"] is not None and
                signs["negative_rational_witness"] is not None)
            assert comparison["additional_local_G_interval_halfwidth"]==[
                [str(x) for x in row] for row in gWidth]
            assert comparison["new_Young_width_charges_are_PSD"]
            assert comparison["difference_not_assumed_Loewner_ordered"]
            count+=1
    assert count==8 and result["eight_original_full24_matched_comparisons"]
    assert result["all_seven_original_band_delta_components_exact"]
    assert result["no_invalid_delta_Loewner_sign_assumption"]
    assert not result["any_new_source_24D_contraction"]
    assert not result["original_470D_inverse_certified"]
    assert not result["signed_original_51over56_negative_cap_certified"]
    assert result["independent_original_Fourier_form_domain_audit"]=="OPEN"
    assert result["complete_even_Weil_CC27_RH"]=="OPEN"
    print("MG51 INDEPENDENT matched full original 24D source delta audit PASS",
         {"matched_full24_matrices":count,"spectral_promotion":False,"RH":"OPEN"},flush=True)
if __name__=="__main__":main()
