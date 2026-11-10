#!/usr/bin/env python3
"""NF489 independent exact-Fraction source custody for original compact pilot.

Read native real physical z(549/500), re-verify source SHA, original NF411,
NF413/NF446/NF451 support and bounds, exact Cauchy+all-m Laplace tails,
two native independent truncations and real boundary identities.
No native source number may be promoted unless all gates pass.
"""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib,argparse,math,sys
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
B=F(11,10);D=F(1,500);X=B-D;H=F(1,10);RAD=F(2,5)
SRC="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAM="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
def read(path):
    s=Path(path).read_bytes()
    return json.loads(s),hashlib.sha256(s).hexdigest()
def iv(v):
    a,b=map(F,v);assert a<=b
    return a,b
def overlap(a,b):
    return a[0]<=b[1] and b[0]<=a[1]
def groups_identities():
    # Actual U is odd. These use six independent EXACT odd-polynomial
    # toy carriers to test true compact source matching, not substitute
    # original NF407 source numerical balls.
    count=0
    for c in [[F(0),F(1)], [F(0),F(-3,7)],
              [F(0),F(7,11),F(0),F(-13,17)],
              [F(0),F(-1),F(0),F(5,11),F(0),F(2,13)],
              [F(0),F(0),F(0),F(1,7)],
              [F(0),F(11,13),F(0),F(-17,19),F(0),F(23,29),F(0),F(-31,37)]]:
        def U(y): return sum((w*y**k for k,w in enumerate(c)),F(0))
        v=U(B)
        for d in (F(1,500),F(1,1000),F(1,10**8)):
            x=B-d
            a=2*d;b=2*(B+x)
            def left(t):return U(x)-(U(x+t/2)+U(x-t/2))/2
            def middle(t):return U(x)-(U(x-t/2)+v)/2
            assert left(a)==middle(a)
            assert middle(b)==U(x)
            assert x+b/2>B and x-b/2==-B
            assert x+a/2==B
            count+=1
    return count
