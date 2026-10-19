#!/usr/bin/env python3
"""MG11: exact original odd 25-source TWO boundary traces and true 23D kernel.

SM41: a_o(xi)<=17+ln(xi), |xi|>=1. MG10: a single nonzero
boundary trace f(B) yields rank-one 1/xi source covariance.
MG11 proves the second derivative trace f'(B) is independent,
and removes BOTH asymptotic jumps by a whole-source change of basis:
on the exact 23D kernel, T=O(xi^-3), hence the complete strong
a_o action high tail is O((ln Lambda)^2/Lambda^5).

Every endpoint value/derivative uses original SM42 rational Taylor
trigonometry/hyperbolic enclosures and exact SI10 rational source
centers. Source third derivative L1 majorants are rational.
A second whole-25D rank-two-plus-I high-tail Loewner bound pays both
endpoint oscillatory terms AND the remainder. No low-frequency
stiffness, real Galerkin strong residual, complete 470D or RH proof.
"""
import argparse,json,sys
from fractions import Fraction as F

# This validator emits exact, outward-enclosed Fraction numerators and
# denominators. The 23-source coupled kernel can legitimately exceed
# CPython's 4300-digit decimal conversion limit. Preserve the full exact
# integers in the artifact rather than truncating or floating them.
if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)
from validate_rpb108_si06_negative_band import B,PI,LN
from validate_rpb108_si10_complement_positivity import protected_inner_cover
from validate_rpb108_sm42_original_physical_gram_and_low_gate import (
    I,omega,sin_cos_period,hyperbolic_interval)
from validate_rpb108_sm41_original_positive_log_tail import (
    mathematical_global_original_positive_multiplier_majorant,
    odd_pilot_tail_enclosure)
from validate_rpb108_mg10_rank_one_endpoint_source_tail import (
    boundary_intervals,jump_scalar_sharp)
from validate_rpb108_mg09_original_endpoint_tail_budget import (
    source_derivative_constants,dyadic_full_SM41_strong)
from sm36_original_odd_numerical_pilot import ROOT,geometry,select_sources

N=25
POLE=24
POWERS=(11,12,13,16,20,24,30,36,40,48,56)
def abs_up(x):
    return max(abs(x.l),abs(x.h))
def positive_gap(x):
    return min(abs(x.l),abs(x.h)) if x.l*x.h>0 else F(0)
def derivative_intervals_and_D3(sources,clusters):
    derivative=[]; majorant=[]
    sh=hyperbolic_interval(B/2,"sinh")
    for kind,j,degree in sources:
        if kind=="pole":
            assert j==-1
            derivative.append(hyperbolic_interval(B/2,"cosh")/2)
            majorant.append(sh.h) # exactly |f'' endpoints| + int |f'''|=sinh(B/2)
            continue
        c=(clusters[j][0]+clusters[j][1])/2
        sn,cs=sin_cos_period(B*c)
        w=omega(c)
        wup=w.h
        assert w.l>0 and wup>0
        if degree==0:
            derivative.append(w*cs)
            # f'' endpoints abs<=w² each; f''' abs<=w³
            majorant.append(2*wup*wup+2*B*wup**3)
        else:
            assert degree==1
            derivative.append(cs-B*w*sn)
            # xcos: f''=-2w sin -w²*x cos, f'''=-3w² cos+w³*x sin
            majorant.append(4*wup+8*B*wup*wup+2*B*B*wup**3)
    assert len(derivative)==len(majorant)==N
    return derivative,majorant

def derivative_remainder_tail(k,D2):
    """Exact whole-real complete source strong squared tail of xi^-3 remainder."""
    assert k>=11
    v=F(17)+F(k)*F(347,500)
    L=F(2**k)
    return F(2)*D2/F(6**6)/L**5*(v*v/F(5)+2*v/F(25)+F(2,125))

def derivative_jump_weight(k):
    """Whole-real jump1 squared tail, sin²<=1 and 2*pi>6.

    For odd sources J1=-2i sin(2*pi*B*xi) f'(B).
    |-J1/(i*2*pi*xi)^2|<= |d*z|/(2*pi²*xi²).
    Even frequency sides: 2/(4*pi^4)<=1/162.
    """
    assert k>=11
    v=F(17)+F(k)*F(347,500)
    L=F(2**k)
    return (v*v/F(3)+2*v/F(9)+F(2,27))/(F(162)*L**3)

