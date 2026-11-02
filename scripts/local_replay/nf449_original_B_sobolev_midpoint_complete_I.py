#!/usr/bin/env python3
"""NF449: exact original J8 B remainder via certified composite midpoint.

DO NOT interpret a passing quadrature job as signed J7/J8 or RH.
The full source is evaluated in 4096-bit Arb BEFORE cancellation and its
original dyadic coefficient uncertainty is charged separately.  No floating
mesh estimate or unverified Gauss rule enters the mathematical remainder.

For a=1/10,b=22/5, F(t)=K(t)(v-U(B-t/2))/2:
 |int_a^b F(t)dt - h sum_{j=0}^{N-1}F(a+(j+1/2)h)| <= 673 h^2.
Proof in NF449 note; original NF413 ||U''||_2<256 and original NF445
|U'(B)|<1 imply sup_{[-B,B]}|U'|<400.
"""
import argparse, hashlib, json, math, sys
from pathlib import Path
from fractions import Fraction as F
from flint import arb,ctx
from nf415_original_cell6_I1_validated_acb import native_source

if hasattr(sys, "set_int_max_str_digits"): sys.set_int_max_str_digits(0)
B=F(11,10)
LOW=F(1,10)
HIGH=F(22,5)
SOURCE_SHA="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAMS_SHA="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
NATIVE_SHA="51b8e0850c678085580940b3ab9afeff8277f446d4407c0200fb75754970db32"
PREFIX_SHA="5c4fa01cb23d2847b78d9bc3c7786e859ea7a713c466da42cf7ef1a04dda527f"
KNOWN_SHA="016b26dd713d796a99bb775a2ce6d0ba6173aff506bda609e96b0a6ab36c5164"

def read(p):
    raw=Path(p).read_bytes()
    return json.loads(raw),hashlib.sha256(raw).hexdigest()
def A(x):
    if isinstance(x,arb): return x
    if isinstance(x,F):return arb(x.numerator)/arb(x.denominator)
    return arb(x)
def outbound(x,digits=115):
    m,r,e=x.mid_rad_10exp(digits)
    scale=F(10)**int(e)
    return (F(int(m)-int(r))*scale,F(int(m)+int(r))*scale)
def overlap(x,y):
    return x[0]<=y[1] and y[0]<=x[1]
def endpoints(x):
    return [str(x[0]),str(x[1])]
def plus(x,y):
    return x[0]+y[0],x[1]+y[1]

class Source:
    def __init__(self,terms,pole):
        self.groups={}
        for f,k,c in terms:
            self.groups.setdefault(f,[]).append((k,A(c)))
        self.groups=list(self.groups.items())
        self.pole=A(pole)
        self.twopi=2*arb.pi()
    def at(self,x):
        powers=[arb(1)]
        for _ in range(13): powers.append(powers[-1]*x)
        out=self.pole*(x/2).sinh()
        for f,terms in self.groups:
            w=self.twopi*A(f)*x
            sn=w.sin(); co=w.cos()
            for k,c in terms:
                out+=c*powers[k]*(sn if k%2==0 else co)
        return out

