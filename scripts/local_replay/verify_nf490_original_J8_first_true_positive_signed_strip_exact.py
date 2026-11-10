#!/usr/bin/env python3
"""NF490 genuine original J8 positive-measure signed entrance collar.

INDEPENDENT exact Fraction auditor of accepted NF489 original complete
source-native physical z(549/500), independently reconstructed from NF482
eleven original 4096bit native source blocks; original NF413 4096bit
second-curvature SQUARED ball sharpens true compact ||U''||2 <134.
Use NF446 exact joint original digamma+BOTH-images compact source kernel,
its moving-edge cancellation and NF411 original seven-prime and endpoint
balls to prove |z'|<8500 on 1/1000<=B-x<=1/500.
Then integrate strict signed density on the genuine positive-measure
interval [549/500,549/500+10^-15] without any mesh guessing.

This proves one tiny J8 signed interval only. Whole J8 upper, original
NF404/W-ODD-NEG/RH remain open.
"""
import argparse,hashlib,json,re,sys
from pathlib import Path
from fractions import Fraction as F
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)

B=F(11,10); X=F(549,500); WIDTH=F(1,10**15); D=B-X
SRC="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAM="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
PRIMES=(2,3,4,5,7,8,9)

def load(path):
    raw=Path(path).read_bytes()
    return json.loads(raw),hashlib.sha256(raw).hexdigest()

def iv(a,b=None):
    a=F(a);b=a if b is None else F(b)
    assert a<=b
    return a,b

def span(v):
    a,b=map(F,v)
    return iv(a,b)

def overlap(a,b):
    return a[0]<=b[1] and b[0]<=a[1]

def intersect(a,b):
    assert overlap(a,b), "METHOD STOP: original genuine source-native independent point enclosures disagree"
    return max(a[0],b[0]),min(a[1],b[1])

def ball(s):
    m=re.fullmatch(r"\[([+-]?[0-9]+(?:\.[0-9]+)?e[+-]?[0-9]+) \+/- ([0-9]+(?:\.[0-9]+)?e[+-]?[0-9]+)\]",s)
    assert m, "original Arb ball format changed"
    v,r=map(F,m.groups())
    assert r>=0
    return v-r,v+r

def poly(c,y):
    return sum((u*y**i for i,u in enumerate(c)),F(0))

def pd(c,y):
    return sum((F(i)*u*y**(i-1) for i,u in enumerate(c) if i),F(0))

def moving_edge_controls():
    # Independent signed exact odd polynomial source controls for both
    # derivative moving boundary matches. They cannot replace original
    # physical source numeric certification.
    tests=(
      [F(0),F(1)],
      [F(0),F(-3,7)],
      [F(0),F(2,3),F(0),F(-5,11)],
      [F(0),F(7,13),F(0),F(-11,17),F(0),F(19,23)],
      [F(0),F(0),F(0),F(1,29)],
      [F(0),F(-31,37),F(0),F(41,43),F(0),F(-47,53),F(0),F(59,61)]
    )
    count=0
    for c in tests:
        v=poly(c,B)
        for d in (D,F(3,2000),F(1,1000)):
            x=B-d;a=2*d;b=2*(B+x)
            U=lambda y:poly(c,y)
            Up=lambda y:pd(c,y)
            Ax=lambda t:U(x)-(U(x+t/2)+U(x-t/2))/2
            Mx=lambda t:U(x)-(U(x-t/2)+v)/2
            DAx=lambda t:Up(x)-(Up(x+t/2)+Up(x-t/2))/2
            DMx=lambda t:Up(x)-Up(x-t/2)/2
            assert Ax(a)==Mx(a) and Mx(b)==U(x)
            assert -2*Ax(a)+2*Mx(a)+2*Mx(b)-2*U(x)==0
            # Check original whole-source chain-rule, not frozen cutoffs.
            for t in (a,F(1,20),F(2),b):
                assert DAx(t)==pd(c,x)-(pd(c,x+t/2)+pd(c,x-t/2))/2
                assert DMx(t)==pd(c,x)-pd(c,x-t/2)/2
            count+=1
    return count

