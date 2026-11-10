#!/usr/bin/env python3
"""NF494 original full NF446 physically joined analytic H(d) 400 Taylor jets.

The genuine original NF492 ALL-ORDERS decomposition
 z(B-d)=H(d)+(U(B-d)-v)/2*log(B/d)
and the original full NF491 w=p+z=H(d)+vC8+U(B-d)/2*log(B/d)
are evaluated with original NF407 246 generators/273 groups and NF406
seven real primes, the original odd sinh, both joint kernel images, and
the true NF404 center. No NF484 image-only square.

Key fixed-window cancellation:
 H(d)=C*U(B-d)+F(d)+L(d)+Rplus(d)
      +U(B-d)/2*(log(1-d/(2B))-Qsmall(d)-Qtail(d))
      -P7(B-d)-CENTER*sinh((B-d)/2).
 F(d)=1/2 int_0^(4B) K(t)(U(B-d)-U(B-d-t/2))dt
 is EXACTLY a finite frequency/order source multiplier, evaluated
 using 14 digamma/polygamma moments per original frequency and
 exponentially decaying complete physical finite-window corrections.
 The analytic continuation of U beyond [-B,B] in F(d) is only an
 algebraic temporary and cancels with Rplus; on real original J8,
 every source argument in the JOINT original formula is physical.

L and Rplus have closed original source-dependent rational beta/harmonic
recurrences. All 400 original H and U coefficients are source-contracted
at 4096-bit Arb BEFORE interval projection. They are checked at d=0
against genuine original NF450 and at d=1/500 against NF492 true H.

This script generates the source numerical balls, not yet the complete
independently audited scalar Ew_T; that is a distinct job.
"""
from __future__ import annotations
import argparse, hashlib, json, math, sys
from fractions import Fraction as F
from pathlib import Path
from flint import arb,acb,ctx
from nf415_original_cell6_I1_validated_acb import native_source,U
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
B=F(11,10)
T=4*B
DELTA=F(1,500)
R=F(1,25)
N=400
M=1000
PREC=4096
SRC="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAM="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
CENTER=F(6677356497477490213,4611686018427387904)
POWERS={2:2,3:3,4:2,5:5,7:7,8:2,9:3}
SOURCE_FEE=F(1,10**300)

def A(x):
    if isinstance(x,arb):return x
    if isinstance(x,F):return arb(x.numerator)/arb(x.denominator)
    return arb(x)
def C(x):return acb(A(x))
def enc(v,digits=230):
    m,r,e=v.mid_rad_10exp(digits)
    fac=F(10)**int(e)
    return F(int(m)-int(r))*fac,F(int(m)+int(r))*fac
def overlap(a,b):return a[0]<=b[1] and b[0]<=a[1]
def poly_value(coeff,x):
    acc=arb(0);power=arb(1);X=A(x)
    for c in coeff:
        acc+=c*power
        power*=X
    return acc
def read(p):
    b=Path(p).read_bytes()
    return json.loads(b),hashlib.sha256(b).hexdigest()

def original_source_jet(terms,pole,y):
    """TRUE complete 273-mode U(y-d) 400 jets with unchanged odd sinh."""
    Y=A(y)
    pi=arb.pi()
    out=[arb(0) for _ in range(N)]
    for f,k,coeff in terms:
        w=2*pi*A(f)
        iw=acb(arb(0),w)
        alpha=acb(arb(0),-A(coeff)/2) if k%2==0 else acb(A(coeff)/2)
        phase=alpha*(iw*Y).exp()
        em=[acb(1)]
        z=-iw
        for n in range(1,N):em.append(em[-1]*z/n)
        poly=[A(math.comb(k,j))*(Y**(k-j))*((-1)**j)
              for j in range(k+1)]
        for n in range(N):
            val=acb(0)
            for j in range(min(n,k)+1):val+=poly[j]*em[n-j]
            out[n]+=2*(phase*val).real
    pp=A(pole)
    ss=(Y/2).sinh();cc=(Y/2).cosh()
    fact=1
    for n in range(N):
        if n:fact*=n
        out[n]+=pp*((-A(F(1,2)))**n)*(ss if n%2==0 else cc)/fact
    return out

