#!/usr/bin/env python3
"""SM53: true original coupled odd three-source signed lower including pole input, no local->global promotion.

Extend SM51/SM52 to actual original supported SI10 sine, its
same-center xcos, and the original sinh(x/2) input pole SOURCE. ALL four signed entries and true exceptional sinh
pole cross included. Original source pair is drawn from the actual
25 physical SI10 source list, never independent surrogate packets.

Core [13,16], 768 exact original whole-real frequency cells:
  m(ξ)>=mlo_I using SM39 rational arch left and SI06 original full
  seven-prime midpoint/endpoint+SM40 true global curvature.
  For mlo>=0, Jensen source-frequency MEAN gives 2h*mlo*u u^T,
    and original physical midpoint/local T'' controls full 3x3
    rational lower -eps I.
  For mlo<0, original Fourier affine moment matrix plus global
    Loewner upper norm error gives legitimate signed LOWER.
Outside core all original 973 SI10 negative leaves / 3892 signed
SM39 subcells are paid as a complete NEGATIVE upper matrix using
original true Fourier source affine and full Loewner remainder.
Disjoint 17 SM12+32 SM49 true positive bands outside core earn
source-Jensen matrix lower, and actual signed sinh pole rank-one
has separately certified full 3x3 physical Gram upper.

The final L52 <= ACTUAL original signed Wodd restricted to this
THREE-dimensional original supported physical source span.
Only an exact rational positive determinant plus positive diagonal
could certify 3D PD. A failed PSD test does NOT assert actual
negative index or signed Weil counterexample.
"""
import argparse,json
from fractions import Fraction as F
from validate_rpb108_si06_negative_band import B,PI,prime_interval
from validate_rpb108_si07_negative_support_cover import M
from validate_rpb108_si10_complement_positivity import KAPPA
from validate_rpb108_sm10_explicit_odd_cap_moments import full_upper_leaves
from validate_rpb108_sm39_rational_left_arch_cap import arch_lower_at
from validate_rpb108_sm40_endpoint_curvature_negative_cap import D2
from validate_rpb108_sm42_original_physical_gram_and_low_gate import (
    I,F0,F1,F2,pole_sin,pole_xcos,hyperbolic_interval,
    original_full_25_physical_interval_gram)
from validate_rpb108_sm46_affine_physical_fourier_source import (
    original_F3,original_third_spatial_moment)
from validate_rpb108_sm43_positive_cell_envelope import (
    ROOT,original_source_centered_windows,ceil_rat,floor_rat)
from validate_rpb108_sm44_physical_fourier_cell_gram import (
    quantize,sqrt_upper,original_full_second_derivative_upper)
from validate_rpb108_sm12_positive_reference_33 import (
    CENTERS as OLD_POS,RADIUS as OLD_R)
from validate_rpb108_sm49_adaptive_positive_jensen import (
    original_adaptive_candidate_cells)

A=F(13);Bcore=F(16);NCORE=768
DEN=10**12
def up(x):return ceil_rat(x,DEN)
def down(x):return floor_rat(x,DEN)
def zero():return [[F(0)]*3 for _ in range(3)]
def accumulate(a,b,coef):
    for i in range(3):
        for j in range(3):a[i][j]+=coef*b[i][j]
def diagonal(a,coef):
    for i in range(3):a[i][i]+=coef
def outer(v):return [[v[i]*v[j] for j in range(3)] for i in range(3)]
def mat_affine(v,d,r):
    return [[v[i]*v[j]+d[i]*d[j]*r*r/3 for j in range(3)] for i in range(3)]

def pair_source(centers,sources):
    assert len(sources)==25 and sources[2][0]=="cluster" and sources[2][2]==0
    j=sources[2][1]
    partners=[k for k,z in enumerate(sources) if z[0]=="cluster" and z[1]==j and z[2]==1]
    assert len(partners)==1,("Genuine original same-center supported xcos partner absent",partners)
    indices=(2,partners[0],24)
    assert centers[j]==F(1845,128) and sources[24][0]=="pole"
    return indices,centers[j]

