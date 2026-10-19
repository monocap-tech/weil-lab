#!/usr/bin/env python3
"""SM44: ORIGINAL selected 25 odd-source TRUE weighted Fourier CELL Gram.

CERTIFIED, SCOPED, conditional on inherited SI06/SM38/SM42-43
original Fourier/closed-form domain identification:
 On the SAME source-centered positive-frequency windows W of total
 measure 1029/64, with 25 genuine original zero-extended physically
 supported sin/xcos/sinh odd sources, rigorously compute a whole
 real, full-coupled 25x25 RATIONAL matrix proxy P_W to the TRUE
 ORIGINAL positive low-frequency source stiffness A_{o,W}.

 * SM43A per-cell exact original signed seven-prime/digamma
   positive multiplier approximation chooses either certified
   constant weight or max(kappa, rational affine signed m). The
   affine kink integral is performed EXACTLY in Fraction arithmetic.
 * At rational midpoint of each cell, the GENUINE physical supported
   Fourier sine transform T_j is ENCLOSED by the independently
   certified SM42 exact rational physical sin/sin, xcos and sinh
   Fourier transforms (never FFT or sampled trig).
 * Source-dependent rational frequency Lipschitz bounds L_j from
   2*pi ∫ |x g_j(x)| dx apply on the ENTIRE original true frequency
   cell. Midpoint Fourier interval radius plus L_j*h/2 rigorously
   encloses |T_j(xi)-v_j|, with rational-rounded v_j.
 * FULL 25x25 source matrix bound:
     ||T T^T-v v^T||_op <=2 sqrt(E2 S2)+E2
   with exact rational certified outward sqrt, where
   E2=sum_j (midpoint_interval_error+Lj*h/2)^2 and
   S2=sum_j (whole_cell_original_Fourier_sup_j)^2.
   Weight integral J=∫ max(kappa, q_cell) is exact rational,
   and rounding J→Jq is separately paid.
 * A_W-P_W is bounded on EVERY coupled original coefficient vector:
    -eps_total I25 <= A_original,W-P_W <=eps_total I25.
   epsilon_total=SM43A exact weight error + NEW exact
   Fourier-cell Gram integration proxy error.
 * Two mesh widths 1/4,1/8; full P_W is a genuine 25x25
   rational matrix with ALL source cross terms. Contraction of
   integration error is required.

DOES NOT cover full original low positive 0..4096 outside W,
nor 470-source high degree polynomial Fourier tails, true original
Astar inverse, entire O1/O2 odd/even, whole Weil, CC27 or RH.
"""
import json
import argparse
from fractions import Fraction as F
from math import isqrt

from validate_rpb108_si06_negative_band import PI,B,prime_interval
from validate_rpb108_si10_complement_positivity import KAPPA
from validate_rpb108_sm42_original_physical_gram_and_low_gate import (
    F0,F1,pole_sin,hyperbolic_interval
)
from validate_rpb108_sm39_rational_left_arch_cap import arch_lower_at
from validate_rpb108_sm43_positive_cell_envelope import (
    ROOT,original_source_centered_windows,
    source_window_support_envelopes,positive_cell_weight_interval,
    arch_upper_at,ceil_rat
)
from validate_rpb108_sm43_positive_affine_error import affine_cell_error

Q=10**8

