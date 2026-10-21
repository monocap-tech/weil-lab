#!/usr/bin/env python3
"""Independent MG45 acceptance: no import of MG45's computational module.

Rebuild 384 original 24D ray-cell signed residual inequalities, MG32
true omitted-frequency full matrix and scalar intersections, from
accepted source artifacts. All proof-critical signs in Fraction.
"""
import json,sys,argparse
from fractions import Fraction as Q
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
import validate_rpb108_mg32_joint_fourier_residual as original
from validate_rpb108_mg25_original24_robust_trial import original_H24_from_physical_source
from validate_rpb108_mg25_robust_source_aware_residual import Id,plus,sub,mul

N=24
def dot(u,v):return sum((x*y for x,y in zip(u,v)),Q(0))
def qf(v,A):return sum((v[i]*A[i][j]*v[j] for i in range(N)
                       for j in range(N)),Q(0))
def mulv(A,v):return [dot(row,v) for row in A]
def sourcecell(z,B,bmid,brad,cell,d):
    left,right,wl,wu,x,xprime,r=cell
    h=right-left;half=h/2
    a=(wl+wu)/2;da=(wu-wl)/2
    u=mulv(B,z)
    bp=dot(bmid,u)
    C=[z[i]-a*u[i]+(2*bp if i==23 else Q(0)) for i in range(N)]
    q0=dot(x,C);q1=dot(xprime,C)
    sourceerr=sum((r[i]*abs(C[i]) for i in range(N)),Q(0))
    multiplier=da*(abs(dot(x,u))+half*abs(dot(xprime,u))
                   +sum((r[i]*abs(u[i]) for i in range(N)),Q(0)))
    poleamp=abs(x[23])+half*abs(xprime[23])+r[23]
    poleerr=2*poleamp*sum((brad[i]*abs(u[i]) for i in range(N)),Q(0))
    rho=sourceerr+multiplier+poleerr
    # Independently reconstruct the older componentwise MG32 source
    # radii before projecting onto this same signed original ray.
    coordinate=Q(0)
    for j in range(N):
        bj=sum((bmid[i]*B[i][j] for i in range(N)),Q(0))
        coeff=[Q(i==j)-a*B[i][j]+(2*bj if i==23 else Q(0))
               for i in range(N)]
        e=sum((r[i]*abs(coeff[i]) for i in range(N)),Q(0))
        md=da*sum((abs(B[i][j])*(abs(x[i])+half*abs(xprime[i])+r[i])
                   for i in range(N)),Q(0))
        pb=sum((brad[i]*abs(B[i][j]) for i in range(N)),Q(0))
        coordinate+=abs(z[j])*(e+md+2*poleamp*pb)
    assert 0<=rho<=coordinate
    p=2*h*(q0*q0+h*h*q1*q1/12+
           2*rho*(abs(q0)+half*abs(q1))+rho*rho)
    old=2*h*(q0*q0+h*h*q1*q1/12+
             2*coordinate*(abs(q0)+half*abs(q1))+coordinate*coordinate)
    assert 0<=p<=old
    keys=("left","right","original_multiplier_lower","original_multiplier_upper",
          "signed_original_residual_center","signed_original_residual_slope",
          "direct_original_source_linearization_rho",
          "prior_coordinatewise_projected_rho",
          "new_original_coupled_ray_cell_upper",
          "prior_coordinatewise_ray_cell_upper")
    actual=(left,right,wl,wu,q0,q1,rho,coordinate,p,old)
    assert [Q(d[k]) for k in keys]==list(actual)
    assert d["strict_source_radius_improvement"]==(rho<coordinate)
    return p,old,rho<coordinate

