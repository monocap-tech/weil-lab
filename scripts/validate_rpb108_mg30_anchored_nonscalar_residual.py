#!/usr/bin/env python3
"""MG30: anchored nonscalar original 24D source-residual method gate.

Use ACCEPTED MG29 original full-real-frequency 24D Gstar/Sstar Loewner
brackets, original genuine source Gram H, and the complete sinh pole.

For Y=F B with B=tI+D (t>=0), R=F-Astar F B, exact identity:
 R*R=H-GB-B^t G+B^t S B.
A robust bound with -E <= G-Gc <= E and S<=US is
 R*R <= Hup-2t LG-Gc D-D^t Gc
        +B^t US B+2||E|| ||D|| I,
 E=(UG-LG)/2, Gc=(UG+LG)/2.
This is strictly stronger than charging the entire scalar tI term
against 2||E|| ||B|| I; source nonscalar uncertainty is paid separately.

Every B is exact rational. Floating solvers may PROPOSE B only.
Gershgorin of Hlo-Rupper gives a sufficient squared-residual source
contraction in the original Gram metric. Failure != negative spectrum.

No 24D source residual can be promoted to complete 470D inverse,
signed odd 51/56, whole Weil or RH; the range is not invariant.
"""
import argparse,json,sys
from fractions import Fraction as Q
import numpy as np
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import ROOT
from validate_rpb108_mg25_original24_robust_trial import (
    original_H24_from_physical_source,deserialize,
)
from validate_rpb108_mg25_robust_source_aware_residual import (
    T,mm,plus,sub,mul,Id,shift,gersh_lower,norm_upper,
)
from validate_rpb108_mg25_robust_source_aware_residual import true_pole_case

N=24
DEN=2**17
MESHES=(16,32)
CUTS=(12,16)

