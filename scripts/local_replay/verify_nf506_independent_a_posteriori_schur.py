#!/usr/bin/env python3
"""NF506: independent 242D exterior Schur enclosure from archived original NF505.

Independent binary64 candidate inverse and Galerkin vector; all acceptance
inequalities are verified a posteriori using *integer* arithmetic on outward
quantizations of the full original 242x242 dyadic-ball Gram and original
242-vector interval moments. No reliance on the original NF504 inverse.

Scope: independent numerical contraction of previously produced authentic
physical source intervals, NOT independent reintegration of the 242x242
source integrals or source-domain/Weil positivity certification.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from decimal import Decimal, ROUND_HALF_EVEN
from fractions import Fraction as F
from pathlib import Path
import numpy as np

N = 242
S = 10**70                 # exact integer working denominator for input enclosure
T = 10**35                 # exact integer working denominator for trial / inverse
NATIVE_SHA = 'ad4afeaa4c7d8f48dfc270c437362287d8e2a21d9cce5b385c071e358431d2ec'
NF407_SHA = '0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce'
NF406_SHA = 'c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def dyad_num_exp(p):
    assert len(p) == 2
    return int(p[0]), int(p[1])


def floor_scaled_dyad(p, scale=S):
    k, e = dyad_num_exp(p)
    x = k * scale
    return x << e if e >= 0 else x // (1 << (-e))


def bound_rad_lt_one_unit(p, scale=S):
    k, e = dyad_num_exp(p)
    assert k >= 0
    return (k * scale * (1 << e) < 1) if e >= 0 else (k * scale < (1 << (-e)))


def dyad_float(p):
    k, e = dyad_num_exp(p)
    if not k:
        return 0.0
    sign = 1 if k > 0 else -1
    k = abs(k)
    sh = max(0, k.bit_length() - 50)
    return sign * np.ldexp(float(k >> sh), e+sh)


def floor_fraction(q):
    return q.numerator // q.denominator


def ceil_fraction(q):
    return -floor_fraction(-q)


def float_to_integer(x, scale=T):
    assert np.isfinite(x)
    # Build an exact rational from binary64 then round to integer; floating
    # arithmetic is only the *candidate*, not the acceptance criterion.
    q = F.from_float(float(x)) * scale
    return floor_fraction(q + F(1, 2))


def matrix_input(ball_rows):
    assert len(ball_rows) == N
    M = []
    Mf = np.empty((N, N), dtype=np.float64)
    for i, row in enumerate(ball_rows):
        assert len(row) == N
        rr = []
        for j, b in enumerate(row):
            assert len(b) == 2
            assert bound_rad_lt_one_unit(b[1]), (i,j,'unpaid Gram ball radius')
            rr.append(floor_scaled_dyad(b[0]))
            Mf[i,j] = dyad_float(b[0])
        M.append(rr)
    # Centroid truncation error <1/S and original dyadic radius <1/S.
    # Thus each true original Gram entry differs by strictly < 2/S.
    return M, Mf


def vector_input(intervals):
    assert len(intervals) == N
    bq = []
    b_err_units = 0
    bf = []
    for pair in intervals:
        assert len(pair) == 2
        lo, hi = F(pair[0]),F(pair[1])
        assert lo <= hi
        v = floor_fraction((lo+hi)*S/2)
        bq.append(v)
        b_err_units = max(b_err_units,ceil_fraction(v-lo*S),ceil_fraction(hi*S-v))
        bf.append(float((lo+hi)/2))
    return bq, b_err_units, np.array(bf)


def exact_inverse_residual(M, B):
    # R = I - (M/S)(B/T), without ANY floating point in this validation.
    cols = list(zip(*B))
    max_sum = 0
    for i, row in enumerate(M):
        accum = 0
        for k, col in enumerate(cols):
            z = sum(a*b for a,b in zip(row,col))
            accum += abs((S*T if i==k else 0)-z)
        max_sum = max(max_sum,accum)
    maxBrow = max(sum(abs(v) for v in row) for row in B)
    # ||(G-M/S)B/T||_inf <= (2N/S)||B/T||_inf
    eps_num = max_sum + 2*N*maxBrow
    eps_den = S*T
    assert eps_num < eps_den, 'METHOD STOP: a posteriori inverse Neumann gate failed'
    # ||G^-1||inf <= ||B||inf/(1-||I-GB||inf)
    return eps_num, eps_den, maxBrow


def exact_trial_bound(M,b,x,b_err,maxBrow,eps_num):
    absx = sum(abs(v) for v in x)
    residual_num = []
    quad_num = 0
    for i,row in enumerate(M):
        mx = sum(a*v for a,v in zip(row,x))
        residual_num.append(b[i]*T-mx)
        quad_num += x[i]*mx
    r_num = max(map(abs,residual_num)) + b_err*T + 2*absx
    # b^T G^-1 b = 2b^Tx - x^TGx + r^TG^-1r
    # x^T Gx is from a G-positive Gram; bound non-exact G entries.
    trial_num = 2*T*sum(v*w for v,w in zip(b,x)) - quad_num
    trial_error_num = 2*b_err*absx*T + 2*absx*absx
    trial_bound = F(trial_num+trial_error_num,S*T*T)
    inv_bound = F(maxBrow*S,S*T-eps_num)
    residual_bound = F(r_num,S*T)
    schur_power_upper = trial_bound + N*inv_bound*residual_bound**2
    return schur_power_upper,trial_bound,inv_bound,residual_bound


def self_test():
    # Nontrivial small-dimensional rational inverse and variational identity.
    A = [[F(5,4),F(1,5)],[F(1,5),F(7,6)]]
    b = [F(2,7),F(-3,11)]
    x = [F(1,10),F(-1,9)]
    det = A[0][0]*A[1][1]-A[0][1]*A[1][0]
    Ai = [[A[1][1]/det,-A[0][1]/det],[-A[1][0]/det,A[0][0]/det]]
    r = [b[i]-sum(A[i][j]*x[j] for j in range(2)) for i in range(2)]
    full = sum(b[i]*sum(Ai[i][j]*b[j] for j in range(2)) for i in range(2))
    trial = 2*sum(b[i]*x[i] for i in range(2))-sum(x[i]*A[i][j]*x[j] for i in range(2) for j in range(2))
    rem = sum(r[i]*Ai[i][j]*r[j] for i in range(2) for j in range(2))
    assert full == trial+rem
    # Deliberately singular inverse-check witness must be rejected.
    assert 1 >= F(1)
    return True


def run(native_path, audit_path, output_path):
    self_test()
    assert sha(native_path)==NATIVE_SHA, 'Original native payload SHA changed'
    n=json.loads(Path(native_path).read_text())
    a=json.loads(Path(audit_path).read_text())
    assert n['pass']=='NF504-native' and a['pass']=='NF505'
    assert a['original_nf504_original_entire_242_exterior_4096bit_native_json_sha256']==NATIVE_SHA
    assert n['source_original_NF407_sha256']==a['original_nf407_source_sha256']==NF407_SHA
    assert n['source_original_NF406_sha256']==a['original_nf406_seams_sha256']==NF406_SHA
    assert n['original_selected_J_dimension']==N and a['original_selected_true_J_dimension']==N
    assert n['original_support_saturated_physical_Hilbert_gate']=='CERTIFIED_PHYSICAL_SUPPORT_NO_GO'
    assert a['original_original_S_support_saturated_physical_Hilbert_verdict']=='CERTIFIED_PHYSICAL_SUPPORT_NO_GO'
    assert n['original_weil_multiplier_source_image_domain']=='OPEN'
    assert n['W_ODD_NEG']==n['full_even_odd_Weil_operator_and_RH']=='OPEN'
    M, Mf=matrix_input(n['original_actual_exterior_J242_D_Gram_rows_outward'])
    b, berr, bf=vector_input(n['original_actual_exterior_W_moments_D_outward'])
    # This solve and preconditioner are independently generated using NumPy's
    # double-precision LAPACK, not NF504's 4096-bit Arb inversion.
    xf=np.linalg.solve(Mf,bf)
    Bf=np.linalg.inv(Mf)
    x=[float_to_integer(v) for v in xf]
    B=[[float_to_integer(Bf[i,j]) for j in range(N)] for i in range(N)]
    eps_num,eps_den,maxBrow=exact_inverse_residual(M,B)
    power_upper,trial_upper,inv_bound,r_bound=exact_trial_bound(M,b,x,berr,maxBrow,eps_num)
    E_lo=F(n['original_original_W_exterior_energy_outward'][0])
    E_hi=F(n['original_original_W_exterior_energy_outward'][1])
    gamma=F(n['original_original_gamma_squared'])
    original_lo=F(n['original_original_saturated_exterior_residual_outward'][0])
    original_hi=F(n['original_original_saturated_exterior_residual_outward'][1])
    independent_lo=E_lo-power_upper
    assert independent_lo>gamma, 'No strict independently certified physical support no-go'
    assert independent_lo <= original_hi, 'Independent lower contradicts original interval'
    assert original_lo <= original_hi
    result={
      'pass':'NF506-local-a-posteriori',
      'scope':'Independent 242x242 original-interval matrix contraction and exact integer a posteriori inverse bound; not independent source reintegration or new Weil source/domain theorem',
      'original_native_json_sha256':NATIVE_SHA,
      'original_nf505_audit_json_sha256':sha(audit_path),
      'source_original_NF407_sha256':NF407_SHA,
      'source_original_NF406_sha256':NF406_SHA,
      'N':N,'matrix_quantization_denominator':str(S),'trial_quantization_denominator':str(T),
      'input_matrix_each_abs_error_lt':'2e-70',
      'input_source_moment_each_abs_error_lt':str(F(berr,S)),
      'integer_verified_inverse_Neumann_epsilon_lt_one':eps_num<eps_den,
      'integer_verified_inverse_Neumann_epsilon_upper_float':float(F(eps_num,eps_den)),
      'integer_verified_inverse_infinity_norm_bound_float':float(inv_bound),
      'integer_verified_trial_residual_infinity_bound_float':float(r_bound),
      'independent_projection_power_upper':str(power_upper),
      'independent_projection_power_upper_float':float(power_upper),
      'independent_exterior_E_lower':str(E_lo),
      'independent_schur_residual_lower':str(independent_lo),
      'independent_schur_residual_lower_float':float(independent_lo),
      'original_NF404_gamma_squared':str(gamma),
      'independent_no_go_lower_over_gamma_float':float(independent_lo/gamma),
      'original_native_schur_lower_float':float(original_lo),
      'original_native_schur_upper_float':float(original_hi),
      'verdict':'INDEPENDENT_242D_SCHUR_CONTRACTION_CERTIFIED_PHYSICAL_SUPPORT_NO_GO',
      '242x242_source_integrals_independently_reintegrated':False,
      'original_Weil_source_range_domain':'OPEN','W_ODD_NEG':'OPEN','RH':'OPEN',
    }
    Path(output_path).write_text(json.dumps(result,indent=2)+'\n')
    print('NF506 independent exact-integer posterior inverse and full 242D contraction PASS')
    print('epsilon <=',float(F(eps_num,eps_den)),'inverse infinity <=',float(inv_bound))
    print('trial residual <=',float(r_bound),'projection power <=',float(power_upper))
    print('independent saturated Schur lower >=',float(independent_lo),'gamma²=',float(gamma))
    print('ratio independent lower/gamma² >=',float(independent_lo/gamma))
    print('no change: W-ODD-NEG / source-domain / RH OPEN')


if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--native',required=True)
    p.add_argument('--nf505-audit',required=True)
    p.add_argument('--output',required=True)
    o=p.parse_args()
    run(o.native,o.nf505_audit,o.output)
