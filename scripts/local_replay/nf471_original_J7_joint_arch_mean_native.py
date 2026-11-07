#!/usr/bin/env python3
"""NF471 complete original NF443↔NF446 joint arch J7 macroscopic mean.

The original native transfer is linear in the original NF407 source.  Compute
its x-integral **analytically** in the physical J7 fixed-support panel:
digamma polynomial/exponential primitives, both endpoint image families'
exponential primitives, removable sinh m=0 pole and original principal log.

Chunked 6000-image source-contracted sums are combined using exact Fraction
interval arithmetic, never independent interval bounds on the huge terms.
Original NF470 six-prime *regular* mean is appended only at final assembly.

Execution requires immutable NF459 original source tree at git SHA
f50e49cdc02b5e1eaacce7f8a66733fce9bc6f05 (contains native NF443).

No result is a full signed J7 integral: covariance / variance remain OPEN.
"""
from __future__ import annotations
import argparse,math,json,sys
from pathlib import Path
from fractions import Fraction as Q
from flint import arb,acb,ctx
from nf415_original_cell6_I1_validated_acb import native_source,U,A,C
from nf454_original_n9_contact_native_moment import read,enclosure,B,SRC_SHA,SEAM_SHA

if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
XLO=Q(26,25);XHI=Q(53,50);XC=Q(21,20);LEN=XHI-XLO
M=6000
PREC=4096
MAX_K=13
ORIGINAL_PARENT="f50e49cdc02b5e1eaacce7f8a66733fce9bc6f05"
NF470_RECEIPT="notes/data/provisional/NF470_original_J7_native_regular_mean_and_two_joint_points_custody.json"
SOURCES="notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json"
SEAMS="notes/data/provisional/NF406_original_prime_support_partition_exact.json"
J7_SUPPORT=(2,3,4,5,7,8)
def R(z):return acb(A(z))
def bounds(z,digits=450):
    return enclosure(z,digits)
def readsource(args):
    ctx.prec=PREC
    source,sha=read(args.source);seams,ssha=read(args.seams)
    assert (sha,ssha)==(SRC_SHA,SEAM_SHA)
    assert source["original_dimension"]==242
    assert len(source["original_exact_native_original_four_critical_coefficients_mid_radius"])==4
    assert len(source["original_source_critical_sine_frequencies"])==32
    assert source["W_ODD_NEG"]==source["RH"]=="OPEN"
    terms,pole,s0=native_source(source)
    assert len(terms)==273 and s0<Q(1,10**700)
    assert all(0<f<883 and 0<=k<=MAX_K for f,k,c in terms)
    raw=sum((abs(q)*B**k for f,k,q in terms),abs(pole))
    assert raw<Q(10)**160
    groups={}
    for f,k,q in terms:groups.setdefault(f,[]).append((k,q))
    assert len(groups)==99
    src=U(source)
    v=src.at(C(A(B))).real
    return sha,ssha,terms,pole,s0,groups,v

def moment_polynomial_exp(lam):
    """∫_XLO^XHI x^j exp(lam*x) dx for j=0..13 in native Arb."""
    lo=A(XLO);hi=A(XHI)
    phase0=(lam*lo).exp();phase1=(lam*hi).exp()
    p0=1/lam;p1=1/lam
    lower=arb(1);upper=arb(1)
    out=[(phase1*p1-phase0*p0)/A(LEN)]
    for j in range(1,MAX_K+1):
        lower*=lo;upper*=hi
        p0=(lower-j*p0)/lam
        p1=(upper-j*p1)/lam
        out.append((phase1*p1-phase0*p0)/A(LEN))
    return out

def native_alpha(q,k):
    """Exactly the original NF443 real sine/cosine coefficient convention."""
    return acb(arb(0),-A(q)/2) if k%2==0 else acb(A(q)/2)

