#!/usr/bin/env python3
"""NF489 independent FIRST full original physical J8 boundary value.

Reuse the 11 ACCEPTED ORIGINAL NF482 native 4096-bit 1200-jet source
coefficient blocks (run 42506659220), evaluate their joint same-source
polynomial at physical t=1 (x=549/500) exactly as Fractions, pay the
preaccepted NF482 original uniform z error 1e-29, and construct the
ACTUAL physical principal and signed pointwise density (not integral).

This is an independently obtained numerical point to CROSS-CHECK the new
NF489 full NF446 compact kernel source-native calculation. Not a signed
J8 cell integral, not NF404.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import argparse,json,hashlib,sys
from verify_nf488_original_J8_terminal_four_moment_source_gate_exact import Iv,arb_ball,log550
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
SRC="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAM="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
PRIMES=(2,3,4,5,7,8,9)
B=F(11,10);D=F(1,500);X=B-D
def load(p):
    s=Path(p).read_bytes()
    return json.loads(s),hashlib.sha256(s).hexdigest()
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--input-dir",required=True)
    ap.add_argument("--output",required=True)
    args=ap.parse_args()
    original,os=load("notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json")
    support,ss=load("notes/data/provisional/NF406_original_prime_support_partition_exact.json")
    nf482,cs=load("notes/data/provisional/NF482_original_first_J8_irrational_n9_source_signed_custody.json")
    nf411,js=load("notes/data/provisional/NF411_original_source_boundary_jet.json")
    nf450,zs=load("notes/data/provisional/NF450_original_B_complete_Laplace_native_sign_custody_index.json")
    assert os==nf482["original_nf407_source_sha256"]==SRC
    assert ss==nf482["original_nf406_seams_sha256"]==SEAM
    assert nf482["original_J8_first_independent_source_certified"]
    assert nf482["source_exact_archive"]["conclusion"]=="SUCCESS"
    assert nf482["source_native_CI"]["first_native_11_source_mode_producers_run"]==42506659220
    assert nf482["source_exact_archive"]["run_id"]==42510017106
    assert nf482["original_true_source_uniform_z_error_strict_upper"]=="1e-29"
    assert nf411["nf407_source_sha256"]==nf450["source_SHA256"]==SRC
    names=["nf482a-central.json","nf482a-primes.json"]+[
        f"nf482a-images-{m}-{m+2000}.json" for m in range(0,18000,2000)]
    assert len(names)==11
    polys=[]
    shas=[]
    midcoeff=[]
    maximum_sum_width=F(0)
    for i,n in enumerate(names):
        f=Path(args.input_dir)/n
        record,rsha=load(f)
        assert record["pass"]=="NF482-A"
        assert record["original_nf407_source_sha256"]==SRC
        assert record["original_nf406_seams_sha256"]==SEAM
        assert record["native_bits"]==4096 and record["polynomial_degree"]==1199
        assert record["physical_panel"]==["log9-B","549/500"]
        assert record["center"]=="686/625" and record["halfwidth"]=="1/2500"
        assert record["source_radii_lt"]=="1e-700"
        assert record["part"]==("central" if i==0 else "primes" if i==1 else "images")
        if i>=2:assert (record["original_image_index_start"],record["original_image_index_stop"])==(2000*(i-2),2000*(i-1))
        arr=record["coefficient_interval_balls"]
        assert len(arr)==1200
        # Exact original source-correlation contraction at one real
        # physical endpoint t=1; no 273-mode absolute products.
        lo=F(0);hi=F(0)
        for row in arr:
            a,b=map(F,row)
            assert a<=b
            lo+=a;hi+=b
        polys.append(Iv(lo,hi))
        shas.append({"name":n,"sha256":rsha})
    # Sum EXACT original 11 full-source polynomial endpoint intervals.
    projected=sum(polys,Iv(0))
    assert projected.width()<F(1,10**35),"METHOD STOP: legacy original coefficient source enclosure width"
    # Accepted NF482 physical original exact source analytic Cauchy,
    # 18k true matched-image omitted all-m tail at d>=1/500 and
    # original dyadic/seven-prime source coefficients are ALL paid
    # by the unchanged source-certified 1e-29 uniform z error.
    err=F(1,10**29)
    z=projected+Iv(-err,err)
    assert z.width()<F(1,10**27)
    assert z.lo>-25000 and z.hi<25000
    # Exact original first-panel endpoint t=1 -> x=549/500.
    assert F(686,625)+F(1,2500)==X
    # Original J8 all seven genuine n9-active principal source v,C8.
    fee=F(1,10**100)
    assert F(nf411["native_source_derivative_uncertainty_exact_upper"])<fee
    v=arb_ball(nf411["original_original_source_value_at_B_arb"])+Iv(-fee,fee)
    alpha=-(arb_ball(nf411["original_original_source_derivative_at_B_arb"]))/2+Iv(-fee,fee)
    C=Iv(0);weights=[]
    for row in nf411["all_seven_original_prime_seam_derivative_identities"]:
        n=row["prime_power"]
        assert n in PRIMES
        ca,cb=map(F,row["c_n_positive_outward"])
        assert 0<ca<=cb<1
        C+=Iv(ca,cb)
        weights.append(n)
    assert tuple(weights)==PRIMES
    h=log550()
    assert F(6)<h.lo<=h.hi<F(7)
    p=v*(C+h/2)
    density=4*p*z+2*z**2
    zb=Iv(*map(F,nf450["complete_z_B_outward_24_decimal"]))
    R=z-zb-alpha*D*h
    assert z.lo>-F(100) and z.hi<F(100) # honest native source control
    # NF487 strict analytically inherited source remainder bound.
    assert R.lo<F(13000)*D and R.hi>-F(13000)*D
    sign="POSITIVE" if z.lo>0 else "NEGATIVE" if z.hi<0 else "UNDECIDED"
    ds="POSITIVE" if density.lo>0 else "NEGATIVE" if density.hi<0 else "UNDECIDED"
    out={
      "pass":"NF489-original-NF482-source-independent-boundary",
      "standing":"EXACT original source 11 accepted 4096bit NF482 polynomial blocks at true J8 x=549/500; genuine physical signed density at ONE point (not an integral)",
      "original_nf407_source_sha256":SRC,
      "original_nf406_seams_sha256":SEAM,
      "source_original_NF482_first_panel_custody_sha256":cs,
      "source_original_NF411_source_jet_sha256":js,
      "source_original_NF450_endpoint_custody_sha256":zs,
      "original_11_native_source_coeff_fragment_sha256":shas,
      "original_true_J8_x":"549/500",
      "real_original_source_first_panel_t":"1",
      "original_source_11_full_1200_jets_used":True,
      "source_original_1200_coeff_sum_interval_width":str(projected.width()),
      "original_NF482_accepted_true_uniform_z_error_overcharge":"1e-29",
      "actual_original_J8_physical_z_x_outward":z.raw(),
      "actual_original_J8_physical_z_x_decimal":z.decimal(48),
      "actual_original_J8_physical_z_sign":sign,
      "original_principal_p_x_outward":p.raw(),
      "actual_original_J8_signed_density_4pz_plus_2z2_x_outward":density.raw(),
      "actual_original_J8_signed_density_4pz_plus_2z2_x_decimal":density.decimal(48),
      "actual_original_J8_signed_density_sign":ds,
      "original_physical_cusp_alpha_outward":alpha.raw(),
      "original_true_joint_physical_R_x_outward":R.raw(),
      "original_true_joint_physical_R_x_decimal":R.decimal(48),
      "original_full_J8_signed_integral_upper":"OPEN",
      "NF404":"OPEN","W_ODD_NEG":"OPEN","RH":"OPEN",
      "next_bold":"Compare this independent NF482 true original physical boundary point with new NF489 original NF446 compact integrator; then correlated signed J8 terminal integration, not a point-sign projection."
    }
    dest=Path(args.output);dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(out,indent=2)+"\n")
    print("NF489 accepted-NF482 original full 11-block source boundary z at x=549/500",*z.decimal(30),sign,flush=True)
    print("NF489 genuine physical J8 signed point density",*density.decimal(30),ds,flush=True)
    print("NF489 original physical R(1/500)",*R.decimal(30),flush=True)
    print("NF489 genuine original complete J8 signed integral/NF404/W-ODD-NEG/RH OPEN",flush=True)
if __name__=="__main__":main()
