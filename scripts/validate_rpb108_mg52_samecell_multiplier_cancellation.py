#!/usr/bin/env python3
"""MG52 — source-vector-coupled original [4,8] multiplier uncertainty.

The actual original source is q(xi)=t(xi)(C0-a(xi)B)
+2 t_p(xi) delta_b^T B, with C0=I+2e_p bmid^T B.
Freeze each accepted MG50 source cell and its ORIGINAL Young tau.
The old radius uses da*sum_i |B_ij| (|v_i|+h|d_i|+r_i).
Replace only this part by the VALID sharper radius
da*(|(vB)_j|+h|(dB)_j|+sum_i |B_ij|r_i), exploiting that the
multiplier error da is a COMMON SCALAR on the same source vector.
Consequently every local upper is smaller at the SAME Young tau;
after exact rational outward compaction verify Unew <= Uold in Loewner
order. This changes no high tail, physical source, or accepted B.
"""
import argparse,json,sys
from fractions import Fraction as Q
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import ROOT
from validate_rpb108_mg25_original24_robust_trial import (
    deserialize, original_H24_from_physical_source)
from validate_rpb108_mg25_robust_source_aware_residual import (
    Id,T,plus,sub,mul,gersh_lower,psd)
from validate_rpb108_mg41_ideal_cross_error_feasibility import classify_ideal
import validate_rpb108_mg32_joint_fourier_residual as orig
import validate_rpb108_mg50_actual_4to8_source_covariance as mg50
N=24;P=23
def rd(x):
    x=deserialize(x)
    assert len(x)==N and all(len(row)==N for row in x)
    return x
def enc(a):return [[str(x) for x in row] for row in a]
def trace(a):return sum((a[i][i] for i in range(N)),Q(0))
def qf(v,a):return sum((v[i]*a[i][j]*v[j] for i in range(N) for j in range(N)),Q(0))
def original_direct_radius_policy(cells,B,bmid,brad):
    old={"old":{"mass":(orig.zero(),orig.zero())}}
    improved={"new":{"mass":(orig.zero(),orig.zero())}}
    count={str(t):0 for t in orig.CHOSEN_TAUS}
    strict=0
    before=after=Q(0)
    bound_gains=[]
    for left,right,wl,wu,v,d,r in cells:
        h=right-left
        half=h/2
        ac=(wl+wu)/2;da=(wu-wl)/2
        pole=abs(v[P])+half*abs(d[P])+r[P]
        coeff=[sum((bmid[i]*B[i][j] for i in range(N)),Q(0)) for j in range(N)]
        berr=[sum((brad[i]*abs(B[i][j]) for i in range(N)),Q(0)) for j in range(N)]
        C=[[Q(i==j)-ac*B[i][j]+(2*coeff[j] if i==P else Q(0))
            for j in range(N)] for i in range(N)]
        center=[sum((v[i]*C[i][j] for i in range(N)),Q(0)) for j in range(N)]
        slope=[sum((d[i]*C[i][j] for i in range(N)),Q(0)) for j in range(N)]
        err_old=[];err_new=[]
        for j in range(N):
            structural=sum((r[i]*abs(C[i][j]) for i in range(N)),Q(0))
            radiusB=sum((r[i]*abs(B[i][j]) for i in range(N)),Q(0))
            oldmult=da*sum((abs(B[i][j])*(abs(v[i])+half*abs(d[i])+r[i])
                            for i in range(N)),Q(0))
            # IMPORTANT: (a(xi)-ac) multiplies ONE source vector.
            # The v and d source sums must be formed BEFORE absolutes.
            vb=sum((v[i]*B[i][j] for i in range(N)),Q(0))
            db=sum((d[i]*B[i][j] for i in range(N)),Q(0))
            newmult=da*(abs(vb)+half*abs(db)+radiusB)
            assert 0<=newmult<=oldmult
            oldrad=structural+oldmult+2*pole*berr[j]
            newrad=structural+newmult+2*pole*berr[j]
            assert 0<=newrad<=oldrad
            err_old.append(oldrad);err_new.append(newrad)
            strict+=int(newrad<oldrad)
        before+=sum(err_old,Q(0))
        after+=sum(err_new,Q(0))
        # Freeze the old original MG50 choice so the improvement
        # is PSD diagonal for each cell, without replacing the
        # accepted original exact Fourier data or reshuffling Young.
        tau=min(orig.CHOSEN_TAUS,key=lambda t:(
          (1+t)*(sum((x*x for x in center),Q(0))
             +h*h*sum((x*x for x in slope),Q(0))/12)
           +(1+1/t)*sum(err_old,Q(0))**2,t))
        count[str(tau)]+=1
        orig.add_directed_cell(old,"old","mass",(Q(1),Q(1)),
                               h,center,slope,err_old,tau)
        orig.add_directed_cell(improved,"new","mass",(Q(1),Q(1)),
                               h,center,slope,err_new,tau)
        # Exact difference in un-compacted upper on this cell is a
        # positive SEMIDEFINITE diagonal matrix.
        ro=sum(err_old,Q(0));rn=sum(err_new,Q(0))
        bound_gains.append({
            "left":str(left),"right":str(right),"frozen_original_tau":str(tau),
            "old_l1_radius":str(ro),"new_l1_radius":str(rn),
            "strictly_reduced_channels":sum(x<y for x,y in zip(err_new,err_old))})
    _,Uold,_,_=orig.finalize(old["old"]["mass"])
    _,Unew,_,_=orig.finalize(improved["new"]["mass"])
    delta=sub(Uold,Unew)
    assert delta==T(delta) and psd(delta)
    assert all(delta[i][j]==0 for i in range(N) for j in range(N) if i!=j)
    assert all(delta[i][i]>=0 for i in range(N))
    assert before>=after>0 and strict>0
    return Uold,Unew,delta,{
       "old_source_residual_radius_sum":str(before),
       "new_source_residual_radius_sum":str(after),
       "strict_reduced_cell_channel_pairs":strict,
       "frozen_original_tau_counts":count,
       "cell_records":bound_gains}