def pair_cell(centers,sources,indices,l,r):
    assert l<r
    mid=(l+r)/2;h=(r-l)/2
    pi=I(PI[0],PI[1]); qs=[];ds=[];errs=[];mean_err=[]
    local=0
    globalKs=original_full_second_derivative_upper(sources)
    third=original_third_spatial_moment(sources)
    c=centers[sources[indices[0]][1]]
    sh=hyperbolic_interval(B/2,'sinh')
    ch=hyperbolic_interval(B/2,'cosh')
    for k in indices:
        typ,j,degree=sources[k]
        assert typ=="cluster" and centers[j]==c
        if typ=='pole':
            val=pole_sin(mid,sh,ch)
            deriv=2*pi*pole_xcos(mid,sh,ch)
            sec=None
        elif degree==0:
            val=(F0(c-mid)-F0(c+mid))/2
            deriv=pi*(F1(c-mid)+F1(c+mid))
            sec=2*pi*pi*(F2(c+mid)-F2(c-mid))
        elif degree==1:
            val=(F1(mid+c)+F1(mid-c))/2
            deriv=pi*(F2(mid+c)+F2(mid-c))
            sec=-2*pi*pi*(original_F3(mid+c)+original_F3(mid-c))
        else:raise AssertionError("unexpected supported degree")
        v=quantize(val.mid());d=quantize(deriv.mid())
        ev=ceil_rat(max(abs(val.l-v),abs(val.h-v)),10**9)
        ed=ceil_rat(max(abs(deriv.l-d),abs(deriv.h-d)),10**9)
        K=globalKs[k] if sec is None else min(globalKs[k],max(abs(sec.l),abs(sec.h))+third[k]*h)
        assert 0<=K<=globalKs[k]
        local+=K<globalKs[k]
        qs.append(v);ds.append(d)
        errs.append(ev+ed*h+K*h*h/2)
        mean_err.append(ev+K*h*h/6)
    # The exact L2 mean of (v+d*t) is vv^T+r² dd^T/3.
    aff=mat_affine(qs,ds,h)
    V2=sum((q*q+dd*dd*h*h/3 for q,dd in zip(qs,ds)),F(0))
    E2=sum((e*e for e in errs),F(0))
    loErr=sum((e*e for e in mean_err),F(0))
    normv=sum((v*v for v in qs),F(0))
    # Rigorous op-norm error to the TRUE integrated source Gram.
    epsA=2*sqrt_upper(V2*E2)+E2
    epsMean=2*sqrt_upper(normv*loErr)+loErr
    assert epsA>=0 and epsMean>=0
    return qs,aff,epsA,epsMean,local

def signed_m_lower(l,r):
    mid=(l+r)/2;arch=arch_lower_at(l)
    midpoint=prime_interval(mid)[0]-M*(r-l)/2
    endpoints=min(prime_interval(l)[0],prime_interval(r)[0])-D2*(r-l)**2/8
    return arch+max(midpoint,endpoints)

def original_complete_negative_outside(centers,sources,indices):
    clusters,W,Mneg,mass=full_upper_leaves()
    parents=[(a,b,h) for c in clusters for a,b,h in c]
    assert len(parents)==973 and len(clusters)==107 and W==F(973,32)
    penalty=zero();n=0;inside=0;outside=0;nonzero=0
    eps_total=F(0);local=0
    for a,b,h in parents:
        parent=h+KAPPA
        for t in range(4):
            l=a+(b-a)*F(t,4);r=a+(b-a)*F(t+1,4)
            n+=1
            assert not(l<A<r or l<Bcore<r)
            if A<=l and r<=Bcore:
                inside+=1
                continue
            outside+=1
            mlo=arch_lower_at(l)+prime_interval((l+r)/2)[0]-M*(r-l)/2
            need=max(F(0),KAPPA-mlo)
            w=min(parent,ceil_rat(need,10**6))
            assert w>=need or w==parent
            if not w:continue
            nonzero+=1
            _,aff,eps,_,loc=pair_cell(centers,sources,indices,l,r)
            local+=loc
            fee=2*(r-l)*w
            accumulate(penalty,aff,fee)
            eps_total+=fee*eps
    assert n==3892 and inside>0 and outside>0 and n==inside+outside
    diagonal(penalty,up(eps_total))
    return penalty,{"original_negative_parent_leaves":973,
                    "original_negative_3892_rational_subcells":3892,
                    "negative_subcells_inside_direct_signed_core":inside,
                    "negative_subcells_outside_direct_core":outside,
                    "outside_true_negative_nonzero_weight_subcells":nonzero,
                    "outside_full_matrix_negative_error_upper":str(up(eps_total)),
                    "outside_source_second_local_improvements":local}

