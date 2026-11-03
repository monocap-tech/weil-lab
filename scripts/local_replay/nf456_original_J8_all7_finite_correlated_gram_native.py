#!/usr/bin/env python3
"""NF456 original FULL SEVEN-PRIME regularized source + NF404 centered finite
response Gram on the entire genuine J8, with full original source coupling.

This is the NON-ARCHIMEDEAN finite sector F, NOT the full original
regularized z=J_arch+F. Compute all n2,3,4,5,7,8,9 ORIGINAL regular
translated terms on J8 using one 4096-bit 320-jet per original source shift,
fully correlated source before square, exact polynomial and log moments.
Also certify n9 independent NF454/NF455 overlap, full six-prime+center
background G=F-z9 and original arch-B anchor via ACCEPTED NF450 z(B).
"""
import argparse,math,json,sys
from pathlib import Path
from fractions import Fraction as Q
from flint import arb,ctx
from nf415_original_cell6_I1_validated_acb import native_source,U,A,C
from nf454_original_n9_contact_native_moment import read,enclosure,B,SRC_SHA,SEAM_SHA
from nf454_original_n9_log_weighted_native import analytic_coefficients,N,R,M,QBOUND

if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
PRIMES=(2,3,4,5,7,8,9)
CENTER=Q(6677356497477490213,4611686018427387904)

def interval_ops(q,r,unit=1):
    return tuple(str(x) for x in q),tuple(str(x) for x in r)

def squared_moment(s,t,a):
    """True exact Arb polynomial source moment, coefficients scaled by a^j."""
    val=arb(0)
    n=len(s)
    for i in range(n):
        val+=s[i]*t[i]/(2*i+1)
        for j in range(i+1,n):
            val+=(s[i]*t[j]+s[j]*t[i])/(i+j+1)
    return val*a

def weighted_integrals(s,a,L):
    """Poly s_j=(original source coeff)_j*a^j, true log(B/(a-y))."""
    u=arb(0)
    logu=arb(0)
    harm=Q(0)
    for j,z in enumerate(s):
        harm+=Q(1,j+1)
        u+=z/(j+1)
        logu+=z*(L+A(harm))/(j+1)
    return a*u,a*logu

def enlarge(v,err,digits=110):
    x,y=enclosure(v,digits)
    return x-err,y+err

