#!/usr/bin/env python3
"""NF458 genuine original J8 matched-joint-arch FINITE endpoint slope.

Evaluate the actual original source-correlated limit
  ell = lim_(d->0+) R_joint(d)/d
under the exact NF457 whole-J8 matched compact physical identity. Retain
full original U / U' 246 dyadic generators (273 consolidated modes),
odd sinh, 32 critical sines, true NF404 centered seven-prime F'.

The only delicate new real source integral is
  I = ∫_0^(4B) K(t)[U'(B-t/2)-U'(B)]dt
   with K(t)=exp(-t/4)/(1-exp(-t)).
Compute I via source-correlated 1150-jet at genuine B on [0,1/20],
and exact original polynomial-frequency Laplace moments on [1/20,4B],
with 1600 geometric K terms and RATIONAL tail from original U'<400.
All analytic and coefficient uncertainties explicitly paid; no quadrature.
Not a full J8 signed integral: further actual R_joint(d) curvature open.
"""
import argparse,json,math,sys
from fractions import Fraction as Q
from pathlib import Path
from flint import arb,acb,ctx
from nf415_original_cell6_I1_validated_acb import native_source,U,A,C
from nf454_original_n9_contact_native_moment import read,enclosure,B,SRC_SHA,SEAM_SHA
from nf457_original_J8_endpoint_matched_compact_remainder_native import source_first_derivative

if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
T=4*B
T0=Q(1,20)
N=1150
L=80
M=1600
MH=40
CENTER=Q(6677356497477490213,4611686018427387904)
PRIMES=(2,3,4,5,7,8,9)

def ujet_at_B(terms,pole):
    """Authentic complete original U(B+s) = sum_j coeff_j s^j in Arb."""
    pic=arb.pi()
    y0=A(B)
    yp=[arb(1)]
    for k in range(13):yp.append(yp[-1]*y0)
    grouped={}
    for f,k,q in terms:grouped.setdefault(f,[]).append((k,q))
    assert sum(map(len,grouped.values()))==273
    total=[arb(0) for _ in range(N)]
    for count,(f,poly) in enumerate(grouped.items(),1):
        iw=acb(arb(0),2*pic*A(f))
        phase=(iw*y0).exp()
        e=[acb(1)]
        for j in range(1,N):e.append(e[-1]*iw/j)
        even=[arb(0) for _ in range(14)]
        odd=[arb(0) for _ in range(14)]
        for k,q in poly:
            dest=even if k%2==0 else odd
            for i in range(k+1):
                dest[i]+=A(q)*math.comb(k,i)*yp[k-i]
        maxk=max(k for k,q in poly)
        for j in range(N):
            ev=acb(0);od=acb(0)
            for i in range(min(maxk,j)+1):
                if even[i]:ev+=even[i]*e[j-i]
                if odd[i]:od+=odd[i]*e[j-i]
            total[j]+=(phase*ev).imag+(phase*od).real
        if count%30==0 or count==len(grouped):
            print("NF458 original B source jet frequencies",count,len(grouped),flush=True)
    sp=(y0/2).sinh();cp=(y0/2).cosh()
    coef=arb(1)
    for j in range(N):
        if j:coef/=2*j
        total[j]+=A(pole)*(sp if j%2==0 else cp)*coef
    return total,len(grouped)

def kbar_taylor():
    """Exact Taylor coefficients q_j of tK(t)=exp(-t/4)*t/(1-e^-t)."""
    d=[];e=[]
    for j in range(L):
        d.append((-1)**j*Q(1,math.factorial(j+1)))
        e.append((-1)**j*Q(1,4**j*math.factorial(j)))
    q=[]
    for n in range(L):
        q.append(e[n]-sum((d[k]*q[n-k] for k in range(1,n+1)),Q(0)))
    assert q[0]==1 and q[1]==Q(1,4)
    return q