def primitive_controls():
    count=0
    for z in (F(1,4),F(3,2),F(5,7),F(8,3),F(-11,9)):
        p=[1/z]
        for k in range(1,14):
            p=[-F(k)*v/z for v in p]+[1/z]
            derivative=[F(j+1)*p[j+1] for j in range(k)]
            for j in range(k+1):
                assert z*p[j]+(derivative[j] if j<k else 0)==(F(1) if j==k else F(0))
            count+=1
    return count
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--native",required=True)
    ap.add_argument("--output",required=True)
    args=ap.parse_args()
    native,nsha=read(args.native)
    original,sorig=read("notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json")
    seams,sseam=read("notes/data/provisional/NF406_original_prime_support_partition_exact.json")
    jet,jsha=read("notes/data/provisional/NF411_original_source_boundary_jet.json")
    zold,zsha=read("notes/data/provisional/NF450_original_B_complete_Laplace_native_sign_custody_index.json")
    nf413,csha=read("notes/data/provisional/NF413_original_full_246_source_curvature_native.json")
    nf451,msha=read("notes/data/provisional/NF451_original_J8_terminal_collar_custody_index.json")
    assert native["pass"]=="NF489"
    assert sorig==native["original_nf407_source_sha256"]==SRC
    assert sseam==native["original_nf406_seams_sha256"]==SEAM
    assert jet["nf407_source_sha256"]==nf413["original_nf407_full_native_source_sha256"]==zold["source_SHA256"]==SRC
    assert nf451["original_source_sha256"]==SRC and nf451["original_seams_sha256"]==SEAM
    assert native["original_nf411_source_jet_sha256"]==jsha and native["original_nf450_endpoint_source_sha256"]==zsha
    assert nf413["original_true_full_u4_second_derivative_L2_upper_integer"]=="256"
    assert native["original_source_generators"]==246 and native["original_source_grouped_modes"]==273
    assert native["original_sinh_pole"] and native["original_full_native_4096bits"]
    assert native["true_original_J8_x"]=="549/500" and native["true_original_distance_to_B"]=="1/500"
    assert native["true_original_t_subintervals"]==["0","1/250","1/10","1099/250"]
    assert native["original_true_source_support"]=="[-11/10,11/10]"
    assert native["original_7_regular_n9_active_prime_power"]==[2,3,4,5,7,8,9]
    assert native["original_true_joint_4096bit_source_taylor_order"]==1300
    assert native["original_taylor_short_order"]==1284
    assert native["original_true_full_analytic_compact_laplace_M"]==800
    assert native["original_true_short_analytic_compact_laplace_M"]==720
    # Immutable exact original NF448 source Cauchy bounds:
    exponent=F(22,7)*883*RAD
    exponent=(exponent.numerator+exponent.denominator-1)//exponent.denominator
    assert exponent==1111
    assert F(11,4)**exponent < 10**500
    M=4*F(10)**160*F(11,4)**exponent
    tail=F(200)*M*(H/RAD)**1284/(1-H/RAD)
    assert tail==F(native["original_true_source_taylor_cauchy_tail_charge"])<F(1,10**50)
    def endtail(m):
        return F(22000,m)*F(3,8)**(m//10)
    assert endtail(800)==F(native["original_true_compact_Laplace_geometric_tail_charge"])<F(1,10**29)
    assert endtail(720)==F(native["original_true_short_compact_Laplace_tail_charge"])<F(1,10**25)
    assert F(native["original_source_true_dyadic_input_charge"])==F(1,10**500)
    assert F(native["original_source_prime_weight_radius_charge"])<F(1,10**24)
    final=iv(native["original_full_true_native_z_outward"])
    short=iv(native["original_short_true_native_z_outward"])
    assert overlap(final,short)
    assert final[1]-final[0]<F(1,10**20)
    assert final[0]>-25000 and final[1]<25000
    Z=iv(zold["complete_z_B_outward_24_decimal"])
    assert Z[1]<0
    # Source-accepted original NF451 complete physical variation check:
    # log(2B/D)=log1100<8 from exact positive e>(8/3).
    assert F(8,3)**8>2*B/D
    var=D*(14000+600*8)
    assert final[0]-Z[1]<var and Z[0]-final[1]<var
    assert native["original_NF451_true_complete_modulus_crosscheck"]
    assert native["original_full_J8_signed_upper"]==native["NF404"]==native["W_ODD_NEG"]==native["RH"]=="OPEN"
    assert groups_identities()==18
    assert primitive_controls()==65
    out={
      "pass":"NF489-independent-source-Fraction",
      "standing":"SOURCE-VERIFIED first complete ORIGINAL joint compact J8 physical z at x=549/500, no whole terminal D8 integrated",
      "source_original_nf407_sha256":SRC,
      "source_original_nf406_seams_sha256":SEAM,
      "native_raw_sha256":nsha,
      "original_nf411_source_jet_sha256":jsha,
      "original_nf413_source_curvature_sha256":csha,
      "original_nf451_complete_compact_modulus_sha256":msha,
      "original_true_J8_x":"549/500",
      "source_original_physical_z_outward":list(map(str,final)),
      "source_original_physical_z_short_crosscheck_outward":list(map(str,short)),
      "original_exact_odd_polynomial_boundary_controls":18,
      "original_exact_polynomial_Laplace_primitive_controls":65,
      "original_true_J8_full_signed_D8_upper":"OPEN",
      "NF404":"OPEN","W_ODD_NEG":"OPEN","RH":"OPEN",
      "next_bold":"NF490 propagate genuine complete compact source point into source-signed interval moment evaluation, not endpoint interpolation without certified error"
    }
    path=Path(args.output);path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(out,indent=2)+"\n")
    print("NF489 first real original J8 physical point independent source Fraction PASS",*[float(x) for x in final],flush=True)
    print("original terminal D8 upper/NF404/RH OPEN",flush=True)
if __name__=="__main__":main()
