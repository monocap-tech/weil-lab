#!/usr/bin/env python3
"""MG10: exact full 25D endpoint-jump + remainder original strong-tail gate.

All original selected 25 physical SI10 sources are ODD and supported
on exactly [-B,B]. Consequently their leading high Fourier boundary
jump lies in ONE common physical trace vector b_j=f_j(B):
 T_z(xi)=-cos(2*pi*B*xi)/(pi*i*xi)*(b*z)+E_z(xi).
The original positive multiplier a_o(xi)<=17+ln|xi| implies a
WHOLE original 25-source strong-tail upper of rank-one-plus-I type.

For exact b, the common endpoint kernel {z:b*z=0} has dimension24:
original endpoint-vanishing h_i=f_i-(b_i/b_pole)*s, i<24,
have O((log Lambda)^2/Lambda^3) complete strong-action high tails.
No original pole/physical function is deleted: this is a basis change.

Rational b intervals come from SM42 original EXACT sine/cos phase
Taylor and exact odd sinh interval. They are not sampled trigonometry.
All results are conditional on the inherited original Fourier/form
domain and multiplier lemmas. No actual resolvent R=J-AZ, complete
470-source Galerkin, odd/even Weil, CC27, RH result is asserted.
"""
import argparse,json
from fractions import Fraction as F
from validate_rpb108_si06_negative_band import B,PI,LN
from validate_rpb108_si10_complement_positivity import protected_inner_cover
from validate_rpb108_sm42_original_physical_gram_and_low_gate import (
    sin_cos_period,hyperbolic_interval)
from validate_rpb108_sm41_original_positive_log_tail import (
    odd_pilot_tail_enclosure,mathematical_global_original_positive_multiplier_majorant)
from validate_rpb108_mg09_original_endpoint_tail_budget import (
    source_derivative_constants,dyadic_strong_from_D,
    dyadic_full_SM41_strong)
from sm36_original_odd_numerical_pilot import ROOT,geometry,select_sources

N=25
P=24
def abs_up(a):
    return max(abs(a.l),abs(a.h))
def boundary_intervals(sources,clusters):
    out=[]
    for kind,j,degree in sources:
        if kind=="pole":
            assert j==-1
            u=hyperbolic_interval(B/2,"sinh")
        else:
            c=sum(clusters[j][:2],F(0))/2
            sn,cs=sin_cos_period(c*B)
            if degree==0:
                u=sn
            else:
                assert degree==1
                u=B*cs
        out.append(u)
    assert len(out)==N and sources[P][0]=="pole"
    assert out[P].l>0
    return out
def jump_scalar_sharp(k):
    # For |xi|>Lambda>=2^11, a_o^2<= (17+ln xi)^2 and
    # |J_z|²=cos²(2pi B xi)/(pi² xi²) * (b*z)².
    # f(xi)=(17+ln xi)^2/xi² monotonically decreases.
    # 2 int_L∞ f cos²(2pi B xi)
    #   =int f +int f cos(4pi B xi)
    #   <=int f +2f(L)/(4pi B).
    # Since pi>3, 1/pi²<1/9 and 1/(2pi B)<1/(6B).
    assert k>=11
    v=F(17)+k*F(347,500)
    L=F(2**k)
    return ((v*v+2*v+2)/L+v*v/(6*B*L*L))/9
def regression():
    # Pure rational finite-dimensional fact: an odd support
    # trace vector is rank one and its kernel codimension one.
    b=[F(2),F(-3),F(5)]
    h0=[F(1),F(0),-b[0]/b[2]]
    h1=[F(0),F(1),-b[1]/b[2]]
    assert sum(x*y for x,y in zip(b,h0))==0
    assert sum(x*y for x,y in zip(b,h1))==0
    assert h0[0]*h1[1]-h0[1]*h1[0]==1
    return True