def quantize(x):
    """Nearest fixed-denominator rational, all error paid separately."""
    x=F(x)
    y=x*Q+F(1,2)
    return F(y.numerator//y.denominator,Q)

def sqrt_upper(x,den=10**8):
    """Exact rational upper root: no float approximation in proof."""
    x=F(x)
    assert x>=0
    if x==0:return F(0)
    n=(x.numerator*den*den+x.denominator-1)//x.denominator
    k=isqrt(n)+1
    v=F(k,den)
    assert v*v>=x
    return v

def original_exact_physical_fourier_midpoint(xi,centers,sources,pole_hyp):
    """TRUE source transform interval, not a sampled FFT transform."""
    xi=F(xi)
    sh,ch=pole_hyp
    vals=[]
    for typ,j,k in sources:
        if typ=="pole":
            v=pole_sin(xi,sh,ch)
        elif k==0:
            c=centers[j]
            v=(F0(c-xi)-F0(c+xi))/2
        elif k==1:
            c=centers[j]
            v=(F1(xi+c)+F1(xi-c))/2
        else:
            raise AssertionError("Only actual original selected 25 k0/k1 Fourier sources.")
        vq=quantize(v.mid())
        rad=ceil_rat(max(vq-v.l,v.h-vq),10**9)
        assert rad>=0 and v.l>=vq-rad and v.h<=vq+rad
        vals.append((vq,rad))
    assert len(vals)==25
    return vals

def original_physical_source_lipschitz(sources):
    """Complete TRUE real-frequency original Fourier source derivative.

    |d/dxi T_g| <=2*pi∫|x*g(x)|dx.
    sin: integral |x| <=B².
    x*cos: integral x² <=2B³/3.
    sinh pole: |sinh(x/2)|<1 on [-B,B] <=B².
    """
    res=[]
    for typ,j,k in sources:
        if typ=="pole" or k==0:
            L=2*PI[1]*B*B
        elif k==1:
            L=F(4,3)*PI[1]*B**3
        else:
            raise AssertionError("unhandled source degree")
        res.append(L)
    return res

def affine_positive_weight_mean(va,vb):
    """Exact rational ∫_0^1 max(kappa,va+(vb-va)t) dt."""
    va=F(va);vb=F(vb)
    if va>=KAPPA and vb>=KAPPA:return (va+vb)/2
    if va<=KAPPA and vb<=KAPPA:return KAPPA
    assert va!=vb
    t=(KAPPA-va)/(vb-va)
    assert F(0)<=t<=F(1)
    if va<KAPPA<vb:
        return KAPPA*t+(KAPPA+vb)*(1-t)/2
    if vb<KAPPA<va:
        return (va+KAPPA)*t/2+KAPPA*(1-t)
    raise AssertionError("unexpected end equality")
    
def actual_original_hybrid_weight_integral(a,b,meta):
    h=b-a
    if meta["reference_choice"]=="original_constant_cell":
        lo,hi,_=positive_cell_weight_interval(a,b)
        mass=h*(lo+hi)/2
    else:
        mla=arch_lower_at(a)+prime_interval(a)[0]
        mua=arch_upper_at(a)+prime_interval(a)[1]
        mlb=arch_lower_at(b)+prime_interval(b)[0]
        mub=arch_upper_at(b)+prime_interval(b)[1]
        qa=(mla+mua)/2
        qb=(mlb+mub)/2
        mass=h*affine_positive_weight_mean(qa,qb)
    assert mass>0
    return mass

def partition(windows,step):
    for aa,bb in windows:
        size=bb-aa
        n=(size.numerator*step.denominator+
           size.denominator*step.numerator-1)//(
           size.denominator*step.numerator)
        assert n>0 and size/F(n)<=step
        for i in range(n):
            yield aa+F(i,n)*size,aa+F(i+1,n)*size