def signed_core(centers,sources,indices):
    step=(Bcore-A)/NCORE;assert step==F(1,256)
    mat=zero();total_eps=F(0);pos=0;neg=0;local=0
    for n in range(NCORE):
        l=A+n*step;r=l+step
        mlo=signed_m_lower(l,r)
        v,aff,epsA,epsMean,loc=pair_cell(centers,sources,indices,l,r)
        local+=loc
        coef=2*step*mlo
        if mlo>=0:
            pos+=1
            accumulate(mat,outer(v),coef)
            total_eps+=coef*epsMean
        else:
            neg+=1
            accumulate(mat,aff,coef)
            total_eps+=(-coef)*epsA
    diagonal(mat,-up(total_eps))
    assert pos+neg==768
    return mat,{"whole_original_signed_core_real_cells":768,
                "original_positive_signed_core_cells":pos,
                "original_negative_signed_core_cells":neg,
                "core_full3x3_Loewner_error_upper":str(up(total_eps)),
                "core_physical_source_second_local_improvements":local}

def true_exterior_positive(centers,sources,indices,chosen):
    bands=[(c-OLD_R,c+OLD_R,F(2),"SM12") for c in OLD_POS]
    bands.extend((x["a"],x["b"],x["delta"],"SM49") for x in chosen)
    bands.sort()
    assert len(bands)==49
    assert all(bands[i][1]<=bands[i+1][0] for i in range(48))
    gains=zero();epsTotal=F(0);outside=0;overlaps=0
    for l,r,delta,label in bands:
        if not (r<=A or l>=Bcore):
            overlaps+=1;continue
        outside+=1
        v,_,_,epsMean,_=pair_cell(centers,sources,indices,l,r)
        coef=2*(r-l)*delta
        accumulate(gains,outer(v),coef)
        epsTotal+=coef*epsMean
    diagonal(gains,-up(epsTotal))
    assert outside+overlaps==49
    return gains,{"true_disjoint_original_SM12_SM49_positive_total":49,
                  "original_exterior_positive_windows_counted":outside,
                  "positive_windows_overlapping_signed_core_discarded":overlaps,
                  "exterior_positive_full3x3_Loewner_error_upper":str(up(epsTotal))}

