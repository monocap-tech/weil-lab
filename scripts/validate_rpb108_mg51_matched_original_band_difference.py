#!/usr/bin/env python3
"""MG51 exact matched-parameter original [4,8] band-substitution audit.

Does NOT certify a new source upper or new original Fourier samples.
Both compared complete 24D matrices are independently valid MG48/MG50
uppers, evaluated at the SAME rational G lower/upper, eta, gamma, pole
profile. Their DIFFERENCE is not asserted Loewner-positive/negative.
"""
import argparse,json,sys
from fractions import Fraction as Q
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import ROOT
from validate_rpb108_mg25_original24_robust_trial import deserialize, original_H24_from_physical_source
from validate_rpb108_mg25_robust_source_aware_residual import Id,T,mm,plus,sub,mul,gersh_lower,psd
from validate_rpb108_mg23_physical_metric_matrix_envelope import KAPPA
N=24;P=23
def read(x):
    a=deserialize(x)
    assert len(a)==N and all(len(r)==N for r in a)
    return a
def enc(a):return [[str(z) for z in r] for r in a]
def sand(a,x):return mm(mm(T(x),a),x)
def cross(a,x,y):return plus(mm(mm(T(x),a),y),mm(mm(T(y),a),x))
def addall(xs):
    out=mul(Q(0),Id(N))
    for x in xs:out=plus(out,x)
    return out
def qf(v,a):return sum((v[i]*a[i][j]*v[j] for i in range(N) for j in range(N)),Q(0))
def diag(ds):
    a=mul(Q(0),Id(N))
    for i,d in enumerate(ds):a[i][i]=d
    return a
def pole_template(B,br):
    d=[sum((br[i]*abs(B[i][j]) for i in range(N)),Q(0)) for j in range(N)]
    return mul(4*sum((x*x for x in d),Q(0)),Id(N)),diag([4*sum(d,Q(0))*x for x in d])
def dirsign(A,v):
    """Exact witness scan; no numerical inertia inference."""
    qs=[]
    basis=[]
    for j in range(N):
        vj=[Q(0)]*N;vj[j]=Q(1);basis.append(vj)
    zs=basis+[v]
    for i in range(N):
      for j in range(i+1,N):
        for sign in (Q(1),Q(-1)):
          z=[Q(0)]*N;z[i]=1;z[j]=sign;zs.append(z)
    pos=neg=None
    for z in zs:
      x=qf(z,A)
      if x>0 and pos is None:pos={"vector":[str(t) for t in z],"exact_quadratic":str(x)}
      if x<0 and neg is None:neg={"vector":[str(t) for t in z],"exact_quadratic":str(x)}
      if pos is not None and neg is not None:break
    return {"positive_rational_witness":pos,"negative_rational_witness":neg,
            "definitely_indefinite":pos is not None and neg is not None}
