#!/usr/bin/env python3
"""MG32: actual-original joint Fourier source residual, scoped and fail-closed.

R=F-Astar F B, Astar=Ao-2|s><s|.
Original odd Fourier row on every REAL frequency:
  r(xi)=t(xi)[I-a_o(xi)B+2e_p b^T B],
where t is original 23 MG11 adapted sources plus genuine sinh pole,
e_p singles out its channel, b=F*s from the physical source Gram.

On the ENTIRE contiguous xi-positive [0,4] partition, directly
bound r(xi) as a single affine vector. This retains the cancellation
between F, Ao F B and the rank-one pole BEFORE squaring. Use original
MG29 source value/derivative/third-fourth source Taylor enclosures,
same original SM43 signed multiplier range, all 24x24 cross terms.

Outside [0,4], rigorously bound physical missing H-H_C and
high-frequency weighted second moment with the original SM41 tail:
S_rem <= M_k^2(Hup-HClo)+tau_S I. Employ FULL accounted
Loewner Young bounds on C0 t - a_o B t, including b uncertainty.

The result is a genuine, though potentially loose, complete-original-
frequency upper for R*R. It is not source invariance, a 470D strong
inverse, signed negative 51/56, even/Weil/CC27/RH.
"""
import argparse,json,sys
from fractions import Fraction as F
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)