def local_signed_integrals(ujet,kbar):
    # Original U'(B-t/2)-U'(B), scaled by the true local t0:
    # A_j=(j+1)c_(j+1)*(-1/2)^j, j>=1; j=0 cancels exactly.
    source_scaled=[]
    powj=-A(T0)/2
    for j in range(1,N-1):
        source_scaled.append((j+1)*ujet[j+1]*powj)
        powj*=(-A(T0)/2)
    ker_scaled=[]
    powj=arb(1)
    for q in kbar:
        ker_scaled.append(A(q)*powj)
        powj*=A(T0)
    value=arb(0)
    for j,src in enumerate(source_scaled,1):
        acc=arb(0)
        for k,b in enumerate(ker_scaled):
            acc+=b/(j+k)
        value+=src*acc
    # ∫_0^t0 (K-1/t) = ∑_{j>=1} q_j t0^j/j
    ih=arb(0)
    for j in range(1,L):
        ih+=ker_scaled[j]/j
    assert value.is_finite() and ih.is_finite()
    return value,ih

def exact_rate_interval(lam):
    """Arb primitive ∫_(t0)^T e^-lam*t dt; lim lam→0 respected."""
    if lam==0:return A(T-T0)
    lam=A(lam)
    return ((-lam*A(T0)).exp()-(-lam*A(T)).exp())/lam

def bulk_full_native(terms,pole,ubprime):
    grouped={}
    for f,k,c in terms:grouped.setdefault(f,[]).append((k,A(c)))
    assert sum(map(len,grouped.values()))==273
    pic=arb.pi()
    yt=A(B-T0/2);yr=-A(B)
    pow0=[arb(1)];pow1=[arb(1)]
    for _ in range(13):
        pow0.append(pow0[-1]*yt);pow1.append(pow1[-1]*yr)
    freq={}
    for f,poly in grouped.items():
        w=2*pic*A(f)
        freq[f]=(w,acb(arb(0),w*yt).exp(),acb(arb(0),w*yr).exp())
    intD=arb(0)
    intK=arb(0)
    for m in range(M):
        lam=Q(4*m+1,4)
        la=A(lam)
        left=(-la*A(T0)).exp()
        right=(-la*A(T)).exp()
        qK=(left-right)/la
        uder=arb(0)
        for f,poly in grouped.items():
            om,phase0,phase1=freq[f]
            zz=acb(2*la,om)
            p0=acb(1)/zz;p1=p0
            maxk=max(k for k,c in poly)
            moms=[2*(left*phase0*p0-right*phase1*p1)]
            for k in range(1,maxk+1):
                p0=(pow0[k]-k*p0)/zz
                p1=(pow1[k]-k*p1)/zz
                moms.append(2*(left*phase0*p0-right*phase1*p1))
            for k,coeff in poly:
                deriv=(k*moms[k-1] if k else acb(0))+acb(arb(0),om)*moms[k]
                uder+=coeff*(deriv.imag if k%2==0 else deriv.real)
        # Pole derivative c_pole/2*cosh(y/2) =c_pole/4*(exp(y/2)+exp(-y/2)).
        poleint=A(pole)/4*(
             (A(B)/2).exp()*exact_rate_interval(lam+Q(1,4))+
             (-A(B)/2).exp()*exact_rate_interval(lam-Q(1,4)))
        uder+=poleint
        intD+=uder-ubprime*qK
        intK+=qK
        if (m+1)%200==0:
            print("NF458 original complete physical Laplace derivative terms",m+1,M,flush=True)
    tail=Q(800)*21*(Q(3,8)**int((Q(M)+Q(1,4))*T0))/(Q(M)+Q(1,4))
    assert tail<Q(1,10**29)
    return intD,intK,tail,len(grouped)

def H_terminal():
    h=arb(0)
    for m in range(MH):
        lam=Q(4*m+1,4)
        h+=(-A(lam)*A(T)).exp()/A(lam)
    tail=2*(Q(3,8)**int((Q(MH)+Q(1,4))*T))/(Q(MH)+Q(1,4))
    assert tail<Q(1,10**60)
    return h,tail

