#!/usr/bin/env python3
"""NF482-A genuine source-original J8 n9-entry FIRST physical signed panel.

The true physical interval is [log(9)-B,549/500] with B=11/10,
x=686/625+(1/2500)t, t in [tlo,1], N=1200, real source and Arb.
Retain 246 genuine NF407 dyadic original source, all 273 original grouped
modes/99 frequencies, correct odd sinh pole, true NF406 SEVEN minus
prime-power support n=2,3,4,5,7,8,9, original NF404 center, original
NF443↔NF446 central digamma and BOTH matched finite 18000 images.

At every point of THIS first original physical J8 panel B-x>=1/500,
so the NF477 true source-correlated all-m image-amplitude bound transfers
through the exact original geometric series at this restricted range.
This restriction does NOT cover full J8 through B; NF481 separate full
source endpoint-corrected 20-jet method must be used there.
The true left physical endpoint is irrational and integrated with original
4096-bit Arb monomial primitives (no rational substitution).
"""
from __future__ import annotations
import argparse, json, math, sys
from pathlib import Path
from fractions import Fraction as Q
from flint import arb,acb,ctx
from nf415_original_cell6_I1_validated_acb import native_source,U,A,C
from nf454_original_n9_contact_native_moment import read,enclosure,B,SRC_SHA,SEAM_SHA
import nf471_original_J7_joint_arch_mean_native as nf471
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)

XC=Q(686,625);H=Q(1,2500);N=1200;M=18000;PREC=4096
PRIMES=(2,3,4,5,7,8,9)
CENTER=Q(6677356497477490213,4611686018427387904)
SOURCE_TREE="f50e49cdc02b5e1eaacce7f8a66733fce9bc6f05"
R_CAUCHY=Q(1,1000)
S0_BOUND=Q(1,10**700)
def native_data(args):
    ctx.prec=PREC
    orig,sh=read(args.source);seams,ks=read(args.seams)
    assert (sh,ks)==(SRC_SHA,SEAM_SHA)
    assert orig["original_dimension"]==242
    assert len(orig["original_exact_native_original_four_critical_coefficients_mid_radius"])==4
    assert len(orig["original_source_critical_sine_frequencies"])==32
    terms,pole,s0=native_source(orig)
    assert len(terms)==273 and s0<S0_BOUND
    assert all(0<f<883 and k<=13 for f,k,c in terms)
    raw=sum((abs(c)*B**k for f,k,c in terms),abs(pole))
    assert raw<Q(10)**160
    groups={}
    for f,k,c in terms:groups.setdefault(f,[]).append((k,c))
    assert len(groups)==99
    src=U(orig);v=src.at(C(A(B))).real
    return sh,ks,terms,pole,s0,groups,v

def binom(n,k):return math.comb(n,k)
def make_poly(coeffs,lam,cy,source_mode):
    """Original scalar complex source polynomial at y=cy+H*s,
    multiplied by exp(lam*y), with source coefficient correlation intact."""
    polynomial=[acb(0) for _ in range(14)]
    if source_mode=="digamma": D=nf471.polygamma_D(lam)
    for k,c in coeffs:
        alpha=nf471.native_alpha(c,k)
        if source_mode=="digamma":
            for j in range(k+1):
                qq=alpha*binom(k,j)*D[k-j]
                for t in range(j+1):
                    polynomial[t]+=qq*binom(j,t)*cy**(j-t)*A(H)**t
        else:
            for t in range(k+1):
                polynomial[t]+=alpha*binom(k,t)*cy**(k-t)*A(H)**t
    # Horner recurrence for the exponential s-series, then P(s)*exp(lam*H*s).
    ev=[acb(1)]
    rate=lam*A(H)
    for j in range(1,N):
        ev.append(ev[-1]*rate/j)
    phase=(lam*cy).exp()
    out=[arb(0) for _ in range(N)]
    for n in range(N):
        z=acb(0)
        for j in range(min(13,n)+1):
            z+=polynomial[j]*ev[n-j]
        out[n]=2*(phase*z).real
    return out

