"""Authenticate NF61 original inputs, new high pairings and frozen target gains."""
import gzip,hashlib,json
from pathlib import Path
from fractions import Fraction as F
import summarize_native_joint_refinement_nf59_106 as prior
sha=prior.sha;read=prior.read

def run():
    replay=read('notes/data/RPB108_NF48_ORIGINAL_NF46_REPLAY_20261009.json');assert replay['status']=='PASS'
    archives=replay['unchanged_historical_runner_report']['original_archive_hashes']
    for a in archives:
        p=Path('nf24-inputs/Weil')/a['name'];assert sha(p)==a['compressed_sha256']
        assert hashlib.sha256(gzip.decompress(p.read_bytes())).hexdigest()==a['uncompressed_sha256']
    floor=read('notes/data/RPB108_NF47_FLOOR_TRANSPORT_VALIDATION_20261009.json')
    assert floor['status']=='PASS' and floor['certificate_sha256']==sha('notes/data/RPB108_NF47_FLOOR_TRANSPORT_CERTIFICATE_20261009.json')
    assert F(floor['original_F112_floor']['independent_original_F112_lower'])>F(207,1000)
    parentpath='notes/data/RPB108_NF60_COMBINED_TARGET_SOURCE_CHECKPOINT_20261010.json'
    parent=read(parentpath);assert parent['status']=='PASS'
    rows=[]
    for parity in ['even','odd']:
        cp=f'notes/data/RPB108_NF61_{parity.upper()}_JOINT_REFINEMENT_CERTIFICATE_20261010.json.gz.b64'
        vp=f'notes/data/RPB108_NF61_{parity.upper()}_JOINT_REFINEMENT_VALIDATION_20261010.json'
        oldvp=f'notes/data/RPB108_NF60_{parity.upper()}_COMBINED_TARGET_SOURCE_VALIDATION_20261010.json'
        c=read(cp);v=read(vp);old=read(oldvp)
        assert v['status']=='PASS' and v['certificate_sha256']==sha(cp)
        assert v['validator_sha256']==sha('scripts/validate_native_joint_refinement_nf61_106.py')
        assert old['status']=='PASS' and c['inherited_NF60_scalar_validation_sha256']==v['inherited_NF60_scalar_validation_sha256']==sha(oldvp)
        assert c['fixed_high_selection']['normalized_frozen_joint_target']==old['frozen_target']
        assert v['independent_frozen_NF60_target_old_lower_value']==old['tightened_target_lower_value']
        assert v['unchanged_NF60_direct_source_norm_interval']==old['refined_scalar_complete_source_norm_squared']
        previous=list(map(F,old['tightened_target_lower_value']));gain=list(map(F,v['independent_frozen_target_correlated_gain']))
        best=list(map(F,v['independent_frozen_target_best_new_lower_value']))
        assert previous[1]<0 and gain[0]>0
        assert previous[0]+gain[0]<=best[0]<=best[1]<=previous[1]+gain[1]
        assert v['frozen_NF60_target_lifted_to_positive']==(best[0]>0)
        assert v['frozen_target_minorant_certified_negative']==(best[1]<0)
        assert c['new_high_dimension']==c['old_high_dimension']+1
        assert c['all_new_native_pairings_certified']==v['independent_native_pairings_checked']==56+c['new_high_dimension']
        assert c['all_new_complete_source_pairings_certified']==v['independent_complete_source_pairings_checked']==56+c['new_high_dimension']
        assert v['exact_new_high_physical_orthogonality_checked'] and v['analytic_infinite_remainders_paid']
        assert c['original_joined_and_T53_columns_unchanged'] and c['old_high_columns_unchanged']
        sign=v['joint_lower_bound_sign'];quotient=None
        if sign['status']=='JOINT_LOWER_BOUND_REJECTED':
            quotient=sign['independent_original_physical_quotient'];assert F(quotient[1])<0
        elif sign['status']=='CERTIFIED_POSITIVE_JOINT_LOWER_BOUND':assert 'independent_positive_congruence_proof' in sign
        else:assert sign['status']=='UNRESOLVED'
        rows.append(dict(parity=parity,status='PASS',certificate_path=cp,certificate_sha256=sha(cp),validation_path=vp,validation_sha256=sha(vp),
            old_high_dimension=c['old_high_dimension'],new_high_dimension=c['new_high_dimension'],
            original_native_pairings_checked=v['independent_native_pairings_checked'],complete_source_pairings_checked=v['independent_complete_source_pairings_checked'],
            frozen_target_old_lower_value=old['tightened_target_lower_value'],strict_correlated_gain=v['independent_frozen_target_correlated_gain'],
            frozen_target_best_new_lower_value=v['independent_frozen_target_best_new_lower_value'],
            frozen_target_grouped_new_lower_value=v['independent_frozen_target_grouped_new_lower_value'],
            target_lifted_to_positive=best[0]>0,target_minorant_certified_negative=best[1]<0,
            current_target_minorant_status='POSITIVE' if best[0]>0 else 'NEGATIVE' if best[1]<0 else 'UNRESOLVED',
            sufficient_additional_gain_to_lift_lower_endpoint_strictly_greater_than=str(max(F(0),-best[0])),
            necessary_additional_gain_to_lift_target_strictly_greater_than=str(max(F(0),-best[1])),
            full_entrywise_joint_lower_bound_status=sign['status'],new_rejecting_witness_original_physical_quotient=quotient,
            scalar_target_is_not_whole_matrix_sufficiency=True,actual_negative_original_form_claimed=False))
    assert sum(r['original_native_pairings_checked'] for r in rows)==149
    assert sum(r['complete_source_pairings_checked'] for r in rows)==149
    assert not all(r['full_entrywise_joint_lower_bound_status']=='CERTIFIED_POSITIVE_JOINT_LOWER_BOUND' for r in rows), 'Discharge whole-aperture closure before publishing both positive gates'
    scripts=['scripts/certify_native_joint_refinement_nf61_106.py','scripts/validate_native_joint_refinement_nf61_106.py','scripts/summarize_native_joint_refinement_nf61_106.py']
    return dict(milestone='NF61',status='PASS',date_UTC='2026-10-10',aperture='53/50',starting_NF60_commit='db69f427046cc6eff5a615ca1d1c32dbae963042',
        inherited_NF60_checkpoint_sha256=sha(parentpath),original_archive_hashes=archives,script_sha256={p:sha(p) for p in scripts},parity_checks=rows,
        total_new_original_native_pairings_checked=149,total_new_complete_source_pairings_checked=149,
        both_frozen_targets_have_strict_positive_correlated_inverse_reaction_gain=True,
        both_frozen_targets_lifted_to_positive=all(r['target_lifted_to_positive'] for r in rows),
        original_F112_floor_retained='207/1000',original_NF46_replay_byte_identity_retained=True,
        NF60_direct_source_norm_enclosures_retained=True,all_original_signed_crosses_and_infinite_remainders_retained=True,
        original_inputs_regenerated=False,original_frozen_vectors_changed=False,actual_negative_original_form_claimed=False,
        whole_aperture_positive=False,highest_certified_whole_aperture='21/20',RH=False,F4=False,Lean=False,all_aperture_positive=False)

if __name__=='__main__':
    p=Path('notes/data/RPB108_NF61_JOINT_INVERSE_REFINEMENT_CHECKPOINT_20261010.json')
    p.write_text(json.dumps(run(),indent=2,sort_keys=True)+'\n');print('NF61 original inputs, 149 native and 149 complete source pairings PASS; whole1.06 OPEN')
