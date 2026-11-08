#!/usr/bin/env python3
"""NF478 independent exact-rational TRUE full ORIGINAL J7 signed integral audit.

Original 246-source/273 modes, two remaining genuine real J7 panels,
source-certified NF477 all-J7 infinite matched-image tail, physical
irrational n9 entry (NOT new n9 negative prime term inside J7), and
source-custodied prior NF476 five contiguous original panels.

No W-ODD-NEG / NF404 / RH promotion follows automatically from conditional
full-J7 source signed negativity.
"""
import argparse,json,math
from pathlib import Path
from fractions import Fraction as F
ROOT=Path(__file__).resolve().parents[2]
SRC="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAM="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
PRIOR=ROOT/"notes/data/provisional/NF476_original_J7_irrational_left_signed_and_partial_custody.json"
TAIL=ROOT/"notes/data/provisional/NF477_original_J7_correlated_resolvent_high_image_tail_custody.json"
NF464_GATE=-F("2.03475e-22")
def iv(v):
    a,b=map(F,v);assert a<=b
    return a,b
def sg(a,b):
    return "NEGATIVE" if b<0 else "POSITIVE" if a>0 else "UNDECIDED"
def log9_exact(K=500):
    """Original log9 = 2 atanh(4/5) with exact rational positive tail."""
    t=F(4,5)
    lo=sum((2*t**(2*j+1)/F(2*j+1) for j in range(K)),F(0))
    rem=2*t**(2*K+1)/(F(2*K+1)*(1-t*t))
    assert rem>0
    return lo,lo+rem
def scale_interval(a,b,l,h):
    v=[a*l,a*h,b*l,b*h]
    return min(v),max(v)
def direct_source_moment_witness(d,Lo,Lhi):
    plo,phi=iv(d["original_pz_normalized_mean_outward"])
    qlo,qhi=iv(d["original_z2_normalized_mean_outward"])
    assert qlo>0
    return scale_interval(4*plo+2*qlo,4*phi+2*qhi,Lo,Lhi)
