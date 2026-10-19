#!/usr/bin/env python3
"""SM63: direct ORIGINAL signed 3-source third-positive-plane acceptance.

Test real supported g1 (SM62's positive complement diagonal) together
with the independently proven positive original g2 sine / g17 xcos
anchor plane, WITHOUT splicing lower blocks or assuming mixed source
cross terms.

Recompute signed multiplier *itself* on [13,16], entire SI10
all-seven-prime negative 973-parent 3892-subcell support outside,
49 old signed-positive bands disjoint from the core, and the
original SM54 first96 + SM55 best242 strictly positive real
frequency windows in [0,13] (all disjoint). Recompute true
frequency Fourier sin/generic xcos at each of 3 DIFFERENT
supported source centers and original full exact exceptional pole
on these true physical sources. All signed cross terms are
included and all 3-source analytic Jensen/affine errors paid.

The baseline SM53 original three-source constructor required all
cluster sources to have the same center; SM63 uses one actual
different-center sine and does NOT reuse that invalid assumption.
No inverse of an indefinite LOWER is taken.

If and ONLY if all three Sylvester minors of this complete
original signed 3x3 LOWER are strictly positive, the ACTUAL
source 3-plane is PD and original supported source25 negative
index is <=22 (given full25 physical Gram SPD).
Otherwise a non-PD LOWER is inconclusive about actual signed
negativity or full odd negative index; report exact minors.
Full 470-source original odd inverse and orthogonal remainder,
even/Weil/CC27/RH remain OPEN.
"""
import argparse,json
from fractions import Fraction as F
from validate_rpb108_si06_negative_band import PI,prime_interval
from validate_rpb108_si07_negative_support_cover import M
from validate_rpb108_si10_complement_positivity import KAPPA
from validate_rpb108_sm10_explicit_odd_cap_moments import full_upper_leaves
from validate_rpb108_sm39_rational_left_arch_cap import arch_lower_at
from validate_rpb108_sm40_endpoint_curvature_negative_cap import D2
from validate_rpb108_sm42_original_physical_gram_and_low_gate import (
    I,F0,F1,F2,original_full_25_physical_interval_gram)
from validate_rpb108_sm43_positive_cell_envelope import (
    ROOT,original_source_centered_windows,ceil_rat)
from validate_rpb108_sm44_physical_fourier_cell_gram import (
    quantize,sqrt_upper,original_full_second_derivative_upper)
from validate_rpb108_sm46_affine_physical_fourier_source import (
    original_F3,original_third_spatial_moment)
from validate_rpb108_sm53_original_3source_pole import signed_m_lower
from validate_rpb108_sm49_adaptive_positive_jensen import original_adaptive_candidate_cells
from validate_rpb108_sm12_positive_reference_33 import (
    CENTERS as OLD_POS,RADIUS as OLD_R)
from validate_rpb108_sm62_full25_338signed_positive import (
    all_338_disjoint_original_signed_positive)

N=3
IX=(1,2,17)
LEFT=F(13);RIGHT=F(16);NCELLS=768;DEN=10**12
def up(x):return ceil_rat(x,DEN)
def zero():return [[F(0)]*N for _ in range(N)]
def accum(A,B,k):
    for i in range(N):
        for j in range(N):A[i][j]+=k*B[i][j]
def diag(A,fee):
    for i in range(N):A[i][i]+=fee
def outer(v):return [[v[i]*v[j] for j in range(N)] for i in range(N)]
def affine(v,d,r):
    return [[v[i]*v[j]+d[i]*d[j]*r*r/3 for j in range(N)]
            for i in range(N)]
def determinant(A):
    return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
           -A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
           +A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))
def compact(A):
    assert all(A[i][j]==A[j][i] for i in range(N) for j in range(N))
    q=[[quantize(A[i][j]) for j in range(N)] for i in range(N)]
    fee=up(max(sum(abs(q[i][j]-A[i][j]) for j in range(N))
               for i in range(N)))
    return [[q[i][j]-(fee if i==j else F(0))
             for j in range(N)] for i in range(N)],fee

