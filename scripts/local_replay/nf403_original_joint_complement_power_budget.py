#!/usr/bin/env python3
"""NF403 original physical lowband-complement norm: exact evidence/entry gate.

Reuses exact original NF401 242D projected norm AND the accepted NF389
original J242-perpendicular 512/513 joint witnesses. Computes a strict
source-derived lowband-complement lower and the new SINGLE original strong
action scalar upper entry gate; it does NOT compute that missing scalar.
"""
import argparse,hashlib,json
from fractions import Fraction as F
from pathlib import Path

NF401='644337986f62a3f25bb6b2005efc82f517975c84629b32b5ae8d1e5b95614515'
NF398='bae006e4fb542c4b0c6d184ae8cfbc2e7c924d45c89092ebda89cf0c6057c877'
N512='9d4b07fb2ca42c14ed995ddcd69811201eacb6f13f9f795a70c4b64889e9f83b'
N513='e0aaa0abb29c8ec75b3524ec6197c12235a7fc7fa66d76c77c4643c2ff27bffe'
D=F(2401,2*10**28)
TAU=F(7,25*10**12)
SIGMA=F(11,4*10**13)
LOW_C=F(863,10**16)

def load(path):
    b=Path(path).read_bytes()
    return json.loads(b),hashlib.sha256(b).hexdigest()