def main():
    p=argparse.ArgumentParser()
    for name in ("mg24","mg29","mg32","mg43","mg44","mg45"):
        p.add_argument("--verified-"+name+"-json",required=True)
    a=p.parse_args()
    from validate_rpb108_mg24_complete_original_coupled_source_enclosures import ROOT
    data={name:json.loads((ROOT/getattr(a,"verified_"+name+"_json")).read_text())
          for name in ("mg24","mg29","mg32","mg43","mg44","mg45")}
    d=data["mg45"]
    assert d["status"]=="ORIGINAL_MG45_SIGNED_SOURCE_RAY_FOURIER_RESIDUAL_LINEARIZATION"
    assert d["canonical_W_ODD_NEG"]=="OPEN"
    assert [d[k] for k in ("MG24_verified_original_run","MG29_verified_original_run",
       "MG32_verified_original_run","MG43_verified_original_run",
       "MG44_verified_original_run")]==[
       39378465438,39440914565,39459624082,39522608989,39542236311]
    h,hrad,Herr=original_H24_from_physical_source()
    assert Herr==Q(data["mg24"]["physical_Gram_Loewner_row_error"])
    Hlo=sub(h,mul(Herr,Id(N)))
    Hup=plus(h,mul(Herr,Id(N)))
    bmid=[h[i][23] for i in range(N)]
    brad=[hrad[i][23] for i in range(N)]
    assert [str(x) for x in bmid]==data["mg24"]["original_pole_b_center"]
    assert [str(x) for x in brad]==data["mg24"]["original_pole_b_radii"]
    cells,HClo,HCup,radius,counts=original.exact_original_cells()
    assert len(cells)==32
    assert radius==Q(next(x for x in data["mg29"]["meshes"]
             if x["mesh_cells"]==32)["total_source_radius_MG29"])
    original.cutoff_tail={
        q["cutoff_k"]:q["complete_original_strong_tail_rational"]
        for q in data["mg24"]["cases"]}
    rays=improved=full=nonneg=0
    for c in d["cases"]:
        k=c["cutoff_k"];mesh=c["mesh_cells"]
        old43=next(q for q in data["mg43"]["scenarios"]
                   if q["mesh_cells"]==mesh and q["cutoff_k"]==k)
        old44=next(q for q in data["mg44"]["cases"]
                   if q["mesh_cells"]==mesh and q["cutoff_k"]==k)
        B=[[Q(v) for v in row] for row in old43["exact_original_rational_B"]]
        rem,beta,polefee=original.complement_upper(
            Hup,HClo,bmid,brad,B,k)
        assert c["MG32_original_omitted_frequency_beta"]==str(beta)
        assert c["MG32_original_pole_remainder_error_fee"]==str(polefee)
        assert len(c["rays"])==len(old44["original_exact_source_rays"])==3
        locimp=locfull=locnon=0
        for r,old in zip(c["rays"],old44["original_exact_source_rays"]):
            rays+=1
            z=[Q(q) for q in r["original_source_rational_ray"]]
            assert z==[Q(q) for q in old["nonzero_original_24D_rational_ray"]]
            assert r["same_archived_original_exact_ray_kind"]==old[
                "archived_original_negative_ray_kind"]
            detail=r["per_cell_exact_diagnostics"]
            assert len(detail)==32
            t=to=Q(0);count=0
            for cell,one in zip(cells,detail):
                v,u,gain=sourcecell(z,B,bmid,brad,cell,one)
                t+=v;to+=u;count+=gain
            assert t<=to
            remainder=qf(z,rem)
            assert remainder>=0
            complete=t+remainder
            archive=Q(old["certified_intersection_upper_with_MG43"])
            selected=min(complete,archive)
            margin=qf(z,Hlo)-selected
            fields=("new_original_direct_prefix_ray_upper",
                    "prior_original_coordinatewise_ray_upper",
                    "original_omitted_frequency_true_residual_upper",
                    "new_complete_original_joint_ray_upper",
                    "previous_MG44_valid_complete_frequency_ray_upper",
                    "selected_intersected_valid_original_ray_upper",
                    "selected_source_rational_lower_margin")
            assert [Q(r[x]) for x in fields]==[
                t,to,remainder,complete,archive,selected,margin]
            assert r["number_original_source_cells"]==32
            assert r["number_original_source_cells_with_strict_radius_gain"]==count
            assert r["strict_direct_band_improvement_over_old_coordinatewise"]==(t<to)
            assert r["strict_full_frequency_improvement_over_MG44"]==(complete<archive)
            assert r["original_pole_included_before_absolute_squaring"]
            assert not r["new_complete_24D_residual_Loewner_matrix_claimed"]
            assert margin>=Q(old["selected_direction_only_source_margin"])
            locimp+=t<to;locfull+=complete<archive;locnon+=margin>=0
        assert [c[x] for x in (
          "number_rays_with_strict_original_prefix_improvement",
          "number_rays_with_strict_complete_frequency_improvement",
          "number_nonnegative_complete_source_ray_margins")]==[
          locimp,locfull,locnon]
        improved+=locimp;full+=locfull;nonneg+=locnon
    assert rays==d["total_original_exact_rays"]==12
    assert improved==d["total_strict_prefix_gain_rays"]
    assert full==d["total_strict_complete_frequency_gain_rays"]
    assert nonneg==d["total_nonnegative_original_complete_ray_lowers"]
    assert not d["complete_original_24D_source_strict_contraction_certified"]
    assert not d["original_full470_source_inverse_certified"]
    assert not d["signed_original_51over56_negative_cap_certified"]
    assert d["independent_original_Fourier_form_domain_audit"]=="OPEN"
    assert d["complete_even_Weil_CC27_RH"]=="OPEN"
    print("MG45 INDEPENDENT ORIGINAL exact signed Fourier-source replay PASS",{
         "rays":rays,"original_cells":rays*32,
         "strict_prefix":improved,"strict_full":full,
         "nonnegative_complete_directional":nonneg})
if __name__=="__main__":main()
