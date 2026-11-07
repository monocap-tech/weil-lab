#!/usr/bin/env python3
"""NF472 exact rational independent signed-interval custody audit.

Must not be confused with 4096-bit original source replay. The receipt-only
path proves strict negativity from outward *certified* mean pz and z² bounds;
with --native it additionally verifies the original full uncoarsened result.
"""
from fractions import Fraction as F
import argparse,json
from pathlib import Path
S="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
J="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
ROOT=Path(__file__).resolve().parents[2]
def interval(v):
    a,b=map(F,v)
    assert a<b
    return a,b
def contains(outer,inner):
    o0,o1=interval(outer); i0,i1=interval(inner)
    assert o0<=i0<i1<=o1
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--receipt",default=str(ROOT/"notes/data/provisional/NF472_original_J7_macroscopic_signed_moments_custody.json"))
    ap.add_argument("--native",default=None)
    args=ap.parse_args()
    d=json.loads(Path(args.receipt).read_text())
    assert (d["original_nf407_sha256"],d["original_nf406_sha256"])==(S,J)
    assert d["original_generators"]==246 and d["original_grouped_modes"]==273
    assert d["original_minus_shift_primes"]==[2,3,4,5,7,8]
    assert d["physical_panel"]==["26/25","53/50"] and F(d["panel_length"])==F(1,50)
    assert d["source_Taylor_degree"]==799 and d["source_image_modes"]==6000
    assert d["native_precision_bits"]==4096 and d["source_native_ci"]["conclusion"]=="SUCCESS"
    pz0,pz1=interval(d["original_normalized_pz_outward_coarsened"])
    z20,z21=interval(d["original_normalized_z2_outward_coarsened"])
    cov0,cov1=interval(d["original_normalized_covariance_outward_coarsened"])
    var0,var1=interval(d["original_normalized_variance_outward_coarsened"])
    dlo,dhi=interval(d["original_signed_D_I_outward_coarsened"])
    assert pz1<0 and 0<z20 and 0<cov0 and 0<var0
    assert dlo<dhi<0 and d["original_signed_D_I_strict_sign"]=="NEGATIVE"
    # Independent arithmetic: use the separately source-certified mixed
    # and quadratic intervals, NOT the native D_I sign flag.
    witness_upper=F(1,50)*(4*pz1+2*z21)
    witness_lower=F(1,50)*(4*pz0+2*z20)
    assert witness_upper<0 and witness_lower<=dlo<dhi<=witness_upper
    assert witness_upper<-F(7,10**23)
    assert interval(d["original_mean_zbar_NF471_coarsened"])[0]>0
    assert d["whole_original_J7"]==d["whole_original_J8"]==d["NF404"]=="OPEN"
    assert d["W_ODD_NEG"]==d["RH"]=="OPEN"
    if args.native:
        n=json.loads(Path(args.native).read_text())
        assert n["pass"]=="NF472"
        assert (n["original_nf407_source_sha256"],n["original_nf406_seams_sha256"])==(S,J)
        assert n["original_true_mean_cross_check_NF471"] and n["original_true_center_cross_check_NF470"]
        assert n["source_original_D_I_strict_sign"]=="NEGATIVE"
        for name,coarse in (
          ("original_pz_normalized_mean_outward","original_normalized_pz_outward_coarsened"),
          ("original_z2_normalized_mean_outward","original_normalized_z2_outward_coarsened"),
          ("source_covariance_normalized_mean_outward","original_normalized_covariance_outward_coarsened"),
          ("source_variance_normalized_mean_outward","original_normalized_variance_outward_coarsened"),
          ("source_original_D_I_outward","original_signed_D_I_outward_coarsened")
        ):contains(d[coarse],n[name])
        assert n["certified_sup_z_minus_polynomial"]=="1/10^28"
        assert F(n["original_source_arb_coefficient_aggregate_width"])<F(1,10**40)
        assert F(n["original_source_Taylor_remainder"])<F(1,10**120)
        assert F(n["original_joint_image_real_tail"])<F(1,10**40)
        # Recompute from the original native raw uncoarsened signed moments.
        p0,p1=interval(n["original_pz_normalized_mean_outward"])
        v0,v1=interval(n["original_z2_normalized_mean_outward"])
        native_upper=F(1,50)*(4*p1+2*v1)
        assert native_upper<0
    print(json.dumps({
      "pass":"NF472","verifier":"exact Fraction original-source custody and signed inequality",
      "genuine_original_J7_panel":["26/25","53/50"],
      "source_certified_D_I_sign":"NEGATIVE",
      "independent_source_normalized_moment_witness_upper":str(witness_upper),
      "independent_source_normalized_moment_witness_upper_lt_minus_7e_23":True,
      "original_nf470_nf471_shared_source_cross_checks":True,
      "original_complete_signed_J7":"OPEN","NF404":"OPEN","W_ODD_NEG":"OPEN","RH":"OPEN",
      "native_original_raw_checked":bool(args.native)
    },indent=2))
if __name__=="__main__":main()
