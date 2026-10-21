#!/usr/bin/env python3
"""MG48: exact complete-frequency 24D source covariance using a shared multiplier.

On D=[-4,4]^c and 4<=|xi|<=2**k, kappa<=a(xi)<=M_k.
The true second moment obeys
    S_D <= (kappa+M_k) G_D - kappa*M_k H_D + tau_2,k I.
For the high tail, (a-kappa)(a-M_k)<=a*a since a>=kappa>0,
so MG24/SM41's accepted full original strong tail tau_2,k pays it.

This is a complete-original 24D LOEWNER residual UPPER, NOT actual R*R.
It never assumes a globally bounded multiplier or a Loewner minimum.
"""
import argparse, json, sys
from fractions import Fraction as Q
if hasattr(sys, "set_int_max_str_digits"): sys.set_int_max_str_digits(0)
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import ROOT
from validate_rpb108_mg25_original24_robust_trial import (
    deserialize, original_H24_from_physical_source)
from validate_rpb108_mg25_robust_source_aware_residual import (
    Id, T, mm, plus, sub, mul, shift, gersh_lower, psd)
from validate_rpb108_mg41_ideal_cross_error_feasibility import classify_ideal
from validate_rpb108_mg23_physical_metric_matrix_envelope import KAPPA

N, P = 24, 23
ETAS = (Q(1,16), Q(1,4), Q(1), Q(4))
GAMMAS = (Q(1,4), Q(1), Q(4))

def matrix(a):
    a = deserialize(a)
    assert len(a) == N and all(len(x) == N for x in a)
    assert a == T(a)
    return a

def enc(a):
    return [[str(x) for x in row] for row in a]

def trace(a):
    return sum((a[i][i] for i in range(N)), Q(0))

def diag(a):
    v = [[Q(0)]*N for _ in range(N)]
    for i,x in enumerate(a): v[i][i]=x
    return v

def sandwich(a,x):
    return mm(mm(T(x),a),x)

def cross(a,x,y):
    return plus(mm(mm(T(x),a),y), mm(mm(T(y),a),x))

def candidates(row47,row46,row24,bmid,brad,Hlo):
    k = row47["cutoff_k"]
    m = Q(17)+Q(347*k,500)
    assert KAPPA>0 and m>KAPPA
    tau2=Q(row24["complete_original_strong_tail_rational"])
    assert tau2>=0 and Q(row24["original_global_lowband_majorant_M"])==m
    assert row47["selected_strongest_valid_whole_method"]=="MG43_whole"
    B=matrix(row47["full_original_rational_response_B"])
    Hdup=matrix(row46["original_complete_omitted_H_upper"])
    # MG47 independently reconstructs exactly kappa*(Hlo-HCup)
    Hdlo=mul(1/KAPPA,matrix(row47["original_G_lower_candidate_matrices"]["mass_kappa"]))
    assert psd(sub(Hdup,Hdlo))
    Glo={name:matrix(x) for name,x in
         row47["original_G_lower_candidate_matrices"].items()}
    Gup={name:matrix(x) for name,x in
         row47["original_G_upper_candidate_matrices"].items()}
    c=[sum((bmid[i]*B[i][j] for i in range(N)),Q(0)) for j in range(N)]
    C0=[[Q(i==j)+(2*c[j] if i==P else Q(0))
         for j in range(N)] for i in range(N)]
    # Centered joint-multiplier mixed term:
    # -C0^T G B-B^T G C0+(kappa+M) B^T G B = -P0^T G B-B^T G P0.
    P0=sub(C0,mul((KAPPA+m)/2,B))
    baseH=plus(sub(sandwich(Hdup,C0),mul(KAPPA*m,sandwich(Hdlo,B))),
               mul(tau2,mm(T(B),B)))
    ds=[sum((brad[i]*abs(B[i][j]) for i in range(N)),Q(0))
        for j in range(N)]
    dsum=sum(ds,Q(0))
    wp=Hdup[P][P]
    assert wp>=0
    Wiso=mul(4*wp*sum((d*d for d in ds),Q(0)),Id(N))
    Wdiag=diag([4*wp*ds[j]*dsum for j in range(N)])
    assert psd(Wiso) and psd(Wdiag)
    pole=(("isotropic",Wiso),("diagonal",Wdiag))
    out=[]
    for ln,L in Glo.items():
      for un,U in Gup.items():
        E=mul(Q(1,2),sub(U,L))
        if not psd(E): raise AssertionError("invalid MG47 first-moment bracket")
        Gc=mul(Q(1,2),plus(L,U))
        core=sub(baseH,cross(Gc,P0,B))
        X=sandwich(E,P0)
        Y=sandwich(E,B)
        assert psd(X) and psd(Y)
        for eta in ETAS:
          adjusted=plus(core,plus(mul(eta,X),mul(1/eta,Y)))
          for gamma in GAMMAS:
            for pn,W in pole:
              upper=plus(mul(1+gamma,adjusted),mul(1+1/gamma,W))
              assert upper==T(upper)
              out.append((ln,un,eta,gamma,pn,upper))
    assert len(out)==3*3*len(ETAS)*len(GAMMAS)*2==216
    return out

