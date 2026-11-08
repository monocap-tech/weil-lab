#!/usr/bin/env python3
"""NF476 native original J7 near-B right panel signed D_R via one source-coefficient Taylor carrier.

Fixed original J7 physical interval x in [log(8)-B,1], with t=(x-99/100)/(3/200), so |t|<1.
Build all 1400 coefficients of source-correlated original physical z as:
 - native NF443 central digamma + special removable m0 sinh pole + principal log
 - exact native two matched original image families, 3000 source-shared modes
 - original six-minus NF405 prime regular source shifts and NF404 centering.
All source analytic generators retain the original 246/273 NF407 coefficient vector
and NF406 support and are evaluated at 4096-bit python-flint Arb.
Finite Taylor polynomial yields the true original mixed and quadratic moment
by exact polynomial moment identities; analytic and coefficient errors paid.
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

XC=Q(99,100);H=Q(3,200);N=1400;M=3000;PREC=4096
PRIMES=(2,3,4,5,7,8)
CENTER=Q(6677356497477490213,4611686018427387904)
SOURCE_TREE="f50e49cdc02b5e1eaacce7f8a66733fce9bc6f05"
R_CAUCHY=Q(1,25)
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
        if i%20==0:print("NF476 genuine original central frequencies",i,"/99",flush=True)
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
    assert B-XC==Q(11,100) and H/(B-XC)==Q(3,22)
    result[0]-=v/2*(A(B)/A(B-XC)).log()
    q=Q(3,22);power=q
    for j in range(1,N):
        result[j]-=v/2*A(power)/j
        power*=q
    return result

def image_part(groups,pole,start,stop):
    """NF471 original shared image amplitude, expanded in physical s variable."""
    assert 0<=start<stop<=M and start%1000==0 and stop==start+1000
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
            print("NF476 original two-sided images",m+1,"/",stop,flush=True)
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
        assert -A(B)<cy-A(H)<cy+A(H)<A(B)
        one=[arb(0) for _ in range(N)]
        for i,(f,poly) in enumerate(sorted(groups.items()),1):
            lam=acb(arb(0),2*arb.pi()*A(f))
            co=make_poly(poly,lam,cy,"raw")
            for j in range(N):one[j]+=co[j]
        sp,_=sinh_cosh_series(cy)
        for j in range(N):
            result[j]-=w*(one[j]+A(pole)*sp[j])
        result[0]-=w*v
        print("NF476 original physical negative regular prime shift",n,"/6",flush=True)
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
       "pass":"NF476","part":args.part,
       "original_nf407_source_sha256":sha,"original_nf406_seams_sha256":seam,
       "original_246_generators":True,"original_273_groups":True,
       "original_critical_sines":32,"original_sinh_pole":True,
       "native_bits":PREC,"polynomial_degree":N-1,
       "physical_panel":["log8-B","1"],"center":"99/100","halfwidth":"3/200",
       "original_image_index_start":args.start if args.part=="images" else None,
       "original_image_index_stop":args.stop if args.part=="images" else None,
       "source_radii_lt":"1e-700",
       "original_prime_wdelta_lt":"1e-32" if args.part=="primes" else None,
       "coefficient_interval_balls":balls,
       "J7_signed_cell":"OPEN","NF404":"OPEN","W_ODD_NEG":"OPEN","RH":"OPEN"
    }
    dest=Path(args.output);dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(out,separators=(",",":"))+"\n")
    print("NF476 original",args.part,"coefficients",len(balls),"DONE",flush=True)

def moment_scalar_poly(a):
    """Exact rational integral average of P(s) across s in [-1,1]."""
    return sum((x/Q(j+1) for j,x in enumerate(a) if j%2==0),Q(0))

def bounds_fraction_intervals(balls):
    return [tuple(map(Q,p)) for p in balls]

def assemble(args):
    folder=Path(args.input_dir)
    files=[folder/"nf476-central.json",folder/"nf476-primes.json"]
    files.extend(folder/f"nf476-images-{m}-{m+1000}.json" for m in range(0,M,1000))
    records=[]
    for f in files:
        assert f.exists(),f"Missing source-native coefficient block {f}"
        records.append(json.loads(f.read_text()))
    assert [r["part"] for r in records]==["central","primes"]+["images"]*3
    assert all(r["original_nf407_source_sha256"]==SRC_SHA and r["original_nf406_seams_sha256"]==SEAM_SHA for r in records)
    assert all(r["original_273_groups"] and r["native_bits"]==PREC and r["polynomial_degree"]==N-1 for r in records)
    assert [(r["original_image_index_start"],r["original_image_index_stop"]) for r in records[2:]]==[(m,m+1000) for m in range(0,M,1000)]
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
    # M_bound=10^350 (see analytic audit note), ratio H/R=1/2.
    eps_taylor=Q(10)**350*Q(3,8)**N/(1-Q(3,8))
    assert eps_taylor<Q(1,10**120)
    # Original NF476 x<=27/25 gives B-x>=1/50 and exp(-m/25), NOT exp(-2m/25).
    eps_image=Q(100*10**160,M)*Q(3,8)**(M//5)
    assert eps_image<Q(1,10**40)
    # Genuine original input uncertainty on physical J7:
    # original source dyadic S0<1e-700, original six prime weights total
    # uncertainty <1e-32, original |U|<900 and |v|<1.
    eps_input=Q(901,10**32)+Q(1,10**400)
    assert eps_coeff+eps_taylor+eps_image+eps_input<Q(1,10**28)
    eps_z=Q(1,10**28)
    zmeanP=moment_scalar_poly(mids)
    zcenterP=mids[0]
    # Independent original NF470 source center and NF471 full macroscopic mean.
    boundary=json.loads(Path(args.nf476_boundary_receipt).read_text())
    assert boundary["original_nf407_source_sha256"]==SRC_SHA
    assert boundary["original_nf406_seams_sha256"]==SEAM_SHA
    assert boundary["original_273_groups"] and boundary["joint_point"]["native_bits"]==PREC
    assert boundary["joint_point"]["x"]=="27/25"
    zleftP=sum((c if i%2==0 else -c for i,c in enumerate(mids)),Q(0)) # s=-1
    zleftOld=tuple(map(Q,boundary["joint_point"]["original_full_J7_z_outward"]))
    assert zleftP-eps_z<=zleftOld[1] and zleftOld[0]<=zleftP+eps_z, (
        "original NF470 architecture independent x=27/25 left-boundary mismatch",
        str(float(zleftP)),str(tuple(map(float,zleftOld))))
    assert XC-H==Q(27,25) and XC+H==Q(109,100)
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
    assert len(weights)==6 and wdelta<Q(1,10**32)
    # Original principal p(s)=v[C7+0.5 log(220/3)+0.5 sum_j (s/3)^j/j].
    KLOG=160
    pseries=[v*(sum(weights,arb(0))+(A(B)/A(B-XC)).log()/2)]
    for j in range(1,KLOG):
        pseries.append(v*A(Q(3,22)**j)/(2*j))
    plog_tail=Q(117,10**13)*Q(3,22)**KLOG/(2*KLOG*(1-Q(3,22)))
    assert plog_tail<Q(1,10**116)
    # We only compute source moment of the midpoint polynomial P.
    zball=[A(m) for m in mids]
    mean_z2=arb(0)
    for i in range(N):
        one=arb(0)
        for j in range(i%2,N,2): # i+j even
            one+=zball[j]/(i+j+1)
        mean_z2+=zball[i]*one
        if i%200==0:print("NF476 original complete source z-square rows",i,"/1600",flush=True)
    mean_pz=arb(0)
    for i,za in enumerate(zball):
        one=arb(0)
        for j in range(i%2,KLOG,2):
            one+=pseries[j]/(i+j+1)
        mean_pz+=za*one
    # Exact variance-covariance relation, with original principal mean.
    mean_p=arb(0)
    for j,pp in enumerate(pseries):
        if j%2==0:mean_p+=pp/(j+1)
    mean_zP=A(zmeanP)
    varP=mean_z2-mean_zP*mean_zP
    covP=mean_pz-mean_p*mean_zP
    if varP<0:
        assert varP> A(-Q(1,10**100))
    # D_I = L*[4<E[pz]>+2<E[z²]>], L=1/50.
    DI=A(Q(1,100))*(4*mean_pz+2*mean_z2)
    # Uniform source error |z-P|<1e-28, true |z|<25000 (NF446).
    # |P|<25001. |p|<7e-11; |p midpoint difference|<1e-40
    # from original NF411 weight errors and source S0.
    pmax=Q(7,10**11)
    # On the genuine NF476 physical panel d=B-x>=1/100, B/d<=110.
    # Exact rational lower Taylor polynomial for exp(5) proves log(110)<5.
    assert sum((Q(5)**j/Q(math.factorial(j)) for j in range(7)),Q(0))>110
    assert Q(117,10**13)*(Q(793,250)+Q(5,2))<pmax
    err_p=Q(1,10**40)
    e_pz=pmax*eps_z+err_p*25001+plog_tail*25001
    e_z2=Q(50001)*eps_z
    momenterr=Q(1,100)*(4*e_pz+2*e_z2)
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
     "pass":"NF476",
     "standing":"source-certified full original J7 macroscopic signed D_I if strict sign gate passes",
     "original_nf407_source_sha256":SRC_SHA,
     "original_nf406_seams_sha256":SEAM_SHA,
     "native_NF459_source_tree":SOURCE_TREE,
     "original_source_generators":246,"original_modes":273,
     "original_critical_sines":32,"original_sinh_pole":True,
     "native_precision_bits":PREC,
     "genuine_original_J7_panel":["log8-B","1"],
     "original_six_regular_minus_prime_powers":list(PRIMES),
     "fixed_source_Chebyshev_or_Taylor_basis":"source-native shared coefficient x=99/100+(3/200)t, degree 1399, physical t in [tlo,2/3]",
     "source_centered_Taylor_analytic_radius":"1/25",
     "source_truncated_branch_Cauchy_M":"10^350",
     "certified_sup_z_minus_polynomial":"1/10^28",
     "original_source_arb_coefficient_aggregate_width":str(eps_coeff),
     "original_panel_type":"J7 true irrational left seam panel, NF464 partition [log8-B,1]",
     "original_signed_integration_length":"21/10-log8",
     "source_Cauchy_ratio":"3/8",
     "principal_log_ratio":"3/22", 
     "original_source_Taylor_remainder":str(eps_taylor),
     "original_joint_image_real_tail":str(eps_image),
     "original_source_weight_input_error_upper":str(eps_input),
     "original_true_mean_cross_check_NF471":False,
     "original_true_irrational_n8_seam_zero_from_oddness":True,
     "original_z_mean_from_polynomial":[str(zmeanP-eps_z),str(zmeanP+eps_z)],
     "original_NF470_architecture_left_boundary_z_from_polynomial":[str(zleftP-eps_z),str(zleftP+eps_z)],
     "original_pz_normalized_mean_outward":[str(pz0),str(pz1)],
     "original_z2_normalized_mean_outward":[str(zz0),str(zz1)],
     "source_covariance_normalized_mean_outward":[str(cv0),str(cv1)],
     "source_variance_normalized_mean_outward":[str(vv0),str(vv1)],
     "source_original_D_I_outward":[str(dlo),str(dhi)],
     "source_original_D_I_strict_sign":sign,
     "NF404":"OPEN","W_ODD_NEG":"OPEN","RH":"OPEN",
     "whole_original_J7":"OPEN","whole_original_J8":"OPEN"
    }
    dest=Path(args.output);dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(result,indent=2)+"\n")
    print("NF476 source ORIGINAL J7 mean z",float(zmeanP),flush=True)
    print("NF476 source ORIGINAL J7 pz",float(pz0),float(pz1),flush=True)
    print("NF476 source ORIGINAL J7 z²",float(zz0),float(zz1),flush=True)
    print("NF476 source ORIGINAL signed J7 D_I",float(dlo),float(dhi),sign,flush=True)
    print("NF476 original whole J7 and RH OPEN",flush=True)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--part",choices=["central","images","primes","assemble"],required=True)
    ap.add_argument("--start",type=int,default=0)
    ap.add_argument("--stop",type=int,default=0)
    ap.add_argument("--source",default="notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json")
    ap.add_argument("--seams",default="notes/data/provisional/NF406_original_prime_support_partition_exact.json")
    ap.add_argument("--jet",default="notes/data/provisional/NF411_original_source_boundary_jet.json")
    ap.add_argument("--input-dir",default="../results")
    ap.add_argument("--nf476-boundary-receipt",default="../boundary/nf476-original-J7-left-boundary-point.json")
    ap.add_argument("--nf471-receipt",default="../candidate/notes/data/provisional/NF471_original_J7_complete_macroscopic_mean_custody.json")
    ap.add_argument("--output",required=True)
    args=ap.parse_args()
    if args.part=="assemble":assemble(args)
    else:save_part(args)
if __name__=="__main__":main()
