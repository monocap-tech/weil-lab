#!/usr/bin/env python3
"""NF410: exact, signed Taylor moment functional for ORIGINAL p=q+r.

Builds rigorous rational enclosures of ∫_cell (x-c)^k p(x) dx for k=0..3,
with all seven actual prime seams and original endpoint log. This eliminates
physical x quadrature when the *continuous original* z is supplied as a
certified rational Taylor model. It DOES NOT certify that missing z model.

Only accepted NF406/NF407/NF409 source receipts are used. Pure Fraction math.
"""
import argparse,hashlib,json,sys
from pathlib import Path
from math import comb
from fractions import Fraction as F
from nf407_original_prime_jump_log_power_exact import I,ilog,compact
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)

B=F(11,10)
PRIMES=(2,3,4,5,7,8,9)
DEGREE=3

def read(path):
    raw=Path(path).read_bytes()
    return json.loads(raw),hashlib.sha256(raw).hexdigest()

def irange_pow(v,n):
    """Interval hull of real power, including even powers across zero."""
    assert n>=0
    if n==0:return I(1)
    if n%2==1:return I(v.l**n,v.u**n)
    if v.l<=0<=v.u:return I(0,max(v.l**n,v.u**n))
    return I(min(v.l**n,v.u**n),max(v.l**n,v.u**n))

def ih(v):return [str(v.l),str(v.u)]
def overlap(a,b):return max(a.l,b.l)<=min(a.u,b.u)
def imin(a,b):return I(min(a.l,b.l),min(a.u,b.u))
def imax(a,b):return I(max(a.l,b.l),max(a.u,b.u))

def hj_scalar(y,j):
    # H_j(y)=∫_0^y t^j log(B/t) dt; H_j(0)=0.
    # On 0<=y<=B this is monotone, H'_j=y^j log(B/y)>=0.
    if y==0:return I(0)
    assert F(0)<y<=B
    return compact(I(y**(j+1))/F(j+1)*
                   (ilog(I(B/y))+F(1,j+1)),70)

def hj_range(y,j):
    assert F(0)<=y.l<=y.u<=B
    return I(hj_scalar(y.l,j).l,hj_scalar(y.u,j).u)

def q_moment(a,b,ctr,k,v):
    # y=B-x, x-ctr=(B-ctr)-y.
    # ∫_a^b (x-ctr)^k q(x)dx
    # = (v/2)*Σ_j (-1)^j binom(k,j)(B-ctr)^(k-j)
    #       [H_j(B-a)-H_j(B-b)].
    A=B-ctr
    ya=I(B)-a
    yb=I(B)-b
    total=I(0)
    for j in range(k+1):
        coeff=F((-1)**j*comb(k,j))*A**(k-j)
        total+=coeff*(hj_range(ya,j)-hj_range(yb,j))
    return compact(v*total/2,60)

def r_moment(a,b,ctr,k,v,shifts,weights):
    # For each real jump location x_n:
    # ∫_a^b 1_{x>x_n}(x-ctr)^k dx =
    # [(b-ctr)^(k+1)-(min(b,max(a,x_n))-ctr)^(k+1)]/(k+1).
    total=I(0)
    for n in PRIMES:
        start=imin(b,imax(a,shifts[n]))
        term=(irange_pow(b-I(ctr),k+1)-
              irange_pow(start-I(ctr),k+1))/F(k+1)
        total+=weights[n]*term
    return compact(v*total,60)

def polynomial_energy_primitive(coeff,a,b,ctr):
    """Exact rational ∫_a^b (Σ_k coeff_k(x-ctr)^k)^2 dx."""
    result=F(0)
    for k,ck in enumerate(coeff):
        for j,cj in enumerate(coeff):
            p=k+j+1
            result+=ck*cj*((b-ctr)**p-(a-ctr)**p)/p
    return result