def main():
    p=argparse.ArgumentParser()
    for name in ("mg24","mg46","mg47"):
        p.add_argument("--verified-"+name+"-json",required=True)
    p.add_argument("--output",default="artifacts/mg48_joint_multiplier_source_covariance.json")
    args=p.parse_args()
    inputs={n:json.loads((ROOT/getattr(args,"verified_"+n+"_json")).read_text())
            for n in ("mg24","mg46","mg47")}
    a24,a46,a47=(inputs[n] for n in ("mg24","mg46","mg47"))
    assert all(x["canonical_W_ODD_NEG"]=="OPEN" for x in inputs.values())
    assert a47["status"]=="ORIGINAL_MG47_WHOLE_MINUS_MEASURED_CONDITIONED_GS_REMAINDER"
    assert a46["status"]=="ORIGINAL_MG46_OMITTED_FREQUENCY_TRUE_GS_CROSS_RESIDUAL_UPPER"
    assert len(a47["scenarios"])==len(a46["scenarios"])==4
    Hmid,Hrad,Herr=original_H24_from_physical_source()
    assert Herr==Q(a24["physical_Gram_Loewner_row_error"])
    Hlo=sub(Hmid,mul(Herr,Id(N)))
    bmid=[Hmid[i][P] for i in range(N)]
    brad=[Hrad[i][P] for i in range(N)]
    assert [str(x) for x in bmid]==a24["original_pole_b_center"]
    assert [str(x) for x in brad]==a24["original_pole_b_radii"]
    result=[]
    for row47,row46 in zip(a47["scenarios"],a46["scenarios"]):
        mesh,k=row47["mesh_cells"],row47["cutoff_k"]
        assert (mesh,k)==(row46["mesh_cells"],row46["cutoff_k"])
        row24=next(x for x in a24["cases"] if x["cutoff_k"]==k)
        direct=matrix(row46["original_MG32_direct_band_24D_upper"])
        baseline=matrix(row47["selected_complete_24D_source_upper"])
        assert gersh_lower(sub(Hlo,baseline))==Q(row47["MG43_accepted_whole_Gersh_lower"])
        assert sub(Hlo,baseline)==matrix(row47["selected_complete_24D_source_lower"])
        trials=[]
        for ln,un,eta,gamma,pn,rem in candidates(
                row47,row46,row24,bmid,brad,Hlo):
            whole=plus(direct,rem)
            lower=sub(Hlo,whole)
            g=gersh_lower(lower)
            trials.append((g,-trace(whole),ln,un,eta,gamma,pn,rem,whole))
        assert len(trials)==216
        winner=max(trials,key=lambda x:x[:2])
        g,_,ln,un,eta,gamma,pn,rem,whole=winner
        chosen=whole if g>gersh_lower(sub(Hlo,baseline)) else baseline
        method="MG48_joint_multiplier" if chosen is whole else "MG43_whole"
        cert=sub(Hlo,chosen)
        kind,witness=classify_ideal(cert)
        assert kind in ("POSITIVE_EXACT_RATIONAL_LDL",
                        "NEGATIVE_EXACT_RATIONAL_RAYLEIGH","INCONCLUSIVE")
        result.append({
            "mesh_cells":mesh,"cutoff_k":k,
            "new_joint_original_candidates":216,
            "all_exact_candidate_margins":[{
                "G_lower":lnn,"G_upper":unn,
                "eta":str(e),"gamma":str(gg),"pole_fee":pp,
                "full24_Gersh":str(z),"full24_upper_trace":str(-negtr)}
                for z,negtr,lnn,unn,e,gg,pp,_,_ in trials],
            "best_joint_parameters":{"G_lower":ln,"G_upper":un,
                        "eta":str(eta),"gamma":str(gamma),"pole_fee":pn},
            "best_joint_complete_24D_upper":enc(whole),
            "best_joint_omitted_24D_upper":enc(rem),
            "best_joint_full24_Gersh":str(g),
            "MG43_full24_Gersh":str(gersh_lower(sub(Hlo,baseline))),
            "selected_method":method,
            "selected_complete_24D_upper":enc(chosen),
            "selected_complete_24D_lower":enc(cert),
            "selected_exact_inertia_classification":kind,
            "selected_exact_inertia_witness":witness,
            "original_source_24D_contraction":kind=="POSITIVE_EXACT_RATIONAL_LDL",
            "same_original_full_signed_multiplier_and_true_pole":True,
            "all_original_frequencies_covered":True,
            "original_470D_inverse_not_proved":True})
        print("MG48 CASE",mesh,k,"joint_Gersh",float(g),
              "MG43_Gersh",float(Q(row47["MG43_accepted_whole_Gersh_lower"])),
              "selected",method,flush=True)
    output={
        "status":"ORIGINAL_MG48_COMPLETE_FREQUENCY_JOINT_MULTIPLIER_24D_RESIDUAL",
        "canonical_W_ODD_NEG":"OPEN",
        "accepted_input_runs":{"MG24":39378465438,"MG46":39638393721,
                               "MG47":39663431182},
        "complete_frequency_joint_S_bound":
            "S_D <= (kappa+M_k)*G_D-kappa*M_k*H_D+tau2_k*I",
        "high_tail_payment":"MG24 original accepted strong tail, not bounded a<=M globally",
        "all_original_864_joint_candidates_exact_rational":True,
        "any_original_source_24D_contraction":any(
            x["original_source_24D_contraction"] for x in result),
        "original_470D_strong_inverse_certified":False,
        "signed_original_51over56_negative_cap_certified":False,
        "independent_original_Fourier_form_domain_audit":"OPEN",
        "complete_even_Weil_CC27_RH":"OPEN",
        "scenarios":result}
    dest=ROOT/args.output
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(output,indent=2)+"\n")
    print("MG48 COMPLETE 864 candidate check",{
          "cases":4,"total":864,"source_positivity":output["any_original_source_24D_contraction"],
          "all470_RH":"OPEN"},flush=True)

if __name__=="__main__": main()
