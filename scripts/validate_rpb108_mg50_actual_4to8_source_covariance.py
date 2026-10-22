#!/usr/bin/env python3
"""MG50: genuinely NEW original 24D physical Fourier measurement on [4,8].

Extend the accepted [0,4] direct source residual to [4,8], retain the
original true pole, and subtract the new band source H/G moments from
MG47's certified *same-original-operator* omitted [4,infinity) brackets.

The residual on |xi|>8 is bounded with MG48's joint multiplier
polynomial inequality, including SM41's complete high tail unchanged.
This is one valid complete original 24D Loewner UPPER; no 470D inverse.
"""
import argparse,json,sys
from fractions import Fraction as Q
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
import validate_rpb108_mg32_joint_fourier_residual as m32
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import ROOT
from validate_rpb108_mg25_original24_robust_trial import (
    deserialize, original_H24_from_physical_source)
from validate_rpb108_mg25_robust_source_aware_residual import (
    Id,T,mm,plus,sub,mul,shift,gersh_lower,psd)
from validate_rpb108_mg41_ideal_cross_error_feasibility import classify_ideal
from validate_rpb108_mg23_physical_metric_matrix_envelope import KAPPA
N=24;P=23; BEGIN=Q(4); END=Q(8); CELLS=32
ETAS=(Q(1,16),Q(1,4),Q(1),Q(4))
GAMMAS=(Q(1,4),Q(1),Q(4))
def mat(a):
    a=deserialize(a)
    assert len(a)==N and all(len(row)==N for row in a)
    return a
def enc(a):return [[str(x) for x in row] for row in a]
def tr(a):return sum((a[i][i] for i in range(N)),Q(0))
def sand(a,b):return mm(mm(T(b),a),b)
def cross(a,b,c):return plus(mm(mm(T(b),a),c),mm(mm(T(c),a),b))
def diagonal(ds):
    a=[[Q(0)]*N for _ in range(N)]
    for i,d in enumerate(ds):a[i][i]=d
    return a
def actual_4to8_original_cells():
    """Fresh ORIGINAL source coefficients: no [0,4] cell reuse or extrapolation."""
    centers,sources,a,c,hyp,Kglob,Kthird=m32.original_partition_preparation()
    assert len(sources)==25 and sources[24][0]=="pole"
    global4=m32.original_fourth_global(sources)
    source=[]
    matrices={"new":{"mass":(m32.zero(),m32.zero()),
                     "one":(m32.zero(),m32.zero())}}
    counts={key:{str(t):0 for t in m32.CHOSEN_TAUS} for key in ("mass","one")}
    for j in range(CELLS):
        left=BEGIN+(END-BEGIN)*Q(j,CELLS)
        right=BEGIN+(END-BEGIN)*Q(j+1,CELLS)
        assert right>left
        width=right-left;half=width/2;mid=(left+right)/2
        wl,wu,_=m32.positive_cell_weight_interval(left,right)
        assert 0<KAPPA<=wl<=wu
        vals=m32.original_exact_physical_fourier_midpoint(mid,centers,sources,hyp)
        derivative,second=m32.original_midpoint_derivative_intervals(
            mid,centers,sources,hyp)
        Kold=[min(g,m32.abs_cap(z)+third*half) if z is not None else g
              for g,z,third in zip(Kglob,second,Kthird)]
        v,d,eold=m32.transformed_affine(vals,derivative,Kold,a,c,half)
        components=m32.splits_original_source(
            v,d,eold,Kold,half,vals,derivative,a,c,23,24)
        s2=m32.exact_original_second_midpoint(mid,centers,sources,hyp)
        third=m32.third_adapted_whole_cell(
            mid,centers,sources,hyp,a,c,Kthird,half,global4)
        old28=m32.true_direct_adapted_curvature(s2,Kthird,a,c,Kold,half)
        radius=[]
        for i,(value,sloperad,curvature,rounding) in enumerate(components):
            direct2=s2[i]-a[i]*s2[24]-c[i]*s2[23] if i<23 else s2[24]
            improved=min(old28[i][0],m32.abs_cap(direct2)+third[i][0]*half)
            r=m32.up(value+sloperad+improved*half*half/2)
            assert 0<=r<=eold[i]
            radius.append(r)
        assert len(v)==len(d)==len(radius)==N
        for key in ("mass","one"):
            low,high=(Q(1),Q(1)) if key=="mass" else (wl,wu)
            tau=max(m32.CHOSEN_TAUS,key=lambda t:(
                m32.lower_cell_trace((low,high),width,v,d,eold,t),-t))
            m32.add_directed_cell(matrices,"new",key,(low,high),
                                  width,v,d,radius,tau)
            counts[key][str(tau)]+=1
        source.append((left,right,wl,wu,v,d,radius))
    assert len(source)==CELLS and source[0][0]==BEGIN and source[-1][1]==END
    assert all(source[i][1]==source[i+1][0] for i in range(CELLS-1))
    hlow,hup,_,_=m32.finalize(matrices["new"]["mass"])
    glow,gup,_,_=m32.finalize(matrices["new"]["one"])
    assert psd(sub(hup,hlow)) and psd(sub(gup,glow))
    return source,hlow,hup,glow,gup,counts