class FourierTriple:
    def __init__(self,centers,sources):
        self.centers,self.sources=centers,sources
        self.pi=I(PI[0],PI[1])
        self.K=original_full_second_derivative_upper(sources)
        self.T3=original_third_spatial_moment(sources)
        assert all(sources[k][0]=="cluster" for k in IX)
        assert sources[1][2]==sources[2][2]==0 and sources[17][2]==1
        assert sources[2][1]==sources[17][1]
        assert sources[1][1]!=sources[2][1]
    def cell(self,l,r):
        assert l<r
        mid=(l+r)/2;half=(r-l)/2
        v=[];d=[];er=[];mean=[];local=0
        for k in IX:
            kind,j,degree=self.sources[k]
            c=self.centers[j]
            if degree==0:
                val=(F0(c-mid)-F0(c+mid))/2
                deriv=self.pi*(F1(c-mid)+F1(c+mid))
                second=2*self.pi*self.pi*(F2(c+mid)-F2(c-mid))
            elif degree==1:
                val=(F1(mid+c)+F1(mid-c))/2
                deriv=self.pi*(F2(mid+c)+F2(mid-c))
                second=-2*self.pi*self.pi*(original_F3(mid+c)+original_F3(mid-c))
            else:raise AssertionError("source not physical degree0/1")
            vi=quantize(val.mid())
            di=quantize(deriv.mid())
            ev=ceil_rat(max(abs(val.l-vi),abs(val.h-vi)),10**9)
            ed=ceil_rat(max(abs(deriv.l-di),abs(deriv.h-di)),10**9)
            K=min(self.K[k],max(abs(second.l),abs(second.h))+self.T3[k]*half)
            assert 0<=K<=self.K[k]
            local+=int(K<self.K[k])
            v.append(vi);d.append(di)
            er.append(ev+ed*half+K*half*half/2)
            mean.append(ev+K*half*half/6)
        eps_aff=2*sqrt_upper(
            sum((vi*vi+di*di*half*half/3 for vi,di in zip(v,d)),F(0))
            *sum((e*e for e in er),F(0))
        )+sum((e*e for e in er),F(0))
        eps_mean=2*sqrt_upper(
            sum((vi*vi for vi in v),F(0))
            *sum((e*e for e in mean),F(0))
        )+sum((e*e for e in mean),F(0))
        return v,affine(v,d,half),eps_aff,eps_mean,local

def signed_original_core(calc):
    step=(RIGHT-LEFT)/NCELLS
    assert step==F(1,256)
    result=zero();eps=F(0);positive=negative=0;local=0
    for i in range(NCELLS):
        a=LEFT+i*step;b=a+step
        m=signed_m_lower(a,b)
        v,A,ea,em,loc=calc.cell(a,b)
        local+=loc
        weight=2*step*m
        if m>=0:
            accum(result,outer(v),weight);eps+=weight*em;positive+=1
        else:
            accum(result,A,weight);eps-=weight*ea;negative+=1
    diag(result,-up(eps))
    assert positive+negative==768
    return result,{"original_signed_core_cells":768,"signed_core_positive":positive,
                    "signed_core_negative":negative,"signed_core_error":str(up(eps)),
                    "core_local_curvature_improvements":local}

def original_true_outside_negative(calc):
    clusters,W,Mneg,mass=full_upper_leaves()
    assert len(clusters)==107 and W==F(973,32)
    leaves=[x for cluster in clusters for x in cluster]
    assert len(leaves)==973
    U=zero();eps=F(0);outside=inside=nonzero=0
    for a,b,h in leaves:
        parent=h+KAPPA
        for t in range(4):
            l=a+(b-a)*F(t,4);r=a+(b-a)*F(t+1,4)
            assert not(l<LEFT<r or l<RIGHT<r)
            if LEFT<=l and r<=RIGHT:
                inside+=1;continue
            outside+=1
            mlo=arch_lower_at(l)+prime_interval((l+r)/2)[0]-M*(r-l)/2
            need=max(F(0),KAPPA-mlo)
            w=min(parent,ceil_rat(need,10**6))
            assert w>=need or w==parent
            if not w:continue
            nonzero+=1
            _,A,ea,em,_=calc.cell(l,r)
            c=2*(r-l)*w
            accum(U,A,c);eps+=c*ea
    assert inside+outside==3892
    diag(U,up(eps))
    return U,{"whole_original_negative_parent_leaves":973,
              "original_negative_quartered_cells":3892,
              "negative_subcells_outside_core":outside,
              "negative_nonzero_subcells_outside_core":nonzero,
              "outside_allcross_upper_error":str(up(eps))}

