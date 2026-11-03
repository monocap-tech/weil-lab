#!/usr/bin/env python3
"""NF457 original complete signed J8 COLLAR 10x NF452, source-rigorous.

Use the already certified original exact endpoint-matched whole-J8 modulus
from source-native NF457:
 |z(B-d)-Z| < d*(9802+200*log((2B-d)/d)).
On 0<d<=1e-14, rigorously bound by d*(10002+200*log(B/d)).
Integrate all principal p*z and z^2 analytically with atanh Fraction logs,
original NF411 seven actual prime weights, original NF450 Z=z(B), original
source-native U(B) receipt. Genuine original physical cell, not finite F.
"""
import argparse,json,sys,hashlib
from pathlib import Path
from fractions import Fraction as Q

if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
B=Q(11,10);DELTA=Q(1,10**14)
SRC_SHA="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAMS_SHA="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"

def read(p):
    raw=Path(p).read_bytes()
    return json.loads(raw),hashlib.sha256(raw).hexdigest()

def log_bounds(t,N=64):
    assert isinstance(t,Q) and t>1
    r=(t-1)/(t+1)
    v=Q(0);term=r
    for j in range(N):
        v+=Q(2)*term/(2*j+1)
        term*=r*r
    e=Q(2)*term/((2*N+1)*(1-r*r))
    assert 0<e<Q(1,10**58) if t==2 else 0<e
    return v,v+e

def plus(*x):
    return sum(x,Q(0))

