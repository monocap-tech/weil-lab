#!/usr/bin/env python3
"""MG45: genuinely new, original complete-frequency source-ray Fourier coupling.

For each of MG44's 12 archived rational rays z and the same genuine
nonscalar 24x24 response B, revisit the ORIGINAL MG32 physical 32-cell
Fourier source rows t(xi)=v+d*h+e, |e_i|<=r_i, all on [0,4].
The actual signed seven-prime/digamma multiplier satisfies
a(xi) in [a0-da,a0+da]; actual pole column b in bmid +/- brad.
For u=Bz and p=bmid dot u, original residual on this source ray is
 r_z(xi)=t(xi) dot (z-a(xi)u+2 e_p (b dot u)).
The new scalar source-row linearization is
 center = v dot C0 z,
 slope = d dot C0 z,
 |remainder| <= rho,
 rho = sum_i r_i |(C0z)_i|
     +da*(|v dot u|+half*|d dot u|+sum_i r_i |u_i|)
     +2*(|v_p|+half*|d_p|+r_p)*sum_i brad_i |u_i|,
 where (C0z)_i=z_i-a0*u_i+2 delta_(i,p)*p.
This retains signed source-vector correlation BEFORE componentwise
absolute error amplification. It is certified for EVERY point of each
original actual full cell, including pole and multiplier uncertainty.

Integrate exactly using +/- frequency symmetry:
  X_cell(z) <= 2 width * [
    center^2 +width^2*slope^2/12
    +2rho*(|center|+half*|slope|)+rho^2].
The older coordinatewise MG32 source-radii projected with |z_j|
provide a separate >=rho bound on the SAME exact true residual ray;
assert rho<=rho_coordinate on all 384 ray-cells.

Outside [0,4] the original complete-frequency residual covariance
is bounded using the independently accepted MG32 physical mass/SM41
complement (not ignored or double-counted); its scalar projection is
added to the direct original band bound. Intersect (scalar min) with
MG44's separately accepted original complete-frequency ray upper.
No full 24D Loewner matrix can be inferred from 12 fixed rays.

No true signed spectrum, all-470 inverse, 51/56 cap, even/Weil/RH.
"""
import argparse,json,sys
from fractions import Fraction as Q
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
import validate_rpb108_mg32_joint_fourier_residual as mg32
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import ROOT
from validate_rpb108_mg25_original24_robust_trial import (
    deserialize,original_H24_from_physical_source)
from validate_rpb108_mg25_robust_source_aware_residual import (
    T,plus,sub,mul,Id)
N=24
P=23

def vec_dot(u,v):
    assert len(u)==len(v)==N
    return sum((x*y for x,y in zip(u,v)),Q(0))
def qf(v,A):
    assert len(v)==N and len(A)==N
    return sum((v[i]*A[i][j]*v[j] for i in range(N)
                for j in range(N)),Q(0))
def matrix_vector(A,v):
    assert len(A)==N and all(len(row)==N for row in A)
    return [vec_dot(row,v) for row in A]
