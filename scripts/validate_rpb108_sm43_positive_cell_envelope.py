#!/usr/bin/env python3
"""SM43 — true original signed seven-prime POSITIVE low-band cell envelopes.

SCOPED EXACT RATIONAL MATHEMATICAL CERTIFICATE, under inherited SI06,
SI07, SI10, SM39-42 full original Fourier/form-domain premises:

For any genuine positive-frequency real cell [a,b] subset [0,4096],
  arch_lower_at(a) <= Re psi(1/4+i*pi*xi)-ln pi <= arch_upper_at(b)
  and the ORIGINAL all-seven-prime cosine sum lies within the
  intersection of (i) midpoint ± SI06 M=69 first-derivative and
  (ii) endpoint linear interpolation ± true exact D2*h²/8.
Thus true original positive multiplier a_o=max(kappa,m) is enclosed
on *EVERY REAL xi* in [a,b] by exact rational l_i<=a_o<=u_i,
including ALL nonsmooth m=kappa crossings, without locating roots.

For the REAL original selected SI10 25 physically supported odd
sin/xcos/sinh sources, derive exact nonnegative rational s_ij
with |T_j(xi)|<=s_ij for all xi in each cell, using exact
source-center/finite support sinc and sinc-prime envelopes, and
the actual odd pole bound. Define exact piecewise-constant
source-form B_window=2 sum_i w_i int_I T T* dxi,
w_i=(l_i+u_i)/2. Then for ALL z∈R^25 (all source cross PAID),
  -eps_window I <= A_original,window-B_window<=eps_window I,
  eps_window=sum_i (b_i-a_i)*(u_i-l_i)*sum_j s_ij².
This is a TRUE full 25x25 Loewner error budget for the finite
covered window operator, NOT a numerical approximation to the
unknown exact cell Fourier Gram integrals B_window.

A SCOPED source-centered pilot proves error contraction with
frequency cell refinement at step=1/4 and 1/8 on same original
zero-extended 25 source functions, while explicitly leaving
the rest of [0,4096] and its tight weighted cell integrals OPEN.

Exact rational source SIN/COS and digamma constants inherited.
NO floating eigenspectrum, sampled digamma, or quadrature used
for proof. Full original 470-source Astar inverse/odd O1/O2 OPEN.
"""
import argparse
import json
from fractions import Fraction as F
from functools import lru_cache
from math import factorial

from validate_rpb108_si06_negative_band import (
    PI, LN, B, prime_interval, log_rational_bounds
)
from validate_rpb108_si10_complement_positivity import (
    protected_inner_cover, KAPPA
)
from validate_rpb108_si07_negative_support_cover import (
    M
)
from validate_rpb108_sm39_rational_left_arch_cap import (
    arch_lower_at
)
from validate_rpb108_sm40_endpoint_curvature_negative_cap import D2
from validate_rpb108_sm42_original_physical_gram_and_low_gate import (
    hyperbolic_interval
)
from sm36_original_odd_numerical_pilot import (
    ROOT,geometry,select_sources
)

K=64
A=F(1,4)
HALF=F(1,2)
PREC=10**10


