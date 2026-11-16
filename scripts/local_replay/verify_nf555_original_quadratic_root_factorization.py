#!/usr/bin/env python3
"""NF555: source-native exact quadratic Hermite root-factorization audit.

For every one of the 67 genuine NF407 oscillator groups (f,m),
compare *independent* exact rational coefficient constructions of
   (X^2 - (2*pi*f)^2)^m = (X-2*pi*f)^m * (X+2*pi*f)^m.
Here pi is an INDETERMINATE Z, not a floating-point number or pi=1.
Coefficients lie in Q[X,Z], with Omega=2*f*Z. This is a symbolic
factorization audit, not a Lean root-multiplicity theorem.
"""
from __future__ import annotations
import argparse
from collections import defaultdict
from fractions import Fraction
from math import comb
import json
from pathlib import Path
from verify_nf545_original_J242_exp_poly_signature import (
    SOURCE_PATH, NF500_PATH, NF500_SHA, SRC_SHA, LEAN_PATH,
    exact_read, signature_from_original_source, signature_from_lean_text,
)

# Sparse bivariate polynomial Q[X,Z]: (degree_X, degree_Z) -> Q.
def times(a, b):
    out=defaultdict(Fraction)
    for (ax,az), ac in a.items():
        for (bx,bz),bc in b.items():
            out[(ax+bx,az+bz)] += ac*bc
    return {key:value for key,value in out.items() if value}

def pow_poly(a, m):
    result={(0,0):Fraction(1)}
    for _ in range(m):
        result=times(result,a)
    return result

def audit(groups, nodes):
    assert len(groups)==67 and sum(m for _,m in groups)==241
    assert nodes[-1]==["pole",None]
    assert [(Fraction(f),k) for f,k in nodes[:241]] == [
        (f,k) for f,m in groups for k in range(m)]
    assert all(f>0 for f,m in groups)
    assert len({f for f,m in groups})==67
    coefficient_checks=0
    max_mult=0
    for f,m in groups:
        w=2*f
        assert m>=1
        max_mult=max(max_mult,m)
        # Left: independent binomial theorem construction of
        # (X² - w²*Z²)^m (no expansion of the right factors).
        left={(2*(m-r),2*r):
              Fraction(comb(m,r)) * (-w*w)**r for r in range(m+1)}
        # Right: fully independent sparse bivariate convolution
        # of (X-wZ)^m * (X+wZ)^m.
        minus=pow_poly({(1,0):Fraction(1),(0,1):-w},m)
        plus=pow_poly({(1,0):Fraction(1),(0,1):w},m)
        right=times(minus,plus)
        assert left==right,("METHOD STOP: original quadratic factorization",f,m)
        coefficient_checks+=len(left)
        # For actual pi>0, w*pi>0, so the other factor evaluates
        # at the positive root to 2*w*pi>0; true pole t=-1/4<0
        # cannot collide with any positive squared oscillator.
        assert w>0 and w*w>0
    assert coefficient_checks==241+67==308
    return {
      "pass":"NF555-original-67-frequency-symbolic-quadratic-Hermite-root-factorization",
      "source_original_oscillator_groups":67,
      "source_original_oscillator_monomials":241,
      "source_true_sinh_pole_index":241,
      "source_real_squared_nodes_with_negative_pole":68,
      "largest_original_block_multiplicity":max_mult,
      "exact_Q[X,Z]_coefficient_checks":coefficient_checks,
      "pi_handling":"formal indeterminate Z, actual pi positive for root separation",
      "all_original_quadratic_factorizations_pass":True,
      "actual_positive_omega_root_cofactor":"X+omega at X=omega equals 2omega>0",
      "true_pole_squared_node":"-1/4, distinct from every positive oscillator square",
      "generic_Lean_factorization_and_cofactor":"NF555 candidate; compiler pending",
      "source_odd_jet_to_rootMultiplicity_Lean":"OPEN",
      "global_independence_and_original_Gram_Lean":"OPEN",
      "original_divisor_source_graph_signed_Weil_RH":"OPEN",
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--output",type=Path)
    args=ap.parse_args()
    source,sha=exact_read(SOURCE_PATH)
    nf500,nf500sha=exact_read(NF500_PATH)
    assert sha==SRC_SHA, "METHOD STOP original NF407 SHA"
    assert nf500["original_source_native_raw_json_sha256"]==NF500_SHA
    assert nf500["original_nf407_sha256"]==sha
    nodes=source["original_selected_generator_node_orders"]
    groups=signature_from_original_source(nodes)
    assert groups==signature_from_lean_text(LEAN_PATH)
    result=audit(groups,nodes)
    result["original_nf407_source_sha256"]=sha
    result["original_nf500_native_raw_source_sha256"]=NF500_SHA
    result["nf500_custody_json_sha256"]=nf500sha
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print("NF555: exact Q[X,Z] quadratic factorization PASS across all 67 original groups")
    print("NF555: 308 exact source polynomial coefficient comparisons, pi symbolic")
    print("NF555: Lean root multiplicity bridge and unconditional Gram/RH OPEN")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
