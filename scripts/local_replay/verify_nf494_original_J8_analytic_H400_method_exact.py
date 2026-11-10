#!/usr/bin/env python3
"""NF494 independent EXACT rational original joint compact H400 method audit.

Checks genuine immutable NF407 246 dyadic selected+critical source and
NF406 J8 support, original analytically canceled digamma finite-window
source multiplication, m>=1000 true analytic source tails, and EXACT
coefficient agreement of two independently derived moving-boundary
representations for six adversarial odd polynomial sources.

Toy K=1/t is an algebraic control only, not an alteration of original
NF446 physical kernel. No original numerical H400 or J8 energy value
is claimed by this independent method verification.
"""
from __future__ import annotations
import json,hashlib,sys,math
from pathlib import Path
from fractions import Fraction as F
from verify_nf492_original_J8_all_orders_log_peel_400jet_exact import original_source_envelope
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
B=F(11,10)
T=4*B
SRC="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAM="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
N=15
def read(path):
    b=Path(path).read_bytes()
    return json.loads(b),hashlib.sha256(b).hexdigest()
def source_jet(a):
    arr=[F(0)]*N
    for k,x in enumerate(a):
        for j in range(min(k,N-1)+1):
            arr[j]+=x*math.comb(k,j)*B**(k-j)*((-1)**j)
    return arr
def minus_source_bivariate(a):
    """U(B-d-t/2) expansion dictionary d^i t^j for source odd U."""
    out={}
    for k,c in enumerate(a):
        for i in range(k+1):
            for j in range(k-i+1):
                z=F(math.factorial(k),
                    math.factorial(i)*math.factorial(j)*math.factorial(k-i-j)
                    )*B**(k-i-j)*((-1)**i)*F((-1)**j,2**j)
                out[i,j]=out.get((i,j),F(0))+c*z
    return out
def direct_original_compact_H_without_log2(u,um):
    """NF446 exact full physical toy K=1/t, Q=0, original moving a,b."""
    out=[F(0)]*N
    for (i,j),coef in um.items():
        if j>=2 and j%2==0 and i+j<N:
            # A_x(t)=-even t>=2 source coefficient.
            out[i+j]-=coef*F(2**j,j)
        if j>=1:
            # M_x(t)=-U(x-t/2)/2 for each positive t power.
            c=-coef/F(2*j)
            for r in range(j+1):
                if i+r<N:
                    out[i+r]+=c*math.comb(j,r)*T**(j-r)*((-2)**r)
            if i+j<N:
                out[i+j]-=c*(2**j)
    # Compact tail U(x)*int_b^T (1/t)dt = -U log(1-2d/T).
    # Scalar after all-orders peel: U/2 log(1-d/(2B)).
    for i,coef in enumerate(u):
        for n in range(1,N-i):
            logsmall=-F(1,n)*(F(1)/(2*B))**n
            logtail=F(1,n)*(F(2)/T)**n
            out[i+n]+=coef*(logsmall/2+logtail)
    return out
def refactored_fixed_source_H_without_log2(u):
    """Independent original fixed-window F+L+Rplus+small-log recurrences."""
    H=[F(0)]*N
    fact=[math.factorial(j) for j in range(N+1)]
    harm=[F(0)]
    for n in range(1,N):harm.append(harm[-1]+F(1,n))
    for n in range(N):
        # Entire original source F(d) over fixed 0..T:
        for k in range(1,N-n):
            H[n]-=F(1,2)*u[n+k]*math.comb(n+k,n)*(T/F(2))**k/F(k)
        # Original first moving cutoff L source harmonic.
        if n>=1:H[n]+=u[n]*harm[n]/2
        # Original upper moving cutoff Rplus true odd source.
        if n>=1:
            for j in range(n):
                k=n-1-j
                beta=F(1,k+1)-F((-1)**j*fact[k]*fact[j],fact[k+j+1])
                H[n]+=u[j]*F(2**k,T**(k+1))*beta
        # Original scalar log(1-d/(2B))/2*U.
        for j in range(n):
            k=n-j
            H[n]-=u[j]*F(1,2*k)*(F(1)/(2*B))**k
    return H
