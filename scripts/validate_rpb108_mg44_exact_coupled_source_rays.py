#!/usr/bin/env python3
"""MG44 — exact directional original coupled H/G/S residual certificate audit.

The MG43 actual complete 24D residual LOWER matrices had exact negative
source Rayleigh rays. That fact excludes each CONSERVATIVE MG43 matrix
but says nothing about the true original residual.

For each accepted exact nonzero rational source ray v and its original
nonscalar response B, put w=Bv. From real original complete-frequency
and pole-inclusive MG24/MG29 source moments:
 Hlo <= H <= Hup, L_i <= G <= U_i, S <= S_i, i=24,29.
 Let C_i=(L_i+U_i)/2, E_i=(U_i-L_i)/2>=0.
 Since -E_i <= G-C_i <= E_i, the real symmetric block
   [[E_i,G-C_i],[G-C_i,E_i]] >= 0.
 It follows EXACTLY by block Cauchy-Schwarz that
   v^T G w >= v^T C_i w - sqrt((v^T E_i v)(w^T E_i w)).
 Therefore the physical source residual satisfies the new
 independently valid fixed-DIRECTION scalar upper
   v^T R(B)^T R(B) v <=
    v^T Hup v -2 max_i G_lower_i(v,w)
                + min_i w^T S_i w.
 Rational sqrt ceiling is paid OUTWARDS, never via float.
 Separately take the min with accepted MG43 full matrix ray upper.
 This is an original genuine-pole and whole-spectrum directional
 certificate, NOT a new full24 Loewner upper for all vectors at once.
 
 The theoretical exact directional lower c(alpha)-sqrt(a(alpha)b(alpha))
 is convex over convex first-moment Loewner mixes, by concavity of
 the geometric mean. Its MAXIMUM on alpha in [0,1] lies at an endpoint.
 Hence using both parents per ray exhausts the simple convex first-
 moment blend family for THIS scalar support function; does not
 exhaust correlated source data or multivector SDP couplings.

 Independence acceptance: 4 source cases x three archived rays:
  - original MG43 negative ray for selected conservative lower;
  - original MG41 negative ray for SAME B's archived MG40 lower;
  - original MG42 upper fee-threshold negative ray for SAME B.
 Check all exact parent G/S two-moment inequalities, outward integer
 sqrt, scalar original residual margins, strict directional
 improvement, and separate negative / nonnegative sign statuses.
 Never promote one-ray nonnegative bounds into 24D positivity.
"""
import argparse,json,sys
from fractions import Fraction as Q
from math import isqrt
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import ROOT
from validate_rpb108_mg25_original24_robust_trial import (
    deserialize,original_H24_from_physical_source)
from validate_rpb108_mg25_robust_source_aware_residual import (
    Id,T,mm,plus,sub,mul,psd)

N=24
GRID_SCALE=10**12
def mat(A):
    M=deserialize(A)
    assert len(M)==N and all(len(row)==N for row in M)
    assert M==T(M)
    return M
def quadratic(v,A,w=None):
    if w is None:w=v
    assert len(v)==N and len(w)==N
    return sum((v[i]*A[i][j]*w[j] for i in range(N)
                for j in range(N)),Q(0))
def mv(A,v):
    return [sum((A[i][j]*v[j] for j in range(N)),Q(0))
            for i in range(N)]
