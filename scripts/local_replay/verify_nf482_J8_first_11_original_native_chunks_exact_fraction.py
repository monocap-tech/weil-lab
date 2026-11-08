#!/usr/bin/env python3
"""NF482-B: true original J8 first physical signed integral via PURE exact Fraction.

Independently consumes 11 unmodified authentic 4096-bit native source Arb
coefficient block JSONs from original source run #42506659220.
Source data: ORIGINAL NF407 246/273/99/32 and genuine NF406 seven
prime-power minus shifts including n=9, original NF443 matched 18k images.

No flint/black-box Gauss mesh here. Exact rational source balls are
contracted BEFORE moment integration, including huge e141 cancellations.
True left endpoint log9-B and principal log(1375/3) are rigorously enclosed
by exact rational atanh series with analytic remainders. Genuine original
p-series and all 1200 z coefficients preserved, high-degree tail paid.
This proves ONLY first physical J8 panel; whole original J8 signed UPPER,
full centered NF404 sufficient scalar, W-ODD-NEG, RH all remain OPEN.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import argparse,json,math,re,sys,hashlib
from decimal import Decimal,localcontext
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)

SRC="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAM="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
N=1200
M=18000
NC=70
B=F(11,10)
XC=F(686,625)
H=F(1,2500)
PRIMES=(2,3,4,5,7,8,9)

def D(v):
    with localcontext() as ctx:
        ctx.prec=60
        return format(Decimal(v.numerator)/Decimal(v.denominator),".53e")
def iv(x):
    a,b=map(F,x);assert a<=b
    return a,b
def atanh_2_interval(t,K):
    """Exact rational bounds on 2*atanh(t), t in (-1,1)."""
    t=F(t)
    assert abs(t)<1
    p=sum((2*t**(2*j+1)/F(2*j+1) for j in range(K)),F(0))
    rem=2*abs(t)**(2*K+1)/(F(2*K+1)*(1-t*t))
    return (p,p+rem) if t>=0 else (p-rem,p)
def midpoint(a,b):return (a+b)/2
def radius(a,b):return (b-a)/2
def arb_enclosure(s):
    # Same NF411 original true U(B), native Arb 4096-bit and input dyadic.
    # The extra 1e-40 original source/prime error below dominates any
    # source-dyadic uncertainty not represented in this Arb text.
    m=re.fullmatch(r"\[([+-]?\d+(?:\.\d+)?e[+-]?\d+) \+/- (\d+(?:\.\d+)?e[+-]?\d+)\]",s)
    assert m,("original 4096bit NF411 source value malformed",s[:100])
    center=F(m.group(1));e=F(m.group(2))
    assert F(0)<e<F(1,10**400)
    return center-e,center+e
def moments(t,kmax):
    assert -1<t<0
    denom=1-t
    power=F(1)
    arr=[]
    for k in range(kmax):
        power*=t
        arr.append((1-power)/(F(k+1)*denom))
    return arr
def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--source-dir",required=True)
    parser.add_argument("--jet",default="notes/data/provisional/NF411_original_source_boundary_jet.json")
    parser.add_argument("--nf477",default="notes/data/provisional/NF477_original_J7_correlated_resolvent_high_image_tail_custody.json")
    parser.add_argument("--output",required=True)
    arg=parser.parse_args()
    root=Path(arg.source_dir)
    sources=list(sorted(root.glob("nf482a-*.json")))
    assert len(sources)==11,("expected 11 original source jobs",list(map(str,sources)))
    records=[]
    for f in sources:
        raw=f.read_bytes()
        o=json.loads(raw)
        assert o["pass"]=="NF482-A" and o["native_bits"]==4096
        assert o["original_nf407_source_sha256"]==SRC and o["original_nf406_seams_sha256"]==SEAM
        assert o["original_246_generators"] and o["original_273_groups"]
        assert o["original_critical_sines"]==32 and o["original_sinh_pole"]
        assert o["physical_panel"]==["log9-B","549/500"]
        assert len(o["coefficient_interval_balls"])==N
        records.append((f.name,o,hashlib.sha256(raw).hexdigest()))
    assert [o["part"] for _,o,_ in records].count("primes")==1
    assert [o["part"] for _,o,_ in records].count("central")==1
    assert [o["part"] for _,o,_ in records].count("images")==9
    assert sorted((o["original_image_index_start"],o["original_image_index_stop"])
                  for _,o,_ in records if o["part"]=="images")==[(j,j+2000) for j in range(0,M,2000)]
    print("NF482 independent original source 11 blocks pass 246/273/7prime SHA",flush=True)
    coeff=[]
    rounding=F(0)
    for j in range(N):
        lo=sum((F(o["coefficient_interval_balls"][j][0]) for _,o,_ in records),F(0))
        hi=sum((F(o["coefficient_interval_balls"][j][1]) for _,o,_ in records),F(0))
        assert lo<=hi
        coeff.append((lo,hi))
        rounding+=radius(lo,hi)
    assert rounding<F(1,10**40)
    tail=json.loads(Path(arg.nf477).read_text())
    assert tail["pass"]=="NF477" and tail["source_sha256"]==SRC and tail["seam_sha256"]==SEAM
    assert tail["independent_exact_fraction_ci"]["status"]=="SUCCESS"
    assert tail["source_resolvent_M"]==M
    Cm=F(tail["complete_original_source_Tm_all_m_ge_18000_strict_upper"])
    eps_image=Cm*F(3,8)**72/(2*F(1,500))
    assert eps_image<F(1,10**40)
    eps_taylor=F(10)**350 * F(2,5)**N / (1-F(2,5))
    assert eps_taylor<F(1,10**120)
    eps_input=F(901,10**32)+F(1,10**400)
    eps_z=rounding+eps_image+eps_taylor+eps_input
    assert eps_z<F(1,10**29)
    Z=[midpoint(*c) for c in coeff[:NC]]
    tail_z=sum((max(abs(lo),abs(hi)) for lo,hi in coeff[NC:]),F(0))
    assert tail_z<F(1,10**45),("original z polynomial cutoff precision",D(tail_z))
    e_z=eps_z+tail_z
    absz=sum(map(abs,Z),F(0))
    assert absz<F(1,10**9)
    print("NF482 exact source P0",D(Z[0]),"first",NC,"coefficients, tail",D(tail_z),flush=True)
    jet=json.loads(Path(arg.jet).read_text())
    assert jet["nf407_source_sha256"]==SRC
    assert jet["original_source_selected_count"]==242 and jet["original_source_critical_count"]==4
    vlo,vhi=arb_enclosure(jet["original_original_source_value_at_B_arb"])
    assert -F(117,10**13)<vlo<vhi<-F(116,10**13)
    weights=[]
    for row in jet["all_seven_original_prime_seam_derivative_identities"]:
        n=row["prime_power"]
        if n in PRIMES:
            a,b=iv(row["c_n_positive_outward"])
            assert F(0)<a<b<F(1)
            weights.append((n,a,b))
    assert tuple(sorted(n for n,_,_ in weights))==PRIMES
    wclo=sum((a for _,a,b in weights),F(0))
    wchi=sum((b for _,a,b in weights),F(0))
    assert F(3)<wchi<F(7)
    # log(1375/3)=9log2+log(1375/1536);
    # log2=2atanh(1/3), log(1375/1536)=2atanh(-161/2911).
    l2lo,l2hi=atanh_2_interval(F(1,3),80)
    lrlo,lrhi=atanh_2_interval(F(-161,2911),80)
    lolo=9*l2lo+lrlo
    lohi=9*l2hi+lrhi
    assert F(6)<lolo<lohi<F(7)
    v=midpoint(vlo,vhi);vd=radius(vlo,vhi)+F(1,10**40)
    c0=midpoint(wclo,wchi)+midpoint(lolo,lohi)/2
    cd=radius(wclo,wchi)+radius(lolo,lohi)/2
    principal=[v*c0]+[v/F(2*j*6**j) for j in range(1,NC)]
    ep=vd*(abs(c0)+cd)+abs(v)*cd
    ep+=sum((vd/F(2*j*6**j) for j in range(1,NC)),F(0))
    ep+=(abs(v)+vd)*F(1,6)**NC/(2*NC*(1-F(1,6)))
    assert ep<F(1,10**38),D(ep)
    absp=sum(map(abs,principal),F(0))
    assert absp<F(2,10**10)
    # True normalized left s=(log9-B-XC)/H from EXACT log9 interval.
    # 250 terms suffice: error <1e-45; use a 35-decimal rational
    # endpoint t0 with a separately paid global moment variation.
    lglo,lghi=atanh_2_interval(F(4,5),250)
    tlo=(lglo-B-XC)/H
    thi=(lghi-B-XC)/H
    assert F(-1)<tlo<thi<F(0)
    S=10**35
    t0=F((tlo.numerator*S)//tlo.denominator,S)
    tdelta=thi-t0
    assert F(0)<tdelta<F(1,10**30),D(tdelta)
    # Uniform |d/dt (1-t^(k+1))/((k+1)(1-t))| <=3 for -1<t<0.
    # All 2NC source moments have this rigorous analytic bound.
    momenterr=3*tdelta
    ms=moments(t0,2*NC)
    z2=sum((Z[i]*Z[j]*ms[i+j] for i in range(NC) for j in range(NC)),F(0))
    pz=sum((Z[i]*principal[j]*ms[i+j] for i in range(NC) for j in range(NC)),F(0))
    A0=4*pz+2*z2
    # Functional error from TRUE original z and principal p, plus
    # physical moment-parameter enclosure. |s|<=1.
    Aerr=4*(absp*e_z +absz*ep+e_z*ep) + 2*(2*absz*e_z+e_z*e_z)
    Aerr+=momenterr*(4*absz*absp+2*absz*absz)
    ll=F(1099,500)-lghi
    lh=F(1099,500)-lglo
    assert F(7,10000)<ll<lh<F(1,1000)
    lmid=midpoint(ll,lh);ldelta=radius(ll,lh)
    d0=lmid*A0
    d_err=lh*Aerr+ldelta*abs(A0)
    dL,dU=d0-d_err,d0+d_err
    assert dL>0,("genuine original signed J8 first physical sign fails",D(dL),D(dU))
    assert d_err<F(1,10**37),("original interval decision precision",D(d_err))
    # A source-certifiable signed partial J8 value, not global NF404.
    print("NF482 exact source original first J8 signed D",D(dL),D(dU),flush=True)
    print("NF482 independent exact source signed enclosure error",D(d_err),flush=True)
    print("NF482 remaining original J8 terminal physical strip [549/500,B] OPEN",flush=True)
    scale=10**39
    lower=F((dL.numerator*scale)//dL.denominator,scale)
    upper=F(-((-dU.numerator*scale)//dU.denominator),scale)
    assert lower<=dL<=dU<=upper
    out={
      "pass":"NF482-B",
      "standing":"SOURCE-CERTIFIED original true first J8 irrational n9 entry partial signed D POSITIVE from native 11x full 4096-bit original 273-mode source balls + independent EXACT Fraction moments; NOT full J8",
      "original_nf407_source_sha256":SRC,
      "original_nf406_seams_sha256":SEAM,
      "original_source_native_coefficient_fragments":[{"filename":n,"sha256":s,"part":o["part"]} for n,o,s in records],
      "original_native_bits":4096,
      "original_246_source_generators":True,"original_273_source_groups":True,
      "original_seven_minus_J8_translates":list(PRIMES),
      "original_n9_irrational_support_start":"log9-B",
      "physical_original_J8_source_panel":["log9-B","549/500"],
      "original_true_source_taylor_polynomial_degree":N-1,
      "original_source_retained_for_independent_exact_moments":NC,
      "original_source_tail_remaining_1200_coefficients_upper":str(tail_z),
      "original_native_source_coefficient_rounding_paid":str(rounding),
      "original_true_source_infinite_image_tail":str(eps_image),
      "original_true_source_Cauchy_analytic_remainder":str(eps_taylor),
      "original_true_source_original_input_dyadic_and_prime_error":str(eps_input),
      "original_source_z_uniform_error":str(eps_z),
      "original_exact_principal_v_arb_source_NF411_interval":[str(vlo),str(vhi)],
      "original_principal_C8_original_7_weight_interval":[str(wclo),str(wchi)],
      "original_true_principal_log1375_over3_interval":[str(lolo),str(lohi)],
      "source_principal_polynomial_error_uniform":str(ep),
      "true_normalized_irrational_left_t_original_interval":[str(tlo),str(thi)],
      "true_moment_rational_endpoint_surrogate":str(t0),
      "surrogate_exact_uniform_monomial_moment_error_bound":str(momenterr),
      "original_principal_z_normalized_mean_exact_nominal":str(pz),
      "original_z_squared_normalized_mean_exact_nominal":str(z2),
      "original_true_physical_signed_D_exact_nominal":str(d0),
      "original_TRUE_first_J8_signed_source_exact_interval":[str(dL),str(dU)],
      "original_TRUE_first_J8_signed_source_coarse_decimal_outward":[D(lower),D(upper)],
      "original_TRUE_first_J8_signed_source_strict_sign":"POSITIVE",
      "original_remaining_J8_terminal_physical_interval":["549/500","B"],
      "original_complete_J8_signed_integral_numeric_upper":"OPEN",
      "original_NF404_full_centered_energy_gate":"OPEN",
      "W_ODD_NEG":"OPEN","RH":"OPEN",
      "next_bold":"NF483 original terminal [549/500,B] full 20-source-jet H-principal endpoint source integration"
    }
    dest=Path(arg.output);dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(out,indent=2)+"\n")
if __name__=="__main__":main()