def one_cell(z,B,bmid,brad,cell):
    u=matrix_vector(B,z)
    left,right,lo,hi,v,d,r=cell
    assert left<right and 0<lo<=hi and len(v)==len(d)==len(r)==N
    width=right-left;half=width/2
    a0=(lo+hi)/2;da=(hi-lo)/2
    dot_bu=vec_dot(bmid,u)
    dot_delta=sum((brad[i]*abs(u[i]) for i in range(N)),Q(0))
    Cz=[z[i]-a0*u[i]+(2*dot_bu if i==P else 0) for i in range(N)]
    center=vec_dot(v,Cz)
    slope=vec_dot(d,Cz)
    base=sum((r[i]*abs(Cz[i]) for i in range(N)),Q(0))
    Fourier_u_r=sum((r[i]*abs(u[i]) for i in range(N)),Q(0))
    multiplier=da*(abs(vec_dot(v,u))+half*abs(vec_dot(d,u))+Fourier_u_r)
    vp=abs(v[P])+half*abs(d[P])+r[P]
    pole=2*vp*dot_delta
    rho=base+multiplier+pole
    assert rho>=0
    # Independently recover MG32's ORIGINAL columnwise residual
    # enclosure and project its absolute error radii on this z.
    prior=Q(0)
    for j in range(N):
        bj=sum((bmid[i]*B[i][j] for i in range(N)),Q(0))
        rowrad=sum((r[i]*abs(Q(i==j)-a0*B[i][j]
             +(2*bj if i==P else Q(0))) for i in range(N)),Q(0))
        weight=da*sum((abs(B[i][j])*
            (abs(v[i])+half*abs(d[i])+r[i]) for i in range(N)),Q(0))
        perr=sum((brad[i]*abs(B[i][j]) for i in range(N)),Q(0))
        prior+=abs(z[j])*(rowrad+weight+2*vp*perr)
    assert rho<=prior
    primary=2*width*(center*center+width*width*slope*slope/12
                 +2*rho*(abs(center)+half*abs(slope))+rho*rho)
    old=2*width*(center*center+width*width*slope*slope/12
                 +2*prior*(abs(center)+half*abs(slope))+prior*prior)
    assert 0<=primary<=old
    return {
       "left":str(left),"right":str(right),
       "original_multiplier_lower":str(lo),"original_multiplier_upper":str(hi),
       "signed_original_residual_center":str(center),
       "signed_original_residual_slope":str(slope),
       "direct_original_source_linearization_rho":str(rho),
       "prior_coordinatewise_projected_rho":str(prior),
       "new_original_coupled_ray_cell_upper":str(primary),
       "prior_coordinatewise_ray_cell_upper":str(old),
       "strict_source_radius_improvement":rho<prior}
# Deliberately avoid an implicit/global B parameter at acceptance:
# the full B is supplied through this wrapper.
def cell_bounds(z,B,bmid,brad,cell):
    return one_cell(z,B,bmid,brad,cell)
def synthetic_regression():
    Z=[Q(0)]*N;Z[0]=Q(1);Z[1]=Q(-1)
    B=[[Q(i==j) for j in range(N)] for i in range(N)]
    bb=[Q(0)]*N;rr=[Q(0)]*N
    v=[Q(0)]*N;v[0]=Q(1);v[1]=Q(1)
    d=[Q(0)]*N
    r=[Q(0)]*N;r[0]=Q(1,10);r[1]=Q(1,10)
    c=(Q(0),Q(1),Q(1),Q(2),v,d,r)
    out=cell_bounds(Z,B,bb,rr,c)
    assert Q(out["signed_original_residual_center"])==0
    assert Q(out["prior_coordinatewise_projected_rho"])>=Q(
        out["direct_original_source_linearization_rho"])
    assert Q(out["new_original_coupled_ray_cell_upper"])<=Q(
        out["prior_coordinatewise_ray_cell_upper"])
    return True
