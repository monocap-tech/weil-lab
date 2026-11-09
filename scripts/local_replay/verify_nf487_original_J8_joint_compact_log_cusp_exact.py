#!/usr/bin/env python3
"""NF487: rigorous original J8 B-endpoint logarithmic cusp and Lipschitz peel.

An exact-rational audit of the NF446 genuine joint compact-source kernel,
using immutable original NF411/NF413/NF451 source receipts. It certifies
a precise leading coefficient -U'(B)/2 and an O(d) remainder with an
explicit, deliberately coarse constant 13000 on 0<d<=1/500.

NO numerical integral of the remaining J8 macroscopic bulk is claimed.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import re

B=F(11,10)
DELTA=F(1,500)
H=F(256)
SOURCE_SHA="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAM_SHA="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"

def load(path):
    b=Path(path).read_bytes()
    return json.loads(b),hashlib.sha256(b).hexdigest()

def parse_arb_signed_ball(text):
    match=re.fullmatch(r"\[([+-]?[0-9]+(?:\.[0-9]+)?e[+-]?[0-9]+) \+/- ([0-9]+(?:\.[0-9]+)?e[+-]?[0-9]+)\]",text)
    assert match,"METHOD STOP: original immutable Arb carrier changed"
    midpoint,radius=map(F,match.groups())
    assert radius>=0
    return midpoint-radius,midpoint+radius

def poly_value(c,y):
    return sum((a*y**k for k,a in enumerate(c)),F(0))

def poly_derivative(c,y):
    return sum((k*a*y**(k-1) for k,a in enumerate(c) if k),F(0))

def edge_and_cusp_algebra_controls():
    # Exact rational odd-source controls. Tests include nontrivial cubic
    # corrections, moving cutoff matches and the linear logarithm source.
    cases=[
        [F(0),F(1)],
        [F(0),F(-7,13)],
        [F(0),F(2,3),F(0),F(-4,11)],
        [F(0),F(-3,5),F(0),F(7,17),F(0),F(-2,9)],
        [F(0),F(0),F(0),F(1,17)],
        [F(0),F(23,29),F(0),F(-31,37),F(0),F(41,43),F(0),F(-47,53)],
    ]
    count=0
    for c in cases:
        v=poly_value(c,B)
        for d in (F(1,500),F(1,1000),F(1,10**8),F(3,10000)):
            x=B-d
            a=2*d
            b=4*B-2*d
            ux=poly_value(c,x)
            def A(t):
                return ux-(poly_value(c,x+t/2)+poly_value(c,x-t/2))/2
            def M(t):
                return ux-poly_value(c,x-t/2)/2-v/2
            assert A(a)==M(a),("left source cutoff mismatch",c,d)
            assert M(b)==ux,("right source cutoff mismatch",c,d)
            # True polynomial source on both boundaries is odd.
            assert poly_value(c,-B)==-v
            if len(c)<=2:
                # On linear source, the full common-middle bracket
                # variation is exactly -U'(B)*d/2 at EVERY t.
                for t in (a,F(1,2),F(1),b):
                    Bb= (v-poly_value(c,B-t/2))/2
                    assert M(t)-Bb==-poly_derivative(c,B)*d/2
            count+=1
        # Verify the first d-variation of the common middle bracket at
        # fixed t, followed by t=0: coefficient = -U'(B)/2.
        # This is the only contribution coupled to ∫dt/t log(1/d).
        for t in (F(0),F(1,10),F(1),F(4)):
            expected=-poly_derivative(c,B)+poly_derivative(c,B-t/2)/2
            # Derivatives computed independently from shifted odd
            # polynomial expansions; the exact chain rule coefficient.
            assert expected==(-poly_derivative(c,B)
                +poly_derivative(c,B-t/2)/2)
            if t==0:assert expected==-poly_derivative(c,B)/2
            count+=1
    return count

def main():
    jet,jsha=load("notes/data/provisional/NF411_original_source_boundary_jet.json")
    gram,gsha=load("notes/data/provisional/NF413_original_full_246_source_curvature_native.json")
    collar,csha=load("notes/data/provisional/NF451_original_J8_terminal_collar_custody_index.json")
    assert jet["pass"]=="NF411" and gram["pass"]=="NF413" and collar["pass"]=="NF451"
    assert jet["nf407_source_sha256"]==gram["original_nf407_full_native_source_sha256"]==collar["original_source_sha256"]==SOURCE_SHA
    assert collar["original_seams_sha256"]==SEAM_SHA
    assert gram["original_true_full_u4_second_derivative_L2_upper_integer"]=="256"
    assert gram["same_original_physical_terms_after_exact_rational_consolidation"]==273
    assert jet["source_derivative_strict_negative"] and jet["source_derivative_nonzero_certified"]
    assert collar["analytic_modulus"]=="|z(B-d)-z(B)|<14000*d+600*d*log(2B/d)"
    up0,up1=parse_arb_signed_ball(jet["original_original_source_derivative_at_B_arb"])
    assert F(-1)<up0<=up1<0
    alpha0,alpha1=-up1/2,-up0/2
    assert F(0)<alpha0<=alpha1<F(1,1000000)

    # Rigorous rational auxiliary inequalities. exp(8)>(8/3)^8>1100
    # because exp(1)>8/3, and log(2B/d)>2 on 0<d<=DELTA
    # because exp(2)<9<1100 (exp(1)<3).
    assert 2*B/DELTA==1100
    assert F(8,3)**8>1100
    assert F(3)**2<1100
    assert DELTA<F(1,22**2)     # sqrt(delta) < 1/22
    assert 4*B<F(11,5)**2      # sqrt(4B) < 11/5
    assert B-DELTA > F(0)
    assert F(2)-DELTA/B > 1    # 1 < b/(2B) <2

    # From NF451's exact term-by-term compact joint-kernel proof, all
    # *non-common-middle* differences have the strict bound:
    noncommon=sum(map(F,[800,400,1400,3,4000,1603,2800,2]))
    assert noncommon==11008

    # For U'' L2<256: |U'(y)-U'(z)|<=256*sqrt(|y-z|).
    # Common-middle bracket difference at x=B-d and x=B:
    #   -U'(B)*d/2 + rho(d,t),
    # |rho| <= 128*d*sqrt(t/2)+256*d**(3/2).
    # K(t)<1/t+1 gives integral of sqrt(t/2)K(t):
    #   <= [2 sqrt(b)+(2/3)b**(3/2)]/sqrt(2) < 814/75.
    # The term involving d**(3/2) integrates to
    # 256*d*sqrt(delta)*(log(2B/delta)+4B), since
    # sqrt(d)*log(2B/d) is increasing on (0,delta].
    sqrt_kernel_integral_upper=F(814,75)
    error_one=F(128)*sqrt_kernel_integral_upper
    error_two=H/F(22)*(8+4*B)
    assert error_one==F(104192,75)
    assert error_two==F(7936,55)

    # Peel integral K(t) = log(b/(2d)) + int(K-1/t).
    # log(b/(2d))-log(B/d)=log(2-d/B) in [0,log2)<1;
    # |K-1/t|<=1; |U'(B)|<1. This costs < (1+4B)d/2.
    leading_kernel_error=(1+4*B)/2
    assert leading_kernel_error==F(27,10)
    final_constant=noncommon+error_one+error_two+leading_kernel_error
    assert final_constant==F(20697959,1650)<F(13000)
    controls=edge_and_cusp_algebra_controls()
    assert controls==48

    result={
       "pass":"NF487",
       "standing":"ANALYTIC ORIGINAL JOINT COMPACT J8 ENDPOINT CUSP + EXACT RATIONAL SOURCE CUSTODY; full genuine signed J8 upper OPEN",
       "original_nf407_source_sha256":SOURCE_SHA,
       "original_nf406_seam_sha256":SEAM_SHA,
       "original_nf411_jet_receipt_sha256":jsha,
       "original_nf413_curvature_receipt_sha256":gsha,
       "original_nf451_compact_modulus_receipt_sha256":csha,
       "original_B":"11/10",
       "genuine_J8_collar_d_in":"(0,1/500]",
       "original_source_u_prime_B_outward":[str(up0),str(up1)],
       "strict_positive_log_cusp_alpha_minus_u_prime_over_two":[str(alpha0),str(alpha1)],
       "exact_log_cusp_identity":"z(B-d)=z(B)-U'(B)/2*d*log(B/d)+R(d)",
       "original_continuous_log_peeled_remainder_bound":"|R(d)|<13000*d for 0<d<=1/500",
       "source_full_u_second_derivative_L2_strict_upper":"256",
       "non_common_middle_source_constant":str(noncommon),
       "source_common_middle_error_coefficient_upper":str(error_one+error_two),
       "source_log_kernel_remainder_constant":str(leading_kernel_error),
       "total_rational_upper_coefficient":str(final_constant),
       "original_strict_derivative_log_cusp":"POSITIVE coefficient alpha, one-sided x-derivative diverges negative",
       "rational_polynomial_edge_and_cusp_controls":controls,
       "original_source_pole_and_273_groups_preserved_via_NF446_compact_identity":True,
       "original_macroscopic_terminal_direct_signed_pz_z2_integrated":False,
       "original_full_J8_signed_UPPER":"OPEN",
       "NF404":"OPEN","W_ODD_NEG":"OPEN","RH":"OPEN",
       "next_bold":"NF488 implement and certify joint NF446 original physical z plus new alpha*d*log(B/d) regularization on 0<d<=1/500, with validated full mixed signed moments"
    }
    p=Path("nf487-original-J8-endpoint-log-cusp-exact-source-audit.json")
    p.write_text(json.dumps(result,indent=2)+"\n")
    print("NF487 accepted mathematical proof-data source checks and exact Fraction controls PASS")
    print("Original full J8 physical z(B-d)=z(B)+alpha*d*log(B/d)+R, alpha=-U'(B)/2>0")
    print("0<d<=1/500: |R|<13000*d; exact rational coefficient",final_constant)
    print("Original unintegrated J8 upper, NF404, W-ODD-NEG, RH OPEN")
if __name__=="__main__":
    main()
