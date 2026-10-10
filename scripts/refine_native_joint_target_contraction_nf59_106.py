"""Independent grouped target contraction through NF59's certified inverse.

Freeze the same physical target and contract W* z before the quadratic
inverse calculation. Every source/native entry retains its paid enclosure.
This refines a target enclosure; it is not a whole-matrix sign proof.
"""
import argparse,json
from pathlib import Path
from fractions import Fraction as F
import validate_native_joint_refinement_nf59_106 as q

def run(parity):
    rows=[]
    for parity in [parity]:
        cp=f'notes/data/RPB108_NF59_{parity.upper()}_JOINT_REFINEMENT_CERTIFICATE_20261010.json.gz.b64'
        vp=f'notes/data/RPB108_NF59_{parity.upper()}_JOINT_REFINEMENT_VALIDATION_20261010.json'
        c=q.read(cp);v=q.read(vp)
        assert v['status']=='PASS' and v['certificate_sha256']==q.sha(cp)
        assert v['validator_sha256']==q.sha('scripts/validate_native_joint_refinement_nf59_106.py')
        q.parent_context(parity)  # Authenticate history and configure the 900-digit route.
        M,QH,GH,B,S=[q.mat(c[k]) for k in ['enlarged_high_physical_Gram','enlarged_high_native_Gram',
            'enlarged_high_complete_source_Gram','enlarged_joint_high_native_crosses','enlarged_joint_high_complete_source_crosses']]
        C=q.ind.add(QH,q.ind.scale(M,-q.K))
        U=q.ind.add(q.ind.add(GH,q.ind.scale(QH,-2*q.K)),q.ind.scale(M,q.K*q.K))
        N=q.ind.add(C,q.ind.scale(U,1/q.K));NI,proof=q.prior.oldcheck.independent_inverse(N)
        W=q.ind.add(S,q.ind.scale(B,-q.K))
        z=list(map(F,c['fixed_high_selection']['normalized_NF58_joint_witness']))
        wz=[q.ind.dot(z,col) for col in zip(*W)]
        correction=q.ind.dot(wz,[q.ind.dot(row,wz) for row in NI])/(q.K*q.K)
        assert correction.h>=0
        correction=q.Box(max(F(0),correction.l),correction.h)  # N is certified positive.
        audit=v['normalized_NF58_target_component_enclosure_audit']['components']
        native=q.Box(*map(F,audit['native_energy']['enclosure']))
        source=q.Box(*map(F,audit['common_source_ceiling']['enclosure']))
        grouped=native-source+correction
        component_widths={label:a.h-a.l for label,a in [('native_energy',native),('common_source_ceiling',source),('inverse_correction',correction)]}
        assert sum(component_widths.values())==grouped.h-grouped.l
        old=q.Box(*map(F,v['independent_normalized_NF58_witness_correlated_new_lower_value']))
        q.prior.overlap(grouped,old)
        tightened=q.Box(max(grouped.l,old.l),min(grouped.h,old.h))
        assert tightened.l>=old.l and tightened.h<=old.h
        expanded_width=F(audit['inverse_correction']['width'])
        rows.append(dict(parity=parity,status='PASS',certificate_sha256=q.sha(cp),validation_sha256=q.sha(vp),
            fixed_normalized_NF58_target=list(map(str,z)),inverse_denominator_positive_proof=proof,
            grouped_high_cross_vector=[a.ends() for a in wz],grouped_inverse_correction=correction.ends(),
            grouped_forward_target_lower_value=grouped.ends(),previous_correlated_target_lower_value=old.ends(),
            grouped_forward_component_widths={k:str(w) for k,w in component_widths.items()},
            grouped_forward_component_width_shares={k:str(w/(grouped.h-grouped.l)) for k,w in component_widths.items()},
            tightened_target_lower_value=tightened.ends(),target_lifted_to_positive=tightened.l>0,
            target_lower_bound_still_certified_negative=tightened.h<0,
            expanded_inverse_correction_width=str(expanded_width),grouped_inverse_correction_width=str(correction.h-correction.l),
            grouped_to_expanded_correction_width_ratio=str((correction.h-correction.l)/expanded_width),
            previous_target_enclosure_width=str(old.h-old.l),tightened_target_enclosure_width=str(tightened.h-tightened.l),
            sufficient_additional_gain_to_lift_tightened_lower_endpoint_strictly_greater_than=str(max(F(0),-tightened.l)),
            all_original_source_errors_and_infinite_remainders_retained=True,actual_negative_original_form_claimed=False,
            whole_matrix_sign_certified=False))
    return dict(milestone='NF59',status='PASS',method='Contract W* z before the certified inverse quadratic; intersect valid target enclosures',
        script_sha256=q.sha(__file__),validator_sha256=q.sha('scripts/validate_native_joint_refinement_nf59_106.py'),
        interval_grid_digits=900,parity_checks=rows,original_inputs_regenerated=False,original_frozen_vectors_changed=False,
        whole_aperture_positive=False,highest_certified_whole_aperture='21/20',actual_negative_original_form_claimed=False)

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--parity',choices=['even','odd'],required=True)
    parser.add_argument('--output',required=True)
    args=parser.parse_args();result=run(args.parity)
    Path(args.output).write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(args.parity,'NF59 grouped target contraction PASS; all original errors retained; whole1.06 OPEN')
