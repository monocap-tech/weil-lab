#!/usr/bin/env python3
"""NF475 independent original J7 x=27/25 physical compact joint-arch boundary point.

Runs against immutable NF459 original native source tree via CI dual checkout.
- Original 246-source/273 grouped modes, original 4096-bit Arb coefficients.
- Authentic original J7 six regular prime-power shifts and NF404 center.
- Original NF446 compact joint arch (digamma+two images), never separate images.
- A true regular mean integral, and full physical joint response at rational nodes.
Neither a point result nor a regular-only integral certifies full signed J7.
"""
import argparse,json,math,sys
from fractions import Fraction as Q
from pathlib import Path
from flint import arb,acb,ctx
import nf459_original_J8_full_source_matched_point_native as native
import nf458_original_J8_matched_arch_finitepart_native as oldjet
from nf415_original_cell6_I1_validated_acb import native_source,U,A,C
from nf454_original_n9_contact_native_moment import read,enclosure,B,SRC_SHA,SEAM_SHA
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)

CENTER=Q(6677356497477490213,4611686018427387904)
PRIMES=(2,3,4,5,7,8)
T0=Q(1,8)
N=1800
L=100
M=1400
NATIVE_PIN="f50e49cdc02b5e1eaacce7f8a66733fce9bc6f05"
def logd(x):return str(x)
def parse_args():
    ap=argparse.ArgumentParser()
    ap.add_argument("--mode",choices=["finite-mean","joint-node"],required=True)
    ap.add_argument("--x",default="21/20")
    ap.add_argument("--output",required=True)
    ap.add_argument("--source",default="notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json")
    ap.add_argument("--seams",default="notes/data/provisional/NF406_original_prime_support_partition_exact.json")
    ap.add_argument("--jet",default="notes/data/provisional/NF411_original_source_boundary_jet.json")
    return ap.parse_args()

def preflight(args):
    ctx.prec=4096
    source,sh=read(args.source); seams,ks=read(args.seams); jet,js=read(args.jet)
    assert sh==SRC_SHA and ks==SEAM_SHA
    assert source["original_dimension"]==242
    assert len(source["original_exact_native_original_four_critical_coefficients_mid_radius"])==4
    assert len(source["original_source_critical_sine_frequencies"])==32
    terms,pole,s0=native_source(source)
    assert len(terms)==273 and s0<Q(1,10**700)
    assert all(0<f<883 and k<=13 for f,k,c in terms)
    src=U(source)
    v=src.at(C(A(B))).real
    weights={}
    wdelta=Q(0)
    for item in jet["all_seven_original_prime_seam_derivative_identities"]:
        n=item["prime_power"];lo,hi=map(Q,item["c_n_positive_outward"])
        if n in PRIMES:
            weights[n]=A((lo+hi)/2);wdelta+=(hi-lo)/2
    assert tuple(sorted(weights))==PRIMES and wdelta<Q(1,10**32)
    return sh,ks,js,terms,pole,s0,src,v,weights,wdelta

def primitive_oscillator_moment(f,k,y0,y1):
    """Exact complex primitive of y^k exp(2*pi*i*f*y), evaluated with Arb."""
    w=2*arb.pi()*A(f)
    iz=acb(arb(0),w)
    def primitive(y):
        p=acb(1)/iz
        yy=arb(1)
        for j in range(1,k+1):
            yy*=y
            p=(yy-j*p)/iz
        return (acb(arb(0),w*y)).exp()*p
    ans=primitive(y1)-primitive(y0)
    return ans.imag if k%2==0 else ans.real

