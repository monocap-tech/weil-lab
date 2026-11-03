#!/usr/bin/env python3
"""NF454 — source-native original n=9 *actual physical* J8 contact moment.

Unchanged original NF407 242 selected + 4 critical 4096-bit dyadic source,
273 frequency/order groups, original odd sinh pole, exact NF406 J8 seam,
NF411 true original endpoint v and original von Mangoldt weight for n9.

For x=x9+y, x9=log(9)-B, 0<y<a=2B-log9,
the new physical regular source term is
  z9(x)=-w9*(U(x-log9)+v)=-w9*(v-U(B-y)).
All this is the *increment* from n9, NOT the complete original z or D8.
Its true zeroth moment A9 = ∫_0^a [v-U(B-y)]dy is integrated in CLOSED
analytic polynomial/trigonometric primitives, no quadrature or source shadows.
The coefficient uncertainty <2a*S0 is paid at the original physical source.
"""
import argparse, hashlib, json, sys
from pathlib import Path
from fractions import Fraction as Q
from flint import arb, acb, ctx
from nf415_original_cell6_I1_validated_acb import native_source, U, A, C

if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
B=Q(11,10)
SRC_SHA="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAM_SHA="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"

def read(path):
    raw=Path(path).read_bytes()
    return json.loads(raw), hashlib.sha256(raw).hexdigest()

def enclosure(q,decimal_digits=110):
    mid,rad,expo=q.mid_rad_10exp(decimal_digits)
    ul=Q(10)**int(expo)
    lo=Q(int(mid)-int(rad))*ul
    hi=Q(int(mid)+int(rad))*ul
    assert lo<=hi
    return lo,hi

