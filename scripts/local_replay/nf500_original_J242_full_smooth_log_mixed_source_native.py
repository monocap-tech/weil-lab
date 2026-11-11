#!/usr/bin/env python3
"""NF500 genuine 242 original selected-source basis cross-moments with log collar.

These are ACTUAL original complete-source native 4096-bit numerical
integrals <j_i,ell_U> on the whole two physical odd J8 collars,
where ell_U=sgn(x)1_{B-delta<|x|<B}U(|x|)/2 log(B/(B-|x|)).
The source is immutable NF407 original 242 selected + four critical
full coefficients / 273 grouped modes/32 sine/o-sinh, unchanged
NF406 seven physical seams; the original U Taylor balls come from
the archived independently accepted NF493 TRUE 4096bit source artifact.

The OLD selected basis is exactly raw
  j_(f,k)(x) = x^k*sin(2*pi*f*x) if k even,
             = x^k*cos(2*pi*f*x) if k odd,
  j_241(x)=sinh(x/2).
No j_i basis is refitted, no new Weil source is assumed.

All ordinary 241 original moments use independent direct 4096-bit
Arb/Acb frequency/order Taylor about ORIGINAL x=B with n<220 on
t=d/delta, and exact analytic moments
 int_0^1 t^j log(B/(delta*t))dt=h/(j+1)+1/(j+1)^2.
Source all 400 U balls normalized before contraction, exact raw
dyadic input tails paid, and original oscillatory basis omitted
Taylor remainder <1e-175. Each true <j_i,ell> interval is widened
by source/series fee 1e-75, and <j_i,phi_eps> additionally by
10*eps_smooth_L2<1e-28, since original ||j_i||_L2(I)<10.

Original pole j_241 is independently double-calculated via the exact
Fraction original NF499 pole moment; overlap required by second audit.

These 242 actual raw selected mixed moments are NOT sufficient by
themselves to evaluate <Q_Jw,Q_Jphi> or ||Q_Jphi||^2. Need original
Gram inverse plus accepted original w full 242 selected column, and
proper source-to-multiplier operator range/domain.
"""
from __future__ import annotations
import argparse,hashlib,json,math,sys
from pathlib import Path
from fractions import Fraction as F
from flint import arb,acb,ctx

if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
SRC="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAM="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
B=F(11,10);DELTA=F(1,500)
PREC=4096
K=110
D=220
SOURCE_FEE=F(1,10**75)
SMOOTH_FEE=F(1,10**28)

def A(x):
    if isinstance(x,arb):return x
    if isinstance(x,F):return arb(x.numerator)/arb(x.denominator)
    return arb(x)
def C(x):return acb(A(x))
def midrad(x,n=220):
    m,r,e=x.mid_rad_10exp(n)
    t=F(10)**int(e)
    return F(int(m)-int(r))*t,F(int(m)+int(r))*t
def read(p):
    b=Path(p).read_bytes();return json.loads(b),hashlib.sha256(b).hexdigest()
def logpositive(z,n=410):
    assert F(0)<z<1
    p=z;lo=F(0)
    for j in range(n):
        lo+=2*p/F(2*j+1);p*=z*z
    return lo,lo+2*p/F(2*n+1)/(1-z*z)

def hyperpole_coeffs(d):
    Y=A(B)/2; Dlt=A(d)
    s=Y.sinh();c=Y.cosh()
    ans=[]
    fact=1
    for n in range(D+14):
        if n:fact*=n
        ans.append((s if n%2==0 else c)*((-Dlt/2)**n)/fact)
    return ans
