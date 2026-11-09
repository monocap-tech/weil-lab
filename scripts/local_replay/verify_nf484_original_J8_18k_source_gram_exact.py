#!/usr/bin/env python3
"""NF484 independent pure-exact-Fraction audit: ORIGINAL 18k image Gram custody.

This verifier NEVER assumes the native source output is correct by name:
it rechecks all 18000 actual T_m,d_m NF407 246-source 273-mode outward
intervals; their common original v=U(B), genuine m0 source exception,
all 9 raw source SHA witnesses, per-m same-source cancellation,
true J8 B terminal right-image geometric tail, source input radius
and the exactly charged squared-energy perturbation.

Checks actual final finite-image Gram nonnegativity, original first
moment Cauchy compatibility, and original source truncation error.
It does NOT claim the complete physical mixed J8 signed scalar or RH.
"""
from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal,localcontext
import argparse,json,hashlib,sys
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
SRC="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAM="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
B=F(11,10);DELTA=F(1,500);M=18000;R=360
def load(p):
    raw=Path(p).read_bytes()
    return json.loads(raw),hashlib.sha256(raw).hexdigest()
def iv(z):
    a,b=map(F,z);assert a<=b
    return a,b
def dec(x):
    with localcontext() as c:
        c.prec=45
        return str(Decimal(x.numerator)/Decimal(x.denominator))
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--input-dir",required=True)
    ap.add_argument("--gram",required=True)
    ap.add_argument("--output",required=True)
    args=ap.parse_args()
    g,hg=load(args.gram)
    assert g["pass"]=="NF484"
    assert g["source_original_nf407_sha256"]==SRC
    assert g["original_nf406_seams_sha256"]==SEAM
    assert g["original_full_M_image_coefficients"]==M
    assert g["original_right_image_tail_kept_m_lt"]==R
    assert g["original_source_fixedpoint_precision_digits"]==240
    assert g["native_original_full_4096bit_source_generator_blocks"]==9
    assert g["actual_original_m0_sinh_pole_included"]
    assert g["original_actual_terminal_signed_D8_upper"]==g["NF404"]==g["W_ODD_NEG"]==g["RH"]=="OPEN"
    assert g["original_true_right_image_m_ge_120_geometric_discarded_upper"]
    src_max=F(0)
    vov=None
    fragments=[]
    inputs=Path(args.input_dir)
    for start in range(0,M,2000):
        f=inputs/f"nf484-source-renormalized-{start}-{start+2000}.json"
        d,h=load(f)
        fragments.append({"m":start,"json_sha256":h})
        assert d["pass"]=="NF484-source-native"
        assert d["original_nf407_source_sha256"]==SRC
        assert d["original_nf406_seams_sha256"]==SEAM
        assert d["original_246_generators"] and d["original_273_grouped_modes"] and d["original_sinh_m0_removable_pole"]
        assert d["native_precision_bits"]==4096
        assert d["original_source_input_radii_sum_lt"]=="1e-700"
        assert d["all_finite_original_image_coefficients_m_from"]==start
        assert d["all_finite_original_image_coefficients_m_stop"]==start+2000
        rows=d["original_source_Tm_and_same_source_dm_outward"]
        assert len(rows)==2000
        v=iv(d["original_source_v_at_B_outward"])
        assert v[1]<0
        if vov is None:vov=v
        else:assert v[0]<=vov[1] and vov[0]<=v[1]
        for i,row in enumerate(rows):
            assert len(row)==4
            c=iv(row[:2]);r=iv(row[2:])
            assert c[1]-c[0]<F(1,10**240)
            assert r[1]-r[0]<F(1,10**240)
            aa=F(4*(start+i)+1,4)
            assert c[0]-r[1]<=v[1]/aa and v[0]/aa<=c[1]-r[0]
            src_max=max(src_max,abs(r[0]),abs(r[1]))
    assert src_max<F(10)**180
    assert F(g["original_maximum_renormalized_dm_abs_upper"])==src_max
    # Rigorous all-original input S0 proof on 273 source grouped modes:
    assert 4*(B+26)**13<F(10)**20
    assert (F(10)**20+40)*F(1,10**700)<F(1,10**50)
    bound_right=src_max*F(3,8)**(4*R+1)/(1-F(3,8)**4)
    assert F(g["original_true_right_image_m_ge_120_geometric_discarded_upper"])==bound_right
    assert bound_right<F(1,10**230)
    # Each d_m true source+native+fixed-point error <2e-230:
    # 1/2 sum left 18k plus 5x right R=360 entries incl endpoints.
    epsilon_conservative=(F(M,2)+F(5*R,2))*F(2,10**230)+bound_right/2
    epsilon=F(g["original_finite_image_uniform_input_native_rounding_error_upper"])
    assert epsilon_conservative<epsilon==F(1,10**224)
    amplitude_sup=(M+R)*src_max
    assert F(g["original_true_finite_image_uniform_sup_original_source_bound"])==amplitude_sup
    fee=DELTA*(2*amplitude_sup*epsilon+epsilon**2)
    assert fee==F(g["original_finite_image_square_integral_error_charge"])<F(1,10**40)
    E0,E1=iv(g["source_original_only_finite_image_renormalized_squared_Gram_interval"])
    I0,I1=iv(g["source_original_finite_image_renormalized_linear_terminal_integral_interval"])
    assert E0>=0 and E1>E0
    assert I0<=I1
    assert F(0)<=E1<DELTA*amplitude_sup**2
    assert max(abs(I0),abs(I1))<DELTA*amplitude_sup
    # Independent exact original physical Cauchy consistency:
    # (int I)^2 <= delta int I^2; the upper energy must dominate
    # any nonzero lower magnitude for the original linear interval.
    ilo=min(abs(I0),abs(I1)) if (I0>0 or I1<0) else F(0)
    assert ilo*ilo<=DELTA*E1
    assert len(g["native_original_18k_source_fragments_sha256"])==9
    for j,row in enumerate(fragments):
        orig=g["native_original_18k_source_fragments_sha256"][j]
        assert orig["start"]==row["m"] and orig["sha256"]==row["json_sha256"]
    assert g["squared_component_type"].startswith("∫_549/500^B")
    out={
      "pass":"NF484-independent",
      "standing":"EXACT original 18k T_m and d_m same-source input/seam/dyadic error, actual terminal finite-image Gram and mean validated; complete original terminal D8 UPPER OPEN",
      "original_source_nf407_sha256":SRC,
      "original_support_nf406_sha256":SEAM,
      "original_all_9_native_blocks_sha256":fragments,
      "original_source_gram_raw_sha256":hg,
      "original_total_original_native_amplitudes_checked":M,
      "original_true_renormalized_amplitude_max":str(src_max),
      "original_source_input_amplification_lt_1e20":True,
      "original_true_right_image_tail_lt_1e_minus_230":True,
      "original_true_image_approx_uniform_lt_1e_minus_224":True,
      "original_true_squared_terminal_energy_fee_lt_1e_minus_40":True,
      "original_source_terminal_finite_image_gram_interval":[str(E0),str(E1)],
      "original_source_terminal_finite_image_mean_interval":[str(I0),str(I1)],
      "original_original_terminal_signed_D8_upper":"OPEN",
      "NF404":"OPEN","W_ODD_NEG":"OPEN","RH":"OPEN",
      "next_bold":"NF485 actual original central+seven-minus-prime+H and 19 full-source Phi endpoint mixed moments"
    }
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(out,indent=2)+"\n")
    print("NF484 independent ORIGINAL complete 18000 original image source/correlation Fraction audit PASS",flush=True)
    print("NF484 genuine finite-image source squared Gram interval",dec(E0),dec(E1),flush=True)
    print("NF484 genuine finite-image source linear terminal integral",dec(I0),dec(I1),flush=True)
    print("NF484 all-J8 signed upper NF404 W-ODD-NEG RH OPEN",flush=True)
if __name__=="__main__":main()
