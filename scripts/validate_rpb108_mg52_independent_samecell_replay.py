#!/usr/bin/env python3
"""MG52 independent same-cell true-original multiplier cancellation audit.

Separate implementation of the source-vector contraction; uses MG50's
separately implemented *independent* new-Fourier-cell generator, NEVER
imports MG52 producer. Checks old direct MG50 matrix, each new direct
full24 source matrix, PSD diagonal upper decrease and full-frequency
original MG43 fallback and exact inertia witnesses.
"""
import argparse,json,sys
from fractions import Fraction as Q
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import ROOT
from validate_rpb108_mg25_original24_robust_trial import original_H24_from_physical_source
import validate_rpb108_mg50_independent_4to8_replay as old50
import validate_rpb108_mg32_joint_fourier_residual as original
N=24;P=23
def rd(x):return [[Q(z) for z in row] for row in x]
def transpose(a):return [list(x) for x in zip(*a)]
def add(a,b):return [[x+y for x,y in zip(u,v)] for u,v in zip(a,b)]
def scl(c,a):return [[c*x for x in row] for row in a]
def sub(a,b):return add(a,scl(-1,b))
def eye():return [[Q(i==j) for j in range(N)] for i in range(N)]
def quadratic(v,a):return sum((v[i]*a[i][j]*v[j] for i in range(N) for j in range(N)),Q(0))
def gersh(a):
    assert a==transpose(a)
    return min((a[i][i]-sum((abs(a[i][j]) for j in range(N) if j!=i),Q(0)) for i in range(N)))
def independent_new_band(cells,B,bc,br):
    """Compute BOTH residual uppers from FIRST PRINCIPLES with frozen tau."""
    a0={"old":{"mass":(original.zero(),original.zero())}}
    a1={"new":{"mass":(original.zero(),original.zero())}}
    reductions=0
    before=after=Q(0)
    counts={str(t):0 for t in original.CHOSEN_TAUS}
    details=[]
    for left,right,wl,wu,v,d,r in cells:
        h=right-left;half=h/2
        aa=(wl+wu)/2;unc=(wu-wl)/2
        Bc=[sum((bc[i]*B[i][j] for i in range(N)),Q(0))
            for j in range(N)]
        Be=[sum((br[i]*abs(B[i][j]) for i in range(N)),Q(0))
            for j in range(N)]
        T=[[Q(i==j)-aa*B[i][j]+(2*Bc[j] if i==P else Q(0))
             for j in range(N)] for i in range(N)]
        vv=[sum((T[i][j]*v[i] for i in range(N)),Q(0))
            for j in range(N)]
        dd=[sum((T[i][j]*d[i] for i in range(N)),Q(0))
            for j in range(N)]
        pole=abs(v[P])+half*abs(d[P])+r[P]
        prev=[];next_=[]
        for j in range(N):
            rr=sum((r[i]*abs(T[i][j]) for i in range(N)),Q(0))
            rB=sum((r[i]*abs(B[i][j]) for i in range(N)),Q(0))
            # Deliberately two distinct expressions:
            # old = independent per-physical-channel |v_i|/|d_i|
            # new = abs of original SAME-SCALAR dot product B^T v,d.
            oldterm=unc*(rB+sum((abs(B[i][j])*(
                       abs(v[i])+half*abs(d[i])) for i in range(N)),Q(0)))
            newterm=unc*(rB+abs(sum((B[i][j]*v[i] for i in range(N)),Q(0)))
                         +half*abs(sum((B[i][j]*d[i] for i in range(N)),Q(0))))
            assert 0<=newterm<=oldterm
            R=rr+2*pole*Be[j]
            prev.append(R+oldterm)
            next_.append(R+newterm)
            assert next_[-1]<=prev[-1]
            reductions+=int(next_[-1]<prev[-1])
        x=sum(prev,Q(0));y=sum(next_,Q(0))
        before+=x;after+=y
        tau=min(original.CHOSEN_TAUS,key=lambda z:(
            (1+z)*(sum((x*x for x in vv),Q(0))
              +h*h*sum((x*x for x in dd),Q(0))/12)
              +(1+1/z)*sum(prev,Q(0))**2,z))
        counts[str(tau)]+=1
        original.add_directed_cell(a0,"old","mass",(Q(1),Q(1)),
                                   h,vv,dd,prev,tau)
        original.add_directed_cell(a1,"new","mass",(Q(1),Q(1)),
                                   h,vv,dd,next_,tau)
        details.append({"left":str(left),"right":str(right),
                        "frozen_original_tau":str(tau),
                        "old_l1_radius":str(x),"new_l1_radius":str(y),
                        "strictly_reduced_channels":sum(a<b for a,b in zip(next_,prev))})
    _,U0,_,_=original.finalize(a0["old"]["mass"])
    _,U1,_,_=original.finalize(a1["new"]["mass"])
    assert all(U0[i][j]==U1[i][j] for i in range(N) for j in range(N) if i!=j)
    gain=sub(U0,U1)
    assert gain==transpose(gain)
    assert all(gain[i][i]>=0 for i in range(N))
    return U0,U1,gain,{
      "old_source_residual_radius_sum":str(before),
      "new_source_residual_radius_sum":str(after),
      "strict_reduced_cell_channel_pairs":reductions,
      "frozen_original_tau_counts":counts,
      "cell_records":details}