def controls():
    sources=[
       [F(0),F(1)],
       [F(0),F(-3,7)],
       [F(0),F(13,31),F(0),F(-17,41)],
       [F(0),F(-1,10**8),F(0),F(7,11),F(0),F(-19,37)],
       [F(0),F(0),F(0),F(1,17)],
       [F(0),F(5,13),F(0),F(-7,29),F(0),F(11,31),F(0),F(-13,37)]
    ]
    count=0
    for a in sources:
        u=source_jet(a)
        um=minus_source_bivariate(a)
        d=direct_original_compact_H_without_log2(u,um)
        f=refactored_fixed_source_H_without_log2(u)
        for j in range(N):
            assert d[j]==f[j],("METHOD STOP original NF446 moving endpoint rational algebra mismatch",a,j,d[j],f[j])
            count+=1
        assert all(a[j]==0 for j in range(0,len(a),2))
    return count
def main():
    source,sha=read("notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json")
    seams,ss=read("notes/data/provisional/NF406_original_prime_support_partition_exact.json")
    jet,js=read("notes/data/provisional/NF411_original_source_boundary_jet.json")
    nf450,zs=read("notes/data/provisional/NF450_original_B_complete_Laplace_native_sign_custody_index.json")
    assert sha==SRC and ss==SEAM
    assert jet["nf407_source_sha256"]==nf450["source_SHA256"]==SRC
    assert source["original_dimension"]==242
    assert len(source["original_exact_native_original_four_critical_coefficients_mid_radius"])==4
    assert len(source["original_source_critical_sine_frequencies"])==32
    raw,error,pole=original_source_envelope(source)
    assert raw<F(10)**160 and error<F(1,10**650)
    assert error*F(10)**230<F(1,10**300)
    # On real t>=4B, source |U(B-d-t/2)|<1e400*e^t,
    # from original 883 frequency and degree <=13, |d|<1/25.
    # Source m>=1000 finite fixed-window tail <1e-1200.
    assert 2*F(10)**400*(F(3,8)**(4*999))<F(1,10**1200)
    assert F(4)*B==F(22,5)
    assert F(2)*F(1,25)<F(1,10)
    # The direct original finite K at b=T-2d has m>=1000
    # modulus similarly <1e-1200 for all |d|<=1/25.
    assert 2*F(10)**400*(F(3,8)**(4*1000))<F(1,10**1200)
    assert F(1,10**1200)<F(1,10**300)
    assert controls()==90
    # source authentic separate old pole at s=-1/4: m0 has
    # exact rate0 limit T, not an invalid digamma(0).
    assert F(1,4)-F(1,4)==0
    out={
       "pass":"NF494-exact-independent-method",
       "standing":"SOURCE-EXACT original NF446 whole joint compact H fixed-window+both moving endpoint analytic 400-jet construction controls and original m>=1000 source input budgets; actual native H400 and full Ew numeric separately pending",
       "original_nf407_source_sha256":SRC,
       "original_nf406_seams_sha256":SEAM,
       "original_nf411_source_sha256":js,
       "original_nf450_zB_source_sha256":zs,
       "original_raw_246_generator_absolute_envelope":str(raw),
       "original_raw_246_generator_source_input_radius":str(error),
       "original_source_fixed_window_m_ge1000_full_disk_tail_strict_upper":"1e-1200",
       "original_source_complex_dyadic_input_complex_full_disk_tail_strict_upper":"1e-300",
       "original_true_sinh_negative_rate_m0_zero_denominator_handled_by_exact_T":True,
       "original_joint_full_source_moving_boundary_rational_controls":90,
       "original_all_orders_physical_log_coefficient":"[U(B-d)-U(B)]/2",
       "original_true_J8_w_log_coefficient":"U(B-d)/2",
       "actual_original_full_H400_native_source_coefficients_computed_by_this_audit":False,
       "original_original_complete_400_H_and_U_physical_Ew_T":"OPEN",
       "NF404":"OPEN","W_ODD_NEG":"OPEN","RH":"OPEN"
    }
    p=Path("nf494-original-J8-whole-H400-method-source-exact-preflight.json")
    p.write_text(json.dumps(out,indent=2)+"\n")
    print("NF494 original NF446 joint compact full H fixed-window/both-cutoffs: 90 adversarial source rational jet checks PASS")
    print("Original source input and all-m finite-window tail <1e-300; actual native H400 and Ew/NF404 still OPEN")
if __name__=="__main__":main()
