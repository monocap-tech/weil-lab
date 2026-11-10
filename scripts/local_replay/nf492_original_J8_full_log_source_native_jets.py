#!/usr/bin/env python3
"""NF492 original native 4096bit all-orders J8 logarithmic source coefficients.

Compute ACTUAL original NF407 246-generator source U(B), U(B-1/500)
and endpoint U^(0..5)(B) without external images, unchanged original
odd sinh. Native source midpoint dyadics plus separately paid 10^-600
input radius. These are physical source values, NOT D8 signed integral.
"""
from __future__ import annotations
import argparse,hashlib,json,math,sys
from fractions import Fraction as F
from pathlib import Path
from flint import arb,acb,ctx
from nf415_original_cell6_I1_validated_acb import native_source,U
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
B=F(11,10);DELTA=F(1,500);X=B-DELTA
SRC="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SOURCE_FEE=F(1,10**600)
def A(x):
    if isinstance(x,arb): return x
    if isinstance(x,F):return arb(x.numerator)/arb(x.denominator)
    return arb(x)
def C(x):return acb(A(x))
def out(q,digits=160):
    m,r,e=q.mid_rad_10exp(digits)
    fac=F(10)**int(e)
    return F(int(m)-int(r))*fac-SOURCE_FEE,F(int(m)+int(r))*fac+SOURCE_FEE
def intersect(x,y):return x[0]<=y[1] and y[0]<=x[1]
def src_jet(terms,pole,y,maxk=5):
    pi=arb.pi()
    Y=A(y)
    out=[arb(0) for _ in range(maxk+1)]
    for f,k,c in terms:
        om=2*pi*A(f)
        iw=acb(arb(0),om)
        alp=acb(arb(0),-A(c)/2) if k%2==0 else acb(A(c)/2)
        ph=alp*(iw*Y).exp()
        for r in range(maxk+1):
            v=acb(0)
            for j in range(min(r,k)+1):
                v+=math.comb(r,j)*(math.factorial(k)//math.factorial(k-j))*(Y**(k-j))*(iw**(r-j))
            out[r]+=2*(ph*v).real
    pole_=A(pole)
    sn=(Y/2).sinh();cs=(Y/2).cosh()
    for r in range(maxk+1):
        out[r]+=pole_*(A(F(1,2))**r)*(sn if r%2==0 else cs)
    return out
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--source",default="notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json")
    ap.add_argument("--output",required=True)
    args=ap.parse_args()
    ctx.prec=4096
    raw=Path(args.source).read_bytes()
    source=json.loads(raw)
    sha=hashlib.sha256(raw).hexdigest()
    assert sha==SRC and source["original_dimension"]==242
    assert len(source["original_exact_native_original_four_critical_coefficients_mid_radius"])==4
    assert len(source["original_source_critical_sine_frequencies"])==32
    terms,pole,s0=native_source(source)
    assert len(terms)==273
    assert s0<F(1,10**700) and F(10)**40*s0<SOURCE_FEE
    assert all(F(0)<f<883 and 0<=k<=13 for f,k,c in terms)
    full=U(source)
    true_B=full.at(C(B)).real
    true_X=full.at(C(X)).real
    jets=src_jet(terms,pole,B)
    val_B=out(true_B)
    val_X=out(true_X)
    assert intersect(val_B,out(jets[0]))
    jet_pairs=[out(j) for j in jets]
    assert F(-1,10**3)<jet_pairs[2][0]<=jet_pairs[2][1]<0
    assert jet_pairs[1][1]<0 and jet_pairs[0][1]<0
    assert F(-10**10)<jet_pairs[5][0]<=jet_pairs[5][1]<10**10
    g_pair=((val_X[0]-val_B[1])/2,(val_X[1]-val_B[0])/2)
    alpha_pair=(-jet_pairs[1][1]/2,-jet_pairs[1][0]/2)
    beta_pair=(jet_pairs[2][0]/4,jet_pairs[2][1]/4)
    assert alpha_pair[0]>0 and beta_pair[1]<0
    outj={
      "pass":"NF492-source-native",
      "standing":"ORIGINAL source 4096-bit true physical U(B-1/500), source derivative jets 0..5 at B, exact all-orders g logarithmic coefficient; no genuine signed D8 integral",
      "original_nf407_source_sha256":SRC,
      "original_selected_plus_critical_generator_count":246,
      "original_source_grouped_freq_order_count":273,
      "original_source_sinh_critical_pole_preserved":True,
      "source_original_precision_bits":4096,
      "original_original_dyadic_full_source_midpoint_radius_sum":str(s0),
      "original_dyadic_full_source_included_radius_charge":str(SOURCE_FEE),
      "original_true_B":"11/10",
      "original_true_J8_d":"1/500",
      "original_true_J8_x":"549/500",
      "original_source_U_B_exact_outward":[str(v) for v in val_B],
      "original_source_U_B_minus_delta_exact_outward":[str(v) for v in val_X],
      "original_source_derivatives_B_order_0_to_5_exact_outward":[[str(v) for v in pair] for pair in jet_pairs],
      "original_true_log_coefficient_g_delta_equal_half_U_difference":[str(v) for v in g_pair],
      "original_true_first_log_coefficient_alpha":[str(v) for v in alpha_pair],
      "original_true_second_log_coefficient_beta":[str(v) for v in beta_pair],
      "original_source_U_second_derivative_B_strict_negative":True,
      "original_source_U_five_derivatives_true_4096bit":True,
      "original_full_original_J8_D8_signed_UPPER":"OPEN",
      "NF404":"OPEN","W_ODD_NEG":"OPEN","RH":"OPEN",
      "next_bold":"NF493: native all 400 source-contracted H and g jets and original true terminal physical signed polynomial-log moments"
    }
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(outj,indent=2)+"\n")
    print("NF492 original full 246-source 4096bit U(B-1/500)",float(val_X[0]),float(val_X[1]),flush=True)
    print("NF492 original full 246-source 4096bit g(1/500)",float(g_pair[0]),float(g_pair[1]),flush=True)
    print("NF492 original true U''(B)",float(jet_pairs[2][0]),float(jet_pairs[2][1]),flush=True)
    print("NF492 true source alpha,beta",float(alpha_pair[0]),float(beta_pair[0]),flush=True)
    print("NF492 source jets PASS; original full signed J8 upper NF404 RH OPEN",flush=True)
if __name__=="__main__":main()