def integrate_original_U_small_boundary(terms,pole,L):
    """Exact primitive of physical U(y), y∈[log9−B,B], via all 273 terms."""
    grouped={}
    for f,k,c in terms:
        grouped.setdefault(f,[]).append((k,c))
    assert sum(map(len,grouped.values()))==273
    ub=A(B)
    phaseL={}
    phaseB={}
    pic=arb.pi()
    for f in grouped:
        w=2*pic*A(f)
        phaseL[f]=(w,acb(arb(0),w*L).exp())
        phaseB[f]=acb(arb(0),w*ub).exp()
    powersL=[arb(1)]
    powersB=[arb(1)]
    for k in range(13):
        powersL.append(powersL[-1]*L)
        powersB.append(powersB[-1]*ub)
    total=arb(0)
    for f,poly in grouped.items():
        w,eL=phaseL[f]
        eB=phaseB[f]
        zz=acb(arb(0),w)
        assert zz.is_finite()
        plo=acb(1)/zz
        phi=plo
        maxk=max(k for k,c in poly)
        moments=[eB*phi-eL*plo]
        for k in range(1,maxk+1):
            phi=(powersB[k]-k*phi)/zz
            plo=(powersL[k]-k*plo)/zz
            moments.append(eB*phi-eL*plo)
        for k,q in poly:
            total+=A(q)*(moments[k].imag if k%2==0 else moments[k].real)
    total+=2*A(pole)*((ub/2).cosh()-(L/2).cosh())
    assert total.is_finite()
    return total, len(grouped)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--source",default="notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json")
    ap.add_argument("--seams",default="notes/data/provisional/NF406_original_prime_support_partition_exact.json")
    ap.add_argument("--jet",default="notes/data/provisional/NF411_original_source_boundary_jet.json")
    ap.add_argument("--nf453",default="notes/data/provisional/NF453_original_J7_J8_principal_and_island_custody.json")
    ap.add_argument("--precision",type=int,default=4096)
    ap.add_argument("--output",required=True)
    args=ap.parse_args()
    assert args.precision>=3072
    ctx.prec=args.precision
    s,sha=read(args.source)
    geo,gs=read(args.seams)
    jet,js=read(args.jet)
    prev,ps=read(args.nf453)
    assert sha==SRC_SHA and gs==SEAM_SHA
    assert jet["nf407_source_sha256"]==sha
    assert prev["source_sha256"]==sha and prev["seams_sha256"]==gs
    assert prev["CI_status"]=="SUCCESS" and prev["D7_whole"]==prev["D8_whole"]=="OPEN"
    assert s["original_dimension"]==242
    assert len(s["original_exact_native_original_four_critical_coefficients_mid_radius"])==4
    assert len(s["original_source_critical_sine_frequencies"])==32
    terms,pole,s0=native_source(s)
    assert len(terms)==273 and s0<Q(1,10**700)
    assert all(0<f<883 and 0<=k<=13 for f,k,c in terms)

    prime9=next(p for p in geo["original_prime_power_log_shifts"] if p["n"]==9)
    log9lo,log9hi=Q(prime9["log_lower"]),Q(prime9["log_upper"])
    a_min,a_max=2*B-log9hi,2*B-log9lo
    assert 0<a_min<a_max<Q(3,1000)
    log9=arb(9).log()
    lo=log9-A(B)           # actual source endpoint B-a, x9
    a=2*A(B)-log9
    x9lo,x9hi=enclosure(lo)
    alo,ahi=enclosure(a)
    assert log9lo-B<=x9lo<=x9hi<=log9hi-B
    assert a_min<=alo<=ahi<=a_max
    assert x9lo>0

    src=U(s)
    v=src.at(C(B)).real
    v0,v1=enclosure(v)
    assert v1<0
    int_u,unique_f=integrate_original_U_small_boundary(terms,pole,lo)
    int0,int1=enclosure(int_u)
    mid_moment=v*a-int_u
    moment_lo,moment_hi=enclosure(mid_moment)
    # Same true dyadic source uncertainty appears twice; triangle overpay.
    source_charge=2*a_max*s0
    moment_lo-=source_charge
    moment_hi+=source_charge
    assert moment_lo<moment_hi
    # independent original NF411 endpoint value bracket
    assert -Q(117,10**13)<v0<v1<-Q(116,10**13)
    assert -Q(117,10**13)-s0<v0-s0<v1+s0<-Q(116,10**13)

    w=next(r for r in jet["all_seven_original_prime_seam_derivative_identities"] if r["prime_power"]==9)
    w0,w1=map(Q,w["c_n_positive_outward"])
    assert 0<w0<w1<Q(1)
    # ∫ z9 = -w9*A9, and 4∫ p9*z9 = -4*v*w9^2*A9.
    values=[-w0*moment_lo,-w0*moment_hi,-w1*moment_lo,-w1*moment_hi]
    zintlo,zinthi=min(values),max(values)
    true_v_bounds=(v0-s0,v1+s0)
    selfproducts=[-4*vv*(ww**2)*mm for vv in true_v_bounds for ww in (w0,w1) for mm in (moment_lo,moment_hi)]
    pz9lo,pz9hi=min(selfproducts),max(selfproducts)
    # Actual seven-prime constant piece C8 of full original principal p,
    # multiplied by the genuine n9 regular-source z9, not an artificial p9.
    c8lo=sum(Q(r["c_n_positive_outward"][0]) for r in jet["all_seven_original_prime_seam_derivative_identities"])
    c8hi=sum(Q(r["c_n_positive_outward"][1]) for r in jet["all_seven_original_prime_seam_derivative_identities"])
    assert 3<c8lo<c8hi<4
    constproducts=[-4*vv*ww*cc*mm for vv in true_v_bounds for ww in (w0,w1)
                   for cc in (c8lo,c8hi) for mm in (moment_lo,moment_hi)]
    constlo,consthi=min(constproducts),max(constproducts)
    # Final quantitative gates on the genuine original n9 source moment,
    # independent of float formatting in the diagnostic prints.
    assert -Q(4446541,10**19)<moment_lo<moment_hi<-Q(4446540,10**19)
    assert Q(1628341,10**19)<zintlo<zinthi<Q(1628342,10**19)
    assert -Q(2785906,10**30)<pz9lo<pz9hi<-Q(2785905,10**30)
    assert -Q(2691164,10**29)<constlo<consthi<-Q(2691163,10**29)

    out={
        "pass":"NF454",
        "standing":"ORIGINAL SOURCE-NATIVE n9 CONTACT LINEAR MOMENT, not whole J8 signed integral; numerical signs require focused CI",
        "source_sha256":sha,"seam_sha256":gs,"nf411_jet_SHA256":js,
        "nf453_original_principal_custody_SHA256":ps,
        "true_original_source_generators":246,
        "true_original_source_frequency_order_groups":len(terms),
        "true_original_distinct_frequencies":unique_f,
        "original_odd_sinh_retained":True,
        "original_coefficient_native_radius_paid":True,
        "native_precision_bits":ctx.prec,
        "true_n9_contact_x9_outward":[str(x9lo),str(x9hi)],
        "true_n9_overlap_length_a_outward":[str(alo),str(ahi)],
        "source_v_original_outward":[str(v0-s0),str(v1+s0)],
        "true_original_source_coefficient_S0":str(s0),
        "true_original_source_radius_charge_on_A9":str(source_charge),
        "actual_original_n9_boundary_A9_integral_outward":[str(moment_lo),str(moment_hi)],
        "original_z9_zeroth_moment_outward":[str(zintlo),str(zinthi)],
        "original_p9_z9_self_signed_4cross_outward":[str(pz9lo),str(pz9hi)],
        "original_full_principal_seven_weight_constant_cross_with_z9":[str(constlo),str(consthi)],
        "uncomputed_log_weighted_original_n9_source_moment":"OPEN",
        "A9_sign":"NEGATIVE" if moment_hi<0 else ("POSITIVE" if moment_lo>0 else "UNDECIDED"),
        "actual_original_z9_zeroth_moment_sign":"POSITIVE" if zintlo>0 else ("NEGATIVE" if zinthi<0 else "UNDECIDED"),
        "original_J8_source_increment_identity":"z9(x)=-w9*[U(x-log(9))+v]; p9=w9*v; p9+z9=-w9*U(x-log(9))",
        "true_original_complete_J7_signed":"OPEN","true_original_complete_J8_signed":"OPEN",
        "original_NF410_NF404_global_scalar":"OPEN","W_ODD_NEG":"OPEN","RH":"OPEN",
    }
    path=Path(args.output);path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(out,indent=2)+"\n")
    print("NF454 source-native n9 physical A9:",float(moment_lo),float(moment_hi),flush=True)
    print("NF454 true z9 moment:",float(zintlo),float(zinthi),flush=True)
    print("NF454 original n9 self 4*p9*z9:",float(pz9lo),float(pz9hi),flush=True)
    print("NF454 original full-principal CONSTANT cross with n9 source:",float(constlo),float(consthi),flush=True)
    print("NF454 whole J7/J8 signed integral, W-ODD-NEG, RH OPEN",flush=True)
if __name__=="__main__":main()
