"""Authenticate original inputs and assemble the NF56 complete joint checkpoint."""
import base64,gzip,hashlib,json
from pathlib import Path
from fractions import Fraction as F

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def read(path):
    raw=Path(path).read_bytes()
    if str(path).endswith('.b64'):raw=gzip.decompress(base64.b64decode(raw))
    return json.loads(raw)

def run():
    replay=read('notes/data/RPB108_NF48_ORIGINAL_NF46_REPLAY_20261009.json');assert replay['status']=='PASS'
    archives=replay['unchanged_historical_runner_report']['original_archive_hashes']
    for row in archives:
        p=Path('nf24-inputs/Weil')/row['name'];assert sha(p)==row['compressed_sha256']
        assert hashlib.sha256(gzip.decompress(p.read_bytes())).hexdigest()==row['uncompressed_sha256']
    probe_path='notes/data/RPB108_NF56_EVEN_UNRESOLVED_JOINT_SIGN_PROBES_20261010.json'
    probe=read(probe_path);assert probe['status']=='PASS'
    assert probe['probe_script_sha256']==sha('scripts/probe_native_joint_sign_nf56_106.py')
    checks=[]
    for parity in ['EVEN','ODD']:
        cp=f'notes/data/RPB108_NF56_{parity}_JOINT_REFINEMENT_CERTIFICATE_20261010.json.gz.b64'
        vp=f'notes/data/RPB108_NF56_{parity}_JOINT_REFINEMENT_VALIDATION_20261010.json'
        c=read(cp);v=read(vp)
        assert v['status']=='PASS' and v['certificate_sha256']==sha(cp)
        assert v['validator_sha256']==sha('scripts/validate_native_joint_refinement_nf56_106.py')
        old=list(map(F,v['independent_normalized_NF55_witness_old_lower_value']))
        new=list(map(F,v['independent_normalized_NF55_witness_correlated_new_lower_value']))
        gain=list(map(F,v['independent_normalized_NF55_witness_correlated_inverse_reaction_improvement']))
        assert gain[0]>0
        if parity=='EVEN':
            assert old[0]<=0<=old[1] and v['old_target_classification']=='UNRESOLVED_SIGN_PROBE'
            assert v['old_target_probe_sha256']==sha('notes/data/RPB108_NF55_EVEN_UNRESOLVED_JOINT_SIGN_PROBES_20261010.json')
            assert probe['certificate_sha256']==sha(cp) and probe['validation_sha256']==sha(vp)
        else:assert old[1]<0 and v['old_target_classification']=='CERTIFIED_REJECTING_WITNESS'
        assert v['old_NF55_witness_lifted_to_positive']==(new[0]>0)
        assert c['interval_grid_digits']==800 and c['moment_degree']==1500
        assert v['precision_configuration']['interval_grid_digits']==900 and v['independent_moment_degree']==1600
        assert c['source_analytic_infinite_remainders_paid'] and v['analytic_infinite_remainders_paid']
        assert c['original_joined_and_T53_columns_unchanged'] and c['old_high_columns_unchanged']
        sign=v['joint_lower_bound_sign'];q=None
        if sign['status']=='JOINT_LOWER_BOUND_REJECTED':
            q=list(map(F,sign['independent_original_physical_quotient']));assert q[1]<0
        elif sign['status']=='CERTIFIED_POSITIVE_JOINT_LOWER_BOUND':assert 'independent_positive_congruence_proof' in sign
        else:assert sign['status']=='UNRESOLVED'
        checks.append(dict(parity=parity.lower(),status='PASS',certificate_path=cp,certificate_sha256=sha(cp),
            validation_path=vp,validation_sha256=sha(vp),old_target_classification=v['old_target_classification'],
            old_target_probe_sha256=v['old_target_probe_sha256'],old_high_dimension=c['old_high_dimension'],new_high_dimension=c['new_high_dimension'],
            original_native_pairings_checked=v['independent_native_pairings_checked'],complete_physical_source_pairings_checked=v['independent_complete_source_pairings_checked'],
            old_NF55_target_resolved_to_strictly_positive_lower_value=new[0]>0,
            independent_normalized_NF55_target_old_lower_value=list(map(str,old)),
            independent_normalized_NF55_target_new_lower_value=list(map(str,new)),
            independent_normalized_NF55_target_new_enclosure_width=str(new[1]-new[0]),
            sufficient_additional_guaranteed_gain_to_lift_recorded_target_lower_endpoint_strictly_greater_than=str(max(F(0),-new[0])),
            target_endpoint_gain_budget_is_not_whole_matrix_sufficiency=True,
            independent_normalized_NF55_target_correlated_inverse_reaction_improvement=list(map(str,gain)),
            new_joint_lower_bound_status=sign['status'],new_exact_rational_rejecting_witness_in_certificate=q is not None,
            independent_new_rejecting_witness_physical_quotient=list(map(str,q)) if q else None,
            necessary_next_inverse_reaction_physical_improvement_strict_lower=str(-q[1]) if q else None,
            necessary_improvement_is_not_whole_matrix_sufficiency=True,actual_negative_original_form_claimed=False))
    assert sum(r['original_native_pairings_checked'] for r in checks)==141
    assert sum(r['complete_physical_source_pairings_checked'] for r in checks)==141
    assert not all(r['new_joint_lower_bound_status']=='CERTIFIED_POSITIVE_JOINT_LOWER_BOUND' for r in checks), 'Discharge whole-aperture closure before publishing both positive gates'
    scripts=['scripts/certify_native_joint_refinement_nf56_106.py','scripts/validate_native_joint_refinement_nf56_106.py',
             'scripts/summarize_native_joint_refinement_nf56_106.py','scripts/native_precision_nf53.py','scripts/probe_native_joint_sign_nf56_106.py']
    return dict(milestone='NF56',status='PASS',date_UTC='2026-10-10',client_date='2026-10-09',client_timezone='America/Los_Angeles',
        aperture='53/50',starting_NF55_commit='29cd9381adeb08a9093b74e1ec487051d68e956b',original_archive_hashes=archives,
        script_sha256={p:sha(p) for p in scripts},parity_checks=checks,
        total_new_original_native_pairings_checked=141,total_new_complete_physical_source_pairings_checked=141,
        both_original_NF55_targets_resolved_to_strict_positive=all(r['old_NF55_target_resolved_to_strictly_positive_lower_value'] for r in checks),
        both_original_NF55_targets_have_strict_correlated_inverse_reaction_improvement=True,
        even_old_target_was_not_a_certified_rejecting_witness=True,
        even_remaining_sign_probe_path=probe_path,even_remaining_sign_probe_sha256=sha(probe_path),
        even_remaining_sign_probe_count=len(probe['sign_probe_candidates']),
        even_all_selected_nonpositive_midpoint_probes_span_zero=probe['all_selected_negative_midpoint_candidates_have_span_zero_enclosures'],
        final_shell_max_even_degree=372,final_shell_max_odd_degree=371,
        producer_interval_grid_digits=800,independent_interval_grid_digits=900,producer_moment_degree=1500,independent_moment_degree=1600,
        analytic_infinite_remainders_and_finite_constant_tails_paid=True,inherited_interval_endpoints_and_physical_errors_preserved=True,
        original_inputs_regenerated=False,original_frozen_vectors_changed=False,complete_original_remaining_Schur_inequality_certified=False,
        whole_aperture_positive=False,highest_certified_whole_aperture='21/20',actual_negative_original_form_claimed=False,RH=False,F4=False,Lean=False,
        next_exact_gate='Resolve remaining complete joint lower-matrix signs and rejecting directions, with all original cross sources and infinite remainders paid; certify D-B S^-1 B* >= 0 in both parities.')

if __name__=='__main__':
    result=run();Path('notes/data/RPB108_NF56_JOINT_INVERSE_REFINEMENT_CHECKPOINT_20261010.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print('NF56 checkpoint PASS;141 native and141 complete source pairings;whole1.06 OPEN')