def source_fprime(terms,pole,jet):
    out=-A(CENTER)*(A(B)/2).cosh()/2
    weights={}
    for x in jet["all_seven_original_prime_seam_derivative_identities"]:
        n=x["prime_power"]
        weights[n]=tuple(map(Q,x["c_n_positive_outward"]))
    assert tuple(sorted(weights))==PRIMES
    s0=Q(0)
    for n,(lo,hi) in weights.items():
        s=A(B)-arb(n).log()
        out-=A((lo+hi)/2)*source_first_derivative(terms,pole,s)
        s0+=(hi-lo)/2
    assert s0<Q(1,10**32)
    return out,400*s0+10**8*Q(1,10**700)

def run(args):
    ctx.prec=args.precision
    assert ctx.prec>=3072
    src,sh=read(args.source)
    seams,ks=read(args.seams)
    jet,jsha=read(args.jet)
    nf413,h413=read(args.nf413)
    nf446,h446=read(args.nf446)
    nf450,h450=read(args.nf450)
    nf456,h456=read(args.nf456)
    nf457,h457=read(args.nf457)
    assert (sh,ks)==(SRC_SHA,SEAM_SHA)
    assert src["original_dimension"]==242 and len(src["original_exact_native_original_four_critical_coefficients_mid_radius"])==4
    assert len(src["original_source_critical_sine_frequencies"])==32
    assert nf413["original_nf407_full_native_source_sha256"]==sh
    assert nf413["original_true_full_u4_second_derivative_L2_upper_integer"]=="256"
    assert nf446["original_nf407_source_sha256"]==sh and nf446["original_nf406_prime_seam_sha256"]==ks
    assert nf450["source_SHA256"]==sh and nf450["seams_SHA256"]==ks
    assert nf456["source_sha256"]==sh and nf456["seams_sha256"]==ks
    assert nf457["source_sha256"]==sh and nf457["seams_sha256"]==ks
    assert nf457["original_matched_remainder_full_J8_strict"]=="|R_J(d)|<8200*d"
    assert nf457["original_unconditional_full_J8_complete_z_modulus"]=="|z(B-d)-Z|<d*(9802+200*log((2B-d)/d))"
    assert nf456["original_nf404_center_exact"]==str(CENTER)
    assert nf457["whole_original_J8_signed"]=="OPEN"
    assert nf450["original_CI_result"]=="SUCCESS"
    terms,pole,s0=native_source(src)
    assert len(terms)==273 and s0<Q(1,10**700)
    raw=sum((abs(q)*B**k for f,k,q in terms),abs(pole))
    assert raw<Q(10)**160 and all(0<f<883 and 0<=k<=13 for f,k,q in terms)
    # Complete Cauchy on |s|=1/5 around B:
    # |B+s|<13/10, (13/11)^13<10, |2pi*f*s|<1111;
    # e^1111<3^1111<10^531, original raw<10^160.
    assert Q(13,11)**13<10 and 3**1111<10**531
    assert Q(44*883,35)<1111
    R=Q(1,5);ratio=T0/(2*R)
    assert ratio==Q(1,8)
    M_U=Q(10)**800
    # For U'(B-t/2): tail of source Taylor derivative n>=N.
    # Uniform < (M_U/R)*q^(N-1)*(N/(1-q)+q/(1-q)^2).
    e_u=(M_U/R)*ratio**(N-1)*(Q(N)/(1-ratio)+ratio/(1-ratio)**2)
    assert e_u<Q(1,10**225)
    k_err=Q(8)*T0**L/(1-T0)
    assert k_err<Q(1,10**100)
    # Actual physical |U'(B-t/2)-U'(B)| <= 256 sqrt(t/2).
    # ∫_0^t0 |D|/t < 256*(3/4)*2*(1/4)=96.
    local_err=Q(100)*k_err+Q(100)*e_u
    assert local_err<Q(1,10**96)

    jets,nfreq=ujet_at_B(terms,pole)
    ubprime=source_first_derivative(terms,pole,A(B))
    aa,bb=enclosure(jets[1]-ubprime,100)
    assert aa<0<bb
    original_ub=tuple(map(Q,nf457["original_native_Uprime_B_outward"]))
    uplo,uphi=enclosure(ubprime,105)
    deriv_radius=10000*s0
    uplo-=deriv_radius;uphi+=deriv_radius
    assert original_ub[0]<uplo<uphi<original_ub[1]
    original_v=tuple(map(Q,nf457["original_U_B_source_outward"]))
    v=jets[0]
    v0,v1=enclosure(v,105)
    assert original_v[0]<v0<v1<original_v[1]

    kbar=kbar_taylor()
    inner_small,hsmall=local_signed_integrals(jets,kbar)
    inner_big,bigK,lap_tail,nfreq2=bulk_full_native(terms,pole,ubprime)
    assert nfreq==nfreq2==99
    # Original source coefficient discrepancy in U' derivative differences:
    # |δU''|<4e7*S0 on physical [-B,B], |δU'(B-t/2)-δU'(B)|
    # <2e7*S0*t, tK(t)<1+t<6 and T=4.4:
    # <2e7*6*4.4*S0 < 1e9*S0.
    radius=Q(10)**9*s0
    assert radius<Q(1,10**690)
    I=inner_small+inner_big
    Ierr=lap_tail+local_err+radius

    # ∫_0^T h(t)dt =∫_0^t0 h(t)dt +
    # ∑_(m≥0)∫_t0^T e^-(m+1/4)t dt - log(T/t0).
    Jh=hsmall+bigK-(A(T)/A(T0)).log()
    JhErr=lap_tail+Q(8)*T0**L/(L*(1-T0))
    assert JhErr<Q(1,10**29)
    h0=A(Q(1,4))
    KT=(-A(T)/4).exp()/(1-(-A(T)).exp())
    hT=KT-1/A(T)
    H,HTail=H_terminal()
    c0=(A(Q(1,4))).digamma()-arb.pi().log()

    Fp,FpErr=source_fprime(terms,pole,jet)
    f0,f1=enclosure(Fp,105)
    f0-=FpErr;f1+=FpErr
    assert -Q(1980840,10**6)<f0<f1<-Q(1980838,10**6)
    # Source-exact endpoint-matched R_J(d)/d finite part, derived by
    # differentiating the ALREADY accepted NF457 original compact-source
    # identity *after* singular source matching, not separate images.
    finite=-c0*ubprime+I/2-ubprime*Jh/2-ubprime/2
    finite+=v/2*(-1/(2*A(B))-2*h0-2*hT)-ubprime*H
    err=(Ierr/2+Q(2)*JhErr+HTail+Q(100)*radius+
         Q(100000)*s0)
    assert err<Q(1,10**26)
    r0,r1=enclosure(finite,100)
    r0-=err;r1+=err
    assert r0<r1 and -8200<r0<r1<8200
    full=finite-Fp
    cmin,cmax=enclosure(full,100)
    cmin-=err+FpErr;cmax+=err+FpErr
    assert cmin<cmax and -8202<cmin<cmax<8202

    print("NF458 original true matched derivative source integral I",float(I),flush=True)
    print("NF458 original true compact regular log-kernel ∫h",float(Jh),flush=True)
    print("NF458 original original R_joint'(B-distance 0+) finite part",float(r0),float(r1),flush=True)
    print("NF458 original full z endpoint regular first-order coefficient",float(cmin),float(cmax),flush=True)
    print("NF458 source-wide independent original Fprime",float(f0),float(f1),flush=True)
    return {
      "pass":"NF458",
      "standing":"source-certified original full J8 matched joint arch finite endpoint slope Rjoint_prime(0+) and complete-original regular z first-order coefficient, NOT whole signed J8",
      "original_source_sha256":sh,"original_seams_sha256":ks,
      "original_nf413_sha256":h413,"original_nf446_sha256":h446,
      "original_nf450_sha256":h450,"original_nf456_sha256":h456,
      "original_nf457_sha256":h457,"original_nf411_sha256":jsha,
      "original_source_generators":246,"original_grouped_frequency_order":273,
      "source_unique_frequencies":99,"original_critical_sine_modes":32,
      "original_odd_sinh_pole":True,"native_bits":ctx.prec,
      "original_physical_support":"[-B,B] only", "original_B":"11/10",
      "analytic_local_t0":"1/20","native_source_jet_N":N,
      "Kbar_taylor_order":L,"geometric_K_bulk_M":M,
      "geometric_H_terminal_M":MH,
      "source_Cauchy_M":"10^800", "source_Cauchy_radius":"1/5",
      "original_true_ratio":"1/8", "original_source_tail_derivative_bound":str(e_u),
      "original_exact_kernel_Taylor_error":str(k_err),
      "original_source_local_integral_error":str(local_err),
      "original_Laplace_bulk_geometric_tail":str(lap_tail),
      "original_dyadic_source_radius_integral":str(radius),
      "original_true_joint_derivative_difference_integral_I":[str(z) for z in (enclosure(I,105)[0]-Ierr,enclosure(I,105)[1]+Ierr)],
      "original_compact_h_integral":[str(z) for z in (enclosure(Jh,105)[0]-JhErr,enclosure(Jh,105)[1]+JhErr)],
      "original_native_Uprime_B":[str(uplo),str(uphi)],
      "original_native_Fprime_B":[str(f0),str(f1)],
      "original_Rjoint_endpoint_finite_part_slope":[str(r0),str(r1)],
      "original_complete_z_endpoint_regular_first_order_coefficient":[str(cmin),str(cmax)],
      "original_exact_matched_Rjoint_finitepart_identity":"-c0*u + 1/2 integral_0^4B K(t)(Uprime(B-t/2)-u)dt -u/2 int_0^4B (K(t)-1/t)dt -u/2 +v/2*(-1/(2B)-2*(K-1/t)(0)-2*(K-1/t)(4B))-u*H(4B)",
      "original_full_z_local_expansion":"z(B-d)-Z=-(u/2)d*log((2B-d)/d)+(Rjoint_finite_part-Fprime(B))*d+o(d)",
      "old_original_full_J8_modulus_remains":"|z(B-d)-Z|<d*(9802+200log((2B-d)/d))",
      "new_full_J8_signed_decision":"OPEN",
      "whole_original_J7":"OPEN", "NF410_NF404":"OPEN", "W_ODD_NEG":"OPEN","RH":"OPEN",
      "next":"NF459 bound finitepart variation uniformly and evaluate actual Rjoint(d) across full J8, original signed pz and z² cell"
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--source",default="notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json")
    ap.add_argument("--seams",default="notes/data/provisional/NF406_original_prime_support_partition_exact.json")
    ap.add_argument("--jet",default="notes/data/provisional/NF411_original_source_boundary_jet.json")
    ap.add_argument("--nf413",default="notes/data/provisional/NF413_original_full_246_source_curvature_native.json")
    ap.add_argument("--nf446",default="notes/data/provisional/NF446_original_joint_compact_kernel_J7_J8_custody_index.json")
    ap.add_argument("--nf450",default="notes/data/provisional/NF450_original_B_complete_Laplace_native_sign_custody_index.json")
    ap.add_argument("--nf456",default="notes/data/provisional/NF456_original_J8_complete_finite_seven_prime_gram_and_archB_custody.json")
    ap.add_argument("--nf457",default="notes/data/provisional/NF457_original_full_J8_matched_compact_and_extended_signed_collar_custody.json")
    ap.add_argument("--precision",type=int,default=4096)
    ap.add_argument("--output",required=True)
    args=ap.parse_args()
    data=run(args)
    out=Path(args.output);out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(data,indent=2)+"\n")
    print("NF458 SOURCE-NATIVE true full original endpoint finitepart computed, complete signed J8/J7 RH OPEN",flush=True)
if __name__=="__main__":main()