def candidate(s47,s46,s50,p,b,br,bandhL,bandhU,bandgL,bandgU):
    B=read(s47["full_original_rational_response_B"])
    C=[[Q(i==j)+(2*sum((b[i0]*B[i0][j] for i0 in range(N)),Q(0)) if i==P else Q(0))
        for j in range(N)] for i in range(N)]
    k=s47["cutoff_k"]
    m=Q(17)+Q(347*k,500)
    P0=sub(C,mul((KAPPA+m)/2,B))
    eta=Q(p["eta"]);gamma=Q(p["gamma"])
    assert eta>0 and gamma>0
    lo=read(s47["original_G_lower_candidate_matrices"][p["G_lower"]])
    up=read(s47["original_G_upper_candidate_matrices"][p["G_upper"]])
    assert psd(sub(up,lo))
    ec=mul(Q(1,2),sub(up,lo))
    gc=mul(Q(1,2),plus(up,lo))
    Hdu=read(s46["original_complete_omitted_H_upper"])
    Hdlo=mul(1/KAPPA,read(s47["original_G_lower_candidate_matrices"]["mass_kappa"]))
    assert psd(sub(Hdu,Hdlo))
    # Accepted MG50 measured band lower/upper define new valid tail.
    Hdu_new=sub(Hdu,bandhL)
    Hdlo_new=sub(Hdlo,bandhU)
    ec_new=plus(ec,mul(Q(1,2),sub(bandgU,bandgL)))
    gc_new=sub(gc,mul(Q(1,2),plus(bandgL,bandgU)))
    assert psd(ec_new) and psd(sub(Hdu_new,Hdlo_new))
    Wiso,Wdiag=pole_template(B,br)
    W=Wiso if p["pole_fee"]=="isotropic" else Wdiag
    poleold=mul(Hdu[P][P],W)
    polenew=mul(Hdu_new[P][P],W)
    tau=Q(0) # strong original high tail is identical, cancels out in delta
    d48=read(s46["original_MG32_direct_band_24D_upper"])
    newdirect=read(s50["actual_4to8_original_direct_24D_upper"])
    # This comparison uses identical original MG24/SM41 tau and B on both sides.
    termold=addall([
        sand(Hdu,C),mul(-KAPPA*m,sand(Hdlo,B)),
        mul(-1,cross(gc,P0,B)),
        mul(eta,sand(ec,P0)),mul(1/eta,sand(ec,B))])
    termnew=addall([
        sand(Hdu_new,C),mul(-KAPPA*m,sand(Hdlo_new,B)),
        mul(-1,cross(gc_new,P0,B)),
        mul(eta,sand(ec_new,P0)),mul(1/eta,sand(ec_new,B))])
    # The common high-tail charge cannot be dropped from actual full uppers.
    # Recover it from archived MG48 best when the parameters match there,
    # otherwise use independently accepted MG24 k-specific strong tail.
    return {"B":B,"C":C,"P0":P0,"ec":ec,"eta":eta,"gamma":gamma,
            "oldcore":termold,"newcore":termnew,"poleold":poleold,
            "polenew":polenew,"direct":d48,"newdirect":newdirect,
            "oldtail_H":Hdu,"newtail_H":Hdu_new,
            "W":W,"m":m,"params":p}
