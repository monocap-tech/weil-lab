#!/usr/bin/env python3
"""MG50 independent exact original 4..8 source measurement and 864 matrix replay.

Recomputes the fresh 32 original physical source cells from accepted
analytic generator primitives. No producer import. Reconstructs each
new coupled residual by UNGROUPED frequency polynomial algebra.
"""
import argparse,json,sys
from fractions import Fraction as Q
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import ROOT
from validate_rpb108_mg25_original24_robust_trial import original_H24_from_physical_source
from validate_rpb108_mg23_physical_metric_matrix_envelope import KAPPA
import validate_rpb108_mg32_joint_fourier_residual as orig
N=24;P=23
def rd(a):return [[Q(x) for x in row] for row in a]
def transpose(a):return [list(v) for v in zip(*a)]
def mm(a,b):
    bt=transpose(b)
    return [[sum((x*y for x,y in zip(row,col)),Q(0)) for col in bt] for row in a]
def add(a,b):return [[u+v for u,v in zip(x,y)] for x,y in zip(a,b)]
def times(k,a):return [[k*x for x in row] for row in a]
def minus(a,b):return add(a,times(-1,b))
def ident():return [[Q(i==j) for j in range(N)] for i in range(N)]
def sand(a,b):return mm(mm(transpose(b),a),b)
def diag(ds):
    o=times(0,ident())
    for i,x in enumerate(ds):o[i][i]=x
    return o
def tr(a):return sum((a[i][i] for i in range(N)),Q(0))
def gersh(a):
    assert a==transpose(a)
    return min((a[i][i]-sum((abs(a[i][j]) for j in range(N) if j!=i),Q(0))
                for i in range(N)))
def qf(v,a):return sum((v[i]*a[i][j]*v[j] for i in range(N) for j in range(N)),Q(0))
def independent_4to8():
    centers,sources,a,c,hyp,Kg,Kt=orig.original_partition_preparation()
    g4=orig.original_fourth_global(sources)
    original=[]
    moment={"local":{"mass":(orig.zero(),orig.zero()),
                     "one":(orig.zero(),orig.zero())}}
    counts={key:{str(t):0 for t in orig.CHOSEN_TAUS} for key in ("mass","one")}
    for j in range(32):
        lo=Q(4)+Q(j,8);hi=lo+Q(1,8)
        half=(hi-lo)/2;mid=(lo+hi)/2
        wl,wu,_=orig.positive_cell_weight_interval(lo,hi)
        assert KAPPA<=wl<=wu
        vals=orig.original_exact_physical_fourier_midpoint(mid,centers,sources,hyp)
        d1,d2=orig.original_midpoint_derivative_intervals(mid,centers,sources,hyp)
        K=[min(x,orig.abs_cap(z)+w*half) if z is not None else x
           for x,z,w in zip(Kg,d2,Kt)]
        v,d,old=orig.transformed_affine(vals,d1,K,a,c,half)
        split=orig.splits_original_source(v,d,old,K,half,vals,d1,a,c,23,24)
        s2=orig.exact_original_second_midpoint(mid,centers,sources,hyp)
        s3=orig.third_adapted_whole_cell(mid,centers,sources,hyp,a,c,Kt,half,g4)
        k2=orig.true_direct_adapted_curvature(s2,Kt,a,c,K,half)
        r=[]
        for i,(v_err,d_err,_,_) in enumerate(split):
            second=s2[24] if i==23 else s2[i]-a[i]*s2[24]-c[i]*s2[23]
            cur=min(k2[i][0],orig.abs_cap(second)+s3[i][0]*half)
            bound=orig.up(v_err+d_err+cur*half*half/2)
            assert 0<=bound<=old[i]
            r.append(bound)
        for key in ("mass","one"):
            wc=(Q(1),Q(1)) if key=="mass" else (wl,wu)
            tau=max(orig.CHOSEN_TAUS,key=lambda t:(
                orig.lower_cell_trace(wc,hi-lo,v,d,old,t),-t))
            orig.add_directed_cell(moment,"local",key,wc,hi-lo,v,d,r,tau)
            counts[key][str(tau)]+=1
        original.append((lo,hi,wl,wu,v,d,r))
    assert original[0][0]==4 and original[-1][1]==8
    assert all(original[j][1]==original[j+1][0] for j in range(31))
    hL,hU,_,_=orig.finalize(moment["local"]["mass"])
    gL,gU,_,_=orig.finalize(moment["local"]["one"])
    return original,hL,hU,gL,gU,counts

