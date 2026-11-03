#!/usr/bin/env python3
"""NF454 independent original 4096-bit n9 *log-weighted* source moment.

Original full J8 principal p=v*(log(B/d)/2+C8); actual n9 regularized
increment z9=-w9*(v-U(B-y)), 0<y<a=2B-log9, d=a-y.

Compute B9=∫_0^a log(B/(a-y))*(v-U(B-y))dy by the COMPLETE original
273-group source Taylor at physical contact y0=log9-B. Integrate each
Taylor coefficient against exact log moments. The source is summed
before the singular integration; rigorous Cauchy tail and native
coefficient radii are paid separately. No Gauss x mesh.
"""
import argparse, json, math, sys
from pathlib import Path
from fractions import Fraction as Q
from flint import arb, acb, ctx
from nf415_original_cell6_I1_validated_acb import native_source,U,A,C
from nf454_original_n9_contact_native_moment import read,enclosure,B,SRC_SHA,SEAM_SHA

if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
N=320
R=Q(1,40)
M=Q(10)**230
QBOUND=Q(3,25)

def analytic_coefficients(terms,pole,y0):
    grouped={}
    for f,k,q in terms: grouped.setdefault(f,[]).append((k,q))
    assert sum(len(t) for t in grouped.values())==273
    total=[arb(0) for _ in range(N)]
    pic=arb.pi()
    for jgrp,(f,poly) in enumerate(grouped.items()):
        iw=acb(arb(0),2*pic*A(f))
        phase=(iw*y0).exp()
        expcoeff=[acb(1)]
        for j in range(1,N):expcoeff.append(expcoeff[-1]*iw/j)
        odd=[arb(0) for _ in range(14)]
        even=[arb(0) for _ in range(14)]
        ypow=[arb(1)]
        for j in range(13):ypow.append(ypow[-1]*y0)
        for k,q in poly:
            co=A(q)
            target=even if k%2==0 else odd
            for i in range(k+1):
                target[i]+=co*math.comb(k,i)*ypow[k-i]
        maxk=max(k for k,q in poly)
        for j in range(N):
            qeven=acb(0)
            qodd=acb(0)
            for i in range(min(maxk,j)+1):
                if even[i]:qeven+=even[i]*expcoeff[j-i]
                if odd[i]:qodd+=odd[i]*expcoeff[j-i]
            total[j]+=(phase*qeven).imag+(phase*qodd).real
        if (jgrp+1)%20==0 or jgrp+1==len(grouped):
            print("NF454 original n9 log source groups",jgrp+1,len(grouped),flush=True)
    sp=(y0/2).sinh()
    cp=(y0/2).cosh()
    pow2=arb(1)
    fact=1
    for j in range(N):
        if j:fact*=j;pow2/=2
        total[j]+=A(pole)*(sp if j%2==0 else cp)*pow2/fact
    return total

