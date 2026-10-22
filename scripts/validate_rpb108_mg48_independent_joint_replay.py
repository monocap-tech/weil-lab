#!/usr/bin/env python3
"""MG48 independent exact-rational replay of all original complete-source candidates.

Reconstructs the JOINT covariance by the ungrouped polynomial expression,
independently of the centered mixed-moment routine in the MG48 producer.
No producer-module imports; comparison is entrywise rational for final matrices.
"""
import argparse,json,sys
from fractions import Fraction as Q
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import ROOT
from validate_rpb108_mg25_original24_robust_trial import original_H24_from_physical_source
from validate_rpb108_mg23_physical_metric_matrix_envelope import KAPPA
N=24; P=23

def rd(a):return [[Q(v) for v in row] for row in a]
def trans(a):return [list(x) for x in zip(*a)]
def matmul(a,b):
    bt=trans(b)
    return [[sum((x*y for x,y in zip(row,col)),Q(0)) for col in bt] for row in a]
def add(a,b):return [[x+y for x,y in zip(u,v)] for u,v in zip(a,b)]
def scale(c,a):return [[c*x for x in row] for row in a]
def minus(a,b):return add(a,scale(-1,b))
def eye():return [[Q(i==j) for j in range(N)] for i in range(N)]
def conjugate(a,x):return matmul(matmul(trans(x),a),x)
def tr(a):return sum((a[i][i] for i in range(N)),Q(0))
def gersh(a):return min(a[i][i]-sum((abs(a[i][j]) for j in range(N) if j!=i),Q(0)) for i in range(N))
def quadratic(a,v):return sum((v[i]*a[i][j]*v[j] for i in range(N) for j in range(N)),Q(0))
def diag(v):
    a=[[Q(0)]*N for _ in range(N)]
    for i,x in enumerate(v):a[i][i]=x
    return a
def ldlpositive(a):
    # independent exact-rational unpivoted 24D positive-definite test
    d=[]; l=[[Q(i==j) for j in range(N)] for i in range(N)]
    for k in range(N):
        dk=a[k][k]-sum((l[k][j]*l[k][j]*d[j] for j in range(k)),Q(0))
        if dk<=0:return False
        d.append(dk)
        for i in range(k+1,N):
            l[i][k]=(a[i][k]-sum((l[i][j]*l[k][j]*d[j] for j in range(k)),Q(0)))/dk
    return True

def replay(row47,row46,row24,center,radius,original_lower):
    assert row47["selected_strongest_valid_whole_method"]=="MG43_whole"
    b=rd(row47["full_original_rational_response_B"])
    direct=rd(row46["original_MG32_direct_band_24D_upper"])
    hU=rd(row46["original_complete_omitted_H_upper"])
    hL=scale(1/KAPPA,rd(row47["original_G_lower_candidate_matrices"]["mass_kappa"]))
    k=row47["cutoff_k"]
    m=Q(17)+Q(347*k,500)
    s=Q(row24["complete_original_strong_tail_rational"])
    assert Q(row24["original_global_lowband_majorant_M"])==m and s>=0
    cb=[sum((center[i]*b[i][j] for i in range(N)),Q(0)) for j in range(N)]
    c0=[[Q(i==j)+(2*cb[j] if i==P else Q(0)) for j in range(N)] for i in range(N)]
    p=minus(c0,scale((KAPPA+m)/2,b))
    dp=[sum((radius[i]*abs(b[i][j]) for i in range(N)),Q(0)) for j in range(N)]
    wd0=scale(4*hU[P][P]*sum((v*v for v in dp),Q(0)),eye())
    wd1=diag([4*hU[P][P]*sum(dp,Q(0))*v for v in dp])
    results=[]
    for ln,lo in row47["original_G_lower_candidate_matrices"].items():
      for un,up in row47["original_G_upper_candidate_matrices"].items():
        low=rd(lo); high=rd(up)
        gc=scale(Q(1,2),add(low,high))
        er=scale(Q(1,2),minus(high,low))
        # Ungrouped original polynomial moment correlation:
        # C^T H C - C^T G B - B^T G C + (kappa+M) B^T G B
        # - kappa*M B^T H B + tau_2 B^T B.
        core=conjugate(hU,c0)
        core=minus(core,matmul(matmul(trans(c0),gc),b))
        core=minus(core,matmul(matmul(trans(b),gc),c0))
        core=add(core,scale(KAPPA+m,conjugate(gc,b)))
        core=minus(core,scale(KAPPA*m,conjugate(hL,b)))
        core=add(core,scale(s,matmul(trans(b),b)))
        # A single centered Loewner uncertainty, not independent signs.
        xe=conjugate(er,p)
        ye=conjugate(er,b)
        for eta in (Q(1,16),Q(1,4),Q(1),Q(4)):
          adjusted=add(core,add(scale(eta,xe),scale(1/eta,ye)))
          for gamma in (Q(1,4),Q(1),Q(4)):
            for pname,W in (("isotropic",wd0),("diagonal",wd1)):
              upper=add(scale(1+gamma,adjusted),scale(1+1/gamma,W))
              whole=add(direct,upper)
              margin=gersh(minus(original_lower,whole))
              results.append((margin,-tr(whole),ln,un,eta,gamma,pname,whole,upper))
    assert len(results)==216
    best=max(results,key=lambda x:x[:2])
    return results,best

