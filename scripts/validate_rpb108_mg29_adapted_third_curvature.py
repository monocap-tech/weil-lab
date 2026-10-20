#!/usr/bin/env python3
"""MG29: original adapted THIRD Fourier derivative with rigorous fourth drift.

MG27 identified Fourier second-derivative Taylor curvature as the dominant
MG26 source uncertainty. MG28 certified a 16-cell improvement by combining
the original adapted second derivative before absolute values.

MG29 also combines the original THIRD derivative BEFORE absolute values,
including the genuine odd sinh pole via an analytic rational-interval
third derivative. The original universal fourth derivative bound
controls movement from the exact rational midpoint throughout each real
frequency cell. The new second-derivative cap intersects with MG28's.

On [0,4], run 16 and 32 contiguous original physical-source rational
cells, using precisely the same positive signed seven-prime/digamma
multiplier bounds and same MG26 choice of Young tau per cell.
Reconstruct 24D H_C/G_C/S_C and full original frequency Gstar/Sstar
using MG26's physical complement H-H_C and true MG24/SM41 high tails.

All interval proofs are exact Fraction; independent accepted original
MG24/MG26/MG28 artifacts are used for inherited premise/source checks.
No assumption of full 470-source inverse, signed cap, or RH.
"""
import argparse,json,sys
from fractions import Fraction as F
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
from validate_rpb108_mg28_direct_adapted_curvature import (
    pole_second_frequency_interval,exact_original_second_midpoint,
    true_direct_adapted_curvature,
)
from validate_rpb108_sm46_affine_physical_fourier_source import (
    original_F3,
)
from validate_rpb108_sm42_original_physical_gram_and_low_gate import (
    I,PI,B,omega,sin_cos_period
)
from validate_rpb108_mg26_contiguous_prefix_mass_closure import (
    ROOT,PREFIX,KEYS,DIM,CUTS,
    original_partition_preparation,whole_brackets,
    original_H24_from_physical_source,
    original_exact_physical_fourier_midpoint,
    original_midpoint_derivative_intervals,
    transformed_affine,positive_cell_weight_interval,
    CHOSEN_TAUS,lower_cell_trace,finalize,zero,
    add_directed_cell,trace,abs_cap,
)
from validate_rpb108_mg27_source_error_budget_audit import (
    splits_original_source,
)
from validate_rpb108_mg14_affine_original_two_moments import up
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import serialize

MESHES=(16,32)
PHYS=25
POLE=24
PIVOT=23
INTERVAL_EXPORT_DEN=10**12

