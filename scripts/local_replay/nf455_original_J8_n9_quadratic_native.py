#!/usr/bin/env python3
"""NF455 source-certified original J8 n9-only quadratic and combined 4pz9+2z9².

Same original NF407 finite physical U, 273 frequency/order modes, exact n9
contact and original NF454 source-native full-principal p*z9.  A source-
correlated 320-jet at the genuine x9=log9-B is integrated in its SQUARE
directly, with separately charged original coefficient error and Cauchy tail.
This computes a genuine J8 *subexpression*, not the full J8 signed integral.
"""
from pathlib import Path
from fractions import Fraction as F
from flint import arb, ctx
import argparse, json, hashlib, sys
from nf415_original_cell6_I1_validated_acb import native_source,U,A,C
from nf454_original_n9_contact_native_moment import read,enclosure,B,SRC_SHA,SEAM_SHA
from nf454_original_n9_log_weighted_native import analytic_coefficients,N,R,M,QBOUND

if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)

def run(args):
    ctx.prec=args.precision
    assert ctx.prec>=3072
    source,sh=read(args.source)
    geo,gs=read(args.seams)
    jet,js=read(args.jet)
    prev,ps=read(args.nf454)
    assert (sh,gs)==(SRC_SHA,SEAM_SHA)
    assert jet["nf407_source_sha256"]==sh
    assert prev["original_source_sha256"]==sh
    assert prev["original_seams_sha256"]==gs
    assert prev["focused_numeric_exact_gates_status"]=="SUCCESS"
    assert prev["whole_J8_signed"]==prev["whole_J7_signed"]=="OPEN"
    assert prev["original_log_B9_strict"]==[
        "-3339027/1000000000000000000",
        "-3339026/1000000000000000000"]
    assert N==320 and R==F(1,40) and M==F(10)**230 and QBOUND==F(3,25)

    terms,pole,s0=native_source(source)
    assert len(terms)==273 and s0<F(1,10**700)
    assert len(source["original_selected_generator_node_orders"])==242
    assert len(source["original_exact_native_original_four_critical_coefficients_mid_radius"])==4
    assert len(source["original_source_critical_sine_frequencies"])==32
    assert all(0<f<883 and 0<=k<=13 for f,k,c in terms)
    assert sum(abs(c)*B**k for f,k,c in terms)+abs(pole)<F(10)**160

    s9=next(p for p in geo["original_prime_power_log_shifts"] if p["n"]==9)
    log9lo,log9hi=F(s9["log_lower"]),F(s9["log_upper"])
    amin,amax=2*B-log9hi,2*B-log9lo
    assert 0<amin<amax<F(3,1000)
    assert amax/R<QBOUND
    log9=arb(9).log()
    a=2*A(B)-log9
    y0=log9-A(B)
    a0,a1=enclosure(a)
    assert amin<=a0<=a1<=amax
    assert y0.is_finite()

    v=U(source).at(C(B)).real
    ucoeff=analytic_coefficients(terms,pole,y0)
    coeff=[v-ucoeff[0]]+[-ucoeff[j] for j in range(1,N)]
    assert len(coeff)==N
    scaled=[]
    powa=arb(1)
    for j in range(N):
        scaled.append(coeff[j]*powa)
        powa*=a

    # Exact analytic source polynomial ∫ V(d)² dd, V(d)=v-U(y0+d).
    # Uses the original correlated source *before* any product; all cross
    # terms among 246 generators and original pole are automatically retained.
    sq=arb(0)
    lin=arb(0)
    for j in range(N):
        lin+=scaled[j]/(j+1)
        sq+=scaled[j]*scaled[j]/(2*j+1)
        for k in range(j+1,N):
            sq+=2*scaled[j]*scaled[k]/(j+k+1)
    sq*=a
    lin*=a

    # Same accepted NF454 Cauchy bound on U(y0+d) for |d|=R:
    # Uraw < 10^160, 2*pi*f*R<139, and |y0+d|<9/8, so |U|<10^230.
    # The complete source Taylor L∞ tail on true d∈[0,a] is bounded by:
    tail=M*(QBOUND**N)/(1-QBOUND)
    assert tail<F(1,10**55)
    # Accepted NF446 real source global |U|<900, |v|<1.
    # Thus |V_mid|<901; |polynomial|<901+tail, so
    # |V_true²-P²| <= (1804+tail)*(tail+2S0)
    # uniformly, where 2S0 is the original dyadic v/U source radius.
    analytic_err=amax*(1804+tail)*tail
    coeff_err=amax*(3608+2*tail)*s0
    assert analytic_err<F(1,10**50) and coeff_err<F(1,10**690)
    square_lo,square_hi=enclosure(sq,115)
    square_lo-=analytic_err+coeff_err
    square_hi+=analytic_err+coeff_err
    assert 0<square_lo<square_hi

    # Independent n9 source zeroth-moment consistency and Jensen check.
    Llo,Lhi=enclosure(lin,110)
    Llo-=amax*tail+2*amax*s0
    Lhi+=amax*tail+2*amax*s0
    assert F(prev["original_A9_strict"][0]) < Llo<Lhi < F(prev["original_A9_strict"][1])
    jensen_lower=Lhi*Lhi/amax # negative Lhi, smallest absolute value
    assert Lhi<0 and square_lo>jensen_lower, "source-native n9 energy violates Jensen"

    w9=next(w for w in jet["all_seven_original_prime_seam_derivative_identities"] if w["prime_power"]==9)
    w0,w1=map(F,w9["c_n_positive_outward"])
    assert 0<w0<w1<1
    z9_sq_lo=2*w0*w0*square_lo
    z9_sq_hi=2*w1*w1*square_hi

    # NF454 source-native whole-original-principal p crossed n9-only z9.
    crosslo,crosshi=(F(q) for q in prev["original_full_principal_4_integral_p_z9_strict"])
    assert crosslo<crosshi<0
    partiallo,partialhi=crosslo+z9_sq_lo,crosshi+z9_sq_hi
    assert partiallo<partialhi

    return {
        "pass":"NF455",
        "standing":"COMPLETE genuine original n9-only z9 SQUARED J8 contribution and combined 4p*z9+2z9² signed subexpression; NOT full original J8 D8",
        "original_source_sha256":sh,"original_seam_sha256":gs,
        "original_nf411_jet_sha256":js,"original_nf454_custody_sha256":ps,
        "original_original_source_generators":246,
        "original_source_frequency_order_groups":273,
        "original_critical_sines":32,"original_odd_sinh_retained":True,
        "native_precision_bits":ctx.prec,
        "actual_original_n9_overlap_a_outward":[str(a0),str(a1)],
        "original_n9_real_source_square_integral_outward":[str(square_lo),str(square_hi)],
        "original_n9_2_integral_z9_squared_outward":[str(z9_sq_lo),str(z9_sq_hi)],
        "original_n9_full_principal_cross_4int_pz9_import":[str(crosslo),str(crosshi)],
        "original_n9_partial_D8_four_pz9_plus_two_z9_square_outward":[str(partiallo),str(partialhi)],
        "source_320_taylor_N":N,
        "source_complex_Cauchy_M":str(M),
        "source_disk_R":str(R),
        "source_dimensionless_ratio_strict":str(QBOUND),
        "original_source_Cauchy_tail_bound":str(tail),
        "source_square_analytic_remainder":str(analytic_err),
        "source_square_coefficient_radius_remainder":str(coeff_err),
        "original_n9_linear_A9_independent_source_native_overlap":True,
        "original_n9_quadratic_Jensen_lower_exact":str(jensen_lower),
        "original_source_square_all_generator_cross_terms_retained":True,
        "entire_original_J8_D8":"OPEN",
        "entire_original_J7_D7":"OPEN",
        "missing_original_background":"4int(p*z0)+4int(z0*z9)+2int(z0^2); z=z0+z9",
        "NF410_NF404_global":"OPEN","W_ODD_NEG":"OPEN","RH":"OPEN",
        "next":"NF456 source correlated full original z0 arch+six-prime background against genuine n9 source, then full signed J8/J7"
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--source",default="notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json")
    ap.add_argument("--seams",default="notes/data/provisional/NF406_original_prime_support_partition_exact.json")
    ap.add_argument("--jet",default="notes/data/provisional/NF411_original_source_boundary_jet.json")
    ap.add_argument("--nf454",default="notes/data/provisional/NF454_original_J8_n9_contact_log_signed_custody.json")
    ap.add_argument("--precision",type=int,default=4096)
    ap.add_argument("--output",required=True)
    args=ap.parse_args()
    d=run(args)
    out=Path(args.output);out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(d,indent=2)+"\n")
    q=d["original_n9_real_source_square_integral_outward"]
    z=d["original_n9_2_integral_z9_squared_outward"]
    p=d["original_n9_partial_D8_four_pz9_plus_two_z9_square_outward"]
    print("NF455 true original n9 ∫ V²",*[float(F(x)) for x in q],flush=True)
    print("NF455 true original n9 2∫z9²",*[float(F(x)) for x in z],flush=True)
    print("NF455 original n9 partial D8 = 4∫p z9+2∫z9²",*[float(F(x)) for x in p],flush=True)
    print("NF455 complete D7,D8, original NF404, W-ODD-NEG RH OPEN",flush=True)
if __name__=="__main__":main()
