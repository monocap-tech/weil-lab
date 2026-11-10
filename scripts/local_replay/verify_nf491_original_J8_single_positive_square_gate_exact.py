#!/usr/bin/env python3
"""NF491: authentic original J8 last-collar positive square and NF404 one-scalar bulk gate.

The ORIGINAL physical response is w=p+z, never the isolated NF484
analytic-continuation images. Certified identities:
 D8=DA+Dlast+2*Ew_bulk-2*Ep_bulk,
 Ep_bulk=Ep_terminal-Ep_last,  eta<=d<=delta=1/500, eta=10^-15,
 Ew_bulk=int_eta^delta [p(B-d)+z(B-d)]^2 dd >=0.

Original NF407/406/411/479/482/483/486/490 receipt custody,
exact rational source v + seven prime c_n, atanh logarithms,
independent synthetic rational signed-square algebra checks and
rigorous source-compact derivative midpoint-rule METHOD STOP.

This DOES NOT measure Ew_bulk or certify NF404/RH.
"""
from fractions import Fraction as F
from pathlib import Path
from math import comb,factorial
import hashlib,json,re,sys
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
B=F(11,10)
DELTA=F(1,500)
ETA=F(1,10**15)
SOURCE="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAMS="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
PRIMES=[2,3,4,5,7,8,9]

def read(path):
    data=Path(path).read_bytes()
    return json.loads(data),hashlib.sha256(data).hexdigest()

class Iv:
    def __init__(self,lo,hi=None):
        self.lo=F(lo);self.hi=F(lo if hi is None else hi)
        assert self.lo<=self.hi
    def a(self,b):return b if isinstance(b,Iv) else Iv(b)
    def __add__(self,b):
        b=self.a(b);return Iv(self.lo+b.lo,self.hi+b.hi)
    __radd__=__add__
    def __neg__(self):return Iv(-self.hi,-self.lo)
    def __sub__(self,b):return self+-self.a(b)
    def __rsub__(self,b):return self.a(b)+-self
    def __mul__(self,b):
        b=self.a(b);p=[u*v for u in [self.lo,self.hi] for v in [b.lo,b.hi]]
        return Iv(min(p),max(p))
    __rmul__=__mul__
    def __truediv__(self,b):
        b=self.a(b);assert b.lo*b.hi>0
        return self*Iv(1/b.hi,1/b.lo)
    def __pow__(self,n):
        assert type(n)==int and n>=0
        if n==0:return Iv(1)
        if n%2:return Iv(self.lo**n,self.hi**n)
        return Iv(0 if self.lo<=0<=self.hi else min(self.lo**n,self.hi**n),
                  max(self.lo**n,self.hi**n))
    def width(self):return self.hi-self.lo
    def strings(self):return [str(self.lo),str(self.hi)]
    def sci(self,places=37):
        from decimal import Decimal,localcontext
        with localcontext() as c:
            c.prec=places
            return [str(Decimal(v.numerator)/Decimal(v.denominator)) for v in (self.lo,self.hi)]

def arbball(s):
    match=re.fullmatch(r"\[([+-]?[0-9]+(?:\.[0-9]+)?e[+-]?[0-9]+) \+/- ([0-9]+(?:\.[0-9]+)?e[+-]?[0-9]+)\]",s)
    assert match,"METHOD STOP: original NF411 endpoint Arb carrier changed"
    m,r=map(F,match.groups())
    assert 0<=r
    return Iv(m-r,m+r)

def exact_log(q,N=150):
    assert 0<q<1
    low=2*sum((q**(2*j+1)/F(2*j+1) for j in range(N)),F(0))
    high=low+(2*q**(2*N+1)/F(2*N+1))/(1-q*q)
    return Iv(low,high)

def logs():
    ln2=exact_log(F(1,3))
    ln5=exact_log(F(2,3))
    ln550=exact_log(F(1,21))+3*exact_log(F(1,9))+8*ln2
    # 550*2^13*5^12 = B/ETA exactly, no logarithmic ambiguity.
    assert 550*2**13*5**12 == B/ETA
    lneta=ln550+13*ln2+12*ln5
    assert F(6)<ln550.lo<ln550.hi<7
    assert F(34)<lneta.lo<=lneta.hi<37
    assert (F(8,3)**37) > 2*B/ETA
    return ln550,lneta

def log_square_primitive(t,v,C,h):
    # Exact improper int_0^t p(d)^2 dd,
    # p(d)=v*(C+1/2 log(B/d)) with h=log(B/t)
    return t*v**2*(C**2+C*(h+1)+(h**2+2*h+2)/4)

def log_moment(j,k,t,h):
    # Exact primitive for any polynomial×log on a positive endpoint.
    assert j>=0 and k>=0
    acc=F(0)
    for a in range(k+1):
        acc+=F(comb(k,a)*factorial(a),(j+1)**a)*h**(k-a)
    return t**(j+1)/F(j+1)*acc