def candidates(row47,row46,row24,newhl,newhu,newgl,newgu,bmid,brad):
    """MG48 joint polynomial on |xi|>8, true original B and pole."""
    k=row47["cutoff_k"]
    m=Q(17)+Q(347*k,500)
    assert m==Q(row24["original_global_lowband_majorant_M"])
    tau=Q(row24["complete_original_strong_tail_rational"])
    B=mat(row47["full_original_rational_response_B"])
    assert B==mat(row46["response_matrix_original_rational"])
    Hdup=sub(mat(row46["original_complete_omitted_H_upper"]),newhl)
    Hdlo=sub(mul(1/KAPPA,mat(row47["original_G_lower_candidate_matrices"]["mass_kappa"])),newhu)
    assert Hdup==T(Hdup) and psd(Hdup) and psd(sub(Hdup,Hdlo))
    gl={name:sub(mat(a),newgu) for name,a in
         row47["original_G_lower_candidate_matrices"].items()}
    gu={name:sub(mat(a),newgl) for name,a in
         row47["original_G_upper_candidate_matrices"].items()}
    q=[sum((bmid[i]*B[i][j] for i in range(N)),Q(0)) for j in range(N)]
    C0=[[Q(i==j)+(2*q[j] if i==P else Q(0)) for j in range(N)]
        for i in range(N)]
    P0=sub(C0,mul((KAPPA+m)/2,B))
    ds=[sum((brad[i]*abs(B[i][j]) for i in range(N)),Q(0))
        for j in range(N)]
    pp=Hdup[P][P];assert pp>=0
    fees=(("isotropic",mul(4*pp*sum((d*d for d in ds),Q(0)),Id(N))),
          ("diagonal",diagonal([4*pp*sum(ds,Q(0))*x for x in ds])))
    hcore=plus(sub(sand(Hdup,C0),mul(KAPPA*m,sand(Hdlo,B))),
               mul(tau,mm(T(B),B)))
    out=[]
    for ln,L in gl.items():
      for un,U in gu.items():
        E=mul(Q(1,2),sub(U,L))
        assert psd(E)
        Gc=mul(Q(1,2),plus(U,L))
        core=sub(hcore,cross(Gc,P0,B))
        ex=sand(E,P0);ey=sand(E,B)
        assert psd(ex) and psd(ey)
        for eta in ETAS:
          base=plus(core,plus(mul(eta,ex),mul(1/eta,ey)))
          for gamma in GAMMAS:
            for pn,W in fees:
              complete=plus(mul(1+gamma,base),mul(1+1/gamma,W))
              assert complete==T(complete)
              out.append((ln,un,eta,gamma,pn,complete))
    assert len(out)==216
    return out