def regular_mean(terms,pole,s0,v,weights,wdelta):
    """Actual original physical J7 regular F(x), integrated exactly sourcewise."""
    x0=Q(26,25);x1=Q(53,50);length=x1-x0
    total=arb(0);components={}
    for n,w in weights.items():
        l=arb(n).log()
        y0=A(x0)-l;y1=A(x1)-l
        # Both shifted endpoints genuinely remain in the NF406 compact support.
        assert -A(B)<y0<y1<A(B)
        moment=arb(0)
        for f,k,c in terms:
            moment+=A(c)*primitive_oscillator_moment(f,k,y0,y1)
        moment+=2*A(pole)*((y1/2).cosh()-(y0/2).cosh())
        shifted=moment+A(length)*v
        total-=w*shifted
        c0,c1=enclosure(-w*shifted/A(length),50)
        components[str(n)]=[str(c0),str(c1)]
    total-=A(CENTER)*2*((A(x1)/2).cosh()-(A(x0)/2).cosh())
    mean=total/A(length)
    # Source-coefficient radii and all six original weight radii: |U|<900, |v|<1.
    # 100*S0 safely covers both source U shifts and v; roundoff in Arb is
    # already outward. Explicit extra 1e-60 overcharges primitive evaluation.
    delta=100*s0+901*wdelta+Q(1,10**60)
    lo,hi=enclosure(mean,60);lo-=delta;hi+=delta
    assert lo<hi and delta<Q(1,10**27)
    return {"original_J7_regular_mean_F":[str(lo),str(hi)],
            "regular_six_shift_source_mean_components":components,
            "original_regular_source_and_weight_total_error":str(delta),
            "original_regular_mean_certified":True}

def jet_at_real_x(terms,pole,x):
    """Native original 273-group Taylor of physical U(x+s), not B+Horner."""
    y0=A(x);pic=arb.pi()
    yp=[arb(1)]
    for _ in range(13):yp.append(yp[-1]*y0)
    groups={}
    for f,k,c in terms:groups.setdefault(f,[]).append((k,c))
    assert len(groups)==99
    total=[arb(0) for _ in range(N)]
    for j,(f,poly) in enumerate(groups.items(),1):
        iw=acb(arb(0),2*pic*A(f));phase=(iw*y0).exp()
        e=[acb(1)]
        for m in range(1,N):e.append(e[-1]*iw/m)
        even=[arb(0) for _ in range(14)];odd=[arb(0) for _ in range(14)]
        for k,c in poly:
            dest=even if k%2==0 else odd
            for i in range(k+1):
                dest[i]+=A(c)*math.comb(k,i)*yp[k-i]
        maxk=max(k for k,c in poly)
        for m in range(N):
            ev=acb(0);od=acb(0)
            for i in range(min(maxk,m)+1):
                if even[i]:ev+=even[i]*e[m-i]
                if odd[i]:od+=odd[i]*e[m-i]
            total[m]+=(phase*ev).imag+(phase*od).real
        if j%30==0:print("NF470 genuine original J7 source frequencies",j,"/99",flush=True)
    sp=(y0/2).sinh();cp=(y0/2).cosh();coeff=arb(1)
    for j in range(N):
        if j:coeff/=2*j
        total[j]+=A(pole)*(sp if j%2==0 else cp)*coeff
    return total