def synthetic_correlation_regression():
    v=[Q(1),Q(-1)]+[Q(0)]*(N-2)
    d=[Q(2),Q(-2)]+[Q(0)]*(N-2)
    B=eye()
    B[0][0]=B[1][0]=Q(1)
    assert sum((B[i][0]*v[i] for i in range(N)),Q(0))==0
    assert sum((B[i][0]*d[i] for i in range(N)),Q(0))==0
    assert sum((abs(B[i][0])*abs(v[i]) for i in range(N)),Q(0))==2
    assert sum((abs(B[i][0])*abs(d[i]) for i in range(N)),Q(0))==4
    return True
def verify_ldl_positive(a):
    a=[list(row) for row in a]
    for i in range(N):
        pivot=a[i][i]
        assert pivot>0
        for j in range(i+1,N):
          for k in range(i+1,N):
            a[j][k]-=a[j][i]*a[i][k]/pivot
    return True
def main():
    p=argparse.ArgumentParser()
    for name in ("mg24","mg47","mg48","mg50","mg52"):
        p.add_argument("--verified-"+name+"-json",required=True)
    a=p.parse_args()
    assert synthetic_correlation_regression()
    load=lambda name:json.loads((ROOT/getattr(a,"verified_"+name+"_json")).read_text())
    d={name:load(name) for name in ("mg24","mg47","mg48","mg50","mg52")}
    report=d["mg52"]
    assert report["status"]=="ORIGINAL_MG52_COUPLED_4TO8_MULTIPLIER_VECTOR_CANCELLATION_24D"
    assert all(x["canonical_W_ODD_NEG"]=="OPEN" for x in d.values())
    hm,hr,he=original_H24_from_physical_source()
    assert he==Q(d["mg24"]["physical_Gram_Loewner_row_error"])
    Hlo=sub(hm,scl(he,eye()))
    bc=[hm[i][P] for i in range(N)]
    br=[hr[i][P] for i in range(N)]
    cells,H0,H1,G0,G1,sourceCounts=old50.independent_4to8()
    assert rd(d["mg50"]["new_band_original_mass_lower"])==H0
    assert rd(d["mg50"]["new_band_original_mass_upper"])==H1
    assert rd(d["mg50"]["new_band_original_G_lower"])==G0
    assert rd(d["mg50"]["new_band_original_G_upper"])==G1
    assert len(cells)==32 and cells[0][0]==Q(4) and cells[-1][1]==Q(8)
    checked=0
    for s47,s48,s50,s52 in zip(d["mg47"]["scenarios"],
                              d["mg48"]["scenarios"],d["mg50"]["cases"],
                              report["cases"]):
        mesh,k=s52["mesh_cells"],s52["cutoff_k"]
        assert (mesh,k)==(s47["mesh_cells"],s47["cutoff_k"])==(s50["mesh_cells"],s50["cutoff_k"])
        B=rd(s47["full_original_rational_response_B"])
        assert rd(s52["original_response_B"])==B
        old,new,gain,stats=independent_new_band(cells,B,bc,br)
        assert old==rd(s50["actual_4to8_original_direct_24D_upper"])
        assert old==rd(s52["original_new_4to8_upper_exact_replayed"])
        assert new==rd(s52["MG52_samecell_new_4to8_upper"])
        assert gain==rd(s52["PSD_direct_upper_reduction"])
        assert stats==s52["source_region_improvements"]
        whole50=rd(s50["best_new_whole_24D_upper"])
        whole52=sub(whole50,gain)
        assert whole50==rd(s52["MG50_best_original_whole_24D_upper"])
        assert whole52==rd(s52["MG52_best_original_whole_24D_upper"])
        assert all((whole50[i][i]-whole52[i][i])>=0 for i in range(N))
        assert all((whole50[i][j]-whole52[i][j])==0
                   for i in range(N) for j in range(N) if i!=j)
        g50=gersh(sub(Hlo,whole50));g52=gersh(sub(Hlo,whole52))
        assert g52>=g50
        assert str(g50)==s52["MG50_Gersh"]
        assert str(g52)==s52["MG52_Gersh"]
        baseline=rd(s47["selected_complete_24D_source_upper"])
        g43=gersh(sub(Hlo,baseline))
        assert str(g43)==s52["MG43_Gersh"]
        ray=[Q(x) for x in s47["selected_exact_inertia_witness"]["rational_vector"]]
        assert [str(x) for x in ray]==s52["same_original_MG43_rational_witness"]
        assert str(quadratic(ray,sub(Hlo,whole50)))==s52["same_ray_source_24D_lower_MG50"]
        assert str(quadratic(ray,sub(Hlo,whole52)))==s52["same_ray_source_24D_lower_MG52"]
        assert str(quadratic(ray,gain))==s52["same_ray_positive_PSD_gain"]
        chosen=whole52 if g52>g43 else baseline
        assert s52["selected_complete_method"]==(
            "MG52_samecell_original_4to8" if g52>g43 else "MG43_whole")
        assert rd(s52["selected_complete_24D_upper"])==chosen
        lower=sub(Hlo,chosen)
        assert rd(s52["selected_complete_24D_lower"])==lower
        typ=s52["selected_exact_24D_inertia"]
        wit=s52["selected_exact_24D_witness"]
        if typ=="NEGATIVE_EXACT_RATIONAL_RAYLEIGH":
            v=[Q(z) for z in wit["rational_vector"]]
            assert quadratic(v,lower)==Q(wit["exact_negative_quadratic"])<0
        elif typ=="POSITIVE_EXACT_RATIONAL_LDL":
            assert verify_ldl_positive(lower)
        else:
            assert typ=="INCONCLUSIVE"
        assert s52["strict_original_source_contraction"]==(
            typ=="POSITIVE_EXACT_RATIONAL_LDL")
        assert s52["samecell_improves_complete_original_24D_upper_Loewner"]
        assert s52["no_actual_operator_negative_eigenmode_claim"]
        checked+=1
    assert checked==4
    assert report["valid_original_complete_frequency_upper_PSD_decrease"]
    assert report["new_24D_source_contraction"]==any(
        s["strict_original_source_contraction"] for s in report["cases"])
    assert not report["full_original_470D_strong_inverse"]
    assert not report["original_odd_signed_51over56"]
    assert report["independent_original_Fourier_form_domain_audit"]=="OPEN"
    assert report["even_Weil_CC27_RH"]=="OPEN"
    print("MG52 INDEPENDENT original same-cell full24 multiplier-vector cancellation PASS",
          {"source_cases":checked,"new24D_contraction":report["new_24D_source_contraction"],
           "470D_RH":"OPEN"},flush=True)
if __name__=="__main__":main()
