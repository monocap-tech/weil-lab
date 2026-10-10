"""Authenticate originals and assemble the passed NF50 joint refinement ledger."""
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
    checks=[]
    for parity in ['EVEN','ODD']:
        cp=f'notes/data/RPB108_NF50_{parity}_JOINT_REFINEMENT_CERTIFICATE_20261010.json.gz.b64'
        vp=f'notes/data/RPB108_NF50_{parity}_JOINT_REFINEMENT_VALIDATION_20261010.json'
        c=read(cp);v=read(vp);assert v['status']=='PASS' and v['certificate_sha256']==sha(cp)
        assert v['validator_sha256']==sha('scripts/validate_native_joint_refinement_nf50_106.py')
        oldvalue=list(map(F,v['independent_normalized_NF49_witness_old_lower_value']))
        newvalue=list(map(F,v['independent_normalized_NF49_witness_new_lower_value']))
        improvement=list(map(F,v['independent_normalized_NF49_witness_inverse_reaction_improvement']))
        assert oldvalue[1]<0 and newvalue[0]>0 and improvement[0]>0
        sign=v['joint_lower_bound_sign'];assert sign['status']=='JOINT_LOWER_BOUND_REJECTED'
        quotient=list(map(F,sign['independent_original_physical_quotient']));assert quotient[1]<0
        assert c['source_analytic_infinite_remainders_paid'] and v['analytic_infinite_remainders_paid']
        assert c['original_joined_and_T53_columns_unchanged'] and c['old_high_columns_unchanged']
        checks.append(dict(parity=parity.lower(),status='PASS',certificate_path=cp,certificate_sha256=sha(cp),validation_path=vp,validation_sha256=sha(vp),
            old_high_dimension=c['old_high_dimension'],new_high_dimension=c['new_high_dimension'],
            original_native_pairings_checked=v['independent_native_pairings_checked'],
            complete_physical_source_pairings_checked=v['independent_complete_source_pairings_checked'],
            original_NF49_witness_lifted_to_strictly_positive_lower_value=True,
            independent_normalized_NF49_witness_old_lower_value=list(map(str,oldvalue)),
            independent_normalized_NF49_witness_new_lower_value=list(map(str,newvalue)),
            independent_normalized_NF49_witness_inverse_reaction_improvement=list(map(str,improvement)),
            new_joint_lower_bound_status=sign['status'],new_exact_rational_witness_in_certificate=True,
            independent_new_witness_physical_quotient=list(map(str,quotient)),
            necessary_next_inverse_reaction_physical_improvement_strict_lower=str(-quotient[1]),
            necessary_improvement_is_not_whole_matrix_sufficiency=True,actual_negative_original_form_claimed=False))
    assert sum(row['original_native_pairings_checked'] for row in checks)==129
    assert sum(row['complete_physical_source_pairings_checked'] for row in checks)==129
    scripts=['scripts/certify_native_joint_refinement_nf50_106.py','scripts/validate_native_joint_refinement_nf50_106.py',
             'scripts/summarize_native_joint_refinement_nf50_106.py']
    return dict(milestone='NF50',date_UTC='2026-10-10',status='PASS',aperture='53/50',
        starting_NF49_commit='2849eaa241412e2deef47e58462269112cde195b',original_archive_hashes=archives,
        script_sha256={p:sha(p) for p in scripts},parity_checks=checks,
        total_new_original_native_pairings_checked=129,total_new_complete_physical_source_pairings_checked=129,
        both_original_NF49_lower_bound_witnesses_lifted_to_strict_positive=True,
        both_enlarged_joint_lower_bounds_rejected_by_new_exact_witnesses=True,
        complete_original_remaining_Schur_inequality_certified=False,whole_aperture_positive=False,
        highest_certified_whole_aperture='21/20',original_inputs_regenerated=False,original_frozen_vectors_changed=False,
        actual_negative_original_form_claimed=False,RH=False,F4=False,Lean=False,
        next_exact_gate='Refine the shared inverse bound for all 56 original sources using the new full joint witnesses; certify D-B S^-1 B* >= 0 in both parities.')

if __name__=='__main__':
    result=run();Path('notes/data/RPB108_NF50_JOINT_INVERSE_REFINEMENT_CHECKPOINT_20261010.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print('NF50 checkpoint PASS;129 native and129 complete source pairings;whole1.06 OPEN')
