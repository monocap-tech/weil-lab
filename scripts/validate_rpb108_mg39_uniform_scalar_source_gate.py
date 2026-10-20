#!/usr/bin/env python3
"""MG39: exact continuum scalar-t and convex source-moment feasibility gate.

Actual complete-real-frequency original source R=F-Astar F(tI), on the
same true SI10 25 physical/23 MG11 adapted+sinh pole 24-dimensional
basis, is bounded by original independently verified MG24 and MG29
physical complete-frequency moment enclosures:

  R*R <= Hup-2t L_G+t*t U_S, for t>=0.
  A(t)=Hlo-Rupper=(Hlo-Hup)+2t L_G-t*t U_S.

Convex interpolation, for lambda in [0,1],
  L_G(lambda)=(1-lambda)L_G24+lambda L_G29
  U_S(lambda)=(1-lambda)U_S24+lambda U_S29,
is still a VALID pair of original Loewner bounds for the SAME
operator, not an unverified entrywise intersection.

For a rational nonzero source vector v,
  v^T A(t,lambda)v = -d+2t*b(lambda)-t*t*c(lambda)
where d=2*Herr*||v||^2,
      b(lambda)=v^T L_G(lambda)v,
      c(lambda)=v^T U_S(lambda)v>=0.
For c>0 its exact supremum for t>=0 is
 -d + max(b,0)^2/c; if b<=0 and c=0 it is -d.
For a FIXED v and t, q is affine in lambda. Thus to prove it is
strictly negative for EVERY t>=0 and EVERY lambda in a rational
interval I, it suffices to check both lambda endpoints, with EXACT
Fraction inequalities (not floating eigenvalues).

Attempt to cover all lambda in [0,1] by disjoint intervals (16
primary, 64 fallback subdivisions) with a different exact rational
v on each interval. If coverage succeeds, this excludes ANY scalar
response t>=0 using ANY convex combination of the two original
complete-frequency source bounds, for that original k and mesh.
It does NOT exclude nonscalar B, better correlated source bounds,
an actual operator positive residual, or RH.

Floating linear algebra may propose rational witnesses; all decisive
statements are exact arithmetic and independently rechecked in CI.
"""
import argparse,json,sys
from fractions import Fraction as F
from pathlib import Path
import numpy as np
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import ROOT
from validate_rpb108_mg25_original24_robust_trial import deserialize
from validate_rpb108_mg25_robust_source_aware_residual import (
    T,plus,sub,mul,Id,gersh_lower
)

N=24
MESHES=(16,32)
CUTS=(12,16)
DEN=2**20

def dot(v,A):
    assert len(v)==N and len(A)==N
    return sum((v[i]*A[i][j]*v[j] for i in range(N)
        for j in range(N)),F(0))

def unit(j):
    return tuple(F(i==j) for i in range(N))

def candidate_vectors(L24,L29,S24,S29):
    """Small deterministic rational-first dictionary; float only suggests."""
    seen=set()
    def add(v):
        v=tuple(v)
        if not any(v):return False
        code=tuple(v)
        if code in seen:return False
        seen.add(code)
        yield v
    for i in range(N):
        yield from add(unit(i))
    # Adjacent / pole-coupled source coordinates.
    for i in range(N-1):
        for sign in (-1,1):
            v=list(unit(i));v[i+1]=F(sign)
            yield from add(v)
    for i in range(N-1):
        for sign in (-1,1):
            v=list(unit(i));v[23]=F(sign)
            yield from add(v)
    for alpha in (0,F(1,4),F(1,2),F(3,4),1):
        L=plus(mul(1-F(alpha),L24),mul(F(alpha),L29))
        S=plus(mul(1-F(alpha),S24),mul(F(alpha),S29))
        for M in (L,S):
            try:
                a=np.array([[float(q) for q in row] for row in M])
                if not np.isfinite(a).all():continue
                a=(a+a.T)/2
                values,W=np.linalg.eigh(a)
                if not np.isfinite(values).all():continue
            except (ValueError,OverflowError,np.linalg.LinAlgError):
                continue
            for i in range(N):
                for scale in (2**14,DEN):
                    v=tuple(F(int(round(float(W[j,i])*scale)),scale)
                            for j in range(N))
                    yield from add(v)
    # No stochastic or ungrounded candidate data.

