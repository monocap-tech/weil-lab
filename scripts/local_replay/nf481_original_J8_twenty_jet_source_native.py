#!/usr/bin/env python3
"""NF481: immutable source-original 20-jet high-image all-m resolvent extension.

For m>=M, prove an original-source global bound on the *whole 273-mode*
matched-image amplitude T_m by the CONVERGENT source-resolvent expansion
 T_m = sum_{n=0}^{N-1} mu_n / (m+1/4)^(n+1) + R_N,
 mu_n = U^(n)(B)/2^n,
and a separately PAID analytic geometric remainder. Crucially, mu_n is
source-contracted BEFORE taking absolute values. This avoids the useless
old |T_m|<=4e160/m bound and does not invent a finite "new source."

The mathematical certificate stays valid across the ENTIRE physical J7
including its irrational right endpoint log9-B, provided the exact Fraction
tail checks and original data SHA verification pass.

No whole J7 sign or RH claim follows merely from tail improvement.
"""
from __future__ import annotations
import argparse, json, math, sys
from fractions import Fraction as Q
from pathlib import Path
from decimal import Decimal, localcontext
from flint import arb, acb, ctx
from nf415_original_cell6_I1_validated_acb import native_source, U, A, C
from nf454_original_n9_contact_native_moment import read, enclosure, B, SRC_SHA, SEAM_SHA
import nf471_original_J7_joint_arch_mean_native as parent
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)

N=360
M=18000
BITS=4096
FREQ_UPPER=883
MAX_K=13
SOURCE_NATIVE_PARENT="f50e49cdc02b5e1eaacce7f8a66733fce9bc6f05"
def bound_abs(z,digits=110):
    lo,hi=enclosure(z,digits)
    assert lo<=hi
    return max(abs(lo),abs(hi)),[str(lo),str(hi)]
def rational_log9_upper(K=70):
    """2atanh(4/5); all positive terms plus exact positive tail."""
    t=Q(4,5)
    lo=sum((2*t**(2*j+1)/Q(2*j+1) for j in range(K)),Q(0))
    tail=2*t**(2*K+1)/(Q(2*K+1)*(1-t*t))
    return lo,lo+tail
def exact_resolvent_remainder():
    """The 273-mode source tail bound, including all k<=13 polynomials.

    Original source is U(x)=sum 2Re alpha_(f,k)*x^k exp(2 pi i f x)
                       +pole*sinh(x/2).
    For a=m+1/4>=M, z=lambda/(2a), |z|<=q=(22/7)*883/M<1.
    The inverse (a-lambda/2)^(-j-1) has convergent binomial power
    series. After retaining all total powers n< N, j term contributes
    a^-j-1 *sum_{r>=N-j} binom(r+j,j) z^r.
    The original *midpoint* raw envelope sum |c|B^k+|pole|<1e160.
    All binomial tails here are exact Fractions, not sampled asymptotics.
    """
    q=Q(22*FREQ_UPPER,7*M) # rigorous pi < 22/7
    assert Q(0)<q<Q(1,5)
    rawbound=Q(10)**160
    total=Q(0)
    binomial_tails=[]
    for j in range(MAX_K+1):
        cutoff=N-j
        assert cutoff>0
        full=(1-q)**(-j-1)
        partial=sum((Q(math.comb(r+j,j))*q**r for r in range(cutoff)),Q(0))
        tail=full-partial
        assert tail>0
        # |sum frequency + poly order contribution| <= (rawbound/M)
        # times the max k=13 falling factorial and B^-j/(2M)^j.
        poly=Q(math.factorial(MAX_K),math.factorial(MAX_K-j))/(2*B*M)**j
        total+=rawbound/Q(M)*poly*tail
        binomial_tails.append(tail)
    # Genuine original odd sinh-pole source has exp(+/-t/4);
    # U_p(B+t/2)=pole/2 [exp(B/2)exp(t/4)-exp(-B/2)exp(-t/4)].
    # exp(B/2)<2, so the source-pole remainder is bounded by the
    # ordinary geometric tail of its convergent 1/(a-1/4) expansion.
    pole=Q(2*10**160,M)*(Q(1,4*M)**N)/(1-Q(1,4*M))
    return total+pole,q,binomial_tails
