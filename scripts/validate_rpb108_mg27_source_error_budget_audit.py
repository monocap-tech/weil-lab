#!/usr/bin/env python3
"""MG27: independent exact rational error-budget classification on MG26's
true 24D SI10/MG11 original source prefix [0,4].

Decompose each certified MG26 affine / sourcewise Young trace-width
into three *nonnegative, exact* charges (plus final outward rounding):
  (a) whole-cell original seven-prime/digamma multiplier interval width,
  (b) Young mixing of the nominal affine covariance, and
  (c) sourcewise original Fourier Taylor error.
Further split (c) into source value/derivative enclosure,
second-order Taylor curvature, and outward source-radius rounding.
All 24 genuine physical channels and all prefix cells 8/16 retained.

The exact sums MUST reproduce the previously verified original MG26
prefix H/G/S matrix interval TRACE widths, not only approximate trends.
This is a methodological diagnostic, not a stronger positive matrix
or a 470-source inverse. No unverified high-band claim is made.
"""
import argparse,json,sys
from fractions import Fraction as F
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
from validate_rpb108_mg26_contiguous_prefix_mass_closure import (
    ROOT,PREFIX,PARTITIONS,KEYS,DIM,
    original_partition_preparation,
    original_exact_physical_fourier_midpoint,
    original_midpoint_derivative_intervals,
    transformed_affine,positive_cell_weight_interval,
    CHOSEN_TAUS,lower_cell_trace,hyperbolic_interval,
    abs_cap
)
from validate_rpb108_mg14_affine_original_two_moments import (
    I,centered_interval,up
)

CATS=("multiplier_width","affine_Young","source_value_interval",
      "source_derivative_interval","source_curvature","source_rounding")
SCALE=10**12