def eval_endpoint(v,lo,hi,L24,L29,S24,S29,Herr):
    nv=sum((x*x for x in v),F(0))
    d=2*Herr*nv
    assert d>0 and nv>0
    def at(lam):
        L=plus(mul(1-lam,L24),mul(lam,L29))
        S=plus(mul(1-lam,S24),mul(lam,S29))
        b=dot(v,L)
        c=dot(v,S)
        # A rigorously valid upper of a true PSD second moment
        # MUST itself be PSD. If this fails, stop instead of
        # treating an invalid negative 'second moment upper' as good.
        assert c>=0
        if b<=0:
            return {"lambda":str(lam),"b":str(b),"c":str(c),
                    "full_scalar_t_continuum_strict_negative":d>0,
                    "max_signed_margin":str(-d),
                    "exact_peak_t":"0"}
        if c==0:
            return {"lambda":str(lam),"b":str(b),"c":str(c),
                    "full_scalar_t_continuum_strict_negative":False,
                    "max_signed_margin":None,"exact_peak_t":None}
        # Exact derivative optimum at t=b/c, positive.
        sup=-d+b*b/c
        return {"lambda":str(lam),"b":str(b),"c":str(c),
                "full_scalar_t_continuum_strict_negative":sup<0,
                "max_signed_margin":str(sup),
                "exact_peak_t":str(b/c)}
    a=at(lo);b=at(hi)
    return d,a,b

def exact_2D_regression():
    # In 24D, take a compact example whose endpoint values
    # are known and whose scalar t maximum can be evaluated exactly.
    L=[[F(0)]*N for _ in range(N)]
    S=[[F(0)]*N for _ in range(N)]
    L[0][0]=F(1,2);S[0][0]=F(1)
    H=F(1,2)
    v=unit(0)
    d,a,b=eval_endpoint(v,F(0),F(1),L,L,S,S,H)
    assert d==1 and a["max_signed_margin"]==str(F(-3,4))
    assert a=={**b,"lambda":"0"}
    assert a["exact_peak_t"]=="1/2"
    # Any nonpositive G direction is uniformly obstructed
    # whenever H upper-lower uncertainty is positive.
    L[0][0]=F(-3,2)
    _,a,b=eval_endpoint(v,F(0),F(1),L,L,S,S,H)
    assert a["max_signed_margin"]=="-1"
    assert a["exact_peak_t"]=="0"
    return True

def directional_profile(v,L24,L29,S24,S29,Herr):
    nv=sum((x*x for x in v),F(0))
    assert nv>0
    return {"v":v,"d":2*Herr*nv,
            "b0":dot(v,L24),"b1":dot(v,L29),
            "c0":dot(v,S24),"c1":dot(v,S29)}

def profile_endpoint(profile,lam):
    d=profile["d"]
    b=(1-lam)*profile["b0"]+lam*profile["b1"]
    c=(1-lam)*profile["c0"]+lam*profile["c1"]
    assert d>0 and c>=0
    if b<=0:
        sup=-d;t0=F(0)
    elif c>0:
        sup=-d+b*b/c;t0=b/c
    else:
        return {"lambda":str(lam),"b":str(b),"c":str(c),
                "full_scalar_t_continuum_strict_negative":False,
                "max_signed_margin":None,"exact_peak_t":None}
    return {"lambda":str(lam),"b":str(b),"c":str(c),
            "full_scalar_t_continuum_strict_negative":sup<0,
            "max_signed_margin":str(sup),"exact_peak_t":str(t0)}

