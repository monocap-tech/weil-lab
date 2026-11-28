#!/usr/bin/env python3
"""IV049 exact-rational audit: original signed Weil single-cell energy-relative Schur bound.

ANALYTICAL PRE-FLIGHT ONLY (NONKERNEL). Fraction/Taylor/integer identities are
machine-checked here; continuum Gamma Fourier inversion, form-domain closure,
Poincare, operator representation, and limit theorem live in the proof report.
No repository or CI operations.
"""
from fractions import Fraction as F
from hashlib import sha256
from math import factorial
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'IV049_energy_relative_cell_schur_receipt.json'
EXPECTED = {
  'IV047_infinite_dim_high_mode_checker.py': 'd64d8b08529e529a1be86923d25d2a76ce81aa42889eab97257c5f6aa0e083a5',
  'IV048_mixed_block_nonvanishing_checker.py': '30c34d3832199bba83fff87527ab8d42852ace0839d1d08dfe4ea1a02a72e3c6',
  'IV044_pole_parity_schur_checker.py': 'b2142d08a295819bd27e554e23c91e7ba774e5fcfa29920c23f1c990ec5a5b1f',
}
for filename, expected in EXPECTED.items():
    observed = sha256((ROOT / filename).read_bytes()).hexdigest()
    assert observed == expected, (filename, observed, expected)

# Exact exp(x) interval, 0<x<=11/10: first N terms and strictly
# geometric tail using the post-N term ratio x/(N+2)<1.
def exp_bounds(x: F, N: int = 24):
    s = sum((x**n/F(factorial(n)) for n in range(N+1)), F(0))
    nxt = x**(N+1)/F(factorial(N+1))
    assert x < N+2
    return s, s + nxt/(1 - x/F(N+2))

def sinh_bounds(x: F):
    e_lo,e_hi=exp_bounds(x)
    return (e_lo-1/e_lo)/2, (e_hi-1/e_hi)/2

def cosh_bounds(x: F):
    e_lo,e_hi=exp_bounds(x)
    return (e_lo+1/e_hi)/2, (e_hi+1/e_lo)/2

sinh_11 = sinh_bounds(F(11,10))
cosh_055 = cosh_bounds(F(11,20))
sinh_055 = sinh_bounds(F(11,20))
assert 2*(sinh_11[1]+F(11,10)) < 5    # ||h||^2<5
assert 2*(sinh_11[1]-F(11,10)) < F(1,2) # ||k||^2<1/2
assert cosh_055[1] < F(4,3)            # ||h||_infty< (3/2)(4/3)=2
assert sinh_055[1] < F(2,3)            # ||k||_infty< (3/2)(2/3)=1
assert (F(3,2)**2)>2 and (F(9,4)**2)>5 and (F(3,4)**2)>F(1,2)
assert 2*F(9,4)+F(3,4) < 6

# Uniform bound for Q Gamma e_J, derived from the original Gamma
# positive physical kernel (proof in report):
# ||Q Gamma e||^2 <= (1+2w)^2 + int_0^infinity log^2(1+1/u)du + (44/5)w.
# Elementary integral upper < 489/100 via ln2<7/10,
# split u in (0,1] and [1,infinity), so no numerical pi integral.
wcap = F(1,1000)
log2_cap=F(7,10)
log_integral_cap=log2_cap**2+2*log2_cap+3
assert log_integral_cap == F(489,100)
gamma_sq_cap=(1+2*wcap)**2 + log_integral_cap+F(44,5)*wcap
assert gamma_sq_cap < F(5,2)**2
# For w<=1/1000, pole vector of e_J has norm <6 sqrt(w)<1/5.
assert 6**2*wcap < F(1,5)**2
assert F(5,2) + F(71,10) + F(1,5) == F(49,5) < 10

# Half of the original exact mixed logarithm is atanh(z), z=11/43.
# Rigorous elementary upper bound: atanh(z) <= sum(z^(2j+1)/(2j+1))
# + z^(2N+1)/((2N+1)(1-z^2)), and > sum.
z=F(11,43)
terms=6
atanh_low=sum((z**(2*j+1)/F(2*j+1) for j in range(terms)), F(0))
atanh_hi=atanh_low+z**(2*terms+1)/(F(2*terms+1)*(1-z*z))
assert atanh_low>F(11,43)
assert atanh_hi < F(131,500) # actual ~0.261624

