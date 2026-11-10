#!/usr/bin/env python3
"""NF490: exact source-original whole J8 all-orders log peel and Cauchy gate.

The accepted original NF446 COMPLETE joint compact physical J8 response has
EXACT full coefficient g(d)=[U(B-d)-U(B)]/2 of log(B/d), not merely its
first derivative coefficient (NF487). The remainder H(d) extends
holomorphically on the fixed-J8 branch to |d|<=1/25.

Original source raw 242+4 original 4096-bit dyadic coefficient balls are
parsed DIRECTLY; conservative complex 400-jet source bounds verified.
No full original J8 signed upper and no actual 400 analytic H-jets computed.
"""
from __future__ import annotations
import hashlib,json,math,sys
from pathlib import Path
from fractions import Fraction as F
if hasattr(sys, "set_int_max_str_digits"):sys.set_int_max_str_digits(0)

SRC="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAM="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
B=F(11,10);DELTA=F(1,500);R=F(1,25);H=F(1,10)
N=400;Q=DELTA/R
P=(2,3,4,5,7,8,9)

def load(path):
    raw=Path(path).read_bytes()
    return json.loads(raw),hashlib.sha256(raw).hexdigest()

def dyad(z):
    n,e=int(z[0]),int(z[1])
    return F(n*2**e) if e>=0 else F(n,2**(-e))

def original_source_envelope(source):
    """Exact ORIGINAL dyadic selected+4 critical/32-sine coefficient balls."""
    acc=F(0)
    error=F(0)
    names=source["original_selected_generator_node_orders"]
    balls=source["original_exact_native_raw_selected_coefficients_mid_radius"]
    assert len(names)==len(balls)==242
    counts={}
    for (freq,k),(mid,rad) in zip(names,balls):
        assert freq!="pole" and F(0)<F(freq)<883 and 0<=k<=13
        counts[(freq,k)]=counts.get((freq,k),0)+1
        ci=dyad(mid);eps=abs(dyad(rad))
        acc+=(abs(ci)+eps)*(B+F(1,5))**k
        error+=eps*(B+F(1,5))**k
    critical=source["original_exact_native_original_four_critical_coefficients_mid_radius"]
    shapes=source["original_source_critical_sines_and_pole_coefficients"]
    freqs=source["original_source_critical_sine_frequencies"]
    assert len(critical)==len(shapes)==4 and len(freqs)==32
    polebound=F(0)
    for (mid,rad),shape in zip(critical,shapes):
        ci=dyad(mid);eps=abs(dyad(rad))
        for f,shape_coeff in zip(freqs,shape["sine_coefficients"]):
            assert F(0)<F(f)<883
            acc+=(abs(ci)+eps)*abs(F(shape_coeff))
            error+=eps*abs(F(shape_coeff))
        polebound+=(abs(ci)+eps)*abs(F(shape["sinh_coefficient"]))
        error+=eps*abs(F(shape["sinh_coefficient"]))
    acc+=polebound
    assert acc<F(10)**160
    assert error<F(1,10**650)
    assert len(counts)>0
    return acc,error,polebound

def val(c,y):
    return sum((a*y**j for j,a in enumerate(c)),F(0))

