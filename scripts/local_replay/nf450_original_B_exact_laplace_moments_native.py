#!/usr/bin/env python3
"""NF450: complete original J8 B endpoint compact integral with exact Laplace moments.

Original 246-generator / 273 grouped physical source retained. On [a,b]=[.1,4.4],
K(t)=sum_{m>=0}exp(-(m+1/4)t) exactly, and each source generator is a
polynomial times one sine/cos or the actual odd sinh pole. Integrate each
finite-m Laplace moment analytically with 4096-bit outward Acb/Arb.

The uncomputed geometric-series tail is bounded solely by ACCEPTED original
NF413 ||U''||2<256 and NF445 |U'(B)|<1, giving |U(B)-U(B-t/2)|<200t.
Tail_m>=M < 1100*(3/8)^floor((M+1/4)/10) *
                 (1/(10*(M+1/4))+1/(M+1/4)^2).
The 3/8 rational base follows e>8/3 (strict); no floating gamma tails.

Neither source/radius nor any genuine n=2,3,4,5,7,8,9 prime term changes.
The original source continues physically ONLY on [-B,B].
CI must pass before numerical sign can be promoted.
"""
import argparse,hashlib,json,sys
from pathlib import Path
from fractions import Fraction as F
from flint import arb,acb,ctx
from nf415_original_cell6_I1_validated_acb import native_source
from nf449_original_B_sobolev_midpoint_complete_I import (
    A,Source,outbound,overlap,plus,endpoints,
    SOURCE_SHA,SEAMS_SHA,NATIVE_SHA,PREFIX_SHA,KNOWN_SHA,
)