def true_pole_upper(gram,indices):
    q=[];e=[]
    for k in indices:
        val=gram[k][24]
        v=quantize(val.mid())
        rad=max(abs(v-val.l),abs(v-val.h))
        q.append(v);e.append(rad)
    q2=sum((x*x for x in q),F(0));e2=sum((x*x for x in e),F(0))
    eps=up(2*(2*sqrt_upper(q2*e2)+e2))
    penalty=outer(q)
    penalty=[[2*x for x in row] for row in penalty]
    diagonal(penalty,eps)
    return penalty,eps,q

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output",default="artifacts/sm53_original_direct_signed_3source_pole_matrix.json")
    args=p.parse_args()
    manifest=json.loads((ROOT/"research/obligations.json").read_text())
    odd=next(x for x in manifest["obligations"] if x["id"]=="W-ODD-NEG")
    assert manifest["active_obligation"]=="W-ODD-NEG"
    assert manifest["objective"]["status"]==odd["status"]=="open"
    assert manifest["governance"]["no_automatic_promotion"] is True
    assert "SM52" in odd["evidence"]
    centers,sources,_=original_source_centered_windows()
    ix,center=pair_source(centers,sources)
    H,originalsources,_=original_full_25_physical_interval_gram()
    assert sources==originalsources
    chosen,ncand,_,_=original_adaptive_candidate_cells(centers,sources)
    assert len(chosen)==32
    core,cs=signed_core(centers,sources,ix)
    negative,ns=original_complete_negative_outside(centers,sources,ix)
    positive,ps=true_exterior_positive(centers,sources,ix,chosen)
    pole,poleeps,poleq=true_pole_upper(H,ix)
    final=zero()
    for i in range(3):
        for j in range(3):
            final[i][j]=core[i][j]-negative[i][j]+positive[i][j]-pole[i][j]
    assert final[0][1]==final[1][0]
    minor2=final[0][0]*final[1][1]-final[0][1]**2
    det=(final[0][0]*(final[1][1]*final[2][2]-final[1][2]*final[2][1])
       -final[0][1]*(final[1][0]*final[2][2]-final[1][2]*final[2][0])
       +final[0][2]*(final[1][0]*final[2][1]-final[1][1]*final[2][0]))
    strict_pd=final[0][0]>0 and minor2>0 and det>0
    result={
      "status":"CERTIFIED_SCOPED_ORIGINAL_TRUE_ODD_SIGNED_3SOURCE_LOWER_WITH_POLE_INPUT",
      "canonical_W_ODD_NEG":"OPEN",
      "physical_original_sine_source_index":ix[0],
      "same_original_cluster_xcos_source_index":ix[1],
      "original_input_sinh_pole_source_index":ix[2],
      "common_original_center":str(center),
      "true_original_source_total_carrier_dimension":25,
      **cs,**ns,**ps,
      "original_3x3_true_pole_Loewner_error_upper":str(poleeps),
      "true_original_pole_rational_vector":[str(q) for q in poleq],
      "true_original_restricted_3x3_signed_lower_matrix":[
         [str(down(x)) if i==j else str(x) for j,x in enumerate(row)]
         for i,row in enumerate(final)],
      "exact_original_restricted_3x3_LOEWNER_lower_matrix":[
         [str(x) for x in row] for row in final],
      "source_sine_only_original_signed_lower_from_3x3":str(down(final[0][0])),
      "source_xcos_only_original_signed_lower_from_3x3":str(down(final[1][1])),
      "source_input_pole_only_original_signed_lower_from_3x3":str(down(final[2][2])),
      "signed_original_3x3_exact_rational_determinant":str(det),
      "signed_original_3x3_leading_second_principal_minor":str(minor2),
      "true_original_3x3_signed_positive_definite_certified":strict_pd,
      "full_true_original_25x25_signed_PSD_certified":False,
      "full_original_470source_Astar_inverse_O1O2_even_Weil_CC27_RH_certified":False,
      "independent_fourier_closed_form_domain_audit":"OPEN",
      "interpretation":"All original signed frequency and exceptional pole effects certified on the exact same-center sin/xcos 2D source span. A failed 3x3 LOWER PSD gate is inconclusive about actual signed inertia; independent full 25/470 and odd/even Weil/RH remain open."
    }
    dest=ROOT/args.output;dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(result,indent=2)+"\n")
    print("SM53 original coupled true signed three-source matrix:",json.dumps({
      "indices":list(ix),
      "center":str(center),
      "signed_lower_diag":[float(final[i][i]) for i in range(3)],
      "second_principal_minor":float(minor2),
      "signed_lower_offdiag":float(final[0][1]),
      "lower_determinant":float(det),
      "actual_coupled_3source_PD_certified":strict_pd,
      "source2_sm51_positive_inherited":True,
      "whole_25source_Weil_RH":"OPEN"
    }),flush=True)

if __name__=="__main__":main()