def polygamma_D(lam):
    """Original NF443 D and all parameter derivatives, including log pi."""
    aa=R(Q(1,4));lo=aa-lam/2;hi=aa+lam/2
    out=[]
    for k in range(MAX_K+1):
        val=(lo.polygamma(k)*((-1)**k)+hi.polygamma(k))/(2**(k+1))
        if k==0:val-=acb.pi().log()
        out.append(val)
    return out

def center_pole_integral(pole):
    """Finite original native m0+digamma sinh-pole central expression."""
    Kpole=(A(1).digamma()+A(Q(1,2)).digamma())/2-arb.pi().log()-A(B)
    lo=A(XLO);hi=A(XHI);center=A(XC)
    # ∫ [Kpole*sinh(x/2)+x*cosh(x/2)] dx =
    # 2*Kpole*cosh(x/2)+2*x*sinh(x/2)-4*cosh(x/2)
    def primitive(x):return 2*Kpole*(x/2).cosh()+2*x*(x/2).sinh()-4*(x/2).cosh()
    mean=A(pole)*(primitive(hi)-primitive(lo))/A(LEN)
    point=A(pole)*(Kpole*(center/2).sinh()+center*(center/2).cosh())
    return mean,point

def central_original(terms,pole,groups,v):
    mean=arb(0);point=arb(0);endpoint=arb(0)
    center=A(XC);Bb=A(B)
    pi=arb.pi()
    for index,(f,poly) in enumerate(sorted(groups.items()),1):
        lam=acb(arb(0),2*pi*A(f))
        mom=moment_polynomial_exp(lam)
        deriv=polygamma_D(lam)
        exB=(lam*Bb).exp()
        exC=(lam*center).exp()
        for k,q in poly:
            alpha=native_alpha(q,k)
            endpoint+=2*(alpha*exB*Bb**k).real
            smean=acb(0);spoint=acb(0)
            for j in range(k+1):
                coeff=math.comb(k,j)*deriv[k-j]
                smean+=coeff*mom[j]
                spoint+=coeff*center**j
            mean+=2*(alpha*smean).real
            point+=2*(alpha*exC*spoint).real
        if index%20==0:
            print("NF471 original central digamma source frequencies",index,"/99",flush=True)
    pm,pp=center_pole_integral(pole)
    mean+=pm;point+=pp
    endpoint+=A(pole)*(Bb/2).sinh()
    vdelta=bounds(endpoint-v,110)
    assert vdelta[0]<Q(1,10**70) and vdelta[1]>-Q(1,10**70)
    # Explicit original principal subtraction: -v/2 log(B/(B-x)).
    def logprim(d):
        return A(d)*((A(B)/A(d)).log()+1)
    logmean=(logprim(B-XLO)-logprim(B-XHI))/A(LEN)
    mean-=endpoint*logmean/2
    point-=endpoint*(A(B)/A(B-XC)).log()/2
    return mean,point,vdelta

def image_groups(groups):
    """Original NF443 m image amplitudes after entire-source grouping."""
    pi=arb.pi();Bb=A(B)
    result=[]
    for f,poly in sorted(groups.items()):
        lam=acb(arb(0),2*pi*A(f));exB=(lam*Bb).exp()
        coefficients=[acb(0) for _ in range(MAX_K+1)]
        for k,q in poly:
            alpha=native_alpha(q,k)
            for j in range(k+1):
                co=Q(math.comb(k,j)*math.factorial(j),2**j)*B**(k-j)
                coefficients[j]+=alpha*exB*R(co)
        result.append((lam,coefficients))
    assert len(result)==99
    return result

def image_factors(m):
    """x-integrals of the TWO real endpoint images, no missing right image."""
    aa=A(Q(4*m+1,4))
    left_hi=(-2*aa*A(B-XHI)).exp()
    left_lo=(-2*aa*A(B-XLO)).exp()
    right_lo=(-2*aa*A(B+XLO)).exp()
    right_hi=(-2*aa*A(B+XHI)).exp()
    # Original native point image = total_m*(left-right)/2.
    fm=(left_hi-left_lo-right_lo+right_hi)/(4*aa*A(LEN))
    fp=((-2*aa*A(B-XC)).exp()-(-2*aa*A(B+XC)).exp())/2
    return fm,fp