def positive_outside(calc,centers,sources,extra338):
    old,available,_,_=original_adaptive_candidate_cells(centers,sources)
    assert len(old)==32 and len(OLD_POS)==17
    windows=[(c-OLD_R,c+OLD_R,F(2),"SM12") for c in OLD_POS]
    windows +=[(x["a"],x["b"],x["delta"],"SM49") for x in old]
    # This is a direct original signed integral lower WITHOUT a kappa
    # full-Gram baseline; the new 338 source-positive increments use
    # their entire rigorously original signed weight, unlike SM62
    # which correctly subtracts its already-paid kappa baseline.
    for l,r,d,origin in extra338:
        assert d>0
        windows.append((l,r,d+KAPPA,origin))
    windows.sort()
    assert len(windows)==387
    assert all(windows[i][1]<=windows[i+1][0] for i in range(len(windows)-1))
    positive=zero();fee=F(0);outside=0
    counts={"SM12":0,"SM49":0,"SM54_96":0,"SM55_242":0}
    for a,b,delta,label in windows:
        if not(b<=LEFT or a>=RIGHT):continue
        outside+=1;counts[label]+=1
        v,_,_,em,_=calc.cell(a,b)
        gamma=2*(b-a)*delta
        accum(positive,outer(v),gamma);fee+=gamma*em
    diag(positive,-up(fee))
    assert counts["SM54_96"]==96 and counts["SM55_242"]==242
    assert outside==sum(counts.values())
    return positive,{"total_true_disjoint_real_signed_positive_windows":len(windows),
       "true_positive_real_windows_outside_core":outside,
       "credited_disjoint_positive_by_source":counts,
       "whole_true_three_source_positive_mean_error":str(up(fee))}