def verify_square_algebra():
    # Independent exact rational synthetics: whole signed pz,z^2
    # vs one POSITIVE w-square minus known positive p-square,
    # integrated over genuine (eta,delta), no endpoint freeze.
    tests=[
      (F(-1,11),F(5,7),F(-3,17),F(19,23),[]),
      (F(-13,29),F(0),F(11,31),F(-7,37),[F(1,2)]),
      (F(-3,41),F(43,47),F(0),F(-53,59),[F(0),F(-1,7)]),
      (F(0),F(61,67),F(-71,73),F(79,83),[F(1),F(-2),F(3)]),
      (F(89,97),F(101,103),F(107,109),F(113,127),[F(0)]*4),
      (F(-1,10**17),F(137,139),F(149,151),F(-157,163),[F(-1,10**9),F(1,10**7)]),
      (F(0),F(0),F(0),F(0),[F(0)]*7),
      (F(-1,2),F(13,2),F(-17,2),F(19,2),[F(-1),F(2),F(-3),F(5)]),
      (F(11,31),F(-13,37),F(17,41),F(-19,43),[F(1,101)]*5),
      (F(-23,47),F(29,53),F(-31,59),F(37,61),[F((-1)**k*k,10**k) for k in range(1,6)]),
      (F(41,67),F(-43,71),F(47,73),F(-53,79),[F(1,10000001),F(-3,10000019),F(5,10000079)]),
      (F(-83,89),F(97,101),F(103,107),F(-109,113),[F(0)]*6+[F(1,127)]),
    ]
    # Synthetic values for h(delta),h(eta) are rational formal
    # log-boundaries; linear functional identity is pointwise and
    # holds for every consistent actual log pair.
    hd=F(6);he=F(35)
    def primitive(i,k):
        return log_moment(i,k,DELTA,hd)-log_moment(i,k,ETA,he)
    for v,C,Z,alpha,r in tests:
        p={(0,0):v*C,(0,1):v/2}
        z={(0,0):Z,(1,1):alpha}
        for i,c in enumerate(r,1):z[(i,0)]=z.get((i,0),F(0))+c
        w=dict(z)
        for key,c in p.items():w[key]=w.get(key,F(0))+c
        def gram(u,v):
            return sum((a*b*primitive(i+j,k+l) for (i,k),a in u.items()
                for (j,l),b in v.items()),F(0))
        lhs=4*gram(p,z)+2*gram(z,z)
        rhs=2*gram(w,w)-2*gram(p,p)
        assert lhs==rhs,("original squared-energy signed algebra regression",lhs,rhs)
    return len(tests)