def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output",default="artifacts/mg10_original_rank_one_endpoint_tail.json")
    args=p.parse_args()
    ledger=json.loads((ROOT/"research/obligations.json").read_text())
    odd=next(o for o in ledger["obligations"] if o["id"]=="W-ODD-NEG")
    assert ledger["active_obligation"]=="W-ODD-NEG"
    assert odd["status"]==ledger["objective"]["status"]=="open"
    assert ledger["governance"]["no_automatic_promotion"]
    assert all(x in odd["evidence"] for x in ("SM41","SM42","SI29"))
    assert mathematical_global_original_positive_multiplier_majorant()
    assert PI[0]>3 and LN[2][1]<F(347,500)
    assert regression()
    clusters,_,_,_,_=protected_inner_cover()
    assert len(clusters)==107
    infos,cap,orders,mass,width,total=geometry()
    sources=select_sources(infos)
    assert len(sources)==N
    endpoint=boundary_intervals(sources,clusters)
    midpoint=[a.mid() for a in endpoint]
    err=[a.width()/2 for a in endpoint]
    assert all(x>=0 for x in err)
    e2=sum((x*x for x in err),F(0))
    b02=sum((x*x for x in midpoint),F(0))
    ds,kind=source_derivative_constants(sources,clusters)
    assert kind=={"sin":16,"xcos":8,"pole":1}
    D2=sum((x*x for x in ds),F(0))
    bp=endpoint[P]
    ratios=[abs_up(endpoint[i])/bp.l for i in range(P)]
    ds_cancel=[ds[i]+ratios[i]*ds[P] for i in range(P)]
    Dcancel2=sum((x*x for x in ds_cancel),F(0))
    assert bp.l>0 and Dcancel2>0
    assert all(abs_up(endpoint[i])<=ratios[i]*bp.l for i in range(P))
    assert all(endpoint[i].l<=midpoint[i]<=endpoint[i].h for i in range(N))
    # The EXACT original boundary-trace functional has rank 1
    # because bpole>0; the 24 original endpoint-vanishing source
    # combinations are analytically independent in coefficient space.
    trank=1
    kernel_dim=N-trank
    assert kernel_dim==24
    t=F(1,2)
    eta=F(1,64)
    checkpoints=[]
    for k in (11,12,13,16,20,24,30,36,40,48,56):
        scalar=odd_pilot_tail_enclosure(infos,sources,2**k)
        old=F(scalar["exact_strong_multiplier_tail_squared_norm_upper"])
        assert old==dyadic_full_SM41_strong(k,F(202,25))
        mu=jump_scalar_sharp(k)
        rem=dyadic_strong_from_D(k,D2)
        rem_kernel=dyadic_strong_from_D(k,Dcancel2)
        rank1=mu*(1+t)*(1+eta)
        isotropic=mu*(1+t)*(1+1/eta)*e2+(1+1/t)*rem
        full_bound=rank1*b02+isotropic
        assert rank1>=0 and isotropic>=0
        assert full_bound>=isotropic
        checkpoints.append({
            "cutoff_power":k,"cutoff":"2^"+str(k),
            "SM41_old_whole25_strong_scalar_upper":str(old),
            "MG10_full25_rank_one_rational_center_coefficient":str(rank1),
            "MG10_full25_isotropic_remainder_and_interval_fee":str(isotropic),
            "MG10_full25_valid_scalar_operator_norm_upper":str(full_bound),
            "MG10_true_exact_boundary_kernel24_strong_upper":str(rem_kernel),
            "MG10_boundary_jump_rank_one_true_weight_upper":str(mu),
            "MG09_raw_25_remainder_strong_upper":str(rem),
            "full25_scalar_improvement_over_SM41":full_bound<old,
            "SM41_whole25_float":float(old),
            "MG10_whole25_float":float(full_bound),
            "MG10_exact_kernel24_float":float(rem_kernel)
        })
    assert len(checkpoints)==11
    assert all(F(c["MG10_true_exact_boundary_kernel24_strong_upper"])>0
               for c in checkpoints)
    # A larger derivative majorant can make the peeled remainder
    # WORSE at modest Lambda. This is a measured method outcome,
    # not a reason to discard an otherwise valid full tail upper.
    # Never assume the rank-one-plus-I bound dominates SM41.
    assert all(F(checkpoints[i]["MG10_true_exact_boundary_kernel24_strong_upper"])>
               F(checkpoints[i+1]["MG10_true_exact_boundary_kernel24_strong_upper"])
               for i in range(10))
    first_better=next((c["cutoff_power"] for c in checkpoints
                      if c["full25_scalar_improvement_over_SM41"]),None)
    out={
      "status":"CERTIFIED_CONDITIONAL_ORIGINAL_25_SOURCE_FULL_STRONG_TAIL_RANK_ONE_PLUS_I",
      "canonical_W_ODD_NEG":"OPEN",
      "original_source_count":N,
      "exact_source_odd_parity_and_common_support":True,
      "original_107_cluster_geometry_replayed":True,
      "source_types":kind,
      "actual_boundary_trace_vector_nonzero":True,
      "original_pole_endpoint_interval":[str(bp.l),str(bp.h)],
      "original_boundary_trace_rank":1,
      "true_original_endpoint_vanishing_source_subspace_dimension":24,
      "exact_physical_boundary_trace_intervals":[[str(x.l),str(x.h)] for x in endpoint],
      "rational_trace_midpoint":[str(x) for x in midpoint],
      "rational_trace_interval_error_radii":[str(x) for x in err],
      "complete_trace_midpoint_squared_norm":str(b02),
      "complete_trace_interval_radius_squared_norm":str(e2),
      "exact_trig_certification_from_SM42":True,
      "all_25_source_derivative_tail_majorant_squared":str(D2),
      "24_boundary_vanishing_corrected_source_remainder_D2":str(Dcancel2),
      "original_all_25_source_full_tail_rank_one_plus_diagonal_inequality":
        "Qtail <= rank1 * bmid*bmid^T + isotropic * I_25",
      "kernel24_analytic_basis":
        "h_i=f_i-(f_i(B)/sinh(B/2))*s, 0<=i<24",
      "kernel24_high_frequency_strong_action_tail_certified":True,
      "whole25_high_frequency_strong_action_tail_certified":True,
      "original_low_frequency_strong_action_certified":False,
      "actual_original_25_source_strong_Galerkin_residual_certified":False,
      "actual_full470_source_residual_and_inverse_certified":False,
      "actual_full470_51_over_56_gate_passed":False,
      "even_Weil_CC27_RH":"OPEN",
      "independent_original_Fourier_form_domain_audit":"OPEN",
      "dyadic_checkpoints":checkpoints,
      "first_tested_dyadic_power_where_MG10_full25_scalar_beats_SM41":first_better,
      "interpretation":"Entire selected true original 25D A_o strong Fourier high tail has a rigorous complete matrix rank-one-plus-I upper; its common endpoint-jump trace rank=1. On the exact physical 24D trace kernel, the WHOLE high tail has fast O((log cutoff)^2/cutoff^3) bound. Still no low-frequency or Galerkin residual / original full470 proof."
    }
    dest=ROOT/args.output
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(out,indent=2)+"\n")
    print("MG10 rank-one entire original 25D high Fourier strong tail:",json.dumps({
       "trace_rank":1,"exact_jump_nullity":24,
       "k12_SM41_whole":checkpoints[1]["SM41_whole25_float"],
       "k12_MG10_rank1_plus_I_whole":checkpoints[1]["MG10_whole25_float"],
       "k12_exact_kernel24":checkpoints[1]["MG10_exact_kernel24_float"],
       "k20_MG10_full25":checkpoints[4]["MG10_whole25_float"],
       "k20_SM41_full25":checkpoints[4]["SM41_whole25_float"],
       "k24_MG10_full25":checkpoints[5]["MG10_whole25_float"],
       "k24_SM41_full25":checkpoints[5]["SM41_whole25_float"],
       "first_tested_improved_dyadic_power":first_better,
       "actual_resolvent_odd_Weil_RH":"OPEN"
    }),flush=True)
if __name__=="__main__":main()
