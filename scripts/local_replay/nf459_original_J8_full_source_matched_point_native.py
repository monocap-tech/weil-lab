#!/usr/bin/env python3
"""NF459 exact original whole-z finite-distance J8 points via physical matched source.

Original NF446 complete joint digamma+both images compact representation, not
separate enormous exterior images. Exact tK Taylor on real near-t=0 and
complete original physical 1600-Laplace moments for t>=1/20; 1150 source
B-jet accommodates entire NF406 J8 true x=B-d and original n9 prime support.

This is an actual finite-d source-correlated z(B-d), F, J and signed
4p*z+2z², not a whole-cell signed integration.
"""
import argparse,math,json,sys
from pathlib import Path
from fractions import Fraction as Q
from flint import arb,acb,ctx
from nf415_original_cell6_I1_validated_acb import native_source,U,A,C
from nf454_original_n9_contact_native_moment import read,enclosure,B,SRC_SHA,SEAM_SHA
from nf458_original_J8_matched_arch_finitepart_native import ujet_at_B,kbar_taylor,N,L,M,T0
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)

PRIMES=(2,3,4,5,7,8,9)
CENTER=Q(6677356497477490213,4611686018427387904)
PROBES=(Q(0),Q(1,1000000),Q(1,1000))
MH=40

def shift_taylor(c,x):
    """Exact Horner formal Taylor translation: q_j=[s^j] P(x+s)."""
    n=len(c)
    a=[arb(0) for _ in range(n)]
    a[0]=c[-1]
    deg=0
    for coeff in reversed(c[:-1]):
        for j in range(deg+1,0,-1):
            a[j]=a[j]*x+a[j-1]
        a[0]=a[0]*x+coeff
        deg+=1
    assert deg==n-1
    return a

def local_original_parts(shift,d,kbar):
    """I0 on [0,2d], I1 on [2d,t0], h on [2d,t0] exactly
       through analytic original source + tK polynomial moments."""
    nu=A(2*d/T0)
    assert 0<=2*d<T0
    Kscaled=[]
    tt=arb(1)
    for q in kbar:
        Kscaled.append(A(q)*tt)
        tt*=A(T0)
    ru=[arb(1)]
    for k in range(1,len(shift)):
        ru.append(ru[-1]*nu)
    H=arb(0)
    for j in range(1,L):
        H+=Kscaled[j]*(1-ru[j])/j
    I0=arb(0);I1tail=arb(0)
    powplus=arb(1);powminus=arb(1)
    factor=A(T0)/2
    for k in range(1,len(shift)):
        powplus*=factor
        powminus*=(-factor)
        acc0=arb(0);acc1=arb(0)
        for l,q in enumerate(Kscaled):
            denom=k+l
            acc0+=q*ru[denom]/denom if denom<len(ru) else q*nu**denom/denom
            acc1+=q*(1-(ru[denom] if denom<len(ru) else nu**denom))/denom
        if k%2==0:
            I0-=shift[k]*powplus*acc0
        I1tail-=shift[k]*powminus*acc1/2
    return I0,I1tail,H

def rate_int(lam,tlo,thi):
    if lam==0:return A(thi-tlo)
    l=A(lam)
    return ((-l*tlo).exp()-(-l*thi).exp())/l

