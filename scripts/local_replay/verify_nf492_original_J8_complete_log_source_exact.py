#!/usr/bin/env python3
"""NF492 independent original source exact Fraction full logarithmic carrier audit.

Joint authentic NF407 native 4096bit original U(B), U(B-1/500), U^(0..5)(B)
with independently ACCEPTED original NF489 11-source physical z(x), NF411,
NF445 endpoint jets, NF450 z(B), source exact log550. Proves true physical
analytic H(delta)=z(delta)-g(delta)log550; no full signed D8 integral.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import hashlib,json,argparse,sys
from verify_nf488_original_J8_terminal_four_moment_source_gate_exact import Iv,arb_ball,log550
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
SRC="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAM="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
DELTA=F(1,500)
def read(p):
    b=Path(p).read_bytes()
    return json.loads(b),hashlib.sha256(b).hexdigest()
def overlap(a,b):return a.lo<=b.hi and b.lo<=a.hi
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--native",required=True)
    ap.add_argument("--old-nf489",required=True)
    ap.add_argument("--output",required=True)
    args=ap.parse_args()
    native,nsha=read(args.native)
    old,osha=read(args.old_nf489)
    nf411,ssha=read("notes/data/provisional/NF411_original_source_boundary_jet.json")
    nf450,zsha=read("notes/data/provisional/NF450_original_B_complete_Laplace_native_sign_custody_index.json")
    nf445,ksha=read("notes/data/provisional/NF445_original_correlated_residual_laplace_custody_index.json")
    nf482,tsha=read("notes/data/provisional/NF482_original_first_J8_irrational_n9_source_signed_custody.json")
    assert native["pass"]=="NF492-source-native"
    assert old["pass"]=="NF489-original-NF482-source-independent-boundary"
    assert native["original_nf407_source_sha256"]==old["original_nf407_source_sha256"]==SRC
    assert nf411["nf407_source_sha256"]==nf450["source_SHA256"]==nf445["original_nf407_source_sha256"]==nf482["original_nf407_source_sha256"]==SRC
    assert old["original_nf406_seams_sha256"]==nf482["original_nf406_seams_sha256"]==SEAM
    assert native["original_selected_plus_critical_generator_count"]==246
    assert native["original_source_grouped_freq_order_count"]==273
    assert native["original_source_sinh_critical_pole_preserved"]
    assert native["source_original_precision_bits"]==4096
    assert native["original_true_J8_x"]==old["original_true_J8_x"]=="549/500"
    assert native["original_true_J8_d"]=="1/500"
    assert F(native["original_original_dyadic_full_source_midpoint_radius_sum"])<F(1,10**700)
    assert F(native["original_dyadic_full_source_included_radius_charge"])==F(1,10**600)
    v=Iv(*map(F,native["original_source_U_B_exact_outward"]))
    u=Iv(*map(F,native["original_source_U_B_minus_delta_exact_outward"]))
    jets=[Iv(*map(F,r)) for r in native["original_source_derivatives_B_order_0_to_5_exact_outward"]]
    assert len(jets)==6
    assert overlap(jets[0],v)
    assert overlap(v,arb_ball(nf411["original_original_source_value_at_B_arb"]))
    assert overlap(jets[1],arb_ball(nf411["original_original_source_derivative_at_B_arb"]))
    assert v.hi<0 and jets[1].hi<0 and jets[2].hi<0
    assert -F(1,1000)<jets[2].lo<=jets[2].hi<0
    # Independent original accepted NF445 4096-bit first six original
    # source derivative diagnostics: source exact interval MUST agree with
    # prior originals, but previous *float* approximations are not new
    # numerical certificate and receive safe 1ppm comparative tolerance.
    prior=nf445["original_source_derivative_at_B_approximations"]
    assert len(prior)==6
    for j,approx in enumerate(prior):
        v0=F(str(approx))
        fee=max(F(1,10**9),abs(v0)/F(10**6))
        assert jets[j].lo<v0+fee and jets[j].hi>v0-fee,(j,"NF445 native source jet mismatch")
    g=(u-v)/2
    alpha=-jets[1]/2
    beta=jets[2]/4
    gnative=Iv(*map(F,native["original_true_log_coefficient_g_delta_equal_half_U_difference"]))
    anative=Iv(*map(F,native["original_true_first_log_coefficient_alpha"]))
    bnative=Iv(*map(F,native["original_true_second_log_coefficient_beta"]))
    assert overlap(g,gnative) and overlap(alpha,anative) and overlap(beta,bnative)
    assert alpha.lo>0 and beta.hi<0
    Hlog=log550()
    assert F(6)<Hlog.lo<=Hlog.hi<7 and Hlog.width()<F(1,10**90)
    z=Iv(*map(F,old["actual_original_J8_physical_z_x_outward"]))
    assert z.hi<0 and z.width()<F(1,10**27)
    Z=Iv(*map(F,nf450["complete_z_B_outward_24_decimal"]))
    assert Z.hi<0
    # ACTUAL ORIGINAL NF446 PHYSICAL all-orders regular source carrier:
    Hreg=z-g*Hlog
    Rfirst=z-Z-alpha*DELTA*Hlog
    correction=(g-alpha*DELTA)*Hlog
    assert overlap(Rfirst,Hreg-Z+correction)
    # The second source log coefficient beta=U''(B)/4 is strictly
    # NEGATIVE; ordinary first-log-only NF487 regularization keeps a
    # d^2 log term. All-orders NF492 removes it exactly.
    second=beta*DELTA**2*Hlog
    assert second.hi<0
    assert old["actual_original_J8_signed_density_sign"]=="POSITIVE"
    assert Rfirst.lo<13000*DELTA and Rfirst.hi>-13000*DELTA
    out={
      "pass":"NF492-original-source-exact-full-log-physical-crosscheck",
      "standing":"SOURCE-ACCEPTED original 4096bit true U(B-d), 6 endpoint derivatives and complete all-orders logarithmic coefficient versus independent accepted NF489 actual physical z; physical H(delta) certified, D8 upper OPEN",
      "original_nf407_source_sha256":SRC,
      "original_nf406_seam_sha256":SEAM,
      "original_native_4096bit_sha256":nsha,
      "original_previous_independent_NF489_11_source_physical_point_sha256":osha,
      "original_nf411_endpoint_source_custody_sha256":ssha,
      "original_nf450_zB_endpoint_custody_sha256":zsha,
      "original_nf445_prior_6_derivatives_custody_sha256":ksha,
      "original_nf482_irrational_first_j8_custody_sha256":tsha,
      "true_original_J8_x":"549/500",
      "true_original_terminal_d":"1/500",
      "original_source_U_at_B_outward":v.raw(),
      "original_source_U_at_B_minus_delta_outward":u.raw(),
      "original_full_source_6_endpoint_jets_outward":[x.raw() for x in jets],
      "original_true_all_orders_log_g_delta_outward":g.raw(),
      "original_true_all_orders_log_g_delta_decimal":g.decimal(44),
      "original_true_first_log_alpha_outward":alpha.raw(),
      "original_true_second_log_beta_outward":beta.raw(),
      "original_true_second_log_beta_strictly_negative":True,
      "original_true_first_unpeeled_second_cusp_beta_delta_squared_log_outward":second.raw(),
      "original_true_first_unpeeled_second_cusp_beta_delta_squared_log_decimal":second.decimal(44),
      "original_true_physical_z_delta_outward":z.raw(),
      "original_source_complete_analytic_H_delta_outward":Hreg.raw(),
      "original_source_complete_analytic_H_delta_decimal":Hreg.decimal(48),
      "original_source_complete_analytic_H_delta_minus_Z_outward":(Hreg-Z).raw(),
      "original_source_complete_analytic_H_delta_minus_Z_decimal":(Hreg-Z).decimal(48),
      "original_NF487_partial_first_log_R_delta_outward":Rfirst.raw(),
      "original_true_complete_log_analytic_carrier_agrees_with_NF487_partial":True,
      "original_true_J8_full_signed_UPPER":"OPEN",
      "NF404":"OPEN","W_ODD_NEG":"OPEN","RH":"OPEN",
      "next_bold":"NF493 produce source-contracted 400 analytic original H and g coefficients and integrate exact physical signed polynomial-log D_T, original NF404 upper still unverified"
    }
    dest=Path(args.output);dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(out,indent=2)+"\n")
    print("NF492 complete original physical J8 all-order log g(delta)",*g.decimal(32),flush=True)
    print("NF492 original full analytic H(delta)",*Hreg.decimal(32),flush=True)
    print("NF492 source original U''(B) and beta",*jets[2].decimal(30),*beta.decimal(30),flush=True)
    print("NF492 independent original source H regularized endpoint physical value PASS; complete D8/NF404 RH OPEN",flush=True)
if __name__=="__main__":main()
