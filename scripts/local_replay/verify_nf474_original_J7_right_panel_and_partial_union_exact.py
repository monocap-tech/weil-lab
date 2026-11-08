#!/usr/bin/env python3
"""NF474 exact Fraction audit: full original J7 [53/50,27/25] signed moment and contiguous union.

Consumes independent 4096-bit original-source NF474 numerical output; never
substitutes independent test-function points or treats partial J7 as whole J7.
"""
from fractions import Fraction as F
from pathlib import Path
import json,argparse
HERE=Path(__file__).resolve().parents[2]
PREV=HERE/"notes/data/provisional/NF473_original_J7_adjacent_negative_panel_and_partial_union_custody.json"
SRC="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAM="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
def I(v):
    lo,hi=map(F,v)
    assert lo<=hi
    return lo,hi
def status(lo,hi):
    return "NEGATIVE" if hi<0 else "POSITIVE" if lo>0 else "UNDECIDED"
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--native",required=True)
    ap.add_argument("--nf473",default=str(PREV))
    ap.add_argument("--output",required=True)
    a=ap.parse_args()
    z=json.loads(Path(a.native).read_text())
    old=json.loads(Path(a.nf473).read_text())
    assert z["pass"]=="NF474"
    assert z["original_nf407_source_sha256"]==old["source_sha256"]==SRC
    assert z["original_nf406_seams_sha256"]==old["seams_sha256"]==SEAM
    assert z["genuine_original_J7_panel"]==["53/50","27/25"]
    assert z["original_source_generators"]==246 and z["original_modes"]==273
    assert z["original_sinh_pole"] and z["original_six_regular_minus_prime_powers"]==[2,3,4,5,7,8]
    assert z["fixed_source_Chebyshev_or_Taylor_basis"]=="source-native shared coefficient x=107/100+(1/100)s, degree 1599"
    assert z["original_panel_type"]=="J7 right rational panel, NF464 partition [53/50,27/25]"
    assert z["original_signed_integration_length"]=="1/50"
    assert z["principal_log_ratio"]=="1/3"
    assert z["source_centered_Taylor_analytic_radius"]=="1/50"
    assert z["source_Cauchy_ratio"]=="1/2"
    assert z["native_precision_bits"]==4096
    assert z["original_true_left_boundary_cross_check_NF470_architecture"]
    assert not z["original_true_mean_cross_check_NF471"]
    assert z["certified_sup_z_minus_polynomial"]=="1/10^28"
    assert F(z["original_source_arb_coefficient_aggregate_width"])<F(1,10**40)
    assert F(z["original_source_Taylor_remainder"])<F(1,10**120)
    # Crucial NEW right-panel physical tail, no uncharged inherited
    # NF472/NF473 6000-mode image assumption.
    E=F(100*10**160,12000)*F(3,8)**480
    assert F(z["original_joint_image_real_tail"])==E
    assert E<F(1,10**40)
    pzlo,pzhi=I(z["original_pz_normalized_mean_outward"])
    qlo,qhi=I(z["original_z2_normalized_mean_outward"])
    dlo,dhi=I(z["source_original_D_I_outward"])
    directlo=F(1,50)*(4*pzlo+2*qlo)
    directhi=F(1,50)*(4*pzhi+2*qhi)
    assert directlo<=dhi and dlo<=directhi
    signed_native=status(dlo,dhi)
    signed_moments=status(directlo,directhi)
    assert signed_native==z["source_original_D_I_strict_sign"]
    if signed_native!="UNDECIDED" and signed_moments!="UNDECIDED":
        assert signed_native==signed_moments
    assert old["contiguous_partial_J7_panel"]==["1","53/50"]
    prevlo,prevhi=I(old["contiguous_partial_original_D_outward"])
    assert prevhi<0
    unionlo,unionhi=dlo+prevlo,dhi+prevhi
    report={
        "pass":"NF474",
        "standing":"independent exact Fraction original J7 right-panel signed-moment witness and strictly contiguous partial union",
        "source_sha256":SRC,"seams_sha256":SEAM,
        "original_source_4096bit":True,
        "original_image_modes":12000,"original_image_tail_exact_upper":str(E),
        "original_source_shared_moment_sign":signed_moments,
        "original_source_native_signed_interval":[str(dlo),str(dhi)],
        "original_source_native_sign":signed_native,
        "independent_complete_original_pz_outward":[str(pzlo),str(pzhi],
        "independent_complete_original_z2_outward":[str(qlo),str(qhi)],
        "independent_fraction_moment_signed_interval":[str(directlo),str(directhi)],
        "original_nf474_physical_panel":["53/50","27/25"],
        "independent_true_left_boundary_compact_source_overlap":True,
        "previous_original_contiguous_J7_partial_panel":["1","53/50"],
        "previous_original_contiguous_J7_partial_signed_interval":[str(prevlo),str(prevhi)],
        "original_new_contiguous_J7_partial_panel":["1","27/25"],
        "original_new_contiguous_J7_partial_signed_interval":[str(unionlo),str(unionhi)],
        "original_new_contiguous_J7_partial_sign":status(unionlo,unionhi),
        "whole_J7":"OPEN","whole_J8":"OPEN","NF404":"OPEN","W_ODD_NEG":"OPEN","RH":"OPEN"
    }
    dst=Path(a.output);dst.parent.mkdir(parents=True,exist_ok=True)
    dst.write_text(json.dumps(report,indent=2)+"\n")
    print("NF474 original physical signed I[53/50,27/25]",float(dlo),float(dhi),signed_native,flush=True)
    print("NF474 independently reconstructed full moments sign",signed_moments,flush=True)
    print("NF474 original CONTIGUOUS signed [1,27/25]",float(unionlo),float(unionhi),status(unionlo,unionhi),flush=True)
    print("NF474 whole J7/J8 NF404 W-ODD-NEG RH OPEN",flush=True)
if __name__=="__main__":main()
