#!/usr/bin/env python3
"""MG36: actual-original complete 24D joint residual full matrix on [4,8].

Rigorous new per-cell covariance upper (row-Gershgorin interval remainder)
avoids applying Young to the entire affine nominal vector. For a true
original source residual Fourier row q_j(x)=v_j+d_j t+e_j(x),
 |e_j(x)| <= rho_j, |t|<=width/2, and a_j=|v_j|+half|d_j|,
the exact two-sign covariance satisfies

 Q_cell <= 2width(vv^T+width² dd^T/12)
    + diag[2width(a_i S+rho_i A+rho_i S)]_i
 where S=sum rho_j, A=sum a_j.

Proof: bound every unknown matrix entry by
 2width(a_i rho_j+rho_i a_j+rho_i rho_j)
and Gershgorin dominate the symmetric unknown error matrix by its
absolute row sums. This is a Loewner upper on the TRUE coupled covariance,
not merely an upper on its trace or on diagonal elements. The original
pole and seven-prime/digamma multiplier remain inside v,d,rho.

Compare the old accepted MG32 sourcewise-Young upper against this new
error-sensitive upper for each original [4,8] cell on the same exact
MG29 adapted source interval; select a VALID full matrix by its exact
rational TRACE, never assert trace gives Loewner dominance.

On the entire frequency axis, add accepted MG32 original [0,4] matrix
and a PSD-monotone *existing* missing-frequency full 24D Loewner upper
from the original [0,4] or [0,8] complement, on the SAME original
rational source B. Export full matrix and its exact source Gersh margin.
Fails closed on signed original 470D and Weil/RH.
"""
import argparse,json,sys
from fractions import Fraction as F
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)

import validate_rpb108_mg32_joint_fourier_residual as m32
import validate_rpb108_mg33_disjoint_joint_residual as m33
from validate_rpb108_mg26_contiguous_prefix_mass_closure import (
    ROOT,CHOSEN_TAUS,finalize,zero,trace
)
from validate_rpb108_mg25_original24_robust_trial import deserialize
from validate_rpb108_mg25_robust_source_aware_residual import (
    Id,T,plus,sub,mul,gersh_lower,norm_upper
)
from validate_rpb108_mg30_anchored_nonscalar_residual import case_candidates

N=24
POLE=23
CUTS=(12,16)
BAND_WINDOWS=tuple((F(4)+F(j,8),F(4)+F(j+1,8)) for j in range(32))

def direct_residual_affine(cell,bmid,brad,B):
    """Exact MG32 original residual affine coefficient/radius replay."""
    left,right,low,high,v,d,r=cell
    width=right-left
    half=width/2
    a0=(low+high)/2
    da=(high-low)/2
    assert 0<=left<right and low>0 and high>=low
    vpole=abs(v[POLE])+half*abs(d[POLE])+r[POLE]
    pcoeff=[sum((bmid[i]*B[i][j] for i in range(N)),F(0))
            for j in range(N)]
    perr=[sum((brad[i]*abs(B[i][j]) for i in range(N)),F(0))
            for j in range(N)]
    C=[[F(i==j)-a0*B[i][j]+
           (2*pcoeff[j] if i==POLE else F(0))
           for j in range(N)] for i in range(N)]
    qv=[sum((v[i]*C[i][j] for i in range(N)),F(0)) for j in range(N)]
    qd=[sum((d[i]*C[i][j] for i in range(N)),F(0)) for j in range(N)]
    qr=[]
    for j in range(N):
        base=sum((r[i]*abs(C[i][j]) for i in range(N)),F(0))
        multiplier=da*sum((abs(B[i][j])*(
            abs(v[i])+half*abs(d[i])+r[i])
            for i in range(N)),F(0))
        pole=2*vpole*perr[j]
        qr.append(base+multiplier+pole)
    assert len(qv)==len(qd)==len(qr)==N and all(x>=0 for x in qr)
    return width,qv,qd,qr

def cell_upper_methods(width,v,d,r):
    """Two independent, rigorously PSD-dominating original upper matrices.

    Both include the original +/- frequency factor 2. Raw exact Fraction,
    no rounded midpoint or floating eigensolver in a proof decision.
    """
    half=width/2
    h2=width*width/12
    a=[abs(v[i])+half*abs(d[i]) for i in range(N)]
    A=sum(a,F(0))
    S=sum(r,F(0))
    nominal=[[2*width*(v[i]*v[j]+h2*d[i]*d[j])
              for j in range(N)] for i in range(N)]
    # Exact symmetric entrywise remainder row-dominance:
    direct=[list(row) for row in nominal]
    for i in range(N):
        direct[i][i]+=2*width*(a[i]*S+r[i]*A+r[i]*S)
    assert direct==T(direct)
    scores=[]
    for tau in CHOSEN_TAUS:
        young=[[ (1+tau)*nominal[i][j] for j in range(N)]
               for i in range(N)]
        for i in range(N):
            young[i][i]+=2*width*(1+1/tau)*S*r[i]
        scores.append((trace(young),tau,young))
    _,tbest,old=min(scores,key=lambda x:(x[0],x[1]))
    chosen_name,selected=min(
        (("MG36_row_Gershgorin",direct),
         ("MG32_directional_Young",old)),
        key=lambda pair:(trace(pair[1]),pair[0]))
    # Bound matrices are nominal PSD plus diagonal PSD.
    assert all(x[i][i]>=0 for x in (direct,old) for i in range(N))
    assert trace(selected)==min(trace(direct),trace(old))
    return selected,old,direct,chosen_name,tbest