def main():
    p=argparse.ArgumentParser()
    for n in ("mg24","mg46","mg47","mg48","mg50"):
        p.add_argument("--verified-"+n+"-json",required=True)
    p.add_argument("--output",default="artifacts/mg51_original_matched_band_difference.json")
    args=p.parse_args()
    load=lambda n:json.loads((ROOT/getattr(args,"verified_"+n+"_json")).read_text())
    a24,a46,a47,a48,a50=[load(n) for n in ("mg24","mg46","mg47","mg48","mg50")]
    assert all(x["canonical_W_ODD_NEG"]=="OPEN" for x in (a24,a46,a47,a48,a50))
    hm,hr,he=original_H24_from_physical_source()
    assert he==Q(a24["physical_Gram_Loewner_row_error"])
    Hlo=sub(hm,mul(he,Id(N)))
    b=[hm[i][P] for i in range(N)]
    br=[hr[i][P] for i in range(N)]
    bandhL=read(a50["new_band_original_mass_lower"])
    bandhU=read(a50["new_band_original_mass_upper"])
    bandgL=read(a50["new_band_original_G_lower"])
    bandgU=read(a50["new_band_original_G_upper"])
    assert psd(sub(bandhU,bandhL)) and psd(sub(bandgU,bandgL))
    Gband_mid=mul(Q(1,2),plus(bandgL,bandgU))
    Gband_err=mul(Q(1,2),sub(bandgU,bandgL))
    records=[]
    for s46,s47,s48,s50 in zip(a46["scenarios"],a47["scenarios"],a48["scenarios"],a50["cases"]):
        mesh,k=s48["mesh_cells"],s48["cutoff_k"]
        assert (mesh,k)==(s46["mesh_cells"],s46["cutoff_k"])==(s47["mesh_cells"],s47["cutoff_k"])==(s50["mesh_cells"],s50["cutoff_k"])
        a24case=next(x for x in a24["cases"] if x["cutoff_k"]==k)
        tau=Q(a24case["complete_original_strong_tail_rational"])
        saved48=s48["best_joint_parameters"]
        saved50=s50["best_new_joint_parameters"]
        ray=[Q(v) for v in s47["selected_exact_inertia_witness"]["rational_vector"]]
        assert qf(ray,sub(Hlo,read(s47["selected_complete_24D_source_upper"])))<0
        comparisons=[]
        for source,p0 in (("MG48_best",saved48),("MG50_best",saved50)):
            c=candidate(s47,s46,s50,p0,b,br,bandhL,bandhU,bandgL,bandgU)
            gamma=c["gamma"];eta=c["eta"];B=c["B"];C=c["C"];P0=c["P0"]
            strong=mul(tau,mm(T(B),B))
            U48=addall([c["direct"],mul(1+gamma,plus(c["oldcore"],strong)),
                        mul(1+1/gamma,c["poleold"])])
            U50=addall([c["direct"],c["newdirect"],
                         mul(1+gamma,plus(c["newcore"],strong)),
                         mul(1+1/gamma,c["polenew"])])
            if source=="MG48_best":assert U48==read(s48["best_joint_complete_24D_upper"])
            if source=="MG50_best":assert U50==read(s50["best_new_whole_24D_upper"])
            components={
                "new_direct_band":c["newdirect"],
                "removed_tail_H_upper":mul(-(1+gamma),sand(bandhL,C)),
                "lost_tail_H_lower_credit":mul((1+gamma)*KAPPA*c["m"],sand(bandhU,B)),
                "new_G_center_cross":mul((1+gamma),cross(Gband_mid,P0,B)),
                "added_G_uncertainty_P0":mul((1+gamma)*eta,sand(Gband_err,P0)),
                "added_G_uncertainty_B":mul((1+gamma)/eta,sand(Gband_err,B)),
                "changed_pole_uncertainty":mul(-(1+1/gamma)*bandhL[P][P],c["W"])}
            delta=sub(U50,U48)
            assert addall(components.values())==delta
            assert psd(components["added_G_uncertainty_P0"])
            assert psd(components["added_G_uncertainty_B"])
            signs=dirsign(delta,ray)
            qpieces={name:qf(ray,z) for name,z in components.items()}
            assert sum(qpieces.values(),Q(0))==qf(ray,delta)
            comparisons.append({
                "matched_parameter_origin":source,
                "parameters":p0,
                "MG48_24D_upper":enc(U48),
                "MG50_24D_upper":enc(U50),
                "MG50_minus_MG48_exact_24D_matrix":enc(delta),
                "exact_diagnostic_matrix_components":{name:enc(z) for name,z in components.items()},
                "on_original_MG43_negative_rational_ray":{
                    "MG48_source_lower":str(qf(ray,sub(Hlo,U48))),
                    "MG50_source_lower":str(qf(ray,sub(Hlo,U50))),
                    "MG50_minus_MG48_upper":str(qf(ray,delta)),
                    "signed_seven_component_ray_differences":{name:str(x) for name,x in qpieces.items()}},
                "exact_24D_difference_sign_witness_scan":signs,
                "matched_MG48_Gersh":str(gersh_lower(sub(Hlo,U48))),
                "matched_MG50_Gersh":str(gersh_lower(sub(Hlo,U50))),
                "additional_local_G_interval_halfwidth":enc(Gband_err),
                "new_Young_width_charges_are_PSD":True,
                "difference_not_assumed_Loewner_ordered":True})
            print("MG51 matched",mesh,k,source,
                  "delta_original_ray",float(qf(ray,delta)),
                  "G_width_B_ray",float(qpieces["added_G_uncertainty_B"]),
                  "new_gersh",float(gersh_lower(sub(Hlo,U50))),flush=True)
        records.append({
            "mesh_cells":mesh,"cutoff_k":k,
            "same_original_MG43_certified_rational_ray":[str(x) for x in ray],
            "matched_parameter_comparisons":comparisons,
            "no_new_24D_Loewner_upper_claim":True,
            "true_original_measured_4to8_information_consumed_from_MG50":True})
    assert len(records)==4
    result={
       "status":"ORIGINAL_MG51_MATCHED_PARAM_4TO8_MATRIX_DIFFERENCE_AUDIT",
       "canonical_W_ODD_NEG":"OPEN",
       "MG50_accepted_original_run":39727680095,
       "MG48_accepted_original_run":39685179933,
       "eight_original_full24_matched_comparisons":True,
       "all_seven_original_band_delta_components_exact":True,
       "independent_new_Fourier_sample":False,
       "no_invalid_delta_Loewner_sign_assumption":True,
       "any_new_source_24D_contraction":False,
       "original_470D_inverse_certified":False,
       "signed_original_51over56_negative_cap_certified":False,
       "independent_original_Fourier_form_domain_audit":"OPEN",
       "complete_even_Weil_CC27_RH":"OPEN",
       "cases":records}
    dest=ROOT/args.output;dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(result,indent=2)+"\n")
    print("MG51 exact 8 matched original source matrix difference cases computed",
          {"cases":8,"new_spectral_certificates":0,"470_RH":"OPEN"},flush=True)
if __name__=="__main__":main()