def main():
    p=argparse.ArgumentParser()
    for n in ("mg24","mg46","mg47","mg48"):
        p.add_argument("--verified-"+n+"-json",required=True)
    p.add_argument("--output",default="artifacts/mg50_actual_original_4to8_source_covariance.json")
    args=p.parse_args()
    load=lambda n:json.loads((ROOT/getattr(args,"verified_"+n+"_json")).read_text())
    a24,a46,a47,a48=[load(n) for n in ("mg24","mg46","mg47","mg48")]
    assert all(x["canonical_W_ODD_NEG"]=="OPEN" for x in (a24,a46,a47,a48))
    assert a48["status"]=="ORIGINAL_MG48_COMPLETE_FREQUENCY_JOINT_MULTIPLIER_24D_RESIDUAL"
    hm,hr,he=original_H24_from_physical_source()
    assert he==Q(a24["physical_Gram_Loewner_row_error"])
    Hlo=sub(hm,mul(he,Id(N)))
    bmid=[hm[i][P] for i in range(N)]
    brad=[hr[i][P] for i in range(N)]
    assert [str(x) for x in bmid]==a24["original_pole_b_center"]
    assert [str(x) for x in brad]==a24["original_pole_b_radii"]
    source,hl,hu,gl,gu,choices=actual_4to8_original_cells()
    original_low,_,_,_,_=m32.exact_original_cells()
    assert len(original_low)==32 and original_low[0][0]==0
    assert original_low[-1][1]==BEGIN
    assert source[0][0]==original_low[-1][1]
    out=[]
    for s47,s46,s48 in zip(a47["scenarios"],a46["scenarios"],a48["scenarios"]):
        mesh,k=s47["mesh_cells"],s47["cutoff_k"]
        assert (mesh,k)==(s46["mesh_cells"],s46["cutoff_k"])==(s48["mesh_cells"],s48["cutoff_k"])
        c24=next(x for x in a24["cases"] if x["cutoff_k"]==k)
        B=mat(s47["full_original_rational_response_B"])
        U0=mat(s46["original_MG32_direct_band_24D_upper"])
        same0,_,_=m32.joint_prefix_upper(original_low,bmid,brad,B)
        assert U0==same0
        newU,rad,pol=m32.joint_prefix_upper(source,bmid,brad,B)
        Umeasured=plus(U0,newU)
        tests=[]
        for ln,un,eta,gamma,pn,tailU in candidates(
                s47,s46,c24,hl,hu,gl,gu,bmid,brad):
            allU=plus(Umeasured,tailU)
            mg=gersh_lower(sub(Hlo,allU))
            tests.append((mg,-tr(allU),ln,un,eta,gamma,pn,allU,tailU))
        best=max(tests,key=lambda a:a[:2])
        g,_,ln,un,eta,gamma,pn,bestU,besttail=best
        baseline=mat(s47["selected_complete_24D_source_upper"])
        bmargin=gersh_lower(sub(Hlo,baseline))
        assert bmargin==Q(s48["MG43_full24_Gersh"])
        selected=bestU if g>bmargin else baseline
        mode="MG50_measured_4to8_plus_joint_tail" if g>bmargin else "MG43_whole"
        lower=sub(Hlo,selected)
        typ,wit=classify_ideal(lower)
        assert typ in ("NEGATIVE_EXACT_RATIONAL_RAYLEIGH",
                       "POSITIVE_EXACT_RATIONAL_LDL","INCONCLUSIVE")
        out.append({
          "mesh_cells":mesh,"cutoff_k":k,
          "actual_4to8_original_direct_24D_upper":enc(newU),
          "actual_0to8_original_direct_24D_upper":enc(Umeasured),
          "direct_4to8_source_radius_l1_sum":str(rad),
          "direct_4to8_Young_counts":pol,
          "all_216_candidate_exact_margins":[{
             "G_lower":n,"G_upper":u,"eta":str(e),"gamma":str(gg),
             "pole_fee":pp,"new_complete_24D_Gersh":str(ggersh),
             "new_complete_24D_trace":str(-negtr)}
             for ggersh,negtr,n,u,e,gg,pp,_,_ in tests],
          "best_new_joint_parameters":{
             "G_lower":ln,"G_upper":un,"eta":str(eta),"gamma":str(gamma),
             "pole_fee":pn},
          "best_new_tail_24D_upper":enc(besttail),
          "best_new_whole_24D_upper":enc(bestU),
          "best_new_whole_Gersh":str(g),
          "MG43_accepted_whole_Gersh":str(bmargin),
          "selected_whole_method":mode,
          "selected_source_24D_upper":enc(selected),
          "selected_source_24D_lower":enc(lower),
          "selected_exact_24D_inertia":typ,
          "selected_exact_24D_inertia_witness":wit,
          "source_contraction":typ=="POSITIVE_EXACT_RATIONAL_LDL",
          "true_original_source_23adapted_plus_true_sinh_pole":True,
          "true_new_4to8_original_fourier_measurement":True,
          "true_all_frequency_tail_paid":True
        })
        print("MG50 ORIGINAL ACTUAL [4,8] case",mesh,k,
              "new",float(g),"MG43",float(bmargin),
              "chosen",mode,flush=True)
    assert len(out)==4
    report={
      "status":"ORIGINAL_MG50_TRUE_4TO8_FOURIER_JOINT_24D_SOURCE_GATE",
      "canonical_W_ODD_NEG":"OPEN",
      "accepted_input_runs":{"MG24":39378465438,"MG46":39638393721,
                             "MG47":39663431182,"MG48":39685179933},
      "new_original_positive_frequency_band":["4","8"],
      "new_actual_original_cell_count":CELLS,
      "new_band_original_mass_lower":enc(hl),
      "new_band_original_mass_upper":enc(hu),
      "new_band_original_G_lower":enc(gl),
      "new_band_original_G_upper":enc(gu),
      "new_band_original_mass_and_G_tau_choices":choices,
      "new_band_never_double_counted":True,
      "measured_direct_full_original_[0,8]_and_high_tail_full":True,
      "all_864_new_original_exact_24D_candidate_matrices":True,
      "any_original_24D_source_contraction":any(r["source_contraction"] for r in out),
      "original_470D_strong_inverse_certified":False,
      "signed_original_51over56_negative_cap_certified":False,
      "independent_original_Fourier_form_domain_audit":"OPEN",
      "complete_even_Weil_CC27_RH":"OPEN",
      "cases":out}
    dest=ROOT/args.output;dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(report,indent=2)+"\n")
    print("MG50 4to8 original physical source candidate construction",
          {"cases":len(out),"candidates":864,"contraction":report["any_original_24D_source_contraction"],
           "470D_RH":"OPEN"},flush=True)
if __name__=="__main__":main()