def main():
    p=argparse.ArgumentParser()
    for n in ("mg24","mg47","mg48","mg50"):
        p.add_argument("--verified-"+n+"-json",required=True)
    p.add_argument("--output",default="artifacts/mg52_original_samecell_multiplier_cancellation.json")
    args=p.parse_args()
    load=lambda n:json.loads((ROOT/getattr(args,"verified_"+n+"_json")).read_text())
    a24,a47,a48,a50=[load(n) for n in ("mg24","mg47","mg48","mg50")]
    assert a50["status"]=="ORIGINAL_MG50_TRUE_4TO8_FOURIER_JOINT_24D_SOURCE_GATE"
    assert all(z["canonical_W_ODD_NEG"]=="OPEN" for z in (a24,a47,a48,a50))
    Hmid,Hrad,Herr=original_H24_from_physical_source()
    assert Herr==Q(a24["physical_Gram_Loewner_row_error"])
    Hlo=sub(Hmid,mul(Herr,Id(N)))
    bmid=[Hmid[i][P] for i in range(N)]
    brad=[Hrad[i][P] for i in range(N)]
    cells,hL,hU,gL,gU,choices=mg50.actual_4to8_original_cells()
    assert len(cells)==32 and cells[0][0]==4 and cells[-1][1]==8
    assert enc(hL)==a50["new_band_original_mass_lower"]
    assert enc(hU)==a50["new_band_original_mass_upper"]
    assert enc(gL)==a50["new_band_original_G_lower"]
    assert enc(gU)==a50["new_band_original_G_upper"]
    cases=[]
    for s47,s48,s50 in zip(a47["scenarios"],a48["scenarios"],a50["cases"]):
        mesh,k=s50["mesh_cells"],s50["cutoff_k"]
        assert (mesh,k)==(s47["mesh_cells"],s47["cutoff_k"])==(s48["mesh_cells"],s48["cutoff_k"])
        B=rd(s47["full_original_rational_response_B"])
        Uold,Unew,gain,stats=original_direct_radius_policy(cells,B,bmid,brad)
        assert enc(Uold)==s50["actual_4to8_original_direct_24D_upper"]
        U50=rd(s50["best_new_whole_24D_upper"])
        U52=sub(U50,gain)
        assert U52==T(U52)
        assert psd(sub(U50,U52))
        # The original unchanged omitted band/tail & original [0,4]
        # are inherited exactly, not recomputed or discarded.
        U43=rd(s47["selected_complete_24D_source_upper"])
        mg43g=gersh_lower(sub(Hlo,U43))
        mg50g=gersh_lower(sub(Hlo,U50))
        mg52g=gersh_lower(sub(Hlo,U52))
        assert mg43g==Q(s50["MG43_accepted_whole_Gersh"])
        assert mg50g==Q(s50["best_new_whole_Gersh"])
        assert mg52g>=mg50g
        sel=U52 if mg52g>mg43g else U43
        method="MG52_samecell_original_4to8" if mg52g>mg43g else "MG43_whole"
        sl=sub(Hlo,sel)
        kind,witness=classify_ideal(sl)
        assert kind in ("NEGATIVE_EXACT_RATIONAL_RAYLEIGH",
                         "POSITIVE_EXACT_RATIONAL_LDL","INCONCLUSIVE")
        ray=[Q(z) for z in s47["selected_exact_inertia_witness"]["rational_vector"]]
        assert qf(ray,sub(Hlo,U43))<0
        cases.append({
          "mesh_cells":mesh,"cutoff_k":k,
          "original_response_B":enc(B),
          "original_new_4to8_upper_exact_replayed":enc(Uold),
          "MG52_samecell_new_4to8_upper":enc(Unew),
          "PSD_direct_upper_reduction":enc(gain),
          "MG50_best_original_whole_24D_upper":enc(U50),
          "MG52_best_original_whole_24D_upper":enc(U52),
          "MG50_Gersh":str(mg50g),
          "MG52_Gersh":str(mg52g),
          "MG43_Gersh":str(mg43g),
          "samecell_improves_complete_original_24D_upper_Loewner":True,
          "source_region_improvements":stats,
          "same_original_MG43_rational_witness":[str(x) for x in ray],
          "same_ray_source_24D_lower_MG50":str(qf(ray,sub(Hlo,U50))),
          "same_ray_source_24D_lower_MG52":str(qf(ray,sub(Hlo,U52))),
          "same_ray_positive_PSD_gain":str(qf(ray,gain)),
          "selected_complete_method":method,
          "selected_complete_24D_upper":enc(sel),
          "selected_complete_24D_lower":enc(sl),
          "selected_exact_24D_inertia":kind,
          "selected_exact_24D_witness":witness,
          "strict_original_source_contraction":kind=="POSITIVE_EXACT_RATIONAL_LDL",
          "no_actual_operator_negative_eigenmode_claim":True})
        print("MG52 ORIGINAL same-cell source",mesh,k,
              "oldGersh",float(mg50g),"newGersh",float(mg52g),
              "PSD_trace_gain",float(trace(gain)),
              "ray_gain",float(qf(ray,gain)),
              "selected",method,flush=True)
    out={
      "status":"ORIGINAL_MG52_COUPLED_4TO8_MULTIPLIER_VECTOR_CANCELLATION_24D",
      "canonical_W_ODD_NEG":"OPEN",
      "verified_parent_runs":{"MG50":39727680095,
          "MG48":39685179933,"MG47":39663431182,"MG24":39378465438},
      "original_true_SI10_MG11_24D_and_sinh_pole":True,
      "new_mathematical_coupling_same_cell_multiplier_source":True,
      "no_new_Fourier_samples":True,
      "exact_original_4to8_replayed":True,
      "old_and_new_direct_use_same_frozen_original_Young_tau":True,
      "valid_original_complete_frequency_upper_PSD_decrease":True,
      "new_24D_source_contraction":any(x["strict_original_source_contraction"] for x in cases),
      "full_original_470D_strong_inverse":False,
      "original_odd_signed_51over56":False,
      "independent_original_Fourier_form_domain_audit":"OPEN",
      "even_Weil_CC27_RH":"OPEN",
      "cases":cases}
    dest=ROOT/args.output;dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(out,indent=2)+"\n")
    print("MG52 original exact four-case full24 source improvement VERIFIED BY PRODUCER",
          {"case_count":len(cases),"source_positive":out["new_24D_source_contraction"],
           "470D_RH":"OPEN"},flush=True)
if __name__=="__main__":main()