from validate_rpb108_mg29_adapted_third_curvature import (
    original_fourth_global,third_adapted_whole_cell,
    exact_original_second_midpoint,true_direct_adapted_curvature,
)
from validate_rpb108_mg26_contiguous_prefix_mass_closure import (
    ROOT,PREFIX,DIM,original_partition_preparation,
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
from validate_rpb108_mg25_original24_robust_trial import deserialize
from validate_rpb108_mg25_robust_source_aware_residual import (
    T,mm,sub,plus,mul,Id,shift,gersh_lower,norm_upper
)
from validate_rpb108_mg30_anchored_nonscalar_residual import (
    case_candidates,anchored_upper
)

N=24
P=23
CELLS=32
K=(12,16)
YOUNG=(F(1,16),F(1,4),F(1),F(4),F(16))
GAMMA=F(1,4)
CAP=10**12

def round_up(x):
    """Rational outward ceiling, never floating proof."""
    x=F(x)
    return F(-(-x.numerator*CAP//x.denominator),CAP)

def compact_symmetric_upper(M):
    """Export exact full matrix upper by outward entrywise error."""
    n=len(M)
    assert M==T(M)
    compact=[[F(int(x*CAP),CAP) for x in row] for row in M]
    err=max(sum((abs(M[i][j]-compact[i][j]) for j in range(n)),F(0))
            for i in range(n))
    return shift(compact,round_up(err))

def exact_original_cells():
    """MG29 32-cell original 23+pole affine source and prefix physical Gram."""
    centers,sources,a,c,hyp,Kglobal,Kthird=original_partition_preparation()
    assert len(sources)==25 and sources[24][0]=="pole"
    glob4=original_fourth_global(sources)
    source=[]
    mats={"prefix":{"mass":(zero(),zero())}}
    taus={str(t):0 for t in CHOSEN_TAUS}
    total_radius=F(0)
    for j in range(CELLS):
        left=PREFIX*F(j,CELLS)
        right=PREFIX*F(j+1,CELLS)
        width=right-left;half=width/2;mid=(left+right)/2
        wl,wu,_=positive_cell_weight_interval(left,right)
        vals=original_exact_physical_fourier_midpoint(mid,centers,sources,hyp)
        derivative,second=original_midpoint_derivative_intervals(
            mid,centers,sources,hyp)
        Kold=[min(g,abs_cap(local)+th*half) if local is not None
              else g for g,local,th in zip(Kglobal,second,Kthird)]
        v,d,eold=transformed_affine(vals,derivative,Kold,a,c,half)
        decomposition=splits_original_source(
            v,d,eold,Kold,half,vals,derivative,a,c,23,24)
        s2=exact_original_second_midpoint(mid,centers,sources,hyp)
        third=third_adapted_whole_cell(
            mid,centers,sources,hyp,a,c,Kthird,half,glob4)
        old28=true_direct_adapted_curvature(
            s2,Kthird,a,c,Kold,half)
        r=[]
        for i,(value,sloperad,curvature,rounding) in enumerate(decomposition):
            dc=(s2[i]-a[i]*s2[24]-c[i]*s2[23]) if i<23 else s2[24]
            improved=min(old28[i][0],abs_cap(dc)+third[i][0]*half)
            ri=up(value+sloperad+improved*half*half/2)
            assert 0<=ri<=eold[i]
            r.append(ri)
        total_radius+=sum(r,F(0))
        tau=max(CHOSEN_TAUS,key=lambda t:
            (lower_cell_trace((F(1),F(1)),width,v,d,eold,t),-t))
        taus[str(tau)]+=1
        add_directed_cell(mats,"prefix","mass",(F(1),F(1)),
                          width,v,d,r,tau)
        source.append((left,right,wl,wu,v,d,r))
    HClo,HCup,_,_=finalize(mats["prefix"]["mass"])
    assert len(source)==CELLS
    assert source[0][0]==0 and source[-1][1]==PREFIX
    assert all(source[i][1]==source[i+1][0]
               for i in range(CELLS-1))
    return source,HClo,HCup,total_radius,taus

def joint_prefix_upper(cells,bmid,brad,B):
    """True joint pole+multiplier residual, BEFORE taking outer product."""
    assert len(B)==N and all(len(row)==N for row in B)
    # Original t*(I+2 e_p b^T B - a0 B).  Original pole
    # coefficient b_i=<s,F_i> is enclosed independently by brad_i.
    qmat={"joint":{"mass":(zero(),zero())}}
    choices={str(t):0 for t in CHOSEN_TAUS}
    errsum=F(0)
    for left,right,wl,wu,v,d,r in cells:
        h=right-left;half=h/2
        a0=(wl+wu)/2
        da=(wu-wl)/2
        vpole=abs(v[P])+half*abs(d[P])+r[P]
        pcoeff=[sum((bmid[i]*B[i][j] for i in range(N)),F(0))
                for j in range(N)]
        perr=[sum((brad[i]*abs(B[i][j]) for i in range(N)),F(0))
              for j in range(N)]
        # C0 is the TRUE original rank-one pole-corrected source matrix
        # at the certified midpoint multiplier center a0.
        C=[[(F(i==j)-a0*B[i][j]+
              (2*pcoeff[j] if i==P else F(0))) for j in range(N)]
           for i in range(N)]
        qv=[sum((v[i]*C[i][j] for i in range(N)),F(0))
            for j in range(N)]
        qd=[sum((d[i]*C[i][j] for i in range(N)),F(0))
            for j in range(N)]
        qr=[]
        for j in range(N):
            base=sum((r[i]*abs(C[i][j]) for i in range(N)),F(0))
            mult=da*sum((abs(B[i][j])*(
                abs(v[i])+half*abs(d[i])+r[i]) for i in range(N)),F(0))
            pole=2*vpole*perr[j]
            rad=base+mult+pole
            assert rad>=0
            qr.append(rad)
        errsum+=sum(qr,F(0))
        # Independent fixed family: optimize this source-residual
        # upper TRACE, not the separate H/G/S lower trace.
        tau=min(CHOSEN_TAUS,key=lambda t:(
            (1+t)*(sum((x*x for x in qv),F(0))
                   +h*h*sum((x*x for x in qd),F(0))/12)
             +(1+1/t)*sum(qr,F(0))**2,t))
        choices[str(tau)]+=1
        add_directed_cell(qmat,"joint","mass",(F(1),F(1)),
                          h,qv,qd,qr,tau)
    lower,upper,_,_=finalize(qmat["joint"]["mass"])
    return upper,errsum,choices

def complement_upper(Hupper,HClo,bmid,brad,B,cutoff):
    """Rigorous all OMITTED real-frequency residual covariance budget.

    q=(t C0)-(a t B), C0=I+2 e_p b^T B. For any beta>0:
      q*q <=(1+beta)(t C0)*(t C0)
            +(1+1/beta)(a t B)*(a t B).
    The original b interval is charged with separate gamma Young.
    """
    old=Hupper
    Hrem=sub(old,HClo)
    assert Hrem==T(Hrem)
    assert all(Hrem[i][i]>=0 for i in range(N))
    M=F(17)+F(347*cutoff,500)
    # MG24/SM41 true original second-moment positive high-tail,
    # pinned to same original cutoff k and original H physical Gram.
    tau2=F(cutoff_tail[cutoff])
    Srem=shift(mul(M*M,Hrem),tau2)
    pcoeff=[sum((bmid[i]*B[i][j] for i in range(N)),F(0))
            for j in range(N)]
    C0=[[F(i==j)+(2*pcoeff[j] if i==P else F(0))
         for j in range(N)] for i in range(N)]
    U0=mm(mm(T(C0),Hrem),C0)
    V=mm(mm(T(B),Srem),B)
    # b true differs by an unknown componentwise signed vector.
    # ΔC=2 e_p delta_b^T B, so
    # ΔC^T Hrem ΔC <= 4*(Hrem)pp *||B^T brad||_2^2 I.
    ds=[sum((brad[i]*abs(B[i][j]) for i in range(N)),F(0))
        for j in range(N)]
    fee=4*Hrem[P][P]*sum((x*x for x in ds),F(0))
    assert fee>=0
    opt=[]
    for beta in YOUNG:
        # nested Young exact Γ for original rank-one pole uncertainty
        q1=shift(mul(1+GAMMA,U0),(1+1/GAMMA)*fee)
        rhs=plus(mul(1+beta,q1),mul(1+1/beta,V))
        opt.append((sum((rhs[i][i] for i in range(N)),F(0)),beta,rhs))
    _,chosen,result=min(opt,key=lambda q:(q[0],q[1]))
    return result,chosen,fee

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--verified-mg24-json",required=True)
    p.add_argument("--verified-mg29-json",required=True)
    p.add_argument("--verified-mg30-json",required=True)
    p.add_argument("--output",default=
       "artifacts/mg32_joint_original_source_residual.json")
    opts=p.parse_args()
    global cutoff_tail
    old24=json.loads((ROOT/opts.verified_mg24_json).read_text())
    old29=json.loads((ROOT/opts.verified_mg29_json).read_text())
    old30=json.loads((ROOT/opts.verified_mg30_json).read_text())
    assert old24["status"]=="ORIGINAL_COMPLETE_FREQUENCY_24CHANNEL_COUPLED_SOURCE_MATRIX_ENCLOSURES"
    assert old29["status"]=="ORIGINAL_ADAPTED_THIRD_FOURIER_SOURCE_MOMENT_REFINEMENT"
    assert old30["status"]=="ORIGINAL_24D_ANCHORED_NONSCALE_MIXED_RESIDUAL_GATE"
    assert old24["canonical_W_ODD_NEG"]==old29["canonical_W_ODD_NEG"]==old30["canonical_W_ODD_NEG"]=="OPEN"
    assert old30["verified_original_MG29_run_id"]==39440914565
    assert old30["verified_original_MG24_run_id"]==39378465438
    assert [x["mesh_cells"] for x in old29["meshes"]]==[16,32]
    assert [x["mesh_cells"] for x in old30["scenarios"]]==[16,16,32,32]
    Hmid,Hrad,Herr=original_H24_from_physical_source()
    Hlo=sub(Hmid,mul(Herr,Id(N)))
    Hup=plus(Hmid,mul(Herr,Id(N)))
    assert Herr==F(old24["physical_Gram_Loewner_row_error"])
    bmid=[Hmid[i][P] for i in range(N)]
    brad=[Hrad[i][P] for i in range(N)]
    assert [str(x) for x in bmid]==old24["original_pole_b_center"]
    assert [str(x) for x in brad]==old24["original_pole_b_radii"]
    cells,HClo,HCup,totalr,taus=exact_original_cells()
    old32=next(x for x in old29["meshes"] if x["mesh_cells"]==32)
    assert totalr==F(old32["total_source_radius_MG29"])
    cutoff_tail={
        c["cutoff_k"]:c["complete_original_strong_tail_rational"]
        for c in old24["cases"]}
    report=[]
    for cutoff in K:
        oldc=next(x for x in old24["cases"] if x["cutoff_k"]==cutoff)
        mg29case=next(x for x in old32["full_original_frequency_scenarios"]
                      if x["cutoff_k"]==cutoff)
        mg30case=next(x for x in old30["scenarios"]
                      if x["mesh_cells"]==32 and x["cutoff_k"]==cutoff)
        LG=deserialize(mg29case["full_original_Gstar_lower"])
        UG=deserialize(mg29case["full_original_Gstar_upper"])
        US=deserialize(mg29case["full_original_Sstar_upper"])
        Gc=mul(F(1,2),plus(LG,UG))
        candidates=case_candidates(Gc,US,F(oldc["scalar_trial_t"]))
        mapping={name:(t,B) for name,t,B in candidates}
        selected=list(dict.fromkeys(["MG24_scalar_t",
                                     mg30case["best_nonscalar_trial"]]))
        selected=[x for x in selected if x]
        outcomes=[]
        for name in selected:
            assert name in mapping
            t,B=mapping[name]
            direct,rad,choices=joint_prefix_upper(cells,bmid,brad,B)
            rem,beta,bfee=complement_upper(Hup,HClo,bmid,brad,B,cutoff)
            Rupper=plus(direct,rem)
            margin=gersh_lower(sub(Hlo,Rupper))
            check=anchored_upper(Hlo,Hup,LG,UG,US,t,B)
            historic=next(x for x in mg30case["trials"] if x["name"]==name)
            assert str(check["margin"])==historic["gershgorin_margin"]
            assert check["positive"] is False
            # Full two-component residual is certified; no assertion
            # that this deliberately crude complementary Young upper
            # is sharper than the MG30 independent G/S envelope.
            outcomes.append({
              "name":name,
              "source_response_rational_matrix":True,
              "original_24D_complete_frequency_pole_included":True,
              "direct_contiguous_prefix_source_residual_covariance":True,
              "prefix_direct_residual_upper_trace":str(trace(direct)),
              "original_missing_frequency_upper_trace":str(trace(rem)),
              "full_original_residual_upper_trace":str(trace(Rupper)),
              "MG30_independent_moment_Gershgorin_margin":str(check["margin"]),
              "joint_original_residual_Gershgorin_margin":str(margin),
              "strict_source_residual_contraction":margin>0,
              "certified_source_gap":str(max(F(0),min(F(1),
                          margin/norm_upper(Hup))) if margin>0 else F(0)),
              "pole_uncertainty_complement_charge":str(bfee),
              "source_joint_interval_radius_l1_sum":str(rad),
              "complement_Young_beta":str(beta),
              "cellwise_original_joint_tau_counts":choices,
              "whole_original_operator_470D_not_certified":True,
            })
        report.append({"cutoff_k":cutoff,
                       "MG29_true_source_cells":CELLS,
                       "original_true_prefix":["0",str(PREFIX)],
                       "original_complete_frequency_tail_bound":True,
                       "nonscalar_candidate_included":any(
                           x["name"]!="MG24_scalar_t" for x in outcomes),
                       "trials":outcomes})
    results=[x for r in report for x in r["trials"]]
    out={
      "status":"ORIGINAL_JOINT_24D_SOURCE_RESIDUAL_FOURIER_PREFIX_AND_TAIL_GATE",
      "canonical_W_ODD_NEG":"OPEN",
      "MG24_accepted_run":39378465438,
      "MG29_accepted_run":39440914565,
      "MG30_accepted_run":39442984941,
      "original_25_physical_SI10_generators_and_23pluspole_channels":True,
      "genuine_original_rank_one_sinh_pole_inside_residual_before_squaring":True,
      "direct_original_full_32_cell_Fourier_source_residual_measured":True,
      "true_original_prime7_arch_multiplier_interval_in_joint_integrand":True,
      "same_MG29_true_affine_source_curvature_replayed_exactly":True,
      "unmeasured_original_real_frequencies_closed_using_physical_mass":True,
      "whole_original_SM41_high_source_strong_tail_paid":True,
      "all_24D_source_crosses_included":True,
      "source_24D_strict_residual_certified":any(
           x["strict_source_residual_contraction"] for x in results),
      "number_original_rational_trials":len(results),
      "source_basis_is_not_operator_invariant":True,
      "full_original_470D_strong_inverse":False,
      "signed_original_51over56_negative_cap":False,
      "independent_original_Fourier_form_domain_audit":"OPEN",
      "even_Weil_CC27_RH":"OPEN",
      "scenarios":report,
      "decision":"First direct *original* Fourier residual covariance on [0,4] with all pole, a_o, source correlations retained; omitted frequencies are still conservatively upper bounded. If no strict source contraction, measure complement-dominance and improve direct joint lowband/selected panels instead of changing coordinates of a negative lower matrix."
    }
    dest=ROOT/opts.output;dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(out,indent=2)+"\n")
    print("MG32 original joint Fourier source residual:",json.dumps({
      "trials":[{"k":r["cutoff_k"],"data":[{
           "trial":t["name"],
           "direct_trace":float(F(t["prefix_direct_residual_upper_trace"])),
           "complement_trace":float(F(t["original_missing_frequency_upper_trace"])),
           "Gersh":float(F(t["joint_original_residual_Gershgorin_margin"])),
           "certified":t["strict_source_residual_contraction"]}
           for t in r["trials"]]} for r in report],
      "original_470D_odd_even_Weil_RH":"OPEN"}),flush=True)
if __name__=="__main__":main()