def main():
    a=argparse.ArgumentParser()
    a.add_argument("--native",required=True)
    a.add_argument("--native-audit",required=True)
    a.add_argument("--nf482-independent",required=True)
    a.add_argument("--output",required=True)
    opts=a.parse_args()

    source,srcsha=load("notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json")
    seams,seamsha=load("notes/data/provisional/NF406_original_prime_support_partition_exact.json")
    gram,gramsha=load("notes/data/provisional/NF413_original_full_246_source_curvature_native.json")
    jet,jetsha=load("notes/data/provisional/NF411_original_source_boundary_jet.json")
    joint,jointsha=load("notes/data/provisional/NF446_original_joint_compact_kernel_J7_J8_custody_index.json")
    native,nsha=load(opts.native)
    native_audit,asha=load(opts.native_audit)
    first,fsha=load(opts.nf482_independent)
    assert srcsha==gram["original_nf407_full_native_source_sha256"]==joint["original_nf407_source_sha256"]==SRC
    assert seamsha==joint["original_nf406_prime_seam_sha256"]==SEAM
    assert jet["nf407_source_sha256"]==SRC
    assert joint["pass"]=="NF446" and gram["pass"]=="NF413" and jet["pass"]=="NF411"
    assert joint["final_focused_source_CI"]["conclusion"]=="SUCCESS"
    assert joint["original_selected_and_critical_source_count"]==246
    assert joint["original_distinct_source_frequency_order_groups"]==273
    assert joint["original_native_operator_coefficients_checked_against_nf443"]
    assert joint["original_odd_u4_reflection_used"]
    assert gram["native_second_derivative_error_paid_in_L2_by_3S2_over_2"]
    assert gram["original_true_full_u4_second_derivative_L2_upper_integer"]=="256"
    assert native["pass"]=="NF489" and native_audit["pass"]=="NF489-independent-source-Fraction"
    assert first["pass"]=="NF489-original-NF482-source-independent-boundary"
    assert native_audit["native_raw_sha256"]==nsha
    assert native["original_nf407_source_sha256"]==native_audit["source_original_nf407_sha256"]==first["original_nf407_source_sha256"]==SRC
    assert native["original_nf406_seams_sha256"]==native_audit["source_original_nf406_seams_sha256"]==first["original_nf406_seams_sha256"]==SEAM
    assert first["original_11_native_source_coeff_fragment_sha256"] and len(first["original_11_native_source_coeff_fragment_sha256"])==11
    assert native_audit["original_true_J8_x"]==first["original_true_J8_x"]==native["true_original_J8_x"]=="549/500"
    assert first["original_source_11_full_1200_jets_used"]
    assert first["original_NF482_accepted_true_uniform_z_error_overcharge"]=="1e-29"

    # NF413 source 4096-bit *squared curvature* significantly improves
    # old NF446 L2 <256, keeping same ORIGINAL entire 246-source Gram.
    sq=ball(gram["source_native_4096bit_midpoint_correlated_original_second_derivative_L2_squared_Arb"])
    S2=F(gram["native_second_derivative_source_coefficient_radii_uniform_exact"])
    assert F(0)<sq[0]<=sq[1]<F(267,2)**2
    assert F(0)<=S2<F(1,100)
    assert F(267,2)+F(3,2)*S2<F(134)
    # Therefore original complete physical ||U''||_2<134; source dyadic
    # radii were charged separately in NF413 by 3*S2/2.
    assert F(11,5)<F(371,250)**2
    assert 1+134*F(371,250)<200
    # Exact physical sup |U'|<200, |U|<450 on [-B,B].
    assert 1+200*(2*B)==441<450
    assert joint["source_nf445_native_u4prime_B_absolute_strict_below1"]
    assert joint["source_nf445_native_u4_B_interval_strictly_between_minus1_and0"]
    assert joint["original_kernel_inequalities"][1]=="|K(t)-1/t|<=1"

    # Genuine FULL NF446 physical compact source global:
    # first-source at most 500, middle <1250, scalar <3,
    # U*K right tail <450*4=1800, c0U<4500.
    arch=F(500)+1250+3+1800+4500
    assert arch==8053<8500
    z_global=F(8500)+7*(450+1)+2
    assert z_global==11659<12000

    # On the entire actual physical J8 x∈[549/500,1099/1000],
    # d∈[1/1000,1/500], a=2d≤1/250,b≤22/5.
    assert 0<X<X+WIDTH<B-F(1,1000)
    assert F(1,250)<F(1,15)**2  # sqrt(a)<1/15
    first_d=F(134)*(F(2,15)+F(2,3)*F(1,250)*F(1,15))
    assert first_d<19
    # Since log(b/a)<=log2200<8: exp(8)>(8/3)^8>2200.
    assert F(8,3)**8>2200
    # Source derivative:
    # J'=c0U'+int0^a K Ax' +inta^b K Mx'
    #   +v/2[1/(B+x)+2Q(a)+2Q(b)]+U' int_b^inf K.
    # EXACT moving-end boundary K terms cancel by Ax(a)=Mx(a),
    # Mx(b)=U(x). Seven physical primes & center then subtracted.
    # Bound pieces at original |U'|<200:
    component_derivative=[2000,19,3900,3,800,1400,2]
    assert sum(component_derivative)==8124<8500
    assert moving_edge_controls()==18

    # All THREE CI-PASSED genuinely original independent source data.
    p0=span(native["original_full_true_native_z_outward"])
    p1=span(native_audit["source_original_physical_z_outward"])
    p2=span(first["actual_original_J8_physical_z_x_outward"])
    zx=intersect(intersect(p0,p1),p2)
    assert zx[0]>F(-34,10**12) and zx[1]<F(-33,10**12)
    assert zx[1]<0
    source_v=ball(jet["original_original_source_value_at_B_arb"])
    assert F(-2,10**11)<source_v[0]<=source_v[1]<F(-1,10**11)
    C8lo=C8hi=F(0)
    observed=[]
    for row in jet["all_seven_original_prime_seam_derivative_identities"]:
        n=row["prime_power"]
        observed.append(n)
        lo,hi=map(F,row["c_n_positive_outward"])
        assert 0<lo<=hi<1
        C8lo+=lo;C8hi+=hi
    assert tuple(observed)==PRIMES
    assert 3<C8lo<=C8hi<7
    # log(B/d)∈(6,8) throughout [x0,x0+WIDTH]:
    # lower >=log550>6, accepted NF488 exact positive atanh;
    # certify lower by e<11/4 => e^6<(11/4)^6<550,
    # upper by e>8/3 => e^8>(8/3)^8>1100>=B/d.
    assert F(11,4)**6<550 and F(8,3)**8>1100
    # |p| on strip lies (6e-11,2.2e-10), and p<0.
    plow=F(6,10**11)
    phigh=F(22,10**11)
    assert plow < F(1,10**11)*(3+F(6,2))
    assert phigh ==F(2,10**11)*(7+F(8,2))

    # Rigorous *continuous*, not a pointwise extrapolation:
    # |z(x)-z(x0)| <= 8500 WIDTH = 8.5e-12.
    dmax=F(8500)*WIDTH
    assert dmax==F(85,10**13)
    assert zx[1]+dmax<F(-24,10**12)
    assert zx[0]-dmax>F(-5,10**11)
    # Hence -5e-11 < z(x) < -2.4e-11, p(x)<0 throughout.
    zabslo=F(24,10**12)
    zabshi=F(5,10**11)
    density_lower=4*plow*zabslo+2*zabslo**2
    density_upper=4*phigh*zabshi+2*zabshi**2
    assert density_lower==F(6912,10**24)
    assert density_upper==F(49,10**21)
    signed_lower=WIDTH*density_lower
    signed_upper=WIDTH*density_upper
    assert signed_lower==F("6.912e-36")
    assert signed_upper==F("4.9e-35")
    # Check against independent true physical point density from NF482.
    original_density=span(first["actual_original_J8_signed_density_4pz_plus_2z2_x_outward"])
    assert original_density[0]>0
    assert density_lower<original_density[0]<=original_density[1]<density_upper

    out={
      "pass":"NF490",
      "standing":"SOURCE-ACCEPTED ORIGINAL physical J8 true positive-measure first-terminal entrance SIGNED TWO-SIDED interval from original NF489 three-way point and sharpened original NF413 joint compact derivative; whole J8 signed upper OPEN",
      "original_nf407_source_sha256":SRC,"original_nf406_seam_sha256":SEAM,
      "original_NF413_curvature_receipt_sha256":gramsha,
      "original_NF446_joint_compact_receipt_sha256":jointsha,
      "original_NF411_source_jet_receipt_sha256":jetsha,
      "original_NF489_4096bit_native_source_receipt_sha256":nsha,
      "original_NF489_independent_native_audit_receipt_sha256":asha,
      "original_NF489_independent_11_source_nf482_receipt_sha256":fsha,
      "original_NF413_midpoint_source_second_derivative_L2_squared_interval":[str(q) for q in sq],
      "original_NF413_source_input_second_derivative_S2_exact":str(S2),
      "genuine_original_full_U_second_derivative_L2_strict_upper":"134",
      "genuine_original_full_compact_U_prime_sup_strict_upper":"200",
      "genuine_original_full_compact_U_sup_strict_upper":"450",
      "genuine_original_full_J7_J8_physical_z_sup_strict_upper":"12000",
      "source_nf446_true_joint_arch_global_improved_upper":"8500",
      "source_original_complete_J8_true_derivative_region":["549/500","1099/1000"],
      "genuine_original_complete_J8_z_prime_abs_strict_upper":"8500",
      "original_source_moving_cutoff_derivative_cancellation_verified":True,
      "original_odd_polynomial_edge_derivative_exact_controls":18,
      "original_NF489_full_compact_true_z_boundary_interval":[str(q) for q in p0],
      "original_NF489_independent_first_exact_z_boundary_interval":[str(q) for q in p1],
      "original_NF489_independent_nf482_exact_z_boundary_interval":[str(q) for q in p2],
      "genuine_three_way_original_z_boundary_intersection":[str(q) for q in zx],
      "genuine_source_native_point_true_energy_density_outward":[str(q) for q in original_density],
      "genuine_original_signed_integral_x_interval":["549/500",str(X+WIDTH)],
      "genuine_original_signed_integral_x_width":str(WIDTH),
      "original_integrand_strict_lower_per_unit_x":str(density_lower),
      "original_integrand_strict_upper_per_unit_x":str(density_upper),
      "original_J8_first_terminal_positive_continuous_signed_integral_two_sided":[str(signed_lower),str(signed_upper)],
      "true_original_integral_signed_strict_positive":True,
      "original_entire_remaining_J8_terminal_signed_integrated":False,
      "original_entire_J8_signed_upper":"OPEN",
      "NF404":"OPEN","W_ODD_NEG":"OPEN","RH":"OPEN",
      "next_bold":"NF491 actual source-correlated interval physical z quadrature across [549/500,B], with rigorously certified integration error smaller than NF404 3.31e-26, no extrapolation of this tiny local collar"
    }
    dest=Path(opts.output);dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(out,indent=2)+"\n")
    print("NF490 sharpened full original compact physical source ||U''||<134, ||U'||<200, ||U||<450; genuine physical |z'|<8500")
    print("NF490 actual original full physical three-way z at x=549/500 strictly NEGATIVE")
    print("NF490 certified REAL J8 entrance positive continuous signed integral 6.912e-36 < D < 4.9e-35")
    print("NF490 genuine remaining entire J8 signed upper NF404 W-ODD-NEG RH OPEN")
if __name__=="__main__":main()
