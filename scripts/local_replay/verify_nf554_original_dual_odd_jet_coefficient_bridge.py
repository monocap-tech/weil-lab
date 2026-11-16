#!/usr/bin/env python3
"""NF554 exact original J242 dual-polynomial/odd-derivative bridge audit.

Audits 242 x 242 coefficient formulas *symbolically*, with no sampled pi,
and preserves the NF407 real sine/cosine parity and true sinh pole. Checks
the signed dual polynomial identity coefficient-by-coefficient, using
integer factorials, and independently tests exact Taylor coefficients.
No generic Lean algebraic-source theorem is inferred from this Python run.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction
from math import factorial
import json
from pathlib import Path
from verify_nf545_original_J242_exp_poly_signature import (
    SOURCE_PATH, NF500_PATH, NF500_SHA, SRC_SHA, LEAN_PATH,
    exact_read, signature_from_original_source, signature_from_lean_text,
)

N = 242


def falling(m: int, k: int) -> int:
    return factorial(m)//factorial(m-k) if k <= m else 0


def audit_dual_source_bridge(nodes, groups):
    assert len(nodes) == N and nodes[-1] == ["pole", None]
    assert len(groups) == 67 and sum(m for _,m in groups) == 241
    assert [(Fraction(f),k) for f,k in nodes[:241]] == [
        (f,k) for f,m in groups for k in range(m)]
    assert all(f>0 for f,m in groups)
    checked=0
    absent=0
    even=0
    odd=0
    # Symbolic monomial omega^e; compare integer coefficient and power
    # directly (never substitute an approximation to omega=2*pi*f).
    for f,k in [(Fraction(f),k) for f,k in nodes[:241]]:
        if k%2==0: even+=1
        else: odd+=1
        for n in range(N):
            q=2*n+1
            # Independent Taylor coefficient for generator:
            # x^k sin(omega*x) (k even), x^k cos(omega*x) (k odd).
            if q < k:
                source_factor=0
                source_power=None
            else:
                remaining=q-k
                assert remaining % 2 == (1 if k % 2 == 0 else 0)
                trig_order=(remaining-1)//2 if k%2==0 else remaining//2
                source_factor=((-1)**trig_order)*factorial(q)//factorial(remaining)
                source_power=remaining
            # The dual odd-jet map:
            # (-1)^n * A[n,(f,k)] == (-1)^floor(k/2)
            #       * derivative_omega^k omega^(2n+1).
            rhs_factor=(-1)**(n+(k//2))*falling(q,k)
            rhs_power=q-k if k<=q else None
            assert source_factor == rhs_factor and source_power == rhs_power, (
                "METHOD STOP: actual original parity/degree dual mismatch",f,k,n)
            checked+=1
            absent+=int(k>q)
    # Genuine pole independent Taylor equation:
    # (d/dx)^(2n+1) sinh(x/2)|_0=2^(-2n-1).
    # For p(t)=sum (-1)^n a_n t^n, coefficient of a_n in
    # (1/2) p(-1/4) is (-1)^n /2 *(-1/4)^n = 2^(-2n-1).
    pole=0
    for n in range(N):
        q=2*n+1
        source_pole=Fraction(1,2**q)
        dual_pole=Fraction((-1)**n,2)*Fraction(-1,4)**n
        assert source_pole==dual_pole,("METHOD STOP: genuine pole",n)
        pole+=1
    assert checked==241*242 and pole==242
    return {
       "pass":"NF554-original-exact-all-242-dual-Hermite-odd-jet-symbolic-bridge",
       "exact_original_oscillator_modes":241,
       "original_sine_even_k_modes":even,
       "original_cosine_odd_k_modes":odd,
       "checked_symbolic_oscillator_odd_jet_coefficients":checked,
       "checked_true_pole_odd_jet_coefficients":pole,
       "zero_when_monomial_order_exceeds_derivative":absent,
       "symbolic_positive_frequency_omega":"omega_f=2*pi*f, no specialization or numeric pi",
       "duality":"a^T A=0 => d_omega^k[omega*p(omega^2)] at omega_f=0; p(-1/4)=0",
       "Hermite_rootMultiplicity_to_divisor_Lean":"OPEN",
       "original_source_global_independence_Lean":"OPEN",
       "original_source_Gram_positivity_Lean":"OPEN",
       "full_Weil_and_RH":"OPEN",
    }


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--output",type=Path)
    args=ap.parse_args()
    source,sha=exact_read(SOURCE_PATH)
    nf500,nf500sha=exact_read(NF500_PATH)
    assert sha==SRC_SHA,"METHOD STOP: NF407 source SHA"
    assert nf500["original_source_native_raw_json_sha256"]==NF500_SHA
    assert nf500["original_nf407_sha256"]==sha
    nodes=source["original_selected_generator_node_orders"]
    groups=signature_from_original_source(nodes)
    assert groups==signature_from_lean_text(LEAN_PATH)
    result=audit_dual_source_bridge(nodes,groups)
    result["original_nf407_source_sha256"]=sha
    result["original_nf500_native_raw_source_sha256"]=NF500_SHA
    result["nf500_custody_json_sha256"]=nf500sha
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(result,sort_keys=True,indent=2)+"\n")
    print("NF554: original 58,322 oscillator odd-jet symbolic coefficient checks PASS")
    print("NF554: genuine sinh-pole 242 odd-jet coefficients PASS")
    print("NF554: Lean source bridge/independence/Gram, W_ODD_NEG, RH OPEN")
    return 0


if __name__=="__main__":
    raise SystemExit(main())
