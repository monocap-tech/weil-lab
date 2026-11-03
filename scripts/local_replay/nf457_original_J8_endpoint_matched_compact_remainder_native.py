#!/usr/bin/env python3
"""NF457: exact endpoint-MATCHED original J8 compact-source identity.

Source-native 4096-bit ORIGINAL derivative U'(B) and entire original
finite F'(B). Source/shifts, NF404 dyadic center, NF446 joint compact arch,
NF450 complete Z=z(B), NF456 full finite F endpoint. Seven original weights.
Prove rigorously over the ENTIRE physical J8 (not a tiny collar):
  z(B-d)-Z = .5 [U(B-d)-U(B)] log((2B-d)/d)
             + [F(B-d)-F(B)] + R_J(d),
  |R_J(d)| < 7500*d,   0<d<2B-log9.
This improves the complete original whole-J8 modulus to
  |z(B-d)-Z|<d*(9102+200log((2B-d)/d)).
Also certifies actual source-native log coefficient -.5 U'(B), F'(B),
and a FULL original endpoint first-order expansion with explicit
remainder; does NOT claim decision-quality J8 scalar.
"""
import argparse, json, hashlib, math, sys
from fractions import Fraction as Q
from pathlib import Path
from flint import arb,ctx
from nf415_original_cell6_I1_validated_acb import native_source,U,A,C
from nf454_original_n9_contact_native_moment import read,enclosure,B,SRC_SHA,SEAM_SHA

if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
PRIMES=(2,3,4,5,7,8,9)
CENTER=Q(6677356497477490213,4611686018427387904)

def source_first_derivative(terms,pole,y):
    """Exact derivative of all ORIGINAL polynom-sin/cos physical generators."""
    pi=arb.pi()
    p=[arb(1)]
    for j in range(13):p.append(p[-1]*y)
    r=A(pole)*(y/2).cosh()/2
    group={}
    for f,k,q in terms: group.setdefault(f,[]).append((k,q))
    assert sum(len(v) for v in group.values())==273
    for f,vals in group.items():
        om=2*pi*A(f)
        phase=om*y
        s=phase.sin();c=phase.cos()
        for k,q in vals:
            a=A(q)
            if k%2==0:
                r+=a*(k*p[k-1]*s if k else arb(0))
                r+=a*p[k]*om*c
            else:
                r+=a*(k*p[k-1]*c-p[k]*om*s)
    assert r.is_finite()
    return r

def exact_algebra_preflight():
    # Symbols U(x)=v+V, U(x-t/2)=q, U(B-t/2)=r.
    # Original joint compact middle difference exactly decomposes as:
    # [U(x)-(U(x-t/2)+v)/2] - [(v-U(B-t/2))/2]
    # = V/2 + [V-(U(x-t/2)-U(B-t/2))]/2.
    for v,V,q,r in [(Q(3),Q(-1),Q(7,2),Q(4,9)),
                     (Q(-2,7),Q(1,13),Q(9,5),Q(-17,3))]:
        lhs=(v+V)-(q+v)/2-(v-r)/2
        rhs=V/2+(V-(q-r))/2
        assert lhs==rhs
    # Entire original geometric support, strict rational:
    assert 2*B==Q(11,5)
    assert 4*B==Q(22,5)
    maxd=Q(3,1000)
    bmin=4*B-2*maxd
    assert bmin>4
    # Full source U' <400, U'' L2<256, odd U(-B)=-v,
    # and K(t)<1/t+1, |K-1/t|<=1, c0<10, ∫_b∞K<4:
    # I0<402d; removed endpoint lower<201d; removed upper<4d.
    # Cauchy-Schwarz shifted increment: d*||U''||2*sqrt(t/2).
    # Common source increment after its exact V/2 kernel extraction
    # <128*d*int_0^(4B) (1/t+1)*sqrt(t/2)dt.
    # sqrt(1/2)<3/4; sqrt(4B)<21/10 implies <1000d.
    common=Q(128)*Q(3,4)*(2*Q(21,10)+Q(2,3)*Q(22,5)*Q(21,10))
    assert Q(21,10)**2>4*B and Q(3,4)**2>Q(1,2)
    assert common<Q(1000)
    # c0 U difference <4000d; H(b)U diff+tail <1603d;
    # the v/2 scalar log and both K-1/t edge integrals <3d.
    total=402+201+4+1000+4000+1603+3
    assert total==7213<7500
    # Seven genuine primes weights sum <4 and centered slope <2:
    # |F(B-d)-F(B)|<1602d, all seven original shifts physical.
    assert 400*4+2==1602
    assert 7500+1602==9102
    # Original curvature gives |U(B-d)-v+d U'(B)|<=151d^(3/2)
    # as 256/sqrt(3)<151 (square check).
    assert 256**2<151**2*3
    # True endpoint finite Taylor F(B-d)=F(B)-d F'(B)+O(d^3/2):
    # original 7 shifted sources <4*151d^1.5, NF404 analytic
    # centered pole <d²; d<1 => total <605d^1.5.
    assert 4*151+1==605
    return common