def bulk_original_source(terms,pole,x,b):
    """Actual original source ∫[t0,b] K(t) U(x-t/2)dt,
       and ∫[t0,b] K(t)dt with original all modes."""
    grouped={}
    for f,k,c in terms:grouped.setdefault(f,[]).append((k,A(c)))
    assert sum(map(len,grouped.values()))==273
    ylo=x-A(T0)/2
    yhi=-A(B)
    a0=[arb(1)];a1=[arb(1)]
    for j in range(13):
        a0.append(a0[-1]*ylo)
        a1.append(a1[-1]*yhi)
    pi=arb.pi()
    phases={}
    for f in grouped:
        w=2*pi*A(f)
        phases[f]=(w,acb(arb(0),w*ylo).exp(),acb(arb(0),w*yhi).exp())
    total=arb(0);totalK=arb(0)
    short_total=None
    for m in range(M):
        lam=Q(4*m+1,4)
        l=A(lam)
        ea=(-l*A(T0)).exp()
        eb=(-l*b).exp()
        totalK+=(ea-eb)/l
        one=arb(0)
        for f,poly in grouped.items():
            w,phase0,phase1=phases[f]
            zz=acb(2*l,w)
            p0=acb(1)/zz;p1=p0
            maxk=max(k for k,c in poly)
            mm=[2*(ea*phase0*p0-eb*phase1*p1)]
            for k in range(1,maxk+1):
                p0=(a0[k]-k*p0)/zz
                p1=(a1[k]-k*p1)/zz
                mm.append(2*(ea*phase0*p0-eb*phase1*p1))
            for k,c in poly:
                one+=c*(mm[k].imag if k%2==0 else mm[k].real)
        one+=A(pole)/2*((x/2).exp()*rate_int(lam+Q(1,4),A(T0),b)
                       -(-x/2).exp()*rate_int(lam-Q(1,4),A(T0),b))
        total+=one
        if m+1==1200:short_total=enclosure(total,105)
        if (m+1)%400==0:print("NF459 original physical source Laplace",m+1,M,"d",float(A(B)-x),flush=True)
    assert short_total is not None
    # Fully original |U|<900 on physical interval, all coefficients correlated.
    tail=Q(900)*21*(Q(3,8)**int((Q(M)+Q(1,4))*T0))/(Q(M)+Q(1,4))
    shorttail=Q(900)*21*(Q(3,8)**int((Q(1200)+Q(1,4))*T0))/(Q(1200)+Q(1,4))
    assert tail<Q(1,10**29) and shorttail<Q(1,10**22)
    tl,th=enclosure(total,105)
    assert short_total[0]-shorttail<th+tail and short_total[1]+shorttail>tl-tail
    return total,totalK,tail,shorttail

def terminal_K(b):
    val=arb(0)
    for m in range(MH):
        lam=Q(4*m+1,4)
        val+=(-A(lam)*b).exp()/A(lam)
    tail=2*(Q(3,8)**int((Q(MH)+Q(1,4))*Q(4)))/(Q(MH)+Q(1,4))
    assert tail<Q(1,10**59)
    return val,tail

def finite_F(src,weights,v,x):
    result=arb(0)
    for n,w in weights.items():
        q=x-arb(n).log()
        a0,a1=enclosure(q,60)
        assert -B-Q(1,10**55)<a0<a1<B
        result-=w*(src.at(C(q)).real+v)
    result-=A(CENTER)*(x/2).sinh()
    return result