def result(args):
    ctx.prec=args.precision
    assert ctx.prec>=3072
    source,sh=read(args.source)
    geo,gs=read(args.seams)
    jet,js=read(args.jet)
    nf453,j453=read(args.nf453)
    nf454,j454=read(args.nf454)
    nf455,j455=read(args.nf455)
    nf450,j450=read(args.nf450)
    assert (sh,gs)==(SRC_SHA,SEAM_SHA)
    assert all(x["source_sha256"]==sh and x["seams_sha256"]==gs for x in (nf453,))
    assert nf455["original_source_sha256"]==nf454["original_source_sha256"]==nf450["source_SHA256"]==sh
    assert nf455["original_seams_sha256"]==nf454["original_seams_sha256"]==nf450["seams_SHA256"]==gs
    assert nf453["CI_status"]==nf454["focused_numeric_exact_gates_status"]=="SUCCESS"
    assert nf455["final_strict_result"]==nf450["original_CI_result"]=="SUCCESS"
    assert jet["nf407_source_sha256"]==sh
    assert all(x["whole_J8"]=="OPEN" for x in [nf455])
    assert N==320 and R==Q(1,40) and M==Q(10)**230 and QBOUND==Q(3,25)

    coeff,pole,s0=native_source(source)
    assert source["original_dimension"]==242 and len(coeff)==273
    assert len(source["original_exact_native_original_four_critical_coefficients_mid_radius"])==4
    assert len(source["original_source_critical_sine_frequencies"])==32
    assert s0<Q(1,10**700)
    raw=sum((abs(q)*B**k for f,k,q in coeff),abs(pole))
    assert raw<Q(10)**160
    assert all(0<f<883 and 0<=k<=13 for f,k,c in coeff)

    intervals={int(x["prime_power"]):tuple(map(Q,x["c_n_positive_outward"])) for x in jet["all_seven_original_prime_seam_derivative_identities"]}
    assert tuple(sorted(intervals))==PRIMES
    weights={n:(p[0]+p[1])/2 for n,p in intervals.items()}
    hiweight=sum((p[1] for p in intervals.values()),Q(0))
    wdelta=sum(((q[1]-q[0])/2 for q in intervals.values()),Q(0))
    assert 0<hiweight<4 and 0<wdelta<Q(1,10**32)

    log9=arb(9).log()
    a=2*A(B)-log9
    x9=log9-A(B)
    al,ah=enclosure(a)
    s9=next(x for x in geo["original_prime_power_log_shifts"] if x["n"]==9)
    amin,amax=2*B-Q(s9["log_upper"]),2*B-Q(s9["log_lower"])
    assert 0<amin<=al<=ah<=amax<Q(3,1000)
    assert amax/R<QBOUND
    assert B/amin<1100 and Q(8,3)**8>1100
    assert Q(3)**139<Q(10)**67
    assert (Q(9,8)/B)**13<2

    src=U(source)
    v=src.at(C(B)).real
    v0,v1=enclosure(v,110)
    assert -Q(117,10**13)<v0<v1<-Q(116,10**13)
    L=(A(B)/a).log()
    terms={n:None for n in PRIMES}
    finite=[arb(0) for _ in range(N)]
    n9co=[arb(0) for _ in range(N)]
    for n in PRIMES:
        # For x=x9+y, ORIGINAL minus regular translate arg:
        # x-log(n)=log(9/n)-B+y. Each real arg lies in [-B,B].
        c=-A(B) if n==9 else x9-arb(n).log()
        cl,ch=enclosure(c,75)
        assert -B-Q(1,10**70)<=cl<ch<B
        assert cl> -Q(9,8) and ch<Q(9,8)
        uco=analytic_coefficients(coeff,pole,c)
        wi=A(weights[n])
        for j in range(N):
            d=-wi*(uco[j]+(v if j==0 else 0))
            finite[j]+=d
            if n==9:n9co[j]=d
        terms[n]=(str(weights[n]),str(intervals[n][0]),str(intervals[n][1]))
        print("NF456 original genuine prime source",n,"of",PRIMES,flush=True)

    # The original NF404 dyadic center is EXACT, not source midpoint.
    sh=(x9/2).sinh()
    ch=(x9/2).cosh()
    inv=arb(1)
    for j in range(N):
        if j:inv/=2*j
        finite[j]-=A(CENTER)*(sh if j%2==0 else ch)*inv
    six=[finite[j]-n9co[j] for j in range(N)]
    scaledF=[];scaled9=[];scaled6=[]
    power=arb(1)
    for j in range(N):
        scaledF.append(finite[j]*power)
        scaled9.append(n9co[j]*power)
        scaled6.append(six[j]*power)
        power*=a

    F0,Flog=weighted_integrals(scaledF,a,L)
    G0,Glog=weighted_integrals(scaled6,a,L)
    Z0,Zlog=weighted_integrals(scaled9,a,L)
    FF=squared_moment(scaledF,scaledF,a)
    GG=squared_moment(scaled6,scaled6,a)
    GZ=squared_moment(scaled6,scaled9,a)
    ZZ=squared_moment(scaled9,scaled9,a)
    endpointF=sum(scaledF,arb(0))

    # Uniform legitimate physical-sector complex Cauchy bound:
    # |U(center+y)|<10^230 for |y|=1/40, seven original
    # nonzero primes with sum weights<4, plus exact center sinh.
    # Thus whole finite F and its components' 320-jet tails <4*tU+2*t_sinh.
    T_U=M*(QBOUND**N)/(1-QBOUND)
    T_C=Q(2)*(QBOUND**N)/(1-QBOUND)
    assert T_U<Q(1,10**55) and T_C<Q(1,10**280)
    # Separate exact original 4096-bit dyadic coefficient radius on
    # every physical shift and original prime weight outward uncertainty.
    E9=intervals[9][1]*(T_U+2*s0)+901*(intervals[9][1]-intervals[9][0])/2
    E6=sum((intervals[n][1]*(T_U+2*s0)+901*(intervals[n][1]-intervals[n][0])/2 for n in PRIMES if n!=9),Q(0))+T_C
    EF=E6+E9
    assert E9>0 and E6>0 and EF<Q(1,10**29)
    # From accepted NF446 |U|<900 and |v|<1; seven weights sum<4
    # and centered term <2: full |F|<3606, |G|<3606, |z9|<901.
    # Use round 4000 for sup original finite F,G and 901 for z9.
    assert 901*hiweight+2<4000
    sqF_err=amax*(8000+EF)*EF
    sqG_err=amax*(8000+E6)*E6
    GZ_err=amax*(4000*E9+(901+E9)*E6)
    ZZ_err=amax*(1802+E9)*E9
    # Entire physical p integral <10^-10 a *(.5*(log(B/a)+1)+4)<1e-9*a.
    # The original p v and weight uncertainty are paid separately:
    # ∫|p_true-p_mid| <a*(9 S0+10^-10 Wdelta).
    p_err=amax*(9*s0+Q(1,10**10)*wdelta)
    assert p_err<Q(1,10**30)
    pF_err=Q(1,10**9)*amax*EF+(4000+EF)*p_err
    pG_err=Q(1,10**9)*amax*E6+(4000+E6)*p_err
    pZ_err=Q(1,10**9)*amax*E9+(901+E9)*p_err

    pF=v*(Flog/2+A(sum(weights.values()))*F0)
    pG=v*(Glog/2+A(sum(weights.values()))*G0)
    pZ=v*(Zlog/2+A(sum(weights.values()))*Z0)
    TF=enlarge(F0,amax*EF)
    TG=enlarge(G0,amax*E6)
    TZ=enlarge(Z0,amax*E9)
    TFlog=enlarge(Flog,9*amax*EF)
    FFiv=enlarge(FF,sqF_err)
    GGiv=enlarge(GG,sqG_err)
    ZZiv=enlarge(ZZ,ZZ_err)
    GZiv=enlarge(GZ,GZ_err)
    PFiv=enlarge(pF,pF_err)
    PGiv=enlarge(pG,pG_err)
    PZiv=enlarge(pZ,pZ_err)
    EF_B=enlarge(endpointF,EF)
    # Strict independent older original n9 prime-only source moments.
    n9_Zstrict=tuple(map(Q,nf455["true_original_2int_z9_square_strict"]))
    n9_Pstrict=tuple(map(Q,nf454["original_full_principal_4_integral_p_z9_strict"]))
    assert 2*ZZiv[0]<n9_Zstrict[1] and 2*ZZiv[1]>n9_Zstrict[0]
    assert 4*PZiv[0]<n9_Pstrict[1] and 4*PZiv[1]>n9_Pstrict[0]
    assert TZ[0]>0 # genuine n9 z9 integrated positive NF454

    # Direct exact source polynomial squares give all six-prime/n9
    # correlation, NOT a fictitious independent-source Gram.
    partialF=(4*PFiv[0]+2*FFiv[0],4*PFiv[1]+2*FFiv[1])
    residualG=(4*PGiv[0]+4*GZiv[0]+2*GGiv[0],
               4*PGiv[1]+4*GZiv[1]+2*GGiv[1])
    partial9=tuple(map(Q,nf455["true_original_partial_D8_n9_strict"]))
    assert partialF[0]<=partial9[1]+residualG[1] and partialF[1]>=partial9[0]+residualG[0]

    # Endpoint match with independently accepted full original NF450 z(B).
    # z(B)=J_arch(B)+F(B). Thus J_arch(B)=z(B)-F(B).
    zBlo,zBhi=map(Q,nf450["complete_z_B_outward_24_decimal"])
    assert zBhi<0
    archB=(zBlo-EF_B[1],zBhi-EF_B[0])
    # Strict entirely rational decision gates, never a sign from float midpoint.
    assert Q(8977981481882,10**13)<EF_B[0]<EF_B[1]<Q(8977981481883,10**13)
    assert -Q(8977981486266,10**13)<archB[0]<archB[1]<-Q(8977981486263,10**13)
    assert Q(22508888853,10**13)<FFiv[0]<FFiv[1]<Q(22508888855,10**13)
    assert Q(45017777699,10**13)<partialF[0]<partialF[1]<Q(45017777701,10**13)
    print("NF456 original complete finite G 2∫G²:",float(2*GGiv[0]),float(2*GGiv[1]),flush=True)
    print("NF456 original true six-prime/n9 4∫G*z9:",float(4*GZiv[0]),float(4*GZiv[1]),flush=True)
    print("NF456 original 4∫pG:",float(4*PGiv[0]),float(4*PGiv[1]),flush=True)
    print("NF456 original extra original G signed subtotal:",float(residualG[0]),float(residualG[1]),flush=True)
    print("NF456 original finite F zeroth moment:",float(TF[0]),float(TF[1]),flush=True)
    print("NF456 original source sup finite error bound:",float(EF),flush=True)
    print("NF456 true original finite F(B) midpoint:",float(EF_B[0]),float(EF_B[1]),flush=True)
    print("NF456 original inferred joint arch J(B):",float(archB[0]),float(archB[1]),flush=True)
    print("NF456 original whole seven-prime/center ∫F²:",float(FFiv[0]),float(FFiv[1]),flush=True)
    print("NF456 original 4∫pF+2∫F²:",float(partialF[0]),float(partialF[1]),flush=True)
    print("NF456 original full J8 D8 STILL OPEN; joint arch remains a correlated cancellation",flush=True)

    return {
     "pass":"NF456",
     "standing":"source-certified complete original J8 seven-prime+NF404-center finite regular source F, all six-prime/n9 cross and square moments; not full original signed D8, joint arch still OPEN",
     "original_source_sha256":sh,"original_seams_sha256":gs,
     "original_nf411_jet_sha256":js,"nf453_sha256":j453,"nf454_sha256":j454,"nf455_sha256":j455,"nf450_sha256":j450,
     "original_selected_plus_critical":246,"original_frequency_order_groups":273,"original_critical_sines":32,"native_precision":ctx.prec,
     "actual_n9_contact_a_outward":[str(al),str(ah)],
     "original_nf404_dyadic_center_exact":str(CENTER),
     "all_original_prime_weights_outward":{str(n):list([str(intervals[n][0]),str(intervals[n][1])]) for n in PRIMES},
     "original_n9_source_320_moment_overlaps_NF454_NF455":True,
     "original_finite_F_zero_moment_outward":list(map(str,TF)),
     "original_finite_G_sixprime_center_zero_moment_outward":list(map(str,TG)),
     "original_finite_F_log_moment_outward":list(map(str,TFlog)),
     "original_finite_F_square_integral_outward":list(map(str,FFiv)),
     "original_finite_G_square_integral_outward":list(map(str,GGiv)),
     "original_finite_G_n9_cross_integral_outward":list(map(str,GZiv)),
     "original_4int_pF_outward":[str(4*PFiv[0]),str(4*PFiv[1])],
     "original_4int_pG_outward":[str(4*PGiv[0]),str(4*PGiv[1])],
     "original_4int_pz9_independent_native_outward":[str(4*PZiv[0]),str(4*PZiv[1])],
     "original_finite_4pF_plus_2F2_outward":list(map(str,partialF)),
     "original_sixprime_center_added_partial_4pG_4Gz9_2G2_outward":list(map(str,residualG)),
     "original_finite_F_at_B_outward":list(map(str,EF_B)),
     "original_inferred_joint_arch_at_B_outward":list(map(str,archB)),
     "original_source_analytic_Cauchy_R":str(R),"original_source_M":str(M),
     "original_source_analytic_tail_single":str(T_U),
     "original_weight_uncertainty_sum":str(wdelta),"original_source_S0":str(s0),
     "original_uniform_F_error":str(EF),
     "original_E_F_less_than_1e_minus_29":True,
     "original_arch_required_in_full_response":"D8=(4int pF+2int F^2)+(4int pJ_arch+4int F J_arch+2int J_arch^2), J_arch original NF446 compact source",
     "full_original_J8_signed":"OPEN","full_original_J7_signed":"OPEN","NF404":"OPEN","W_ODD_NEG":"OPEN","RH":"OPEN",
     "next":"NF457 source-correlated joint arch J_arch difference from accepted endpoint matched against finite F, not separately huge L2 components"
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--source",default="notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json")
    ap.add_argument("--seams",default="notes/data/provisional/NF406_original_prime_support_partition_exact.json")
    ap.add_argument("--jet",default="notes/data/provisional/NF411_original_source_boundary_jet.json")
    ap.add_argument("--nf453",default="notes/data/provisional/NF453_original_J7_J8_principal_and_island_custody.json")
    ap.add_argument("--nf454",default="notes/data/provisional/NF454_original_J8_n9_contact_log_signed_custody.json")
    ap.add_argument("--nf455",default="notes/data/provisional/NF455_original_J8_n9_quadratic_and_partial_D_custody.json")
    ap.add_argument("--nf450",default="notes/data/provisional/NF450_original_B_complete_Laplace_native_sign_custody_index.json")
    ap.add_argument("--precision",type=int,default=4096)
    ap.add_argument("--output",required=True)
    args=ap.parse_args()
    d=result(args)
    out=Path(args.output);out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(d,indent=2,default=str)+"\n")
    print("NF456 source-native finite-sector exact-moment CI success; original whole J8 and RH OPEN",flush=True)
if __name__=="__main__":main()
