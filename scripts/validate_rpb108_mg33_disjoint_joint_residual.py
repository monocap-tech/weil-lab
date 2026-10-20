#!/usr/bin/env python3
"""MG33: certified disjoint true-original joint source residual on 3 frequency sectors.

Extends accepted MG32 32-cell [0,4] with a new contiguous [4,8]
32-cell positive band and ALL accepted MG19 selected nonflat panels
whose left endpoints are >=8. The three sectors are disjoint in
Lebesgue frequency measure (negative mirror included in existing
MG15/MG32 factor 2). All source values, third/fourth Taylor radii,
SM43 signed prime-seven/digamma multiplier interval and actual sinh
pole are recomputed for every NEW real cell. The MG19 certificate is
used for verified site geometry, NOT for an invalid reuse of its
G/S matrices as though they were the residual covariance.

For each exact original MG30 rational B on the MG32 shortlist:
 R*R = integral[measured] r*r + integral[unmeasured] r*r,
 r(xi)=t(xi)(I-a_o(xi)B+2e_p b^t B).

The measured residuals are enclosed jointly before squaring.
For remaining real frequencies Hrem <= Hup - sum(measured Hlo)
and SM41 second source tail give the same rigorous MG32 complement.
Compare three valid complete-frequency enclosures:
  baseline [0,4]; full contiguous [0,8]; nonoverlap hybrid [0,8]
  plus the original selected MG19 frequency cells outside it.

Failure of a bound's strict Gershgorin positivity is a failed
sufficient certificate, not a negative mode of the original operator,
nor even a negative quadratic of the actual residual.
No full 470D inverse, signed 51/56, odd/even/Weil/CC27/RH.
"""
import argparse,json,sys
from fractions import Fraction as F
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
import validate_rpb108_mg32_joint_fourier_residual as m32
from validate_rpb108_mg29_adapted_third_curvature import (
    original_fourth_global,third_adapted_whole_cell,
    exact_original_second_midpoint,true_direct_adapted_curvature,
)
from validate_rpb108_mg26_contiguous_prefix_mass_closure import (
    ROOT,DIM,original_partition_preparation,
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
from validate_rpb108_mg14_affine_original_two_moments import up
from validate_rpb108_mg25_original24_robust_trial import deserialize
from validate_rpb108_mg25_robust_source_aware_residual import (
    Id,sub,plus,mul,gersh_lower,norm_upper
)
from validate_rpb108_mg30_anchored_nonscalar_residual import case_candidates

N=24
POLE=23
CUTS=(12,16)
BAND_MESH=32
BAND_LOW=F(4)
BAND_HIGH=F(8)

def verified_nonoverlap(original_mg19):
    """Only geometry inherited from the previously accepted 24 MG19 sites."""
    assert original_mg19["status"]==(
        "SCOPED_NONFLAT_ORIGINAL_INTERSECTED_RELATIVE_WEIGHT_FULL_SOURCE_MOMENTS")
    assert original_mg19["canonical_W_ODD_NEG"]=="OPEN"
    assert original_mg19["selected_new_nonflat_cells"]==24
    assert original_mg19["true_source_count"]==25
    assert original_mg19["all_24_coupled_source_channels_retained"]
    assert original_mg19["MG19_all_independent_relative_weight_factors_intersected"]
    assert original_mg19["original_true_nonflat_multiplier_certified_each_cell"]
    sites=original_mg19["per_cell_diagnostics"]
    assert len(sites)==24
    pairs=[(F(d["left"]),F(d["right"])) for d in sites]
    assert all(a<b for a,b in pairs)
    assert all(pairs[i][1]<pairs[i+1][0] for i in range(23))
    selected=[(a,b) for a,b in pairs if a>=BAND_HIGH]
    assert all(a>=BAND_HIGH and a<b for a,b in selected)
    assert all(b<=F(2)**CUTS[0] for a,b in selected)
    assert all(selected[i][1]<selected[i+1][0]
               for i in range(len(selected)-1))
    # Accepted nonflat geometry is not necessarily above 8.
    # If none survive, do not assert fictitious source coverage.
    return pairs,selected

def extra_actual_original_cells(windows):
    """Same MG29 24D actual adapted-source Taylor enclosures as MG32.

    Each cell is evaluated at its own rational midpoint, NOT
    extrapolated from [0,4]; this is important above frequency 8.
    Return true all-source Gram lower for the disjoint union.
    """
    if not windows:return [],[[F(0)]*N for _ in range(N)],F(0),{}
    centers,sources,a,c,hyp,Kglobal,Kthird=original_partition_preparation()
    assert len(sources)==25 and sources[24][0]=="pole"
    L4=original_fourth_global(sources)
    mats={"extra":{"mass":(zero(),zero())}}
    tau_counts={str(t):0 for t in CHOSEN_TAUS}
    out=[]
    total_r=F(0)
    for left,right in windows:
        assert left>=BAND_LOW and right>left
        width=right-left;half=width/2;mid=(left+right)/2
        wl,wu,_=positive_cell_weight_interval(left,right)
        assert F(0)<wl<=wu
        vals=original_exact_physical_fourier_midpoint(
            mid,centers,sources,hyp)
        d1,d2=original_midpoint_derivative_intervals(
            mid,centers,sources,hyp)
        Kold=[min(g,abs_cap(q)+L3*half) if q is not None else g
              for g,q,L3 in zip(Kglobal,d2,Kthird)]
        v,d,eold=transformed_affine(vals,d1,Kold,a,c,half)
        dec=splits_original_source(
            v,d,eold,Kold,half,vals,d1,a,c,23,24)
        actual2=exact_original_second_midpoint(mid,centers,sources,hyp)
        third=third_adapted_whole_cell(
            mid,centers,sources,hyp,a,c,Kthird,half,L4)
        K28=true_direct_adapted_curvature(
            actual2,Kthird,a,c,Kold,half)
        e=[]
        for i,(value,slope,oldcurv,rounding) in enumerate(dec):
            combined=(actual2[i]-a[i]*actual2[24]
                      -c[i]*actual2[23]) if i<23 else actual2[24]
            direct=min(K28[i][0],abs_cap(combined)+third[i][0]*half)
            rad=up(value+slope+direct*half*half/2)
            assert 0<=rad<=eold[i]
            e.append(rad)
        total_r+=sum(e,F(0))
        tau=max(CHOSEN_TAUS,key=lambda t:(
            lower_cell_trace((F(1),F(1)),width,v,d,eold,t),-t))
        tau_counts[str(tau)]+=1
        add_directed_cell(mats,"extra","mass",(F(1),F(1)),
                          width,v,d,e,tau)
        out.append((left,right,wl,wu,v,d,e))
    assert len(out)==len(windows)
    assert all(out[i][1]<=out[i+1][0] for i in range(len(out)-1))
    L,U,_,_=finalize(mats["extra"]["mass"])
    return out,L,total_r,tau_counts

def trial_case(cutoff,old24,old29,old30,old32,
               prefix_cells,prefix_Hlo,
               band_cells,band_Hlo,site_cells,site_Hlo,
               Hlo,Hup,bmid,brad):
    mg29=next(x for x in old29["meshes"] if x["mesh_cells"]==32)
    case=next(x for x in mg29["full_original_frequency_scenarios"]
              if x["cutoff_k"]==cutoff)
    prev=next(x for x in old30["scenarios"]
              if x["mesh_cells"]==32 and x["cutoff_k"]==cutoff)
    before=next(x for x in old32["scenarios"]
                if x["cutoff_k"]==cutoff)
    cap=next(x for x in old24["cases"] if x["cutoff_k"]==cutoff)
    LG=deserialize(case["full_original_Gstar_lower"])
    UG=deserialize(case["full_original_Gstar_upper"])
    US=deserialize(case["full_original_Sstar_upper"])
    Gc=mul(F(1,2),plus(LG,UG))
    selection=case_candidates(Gc,US,F(cap["scalar_trial_t"]))
    mapping={name:(t,B) for name,t,B in selection}
    assert len(mapping)==prev["candidate_count"]==9
    names=[x["name"] for x in before["trials"]]
    assert len(names)==len(set(names))==2
    assert "MG24_scalar_t" in names
    out=[]
    fullband_Hlo=plus(prefix_Hlo,band_Hlo)
    hybrid_Hlo=plus(fullband_Hlo,site_Hlo)
    for name in names:
        assert name in mapping
        t,B=mapping[name]
        pfx,prad,ptau=m32.joint_prefix_upper(prefix_cells,bmid,brad,B)
        band,brad_total,btau=m32.joint_prefix_upper(
            band_cells,bmid,brad,B)
        sites,srad_total,stau=m32.joint_prefix_upper(
            site_cells,bmid,brad,B) if site_cells else (
                [[F(0)]*N for _ in range(N)],F(0),{})
        # All three complete-original-frequency variants close their
        # OWN genuine disjoint missing-source Fourier mass; the
        # original whole-high multiplier excess stays fully paid.
        before_rem,old_beta,old_pole=m32.complement_upper(
            Hup,prefix_Hlo,bmid,brad,B,cutoff)
        band_rem,band_beta,band_pole=m32.complement_upper(
            Hup,fullband_Hlo,bmid,brad,B,cutoff)
        hybrid_rem,hy_beta,hy_pole=m32.complement_upper(
            Hup,hybrid_Hlo,bmid,brad,B,cutoff)
        baseline=plus(pfx,before_rem)
        newband=plus(plus(pfx,band),band_rem)
        fullhybrid=plus(plus(plus(pfx,band),sites),hybrid_rem)
        earlier=next(x for x in before["trials"] if x["name"]==name)
        # Exact independent REPLAY of MG32 original accepted result.
        assert str(trace(pfx))==earlier[
            "prefix_direct_residual_upper_trace"]
        assert str(trace(before_rem))==earlier[
            "original_missing_frequency_upper_trace"]
        assert str(gersh_lower(sub(Hlo,baseline)))==earlier[
            "joint_original_residual_Gershgorin_margin"]
        assert str(trace(baseline))==earlier[
            "full_original_residual_upper_trace"]
        results=[]
        for label,upper,remainder,segments,beta,po in (
            ("MG32_prefix_only",baseline,before_rem,
             [(pfx,"prefix")],old_beta,old_pole),
            ("MG33_contiguous_0to8",newband,band_rem,
             [(pfx,"prefix"),(band,"new_band")],band_beta,band_pole),
            ("MG33_hybrid_with_MG19",fullhybrid,hybrid_rem,
             [(pfx,"prefix"),(band,"new_band"),(sites,"MG19_panels")],
             hy_beta,hy_pole)):
            signed=gersh_lower(sub(Hlo,upper))
            tr=trace(upper)
            assert tr==sum((trace(x) for x,y in segments),F(0))+trace(remainder)
            assert tr>=0
            results.append({
                "variant":label,
                "true_original_pole_inside_residual":True,
                "complete_original_real_frequency_upper":True,
                "physical_disjoint_frequency_partition":True,
                "upper_trace":str(tr),
                "remaining_original_frequency_upper_trace":str(
                    trace(remainder)),
                "remaining_fraction_of_total_upper_trace":str(
                    trace(remainder)/tr) if tr>0 else None,
                "strict_Gershgorin_margin":str(signed),
                "strict_24D_source_contraction":signed>0,
                "complete_original_470D_inverse_certified":False,
                "frequency_contributions_upper_trace":{
                    label:str(trace(x)) for x,label in segments},
                "complement_Young_beta":str(beta),
                "original_pole_uncertainty_complement_fee":str(po)})
        base,new,hyr=results
        out.append({
            "trial_name":name,
            "source_matrix_rationalized":True,
            "strict_original_24D_source_contraction":any(
                r["strict_24D_source_contraction"] for r in results),
            "all_three_rigorous_complete_frequency_variants":results,
            "hybrid_upper_trace_over_baseline":str(
                F(hyr["upper_trace"])/F(base["upper_trace"])),
            "hybrid_Gershgorin_improvement_vs_MG32":str(
                F(hyr["strict_Gershgorin_margin"])-
                F(base["strict_Gershgorin_margin"])),
            "contiguous_0to8_Gershgorin_improvement_vs_MG32":str(
                F(new["strict_Gershgorin_margin"])-
                F(base["strict_Gershgorin_margin"]))})
    return {"cutoff_k":cutoff,
            "same_accepted_MG32_actual_original_trial_B":True,
            "actual_original_24D_23pluspole_basis":True,
            "all_full_frequency_SM41_original_strong_tails_paid":True,
            "trials":out}

def main():
    p=argparse.ArgumentParser()
    for k in ("mg19","mg24","mg29","mg30","mg32"):
        p.add_argument("--verified-"+k+"-json",required=True)
    p.add_argument("--output",default=
        "artifacts/mg33_original_disjoint_joint_residual.json")
    a=p.parse_args()
    load=lambda k:json.loads((ROOT/getattr(a,"verified_"+k+"_json")).read_text())
    old19,old24,old29,old30,old32=(
        load(k) for k in ("mg19","mg24","mg29","mg30","mg32"))
    assert old24["status"]=="ORIGINAL_COMPLETE_FREQUENCY_24CHANNEL_COUPLED_SOURCE_MATRIX_ENCLOSURES"
    assert old29["status"]=="ORIGINAL_ADAPTED_THIRD_FOURIER_SOURCE_MOMENT_REFINEMENT"
    assert old30["status"]=="ORIGINAL_24D_ANCHORED_NONSCALE_MIXED_RESIDUAL_GATE"
    assert old32["status"]=="ORIGINAL_JOINT_24D_SOURCE_RESIDUAL_FOURIER_PREFIX_AND_TAIL_GATE"
    assert all(d["canonical_W_ODD_NEG"]=="OPEN"
               for d in (old19,old24,old29,old30,old32))
    assert old32["MG24_accepted_run"]==39378465438
    assert old32["MG29_accepted_run"]==39440914565
    assert old32["MG30_accepted_run"]==39442984941
    assert old32["number_original_rational_trials"]==4
    assert old32["direct_original_full_32_cell_Fourier_source_residual_measured"]
    all_mg19,selected=verified_nonoverlap(old19)
    bandwindows=[
        (BAND_LOW+F(j,BAND_MESH)*(BAND_HIGH-BAND_LOW),
         BAND_LOW+F(j+1,BAND_MESH)*(BAND_HIGH-BAND_LOW))
        for j in range(BAND_MESH)]
    assert bandwindows[0][0]==BAND_LOW
    assert bandwindows[-1][1]==BAND_HIGH
    assert all(bandwindows[i][1]==bandwindows[i+1][0]
               for i in range(BAND_MESH-1))
    assert all(x[0]>=BAND_HIGH for x in selected)
    combined=bandwindows+selected
    assert all(combined[i][1]<=combined[i+1][0]
               for i in range(len(combined)-1))
    Hmid,Hrad,Herr=original_H24_from_physical_source()
    assert Herr==F(old24["physical_Gram_Loewner_row_error"])
    Hlo=sub(Hmid,mul(Herr,Id(N)))
    Hup=plus(Hmid,mul(Herr,Id(N)))
    bmid=[Hmid[i][POLE] for i in range(N)]
    brad=[Hrad[i][POLE] for i in range(N)]
    assert [str(q) for q in bmid]==old24["original_pole_b_center"]
    assert [str(q) for q in brad]==old24["original_pole_b_radii"]
    prefix,Hpfxlo,Hpfxup,pfxsum,taux=m32.exact_original_cells()
    old29mesh=next(x for x in old29["meshes"] if x["mesh_cells"]==32)
    assert pfxsum==F(old29mesh["total_source_radius_MG29"])
    band,Hband,bandr,taub=extra_actual_original_cells(bandwindows)
    sites,Hsites,siter,taus=extra_actual_original_cells(selected)
    assert len(band)==BAND_MESH and len(sites)==len(selected)
    m32.cutoff_tail={
        c["cutoff_k"]:c["complete_original_strong_tail_rational"]
        for c in old24["cases"]}
    cases=[trial_case(k,old24,old29,old30,old32,
                      prefix,Hpfxlo,band,Hband,sites,Hsites,
                      Hlo,Hup,bmid,brad) for k in CUTS]
    items=[t for c in cases for t in c["trials"]]
    certified=sum(v["strict_24D_source_contraction"]
                  for t in items
                  for v in t["all_three_rigorous_complete_frequency_variants"])
    out={
      "status":"ORIGINAL_DISJOINT_THREE_SECTOR_JOINT_SOURCE_RESIDUAL_GATE",
      "canonical_W_ODD_NEG":"OPEN",
      "verified_MG19_run_id":39363425186,
      "verified_MG24_run_id":39378465438,
      "verified_MG29_run_id":39440914565,
      "verified_MG30_run_id":39442984941,
      "verified_MG32_run_id":39459624082,
      "true_original_source_SI10_25physical_23pluspole_dimension24":True,
      "all_real_frequency_sectors_disjoint_original_source":True,
      "negative_frequency_mirror_included_by_exact_cell_factor_two":True,
      "entire_MG32_original_32_cell_baseline_replayed_exactly":True,
      "new_original_band_4to8_contiguous_32cells":True,
      "MG19_original_nonflat_verified_24site_catalog_used":True,
      "MG19_selected_nonoverlapping_panels_after8":len(sites),
      "MG19_selected_panels_below8_not_double_counted":24-len(sites),
      "selected_original_MG19_additional_positive_frequency_width":str(
          sum((right-left for left,right in selected),F(0))),
      "actual_original_source_fourier_Taylor_third_fourth_on_every_new_cell":True,
      "actual_prime7_arch_signed_original_multiplier_on_every_new_cell":True,
      "full_original_24D_pole_corrected_joint_residual_on_measured_cells":True,
      "remaining_all_original_frequencies_closed_by_physical_source_mass":True,
      "complete_original_SM41_strong_source_high_tails_paid":True,
      "original_24D_source_strict_contraction_count":certified,
      "full_original_470D_strong_inverse_certified":False,
      "signed_original_negative_51over56_cap_certified":False,
      "independent_original_Fourier_form_domain_audit":"OPEN",
      "even_Weil_CC27_RH":"OPEN",
      "measured_frequency_sectors":[
          {"type":"contiguous","left":"0","right":"4","cells":32},
          {"type":"contiguous","left":"4","right":"8","cells":BAND_MESH},
          {"type":"MG19_certified_selected_nonflat",
           "sites":[[str(x),str(y)] for x,y in selected],
           "cells":len(selected)}],
      "source_radius_L1_sums":{
           "MG29_replayed_prefix":str(pfxsum),
           "new_4to8_band":str(bandr),
           "accepted_MG19_sites_after8_recomputed":str(siter)},
      "original_rational_trial_cutoffs":cases,
      "decision":"Compare exactly replayed MG32 prefix, extended contiguous [0,8], and nonoverlapping MG19-selected hybrid on the SAME original rational B. A smaller upper trace alone is not PSD Loewner dominance or positivity; only strict Hlo-Rupper full 24D matrix acceptance can promote source contraction. All 470D/Weil/RH OPEN."
    }
    target=ROOT/a.output;target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps(out,indent=2)+"\n")
    print("MG33 original disjoint joint-source:",json.dumps({
       "new_band_cells":len(band),
       "MG19_sites_after8":len(sites),
       "original_full_frequency":[{
           "k":c["cutoff_k"],
           "cases":[{
             "trial":t["trial_name"],
             "results":[{
                "variant":v["variant"],
                "total_upper_trace":float(F(v["upper_trace"])),
                "complement_upper_trace":float(F(v["remaining_original_frequency_upper_trace"])),
                "Gersh":float(F(v["strict_Gershgorin_margin"])),
                "strict":v["strict_24D_source_contraction"]}
                for v in t["all_three_rigorous_complete_frequency_variants"]]}
           for t in c["trials"]]}
         for c in cases],
       "signed470_even_Weil_RH":"OPEN"}),flush=True)
if __name__=="__main__":main()
