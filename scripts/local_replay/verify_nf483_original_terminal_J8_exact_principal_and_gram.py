#!/usr/bin/env python3
"""NF483 authentic original J8 principal L2 EXACT and finite-image Gram route.

This is an accepted source-custodied ANALYTIC component of the original
J8 terminal response, not the original terminal mixed/quadratic integral.

All original NF411 4096-bit source v = U(B), original seven NF406 J8 prime
weights, NF450 z(B) and physical log(9) endpoint are carried as outward
exact Fractions. The genuine principal squared energy is integrated
ANALYTICALLY, including the improper physical x=B logarithmic endpoint.

The source-frozen z(B) model is separately tested and its ORIGINAL NF451
remainder charged. It is NOT silently turned into a genuine z(x) integral.

The finite 18000 authentic image terms are assigned an EXACT
source-coefficient convolution + cross-correlation Gram formula, avoiding
naive O(18000^2) pointwise source squaring. The identity is replayed on
adversarial exact rational signed controls; actual 18000 source data and
nineteen endpoint Phi functions are not numerically integrated here.
"""
import argparse,hashlib,json,math,re,sys
from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal,localcontext
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[2]
DATA=ROOT/"notes/data/provisional"
B=F(11,10);DELTA=F(1,500);PRIMES=(2,3,4,5,7,8,9)
SRC="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAM="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
def load(path):
    raw=Path(path).read_bytes()
    return json.loads(raw),hashlib.sha256(raw).hexdigest()
def dec(a,d=48):
    with localcontext() as c:
        c.prec=d
        return str(Decimal(a.numerator)/Decimal(a.denominator))
def interval(a):
    x,y=map(F,a);assert x<=y
    return x,y
def arb_interval(s):
    mt=re.fullmatch(r"\[([+-]?[0-9]+(?:\.[0-9]+)?)e([+-]?[0-9]+)\s+\+/-\s+([0-9]+(?:\.[0-9]+)?)e([+-]?[0-9]+)\]",s.strip())
    assert mt is not None,("source-Arb value format mismatch",s[:130])
    center=F(mt.group(1))*F(10)**int(mt.group(2))
    radius=F(mt.group(3))*F(10)**int(mt.group(4))
    assert radius>0
    return center-radius,center+radius
def logpos(t,N=120):
    """Exact positive rational interval of log(t), 1<t<=2."""
    assert F(1)<t<=F(2)
    r=(t-1)/(t+1)
    lo=2*sum((r**(2*k+1)/F(2*k+1) for k in range(N)),F(0))
    hi=lo+2*r**(2*N+1)/(F(2*N+1)*(1-r*r))
    assert 0<lo<hi
    return lo,hi
def log9_positive(K=500):
    t=F(4,5)
    lo=2*sum((t**(2*k+1)/F(2*k+1) for k in range(K)),F(0))
    hi=lo+2*t**(2*K+1)/(F(2*K+1)*(1-t*t))
    return lo,hi
def J_exp_integer(lam,x):
    """Formal exponential time moment kernel, for actual source evaluations:
       lambda=0: x; lambda ≠0: (1-exp(-lambda*x))/lambda.
       Symbolic/formal verification below uses polynomial Laurent powers.
    """
    if lam==0: return ("length",str(x))
    return ("exp_moment",str(lam),str(x))

def convolution_signed(c):
    n=len(c)
    q=[F(0)]*(2*n-1)
    for i in range(n):
        for j in range(n):
            q[i+j]+=c[i]*c[j]
    return q
def correlation_signed(a,b):
    n=len(a);assert len(b)==n
    d={k:F(0) for k in range(1-n,n)}
    for i in range(n):
        for j in range(n):
            d[i-j]+=a[i]*b[j]
    return d
