#!/usr/bin/env python3
"""MG28: direct interval enclosure of actual original adapted Fourier curvature.

For 23 ORIGINAL MG11 physical zero-extended double-boundary-vanishing
h_i=f_i-a_i*s-c_i*f_pivot, evaluate the WHOLE transformed Fourier second
derivative at each rational cell midpoint *before taking absolute values*:
 T''_h = T''_f - a_i T''_s - c_i T''_pivot.
The original sinh pole T''_s is differentiated exactly twice from the
SM42 true hyperbolic/trigonometric rational interval formula; the other
24 original physical T'' derivatives use genuine SM46 intervals.
A rigorously bounded whole-cell third derivative pays midpoint drift.

Compare original MG26 componentwise curvature K_old with
  Knew=min(Kold, maxabs(true combined midpoint T'' interval)
                 + (L3_i+|a|L3_pole+|c|L3_pivot)*half).
Rebuild original contiguous [0,4] 24D physical H/G/S source moments
with exactly the same valid MG26 tau policy; retain original physical
Gram complement and all rank-one sinh pole terms in complete frequency
Gstar/Sstar. No unverified 470D inverse or Weil/RH promotion.
"""
import argparse,json,sys
from fractions import Fraction as F
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)

from validate_rpb108_mg26_contiguous_prefix_mass_closure import (
    ROOT,PREFIX,PARTITIONS,KEYS,DIM,CUTS,
    original_partition_preparation,whole_brackets,
    original_H24_from_physical_source,
    original_exact_physical_fourier_midpoint,
    original_midpoint_derivative_intervals,
    transformed_affine,positive_cell_weight_interval,
    CHOSEN_TAUS,lower_cell_trace,finalize,zero,
    add_directed_cell,trace,abs_cap
)
from validate_rpb108_mg27_source_error_budget_audit import (
    splits_original_source
)
from validate_rpb108_sm42_original_physical_gram_and_low_gate import (
    I,PI,B,omega,sin_cos_period
)
from validate_rpb108_mg14_affine_original_two_moments import up
from validate_rpb108_sm46_affine_physical_fourier_source import (
    original_third_spatial_moment
)
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import serialize

def pole_second_frequency_interval(xi,hyp):
    """Actual sinh-pole T''(xi), no guessed finite difference.

    T(w)=N/D with w=2*pi*xi, a=1/2,
    N=2*(a*ch*sin(Bw)-w*sh*cos(Bw)), D=a²+w².
    d²T/dxi²=(2pi)²*[N''/D -2N'D'/D²
                          -ND''/D² +2N(D')²/D³].
    All sin,cos,sinh,cosh and pi are rigorous original rational
    intervals. D>=a²>0 also at xi=0; no pole singularity.
    """
    xi=F(xi);assert xi>=0
    sh,ch=hyp
    w=omega(xi)
    sn,cs=sin_cos_period(B*xi)
    a=F(1,2)
    D=I(a*a)+w*w
    N=2*(a*ch*sn-w*sh*cs)
    Np=2*(a*ch*B*cs-sh*cs+w*sh*B*sn)
    Npp=2*(-a*ch*B*B*sn+2*sh*B*sn+w*sh*B*B*cs)
    Dw=2*w
    val=Npp/D - 2*Np*Dw/(D*D) - 2*N/(D*D)+2*N*Dw*Dw/(D*D*D)
    pii=I(PI[0],PI[1])
    result=4*pii*pii*val
    assert result.l<=result.h
    return result

def exact_original_second_midpoint(mid,centers,sources,hyp):
    """SM46 original 25 T''s, replacing its unavailable pole second."""
    _,second=original_midpoint_derivative_intervals(
        mid,centers,sources,hyp)
    assert len(second)==25 and second[24] is None
    second[24]=pole_second_frequency_interval(mid,hyp)
    assert all(z is not None for z in second)
    return second

def true_direct_adapted_curvature(second,third,a,c,old_K,half):
    """Original 23 adapted channels, plus real pole at index 23."""
    assert len(second)==len(third)==len(old_K)==25
    output=[]
    # Original free physical source indices are 0,..,22.
    for i in range(23):
        # Both coefficient intervals and source intervals are genuine
        # original SI10/SM46 objects, no floating point evaluations.
        combo=second[i]-a[i]*second[24]-c[i]*second[23]
        drift=third[i]+abs_cap(a[i])*third[24]+abs_cap(c[i])*third[23]
        direct=abs_cap(combo)+drift*half
        old=old_K[i]+abs_cap(a[i])*old_K[24]+abs_cap(c[i])*old_K[23]
        bounded=min(old,direct)
        assert bounded>=0 and bounded<=old
        output.append((bounded,old,direct))
    # Last adapted source is exactly sinh pole, not an elimination.
    direct_p=abs_cap(second[24])+third[24]*half
    output.append((min(old_K[24],direct_p),old_K[24],direct_p))
    assert len(output)==DIM
    return output