def main():
    a=argparse.ArgumentParser()
    for n in ("mg24","mg46","mg47","mg48"):
        a.add_argument("--verified-"+n+"-json",required=True)
    opts=a.parse_args()
    load=lambda n:json.loads((ROOT/getattr(opts,"verified_"+n+"_json")).read_text())
    old24,old46,old47,new48=[load(n) for n in ("mg24","mg46","mg47","mg48")]
    assert new48["status"]=="ORIGINAL_MG48_COMPLETE_FREQUENCY_JOINT_MULTIPLIER_24D_RESIDUAL"
    assert old47["canonical_W_ODD_NEG"]==new48["canonical_W_ODD_NEG"]=="OPEN"
    hm,hr,he=original_H24_from_physical_source()
    assert he==Q(old24["physical_Gram_Loewner_row_error"])
    hlow=minus(hm,scale(he,eye()))
    center=[hm[i][P] for i in range(N)]
    radius=[hr[i][P] for i in range(N)]
    assert [str(v) for v in center]==old24["original_pole_b_center"]
    assert [str(v) for v in radius]==old24["original_pole_b_radii"]
    total=0;good=0
    for old47row,old46row,newrow in zip(old47["scenarios"],old46["scenarios"],new48["scenarios"]):
        mesh,k=old47row["mesh_cells"],old47row["cutoff_k"]
        assert (mesh,k)==(old46row["mesh_cells"],old46row["cutoff_k"])==(newrow["mesh_cells"],newrow["cutoff_k"])
        old24row=next(z for z in old24["cases"] if z["cutoff_k"]==k)
        tests,winner=replay(old47row,old46row,old24row,center,radius,hlow)
        saved=newrow["all_exact_candidate_margins"]
        assert len(saved)==len(tests)==newrow["new_joint_original_candidates"]==216
        for got,record in zip(tests,saved):
            g,negative_trace,ln,un,eta,gamma,pname,_,_=got
            assert record=={"G_lower":ln,"G_upper":un,"eta":str(eta),
                "gamma":str(gamma),"pole_fee":pname,
                "full24_Gersh":str(g),"full24_upper_trace":str(-negative_trace)}
        mg,_,ln,un,eta,gamma,pn,upper,omitted=winner
        assert rd(newrow["best_joint_complete_24D_upper"])==upper
        assert rd(newrow["best_joint_omitted_24D_upper"])==omitted
        assert mg==Q(newrow["best_joint_full24_Gersh"])
        assert newrow["best_joint_parameters"]=={"G_lower":ln,"G_upper":un,
            "eta":str(eta),"gamma":str(gamma),"pole_fee":pn}
        baseline=rd(old47row["selected_complete_24D_source_upper"])
        oldmargin=gersh(minus(hlow,baseline))
        assert oldmargin==Q(old47row["MG43_accepted_whole_Gersh_lower"])
        assert oldmargin==Q(newrow["MG43_full24_Gersh"])
        chosen=upper if mg>oldmargin else baseline
        name="MG48_joint_multiplier" if mg>oldmargin else "MG43_whole"
        assert newrow["selected_method"]==name
        assert chosen==rd(newrow["selected_complete_24D_upper"])
        lower=minus(hlow,chosen)
        assert lower==rd(newrow["selected_complete_24D_lower"])
        outcome=newrow["selected_exact_inertia_classification"]
        wit=newrow["selected_exact_inertia_witness"]
        if outcome=="POSITIVE_EXACT_RATIONAL_LDL":
            assert ldlpositive(lower)
            good+=1
        elif outcome=="NEGATIVE_EXACT_RATIONAL_RAYLEIGH":
            v=[Q(x) for x in wit["rational_vector"]]
            assert len(v)==24 and any(v)
            assert quadratic(lower,v)==Q(wit["exact_negative_quadratic"])<0
        else:
            assert outcome=="INCONCLUSIVE" and wit=={}
        assert newrow["original_source_24D_contraction"]==(outcome=="POSITIVE_EXACT_RATIONAL_LDL")
        assert newrow["all_original_frequencies_covered"]
        total+=len(tests)
    assert total==864 and good==sum(r["original_source_24D_contraction"] for r in new48["scenarios"])
    assert new48["all_original_864_joint_candidates_exact_rational"]
    assert new48["any_original_source_24D_contraction"]==(good>0)
    assert not new48["original_470D_strong_inverse_certified"]
    assert not new48["signed_original_51over56_negative_cap_certified"]
    assert new48["independent_original_Fourier_form_domain_audit"]=="OPEN"
    assert new48["complete_even_Weil_CC27_RH"]=="OPEN"
    print("MG48 independent original exact rational polynomial covariance replay PASS",
          {"matrices":total,"positive24":good,"all470_RH":"OPEN"},flush=True)

if __name__=="__main__": main()