def selected_ordinary_coeffs(f,k):
    assert F(0)<f<883 and 0<=k<=13
    iw=acb(arb(0),2*arb.pi()*A(f))
    phase=(iw*A(B)).exp()
    z=-iw*A(DELTA)
    es=[acb(1)]
    for n in range(1,D):
        es.append(es[-1]*z/n)
    pc=[A(math.comb(k,j))*A(B)**(k-j)*((-A(DELTA))**j) for j in range(k+1)]
    out=[]
    for n in range(D+k):
        v=acb(0)
        for j in range(max(0,n-D+1),min(k,n)+1):
            v+=pc[j]*es[n-j]
        t=phase*v
        out.append(t.imag if k%2==0 else t.real)
    return out

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--nf493-native",required=True)
    ap.add_argument("--nf499-pole",required=True)
    ap.add_argument("--output",required=True)
    opt=ap.parse_args()
    ctx.prec=PREC
    orig,sha=read("notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json")
    seams,s_sha=read("notes/data/provisional/NF406_original_prime_support_partition_exact.json")
    src,nsha=read(opt.nf493_native)
    source_pole,psha=read(opt.nf499_pole)
    assert sha==SRC and s_sha==SEAM
    assert src["pass"]=="NF493-original-source-400-log-jets"
    assert source_pole["pass"]=="NF499-pole" and source_pole["original_nf407_source_sha256"]==SRC
    assert src["original_nf407_source_sha256"]==SRC
    assert src["original_nf406_seams_sha256"]==SEAM
    assert src["original_native_precision_bits"]==PREC
    assert src["original_true_log_source_coefficient"]=="U(B-d)/2"
    assert src["original_source_log_u_taylor_degree"]=="399"
    assert len(src["original_real_original_U_dyadic_coefficient_ball_first_400"])==400
    assert orig["original_dimension"]==242
    assert len(orig["original_exact_native_original_four_critical_coefficients_mid_radius"])==4
    assert len(orig["original_source_critical_sine_frequencies"])==32
    rows=orig["original_selected_generator_node_orders"]
    assert len(rows)==242 and rows[241]==["pole",None]
    assert all((f=="pole" and k is None) or
      (f!="pole" and 0<F(f)<883 and type(k)==int and 0<=k<=13)
      for f,k in rows)

    # True complete original 400 source normalized in t=d/delta.
    xs=src["original_real_original_U_dyadic_coefficient_ball_first_400"]
    l1=F(0);tail=F(src["original_source_400_taylor_analytic_Cauchy_abs_tail"])
    a=[]
    for j,(lo,hi) in enumerate(xs):
        lo,hi=F(lo)*DELTA**j,F(hi)*DELTA**j
        assert lo<=hi
        v=max(abs(lo),abs(hi))
        l1+=v
        if j<K:
            a.append(A((lo+hi)/2))
        else:
            tail+=v
    assert F(0)<l1+F(src["original_source_400_taylor_analytic_Cauchy_abs_tail"])<F(2,10**7)
    assert tail<F(2,10**79)
    # This small overcharge pays all original kept coefficient source
    # outward interval radii even if native flint centers round.
    retained_source_radii=sum(
        ((F(hi)-F(lo))*DELTA**j/2 for j,(lo,hi) in enumerate(xs[:K])),
        F(0))
    assert retained_source_radii<F(1,10**180)
    assert F(0)<SOURCE_FEE
    assert 100*(tail+retained_source_radii)<SOURCE_FEE/F(4)

    # Original f up to 883, on x=B-delta*t:
    # |omega*delta|<12, |(B-delta*t)^k|<(3/2)^13<200,
    # exp(12)<10^6. Full basis tail beyond D terms strictly
    # <200*10^6*12^D/D! <1e-175 for every one of 241 rows.
    basis_tail=F(200*10**6*12**D,math.factorial(D))
    assert basis_tail<F(1,10**175)
    assert F(3,2)**13<200
    assert F(11,4)**12<F(10**6)
    assert 2*F(22,7)*883*DELTA<12
    # For D-limited exp times degree-k real monomial polynomial,
    # last retained degree =D-1+k; remainder bound unchanged
    # by a <=200 polynomial absolute bound on |t|<=1.
    assert basis_tail*F(2,10**7)/F(40)<SOURCE_FEE/F(4)

    # Entire original log550 exact rational atanh; no free midpoint.
    low2,hi2=logpositive(F(1,3))
    lowr,hir=logpositive(F(19,531))
    hlo,hhi=9*low2+lowr,9*hi2+hir
    assert F(6)<hlo<hhi<7 and hhi-hlo<F(1,10**375)
    h=A((hlo+hhi)/2)
    assert (hhi-hlo)*F(2,10**7)<SOURCE_FEE/F(4)

    # Real source log moments of U(B-delta*t) BEFORE any selected basis
    # projection. Contraction is complete over genuine NF407 coefficients.
    moments=[]
    for j in range(D+14):
        x=arb(0)
        for n in range(K):
            q=F(n+j+1)
            x+=a[n]*(h/A(q)+A(1/q**2))
        moments.append(x)

    values=[]
    for idx,(f,k) in enumerate(rows):
        cs=(hyperpole_coeffs(DELTA) if f=="pole" else selected_ordinary_coeffs(F(f),k))
        assert len(cs)>=D
        m=arb(0)
        for j in range(len(cs)):
            m+=cs[j]*moments[j]
        m*=A(DELTA)
        lo,hi=midrad(m,220)
        # Source input dyadic radii + U remainder + oscillator
        # Taylor series + independent exact log positive interval.
        lo-=SOURCE_FEE;hi+=SOURCE_FEE
        assert lo<hi
        assert max(abs(lo),abs(hi))<F(1,10**7)
        values.append({
            "raw_selected_index":idx,
            "original_generator":(str(f) if f!="pole" else "pole"),
            "original_monomial_order":k,
            "original_real_odd_generator_shape":("sinh(x/2)" if f=="pole" else ("x^k*sin(2*pi*f*x)" if k%2==0 else "x^k*cos(2*pi*f*x)")),
            "original_true_raw_log_source_moment_outward":[str(lo),str(hi)],
            "original_true_smooth_phi_selected_moment_outward":[str(lo-SMOOTH_FEE),str(hi+SMOOTH_FEE)]
        })
        if (idx+1)%40==0:
            print("NF500 source original 4096bit all-242 selected mixed J8 log moments",idx+1,"/242",flush=True)
    assert len(values)==242
    # The prior NF499 exact rational pole moment was independently
    # accepted; this anchored same ORIGINAL 4096-bit source-checks
    # no accidental half-collar or wrong parity.
    pole_lo,pole_hi=map(F,values[241]["original_true_raw_log_source_moment_outward"])
    prior_pole_lo,prior_pole_hi=map(F,source_pole["original_true_raw_log_carrier_selected_pole_moment_outward"])
    assert pole_lo<=prior_pole_hi and prior_pole_lo<=pole_hi, "METHOD STOP NF500 complete original selected pole disagrees with independently accepted NF499 exact Fraction moment"
    assert F("7.88476182953535359929e-13")<prior_pole_lo<=prior_pole_hi<F("7.88476182953535359931e-13")
    assert pole_hi-pole_lo<F(1,10**70)
    assert pole_lo>F(0)
    phi_lo,phi_hi=map(F,values[241]["original_true_smooth_phi_selected_moment_outward"])
    assert phi_lo>0
    result={
       "pass":"NF500-native",
       "standing":"TRUE ORIGINAL NF407/406 COMPLETE ALL 242 SELECTED BASIS VS ACTUAL SOURCE 2-COLLAR LOG CARRIER SOURCE-NATIVE 4096bit MOMENTS; smoothing paid per original selected row; Gram inverse full Q_J w capture and authentic Weil source/graph domain STILL OPEN",
       "original_nf407_source_sha256":SRC,
       "original_nf406_seams_sha256":SEAM,
       "original_source_original_nf493_4096bit_full_400_U_native_json_sha256":nsha,
       "original_original_nf499_independently_exact_pole_moment_sha256":psha,
       "original_selected_basis_242_raw_index_order":rows,
       "original_selected_242_odd_source_full_two_collar_basis_moments_outward":values,
       "original_source_accepted_raw_400_U_normalized_l1_upper":str(l1),
       "original_source_accepted_110_to_400_plus_infinite_analytic_U_l1_tail":str(tail),
       "original_retained_source_110_dyadic_native_input_radii_total":str(retained_source_radii),
       "original_selected_oscillator_220_term_all_241_source_remainder_each_lt":str(basis_tail),
       "original_exact_log550_rational_positive_atanh_410term_interval":[str(hlo),str(hhi)],
       "original_each_raw_selected_moment_analytic_plus_original_dyadic_overcharge":str(SOURCE_FEE),
       "original_source_smoothing_log_carrier_to_phi_all_242_selected_row_abs_fee":str(SMOOTH_FEE),
       "original_native_source_precision_bits":PREC,
       "original_actual_source_original_true_sinh_pole_index":241,
       "original_selected_pole_source_anchored_NF499_original_true_interval":[str(prior_pole_lo),str(prior_pole_hi)],
       "original_242_selected_mixed_moments_computed":True,
       "original_full_original_selected_242_Gram_inverse_computed":False,
       "original_full_P_J_phi_power_computed":False,
       "original_true_Q_J_w_against_Q_J_phi_capture_computed":False,
       "original_smooth_source_multiplier_range_domain_eligible_verified":False,
       "NF404_fixed_selected_certificate":"CERTIFIED FAIL (NF495-NF497)",
       "W_ODD_NEG":"OPEN","whole_even_odd_Weil_domain":"OPEN","RH":"OPEN",
       "next_bold":"NF501 use archived genuine original 242D Gram frame / NF401 old original 242D w column to calculate Q_Jphi and entire actual Q_Jw capture; independently establish graph/source-domain eligibility"
    }
    p=Path(opt.output);p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(result,indent=2)+"\n")
    print("NF500 ALL 242 original raw selected log moments SOURCE NATIVE 4096bit completed, original independent pole anchor verified",flush=True)
    print("NF500 original smooth selected phi 242 moments outward fee 1e-28 each; full Q_J projector/Weil eligibility OPEN",flush=True)
if __name__=="__main__":
    main()