def compute_native_source_resolvent(args):
    original,sha=read(args.source)
    seams,ss=read(args.seams)
    assert (sha,ss)==(SRC_SHA,SEAM_SHA)
    assert original["original_dimension"]==242
    assert len(original["original_exact_native_original_four_critical_coefficients_mid_radius"])==4
    assert len(original["original_source_critical_sine_frequencies"])==32
    ctx.prec=BITS
    terms,pole,s0=native_source(original)
    assert s0<Q(1,10**700)
    assert len(terms)==273 and all(0<f<FREQ_UPPER and k<=MAX_K for f,k,c in terms)
    raw=sum((abs(c)*B**k for f,k,c in terms),abs(pole))
    assert raw<Q(10)**160
    groups={}
    for f,k,c in terms:groups.setdefault(f,[]).append((k,c))
    assert len(groups)==99
    image_groups=parent.image_groups(groups)
    # One shared source-coefficient vector: sum source frequency contributions
    # to each mu_n BEFORE taking abs and bounding for ALL m>=M.
    mu=[arb(0) for _ in range(N)]
    for idx,(lam,coefficients) in enumerate(image_groups,1):
        z=lam/2
        invz=1/z
        invpowers=[acb(1)]
        for j in range(1,MAX_K+1):invpowers.append(invpowers[-1]*invz)
        d=[c*invpowers[j] for j,c in enumerate(coefficients)]
        power=acb(1)
        for n in range(N):
            poly=acb(0)
            for j in range(min(n,MAX_K)+1):
                poly+=d[j]*math.comb(n,j)
            mu[n]+=2*(power*poly).real
            power*=z
        if idx%20==0:
            print("NF481 full original source contracted 1/a jets",idx,"/",len(image_groups),flush=True)
    # Full original pole at all m>=M (no special m0 issue).
    pb=A(pole)
    ep=(A(B)/2).exp()
    em=(-A(B)/2).exp()
    pos=arb(1);neg=arb(1)
    for n in range(N):
        mu[n]+=pb*(ep*pos-em*neg)/2
        pos/=4;neg/=-4
    # Independent true original source endpoint U(B) and first derivative.
    u=U(original)
    vb=u.at(C(A(B))).real
    d0=mu[0]-vb
    dlo,dhi=enclosure(d0,170)
    assert dlo<=0<=dhi and max(abs(dlo),abs(dhi))<Q(1,10**90)
    first=[list(map(str,enclosure(mu[j],105))) for j in range(20)]
    # Remainder is PAID using the pre-contraction raw source envelope, but
    # the first 360 source derivatives have been fully contracted and
    # bounded only after summation -- essential correlation custody.
    remainder,q,tails=exact_resolvent_remainder()
    leading=Q(0)
    maximum_order=-1
    biggest_ratio=Q(0)
    # Both all-rounding and source dyadic uncertainty are added.
    for n,value in enumerate(mu):
        ai,_=bound_abs(value,120)
        term=ai/Q(M)**(n+1)
        leading+=term
        if term>biggest_ratio:biggest_ratio=term;maximum_order=n
        if n%60==0:
            print("NF481 original correlated source jets",n,"/",N,flush=True)
    errinput=Q(5,10**700*M)
    Cbound=leading+remainder+errinput
    # Verify actual original source image at m=M and an independent larger
    # m using the ORIGINAL rational grouped 273-mode amplitude. The
    # source-correlated convergent expansion must overlap the direct formula.
    checks=[]
    for m in (M,2*M):
        a=A(Q(4*m+1,4))
        source_real=arb(0)
        for lam,coeff in image_groups:
            inv=1/(acb(a)-lam/2)
            current=inv
            tot=acb(0)
            for vj in coeff:
                tot+=vj*current
                current*=inv
            source_real+=2*tot.real
        source_real+=pb*(ep/A(m)-em/A(Q(2*m+1,2)))/2
        summ=arb(0);inv=1/a;weight=inv
        for value in mu:
            summ+=value*weight
            weight*=inv
        diff=source_real-summ
        rd,interval=bound_abs(diff,115)
        # The rational remainder at m=M is valid for both tested m>=M.
        assert rd<remainder+Q(1,10**80), (
          "correlation-resolvent direct source identity FAILED",m,str(rd),str(remainder))
        native_sample=bound_abs(source_real,70)[1]
        checks.append({"m":m,"direct_full_original_Tm_outward":native_sample,
                       "correlated_resolvent_agrees_with_direct":True,
                       "raw_difference_bound":str(rd)})
    # Irrational J7 right endpoint: dmin=2B-log9. Prove with exact
    # atanh(4/5) rational series that dmin>11/4000.
    l9lo,l9hi=rational_log9_upper()
    dmin_lower=Q(11,4000)
    assert 2*B-l9hi>dmin_lower
    # Source amplitude bound C for EVERY m>=M with |T_m|<=C.
    # exp(-2 m dmin) <= (3/8)^floor(2 M dmin);
    # geometric denominator 1/(1-exp(-2dmin)) <=1/dmin
    # since 1-exp(-2d)>=d for 0<d<1/2.
    exponent=(Q(2)*M*dmin_lower).numerator//(Q(2)*M*dmin_lower).denominator
    assert exponent==99
    left_image_tail_bound=Cbound/Q(dmin_lower)*Q(3,8)**exponent
    # Each original source point image includes (left-right)/2.
    # Do NOT divide the tail again by 2 for increased safety.
    sign_quality=left_image_tail_bound<Q(1,10**40)
    # A high-tail method-stop is a VALID research result if this fails:
    # no finite signed original J7 point/panel is certified here.
    def number(d):
        with localcontext() as c:
            c.prec=40
            return str(Decimal(d.numerator)/Decimal(d.denominator))
    result={
      "pass":"NF481",
      "original_full_twenty_jets_native_correlation":True,
      "original_parent_NF477_360jet_architecture_unchanged":True,
      "object":"unchanged original 246-source/273-mode NF443 matched two endpoint image amplitude T_m",
      "standing":"source-correlated all-m high-image tail PASS" if sign_quality else "METHOD STOP: post-contraction derivative absolute jets fail high-image tail target",
      "original_nf407_sha256":sha,"original_nf406_sha256":ss,
      "original_native_source_parent":SOURCE_NATIVE_PARENT,
      "original_246_generators":True,"original_273_modes":True,"original_99_frequency_groups":True,
      "original_odd_sinh_pole":True,
      "native_precision_bits":BITS,
      "source_resolvent_lower_m":M,
      "source_resolvent_contracted_order":N,
      "genuine_original_source_input_radius_lt":"1e-700",
      "original_raw_precontraction_envelope_lt":"1e160",
      "exact_resolvent_q_bound":str(q),
      "exact_absolute_binomial_remainder":str(remainder),
      "exact_absolute_binomial_remainder_decimal":number(remainder),
      "post_contraction_original_360_jet_absolute_sum":str(leading),
      "post_contraction_original_360_jet_absolute_sum_decimal":number(leading),
      "source_uniform_all_m_amplitude_bound":str(Cbound),
      "source_uniform_all_m_amplitude_bound_decimal":number(Cbound),
      "largest_jet_contribution_order":maximum_order,
      "original_first_twenty_source_jets_outward":first,
      "direct_original_grouped_Tm_matches_convergent_source_resolvent":checks,
      "original_right_seam_log9_minus_B_rational_upper":[str(l9lo),str(l9hi)],
      "original_true_right_seam_distance_lower":str(dmin_lower),
      "geometric_right_seam_tail_exponent":int(exponent),
      "complete_original_J7_both_right_endpoint_image_tail_bound":str(left_image_tail_bound),
      "complete_original_J7_both_right_endpoint_image_tail_decimal":number(left_image_tail_bound),
      "complete_original_J7_both_right_endpoint_tail_lt_1e_minus_40":sign_quality,
      "source_correlated_infinite_tail_result":"CERTIFIED" if sign_quality else "OPEN",
      "remaining_two_right_original_J7_signed_panels":"OPEN",
      "complete_original_J7":"OPEN","J8":"OPEN","NF404":"OPEN","W_ODD_NEG":"OPEN","RH":"OPEN"
    }
    path=Path(args.output);path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(result,indent=2)+"\n")
    print("NF481 total real original 273-mode T_m amplitude for all m>=18000:",number(Cbound),flush=True)
    print("NF481 geometric whole genuine original J7 high image tail:",number(left_image_tail_bound),flush=True)
    print("NF481 SOURCE CORRELATED HIGH TAIL STATUS",result["standing"],flush=True)
    print("NF481 original two signed right physical panels and whole J7 OPEN",flush=True)
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--source",default="notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json")
    ap.add_argument("--seams",default="notes/data/provisional/NF406_original_prime_support_partition_exact.json")
    ap.add_argument("--output",required=True)
    compute_native_source_resolvent(ap.parse_args())
if __name__=="__main__":main()
