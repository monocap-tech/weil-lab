#!/usr/bin/env python3
"""NF489: first genuine physical J8 terminal complete source-native point.

At x=B-1/500, evaluate accepted NF446 JOINT compact physical z, never
separately evaluate its 10^142 native exterior analytic continuation
image shadows. Retain all original 246/273 source + true odd sinh pole,
NF406 n=2,3,4,5,7,8,9 minus translates and original NF404 center.

Original true integrals are split on source compact t range:
 [0,a] (symmetric difference) and [a,h] (middle source) by
 4096bit original-source-contracted analytic Taylor/Cauchy;
 [h,b] by exact analytic original-source oscillator Laplace
 primitives of K(t)=sum_m exp(-(m+1/4)t), with certified compact
 physical geometric all-m remainder, h=1/10,a=1/250,b=549/125.
No quadrature guesses and NO whole J8 signed integral claim.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
from flint import arb,acb,ctx
from nf415_original_cell6_I1_validated_acb import native_source,U
import argparse,hashlib,json,math,sys

if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
B=F(11,10); D=F(1,500); X=B-D
AA=2*D;BB=2*(B+X);H=F(1,10);RAD=F(2,5)
N=1300;M_FULL=800;M_SHORT=720;PREC=4096
SRC="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAM="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
PRIMES=(2,3,4,5,7,8,9)
CENTER=F(6677356497477490213,4611686018427387904)
def A(x):
    if isinstance(x,arb):return x
    if isinstance(x,F):return arb(x.numerator)/arb(x.denominator)
    return arb(x)
def C(x):return acb(A(x))
def read(p):
    s=Path(p).read_bytes()
    return json.loads(s),hashlib.sha256(s).hexdigest()
def enclosure(q,digits=150):
    m,r,e=q.mid_rad_10exp(digits)
    f=F(10)**int(e)
    return F(int(m)-int(r))*f,F(int(m)+int(r))*f
def iv_overlap(a,b):return a[0]<=b[1] and b[0]<=a[1]
def iv_plus(a,b):return a[0]+b[0],a[1]+b[1]
def iv_broad(a,err):return a[0]-err,a[1]+err
def rate_integral(rate):
    if rate==0:return A(BB-H)
    r=A(rate)
    return ((-r*A(H)).exp()-(-r*A(BB)).exp())/r

def original_source_taylor(terms,pole):
    """U(X-t/2) full original source coefficients to order N.

    U(X+t/2) is same expansion with (-1)^n signed coefficients.
    Source source modes are FULLY contracted at each n.
    """
    u=[arb(0) for _ in range(N)]
    pi=arb.pi()
    half=A(F(1,2))
    for idx,(f,k,c) in enumerate(terms,1):
        om=2*pi*A(f)
        iw=acb(arb(0),om)
        alpha=acb(arb(0),-A(c)/2) if k%2==0 else acb(A(c)/2)
        pre=alpha*(iw*A(X)).exp()
        z=-iw/2
        ev=[acb(1)]
        for n in range(1,N):
            ev.append(ev[-1]*z/n)
        pp=[A(math.comb(k,j))*A(X)**(k-j)*(-half)**j for j in range(k+1)]
        for n in range(N):
            term=acb(0)
            for j in range(min(k,n)+1):
                term+=pp[j]*ev[n-j]
            u[n]+=2*(pre*term).real
        if idx%90==0:print("NF489 authentic original source Taylor modes",idx,"/273",flush=True)
    pp=A(pole)
    sinh=(A(X)/2).sinh()
    cosh=(A(X)/2).cosh()
    fact=1
    for n in range(N):
        if n: fact*=n
        u[n]+=pp*((-A(F(1,4)))**n)*(sinh if n%2==0 else cosh)/fact
    return u

def kernel_tK():
    """L=t exp(-t/4)/(1-exp(-t)) exact formal inverse, l0=1."""
    ker=[arb(0) for _ in range(N)]
    ep=[arb(0) for _ in range(N)]
    fac=1
    for n in range(N):
        if n:fac*=n
        ep[n]=(-A(F(1,4)))**n/fac
    ker[0]=arb(1)
    for n in range(1,N):
        val=ep[n]
        for j in range(1,n+1):
            val-=A(F((-1)**j,math.factorial(j+1)))*ker[n-j]
        ker[n]=val
    return ker

def near_t_integrals(u,v,ker,lim):
    """Exact original [0,a],[a,h] primitive from finite Taylor, no mesh."""
    # Original A_x and M_x are same ORIGINAL source u_n.
    asym=[arb(0) for _ in range(lim)]
    middle=[arb(0) for _ in range(lim)]
    middle[0]=(u[0]-v)/2
    for n in range(1,lim):
        middle[n]=-u[n]/2
        if n%2==0: asym[n]=-u[n]
    # A*L and M*L Taylor coefficients.
    outA=[arb(0) for _ in range(lim)]
    outM=[arb(0) for _ in range(lim)]
    for n in range(lim):
        va=arb(0);vm=arb(0)
        for j in range(n+1):
            va+=ker[j]*asym[n-j]
            vm+=ker[j]*middle[n-j]
        outA[n]=va;outM[n]=vm
    r=A(AA);h=A(H)
    integralA=arb(0);integralM=outM[0]*(h/r).log()
    integralQ=arb(0)
    ar=r; hr=h
    for n in range(1,lim):
        integralA+=outA[n]*ar/n
        integralM+=outM[n]*(hr-ar)/n
        integralQ+=ker[n]*(hr-ar)/n
        ar*=r;hr*=h
    assert outA[0].contains(0)
    return integralA,integralM,integralQ

def original_laplace_middle(terms,pole,uval,v):
    """Full correlated original J8 [h,b] physical source Laplace moments."""
    grouped={}
    for f,k,c in terms:
        grouped.setdefault(f,[]).append((k,A(c)))
    assert len(grouped)==99 and sum(len(a) for a in grouped.values())==273
    ya=X-H/2;yb=-B
    assert X-BB/2==yb
    pa=[A(ya)**j for j in range(14)]
    pb=[A(yb)**j for j in range(14)]
    phases={}
    pi=arb.pi()
    for f in grouped:
        om=2*pi*A(f)
        phases[f]=(om,acb(arb(0),om*A(ya)).exp(),acb(arb(0),om*A(yb)).exp())
    integratedK=arb(0)
    integratedKU=arb(0)
    integratedTail=arb(0)
    atshort=None
    for m in range(M_FULL):
        lam=F(4*m+1,4);la=A(lam)
        eh=(-la*A(H)).exp();eb=(-la*A(BB)).exp()
        J=(eh-eb)/la
        integratedK+=J
        integratedTail+=eb/la
        source_piece=arb(0)
        for f,poly in grouped.items():
            om,phaseA,phaseB=phases[f]
            z=acb(2*la,om)
            prA=acb(1)/z;prB=prA
            vals=[2*(phaseA*eh*prA-phaseB*eb*prB)]
            maxk=max(k for k,c in poly)
            for k in range(1,maxk+1):
                prA=(pa[k]-k*prA)/z
                prB=(pb[k]-k*prB)/z
                vals.append(2*(phaseA*eh*prA-phaseB*eb*prB))
            for k,c in poly:
                source_piece+=c*(vals[k].imag if k%2==0 else vals[k].real)
        # physical original sinh U(X-t/2)/2; m0 rate0 handled.
        pole_int=(A(X)/2).exp()*rate_integral(lam+F(1,4))
        pole_int-=(-A(X)/2).exp()*rate_integral(lam-F(1,4))
        source_piece+=A(pole)*pole_int/2
        integratedKU+=source_piece
        if m+1==M_SHORT:
            atshort=(integratedK,integratedKU,integratedTail)
        if (m+1)%80==0:print("NF489 source-contracted original compact [h,b] Laplace",m+1,"/800",flush=True)
    assert atshort is not None
    return (integratedK,integratedKU,integratedTail),atshort

def assembled_point(native,near,laplace,uregs,weights):
    uval,v=native
    first,middle,qsmall=near
    k_mid,u_mid,k_tail=laplace
    # Original NF446 JOINT J_U after full central+both image
    # exterior continuation cancellation.  No T_m exterior images.
    c0=A(F(1,4)).digamma()-arb.pi().log()
    wholeMiddle=(uval-v/2)*k_mid-u_mid/2
    qbig=k_mid-(A(BB)/A(H)).log()
    scalar=v/2*((A(B+X)/A(B)).log()+qsmall+qbig)
    J=c0*uval+first+middle+wholeMiddle+scalar+uval*k_tail
    # Exact original NF406 all seven n9-active regular minus U shifts:
    regular=arb(0)
    for n in PRIMES:
        regular+=weights[n]*(uregs[n]+v)
    z=J-regular-A(CENTER)*(A(X)/2).sinh()
    return z,J,regular

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--source",default="notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json")
    ap.add_argument("--seams",default="notes/data/provisional/NF406_original_prime_support_partition_exact.json")
    ap.add_argument("--jet",default="notes/data/provisional/NF411_original_source_boundary_jet.json")
    ap.add_argument("--nf450",default="notes/data/provisional/NF450_original_B_complete_Laplace_native_sign_custody_index.json")
    ap.add_argument("--out",required=True)
    opt=ap.parse_args()
    ctx.prec=PREC
    original,ssh=read(opt.source)
    seam,sk=read(opt.seams)
    jet,jsha=read(opt.jet)
    zold,zsha=read(opt.nf450)
    assert ssh==SRC and sk==SEAM and jet["nf407_source_sha256"]==zold["source_SHA256"]==SRC
    assert original["original_dimension"]==242 and len(original["original_source_critical_sine_frequencies"])==32
    terms,pole,s0=native_source(original)
    assert len(terms)==273 and s0<F(1,10**700)
    assert all(0<f<883 and 0<=k<=13 for f,k,c in terms)
    raw=sum((abs(c)*(B+RAD/2)**k for f,k,c in terms),abs(pole))
    assert raw<F(10)**160
    # The same original NF448 Cauchy source envelope, valid at X=B-d.
    E=F(22,7)*883*RAD
    E=(E.numerator+E.denominator-1)//E.denominator
    assert E==1111 and F(11,4)**E<F(10)**500
    source_M=4*F(10)**160*F(11,4)**E
    ratio=H/RAD
    assert ratio==F(1,4) and AA<H and BB>4
    # Two separate original near-origin source integrals, broad common
    # source complex bound and tK source analytic radius R.
    cauchy_tail=F(200)*source_M*ratio**(N-16)/(1-ratio)
    assert cauchy_tail<F(1,10**50), "METHOD STOP: original near-t correlated Cauchy tail"
    # Actual original true full-compact source: no source-ent y>B.
    src=U(original)
    v=src.at(C(A(B))).real
    ux=src.at(C(A(X))).real
    ug={}
    for n in PRIMES:
        y=A(X)-arb(n).log()
        assert A(-B)<y<A(B)
        ug[n]=src.at(C(y)).real
    weights={}
    weight_radius=F(0)
    for row in jet["all_seven_original_prime_seam_derivative_identities"]:
        n=row["prime_power"]
        if n in PRIMES:
            low,high=map(F,row["c_n_positive_outward"])
            assert 0<low<=high<1
            weights[n]=A((low+high)/2)
            weight_radius+=(high-low)/2
    assert tuple(sorted(weights))==PRIMES
    assert weight_radius<F(1,10**25)
    # Real original dyadic source input: uniform S0 <1e-700, physically
    # compact NF413 source derivative error amplification <1e10.
    source_input_fee=F(1,10**500)
    assert F(10)**10*s0<source_input_fee
    assert AA==F(1,250) and BB==F(1099,250)
    print("NF489 original source-native joint compact Taylor start",flush=True)
    u=original_source_taylor(terms,pole)
    assert iv_overlap(enclosure(u[0]),enclosure(ux))
    l=kernel_tK()
    localfull=near_t_integrals(u,v,l,N)
    localshort=near_t_integrals(u,v,l,N-16)
    print("NF489 original source-native exact Laplace source join start",flush=True)
    lapfull,lapshort=original_laplace_middle(terms,pole,ux,v)
    zfull,jfull,regfull=assembled_point((ux,v),localfull,lapfull,ug,weights)
    zshort,jshort,regshort=assembled_point((ux,v),localshort,lapshort,ug,weights)
    # All m>=M original true compact source tail:
    # |M_x| < |U(x)|+|U(x-t/2)|/2+|v|/2<1351,
    # |v|/2 * omitted K <1/2, tail U(x)*K at b has
    # much stronger e^-b geometric; charge 2000 for safety.
    # e^h>=1+h, 1/(1-e^-h)<1+1/h=11.
    def tail(m):
        return F(2000)*F(11,1)*F(3,8)**(m//10)/F(m)
    boundfull=tail(M_FULL)
    boundshort=tail(M_SHORT)
    assert boundfull<F(1,10**29)
    assert boundshort<F(1,10**25)
    # Genuine source errors original 7 exact c_n weights,
    # |U|<900, |v|<1 => <901*sum weights radii.
    precision_charge=F(1,10**23)
    assert F(901)*weight_radius+source_input_fee+cauchy_tail+boundshort<precision_charge
    ff=iv_broad(enclosure(zfull),boundfull+precision_charge)
    ss=iv_broad(enclosure(zshort),boundshort+precision_charge)
    assert iv_overlap(ff,ss),"METHOD STOP: original two native truncations disagree"
    assert ff[1]-ff[0]<F(1,10**20),"METHOD STOP source output wider than 1e-20"
    # Accepted NF451 source modulus must overlap original NF450 z(B).
    zB=tuple(map(F,zold["complete_z_B_outward_24_decimal"]))
    assert zB[0]<zB[1]<0
    # 0<d<=1/500 original certified: |z(B-d)-z(B)|<
    # d*(14000+600*log(2B/d)); log(2B/d)=log1100<8.
    assert F(8,3)**8>2*B/D
    maxdist=D*(F(14000)+600*8)
    assert ff[0]-zB[1]<maxdist and zB[0]-ff[1]<maxdist
    out={
      "pass":"NF489",
      "standing":"FIRST genuine full ORIGINAL J8 x=B-1/500 source-cancelled physical joint compact point; NOT whole source signed D8 integration",
      "original_nf407_source_sha256":SRC,"original_nf406_seams_sha256":SEAM,
      "original_nf411_source_jet_sha256":jsha,"original_nf450_endpoint_source_sha256":zsha,
      "original_source_generators":246,"original_source_grouped_modes":273,"original_sinh_pole":True,
      "original_full_native_4096bits":True,
      "true_original_J8_x":"549/500","true_original_distance_to_B":"1/500",
      "true_original_t_subintervals":["0","1/250","1/10","1099/250"],
      "original_true_source_support":"[-11/10,11/10]",
      "original_7_regular_n9_active_prime_power":[2,3,4,5,7,8,9],
      "original_true_joint_4096bit_source_taylor_order":N,
      "original_true_joint_source_complex_Cauchy_radius":"2/5",
      "original_taylor_short_order":N-16,
      "original_true_full_analytic_compact_laplace_M":M_FULL,
      "original_true_short_analytic_compact_laplace_M":M_SHORT,
      "original_true_source_taylor_cauchy_tail_charge":str(cauchy_tail),
      "original_true_compact_Laplace_geometric_tail_charge":str(boundfull),
      "original_true_short_compact_Laplace_tail_charge":str(boundshort),
      "original_source_prime_weight_radius_charge":str(F(901)*weight_radius),
      "original_source_true_dyadic_input_charge":str(source_input_fee),
      "original_full_true_native_z_outward":[str(x) for x in ff],
      "original_short_true_native_z_outward":[str(x) for x in ss],
      "original_full_native_joint_archmid_outward":[str(x) for x in enclosure(jfull)],
      "original_full_native_regular_minus_outward":[str(x) for x in enclosure(regfull)],
      "original_original_NF450_Z_at_B_outward":[str(x) for x in zB],
      "original_NF451_true_complete_modulus_crosscheck":True,
      "original_full_J8_signed_upper":"OPEN","NF404":"OPEN","W_ODD_NEG":"OPEN","RH":"OPEN",
      "next_bold":"NF490 validated source-joint finite spectral panels and interval Taylor primitives across real terminal 0<d<=1/500, then 4p z +2z² integrated"
    }
    p=Path(opt.out);p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(out,indent=2)+"\n")
    print("NF489 genuine first original J8 complete joint-compact physical z(549/500)",*[float(x) for x in ff],flush=True)
    print("NF489 original source-native high precision first physical point PASS; full signed D8 upper NF404 RH OPEN",flush=True)
if __name__=="__main__":main()