if hasattr(sys,"set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)
B=F(11,10); a=F(1,10); b=F(22,5)
YA=B-a/2; YB=B-b/2
M_FULL=384; M_SHORT=320
NF449_SOURCE_SHA="9b4aca393d5c15faa69be3c1a47fef78c742cb26"

def read(p):
    raw=Path(p).read_bytes()
    return json.loads(raw),hashlib.sha256(raw).hexdigest()

def rate_integral(rate):
    """Exact finite-interval exponential integral, in outward Arb."""
    if rate==0:
        return A(b-a)
    r=A(rate)
    return ((-r*A(a)).exp()-(-r*A(b)).exp())/r

def source_radius_levy(s0):
    # Original NF448/NF449: uniform real physical |delta U'(y)|<10000*S0.
    # On t∈[a,b], |delta v - delta U(B-t/2)|<5000*t*S0,
    # so |delta F|<2500*t*K(t)*S0 and t*K(t)<1+t <=27/5.
    # Total source discrepancy < 2500*(43/10)*(27/5)*S0=58050*S0.
    assert 2500*(b-a)*(1+b)<10**6
    return 10**6*s0

def geometric_tail(m):
    """Exact rational upper bound using e>8/3 and 1/(1-e^-a)<11."""
    lam=F(4*m+1,4)
    n=int(lam*a)
    assert n>=0
    bound=F(1100)*(F(3,8)**n)*(a/lam + 1/(lam*lam))
    return bound

def verify_polynomial_primitive():
    # For k>=0: P_k(y;z) = y^k/z - (k/z)P_{k-1}(y;z).
    # Exactly (d/dy + z)P_k=y^k, checked here as rational polynomials
    # at 4 independently selected nonzero rational z, through degree13.
    for z in (F(1,4),F(3,2),F(5,7),F(8,3)):
        p=[F(1)/z]
        for k in range(1,14):
            # polynomial in y as coefficient array
            old=p[:]
            p=[-F(k)*v/z for v in old]+[F(1)/z]
            # above coefficient arrays include the high-degree j=k term.
            assert len(p)==k+1
            derivative=[F(j+1)*p[j+1] for j in range(k)]
            for j in range(k+1):
                lhs=z*p[j]+(derivative[j] if j<k else 0)
                assert lhs==(F(1) if j==k else F(0))
    return True

def analytic_sum(terms,pole,v,mfull,mshort):
    # Keep all 273 (frequency,order) groups. Every complex phase depends
    # only on physical endpoint and ORIGINAL f, not on Laplace index m.
    grouped={}
    for f,k,c in terms:
        grouped.setdefault(f,[]).append((k,A(c)))
    assert sum(map(len,grouped.values()))==273

    pi=arb.pi()
    zarg_a=A(YA);zarg_b=A(YB)
    yp_a=[arb(1)];yp_b=[arb(1)]
    for _ in range(13):
        yp_a.append(yp_a[-1]*zarg_a)
        yp_b.append(yp_b[-1]*zarg_b)
    phase={}
    for f in grouped:
        om=2*pi*A(f)
        phase[f]=(om,acb(arb(0),om*zarg_a).exp(),acb(arb(0),om*zarg_b).exp())
    assert len(phase)>0
    val=arb(0)
    short=None
    for m in range(mfull):
        lam=F(4*m+1,4)
        la=A(lam)
        ea=(-la*A(a)).exp()
        eb=(-la*A(b)).exp()
        uv=arb(0)
        # Exact original physical polynomial-oscillator Laplace moments.
        # Substitute y=B-t/2. Then J_k=2( E_a P_k(YA)-E_b P_k(YB)),
        # E_x=e^-lam t_x e^(i 2pi f Y_x), ζ=2lam+i 2pi f,
        # P0=1/ζ, Pk=(y^k-k P_{k-1})/ζ.
        for f,poly in grouped.items():
            om,pha,phb=phase[f]
            zz=acb(2*la,om)
            pa=acb(1)/zz
            pb=pa
            maxk=max(k for k,c in poly)
            moments=[2*(pha*ea*pa-phb*eb*pb)]
            for k in range(1,maxk+1):
                pa=(yp_a[k]-k*pa)/zz
                pb=(yp_b[k]-k*pb)/zz
                moments.append(2*(pha*ea*pa-phb*eb*pb))
            for k,c in poly:
                uv+=c*(moments[k].imag if k%2==0 else moments[k].real)
        # The true original sinh source is not a new imaginary frequency.
        # One special exact rate m=0 has lam-1/4=0.
        pole_int=(A(B)/2).exp()*rate_integral(lam+F(1,4))
        pole_int-=(-(A(B)/2)).exp()*rate_integral(lam-F(1,4))
        uv+=A(pole)*pole_int/2
        vpart=v*(ea-eb)/la
        val+=(vpart-uv)/2
        if m+1==mshort:
            short=outbound(val)
        if (m+1)%32==0:
            print("NF450 complete source exact Laplace moments",m+1,"/",mfull,flush=True)
    assert short is not None
    return outbound(val),short,len(phase)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--source",default="notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json")
    ap.add_argument("--seams",default="notes/data/provisional/NF406_original_prime_support_partition_exact.json")
    ap.add_argument("--nf413",default="notes/data/provisional/NF413_original_full_246_source_curvature_native.json")
    ap.add_argument("--nf445",required=True)
    ap.add_argument("--nf447-known",required=True)
    ap.add_argument("--nf448",required=True)
    ap.add_argument("--nf449",required=True)
    ap.add_argument("--output",required=True)
    ap.add_argument("--precision",type=int,default=4096)
    args=ap.parse_args()
    assert args.precision>=3072
    ctx.prec=args.precision
    src,sh=read(args.source)
    seams,ks=read(args.seams)
    curv,curv_sha=read(args.nf413)
    native,ns=read(args.nf445)
    prefix,ps=read(args.nf448)
    known,zs=read(args.nf447_known)
    old,oldsha=read(args.nf449)
    assert (sh,ks,ns,ps,zs)==(SOURCE_SHA,SEAMS_SHA,NATIVE_SHA,PREFIX_SHA,KNOWN_SHA)
    assert curv["original_nf407_full_native_source_sha256"]==sh
    assert curv["original_true_full_u4_second_derivative_L2_upper_integer"]=="256"
    assert old["original_source_SHA256"]==sh and old["original_generators"]==246
    assert old["original_groups"]==273 and old["original_complete_I_B_source_certified_if_CI_pass"]
    assert native["original_precision_bits"]==4096
    assert native["original_nf407_source_sha256"]==sh
    assert native["original_nf406_seams_sha256"]==ks
    assert prefix["original_true_panel"]==["0","1/10"]
    assert prefix["original_nf445_native_json_sha256"]==ns
    assert known["original_original_source_246_selected_critical"]==246
    assert known["original_source_273_frequency_order"]==273
    assert all(x["W_ODD_NEG"]==x["RH"]=="OPEN" for x in (src,native,prefix,known,old))
    terms,pole,s0=native_source(src)
    assert len(terms)==273 and s0<F(1,10**700)
    assert len(src["original_exact_native_original_four_critical_coefficients_mid_radius"])==4
    assert len(src["original_source_critical_sine_frequencies"])==32
    assert all(0<f<883 and 0<=k<=13 for f,k,c in terms)
    assert verify_polynomial_primitive()
    v=Source(terms,pole).at(A(B))
    assert overlap(outbound(v),tuple(map(F,native["original_source_v_analytic_carrier_interval"])))
    derivative=list(map(F,native["original_source_derivative_intervals_at_B"]["1"]))
    assert -1<derivative[0]<=derivative[1]<1
    tail_full=geometric_tail(M_FULL)
    tail_short=geometric_tail(M_SHORT)
    assert tail_full<F(1,10**16) and tail_short<F(1,10**13)
    print("NF450 rational strict full and shorter Laplace series bounds",float(tail_full),float(tail_short),flush=True)
    num_full,num_short,nfreq=analytic_sum(terms,pole,v,M_FULL,M_SHORT)
    source_charge=source_radius_levy(s0)
    full=(num_full[0]-tail_full-source_charge,num_full[1]+tail_full+source_charge)
    short=(num_short[0]-tail_short-source_charge,num_short[1]+tail_short+source_charge)
    assert overlap(full,short)
    assert full[1]-full[0]<F(1,10**14)
    # Independently certified previous NF449 physical Sobolev enclosure:
    old_rem=tuple(map(F,old["original_remaining_interval"]))
    assert overlap(full,old_rem)
    pref_iv=tuple(map(F,prefix["original_full_true_panel_integral_enclosure"]))
    known_iv=tuple(map(F,known["original_all_known_joint_arch_scalar_prime_and_center_interval"]))
    I=plus(pref_iv,full)
    z=plus(I,known_iv)
    old_z=tuple(map(F,old["original_complete_z_B_interval"]))
    assert overlap(z,old_z)
    sign="NEGATIVE" if z[1]<0 else "POSITIVE" if z[0]>0 else "UNRESOLVED"
    out={
       "pass":"NF450",
       "standing":"SOURCE-NATIVE HIGH-PRECISION COMPLETE I_B AND z(B) INTERVAL, ACCEPT ONLY AFTER FULL FOCUSED CI",
       "original_source_SHA256":sh,
       "original_seams_SHA256":ks,
       "original_nf413_source_sha256":curv_sha,
       "original_nf445_native_SHA256":ns,
       "original_nf447_known_SHA256":zs,
       "original_nf448_prefix_SHA256":ps,
       "original_nf449_native_SHA256":oldsha,
       "original_selected_critical_generators":246,
       "original_frequency_order_groups":len(terms),
       "original_distinct_source_frequencies":nfreq,
       "original_critical_sines":32,
       "original_odd_sinh_pole_included":True,
       "original_native_precision_bits":args.precision,
       "original_physical_source_support_preserved":"[-11/10,11/10]",
       "original_remaining_true_t_interval":["1/10","22/5"],
       "original_full_Laplace_m_terms":M_FULL,
       "original_short_Laplace_m_terms":M_SHORT,
       "original_geometric_kernel_identity":"K(t)=sum_m>=0 exp(-(m+1/4)*t), t>0",
       "original_exact_polynomial_complex_Laplace_primitive_verified":True,
       "original_exact_rational_tail_full":str(tail_full),
       "original_exact_rational_tail_short":str(tail_short),
       "original_source_coefficient_radius_charge":str(source_charge),
       "original_full_native_interval":endpoints(num_full),
       "original_short_native_interval":endpoints(num_short),
       "original_remaining_interval":endpoints(full),
       "original_short_remaining_interval":endpoints(short),
       "original_short_truncation_overlaps":True,
       "original_NF449_independent_Sobolev_enclosure_overlaps":True,
       "original_full_I_B_interval":endpoints(I),
       "original_full_zB_interval":endpoints(z),
       "original_NF449_original_zB_overlaps":True,
       "original_zB_sign_certified_by_interval":sign,
       "original_true_J7_signed_integral_decided":False,
       "original_true_J8_signed_integral_decided":False,
       "original_original_NF410_NF404_global_scalar_decided":False,
       "W_ODD_NEG":"OPEN","RH":"OPEN"
    }
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(out,indent=2)+"\n")
    print("NF450 ORIGINAL TRUE FULL I_B",float(I[0]),float(I[1]),flush=True)
    print("NF450 ORIGINAL TRUE z(B)",float(z[0]),float(z[1]),"SIGN:",sign,flush=True)
    print("NF450 J7/J8 actual signed cells W-ODD-NEG RH OPEN",flush=True)

if __name__=="__main__":main()
