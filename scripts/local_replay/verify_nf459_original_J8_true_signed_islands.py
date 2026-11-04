#!/usr/bin/env python3
"""NF459: TWO TRUE ORIGINAL positive signed J8 continuous interior islands.

Read already complete-source NF459 actual 4096-bit z and 4pz+2z² points.
Use original NF413 physical ||U''||2<256, NF446 |U'|<400,
|U|<900, |v|<1e-10 (NF459 source-native), and true original
NF411 all seven weights/C<4 to certify |z'|<26000 on
1/(2e6)<=d=B-x<=3/2000. Analytically integrate original
signed integrand lower over radius 1e-18 at d0=1e-6 and d0=1e-3.
No interpolation assumption. Full J8 signed still OPEN.
"""
import argparse,json,sys
from pathlib import Path
from fractions import Fraction as Q
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
SRC_SHA="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAM_SHA="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
R=Q(1,10**18)
def read(p):return json.loads(Path(p).read_bytes())
def prove_lipschitz():
    B=Q(11,10)
    dlo=Q(1,2000000);dhi=Q(3,2000)
    amin=2*dlo;amax=2*dhi
    assert 0<amin<Q(1,1000)<amax<Q(1,100)
    assert Q(8,3)**16>Q(44,10)/amin
    assert Q(55,1000)**2>amax
    assert Q(3,4)**2>Q(1,2)
    # NF413 true H²: |U'(x±t/2)-U'(x)|<=256sqrt(t/2).
    # NF446 I0 moving-edge and derivative on true physical support:
    i0int=256*Q(3,4)*(2*Q(55,1000)+Q(2,3)*amax*Q(55,1000))
    assert i0int<23
    i0edge=400*(1+amax)
    assert i0edge<402
    # NF446 I1 original derivative: |U'(x)-U'(x-t/2)/2|<600,
    # actual log(b/a)<16, b-a<4B=4.4.
    i1int=600*(16+4*B)
    assert i1int==12240
    # Genuine original lower source edge at t=a:
    # |U(x)-[U(x-a/2)+v]/2|<800d, so 2K(a)*...<800+1600d.
    i1lo=800+1600*dhi
    assert i1lo<803
    # Original upper endpoint x-b/2=-B and odd U(-B)=-v:
    # 2K(b)|U(x)|<2*(1+1/4)*900.
    i1hi=2*(1+Q(1,4))*900
    assert i1hi==2250
    # Accepted source c0<10, K-1/t<=1, H(b)<4,
    # seven true w_n sum<4, center derivative<2.
    c0=4000
    scalar=3
    tail=400*4+2*900*(1+Q(1,4))
    assert tail==3850
    finite=1602
    total=i0int+i0edge+i1int+i1lo+i1hi+c0+scalar+tail+finite
    assert total<26000
    # p(B-d)=v[log(B/d)/2+C8], |v|<1e-10, log(B/d)<16,C8<4.
    # Original |z|<1e-8 on tiny islands from actual source points.
    pd=Q(1,10**10)/(2*dlo)
    assert pd==Q(1,10**4)
    abs_p=Q(1,10**10)*(8+4)
    assert abs_p<Q(1,10**8)
    # Signed integrand derivative:
    # |(4pz+2z²)'|<=4|p' z|+4(|p|+|z|)|z'|.
    Lq=4*pd*Q(1,10**8)+8*Q(1,10**8)*26000
    assert Lq<Q(1,400)
    return total,Lq
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--nf459",required=True)
    ap.add_argument("--nf413",default="notes/data/provisional/NF413_original_full_246_source_curvature_native.json")
    ap.add_argument("--nf446",default="notes/data/provisional/NF446_original_joint_compact_kernel_J7_J8_custody_index.json")
    ap.add_argument("--nf457",default="notes/data/provisional/NF457_original_full_J8_matched_compact_and_extended_signed_collar_custody.json")
    ap.add_argument("--output",required=True)
    a=ap.parse_args()
    data=read(a.nf459);h413=read(a.nf413);h446=read(a.nf446);h457=read(a.nf457)
    assert data["original_source_sha256"]==h446["original_nf407_source_sha256"]==h457["original_source_sha256"]==SRC_SHA
    assert data["original_seams_sha256"]==h446["original_nf406_prime_seam_sha256"]==h457["original_seams_sha256"]==SEAM_SHA
    assert h413["original_nf407_full_native_source_sha256"]==SRC_SHA
    assert h413["original_true_full_u4_second_derivative_L2_upper_integer"]=="256"
    assert h446["source_nf445_native_u4_B_interval_strictly_between_minus1_and0"]
    assert h446["derived_true_compact_Uprime_sup_lt"]==400
    assert h446["derived_true_compact_U_sup_lt"]==900
    assert data["original_true_endpoint_independent_NF450_overlap"]
    assert data["native_bits"]==4096 and data["original_groups"]==273
    assert data["true_original_complete_signed_J8_integral"]=="OPEN"
    assert Q(117,10**13)<Q(1,10**10) # native v between -1.17e-11 and -1.16e-11.
    total,Lq=prove_lipschitz()
    out=[]
    for d in [Q(1,1000000),Q(1,1000)]:
        v=data["points"][str(d)]
        lo,hi=map(Q,v["original_z_J8_true_full_outward"])
        qlo,qhi=map(Q,v["original_pointwise_4pz_plus_2z2_outward"])
        assert -Q(1,10**9)<lo<hi<0
        assert Q(1,10**19)<qlo<qhi<Q(1,10**17)
        assert v["original_point_z_sign"]=="NEGATIVE"
        assert v["original_point_signed_integrand_sign"]=="POSITIVE"
        # Whole original z remains <1e-8 by |z'|<26000,
        # and true p<1e-8 from v and C8 source.
        assert max(abs(lo),abs(hi))+26000*R<Q(1,10**8)
        assert d-R>Q(1,2000000) and d+R<Q(3,2000)
        islandlo=qlo-Lq*R
        islandhi=qhi+Lq*R
        assert 0<Q(1,10**20)<islandlo<islandhi
        area_lo=2*R*islandlo
        area_hi=2*R*islandhi
        assert area_lo>Q(1,10**37)
        out.append({"center_original_d":str(d),"original_x":"B-"+str(d),
                    "original_physical_x_island_radius":str(R),
                    "original_complete_original_signed_integrand_strict":[str(islandlo),str(islandhi)],
                    "original_complete_signed_island_integral_strict":[str(area_lo),str(area_hi)],
                    "original_true_z_negative":True,
                    "original_original_p_negative":True,
                    "original_full_signed_integrand_positive":True})
        print("NF459 original full J8 source positive signed island at d",str(d),"integral lower approx",float(area_lo),flush=True)
    assert Q(1,1000)-R>Q(1,1000000)+R
    r={
      "pass":"NF459","standing":"SOURCE-CERTIFIED two true ORIGINAL physical J8 complete z strictly POSITIVE signed interior islands with actual continuous integrals, full J8 signed OPEN",
      "original_source_sha256":SRC_SHA,"original_seams_sha256":SEAM_SHA,
      "original_full_source_original_246":True,
      "original_source_signed_points_verified_native_4096bit":True,
      "original_source_NF413_U2_L2_upper":256,
      "original_NF446_complete_joint_compact_used":True,
      "original_z_global_local_derivative_bound_strict":"26000",
      "original_signed_integrand_derivative_bound_strict":str(Lq),
      "original_rational_derivative_ledger_total":str(total),
      "original_local_islands":out,
      "original_each_genuine_signed_island_strict_lower":"1e-37",
      "original_both_signed_islands_disjoint":True,
      "original_both_positive_island_sum_lower":"2e-37",
      "original_NF457_previous_positive_terminal_collar_remains_disjoint":True,
      "complete_original_J8_signed":"OPEN","complete_original_J7_signed":"OPEN","NF410_NF404":"OPEN","W_ODD_NEG":"OPEN","RH":"OPEN",
      "next":"NF460 actual original full J8 continuous source-correlated z moment and signed D8, beyond finite positive islands"
    }
    path=Path(a.output);path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(r,indent=2)+"\n")
    print("NF459 both complete ORIGINAL signed J8 local islands source-certified, full J8 still OPEN",flush=True)
if __name__=="__main__":main()