def kernel_coefficients():
    """L=tK at t=0 and K(T-u) about u=0, all 400 joint source coeffs."""
    print("NF494 4096bit original joint kernel L=tK Taylor started",flush=True)
    l=[arb(0) for _ in range(N)]
    e=[arb(0) for _ in range(N)]
    fac=1
    for n in range(N):
        if n:fac*=n
        e[n]=(-A(F(1,4)))**n/fac
    l[0]=arb(1)
    facts=[math.factorial(j+1) for j in range(N)]
    for n in range(1,N):
        val=e[n]
        for j in range(1,n+1):
            val-=A(F((-1)**j,facts[j]))*l[n-j]
        l[n]=val
    assert l[0].contains(1)
    assert l[1].contains(A(F(1,4)))
    print("NF494 exact original kernel t=4B derivative coefficients started",flush=True)
    kap=[arb(0) for _ in range(N)]
    tailT=arb(0)
    xT=A(T)
    for m in range(M):
        rate=A(F(4*m+1,4))
        em=(-rate*xT).exp()
        tailT+=em/rate
        term=em
        for k in range(N):
            kap[k]+=term
            term=term*rate/(k+1)
        if (m+1)%200==0:
            print("NF494 original compact tail K(4B-u) modes",m+1,"/",M,flush=True)
    return l,kap,tailT

def fixed_window_frequencies(terms,pole,tailT):
    """Exact original full fixed-window 0<t<4B source multiplier.

    Digamma/polygamma integral is over t≥0; subtract t≥4B
    explicit same-source Laplace exponentials *before squaring.
    """
    grouped={}
    for f,k,coeff in terms:
        grouped.setdefault(f,[]).append((k,A(coeff)))
    assert len(grouped)==99 and sum(map(len,grouped.values()))==273
    a=A(F(1,4)); xT=A(T);pi=arb.pi()
    psi_a=a.digamma()
    moments={}
    for idx,(f,poly) in enumerate(grouped.items(),1):
        om=2*pi*A(f)
        s=acb(arb(0),om/2)
        z=acb(a)+s
        top=max(k for k,c in poly)
        tail=[acb(0) for _ in range(top+1)]
        for m in range(M):
            r=acb(A(F(4*m+1,4)))+s
            er=(-r*xT).exp()
            moment=er/r
            tail[0]+=moment
            for j in range(1,top+1):
                moment=(A(T)**j*er+j*moment)/r
                tail[j]+=moment
        # The original physical fixed-window source cancellation
        # is built into J0. Frequency integral needs no quadrature.
        js=[(z.digamma()-acb(psi_a)-acb(tailT)+tail[0])]
        for j in range(1,top+1):
            js.append(((-1)**(j+1))*z.polygamma(j)-tail[j])
        moments[f]=js
        if idx%20==0:
            print("NF494 original 273-mode true fixed-compact F digamma/finite-window moments",idx,"/99 frequencies",flush=True)
    out=[arb(0) for _ in range(N)]
    for f,poly in grouped.items():
        J=moments[f]; om=2*pi*A(f); iw=acb(arb(0),om)
        polyCo=[acb(0) for _ in range(14)]
        for k,coeff in poly:
            alpha=acb(arb(0),-coeff/2) if k%2==0 else acb(coeff/2)
            for j in range(k+1):
                moment=J[0]/2 if j==0 else -((-A(F(1,2)))**j)*J[j]/2
                polyCo[k-j]+=alpha*math.comb(k,j)*moment
        dpoly=[acb(0) for _ in range(14)]
        for k,c in enumerate(polyCo):
            for j in range(k+1):
                dpoly[j]+=c*math.comb(k,j)*A(B)**(k-j)*((-1)**j)
        em=[acb(1)]
        z=-iw
        for n in range(1,N):em.append(em[-1]*z/n)
        phase=(iw*A(B)).exp()
        for n in range(N):
            val=acb(0)
            for j in range(min(n,13)+1):val+=dpoly[j]*em[n-j]
            out[n]+=2*(phase*val).real

    # Authentic original odd sinh m0. Negative-rate J0 at s=-1/4
    # is evaluated WITHOUT singular psi(0) and with its m0 zero-rate
    # term replaced by exact physical finite T.
    sp=A(F(1,4))
    plus=(A(F(1,2)).digamma()-psi_a)
    tail_plus=arb(0)
    for m in range(M):
        r=A(F(2*m+1,2))
        tail_plus+=(-r*xT).exp()/r
    plus-=tailT-tail_plus
    minus=4*(1-(-sp*xT).exp())-xT+A(1).digamma()-A(F(5,4)).digamma()
    for m in range(1,M):
        lam=A(F(4*m+1,4)); r=A(m)
        minus-=(-lam*xT).exp()/lam-(-r*xT).exp()/r
    pp=A(pole)/4
    pphase=(A(B)/2).exp()
    mphase=(-A(B)/2).exp()
    fact=1
    for n in range(N):
        if n:fact*=n
        out[n]+=pp*(pphase*plus*(-A(F(1,2)))**n -
                    mphase*minus*A(F(1,2))**n)/fact
    print("NF494 whole original fixed-window source 400 F_j all modes and true m0 SUCCESS",flush=True)
    return out