def sinh_cosh_series(cy):
    """Taylor of sinh((cy+H*s)/2), cosh((cy+H*s)/2)."""
    plus=[(cy/2).exp()];minus=[(-cy/2).exp()]
    for i in range(1,N):
        plus.append(plus[-1]*A(H)/2/i)
        minus.append(minus[-1]*(-A(H))/2/i)
    return ([(a-b)/2 for a,b in zip(plus,minus)],
            [(a+b)/2 for a,b in zip(plus,minus)])

def central_part(groups,pole,v):
    result=[arb(0) for _ in range(N)]
    for i,(f,poly) in enumerate(sorted(groups.items()),1):
        lam=acb(arb(0),2*arb.pi()*A(f))
        coeff=make_poly(poly,lam,A(XC),"digamma")
        for j in range(N):result[j]+=coeff[j]
        if i%20==0:print("NF482-A genuine original central frequencies",i,"/99",flush=True)
    sp,cp=sinh_cosh_series(A(XC))
    Kpole=(A(1).digamma()+A(Q(1,2)).digamma())/2-arb.pi().log()-A(B)
    for j in range(N):
        xc_cp=A(XC)*cp[j]
        if j:xc_cp+=A(H)*cp[j-1]
        result[j]+=A(pole)*(Kpole*sp[j]+xc_cp)
        # Original *source*-independent NF404 exact centered odd sinh.
        result[j]-=A(CENTER)*sp[j]
    # The same original endpoint value v enters the original
    # principal-log subtraction, NOT into the finite regular shifts here.
    assert B-XC==Q(3,1250) and H/(B-XC)==Q(1,6)
    result[0]-=v/2*(A(B)/A(B-XC)).log()
    q=Q(1,6);power=q
    for j in range(1,N):
        result[j]-=v/2*A(power)/j
        power*=q
    return result

def image_part(groups,pole,start,stop):
    """NF471 original shared image amplitude, expanded in physical s variable."""
    assert 0<=start<stop<=M and start%2000==0 and stop==start+2000
    image_groups=nf471.image_groups(groups)
    result=[arb(0) for _ in range(N)]
    v=A(pole);Bp2=(A(B)/2).exp();Bm2=(-A(B)/2).exp()
    for m in range(start,stop):
        aa=acb(A(Q(4*m+1,4)))
        total=arb(0)
        for lam,cs in image_groups:
            inv=1/(aa-lam/2)
            power=inv;one=acb(0)
            for c in cs:
                one+=c*power
                power*=inv
            total+=2*one.real
        if m==0:
            total-=v*Bm2
        else:
            total+=v*(Bp2/A(m)-Bm2/A(Q(2*m+1,2)))/2
        rate=2*A(Q(4*m+1,4))*A(H)
        left=(-2*A(Q(4*m+1,4))*A(B-XC)).exp()
        right=(-2*A(Q(4*m+1,4))*A(B+XC)).exp()
        pl=arb(1);pr=arb(1)
        for j in range(N):
            result[j]+=total*(left*pl-right*pr)/2
            pl=pl*rate/(j+1)
            pr=pr*(-rate)/(j+1)
        if (m+1)%250==0:
            print("NF482-A original two-sided images",m+1,"/",stop,flush=True)
    return result

def prime_part(groups,pole,v,args):
    """Genuine original J7 n=2,3,4,5,7,8 minus regular translates."""
    jet,jsha=read(args.jet)
    assert jet["all_seven_original_prime_seam_derivative_identities"]
    weights={}
    wdelta=Q(0)
    for item in jet["all_seven_original_prime_seam_derivative_identities"]:
        n=item["prime_power"]
        if n in PRIMES:
            lo,hi=map(Q,item["c_n_positive_outward"])
            weights[n]=A((lo+hi)/2);wdelta+=(hi-lo)/2
    assert tuple(sorted(weights))==PRIMES and wdelta<Q(1,10**32)
    result=[arb(0) for _ in range(N)]
    for n,w in weights.items():
        cy=A(XC)-arb(n).log()
        # Entire complex carrier may cross the n9 physical support seam;
        # the actual original J7 six-minus support is used only up to log9-B.
        assert -A(B)-A(R_CAUCHY)<cy-A(H)<cy+A(H)<A(B)
        one=[arb(0) for _ in range(N)]
        for i,(f,poly) in enumerate(sorted(groups.items()),1):
            lam=acb(arb(0),2*arb.pi()*A(f))
            co=make_poly(poly,lam,cy,"raw")
            for j in range(N):one[j]+=co[j]
        sp,_=sinh_cosh_series(cy)
        for j in range(N):
            result[j]-=w*(one[j]+A(pole)*sp[j])
        result[0]-=w*v
        print("NF482-A original physical negative regular prime shift",n,"/7",flush=True)
    return result,weights,wdelta,jsha

