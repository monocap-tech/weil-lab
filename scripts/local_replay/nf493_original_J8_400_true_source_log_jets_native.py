#!/usr/bin/env python3
"""NF493 original NF407 source-native ALL FOUR HUNDRED log-coefficient jets.

Compute exactly the SAME ORIGINAL complete 242-selected+4-critical (273
frequency/order) compact source U(B-d) Taylor u_0..u_399 with 4096-bit
Arb/Acb, before absolute values or mode-wise energy. The resulting
U(B-d)/2 is the exact all-orders logarithmic coefficient in the genuine
NF491 nonnegative whole physical square (p+z)^2.

This job does not compute analytic H's 400 jets and CANNOT close Ew or D8.
All genuine 400 source coefficients and their uncertainties are emitted
as original-source rational outward intervals for an independent
EXACT Fraction polynomial-log-square moment calculation.
"""
from __future__ import annotations
import argparse,hashlib,json,math,sys
from pathlib import Path
from fractions import Fraction as F
from flint import arb,acb,ctx
from nf415_original_cell6_I1_validated_acb import native_source,U

if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
B=F(11,10)
DELTA=F(1,500)
R=F(1,25)
N=400
PREC=4096
SRC="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAM="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
SOURCE_COMPLEX_DYADIC_FEE=F(1,10**450)

def A(q):
    if isinstance(q,arb):return q
    if isinstance(q,F):return arb(q.numerator)/arb(q.denominator)
    return arb(q)
def C(q):return acb(A(q))
def native_iv(x,digits=230):
    m,r,e=x.mid_rad_10exp(digits)
    factor=F(10)**int(e)
    assert int(r)>=0
    return F(int(m)-int(r))*factor,F(int(m)+int(r))*factor