def main():
    arg=argparse.ArgumentParser()
    arg.add_argument("--seams",default="notes/data/provisional/NF406_original_prime_support_partition_exact.json")
    arg.add_argument("--principal",default="notes/data/provisional/NF407_original_prime_jump_log_power_exact.json")
    arg.add_argument("--nf409",default="notes/data/provisional/NF409_original_principal_cell_integrals_exact.json")
    arg.add_argument("--output",required=True)
    args=arg.parse_args()
    seams,ssha=read(args.seams)
    principal,psha=read(args.principal)
    old,osha=read(args.nf409)
    assert principal["original_nf406_seams_sha256"]==ssha
    assert old["original_nf406_seams_sha256"]==ssha
    assert old["original_nf407_principal_source_sha256"]==psha
    assert seams["number_of_open_physical_support_cells"]==16
    assert all(d["W_ODD_NEG"]==d["RH"]=="OPEN" for d in (seams,principal,old))
    v=I(*map(F,principal["original_source_u4_endpoint_interval"]))
    assert v.u<0
    shifts={}
    weights={}
    for entry in principal["source_true_original_prime_jump_terms"]:
        n=entry["n"]
        shifts[n]=I(*map(F,entry["positive_jump_location_absolute_interval"]))
        weights[n]=I(*map(F,entry["signed_mangoldt_weight_positive_interval"]))
        assert F(0)<shifts[n].l<=shifts[n].u<B and weights[n].l>0
    assert set(shifts)==set(PRIMES)
    nodes=seams["certified_ordered_knots"][8:]
    assert len(nodes)==9 and nodes[0]["label"]=="0" and nodes[-1]["label"]=="+B"
    totals=I(0)
    cells=[]
    oldcells=old["original_eight_positive_source_principal_integrals"]
    for i in range(8):
        x,y=nodes[i:i+2]
        a=I(F(x["low"]),F(x["high"]))
        b=I(F(y["low"]),F(y["high"]))
        assert a.u<b.l
        ctr=(a.l+a.u+b.l+b.u)/4
        moments=[]
        for k in range(DEGREE+1):
            q=q_moment(a,b,ctr,k,v)
            r=r_moment(a,b,ctr,k,v,shifts,weights)
            moments.append(compact(q+r,54))
        old0=I(*map(F,oldcells[i]["known_signed_p_integral_enclosure"]))
        assert overlap(moments[0],old0),("original NF409 k=0 mismatch",i+1)
        assert moments[0].u<0
        totals+=moments[0]
        cells.append({
            "cell":i+1,"left_label":x["label"],"right_label":y["label"],
            "center_rational":str(ctr),
            "left_source_interval":ih(a),"right_source_interval":ih(b),
            "signed_original_p_moments_by_degree_0_to_3":[ih(m) for m in moments],
            "degree_zero_overlap_with_independent_nf409":True,
            "verified_original_z_taylor_coefficients":None,
            "verified_original_z_minus_model_sup_error":None
        })
    totals=compact(totals,54)
    global0=I(*map(F,old["original_independent_global_signed_principal_integral_outward"]))
    assert overlap(totals,global0)
    ep=I(*map(F,principal["original_known_q_plus_all_seven_prime_jumps_power_interval"]))
    assert ep.l>0
    out={
        "pass":"NF410",
        "standing":"EXACT ORIGINAL SIGNED PRINCIPAL TAYLOR MOMENT FUNCTIONAL; NO ORIGINAL CONTINUOUS z TAYLOR ENCLOSURE OR CENTERED NORM DECISION",
        "original_nf406_source_sha256":ssha,
        "original_nf407_source_sha256":psha,
        "original_nf409_source_sha256":osha,
        "supported_original_half_width":str(B),
        "degree":DEGREE,
        "original_source_seams_and_all_seven_signed_prime_weights_retained":True,
        "original_positive_original_physical_cells":cells,
        "global_zero_degree_moment_from_cells":ih(totals),
        "independent_original_nf409_global_moment_overlap":True,
        "original_known_principal_power_outward":ih(ep),
        "exact_polynomial_energy_functional":
            "For rational T_i(x)=sum_k a_ik (x-c_i)^k, E_T=E_p+2 sum_i integral T_i^2 +4 sum_i sum_k a_ik*M_ik. The T_i^2 terms have exact rational polynomial primitives; M_ik are the certified source-correlated intervals in this receipt.",
        "rigorous_completion_rule":
            "Independently prove |z(x)-T_i(x)|<=delta_i on EVERY original cell, including one-sided prime seams and the x=B log endpoint. Then eps²<=2 sum_i width_i*delta_i², choose rational R with E_T<=R², and obtain E_true in [E_T-2R eps-eps²,E_T+2R eps+eps²], paying NF408 native source radius. Compare BOTH endpoints to NF404 exact cap. Never infer a bound from Gauss agreement.",
        "original_continuous_z_taylor_coefficients_certified":False,
        "original_continuous_z_remainder_certified":False,
        "original_full_centered_scalar_rigorous_lower_upper_computed":False,
        "nf404_sufficient_gate_decided":False,
        "new_signed_kernel_cells":0,"W_ODD_NEG":"OPEN","RH":"OPEN"
    }
    outpath=Path(args.output)
    outpath.parent.mkdir(parents=True,exist_ok=True)
    outpath.write_text(json.dumps(out,indent=2)+"\n")
    print("NF410 true original p moments 0..3 across 8 signed cells: EXACT RATIONAL INTERVAL")
    print("NF410 source-signed degree-zero independent NF409 overlap: PASS")
    print("NF410 continuous original z enclosure and NF404 threshold decision: OPEN")
if __name__=="__main__":main()