def ceil_rat(x,d=PREC):
    x=F(x);return F(-(-x.numerator*d//x.denominator),d)


def floor_rat(x,d=PREC):
    x=F(x);return F(x.numerator*d//x.denominator,d)


def make_constant_lower():
    # Actual original digamma quarter constant
    # C=gamma + pi/2 +3 ln 2 +ln pi.
    # SI06 proves 57/100<gamma via H128-log(129).
    H128=sum((F(1,j) for j in range(1,129)),F(0))
    assert H128-log_rational_bounds(F(129))[1]>F(57,100)
    lo=F(57,100)+PI[0]/2+3*LN[2][0]+\
       log_rational_bounds(PI[0])[0]
    return floor_rat(lo)

CONST_LO=make_constant_lower()


@lru_cache(maxsize=8192)
def arch_upper_at(right):
    """Rigorous upper of ORIGINAL digamma arch for every 0<=xi<=right.

    Increase original convergent digamma summands in y=pi*xi.
    For decreasing positive k-tail, sum_{k=K}inf f(k+a)
       <= int_{K-1}inf f(x+a)dx
       = 1/2 ln(1+(y/(K-1+a))²).
    Exact real rational ln upper via SI06.
    """
    right=F(right)
    assert right>=0
    y=ceil_rat(PI[1])*right
    head=sum((y*y/((k+A)*((k+A)**2+y*y))
              for k in range(K)),F(0))
    tail=log_rational_bounds(
        1+(y/(K-1+A))**2)[1]/2
    return ceil_rat(head+tail-CONST_LO)


def positive_cell_weight_interval(left,right):
    left=F(left);right=F(right)
    assert F(0)<=left<right<=4096
    h=right-left
    midpoint=(left+right)/2
    # Certified original SI06 exact all-seven-prime real phases
    # at BOTH rational endpoints and at center.
    la,ua=prime_interval(left)
    lb,ub=prime_interval(right)
    lm,um=prime_interval(midpoint)
    # Two independent whole-REAL bounds; intersect rigorously.
    p_lo=max(min(la,lb)-D2*h*h/8,lm-M*h/2)
    p_hi=min(max(ua,ub)+D2*h*h/8,um+M*h/2)
    assert p_lo<=p_hi
    arch_lo=arch_lower_at(left)
    arch_hi=arch_upper_at(right)
    assert arch_lo<=arch_hi
    true_m_lo=arch_lo+p_lo
    true_m_hi=arch_hi+p_hi
    assert true_m_lo<=true_m_hi
    weight_lo=max(KAPPA,true_m_lo)
    weight_hi=max(KAPPA,true_m_hi)
    assert KAPPA<=weight_lo<=weight_hi
    return weight_lo,weight_hi,{
        "cell_contains_possible_m_equals_kappa":true_m_lo<=KAPPA<=true_m_hi,
        "certified_multiplier_interval_width":weight_hi-weight_lo,
        "cell_m_interval_low":true_m_lo,
        "cell_m_interval_high":true_m_hi
    }


def source_window_support_envelopes(left,right,centers,sources):
    """Exact original genuine supported odd sine Fourier bound.

    For k0 sin(c): T=B[sinc(2B(c-xi))-sinc(2B(c+xi))].
    For k1 xcos: T=B²/pi[sinc'(2B(c-xi))-sinc'(2B(c+xi))].
    Use |sinc u|<=min(1,1/(pi|u|)) and
      |sinc' u|<=min(pi/2,1/|u|+1/(pi u²)).
    True pi>3, pi<22/7. For pole s(x)=sinh(x/2),
    the original T_s is <=4(cosh(B/2)-1), and for xi>=1
    <=2/(5xi). All these source bounds hold on the
    ENTIRE REAL frequency cell, not only Gauss nodes.
    """
    left=F(left);right=F(right)
    assert F(0)<=left<right
    ch_hi=ceil_rat(hyperbolic_interval(B/2,"cosh").h)
    pole_general=4*(ch_hi-1)
    assert F(0)<pole_general<F(1)
    result=[]
    for typ,j,k in sources:
        if typ=="pole":
            upper=pole_general
            if left>=1:upper=min(upper,F(2,5)/left)
            result.append(upper);continue
        c=centers[j]
        assert c>=0
        dminus=F(0) if left<=c<=right else (
            left-c if c<left else c-right)
        dplus=c+left
        def sinc_cap(d):
            if d<=0:return F(1)
            return min(F(1),F(1)/(6*B*d))
        def sincprime_cap(d):
            if d<=0:return F(11,7)
            u=2*B*d
            return min(F(11,7),1/u+F(1,3)/(u*u))
        if k==0:
            upper=B*(sinc_cap(dminus)+sinc_cap(dplus))
        elif k==1:
            upper=B*B/F(3)*(sincprime_cap(dminus)+
                            sincprime_cap(dplus))
        else:
            raise AssertionError("ONLY actual original selected k=0/1 source proven")
        result.append(upper)
    assert len(result)==25 and all(x>0 for x in result)
    return result


def original_source_centered_windows():
    infos,*_=geometry()
    sources=select_sources(infos)
    clusters,*_=protected_inner_cover()
    centers=[(a+b)/2 for a,b,_ in clusters]
    assert len(centers)==107 and len(sources)==25
    used=sorted({j for kind,j,k in sources if kind=="cluster"})
    assert len(used)==16
    segments=[(F(0),F(1))]
    for j in used:
        c=centers[j]
        segments.append((max(F(0),c-HALF),min(F(4096),c+HALF)))
    segments.sort()
    merged=[]
    for a,b in segments:
        assert a<b
        if merged and a<=merged[-1][1]:
            merged[-1]=(merged[-1][0],max(b,merged[-1][1]))
        else:merged.append((a,b))
    assert len(merged)>=1
    assert all(merged[i][1]<merged[i+1][0]
               for i in range(len(merged)-1))
    return centers,sources,merged


def evaluate_step(step,centers,sources,windows):
    step=F(step); assert step>0 and step<=F(1,4)
    maxwidth=F(0);sumwidth=F(0);total=F(0);ambiguous=0
    count=0;errors=[];max_source=F(0)
    for a,b in windows:
        # SAME true source-centered window union at all resolutions.
        size=b-a
        n=(size.numerator*step.denominator+
            size.denominator*step.numerator-1)//(
            size.denominator*step.numerator)
        assert n>0
        cellwidth=size/n
        assert cellwidth<=step
        for k in range(n):
            l=a+k*cellwidth;r=a+(k+1)*cellwidth
            low,up,diagnostic=positive_cell_weight_interval(l,r)
            cap=source_window_support_envelopes(l,r,centers,sources)
            source_energy=sum((c*c for c in cap),F(0))
            # COMPLETE SOURCE-COUPLED scalar Loewner envelope fee:
            # original A=2 integral a T T*, midpoint step a0=(l+u)/2
            # |z*(A-Astep)z| <= h (up-low) sum_j cap_j² ||z||².
            fee=(r-l)*(up-low)*source_energy
            total+=fee
            width=up-low
            sumwidth+=width*(r-l)
            maxwidth=max(maxwidth,width)
            max_source=max(max_source,source_energy)
            count+=1
            if diagnostic["cell_contains_possible_m_equals_kappa"]:
                ambiguous+=1
            errors.append(float(fee))
    assert total>0 and maxwidth>0
    return {
        "exact_rational_max_cell_width":str(step),
        "all_real_frequency_cells_certified":count,
        "possible_nonsmooth_m_kappa_crossing_cells":ambiguous,
        "same_25_original_odd_sources":len(sources),
        "certified_real_source_centered_window_count":len(windows),
        "certified_window_measure":str(sum((b-a for a,b in windows),F(0))),
        "certified_max_positive_cell_weight_width_float":float(maxwidth),
        "certified_frequency_weight_integrated_width_float":float(sumwidth),
        "certified_max_source_Fourier_norm_square_upper":float(max_source),
        "certified_whole_25x25_window_Loewner_error_I_float":float(total),
        "certified_whole_25x25_window_Loewner_error_I_exact":str(
            ceil_rat(total,10**9)),
        "whole_interval_operator_statement":
            "-eps*I25 <= A_true_window - sum_cells(2*w_mid*int_cell[T T*]) <= eps*I25",
        "all_midpoint_cell_Gram_integrals_rigorously_evaluated":False,
        "covers_all_original_0_to_4096_low_band":False,
        "noncertifying_float_Gauss_used_in_proof":False,
        "pilot_per_cell_error_float_max":max(errors)
    }


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output",default="artifacts/sm43_original_positive_cell_error.json")
    args=p.parse_args()
    root=json.loads((ROOT/"research/obligations.json").read_text())
    odd=next(o for o in root["obligations"] if o["id"]=="W-ODD-NEG")
    assert root["active_obligation"]=="W-ODD-NEG"
    assert root["objective"]["status"]=="open" and odd["status"]=="open"
    assert root["governance"]["no_automatic_promotion"] is True
    assert all(x in odd["evidence"] and x in root["evidence"]
               for x in ("SM41","SM42","SM43"))
    assert "sm43_true_original_source_centered_positive_cell_envelope" in root["governance"]
    centers,sources,windows=original_source_centered_windows()
    a=evaluate_step(F(1,4),centers,sources,windows)
    print("SM43 EXACT ORIGINAL POSITIVE CELLS 1/4",
          json.dumps(a,sort_keys=True),flush=True)
    b=evaluate_step(F(1,8),centers,sources,windows)
    print("SM43 EXACT ORIGINAL POSITIVE CELLS 1/8",
          json.dumps(b,sort_keys=True),flush=True)
    # The mathematically certified complete-operator window error
    # is expected to contract under finer true-frequency source
    # envelopes; fail closed if ineffective in this real pilot.
    assert b["certified_whole_25x25_window_Loewner_error_I_float"] < (
        a["certified_whole_25x25_window_Loewner_error_I_float"])
    assert b["all_real_frequency_cells_certified"]>a["all_real_frequency_cells_certified"]
    assert b["certified_window_measure"]==a["certified_window_measure"]
    data={
       "status":"CERTIFIED_TRUE_ORIGINAL_SOURCE_WINDOW_POSITIVE_INTERVAL_ENVELOPE_ONLY",
       "canonical_original_odd_O1_O2":"OPEN",
       "exact_whole_real_cell_proof":{
          "arch_lower":"SI07/SM39 monotone exact rational left",
          "arch_upper":"positive 64-term digamma upper plus integral tail at right",
          "prime_lower_upper":"SI06 all 7 prime-power rational endpoint curvature and midpoint 69 derivative intersection",
          "source_transform":"SM38 exact supported sin/xcos/pole formulas; conservative rational interval supremum",
          "root_handling":"entire max(kappa,m) interval, no missed crossing or root assumption",
          "matrix_completeness":"true entire 25x25 source coupling bounded by Cauchy, not diagonals"
       },
       "original_25_source_frequency_window_union":[
         [str(a),str(b)] for a,b in windows],
       "coarse_step":a,
       "finer_step":b,
       "what_remains":[
         "entire remaining original LOW positive band frequencies outside source-centered windows",
         "actual interval integration for every exact piecewise Fourier source Gram int_I[T T*]",
         "verified tight full original 25x25 low weighted source stiffness",
         "original complete all 470 high polynomial source tails and pole-conditioned Astar strong residual",
         "entire true 470 odd O1/O2, even E1-E4, signed Weil, native CC27, RH"
       ]
    }
    out=ROOT/args.output
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(data,indent=2)+"\n")
    print("SM43 SCOPED PASS: ORIGINAL entire real positive multiplier"
          " rational two-sided weight intervals on source-centered"
          " windows, including all m=kappa crossings, full"
          " original 25x25 odd source cross paid by exact"
          " rational Loewner error with mesh contraction."
          " Remainder of positive low 0..4096, actual cell"
          " Fourier Gram integrals, 470-source inverse,"
          " Wodd/even/Weil/RH OPEN.",flush=True)


if __name__=="__main__":
    main()