def compute(step,centers,sources,windows):
    n=len(sources)
    gram=[[F(0) for _ in range(n)] for _ in range(n)]
    lips=original_physical_source_lipschitz(sources)
    sh=hyperbolic_interval(B/2,"sinh")
    ch=hyperbolic_interval(B/2,"cosh")
    true_weight_error=F(0)
    cell_gram_error=F(0)
    ncell=0
    choices={"original_constant_cell":0,"signed_positive_part_affine":0}
    maxmidrad=F(0)
    maxfrequencyhalfstep=F(0)
    for a,b in partition(windows,step):
        ncell+=1;h=b-a
        assert 0<=a<b<=4096
        werr,meta=affine_cell_error(a,b,centers,sources)
        true_weight_error+=werr
        choices[meta["reference_choice"]]+=1
        mass=actual_original_hybrid_weight_integral(a,b,meta)
        massq=quantize(mass)
        massround=abs(mass-massq)
        midpoint=(a+b)/2
        point=original_exact_physical_fourier_midpoint(
            midpoint,centers,sources,(sh,ch))
        sup=source_window_support_envelopes(a,b,centers,sources)
        E=[rad+L*h/2 for (v,rad),L in zip(point,lips)]
        e2=sum((x*x for x in E),F(0))
        s2=sum((x*x for x in sup),F(0))
        mids=[v for v,rad in point]
        v2=sum((v*v for v in mids),F(0))
        for (v,rad),cap in zip(point,sup):
            # Midpoint interval is inside the true entire cell;
            # cap is an upper of true original |T| on this cell.
            assert abs(v)<=cap+rad
            maxmidrad=max(maxmidrad,rad)
        maxfrequencyhalfstep=max(maxfrequencyhalfstep,h/2)
        # Entire coupled 25x25 rank-one proxy operator error,
        # including ALL offdiag entries, via exact Cauchy:
        # |TT^t-vv^t| <= ||T-v|| (||T||+||v||)
        # <=2 sqrt(e2*s2)+e2.
        # 2∫ w(...) difference pays both Fourier halves.
        root=sqrt_upper(e2*s2)
        err=2*mass*(2*root+e2)+2*massround*v2
        assert err>=0
        cell_gram_error+=err
        coeff=2*massq
        for i in range(n):
            for j in range(i,n):
                gram[i][j]+=coeff*mids[i]*mids[j]
    for i in range(n):
        for j in range(i):
            gram[i][j]=gram[j][i]
    assert ncell>0 and n==25
    eps=true_weight_error+cell_gram_error
    assert eps>0
    diag=[gram[i][i] for i in range(n)]
    # Complete original source Gram/multiplier matrix is real
    # symmetric and all entries from exact Fraction expressions.
    assert all(di>=0 for di in diag)
    assert all(gram[i][j]==gram[j][i] for i in range(n) for j in range(n))
    return {
        "max_frequency_cell_width":str(step),
        "true_original_source_count":25,
        "actual_true_source_window_measure":str(sum((b-a for a,b in windows),F(0))),
        "real_frequency_cells":ncell,
        "whole_original_cell_reference_types":choices,
        "exact_full_matrix_proxy_entries_rational":True,
        "original_true_weight_interpolation_Loewner_eps_outward":
            str(ceil_rat(true_weight_error,10**9)),
        "new_true_physical_Fourier_cell_Gram_Loewner_eps_outward":
            str(ceil_rat(cell_gram_error,10**9)),
        "total_true_original_weighted_source_window_stiffness_Loewner_eps_outward":
            str(ceil_rat(eps,10**9)),
        "true_weight_error_float":float(true_weight_error),
        "true_cell_gram_error_float":float(cell_gram_error),
        "total_error_float":float(eps),
        "max_true_midpoint_Fourier_source_interval_radius_float":float(maxmidrad),
        "max_true_frequency_halfwidth_float":float(maxfrequencyhalfstep),
        "rational_matrix_max_diagonal_float":float(max(diag)),
        "rational_matrix_min_diagonal_float":float(min(diag)),
        "exact_rational_complete_25x25_proxy_matrix":
            [[str(x) for x in row] for row in gram],
        "covers_all_original_low_0_to_4096":False,
        "certifies_true_original_Astar_inverse":False,
        "certifies_original_complete_odd_O1_O2":False
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output",default="artifacts/sm44_original_physical_fourier_cell_gram.json")
    args=p.parse_args()
    root=json.loads((ROOT/"research/obligations.json").read_text())
    odd=next(v for v in root["obligations"] if v["id"]=="W-ODD-NEG")
    assert root["active_obligation"]=="W-ODD-NEG"
    assert root["objective"]["status"]=="open" and odd["status"]=="open"
    assert root["governance"]["no_automatic_promotion"] is True
    assert "SM44" in odd["evidence"] and "SM44" in root["evidence"]
    assert "sm44_true_original_fourier_cell_gram" in root["governance"]
    centers,sources,windows=original_source_centered_windows()
    coarse=compute(F(1,4),centers,sources,windows)
    print("SM44 TRUE ORIGINAL full physical Fourier 25 source"
          " cell Gram 1/4",json.dumps({k:v for k,v in coarse.items()
            if k!="exact_rational_complete_25x25_proxy_matrix"},sort_keys=True),flush=True)
    fine=compute(F(1,8),centers,sources,windows)
    print("SM44 TRUE ORIGINAL full physical Fourier 25 source"
          " cell Gram 1/8",json.dumps({k:v for k,v in fine.items()
            if k!="exact_rational_complete_25x25_proxy_matrix"},sort_keys=True),flush=True)
    assert fine["actual_true_source_window_measure"]==coarse["actual_true_source_window_measure"]
    assert fine["real_frequency_cells"]>coarse["real_frequency_cells"]
    assert fine["true_cell_gram_error_float"]<coarse["true_cell_gram_error_float"],(
        "SM44 original Fourier-cell integration error did not contract")
    assert fine["true_weight_error_float"]<coarse["true_weight_error_float"]
    assert fine["total_error_float"]<coarse["total_error_float"]
    result={
        "status":"CERTIFIED_SELECTED_ORIGINAL_POSITIVE_SOURCE_WINDOW_FULL_25x25_RATIONAL_PROXY_WITH_ERROR",
        "canonical_original_odd_O1_O2":"OPEN",
        "proof_scope":"SOURCE_CENTERED_WINDOWS_ONLY_NOT_ENTIRE_POSITIVE_LOW_0_TO_4096",
        "true_original_supported_source_types":"16 sin(k0),8 xcos(k1),1 sinh(x/2) odd pole",
        "fully_certified_operator_statement":"-eps_total I25 <= true original Ao source positive frequency windows - EXACT rational full 25x25 proxy matrix <=eps_total I25",
        "coarse_mesh":{k:v for k,v in coarse.items()
                       if k!="exact_rational_complete_25x25_proxy_matrix"},
        "fine_mesh":fine,
        "remaining":[
            "full true original positive low 0..4096 outside selected windows",
            "sharper source-conditioned/interval matrix tails, this source-coordinate scalar error is conservative",
            "complete actual original 470 degree-k sources, correct high log positive tail and strong residual",
            "full original Astar pole-conditioned resolvent and all-470 N<=51/56 G or exact Schur",
            "canonical odd W-ODD-NEG O1/O2, even E1-E4, signed Weil CC27 and RH",
            "independent original Fourier and closed-form domain analytic audit"
        ]
    }
    dest=ROOT/args.output;dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(result,indent=2)+"\n")
    print("SM44 SCOPED CERTIFICATE: original true 25x25 positive"
          " source WINDOW stiffness now approximated by COMPLETE"
          " explicit RATIONAL matrix with outward whole-matrix"
          " Loewner error paying exact scalar original weighted"
          " interpolation, all true physical source Fourier"
          " cell integration error and every cross. Rest of"
          " original low, 470 inverse and Weil/RH OPEN.",flush=True)

if __name__=="__main__":
    main()
