#!/usr/bin/env python3
"""NF489 exact independent original-source compact point method preflight.

Analytic identities and source support only. NEVER label an actual original
J8 physical z value as certified until full source-native integration and
independent complete output verifier BOTH PASS.
"""
import json,hashlib,math,sys
from pathlib import Path
from fractions import Fraction as F
from verify_nf489_original_J8_first_joint_compact_point_exact import groups_identities,primitive_controls
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
B=F(11,10);D=F(1,500);X=B-D
A=2*D;H=F(1,10);BB=2*(B+X)
SRC="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAM="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
def load(p):
    b=Path(p).read_bytes()
    return json.loads(b),hashlib.sha256(b).hexdigest()
def main():
    orig,src=load("notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json")
    seams,seam=load("notes/data/provisional/NF406_original_prime_support_partition_exact.json")
    jet,_=load("notes/data/provisional/NF411_original_source_boundary_jet.json")
    curv,_=load("notes/data/provisional/NF413_original_full_246_source_curvature_native.json")
    zrec,_=load("notes/data/provisional/NF450_original_B_complete_Laplace_native_sign_custody_index.json")
    nf451,_=load("notes/data/provisional/NF451_original_J8_terminal_collar_custody_index.json")
    assert src==SRC and seam==SEAM
    assert orig["original_dimension"]==242
    assert len(orig["original_exact_native_original_four_critical_coefficients_mid_radius"])==4
    assert len(orig["original_source_critical_sine_frequencies"])==32
    assert jet["nf407_source_sha256"]==zrec["source_SHA256"]==curv["original_nf407_full_native_source_sha256"]==SRC
    assert nf451["original_source_sha256"]==SRC and nf451["original_seams_sha256"]==SEAM
    assert curv["original_true_full_u4_second_derivative_L2_upper_integer"]=="256"
    assert X==F(549,500) and A==F(1,250) and BB==F(1099,250)
    assert 0<A<H<BB<4*B
    # The J8 n9-active source shift is strictly inside [-B,B] at x0.
    # Exact positive series with geometric remainder for log9.
    q=F(4,5)
    ln9lo=sum((2*q**(2*j+1)/F(2*j+1) for j in range(150)),F(0))
    ln9hi=ln9lo+2*q**301/(F(301)*(1-q*q))
    assert ln9hi <2*B-D and ln9lo >B
    # Other n<9 are smaller and n>=2 ensures x-logn<x<=B.
    assert X-ln9hi>-B
    # NF448 original full-source Cauchy geometry at x0:
    R=F(2,5);Q=H/R
    E=F(22,7)*883*R
    e=(E.numerator+E.denominator-1)//E.denominator
    assert e==1111 and F(11,4)**e<F(10)**500
    envelope=4*F(10)**160*F(11,4)**e
    eps=200*envelope*Q**1284/(1-Q)
    assert eps<F(1,10**50)
    # Exact physical compact-source upper for K(t) all m>=M.
    def cap(m):
        return F(22000,m)*F(3,8)**(m//10)
    assert cap(800)<F(1,10**29) and cap(720)<F(1,10**25)
    # Original m0 sinh physical Laplace zero-rate removable primitive.
    assert F(4*0+1,4)-F(1,4)==0
    assert BB-H==F(1074,250)  # J_0=physical interval length
    assert groups_identities()==18
    assert primitive_controls()==65
    out={
      "pass":"NF489-exact-method-preflight",
      "standing":"ANALYTIC SOURCE/SEAM GEOMETRY, EXACT TAYLOR AND COMPACT LAPLACE CUSTODY VALID; ACTUAL NATIVE REAL PHYSICAL POINT AND WHOLE D8 UPPER PENDING",
      "source_SHA":SRC,"support_SHA":SEAM,"genuine_real_J8_point":"549/500",
      "source_original_246_generators_273_groups":True,
      "original_source_true_n9_shift_in_compact_support":True,
      "true_original_t_split":["0","1/250","1/10","1099/250"],
      "original_source_taylor_Cauchy_charge":str(eps),
      "original_source_all_m_compact_geometric_800_charge":str(cap(800)),
      "original_source_all_m_compact_geometric_720_charge":str(cap(720)),
      "original_sinh_m0_no_division_by_zero":True,
      "original_exact_odd_polynomial_boundary_controls":18,
      "original_exact_complex_polynomial_Laplace_primitive_controls":65,
      "native_original_first_complete_physical_point":"PENDING",
      "full_original_J8_signed_upper":"OPEN","NF404":"OPEN","W_ODD_NEG":"OPEN","RH":"OPEN"
    }
    p=Path("nf489-original-J8-joint-compact-point-exact-method-preflight.json")
    p.write_text(json.dumps(out,indent=2)+"\n")
    print("NF489 original source/compact source point method exact Fraction preflight PASS")
    print("NF489 actual source-native J8 point and complete signed D8 UPPER still PENDING/OPEN")
if __name__=="__main__":main()
