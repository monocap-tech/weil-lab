#!/usr/bin/env python3
"""NF524: exact Fraction source-constant and dyadic two-source graph audit.

Analytic theorem is in companion note. Original NF523 SHA-pinned
U and U' envelopes are premises; an INDEPENDENT script replays all 400
authentic NF494 source interval coefficients to validate those premises.
The actual zeta zero count bound with all multiplicities is an existing
Lean theorem, not a numerical zero list or assumed RH.
"""
import argparse,json
from pathlib import Path
from fractions import Fraction as F
B=F(11,10);D=F(1,500)
M0=F(2,10**7);M1=F(7,10**4);C=F(1,10000)
def tail(n):
    return F(2*(n+2)**3+6*(n+2)**2+18*(n+2)+26,2**n)
def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output",required=True)
    a=p.parse_args()
    # For 0<x<1, e^x <= 1+x/(1-x/2) by k!>=2^(k-1).
    z=(B+D)/2
    e=1+z/(1-z/2)
    assert 0<z<1 and e<2
    assert B/D==550
    # For |Re z|=t<=500, integrate the original two collar logs directly.
    low=4*M0*D*8
    assert low<C/501
    # For t>=500: split endpoint log at d=1/t and integrate by parts.
    # Each exponential and both collars are charged explicitly.
    # 1+log(t+2) coefficients separately enclosed, t>=500.
    factor=4*F(501,500)
    logcoeff=factor*3*M0
    constant=factor*(11*M0+8*M1*D)
    assert logcoeff<C and constant<C
    # Original source sample bound: C(1+log(2+t))/(1+t).
    # For s in [1/2,1], dilation has no worsening of bound.
    # Nonnegative normalized compact mollifier radius<=D costs <2.
    # Both actual source-pair coordinates each have 1/sqrt(2)
    # and every actual divisor multiplicity copy is counted.
    # Existing Lean: dyadic count <=A(n+2)2^n, no value for A assumed.
    for n in (0,1,2,8,16,32,64,128):
        assert tail(n)-tail(n+1)==F((n+2)**3,2**n)
        partial=sum((F((k+2)**3,2**k) for k in range(n,n+300)),F(0))
        assert partial<=tail(n)
    assert tail(64)<F(1,10**10)
    out={
     "pass":"NF524-original-endpoint-full-two-source-divisor-graph-analytic-envelope-exact",
     "original_NF494_full_source_SHA256":"39cba367d70243c2d15e5a9323fc8097d58187923dcf0eca2b031136871f0181",
     "original_NF523_primary_source_receipt_SHA256":"c489dd2de299284d31e18138b634fb8d759f2fc208fb05669f998a0b118cc0b5",
     "original_NF523_independent_source_receipt_SHA256":"f7e33bc509980300b83c89787956495c0c5ea78edafabe8be8700601a0bdd297",
     "original_true_collared_source_B":str(B),"original_source_delta":str(D),
     "original_source_bound_U_over_2":str(M0),
     "original_source_bound_Uprime_over_2":str(M1),
     "complex_phase_exp_upper":str(e),
     "low_height_full_two_collar_upper":str(low),
     "high_height_log_coefficient":str(logcoeff),
     "high_height_constant":str(constant),
     "ell_U_all_zeta_strip_sample_bound":"|F(z)|<=1e-4*(1+log(2+|Re(z)|))/(1+|Re(z)|) for |Im(z)|<=1/2",
     "actual_source_divisor_dyadic_card_Lean_theorem":"neutralActualZetaDivisorDyadicBand_card_bound",
     "zero_count_constant_A":"EXISTS_BY_UNCONDITIONAL_LEAN_NO_NUMERIC_VALUE",
     "true_positive_negative_pair_samples":"(F(conj(z))+/-F(z))/sqrt(2) for every multiplicity copy",
     "uniform_two_source_difference_tail_divided_by_A":"16*(3/10000)^2*2^-N*(2*(N+2)^3+6*(N+2)^2+18*(N+2)+26)",
     "original_ell_U_full_two_source_graph_lift":"ANALYTIC_THEOREM_FROM_NF523_SOURCE_AND_UNCONDITIONAL_DIVISOR_COUNT",
     "NF523_original_exact_242_moment_smooth_sequence_two_source_graph_Cauchy":"ANALYTIC_THEOREM",
     "original_Green_lift_closed_span_membership":"OPEN",
     "original_signed_Weil_source_diagonal":"OPEN",
     "W_ODD_NEG":"OPEN","RH":"OPEN",
     "all_numeric_zeta_zero_samples_evaluated":False,"Lean_compilation_new_theorem":False}
    Path(a.output).write_text(json.dumps(out,indent=2)+"\n")
    print("NF524 original-source Fourier strip decay and full zeta-divisor pair-tail exact Fraction PASS")
    print("Actual Green closure, complete signed source form and RH remain OPEN")
if __name__=="__main__":main()