def save_part(args):
    sha,seam,terms,pole,s0,groups,v=native_data(args)
    assert ctx.prec==PREC
    if args.part=="central":
        coeff=central_part(groups,pole,v)
    elif args.part=="images":
        coeff=image_part(groups,pole,args.start,args.stop)
    else:
        coeff,weights,wdelta,jetsha=prime_part(groups,pole,v,args)
    balls=[list(map(str,enclosure(c,300))) for c in coeff]
    # The interval width is the native 300-significant-decimal precision error;
    # input-radii and truncation are paid separately in assembly, not hidden.
    out={
       "pass":"NF482-A","part":args.part,
       "original_nf407_source_sha256":sha,"original_nf406_seams_sha256":seam,
       "original_246_generators":True,"original_273_groups":True,
       "original_critical_sines":32,"original_sinh_pole":True,
       "native_bits":PREC,"polynomial_degree":N-1,
       "physical_panel":["log9-B","549/500"],"center":"686/625","halfwidth":"1/2500",
       "original_image_index_start":args.start if args.part=="images" else None,
       "original_image_index_stop":args.stop if args.part=="images" else None,
       "source_radii_lt":"1e-700",
       "original_prime_wdelta_lt":"1e-32" if args.part=="primes" else None,
       "coefficient_interval_balls":balls,
       "J8_signed_cell":"OPEN","NF404":"OPEN","W_ODD_NEG":"OPEN","RH":"OPEN"
    }
    dest=Path(args.output);dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(out,separators=(",",":"))+"\n")
    print("NF482-A original",args.part,"coefficients",len(balls),"DONE",flush=True)

def original_J8_true_irrational_entry_moments():
    """Original J8 first [log9-B,549/500] physical Arb primitives: t∈[tlo,1]."""
    xleft=arb(9).log()-A(B)
    xright=A(Q(549,500))
    Lphys=xright-xleft
    tlo=(xleft-A(XC))/A(H)
    thi=(xright-A(XC))/A(H)
    assert A(Q(7,10000))<Lphys<A(Q(1,1000))
    assert -arb(1)<tlo<0
    assert XC+H==Q(549,500)  # true right physical x, exact rational
    thi=arb(1)
    assert A(XC)-A(H)<xleft<xright
    assert A(XC)+A(R_CAUCHY)<A(B)
    assert B-Q(549,500)==Q(1,500)
    moments=[]
    lo=arb(1);hi=arb(1);den=thi-tlo
    for k in range(2*N):
        lo*=tlo;hi*=thi
        moments.append((hi-lo)/(den*(k+1)))
    l,h=enclosure(moments[0],100)
    assert l<=Q(1)<=h
    return xleft,xright,Lphys,tlo,thi,moments

def native_arb_mean(a,moments):
    assert len(a)<=len(moments)
    return sum((x*moments[k] for k,x in enumerate(a)),arb(0))

def bounds_fraction_intervals(balls):
    return [tuple(map(Q,p)) for p in balls]