def run(args):
    ctx.prec=args.precision
    assert ctx.prec>=3072
    s,sh=read(args.source)
    seams,ks=read(args.seams)
    jet,js=read(args.jet)
    native,ns=read(args.unweighted)
    assert (sh,ks)==(SRC_SHA,SEAM_SHA)
    assert native["source_sha256"]==sh and native["seam_sha256"]==ks
    assert native["true_original_source_frequency_order_groups"]==273
    assert native["original_coefficient_native_radius_paid"]
    assert jet["nf407_source_sha256"]==sh
    log9=arb(9).log()
    a=2*A(B)-log9
    y0=log9-A(B)
    seam9=next(x for x in seams["original_prime_power_log_shifts"] if x["n"]==9)
    alo,ahi=Q(2)*B-Q(seam9["log_upper"]),Q(2)*B-Q(seam9["log_lower"])
    assert 0<alo<ahi<Q(3,1000)
    assert ahi/R<QBOUND
    assert B/alo<Q(1100)
    # Since e>8/3, (8/3)^8>1100; positive log(B/a)<8.
    assert Q(8,3)**8>1100
    # For |d|=R around original y0, physical source analytic continuation
    # satisfies |U(y0+d)| < 10^230 on circle: |y0+d|<9/8, max f<883,
    # |2 pi f Im(d)|<139, e^139<3^139<10^67; raw source sum <10^160.
    assert Q(3)**139<Q(10)**67
    assert (Q(9,8)/B)**13 < 2
    coeffs,pole,s0=native_source(s)
    assert len(coeffs)==273 and s0<Q(1,10**700)
    raw=sum((abs(q)*B**k for f,k,q in coeffs),abs(pole))
    assert raw<Q(10)**160 and all(0<f<883 and k<=13 for f,k,q in coeffs)
    Ctail=M*(QBOUND**N)/(1-QBOUND)
    assert Ctail<Q(1,10**55)
    logtail=9*ahi*Ctail
    assert logtail<Q(1,10**50)
    source_charge=18*ahi*s0
    assert source_charge<Q(1,10**700)

    utaylor=analytic_coefficients(coeffs,pole,y0)
    v=U(s).at(C(B)).real
    L=(A(B)/a).log()
    prod=arb(1)
    acc=arb(0)
    acc0=arb(0)
    for j in range(N):
        prod*=a
        inv=A(Q(1,j+1))
        h=prod*inv*(L+inv)
        current=(v-utaylor[0]) if j==0 else -utaylor[j]
        acc+=current*h
        acc0+=current*prod*inv
    b0,b1=enclosure(acc,100)
    b0-=logtail+source_charge
    b1+=logtail+source_charge
    assert b0<b1
    a0,a1=enclosure(acc0,100)
    a0-=ahi*Ctail+2*ahi*s0
    a1+=ahi*Ctail+2*ahi*s0
    storedA0,storedA1=(Q(z) for z in native["actual_original_n9_boundary_A9_integral_outward"])
    assert a0<=storedA1 and storedA0<=a1, "independent 320-coefficient original source A9 disagrees with native exact primitive"

    vv0,vv1=(Q(z) for z in native["source_v_original_outward"])
    w9=next(x for x in jet["all_seven_original_prime_seam_derivative_identities"] if x["prime_power"]==9)
    w0,w1=(Q(z) for z in w9["c_n_positive_outward"])
    c0=sum((Q(x["c_n_positive_outward"][0]) for x in jet["all_seven_original_prime_seam_derivative_identities"]),Q(0))
    c1=sum((Q(x["c_n_positive_outward"][1]) for x in jet["all_seven_original_prime_seam_derivative_identities"]),Q(0))
    # true original complete principal cross of the original n9 regularized
    # source increment, not n9-self or all original z.
    Xvals=[-4*v*w*(c*aa+bb/2)
           for v in (vv0,vv1) for w in (w0,w1)
           for c in (c0,c1) for aa in (storedA0,storedA1)
           for bb in (b0,b1)]
    Xlo,Xhi=min(Xvals),max(Xvals)
    assert Xlo<Xhi
    return {
        "pass":"NF454",
        "standing":"original complete-principal p cross with genuine n9-only z9 via source-native analytic log moments; whole original J8 signed OPEN",
        "original_source_sha256":sh,"original_seams_sha256":ks,
        "original_nf411_source_jet_receipt_sha256":js,
        "original_unweighted_n9_native_JSON_sha256":ns,
        "source_original_groups":273,"source_original_generators":246,
        "original_source_kmax":13,"original_fmax_strict":883,
        "original_analytic_Cauchy_disk_radius":str(R),
        "original_source_complex_Cauchy_sup_upper":str(M),
        "original_taylor_orders":N,
        "original_log_integral_Cauchy_tail_upper":str(logtail),
        "original_coefficient_radius_paid":str(source_charge),
        "original_B9_log_weighted_n9_source_moment_outward":[str(b0),str(b1)],
        "original_independent_A9_taylor_interval_overlaps_exact_analytic_native":True,
        "original_full_principal_cross_4pz9_outward":[str(Xlo),str(Xhi)],
        "B9_sign":"NEGATIVE" if b1<0 else ("POSITIVE" if b0>0 else "UNDECIDED"),
        "true_original_n9_4pz9_sign":"NEGATIVE" if Xhi<0 else ("POSITIVE" if Xlo>0 else "UNDECIDED"),
        "entire_original_J7_signed":"OPEN","entire_original_J8_signed":"OPEN",
        "NF410_NF404_global":"OPEN","W_ODD_NEG":"OPEN","RH":"OPEN"
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--source",default="notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json")
    ap.add_argument("--seams",default="notes/data/provisional/NF406_original_prime_support_partition_exact.json")
    ap.add_argument("--jet",default="notes/data/provisional/NF411_original_source_boundary_jet.json")
    ap.add_argument("--unweighted",required=True)
    ap.add_argument("--precision",type=int,default=4096)
    ap.add_argument("--output",required=True)
    args=ap.parse_args()
    d=run(args)
    output=Path(args.output);output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(d,indent=2)+"\n")
    print("NF454 original complete weighted B9",float(Q(d["original_B9_log_weighted_n9_source_moment_outward"][0])),float(Q(d["original_B9_log_weighted_n9_source_moment_outward"][1])),flush=True)
    print("NF454 original full 4*p*z9",float(Q(d["original_full_principal_cross_4pz9_outward"][0])),float(Q(d["original_full_principal_cross_4pz9_outward"][1])),flush=True)
    print("NF454 full J8 signed, W-ODD-NEG and RH OPEN",flush=True)
if __name__=="__main__":main()
