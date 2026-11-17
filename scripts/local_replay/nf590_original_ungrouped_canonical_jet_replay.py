#!/usr/bin/env python3
"""NF590 direct interval evaluation of the ungrouped Lean recurrence.

No mode grouping, no numerical derivative, no reuse of existing jet
intervals. Exact primitive NF407 boxes; same coefficient choice for
each source term (ordinary interval arithmetic overapproximates its
correlation but does not assume independently realizable coefficients).
The pole is evaluated through the two exponential jet recurrences,
matching the new analytic definition, rather than the parity formula.
Arb interval evidence is not a Lean transcendental proof term.
"""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import argparse
import json
import math
import re

from flint import arb, acb, ctx
from verify_nf587_original_NF407_lean_binding import (
    read_source, check_source, SHA, ROOT,
)
from nf587_original_NF407_full_box_normalized_U400 import A, ball, outward

N=400
B=F(11,10)
D=F(-1,500)
Q=10**40

def expjet(z):
    e=[acb(1)]
    for n in range(1,N):
        e.append(e[-1]*z/n)
    return e

@lru_cache(maxsize=None)
def oscillator(f,k):
    iw=acb(0,2*arb.pi()*A(f))
    phase=(acb(0,-1) if k%2==0 else acb(1))*(iw*A(B)).exp()
    e=expjet(iw*A(D))
    p=[math.comb(k,m)*A(B)**(k-m)*A(D)**m for m in range(k+1)]
    result=[]
    for n in range(N):
        s=acb(0)
        for m in range(min(k,n)+1):
            s+=p[m]*e[n-m]
        result.append((phase*s).real)
    return tuple(result)

def pole():
    p=acb(A(F(11,20))).exp()
    q=acb(A(F(-11,20))).exp()
    ep=expjet(acb(A(F(-1,1000))))
    en=expjet(acb(A(F(1,1000))))
    return tuple(((p*ep[n]-q*en[n]).real)/2 for n in range(N))

def main(output):
    ctx.prec=4096
    j=read_source()
    check_source(j)
    coeff=[arb(0) for _ in range(N)]
    P=pole()
    primitive_count=0
    def add(c,v):
        nonlocal primitive_count
        primitive_count+=1
        for n in range(N):
            coeff[n]+=c*v[n]
    for (f,k),row in zip(j["original_selected_generator_node_orders"],
        j["original_exact_native_raw_selected_coefficients_mid_radius"]):
        add(ball(row), P if f=="pole" else oscillator(F(f),k))
    for shape,row in zip(j["original_source_critical_sines_and_pole_coefficients"],
        j["original_exact_native_original_four_critical_coefficients_mid_radius"]):
        c=ball(row)
        for f,q in zip(j["original_source_critical_sine_frequencies"],shape["sine_coefficients"]):
            add(c*A(F(q)),oscillator(F(f),0))
        add(c*A(F(shape["sinh_coefficient"])),P)
    assert primitive_count==374
    intervals=[outward(x) for x in coeff]
    actual=[]
    for lo,hi in intervals:
        r=Q*max(abs(lo),abs(hi))
        actual.append(-(-r.numerator//r.denominator))
    table=(ROOT/"WeilDefect/Arithmetic/ActualZetaOriginalU400NormalizedBudget.lean").read_text()
    block=table.split("def neutralNF588U400CeilPrefix",1)[1].split(":=",1)[1].split("]",1)[0]
    prefix=list(map(int,re.findall(r"\d+",block)))
    ceilings=prefix+[1]*(N-len(prefix))
    assert len(ceilings)==N
    assert all(a<=b for a,b in zip(actual,ceilings))
    assert intervals[0][1]<-F(1,10**11)
    record={
        "pass":"NF590-ungrouped-canonical-recurrence",
        "original_nf407_source_sha256":SHA,
        "precision_bits":4096,"N":N,
        "primitive_summands":primitive_count,"grouped":False,
        "pole":"difference of two exponential recurrences",
        "normalized_intervals":[[str(a),str(b)] for a,b in intervals],
        "all_400_existing_ceilings_dominate":True,
        "all_400_ceilings_equal":actual==ceilings,
        "formal_transcendental_enclosures":"OPEN",
        "RH":"OPEN"
    }
    Path(output).write_text(json.dumps(record,indent=2)+"\n")
    print("NF590 ungrouped original recurrence PASS; 400 ceiling comparisons",
          "equal" if actual==ceilings else "dominated",flush=True)

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--output",required=True)
    main(p.parse_args().output)