def main():
    p=argparse.ArgumentParser()
    p.add_argument("--right",required=True)
    p.add_argument("--terminal",required=True)
    p.add_argument("--prior",default=str(PRIOR))
    p.add_argument("--tail",default=str(TAIL))
    p.add_argument("--output",required=True)
    a=p.parse_args()
    right=json.loads(Path(a.right).read_text())
    end=json.loads(Path(a.terminal).read_text())
    prior=json.loads(Path(a.prior).read_text())
    tail=json.loads(Path(a.tail).read_text())
    for d in (right,end):
        assert d["original_nf407_source_sha256"]==SRC and d["original_nf406_seams_sha256"]==SEAM
        assert d["original_source_generators"]==246 and d["original_modes"]==273
        assert d["original_critical_sines"]==32 and d["original_sinh_pole"]
        assert d["native_precision_bits"]==4096
        assert d["original_six_regular_minus_prime_powers"]==[2,3,4,5,7,8]
        assert d["certified_sup_z_minus_polynomial"]=="1/10^28"
        assert F(d["original_source_arb_coefficient_aggregate_width"])<F(1,10**40)
        assert F(d["original_source_Taylor_remainder"])<F(1,10**120)
        assert F(d["original_source_weight_input_error_upper"])<F(1,10**28)
        assert F(d["original_joint_image_real_tail"])==F(tail["original_both_endpoint_infinite_image_uniform_tail_strict_upper"])
        assert d["whole_original_J7"]==d["whole_original_J8"]==d["NF404"]==d["W_ODD_NEG"]==d["RH"]=="OPEN"
    assert tail["pass"]=="NF477" and tail["source_sha256"]==SRC and tail["seam_sha256"]==SEAM
    assert tail["independent_exact_fraction_ci"]["status"]=="SUCCESS"
    assert tail["original_both_endpoint_image_tail_lt_1e_minus_40"]
    assert tail["source_resolvent_M"]==18000
    assert prior["original_nf407_source_sha256"]==SRC and prior["original_nf406_seams_sha256"]==SEAM
    assert prior["new_true_original_contiguous_partial_panel"]==["log8-B","109/100"]
    assert right["pass"]=="NF478-R" and end["pass"]=="NF478-T"
    assert right["genuine_original_J7_panel"]==["109/100","219/200"]
    assert end["genuine_original_J7_panel"]==["219/200","log9-B"]
    assert right["original_signed_integration_length"]=="1/200"
    assert right["source_Cauchy_ratio"]=="1/2" and right["principal_log_ratio"]=="1/3"
    assert end["original_signed_integration_length"]=="log9-439/200"
    assert end["source_Cauchy_ratio"]=="12/25" and end["principal_log_ratio"]=="4/13"
    assert right["original_true_left_boundary_cross_check_original_compact"]
    assert end["original_true_left_boundary_matches_NF478_R"]
    assert end["original_true_irrational_n9_entry_seam_zero_from_oddness"]
    e0,e1=iv(end["original_n9_entry_seam_vanishing_outward"])
    assert e0<=0<=e1 and max(abs(e0),abs(e1))<F(1,10**70)
    # Right panel is exactly length 1/200: no inherited earlier 1/100 factor.
    r0,r1=iv(right["source_original_D_I_outward"])
    rd0,rd1=direct_source_moment_witness(right,F(1,200),F(1,200))
    assert r0<=rd1 and rd0<=r1
    # Terminal panel's endpoint is the exact physical original log9-B.
    loglo,loghi=log9_exact()
    lengthlo=loglo-F(439,200)
    lengthhi=loghi-F(439,200)
    assert F(1,500)<lengthlo<lengthhi<F(1,400)
    tlo,tup=iv(end["original_irrational_physical_length_outward"])
    assert tlo<=lengthhi and lengthlo<=tup, "original irrational physical length mismatch"
    xlo,xhi=iv(end["original_irrational_right_endpoint_log9_minus_B_outward"])
    assert xlo<=loghi-F(11,10) and loglo-F(11,10)<=xhi
    assert end["original_normalized_t_lower"]=="-11/12"
    thi0,thi1=iv(end["original_normalized_t_upper_outward"])
    expected0=(loglo-F(11,10)-F(10961,10000))/F(3,2500)
    expected1=(loghi-F(11,10)-F(10961,10000))/F(3,2500)
    assert thi0<=expected1 and expected0<=thi1
    assert F(0)<thi0<thi1<F(1)
    assert F(end["original_source_Taylor_remainder"])<F(1,10**120)
    eD0,eD1=iv(end["source_original_D_I_outward"])
    ed0,ed1=direct_source_moment_witness(end,lengthlo,lengthhi)
    assert eD0<=ed1 and ed0<=eD1
    # Actual original J7 physical signed decomposition has no artificial
    # gaps or double counting: five old cells, NF478-R, terminal n9 seam.
    priorlo,priorhi=iv(prior["new_true_original_contiguous_signed_D_outward"])
    full_lo,full_hi=priorlo+r0+eD0,priorhi+r1+eD1
    remainslo,remainshi=r0+eD0,r1+eD1
    gate=full_hi<NF464_GATE
    out={
      "pass":"NF478",
      "standing":"independent TRUE original 7-panel J7 source signed interval and NF464 conditional threshold audit",
      "original_nf407_source_sha256":SRC,"original_nf406_seams_sha256":SEAM,
      "original_original_nf477_all_m_image_tail":str(F(tail["original_both_endpoint_infinite_image_uniform_tail_strict_upper"])),
      "source_native_R_panel":["109/100","219/200"],
      "source_native_R_signed_interval":[str(r0),str(r1)],
      "independent_exact_Fraction_R_moments_signed_interval":[str(rd0),str(rd1)],
      "source_native_R_sign":sg(r0,r1),
      "source_native_T_panel":["219/200","log9-B"],
      "original_true_terminal_log9_length_exact_rational":[str(lengthlo),str(lengthhi)],
      "source_native_T_signed_interval":[str(eD0),str(eD1)],
      "independent_exact_Fraction_T_moments_signed_interval":[str(ed0),str(ed1)],
      "source_native_T_sign":sg(eD0,eD1),
      "original_remaining_two_right_J7_signed_interval":[str(remainslo),str(remainshi)],
      "prior_original_five_contiguous_signed_interval":[str(priorlo),str(priorhi)],
      "whole_original_J7_physical_support":["log8-B","log9-B"],
      "original_COMPLETE_seven_panel_J7_signed_interval":[str(full_lo),str(full_hi)],
      "original_COMPLETE_seven_panel_J7_signed_sign":sg(full_lo,full_hi),
      "NF464_conditional_J7_negative_threshold":str(NF464_GATE),
      "NF464_conditional_J7_negative_gate_source_certified":gate,
      "NF404":"OPEN","W_ODD_NEG":"OPEN","whole_original_J8":"OPEN","RH":"OPEN"}
    dst=Path(a.output);dst.parent.mkdir(parents=True,exist_ok=True)
    dst.write_text(json.dumps(out,indent=2)+"\n")
    print("NF478 ORIGINAL J7 right R",float(r0),float(r1),sg(r0,r1),flush=True)
    print("NF478 ORIGINAL J7 terminal T",float(eD0),float(eD1),sg(eD0,eD1),flush=True)
    print("NF478 entire genuine original J7",float(full_lo),float(full_hi),sg(full_lo,full_hi),flush=True)
    print("NF478 NF464 conditional J7 source threshold",gate,flush=True)
    print("NF478 NF404 W-ODD-NEG J8 RH OPEN",flush=True)
if __name__=="__main__":main()