def test_exact_interval_rank():
    # Exact rational determinant with finite interval enclosure.
    b0=I(F(2));b1=I(F(3))
    d0=I(F(5));d1=I(F(7))
    det=b0*d1-b1*d0
    assert det.l==det.h==-1 and positive_gap(det)==1
    return True

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output",default="artifacts/mg11_original_dual_boundary_kernel.json")
    opts=p.parse_args()
    ledger=json.loads((ROOT/"research/obligations.json").read_text())
    odd=next(o for o in ledger["obligations"] if o["id"]=="W-ODD-NEG")
    assert ledger["active_obligation"]=="W-ODD-NEG"
    assert odd["status"]==ledger["objective"]["status"]=="open"
    assert ledger["governance"]["no_automatic_promotion"]
    assert all(x in odd["evidence"] for x in ("SM41","SM42","SI29"))
    assert mathematical_global_original_positive_multiplier_majorant()
    assert LN[2][1]<F(347,500) and PI[0]>3
    assert test_exact_interval_rank()
    clusters,_,_,_,_=protected_inner_cover()
    assert len(clusters)==107
    infos,*_=geometry()
    sources=select_sources(infos)
    assert len(sources)==N and sources[POLE][0]=="pole"
    b=boundary_intervals(sources,clusters)
    d,D3=derivative_intervals_and_D3(sources,clusters)
    assert b[POLE].l>0 and d[POLE].l>0
    candidates=[]
    for q in range(N-1):
        det=b[POLE]*d[q]-b[q]*d[POLE]
        gap=positive_gap(det)
        if gap>0:candidates.append((gap,q,det))
    assert candidates,"MISSING independently certified physical derivative trace"
    gap,pivot,det=max(candidates,key=lambda v:(v[0],-v[1]))
    assert pivot!=POLE and gap>0
    R=tuple(i for i in range(N) if i not in (POLE,pivot))
    assert len(R)==23
    # True analytic coefficients cancelling BOTH boundary traces:
    # a_i=(b_i*d_pivot-b_pivot*d_i)/Delta,
    # c_i=(b_pole*d_i-b_i*d_pole)/Delta,
    # Delta=b_pole*d_pivot-b_pivot*d_pole.
    # Here upper caps use interval absolute numerators and det gap;
    # exact cancellation is a symbolic consequence of the formulas.
    aa=[];cc=[];Dcancel=[]
    for i in R:
        A=(abs_up(b[i])*abs_up(d[pivot])
           +abs_up(b[pivot])*abs_up(d[i]))/gap
        C=(abs_up(b[POLE])*abs_up(d[i])
           +abs_up(b[i])*abs_up(d[POLE]))/gap
        aa.append(A);cc.append(C)
        Dcancel.append(D3[i]+A*D3[POLE]+C*D3[pivot])
    assert len(Dcancel)==23 and all(x>0 for x in Dcancel)
    D2=sum((x*x for x in D3),F(0))
    Dkernel2=sum((x*x for x in Dcancel),F(0))
    bmid=[x.mid() for x in b]; dmid=[x.mid() for x in d]
    berr=[x.width()/2 for x in b];derr=[x.width()/2 for x in d]
    bm2=sum((x*x for x in bmid),F(0))
    dm2=sum((x*x for x in dmid),F(0))
    be2=sum((x*x for x in berr),F(0))
    de2=sum((x*x for x in derr),F(0))
    assert bm2>0 and dm2>0
    eta=F(1,64)
    check=[]
    for k in POWERS:
        l=F(2**k)
        j0=jump_scalar_sharp(k) # 1/xi with actual cos oscillation
        j1=derivative_jump_weight(k) # 1/xi² with sin phase paid
        rem=derivative_remainder_tail(k,D2)
        kernel=derivative_remainder_tail(k,Dkernel2)
        # Three full-frequency terms; (x+y+z)^2 <=3(x²+y²+z²).
        # Interval rational endpoint enclosures: (bm+delta)^2
        # <=(1+eta)bm bm^T+(1+1/eta)||delta||² I.
        alpha=3*(1+eta)*j0
        beta=3*(1+eta)*j1
        diag=3*((1+1/eta)*(j0*be2+j1*de2)+rem)
        new=alpha*bm2+beta*dm2+diag
        old=F(odd_pilot_tail_enclosure(infos,sources,2**k)[
            "exact_strong_multiplier_tail_squared_norm_upper"])
        assert old==dyadic_full_SM41_strong(k,F(202,25))
        assert min(j0,j1,rem,kernel,alpha,beta,diag)>0
        check.append({
           "cutoff_power":k,"cutoff":"2^"+str(k),
           "SM41_old_full25_strong_upper":str(old),
           "MG11_full25_rank1_endpoint_value_weight":str(alpha),
           "MG11_full25_rank1_endpoint_derivative_weight":str(beta),
           "MG11_full25_isotropic_interval_and_third_remainder":str(diag),
           "MG11_full25_valid_scalar_operator_upper":str(new),
           "MG11_exact_dual_trace_kernel23_entire_strong_upper":str(kernel),
           "MG11_full25_scalar_beats_SM41":new<old,
           "SM41_full25_float":float(old),
           "MG11_full25_float":float(new),
           "MG11_kernel23_float":float(kernel)
        })
    assert len(check)==len(POWERS)
    assert all(F(check[i]["MG11_exact_dual_trace_kernel23_entire_strong_upper"])>
               F(check[i+1]["MG11_exact_dual_trace_kernel23_entire_strong_upper"])
               for i in range(len(check)-1))
    first=next((x["cutoff_power"] for x in check if x["MG11_full25_scalar_beats_SM41"]),None)
    artifact={
      "status":"SCOPED_ORIGINAL_25D_DUAL_TRACE_RANK2_AND_FULL_STRONG_TAIL_CERTIFICATE",
      "canonical_W_ODD_NEG":"OPEN",
      "source_count":N,
      "original_107_SI10_physical_clusters_replayed":True,
      "all_original_sources_odd_on_common_support":True,
      "source_types":{"sin":16,"xcos":8,"pole":1},
      "original_exact_endpoints_from_SM42":True,
      "original_boundary_value_rank":1,
      "exact_value_derivative_boundary_map_rank":2,
      "independent_second_trace_pivot_source_index":pivot,
      "first_trace_pivot_source_index":POLE,
      "exact_rational_second_trace_det_interval":[str(det.l),str(det.h)],
      "strict_abs_determinant_lower":str(gap),
      "exact_23D_dual_boundary_vanishing_source_indices":list(R),
      "true_original_23D_dual_trace_kernel_dimension":23,
      "complete_source_boundary_value_rational_midpoints":[str(x) for x in bmid],
      "complete_source_boundary_derivative_rational_midpoints":[str(x) for x in dmid],
      "complete_source_boundary_value_interval_radius_squared":str(be2),
      "complete_source_boundary_derivative_interval_radius_squared":str(de2),
      "exact_original_third_derivative_majorant_squared_sum":str(D2),
      "boundary_corrected_23source_third_derivative_majorant_squared_sum":str(Dkernel2),
      "exact_23_kernel_pivot_pole_coefficient_upper":[str(x) for x in aa],
      "exact_23_kernel_pivot_other_coefficient_upper":[str(x) for x in cc],
      "full_original25_strong_tail_rank_two_plus_I":
        "Qtail<=alpha*bmid*bmid^T+beta*dmid*dmid^T+diagonal*I25",
      "exact_23D_kernel_whole_strong_tail_decay":
        "O((log cutoff)^2/cutoff^5) in explicit corrected source coefficients",
      "dyadic_checkpoints":check,
      "first_tested_cutoff_power_where_full25_scalar_improves_SM41":first,
      "true_full470_boundary_map_rank2_if_all_470_original_odd_support_generators":True,
      "quantitative_full470_dual_trace_tail_certified":False,
      "original_low_frequency_stiffness_certified":False,
      "original_strong_Galerkin_residual_certified":False,
      "true_original_470_source_51_over_56_gate_passed":False,
      "complete_odd_even_Weil_CC27_RH":"OPEN",
      "independent_original_Fourier_form_domain_audit":"OPEN",
      "interpretation":"Full original source25 high Fourier strong tail rank TWO plus scalar residual, with both endpoint value and endpoint derivative paid. Exact true 23D boundary kernel has 1/xi^3 source Fourier decay, but may be badly conditioned; no low frequency/full 470/odd/Weil/RH promotion."
    }
    dest=ROOT/opts.output;dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(artifact,indent=2)+"\n")
    print("MG11 true original dual boundary source certificate:",json.dumps({
       "rank":2,"true_kernel_dim":23,
       "pivot_source":pivot,
       "determinant_lower":float(gap),
       "k12_old":check[1]["SM41_full25_float"],
       "k12_dual_kernel":check[1]["MG11_kernel23_float"],
       "k20_old":check[4]["SM41_full25_float"],
       "k20_full25":check[4]["MG11_full25_float"],
       "first_scalar_better_power":first,
       "original_470_odd_Weil_RH":"OPEN"}),flush=True)
if __name__=="__main__":
    main()