def calculate_partition(m,prep):
    centers,sources,a,c,hyp,Kglobal,Kthird=prep
    assert m in PARTITIONS and len(sources)==25
    # Initial pole formula parity at origin is an independent
    # analytic regression: odd pole transform => T''_s(0)=0.
    zero_p=pole_second_frequency_interval(F(0),hyp)
    assert zero_p.l<=0<=zero_p.h
    mats={key:(zero(),zero()) for key in KEYS}
    taus={key:{str(t):0 for t in CHOSEN_TAUS} for key in KEYS}
    changed=0;delta_r=F(0);old_total=F(0);new_total=F(0)
    curvature_old=F(0);curvature_new=F(0)
    top=[]
    cells=[]
    for j in range(m):
        l=PREFIX*F(j,m);r=PREFIX*F(j+1,m)
        h=r-l;half=h/2;mid=(l+r)/2
        wlo,whi,_=positive_cell_weight_interval(l,r)
        vals=original_exact_physical_fourier_midpoint(
            mid,centers,sources,hyp)
        deriv,seconds=original_midpoint_derivative_intervals(
            mid,centers,sources,hyp)
        oldK=[min(glob,abs_cap(local)+third*half)
              if local is not None else glob
              for glob,local,third in zip(Kglobal,seconds,Kthird)]
        v,d,eold=transformed_affine(vals,deriv,oldK,a,c,half)
        original_components=splits_original_source(
            v,d,eold,oldK,half,vals,deriv,a,c,23,24)
        actual_second=exact_original_second_midpoint(
            mid,centers,sources,hyp)
        curv=true_direct_adapted_curvature(
            actual_second,Kthird,a,c,oldK,half)
        enew=[]
        for i,(rv,rd,oldcurv,rounding) in enumerate(original_components):
            k_direct,k_old,k_test=curv[i]
            assert k_direct<=k_old
            er=up(rv+rd+k_direct*half*half/2)
            assert er<=eold[i], ("new certified radius exceeded old",j,i)
            assert er>=rv+rd+k_direct*half*half/2
            old_total+=eold[i];new_total+=er
            curvature_old+=oldcurv
            curvature_new+=k_direct*half*half/2
            delta_r+=eold[i]-er
            changed+=int(er<eold[i])
            enew.append(er)
            top.append((eold[i]-er,j,i))
        for key in KEYS:
            L,U=(((F(1),F(1)) if key=="mass" else
                   (wlo,whi) if key=="one" else
                   (wlo*wlo,whi*whi)))
            # Choose the SAME tau that MG26 used on the same cell,
            # isolating radius improvement from optimizer effects.
            tau=max(CHOSEN_TAUS,key=lambda t:
               (lower_cell_trace((L,U),h,v,d,eold,t),-t))
            taus[key][str(tau)]+=1
            add_directed_cell({key:mats},key,key,(L,U),
                              h,v,d,enew,tau)
        cells.append({"left":str(l),"right":str(r),
                      "source_radius_old_sum":str(sum(eold,F(0))),
                      "source_radius_new_sum":str(sum(enew,F(0))),
                      "strictly_improved_channels":sum(
                           x<y for x,y in zip(enew,eold))})
    assert len(cells)==m
    assert cells[0]["left"]=="0" and cells[-1]["right"]==str(PREFIX)
    moments={}
    for key in KEYS:
        L,U,ell,eu=finalize(mats[key])
        moments[key]={
            "lower_matrix":L,"upper_matrix":U,
            "lower_trace":trace(L),"upper_trace":trace(U),
            "lower_rounding":ell,"upper_rounding":eu}
    return {
      "cell_count":m,
      "measured_positive_prefix":["0",str(PREFIX)],
      "physical_original_25_catalog":True,
      "24_original_23pluspole_channels":True,
      "pole_second_analytic_interval_parity_regression":True,
      "true_transformed_second_derivative_midpoints_used":True,
      "no_float_derivatives_used":True,
      "strictly_improved_cell_channels":changed,
      "sum_old_source_radii":str(old_total),
      "sum_new_source_radii":str(new_total),
      "source_radius_total_reduction":str(delta_r),
      "source_curvature_old_total":str(curvature_old),
      "source_curvature_direct_total":str(curvature_new),
      "same_original_MG26_tau_counts":taus,
      "top_source_radius_reductions":[
          {"source_channel":i,"pole_channel":i==23,"cell_index":j,
           "radius_reduction":str(w)}
          for w,j,i in sorted(top,reverse=True)[:10]],
      "per_cell":cells,
      "full_24D":moments
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--verified-mg26-json",required=True)
    p.add_argument("--verified-mg24-json",required=True)
    p.add_argument("--output",default=
         "artifacts/mg28_direct_adapted_source_curvature.json")
    o=p.parse_args()
    mg26=json.loads((ROOT/o.verified_mg26_json).read_text())
    mg24=json.loads((ROOT/o.verified_mg24_json).read_text())
    assert mg26["status"]=="ORIGINAL_CONTIGUOUS_PREFIX_COUPLED_MASS_CLOSURE_24D"
    assert mg26["canonical_W_ODD_NEG"]=="OPEN"
    assert mg24["status"]==(
        "ORIGINAL_COMPLETE_FREQUENCY_24CHANNEL_COUPLED_SOURCE_MATRIX_ENCLOSURES")
    assert mg24["canonical_W_ODD_NEG"]=="OPEN"
    Hmid,Hrad,Herr=original_H24_from_physical_source()
    assert Herr==F(mg24["physical_Gram_Loewner_row_error"])
    b=[Hmid[i][23] for i in range(DIM)]
    eb=[Hrad[i][23] for i in range(DIM)]
    sigma=b[23];esigma=eb[23]
    prep=original_partition_preparation()
    runs=[]
    for m in PARTITIONS:
        part=calculate_partition(m,prep)
        old=next(q for q in mg26["partitions"] if q["cell_count"]==m)
        assert old["weighted_Young_tau_choice_counts"]==part["same_original_MG26_tau_counts"]
        prefix={}
        for key in KEYS:
            new=part["full_24D"][key]
            prior=old["prefix_moments"][key]
            oldw=F(prior["upper_trace"])-F(prior["lower_trace"])
            neww=new["upper_trace"]-new["lower_trace"]
            assert neww>=0 and oldw>0
            prefix[key]={
              "new_lower_trace":str(new["lower_trace"]),
              "new_upper_trace":str(new["upper_trace"]),
              "new_bracket_trace_width":str(neww),
              "verified_MG26_trace_width":str(oldw),
              "new_to_MG26_width_ratio":str(neww/oldw),
              "strict_trace_width_improvement":neww<oldw,
              "new_lower":serialize(new["lower_matrix"]),
              "new_upper":serialize(new["upper_matrix"])
            }
        part["prefix_trace_width_comparison"]=prefix
        scenario=[]
        for case in mg24["cases"]:
            if case["cutoff_k"] not in CUTS:continue
            newcase=whole_brackets(part,case,Hmid,Herr,b,eb,sigma,esigma)
            oldcase=next(x for x in old["complete_original_frequency_scenarios"]
                    if x["cutoff_k"]==case["cutoff_k"])
            for symbol in ("Gstar","Sstar"):
                newwidth=F(newcase["new_"+symbol+"_bracket_width_trace"])
                oldwidth=F(oldcase["new_"+symbol+"_bracket_width_trace"])
                assert oldwidth>0 and newwidth>=0
                newcase[symbol+"_width_ratio_to_MG26"]=str(newwidth/oldwidth)
            scenario.append(newcase)
        part["full_24D"]={
            key:{"lower":serialize(part["full_24D"][key]["lower_matrix"]),
                 "upper":serialize(part["full_24D"][key]["upper_matrix"])}
            for key in KEYS}
        part["complete_original_frequency_scenarios"]=scenario
        runs.append(part)
    out={
      "status":"ORIGINAL_DIRECT_ADAPTED_CURVATURE_MOMENT_CERTIFICATE",
      "canonical_W_ODD_NEG":"OPEN",
      "verified_MG24_run_id":39378465438,
      "verified_MG26_run_id":39380800739,
      "physical_25_source_catalog_24_adapted_channels":True,
      "true_original_sinh_pole_second_interval_included":True,
      "direct_transformed_second_derivative_with_original_coefficients":True,
      "third_derivative_drift_paid":True,
      "all_real_frequencies_closed_with_original_mass_and_SM41_tails":True,
      "new_original_470D_signed_cap_certified":False,
      "independent_original_Fourier_domain_audit":"OPEN",
      "even_Weil_CC27_RH":"OPEN",
      "partitions":runs}
    outpath=ROOT/o.output
    outpath.parent.mkdir(parents=True,exist_ok=True)
    outpath.write_text(json.dumps(out,indent=2)+"\n")
    print("MG28 direct original Fourier curvature:",json.dumps({
      "partitions":[{"cells":x["cell_count"],
           "improved_source_cells":x["strictly_improved_cell_channels"],
           "source_radius_reduction":float(F(x["source_radius_total_reduction"])),
           "prefix_width_ratios":{k:float(F(v["new_to_MG26_width_ratio"]))
             for k,v in x["prefix_trace_width_comparison"].items()},
           "global_Gstar_Sstar_ratios":[{
             k:float(F(s[k+"_width_ratio_to_MG26"])) for k in ("Gstar","Sstar")}
             for s in x["complete_original_frequency_scenarios"]]}
             for x in runs],
       "full470_odd_even_Weil_RH":"OPEN"}),flush=True)
if __name__=="__main__":main()