def independent_direct(cells,B,bmid,brad):
    measured={"direct":{"mass":(orig.zero(),orig.zero())}}
    choices={str(t):0 for t in orig.CHOSEN_TAUS}
    err=Q(0)
    for left,right,wl,wu,v,d,r in cells:
        half=(right-left)/2
        a0=(wl+wu)/2
        da=(wu-wl)/2
        coeff=[sum((bmid[i]*B[i][j] for i in range(N)),Q(0))
               for j in range(N)]
        unc=[sum((brad[i]*abs(B[i][j]) for i in range(N)),Q(0))
             for j in range(N)]
        pole=abs(v[P])+half*abs(d[P])+r[P]
        C=[[Q(i==j)-a0*B[i][j]+(2*coeff[j] if i==P else Q(0))
            for j in range(N)] for i in range(N)]
        base=[sum((v[i]*C[i][j] for i in range(N)),Q(0)) for j in range(N)]
        slope=[sum((d[i]*C[i][j] for i in range(N)),Q(0)) for j in range(N)]
        radius=[]
        for j in range(N):
            x=sum((r[i]*abs(C[i][j]) for i in range(N)),Q(0))
            x+=da*sum((abs(B[i][j])*(abs(v[i])+half*abs(d[i])+r[i])
                       for i in range(N)),Q(0))
            x+=2*pole*unc[j]
            radius.append(x)
        err+=sum(radius,Q(0))
        tau=min(orig.CHOSEN_TAUS,key=lambda t:(
            (1+t)*(sum((x*x for x in base),Q(0))
                   +(right-left)**2*sum((x*x for x in slope),Q(0))/12)
            +(1+1/t)*sum(radius,Q(0))**2,t))
        choices[str(tau)]+=1
        orig.add_directed_cell(measured,"direct","mass",
                               (Q(1),Q(1)),right-left,base,slope,radius,tau)
    _,U,_,_=orig.finalize(measured["direct"]["mass"])
    return U,err,choices