def outward_interval(x):
    """Exact enclosing rational quantization; NEVER nearest-point sampling.

    Bounds by at most 10^-12 per endpoint, reducing huge SI06 Taylor
    numerator/denominator growth before 24D source/matrix arithmetic.
    """
    d=INTERVAL_EXPORT_DEN
    lo=x.l*d;hi=x.h*d
    lower=F(lo.numerator//lo.denominator,d)
    upper=F(-(-hi.numerator//hi.denominator),d)
    assert lower<=x.l<=x.h<=upper
    return I(lower,upper)

def f3_enclosed(q):
    return outward_interval(original_F3(q))

def original_F4(q):
    """Int[-B,B] x^4 cos(2*pi*q*x) dx via exact rational trig.

    Repeated integration by parts, removable value q=0. The
    frequency phase and pi intervals are inherited SM42 enclosures.
    """
    q=F(q)
    if q==0:return I(2*B**5/5)
    sn,cs=sin_cos_period(B*q)
    w=omega(q)
    return outward_interval(2*(B**4*sn/w + 4*B**3*cs/(w*w)
              -12*B**2*sn/(w**3) -24*B*cs/(w**4)
              +24*sn/(w**5)))

def pole_third_frequency_interval(xi,hyp):
    """Third derivative of original SM42 sinh pole source Fourier T_s.

    Let w=2*pi*xi, D=a^2+w^2, a=1/2 and
    N=2(a*cosh(B/2)*sin(Bw)-w*sinh(B/2)*cos(Bw)).
    d^3(N/D)/dw^3 =
       N'''/D -3N''D'/D² -3N'D''/D²
         +6N'(D')²/D³+6ND'D''/D³-6N(D')³/D⁴.
    Multiply by (2pi)^3, exact rational-interval arithmetic.
    """
    xi=F(xi);assert xi>=0
    sh,ch=hyp
    w=omega(xi)
    sn,cs=sin_cos_period(B*xi)
    a=F(1,2)
    den=I(a*a)+w*w
    N=2*(a*ch*sn-w*sh*cs)
    N1=2*(a*ch*B*cs-sh*cs+w*sh*B*sn)
    N2=2*(-a*ch*B*B*sn+2*sh*B*sn+w*sh*B*B*cs)
    N3=2*(-a*ch*B**3*cs+3*sh*B*B*cs-w*sh*B**3*sn)
    D1=2*w
    D2=2
    term=(N3/den -3*N2*D1/(den**2)-3*N1*D2/(den**2)
          +6*N1*(D1**2)/(den**3)
          +6*N*D1*D2/(den**3)-6*N*(D1**3)/(den**4))
    pi=I(PI[0],PI[1])
    return outward_interval(8*pi*pi*pi*term)

def original_third_midpoint(mid,centers,sources,hyp):
    """True original 25 generator T''' intervals, INCLUDING pole."""
    pi=I(PI[0],PI[1])
    factor=-4*pi*pi*pi
    result=[]
    for typ,j,k in sources:
        if typ=="pole":
            interval=pole_third_frequency_interval(mid,hyp)
        elif k==0:
            c=centers[j]
            interval=factor*(f3_enclosed(c+mid)+f3_enclosed(c-mid))
        elif k==1:
            c=centers[j]
            interval=factor*(original_F4(mid+c)+original_F4(mid-c))
        else:
            raise AssertionError("unverified source polynomial degree")
        result.append(outward_interval(interval))
    assert len(result)==PHYS
    return result

def original_fourth_global(sources):
    """Entire real |T''''| <= (2*pi_upper)^4 int |x^4 g(x)| dx.

    Original odd sin(c*x), pole sinh(x/2) have |g|<=1.
    Original xcos source has |g|<=|x|. No support extrapolation.
    """
    pref=16*PI[1]**4
    return [
       pref*(B**6/3 if typ!="pole" and k==1 else 2*B**5/5)
       for typ,j,k in sources
    ]

def third_adapted_whole_cell(mid,centers,sources,hyp,a,c,old3,half,global4):
    """True adapted third derivative on full cell.

    The midpoint adapted interval is calculated BEFORE taking
    absolutes. A sourcewise fourth drift then bounds the full
    real cell. Intersect with the already proved MG28 third bound.
    """
    d3=original_third_midpoint(mid,centers,sources,hyp)
    assert len(d3)==len(old3)==len(global4)==PHYS
    result=[]
    for i in range(23):
        t=d3[i]-a[i]*d3[POLE]-c[i]*d3[PIVOT]
        old=(old3[i]+abs_cap(a[i])*old3[POLE]
             +abs_cap(c[i])*old3[PIVOT])
        drift=global4[i]+abs_cap(a[i])*global4[POLE]+abs_cap(c[i])*global4[PIVOT]
        candidate=abs_cap(t)+drift*half
        result.append((min(old,candidate),old,candidate))
    pole_direct=abs_cap(d3[POLE])+global4[POLE]*half
    result.append((min(old3[POLE],pole_direct),old3[POLE],pole_direct))
    assert len(result)==DIM
    assert all(F(0)<=new<=old for new,old,_ in result)
    return result

def analytic_regressions(hyp):
    """Independent analytic parity and pole third-derivative sign."""
    second0=pole_second_frequency_interval(F(0),hyp)
    third0=pole_third_frequency_interval(F(0),hyp)
    assert second0.l<=0<=second0.h  # odd transform
    # T_s'''(0)=-(2pi)^3 int[-B,B] x^3 sinh(x/2) dx <0.
    assert third0.h<0
    # Original physical F4 is even and has removable origin.
    assert original_F4(F(0)).l==original_F4(F(0)).h==2*B**5/5
    for q in (F(1,4),F(1,2),F(1)):
        a=original_F4(q);b=original_F4(-q)
        assert max(a.l,b.l)<=min(a.h,b.h)
    return True

def calculate_mesh(m,prep):
    centers,sources,a,c,hyp,Kglobal,Kthird=prep
    assert m in MESHES and PREFIX>0 and len(sources)==PHYS
    global4=original_fourth_global(sources)
    assert analytic_regressions(hyp)
    policy=("mg28_replay","mg29_third")
    mats={name:{key:(zero(),zero()) for key in KEYS} for name in policy}
    taus={key:{str(t):0 for t in CHOSEN_TAUS} for key in KEYS}
    n_changed=0; sum28=sum29=F(0); sumK28=sumK29=F(0)
    src_diffs=[F(0) for _ in range(DIM)]
    cells=[];curvature_new_by_cell=[]
    for j in range(m):
        left=PREFIX*F(j,m);right=PREFIX*F(j+1,m)
        width=right-left;half=width/2;mid=(left+right)/2
        wl,wu,_=positive_cell_weight_interval(left,right)
        vals=original_exact_physical_fourier_midpoint(mid,centers,sources,hyp)
        dfirst,dsecond=original_midpoint_derivative_intervals(
            mid,centers,sources,hyp)
        physicalK=[
            min(g,abs_cap(sec)+th*half) if sec is not None else g
            for g,sec,th in zip(Kglobal,dsecond,Kthird)]
        v,d,eold=transformed_affine(
            vals,dfirst,physicalK,a,c,half)
        components=splits_original_source(
            v,d,eold,physicalK,half,vals,dfirst,a,c,PIVOT,POLE)
        actual_second=exact_original_second_midpoint(
            mid,centers,sources,hyp)
        third=third_adapted_whole_cell(
            mid,centers,sources,hyp,a,c,Kthird,half,global4)
        K28=true_direct_adapted_curvature(
            actual_second,Kthird,a,c,physicalK,half)
        # Refined full-cell second derivative:
        # |T''(x)|<=|T''(mid)|+sup_cell|T'''|*half.
        K29=[]
        for i in range(DIM):
            k28,old,generic=K28[i]
            t2=(actual_second[i]-a[i]*actual_second[POLE]-
                c[i]*actual_second[PIVOT]) if i<23 else actual_second[POLE]
            candidate=abs_cap(t2)+third[i][0]*half
            k29=min(k28,candidate)
            assert F(0)<=k29<=k28
            K29.append(k29)
        e28=[];e29=[]
        for i,(value,derivative,oldcurv,rounding) in enumerate(components):
            r28=up(value+derivative+K28[i][0]*half*half/2)
            r29=up(value+derivative+K29[i]*half*half/2)
            assert r29<=r28<=eold[i]
            e28.append(r28);e29.append(r29)
            src_diffs[i]+=r28-r29
            sum28+=r28;sum29+=r29
            sumK28+=K28[i][0]*half*half/2
            sumK29+=K29[i]*half*half/2
            n_changed+=int(r29<r28)
        for key in KEYS:
            low,hi=((F(1),F(1)) if key=="mass"
                    else (wl,wu) if key=="one"
                    else (wl*wl,wu*wu))
            # Frozen original MG26 tau (selected against eold),
            # so reduction reflects direct derivative, not optimizer.
            tau=max(CHOSEN_TAUS,key=lambda t:(
                lower_cell_trace((low,hi),width,v,d,eold,t),-t))
            taus[key][str(tau)]+=1
            add_directed_cell({key:mats["mg28_replay"]},key,key,
                              (low,hi),width,v,d,e28,tau)
            add_directed_cell({key:mats["mg29_third"]},key,key,
                              (low,hi),width,v,d,e29,tau)
        cells.append({"left":str(left),"right":str(right),
                      "strict_improved_channels":
                          sum(x<y for x,y in zip(e29,e28)),
                      "sum_MG28_radii":str(sum(e28,F(0))),
                      "sum_MG29_radii":str(sum(e29,F(0))),
                      "sum_transformed_third_drift_old":str(
                          sum(t[1] for t in third)),
                      "sum_transformed_third_drift_new":str(
                          sum(t[0] for t in third))})
    assert cells[0]["left"]=="0" and cells[-1]["right"]==str(PREFIX)
    assert all(cells[i]["right"]==cells[i+1]["left"]
               for i in range(m-1))
    out={}
    for pol in policy:
        moments={}
        for key in KEYS:
            L,U,el,eu=finalize(mats[pol][key])
            assert trace(U)>=trace(L)
            moments[key]={
                 "lower_matrix":L,"upper_matrix":U,
                 "trace_width":trace(U)-trace(L),
                 "lower_trace":trace(L),"upper_trace":trace(U)}
        out[pol]=moments
    assert sum29<=sum28 and sumK29<=sumK28
    return {"cell_count":m,"prefix":["0",str(PREFIX)],
            "actual_25_original_SI10_physical_sources":True,
            "coupled_24_original_channels":True,
            "original_pole_third_exact_analytic_interval":True,
            "direct_transformed_original_third_before_absolute":True,
            "whole_cell_fourth_derivative_drift_paid":True,
            "source_radii_29_le_28_every_cell_channel":True,
            "number_strictly_improved_source_cell_pairs":n_changed,
            "sum_28_radii":str(sum28),"sum_29_radii":str(sum29),
            "sum_28_curvature_remainders":str(sumK28),
            "sum_29_curvature_remainders":str(sumK29),
            "per_source_radius_improvement":[str(x) for x in src_diffs],
            "frozen_original_MG26_tau_counts":taus,
            "cells":cells,"matrices":out}

def original_scenarios(mdata,old24,Hmid,Herr,b,eb,sigma,esigma):
    from validate_rpb108_mg26_contiguous_prefix_mass_closure import whole_brackets
    scen={}
    for pol in ("mg28_replay","mg29_third"):
        scen[pol]=[]
        for case in old24["cases"]:
            if case["cutoff_k"] not in CUTS:continue
            part={"full_24D":mdata["matrices"][pol]}
            res=whole_brackets(part,case,Hmid,Herr,b,eb,sigma,esigma)
            scen[pol].append(res)
    return scen

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--verified-mg24-json",required=True)
    p.add_argument("--verified-mg26-json",required=True)
    p.add_argument("--verified-mg28-json",required=True)
    p.add_argument("--output",default="artifacts/mg29_original_direct_third_drift.json")
    opt=p.parse_args()
    m24=json.loads((ROOT/opt.verified_mg24_json).read_text())
    m26=json.loads((ROOT/opt.verified_mg26_json).read_text())
    m28=json.loads((ROOT/opt.verified_mg28_json).read_text())
    assert m24["status"]=="ORIGINAL_COMPLETE_FREQUENCY_24CHANNEL_COUPLED_SOURCE_MATRIX_ENCLOSURES"
    assert m26["status"]=="ORIGINAL_CONTIGUOUS_PREFIX_COUPLED_MASS_CLOSURE_24D"
    assert m28["status"]=="ORIGINAL_DIRECT_ADAPTED_CURVATURE_MOMENT_CERTIFICATE"
    assert all(z["canonical_W_ODD_NEG"]=="OPEN" for z in (m24,m26,m28))
    assert m28["verified_MG24_run_id"]==39378465438
    assert m28["verified_MG26_run_id"]==39380800739
    Hmid,Hrad,Herr=original_H24_from_physical_source()
    assert Herr==F(m24["physical_Gram_Loewner_row_error"])
    b=[Hmid[i][23] for i in range(DIM)]
    eb=[Hrad[i][23] for i in range(DIM)]
    sigma=b[23];esigma=eb[23]
    prep=original_partition_preparation()
    reports=[]
    for mesh in MESHES:
        part=calculate_mesh(mesh,prep)
        if mesh==16:
            p28=next(x for x in m28["partitions"] if x["cell_count"]==16)
            assert part["frozen_original_MG26_tau_counts"]==p28["same_original_MG26_tau_counts"]
            assert part["sum_28_radii"]==p28["sum_new_source_radii"]
            for k in KEYS:
                prior=p28["prefix_trace_width_comparison"][k]
                assert part["matrices"]["mg28_replay"][k]["trace_width"]==F(
                    prior["new_bracket_trace_width"]),(
                    "MG29 must replay independently accepted original MG28 exactly",k)
        comparisons={}
        for k in KEYS:
            old=part["matrices"]["mg28_replay"][k]["trace_width"]
            new=part["matrices"]["mg29_third"][k]["trace_width"]
            assert old>0 and new>=0
            comparisons[k]={
                 "mg28_same_mesh_trace_width":str(old),
                 "mg29_direct_third_trace_width":str(new),
                 "new_over_mg28_width":str(new/old),
                 "strict_improvement":new<old}
        scenarios=original_scenarios(part,m24,Hmid,Herr,b,eb,sigma,esigma)
        merged=[]
        for idx in range(len(CUTS)):
            c28=scenarios["mg28_replay"][idx]
            c29=scenarios["mg29_third"][idx]
            assert c28["cutoff_k"]==c29["cutoff_k"]==CUTS[idx]
            entry={
              "cutoff_k":CUTS[idx],
              "original_complete_frequency_and_true_pole":True,
              "new_strict_matrix_scalar_residual_certified":
                 c29["new_strict_matrix_scalar_residual_certified"],
              "new_weak_scalar_residual_Gershgorin_margin":
                 c29["new_weak_scalar_residual_Gershgorin_margin"],
              "full_original_Gstar_lower":c29["whole_Gstar_lower"],
              "full_original_Gstar_upper":c29["whole_Gstar_upper"],
              "full_original_Sstar_lower":c29["whole_Sstar_lower"],
              "full_original_Sstar_upper":c29["whole_Sstar_upper"],
            }
            for name in ("Gstar","Sstar"):
                ow=F(c28["new_"+name+"_bracket_width_trace"])
                nw=F(c29["new_"+name+"_bracket_width_trace"])
                oldmg24=F(c29["old_MG24_"+name+"_bracket_width_trace"])
                assert ow>0 and oldmg24>0 and nw>=0
                entry[name+"_same_mesh_28_width"]=str(ow)
                entry[name+"_29_width"]=str(nw)
                entry[name+"_29_over_28_width"]=str(nw/ow)
                entry[name+"_29_over_MG24_width"]=str(nw/oldmg24)
            merged.append(entry)
        reports.append({
            "mesh_cells":mesh,
            "contiguous_positive_band":[str(F(0)),str(PREFIX)],
            "same_actual_original_SI10_23pluspole_sources":True,
            "derivative_interval_full_real_cell_certified":True,
            "measured_source_cell_pairs":mesh*DIM,
            "strictly_improved_source_cell_pairs":
               part["number_strictly_improved_source_cell_pairs"],
            "total_source_radius_MG28":part["sum_28_radii"],
            "total_source_radius_MG29":part["sum_29_radii"],
            "source_radii_monotone_each_true_cell":True,
            "per_source_radius_improvement":part["per_source_radius_improvement"],
            "prefix_widths":comparisons,
            "full_original_frequency_scenarios":merged,
        })
    out={
      "status":"ORIGINAL_ADAPTED_THIRD_FOURIER_SOURCE_MOMENT_REFINEMENT",
      "canonical_W_ODD_NEG":"OPEN",
      "mg24_original_accepted_run":39378465438,
      "mg26_original_accepted_run":39380800739,
      "mg28_original_accepted_run":39438064440,
      "pole_third_analytically_differentiated_from_original_formula":True,
      "all_true_original_source_third_derivatives_combined_before_absolute":True,
      "true_original_fourth_drift_paid_on_every_cell":True,
      "actual_source_24D_moments_on_0to4_prefix":True,
      "MG28_16_cell_verbatim_trace_width_replay":True,
      "whole_original_frequency_pole_source_moments_enclosed":True,
      "not_entire_low_frequency_band_integrated":True,
      "original_470D_strong_residual_certified":False,
      "signed_odd_negative_51over56_cap_certified":False,
      "independent_original_Fourier_form_domain_audit":"OPEN",
      "even_Weil_CC27_RH":"OPEN",
      "meshes":reports
    }
    dest=ROOT/opt.output;dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(out,indent=2)+"\n")
    print("MG29 original adapted third curvature:",json.dumps({
       "meshes":[{
         "cells":a["mesh_cells"],
         "source_pairs_improved":a["strictly_improved_source_cell_pairs"],
         "prefix_width_new_over_28":{
             k:float(F(v["new_over_mg28_width"]))
             for k,v in a["prefix_widths"].items()},
         "whole_frequency":[{
             "k":v["cutoff_k"],
             "Gstar_over_28":float(F(v["Gstar_29_over_28_width"])),
             "Sstar_over_28":float(F(v["Sstar_29_over_28_width"])),
             "Gstar_over_mg24":float(F(v["Gstar_29_over_MG24_width"])),
             "Sstar_over_mg24":float(F(v["Sstar_29_over_MG24_width"])),
             "strict_contraction":v["new_strict_matrix_scalar_residual_certified"]
           }for v in a["full_original_frequency_scenarios"]]}
           for a in reports],"W_ODD_NEG_RH":"OPEN"}),flush=True)
if __name__=="__main__":main()
