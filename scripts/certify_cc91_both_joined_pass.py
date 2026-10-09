#!/usr/bin/env python3
"""Independent NF46 even update and preserved NF45 odd certificate consumer."""
import argparse,hashlib,json
from pathlib import Path
from fractions import Fraction as F
import certify_cc81_boundary_response_consumer as c
import certify_cc83_five_source_consumer as five
import certify_cc87_seven_source_consumer as seven
import certify_cc88_correlated_seventh_response as direct

HASH={
'RPB108_NF46_EVEN_NEXT_SHELL_CERTIFICATE_20261009.json':'4556f7f990a5ba9e7ec139e5f809b8b26b51203ca790f224b6f63f22299c69e7',
'RPB108_NF46_NEXT_SHELL_VALIDATION_20261009.json':'22984c0fc5a716c61e649e7334b97e0bcf9b30eeb3af4979f7e546563ac93a37'}
def load(root,name):
    raw=(root/'notes/data'/name).read_bytes();assert hashlib.sha256(raw).hexdigest()==HASH[name]
    return json.loads(raw)
def condensation(k):
    assert k==c.transpose(k)
    e=[row[:2] for row in k[:2]];ei=five.inverse2(e);r=[[k[0][2]],[k[1][2]]]
    assert k[0][0][0]>0 and c.det2(e)[0]>0
    beta=c.mm(c.transpose(r),ei)[0]
    s=c.sub(k[2][2],c.mm(c.mm(c.transpose(r),ei),r)[0][0])
    return s,ei,beta
def positive(k):
    s,ei,beta=condensation(k);det=c.det3(k);assert s[0]>0 and det[0]>0
    e=[row[:2] for row in k[:2]]
    epsilon=min(c.det2(e)[0]/(e[0][0][1]+e[1][1][1]),s[0])/(3+sum(direct.absmax(x)**2 for x in beta))
    assert epsilon>0
    return dict(condensed_margin=c.pair(s),determinant=c.pair(det),
        retained_coordinate_coercivity_lower=c.pair(c.iv(epsilon))[0])