def assemble(args):
    folder=Path(args.input_dir)
    files=[folder/"nf482a-central.json",folder/"nf482a-primes.json"]
    files.extend(folder/f"nf482a-images-{m}-{m+2000}.json" for m in range(0,M,2000))
    records=[]
    for f in files:
        assert f.exists(),f"Missing source-native coefficient block {f}"
        records.append(json.loads(f.read_text()))
    assert [r["part"] for r in records]==["central","primes"]+["images"]*9
    assert all(r["original_nf407_source_sha256"]==SRC_SHA and r["original_nf406_seams_sha256"]==SEAM_SHA for r in records)
    assert all(r["original_273_groups"] and r["native_bits"]==PREC and r["polynomial_degree"]==N-1 for r in records)
    assert [(r["original_image_index_start"],r["original_image_index_stop"]) for r in records[2:]]==[(m,m+2000) for m in range(0,M,2000)]
    bounds=[bounds_fraction_intervals(r["coefficient_interval_balls"]) for r in records]
    assert all(len(a)==N for a in bounds)
    mids=[];rads=[]
    for j in range(N):
        lo=sum((bb[j][0] for bb in bounds),Q(0))
        hi=sum((bb[j][1] for bb in bounds),Q(0))
        assert lo<=hi
        mids.append((lo+hi)/2);rads.append((hi-lo)/2)
    eps_coeff=sum(rads,Q(0))
    # This is a constructive uniform error on the whole REAL panel,
    # not a pointwise derivative extrapolation.
    assert eps_coeff<Q(1,10**40),("source-coefficient interval contraction unresolved",str(float(eps_coeff)))
    # Fixed six-minus physical response analytically extended on |x-99/100|<=1/25, even beyond left *support switch*.
    # M_bound=10^350, physical source extension radius R=1/25, H/R=3/8.
    eps_taylor=Q(10)**350*Q(2,5)**N/(1-Q(2,5))
    assert eps_taylor<Q(1,10**120)
    # NF477 ORIGINAL |T_m| uniformly <8.655078527626e-16 all m>=18000.
    # At genuine first J8 x<=549/500 => d=B-x>=1/500.
    # Both original images: |F_m|<=e^(-2 m d), and 1-e^(-2d)>=d
    # on this genuine restricted source J8, NOT on all J8 through x=B.
    receipt477=json.loads(Path(args.nf477_tail_receipt).read_text())
    assert receipt477["pass"]=="NF477" and receipt477["source_sha256"]==SRC_SHA and receipt477["seam_sha256"]==SEAM_SHA
    assert receipt477["source_resolvent_M"]==M and receipt477["source_resolvent_N"]==360
    assert receipt477["independent_exact_fraction_ci"]["status"]=="SUCCESS"
    Cm=Q(receipt477["complete_original_source_Tm_all_m_ge_18000_strict_upper"])
    assert Cm<Q(9,10**15)
    eps_image=Cm*Q(3,8)**(M//250)/(2*Q(1,500))
    assert eps_image<Q(1,10**40)
    # Genuine original input uncertainty on physical J8:
    # original source dyadic S0<1e-700, original six prime weights total
    # uncertainty <1e-32, original |U|<900 and |v|<1.
    eps_input=Q(901,10**32)+Q(1,10**400)
    assert eps_coeff+eps_taylor+eps_image+eps_input<Q(1,10**28)
    eps_z=Q(1,10**28)
    # Entire original J8 first physical panel has genuine irrational LEFT
    # support at log9-B; the analytic fixed seven-minus source may extend
    # beyond support ONLY for computing local Taylor coefficients.
    ctx.prec=PREC
    xleft,xright,Lphys,tlo,thi,moments=original_J8_true_irrational_entry_moments()
    zball=[A(m) for m in mids]
    zmeanP=native_arb_mean(zball,moments)
    zcenterP=mids[0]
    tlo_lo,tlo_hi=enclosure(tlo,100)
    assert -Q(1)<tlo_lo<tlo_hi<Q(0)
    # Same-source exact original n9 added regular shift cancels its original
    # principal jump AT THE LEFT IRRATIONAL PHYSICAL SUPPORT SEAM.
    original,sh=read(args.source)
    src=U(original)
    n9_entry=src.at(C(-A(B))).real+src.at(C(A(B))).real
    e0,e1=enclosure(n9_entry,120)
    assert e0<=0<=e1 and max(abs(e0),abs(e1))<Q(1,10**70)
    assert XC-H<xleft<XC+H
    # Check J7 side at the original n9 boundary via an independent prior
    # physical certified original NF478-T right endpoint interval.
    previous=json.loads(Path(args.nf478t_receipt).read_text())
    assert previous["pass"]=="NF478-T"
    assert previous["original_nf407_source_sha256"]==SRC_SHA
    assert previous["original_nf406_seams_sha256"]==SEAM_SHA
    assert previous["genuine_original_J7_panel"]==["219/200","log9-B"]
    prevx0,prevx1=map(Q,previous["original_irrational_right_endpoint_log9_minus_B_outward"])
    xl0,xl1=enclosure(xleft,110)
    assert xl0<=prevx1 and prevx0<=xl1
    ctx.prec=PREC
    orig,sh=read(args.source);jet,js=read(args.jet)
    terms,pole,s0=native_source(orig)
    src=U(orig);v=src.at(C(A(B))).real
    weights=[]
    wdelta=Q(0)
    for item in jet["all_seven_original_prime_seam_derivative_identities"]:
        if item["prime_power"] in PRIMES:
            lo,hi=map(Q,item["c_n_positive_outward"])
            weights.append(A((lo+hi)/2));wdelta+=(hi-lo)/2
    assert len(weights)==7 and wdelta<Q(1,10**32)
    # Genuine original J8 p(t)=v[C8+0.5 log(1375/3)+0.5 sum_j (t/6)^j/j].
    KLOG=220
    pseries=[v*(sum(weights,arb(0))+(A(B)/A(B-XC)).log()/2)]
    for j in range(1,KLOG):
        pseries.append(v*A(Q(1,6)**j)/(2*j))
    plog_tail=Q(117,10**13)*Q(1,6)**KLOG/(2*KLOG*(1-Q(1,6)))
    assert plog_tail<Q(1,10**116)
    # ALL monomial moments are nonzero on this asymmetric physical
    # irrational interval. Their Arb enclosures are derived from exact
    # antiderivative values at log8-B and 1, not a finite quadrature mesh.
    mean_z2=arb(0)
    for i in range(N):
        one=arb(0)
        for j in range(N):
            one+=zball[j]*moments[i+j]
        mean_z2+=zball[i]*one
        if i%200==0:print("NF482-A original J8 n9 source irrational-entry z-square rows",i,"/1400",flush=True)
    mean_pz=arb(0)
    for i,za in enumerate(zball):
        one=arb(0)
        for j in range(KLOG):
            one+=pseries[j]*moments[i+j]
        mean_pz+=za*one
    mean_p=native_arb_mean(pseries,moments)
    mean_zP=zmeanP
    varP=mean_z2-mean_zP*mean_zP
    covP=mean_pz-mean_p*mean_zP
    if varP<0:
        assert varP> A(-Q(1,10**100))
    # Genuine original irrational physical L=1099/500-log9 (NOT a rational approximation).
    DI=Lphys*(4*mean_pz+2*mean_z2)
    # Uniform source error |z-P|<1e-28, true |z|<25000 (NF446).
    # |P|<25001. |p|<2e-10 on original first J8 strip, not at B;
    # from original NF411 weight errors and source S0.
    pmax=Q(2,10**10)
    # On this restricted TRUE J8 x<=549/500, d>=1/500, B/d<=550;
    # exp6>400 by its 16-term positive rational Taylor partial.
    assert sum((Q(7)**j/Q(math.factorial(j)) for j in range(15)),Q(0))>550
    assert Q(117,10**13)*(Q(7)+Q(7,2))<pmax
    err_p=Q(1,10**40)
    e_pz=pmax*eps_z+err_p*25001+plog_tail*25001
    e_z2=Q(50001)*eps_z
    momenterr=Q(1,1000)*(4*e_pz+2*e_z2) # original true J8 physical first strip length <1/1000
    assert momenterr<Q(1,10**23)
    dlo,dhi=enclosure(DI,90)
    dlo-=momenterr;dhi+=momenterr
    pz0,pz1=enclosure(mean_pz,90);pz0-=e_pz;pz1+=e_pz
    zz0,zz1=enclosure(mean_z2,90);zz0-=e_z2;zz1+=e_z2
    # Correlated source covariance and variance, keep their own explicit
    # original errors rather than infer signs from pointwise islands.
    cv0,cv1=enclosure(covP,90)
    vv0,vv1=enclosure(varP,90)
    errcov=e_pz+Q(1,10**23)
    errvar=e_z2+Q(1,10**23)
    cv0-=errcov;cv1+=errcov;vv0-=errvar;vv1+=errvar
    sign="NEGATIVE" if dhi<0 else "POSITIVE" if dlo>0 else "UNDECIDED"
    result={
     "pass":"NF482-A",
     "standing":"source-certified full original J7 macroscopic signed D_I if strict sign gate passes",
     "original_nf407_source_sha256":SRC_SHA,
     "original_nf406_seams_sha256":SEAM_SHA,
     "native_NF459_source_tree":SOURCE_TREE,
     "original_source_generators":246,"original_modes":273,
     "original_critical_sines":32,"original_sinh_pole":True,
     "native_precision_bits":PREC,
     "genuine_original_J8_panel":["log9-B","549/500"],
     "original_seven_regular_minus_prime_powers":list(PRIMES),
     "fixed_source_Chebyshev_or_Taylor_basis":"source-native shared coefficient x=686/625+(1/2500)t, degree 1199, physical t in [tlo,1]",
     "source_centered_Taylor_analytic_radius":"1/1000",
     "source_truncated_branch_Cauchy_M":"10^350",
     "certified_sup_z_minus_polynomial":"1/10^28",
     "original_source_arb_coefficient_aggregate_width":str(eps_coeff),
     "original_panel_type":"J8 first n9-active irrational left-seam panel, physical [log9-B,549/500]",
     "original_signed_integration_length":"1099/500-log9",
     "source_Cauchy_ratio":"2/5",
     "principal_log_ratio":"1/6", 
     "original_source_Taylor_remainder":str(eps_taylor),
     "original_joint_image_real_tail":str(eps_image),
     "original_source_weight_input_error_upper":str(eps_input),
     "original_true_mean_cross_check_NF471":False,
     "original_true_irrational_n9_entry_seam_zero_from_oddness":True,
     "original_irrational_left_endpoint_log9_minus_B_outward":list(map(str,enclosure(xleft,110))),
     "original_irrational_physical_length_outward":list(map(str,enclosure(Lphys,110))),
     "original_normalized_t_lower_outward":list(map(str,enclosure(tlo,110))),
     "original_normalized_t_upper":"1",
     "original_n9_entry_seam_vanishing_outward":[str(e0),str(e1)],
     "original_J7_J8_irrational_entry_seam_overlap":True,
     "original_z_mean_from_polynomial":list(map(str,[enclosure(zmeanP,90)[0]-eps_z,enclosure(zmeanP,90)[1]+eps_z])),
     "original_pz_normalized_mean_outward":[str(pz0),str(pz1)],
     "original_z2_normalized_mean_outward":[str(zz0),str(zz1)],
     "source_covariance_normalized_mean_outward":[str(cv0),str(cv1)],
     "source_variance_normalized_mean_outward":[str(vv0),str(vv1)],
     "source_original_D_I_outward":[str(dlo),str(dhi)],
     "source_original_D_I_strict_sign":sign,
     "NF404":"OPEN","W_ODD_NEG":"OPEN","RH":"OPEN",
     "whole_original_J8":"OPEN"
    }
    dest=Path(args.output);dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(result,indent=2)+"\n")
    print("NF482-A source ORIGINAL J8 mean z",float(zmeanP),flush=True)
    print("NF482-A source ORIGINAL J8 pz",float(pz0),float(pz1),flush=True)
    print("NF482-A source ORIGINAL J8 z²",float(zz0),float(zz1),flush=True)
    print("NF482-A source ORIGINAL signed J7 D_I",float(dlo),float(dhi),sign,flush=True)
    print("NF482-A original whole J8 and RH OPEN",flush=True)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--part",choices=["central","images","primes","assemble"],required=True)
    ap.add_argument("--start",type=int,default=0)
    ap.add_argument("--stop",type=int,default=0)
    ap.add_argument("--source",default="notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json")
    ap.add_argument("--seams",default="notes/data/provisional/NF406_original_prime_support_partition_exact.json")
    ap.add_argument("--jet",default="notes/data/provisional/NF411_original_source_boundary_jet.json")
    ap.add_argument("--input-dir",default="../results")
    ap.add_argument("--nf482a-boundary-receipt",default="../boundary/nf482a-original-J7-left-boundary-point.json")
    ap.add_argument("--nf471-receipt",default="../candidate/notes/data/provisional/NF471_original_J7_complete_macroscopic_mean_custody.json")
    ap.add_argument("--nf478t-receipt",default="../prior-original-J7/nf478t-original-J7-source-signed-moments.json")
    ap.add_argument("--nf477-tail-receipt",default="../candidate/notes/data/provisional/NF477_original_J7_correlated_resolvent_high_image_tail_custody.json")
    ap.add_argument("--output",required=True)
    args=ap.parse_args()
    if args.part=="assemble":assemble(args)
    else:save_part(args)
if __name__=="__main__":main()
