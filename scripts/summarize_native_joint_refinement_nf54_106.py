"""Authenticate originals and assemble the passed NF54 joint refinement ledger."""
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
        path=Path('nf24-inputs/Weil')/row['name']
        assert sha(path)==row['compressed_sha256']
        assert hashlib.sha256(gzip.decompress(path.read_bytes())).hexdigest()==row['uncompressed_sha256']
    probe_path='notes/data/RPB108_NF54_EVEN_UNRESOLVED_JOINT_SIGN_PROBES_20261010.json'
    probe=read(probe_path);assert probe['status']=='PASS' and not probe['entire_matrix_sign_certified']
    assert probe['probe_script_sha256']==sha('scripts/probe_native_joint_sign_nf54_106.py')
    checks=[]
    for parity in ['EVEN','ODD']:
        cp=f'notes/data/RPB108_NF54_{parity}_JOINT_REFINEMENT_CERTIFICATE_20261010.json.gz.b64'
        vp=f'notes/data/RPB108_NF54_{parity}_JOINT_REFINEMENT_VALIDATION_20261010.json'
        c=read(cp);v=read(vp);assert v['status']=='PASS' and v['certificate_sha256']==sha(cp)
        assert v['validator_sha256']==sha('scripts/validate_native_joint_refinement_nf54_106.py')
        oldvalue=list(map(F,v['independent_normalized_NF53_witness_old_lower_value']))
        newvalue=list(map(F,v['independent_normalized_NF53_witness_correlated_new_lower_value']))
        improvement=list(map(F,v['independent_normalized_NF53_witness_correlated_inverse_reaction_improvement']))
        assert oldvalue[1]<0 and improvement[0]>0
        assert c['interval_grid_digits']==800 and c['moment_degree']==1300
        assert v['precision_configuration']['interval_grid_digits']==900 and v['independent_moment_degree']==1400
        assert v['old_NF53_witness_lifted_to_positive']==(newvalue[0]>0)
        sign=v['joint_lower_bound_sign']
        if parity=='EVEN':
            assert sign['status']=='UNRESOLVED'
            assert probe['certificate_sha256']==sha(cp) and probe['validation_sha256']==sha(vp)
            quotient=None
        else:
            assert sign['status']=='JOINT_LOWER_BOUND_REJECTED'
            quotient=list(map(F,sign['independent_original_physical_quotient']));assert quotient[1]<0
        assert c['source_analytic_infinite_remainders_paid'] and v['analytic_infinite_remainders_paid']
        assert c['original_joined_and_T53_columns_unchanged'] and c['old_high_columns_unchanged']
        checks.append(dict(parity=parity.lower(),status='PASS',certificate_path=cp,certificate_sha256=sha(cp),validation_path=vp,validation_sha256=sha(vp),
            old_high_dimension=c['old_high_dimension'],new_high_dimension=c['new_high_dimension'],
            original_native_pairings_checked=v['independent_native_pairings_checked'],
            complete_physical_source_pairings_checked=v['independent_complete_source_pairings_checked'],
            original_NF53_witness_lifted_to_strictly_positive_lower_value=newvalue[0]>0,
            independent_normalized_NF53_witness_old_lower_value=list(map(str,oldvalue)),
            independent_normalized_NF53_witness_new_lower_value=list(map(str,newvalue)),
            independent_normalized_NF53_witness_inverse_reaction_improvement=list(map(str,improvement)),
            new_joint_lower_bound_status=sign['status'],new_exact_rational_rejecting_witness_in_certificate=quotient is not None,
            independent_new_witness_physical_quotient=list(map(str,quotient)) if quotient else None,
            necessary_next_inverse_reaction_physical_improvement_strict_lower=str(-quotient[1]) if quotient else None,
            necessary_improvement_is_not_whole_matrix_sufficiency=True,actual_negative_original_form_claimed=False))
    assert sum(row['original_native_pairings_checked'] for row in checks)==137
    assert sum(row['complete_physical_source_pairings_checked'] for row in checks)==137
    scripts=['scripts/certify_native_joint_refinement_nf54_106.py','scripts/validate_native_joint_refinement_nf54_106.py',
             'scripts/summarize_native_joint_refinement_nf54_106.py','scripts/native_precision_nf53.py','scripts/probe_native_joint_sign_nf54_106.py']
    return dict(milestone='NF54',date_UTC='2026-10-10',client_date='2026-10-09',client_timezone='America/Los_Angeles',status='PASS',aperture='53/50',
        starting_NF53_commit='8f8be75830329df947e261fdc965dda3bf366bc7',original_archive_hashes=archives,
        script_sha256={p:sha(p) for p in scripts},parity_checks=checks,
        total_new_original_native_pairings_checked=137,total_new_complete_physical_source_pairings_checked=137,
        both_original_NF53_lower_bound_witnesses_lifted_to_strict_positive=all(r['original_NF53_witness_lifted_to_strictly_positive_lower_value'] for r in checks),
        both_original_NF53_witnesses_have_strict_correlated_inverse_reaction_improvement=True,
        both_enlarged_joint_lower_bounds_rejected_by_new_exact_witnesses=False,
        even_enlarged_joint_lower_bound_status='UNRESOLVED',odd_enlarged_joint_lower_bound_status='JOINT_LOWER_BOUND_REJECTED',
        even_unresolved_sign_probe_path=probe_path,even_unresolved_sign_probe_sha256=sha(probe_path),
        even_frozen_sign_probe_count=len(probe['sign_probe_candidates']),
        complete_original_remaining_Schur_inequality_certified=False,whole_aperture_positive=False,
        highest_certified_whole_aperture='21/20',original_inputs_regenerated=False,original_frozen_vectors_changed=False,
        actual_negative_original_form_claimed=False,RH=False,F4=False,Lean=False,
        correlated_gain_method='Positive rank-one Schur update with exact cancellation of the common Xi Gram',
        final_shell_max_even_degree=308,final_shell_max_odd_degree=307,
        producer_interval_grid_digits=800,independent_interval_grid_digits=900,
        producer_moment_degree=1300,independent_moment_degree=1400,
        inherited_grid500_interval_endpoints_promoted_exactly=True,
        NF53_extended_shell_precision_barrier_remains_discharged=True,
        inherited_grid800_NF53_source_reconstructed_at_each_checked_grid=True,
        finite_analytic_series_tails_paid=True,
        next_exact_gate='Resolve the first frozen even sign-probe direction with tighter complete inverse/source enclosures, and discharge the odd rejecting witness with all original cross sources and infinite remainders paid. Certify D-B S^-1 B* >= 0 in both parities.')

if __name__=='__main__':
    result=run();Path('notes/data/RPB108_NF54_JOINT_INVERSE_REFINEMENT_CHECKPOINT_20261010.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print('NF54 checkpoint PASS;137 native and137 complete source pairings;whole1.06 OPEN')