# Genuine NF599 positive physical atom bound for ANY unit test supported
# in a cell J (no n>=2 shift can intersect J):
# W[q] > -28/5 + sum_{n<N}4/(4n+1) - (N+8)w.
# Floor-sum supplies an exact rational LOWER bound (no float rounding).
N=32768
scale=10**6
floor_sum=sum((4*scale)//(4*n+1) for n in range(N))
assert floor_sum==14608246
harmonic_rational_lower=F(floor_sum,scale)
results={}
for M in (100000,132000):
    w=F(11,5*M)
    assert w<=wcap
    cell_energy_lower = -F(28,5) + harmonic_rational_lower - (N+8)*w
    parity_energy_lower = cell_energy_lower-11*w
    assert cell_energy_lower>F(207,25), (M,cell_energy_lower)
    assert parity_energy_lower>F(207,25), (M,parity_energy_lower)
    # W(e,q)= -atanh(11/43)+eps, |eps|<=10w,
    # and reflected parity pair gives |eps|<=21w.
    single_mixed_abs_upper = atanh_hi +10*w
    parity_mixed_abs_upper= atanh_hi+21*w
    assert single_mixed_abs_upper < F(131,500), (M,single_mixed_abs_upper)
    assert parity_mixed_abs_upper < F(263,1000), (M,parity_mixed_abs_upper)
    # For a SPECIFIC central-contrast high direction q only, the
    # positive Schur decrement |W(e,q)|^2/W(q) is bracketed.
    # Lower bracket is IV048's actual previous strictly positive loss;
    # upper bracket is new energy-normalized source support gain.
    single_loss_upper=F(131,500)**2 / F(207,25)
    parity_loss_upper=F(263,1000)**2 / F(207,25)
    assert F(1,2128)<single_loss_upper<F(1,100)
    assert F(1,4240)<parity_loss_upper<F(1,100)
    results[str(M)]={
      'width':str(w),
      'true_NF599_32768_gain_floor_lower':str(harmonic_rational_lower),
      'original_W_central_contrast_strict_lower':str(cell_energy_lower),
      'original_W_reflected_parity_contrast_strict_lower':str(parity_energy_lower),
      'absolute_original_W_low_high_coupling_upper':str(single_mixed_abs_upper),
      'absolute_original_W_parity_low_high_coupling_upper':str(parity_mixed_abs_upper),
      'single_high_direction_Schur_loss_strict_interval':[
        str(F(1,2128)),str(single_loss_upper)],
      'reflected_parity_high_direction_Schur_loss_strict_interval':[
        str(F(1,4240)),str(parity_loss_upper)],
      'decimal_Schur_upper_single_illustration':format(float(single_loss_upper),'.10f'),
      'decimal_Schur_upper_parity_illustration':format(float(parity_loss_upper),'.10f'),
    }

receipt={
    'stage':'IV049',
    'status':'exact rational / Taylor / integer preflight PASS; continuum/operator statements mathematical NONKERNEL',
    'original_source_sign':'W=Gamma-P_original+|<h,f>|²-|<k,f>|²',
    'analytic_global_Gamma_test':'K(s)<=1/(2s)+1 all s>0; ||Q Gamma e_J||^2 <25/4 all w<=1/1000',
    'log_integral_upper':'489/100 from ln2<7/10 and elementary integrals',
    'pole_and_prime_test':'||Q pole e||<6sqrt(w)<1/5 and ||P||<71/10',
    'single_cell_full_mixed_operator_upper':'||Q W e_J||<49/5<10, uniformly in mesh location',
    'conditional_energy_relative_bound':'0<=b_M(e_J)=sup_{q in Q_M} |W(e_J,q)|²/W(q) < (49/5)^2/c_M, where c_M=inf_{q in Q_M, ||q||=1}W(q)>0',
    'asymptotic_form_statement':'c_M->infinity as w=11/(5M)->0, from source gamma(t)->infinity and (2Rw)^2 Fourier concentration. Hence sup_J b_M(e_J)->0. Does not show ||C_Q^-1/2 B||->0.',
    'finite_N':N,
    'NF599_integer_gain_floor_scale':scale,
    'NF599_integer_gain_floor_sum':floor_sum,
    'half_log_source_argument':'atanh(11/43)=0.5 log(27/16)',
    'half_log_rational_bracket':[str(atanh_low),str(atanh_hi)],
    'mesh_cases':results,
    'formalization_gaps':['NF599 finite source inverse Fourier identity attached to IV011','closed Gamma form/operator domains and sharp-cell projections','high-mode source form closure and c_M growth','entire low-block Schur correction including dense cell combinations'],
    'no_new_CI':True,
    'predecessor_SHA256':EXPECTED,
}
receipt['checker_SHA256']=sha256(Path(__file__).read_bytes()).hexdigest()
OUT.write_text(json.dumps(receipt,sort_keys=True,indent=2)+'\n')
print('IV049 original signed energy-relative cell Schur exact preflight PASS — NONKERNEL')
print('uniform single column ||Q W e_J||<49/5; c_M grows to infinity, so individual energy-relative Schur cost tends to zero')
print('NF599 floor-sum 32768:',floor_sum)
for k,r in results.items():
    print('M',k,'w',r['width'],'W[q]>',r['original_W_central_contrast_strict_lower'],
          'parity W[q]>',r['original_W_reflected_parity_contrast_strict_lower'])
    print('  single Schur loss between',*r['single_high_direction_Schur_loss_strict_interval'],
          '; parity between',*r['reflected_parity_high_direction_Schur_loss_strict_interval'])
print('sha256:',receipt['checker_SHA256'])
print('receipt:',OUT)