def original_band_upper(cells,bmid,brad,B):
    """Select per-cell, then export *complete* 24x24 original Loewner upper."""
    raw=zero()
    methods={"MG36_row_Gershgorin":0,"MG32_directional_Young":0}
    raw_trace_original=F(0)
    raw_trace_new=F(0)
    improvement=F(0)
    diagnostics=[]
    for cell in cells:
        width,qv,qd,qr=direct_residual_affine(cell,bmid,brad,B)
        improved,old,direct,method,tau=cell_upper_methods(width,qv,qd,qr)
        methods[method]+=1
        raw_trace_original+=trace(old)
        raw_trace_new+=trace(improved)
        improvement+=trace(old)-trace(improved)
        for i in range(N):
            for j in range(N):
                raw[i][j]+=improved[i][j]
        diagnostics.append({
           "left":str(cell[0]),"right":str(cell[1]),
           "selected_certified_Loewner_upper_by_trace":method,
           "old_directional_Young_raw_trace":str(trace(old)),
           "direct_row_Gersh_raw_trace":str(trace(direct)),
           "selected_raw_trace":str(trace(improved)),
           "radii_l1":str(sum(qr,F(0))),
           "radii_l2_squared":str(sum((x*x for x in qr),F(0))),
           "old_Young_tau":str(tau),
           "valid_full_matrix_not_trace_only":True})
    assert raw==T(raw)
    assert len(cells)==32 and sum(methods.values())==32
    assert improvement>=0
    _,upper,_,fee=finalize((zero(),raw))
    assert trace(upper)>=raw_trace_new
    return upper,{
       "methods":methods,"per_cell":diagnostics,
       "original_old_raw_trace":str(raw_trace_original),
       "new_raw_trace":str(raw_trace_new),
       "exact_raw_trace_improvement":str(improvement),
       "original_24x24_upper_export_fee":str(fee)}

def accepted_original_trials(old24,old29,old30,old32,cutoff):
    mesh=next(x for x in old29["meshes"] if x["mesh_cells"]==32)
    mom=next(x for x in mesh["full_original_frequency_scenarios"]
             if x["cutoff_k"]==cutoff)
    mg30=next(x for x in old30["scenarios"]
              if x["mesh_cells"]==32 and x["cutoff_k"]==cutoff)
    mg32=next(x for x in old32["scenarios"] if x["cutoff_k"]==cutoff)
    c24=next(x for x in old24["cases"] if x["cutoff_k"]==cutoff)
    Gc=mul(F(1,2),plus(deserialize(mom["full_original_Gstar_lower"]),
                      deserialize(mom["full_original_Gstar_upper"])))
    B={n:b for n,t,b in case_candidates(
        Gc,deserialize(mom["full_original_Sstar_upper"]),
        F(c24["scalar_trial_t"]))}
    assert len(B)==mg30["candidate_count"]==9
    names=[t["name"] for t in mg32["trials"]]
    assert len(names)==2 and "MG24_scalar_t" in names
    return [(name,B[name]) for name in names],mg32

