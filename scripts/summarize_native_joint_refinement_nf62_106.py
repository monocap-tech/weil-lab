"""Authenticate NF62 original inputs, new high pairings and frozen target gains."""
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
    parentpath='notes/data/RPB108_NF61_JOINT_INVERSE_REFINEMENT_CHECKPOINT_20261010.json'
    parent=read(parentpath);assert parent['status']=='PASS'
    rows=[]
    for parity in ['even','odd']:
        cp=f'notes/data/RPB108_NF62_{parity.upper()}_JOINT_REFINEMENT_CERTIFICATE_20261010.json.gz.b64'
        vp=f'notes/data/RPB108_NF62_{parity.upper()}_JOINT_REFINEMENT_VALIDATION_20261010.json'
        oldvp=f'notes/data/RPB108_NF61_{parity.upper()}_JOINT_REFINEMENT_VALIDATION_20261010.json'
        c=read(cp);v=read(vp);old=read(oldvp)
        selectionpath=f'notes/data/RPB108_NF62_{parity.upper()}_FROZEN_EXTERIOR_SELECTION_20261010.json'
        assert read(selectionpath)==c['fixed_high_selection']
        assert v['status']=='PASS' and v['certificate_sha256']==sha(cp)
        assert v['validator_sha256']==sha('scripts/validate_native_joint_refinement_nf62_106.py')
        assert old['status']=='PASS' and c['old_target_probe_sha256']==v['inherited_NF61_target_validation_sha256']==sha(oldvp)
        assert c['fixed_high_selection']['normalized_frozen_joint_target']==read(f'notes/data/RPB108_NF61_{parity.upper()}_JOINT_REFINEMENT_CERTIFICATE_20261010.json.gz.b64')['fixed_high_selection']['normalized_frozen_joint_target']
        assert v['independent_frozen_NF61_target_old_lower_value']==old['independent_frozen_target_best_new_lower_value']
        assert v['unchanged_NF60_direct_source_norm_interval']==old['unchanged_NF60_direct_source_norm_interval']
        previous=list(map(F,old['independent_frozen_target_best_new_lower_value']));gain=list(map(F,v['independent_frozen_target_correlated_gain']))
        best=list(map(F,v['independent_frozen_target_best_new_lower_value']))
        assert previous[1]<0 and gain[0]>=0
        assert previous[0]+gain[0]<=best[0]<=best[1]<=previous[1]+gain[1]
        assert v['frozen_NF61_target_lifted_to_positive']==(best[0]>0)
        assert v['frozen_target_minorant_certified_negative']==(best[1]<0)
        assert c['new_high_dimension']==c['old_high_dimension']+1
        assert c['all_new_native_pairings_certified']==v['independent_native_pairings_checked']==56+c['new_high_dimension']
        assert c['all_new_complete_source_pairings_certified']==v['independent_complete_source_pairings_checked']==56+c['new_high_dimension']
        assert v['exact_new_high_physical_orthogonality_checked'] and v['analytic_infinite_remainders_paid']
        assert v['exact_exterior_high_support_checked'] and c['selection_exterior_to_all_old_high_support']
        assert c['interval_grid_digits']==1000 and c['selection_interval_grid_digits']==800
        assert v['precision_configuration']['interval_grid_digits']==1100
        assert c['source_square_moment_degree_required']==v['source_square_moment_degree_required']<=1700
        assert c['original_joined_and_T53_columns_unchanged'] and c['old_high_columns_unchanged']
        sign=v['joint_lower_bound_sign'];quotient=None
        if sign['status']=='JOINT_LOWER_BOUND_REJECTED':
            quotient=sign['independent_original_physical_quotient'];assert F(quotient[1])<0
        elif sign['status']=='CERTIFIED_POSITIVE_JOINT_LOWER_BOUND':assert 'independent_positive_congruence_proof' in sign
        else:assert sign['status']=='UNRESOLVED'
        probepath=f'notes/data/RPB108_NF62_{parity.upper()}_UNRESOLVED_JOINT_SIGN_PROBES_20261010.json'
        probe=read(probepath)
        assert probe['status']=='PASS' and probe['certificate_sha256']==sha(cp) and probe['validation_sha256']==sha(vp)
        assert probe['probe_script_sha256']==sha('scripts/probe_native_joint_sign_nf62_106.py')
        assert probe['all_56_midpoint_pivots_examined']
        import certify_native_remaining_native_nf48_106 as frame
        floorcert=read('notes/data/RPB108_NF47_FLOOR_TRANSPORT_CERTIFICATE_20261009.json')
        ids,T,_,P=frame.constraint_frame(floorcert['parity_frames'][['even','odd'].index(parity)])
        physical=P+[(ids,col) for col in zip(*T)]
        for candidate in probe['sign_probe_candidates']:
            z=list(map(F,candidate['fixed_rational_sign_probe']));assert len(z)==56
            lo=F(0);hi=F(0);values=iter(c['complete_joint_original_Schur_lower_upper_triangle'])
            for i in range(56):
                for j in range(i,56):
                    l,h=map(F,next(values));w=z[i]*z[j]*(1 if i==j else 2)
                    lo+=w*(l if w>=0 else h);hi+=w*(h if w>=0 else l)
            assert list(map(str,[lo,hi]))==candidate['certified_matrix_probe_value']
            coeff={}
            for scalar,(jj,cc) in zip(z,physical):
                for j,a in zip(jj,cc):coeff[j]=coeff.get(j,F(0))+scalar*a
            mass=sum(a*a for a in coeff.values());assert mass>0 and str(mass)==candidate['original_physical_mass_squared']
            assert list(map(str,[lo/mass,hi/mass]))==candidate['certified_matrix_probe_physical_quotient']
            assert candidate['enclosure_spans_zero']==(lo<=0<=hi)
            assert candidate['lower_matrix_probe_classification']==('CERTIFIED_NEGATIVE_LOWER_MATRIX_PROBE' if hi<0 else 'SPAN_ZERO' if lo<=0<=hi else 'CERTIFIED_POSITIVE_LOWER_MATRIX_PROBE')
        rows.append(dict(parity=parity,status='PASS',certificate_path=cp,certificate_sha256=sha(cp),validation_path=vp,validation_sha256=sha(vp),
            old_high_dimension=c['old_high_dimension'],new_high_dimension=c['new_high_dimension'],
            original_native_pairings_checked=v['independent_native_pairings_checked'],complete_source_pairings_checked=v['independent_complete_source_pairings_checked'],
            frozen_target_old_lower_value=old['independent_frozen_target_best_new_lower_value'],strict_correlated_gain=v['independent_frozen_target_correlated_gain'],
            frozen_target_best_new_lower_value=v['independent_frozen_target_best_new_lower_value'],
            frozen_target_grouped_new_lower_value=v['independent_frozen_target_grouped_new_lower_value'],
            strict_positive_correlated_gain_certified=gain[0]>0,
            exterior_selection_indices=c['fixed_high_selection']['selection_indices'],
            source_square_moment_degree_required=c['source_square_moment_degree_required'],
            residual_probe_path=probepath,residual_probe_sha256=sha(probepath),
            frozen_exterior_selection_path=selectionpath,frozen_exterior_selection_sha256=sha(selectionpath),
            residual_probes_independently_checked=len(probe['sign_probe_candidates']),
            residual_probe_joint_lower_bound_status='REJECTED_BY_CERTIFIED_NEGATIVE_PROBE' if any(r['lower_matrix_probe_classification']=='CERTIFIED_NEGATIVE_LOWER_MATRIX_PROBE' for r in probe['sign_probe_candidates']) else 'UNRESOLVED',
            first_certified_negative_residual_probe=next((r for r in probe['sign_probe_candidates'] if r['lower_matrix_probe_classification']=='CERTIFIED_NEGATIVE_LOWER_MATRIX_PROBE'),None),
            residual_probe_classifications=[r['lower_matrix_probe_classification'] for r in probe['sign_probe_candidates']],
            target_lifted_to_positive=best[0]>0,target_minorant_certified_negative=best[1]<0,
            current_target_minorant_status='POSITIVE' if best[0]>0 else 'NEGATIVE' if best[1]<0 else 'UNRESOLVED',
            sufficient_additional_gain_to_lift_lower_endpoint_strictly_greater_than=str(-best[0]) if best[0]<=0 else None,
            necessary_additional_gain_to_lift_target_strictly_greater_than=str(-best[1]) if best[1]<0 else None,
            full_entrywise_joint_lower_bound_status=sign['status'],new_rejecting_witness_original_physical_quotient=quotient,
            scalar_target_is_not_whole_matrix_sufficiency=True,actual_negative_original_form_claimed=False))
    assert sum(r['original_native_pairings_checked'] for r in rows)==151
    assert sum(r['complete_source_pairings_checked'] for r in rows)==151
    assert not all(r['full_entrywise_joint_lower_bound_status']=='CERTIFIED_POSITIVE_JOINT_LOWER_BOUND' for r in rows), 'Discharge whole-aperture closure before publishing both positive gates'
    scripts=['scripts/certify_native_joint_refinement_nf62_106.py','scripts/validate_native_joint_refinement_nf62_106.py','scripts/summarize_native_joint_refinement_nf62_106.py','scripts/native_precision_nf62.py','scripts/probe_native_joint_sign_nf62_106.py']
    return dict(milestone='NF62',status='PASS',date_UTC='2026-10-10',aperture='53/50',starting_NF61_commit='a119005c56e3ea39d80f228e5dff57e0297aab96',
        inherited_NF61_checkpoint_sha256=sha(parentpath),original_archive_hashes=archives,script_sha256={p:sha(p) for p in scripts},parity_checks=rows,
        total_new_original_native_pairings_checked=151,total_new_complete_source_pairings_checked=151,
        both_frozen_targets_have_strict_positive_correlated_inverse_reaction_gain=all(r['strict_positive_correlated_gain_certified'] for r in rows),
        remaining_joint_probes_independently_rechecked_by_upper_triangle_and_exact_physical_mass=True,
        both_frozen_targets_lifted_to_positive=all(r['target_lifted_to_positive'] for r in rows),
        original_F112_floor_retained='207/1000',original_NF46_replay_byte_identity_retained=True,
        NF60_direct_source_norm_enclosures_retained=True,exterior_shell_tested=True,all_original_signed_crosses_and_infinite_remainders_retained=True,
        original_inputs_regenerated=False,original_frozen_vectors_changed=False,actual_negative_original_form_claimed=False,
        whole_aperture_positive=False,highest_certified_whole_aperture='21/20',RH=False,F4=False,Lean=False,all_aperture_positive=False)

if __name__=='__main__':
    p=Path('notes/data/RPB108_NF62_JOINT_INVERSE_REFINEMENT_CHECKPOINT_20261010.json')
    p.write_text(json.dumps(run(),indent=2,sort_keys=True)+'\n');print('NF62 original inputs, 151 native and 151 complete source pairings PASS; whole1.06 OPEN')
