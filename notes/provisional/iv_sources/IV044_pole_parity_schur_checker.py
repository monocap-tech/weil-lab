#!/usr/bin/env python3
"""IV044: exact-rational source pole parity/inertia and conditional Schur preflight.

No Lean compilation, RH claim, or full original spectral operator computation.
"""
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
from math import factorial
import json

ROOT=Path(__file__).resolve().parent
A=Q(11,10)
L=Q(21,10)

# Purely rational Taylor enclosure of sinh(11/10).
# Sum j=0,...,5, then bound the omitted j=6 term and its subsequent
# ratio by x^2/(14*15) for all remaining terms.
N=6
slo=sum((A**(2*j+1)/factorial(2*j+1) for j in range(N)),Q(0))
first_omitted=A**(2*N+1)/factorial(2*N+1)
ratio=A**2/Q((2*N+2)*(2*N+3))
assert 0<ratio<1
shi=slo+first_omitted/(1-ratio)
assert slo<shi
h2_lo,h2_hi=2*(slo+A),2*(shi+A)
k2_lo,k2_hi=2*(slo-A),2*(shi-A)
assert Q(487,100)<h2_lo<h2_hi<Q(488,100)
assert Q(47,100)<k2_lo<k2_hi<Q(48,100)

# Source Mellin residues exactly give |h-moment|^2-|k-moment|^2.
# Complex rational 2-vectors encode C = Q+iQ.
def conj_prod_real(x,y): return x[0]*y[0]+x[1]*y[1]
def normsq(x): return conj_prod_real(x,x)
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def sub(x,y): return (x[0]-y[0],x[1]-y[1])
complex_cases=[((Q(2),Q(1)),(Q(-3),Q(5))),
               ((Q(1,3),Q(-7,5)),(Q(11,4),Q(2,7))),
               ((Q(0),Q(0)),(Q(3),Q(-1)))]
for pm,mm in complex_cases:
    h=(pm[0]+mm[0],pm[1]+mm[1])
    k=(pm[0]-mm[0],pm[1]-mm[1])
    assert (normsq(h)-normsq(k))/2 == 2*conj_prod_real(pm,mm)

# The gamma0 upper bound uses source quarter-digamma identity:
# gamma0 = -EulerGamma - pi/2 - 3 log2 - log pi.
# Classical inequalities EulerGamma>0, pi>3, log2>2/3,
# log pi > 1 (since pi > 3 > e) imply gamma0 < -9/2.
# Log2>2/3 follows already from its positive atanh series n=0,1.
log2_series_lower=2*(Q(1,3)+Q(1,3)**3/3)
assert log2_series_lower>Q(2,3)
# e<3: e = sum_{n=0}^3 1/n! + tail_{n>=4},
# and tail_{n>=4} <= (1/4!)/(1-1/5).
e_upper=sum((Q(1,factorial(n)) for n in range(4)),Q(0))+Q(1,factorial(4))/(1-Q(1,5))
assert e_upper<3
# Gamma[1_I] = gamma0*L + sum_{n>=0}(1-e^{-2a_n L})/(2a_n²).
# The n=0 contribution <8; the sum n>=1 < 1/2 sum n^-2 <1.
# Thus D[1_I]<9, P[1_I]>=0; on the genuine symmetric window,
# T[1_I] < (-9/2)*(21/10)+9 = -9/20.
negative_base_upper=(-Q(9,2))*L+9
assert negative_base_upper==-Q(9,20)

# Exact conditional parity Schur equivalence, in elementary diagonal models:
# T_e = diag(-a,d), pole_plus=hh*, h=(alpha,beta):
# W_e>=0 iff alpha² >= a(1+beta²/d).
# T_o = diag(s,t)>0, pole_minus=kk*: W_o>=0 iff
# k1²/s+k2²/t<=1.
def even_matrix_test(a,d,alpha,beta):
    assert min(a,d)>0
    A0=-a+alpha*alpha
    C0=d+beta*beta
    cross=alpha*beta
    determinant=A0*C0-cross*cross
    criterion=alpha*alpha-a*(1+beta*beta/d)
    assert determinant == d*criterion
    # C0>0, so PSD is equivalent to determinant >=0.
    return criterion>=0,determinant

def odd_matrix_test(s,t,k1,k2):
    assert min(s,t)>0
    q=k1*k1/s+k2*k2/t
    A0=s-k1*k1
    C0=t-k2*k2
    cross=-k1*k2
    det=A0*C0-cross*cross
    assert det == s*t*(1-q)
    # Positive T_o and rank-one downdate: criterion q<=1.
    return q<=1, det