def overlap(a,b):return a[0]<=b[1] and b[0]<=a[1]
def add_error(iv,e):return iv[0]-e,iv[1]+e
def signed_source_400_jets(terms,pole):
    """4096bit full source linear form, no image-only analytic continuation."""
    orig=[arb(0) for _ in range(N)]
    pi=arb.pi()
    count=0
    for f,k,c in terms:
        assert F(0)<f<883 and 0<=k<=13
        omega=2*pi*A(f)
        iw=acb(arb(0),omega)
        alpha=acb(arb(0),-A(c)/2) if k%2==0 else acb(A(c)/2)
        phase=alpha*(iw*A(B)).exp()
        em=[acb(1)]
        z=-iw
        for n in range(1,N):
            em.append(em[-1]*z/n)
        poly=[A(math.comb(k,j))*A(B)**(k-j)*((-1)**j)
              for j in range(k+1)]
        for n in range(N):
            s=acb(0)
            for j in range(min(n,k)+1):
                s+=poly[j]*em[n-j]
            orig[n]+=2*(phase*s).real
        count+=1
        if count%90==0:
            print("NF493 original ALL 246 generator full-U source log Taylor",count,"of 273",flush=True)
    assert count==273
    # The SAME ORIGINAL odd sinh source (not reinterpreted as one
    # oscillatory image). Its sinh/cosh jets have no m0 singularity.
    pp=A(pole)
    ss=(A(B)/2).sinh()
    cc=(A(B)/2).cosh()
    factorial=1
    for n in range(N):
        if n:factorial*=n
        orig[n]+=pp*(A(F(-1,2))**n)*(ss if n%2==0 else cc)/factorial
    return orig

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--source",default="notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json")
    ap.add_argument("--seams",default="notes/data/provisional/NF406_original_prime_support_partition_exact.json")
    ap.add_argument("--output",required=True)
    opt=ap.parse_args()
    ctx.prec=PREC
    raw=Path(opt.source).read_bytes()
    seamsraw=Path(opt.seams).read_bytes()
    source=json.loads(raw)
    seams=json.loads(seamsraw)
    sha=hashlib.sha256(raw).hexdigest()
    support_sha=hashlib.sha256(seamsraw).hexdigest()
    assert sha==SRC and support_sha==SEAM
    assert source["original_dimension"]==242
    assert len(source["original_exact_native_original_four_critical_coefficients_mid_radius"])==4
    assert len(source["original_source_critical_sine_frequencies"])==32
    terms,pole,s0=native_source(source)
    assert len(terms)==273 and s0<F(1,10**700)
    # Original input radii are part of the original source. The
    # 1e-450 holomorphic source input overcharge follows from
    # NF492 exact original dyadic complex amplitude error <1e-650
    # and its original bounded complex oscillator growth <1e200.
    assert s0*F(10)**250 < SOURCE_COMPLEX_DYADIC_FEE
    assert DELTA/R==F(1,20)
    print("NF493 4096bit SAME ORIGINAL 400 full source Taylor coefficients started",flush=True)
    u=signed_source_400_jets(terms,pole)
    src=U(source)
    vb=src.at(C(A(B))).real
    vd=src.at(C(A(B-DELTA))).real
    assert overlap(native_iv(u[0]),native_iv(vb))
    polyd=arb(0)
    term=arb(1)
    for n in range(N):
        polyd+=u[n]*term
        term*=A(DELTA)
    cauchy=F(10)**400*(DELTA/R)**N/(1-DELTA/R)
    assert cauchy<F(1,10**119)
    assert overlap(add_error(native_iv(polyd),cauchy),
                   add_error(native_iv(vd),F(1,10**400))),(
                   "METHOD STOP: original 400 same-source local Taylor does not overlap direct U(B-d)")
    assert native_iv(vb)[1]<0 and native_iv(vd)[0]>0
    # Source-error charged COEFFICIENT-WISE using the fixed analytic
    # branch radius R=1/25, preserving exact original intervals.
    complete=[]
    for n,z in enumerate(u):
        ci=native_iv(z)
        fee=SOURCE_COMPLEX_DYADIC_FEE*F(25)**n
        complete.append(tuple(map(str,add_error(ci,fee))))
    full_coefficient_0=tuple(map(str,native_iv(vb)))
    full_at_delta=tuple(map(str,native_iv(vd)))
    out={
      "pass":"NF493-original-source-400-log-jets",
      "standing":"ACTUAL ALL 400 original NF407 complete physical U(B-d) Taylor coefficient balls NATIVE 4096bit, independently source-custodied physical endpoint check; numeric ONLY pure U²log² component, not H or Ew_bulk",
      "original_nf407_source_sha256":SRC,
      "original_nf406_seams_sha256":SEAM,
      "original_selected_generators":242,
      "original_critical_generators":4,
      "original_grouped_source_modes":273,
      "original_critical_sine_frequencies":32,
      "original_full_odd_sinh_pole_preserved":True,
      "original_native_precision_bits":PREC,
      "original_source_native_dyadic_midpoint_radii_sum_exact":str(s0),
      "original_source_input_complete_complex_sup_fee":"1e-450",
      "original_source_input_added_each_taylor_jet":"1e-450*25**n",
      "true_original_B":"11/10",
      "original_J8_terminal_delta":"1/500",
      "original_analytic_fixed_branch_Cauchy_radius":"1/25",
      "original_real_terminal_ratio":"1/20",
      "original_true_log_source_coefficient":"U(B-d)/2",
      "original_source_log_u_taylor_degree":"399",
      "original_real_original_U_dyadic_coefficient_ball_first_400":complete,
      "original_source_4096bit_v_at_B_outward":list(full_coefficient_0),
      "original_source_4096bit_U_at_B_minus_delta_outward":list(full_at_delta),
      "original_source_400_taylor_direct_overlap":True,
      "original_source_400_taylor_analytic_Cauchy_abs_tail":str(cauchy),
      "original_complete_source_raw_246_odd_sinh_unchanged":True,
      "original_physical_full_square_one_source_log_component":"(1/4)int_0^(1/500) U(B-d)^2 log(B/d)^2 dd",
      "original_400_H_analytic_coefficients_numerically_computed":False,
      "original_complete_original_Ew_bulk_numerically_certified":False,
      "original_full_J8_D8_signed_UPPER":"OPEN",
      "NF404":"OPEN","W_ODD_NEG":"OPEN","RH":"OPEN",
      "next_bold":"NF494 compute actual 400 source-contracted analytic H(d) coefficients from original NF446 physical compact response; then cross terms with completed U 400 log-square component to assemble full Ew_T"
    }
    path=Path(opt.output);path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(out,indent=2)+"\n")
    print("NF493 exact original 400 U(B-d) jets FULL physical source U(B) bounds",*[float(x) for x in native_iv(vb)],flush=True)
    print("NF493 full original 400 source series vs independent direct U(B-1/500) PASS",
          *[float(x) for x in native_iv(vd)],flush=True)
    print("NF493 original 400 U jets source Cauchy <1e-119; full H and Ew_bulk and NF404 OPEN",flush=True)
if __name__=="__main__":main()