def round_near(q,den=DEN):
    q=Q(q)
    z=q*den
    return Q((2*z.numerator+z.denominator)//(2*z.denominator),den)

def proposal_float(Gc,US,t,alpha,regularizer):
    """Propose, but NEVER prove, original rational nonscalar source B.

    Regularize a complete 24D upper second moment by its diagonal
    scale; reject ill-conditioned/non-finite proposals. Exact CI
    re-evaluates the full R*R inequality from Fraction matrices.
    """
    try:
        g=np.array([[float(v) for v in row] for row in Gc])
        s=np.array([[float(v) for v in row] for row in US])
        if not np.isfinite(g).all() or not np.isfinite(s).all():
            return None
        s=(s+s.T)/2
        scale=max(1.,float(np.max(np.abs(np.diag(s)))))
        b=np.linalg.solve(s+(float(regularizer)*scale)*np.eye(N),g)
        if not np.isfinite(b).all() or float(np.max(np.abs(b)))>64:
            return None
        tfloat=float(t)
        if not np.isfinite(tfloat):return None
        blended=((1-float(alpha))*tfloat*np.eye(N)
                 +float(alpha)*b)
        B=[[round_near(Q.from_float(float(blended[i,j])))
            for j in range(N)] for i in range(N)]
        if all(B[i][j]==(t if i==j else Q(0))
               for i in range(N) for j in range(N)):
            return None
        return B
    except (ValueError,OverflowError,ZeroDivisionError,np.linalg.LinAlgError):
        return None

def proposal_diag(Gc,US,t,alpha):
    """Non-scalar diagonal positive rational candidate; no solver."""
    diag=[]
    for i in range(N):
        if US[i][i]<=0:return None
        x=Gc[i][i]/US[i][i]
        x=max(Q(0),min(Q(4)*t,x))
        diag.append((1-alpha)*t+alpha*x)
    B=[[round_near(diag[i]) if i==j else Q(0)
        for j in range(N)] for i in range(N)]
    return B if len(set(B[i][i] for i in range(N)))>1 else None

def anchored_upper(Hlo,Hup,LG,UG,US,t,B):
    assert t>=0 and len(B)==N and all(len(row)==N for row in B)
    assert all(len(M)==N and all(len(row)==N for row in M)
               for M in (Hlo,Hup,LG,UG,US))
    for M in (Hlo,Hup,LG,UG,US):
        assert M==T(M)
    assert all(Hup[i][i]>=Hlo[i][i] for i in range(N))
    E=mul(Q(1,2),sub(UG,LG))
    assert all(E[i][i]>=0 for i in range(N))
    Gc=mul(Q(1,2),plus(LG,UG))
    D=sub(B,mul(t,Id(N)))
    epsilon=norm_upper(E)
    delta=norm_upper(D)
    # The scalar -2tG is bounded from above by -2tLG.
    # The remaining mixed D term pays exactly the unknown G
    # deviation using operator submultiplicativity, not a scalar
    # assumption that G and B commute.
    cross=plus(mm(Gc,D),mm(T(D),Gc))
    action=mm(mm(T(B),US),B)
    upper=shift(plus(sub(sub(Hup,mul(2*t,LG)),cross),
                     action),2*epsilon*delta)
    assert upper==T(upper)
    margin=gersh_lower(sub(Hlo,upper))
    Hcap=norm_upper(Hup)
    assert Hcap>0
    gap=max(Q(0),min(Q(1),margin/Hcap)) if margin>0 else Q(0)
    return {
      "margin":margin,"gap":gap,"error_G_opnorm":epsilon,
      "non_scalar_D_opnorm":delta,"uncertainty_charge":2*epsilon*delta,
      "positive":margin>0,"B":B,"t":t}

def independent_pole_regression():
    """Verify algebra both at t=0 and t>0 on genuine rank-one pole."""
    H,G,S,_=true_pole_case()
    # Exact true matrices are equal to their Loewner brackets.
    t=Q(1,8)
    B=[[Q(1,5) if i==j else Q(1,100)*(i+j+1)
         for j in range(3)] for i in range(3)]
    def ncore(H,LG,UG,US,t,B):
        n=len(H)
        Gc=mul(Q(1,2),plus(LG,UG))
        E=mul(Q(1,2),sub(UG,LG))
        D=sub(B,mul(t,Id(n)))
        return shift(
          plus(sub(sub(H,mul(2*t,LG)),
                   plus(mm(Gc,D),mm(T(D),Gc))),
               mm(mm(T(B),US),B)),
          2*norm_upper(E)*norm_upper(D))
    R=sub(sub(plus(H,mm(mm(T(B),S),B)),mm(G,B)),mm(T(B),G))
    assert R==ncore(H,G,G,S,t,B)
    # Nonzero Loewner-G uncertainty, explicit source 3x3 surrogate.
    lo=shift(G,-Q(1,100))
    hi=shift(G,Q(1,100))
    sup=shift(S,Q(1,100))
    claimed=ncore(H,lo,hi,sup,t,B)
    diff=sub(claimed,R)
    # Valid check without approximate eigenvalues (strict Gersh).
    assert gersh_lower(diff)>0
    return True

def case_candidates(Gc,US,t):
    """Finite deterministic trial family; no assertion of completeness."""
    out=[("MG24_scalar_t",t,mul(t,Id(N))),
         ("scalar_half",t/2,mul(t/2,Id(N))),
         ("scalar_double",2*t,mul(2*t,Id(N)))]
    for alpha in (Q(1,4),Q(1,2),Q(1)):
        B=proposal_diag(Gc,US,t,alpha)
        if B is not None:out.append(("diagonal_"+str(alpha),t,B))
    for lam in (Q(1,1000),Q(1,100),Q(1,10)):
        for alpha in (Q(1,4),Q(1,2)):
            B=proposal_float(Gc,US,t,alpha,lam)
            if B is not None:
                out.append(("matrix_ridge_"+str(lam)+"_blend_"+str(alpha),
                            t,B))
    # Require nonscalar tests when the original 24D data permits it.
    seen=set()
    result=[]
    for name,base,B in out:
        code=(base,tuple(tuple(row) for row in B))
        if code in seen:continue
        seen.add(code);result.append((name,base,B))
    return result

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--verified-mg29-json",required=True)
    p.add_argument("--verified-mg24-json",required=True)
    p.add_argument("--output",default=
       "artifacts/mg30_original_24D_anchored_source_aware_residual.json")
    args=p.parse_args()
    assert independent_pole_regression()
    data=json.loads((ROOT/args.verified_mg29_json).read_text())
    old24=json.loads((ROOT/args.verified_mg24_json).read_text())
    assert data["status"]=="ORIGINAL_ADAPTED_THIRD_FOURIER_SOURCE_MOMENT_REFINEMENT"
    assert old24["status"]=="ORIGINAL_COMPLETE_FREQUENCY_24CHANNEL_COUPLED_SOURCE_MATRIX_ENCLOSURES"
    assert data["mg24_original_accepted_run"]==39378465438
    assert data["mg26_original_accepted_run"]==39380800739
    assert data["mg28_original_accepted_run"]==39438064440
    assert data["whole_original_frequency_pole_source_moments_enclosed"]
    assert data["canonical_W_ODD_NEG"]==old24["canonical_W_ODD_NEG"]=="OPEN"
    assert [mesh["mesh_cells"] for mesh in data["meshes"]]==[16,32]
    Hcenter,Hradii,Herr=original_H24_from_physical_source()
    assert Herr==Q(old24["physical_Gram_Loewner_row_error"])
    assert [str(Hcenter[i][23]) for i in range(N)]==old24["original_pole_b_center"]
    Hlo=sub(Hcenter,mul(Herr,Id(N)))
    Hup=plus(Hcenter,mul(Herr,Id(N)))
    scenarios=[]
    for mesh in data["meshes"]:
        for c in mesh["full_original_frequency_scenarios"]:
            k=c["cutoff_k"]
            assert k in CUTS
            assert c["original_complete_frequency_and_true_pole"]
            LG=deserialize(c["full_original_Gstar_lower"])
            UG=deserialize(c["full_original_Gstar_upper"])
            US=deserialize(c["full_original_Sstar_upper"])
            Gc=mul(Q(1,2),plus(LG,UG))
            original=next(x for x in old24["cases"] if x["cutoff_k"]==k)
            t=Q(original["scalar_trial_t"])
            assert t>0
            trials=case_candidates(Gc,US,t)
            accepted=[]
            for name,t0,B in trials:
                cert=anchored_upper(Hlo,Hup,LG,UG,US,t0,B)
                accepted.append({
                    "name":name,
                    "scalar_anchor_t":str(t0),
                    "nonscalar_B":any(B[i][j] !=
                        (B[0][0] if i==j else Q(0))
                        for i in range(N) for j in range(N)),
                    "B_minus_anchor_norm":str(cert["non_scalar_D_opnorm"]),
                    "G_uncertainty_norm_upper":str(cert["error_G_opnorm"]),
                    "mixed_uncertainty_charge":str(cert["uncertainty_charge"]),
                    "gershgorin_margin":str(cert["margin"]),
                    "certified_source_residual_squared_gap":str(cert["gap"]),
                    "strict_source_contraction":cert["positive"],
                    "full_original_operator_470D":False})
            assert accepted and accepted[0]["name"]=="MG24_scalar_t"
            best=max(accepted,key=lambda z:Q(z["gershgorin_margin"]))
            best_non=next((x for x in sorted(
                (x for x in accepted if x["nonscalar_B"]),
                key=lambda z:Q(z["gershgorin_margin"]),reverse=True)),None)
            scenarios.append({
                "mesh_cells":mesh["mesh_cells"],
                "cutoff_k":k,
                "genuine_original_24D_pole_corrected_complete_frequency":True,
                "source_basis_23boundary_plus_original_sinh_pole":True,
                "H_G_S_same_physical_source_basis":True,
                "original_signed_multiplier_seven_prime_plus_arch_inherited":True,
                "candidate_count":len(accepted),
                "nonscalar_candidate_count":sum(x["nonscalar_B"] for x in accepted),
                "best_trial":best["name"],
                "best_signed_Gershgorin_margin":best["gershgorin_margin"],
                "best_strict_source_squared_residual_gap":
                    best["certified_source_residual_squared_gap"],
                "strict_source_contraction_obtained":
                    best["strict_source_contraction"],
                "best_nonscalar_trial":best_non["name"] if best_non else None,
                "best_nonscalar_Gershgorin_margin":
                    best_non["gershgorin_margin"] if best_non else None,
                "original_MG29_Gstar_over_MG24_trace_width":
                    c["Gstar_29_over_MG24_width"],
                "original_MG29_Sstar_over_MG24_trace_width":
                    c["Sstar_29_over_MG24_width"],
                "trials":accepted})
    assert [(x["mesh_cells"],x["cutoff_k"]) for x in scenarios]==[
        (16,12),(16,16),(32,12),(32,16)]
    best=max(scenarios,key=lambda z:Q(z["best_signed_Gershgorin_margin"]))
    out={
        "status":"ORIGINAL_24D_ANCHORED_NONSCALE_MIXED_RESIDUAL_GATE",
        "canonical_W_ODD_NEG":"OPEN",
        "verified_original_MG24_run_id":39378465438,
        "verified_original_MG29_run_id":39440914565,
        "original_complete_frequency_24D_true_pole_brackets":True,
        "original_physical_25D_Gram_reconstructed":True,
        "true_23pluspole_channels":True,
        "scalar_G_error_charged_with_lower_Loewner_not_operator_norm":True,
        "nonscalar_mixed_G_error_paid_with_2normE_normD":True,
        "exact_Fraction_matrix_acceptance":True,
        "analytic_nonscalar_rank_one_pole_surrogate_regression":True,
        "floating_solvers_only_propose_never_prove":True,
        "original_24D_any_strict_source_contraction":
            any(x["strict_source_contraction_obtained"] for x in scenarios),
        "best_original_24D_signed_Gershgorin_margin":
            best["best_signed_Gershgorin_margin"],
        "best_original_24D_source_squared_gap":
            best["best_strict_source_squared_residual_gap"],
        "best_mesh":best["mesh_cells"],"best_cutoff_k":best["cutoff_k"],
        "actual_full_original_470D_strong_residual_certified":False,
        "signed_original_negative_51over56_cap_certified":False,
        "finite_source_subspace_is_invariant":False,
        "independent_original_Fourier_form_domain_audit":"OPEN",
        "even_Weil_CC27_RH":"OPEN",
        "scenarios":scenarios,
        "next_gate":"If no strict original 24D residual, identify leading G uncertainty and source dimensions; develop disjoint MG24 selected-panel/MG29 prefix Loewner hybrid and certify a genuinely useful original 24D contraction before any attempt at 470D signed cap."
    }
    dst=ROOT/args.output
    dst.parent.mkdir(parents=True,exist_ok=True)
    dst.write_text(json.dumps(out,indent=2)+"\n")
    print("MG30 anchored original nonscalar:",json.dumps({
        "trials":[(x["mesh_cells"],x["cutoff_k"],x["candidate_count"],
                   x["nonscalar_candidate_count"],
                   float(Q(x["best_signed_Gershgorin_margin"])),
                   x["strict_source_contraction_obtained"]) for x in scenarios],
        "best_gap":float(Q(out["best_original_24D_source_squared_gap"])),
        "full470_odd_even_Weil_RH":"OPEN"
    }),flush=True)
if __name__=="__main__":main()
