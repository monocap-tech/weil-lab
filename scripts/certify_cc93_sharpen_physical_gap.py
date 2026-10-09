#!/usr/bin/env python3
"""Inverse-trace and authenticated lifted-mass refinement of CC92."""
import argparse,json,math
from pathlib import Path
from fractions import Fraction as F
import certify_cc80_defect_response_acceptance as exact
import certify_cc81_boundary_response_consumer as c
import certify_cc88_correlated_seventh_response as direct
import certify_cc91_both_joined_pass as joined
import certify_cc92_conditional_physical_restriction as physical

def sqrtupper(value):
    assert value>=0
    scale=10**50;scaled=value*scale*scale
    numerator=math.isqrt(scaled.__floor__())
    if numerator*numerator<scaled:numerator+=1
    upper=F(numerator,scale);assert upper*upper>=value
    return upper
def controls():
    cases=[]
    for scale in [F(1),F(1,10**18)]:
        k=exact.mat([[2,1,scale],[1,2,scale],[scale,scale,scale**2]])
        assert all(x>0 for x in exact.pivots(k))
        inv=exact.inv(k);trace=sum(inv[i][i] for i in range(3));eps=1/trace
        shifted=exact.add(k,exact.diag([-eps]*3))
        assert all(x>0 for x in exact.pivots(shifted))
        ss,ei,beta=joined.condensation([[c.iv(x) for x in row] for row in k])
        computed=ei[0][0][0]+ei[1][1][0]+(1+sum(x[0]**2 for x in beta))/ss[0]
        assert computed==trace
        cases.append(dict(scale=str(scale),exact_inverse_trace_identity=True,
            exact_shifted_matrix_positive=True))
    for value in [F(0),F(2),F(1,10**120),F(37,101)]:assert sqrtupper(value)**2>=value
    return dict(two_scale_inverse_trace_controls=cases,rational_mass_sqrt_enclosures=True)
def run(massroot,newroot,parentroot,oldroot):
    prior=physical.run(massroot,newroot,parentroot,oldroot)
    seed=physical.load(massroot,'RPB108_NF26_HIGH_CORRECTION_CERTIFICATE_20261009.json')
    response=physical.load(massroot,'RPB108_NF29_LIFTED_RESPONSE_CERTIFICATE_20261009.json')
    extra=physical.load(massroot,'RPB108_NF30_FIXED_EXPANDED_RESPONSE_20261009.json')
    rows=[]
    for parity in ['even','odd']:
        masses=physical.load(massroot,'RPB108_NF35_'+parity.upper()+'_JOINED_WITNESSES_CERTIFICATE_20261009.json')
        move=physical.load(massroot,'RPB108_NF37_'+parity.upper()+'_FREE_CORRECTION_FUNCTIONAL_CERTIFICATE_20261009.json')
        correction=physical.load(massroot,'RPB108_NF36_'+parity.upper()+'_COLLECTIVE_CORRECTION_CERTIFICATE_20261009.json')
        seedpar=next(r for r in seed['parity_certificates'] if r['parity']==parity)
        responsepar=next(r for r in response['parity_certificates'] if r['parity']==parity)
        base=[sqrtupper(F(masses['inherited_retained_masses'][0]))+F(seedpar['correction_norm_upper']),
            sqrtupper(F(responsepar['lifted_response_norm_squared'])),
            F(masses['retained_witness_norm_upper'])+F(masses['high_witness_component_norm_upper'])]
        if parity=='even':base[1]+=sum(abs(F(x)) for x in extra['fixed_rational_coefficients'])
        norm=F(correction['correction_norm_upper'])
        bounds=[x+abs(F(lam))*norm for x,lam in zip(base,move['selected_rational_functional'])]
        mass=sum(x*x for x in bounds);assert 0<mass<12
        if parity=='even':d=joined.load(newroot,'RPB108_NF46_EVEN_NEXT_SHELL_CERTIFICATE_20261009.json');count='eight'
        else:d=joined.seven.load(parentroot,'RPB108_NF45_ODD_INVERSE_WITNESS_CERTIFICATE_20261009.json');count='seven'
        k=c.matrix(d['conditional_'+count+'_high_joined_Schur_lower_matrix'])
        s,ei,beta=joined.condensation(k);assert s[0]>0
        trace=ei[0][0][1]+ei[1][1][1]+(1+sum(direct.absmax(x)**2 for x in beta))/s[0]
        eps=1/trace;assert eps>0
        oldrow=next(r for r in prior['parity_checks'] if r['parity']==parity)
        source=F(oldrow['inverse_source_operator_norm_square_upper'])
        gap=min(eps/(4*(mass+source)),direct.K/2)
        oldgap=F(oldrow['conditional_physical_gap_lower']);assert gap>oldgap
        rows.append(dict(parity=parity,three_actual_lifted_norm_upper_bounds=[c.pair(c.iv(x))[1] for x in bounds],
            actual_lifted_Gram_operator_upper=c.pair(c.iv(mass))[1],
            joined_inverse_trace_upper=c.pair(c.iv(trace))[1],
            inverse_trace_coordinate_coercivity_lower=c.pair(c.iv(eps))[0],
            conditional_physical_gap_lower=c.pair(c.iv(gap))[0],
            improvement_factor_over_CC92_lower=c.pair(c.iv(gap/oldgap))[0]))
    gap=min(F(r['conditional_physical_gap_lower']) for r in rows)
    return dict(milestone='CC93',integration_parent='9183934b66e7cd647ac9def9f6ea6290c17e9b23',
        read_only_source='6658ff2837838ab00b9b9c605fdd200d473c3293',parity_checks=rows,
        conditional_six_direction_plus_all_F_physical_gap_lower=str(gap),
        exact_controls=controls(),same_original_restriction_as_CC92=True,
        new_native_source=False,background_floor_newly_proved=False,
        original_form_domain_attachment_inherited=True,complete_retained_matrix_certified=False,
        whole_aperture_positive=False,highest_certified_whole_aperture='21/20')
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('mass_root',type=Path);ap.add_argument('NF46_root',type=Path);ap.add_argument('NF45_root',type=Path);ap.add_argument('NF44_root',type=Path);ap.add_argument('--output',type=Path,required=True)
    a=ap.parse_args();d=run(a.mass_root,a.NF46_root,a.NF45_root,a.NF44_root);a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(d,indent=2)+'\n')
    print('CC93 PASS: sharper conditional physical gap',float(F(d['conditional_six_direction_plus_all_F_physical_gap_lower'])))