def physical_moving_corrections(u,l,kap):
    """Four exact old-source beta/harmonic recurrences, no mesh."""
    print("NF494 original joint two moving endpoint series, 400 jets",flush=True)
    Fcts=[math.factorial(i) for i in range(N+1)]
    harmonics=[F(0)]
    for j in range(1,N):harmonics.append(harmonics[-1]+F(1,j))
    left=[arb(0) for _ in range(N)]
    right=[arb(0) for _ in range(N)]
    qsmall=[arb(0) for _ in range(N)]
    qtail=[arb(0) for _ in range(N)]
    logsmall=[arb(0) for _ in range(N)]
    for n in range(1,N):
        ln=arb(0);rn=arb(0)
        for j in range(1,n+1):
            k=n-j
            if k==0:bet=harmonics[j]
            else:bet=F(1,k)-F(Fcts[k-1]*Fcts[j],Fcts[k+j])
            ln+=u[j]*l[k]*A(F(2)**k*bet)/2
        for j in range(n):
            k=n-1-j
            bet=F(1,k+1)-F((-1)**j*Fcts[k]*Fcts[j],Fcts[j+k+1])
            rn+=u[j]*kap[k]*A(F(2)**k*bet)
        left[n]=ln;right[n]=rn
        qsmall[n]=l[n]*A(F(2)**n/F(n))
        qtail[n]=A(F(2)**n/F(n))*(kap[n-1]-A(F(1)/T**n))
        logsmall[n]=-A(F(1,n)*(F(1,1)/(2*B))**n)
    assert left[0].contains(0) and right[0].contains(0)
    scalar=[arb(0) for _ in range(N)]
    for n in range(N):
        val=arb(0)
        for j in range(n):
            k=n-j
            val+=u[j]*(logsmall[k]-qsmall[k]-qtail[k])
        scalar[n]=val/2
    return left,right,scalar