def sqrt_outward(q):
    assert q>=0
    if q==0:return Q(0)
    # Largest integer n with n^2*q.den<=q.num*SCALE^2.
    n=isqrt((q.numerator*GRID_SCALE*GRID_SCALE)//q.denominator)
    lo=Q(n,GRID_SCALE)
    hi=lo if lo*lo==q else Q(n+1,GRID_SCALE)
    assert lo*lo<=q<=hi*hi and hi-lo<=Q(1,GRID_SCALE)
    return hi
def source_ray(v,B,Hlo,Hup,parents,accepted_U):
    assert len(v)==N and any(v)
    w=mv(B,v)
    Hupper=quadratic(v,Hup)
    Hlower=quadratic(v,Hlo)
    s_uppers=[]
    g_lowers=[]
    detailed=[]
    for label,LG,UG,US in parents:
        E=mul(Q(1,2),sub(UG,LG))
        C=mul(Q(1,2),plus(LG,UG))
        a=quadratic(v,E)
        b=quadratic(w,E)
        assert E==T(E) and a>=0 and b>=0
        prod=a*b
        radius=sqrt_outward(prod)
        center=quadratic(v,C,w)
        gl=center-radius
        su=quadratic(w,US)
        assert su>=0
        g_lowers.append((gl,label))
        s_uppers.append((su,label))
        detailed.append({
           "source_parent":label,
           "exact_original_G_cross_center":str(center),
           "exact_original_G_error_vEv":str(a),
           "exact_original_G_error_Bv_E_Bv":str(b),
           "exact_original_cross_sqrt_radicand":str(prod),
           "outward_rational_cross_sqrt_upper":str(radius),
           "verified_original_cross_first_moment_lower":str(gl),
           "verified_original_second_moment_upper":str(su),
           "original_true_pole_and_all_real_frequency":True})
    gl,gl_source=max(g_lowers)
    su,su_source=min(s_uppers)
    direct=Hupper-2*gl+su
    old=quadratic(v,accepted_U)
    # Both are *independently valid* uppers on SAME true scalar
    # source residual direction. Taking min in 1D is valid.
    better=min(direct,old)
    old_margin=Hlower-old
    raw_margin=Hlower-direct
    chosen=Hlower-better
    assert chosen>=old_margin
    return {
        "nonzero_original_24D_rational_ray":[str(x) for x in v],
        "original_Bv_rational_ray":[str(x) for x in w],
        "old_MG43_full24_source_upper_projected":str(old),
        "new_directed_original_complete_residual_upper":str(direct),
        "certified_intersection_upper_with_MG43":str(better),
        "original_source_Hlower_ray":str(Hlower),
        "original_source_Hupper_ray":str(Hupper),
        "old_MG43_source_lower_ray_margin":str(old_margin),
        "new_direction_only_unmixed_margin":str(raw_margin),
        "selected_direction_only_source_margin":str(chosen),
        "new_directional_bound_improves_MG43_on_this_ray":direct<old,
        "strict_nonnegative_directional_certification":chosen>=0,
        "chosen_first_moment_original_parent":gl_source,
        "chosen_second_moment_original_parent":su_source,
        "independent_parent_directional_bounds":detailed,
        "NO_complete_24D_matrix_Loewner_promotion":True,
        "NO_operator_signed_spectral_assertion":True}
def self_test():
    for r in (Q(0),Q(1),Q(2),Q(5,3),Q(1,10**30),Q(10**28,3)):
        u=sqrt_outward(r)
        assert u*u>=r and (u-Q(1,GRID_SCALE))**2<=r if u else r==0
    A=[[Q(i==j) for j in range(N)] for i in range(N)]
    Z=[[Q(0) for j in range(N)] for i in range(N)]
    B=[[Q(i==j) for j in range(N)] for i in range(N)]
    v=[Q(i==0) for i in range(N)]
    out=source_ray(v,B,A,A,[("toy1",Z,plus(Z,mul(2,A)),mul(3,A)),
                            ("toy2",Z,plus(Z,mul(4,A)),mul(5,A))],mul(9,A))
    assert Q(out["new_directed_original_complete_residual_upper"])==Q(6)
    assert out["chosen_second_moment_original_parent"]=="toy1"
    assert out["new_directional_bound_improves_MG43_on_this_ray"]
    return True
def audit():
    p=argparse.ArgumentParser()
    for name in ("mg24","mg29","mg40","mg41","mg42","mg43"):
        p.add_argument("--verified-"+name+"-json")
    p.add_argument("--self-test",action="store_true")
    p.add_argument("--output",default=
        "artifacts/mg44_original_exact_directional_coupled_source.json")
    a=p.parse_args()
    assert self_test()
    if a.self_test:
        print("MG44 exact original directional block-PSD cross-term and integer sqrt tests PASS")
        return
    assert all(getattr(a,"verified_"+n+"_json") for n in
               ("mg24","mg29","mg40","mg41","mg42","mg43"))
    load=lambda n:json.loads((ROOT/getattr(a,"verified_"+n+"_json")).read_text())
    m24,m29,m40,m41,m42,m43=(
       load(n) for n in ("mg24","mg29","mg40","mg41","mg42","mg43"))
    assert all(x["canonical_W_ODD_NEG"]=="OPEN"
               for x in (m24,m29,m40,m41,m42,m43))
    assert m24["status"]=="ORIGINAL_COMPLETE_FREQUENCY_24CHANNEL_COUPLED_SOURCE_MATRIX_ENCLOSURES"
    assert m29["status"]=="ORIGINAL_ADAPTED_THIRD_FOURIER_SOURCE_MOMENT_REFINEMENT"
    assert m40["status"]=="ORIGINAL_MG40_ANISOTROPIC_FULL_SOURCE_G_CROSS_ERROR_GATE"
    assert m41["status"]=="ORIGINAL_MG41_NONSCALE_IDEAL_G_CROSS_FEE_FEASIBILITY"
    assert m42["status"]=="ORIGINAL_MG42_EXACT_RELATIVE_SOURCE_G_ERROR_FEE_BUDGET"
    assert m43["status"]=="ORIGINAL_MG43_INDEPENDENT_COUPLED_G_S_LOEWNER_PARAMETER_RECOMBINATION"
    assert not m43["any_strict_original_24D_source_contraction"]
    Hmid,Hrad,Herr=original_H24_from_physical_source()
    assert Herr==Q(m24["physical_Gram_Loewner_row_error"])
    Hlo=sub(Hmid,mul(Herr,Id(N)))
    Hup=plus(Hmid,mul(Herr,Id(N)))
    results=[]
    for mesh in (16,32):
      for k in (12,16):
        cs=next(c for c in m43["scenarios"]
                if c["mesh_cells"]==mesh and c["cutoff_k"]==k)
        c24=next(c for c in m24["cases"] if c["cutoff_k"]==k)
        c29=next(c for c in next(x for x in m29["meshes"]
             if x["mesh_cells"]==mesh)["full_original_frequency_scenarios"]
             if c["cutoff_k"]==k)
        c40=next(c for c in m40["scenarios"]
              if c["mesh_cells"]==mesh and c["cutoff_k"]==k)
        c41=next(c for c in m41["scenarios"]
              if c["mesh_cells"]==mesh and c["cutoff_k"]==k)
        c42=next(c for c in m42["scenarios"]
              if c["mesh_cells"]==mesh and c["cutoff_k"]==k)
        assert cs["source_response_name"]==c42["original_nonscalar_B"]==(
            c40["best_nonscalar_name"])
        B=deserialize(cs["exact_original_rational_B"])
        assert len(B)==N and all(len(row)==N for row in B)
        prev=mat(cs["original_24D_new_upper_matrix"])
        rays=[
          ("MG43_original_selected_negative_source_ray",
           [Q(x) for x in cs["full24_exact_inertia_witness"]["rational_vector"]]),
          ("MG41_original_MG40_fee_bearing_negative_source_ray",
           [Q(x) for x in next(t for t in c41["trials"]
               if t["name"]==cs["source_response_name"])[
                   "actual_MG40_source_certificate_exact_witness"]["rational_vector"]]),
          ("MG42_original_relative_fee_upper_negative_source_ray",
           [Q(x) for x in c42["upper_exact_negative_Rayleigh_certificate"][
               "rational_source_direction"]])
        ]
        assert cs["full24_exact_inertia_classification"]=="NEGATIVE_EXACT_RATIONAL_RAYLEIGH"
        parents=[
          ("MG24",mat(c24["complete_Gstar_lower"]),
                  mat(c24["complete_Gstar_upper"]),
                  mat(c24["complete_Sstar_upper"])),
          ("MG29",mat(c29["full_original_Gstar_lower"]),
                  mat(c29["full_original_Gstar_upper"]),
                  mat(c29["full_original_Sstar_upper"]))
        ]
        for _,LG,UG,US in parents:
            assert psd(sub(UG,LG)) and psd(US)
        rows=[]
        for label,v in rays:
            x=source_ray(v,B,Hlo,Hup,parents,prev)
            x["archived_original_negative_ray_kind"]=label
            if label=="MG43_original_selected_negative_source_ray":
                assert Q(x["old_MG43_source_lower_ray_margin"])==Q(
                  cs["full24_exact_inertia_witness"]["exact_negative_quadratic"])<0
            rows.append(x)
        results.append({
            "mesh_cells":mesh,"cutoff_k":k,
            "true_original_23adapted_plus_genuine_sinh_pole24D":True,
            "original_full_real_frequency_seven_prime_arch_pole":True,
            "MG43_selected_original_nonscalar_B":cs["source_response_name"],
            "MG43_original_first_moment_alpha":cs["new_G_blend_alpha"],
            "MG43_original_second_moment_beta":cs["new_S_blend_beta"],
            "MG43_original_matrix_eta":cs["new_matrix_eta"],
            "number_independently_grounded_exact_source_rays":len(rows),
            "count_new_directional_upper_strictly_better":sum(
                r["new_directional_bound_improves_MG43_on_this_ray"]
                for r in rows),
            "count_directional_source_lower_nonnegative":sum(
                r["strict_nonnegative_directional_certification"]
                for r in rows),
            "original_exact_source_rays":rows})
    assert [(c["mesh_cells"],c["cutoff_k"]) for c in results]==[
            (16,12),(16,16),(32,12),(32,16)]
    out={
      "status":"ORIGINAL_MG44_EXACT_COUPLED_SOURCE_DIRECTIONAL_SCHWARZ_ENCLOSURES",
      "canonical_W_ODD_NEG":"OPEN",
      "verified_original_MG24_run":39378465438,
      "verified_original_MG29_run":39440914565,
      "verified_original_MG40_run":39513403010,
      "verified_original_MG41_run":39519080670,
      "verified_original_MG42_run":39520549337,
      "verified_original_MG43_run":39522608989,
      "same_true_original_full24_source_operator_moments":True,
      "original_real_frequency_sinh_pole_and_signed_arch_primes_inherited":True,
      "original_two_parent_Loewner_first_moment_brackets":True,
      "original_two_parent_Loewner_second_moment_uppers":True,
      "exact_Cauchy_cross_uncertainty_support_per_fixed_rational_ray":True,
      "sqrt_rounding_outward_only_integer_isqrt":True,
      "complete_original_24D_Loewner_residual_certificate_new":False,
      "individual_ray_certificates_NOT_complete_source_pos":True,
      "total_rays_audited":sum(x["number_independently_grounded_exact_source_rays"]
                              for x in results),
      "total_directional_uppers_strictly_improved":sum(
          x["count_new_directional_upper_strictly_better"] for x in results),
      "total_nonnegative_directional_source_lowers":sum(
          x["count_directional_source_lower_nonnegative"] for x in results),
      "original_24D_complete_source_contraction_certified":False,
      "original_full470_source_inverse_certified":False,
      "signed_original_51over56_negative_cap_certified":False,
      "independent_original_Fourier_form_domain_audit":"OPEN",
      "complete_even_Weil_CC27_RH":"OPEN",
      "cases":results,
      "next":"If individual negative-witness rays clear under independently valid original direction-specific source moment intersections, design a rigorously Loewner-valid full24 joint source residual enclosure (e.g. rational PSD block coupling), not a collection of pointwise rays. If even the tight individual-direction brackets remain negative, direct original source information and correlation beyond MG24/MG29 are needed."
    }
    dest=ROOT/a.output
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(out,indent=2)+"\n")
    print("MG44 original coupled ray-source bounds:",json.dumps({
      "cases":[{"mesh":x["mesh_cells"],"k":x["cutoff_k"],
                "strict_upper_improvements":x[
                    "count_new_directional_upper_strictly_better"],
                "nonnegative_directional_bounds":x[
                    "count_directional_source_lower_nonnegative"],
                "rays":x["number_independently_grounded_exact_source_rays"]}
               for x in results],
      "total_rays":out["total_rays_audited"],
      "total_improved":out["total_directional_uppers_strictly_improved"],
      "total_ray_margins_nonnegative":out["total_nonnegative_directional_source_lowers"],
      "full24_470D_Weil_RH":"OPEN"}),flush=True)
if __name__=="__main__":audit()