def pole_upper(H):
    q=[];e=[]
    for k in IX:
        val=H[k][24]
        x=quantize(val.mid())
        q.append(x);e.append(max(abs(val.l-x),abs(val.h-x)))
    q2=sum((x*x for x in q),F(0))
    e2=sum((x*x for x in e),F(0))
    fee=up(2*(2*sqrt_upper(q2*e2)+e2))
    A=[[2*q[i]*q[j]+(fee if i==j else F(0))
        for j in range(N)] for i in range(N)]
    return A,fee

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output",default="artifacts/sm63_original_direct_signed_positive_three_source.json")
    a=p.parse_args()
    m=json.loads((ROOT/"research/obligations.json").read_text())
    odd=next(x for x in m["obligations"] if x["id"]=="W-ODD-NEG")
    assert m["active_obligation"]=="W-ODD-NEG"
    assert m["objective"]["status"]==odd["status"]=="open"
    assert m["governance"]["no_automatic_promotion"]
    assert all(x in odd["evidence"] for x in ("SM52","SM53","SM55","SM59","SM62","SM63"))
    centers,sources,_=original_source_centered_windows()
    assert len(sources)==25 and sources[24][0]=="pole"
    calc=FourierTriple(centers,sources)
    H,actual,_=original_full_25_physical_interval_gram()
    assert actual==sources
    G=[[H[i][j] for j in IX] for i in IX]
    Gq=[[quantize(x.mid()) for x in row] for row in G]
    gerr=max(sum(max(abs(G[i][j].l-Gq[i][j]),abs(G[i][j].h-Gq[i][j]))
         for j in range(N)) for i in range(N))
    GL=[[Gq[i][j]-(gerr if i==j else F(0)) for j in range(N)] for i in range(N)]
    assert GL[0][0]>0
    assert GL[0][0]*GL[1][1]-GL[0][1]**2>0
    assert determinant(GL)>0
    windows,windowstats=all_338_disjoint_original_signed_positive(centers,sources)
    assert len(windows)==338
    core,cs=signed_original_core(calc)
    negative,ns=original_true_outside_negative(calc)
    positive,ps=positive_outside(calc,centers,sources,windows)
    pole,pfee=pole_upper(H)
    matrix=[[core[i][j]-negative[i][j]+positive[i][j]-pole[i][j]
             for j in range(N)] for i in range(N)]
    L,rounding=compact(matrix)
    # Direct signed result ordered (g1,g2,g17); independently
    # require the anchor (g2,g17) 2x2 positive test from SM52.
    anchor52=json.loads((ROOT/"certificates/rpb108_sm52_original_coupled_source_matrix.json").read_text())
    assert anchor52["source_indices"]==[2,17]
    Aa=[[F(x) for x in row] for row in anchor52["matrix"]]
    assert Aa[0][0]>0 and Aa[0][0]*Aa[1][1]-Aa[0][1]**2>0
    # Direct complete 3source LOWER has all true source cross
    # and true pole. Its original signed positive acceptance needs
    # three exact Sylvester minors, no numerical "looks positive".
    m1=L[0][0]
    m2=m1*L[1][1]-L[0][1]**2
    m3=determinant(L)
    positive3=m1>0 and m2>0 and m3>0
    out={
       "status":"SCOPED_ORIGINAL_TRUE_SIGNED_DIFFERENT_CENTER_THIRD_SOURCE_3D_ACCEPTANCE",
       "canonical_W_ODD_NEG":"OPEN",
       "actual_original_source_indices":list(IX),
       "actual_original_source_dimension":25,
       "sine1_center_differs_from_sine2_xcos17":True,
       "original_physical_three_source_Gram_strict_SPD":True,
       "original_disjoint_new_signed_positive_windows":338,
       **windowstats,**cs,**ns,**ps,
       "original_true_sinh_exceptional_pole_upper_paid":True,
       "original_3source_pole_upper_error":str(pfee),
       "entire_original_signed_3x3_LOEWNer_lower":[[str(x) for x in row] for row in L],
       "full_original_signed_3source_LOEWNer_export_fee":str(rounding),
       "full_original_signed_3source_exact_sylvester_minors":[str(x) for x in (m1,m2,m3)],
       "full_original_signed_3source_lower_positive_definite_certified":positive3,
       "original_actual_true_signed_third_positive_plane_dimension_certified":3 if positive3 else 2,
       "original_actual_25D_negative_index_upper_if_certified":22 if positive3 else 23,
       "actual_signed_source25_negative_index_EXACTLY_classified":False,
       "entire_infinite_original_odd_negative_index_classified":False,
       "original470_Astar_inverse_and_orthogonal_remainder":False,
       "odd_O1O2_even_Weil_CC27_RH":False,
       "independent_original_fourier_form_domain_premise_audit":"OPEN",
       "interpretation":"Original complete 3source [1,2,17] signed all-real integral/pole matrix, with heterogeneous physical sine centers and 338 rigorous new disjoint positive windows. Actual 25D index<=22 ONLY if this full 3x3 lower is PD. A negative lower pivot is not an actual negative witness."
    }
    target=ROOT/a.output;target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps(out,indent=2)+"\n")
    print("SM63 true original direct 3source signed third-plane test:",json.dumps({
       "source_indices":list(IX),
       "new_signed_windows":338,
       "leading_lower_minors":[float(x) for x in (m1,m2,m3)],
       "strict_three_source_signed_positive":positive3,
       "actual_source25_index_ceiling":22 if positive3 else 23,
       "full_original_odd_Weil_RH":"OPEN"
    }),flush=True)

if __name__=="__main__":main()