def midpoint(source,v,n):
    h=(HIGH-LOW)/n
    step=A(h)
    t=A(LOW+h/2)
    s=arb(0)
    for j in range(n):
        x=A(B)-t/2
        denominator=1-(-t).exp()
        assert not denominator.contains(0)
        k=(-t/4).exp()/denominator
        s+=(k/2)*(v-source.at(x))
        t+=step
        if (j+1)%512==0:print("NF449 original source midpoint nodes",j+1,"/",n,flush=True)
    q=outbound(s*step)
    # NF413 + NF445 curvature and endpoint derivative, exact K monotonicity,
    # explicit L1 Peano kernel yield <673*h*h (see proof note).
    e=673*h*h
    return (q[0]-e,q[1]+e),q,e

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--source",default="notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json")
    p.add_argument("--seams",default="notes/data/provisional/NF406_original_prime_support_partition_exact.json")
    p.add_argument("--nf413",default="notes/data/provisional/NF413_original_full_246_source_curvature_native.json")
    p.add_argument("--nf445",required=True)
    p.add_argument("--nf448",required=True)
    p.add_argument("--nf447-known",required=True)
    p.add_argument("--output",required=True)
    p.add_argument("--precision",type=int,default=4096)
    p.add_argument("--nodes",type=int,default=4096)
    p.add_argument("--cross-nodes",type=int,default=1024)
    args=p.parse_args()
    assert args.precision>=3072 and args.nodes>=args.cross_nodes>=256
    ctx.prec=args.precision
    src,sha=read(args.source)
    seams,ksha=read(args.seams)
    curvature,_=read(args.nf413)
    native,nsha=read(args.nf445)
    pref,psha=read(args.nf448)
    known,zsha=read(args.nf447_known)
    assert (sha,ksha,nsha,psha,zsha)==(SOURCE_SHA,SEAMS_SHA,NATIVE_SHA,PREFIX_SHA,KNOWN_SHA)
    assert src["original_dimension"]==242
    assert len(src["original_exact_native_original_four_critical_coefficients_mid_radius"])==4
    assert len(src["original_source_critical_sine_frequencies"])==32
    assert curvature["original_nf407_full_native_source_sha256"]==sha
    assert curvature["original_true_full_u4_second_derivative_L2_upper_integer"]=="256"
    assert native["original_nf407_source_sha256"]==sha
    assert native["original_nf406_seams_sha256"]==ksha
    assert native["original_precision_bits"]==4096
    deriv=list(map(F,native["original_source_derivative_intervals_at_B"]["1"]))
    assert -1<deriv[0]<=deriv[1]<1
    assert pref["original_true_panel"]==["0","1/10"]
    assert known["original_original_source_246_selected_critical"]==246
    assert known["original_source_273_frequency_order"]==273
    assert all(d["W_ODD_NEG"]==d["RH"]=="OPEN" for d in (src,native,pref,known))
    terms,pole,s0=native_source(src)
    assert len(terms)==273 and s0<F(1,10**700)
    assert all(0<f<883 and 0<=k<=13 for f,k,c in terms)
    source=Source(terms,pole)
    v=source.at(A(B))
    assert overlap(outbound(v),tuple(map(F,native["original_source_v_analytic_carrier_interval"])))
    # Derive rational L1 curvature ceiling without a new source or support:
    # 100*(K(a)+a |K'(a)|) + 200 K(a) + 1/8 K(a)
    # * ||U''(B-t/2)||_L1 < 100*(11+411/40)+2200+1056
    # =5383.5 < 5384. Midpoint Peano kernel <=h^2/8, so 673h^2.
    assert F(100)*(11+F(411,40))+2200+1056==F(10767,2)
    assert F(10767,2)<5384 and F(5384,8)==673
    print("NF449 original rigorous Sobolev L1 second derivative < 5384",flush=True)
    main_iv,main_q,main_err=midpoint(source,v,args.nodes)
    cross_iv,cross_q,cross_err=midpoint(source,v,args.cross_nodes)
    radius=10**6*s0 # original full dyadic charge by NF448 U' error <=10000 S0
    main_iv=(main_iv[0]-radius,main_iv[1]+radius)
    cross_iv=(cross_iv[0]-radius,cross_iv[1]+radius)
    assert overlap(main_iv,cross_iv)
    assert main_q[1]-main_q[0]<F(1,10**30)
    assert cross_q[1]-cross_q[0]<F(1,10**30)
    assert main_iv[1]-main_iv[0]<F(1,100)
    assert main_err<F(1,1000)
    pref_iv=tuple(map(F,pref["original_full_true_panel_integral_enclosure"]))
    known_iv=tuple(map(F,known["original_all_known_joint_arch_scalar_prime_and_center_interval"]))
    assert pref_iv[0]<=pref_iv[1] and known_iv[0]<=known_iv[1]
    total=plus(pref_iv,main_iv)
    z=plus(known_iv,total)
    sign="POSITIVE" if z[0]>0 else "NEGATIVE" if z[1]<0 else "UNRESOLVED"
    out={
      "pass":"NF449",
      "standing":"CONDITIONAL until focused source-native CI; complete original compact endpoint I_B interval not J7/J8 signed cells",
      "original_source_SHA256":sha,"original_seams_SHA256":ksha,
      "original_NF445_native_SHA256":nsha,"original_NF448_prefix_SHA256":psha,
      "original_NF447_known_SHA256":zsha,
      "original_generators":246,"original_groups":273,"precision_bits":args.precision,
      "original_physical_source_argument_range":"[-11/10,21/20] subset [-11/10,11/10]",
      "original_remaining_panel":["1/10","22/5"],
      "original_Sobolev_curvature_L1_strict_upper":"5384",
      "original_midpoint_Peano_error":"673*(43/(10*N))^2",
      "original_main_nodes":args.nodes,"original_cross_nodes":args.cross_nodes,
      "original_main_midpoint_native_interval":endpoints(main_q),
      "original_cross_midpoint_native_interval":endpoints(cross_q),
      "original_main_exact_quadrature_error":str(main_err),
      "original_cross_exact_quadrature_error":str(cross_err),
      "original_source_dyadic_radius_charge":str(radius),
      "original_remaining_interval":endpoints(main_iv),
      "original_cross_independent_resolution_overlaps":True,
      "original_NF448_prefix_interval":endpoints(pref_iv),
      "original_complete_I_B_interval":endpoints(total),
      "original_NF447_known_part_interval":endpoints(known_iv),
      "original_complete_z_B_interval":endpoints(z),
      "original_z_B_sign_by_certified_interval":sign,
      "original_complete_I_B_source_certified_if_CI_pass":True,
      "original_z_B_source_certified_if_CI_pass":True,
      "original_J7_signed_integral_decided":False,
      "original_J8_signed_integral_decided":False,
      "original_full_NF410_NF404_scalar_decided":False,
      "W_ODD_NEG":"OPEN","RH":"OPEN"
    }
    dest=Path(args.output);dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(out,indent=2)+"\n")
    print("NF449 ORIGINAL complete I_B",float(total[0]),float(total[1]),"z(B)",float(z[0]),float(z[1]),"SIGN",sign,flush=True)
    print("NF449 original J7/J8 whole signed integrals, global RH remain OPEN",flush=True)

if __name__=="__main__":main()
