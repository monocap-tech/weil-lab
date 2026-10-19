#!/usr/bin/env python3
"""MG05: anisotropic full 4D signed Fourier-cell remainder method gate.

Test the original real supported positive three-plane (g1,g2,g17)
independently certified by SM63, together with original xcos source
g22, the largest remaining strictly negative-but-near-zero diagonal
candidate in the complete SM62 source lower. No block splicing or
unsupported cross assumptions: evaluate the complete physical 4x4
original signed Fourier form directly.

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

If and ONLY if all four Sylvester minors of this complete
original signed 4x4 LOWER are strictly positive, the ACTUAL
source 4-plane is PD and original supported source25 negative
index is <=21 (given full25 physical Gram SPD).
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

N=4
IX=(1,2,17,22)
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
    n=len(A)
    assert n>=1 and all(len(row)==n for row in A)
    if n==1:return A[0][0]
    return sum(((-1 if k%2 else 1)*A[0][k]*
        determinant([[A[i][j] for j in range(n) if j!=k]
                      for i in range(1,n)])
        for k in range(n)),F(0))
def leading_minors(A):
    n=len(A)
    return [determinant([row[:k] for row in A[:k]])
            for k in range(1,n+1)]

POLICIES=("scalar","trace","fourth","parent3")

def choose_error(v,d,rad,half,gamma,scalar_error,fees,chosen):
    """Compare two independently valid COMPLETE-4D error enclosures.

    Pointwise Fourier vector T=z+e, z=v+d*t, |t|<=half, |e_i|<=rad_i.
    For a mean estimate set d=0 and rad_i=mean curvature bound.
    Scalar full-matrix error = gamma*scalar_error * I.
    Anisotropic complete Loewner error uses d_ij =
      a_i*r_j+a_j*r_i+r_i*r_j, a_i=|v_i|+|d_i|*half,
      and diag(row_sum(d)). Every offdiagonal is still bounded.
    """
    assert gamma>=0 and scalar_error>=0
    assert len(v)==len(d)==len(rad)==N and all(x>=0 for x in rad)
    a=[abs(v[i])+abs(d[i])*half for i in range(N)]
    sr=sum(rad,F(0));sa=sum(a,F(0))
    directional=[gamma*((a[i]+rad[i])*sr+rad[i]*sa) for i in range(N)]
    scalar=gamma*scalar_error
    for policy in POLICIES:
        if policy=="scalar":
            value=[scalar]*N
        else:
            idx=range(N) if policy=="trace" else ((3,) if policy=="fourth" else range(3))
            use_aniso=sum((directional[i] for i in idx),F(0))<len(tuple(idx))*scalar
            value=directional if use_aniso else [scalar]*N
            if use_aniso: chosen[policy]+=1
        for i in range(N): fees[policy][i]+=value[i]

def empty_fees():
    return {k:[F(0)]*N for k in POLICIES}
def empty_counts():
    return {k:0 for k in POLICIES if k!="scalar"}
def apply_fees(raw,fees):
    return {key:[[raw[i][j]-(up(fee[i]) if i==j else F(0))
                     for j in range(N)] for i in range(N)]
            for key,fee in fees.items()}
def diffmat(A,B):
    return [[A[i][j]-B[i][j] for j in range(N)] for i in range(N)]
def addmat(A,B):
    return [[A[i][j]+B[i][j] for j in range(N)] for i in range(N)]

def compact(A):
    assert all(A[i][j]==A[j][i] for i in range(N) for j in range(N))
    q=[[quantize(A[i][j]) for j in range(N)] for i in range(N)]
    fee=up(max(sum(abs(q[i][j]-A[i][j]) for j in range(N))
               for i in range(N)))
    return [[q[i][j]-(fee if i==j else F(0))
             for j in range(N)] for i in range(N)],fee

class FourierQuartet:
    def __init__(self,centers,sources):
        self.centers,self.sources=centers,sources
        self.pi=I(PI[0],PI[1])
        self.K=original_full_second_derivative_upper(sources)
        self.T3=original_third_spatial_moment(sources)
        assert all(sources[k][0]=="cluster" for k in IX)
        assert sources[1][2]==sources[2][2]==0 and sources[17][2]==sources[22][2]==1
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
        return v,affine(v,d,half),eps_aff,eps_mean,local,er,mean,d

def signed_original_core(calc):
    step=(RIGHT-LEFT)/NCELLS
    assert step==F(1,256)
    raw=zero();fees=empty_fees();chosen=empty_counts()
    positive=negative=local=0
    for i in range(NCELLS):
        a=LEFT+i*step;b=a+step
        m=signed_m_lower(a,b)
        v,A,ea,em,loc,er,mean,d=calc.cell(a,b)
        local+=loc
        weight=2*step*m
        if m>=0:
            accum(raw,outer(v),weight)
            choose_error(v,[F(0)]*N,mean,F(0),weight,em,fees,chosen)
            positive+=1
        else:
            accum(raw,A,weight)
            choose_error(v,d,er,step/2,-weight,ea,fees,chosen)
            negative+=1
    assert positive+negative==768
    return apply_fees(raw,fees),{
       "original_signed_core_cells":768,
       "signed_core_positive":positive,
       "signed_core_negative":negative,
       "core_local_curvature_improvements":local,
       "anisotropic_selected_core":chosen,
       "core_scalar_total_fee":str(up(fees["scalar"][0]))}

def original_true_outside_negative(calc):
    clusters,W,Mneg,mass=full_upper_leaves()
    assert len(clusters)==107 and W==F(973,32)
    leaves=[x for cluster in clusters for x in cluster]
    assert len(leaves)==973
    raw=zero();fees=empty_fees();chosen=empty_counts()
    outside=inside=nonzero=0
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
            v,A,ea,em,loc,er,mean,d=calc.cell(l,r)
            gamma=2*(r-l)*w
            accum(raw,A,gamma)
            choose_error(v,d,er,(r-l)/2,gamma,ea,fees,chosen)
    assert inside+outside==3892
    return apply_fees(raw,fees),{
       "whole_original_negative_parent_leaves":973,
       "original_negative_quartered_cells":3892,
       "negative_subcells_outside_core":outside,
       "negative_nonzero_subcells_outside_core":nonzero,
       "outside_allcross_anisotropic_selected":chosen,
       "outside_scalar_total_fee":str(up(fees["scalar"][0]))}

def positive_outside(calc,centers,sources,extra338):
    old,available,_,_=original_adaptive_candidate_cells(centers,sources)
    assert len(old)==32 and len(OLD_POS)==17
    windows=[(c-OLD_R,c+OLD_R,F(2),"SM12") for c in OLD_POS]
    windows +=[(x["a"],x["b"],x["delta"],"SM49") for x in old]
    for l,r,d,origin in extra338:
        assert d>0
        windows.append((l,r,d+KAPPA,origin))
    windows.sort()
    assert len(windows)==387
    assert all(windows[i][1]<=windows[i+1][0] for i in range(len(windows)-1))
    raw=zero();fees=empty_fees();chosen=empty_counts()
    outside=0
    counts={"SM12":0,"SM49":0,"SM54_96":0,"SM55_242":0}
    for a,b,delta,label in windows:
        if not(b<=LEFT or a>=RIGHT):continue
        outside+=1;counts[label]+=1
        v,aff,ea,em,local,er,mean,d=calc.cell(a,b)
        gamma=2*(b-a)*delta
        accum(raw,outer(v),gamma)
        choose_error(v,[F(0)]*N,mean,F(0),gamma,em,fees,chosen)
    assert counts["SM54_96"]==96 and counts["SM55_242"]==242
    assert outside==sum(counts.values())
    return apply_fees(raw,fees),{
       "total_true_disjoint_real_signed_positive_windows":len(windows),
       "true_positive_real_windows_outside_core":outside,
       "credited_disjoint_positive_by_source":counts,
       "outside_positive_anisotropic_selected":chosen,
       "positive_scalar_total_fee":str(up(fees["scalar"][0]))}

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
    p.add_argument("--output",default="artifacts/mg05_anisotropic_direct_four_source.json")
    a=p.parse_args()
    m=json.loads((ROOT/"research/obligations.json").read_text())
    odd=next(x for x in m["obligations"] if x["id"]=="W-ODD-NEG")
    assert m["active_obligation"]=="W-ODD-NEG"
    assert m["objective"]["status"]==odd["status"]=="open"
    assert m["governance"]["no_automatic_promotion"]
    assert all(x in odd["evidence"] for x in ("SM52","SM53","SM55","SM59","SM62","SM63","SM64"))
    centers,sources,_=original_source_centered_windows()
    assert len(sources)==25 and sources[24][0]=="pole"
    calc=FourierQuartet(centers,sources)
    H,actual,_=original_full_25_physical_interval_gram()
    assert actual==sources
    G=[[H[i][j] for j in IX] for i in IX]
    Gq=[[quantize(x.mid()) for x in row] for row in G]
    gerr=max(sum(max(abs(G[i][j].l-Gq[i][j]),abs(G[i][j].h-Gq[i][j]))
         for j in range(N)) for i in range(N))
    GL=[[Gq[i][j]-(gerr if i==j else F(0)) for j in range(N)] for i in range(N)]
    gram_minors=leading_minors(GL)
    assert len(gram_minors)==4 and all(x>0 for x in gram_minors)
    windows,windowstats=all_338_disjoint_original_signed_positive(centers,sources)
    assert len(windows)==338
    core,cs=signed_original_core(calc)
    negative,ns=original_true_outside_negative(calc)
    positive,ps=positive_outside(calc,centers,sources,windows)
    pole,pfee=pole_upper(H)
    anchor52=json.loads((ROOT/"certificates/rpb108_sm52_original_coupled_source_matrix.json").read_text())
    assert anchor52["source_indices"]==[2,17]
    Aa=[[F(x) for x in row] for row in anchor52["matrix"]]
    assert Aa[0][0]>0 and Aa[0][0]*Aa[1][1]-Aa[0][1]**2>0
    records={}
    for policy in POLICIES:
        matrix=[[core[policy][i][j]-negative[policy][i][j]
                   +positive[policy][i][j]-pole[i][j]
                   for j in range(N)] for i in range(N)]
        L,rounding=compact(matrix)
        minors=leading_minors(L)
        records[policy]={
          "exact_sylvester_minors":[str(x) for x in minors],
          "strict_PD":all(x>0 for x in minors),
          "source4_signed_LOEWNer_lower":[[str(x) for x in row] for row in L],
          "full_outward_rounding_fee":str(rounding),
          "fourth_diagonal":str(L[3][3]),
          "lower_matrix_trace":str(sum((L[i][i] for i in range(N)),F(0)))
        }
    scalar=records["scalar"]
    valid_pd=[key for key in POLICIES if records[key]["strict_PD"]]
    best=max(POLICIES,key=lambda key:(
        int(records[key]["strict_PD"]),
        sum(F(x)>0 for x in records[key]["exact_sylvester_minors"]),
        F(records[key]["exact_sylvester_minors"][-1])))
    assert best in records
    # The scalar certificate is the same original SM64 construction,
    # recomputed here on exactly the same original signed source cells.
    final_pd=bool(valid_pd)
    out={
       "status":"SCOPED_MG05_ANISOTROPIC_COMPLETE_ORIGINAL_FOUR_SOURCE_SIGNED_LOEWNer",
       "canonical_W_ODD_NEG":"OPEN",
       "actual_original_source_indices":list(IX),
       "actual_original_source_dimension":25,
       "original_physical_four_source_Gram_strict_SPD":True,
       "original_disjoint_new_signed_positive_windows":338,
       **windowstats,**cs,**ns,**ps,
       "original_true_sinh_exceptional_pole_upper_paid":True,
       "original_full_source_pole_upper_error":str(pfee),
       "true_signed_original_same_integral_all_policies":True,
       "four_full_source_error_policies":list(POLICIES),
       "policy_records":records,
       "best_policy_by_strict_gate_and_exact_minor_diagnostics":best,
       "any_complete_four_source_lower_strict_PD":final_pd,
       "original_actual_25D_negative_index_ceiling_if_verified":21 if final_pd else 22,
       "inherited_independent_SM63_true_positive_plane_dimension":3,
       "complete_original_25source_negative_index_EXACTLY_classified":False,
       "entire_infinite_original_odd_negative_index_classified":False,
       "original470_Astar_inverse_and_orthogonal_remainder":False,
       "odd_O1O2_even_Weil_CC27_RH":False,
       "independent_original_fourier_form_domain_premise_audit":"OPEN",
       "interpretation":"All four certified true 4D signed Loewner lower matrices share the original physical signed frequency sources and pole; only certified full-matrix cell mean/affine error distribution differs. Strict PD of any one yields actual finite25 index<=21; negative lower pivots are not actual signed modes."
    }
    target=ROOT/a.output;target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps(out,indent=2)+"\n")
    print("MG05 source4 anisotropic method gate:",json.dumps({
       "source_indices":list(IX),
       "strict_four_source_signed_positive":final_pd,
       "policies_with_strict_4D_PD":valid_pd,
       "source4_scalar_fourth_diagonal":float(F(records["scalar"]["fourth_diagonal"])),
       "source4_anisotropic_fourth_diagonal":float(F(records["fourth"]["fourth_diagonal"])),
       "actual_source25_index_ceiling":21 if final_pd else 22,
       "full_original_odd_Weil_RH":"OPEN"
    }),flush=True)

if __name__=="__main__":main()