def certificate_for_interval(left,right,profiles):
    for profile in profiles:
        a=profile_endpoint(profile,left)
        if not a["full_scalar_t_continuum_strict_negative"]:continue
        b=profile_endpoint(profile,right)
        if b["full_scalar_t_continuum_strict_negative"]:
            return {
                "interval":[str(left),str(right)],
                "nonzero_original_24D_rational_direction":[
                    str(x) for x in profile["v"]],
                "exact_positive_Hupper_minus_Hlower_direction":str(profile["d"]),
                "endpoints":[a,b],
                "uniform_all_t_nonnegative_and_lambda_in_interval_no_go":True,
                "true_operator_negative_mode_inferred":False}
    return None

def audit_case(k,mesh,L24,S24,L29,S29,Herr,t0,old30case):
    assert all(M==T(M) for M in (L24,S24,L29,S29))
    assert Herr>0
    assert k in CUTS and mesh in MESHES
    assert old30case["mesh_cells"]==mesh and old30case["cutoff_k"]==k
    assert old30case["strict_source_contraction_obtained"] is False
    candidates=list(candidate_vectors(L24,L29,S24,S29))
    assert candidates
    # Cache exact directional quadratics ONCE, not 24x24 Fraction
    # matrix multiplication afresh for every lambda interval.
    profiles=[directional_profile(v,L24,L29,S24,S29,Herr)
              for v in candidates]
    # The MG30 exact fixed-t scalar certificate is replayed here.
    Hcharge=mul(2*Herr,Id(N))
    for lam,L,S in ((F(0),L24,S24),(F(1),L29,S29)):
        A= sub(sub(mul(2*t0,L),mul(t0*t0,S)),Hcharge)
        if lam==1:
            hist=next(t for t in old30case["trials"] if t["name"]=="MG24_scalar_t")
            assert str(gersh_lower(A))==hist["gershgorin_margin"]
    winners=[]
    for n in (16,64):
        slices=[]
        for j in range(n):
            left,right=F(j,n),F(j+1,n)
            w=certificate_for_interval(left,right,profiles)
            slices.append(w)
        successes=sum(x is not None for x in slices)
        winners=slices
        if successes==n:break
    full=all(x is not None for x in winners)
    return {
       "cutoff_k":k,"MG29_original_mesh":mesh,
       "physical_source_23adapted_plus_genuine_sinh_pole":True,
       "original_signed_arch_plus_seven_prime_complete_frequency":True,
       "original_MG30_scalar_fixed_t_rational_margin_replayed":True,
       "scalar_t_nonnegative_continuum_and_source_moment_blend_full_coverage":full,
       "lambda_partition_denominator":len(winners),
       "number_uniform_rational_witnessed_intervals":sum(x is not None for x in winners),
       "number_unresolved_lambda_intervals":sum(x is None for x in winners),
       "tested_rational_direction_proposals":len(candidates),
       "original_scalar_MG24_t":str(t0),
       "intervals":winners,
       "no_non_scalar_B_or_full470_or_RH_classification":True}