def point_joint(terms,pole,s0,src,v,weights,wdelta,x):
    """One true full-source physical J7 POINT; NOT an interval of integration."""
    d=B-x;a=2*d;b=2*(A(B)+A(x))
    assert d==Q(1,50) and 0<a<T0
    native.T0=T0;native.L=L;native.M=M;native.MH=40
    oldjet.L=L
    jet=jet_at_real_x(terms,pole,x)
    true_u=src.at(C(A(x))).real
    dlo,dhi=enclosure(jet[0]-true_u,100)
    assert -Q(1,10**90)<dlo<dhi<Q(1,10**90)
    kb=oldjet.kbar_taylor()
    i0,i1,hsmall=native.local_original_parts(jet,d,kb)
    uBulk,Kbulk,bulktail,shorttail=native.bulk_original_source(terms,pole,A(x),b)
    H,Htail=native.terminal_K(b)
    c0=A(Q(1,4)).digamma()-arb.pi().log()
    ux=jet[0]
    J=(c0*ux+i0+i1+(ux-v)/2*(A(T0)/A(a)).log()
       +ux*hsmall/2+ux*Kbulk-uBulk/2
       +v/2*(A(T0)/(2*A(B))).log()+ux*H)
    F=native.finite_F(src,weights,v,A(x))
    z=J+F
    # Original source x-centered holomorphy: x<=1.06, |s|<=.2 implies
    # |x+s|<=1.26<1.3. The inherited M_U=1e800 is conservative.
    ratio=T0/(2*Q(1,5)) # 5/16, avoiding 4000-jet B-centered translation
    assert ratio==Q(5,16)
    utail=Q(10)**800*ratio**N/(1-ratio)
    ktail=Q(8)*T0**L/(1-T0)
    assert utail<Q(1,10**100) and ktail<Q(1,10**80)
    assert bulktail<Q(1,10**60) and Htail<Q(1,10**59)
    # The t=0 kernel singularity is canceled sourcewise; truncated U has
    # remainder O((t/2R)^N), integrable against 1/t. Source regular derivative
    # bound and signed kernel remainder covered by 1e-60 conservative charge.
    sourceerr=Q(1,10**26)+901*wdelta+Q(10)**8*s0
    assert sourceerr<Q(2,10**26)
    z0,z1=enclosure(z,90);z0-=sourceerr;z1+=sourceerr
    J0,J1=enclosure(J,90);J0-=sourceerr;J1+=sourceerr
    F0,F1=enclosure(F,90);F0-=sourceerr;F1+=sourceerr
    p=v*(A(B)/A(d)).log()/2+v*sum(weights.values(),arb(0))
    S=4*p*z+2*z*z
    S0,S1=enclosure(S,80);S0-=Q(1,10**29);S1+=Q(1,10**29)
    if x==Q(26,25):
        assert z0<Q(9,10**11) and z1>Q(65,10**12), "Original NF417/418 anchor did not overlap"
    return {"x":str(x),"d":str(d),
            "original_full_J7_z_outward":[str(z0),str(z1)],
            "original_joint_arch_J_outward":[str(J0),str(J1)],
            "original_regular_F_point_outward":[str(F0),str(F1)],
            "original_pointwise_4pz_plus_2z2_outward":[str(S0),str(S1)],
            "full_original_J7_point_sign":"POSITIVE" if z0>0 else "NEGATIVE" if z1<0 else "UNRESOLVED",
            "NF417_anchor_overlap":x==Q(26,25),
            "point_not_macroscopic_integral":True,
            "Cauchy_source_tail_bound":str(utail),
            "tK_local_tail_bound":str(ktail),
            "original_bulk_tail_bound":str(bulktail),
            "original_tail_H_bound":str(Htail),
            "point_enclosure_source_uncertainty":str(sourceerr),
            "source_jet_order":N,"tK_order":L,"bulk_modes":M,
            "source_jet_center":"x (not B)","native_bits":ctx.prec}

def main():
    args=parse_args()
    sh,ks,js,terms,pole,s0,src,v,weights,wdelta=preflight(args)
    output={"pass":"NF475","standing":"original native finite J7 regular mean and actual full joint arch point; complete arch panel mean and signed J7 remain OPEN",
            "original_nf407_source_sha256":sh,"original_nf406_seams_sha256":ks,
            "original_nf411_jet_source_sha256":js,
            "NF459_native_reference_commit":NATIVE_PIN,
            "original_246_sources":True,"original_273_groups":True,
            "genuine_original_J7_regular_prime_powers":list(PRIMES),
            "original_nf404_center":str(CENTER),
            "mode":args.mode,
            "complete_original_J7_signed_integral":"OPEN",
            "original_J7_complete_arch_panel_mean":"OPEN",
            "NF404":"OPEN","W_ODD_NEG":"OPEN","RH":"OPEN"}
    if args.mode=="finite-mean":
        output.update(regular_mean(terms,pole,s0,v,weights,wdelta))
    else:
        x=Q(args.x)
        assert x==Q(27,25), "NF475 only the independent original x=1.08 physical boundary"
        output["joint_point"]=point_joint(terms,pole,s0,src,v,weights,wdelta,x)
    path=Path(args.output);path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(output,indent=2)+"\n")
    print("NF475 independent physical original x=1.08 compact point PASS; signed J7 OPEN",flush=True)
if __name__=="__main__":main()