def run(args):
    a,asha=load(args.acceptance)
    receipt,_=load(args.receipt)
    nf398,nf398sha=load(args.nf398)
    joint,jsha=load(args.joint)
    jup,usha=load(args.joint_upper)
    n512,h512=load(args.n512)
    n513,h513=load(args.n513)

    assert receipt['native_column_accepted'] is True
    assert receipt['original_native_json_sha256']==a['native_sha256']==NF401
    assert a['source_nf398_sha256']==nf398sha==NF398
    assert a['independent_raw_two_coefficient_j387_contraction_intersection_pass'] is True
    assert h512==joint['source_native_512_sha256']==jup['original_n512_sha256']==N512
    assert h513==joint['source_native_513_sha256']==jup['original_n513_sha256']==N513
    assert n512['original_physical_16_Gram_overlaps'] is True
    assert n513['original_physical_16_Gram_overlaps'] is True
    assert n512['original_signed_32_CE_BP_overlaps'] is True
    assert n513['original_signed_32_CE_BP_overlaps'] is True
    assert jup['original_physical_and_signed_overlap_preflight_pass'] is True
    assert joint['certified_physical_G_strictly_SPD'] is True
    assert joint['original_direction_four_squared_budget']==str(D)
    assert jup['certified_whole_two_ray_fraction_strict_upper']=='307/2000'
    assert joint['original_full_two_witness_dual_upper_computed'] is False
    assert jup['unmeasured_remainder_observed'] is False
    assert nf398['original_NF375_fourth_cutoff']==2**24
    assert F(nf398['original_NF375_fourth_lowband_future_target'])==TAU
    assert all(v['W_ODD_NEG']==v['RH']=='OPEN' for v in (a,receipt,nf398,joint,jup,n512,n513))

    H=F(nf398['original_NF375_fourth_highband_action_norm_upper'])
    dlow=F(joint['certified_squared_dual_lower_best_rational_ray'])
    dupper=F(307,2000)*D
    gamma=SIGMA-H
    gamma2=gamma*gamma
    assert H>0 and 0<gamma<SIGMA<TAU
    assert SIGMA**2+H**2<TAU**2
    assert 0<dlow<dupper<gamma2
    # NF389 original joint physical J-perp pairing forces a positive
    # ORIGINAL supported lowband-complement lower for every selected j.
    assert (LOW_C+H)**2<dlow
    # Accepted NF401 outward physical norm interval is extraordinarily
    # narrow: keep its ENTIRE exact-fraction endpoints, never round the
    # original ~0.494 squared mass to 9 decimal places.
    p_lo,p_hi=map(F,a['selected_projection_norm_interval'])
    assert 0<p_lo<p_hi
    assert p_hi-p_lo<F(1,10**100)
    selected_power_lower=p_lo**2
    scalar_full_power_sufficient_cap=selected_power_lower+gamma2
    # Exact Pythagoras: ||Qw||²=||w||²-||Pw||².
    # If original ||w||²<=cap, then ||Qw||²<=gamma² and
    # ||Q tL||<=SIGMA; NF400 orthogonality gives
    # ||tL-Pw||²<=SIGMA²+H²<TAU².
    # Reuse the finite two-witness joint POWER upper to type remaining
    # unmeasured physical Q-orthogonal power with an exact budget.
    complement_remainder_cap=gamma2-dupper
    assert complement_remainder_cap>F(32,10**27)
    assert dlow>F(18,10**27)  # >1.8e-26, original finite evidence
    assert scalar_full_power_sufficient_cap>selected_power_lower
    # Note: original scalar upper has NOT been supplied. This is an
    # exact acceptance target, not a computed upper or an upper on RH.
    out={
       'pass':'NF403',
       'standing':'EXACT ORIGINAL N512/N513 JOINT LOWBAND LOWER AND SINGLE-SCALAR UPPER ACCEPTANCE CONTRACT',
       'original_nf401_accepted_242D_native_sha256':NF401,
       'original_nf398_highband_native_sha256':NF398,
       'original_n512_native_sha256':N512,
       'original_n513_native_sha256':N513,
       'original_nf389_joint_lower_report_sha256':jsha,
       'original_nf389_joint_upper_report_sha256':usha,
       'original_cutoff':2**24,
       'original_NF375_lowband_target':str(TAU),
       'original_NF375_highband_H':str(H),
       'source_new_exact_strict_Jperp_lowband_lower':str(LOW_C),
       'source_strict_joint_dual_power_lower':str(dlow),
       'source_strict_joint_dual_power_upper':str(dupper),
       'source_sufficient_Jperp_full_action_radius_gamma':str(gamma),
       'source_sufficient_Jperp_full_action_power_budget':str(gamma2),
       'source_two_witness_orthogonal_remainder_power_cap':str(complement_remainder_cap),
       'source_two_witness_orthogonal_remainder_cap_strict_lower':'32/1000000000000000000000000000',
       'original_full_supported_multiplier_power_required_upper':str(scalar_full_power_sufficient_cap),
       'original_selected_projection_power_lower_used':str(selected_power_lower),
       'original_selected_projection_norm_interval_width_lt_1e_minus_100':True,
       'original_selected_projection_sufficient_full_power_test':
          'certified upper ||1_I m(D)u4||^2 <= recorded exact scalar cap implies ||t_L-P_J m(D)u4||<tau',
       'original_scalar_full_action_norm_upper_computed':False,
       'original_512_513_orthogonal_remainder_upper_computed':False,
       'original_complete_lowband_upper_computed':False,
       'original_general_operator_domain_audited':False,
       'W_ODD_NEG':'OPEN','RH':'OPEN'
    }
    payload=json.dumps(out,indent=2)+'\n'
    if args.output:
        Path(args.output).parent.mkdir(parents=True,exist_ok=True)
        Path(args.output).write_text(payload)
    print('NF403 original two-witness lower >',LOW_C)
    print('NF403 exact full-action complement-budget and single-scalar cap PASS (gate only)')
    print('NF403 no original scalar norm upper, complete lowband upper or RH closure')
    if not args.output:print(payload,end='')

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--acceptance',default='notes/data/provisional/NF401_original_242D_selected_column_independent_acceptance.json')
    p.add_argument('--receipt',default='notes/data/provisional/NF401_original_242D_execution_receipt.json')
    p.add_argument('--nf398',default='notes/data/provisional/NF398_original_j387_selected_signed_native.json')
    p.add_argument('--joint',default='notes/data/provisional/NF389_original_joint_lower_exact_parent.json')
    p.add_argument('--joint-upper',default='notes/data/provisional/NF389_original_two_ray_sharper_upper_exact.json')
    p.add_argument('--n512',default='notes/data/provisional/NF380_original_archived_unfitted_signed_dual_native.json')
    p.add_argument('--n513',default='notes/data/provisional/NF389_original_n513_signed_native.json')
    p.add_argument('--output',default=None)
    run(p.parse_args())