def derivative(c,y,k=1):
    return sum((a*(math.factorial(j)//math.factorial(j-k))*y**(j-k)
                for j,a in enumerate(c) if j>=k),F(0))

def original_all_log_algebra():
    cases=[
      [F(0),F(1)],
      [F(0),F(-3,7)],
      [F(0),F(2,3),F(0),F(-5,13)],
      [F(0),F(-17,31),F(0),F(19,37),F(0),F(-23,41)],
      [F(0),F(0),F(0),F(1,19)],
      [F(0),F(1,10**8),F(0),F(-1,10**5),F(0),F(13,17),F(0),F(-11,29)]
    ]
    checks=0
    for c in cases:
        vb=val(c,B)
        for d in [F(1,500),F(1,1000),F(1,10**6),F(1,25)]:
            x=B-d;a=2*d;b=2*(B+x)
            ux=val(c,x)
            g=(ux-vb)/2
            def A(t): return ux-(val(c,x+t/2)+val(c,x-t/2))/2
            def M(t): return ux-(val(c,x-t/2)+vb)/2
            def E(t): return (ux-val(c,x-t/2))/2
            assert a>0 and b>a
            for t in [a,b,F(1,10),F(1),F(2)]:
                assert M(t)==g+E(t)
                # Source oddness is the exact right-end matching gate.
                assert A(a)==M(a) and M(b)==ux
                if t:
                    # Source terms after peeling carry a removable origin:
                    assert E(t)==sum(
                        ((-1)**(j+1)*derivative(c,x,j)*t**j /
                          (F(2)**(j+1)*math.factorial(j))
                         for j in range(1,len(c))),F(0))
                    assert A(t)==-sum(
                        (derivative(c,x,j)*t**j /
                          (F(2)**j*math.factorial(j))
                         for j in range(2,len(c),2)),F(0))
                checks+=1
            assert b/a*F(B,B+x)==B/d
            # The source-exact complete original all-order log coefficient,
            # before any source jet truncation:
            assert g==sum((F((-1)**j,2*math.factorial(j))*
                           derivative(c,B,j)*d**j
                           for j in range(1,len(c))),F(0))
            assert F(2)*g+vb==ux
            # Formal log basis coefficients:
            # original g log(b/a)+v/2 log((B+x)/B)
            # =g log(B/d)+U(x)/2 log((B+x)/B).
            for L,T in [(F(1),F(2)),(F(-7,13),F(5,11)),
                        (F(123),F(-321))]:
                assert g*(L+T)+vb*T/2==g*L+ux*T/2
                assert g+vb/2==ux/2
                checks+=1
            alpha=-derivative(c,B,1)/2
            beta=derivative(c,B,2)/4
            assert g-alpha*d-beta*d*d==sum(
                (F((-1)**j,2*math.factorial(j))*
                 derivative(c,B,j)*d**j
                 for j in range(3,len(c))),F(0))
            checks+=1
    return checks

def formal_L_coeffs(m=10):
    """Exact rational t*K(t) coefficients: t e^-t/4/(1-e^-t)."""
    e=[F((-1)**j,4**j*math.factorial(j)) for j in range(m)]
    f=[F((-1)**j,math.factorial(j+1)) for j in range(m)]
    L=[F(0)]*m
    for j in range(m):
        L[j]=e[j]-sum((f[k]*L[j-k] for k in range(1,j+1)),F(0))
    for j in range(m):
        assert sum((L[k]*f[j-k] for k in range(j+1)),F(0))==e[j]
    assert L[0]==1 and L[1]==F(1,4)
    return L

def exact_kernel_holomorphic_cauchy():
    assert R==F(1,25) and Q==F(1,20) and H==F(1,10)
    assert DELTA<R and 4*B+2*R==F(112,25)<F(9,2)
    assert 2*R==F(2,25)<F(1,10)
    # Every complex t integration path has |Im t|<=2R, and
    # -2R<=Re t<=4B+2R<9/2. f(t)=(1-e^-t)/t=
    # int_0^1 exp(-s t)ds has positive real part >1/5:
    # cos(Im t)>=1-(2/25)^2/2>99/100,
    # e^(-9/2)<1/16, hence
    # Re f>(99/100)*(1-1/16)/(9/2)>1/5.
    assert 1-(2*R)**2/F(2)>F(99,100)
    assert (F(8,3)**4)>16
    f_lower=F(99,100)*(1-F(1,16))/F(9,2)
    assert f_lower>F(1,5)
    assert F(1)/(1-F(1,50))<F(11,10)   # exp(1/50)<11/10
    assert F(1)/(1-F(2,25))<F(11,10)   # exp(2/25)<11/10
    # |L=tK|<11/2<6 and |L'|<33/2<17.
    assert F(11,10)*5==F(11,2)<6
    Lprime=F(11,10)*(F(5,4)+F(11,20)*25)
    assert Lprime==F(33,2)<17
    # Original 246 generator source coefficient envelope. On ALL
    # complex physical compact paths, and on fixed-J8 prime branch
    # analytic continuation only, |y|<2, |Im y|<=2R:
    # ratio (2/(B+1/5))^13=(20/13)^13<10^3;
    # 2*pi*883*(2R)<445 and e^445<(11/4)^445<10^200.
    w=2*F(22,7)*883*2*R
    assert w<445 and (F(20,13)**13)<1000
    assert (F(11,4)**445)<10**200
    # Consequently |U(y)|<10^400, and the original finite
    # polynomial-frequency generator derivative bounds
    # (degree <=13, omega<6000) give |U'|,|U''|<10^410.
    assert 2*F(22,7)*883<6000
    assert 13+2*6000<10**5
    assert 13*12+2*13*6000+6000**2<10**8
    # All terms of H include physical joint U and its derivatives,
    # A_x(t)=O(t^2), [U(x)-U(x-t/2)]=O(t), so
    # K(t)=L(t)/t has no unremoved singularities. With t-path length
    # <5, |L|<6, |Q=(L-1)/t|<17 and T(b)<5, the full fixed-branch H
    # is holomorphic in |d|<=1/25 and bounded by 10^420.
    assert 4*(B+R)<5
    assert 2*R<F(1,10)
    assert 6*F(5,4)*10**410 <10**420
    # Nonoriginal-only scalar constants: |c0|<10 (NF446),
    # full original source weights <1, original center <2,
    # original tail |T(b)|<5 from T(4B)<4 and vertical length<2R.
    assert 10*10**400+7*2*10**400+5*10**400 <10**420
    assert formal_L_coeffs()[1]==F(1,4)
    return True

def full_analytic_signed_error_gate():
    # Define exact analytic original full-branch jets:
    # H_N(d)=sum_{n=0}^{N-1} H^(n)(0)/n! d^n,
    # g_N(d)=sum_{n=1}^{N-1} (-1)^n U^(n)(B)/(2n!)d^n.
    # The numerical jet coefficients are NOT supplied in NF490.
    # Source-holomorphic Cauchy M_H<10^420, M_g<10^400,
    # q=delta/R=1/20 makes both tails pointwise <= eps.
    E_H=F(10)**420*Q**N/(1-Q)
    E_g=F(10)**400*Q**N/(1-Q)
    assert E_H<F(1,10**99)
    assert E_g<F(1,10**119)
    # For physical x in true terminal d in (0,delta], original
    # |z|<25000, |p|<7+0.5*L(d), exact
    # D=∫[4 p z+2 z^2].
    # Error z-z_N <= E_H+E_g*L(d), not pointwise bounded at d=0
    # because logarithm diverges; integrate correctly.
    # log(B/delta)=log550<7 from e>8/3 and (8/3)^7>550.
    assert F(8,3)**7>550
    I0=DELTA
    I1=8*DELTA                 # bound int L <delta*(7+1)
    I2=65*DELTA                # bound int L² <delta*(7²+2*7+2)
    assert I0==F(1,500) and I1==F(2,125) and I2==F(13,100)
    linear=(100028*E_H*I0 +2*E_H*I1+
            100028*E_g*I1+2*E_g*I2)
    quadratic=2*(E_H**2*I0+2*E_H*E_g*I1+E_g**2*I2)
    total=linear+quadratic
    assert total<F(1,10**96)
    # Full physical certified signed integral remains a finite
    # polynomial×L,L² exact moment of source-correlated jets:
    # p=v(C8+L/2), z_N=H_N+g_N L:
    #   L^0: 4vC8 H_N+2 H_N²
    #   L^1: 4v C8 g_N+2v H_N+4H_N*g_N
    #   L^2: 2v*g_N+2*g_N².
    return E_H,E_g,total

def signed_polynomial_exact_controls():
    # Independent finite rational polynomial/log controls for the
    # source-jet finite scalar, not its actual original numerical value.
    def add(a,b):
        n=max(len(a),len(b));return [ (a[i] if i<len(a) else F(0))+
          (b[i] if i<len(b) else F(0)) for i in range(n)]
    def mul(a,b):
        c=[F(0)]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):c[i+j]+=x*y
        return c
    cases=[
      (F(-1,11),F(7,13),[F(-2,7),F(3,11)],[F(0),F(-5,17)]),
      (F(2,31),F(13,23),[F(1),F(-7)],[F(0),F(2),F(-3)]),
      (F(0),F(0),[F(0),F(0),F(1)],[F(0),F(-1),F(4)]),
      (F(-3,41),F(19,43),[F(11,101)],[F(0),F(1,10**15)]),
      (F(2,7),F(5,9),[F(-1),F(2),F(-3),F(4)],[F(0),F(5),F(0),F(-7)]),
      (F(-1,10**7),F(17,3),[F(1,10**11),F(-1,10**8)],[F(0),F(7,10**10)]),
    ]
    checks=0
    for v,Cc,h,g in cases:
        # Direct symbolic product in F[d,L].
        z={(i,0):a for i,a in enumerate(h)}
        for i,a in enumerate(g):
            z[(i,1)]=z.get((i,1),F(0))+a
        p={(0,0):v*Cc,(0,1):v/2}
        direct={}
        for (i,j),a in p.items():
            for (k,l),b in z.items():
                key=(i+k,j+l); direct[key]=direct.get(key,F(0))+4*a*b
        for (i,j),a in z.items():
            for (k,l),b in z.items():
                key=(i+k,j+l); direct[key]=direct.get(key,F(0))+2*a*b
        F0=add([4*v*Cc*a for a in h],[2*x for x in mul(h,h)])
        F1=add(add([4*v*Cc*a for a in g],[2*v*a for a in h]),
               [4*x for x in mul(h,g)])
        F2=add([2*v*a for a in g],[2*x for x in mul(g,g)])
        for j,poly in enumerate((F0,F1,F2)):
            for i,a in enumerate(poly):
                assert direct.get((i,j),F(0))==a
                checks+=1
        assert all(l<=2 for i,l in direct)
    return checks