def images_original(groups,pole,start,stop):
    image_source=image_groups(groups)
    mean=arb(0);point=arb(0)
    pole_coeff=A(pole);Bp2=(A(B)/2).exp();Bm2=(-A(B)/2).exp()
    for m in range(start,stop):
        aa=R(Q(4*m+1,4))
        total=arb(0)
        for lam,coeff in image_source:
            inv=1/(aa-lam/2)
            power=inv;acc=acb(0)
            for c in coeff:
                acc+=c*power
                power*=inv
            total+=2*acc.real
        # Native sinh pole finite m=0 remainder: DO NOT divide by m=0.
        if m==0:
            total-=pole_coeff*Bm2
        else:
            total+=pole_coeff*(Bp2/A(m)-Bm2/A(Q(2*m+1,2)))/2
        fm,fp=image_factors(m)
        mean+=total*fm
        point+=total*fp
        if (m+1)%250==0:
            print("NF471 real original 2-sided source image modes",m+1,"/",stop,flush=True)
    return mean,point

def emit_interval(z):
    lo,hi=bounds(z,450)
    e=Q(1,10**40)
    return [str(lo-e),str(hi+e)]

def analytic_tail():
    # |original image source amplitude at m|<=4*10^160/m,
    # on this panel exp[-2(m+1/4)(B-x)]<=exp[-(2/25)m].
    # ∑_{m>=6000} exp[-(2/25)m]/m
    # <=20 exp[-(2/25)*6000]/6000, and e^-1<3/8.
    # Round safe factor to 100, preserve exact-rational arithmetic.
    tail=Q(100*10**160,M)*Q(3,8)**(2*M//25)
    assert tail<Q(1,10**40)
    return tail

def make_part(args):
    sha,ssha,terms,pole,s0,groups,v=readsource(args)
    if args.part=="central":
        m,p,delta=central_original(terms,pole,groups,v)
        print("NF471 original independent endpoint source interval overlap",flush=True)
    else:
        assert args.start in range(0,M,1000) and args.stop==args.start+1000
        m,p=images_original(groups,pole,args.start,args.stop)
    result={
      "pass":"NF471","part":args.part,
      "mode":"full original NF443 central digamma+two image physical transfer integrated analytically",
      "source_sha256":sha,"seam_sha256":ssha,
      "original_nf407_generators":246,"original_273_groups":True,
      "original_sinh_pole":True,"original_critical_sines":32,
      "native_bits":ctx.prec,
      "panel":["26/25","53/50"],"point_check":"21/20",
      "image_start":args.start if args.part=="images" else None,
      "image_stop":args.stop if args.part=="images" else None,
      "source_part_mean_outward":emit_interval(m),
      "source_part_point_outward":emit_interval(p),
      "per_part_source_input_charge":"1e-40",
      "complete_original_J7_signed_integral":"OPEN"
    }
    Path(args.output).write_text(json.dumps(result,indent=2)+"\n")
    print("NF471 original source-correlated",args.part,"DONE",flush=True)

def assemble(args):
    folder=Path(args.input_dir)
    parts=list(folder.glob("nf471-*.json"))
    assert len(parts)==7, [x.name for x in parts]
    central=[q for q in parts if q.name=="nf471-central.json"]
    images=sorted([q for q in parts if q.name.startswith("nf471-images-")])
    assert len(central)==1 and len(images)==6
    records=[json.loads(f.read_text()) for f in central+images]
    assert sum(r["part"]=="central" for r in records)==1
    assert all(r["source_sha256"]==SRC_SHA and r["seam_sha256"]==SEAM_SHA for r in records)
    assert all(r["native_bits"]==PREC and r["original_273_groups"] for r in records)
    ranges=sorted((r["image_start"],r["image_stop"]) for r in records if r["part"]=="images")
    assert ranges==[(j,j+1000) for j in range(0,M,1000)]
    def combine(key):
        lo=sum((Q(r[key][0]) for r in records),Q(0))
        hi=sum((Q(r[key][1]) for r in records),Q(0))
        return lo,hi
    mlo,mhi=combine("source_part_mean_outward")
    plo,phi=combine("source_part_point_outward")
    tail=analytic_tail()
    mlo-=tail;mhi+=tail;plo-=tail;phi+=tail
    assert mlo<mhi and plo<phi
    # Independent source-native NF470 complete compact J from original
    # different Laplace architecture, at a genuine same-source J7 center.
    receipt=json.loads(Path(args.nf470_receipt).read_text())
    assert receipt["original_nf407_sha256"]==SRC_SHA
    assert receipt["original_nf406_sha256"]==SEAM_SHA
    assert receipt["original_modes"]==273
    old=tuple(map(Q,receipt["original_full_J7_points"]["21/20"]["joint_arch_decimal_outward"]))
    # Exact interval overlap after explicitly paying the new image tail.
    assert plo<=old[1] and old[0]<=phi, (
      "original NF470 independent joint source center mismatch",
      str(float(plo)),str(float(phi)),str(float(old[0])),str(float(old[1])))
    flo,fhi=map(Q,receipt["original_finite_regular_mean_interval_decimal_outward"])
    zlo=mlo+flo;zhi=mhi+fhi
    assert zlo<zhi
    # Decision-quality means require actual interval width <1e-17.
    assert mhi-mlo<Q(1,10**17)
    assert zhi-zlo<Q(1,10**17)
    result={
      "pass":"NF471","standing":"source-certified genuine original complete J7 macroscopic z mean; not signed D_I",
      "original_nf407_source_sha256":SRC_SHA,"original_nf406_seams_sha256":SEAM_SHA,
      "original_246_generators":True,"original_273_groups":True,
      "original_sinh_pole":True,"original_critical_sines":32,
      "original_native_parent":ORIGINAL_PARENT,"native_bits":PREC,
      "original_J7_macroscopic_panel":["26/25","53/50"],
      "analytic_original_source_mean_method":"full original native digamma+both image families, source-contracted, analytic x-primitives, 6000 image modes, original special m0 sinh pole, exact principal log",
      "original_arch_joint_J_mean_outward":[str(mlo),str(mhi)],
      "original_finite_regular_F_mean_outward":[str(flo),str(fhi)],
      "original_complete_z_mean_outward":[str(zlo),str(zhi)],
      "independent_NF470_original_same_source_center_overlap":True,
      "original_arch_joint_center_point_outward":[str(plo),str(phi)],
      "original_image_m6000_tail_rational":str(tail),
      "source_input_uncertainty_each_of_seven_parts":"1e-40",
      "original_full_signed_J7_panel":"OPEN",
      "source_correlated_covariance_variance":"OPEN",
      "NF404":"OPEN","W_ODD_NEG":"OPEN","RH":"OPEN",
      "next":"NF472 source-integrate original correlated second moments pz and z^2 using signed covariance and variance; neither mean nor point signs imply whole panel sign"
    }
    Path(args.output).write_text(json.dumps(result,indent=2)+"\n")
    print("NF471 actual ORIGINAL MACROSCOPIC J7 complete source mean",float(zlo),float(zhi),flush=True)
    print("NF471 exact ORIGINAL joint arch mean",float(mlo),float(mhi),flush=True)
    print("NF471 original complete signed J7 remains OPEN",flush=True)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--part",choices=["central","images","assemble"],required=True)
    ap.add_argument("--source",default=SOURCES)
    ap.add_argument("--seams",default=SEAMS)
    ap.add_argument("--start",type=int,default=0)
    ap.add_argument("--stop",type=int,default=0)
    ap.add_argument("--input-dir",default="../results")
    ap.add_argument("--nf470-receipt",default="../candidate/"+NF470_RECEIPT)
    ap.add_argument("--output",required=True)
    args=ap.parse_args()
    if args.part=="assemble":assemble(args)
    else:make_part(args)
if __name__=="__main__":main()