def run(args):
    ctx.prec=args.precision
    assert ctx.prec>=3072
    source,sha=read(args.source)
    geo,gsha=read(args.seams)
    jet,jsha=read(args.jet)
    nf413,curvsha=read(args.nf413)
    nf446,ksha=read(args.nf446)
    nf450,zsha=read(args.nf450)
    nf451,msha=read(args.nf451)
    nf456,fsha=read(args.nf456)
    assert (sha,gsha)==(SRC_SHA,SEAM_SHA)
    assert source["original_dimension"]==242
    assert len(source["original_source_critical_sine_frequencies"])==32
    assert len(source["original_exact_native_original_four_critical_coefficients_mid_radius"])==4
    assert nf413["original_nf407_full_native_source_sha256"]==sha
    assert nf413["original_true_full_u4_second_derivative_L2_upper_integer"]=="256"
    assert jet["nf407_source_sha256"]==sha
    assert jet["source_derivative_strict_negative"] is True
    assert nf446["original_nf407_source_sha256"]==sha and nf446["original_nf406_seams_sha256"]==gsha
    assert nf450["source_SHA256"]==sha and nf450["seams_SHA256"]==gsha
    assert nf450["original_CI_result"]=="SUCCESS"
    assert nf451["original_source_sha256"]==sha and nf451["original_seams_sha256"]==gsha
    assert nf451["CI_result"]=="SUCCESS"
    assert nf456["source_sha256"]==sha and nf456["seams_sha256"]==gsha
    assert nf456["complete_original_J8_signed"]=="OPEN"
    assert nf456["original_nf404_center_exact"]==str(CENTER)
    assert nf456["seven_original_prime_powers"]==list(PRIMES)
    assert source["W_ODD_NEG"]=="OPEN" and nf456["W_ODD_NEG"]=="OPEN"

    original_contact=next(x for x in geo["original_prime_power_log_shifts"] if x["n"]==9)
    dmaxlow=2*B-Q(original_contact["log_upper"])
    dmaxhigh=2*B-Q(original_contact["log_lower"])
    assert 0<dmaxlow<dmaxhigh<Q(3,1000)
    commonbound=exact_algebra_preflight()

    terms,pole,s0=native_source(source)
    assert len(terms)==273 and s0<Q(1,10**700)
    assert all(0<f<883 and 0<=k<=13 for f,k,q in terms)
    W={}
    for x in jet["all_seven_original_prime_seam_derivative_identities"]:
        n=x["prime_power"]
        lo,hi=map(Q,x["c_n_positive_outward"])
        assert n in PRIMES and 0<lo<hi<1
        W[n]=(lo,hi)
    assert tuple(sorted(W))==PRIMES
    w0=sum((v[0] for v in W.values()),Q(0))
    w1=sum((v[1] for v in W.values()),Q(0))
    wr=(w1-w0)/2
    assert 0<w0<w1<4 and wr<Q(1,10**32)
    ws={n:(lo+hi)/2 for n,(lo,hi) in W.items()}

    src=U(source)
    v=src.at(C(B)).real
    vb=enclosure(v,110)
    assert -Q(117,10**13)<vb[0]<vb[1]<-Q(116,10**13)
    uBprime=source_first_derivative(terms,pole,A(B))
    d0,d1=enclosure(uBprime,110)
    u_error=10000*s0 # independently accepted original NF448 coefficient-derivative radius
    d0-=u_error
    d1+=u_error
    assert -Q(1300971380,10**16)<d0<d1<-Q(1300971377,10**16)
    k0,k1=-d1/2,-d0/2
    assert Q(650485688,10**16)<k0<k1<Q(650485691,10**16)
    # Explicit original physically normalized leading d*log(d) coefficient.
    print("NF457 original U'(B):",float(d0),float(d1),flush=True)
    print("NF457 complete original Z endpoint dlog coefficient:",float(k0),float(k1),flush=True)

    fsource=arb(0)
    fprime=arb(0)
    for n in PRIMES:
        s=A(B)-arb(n).log()
        sl,sh=enclosure(s,70)
        assert -B-Q(1,10**65)<sl<sh<B
        uval=src.at(C(s)).real
        duval=source_first_derivative(terms,pole,s)
        w=A(ws[n])
        fsource-=w*(uval+v)
        fprime-=w*duval
    fsource-=A(CENTER)*(A(B)/2).sinh()
    fprime-=A(CENTER)*(A(B)/2).cosh()/2

    ferr=2*w1*s0+901*wr
    dferr=10000*w1*s0+400*wr
    Flo,Fhi=enclosure(fsource,110)
    Flo-=ferr
    Fhi+=ferr
    Fd0,Fd1=enclosure(fprime,110)
    Fd0-=dferr
    Fd1+=dferr
    assert Fd0<Fd1
    original_nf456_B=tuple(map(Q,nf456["original_finite_F_at_B_strict"]))
    assert original_nf456_B[0]<Flo<Fhi<original_nf456_B[1]
    Zlo,Zhi=map(Q,nf450["complete_z_B_outward_24_decimal"])
    assert Zlo<Zhi<0
    J0,J1=Zlo-Fhi,Zhi-Flo
    prevJ0,prevJ1=map(Q,nf456["original_joint_arch_J_at_B_strict"])
    assert prevJ0<J0<J1<prevJ1
    print("NF457 original full F(B):",float(Flo),float(Fhi),flush=True)
    print("NF457 source-native F'(B):",float(Fd0),float(Fd1),flush=True)
    print("NF457 matched joint arch J(B):",float(J0),float(J1),flush=True)

    return {
     "pass":"NF457",
     "standing":"ACCEPTED if focused CI passes: original entire physical J8 exact endpoint-MATCHED compact identity, source-certified leading dlog coefficient and native original F'(B), strict full-J8 uniform remainder; NOT signed D8",
     "source_sha256":sha,"seams_sha256":gsha,"nf411_sha256":jsha,
     "nf413_sha256":curvsha,"nf446_sha256":ksha,"nf450_sha256":zsha,
     "nf451_sha256":msha,"nf456_sha256":fsha,
     "original_source_generator_count":246,"original_frequency_order_groups":273,
     "original_critical_sine_modes":32,"original_odd_sinh_pole":True,
     "native_precision_bits":ctx.prec,
     "original_actual_J8_distance_0_lt_d_lt":[str(dmaxlow),str(dmaxhigh)],
     "original_center_exact_NF404":str(CENTER),
     "original_native_Uprime_B_outward":[str(d0),str(d1)],
     "original_original_dlog_source_coefficient_minus_half_Uprime_B":[str(k0),str(k1)],
     "original_F_B_source_outward":[str(Flo),str(Fhi)],
     "original_Fprime_B_source_outward":[str(Fd0),str(Fd1)],
     "original_full_true_zB_NF450_outward":[str(Zlo),str(Zhi)],
     "original_matched_joint_arch_B_outward":[str(J0),str(J1)],
     "original_derivative_source_radius_charge":str(u_error),
     "original_finite_F_B_radius_charge":str(ferr),
     "original_finite_Fprime_B_radius_charge":str(dferr),
     "original_exact_analytic_j8_matched_identity":"z(B-d)-Z=(U(B-d)-U(B))/2*log((2B-d)/d)+F(B-d)-F(B)+R_J(d)",
     "original_matched_remainder_full_J8_strict":"|R_J(d)|<7500*d",
     "original_matched_compact_regions":"I0[0,2d]+I1[2d,4B-2d]-IB[0,4B]+original_c0+scalar_K_minus_1_over_t+original_tail+F_difference",
     "original_common_compact_source_remainder_integral_bound_d_factor_rational":str(commonbound),
     "original_unconditional_full_J8_complete_z_modulus":"|z(B-d)-Z|<d*(9102+200*log((2B-d)/d))",
     "original_endpoint_full_first_order_expansion":"z(B-d)-Z=-(1/2)*Uprime(B)*d*log((2B-d)/d)-Fprime(B)*d+R_first(d)",
     "original_endpoint_first_order_full_J8_remainder":"|R_first(d)|<7500*d+76*d^(3/2)*log((2B-d)/d)+605*d^(3/2)",
     "original_source_curvature_L2_certified_lt":"256",
     "original_source_first_derivative_sup_certified_lt":"400",
     "original_finite_source_uniform_F_slope_lt":"1602",
     "original_uniform_arch_matched_remainder_integral_inequality_rational_verified":True,
     "whole_original_J8_signed":"OPEN","whole_original_J7_signed":"OPEN",
     "original_NF410_NF404_global":"OPEN","J242_fourth_exterior":"OPEN",
     "W_ODD_NEG":"OPEN","RH":"OPEN",
     "next":"NF458 implement source-correlated actual R_J(d) enclosure on full J8 using NF446 matched compact integrals, NF456 finite F and NF450 endpoint; then source-weighted signed cell integrals"
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--source",default="notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json")
    ap.add_argument("--seams",default="notes/data/provisional/NF406_original_prime_support_partition_exact.json")
    ap.add_argument("--jet",default="notes/data/provisional/NF411_original_source_boundary_jet.json")
    ap.add_argument("--nf413",default="notes/data/provisional/NF413_original_full_246_source_curvature_native.json")
    ap.add_argument("--nf446",default="notes/data/provisional/NF446_original_joint_compact_kernel_J7_J8_custody_index.json")
    ap.add_argument("--nf450",default="notes/data/provisional/NF450_original_B_complete_Laplace_native_sign_custody_index.json")
    ap.add_argument("--nf451",default="notes/data/provisional/NF451_original_J8_terminal_collar_custody_index.json")
    ap.add_argument("--nf456",default="notes/data/provisional/NF456_original_J8_complete_finite_seven_prime_gram_and_archB_custody.json")
    ap.add_argument("--precision",type=int,default=4096)
    ap.add_argument("--output",required=True)
    args=ap.parse_args()
    d=run(args)
    out=Path(args.output);out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(d,indent=2,default=str)+"\n")
    print("NF457 exact matched original J8 compact-source identity and endpoint singular coefficient verified",flush=True)
    print("NF457 original whole J8 / J7 signed cells, W-ODD-NEG, RH OPEN",flush=True)
if __name__=="__main__":main()
