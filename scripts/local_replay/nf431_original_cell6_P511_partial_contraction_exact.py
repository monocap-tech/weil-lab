#!/usr/bin/env python3
"""NF431: SHA-pinned exact Fraction replay of ORIGINAL 512-mode PARTIAL polynomial.

Requires SHA-pinned NF428 source-correlation coefficient + principal p moment
artifacts, and NF429 2999 ORIGINAL irrational-cell raw dx moments.
This certifies P511 polynomial contraction, NEVER the actual full z integral.
"""
import argparse
import hashlib
import json
import zipfile
from fractions import Fraction as F
from pathlib import Path

Z_SHA = "d4e812d685813f8711aa4dce6422df27c301789cc23e944094c518e2f9247c3c"
Z_HIGH_SHA = "10c93ca7f4b7779334fd686ef1fd348f79fe873068af3897c2a936487dbdcbf8"
P_SHA = "bc7c98e1ac16b1147eaff91f11a6bf33ce4326d6237b5728c1987cec39f8cf25"
J_SHA = "8f83c9658dec776b84f9d013eb22d7ed1533a02e464ba975553c76210435e1d1"
N=512
ZERO=(F(0),F(0))
def load(path, expected):
    raw=Path(path).read_bytes()
    if zipfile.is_zipfile(path):
        with zipfile.ZipFile(path) as z:
            names=[v for v in z.namelist() if v.endswith(".json")]
            assert len(names)==1
            raw=z.read(names[0])
    digest=hashlib.sha256(raw).hexdigest()
    assert digest==expected, ("source artifact digest mismatch",digest,expected)
    return json.loads(raw)
def ib(v):
    lo,hi=map(F,v);assert lo<=hi
    return lo,hi
def add(x,y):return x[0]+y[0],x[1]+y[1]
def mul(x,y):
    p=[x[0]*y[0],x[0]*y[1],x[1]*y[0],x[1]*y[1]]
    return min(p),max(p)
def scale(q,x):
    return (q*x[0],q*x[1]) if q>=0 else (q*x[1],q*x[0])
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--z",required=True)
    ap.add_argument("--z-high",required=True)
    ap.add_argument("--p",required=True)
    ap.add_argument("--j",required=True)
    ap.add_argument("--output",required=True)
    args=ap.parse_args()
    z=load(args.z,Z_SHA);h=load(args.z_high,Z_HIGH_SHA)
    p=load(args.p,P_SHA);j=load(args.j,J_SHA)
    assert z["pass"]==p["pass"]=="NF428" and h["pass"]=="NF431" and j["pass"]=="NF429"
    assert z["source_sha256"]==h["source_sha256"]==p["nf407_original_full_source_sha256"]==j["nf407_original_source_sha256"]
    assert z["seams_sha256"]==h["seams_sha256"]==p["nf406_original_seams_sha256"]==j["nf406_original_seams_sha256"]
    assert z["W_ODD_NEG"]==z["RH"]==h["W_ODD_NEG"]==h["RH"]==p["W_ODD_NEG"]==p["RH"]==j["W_ODD_NEG"]==j["RH"]=="OPEN"
    assert z["original_true_cell6"]==h["original_true_cell6"]==p["original_x_domain"]==j["original_actual_log7_log8_cell6"]
    assert z["number_of_certified_low_mode_coefficients"]==256
    assert (h["mode_start_inclusive"],h["mode_stop_exclusive"])==(256,N)
    assert h["number_of_certified_new_high_mode_coefficients"]==256
    assert h["original_analytic_global_transfer_pointwise_NF416_overlap_pass"]
    assert h["original_exact_NF404_dyadic_center"]==z["original_exact_NF404_dyadic_center"]
    assert p["all_1500_source_signed_chebyshev_moments_certified"]
    assert len(j["original_cell6_raw_Chebyshev_dx_moments_n0_to_n2998"])==2999
    assert z["original_all_five_post_seam_primes_retained"]==h["original_all_five_post_seam_primes_retained"]==p["original_signed_primes_on_cell6"]==[2,3,4,5,7]
    assert z["original_two_neither_branches"]==h["original_two_neither_branches"]==p["original_inactive_prime_branches"]==[8,9]
    c=z["coefficients"]+h["coefficients"]
    assert [q["n"] for q in c]==list(range(N))
    a=[ib(q["true_original_cell6_fixed_branch_coefficient_outward_interval"]) for q in c]
    pm=[ib(q) for q in p["original_signed_p_chebyshev_moments_n0_to_n1499"][:N]]
    jm=[ib(q) for q in j["original_cell6_raw_Chebyshev_dx_moments_n0_to_n2998"][:2*N-1]]
    pz=ZERO;z2=ZERO
    for x,y in zip(a,pm):pz=add(pz,mul(x,y))
    for i in range(N):
        for k in range(i,N):
            b=mul(a[i],a[k])
            moment=scale(F(1,2),add(jm[i+k],jm[k-i]))
            z2=add(z2,scale(1 if i==k else 2,mul(b,moment)))
    signed=add(scale(4,pz),scale(2,z2))
    assert pz[1]<0 and z2[0]>0 and signed[1]<0
    assert z2[1]-z2[0]<F(1,10**40)
    assert pz[1]-pz[0]<F(1,10**40)
    assert signed[1]-signed[0]<F(1,10**40)
    result={
      "pass":"NF431",
      "standing":"EXACT ORIGINAL-SOURCE PARTIAL CHEBYSHEV POLYNOMIAL P511 CONTRACTION; TRUE z INTEGRAL OPEN",
      "original_nf428_z256_json_sha256":Z_SHA,
      "original_nf431_z256_to511_json_sha256":Z_HIGH_SHA,
      "original_nf428_p1500_json_sha256":P_SHA,
      "original_nf429_j2999_json_sha256":J_SHA,
      "source_sha256":z["source_sha256"],
      "seams_sha256":z["seams_sha256"],
      "original_partial_z_modes":N,
      "original_required_z_modes_for_true_cell6":1265,
      "original_missing_z_modes":753,
      "original_P511_pz_outward_interval":list(map(str,pz)),
      "original_P511_squared_outward_interval":list(map(str,z2)),
      "original_P511_nonprincipal_signed_2z2_plus_4pz_outward_interval":list(map(str,signed)),
      "actual_original_cell6_integral_certified":False,
      "original_NF404_full_scalar_decided":False,
      "W_ODD_NEG":"OPEN","RH":"OPEN"
    }
    out=Path(args.output);out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2)+"\n")
    print("NF431 exact original-source partial P511 pz, z2 and signed contraction PASS")
    print("TRUE J6 z integral OPEN: source n512..1264 not known")
if __name__=="__main__":main()