def assemble_H(terms,pole,u,l,kap,tailT,jet):
    psi_a=A(F(1,4)).digamma();psi1=A(1).digamma()
    logpi=arb.pi().log()
    # Derived exactly from ∫_0^(4B)(K-1/t):
    # Q0=psi(1)-psi(1/4)-log(4B)-T(4B)
    # C=c0 +T(4B)+(log2+Q0)/2, NF446 c0=psi(1/4)-log pi.
    const=(psi_a+psi1-2*logpi+(A(F(2)/T)).log()+tailT)/2
    fixed=fixed_window_frequencies(terms,pole,tailT)
    left,right,scalar=physical_moving_corrections(u,l,kap)
    result=[const*u[n]+fixed[n]+left[n]+right[n]+scalar[n] for n in range(N)]

    # Every true original J8 regular translation U(x-log n)+v is
    # contracted at actual native original 4096bit, not replaced by
    # copied source intervals of insufficient precision.
    for n,p in POWERS.items():
        x0=A(B)-A(n).log()
        assert A(-B)<x0<A(B)
        prime=A(p).log()/A(n).sqrt()
        old=[F(a) for a in jet[str(n)]]
        plo,phi=enc(prime,180)
        assert F(0)<old[0]<=plo<=phi<=old[1]<1, (
             "METHOD STOP: original exact Λ(n)/sqrt(n) 4096bit native value outside unchanged NF411 source interval",n)
        reg=original_source_jet(terms,pole,x0)
        for j in range(N):
            result[j]-=prime*(reg[j]+(u[0] if j==0 else arb(0)))
        print("NF494 original actual n9-active J8 regular source prime mode",n,flush=True)
    pp=A(CENTER)
    ss=(A(B)/2).sinh();cc=(A(B)/2).cosh()
    fact=1
    for n in range(N):
        if n:fact*=n
        result[n]-=pp*((-A(F(1,2)))**n)*(ss if n%2==0 else cc)/fact
    return result,const

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--output",required=True)
    ap.add_argument("--source",default="notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json")
    ap.add_argument("--seams",default="notes/data/provisional/NF406_original_prime_support_partition_exact.json")
    ap.add_argument("--jet",default="notes/data/provisional/NF411_original_source_boundary_jet.json")
    ap.add_argument("--nf450",default="notes/data/provisional/NF450_original_B_complete_Laplace_native_sign_custody_index.json")
    args=ap.parse_args()
    ctx.prec=PREC
    src,sha=read(args.source);seams,ss=read(args.seams)
    jet,js=read(args.jet);old,os=read(args.nf450)
    assert sha==SRC and ss==SEAM
    assert jet["nf407_source_sha256"]==old["source_SHA256"]==SRC
    terms,pole,s0=native_source(src)
    assert len(terms)==273 and s0<F(1,10**700)
    assert F(10)**300*s0<SOURCE_FEE
    assert src["original_dimension"]==242
    assert len(src["original_exact_native_original_four_critical_coefficients_mid_radius"])==4
    assert len(src["original_source_critical_sine_frequencies"])==32
    weights={}
    for row in jet["all_seven_original_prime_seam_derivative_identities"]:
        n=row["prime_power"]
        assert n in POWERS
        weights[str(n)]=row["c_n_positive_outward"]
    assert len(weights)==7
    print("NF494 native 4096bit complete original original U 400 log jets",flush=True)
    u=original_source_jet(terms,pole,A(B))
    l,kap,tailT=kernel_coefficients()
    H,const=assemble_H(terms,pole,u,l,kap,tailT,weights)
    endpoint=tuple(map(F,old["complete_z_B_outward_24_decimal"]))
    assert overlap(enc(H[0]),endpoint),"METHOD STOP: original joint compact H0 != NF450 physical z(B)"
    assert endpoint[1]<0 and enc(H[0])[1]<0
    uh=poly_value(u,DELTA)
    hh=poly_value(H,DELTA)
    real_original_U=U(src).at(C(A(B-DELTA))).real
    assert overlap(enc(uh),enc(real_original_U)),"METHOD STOP: original NF493 U400 source check"
    assert enc(uh)[0]>0
    # Original exact NF492 accepted H(1/500) approximately -7.6176278061e-10
    # The check here is intentionally diagnostic; the independent
    # exact original NF492 raw H receipt provides the strict interval.
    target=F("-7.61762780612701731786e-10")
    assert enc(hh)[0]<target+F(1,10**18) and enc(hh)[1]>target-F(1,10**18),(
        "METHOD STOP: actual whole original H400 disagrees with accepted NF492 physical H")
    assert enc(hh)[1]<0
    # Original NF492 global Cauchy fee with source error:
    cauchyH=F(10)**420*(DELTA/R)**N/(1-DELTA/R)
    cauchyU=F(10)**400*(DELTA/R)**N/(1-DELTA/R)
    assert cauchyH<F(1,10**99) and cauchyU<F(1,10**119)
    # Includes original 1e-300 holomorphic source+truncated fixed-window
    # special-functions & both original moving-endpoint source errors.
    coeff_fee=[SOURCE_FEE*F(25)**n for n in range(N)]
    def serial(vals):
        return [[str(x-c),str(y+c)] for n,z in enumerate(vals)
                for x,y in [enc(z)] for c in [coeff_fee[n]]]
    result={
       "pass":"NF494-native",
       "standing":"FULL ALL 400 TRUE ORIGINAL NF446 joint compact REAL ANALYTIC H(d) source-contracted 4096bit coefficients plus actual original U400, NF450 endpoint / NF492 independent Hdelta checkpoint, actual numeric Ew_T source square OPEN until exact independent moment audit",
       "original_nf407_source_sha256":SRC,
       "original_nf406_seams_sha256":SEAM,
       "original_nf411_source_jet_sha256":js,
       "original_nf450_z_B_source_sha256":os,
       "original_source_original_246_generators_273_modes":True,
       "original_source_true_sinh_zero_rate_pole":True,
       "original_critical_sine_frequencies":32,
       "native_precision_bits":PREC,
       "original_B":"11/10",
       "original_true_terminal_delta":"1/500",
       "original_source_400_jet_order":N,
       "original_compact_fixed_kernel_T":"22/5",
       "original_joint_source_fixed_window_digamma_polygamma_max_order":13,
       "original_fixed_source_K_tail_index_count":M,
       "original_source_analytic_Cauchy_radius":"1/25",
       "original_source_each_coeff_holomorphic_numeric_input_overcharge":"1e-300*25**n",
       "original_source_original_dyadic_midpoint_radii_sum":str(s0),
       "original_U_400_native_outward":[[str(x) for x in iv] for iv in serial(u)],
       "original_H_400_native_outward":[[str(x) for x in iv] for iv in serial(H)],
       "original_original_NF450_z_B_outward":[str(x) for x in endpoint],
       "original_source_H_at_B_minus_delta_400_native_outward":[str(x) for x in enc(hh)],
       "original_source_U_at_B_minus_delta_400_native_outward":[str(x) for x in enc(uh)],
       "original_original_NF492_true_Hdelta_reference_approx":str(target),
       "original_complete_J8_source_H0_equals_original_z_B":True,
       "original_original_H400_analytic_tail":str(cauchyH),
       "original_original_U400_analytic_tail":str(cauchyU),
       "original_fixed_window_source_input_and_m_greater_than_M_analytic_fee":"1e-300 on |d|<=1/25; source coeff fee 1e-300*25^n",
       "original_full_J8_Ew_integrated":False,
       "original_complete_D8_UPPER":"OPEN",
       "NF404":"OPEN","W_ODD_NEG":"OPEN","RH":"OPEN",
       "next_bold":"NF494 independent pure Fraction original source covariance-preserving whole square H400/U400 polynomial-log moment with native input, Cauchy, first n9 panel and NF491 final collar, then NF404"
    }
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(result,indent=2)+"\n")
    print("NF494 original whole analytic H0",*[float(x) for x in enc(H[0])],flush=True)
    print("NF494 original true physical H(549/500) native source 400 jets",*[float(x) for x in enc(hh)],flush=True)
    print("NF494 SOURCE NATIVE original H400/U400 all source 4096bit PASS, independent actual Ew still OPEN",flush=True)
if __name__=="__main__":main()
