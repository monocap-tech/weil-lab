#!/usr/bin/env python3
"""Weil-Lab IV040 analytic-only exact finite arithmetic checker.

Checks the 144-term NF599 positive gain at t=150 by small-integer
outward floors, the source's finite prime norm universal bound,
and signed local Weil coefficient improvements. No Lean proof or
full functional-analysis compiler assertion is made.
"""
from fractions import Fraction as Q
from math import isqrt
from pathlib import Path
import subprocess
import sys
import hashlib
import json

HERE=Path(__file__).resolve().parent
OUT=HERE/'IV040_gamma_cutoff_optimization_receipt.json'
SCALE=10**4
N=144
T=150
C=Q(281,100)
GLOBAL_GAMMA_LO= -Q(28,5)
FREQ_HALF_BAND=25
POLE_PER_MU=Q(8)
TOP_4_UPPER=Q(46657,40000)
LAMBDA_3_UPPER=Q(11,10)

# Exact integer conversion of NF599's gain at t=150:
# a_n = n + 1/4 = (4n+1)/4, z=(t/2)^2=5625.
# g_a(t) = 360000 / [(4n+1)*((4n+1)^2+90000)].
def gain_denom(n):
    k=4*n+1
    return k*(k*k+90000)

def log_bounds(n,terms=96):
    y=Q(n-1,n+1)
    summ=sum((2*y**(2*k+1)/Q(2*k+1) for k in range(terms)),Q(0))
    error=(2*y**(2*terms+1)/Q(2*terms+1))/(1-y*y)
    return summ,summ+error