def main():
    p=argparse.ArgumentParser()
    for k in ("mg24","mg29","mg30","mg32","mg33","mg35"):
        p.add_argument("--verified-"+k+"-json",required=True)
    p.add_argument("--output",default=
        "artifacts/mg36_original_joint_4to8_fullmatrix.json")
    args=p.parse_args()
    load=lambda k:json.loads((ROOT/getattr(args,"verified_"+k+"_json")).read_text())
    old24,old29,old30,old32,old33,old35=(
        load(k) for k in ("mg24","mg29","mg30","mg32","mg33","mg35"))
    assert old24["status"]=="ORIGINAL_COMPLETE_FREQUENCY_24CHANNEL_COUPLED_SOURCE_MATRIX_ENCLOSURES"
    assert old29["status"]=="ORIGINAL_ADAPTED_THIRD_FOURIER_SOURCE_MOMENT_REFINEMENT"
    assert old30["status"]=="ORIGINAL_24D_ANCHORED_NONSCALE_MIXED_RESIDUAL_GATE"
    assert old32["status"]=="ORIGINAL_JOINT_24D_SOURCE_RESIDUAL_FOURIER_PREFIX_AND_TAIL_GATE"
    assert old33["status"]=="ORIGINAL_DISJOINT_THREE_SECTOR_JOINT_SOURCE_RESIDUAL_GATE"
    assert old35["status"]=="ORIGINAL_MG35_PSD_MONOTONE_REMAINDER_UPPER_TRACE_GUARD"
    assert all(x["canonical_W_ODD_NEG"]=="OPEN"
               for x in (old24,old29,old30,old32,old33,old35))
    assert old35["verified_original_MG33_run"]==39462301107
    assert old35["verified_original_MG34_run"]==39467773045
    assert old33["MG19_selected_nonoverlapping_panels_after8"]==2
    assert len(BAND_WINDOWS)==32 and BAND_WINDOWS[0][0]==4
    assert BAND_WINDOWS[-1][1]==8
    assert all(BAND_WINDOWS[i][1]==BAND_WINDOWS[i+1][0]
               for i in range(31))
    assert old32["number_original_rational_trials"]==4

    Hmid,Hrad,Herr=m32.original_H24_from_physical_source()
    assert Herr==F(old24["physical_Gram_Loewner_row_error"])
    Hlo=sub(Hmid,mul(Herr,Id(N)))
    Hup=plus(Hmid,mul(Herr,Id(N)))
    bmid=[Hmid[i][POLE] for i in range(N)]
    brad=[Hrad[i][POLE] for i in range(N)]
    assert [str(x) for x in bmid]==old24["original_pole_b_center"]
    assert [str(x) for x in brad]==old24["original_pole_b_radii"]

    prefix,Hpfxlo,_,radius,prefix_tau=m32.exact_original_cells()
    assert radius==F(next(x for x in old29["meshes"]
        if x["mesh_cells"]==32)["total_source_radius_MG29"])
    band,Hbandlo,bandrad,band_tau=m33.extra_actual_original_cells(BAND_WINDOWS)
    assert len(prefix)==len(band)==32
    m32.cutoff_tail={c["cutoff_k"]:c["complete_original_strong_tail_rational"]
                     for c in old24["cases"]}
    report=[]
    for cutoff in CUTS:
        trials,prior32=accepted_original_trials(
            old24,old29,old30,old32,cutoff)
        old33case=next(x for x in old33["original_rational_trial_cutoffs"]
                       if x["cutoff_k"]==cutoff)
        mg35cases={(x["cutoff_k"],x["original_rational_trial"]):x
                   for x in old35["scenarios"]}
        for name,B in trials:
            old32t=next(x for x in prior32["trials"] if x["name"]==name)
            old33t=next(x for x in old33case["trials"]
                        if x["trial_name"]==name)
            old33vars=old33t["all_three_rigorous_complete_frequency_variants"]
            pfx,_,_=m32.joint_prefix_upper(prefix,bmid,brad,B)
            oldband,_,_=m32.joint_prefix_upper(band,bmid,brad,B)
            newband,detail=original_band_upper(band,bmid,brad,B)
            assert str(trace(pfx))==old32t["prefix_direct_residual_upper_trace"]
            assert str(trace(oldband))==old33vars[1][
                "frequency_contributions_upper_trace"]["new_band"]
            assert str(trace(pfx))==old33vars[0][
                "frequency_contributions_upper_trace"]["prefix"]
            # This compares upper TRACE, NOT PSD order oldband-newband.
            # The per-cell method selection is valid because both
            # competing full matrices are individually valid Loewner uppers.
            assert trace(newband)<=trace(oldband)
            r0,oldbeta,_=m32.complement_upper(
                Hup,Hpfxlo,bmid,brad,B,cutoff)
            r1,newbeta,_=m32.complement_upper(
                Hup,plus(Hpfxlo,Hbandlo),bmid,brad,B,cutoff)
            assert str(trace(r0))==old33vars[0][
                "remaining_original_frequency_upper_trace"]
            assert str(trace(r1))==old33vars[1][
                "remaining_original_frequency_upper_trace"]
            # PSD true-frequency inclusion permits older r0 to bound
            # the now smaller omitted set, independent of its own
            # sourcewise-Young mass lower being indefinite.
            chosen,rem=min((("MG32_0to4",r0),("MG33_0to8",r1)),
                           key=lambda item:(trace(item[1]),item[0]))
            assert chosen=="MG32_0to4"   # accepted MG35 numerical diagnosis
            U=plus(plus(pfx,newband),rem)
            assert U==T(U)
            signed=gersh_lower(sub(Hlo,U))
            gap=(max(F(0),min(F(1),signed/norm_upper(Hup)))
                 if signed>0 else F(0))
            guarded_old=trace(pfx)+trace(oldband)+trace(rem)
            full=trace(U)
            assert full<=guarded_old
            verified_guard=mg35cases[(cutoff,name)]
            assert str(guarded_old)==verified_guard[
                "full_original_frequency_upper_trace_scenarios"][1][
                "selected_valid_complete_frequency_upper_trace"]
            assert not old32t["strict_source_residual_contraction"]
            report.append({
                "cutoff_k":cutoff,"source_trial":name,
                "original_23adapted_plus_true_pole_channels":True,
                "complete_real_frequency_and_original_multiplier":True,
                "original_Fourier_source_Taylor_reconstructed_on_4to8":True,
                "old_MG33_joint_4to8_upper_trace":str(trace(oldband)),
                "new_MG36_joint_4to8_upper_trace":str(trace(newband)),
                "new_direct_band_over_MG33_trace":str(trace(newband)/trace(oldband)),
                "rigorous_original_direct_band_trace_gain":str(
                    trace(oldband)-trace(newband)),
                "PSD_safe_remainder_chosen_from":chosen,
                "PSD_safe_remainder_upper_trace":str(trace(rem)),
                "MG32_baseline_complete_upper_trace":old32t[
                    "full_original_residual_upper_trace"],
                "MG35_guarded_0to8_complete_upper_trace":str(guarded_old),
                "MG36_complete_original_Rupper_trace":str(full),
                "MG36_over_MG32_baseline_upper_trace":str(
                    full/F(old32t["full_original_residual_upper_trace"])),
                "full_original_24D_strict_Gershgorin_margin":str(signed),
                "full_original_24D_squared_source_gap":str(gap),
                "strict_original_source_contraction":signed>0,
                "new_direct_band_FULL24_upper":[
                    [str(x) for x in row] for row in newband],
                "full_original_Rupper_FULL24":[
                    [str(x) for x in row] for row in U],
                "full_original_Hlo_minus_Rupper_FULL24":[
                    [str(x) for x in row] for row in sub(Hlo,U)],
                "original_band_cells":detail,
                "full_original_470D_signed_cap_not_certified":True,
            })
    assert len(report)==4
    out={
        "status":"ORIGINAL_MG36_DIRECT_BAND_RESIDUAL_FULL24_MATRIX_GATE",
        "canonical_W_ODD_NEG":"OPEN",
        "verified_MG24_run_id":39378465438,
        "verified_MG29_run_id":39440914565,
        "verified_MG30_run_id":39442984941,
        "verified_MG32_run_id":39459624082,
        "verified_MG33_run_id":39462301107,
        "verified_MG35_run_id":39488378664,
        "original_true_25_SI10_physical_23adapted_plus_sinh_pole":True,
        "sourcewise_original_residual_4to8_combined_before_squaring":True,
        "actual_original_signed_arch_prime7_multiplier_every_cell":True,
        "matrix_entrywise_remainder_row_Gershgorin_proof":True,
        "new_complete_24D_original_residual_UPPER_matrices_exported":True,
        "exact_MG32_MG33_MG35_original_trace_replay":True,
        "PSD_monotone_full_matrix_original_remainder_reuse":True,
        "all_true_real_frequencies_accounted_for":True,
        "any_strict_24D_source_residual_contraction":
             any(x["strict_original_source_contraction"] for x in report),
        "true_original_470D_strong_inverse":False,
        "signed_original_51over56_odd_negative_cap":False,
        "independent_Fourier_form_domain_audit":"OPEN",
        "complete_even_Weil_CC27_RH":"OPEN",
        "scenarios":report,
        "next":"If no original full24 strict source contraction, inspect actual exact direct-band gains and sourcewise interval curvature, refine the joint error covariance while preserving the original true pole. Do not claim the full 470D signed cap."
    }
    dst=ROOT/args.output
    dst.parent.mkdir(parents=True,exist_ok=True)
    dst.write_text(json.dumps(out,indent=2)+"\n")
    print("MG36 original [4,8] full24 residual:",json.dumps({
      "tests":[{
         "k":t["cutoff_k"],"trial":t["source_trial"],
         "band_new_over_old":float(F(t["new_direct_band_over_MG33_trace"])),
         "complete_new_over_MG32":float(F(t["MG36_over_MG32_baseline_upper_trace"])),
         "full_Gershgorin":float(F(t["full_original_24D_strict_Gershgorin_margin"])),
         "strict":t["strict_original_source_contraction"],
         "chosen_methods":t["original_band_cells"]["methods"]}
         for t in report],"original_470D_even_Weil_RH":"OPEN"}),flush=True)
if __name__=="__main__":main()