def main():
    p=argparse.ArgumentParser()
    for k in ("mg24","mg29","mg30"):
        p.add_argument("--verified-"+k+"-json")
    p.add_argument("--output",default="artifacts/mg39_original_uniform_scalar_source_gate.json")
    p.add_argument("--self-test",action="store_true")
    args=p.parse_args()
    assert exact_2D_regression()
    if args.self_test:
        print("MG39 exact scalar quadratic regression PASS")
        return
    assert all(getattr(args,"verified_"+k+"_json") for k in ("mg24","mg29","mg30")), "All accepted original artifacts are mandatory for source conclusions"
    old24=json.loads((ROOT/args.verified_mg24_json).read_text())
    old29=json.loads((ROOT/args.verified_mg29_json).read_text())
    old30=json.loads((ROOT/args.verified_mg30_json).read_text())
    assert old24["status"]=="ORIGINAL_COMPLETE_FREQUENCY_24CHANNEL_COUPLED_SOURCE_MATRIX_ENCLOSURES"
    assert old29["status"]=="ORIGINAL_ADAPTED_THIRD_FOURIER_SOURCE_MOMENT_REFINEMENT"
    assert old30["status"]=="ORIGINAL_24D_ANCHORED_NONSCALE_MIXED_RESIDUAL_GATE"
    assert old24["canonical_W_ODD_NEG"]==old29["canonical_W_ODD_NEG"]==old30["canonical_W_ODD_NEG"]=="OPEN"
    assert old30["verified_original_MG24_run_id"]==39378465438
    assert old30["verified_original_MG29_run_id"]==39440914565
    Herr=F(old24["physical_Gram_Loewner_row_error"])
    assert Herr>0
    rows=[]
    for mesh in MESHES:
        original=next(x for x in old29["meshes"] if x["mesh_cells"]==mesh)
        for k in CUTS:
            m24=next(x for x in old24["cases"] if x["cutoff_k"]==k)
            m29=next(x for x in original["full_original_frequency_scenarios"]
                     if x["cutoff_k"]==k)
            m30=next(x for x in old30["scenarios"]
                     if x["mesh_cells"]==mesh and x["cutoff_k"]==k)
            rows.append(audit_case(
                k,mesh,deserialize(m24["complete_Gstar_lower"]),
                deserialize(m24["complete_Sstar_upper"]),
                deserialize(m29["full_original_Gstar_lower"]),
                deserialize(m29["full_original_Sstar_upper"]),
                Herr,F(m24["scalar_trial_t"]),m30))
    assert [(r["MG29_original_mesh"],r["cutoff_k"]) for r in rows]==[
        (16,12),(16,16),(32,12),(32,16)]
    output={
      "status":"ORIGINAL_MG39_CONTINUUM_SCALAR_SOURCE_ENCLOSURE_FEASIBILITY",
      "canonical_W_ODD_NEG":"OPEN",
      "verified_MG24_original_run":39378465438,
      "verified_MG29_original_run":39440914565,
      "verified_MG30_original_run":39442984941,
      "original_physical_25_SI10_sources_and_23plus_sinh_pole_24D":True,
      "same_original_source_basis_for_both_complete_frequency_brackets":True,
      "convex_Loewner_bracket_interpolation_valid":True,
      "two_endpoint_negative_all_t_quadratic_implies_interval_no_go":True,
      "floating_eigenvectors_only_proposed_rational_witnesses":True,
      "uniform_all_t_all_blends_certified_in_every_case":
         all(x["scalar_t_nonnegative_continuum_and_source_moment_blend_full_coverage"]
             for x in rows),
      "this_is_not_a_negative_mode_of_actual_signed_odd_operator":True,
      "full_original_470D_source_inverse_certified":False,
      "original_signed_51over56_negative_cap_certified":False,
      "independent_original_Fourier_form_domain_audit":"OPEN",
      "complete_even_Weil_CC27_RH":"OPEN",
      "cases":rows,
      "next":"If full uniform no-go, exclude all nonnegative scalar t under ANY convex MG24/MG29 source-moment bracket and pivot to genuinely new coupled matrix bounds or nonscalar B. If some lambda intervals unresolved, refine exact rational source directions and report only demonstrated intervals. Never confuse a negative lower certificate with an actual operator negative mode."
    }
    dst=ROOT/args.output
    dst.parent.mkdir(parents=True,exist_ok=True)
    dst.write_text(json.dumps(output,indent=2)+"\n")
    print("MG39 original universal scalar source gate:",json.dumps({
      "cases":[{"mesh":x["MG29_original_mesh"],"k":x["cutoff_k"],
                "witnessed":x["number_uniform_rational_witnessed_intervals"],
                "partition":x["lambda_partition_denominator"],
                "all_t_all_blends_excluded":
                     x["scalar_t_nonnegative_continuum_and_source_moment_blend_full_coverage"]}
               for x in rows],
      "470D_even_Weil_CC27_RH":"OPEN"}),flush=True)
if __name__=="__main__":main()