def round_upper(q,denom):
    a=q*denom
    return Q(-(-a.numerator//a.denominator),denom)

def sqrt_lower(n,denom=10**10):
    # square of floor sqrt(n*denom^2) <= n*denom^2
    k=isqrt(n*denom*denom)
    assert Q(k,denom)**2<=n
    return Q(k,denom)

def main():
    floors=[]
    for n in range(N):
        d=gain_denom(n)
        floors.append((360000*SCALE)//d)
        assert Q(floors[-1],SCALE)<=Q(360000,d)
    floor_total=sum(floors)
    floor_bound=Q(floor_total,SCALE)
    exact_gain_sum=sum((Q(360000,gain_denom(n)) for n in range(N)),Q(0))
    assert floor_total==84175,(floor_total,'independent stable integer receipt changed')
    assert exact_gain_sum>=floor_bound>Q(42,5)
    gamma_lower=GLOBAL_GAMMA_LO+floor_bound
    assert gamma_lower==Q(28175,10000) and gamma_lower>C
    # Outside (-25,25), |-2πξ|>=50π>150 using π>3.
    assert 2*FREQ_HALF_BAND*3==T
    coeff=(C-GLOBAL_GAMMA_LO)*2*FREQ_HALF_BAND + POLE_PER_MU
    assert coeff==Q(857,2)
    # Original real window [-11/10,11/10] only n<=9 can translate;
    # positive von-Mangoldt indices 2,3,4,5,7,8,9.
    active=[(2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3)]
    norm_upper=Q(0)
    terms={}
    for n,p in active:
        _,upper=log_bounds(p)
        u=round_upper(upper,10**10)
        sq=sqrt_lower(n)
        norm_upper += 2*u/sq
        terms[str(n)]={'lambda_log_p_upper':str(u),'sqrt_n_lower':str(sq)}
    # All seven active genuine Λ(n)/√n, with both shift signs.
    assert norm_upper<Q(71,10),float(norm_upper)
    # Source accepted IV039 rational upper spectral bracket for 4-fiber n2 leaf.
    cases={
       'original_triangle_B':(Q(3,5000),LAMBDA_3_UPPER),
       'IV038_prime_isolated_four_cell':(Q(11,10000),LAMBDA_3_UPPER),
       'IV038_fully_n2_attached_four_cell':(Q(1,1250),TOP_4_UPPER),
       'IV039_anchored_largest_tested_r':(Q(17,20000),TOP_4_UPPER),
       'IV039_old_gate_failure_r_0_000205':(Q(3,5000)+Q(41,200000),TOP_4_UPPER),
       'IV039_sliding_n2_separated':(Q(1,1250),LAMBDA_3_UPPER),
    }
    bound={key:C-coeff*mu-upper for key,(mu,upper) in cases.items()}
    # All > 1, in particular every observed IV039 collision is safely positive.
    assert all(m>1 for m in bound.values()),bound
    assert bound['IV039_anchored_largest_tested_r']==Q(25587,20000)
    assert bound['IV038_fully_n2_attached_four_cell']==Q(52031,40000)
    assert bound['IV039_old_gate_failure_r_0_000205']>Q(129,100)

    # Exact universal small-support form criterion for any prescribed margin H:
    # for source real gamma(t) -> +∞, choose M > H + Cprime, then choose
    # μ < (M-Cprime-H)/(2K(M+28/5)+8) for corresponding finite K.
    # The full qualitative proof needs NF599's infinite positive gain monotonicity;
    # arithmetic here confirms a fixed instance and the finite prime-norm bound.
    result={
      'stage':'IV040',
      'source':'original Zeta23 signed Gamma - prime + two Hermitian pole terms',
      'standing':'analytical derivation, exact-rational preflight PASS; NOT Lean kernel',
      'source_gamma_lean_functions':['neutralNF599GammaLower_partial','neutralNF599GammaZero_lower','neutralNF599Gain_mono_sq'],
      'gamma_test_t':T,
      'number_of_rational_gain_terms':N,
      'NF599_gain_integer_numerator':360000,
      'NF599_gain_integer_denominator':'(4n+1)*((4n+1)^2+90000)',
      'integer_floor_scale':SCALE,
      'integer_sum_of_144_floors':floor_total,
      'sum_gain_floor_lower':str(floor_bound),
      'gamma_150_lower_via_floor_and_gamma0':str(gamma_lower),
      'chosen_strict_gamma_cutoff':str(C),
      'fourier_low_band':'(-25,25)',
      'true_gamma_global_lower':'-28/5',
      'true_source_two_poles_coefficient':str(POLE_PER_MU),
      'full_signed_support_measure_coefficient':str(coeff),
      'new_capacity_gate':'lambda_plus(E) + (857/2)*measure(E) < 281/100',
      'cases_positive_margin_lower_unchanged_source':{key:{'measure':str(cases[key][0]),'prime_upper':str(cases[key][1]),'weil_lower_coefficient':str(m)} for key,m in bound.items()},
      'universal_active_prime_indices':[n for n,_ in active],
      'uniform_original_prime_two_direction_norm_bound_rational_upper':str(norm_upper),
      'universal_prime_norm_below':'71/10',
      'universal_small_measure_weil_margin_diverges_conceptual_lemma':'mathematical argument only, not a finite preflight proof',
      'IV039_critical_width_is_only_old_sufficient_bound_failure':True,
      'IV039_eigenvalue_jump_still_valid':True,
      'not_global_Weil_positivity_or_RH':True,
      'new_repo_branch_commit_pr_workflow':False,
    }
    result['checker_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    OUT.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n',encoding='utf8')
    print('IV040 exact-rational NF599 Gamma cutoff preflight PASS — NONKERNEL')
    print(f'144 gains integer floor lower {floor_total}/{SCALE} > 42/5; gamma >= {gamma_lower} > 281/100')
    print('new source support-capacity coefficient:',coeff)
    for key,m in bound.items():
        print(f' {key}: signed Weil > {m} × L2 mass ({float(m):.8f})')
    print(f'universal n2..n9 prime operator norm < 71/10: checked ({float(norm_upper):.9f})')
    print('receipt:',OUT)

if __name__=='__main__':main()