def point(src,terms,pole,ujet,kbar,weights,v,c0,d,s0,wdelta):
    x=A(B-d)
    b=2*(A(B)+x)
    a=2*d
    xcoeff=ujet if d==0 else shift_taylor(ujet,-A(d))
    ux=xcoeff[0]
    utrue=src.at(C(x)).real
    dif0,dif1=enclosure(ux-utrue,110)
    assert -Q(1,10**110)<dif0<dif1<Q(1,10**110)
    I0,I1tail,hsmall=local_original_parts(xcoeff,d,kbar)
    uBulk,Kbulk,bulkTail,shortTail=bulk_original_source(terms,pole,x,b)
    htail,htailErr=terminal_K(b)
    # NF446 exact true compact arch after principal log subtraction,
    # with both original images jointly included and source physically
    # supported. The algebra cancels v*Kbulk and hsmall v exactly.
    # For d=0 only, the (ux-v)/2 log(T0/(2d)) limiting term is ZERO.
    Lterm=arb(0) if d==0 else (ux-v)/2*(A(T0)/A(a)).log()
    J=c0*ux+I0+I1tail+Lterm+ux*hsmall/2
    J+=ux*Kbulk-uBulk/2+A(v)/2*(A(T0)/(2*A(B))).log()+ux*htail
    F=finite_F(src,weights,v,x)
    z=J+F
    # Entire original physical source/input charges:
    # M=10^800 R=1/5, q<=3/20, N=1150 => <1e-146;
    # 80-term kbar error <1e-100 on |t|<=1/20;
    # uncomputed exact m>=1600 physical kernel <1e-29;
    # accepted original dyadic error S0<1e-700; prime
    # source weights are separately charged by 901*wdelta.
    # Full error <1e-27 + 901*wdelta + 1e8*S0.
    assert Q(10)**800*(Q(3,20)**N)/(1-Q(3,20))<Q(1,10**146)
    assert 8*T0**L/(1-T0)<Q(1,10**100)
    assert bulkTail<Q(1,10**29) and htailErr<Q(1,10**59)
    error=Q(1,10**27)+901*wdelta+Q(10)**8*s0
    assert error<Q(1,10**26)
    z0,z1=enclosure(z,100)
    z0-=error;z1+=error
    J0,J1=enclosure(J,100)
    J0-=error;J1+=error
    F0,F1=enclosure(F,100)
    F0-=error;F1+=error
    print("NF459 ORIGINAL full z(B-d) d",str(d),"approx",float(z0),float(z1),flush=True)
    return (z0,z1),(J0,J1),(F0,F1),bulkTail

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--source",default="notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json")
    ap.add_argument("--seams",default="notes/data/provisional/NF406_original_prime_support_partition_exact.json")
    ap.add_argument("--jet",default="notes/data/provisional/NF411_original_source_boundary_jet.json")
    ap.add_argument("--nf446",default="notes/data/provisional/NF446_original_joint_compact_kernel_J7_J8_custody_index.json")
    ap.add_argument("--nf450",default="notes/data/provisional/NF450_original_B_complete_Laplace_native_sign_custody_index.json")
    ap.add_argument("--nf456",default="notes/data/provisional/NF456_original_J8_complete_finite_seven_prime_gram_and_archB_custody.json")
    ap.add_argument("--nf457",default="notes/data/provisional/NF457_original_full_J8_matched_compact_and_extended_signed_collar_custody.json")
    ap.add_argument("--nf458",default="notes/data/provisional/NF458_original_J8_matched_joint_arch_finitepart_source_custody.json")
    ap.add_argument("--precision",type=int,default=4096)
    ap.add_argument("--output",required=True)
    args=ap.parse_args()
    ctx.prec=args.precision
    assert ctx.prec>=3072
    s,sh=read(args.source);seams,gs=read(args.seams);jet,js=read(args.jet)
    nf446,h446=read(args.nf446);nf450,h450=read(args.nf450)
    nf456,h456=read(args.nf456);nf457,h457=read(args.nf457);nf458,h458=read(args.nf458)
    assert (sh,gs)==(SRC_SHA,SEAM_SHA)
    assert nf446["original_nf407_source_sha256"]==sh and nf446["original_nf406_prime_seam_sha256"]==gs
    assert nf450["source_SHA256"]==nf456["source_sha256"]==nf458["source_sha256"]==sh
    assert nf457["original_source_sha256"]==sh
    assert s["original_dimension"]==242
    assert len(s["original_exact_native_original_four_critical_coefficients_mid_radius"])==4
    assert len(s["original_source_critical_sine_frequencies"])==32
    assert nf450["original_CI_result"]=="SUCCESS" and nf458["expanded_strict_status"]=="SUCCESS"
    assert nf458["whole_J8_signed"]=="OPEN" and nf457["original_complete_signed_J8"]=="OPEN"
    assert nf456["original_nf404_center_exact"]==str(CENTER)
    seam9=next(x for x in seams["original_prime_power_log_shifts"] if x["n"]==9)
    physical_min=2*B-Q(seam9["log_upper"])
    assert max(PROBES)<physical_min<Q(3,1000)
    coeff,pole,s0=native_source(s)
    assert len(coeff)==273 and s0<Q(1,10**700)
    raw=sum((abs(c)*B**k for f,k,c in coeff),abs(pole))
    assert raw<Q(10)**160 and all(0<f<883 and k<=13 for f,k,c in coeff)
    pi=arb.pi()
    c0=A(Q(1,4)).digamma()-pi.log()
    src=U(s)
    v=src.at(C(B)).real
    vv0,vv1=enclosure(v,110)
    assert -Q(117,10**13)<vv0<vv1<-Q(116,10**13)
    weights={}
    sumdelta=Q(0)
    for x in jet["all_seven_original_prime_seam_derivative_identities"]:
        n=x["prime_power"];lo,hi=map(Q,x["c_n_positive_outward"])
        weights[n]=A((lo+hi)/2)
        sumdelta+=(hi-lo)/2
    assert tuple(sorted(weights))==PRIMES and sumdelta<Q(1,10**32)
    ep=tuple(map(Q,nf450["complete_z_B_outward_24_decimal"]))
    assert ep[1]<0
    logC=sum(weights.values(),arb(0))
    jets,distinct=ujet_at_B(coeff,pole)
    assert distinct==99
    kb=kbar_taylor()
    output={}
    for d in PROBES:
        zv,Jv,Fv,tail=point(src,coeff,pole,jets,kb,weights,v,c0,d,s0,sumdelta)
        if d==0:
            assert zv[0]<ep[1] and ep[0]<zv[1], "Independent NF450 complete original physical endpoint mismatch"
            assert Q(nf456["original_finite_F_at_B_strict"][0])<Fv[0]<Fv[1]<Q(nf456["original_finite_F_at_B_strict"][1])
            print("NF459 independent exact source NF446 endpoint and accepted NF450 Z overlap",flush=True)
        else:
            # Actual entire original signed integrand including singular
            # prime principal at THIS finite d, not a signed integral.
            p=v*(A(B)/A(d)).log()/2+v*logC
            zmid=A((zv[0]+zv[1])/2)
            vtime=4*p*zmid+2*zmid*zmid
            t0,t1=enclosure(vtime,85)
            # principal interval source/weight uncertainty overcharge.
            err=Q(1,10**26)
            t0-=err;t1+=err
            xlog=(A(2*B-d)/A(d)).log()
            zanchor=(A(ep[0])+A(ep[1]))/2
            k=A(Q(6504856890269607,10**23))
            cr=A(Q(-6494948795121242,10**23))
            remainder=zmid-zanchor-k*A(d)*xlog-cr*A(d)
            r0,r1=enclosure(remainder,90)
            rerr=(ep[1]-ep[0])/2 +d*Q(20,10**14)+Q(1,10**26)
            r0-=rerr;r1+=rerr
            output[str(d)]={
                "original_z_J8_true_full_outward":[str(zv[0]),str(zv[1])],
                "original_joint_arch_J_outward":[str(Jv[0]),str(Jv[1])],
                "original_finite_F_outward":[str(Fv[0]),str(Fv[1])],
                "original_pointwise_4pz_plus_2z2_outward":[str(t0),str(t1)],
                "original_matched_finite_d_remainder_after_NF458_first_order_outward":[str(r0),str(r1)],
                "original_point_z_sign":"POSITIVE" if zv[0]>0 else "NEGATIVE" if zv[1]<0 else "UNRESOLVED",
                "original_point_signed_integrand_sign":"POSITIVE" if t0>0 else "NEGATIVE" if t1<0 else "UNRESOLVED",
                "original_source_geometric_tail":str(tail)
            }
            print("NF459 full ORIGINAL signed integrand d",str(d),float(t0),float(t1),flush=True)
            print("NF459 actual source-correlated nonlinear finite-d remainder",str(d),float(r0),float(r1),flush=True)
    result={
       "pass":"NF459","standing":"source-certified true original entire physical z evaluated at two nonzero J8 points and independent NF450 endpoint, original true pointwise signed integrand and actual finite-d matched nonlinear remainder; complete signed J8 OPEN",
       "original_source_sha256":sh,"original_seams_sha256":gs,
       "nf446_sha256":h446,"nf450_sha256":h450,"nf456_sha256":h456,"nf457_sha256":h457,"nf458_sha256":h458,"original_nf411_sha256":js,
       "original_246_generators":True,"original_groups":273,"source_distinct_frequencies":99,
       "critical_original_sines":32,"original_sinh":True,
       "native_bits":ctx.prec,
       "original_true_physical_point_distances":[str(x) for x in PROBES],
       "source_analytic_Bjet_N":N,"original_tK_taylor_orders":L,"original_bulk_laplace_modes":M,
       "original_local_panel":"[0,1/20]","original_bulk_physical_panel":"[1/20, 4B-2d]",
       "original_source_cauchy_M":"10^800","original_source_cauchy_R":"1/5","source_ratio_lt":"3/20",
       "original_true_endpoint_independent_NF450_overlap":True,
       "original_true_B_endpoint_exact_outward":[str(x) for x in ep],
       "points":output,
       "true_original_complete_signed_J8_integral":"OPEN","true_original_complete_signed_J7_integral":"OPEN",
       "global_NF410_NF404":"OPEN","W_ODD_NEG":"OPEN","RH":"OPEN",
       "next":"NF460 certify original source-point same-sign finite islands and correlation-preserving high-order whole J8 moments/intervals; no entire signed D8 from point samples"
    }
    path=Path(args.output);path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(result,indent=2)+"\n")
    print("NF459 full original J8 source point / matched remainder checks PASSED, complete J8 signed OPEN",flush=True)
if __name__=="__main__":main()