def run(args):
    src,sha=read(args.source)
    seams,gs=read(args.seams)
    jet,js=read(args.jet)
    endpoint,zs=read(args.nf450)
    old,os=read(args.nf452)
    full,fs=read(args.nf457)
    assert (sha,gs)==(SRC_SHA,SEAMS_SHA)
    assert src["original_dimension"]==242
    assert len(src["original_exact_native_original_four_critical_coefficients_mid_radius"])==4
    assert len(src["original_source_critical_sine_frequencies"])==32
    assert jet["nf407_source_sha256"]==sha
    assert endpoint["source_SHA256"]==sha and endpoint["seams_SHA256"]==gs
    assert endpoint["original_CI_result"]=="SUCCESS"
    assert old["original_source_sha256"]==sha and old["original_seams_sha256"]==gs
    assert old["focused_CI_result"]=="SUCCESS"
    assert DELTA==10*Q(old["collar_delta"])
    assert full["source_sha256"]==sha and full["seams_sha256"]==gs
    assert full["original_source_generator_count"]==246
    assert full["original_frequency_order_groups"]==273
    assert full["original_matched_remainder_full_J8_strict"]=="|R_J(d)|<8200*d"
    assert full["original_unconditional_full_J8_complete_z_modulus"]=="|z(B-d)-Z|<d*(9802+200*log((2B-d)/d))"
    assert full["whole_original_J8_signed"]=="OPEN" and full["RH"]=="OPEN"
    assert src["W_ODD_NEG"]=="OPEN"
    seam9=next(x for x in seams["original_prime_power_log_shifts"] if x["n"]==9)
    dmaxlo=2*B-Q(seam9["log_upper"])
    assert 0<DELTA<dmaxlo<Q(3,1000)
    v0,v1=map(Q,full["original_U_B_source_outward"])
    assert -Q(117,10**13)<v0<v1<-Q(116,10**13)
    Z0,Z1=map(Q,endpoint["complete_z_B_outward_24_decimal"])
    assert Z0<Z1<0
    weights=[(x["prime_power"],tuple(map(Q,x["c_n_positive_outward"]))) for x in jet["all_seven_original_prime_seam_derivative_identities"]]
    assert tuple(n for n,_ in weights)==(2,3,4,5,7,8,9)
    C0=sum((bounds[0] for n,bounds in weights),Q(0))
    C1=sum((bounds[1] for n,bounds in weights),Q(0))
    assert Q(7,2)<C0<C1<4

    # log(B/delta)=log(11/10)+14log(5/4)+42log(2).
    # No giant atanh argument, no float log; each one has 64 exact terms.
    l11=log_bounds(Q(11,10))
    l54=log_bounds(Q(5,4))
    l2=log_bounds(Q(2))
    Llo=l11[0]+14*l54[0]+42*l2[0]
    Lhi=l11[1]+14*l54[1]+42*l2[1]
    assert 32<Llo<Lhi<34
    assert Lhi+ l2[1] <34 # log(2B/delta) exact upper

    # Monotonicity on (0,delta]: d*(A+C*log(B/d)) increasing because
    # derivative A+C*(log(B/d)-1)>0. The original log((2B-d)/d)
    # is strictly < log(B/d)+log2 < log(B/d)+1.
    A=Q(10002)
    C=Q(200)
    I0=DELTA**2/2
    I1=I0*(Lhi+Q(1,2))
    I2=I0*(Lhi*Lhi+Lhi+Q(1,2))
    A1=A*I0+C*I1
    Mstar=DELTA*(A+C*Lhi)
    assert Mstar<Q(17,10**11)
    # Coarse endpoint-decay sign check on all of 0<d<=delta.
    assert Z1+Mstar<-Q(27,10**11)
    assert -(Z0-Mstar)<Q(61,10**11) # |z|<6.1e-10

    # Same actual original NF452 signed functional, now delta=1e-14.
    # D0=2delta*vZ*(L+1+2C)+2delta Z².
    D0lo=2*DELTA*v1*Z1*(Llo+1+2*C0)+2*DELTA*Z1*Z1
    D0hi=2*DELTA*v0*Z0*(Lhi+1+2*C1)+2*DELTA*Z0*Z0
    assert 0<D0lo<D0hi
    # Original z modulus e(d) bounded by M(d)=d*(A+C*log(B/d)).
    # Exact moments Ij=∫_0^delta d*log^j(B/d) dd.
    Ap=(-v0)*(C*I2/2+(A/2+C*C1)*I1+A*C1*I0)
    R=4*Ap+4*(-Z0)*A1+2*Mstar*A1
    assert 0<R<D0lo
    dlo,dhi=D0lo-R,D0hi+R
    assert Q(54,10**34)<dlo<dhi<Q(106,10**34)
    # Source-coefficient uncertainties are part of the original
    # NF457 native v source ball and accepted NF450 Z interval.
    # The actual signed collar includes z² (not just its pz cross).
    return {
      "pass":"NF457",
      "standing":"ACCEPTED if focused source-native plus Fraction CI pass: original complete J8 d=1e-14 signed collar, full J8 signed OPEN",
      "original_source_SHA256":sha,"original_seams_SHA256":gs,
      "original_nf411_source_jet_SHA256":js,
      "original_nf450_endpoint_custody_SHA256":zs,
      "original_nf452_prior_small_collar_SHA256":os,
      "original_nf457_matched_source_native_JSON_SHA256":fs,
      "original_generators":246,"original_frequency_order_groups":273,
      "original_collar_width":str(DELTA),
      "original_collar_is_10x_NF452":True,
      "original_physical_J8_original_n9_active":True,
      "original_rational_64term_logs_only":True,
      "original_L_log_B_over_delta_outward":[str(Llo),str(Lhi)],
      "original_original_v_source_outward":[str(v0),str(v1)],
      "original_original_zB_NF450_outward":[str(Z0),str(Z1)],
      "original_seven_prime_weight_sum_outward":[str(C0),str(C1)],
      "original_matched_modulus_used":"|z(B-d)-z(B)|<d*(9802+200*log((2B-d)/d))",
      "original_relaxed_monotone_modulus":"M(d)=d*(10002+200*log(B/d))",
      "original_uniform_source_z_strict_negative_on_entire_extended_collar":True,
      "original_p_strict_negative_on_entire_extended_collar":True,
      "original_original_D0_analytic_model_outward":[str(D0lo),str(D0hi)],
      "original_pz_z2_integral_error_upper_exact":str(R),
      "original_complete_J8_extended_collar_D_strict_outward":[str(dlo),str(dhi)],
      "original_acceptance_gate":"5.4e-33 < D_{J8,collar d=1e-14} < 1.06e-32",
      "whole_original_J8_signed":"OPEN","whole_original_J7_signed":"OPEN",
      "NF404_global":"OPEN","W_ODD_NEG":"OPEN","RH":"OPEN"
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--source",default="notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json")
    ap.add_argument("--seams",default="notes/data/provisional/NF406_original_prime_support_partition_exact.json")
    ap.add_argument("--jet",default="notes/data/provisional/NF411_original_source_boundary_jet.json")
    ap.add_argument("--nf450",default="notes/data/provisional/NF450_original_B_complete_Laplace_native_sign_custody_index.json")
    ap.add_argument("--nf452",default="notes/data/provisional/NF452_original_J8_terminal_signed_moments_custody_index.json")
    ap.add_argument("--nf457",required=True)
    ap.add_argument("--output",required=True)
    a=ap.parse_args()
    r=run(a)
    path=Path(a.output);path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(r,indent=2)+"\n")
    lo,hi=map(Q,r["original_complete_J8_extended_collar_D_strict_outward"])
    print("NF457 true complete signed original J8 extended collar:",float(lo),float(hi),flush=True)
    print("NF457 full J8, J7, W-ODD-NEG, RH OPEN",flush=True)
if __name__=="__main__":main()
