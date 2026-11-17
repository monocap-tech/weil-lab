#!/usr/bin/env python3
"""NF587 independent full-box normalized 400-jet replay.

Uses the actual NF407 primitive coefficient boxes, not midpoint plus a
separately assumed amplitude fee. Includes all four critical probes,
all selected modes and the original sinh pole. Evaluates normalized
Taylor coefficients v_n of U(B-delta*w) at w=0 with 4096-bit Arb.
The Cauchy bound is the coarse full-disc 10^400 bound derived from
exact source-box bounds and elementary complex sin/cos/sinh estimates.

This is a numerical interval certificate, NOT a Lean proof of the
Taylor/analytic identity or of custody of the original linear solve.
"""
from fractions import Fraction as F
from pathlib import Path
from flint import arb, acb, ctx
import argparse
import json
import math
from verify_nf587_original_NF407_lean_binding import read_source, check_source, dy, SHA

B, DELTA, R, N = F(11,10), F(1,500), F(1,25), 400

def A(q):
    q = F(q)
    return arb(q.numerator)/arb(q.denominator)

def ball(row):
    m,r = map(dy,row)
    assert r >= 0
    # Arb product with [-1,1], including rational conversion rounding.
    return A(m)+arb(0,1)*A(r)

def outward(x):
    m,r,e=x.mid_rad_10exp(230)
    assert int(r)>=0
    f=F(10)**int(e)
    return F(int(m)-int(r))*f, F(int(m)+int(r))*f

def main(out):
    ctx.prec=4096
    j=read_source()
    check_source(j)
    terms={}
    pole=arb(0)
    def add(f,k,c):
        key=F(f),k
        terms[key]=terms.get(key,arb(0))+c
    for (f,k),row in zip(j["original_selected_generator_node_orders"],
        j["original_exact_native_raw_selected_coefficients_mid_radius"]):
        c=ball(row)
        if f=="pole":
            pole+=c
        else:
            add(f,k,c)
    for shape,row in zip(j["original_source_critical_sines_and_pole_coefficients"],
        j["original_exact_native_original_four_critical_coefficients_mid_radius"]):
        c=ball(row)
        for f,q in zip(j["original_source_critical_sine_frequencies"],shape["sine_coefficients"]):
            add(f,0,c*A(F(q)))
        pole+=c*A(F(shape["sinh_coefficient"]))
    assert len(terms)==273
    Bv,Dv=A(B),A(DELTA)
    v=[arb(0) for _ in range(N)]
    pi=arb.pi()
    for count,((f,k),c) in enumerate(sorted(terms.items()),1):
        assert F(0)<f<883 and 0<=k<=13
        iw=acb(arb(0),2*pi*A(f))
        # x=B-delta*w. Real part of -i exp(i omega x)
        # gives sine; real part of exp(i omega x) gives cosine.
        alpha=acb(arb(0),-c) if k%2==0 else acb(c)
        phase=alpha*(iw*Bv).exp()
        z=-iw*Dv
        e=[acb(1)]
        for n in range(1,N):
            e.append(e[-1]*z/n)
        poly=[math.comb(k,m)*Bv**(k-m)*(-Dv)**m for m in range(k+1)]
        for n in range(N):
            s=acb(0)
            for m in range(min(n,k)+1):
                s+=poly[m]*e[n-m]
            v[n]+=(phase*s).real
        if count%90==0: print("NF587 full-box modes",count,"of",len(terms),flush=True)
    # Literal sinh pole, including its actual coefficient uncertainty.
    even=(Bv/2).sinh()
    odd=(Bv/2).cosh()
    fac=arb(1)
    for n in range(N):
        if n: fac=fac*(-Dv/2)/n
        v[n]+=pole*fac*(even if n%2==0 else odd)
    intervals=[outward(x) for x in v]
    absbounds=[max(abs(a),abs(b)) for a,b in intervals]
    q=DELTA/R
    CM=F(10)**400
    tail0=CM*q**N/(1-q)
    tail1=CM/R*q**(N-1)*(N/(1-q)+q/(1-q)**2)
    M0=sum(absbounds)+tail0
    M1=sum(n*absbounds[n]/DELTA for n in range(1,N))+tail1
    assert M0 < F(2,10**7)
    assert M1 < F(7,10**4)
    assert intervals[0][1] < -F(1,10**11)
    record={
      "pass":"NF587-full-box-normalized-400-jet",
      "original_nf407_source_sha256":SHA,
      "precision_bits":4096,
      "selected":242,"critical":4,"grouped_modes":273,
      "actual_sinh_pole":True,"direct_source_box":True,
      "B":str(B),"delta":str(DELTA),"cauchy_R":str(R),
      "cauchy_M":str(CM),"N":N,
      "normalization":"v_n = [d^n] U(B-d) * delta^n",
      "normalized_intervals":[[str(a),str(b)] for a,b in intervals],
      "tail0":str(tail0),"tail1":str(tail1),
      "M0":str(M0),"M1":str(M1),"endpoint_upper":str(intervals[0][1]),
      "source_identity_Lean":"OPEN",
      "full_signed_Weil_coercivity":"OPEN","RH":"OPEN"
    }
    Path(out).write_text(json.dumps(record,indent=2)+"\n")
    print("NF587 direct full-box normalized U400 PASS",
          float(M0),float(M1),float(intervals[0][1]),flush=True)

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--output",required=True)
    main(p.parse_args().output)