def cap(x):
    x=F(x)
    assert x>=0
    t=F(-(-x.numerator*SCALE//x.denominator),SCALE)
    assert t>=x
    return str(t)

def trace_matrix(A):
    return sum((F(A[i][i]) for i in range(len(A))),F(0))

def zero():
    return {c:F(0) for c in CATS}

def splits_original_source(v,d,r,K,half,vals,deriv,a,c,pivot,pole):
    """Recover component fees reproducing actual MG14 transformed_affine.

    Only exact intervals; independent of MG26 matrix loop.
    """
    phys=[I(x-e,x+e) for x,e in vals]
    by_source=[]
    for i in range(len(phys)):
        if i==pivot:continue
        if i==pole:
            x=phys[pole];dx=deriv[pole]
            Kcorr=K[pole]
        else:
            x=phys[i]-a[i]*phys[pole]-c[i]*phys[pivot]
            dx=deriv[i]-a[i]*deriv[pole]-c[i]*deriv[pivot]
            Kcorr=(K[i]+abs_cap(a[i])*K[pole]
                   +abs_cap(c[i])*K[pivot])
        vv,vr=centered_interval(x)
        dd,dr=centered_interval(dx)
        a0=vr; a1=dr*half; a2=Kcorr*half*half/2
        rr=up(a0+a1+a2)
        assert rr>=a0+a1+a2
        t=len(by_source)
        assert vv==v[t] and dd==d[t] and rr==r[t],(
            "MG26 original Fourier/source bound drift",i,t)
        by_source.append((a0,a1,a2,rr-(a0+a1+a2)))
    assert len(by_source)==DIM
    return by_source

def exact_source_trace_widths(cell_width,weight_lo,weight_hi,v,d,r,
                              components,tau):
    """Exact trace difference in the SAME MG26 directional Young policy."""
    assert F(0)<weight_lo<=weight_hi and F(0)<tau<1
    assert len(v)==len(d)==len(r)==len(components)==DIM
    s=sum(r,F(0))
    out=zero()
    per_source=[]
    for i in range(DIM):
        cii=v[i]*v[i]+cell_width*cell_width*d[i]*d[i]/12
        mult=2*cell_width*(weight_hi-weight_lo)*cii
        young=2*cell_width*tau*(weight_hi+weight_lo)*cii
        fee=2*cell_width*(
            (weight_hi+weight_lo)/tau +weight_hi-weight_lo)*s
        rv,rd,rc,rounding=components[i]
        source_components=[fee*x for x in (rv,rd,rc,rounding)]
        assert sum(source_components,F(0))==fee*r[i]
        parts=[mult,young]+source_components
        assert len(parts)==len(CATS) and all(z>=0 for z in parts)
        for key,value in zip(CATS,parts):out[key]+=value
        per_source.append(dict(zip(CATS,parts)))
    # Verify symbolic decomposition against the literal lower/upper
    # original MG15/MG26 directional formula, *not* round-off floats.
    C=sum((v[i]*v[i]+cell_width*cell_width*d[i]*d[i]/12
           for i in range(DIM)),F(0))
    lower=2*cell_width*weight_lo*(
        (1-tau)*C-(1/tau-1)*s*s)
    upper=2*cell_width*weight_hi*(
        (1+tau)*C+(1+1/tau)*s*s)
    assert upper-lower==sum(out.values(),F(0))
    return out,per_source

def audit_partition(m,old,prepared):
    centers,sources,a,c,hyp,Kglobal,Kthird=prepared
    assert m in PARTITIONS and len(sources)==25
    original=next(p for p in old["partitions"] if p["cell_count"]==m)
    assert original["true_coverage_no_gaps_or_overlaps"]
    assert original["actual_original_contiguous_positive_band"]==["0","4"]
    sums={key:zero() for key in KEYS}
    source_sums={key:[zero() for _ in range(DIM)] for key in KEYS}
    region_sums={key:[] for key in KEYS}
    tau_counts={key:{str(x):0 for x in CHOSEN_TAUS} for key in KEYS}
    worst_radius_records=[]
    for j in range(m):
        left=PREFIX*F(j,m);right=PREFIX*F(j+1,m)
        width=right-left;half=width/2;mid=(left+right)/2
        low,high,_=positive_cell_weight_interval(left,right)
        vals=original_exact_physical_fourier_midpoint(
            mid,centers,sources,hyp)
        derivatives,seconds=original_midpoint_derivative_intervals(
            mid,centers,sources,hyp)
        K=[min(g,abs_cap(local)+third*half)
           if local is not None else g
           for g,local,third in zip(Kglobal,seconds,Kthird)]
        v,d,r=transformed_affine(vals,derivatives,K,a,c,half)
        comps=splits_original_source(v,d,r,K,half,vals,derivatives,
                                     a,c,23,24)
        assert all(sum(p,F(0))==r[i] for i,p in enumerate(comps))
        worst_radius_records.append({
            "left":str(left),"right":str(right),
            "max_source_radius_upper":cap(max(r))})
        for key in KEYS:
            wlo,whi=((F(1),F(1)) if key=="mass"
                      else (low,high) if key=="one"
                      else (low*low,high*high))
            tau=max(CHOSEN_TAUS,key=lambda t:
                (lower_cell_trace((wlo,whi),width,v,d,r,t),-t))
            tau_counts[key][str(tau)]+=1
            cats,per=exact_source_trace_widths(
                width,wlo,whi,v,d,r,comps,tau)
            for name,value in cats.items():sums[key][name]+=value
            for i in range(DIM):
                for name,value in per[i].items():
                    source_sums[key][i][name]+=value
            region_sums[key].append({
                "left":str(left),"right":str(right),
                "chosen_Young_tau":str(tau),
                "multiplier_interval_width_upper":cap(whi-wlo),
                "sum_source_Taylor_radii_upper":cap(sum(r,F(0))),
                "error_categories_upper":{k:cap(x) for k,x in cats.items()},
                "raw_total_trace_width_upper":
                    cap(sum(cats.values(),F(0)))})
    out={}
    for key in KEYS:
        assert tau_counts[key]==original["weighted_Young_tau_choice_counts"][key]
        accepted=original["prefix_moments"][key]
        measured=(trace_matrix(accepted["upper"])
                  -trace_matrix(accepted["lower"]))
        raw=sum(sums[key].values(),F(0))
        # MG26 finalize() rounds true 24x24 lower/upper outward and
        # may add a nonnegative whole-matrix diagonal export fee.
        assert raw<=measured,(
            "MG26 prefix exact source-width reconstruction failed",
            m,key,float(raw),float(measured))
        residual=measured-raw
        assert residual>=0
        dominant=max(CATS,key=lambda k:(sums[key][k],k))
        ranking=sorted(
            [(sum(source_sums[key][i][k] for k in CATS),i)
              for i in range(DIM)],reverse=True)
        assert sum((sum(source_sums[key][i].values(),F(0))
                    for i in range(DIM)),F(0))==raw
        assert all(sums[key][k]>=0 for k in CATS)
        out[key]={
            "certified_original_MG26_prefix_trace_width":str(measured),
            "raw_exact_unrounded_trace_width_upper":cap(raw),
            "outward_export_rounding_fee_upper":cap(residual),
            "categories_upper":{k:cap(sums[key][k]) for k in CATS},
            "dominant_error_category":dominant,
            "dominant_error_share_lower":
                str(F((sums[key][dominant]/measured).numerator*10**9//
                       (sums[key][dominant]/measured).denominator,10**9))
                if measured>0 else "0",
            "per_cell":region_sums[key],
            "top_6_source_trace_width_contributors":[
                {"channel":i,
                 "pole_channel":i==23,
                 "fee_upper":cap(w),
                 "source_fees_upper":{
                    k:cap(x) for k,x in source_sums[key][i].items()}}
                for w,i in ranking[:6]],
            "rational_sum_partition_matches_verified_MG26":True,
            "tau_count_matches_verified_MG26":True
        }
    return {
      "count":m,
      "exact_original_contiguous_frequency_coverage":["0","4"],
      "source_basis_original_23boundary_plus_pole":True,
      "source_radius_samples":worst_radius_records,
      "source_moments":out}

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--verified-mg26-json",required=True)
    parser.add_argument("--output",default=
        "artifacts/mg27_original_prefix_error_budget_audit.json")
    args=parser.parse_args()
    old=json.loads((ROOT/args.verified_mg26_json).read_text())
    assert old["status"]=="ORIGINAL_CONTIGUOUS_PREFIX_COUPLED_MASS_CLOSURE_24D"
    assert old["canonical_W_ODD_NEG"]=="OPEN"
    assert old["verified_MG24_run_id"]==39378465438
    assert old["true_contiguous_prefix_rational_cell_integrals"]
    assert old["all_original_prime7_arch_multiplier_cell_bounds"]
    assert old["true_original_pole_mixed_response_paid"]
    assert [p["cell_count"] for p in old["partitions"]]==[8,16]
    prepared=original_partition_preparation()
    runs=[audit_partition(m,old,prepared) for m in PARTITIONS]
    m8,m16=runs
    diagnosis={}
    for key in KEYS:
        a=m8["source_moments"][key]
        b=m16["source_moments"][key]
        w8=F(a["certified_original_MG26_prefix_trace_width"])
        w16=F(b["certified_original_MG26_prefix_trace_width"])
        assert w8>0 and w16>0
        diagnosis[key]={
          "prefix_width_8_cell":str(w8),
          "prefix_width_16_cell":str(w16),
          "width_improvement_8_to_16":str(w8/w16),
          "dominant_8_cell_charge":a["dominant_error_category"],
          "dominant_16_cell_charge":b["dominant_error_category"],
          "original_16_cell_source_taylor_total_upper":cap(
              sum(F(b["categories_upper"][name]) for name in CATS[2:])),
          "no_extrapolated_32_cell_acceptance":True}
    out={
      "status":"ORIGINAL_MG26_EXACT_SOURCE_ERROR_BUDGET_ATTRIBUTION",
      "canonical_W_ODD_NEG":"OPEN",
      "verified_MG26_run_id":39380800739,
      "MG26_exact_preexport_width_replay_passed":True,
      "same_original_SI10_25generator_23pluspole_source_basis":True,
      "true_original_arch_prime7_interval_weight_paid":True,
      "actual_contiguous_positive_prefix":["0","4"],
      "all_mixed_24D_source_terms_inherited":True,
      "error_fees_classified_exact_rational_before_export":True,
      "sourcewise_Taylor_value_derivative_curvature_and_rounding_separated":True,
      "MG26_original_complete_frequency_Gstar_Sstar_brackets_sharpened":False,
      "new_complete_original_24D_strict_residual":False,
      "actual_470D_signed_original_cap":False,
      "independent_Fourier_form_domain_audit":"OPEN",
      "even_Weil_CC27_RH":"OPEN",
      "partitions":runs,
      "method_diagnosis":diagnosis,
      "decision":"Check exact dominant sourcewise Taylor vs Young vs original multiplier interval fees. Introduce adaptive mesh or non-Young covariance only where measured original source penalty justifies it. No 32-cell / global inverse extrapolation."
    }
    dst=ROOT/args.output;dst.parent.mkdir(parents=True,exist_ok=True)
    dst.write_text(json.dumps(out,indent=2)+"\n")
    print("MG27 original source error-budget audit:",
       json.dumps({"8_to_16":{
        k:{"width_gain":float(F(v["width_improvement_8_to_16"])),
           "dominant_8":v["dominant_8_cell_charge"],
           "dominant_16":v["dominant_16_cell_charge"]}
        for k,v in diagnosis.items()},
       "fully_470_signed_even_Weil_RH":"OPEN"}),flush=True)
if __name__=="__main__":main()
