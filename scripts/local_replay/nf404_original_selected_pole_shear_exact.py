#!/usr/bin/env python3
"""NF404 ORIGINAL 242D selected pole-centering, exact Fraction, no Arb.

Uses accepted original outward 242D physical response and original pole
generator s=sinh(x/2) in original J242. Certifies one fixed dyadic a
which removes virtually all measured selected power. This is exact
original-source geometry, NOT an upper on unmeasured full supported w.
"""
import argparse,json,hashlib,math,sys
from pathlib import Path
from fractions import Fraction as F
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
NATIVE_SHA='644337986f62a3f25bb6b2005efc82f517975c84629b32b5ae8d1e5b95614515'
ACCEPT_SHA='4546d47d16bbcf88f7d41b1ce1255d2fcbe5dcc1b41241a3b277bf8dcbc36f02'
RANK_SHA='9b9820a0163e5e8bf08dd1c2525c757ff67214b49a40cb093d00bc611c9ff9e2'
NF403_SHA='advisory-not-needed'
B=F(11,10)
DPOLE=F(26709425989909960852,2**64)

def load(p):
    b=Path(p).read_bytes()
    return json.loads(b),hashlib.sha256(b).hexdigest()
def ends(v):
    assert len(v)==2
    a,b=map(F,v)
    assert a<=b
    return a,b
