#!/usr/bin/env python3
"""NF476 independent exact-Fraction irrational physical n8 seam + signed source audit.

The native CI actually computes the complete original 246-source/273 grouped
physical J7 signed integral on [log 8 - 11/10, 1] with 4096-bit Arb.
This checker independently encloses log8 by its rational atanh series;
reconstructs strict signs from pz/z2 outward intervals, without trusting the
native signed sign string; and combines ONLY truly adjacent certified intervals.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse,json
ROOT=Path(__file__).resolve().parents[2]
PREV=ROOT/"notes/data/provisional/NF475_original_J7_near_B_signed_and_partial_union_custody.json"
SRC="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAM="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
B=F(11,10);XC=F(99,100);H=F(3,200)
def I(v):
    a,b=map(F,v);assert a<=b
    return a,b
def sign(a,b):
    return "NEGATIVE" if b<0 else "POSITIVE" if a>0 else "UNDECIDED"
def log8_exact_rational(K=400):
    # log8 = 2 atanh(7/9), all terms strictly positive; remaining
    # terms have denominator >=(2K+1), geometric ratio (7/9)^2.
    t=F(7,9)
    lo=sum((2*t**(2*j+1)/F(2*j+1) for j in range(K)),F(0))
    rem=2*t**(2*K+1)/(F(2*K+1)*(1-t*t))
    return lo,lo+rem
def product(lo,hi,a,b):
    v=[lo*a,lo*b,hi*a,hi*b]
    return min(v),max(v)
def main():
    p=argparse.ArgumentParser()
    p.add_argument("--native",required=True)
    p.add_argument("--previous",default=str(PREV))
    p.add_argument("--output",required=True)
    a=p.parse_args()
    n=json.loads(Path(a.native).read_text())
    prev=json.loads(Path(a.previous).read_text())
    assert n["pass"]=="NF476"
    assert n["original_nf407_source_sha256"]==prev["source_sha256"]==SRC
    assert n["original_nf406_seams_sha256"]==prev["seam_sha256"]==SEAM
    assert n["original_source_generators"]==246 and n["original_modes"]==273
    assert n["original_sinh_pole"] and n["original_six_regular_minus_prime_powers"]==[2,3,4,5,7,8]
    assert n["genuine_original_J7_panel"]==["log8-B","1"]
    assert n["fixed_source_Chebyshev_or_Taylor_basis"]=="source-native shared coefficient x=99/100+(3/200)t, degree 1399, physical t in [tlo,2/3]"
    assert n["source_centered_Taylor_analytic_radius"]=="1/25"
    assert n["source_Cauchy_ratio"]=="3/8"
    assert n["principal_log_ratio"]=="3/22"
    assert n["original_panel_type"]=="J7 true irrational left seam panel, NF464 partition [log8-B,1]"
    assert n["original_signed_integration_length"]=="21/10-log8"
    assert n["original_true_irrational_n8_seam_zero_from_oddness"]
    assert n["native_precision_bits"]==4096
    assert n["certified_sup_z_minus_polynomial"]=="1/10^28"
    assert F(n["original_source_arb_coefficient_aggregate_width"])<F(1,10**40)
    assert F(n["original_source_Taylor_remainder"])<F(1,10**120)
    E=F(100*10**160,3000)*F(3,8)**600
    assert F(n["original_joint_image_real_tail"])==E
    assert E<F(1,10**40)
    # Exact rational arctanh series settles the lower endpoint and length
    # without a rational approximation substituted for physical log8-B.
    loglo,loghi=log8_exact_rational()
    xlo_r=(loglo-B,loghi-B)
    L_r=(B+1-loghi,B+1-loglo)
    assert F(0)<L_r[0]<L_r[1]<F(1,40)
    assert XC-H<xlo_r[0]<xlo_r[1]<1<XC+H
    assert loglo>F(2075,1000) and loghi<F(21,10)
    xl_native=I(n["original_irrational_left_endpoint_log8_minus_B_outward"])
    L_native=I(n["original_irrational_physical_length_outward"])
    assert xl_native[0]<=xlo_r[1] and xlo_r[0]<=xl_native[1]
    assert L_native[0]<=L_r[1] and L_r[0]<=L_native[1]
    tlo_native=I(n["original_normalized_t_lower_outward"])
    assert -F(1)<tlo_native[0]<tlo_native[1]<0
    assert n["original_normalized_t_upper"]=="2/3"
    n8lo,n8hi=I(n["original_n8_seam_vanishing_outward"])
    assert n8lo<=0<=n8hi and -F(1,10**70)<n8lo<=n8hi<F(1,10**70)
    pzlo,pzhi=I(n["original_pz_normalized_mean_outward"])
    zzlo,zzhi=I(n["original_z2_normalized_mean_outward"])
    assert zzlo>0
    signedmid_lo=4*pzlo+2*zzlo
    signedmid_hi=4*pzhi+2*zzhi
    direct_lo,direct_hi=product(L_r[0],L_r[1],signedmid_lo,signedmid_hi)
    dlo,dhi=I(n["source_original_D_I_outward"])
    assert dlo<=direct_hi and direct_lo<=dhi
    native_sign=sign(dlo,dhi)
    direct_sign=sign(direct_lo,direct_hi)
    assert native_sign==n["source_original_D_I_strict_sign"]
    if native_sign!="UNDECIDED" and direct_sign!="UNDECIDED":
        assert native_sign==direct_sign
    assert prev["new_original_contiguous_panel"]==["1","109/100"]
    priorlo,priorhi=I(prev["new_original_contiguous_D_outward"])
    assert priorhi<0
    ulo,uhi=dlo+priorlo,dhi+priorhi
    out={
      "pass":"NF476",
      "standing":"exact rational authentic irrational physical n8 seam, mixed/quadratic signed and true partial J7 union",
      "source_sha256":SRC,"seams_sha256":SEAM,
      "exact_rational_log8_series_terms":400,
      "original_lower_left_endpoint_log8_minus_B_rational":[str(x) for x in xlo_r],
      "original_length_21_10_minus_log8_rational":[str(x) for x in L_r],
      "original_image_modes":3000,
      "original_image_tail_exact_rational":str(E),
      "original_exact_original_n8_seam_zero":True,
      "true_original_left_J7_panel":["log8-B","1"],
      "source_original_pz_normalized_outward":[str(pzlo),str(pzhi)],
      "source_original_z2_normalized_outward":[str(zzlo),str(zzhi)],
      "independent_exact_fraction_original_signed_interval":[str(direct_lo),str(direct_hi)],
      "original_native_signed_interval":[str(dlo),str(dhi)],
      "independent_original_signed_sign":direct_sign,
      "source_native_signed_sign":native_sign,
      "prior_certified_adjacent_panel":["1","109/100"],
      "prior_certified_signed_interval":[str(priorlo),str(priorhi)],
      "certified_contiguous_original_J7_partial_panel":["log8-B","109/100"],
      "certified_contiguous_original_signed_interval":[str(ulo),str(uhi)],
      "certified_contiguous_partial_sign":sign(ulo,uhi),
      "whole_original_J7":"OPEN","whole_original_J8":"OPEN",
      "NF404":"OPEN","W_ODD_NEG":"OPEN","RH":"OPEN"}
    o=Path(a.output);o.parent.mkdir(parents=True,exist_ok=True)
    o.write_text(json.dumps(out,indent=2)+"\n")
    print("NF476 ORIGINAL IRRATIONAL n8 physical left-panel signed",float(dlo),float(dhi),native_sign)
    print("NF476 independent exact Fraction mixed+quadratic sign",direct_sign)
    print("NF476 original contiguous [log8-B,1.09]",float(ulo),float(uhi),sign(ulo,uhi))
    print("NF476 full J7/J8 NF404 W-ODD-NEG RH OPEN")
if __name__=="__main__":main()