def main():
    p=argparse.ArgumentParser()
    for n in ("mg24","mg29","mg32","mg43","mg44"):
        p.add_argument("--verified-"+n+"-json")
    p.add_argument("--self-test",action="store_true")
    p.add_argument("--output",default=
        "artifacts/mg45_original_joint_ray_fourier_residual.json")
    a=p.parse_args()
    assert synthetic_regression()
    if a.self_test:
        print("MG45 exact original signed Fourier scalar residual cancellation regression PASS")
        return
    assert all(getattr(a,"verified_"+n+"_json") for n in
               ("mg24","mg29","mg32","mg43","mg44"))
    load=lambda n:json.loads((ROOT/getattr(a,"verified_"+n+"_json")).read_text())
    m24,m29,m32,m43,m44=(load(n) for n in
                         ("mg24","mg29","mg32","mg43","mg44"))
    assert all(x["canonical_W_ODD_NEG"]=="OPEN" for x in
               (m24,m29,m32,m43,m44))
    assert m24["status"]=="ORIGINAL_COMPLETE_FREQUENCY_24CHANNEL_COUPLED_SOURCE_MATRIX_ENCLOSURES"
    assert m29["status"]=="ORIGINAL_ADAPTED_THIRD_FOURIER_SOURCE_MOMENT_REFINEMENT"
    assert m32["status"]=="ORIGINAL_JOINT_24D_SOURCE_RESIDUAL_FOURIER_PREFIX_AND_TAIL_GATE"
    assert m43["status"]=="ORIGINAL_MG43_INDEPENDENT_COUPLED_G_S_LOEWNER_PARAMETER_RECOMBINATION"
    assert m44["status"]=="ORIGINAL_MG44_EXACT_COUPLED_SOURCE_DIRECTIONAL_SCHWARZ_ENCLOSURES"
    Hmid,Hrad,Herr=original_H24_from_physical_source()
    assert Herr==Q(m24["physical_Gram_Loewner_row_error"])
    Hup=plus(Hmid,mul(Herr,Id(N)))
    Hlo=sub(Hmid,mul(Herr,Id(N)))
    bmid=[Hmid[i][P] for i in range(N)]
    brad=[Hrad[i][P] for i in range(N)]
    assert [str(v) for v in bmid]==m24["original_pole_b_center"]
    assert [str(v) for v in brad]==m24["original_pole_b_radii"]
    cells,HClo,HCup,ra,counts=mg32.exact_original_cells()
    assert len(cells)==32
    assert ra==Q(next(x for x in m29["meshes"]
                 if x["mesh_cells"]==32)["total_source_radius_MG29"])
    mg32.cutoff_tail={c["cutoff_k"]:c["complete_original_strong_tail_rational"]
                      for c in m24["cases"]}
    cases=[]
    for c in m44["cases"]:
        mesh,k=c["mesh_cells"],c["cutoff_k"]
        old43=next(x for x in m43["scenarios"]
                   if x["mesh_cells"]==mesh and x["cutoff_k"]==k)
        B=deserialize(old43["exact_original_rational_B"])
        assert B==[list(row) for row in B]
        remain,beta,polefee=mg32.complement_upper(Hup,HClo,bmid,brad,B,k)
        out=[]
        for ray in c["original_exact_source_rays"]:
            z=[Q(t) for t in ray["nonzero_original_24D_rational_ray"]]
            assert len(z)==N and any(z)
            details=[cell_bounds(z,B,bmid,brad,cell) for cell in cells]
            band=sum((Q(d["new_original_coupled_ray_cell_upper"])
                      for d in details),Q(0))
            band_prior=sum((Q(d["prior_coordinatewise_ray_cell_upper"])
                            for d in details),Q(0))
            assert band<=band_prior
            rem=qf(z,remain)
            assert rem>=0
            whole=band+rem
            old=Q(ray["certified_intersection_upper_with_MG43"])
            best=min(old,whole)
            Hlower=qf(z,Hlo)
            assert Hlower-best>=Q(ray["selected_direction_only_source_margin"])
            out.append({
              "same_archived_original_exact_ray_kind":
                  ray["archived_original_negative_ray_kind"],
              "original_source_rational_ray":[str(t) for t in z],
              "original_signed_multiplier_source_and_pole_recombined":True,
              "all_32_original_contiguous_prefix_cells_replayed":True,
              "new_original_direct_prefix_ray_upper":str(band),
              "prior_original_coordinatewise_ray_upper":str(band_prior),
              "original_omitted_frequency_true_residual_upper":str(rem),
              "new_complete_original_joint_ray_upper":str(whole),
              "previous_MG44_valid_complete_frequency_ray_upper":str(old),
              "selected_intersected_valid_original_ray_upper":str(best),
              "selected_source_rational_lower_margin":str(Hlower-best),
              "strict_full_frequency_improvement_over_MG44":whole<old,
              "strict_direct_band_improvement_over_old_coordinatewise":
                  band<band_prior,
              "number_original_source_cells_with_strict_radius_gain":
                  sum(d["strict_source_radius_improvement"] for d in details),
              "number_original_source_cells":len(details),
              "original_pole_included_before_absolute_squaring":True,
              "new_complete_24D_residual_Loewner_matrix_claimed":False,
              "per_cell_exact_diagnostics":details})
        cases.append({
          "mesh_cells":mesh,"cutoff_k":k,
          "nonscalar_original_source_response":old43["source_response_name"],
          "MG32_original_omitted_frequency_beta":str(beta),
          "MG32_original_pole_remainder_error_fee":str(polefee),
          "number_accepted_exact_original_rays":len(out),
          "number_rays_with_strict_original_prefix_improvement":
              sum(x["strict_direct_band_improvement_over_old_coordinatewise"]
                  for x in out),
          "number_rays_with_strict_complete_frequency_improvement":
              sum(x["strict_full_frequency_improvement_over_MG44"]
                  for x in out),
          "number_nonnegative_complete_source_ray_margins":
              sum(Q(x["selected_source_rational_lower_margin"])>=0
                  for x in out),
          "rays":out})
    assert [(x["mesh_cells"],x["cutoff_k"]) for x in cases]==[
        (16,12),(16,16),(32,12),(32,16)]
    output={
     "status":"ORIGINAL_MG45_SIGNED_SOURCE_RAY_FOURIER_RESIDUAL_LINEARIZATION",
     "canonical_W_ODD_NEG":"OPEN",
     "MG24_verified_original_run":39378465438,
     "MG29_verified_original_run":39440914565,
     "MG32_verified_original_run":39459624082,
     "MG43_verified_original_run":39522608989,
     "MG44_verified_original_run":39542236311,
     "all_original_SI10_25physical_23adapted_plus_true_sinh_pole":True,
     "source_signed_original_seven_prime_arch_and_pole":True,
     "all_32_actual_original_frequency_prefix_cells":True,
     "old_original_MG32_physical_mass_SM41_tail_complement_inherited":True,
     "signed_original_Bv_source_multiplier_coalesced_before_abs":True,
     "all_crosses_in_integrand_preserved_before_scalar_square":True,
     "original_new_directional_bounds_only_not_full24_Loewner":True,
     "total_original_exact_rays":sum(c["number_accepted_exact_original_rays"]
                                     for c in cases),
     "total_strict_prefix_gain_rays":sum(
         c["number_rays_with_strict_original_prefix_improvement"]
         for c in cases),
     "total_strict_complete_frequency_gain_rays":sum(
         c["number_rays_with_strict_complete_frequency_improvement"]
         for c in cases),
     "total_nonnegative_original_complete_ray_lowers":sum(
         c["number_nonnegative_complete_source_ray_margins"] for c in cases),
     "complete_original_24D_source_strict_contraction_certified":False,
     "original_full470_source_inverse_certified":False,
     "signed_original_51over56_negative_cap_certified":False,
     "independent_original_Fourier_form_domain_audit":"OPEN",
     "complete_even_Weil_CC27_RH":"OPEN",
     "cases":cases,
     "next":"If all 32 real-prefix cell source error bounds improve but no full-frequency margin clears, the exact original MG32 omitted-frequency covariance is dominant; improve it by a NEW all-real-frequency source-dependent joint estimate rather than adding measured bands to an unchanged remainder. Do not claim 24D Loewner positivity from fixed-ray scalars."
    }
    dest=ROOT/a.output;dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(output,indent=2)+"\n")
    print("MG45 original signed Fourier ray covariance:",json.dumps({
       "cases":[{
          "mesh":c["mesh_cells"],"k":c["cutoff_k"],
          "strict_prefix_rays":c["number_rays_with_strict_original_prefix_improvement"],
          "strict_full_rays":c["number_rays_with_strict_complete_frequency_improvement"],
          "nonnegative_full_ray_margins":c[
              "number_nonnegative_complete_source_ray_margins"]}
         for c in cases],
         "true_original_rays":output["total_original_exact_rays"],
         "original_source_contraction":False,
         "470D_Weil_RH":"OPEN"}),flush=True)
if __name__=="__main__":main()