def exact_finite_image_gram_control():
    """Check HANKEL + CROSS CORRELATION identity, adversarial signed c.

    For a_m=m+1/4, let t=exp(-d/2), q=exp(-B):
    F_m(d)=t^(4m+1)-q^(4m+1)*t^(-(4m+1)).
    Image source I(d)=sum_m c_m F_m(d)/2.
    Then 4I(d)^2 = sum_s(c*c)_s t^(4s+2)
      +sum_s(b*b)_s t^(-4s-2)
      -2sum_k(c cross b)_k t^(4k), b_m=c_m q^(4m+1).
    This is valid for EVERY actual original source coefficient array
    including m0, no positivity or diagonal simplification.
    """
    tests=[
      [F(1)],
      [F(0),F(2),-F(3)],
      [F(7,11),-F(9,4),F(0),F(13,17),-F(5,7)],
      [F(1),-F(1),F(1),-F(1),F(1),-F(1)]
    ]
    checked=0
    for c in tests:
        n=len(c)
        for q,t in [(F(1,7),F(3,5)),(F(2,9),F(5,7)),(F(1,3),F(4,5))]:
            # Algebraic checks only: these fractions are NOT asserted
            # to equal the true physical original exp(-B), exp(-d/2).
            b=[c[m]*q**(4*m+1) for m in range(n)]
            I=sum((c[m]*(t**(4*m+1)-b[m]/c[m]*t**(-(4*m+1)))/2 if c[m] else F(0) for m in range(n))
            # Avoid any new physical source contraction; identity is formal.
            convc=convolution_signed(c);convb=convolution_signed(b)
            corr=correlation_signed(c,b)
            val=sum((co*t**(4*s+2) for s,co in enumerate(convc)),F(0))
            val+=sum((co*t**(-4*s-2) for s,co in enumerate(convb)),F(0))
            val-=2*sum((v*t**(4*k) for k,v in corr.items()),F(0))
            assert 4*I*I==val,("correlated source image Gram identity FAILED",n,str(q),str(t))
            checked+=1
    assert checked==12
    # Exact physical exponents for TRUE original a_m=m+1/4:
    # t^(4s+2)=e^[-(2s+1)d], t^(4k)=e^[-2kd].
    # Thus all 18k^2 quadratic finite-image moments require two
    # coefficient CONVOLUTIONS and one cross-CORRELATION, then 1D
    # analytic exponential moment weights J_exp_integer(lambda,delta).
    assert J_exp_integer(0,DELTA)==("length","1/500")
    assert J_exp_integer(1,DELTA)==("exp_moment","1","1/500")
    assert J_exp_integer(-1,DELTA)==("exp_moment","-1","1/500")
    return checked
def main():
    a=argparse.ArgumentParser();a.add_argument("--output",required=True)
    args=a.parse_args()
    source,hsrc=load(DATA/"NF407_original_fourth_physical_coefficients_native.json")
    seam,hseam=load(DATA/"NF406_original_prime_support_partition_exact.json")
    jet,hjet=load(DATA/"NF411_original_source_boundary_jet.json")
    end,hend=load(DATA/"NF450_original_B_complete_Laplace_native_sign_custody_index.json")
    mod,hmod=load(DATA/"NF451_original_J8_terminal_collar_custody_index.json")
    epold,hepold=load(DATA/"NF453_original_J7_J8_principal_and_island_custody.json")
    j8A,hj8A=load(DATA/"NF482_original_J8_first_irrational_signed_partial_native_custody.json")
    nf479,h479=load(DATA/"NF479_original_full_J8_forced_positive_NF404_transfer_custody.json")
    assert hsrc==SRC==jet["nf407_source_sha256"]
    assert hseam==SEAM==end["seams_SHA256"]==mod["original_seams_sha256"]
    assert source["original_dimension"]==242
    assert len(source["original_exact_native_original_four_critical_coefficients_mid_radius"])==4
    assert len(source["original_source_critical_sine_frequencies"])==32
    assert end["original_CI_result"]==mod["CI_result"]=="SUCCESS"
    assert j8A["source_nf407_sha256"]==SRC and j8A["source_nf406_seams_sha256"]==SEAM
    assert j8A["original_first_J8_source_CI"]["independent_exact_repair_ci_status"]=="SUCCESS"
    assert nf479["source_original_nf407_sha256"]==SRC
    assert epold["source_sha256"]==SRC and epold["seams_sha256"]==SEAM
    assert epold["CI_status"]=="SUCCESS"
    assert end["complete_z_B_strictly_negative"]
    assert jet["original_source_selected_count"]==242 and jet["original_source_critical_count"]==4
    n9=next(k for k in seam["original_prime_power_log_shifts"] if k["n"]==9)
    assert 2*B-F(n9["log_upper"])>F(1,1000)
    v0,v1=arb_interval(jet["original_original_source_value_at_B_arb"])
    z0,z1=map(F,end["complete_z_B_outward_24_decimal"])
    assert v0<v1<0 and z0<z1<0
    vals=jet["all_seven_original_prime_seam_derivative_identities"]
    assert tuple(k["prime_power"] for k in vals)==PRIMES
    C0=sum((F(k["c_n_positive_outward"][0]) for k in vals),F(0))
    C1=sum((F(k["c_n_positive_outward"][1]) for k in vals),F(0))
    assert 3<C0<C1<4
    V0,V1=-v1,-v0;Z0,Z1=-z1,-z0
    # TRUE J8 full physical length L8=2B-log9 (not rational surrogate).
    l9,u9=log9_positive()
    L8lo=2*B-u9
    L8hi=2*B-l9
    assert F(1,500)<L8lo<L8hi<F(1,300)
    assert 256 < B/L8hi < B/L8lo <512
    log2lo,log2hi=logpos(F(2))
    lrlo,lrhi=logpos(B/(256*L8hi))
    lslo,lshi=logpos(B/(256*L8lo))
    h8lo=8*log2lo+lrlo
    h8hi=8*log2hi+lshi
    # TRUE terminal physical [B-1/500,B].
    assert B-F(549,500)==DELTA
    log11lo,log11hi=logpos(F(11,10))
    logfive_lo,logfive_hi=logpos(F(5,4))
    hTlo=log11lo+3*logfive_lo+8*log2lo
    hThi=log11hi+3*logfive_hi+8*log2hi
    assert 6<hTlo<hThi<7
    assert h8lo>0 and h8lo<h8hi<7
    # Positive, increasing in C and h: F(C,h) principal L2 primitive.
    def principal_poly(C,h):
        return C*C+C*(h+1)+(h*h+2*h+2)/4
    pTlo=DELTA*V0*V0*principal_poly(C0,hTlo)
    pThi=DELTA*V1*V1*principal_poly(C1,hThi)
    p8lo=L8lo*V0*V0*principal_poly(C0,h8lo)
    p8hi=L8hi*V1*V1*principal_poly(C1,h8hi)
    assert F(0)<pTlo<pThi<p8lo<p8hi<F(1,10**21)
    ep0,ep1=map(F,epold["original_j8_ep"])
    assert ep0<=p8hi and p8lo<=ep1, "must overlap original NF453 principal E8"
    assert p8hi-p8lo<F(1,10**26),"whole original E_p8 must improve far beyond NF404 3.31e-26 corridor"
    # Original source exact terminal J8 principal linear moment.
    pmag_lo=DELTA*V0*(C0+(hTlo+1)/2)
    pmag_hi=DELTA*V1*(C1+(hThi+1)/2)
    # Source-frozen signed model z(B-d)≈Z (NOT native certified).
    d0lo=4*Z0*pmag_lo+2*DELTA*Z0*Z0
    d0hi=4*Z1*pmag_hi+2*DELTA*Z1*Z1
    assert F(0)<d0lo<d0hi
    # Original accepted NF451 true physical modulus:
    # |e(d)|<=d[14000+600 log(2B/d)] < d[14600+600 h(d)]
    # exact log-weighted moments with source true h=log(B/d).
    i0=DELTA**2/2
    i1=i0*(hThi+F(1,2))
    i2=i0*(hThi*hThi+hThi+F(1,2))
    Mint=14600*i0+600*i1
    pmint=V1*(C1*Mint+F(1,2)*(14600*i1+600*i2))
    j0=DELTA**3/3
    j1=j0*(hThi+F(1,3))
    j2=j0*(hThi*hThi+F(2,3)*hThi+F(2,9))
    M2int=14600**2*j0+2*14600*600*j1+600**2*j2
    original_error=4*pmint+4*Z1*Mint+2*M2int
    assert d0lo< F(2,10**21)
    assert original_error>F(1,10),"source modulus obviously too loose on entire 1/500 terminal"
    Dlo,Dhi=d0lo-original_error,d0hi+original_error
    assert Dlo<0<Dhi
    # Exact first-panel and original signed threshold custody unchanged.
    a0,a1=map(F,j8A["original_first_J8_signed_D_outward_conservative"])
    assert 0<a0<a1
    original_gate=F(nf479["original_J8_signed_sufficient_upper_for_NF404_approx"])
    terminal_sufficient=original_gate-a1
    assert F(0)<terminal_sufficient<F(2,10**22)
    assert Dlo<terminal_sufficient<Dhi
    controls=exact_finite_image_gram_control()
    out={
      "pass":"NF483",
      "standing":"ACCEPTED original 246-source/seven-prime exact analytic E_p whole J8 and true terminal; exact finite-image Gram Hankel/correlation identity; original source endpoint-frozen z(B) signed MODEL decisively non-certified under true NF451 modulus, terminal true signed D8 UPPER OPEN",
      "original_nf407_source_sha256":SRC,"original_nf406_seams_sha256":SEAM,
      "original_original_nf411_source_endpoint_sha256":hjet,
      "original_nf450_source_zB_SHA256":hend,
      "original_nf451_true_source_modulus_sha256":hmod,
      "original_nf482_original_first_J8_source_native_exact_custody_sha256":hj8A,
      "original_true_J8_interval":["log9-B","B"],
      "original_true_terminal_J8_interval":["549/500","B"],
      "original_terminal_length":"1/500",
      "original_true_J8_length_exact_rational":[str(L8lo),str(L8hi)],
      "original_full_principal_7_minus_J8_weight_set":list(PRIMES),
      "original_source_v_interval":[str(v0),str(v1)],
      "original_source_C8_interval":[str(C0),str(C1)],
      "original_source_Z_at_B_interval":[str(z0),str(z1)],
      "original_log_B_over_terminal_delta_exact_rational":[str(hTlo),str(hThi)],
      "original_log_B_over_full_J8_length_exact_rational":[str(h8lo),str(h8hi)],
      "exact_principal_L2_primitive":"L*v^2*(C8^2 + C8*(log(B/L)+1) + (log(B/L)^2+2log(B/L)+2)/4)",
      "original_true_terminal_principal_Ep_squared_interval":[str(pTlo),str(pThi)],
      "original_true_terminal_principal_Ep_squared_decimal":[dec(pTlo),dec(pThi)],
      "original_TRUE_COMPLETE_J8_principal_Ep_squared_interval":[str(p8lo),str(p8hi)],
      "original_TRUE_COMPLETE_J8_principal_Ep_squared_decimal":[dec(p8lo),dec(p8hi)],
      "original_TRUE_COMPLETE_J8_principal_Ep_interval_width_decimal":dec(p8hi-p8lo),
      "original_nf453_older_principal_J8_energy_overlap":True,
      "original_terminal_integral_p_interval":[str(-pmag_hi),str(-pmag_lo)],
      "original_terminal_Z_frozen_signed_model_interval":[str(d0lo),str(d0hi)],
      "original_terminal_Z_frozen_signed_model_decimal":[dec(d0lo),dec(d0hi)],
      "original_accepted_nf451_source_modulus":"|z(B-d)-Z| < d*(14000+600*log(2B/d)), no constant-z source replacement",
      "original_true_terminal_modulus_integrated_signed_error_upper":str(original_error),
      "original_true_terminal_modulus_integrated_signed_error_upper_decimal":dec(original_error),
      "original_terminal_modulus_only_D8_interval":[str(Dlo),str(Dhi)],
      "original_terminal_modulus_only_sign":"UNDECIDED - formally includes both signs and NF404 threshold",
      "source_original_NF479_terminal_sufficient_upper":str(terminal_sufficient),
      "original_endpoint_Z_frozen_model_NOT_CERTIFIED_as_true_D8":True,
      "source_original_18k_matched_images_exact_finite_energy_gram_identity":"4I(d)^2=sum_s(c*c)_s t^(4s+2)+sum_s(b*b)_s t^(-4s-2)-2sum_{k=-(M-1)}^(M-1)(c cross b)_k t^(4k), a_m=m+1/4, t=e^(-d/2), b_m=c_m*e^(-B(4m+1))",
      "original_finite_image_gram_exponential_moments":"J_lambda(delta)=(1-exp(-lambda delta))/lambda, J_0(delta)=delta; lambda=2s+1,-(2s+1),2k",
      "original_signed_rational_gram_symbolic_control_count":controls,
      "actual_original_m_0_to_17999_arch_source_gram_evaluated":False,
      "actual_original_19_source_Phi_cross_moments_evaluated":False,
      "original_TRUE_terminal_J8_signed_integral_upper":"OPEN",
      "original_complete_J8_signed_upper":"OPEN","NF404":"OPEN","W_ODD_NEG":"OPEN","RH":"OPEN",
      "next_bold":"NF484: use exact Hankel/convolution source-coefficient Gram to compute original finite 18k image square plus 19 source Phi and all mixed pz/regular shifted source contributions with rigorous interval arithmetic; certify true terminal J8 D upper, not endpoint-frozen surrogate"
    }
    dest=Path(args.output);dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(out,indent=2)+"\n")
    print("NF483 original TRUE full J8 principal Ep",dec(p8lo),dec(p8hi),flush=True)
    print("NF483 original TRUE terminal J8 principal Ep",dec(pTlo),dec(pThi),flush=True)
    print("NF483 frozen endpoint signed model NOT certified",dec(d0lo),dec(d0hi),flush=True)
    print("NF483 true original NF451 signed modulus error",dec(original_error),flush=True)
    print("NF483 authentic finite original image Gram exact Fraction controls",controls,flush=True)
    print("NF483 actual original terminal signed UPPER and NF404, W-ODD-NEG RH OPEN",flush=True)
if __name__=="__main__":main()
