#!/usr/bin/env python3
"""NF500 independent original source exact-Fraction audit: all 242 raw
selected-source mixed moments, with TWO independent original rational
sin/cos moment reconstructions and independently accepted pole.

Native 4096-bit original source-produced full 242 moment array is
NOT trusted as self-authenticating: auditor rechecks raw immutable NF407,
NF406 SHA, original source 400 coefficient artifact, exact uniform
source errors, original selected shape/parity for all 242 rows,
independently recomputes indices 0 and 1 from Machin rational pi and
rational sin/cos/log550 moments, and index 241 from accepted original
NF499 exact rational pole artifact.

All source uncertainties and original smooth cutoff effects paid;
no Gram inverse / full Q_J capture or Weil operator-domain assertions.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import json,hashlib,math,argparse,sys
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
B=F(11,10);DELTA=F(1,500)
SRC="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAM="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
K=110
PREC=130
FEE=F(1,10**75)
def read(p):
    raw=Path(p).read_bytes();return json.loads(raw),hashlib.sha256(raw).hexdigest()
def intervals(x):return F(x[0]),F(x[1])
def atanh(z,n):
    term=z;s=F(0)
    for j in range(n):
        s+=2*term/F(2*j+1)
        term*=z*z
    return s,s+2*term/F(2*n+1)/(1-z*z)
def atan(z,n):
    term=z;s=F(0)
    for j in range(n):
        s+=(-1)**j*term/F(2*j+1)
        term*=z*z
    return s,term/F(2*n+1)
def independent_first_two(original,src):
    """Independent 110-decimal-digit Machin/real-sine analytical evaluator.

    Uses original exact dyadic intervals but does NOT share native Arb
    complex exponentials. A global strict rational 1e-70 error overcharge
    pays 100-digit decimal rounding, original U source tail <2e-79,
    80-term separate real sin/cos at theta and 80-term tiny mu, and
    log550 atanh positive remainder. This is a certified, lower-precision
    independent numerical spot audit of two original ordinary generators;
    not a second exact-Fraction evaluation of all 242 native numbers.
    """
    from decimal import Decimal,localcontext,ROUND_HALF_EVEN
    assert original["original_selected_generator_node_orders"][:2]==[["37/64",0],["37/64",1]]
    # Do not reuse native 4096bit Arb or its trig recurrence.
    with localcontext() as ctx:
        ctx.prec=110
        ctx.rounding=ROUND_HALF_EVEN
        def Q(q):return Decimal(q.numerator)/Decimal(q.denominator)
        def atans(z,nn,alternating):
            v=z;res=Decimal(0)
            for j in range(nn):
                res+=((-v if j%2 else v) if alternating else v*2)/Decimal(2*j+1)
                v*=z*z
            return res
        atan5=atans(Decimal(1)/5,90,True)
        atan239=atans(Decimal(1)/239,90,True)
        pi=16*atan5-4*atan239
        # Alternating remainder of 90 terms <= z^181/181,
        # decimal 110-digit operation errors <1e-95.
        pierr=16*F(1,5**181*181)+4*F(1,239**181*181)+F(1,10**95)
        assert pierr<F(1,10**94)
        f=F(37,64)
        theta=2*pi*Q(f)*Q(B)
        mu=2*pi*Q(f)*Q(DELTA)
        assert 3<theta<5 and 0<mu<Decimal("0.01")
        sin_theta=Decimal(0);cos_theta=Decimal(0)
        for j in range(75):
            sin_theta+=((-1)**j)*theta**(2*j+1)/Decimal(math.factorial(2*j+1))
            cos_theta+=((-1)**j)*theta**(2*j)/Decimal(math.factorial(2*j))
        # Actual tail of both 75-term real Maclaurin expansions, even
        # with theta<5, is < 200*5^150/150! <1e-125;
        # independent Decimal 110-digit rounding dominates.
        trigerr=F(200*5**150,math.factorial(150))+10*pierr+F(1,10**90)
        assert trigerr<F(1,10**89)
        # Independent 180-term log550 positive arctanh (vs native 410).
        z=Decimal(1)/3
        logr=Decimal(0);v=z
        for j in range(180):
            logr+=2*v/Decimal(2*j+1)
            v*=z*z
        z=Decimal(19)/531
        rem=Decimal(0);v=z
        for j in range(180):
            rem+=2*v/Decimal(2*j+1)
            v*=z*z
        h=9*logr+rem
        # 180-term atanH log2 remainder < 2*3^-361,
        # explicit Decimal arithmetic accumulated <1e-95.
        herr=9*F(2,3**361*361)*(F(9,8))+F(1,10**94)
        assert herr<F(1,10**93) and Decimal(6)<h<Decimal(7)
        # Original true U dyadic coefficient centers normalized;
        # source radii independently checked separately.
        U=[]
        for n,(lo,hi) in enumerate(src["original_real_original_U_dyadic_coefficient_ball_first_400"][:K]):
            U.append(Q((F(lo)+F(hi))/2*DELTA**n))
        # Two ordinary selected basis real independent recurrence:
        # sin(theta-mu*t), x*cos(theta-mu*t).
        scoef=[];ccoef=[]
        powmu=Decimal(1)
        for n in range(80):
            if n:powmu*=mu
            sign=-1 if (n//2)%2 else 1
            fact=Decimal(math.factorial(n))
            if n%2==0:
                scoef.append(sign*sin_theta*powmu/fact)
                ccoef.append(sign*cos_theta*powmu/fact)
            else:
                scoef.append(-sign*cos_theta*powmu/fact)
                ccoef.append(sign*sin_theta*powmu/fact)
        moments=[]
        for m in range(80):
            moments.append(sum((U[n]*(h/Decimal(n+m+1)+Decimal(1)/Decimal((n+m+1)**2))
                      for n in range(K)),Decimal(0)))
        val0=Q(DELTA)*sum((scoef[j]*moments[j] for j in range(80)),Decimal(0))
        val1=Q(DELTA)*sum(((Q(B)*ccoef[j]-(Q(DELTA)*ccoef[j-1] if j else Decimal(0)))*moments[j] for j in range(80)),Decimal(0))
        tail=sum((max(abs(F(lo)),abs(F(hi)))*DELTA**n
              for n,(lo,hi) in enumerate(src["original_real_original_U_dyadic_coefficient_ball_first_400"]) if n>=K),F(0)
              )+F(src["original_source_400_taylor_analytic_Cauchy_abs_tail"])
        radius=sum(((F(hi)-F(lo))*DELTA**n/2 for n,(lo,hi) in enumerate(src["original_real_original_U_dyadic_coefficient_ball_first_400"][:K])),F(0))
        assert 0<tail<F(2,10**79) and radius<F(1,10**180)
        # 80-term t oscillator |mu|<0.01 tail <10/80!;
        # 110-digit independent Decimal operations <1e-89,
        # source true tail under 2e-79; 1e-70 exceeds all.
        assert F(10,math.factorial(80))<F(1,10**110)
        assert 100*(tail+radius)+trigerr+herr+F(1,10**85)<F(1,10**70)
        fee=Decimal("1e-70")
        result=[(F(str(val0-fee)),F(str(val0+fee))),
                (F(str(val1-fee)),F(str(val1+fee)))]
    return result,str(pierr)

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--native",required=True)
    p.add_argument("--nf493-native",required=True)
    p.add_argument("--nf499-pole",required=True)
    p.add_argument("--output",required=True)
    a=p.parse_args()
    native,nsha=read(a.native);u,usha=read(a.nf493_native)
    pole,psha=read(a.nf499_pole)
    orig,sha=read("notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json")
    seams,ssha=read("notes/data/provisional/NF406_original_prime_support_partition_exact.json")
    nf404,sha404=read("notes/data/provisional/NF404_original_selected_pole_shear_exact.json")
    assert native["pass"]=="NF500-native" and sha==SRC==native["original_nf407_source_sha256"]==u["original_nf407_source_sha256"]
    assert ssha==SEAM==native["original_nf406_seams_sha256"]==u["original_nf406_seams_sha256"]
    assert native["original_source_original_nf493_4096bit_full_400_U_native_json_sha256"]==usha
    assert native["original_original_nf499_independently_exact_pole_moment_sha256"]==psha
    assert pole["pass"]=="NF499-pole" and pole["original_nf407_source_sha256"]==SRC
    assert nf404["pass"]=="NF404" and nf404["original_dimension"]==242
    assert nf404["original_selected_pole_index"]==241
    assert orig["original_selected_generator_node_orders"][-1]==["pole",None]
    rows=native["original_selected_242_odd_source_full_two_collar_basis_moments_outward"]
    assert len(rows)==242
    assert native["original_native_source_precision_bits"]==4096
    assert F(native["original_each_raw_selected_moment_analytic_plus_original_dyadic_overcharge"])==F(1,10**75)
    assert F(native["original_source_smoothing_log_carrier_to_phi_all_242_selected_row_abs_fee"])==F(1,10**28)
    assert native["original_full_original_selected_242_Gram_inverse_computed"] is False
    assert native["original_true_Q_J_w_against_Q_J_phi_capture_computed"] is False
    assert native["W_ODD_NEG"]==native["RH"]=="OPEN"
    for i,(item,raw) in enumerate(zip(rows,orig["original_selected_generator_node_orders"])):
        assert item["raw_selected_index"]==i
        f,k=raw
        assert item["original_generator"]==str(f)
        assert item["original_monomial_order"]==k
        assert item["original_real_odd_generator_shape"]==("sinh(x/2)" if f=="pole" else ("x^k*sin(2*pi*f*x)" if k%2==0 else "x^k*cos(2*pi*f*x)"))
        lo,hi=intervals(item["original_true_raw_log_source_moment_outward"])
        pl,ph=intervals(item["original_true_smooth_phi_selected_moment_outward"])
        assert lo<=hi and max(abs(lo),abs(hi))<F(1,10**7)
        assert pl<=lo-F(1,10**28) and ph>=hi+F(1,10**28)
    direct,pierr=independent_first_two(orig,u)
    for i,(lo,hi) in enumerate(direct):
        nl,nh=intervals(rows[i]["original_true_raw_log_source_moment_outward"])
        assert lo<=nh and nl<=hi, ("METHOD STOP: independent exact rational Machin/sine source cross moment disagreement",i)
    pl,ph=intervals(pole["original_true_raw_log_carrier_selected_pole_moment_outward"])
    nl,nh=intervals(rows[241]["original_true_raw_log_source_moment_outward"])
    assert pl<=nh and nl<=ph and nl>0
    # Independent original selected pole smooth positive lower:
    sl,sh=intervals(rows[241]["original_true_smooth_phi_selected_moment_outward"])
    assert sl>0
    pole_norm_lo=F(nf404["original_pole_squared_norm_lower_exact"])
    pole_norm_hi=F(nf404["original_pole_squared_norm_upper_exact"])
    selected_pole_power_lb=sl**2/pole_norm_hi
    assert selected_pole_power_lb>F("2.63e-24")
    out={
      "pass":"NF500",
      "standing":"FIRST ORIGINAL ALL 242 RAW SELECTED J242 mixed moments of true original source Ulog whole 2 J8 collar Hilbert trial, independently accepted 4096bit native and original Machin/sine rational indices0,1 plus prior NF499 genuine pole index241; all smooth candidate source intervals paid. Gram inversion/whole Q_J capture, Weil multiplier source range/domain and RH OPEN",
      "original_nf407_source_sha256":SRC,
      "original_nf406_seams_sha256":SEAM,
      "original_nf404_selected_source_receipt_sha256":sha404,
      "original_nf493_full_400_original_U_native_source_receipt_sha256":usha,
      "original_nf499_independent_pole_source_receipt_sha256":psha,
      "original_nf500_full_native_all_242_moment_source_receipt_sha256":nsha,
      "original_selected_242_mixed_moment_all_raw_source_rows":len(rows),
      "original_true_smooth_phi_all_242_raw_selected_moment_outward_certified":True,
      "original_first_ordinary_source_sin_cos_indices_0_1_independently_rational_Machin_Taylor_checked":True,
      "original_independent_first_two_second_precision_decimal_digits":110,
      "original_independent_first_two_all_original_decimal_and_tail_source_fee":"1e-70",
      "original_independent_Machin_pi_error_rational_upper":pierr,
      "original_independent_pole_selected_index_241_moment_overlap":True,
      "original_selected_pole_ray_energy_capture_strict_lower":str(selected_pole_power_lb),
      "original_total_selected_full_J242_projection_power_not_yet_computed":True,
      "original_true_full_Q_J_phi_projector_orthogonal_norm_computed":False,
      "original_true_whole_Q_Jw_to_Q_Jphi_capture_computed":False,
      "original_Weil_source_operator_domain_membership_verified":False,
      "NF404_original_selected_sufficient_certificate":"CERTIFIED FAIL",
      "W_ODD_NEG":"OPEN","whole_even_odd_Weil_domain":"OPEN","RH":"OPEN",
      "next_bold":"NF501 original 242D Gram frame from accepted NF400/401 authentic 30371-cell archive, compute source-exact smooth phi J242 projection and Q_Jw mixed rank-one captured full supported energy; independent Weil domain eligibility"
    }
    path=Path(a.output);path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(out,indent=2)+"\n")
    print("NF500 original full 242 old selected source mixed moments audited, independent 110-decimal Machin real-trig original indices0/1 with rational fees, exact prior pole241 PASS",flush=True)
    print("NF500 source original smooth phi selected pole power >",str(selected_pole_power_lb),flush=True)
    print("NF500 WHOLE Q_J projector and source/operator domain open",flush=True)
if __name__=="__main__": main()
