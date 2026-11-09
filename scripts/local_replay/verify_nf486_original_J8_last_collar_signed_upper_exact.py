#!/usr/bin/env python3
"""NF486 independent exact-rational J8 last 1e-15 collar signed UPPER.

Reuses ACCEPTED unchanged original NF411 physical v=U(B) source ball,
NF450 true original z(B) outward endpoints, and the NF451 true
original full compact-source modulus and strictly positive lower.

No original source coefficients fitted, no improper endpoint deleted;
the remaining [1e-15,1/500] J8 terminal is OPEN.
"""
import hashlib
import json
import re
from pathlib import Path
from fractions import Fraction as F

SOURCE_SHA="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
B=F(11,10)
ETA=F(1,10**15)
Z0=F("-0.000000000438192141572373")
Z1=F("-0.000000000438192103364328")
V_BOUND=F(2,10**11)
Z_BOUND=F(5,10**10)
LOG_BOUND=F(39)
CELL_PRIME_WEIGHT_BOUND=F(7)

def main():
    srcpath=Path("notes/data/provisional/NF411_original_source_boundary_jet.json")
    src=json.loads(srcpath.read_text())
    assert src["pass"]=="NF411"
    assert src["nf407_source_sha256"]==SOURCE_SHA
    text=src["original_original_source_value_at_B_arb"]
    match=re.fullmatch(r"\[([+-]?[0-9]+(?:\.[0-9]+)?e[+-]?[0-9]+) \+/- ([0-9]+(?:\.[0-9]+)?e[+-]?[0-9]+)\]",text)
    assert match, "METHOD STOP: original NF411 Arb endpoint carrier changed"
    vm,vr=map(F,match.groups())
    assert vm<0 and vr>=0 and abs(vm)+vr<V_BOUND
    assert Z0<Z1<0 and max(abs(Z0),abs(Z1))<F(44,10**11)
    assert ETA<F(1,500)
    # NF451 source-accepted positive-log majorant:
    # log(2B/ETA)<39 follows from the original exact rational
    # inequality (8/3)^39 > 2B/ETA and exp(1)>8/3.
    assert F(8,3)**39 > 2*B/ETA
    assert LOG_BOUND==39
    # d*log(2B/d) is increasing for 0<d<=ETA, because
    # log(2B/d)>1; hence the *whole continuous* original
    # original NF451 source modulus is controlled by endpoint d=ETA.
    eps=ETA*(F(14000)+F(600)*LOG_BOUND)
    assert eps==F(37400,10**15)
    assert max(abs(Z0),abs(Z1))+eps<Z_BOUND
    # Since p(d)=v(C8+0.5 log(B/d)), v<0, 0<C8<7,
    # and log(B/ETA)<log(2B/ETA)<39, its improper L1 norm
    # has an exact primitive, no numerical cutoff inside (0,ETA).
    integral_abs_p_bound=V_BOUND*ETA*(
        CELL_PRIME_WEIGHT_BOUND+(LOG_BOUND+1)/2)
    assert integral_abs_p_bound==F(54,10**26)
    mixed_abs_upper=4*Z_BOUND*integral_abs_p_bound
    quadratic_abs_upper=2*Z_BOUND**2*ETA
    total_upper=mixed_abs_upper+quadratic_abs_upper
    assert mixed_abs_upper==F(108,10**35)
    assert quadratic_abs_upper==F(50,10**35)
    assert total_upper==F(158,10**35)
    # NF451 accepted genuine same-source positive signed lower:
    old_lower=F(32,10**35)
    assert F(0)<old_lower<total_upper
    # The nearest original NF479 selected-complement corridor is
    # 3.31057841820960775340e-26; collar gross UPPER is
    # substantially smaller without any shadow decomposition.
    corridor_floor=F("3.31057841820960775340e-26")
    assert total_upper<corridor_floor/F(100000)
    receipt={
      "pass":"NF486",
      "standing":"EXACT source-inherited original J8 microscopic signed upper proved by original full compact response; original whole terminal upper OPEN",
      "original_nf407_sha256":SOURCE_SHA,
      "original_NF411_v_Arb_value_rechecked":text,
      "original_NF411_source_receipt_sha256":hashlib.sha256(srcpath.read_bytes()).hexdigest(),
      "original_NF450_true_z_B_outward":[str(Z0),str(Z1)],
      "original_NF451_original_full_joint_compact_modulus":"14000*d + 600*d*log(2B/d)",
      "original_NF451_prior_signed_lower":str(old_lower),
      "real_J8_last_collar_delta":str(ETA),
      "physical_original_seven_n9_active_prime_support":[2,3,4,5,7,8,9],
      "original_v_abs_strict_upper":str(V_BOUND),
      "original_z_uniform_last_collar_abs_strict_upper":str(Z_BOUND),
      "original_last_collar_principal_L1_strict_upper":str(integral_abs_p_bound),
      "original_last_collar_true_signed_upper":str(total_upper),
      "original_last_collar_original_signed_interval_open":[str(old_lower),str(total_upper)],
      "original_remaining_physical_terminal":["B-1/500","B-1/10^15"],
      "original_infinite_endpoint_not_replaced":True,
      "complete_remaining_original_J8_signed_upper":"OPEN",
      "NF404":"OPEN","W_ODD_NEG":"OPEN","RH":"OPEN",
      "next_bold":"NF487: source-contract complete original NF446 compact physical response on [1e-15,1/500], full signed pz+z2, retaining joint cancellation"
    }
    out=Path("nf486-original-J8-last-collar-exact-source-upper.json")
    out.write_text(json.dumps(receipt,indent=2)+"\n")
    print("NF486 exact original last J8 signed collar ACCEPTED RELATIVE TO SOURCE DEPENDENCIES")
    print("3.2e-34 < D8_last_1e-15 < 1.58e-33")
    print("whole D8 upper NF404 W-ODD-NEG RH OPEN")
if __name__=="__main__":
    main()
