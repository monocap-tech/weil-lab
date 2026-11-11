#!/usr/bin/env python3
"""NF500 independent original source exact-Fraction audit: all 242 raw
selected-source mixed moments, with TWO independent original rational
sin/cos moment reconstructions and independently accepted pole.

Native 4096-bit original source-produced full 242 moment array is
NOT trusted as self-authenticating: auditor rechecks raw immutable NF407,
NF406 SHA, original source 400 coefficient artifact, exact uniform
source errors, original selected shape/parity for all 242 rows,
independently recomputes indices 0 and 1 from Machin rational pi and
rational sin/cos/log550 moments, and index 241 from accepted original
NF499 exact rational pole artifact.

All source uncertainties and original smooth cutoff effects paid;
no Gram inverse / full Q_J capture or Weil operator-domain assertions.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import json,hashlib,math,argparse,sys
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
B=F(11,10);DELTA=F(1,500)
SRC="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAM="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
K=110
PREC=130
FEE=F(1,10**75)
def read(p):
    raw=Path(p).read_bytes();return json.loads(raw),hashlib.sha256(raw).hexdigest()
def intervals(x):return F(x[0]),F(x[1])
def atanh(z,n):
    term=z;s=F(0)
    for j in range(n):
        s+=2*term/F(2*j+1)
        term*=z*z
    return s,s+2*term/F(2*n+1)/(1-z*z)
def atan(z,n):
    term=z;s=F(0)
    for j in range(n):
        s+=(-1)**j*term/F(2*j+1)
        term*=z*z
    return s,term/F(2*n+1)
def independent_first_two(original,src):
    # Independent original rational pi (Machin), not Arb.
    a,ea=atan(F(1,5),PREC);b,eb=atan(F(1,239),PREC)
    pi=16*a-4*b
    pierr=16*ea+4*eb
    assert pierr<F(1,10**176) and F(3)<pi<F(4)
    # NF407 authentic generator indices [37/64,0], [37/64,1].
    assert original["original_selected_generator_node_orders"][:2]==[["37/64",0],["37/64",1]]
    freq=F(37,64)
    theta=2*pi*freq*B
    mu=2*pi*freq*DELTA
    assert 3<theta<5 and 0<mu<F(1,100)
    # Independent real sin(theta), cos(theta) rational Taylor;
    # all intervals paid by global conservative error <1e-75.
    sin_theta=sum(((-1)**j*theta**(2*j+1)/math.factorial(2*j+1) for j in range(100)),F(0))
    cos_theta=sum(((-1)**j*theta**(2*j)/math.factorial(2*j) for j in range(100)),F(0))
    assert F(-1)<sin_theta<F(1) and F(-1)<cos_theta<F(1)
    trigerr=F(200*5**200,math.factorial(200))+10*pierr
    assert trigerr<F(1,10**174)
    # Original 400 exact source coefficient midpoints from separate
    # immutable source-native NF493 accepted artifact, same 110 prefix.
    source_norm=[]
    for n,(lo,hi) in enumerate(src["original_real_original_U_dyadic_coefficient_ball_first_400"][:K]):
        source_norm.append((F(lo)+F(hi))/2*DELTA**n)
    source_error=sum(((F(hi)-F(lo))*DELTA**n/2 for n,(lo,hi) in enumerate(src["original_real_original_U_dyadic_coefficient_ball_first_400"][:K])),F(0))
    # Original independent exact source all 400 tail from archive.
    tail=sum((max(abs(F(a)),abs(F(b)))*DELTA**n
         for n,(a,b) in enumerate(src["original_real_original_U_dyadic_coefficient_ball_first_400"])
         if n>=K),F(0))+F(src["original_source_400_taylor_analytic_Cauchy_abs_tail"])
    assert tail<F(2,10**79) and source_error<F(1,10**180)
    # Independent exact log550 =9log2+log(275/256)
    log2lo,log2hi=atanh(F(1,3),410)
    remlo,remhi=atanh(F(19,531),410)
    h=9*(log2lo+log2hi)/2+(remlo+remhi)/2
    herr=9*(log2hi-log2lo)/2+(remhi-remlo)/2
    assert F(6)<h<F(7) and herr<F(1,10**375)
    # Build sine/cosine in t from real rational trig at B:
    # sin(theta-mu*t), cos(theta-mu*t).
    sarr=[];carr=[]
    for n in range(80):
        j=n//2
        q=(-1)**j*mu**n/math.factorial(n)
        if n%2==0:
            sarr.append(sin_theta*q);carr.append(cos_theta*q)
        else:
            sarr.append(-cos_theta*q);carr.append(sin_theta*q)
    # original selected j0=sin(w x), j1=x*cos(w x).
    bc0=sarr
    bc1=[B*carr[n]-(DELTA*carr[n-1] if n>0 else 0) for n in range(80)]
    def integrated(bc):
        row=[sum((source_norm[n]*(h/F(n+j+1)+F(1,(n+j+1)**2)) for n in range(K)),F(0))
             for j in range(len(bc))]
        return DELTA*sum((bc[j]*row[j] for j in range(len(bc))),F(0))
    actual=[integrated(bc0),integrated(bc1)]
    # For original first two k<=1 basis |j_i|<=B, original U
    # tail under 2e-79, remainder of sine/cos mu-series 80 terms
    # <e^1 /80!, plus real trig/pi, h intervals. Global source
    # fee 1e-75 massively overcharges all.
    assert 2*F(2,10**79)*DELTA*10<FEE/F(2)
    assert F(10,math.factorial(80))*DELTA*F(2,10**7)<FEE/F(4)
    assert 10*(trigerr+herr+source_error)<FEE/F(4)
    return [(val-FEE,val+FEE) for val in actual],str(pierr)

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--native",required=True)
    p.add_argument("--nf493-native",required=True)
    p.add_argument("--nf499-pole",required=True)
    p.add_argument("--output",required=True)
    a=p.parse_args()
    native,nsha=read(a.native);u,usha=read(a.nf493_native)
    pole,psha=read(a.nf499_pole)
    orig,sha=read("notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json")
    seams,ssha=read("notes/data/provisional/NF406_original_prime_support_partition_exact.json")
    nf404,sha404=read("notes/data/provisional/NF404_original_selected_pole_shear_exact.json")
    assert native["pass"]=="NF500-native" and sha==SRC==native["original_nf407_source_sha256"]==u["original_nf407_source_sha256"]
    assert ssha==SEAM==native["original_nf406_seams_sha256"]==u["original_nf406_seams_sha256"]
    assert native["original_source_original_nf493_4096bit_full_400_U_native_json_sha256"]==usha
    assert native["original_original_nf499_independently_exact_pole_moment_sha256"]==psha
    assert pole["pass"]=="NF499-pole" and pole["original_nf407_source_sha256"]==SRC
    assert nf404["pass"]=="NF404" and nf404["original_dimension"]==242
    assert nf404["original_selected_pole_index"]==241
    assert orig["original_selected_generator_node_orders"][-1]==["pole",None]
    rows=native["original_selected_242_odd_source_full_two_collar_basis_moments_outward"]
    assert len(rows)==242
    assert native["original_native_source_precision_bits"]==4096
    assert native["original_each_raw_selected_moment_analytic_plus_original_dyadic_overcharge"]=="1/1000000000000000000000000000000000000000000000000000000000000000000000000000"
    assert F(native["original_source_smoothing_log_carrier_to_phi_all_242_selected_row_abs_fee"])==F(1,10**28)
    assert native["original_full_original_selected_242_Gram_inverse_computed"] is False
    assert native["original_true_Q_J_w_against_Q_J_phi_capture_computed"] is False
    assert native["W_ODD_NEG"]==native["RH"]=="OPEN"
    for i,(item,raw) in enumerate(zip(rows,orig["original_selected_generator_node_orders"])):
        assert item["raw_selected_index"]==i
        f,k=raw
        assert item["original_generator"]==str(f)
        assert item["original_monomial_order"]==k
        assert item["original_real_odd_generator_shape"]==("sinh(x/2)" if f=="pole" else ("x^k*sin(2*pi*f*x)" if k%2==0 else "x^k*cos(2*pi*f*x)"))
        lo,hi=intervals(item["original_true_raw_log_source_moment_outward"])
        pl,ph=intervals(item["original_true_smooth_phi_selected_moment_outward"])
        assert lo<=hi and max(abs(lo),abs(hi))<F(1,10**7)
        assert pl<=lo-F(1,10**28) and ph>=hi+F(1,10**28)
    direct,pierr=independent_first_two(orig,u)
    for i,(lo,hi) in enumerate(direct):
        nl,nh=intervals(rows[i]["original_true_raw_log_source_moment_outward"])
        assert lo<=nh and nl<=hi, ("METHOD STOP: independent exact rational Machin/sine source cross moment disagreement",i)
    pl,ph=intervals(pole["original_true_raw_log_carrier_selected_pole_moment_outward"])
    nl,nh=intervals(rows[241]["original_true_raw_log_source_moment_outward"])
    assert pl<=nh and nl<=ph and nl>0
    # Independent original selected pole smooth positive lower:
    sl,sh=intervals(rows[241]["original_true_smooth_phi_selected_moment_outward"])
    assert sl>0
    pole_norm_lo=F(nf404["original_pole_squared_norm_lower_exact"])
    pole_norm_hi=F(nf404["original_pole_squared_norm_upper_exact"])
    selected_pole_power_lb=sl**2/pole_norm_hi
    assert selected_pole_power_lb>F("2.63e-24")
    out={
      "pass":"NF500",
      "standing":"FIRST ORIGINAL ALL 242 RAW SELECTED J242 mixed moments of true original source Ulog whole 2 J8 collar Hilbert trial, independently accepted 4096bit native and original Machin/sine rational indices0,1 plus prior NF499 genuine pole index241; all smooth candidate source intervals paid. Gram inversion/whole Q_J capture, Weil multiplier source range/domain and RH OPEN",
      "original_nf407_source_sha256":SRC,
      "original_nf406_seams_sha256":SEAM,
      "original_nf404_selected_source_receipt_sha256":sha404,
      "original_nf493_full_400_original_U_native_source_receipt_sha256":usha,
      "original_nf499_independent_pole_source_receipt_sha256":psha,
      "original_nf500_full_native_all_242_moment_source_receipt_sha256":nsha,
      "original_selected_242_mixed_moment_all_raw_source_rows":len(rows),
      "original_true_smooth_phi_all_242_raw_selected_moment_outward_certified":True,
      "original_first_ordinary_source_sin_cos_indices_0_1_independently_rational_Machin_Taylor_checked":True,
      "original_independent_Machin_pi_error_rational_upper":pierr,
      "original_independent_pole_selected_index_241_moment_overlap":True,
      "original_selected_pole_ray_energy_capture_strict_lower":str(selected_pole_power_lb),
      "original_total_selected_full_J242_projection_power_not_yet_computed":True,
      "original_true_full_Q_J_phi_projector_orthogonal_norm_computed":False,
      "original_true_whole_Q_Jw_to_Q_Jphi_capture_computed":False,
      "original_Weil_source_operator_domain_membership_verified":False,
      "NF404_original_selected_sufficient_certificate":"CERTIFIED FAIL",
      "W_ODD_NEG":"OPEN","whole_even_odd_Weil_domain":"OPEN","RH":"OPEN",
      "next_bold":"NF501 original 242D Gram frame from accepted NF400/401 authentic 30371-cell archive, compute source-exact smooth phi J242 projection and Q_Jw mixed rank-one captured full supported energy; independent Weil domain eligibility"
    }
    path=Path(a.output);path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(out,indent=2)+"\n")
    print("NF500 original full 242 old selected source mixed moments audited, exact independent rational original indices 0,1 and 241 PASS",flush=True)
    print("NF500 source original smooth phi selected pole power >",str(selected_pole_power_lb),flush=True)
    print("NF500 WHOLE Q_J projector and source/operator domain open",flush=True)
if __name__=="__main__": main()