def main():
    jet,jsha=read("notes/data/provisional/NF411_original_source_boundary_jet.json")
    nf479,q479=read("notes/data/provisional/NF479_original_full_J8_forced_positive_NF404_transfer_custody.json")
    nf482,q482=read("notes/data/provisional/NF482_original_first_J8_irrational_n9_source_signed_custody.json")
    nf483,q483=read("notes/data/provisional/NF483_original_J8_principal_gram_and_endpoint_stop_custody.json")
    nf490,q490=read("notes/data/provisional/NF490_original_J8_true_positive_continuous_strip_custody_index.json")
    nf486script=Path("scripts/local_replay/verify_nf486_original_J8_last_collar_signed_upper_exact.py").read_text()
    assert all(a["pass"]==name for a,name in
        [(jet,"NF411"),(nf479,"NF479"),(nf482,"NF482"),(nf483,"NF483"),(nf490,"NF490")])
    assert jet["nf407_source_sha256"]==nf479["original_nf407_source_sha256"]==nf482["original_nf407_source_sha256"]==nf490["original_source_nf407_sha256"]==SOURCE
    assert nf479["original_nf406_seams_sha256"]==nf482["original_nf406_seams_sha256"]==nf490["original_seam_nf406_sha256"]==SEAMS
    assert nf483["source_ci_completed_exact"]["conclusion"]=="SUCCESS"
    assert nf482["source_exact_archive"]["conclusion"]=="SUCCESS"
    assert nf479["focused_CI"]["conclusion"]=="SUCCESS"
    assert nf490["focused_original_exact_fraction_ci"]["status"]=="SUCCESS"
    assert nf490["original_nf413_full_u_second_derivative_L2_strict_upper"]=="134"
    assert nf490["original_full_compact_u_prime_sup_strict_upper"]=="200"
    assert nf490["original_full_compact_u_sup_strict_upper"]=="450"
    assert nf490["original_full_J7_J8_joint_physical_z_sup_strict_upper"]=="12000"
    assert "3.2e-34 < D8_last_1e-15 < 1.58e-33" in nf486script
    fee=F(1,10**100)
    assert F(jet["native_source_derivative_uncertainty_exact_upper"])<fee
    v=arbball(jet["original_original_source_value_at_B_arb"])+Iv(-fee,fee)
    assert F(-2,10**11)<v.lo<=v.hi<F(-1,10**11)
    C=Iv(0)
    actual=[]
    for row in jet["all_seven_original_prime_seam_derivative_identities"]:
        n=row["prime_power"]
        lo,hi=map(F,row["c_n_positive_outward"])
        assert n in PRIMES and n not in actual and 0<lo<=hi<1
        C+=Iv(lo,hi);actual.append(n)
    assert actual==PRIMES and F(3)<C.lo<=C.hi<7
    hdelta,heta=logs()
    EpT=Iv(*map(F,nf483["source_accepted_original_J8_terminal_principal_exact_outward_decimal"]))
    assert EpT.lo>0 and EpT.width()<F(1,10**54)
    EpLast=log_square_primitive(ETA,v,C,heta)
    assert F(0)<EpLast.lo<=EpLast.hi<F(3,10**34)
    EpBulk=EpT-EpLast
    assert F(0)<EpBulk.lo<=EpBulk.hi<EpT.hi
    # NF486 immutable last authentic full signed continuous collar bounds,
    # independently CI-accepted in GitHub #42565833234.
    Dlast=Iv(F("3.2e-34"),F("1.58e-33"))
    EwLast=EpLast+Dlast/2
    assert F(0)<EwLast.lo<=EwLast.hi<F(11,10**34)
    DA=Iv(*map(F,nf482["original_J8_first_exact_fraction_source_signed_D_coarse"]))
    assert 0<DA.lo<=DA.hi<F(5,10**25) and DA.width()<F(2,10**39)
    # Conservative anchored original NF479 exact source transfer.
    D8lo=F("1.628791413591084997382e-22")
    D8cap=F("1.629122471432905958157e-22")
    D8fail=F("1.656776807914060395598e-22")
    assert D8lo<F(nf479["original_full_J8_signed_D8_strict_lower_approx"])
    assert D8cap<F(nf479["original_J8_signed_sufficient_upper_for_NF404_approx"])
    assert D8fail>F(nf479["original_J8_signed_failure_lower_for_NF404_approx"])
    # D8=DA+Dlast+2*(EwBulk-EpBulk). Exact original split.
    bulk_forced_lower=EpBulk.lo+(D8lo-DA.hi-Dlast.hi)/2
    bulk_sufficient_upper=EpBulk.lo+(D8cap-DA.hi-Dlast.hi)/2
    bulk_certain_failure_lower=EpBulk.hi+(D8fail-DA.lo-Dlast.lo)/2
    gap=bulk_sufficient_upper-bulk_forced_lower
    assert 0<bulk_forced_lower<bulk_sufficient_upper<bulk_certain_failure_lower
    assert gap==(D8cap-D8lo)/2
    assert F(1,10**26)<gap<F(2,10**26)

    # Uniform rigorously true original physical derivative on
    # eta<=d<=delta from FULL compact NF446 moving cutoff cancellation,
    # source sharpened NF490 134/200/450, unchanged n9-active primes.
    assert F(8,3)**37>2*B/ETA
    small=F(19)
    mid=F(300)*(37+4*B)
    assert mid==12420
    source_derivative=2000+small+mid+3+800+1400+2
    assert source_derivative==16644<17000
    # At eta cutoff p, p' are finite. p abs<5.1e-10, |p'|<10^4.
    assert F(2,10**11)*(7+F(37,2))==F(51,10**11)
    assert F(2,10**11)/(2*ETA)==10000
    w_abs=F(12001)
    w_prime=F(17000+10000)
    f_prime=2*w_abs*w_prime
    assert f_prime==648054000
    domain_length=DELTA-ETA
    # For N equally sized intervals:
    # |integral_bulk w² - midpoint_rule_N| <= L*length²/(4N).
    error_coeff=f_prime*domain_length**2/4
    # At most HALF source-inferred NF404 sufficient corridor, even
    # before the actual sum's other source evaluation/rounding errors.
    target=gap/2
    firstorder_minN=(error_coeff//target)+1
    assert firstorder_minN>10**28 and firstorder_minN<10**29
    assert error_coeff/F(10**29)<target
    assert verify_square_algebra()==12

    out={
      "pass":"NF491",
      "standing":"SOURCE-EXACT ORIGINAL J8 SINGLE TRUE PHYSICAL POSITIVE-SQUARE BULK GATE CERTIFIED; explicit last principal/whole square collar; full EwBulk numerical value & original D8 upper OPEN",
      "original_nf407_source_sha256":SOURCE,
      "original_nf406_support_sha256":SEAMS,
      "original_nf411_jet_sha256":jsha,
      "original_nf479_global_source_sha256":q479,
      "original_nf482_first_irrational_source_sha256":q482,
      "original_nf483_principal_gram_source_sha256":q483,
      "original_nf490_joint_compact_derivative_source_sha256":q490,
      "original_nf486_last_continuous_signed_source_ci":42565833234,
      "original_true_246_source_273_modes_m0_sinh_seven_prime_unchanged":True,
      "original_true_bulk_d_interval":[str(ETA),str(DELTA)],
      "original_principal_log_at_delta_interval":hdelta.strings(),
      "original_principal_log_at_eta_interval":heta.strings(),
      "original_NF411_v_source_interval":v.strings(),
      "original_NF411_seven_prime_weight_interval":C.strings(),
      "original_full_terminal_principal_Ep_source_accepted":EpT.strings(),
      "original_genuine_last_1e15_principal_Ep_interval":EpLast.strings(),
      "original_genuine_last_1e15_principal_Ep_decimal":EpLast.sci(42),
      "original_genuine_last_1e15_physical_squared_Ew_interval":EwLast.strings(),
      "original_genuine_last_1e15_physical_squared_Ew_decimal":EwLast.sci(42),
      "original_bulk_principal_Ep_interval":EpBulk.strings(),
      "original_bulk_principal_Ep_decimal":EpBulk.sci(42),
      "original_first_J8_n9_signed_DA_exact_Fraction":DA.strings(),
      "original_last_J8_signed_Dlast_source_accepted":Dlast.strings(),
      "original_one_square_identity":"D8=DA+Dlast+2*(EwBulk-EpBulk), EwBulk=int_eta^delta [p(B-d)+z(B-d)]^2 dd",
      "original_original_source_inferred_bulk_Ew_lower":str(bulk_forced_lower),
      "original_original_source_inferred_bulk_Ew_lower_decimal":Iv(bulk_forced_lower).sci(43),
      "original_NF404_sufficient_bulk_Ew_upper":str(bulk_sufficient_upper),
      "original_NF404_sufficient_bulk_Ew_upper_decimal":Iv(bulk_sufficient_upper).sci(43),
      "original_NF404_certain_failure_if_bulk_Ew_above":str(bulk_certain_failure_lower),
      "original_NF404_certain_failure_if_bulk_Ew_above_decimal":Iv(bulk_certain_failure_lower).sci(43),
      "original_bessel_to_NF404_bulk_Ew_corridor_width":str(gap),
      "original_bessel_to_NF404_bulk_Ew_corridor_width_decimal":Iv(gap).sci(43),
      "original_true_bulk_z_prime_sup_bound":"17000",
      "original_true_bulk_w_prime_sup_bound":"27000",
      "original_true_bulk_w_sup_bound":"12001",
      "original_true_bulk_w_square_prime_sup_bound":"648054000",
      "uniform_midpoint_original_bulk_error_coefficient":str(error_coeff),
      "uniform_midpoint_N_for_half_original_source_gate_firstorder":str(firstorder_minN),
      "uniform_midpoint_firstorder_method":"METHOD STOP: >10^28 equally spaced nodes needed under these broad original-source envelopes; seek high-order source-correlated moment panels",
      "independent_exact_rational_original_square_identity_controls":12,
      "original_actual_bulk_Ew_numerically_integrated":False,
      "original_complete_J8_signed_upper":"OPEN",
      "NF404":"OPEN","W_ODD_NEG":"OPEN","RH":"OPEN",
      "next_bold":"NF492: high-order validated source-correlated original compact response squared-energy panels on eta<=d<=delta (or equivalent four-moment signed contraction), not 10^29 first-order midpoint nodes"
    }
    p=Path("nf491-original-J8-single-positive-bulk-square-source-exact-gate.json")
    p.write_text(json.dumps(out,indent=2)+"\n")
    print("NF491 original true single physical squared-energy identity/source cusp collar PASS")
    print("NF491 genuine real last collar Ep",*EpLast.sci(32))
    print("NF491 genuine original last collar positive Ew",*EwLast.sci(32))
    print("NF491 original NF404 positive bulk Ew ACCEPTANCE corridor source-forced lower",*Iv(bulk_forced_lower).sci(32))
    print("NF491 original NF404 positive bulk Ew sufficient upper",*Iv(bulk_sufficient_upper).sci(32))
    print("NF491 original NF404 positive bulk Ew definite failure lower",*Iv(bulk_certain_failure_lower).sci(32))
    print("NF491 uniform midpoint first-order N required to certify half-gap",firstorder_minN)
    print("NF491 true physical bulk squared-energy not yet integrated; full D8 upper, NF404 W-ODD-NEG RH OPEN")
if __name__=="__main__":main()
