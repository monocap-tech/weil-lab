#!/usr/bin/env python3
"""Original BS infinite-tail upper from physical Hermite and inverse compression.

Only exact composition of accepted inputs; no inverse or projection evaluated.
"""
import argparse,hashlib,json,time
from fractions import Fraction as F
from pathlib import Path
PINS={'reference':'f1149e27da8a0e1d90e48b8ee0eb8a0a0b8ef51d0910499a7fcd19a082efca07',
      'envelope':'19af532b6bbd4a808854696b2a993e7ebd966e04da27fdd5f55e8b736668770b',
      'critical':'a84b19c1fefc4e680c5c19ea643bbe5badce639374cb0a424211ee980020f922'}
def main():
    p=argparse.ArgumentParser()
    for k in PINS:p.add_argument('--'+k,required=True)
    p.add_argument('--output',default='artifacts/original_BS_infinite_tail_upper.json');args=p.parse_args();start=time.monotonic();data={}
    for k,h in PINS.items():
        raw=Path(getattr(args,k)).read_bytes();assert hashlib.sha256(raw).hexdigest()==h;data[k]=json.loads(raw)
    r,e,c=(data[k] for k in PINS)
    assert r['status']=='CONDITIONAL_FULL_ORIGINAL_SI29_REFERENCE_INVERSE_ON_J470_PERP'
    assert r['original_J_count']==e['original_source_count']==470
    assert r['native_input_sha256']==e['input_sha256']['native']=='c9ee487f8abe7b633c47d2ef7d72e2cc4f7289bc794b2d8fc02bb61520b25e60'
    assert r['actual_continuous_feature_count']==14
    delta=F(r['clean_relative_error_upper']);kappa=F(r['kappa']);ks=F(r['inherited_B14_coercivity'])
    beta=F(r['reference_inverse_residual_upper_factor'])
    assert delta==F(1,10**500) and kappa==F(1,1000) and ks==F(33621,10**9)
    assert beta==(1+delta)/kappa
    assert e['full_original_973_leaves_paid'] and e['all_107_clusters_paid']
    eps=F(e['whole_envelope_complement_upper']);assert 0<eps<F(2431,10**11)
    assert c['status']=='CONDITIONAL_ORIGINAL_FOUR_NEAR_CRITICAL_BS_MODES'
    assert c['near_critical_dimension_lower']==4 and F(c['inherited_Astar_floor'])==ks
    eta=F(c['fourth_BS_distance_from_one_upper']);lower=F(c['fourth_BS_eigenvalue_lower'])
    assert lower==1-eta>1-F(3,10**12)
    tail=beta*eps;clean=F(2431,10**8);level=1-F(3,10**12)
    assert 0<tail<clean<level<lower
    coarse=eps/ks;assert coarse/tail>F(297,10)
    # Schur mixing price for the NEW B-space complement, not physical QH.
    price=tail/(1-tail);threshold=1-tail
    result=dict(status='CONDITIONAL_ORIGINAL_BS_INFINITE_TAIL_AND_FINITE_COUNT_UPPER',input_sha256=PINS,
      original_physical_source_count=470,physical_complement_negative_upper=str(eps),compressed_actual_Astar_inverse_upper=str(beta),
      inverse_compression_relative_error=str(delta),inherited_global_Astar_floor=str(ks),physical_complement_floor=str(kappa),
      BS_deflation_subspace='range(Kminus^(1/2) J470), using the ACTUAL physical operator square root',
      BS_deflation_rank_upper=470,BS_complement_operator_upper=str(tail),clean_BS_complement_operator_upper=str(clean),
      eigenvalue_index=471,eigenvalue_upper=str(tail),fourth_eigenvalue_lower=str(lower),
      critical_level=str(level),critical_count_lower=4,critical_count_upper=470,
      original_negative_index_upper=470,global_coercivity_only_tail_upper=str(coarse),tail_improvement_factor=str(coarse/tail),
      complete_Schur='I-H-D(I-C)^(-1)D* >=0, H=Pi B Pi, D=Pi B R, C=R B R, R=I-Pi',
      complement_inverse_upper=str(1/(1-tail)),generic_mixed_Schur_price=str(price),generic_sufficient_finite_threshold=str(threshold),
      actual_physical_Q_B_Q_bound_claimed=False,physical_and_BS_deflation_spaces_identified=False,compressed_multiplier_square_identity_used=False,
      actual_BS_projection_computed=False,actual_finite_BS_block_computed=False,actual_mixed_BS_block_computed=False,finite_gate_certified=False,
      exact_critical_count_certified=False,global_true_BS_norm_upper_one_certified=False,full_signed_positivity_certified=False,
      W_ODD_NEG='OPEN',inherited_original_domain_review='OPEN',elapsed_seconds=time.monotonic()-start)
    path=Path(args.output);path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(result,indent=2)+'\n')
    print('ORIGINAL BS INFINITE TAIL PASS: lambda471 <0.00002431; critical count at 1-3e-12 is 4..470; complete finite/mixed Schur OPEN; seconds',round(result['elapsed_seconds'],3))
if __name__=='__main__':main()
