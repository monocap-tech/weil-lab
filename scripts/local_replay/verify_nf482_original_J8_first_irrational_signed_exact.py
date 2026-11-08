#!/usr/bin/env python3
"""NF482-A independent exact Fraction actual first J8 physical signed panel audit.

Original NF407 246 original dyadic generators/273 modes, true NF406 n9
regular J8 support, the same original NF478 terminal J7 right seam,
NF477 ALL-m>=18000 complete original source amplitude and a *new*, exact
geometric tail on restricted J8 x<=549/500 (not its B endpoint).
The complete original signed D on physical [log9-B,549/500] is a native
source-certified physical integral, not an imputed full J8 signed upper.
"""
import argparse,json,sys
from pathlib import Path
from fractions import Fraction as Q
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[2]
SRC="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAM="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
def iv(x):
    a,b=map(Q,x);assert a<=b
    return a,b
def log9(K=350):
    t=Q(4,5)
    lower=sum((2*t**(2*j+1)/Q(2*j+1) for j in range(K)),Q(0))
    rem=2*t**(2*K+1)/(Q(2*K+1)*(1-t*t))
    return lower,lower+rem
def scaled(a,b,ell,h):
    x=[a*ell,a*h,b*ell,b*h]
    return min(x),max(x)
def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--native",required=True)
    parser.add_argument("--prior-j7",required=True)
    parser.add_argument("--nf477-custody",default=str(ROOT/"notes/data/provisional/NF477_original_J7_correlated_resolvent_high_image_tail_custody.json"))
    parser.add_argument("--output",required=True)
    a=parser.parse_args()
    d=json.loads(Path(a.native).read_text())
    prev=json.loads(Path(a.prior_j7).read_text())
    tail=json.loads(Path(a.nf477_custody).read_text())
    assert d["pass"]=="NF482-A"
    assert d["original_nf407_source_sha256"]==prev["original_nf407_source_sha256"]==tail["source_sha256"]==SRC
    assert d["original_nf406_seams_sha256"]==prev["original_nf406_seams_sha256"]==tail["seam_sha256"]==SEAM
    assert d["original_source_generators"]==246 and d["original_modes"]==273
    assert d["original_sinh_pole"] and d["original_critical_sines"]==32
    assert d["native_precision_bits"]==4096
    assert d["genuine_original_J8_panel"]==["log9-B","549/500"]
    assert d["original_panel_type"].startswith("J8 first n9-active")
    assert d["original_seven_regular_minus_prime_powers"]==[2,3,4,5,7,8,9]
    assert d["source_Cauchy_ratio"]=="2/5" and d["principal_log_ratio"]=="1/6"
    assert d["original_signed_integration_length"]=="1099/500-log9"
    assert d["original_first_J8_actual_signed_panel_only"]
    assert d["original_J7_J8_irrational_entry_seam_overlap"]
    assert d["original_true_irrational_n9_entry_seam_zero_from_oddness"]
    assert d["original_source_Taylor_remainder"] and Q(d["original_source_Taylor_remainder"])<Q(1,10**120)
    assert Q(d["original_source_arb_coefficient_aggregate_width"])<Q(1,10**40)
    assert Q(d["original_source_weight_input_error_upper"])<Q(1,10**28)
    assert d["certified_sup_z_minus_polynomial"]=="1/10^29"
    assert d["whole_original_J8"]==d["NF404"]==d["W_ODD_NEG"]==d["RH"]=="OPEN"
    assert tail["source_resolvent_M"]==18000 and tail["independent_exact_fraction_ci"]["status"]=="SUCCESS"
    Cm=Q(tail["complete_original_source_Tm_all_m_ge_18000_strict_upper"])
    newtail=Cm*Q(3,8)**72/(2*Q(1,500))
    assert Q(d["original_joint_image_real_tail"])==newtail<Q(1,10**40)
    # This actual 18k source tail uses physical d>=1/500 and MAY NOT
    # replace NF480/481 endpoint resummation for x approaching B.
    l9,u9=log9()
    lengthlo=Q(1099,500)-u9
    lengthhi=Q(1099,500)-l9
    assert Q(7,10000)<lengthlo<lengthhi<Q(1,1000)
    a0,a1=iv(d["original_irrational_physical_length_outward"])
    assert a0<=lengthhi and lengthlo<=a1
    xlo,xhi=iv(d["original_irrational_left_endpoint_log9_minus_B_outward"])
    assert xlo<=u9-Q(11,10) and l9-Q(11,10)<=xhi
    tlo,tup=iv(d["original_normalized_t_lower_outward"])
    t0=(l9-Q(11,10)-Q(686,625))/Q(1,2500)
    t1=(u9-Q(11,10)-Q(686,625))/Q(1,2500)
    assert tlo<=t1 and t0<=tup
    assert Q(-1)<t0<t1<Q(0) and d["original_normalized_t_upper"]=="1"
    e0,e1=iv(d["original_n9_entry_seam_vanishing_outward"])
    assert e0<=0<=e1 and max(abs(e0),abs(e1))<Q(1,10**70)
    assert prev["genuine_original_J7_panel"]==["219/200","log9-B"]
    # Exact independent original-source moments from outward intervals.
    pz0,pz1=iv(d["original_pz_normalized_mean_outward"])
    z0,z1=iv(d["original_z2_normalized_mean_outward"])
    assert z0>0
    old0,old1=iv(d["source_original_D_I_outward"])
    w0,w1=scaled(4*pz0+2*z0,4*pz1+2*z1,lengthlo,lengthhi)
    assert old0<=w1 and w0<=old1
    status="POSITIVE" if old0>0 else "NEGATIVE" if old1<0 else "UNDECIDED"
    assert d["source_original_D_I_strict_sign"]==status
    # Compare to NF479 source-sign logic only as a context, no automatic
    # promotion from a partial signed panel to the whole original D8.
    out={
      "pass":"NF482",
      "standing":"independent exact Fraction original first J8 physical n9-entry irrational signed panel; whole original J8 D8 upper and NF404 remain OPEN",
      "original_nf407_source_sha256":SRC,"original_nf406_seams_sha256":SEAM,
      "source_original_273_mode_continuous_J8_panel":["log9-B","549/500"],
      "true_original_irrational_J8_panel_length_exact_rational":[str(lengthlo),str(lengthhi)],
      "nf477_original_all_m_amplitude_bound":str(Cm),
      "NEW_physical_J8_d_gte_1_over_500_image_tail_bound":str(newtail),
      "source_original_pz_mean_bounds":[str(pz0),str(pz1)],
      "source_original_z2_mean_bounds":[str(z0),str(z1)],
      "independent_exact_signed_D_from_original_pz_z2":[str(w0),str(w1)],
      "original_source_native_signed_D_outward":[str(old0),str(old1)],
      "genuine_first_original_J8_panel_signed_sign":status,
      "original_J8_n9_entry_source_seam_exact_zero":True,
      "original_J8_remaining_physical_interval":["549/500","B"],
      "full_original_J8_signed_upper":"OPEN","NF404":"OPEN","W_ODD_NEG":"OPEN","RH":"OPEN",
      "next_bold":"NF483 genuine original J8 terminal [549/500,B] exact H-principal cancellation, full 20-source-jet analytical functions and original m<18000 complete signed energy"
    }
    path=Path(a.output);path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(out,indent=2)+"\n")
    print("NF482 original physical J8 signed first interval",float(old0),float(old1),status,flush=True)
    print("NF482 exact physical first J8 original matched-image infinite tail",float(newtail),flush=True)
    print("NF482 full J8 signed UPPER, NF404, W-ODD-NEG, RH OPEN",flush=True)
if __name__=="__main__":main()