def sinh_minus_B(N=100):
    """Exact rational Taylor interval for ||sinh(x/2)||² over [-B,B].

    ∫_{-B}^B sinh²(x/2) dx = sinh(B)-B.
    First OMITTED term t_N, ratios <= r_N <1/4; tail <t_N/(1-r_N).
    """
    assert B>0 and N>=30
    series=sum((B**(2*n+1)/math.factorial(2*n+1) for n in range(1,N)),F(0))
    next_term=B**(2*N+1)/math.factorial(2*N+1)
    ratio=B*B/F((2*N+2)*(2*N+3))
    assert 0<ratio<F(1,4)
    assert 0<next_term
    return series,series+next_term/(1-ratio)

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--native',default='notes/data/provisional/NF401_original_242D_selected_column_source_native.json')
    p.add_argument('--acceptance',default='notes/data/provisional/NF401_original_242D_selected_column_independent_acceptance.json')
    p.add_argument('--receipt',default='notes/data/provisional/NF401_original_242D_execution_receipt.json')
    p.add_argument('--rank',default='notes/data/provisional/parents/pr350_original_BS_pruned_rank_bound.json')
    p.add_argument('--nf403',default='notes/data/provisional/NF403_original_joint_complement_power_exact.json')
    p.add_argument('--output',required=True)
    a=p.parse_args()
    n,nsha=load(a.native)
    acc,accsha=load(a.acceptance)
    rec,_=load(a.receipt)
    rank,rsha=load(a.rank)
    prior,_=load(a.nf403)
    assert nsha==acc['native_sha256']==rec['original_native_json_sha256']==NATIVE_SHA
    assert accsha==ACCEPT_SHA
    assert rec['native_column_accepted'] is True
    assert rsha==n['original_rank_sha256']==RANK_SHA
    assert n['original_dimension']==242
    assert rank['retained_original_pole'] and len(rank['selected_multiplicities'])==len(rank['original_nodes'])
    assert sum(rank['selected_multiplicities'])==241
    assert len(n['original_selected_raw_J_basis_moment_column_outward'])==242
    assert n['original_pole_restored'] is True
    assert n['new_signed_kernel_cells']==0
    assert n['W_ODD_NEG']==n['RH']==acc['W_ODD_NEG']==acc['RH']=='OPEN'
    assert prior['original_nf401_accepted_242D_native_sha256']==NATIVE_SHA
    assert prior['original_scalar_full_action_norm_upper_computed'] is False
    ps_lo,ps_hi=ends(n['original_projected_norm_interval_outward'])
    b_lo,b_hi=ends(n['original_selected_raw_J_basis_moment_column_outward'][241])
    assert 0<ps_lo<=ps_hi and 0<b_lo<=b_hi
    ss_lo,ss_hi=sinh_minus_B()
    assert F(0)<ss_lo<=ss_hi
    assert ss_hi-ss_lo<F(1,10**200)
    # source-selected pole coefficient c_exact = <w,s>/||s||².
    # Fixed dyadic c0 is selected ONCE; exact physical projection and
    # complement identities hold for ANY dyadic c0 without assuming that
    # it equals the original unknown c_exact.
    center=DPOLE
    centered_lo=ps_lo**2-2*center*b_hi+center**2*ss_lo
    centered_hi=ps_hi**2-2*center*b_lo+center**2*ss_hi
    assert 0<centered_lo<=centered_hi
    # Certified actual ORIGINAL 242D selected-moment near-collinearity:
    assert F(109,10**23) < centered_lo
    assert centered_hi < F(11,10**22)
    # Exact source bound on distance of rational center to the unique
    # original pole coefficient <w,s>/||s||², without rounding to float.
    mismatch_bound=max(abs(b_lo-center*ss_hi),abs(b_hi-center*ss_lo))
    assert mismatch_bound<F(1,2**64)*ss_lo
    c_lower=b_lo/ss_hi
    c_upper=b_hi/ss_lo
    assert c_lower>0 and c_lower<c_upper
    # New original center scalar physical power sufficiency:
    # (because s∈J)
    # ||Q_J w||² = ||w-c0 s||² - ||P_J w-c0 s||².
    # Thus if the as-yet-UNMEASURED whole supported original
    # ||w-c0 s||² ≤centered_lo+gamma², the original NF403
    # selected fourth lowband target follows.
    gamma=F(prior['source_sufficient_Jperp_full_action_radius_gamma'])
    gamma2=gamma*gamma
    assert gamma>0 and gamma2>0
    centered_gate=centered_lo+gamma2
    assert centered_lo<centered_gate<centered_hi+gamma2
    # To avoid hidden cancellation in future numeric physical scalar,
    # directly evaluate the positive physical integral
    # ∫_I |(m(D)u4)(x)-c0 sinh(x/2)|² dx.
    # Unlike original ||w||²~0.494, the new benchmark is ~1.095e-21
    # if original fourth residual is indeed small.
    assert centered_lo>F(1,10**22)
    assert centered_hi<F(2,10**21)
    assert gamma2/centered_lo<F(1,1000) # desired relative tolerance <0.1%
    out={
       'pass':'NF404',
       'standing':'EXACT ORIGINAL 242D SELECTED POLE-SHEAR PHYSICAL POWER REDUCTION; FULL ACTION UPPER OPEN',
       'original_nf401_selected_native_sha256':NATIVE_SHA,
       'original_nf401_accepted_exact_receipt_sha256':ACCEPT_SHA,
       'original_rank_sha256':RANK_SHA,
       'original_dimension':242,
       'original_selected_pole_index':241,
       'original_pole_squared_norm_exact_analytic_identity':'sinh(11/10)-11/10',
       'original_pole_squared_norm_lower_exact':str(ss_lo),
       'original_pole_squared_norm_upper_exact':str(ss_hi),
       'original_pole_squared_norm_interval_width_lt_1e_minus_200':True,
       'original_pole_moment_outward_interval':n['original_selected_raw_J_basis_moment_column_outward'][241],
       'original_full_selected_projection_norm_outward_interval':n['original_projected_norm_interval_outward'],
       'fixed_dyadic_pole_coefficient':str(center),
       'original_true_pole_coefficient_interval':[str(c_lower),str(c_upper)],
       'original_true_pole_coefficient_minus_dyadic_abs_lt_2power_minus64':True,
       'original_selected_after_pole_shear_power_lower_exact':str(centered_lo),
       'original_selected_after_pole_shear_power_upper_exact':str(centered_hi),
       'strict_new_selected_after_pole_shear_power_bracket':'109/10^23 < power < 11/10^22',
       'exact_sufficient_new_full_supported_centered_scalar_power_upper_target':str(centered_gate),
       'exact_source_original_full_complement_power_budget':str(gamma2),
       'new_physical_integrand':'|1_I(m(D)u4 - (26709425989909960852/2^64) sinh(x/2))|^2',
       'source_energy_cancellation_reduction':'subtraction of known pole energy before computing original full physical scalar; do not subtract ~0.494 source energies',
       'actual_original_full_supported_centered_scalar_integrated':False,
       'original_J242_perpendicular_lowband_upper_computed':False,
       'original_general_operator_domain_audited':False,
       'new_signed_kernel_cells':0,
       'W_ODD_NEG':'OPEN','RH':'OPEN'
    }
    dst=Path(a.output);dst.parent.mkdir(parents=True,exist_ok=True)
    dst.write_text(json.dumps(out,indent=2)+'\n')
    print('NF404 original finite selected J242 pole-shear exact power bracket PASS',flush=True)
    print('NF404 0.494 selected mass separated; remaining selected physical power <1.1e-21',flush=True)
    print('NF404 centered physical scalar upper target exact; actual scalar UNMEASURED',flush=True)
if __name__=='__main__':main()
