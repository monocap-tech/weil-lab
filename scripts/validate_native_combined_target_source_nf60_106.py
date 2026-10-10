"""Independent 900-digit, cell-first NF60 combined-source scalar refinement.

Does not import the NF60 producer. Rebuilds exact physical coefficients,
native low integrals, projected source norm and every analytic error payment.
"""
import argparse,json
from fractions import Fraction as F
from pathlib import Path
import validate_native_joint_refinement_nf59_106 as q

def run(path):
    c=q.read(path);parity=c['parity'];ctx,parent,_=q.parent_context(parity)
    cp=f'notes/data/RPB108_NF59_{parity.upper()}_JOINT_REFINEMENT_CERTIFICATE_20261010.json.gz.b64'
    vp=f'notes/data/RPB108_NF59_{parity.upper()}_JOINT_REFINEMENT_VALIDATION_20261010.json'
    gp=f'notes/data/RPB108_NF59_{parity.upper()}_GROUPED_TARGET_CONTRACTION_20261010.json'
    old=q.read(cp);validation=q.read(vp);grouped=q.read(gp)
    assert c['milestone']=='NF60' and c['aperture']=='53/50'
    assert c['producer_sha256']==q.sha('scripts/certify_native_combined_target_source_nf60_106.py')
    assert c['inherited_NF59_certificate_sha256']==q.sha(cp)==validation['certificate_sha256']
    assert validation['status']=='PASS' and c['inherited_NF59_validation_sha256']==q.sha(vp)
    assert validation['validator_sha256']==q.sha('scripts/validate_native_joint_refinement_nf59_106.py')
    assert grouped['status']=='PASS' and grouped['script_sha256']==q.sha('scripts/refine_native_joint_target_contraction_nf59_106.py')
    g=grouped['parity_checks'][0];assert g['certificate_sha256']==q.sha(cp) and g['validation_sha256']==q.sha(vp)
    z=list(map(F,old['fixed_high_selection']['normalized_NF58_joint_witness']))
    assert list(map(str,z))==c['frozen_normalized_target']==g['fixed_normalized_NF58_target']
    merged={}
    for (ii,cc),w in zip(ctx['P']+[(ctx['ids'],col) for col in ctx['T']],z):
        for j,a in zip(ii,cc):merged[j]=merged.get(j,F(0))+w*a
    ii=sorted(merged);cc=[merged[j] for j in ii];mass=sum(a*a for a in cc)
    assert ii==c['combined_physical_indices'] and list(map(str,cc))==c['combined_physical_coefficients']
    assert str(mass)==c['exact_combined_physical_mass_squared'] and 0<mass<=1
    normalization=F(old['fixed_high_selection']['NF58_witness_normalizing_upper'])
    assert mass==F(parent['joint_lower_bound_sign']['witness_original_physical_mass_squared'])/normalization**2
    work=Path('work/nf60')/(parity+'-independent');work.mkdir(parents=True,exist_ok=True)
    m=ctx['m'];key=q.sha(__file__)+'-'+q.sha(cp)
    sy=q.prior.cached(work/'combined_source.pkl',key,lambda:m.source(ii,cc))
    fun=q.functional(sy,m,max(ii));error=m.eta*q.prior.root(mass)
    low=[q.polynomial_value(q.n.basis(j),fun)+q.Box(-error,error) for j in ctx['ids']]
    frozen=[q.Box(*map(F,e)) for e in c['source_low_projection']];q.prior.compare([low],[frozen])
    mids=[(a.l+a.h)/2 for a in frozen]
    r=(sy[0],q.n.add(sy[1],q.n.scale(q.n.physical(ctx['ids'],mids),-1)),sy[2],sy[3])
    needed=error+8*max(max(abs(a.l-b),abs(a.h-b)) for a,b in zip(low,mids))
    ey=F(c['projected_source_error_upper']);assert ey>=needed
    assert F(c['physical_norm_upper'])**2>=mass and F(c['unprojected_source_error_upper'])>=error
    assert F(c['regular_and_signed_pole_tail_operator_upper'])>=m.eta
    print(parity,'independent exact target and low projection PASS',flush=True)
    raw=q.prior.pair(r,q.prior.cell_action(r,m,len(r[1]),len(r[2])))
    q.prior.overlap(raw,q.Box(*map(F,c['raw_combined_projected_source_norm_squared'])))
    nr=q.prior.root(max(F(0),raw.h));payment=2*ey*nr+ey**2
    assert F(c['approximant_norm_upper'])>=nr
    assert F(c['source_norm_squared_error_payment'])>=payment
    paid=raw+q.Box(-payment,payment);q.prior.overlap(paid,q.Box(*map(F,c['paid_combined_complete_source_norm_squared'])))
    paid=q.Box(max(F(0),paid.l),paid.h)
    audit=validation['normalized_NF58_target_component_enclosure_audit']['components']
    native=q.Box(*map(F,audit['native_energy']['enclosure']))
    oldceiling=q.Box(*map(F,audit['common_source_ceiling']['enclosure']))
    oldnorm=oldceiling*q.K;q.prior.overlap(paid,oldnorm)
    refined=q.Box(max(paid.l,oldnorm.l),min(paid.h,oldnorm.h))
    correction=q.Box(*map(F,g['grouped_inverse_correction']))
    ceiling=refined/q.K
    forward=native-ceiling+correction
    previous=q.Box(*map(F,g['tightened_target_lower_value']));q.prior.overlap(forward,previous)
    target=q.Box(max(forward.l,previous.l),min(forward.h,previous.h))
    widths={'native_energy':native.h-native.l,'common_source_ceiling':ceiling.h-ceiling.l,'inverse_correction':correction.h-correction.l}
    assert sum(widths.values())==forward.h-forward.l
    print(parity,'independent combined-source norm and scalar refinement PASS',flush=True)
    return dict(milestone='NF60',parity=parity,status='PASS',certificate_sha256=q.sha(path),validator_sha256=q.sha(__file__),
        inherited_grouped_target_report_sha256=q.sha(gp),original_archive_uncompressed_sha256=ctx['hashes'],
        interval_grid_digits=900,moment_degree=1800,exact_physical_mass_identity='PASS',
        independent_projected_source_error_required=str(needed),independent_raw_source_norm_squared=raw.ends(),
        independent_paid_complete_source_norm_squared=paid.ends(),old_scalar_complete_source_norm_squared=oldnorm.ends(),
        refined_scalar_complete_source_norm_squared=refined.ends(),
        source_norm_width_ratio=str((refined.h-refined.l)/(oldnorm.h-oldnorm.l)),
        frozen_target=c['frozen_normalized_target'],unchanged_grouped_inverse_correction=correction.ends(),
        refined_forward_target_lower_value=forward.ends(),previous_target_lower_value=previous.ends(),
        tightened_target_lower_value=target.ends(),target_lifted_to_positive=target.l>0,
        target_minorant_certified_negative=target.h<0,forward_component_widths={k:str(w) for k,w in widths.items()},
        sufficient_additional_gain_to_lift_lower_endpoint_strictly_greater_than=str(max(F(0),-target.l)),
        all_original_source_errors_and_infinite_remainders_retained=True,actual_negative_original_form_claimed=False,
        original_inputs_regenerated=False,original_frozen_vectors_changed=False,whole_matrix_sign_certified=False,
        whole_aperture_positive=False,highest_certified_whole_aperture='21/20')

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--certificate',required=True);parser.add_argument('--output',required=True)
    args=parser.parse_args();Path(args.output).write_text(json.dumps(run(args.certificate),indent=2,sort_keys=True)+'\n')