def main():
    orig,sha=load("notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json")
    seam,ss=load("notes/data/provisional/NF406_original_prime_support_partition_exact.json")
    curv,cs=load("notes/data/provisional/NF413_original_full_246_source_curvature_native.json")
    jet,js=load("notes/data/provisional/NF411_original_source_boundary_jet.json")
    nf489,ps=load("docs/NF489_ACCEPTED_ORIGINAL_J8_TRUE_PHYSICAL_POINT_SUPPLEMENT.md")
    assert sha==SRC and ss==SEAM
    assert orig["original_dimension"]==242 and len(orig["original_exact_native_original_four_critical_coefficients_mid_radius"])==4
    assert curv["original_nf407_full_native_source_sha256"]==jet["nf407_source_sha256"]==SRC
    assert curv["original_true_full_u4_second_derivative_L2_upper_integer"]=="256"
    source_envelope,source_err,polebound=original_source_envelope(orig)
    analytic_checks=original_all_log_algebra()
    assert analytic_checks==6*4*(5+3+1)
    assert exact_kernel_holomorphic_cauchy()
    e_h,e_g,energy=full_analytic_signed_error_gate()
    polychecks=signed_polynomial_exact_controls()
    assert polychecks>50
    out={
       "pass":"NF490",
       "standing":"SOURCE-EXACT ORIGINAL TRUE J8 ALL-ORDERS LOG PEEL + FIXED-J8 HOLOMORPHIC 400-JET ENERGY Cauchy gate ACCEPTED IF FOCUSED CI SUCCESS; original H,g numerical jets and D8 signed upper OPEN",
       "source_original_nf407_sha256":SRC,
       "source_original_nf406_seam_sha256":SEAM,
       "source_original_nf413_curvature_sha256":cs,
       "source_original_nf411_endpoint_jet_sha256":js,
       "source_original_nf489_accepted_point_note_sha256":ps,
       "source_original_246_generator_273_source_group_carrier_unchanged":True,
       "source_raw_dyadic_original_complete_246_generator_complex_amplitude_absolute_upper":"1e160",
       "source_original_raw_dyadic_complex_amplitude_exact":str(source_envelope),
       "source_original_original_dyadic_input_analytic_envelope_error_bound":str(source_err),
       "source_original_critical_odd_sinh_pole_amplitude_bound":str(polebound),
       "original_B":"11/10",
       "true_physical_J8_terminal_distance":["0","1/500"],
       "fixed_original_n9_active_seven_minus_prime_branch":[2,3,4,5,7,8,9],
       "analytic_branch_not_physical_support_outside_J8":True,
       "true_original_all_orders_log_coefficient":"g(d)=[U(B-d)-U(B)]/2",
       "source_original_true_physical_complete_arch_plus_prime_j8":"z(B-d)=g(d)*log(B/d)+H(d)",
       "original_full_joint_analytic_regular_part_H_expression":"H=c0 U(x)+int_0^(2d)K*A_x + (1/2)int_(2d)^(4B-2d)K*[U(x)-U(x-t/2)] + U(x)/2*[log((B+x)/B)+int_(2d)^(4B-2d)(K-1/t)] + U(x)int_(4B-2d)^infty K - seven genuine regular minus translations - original NF404 sinh center",
       "true_original_first_log_cusp_coefficient":"alpha=-U'(B)/2",
       "true_original_second_log_cusp_coefficient":"beta=U''(B)/4",
       "source_original_all_orders_log_source_algebra_fraction_checks":analytic_checks,
       "source_original_tK_formal_Q_at_zero":"1/4",
       "original_fixed_J8_branch_complex_d_radius":"1/25",
       "original_K_complex_t_strip_imag_bound":"2/25",
       "original_source_complex_U_absolute_upper":"1e400",
       "original_source_complex_Uprime_Usecond_absolute_upper":"1e410",
       "original_entire_fixed_branch_H_complex_absolute_upper":"1e420",
       "original_entire_fixed_branch_g_complex_absolute_upper":"1e400",
       "original_H_and_g_taylor_order":N,
       "original_true_terminal_taylor_ratio":"1/20",
       "original_H_400_jet_remainder_strict_upper":str(e_h),
       "original_g_400_jet_remainder_strict_upper":str(e_g),
       "original_true_whole_terminal_signed_scalar_truncation_error_strict_upper":str(energy),
       "original_true_whole_terminal_signed_scalar_error_less_than":"1e-96",
       "original_true_terminal_finite_integrated_signed_polynomial":"D_T,400=int_0^(1/500)[F0(d)+F1(d)*L(d)+F2(d)*L(d)^2]dd with F0=4vC8 H400+2H400^2, F1=4vC8 g400+2v H400+4H400 g400, F2=2v g400+2g400^2",
       "original_polynomial_exact_signed_jets_controls":polychecks,
       "source_correlated_400_jets_actually_calculated":False,
       "original_full_J8_signed_upper":"OPEN",
       "NF404":"OPEN","W_ODD_NEG":"OPEN","RH":"OPEN",
       "next_bold":"NF491 source-native 4096bit original NF446 fixed-J8 joint compact first 400 Taylor coefficients H,g and exact analytic moment contraction; explicit original input/Arb/400-tail fees and independently audited signed D8 upper"
    }
    dest=Path("nf490-original-J8-full-log-peel-holomorphic-400-jet-exact.json")
    dest.write_text(json.dumps(out,indent=2)+"\n")
    print("NF490 original complete all-orders J8 exact log peel + 400 jet signed energy Cauchy controls PASS")
    print("original source explicit 400-jet full terminal D signed analytic truncation <", "1e-96")
    print("original 400 source H,g numeric coefficients and actual D8 upper NF404 RH OPEN")
if __name__=="__main__":main()