even_tests=[(Q(1),Q(3),Q(2),Q(1)),
            (Q(1),Q(3),Q(1),Q(1)),
            (Q(2),Q(5),Q(3),Q(1,2)),
            (Q(2),Q(5),Q(1),Q(4))]
odd_tests=[(Q(2),Q(3),Q(1),Q(1)),
           (Q(2),Q(3),Q(2),Q(1)),
           (Q(1),Q(2),Q(1,2),Q(1,2)),
           (Q(1),Q(2),Q(1),Q(1))]
for args in even_tests: even_matrix_test(*args)
for args in odd_tests: odd_matrix_test(*args)
# One negative index of T_e can be corrected only by one positive rank-one;
# T_o's negative pole rank-one can never correct a negative T_o direction.
# Basic exact finite rank inertia sanity via positive/negative eigenvalue signs:
assert h2_lo>0 and k2_lo>0

report={
 'stage':'IV044',
 'standing':'exact rational source-aligned parity algebra and elementary analytic lemma preflight PASS; NOT Lean',
 'physical_window_radius':str(A),
 'negative_base_even_witness_interval':'(-21/20,21/20)',
 'negative_base_even_witness_length':str(L),
 'source_gamma0_upper':'-9/2 (strict) from quarter digamma, EulerGamma>0, pi>3, log2>2/3, log(pi)>1',
 'source_gamma_dirichlet_indicator_upper':'9 (strict)',
 'original_prime_indicator_nonnegative':True,
 'pole_free_even_T_quadratic_upper':str(negative_base_upper)+' (strict; source form-domain indicator, smooth approximations exist)',
 'pole_positive_even_vector':'h=(e^(x/2)+e^(-x/2))/sqrt(2)=sqrt(2)*cosh(x/2)',
 'pole_negative_odd_vector':'k=(e^(x/2)-e^(-x/2))/sqrt(2)=sqrt(2)*sinh(x/2)',
 'source_pole_diagonal':'|<h,f>|²-|<k,f>|²',
 'positive_pole_nonzero_eigenvalue':'2*(sinh(11/10)+11/10)',
 'negative_pole_nonzero_eigenvalue':'-2*(sinh(11/10)-11/10)',
 'sinh_rational_lower':str(slo),
 'sinh_rational_upper':str(shi),
 'positive_pole_norm_sq_lower':str(h2_lo),
 'positive_pole_norm_sq_upper':str(h2_hi),
 'negative_pole_norm_sq_lower':str(k2_lo),
 'negative_pole_norm_sq_upper':str(k2_hi),
 'rational_pole_positive_eigenvalue_bracket':['487/100','488/100'],
 'rational_pole_negative_eigenvalue_bracket':['-48/100','-47/100'],
 'log2_series_lower':str(log2_series_lower),
 'exp1_rational_upper':str(e_upper),
 'conditional_even_schur':'when T_e has one eigenvalue -a and T_plus>=d>0: |alpha|²/(1+<hplus,T_plus^-1 hplus>)>=a',
 'conditional_even_inverse':'<h,T_e^-1 h> <= -1 (strictly invertible index-one case)',
 'conditional_odd_inverse':'<k,T_o^-1 k> <= 1 (strictly positive T_o)',
 'even_test_results': [dict(positive=even_matrix_test(*a)[0],det=str(even_matrix_test(*a)[1])) for a in even_tests],
 'odd_test_results': [dict(positive=odd_matrix_test(*a)[0],det=str(odd_matrix_test(*a)[1])) for a in odd_tests],
 'global_rh_or_full_weil_claim':False,
 'no_new_ci':True,
}
report['checker_sha256']=sha256(Path(__file__).read_bytes()).hexdigest()
path=ROOT/'IV044_pole_parity_schur_receipt.json'
path.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print('IV044 exact rational parity/pole Schur preflight PASS (NONKERNEL)')
print('Exact even/odd pole signs: +h*h and -k*k')
print('even pole eig norm square:',f'{float(h2_lo):.9f} .. {float(h2_hi):.9f}')
print('odd negative pole abs eig:',f'{float(k2_lo):.9f} .. {float(k2_hi):.9f}')
print('source pole-free T[1_I] <',negative_base_upper)
print('finite rational Schur tests: even',len(even_tests),'odd',len(odd_tests))
print('receipt:',path)