def reproduce(a24,a46,a47,a48,a50):
    hm,hr,he=original_H24_from_physical_source()
    assert he==Q(a24["physical_Gram_Loewner_row_error"])
    hlow=minus(hm,times(he,ident()))
    bmid=[hm[i][P] for i in range(N)]
    brad=[hr[i][P] for i in range(N)]
    cells,hL,hU,gL,gU,counts=independent_4to8()
    assert rd(a50["new_band_original_mass_lower"])==hL
    assert rd(a50["new_band_original_mass_upper"])==hU
    assert rd(a50["new_band_original_G_lower"])==gL
    assert rd(a50["new_band_original_G_upper"])==gU
    assert counts==a50["new_band_original_mass_and_G_tau_choices"]
    original,_,_,_,_=orig.exact_original_cells()
    n=0;positive=0
    for c46,c47,c48,c50 in zip(a46["scenarios"],a47["scenarios"],
                                a48["scenarios"],a50["cases"]):
        mesh,k=c50["mesh_cells"],c50["cutoff_k"]
        assert (mesh,k)==(c46["mesh_cells"],c46["cutoff_k"])==(c47["mesh_cells"],c47["cutoff_k"])==(c48["mesh_cells"],c48["cutoff_k"])
        B=rd(c47["full_original_rational_response_B"])
        uc,_,_=independent_direct(original,B,bmid,brad)
        assert uc==rd(c46["original_MG32_direct_band_24D_upper"])
        new,rad,choices=independent_direct(cells,B,bmid,brad)
        assert new==rd(c50["actual_4to8_original_direct_24D_upper"])
        assert str(rad)==c50["direct_4to8_source_radius_l1_sum"]
        assert choices==c50["direct_4to8_Young_counts"]
        direct=add(uc,new)
        assert direct==rd(c50["actual_0to8_original_direct_24D_upper"])
        row24=next(x for x in a24["cases"] if x["cutoff_k"]==k)
        masslo=minus(times(1/KAPPA,rd(c47["original_G_lower_candidate_matrices"]["mass_kappa"])),hU)
        massup=minus(rd(c46["original_complete_omitted_H_upper"]),hL)
        m=Q(17)+Q(347*k,500)
        tau=Q(row24["complete_original_strong_tail_rational"])
        assert m==Q(row24["original_global_lowband_majorant_M"])
        cp=[sum((bmid[i]*B[i][j] for i in range(N)),Q(0)) for j in range(N)]
        C=[[Q(i==j)+(2*cp[j] if i==P else Q(0)) for j in range(N)]
           for i in range(N)]
        centerP=minus(C,times((KAPPA+m)/2,B))
        ds=[sum((brad[i]*abs(B[i][j]) for i in range(N)),Q(0))
            for j in range(N)]
        W0=times(4*massup[P][P]*sum((x*x for x in ds),Q(0)),ident())
        W1=diag([4*massup[P][P]*sum(ds,Q(0))*x for x in ds])
        options=[]
        for ln,Lo in c47["original_G_lower_candidate_matrices"].items():
          for un,Up in c47["original_G_upper_candidate_matrices"].items():
            L=minus(rd(Lo),gU);U=minus(rd(Up),gL)
            Gc=times(Q(1,2),add(L,U))
            E=times(Q(1,2),minus(U,L))
            # Independent ungrouped physical joint polynomial.
            core= sand(massup,C)
            core= minus(core,times(KAPPA*m,sand(masslo,B)))
            core= add(core,times(tau,mm(transpose(B),B)))
            core= minus(core,mm(mm(transpose(C),Gc),B))
            core= minus(core,mm(mm(transpose(B),Gc),C))
            core= add(core,times(KAPPA+m,sand(Gc,B)))
            ex=sand(E,centerP);ey=sand(E,B)
            for eta in (Q(1,16),Q(1,4),Q(1),Q(4)):
              adjusted=add(core,add(times(eta,ex),times(1/eta,ey)))
              for gamma in (Q(1,4),Q(1),Q(4)):
                for pn,W in (("isotropic",W0),("diagonal",W1)):
                  rem=add(times(1+gamma,adjusted),times(1+1/gamma,W))
                  whole=add(direct,rem)
                  margin=gersh(minus(hlow,whole))
                  options.append((margin,-tr(whole),ln,un,eta,gamma,pn,whole,rem))
        assert len(options)==len(c50["all_216_candidate_exact_margins"])==216
        for value,saved in zip(options,c50["all_216_candidate_exact_margins"]):
            g,ntr,ln,un,eta,gamma,pn,_,_=value
            assert saved=={"G_lower":ln,"G_upper":un,"eta":str(eta),
                           "gamma":str(gamma),"pole_fee":pn,
                           "new_complete_24D_Gersh":str(g),
                           "new_complete_24D_trace":str(-ntr)}
        best=max(options,key=lambda v:v[:2])
        g,_,ln,un,eta,gamma,pn,whole,rem=best
        assert rd(c50["best_new_tail_24D_upper"])==rem
        assert rd(c50["best_new_whole_24D_upper"])==whole
        assert str(g)==c50["best_new_whole_Gersh"]
        assert c50["best_new_joint_parameters"]=={
            "G_lower":ln,"G_upper":un,"eta":str(eta),"gamma":str(gamma),"pole_fee":pn}
        mg43=rd(c47["selected_complete_24D_source_upper"])
        g43=gersh(minus(hlow,mg43))
        assert str(g43)==c50["MG43_accepted_whole_Gersh"]
        chosen=whole if g>g43 else mg43
        typ="MG50_measured_4to8_plus_joint_tail" if g>g43 else "MG43_whole"
        assert c50["selected_whole_method"]==typ
        assert rd(c50["selected_source_24D_upper"])==chosen
        lower=minus(hlow,chosen)
        assert rd(c50["selected_source_24D_lower"])==lower
        if c50["selected_exact_24D_inertia"]=="NEGATIVE_EXACT_RATIONAL_RAYLEIGH":
            v=[Q(x) for x in c50["selected_exact_24D_inertia_witness"]["rational_vector"]]
            assert qf(v,lower)==Q(c50["selected_exact_24D_inertia_witness"]["exact_negative_quadratic"])<0
        elif c50["selected_exact_24D_inertia"]=="POSITIVE_EXACT_RATIONAL_LDL":
            # Independently require every leading Schur complement pivot positive
            a=[list(row) for row in lower]
            for j in range(N):
                pivot=a[j][j]
                assert pivot>0
                for x in range(j+1,N):
                    for y in range(j+1,N):
                        a[x][y]-=a[x][j]*a[j][y]/pivot
            positive+=1
        else:
            assert c50["selected_exact_24D_inertia"]=="INCONCLUSIVE"
        n+=len(options)
    assert n==864
    assert a50["all_864_new_original_exact_24D_candidate_matrices"]
    assert a50["any_original_24D_source_contraction"]==(positive>0)
    assert not a50["original_470D_strong_inverse_certified"]
    assert not a50["signed_original_51over56_negative_cap_certified"]
    assert a50["complete_even_Weil_CC27_RH"]=="OPEN"
    print("MG50 INDEPENDENT original 4to8 Fourier/source + 864 polynomial matrix replay PASS",
          {"candidate_matrices":n,"source24_positive":positive,
           "original_470D_RH":"OPEN"},flush=True)
def main():
    parser=argparse.ArgumentParser()
    for n in ("mg24","mg46","mg47","mg48","mg50"):
        parser.add_argument("--verified-"+n+"-json",required=True)
    args=parser.parse_args()
    load=lambda n:json.loads((ROOT/getattr(args,"verified_"+n+"_json")).read_text())
    a24,a46,a47,a48,a50=[load(n) for n in ("mg24","mg46","mg47","mg48","mg50")]
    assert a50["status"]=="ORIGINAL_MG50_TRUE_4TO8_FOURIER_JOINT_24D_SOURCE_GATE"
    assert all(x["canonical_W_ODD_NEG"]=="OPEN" for x in (a24,a46,a47,a48,a50))
    reproduce(a24,a46,a47,a48,a50)
if __name__=="__main__":main()
