"""Authenticate NF60 scalar refinements, original archives and inherited gates."""
import gzip,hashlib,json
from pathlib import Path
from fractions import Fraction as F
import summarize_native_joint_refinement_nf59_106 as prior
sha=prior.sha;read=prior.read

def run():
    archives=read('notes/data/RPB108_NF48_ORIGINAL_NF46_REPLAY_20261009.json')['unchanged_historical_runner_report']['original_archive_hashes']
    for a in archives:
        p=Path('nf24-inputs/Weil')/a['name'];assert sha(p)==a['compressed_sha256']
        assert hashlib.sha256(gzip.decompress(p.read_bytes())).hexdigest()==a['uncompressed_sha256']
    floor=read('notes/data/RPB108_NF47_FLOOR_TRANSPORT_VALIDATION_20261009.json')
    assert floor['status']=='PASS' and floor['certificate_sha256']==sha('notes/data/RPB108_NF47_FLOOR_TRANSPORT_CERTIFICATE_20261009.json')
    assert F(floor['original_F112_floor']['independent_original_F112_lower'])>F(207,1000)
    replay=read('notes/data/RPB108_NF48_ORIGINAL_NF46_REPLAY_20261009.json');assert replay['status']=='PASS'
    parentpath='notes/data/RPB108_NF59_JOINT_INVERSE_REFINEMENT_CHECKPOINT_20261010.json'
    parent=read(parentpath);assert parent['status']=='PASS'
    rows=[]
    for parity in ['even','odd']:
        cp=f'notes/data/RPB108_NF60_{parity.upper()}_COMBINED_TARGET_SOURCE_CERTIFICATE_20261010.json'
        vp=f'notes/data/RPB108_NF60_{parity.upper()}_COMBINED_TARGET_SOURCE_VALIDATION_20261010.json'
        c=read(cp);v=read(vp)
        assert v['status']=='PASS' and v['certificate_sha256']==sha(cp)
        assert v['validator_sha256']==sha('scripts/validate_native_combined_target_source_nf60_106.py')
        assert c['producer_sha256']==sha('scripts/certify_native_combined_target_source_nf60_106.py')
        assert v['frozen_target']==c['frozen_normalized_target'] and v['exact_physical_mass_identity']=='PASS'
        old=list(map(F,v['previous_target_lower_value']));new=list(map(F,v['tightened_target_lower_value']))
        assert old[0]<=new[0]<=new[1]<=old[1]
        assert v['target_lifted_to_positive']==(new[0]>0) and v['target_minorant_certified_negative']==(new[1]<0)
        inherited=next(r for r in parent['parity_checks'] if r['parity']==parity)
        rows.append(dict(parity=parity,status='PASS',certificate_path=cp,certificate_sha256=sha(cp),
            validation_path=vp,validation_sha256=sha(vp),source_norm_width_ratio=v['source_norm_width_ratio'],
            previous_target_lower_value=v['previous_target_lower_value'],tightened_target_lower_value=v['tightened_target_lower_value'],
            target_lifted_to_positive=v['target_lifted_to_positive'],target_minorant_certified_negative=v['target_minorant_certified_negative'],
            exact_frozen_target_physical_mass_squared=c['exact_combined_physical_mass_squared'],
            current_physical_high_minorant_status='REJECTED_BY_SCALAR_TARGET' if new[1]<0 else 'SCALAR_TARGET_POSITIVE' if new[0]>0 else 'SCALAR_TARGET_UNRESOLVED',
            necessary_additional_gain_to_lift_target_strictly_greater_than=str(max(F(0),-new[1])),
            inherited_high_dimension=inherited['new_high_dimension'],inherited_full_joint_matrix_status=inherited['new_joint_lower_bound_status'],
            sufficient_additional_gain_to_lift_lower_endpoint_strictly_greater_than=v['sufficient_additional_gain_to_lift_lower_endpoint_strictly_greater_than'],
            forward_component_widths=v['forward_component_widths'],actual_negative_original_form_claimed=False))
    scripts=['scripts/certify_native_combined_target_source_nf60_106.py','scripts/validate_native_combined_target_source_nf60_106.py','scripts/summarize_native_combined_target_source_nf60_106.py']
    return dict(milestone='NF60',status='PASS',date_UTC='2026-10-10',aperture='53/50',
        starting_NF59_commit='a8f814c8c1a40dc6e6aba7166b47793198f94ad8',inherited_NF59_checkpoint_sha256=sha(parentpath),
        original_archive_hashes=archives,script_sha256={p:sha(p) for p in scripts},parity_checks=rows,
        method='Exact combined physical target source, independent cell-first norm, complete analytic tail payment, intersection with prior scalar bounds',
        original_F112_floor_retained='207/1000',original_NF46_replay_byte_identity_retained=True,
        high_minorant_and_signed_transport_crosses_unchanged=True,original_frozen_vectors_changed=False,original_inputs_regenerated=False,
        all_thirteen_prime_cells_and_endpoint_log_and_signed_pole_retained=True,
        all_original_infinite_remainders_paid=True,whole_matrix_sign_certified=False,whole_aperture_positive=False,
        highest_certified_whole_aperture='21/20',RH_proved=False,F4_closed=False,Lean_closed=False,all_aperture_positive=False,
        actual_negative_original_form_claimed=False)

if __name__=='__main__':
    p=Path('notes/data/RPB108_NF60_COMBINED_TARGET_SOURCE_CHECKPOINT_20261010.json')
    p.write_text(json.dumps(run(),indent=2,sort_keys=True)+'\n');print('NF60 original inputs and both scalar refinements PASS; whole1.06 OPEN')