def run(root,parentroot,oldroot):
    val=load(root,'RPB108_NF46_NEXT_SHELL_VALIDATION_20261009.json')
    d=load(root,'RPB108_NF46_EVEN_NEXT_SHELL_CERTIFICATE_20261009.json')
    old=seven.load(parentroot,'RPB108_NF45_EVEN_INVERSE_WITNESS_CERTIFICATE_20261009.json')
    odd=seven.load(parentroot,'RPB108_NF45_ODD_INVERSE_WITNESS_CERTIFICATE_20261009.json')
    assert val['status']=='PASS' and not val['background_floor_newly_proved'] and not val['whole_aperture_positive']
    assert val['even_check']['certificate_sha256']==HASH['RPB108_NF46_EVEN_NEXT_SHELL_CERTIFICATE_20261009.json']
    assert val['even_check']['trial_sha256']==d['fixed_trial_sha256']
    assert val['preserved_odd_NF45_certificate']['sha256']==seven.HASH['RPB108_NF45_ODD_INVERSE_WITNESS_CERTIFICATE_20261009.json']
    assert d['NF45_input_sha256']==val['NF45_input_sha256']
    assert all(x in d['NF45_input_sha256'] for x in [old['fixed_trial_sha256'],odd['fixed_trial_sha256'],*seven.HASH.values()])
    assert d['conditional_joined_sign_certified'] and not d['eight_high_minorant_fails_to_certify']
    assert not any(d[x] for x in ['background_floor_newly_proved','actual_negative_original_form_claimed','whole_aperture_positive','RH','F4','Lean'])
    for suffix in ['physical_Gram','native_Gram','complete_source_Gram']:
        assert [row[:7] for row in d['eight_high_'+suffix][:7]]==old['seven_high_'+suffix]
    for suffix in ['native_crosses','source_crosses']:
        assert [row[:7] for row in d['joined_eight_high_'+suffix]]==old['joined_seven_high_'+suffix]
    mass=c.matrix(d['eight_high_physical_Gram'])
    assert all(mass[7][j]==c.iv(0) and mass[j][7]==c.iv(0) for j in range(7))
    assert F(99,100)<mass[7][7][0]<=mass[7][7][1]<=1
    assert c.iv(d['eighth_native_defect_after_seven_high_minorant'])[0]>0
    for key in ['eight_high_surplus_positive_proof','eight_high_inverse_denominator_positive_proof']:
        assert F(d[key]['congruence_Gershgorin_lower'])>0 and 0<=F(d[key]['inverse_residual_row_norm'])<1
    q=c.matrix(d['eight_high_native_Gram']);g=c.matrix(d['eight_high_complete_source_Gram'])
    n=direct.sub(direct.scale(g,1/direct.K),q)
    w=direct.sub(c.matrix(d['joined_eight_high_source_crosses']),direct.scale(c.matrix(d['joined_eight_high_native_crosses']),direct.K))
    ni,rho,error=direct.inverse([row[:7] for row in n[:7]])
    border=[[row[7]] for row in n[:7]];solved=direct.mm(ni,border)
    delta=c.sub(n[7][7],direct.mm(c.transpose(border),solved)[0][0]);assert delta[0]>0
    b=c.mul(c.iv(direct.K**2),delta)
    z=direct.sub([[row[7]] for row in w],direct.mm([row[:7] for row in w],solved))
    credit=[[c.div(direct.square(z[i][0]) if i==j else c.mul(z[i][0],z[j][0]),b) for j in range(3)] for i in range(3)]
    pubcredit=c.matrix(d['conditional_extra_joined_inverse_improvement'])
    assert all(c.overlap(credit[i][j],pubcredit[i][j]) for i in range(3) for j in range(3))
    k=c.matrix(d['conditional_eight_high_joined_Schur_lower_matrix'])
    kold=c.matrix(old['conditional_seven_high_joined_Schur_lower_matrix'])
    assert all(c.overlap(k[i][j],c.add(kold[i][j],credit[i][j])) for i in range(3) for j in range(3))
    h=list(map(F,d['frozen_NF45_witness']));assert h==list(map(F,old['updated_frozen_rational_witness']))
    assert c.overlap(c.quad(k,h),c.iv(d['conditional_frozen_witness_value']))
    zh=direct.mm([[c.iv(x) for x in h]],z)[0][0];gain=c.div(direct.square(zh),b);assert gain[0]>0
    assert c.overlap(gain,c.iv(d['conditional_extra_frozen_witness_improvement']))
    updated=list(map(F,d['updated_frozen_rational_witness']))
    assert updated[2]==1 and c.quad(k,updated)[0]>0
    assert c.overlap(c.quad(k,updated),c.iv(d['updated_witness_lower_certificate_value']))
    assert F(d['necessary_further_updated_witness_response_strict_lower'])==0
    evencheck=positive(k);oddcheck=positive(c.matrix(odd['conditional_seven_high_joined_Schur_lower_matrix']))
    assert c.overlap(c.iv(evencheck['condensed_margin']),c.iv(d['conditional_joined_condensed_margin']))
    assert c.overlap(c.iv(evencheck['determinant']),c.iv(d['conditional_joined_determinant']))
    current=next(r for r in direct.run(parentroot,oldroot)['parity_checks'] if r['parity']=='even')
    currentk=c.matrix(current['tightened_seven_source_lower_matrix']);s,ei,beta=condensation(currentk);assert s[1]<0
    zp=[z[0][0],z[1][0]]
    a=c.mm(c.mm([zp],ei),[[x] for x in zp])[0][0]
    tau=c.sub(z[2][0],c.sumiv(c.mul(x,y) for x,y in zip(zp,beta)))
    acceptance=c.sub(direct.square(tau),c.mul(c.neg(s),c.add(b,a)));assert acceptance[0]>0
    return dict(milestone='CC91',integration_parent='f61e5d65926837dd660b274391c5bdb9da30b8e6',
        read_only_source='6658ff2837838ab00b9b9c605fdd200d473c3293',
        even=evencheck,odd_preserved=oddcheck,eight_source_physical_orthogonality_to_seven=True,
        NF45_parent_entries_preserved_exactly=True,direct_eighth_response_matrix=[[c.pair(x) for x in row] for row in credit],
        direct_eighth_response_at_NF45_witness=c.pair(gain),full_cone_acceptance_surplus=c.pair(acceptance),
        new_response_outside_CC90_rejection_neighborhood=True,
        independently_verified_seven_block_inverse_residual_upper=c.pair(c.iv(rho))[1],
        both_fixed_joined_packets_conditionally_positive=True,
        background_floor_hypothesis=d['background_floor_hypothesis'],background_floor_newly_proved=False,
        native_integrations_replayed=False,physical_whole_domain_gap_certified=False,
        complete_retained_matrix_certified=False,whole_aperture_positive=False,
        highest_certified_whole_aperture='21/20')

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('NF46_root',type=Path);ap.add_argument('NF45_root',type=Path);ap.add_argument('NF44_root',type=Path);ap.add_argument('--output',type=Path,required=True)
    a=ap.parse_args();d=run(a.NF46_root,a.NF45_root,a.NF44_root);a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(d,indent=2)+'\n')
    print('CC91 PASS: NF46 even full matrix and response cone pass; NF45 odd positive sign preserved')
