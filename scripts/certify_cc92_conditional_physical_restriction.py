#!/usr/bin/env python3
"""Conditional physical coercivity for the original joined six directions + F."""
import argparse,hashlib,json
from pathlib import Path
from fractions import Fraction as F
import certify_cc81_boundary_response_consumer as c
import certify_cc87_seven_source_consumer as seven
import certify_cc88_correlated_seventh_response as direct
import certify_cc91_both_joined_pass as joined
import certify_cc80_defect_response_acceptance as exact

HASH={
'RPB108_NF36_EVEN_COLLECTIVE_CORRECTION_CERTIFICATE_20261009.json':'af7409645c5d28e56799ab56dbd862d0ae8e3b126ce56713e61f69277bcb5b18',
'RPB108_NF36_ODD_COLLECTIVE_CORRECTION_CERTIFICATE_20261009.json':'50e2cfa384d599daf3ea82d6602b0c1a84e3a86bbe738fb2e80b93177f25573f',
'RPB108_NF37_EVEN_FREE_CORRECTION_FUNCTIONAL_CERTIFICATE_20261009.json':'ed0827518c5a76c3fc0c56e795518b9e2be9f1edb9860ff78dd1577551cc757d',
'RPB108_NF37_ODD_FREE_CORRECTION_FUNCTIONAL_CERTIFICATE_20261009.json':'30c4e46afc86c022d8b867b2cbfaa698b4d5a9441fc7d79200045a0325d3d3af',
'RPB108_NF26_HIGH_CORRECTION_CERTIFICATE_20261009.json':'f2010510bacac64c45ef1825cd5e2c41e395519417815a43530e44e6cfdbf930',
'RPB108_NF29_LIFTED_RESPONSE_CERTIFICATE_20261009.json':'069d4acc267a0ac48154427a033cccca96243743dd31e36449f7189de03e895a',
'RPB108_NF30_FIXED_EXPANDED_RESPONSE_20261009.json':'7460d5ed3b159d34fa002a56382b40f91cde1d7712fe5e2b1b0ff2b4df7cb65b',
'RPB108_NF35_EVEN_JOINED_WITNESSES_CERTIFICATE_20261009.json':'68e9c2bb0c9109f6b781781f544b9da1271554819e199041360620ddbf3053c3',
'RPB108_NF35_ODD_JOINED_WITNESSES_CERTIFICATE_20261009.json':'eaeb8dff861eab54e3b0cc15457a209c62d4bf8dcbe884b74fef8ea9757e0879',
'RPB108_NF35_JOINED_WITNESSES_VALIDATION_20261009.json':'ab9e4ebd605063b6c3a929b96be9f0fc20c380c658f51d6055475e4b3ed1e3c9'}
def load(root,name):
    raw=(root/'notes/data'/name).read_bytes();assert hashlib.sha256(raw).hexdigest()==HASH[name]
    return json.loads(raw)
def controls():
    a=exact.mat([[2,F(1,4)],[F(1,4),1]]);kap=F(1,2)
    assert all(x>0 for x in exact.pivots(exact.add(a,exact.diag([-kap,-kap]))))
    r=[[F(1,3)],[F(1,5)]];ai=exact.inv(a);lift=exact.mul(ai,r)
    epsilon=F(1,100);q=epsilon+exact.mul(exact.mul(exact.tr(r),ai),r)[0][0]
    full=[[q,r[0][0],r[1][0]],[r[0][0],*a[0]],[r[1][0],*a[1]]]
    # Nonorthogonal lifted physical coordinates, including the high space.
    v=[F(1),F(3,4),F(1,2)]
    mass=[[sum(x*x for x in v),v[1],v[2]],[v[1],1,0],[v[2],0,1]]
    bound=F(12);coupling=sum(x[0]**2 for x in r)/kap**2
    gap=min(epsilon/(4*(bound+coupling)),kap/2)
    shifted=exact.add(full,[[-gap*x for x in row] for row in mass])
    assert all(x>0 for x in exact.pivots(shifted))
    h=[F(1),-lift[0][0],-lift[1][0]]
    energy=sum(h[i]*full[i][j]*h[j] for i in range(3) for j in range(3));assert energy==epsilon
    phys=sum(h[i]*mass[i][j]*h[j] for i in range(3) for j in range(3));assert phys>1
    assert energy<epsilon*phys  # A coordinate gap is not a physical gap.
    zero=[row[:] for row in full];zero[0][0]-=epsilon
    assert sum(h[i]*zero[i][j]*h[j] for i in range(3) for j in range(3))==0
    return dict(nonorthogonal_physical_completion_bound_positive=True,
        coordinate_gap_cannot_be_reused_as_physical_gap=True,
        zero_Schur_positive_background_control_has_physical_null=True)
def run(massroot,newroot,parentroot,oldroot):
    joined.run(newroot,parentroot,oldroot)
    val=load(massroot,'RPB108_NF35_JOINED_WITNESSES_VALIDATION_20261009.json');assert val['status']=='PASS'
    seed=load(massroot,'RPB108_NF26_HIGH_CORRECTION_CERTIFICATE_20261009.json')
    response=load(massroot,'RPB108_NF29_LIFTED_RESPONSE_CERTIFICATE_20261009.json')
    extra=load(massroot,'RPB108_NF30_FIXED_EXPANDED_RESPONSE_20261009.json')
    rows=[]
    for parity in ['even','odd']:
        name='RPB108_NF35_'+parity.upper()+'_JOINED_WITNESSES_CERTIFICATE_20261009.json'
        mass=load(massroot,name)
        proof=next(x for x in val['parity_checks'] if x['parity']==parity)
        assert proof['certificate_sha256']==HASH[name] and proof['retained_components_exactly_orthogonal']
        assert all(HASH[x] in mass['authenticated_input_sha256'] for x in [
            'RPB108_NF26_HIGH_CORRECTION_CERTIFICATE_20261009.json',
            'RPB108_NF29_LIFTED_RESPONSE_CERTIFICATE_20261009.json',
            'RPB108_NF30_FIXED_EXPANDED_RESPONSE_20261009.json'])
        seedpar=next(x for x in seed['parity_certificates'] if x['parity']==parity)
        pairpar=next(x for x in response['parity_certificates'] if x['parity']==parity)
        # Original orthonormal Legendre coordinates and orthogonal high lifts.
        assert 0<F(mass['inherited_retained_masses'][0])<F(121,100)
        assert F(seedpar['correction_norm_upper'])<F(1,10)
        assert 0<F(pairpar['lifted_response_norm_squared'])<1
        if parity=='even':
            assert len(set(extra['additional_high_indices']))==len(extra['fixed_rational_coefficients'])
            assert sum(abs(F(x)) for x in extra['fixed_rational_coefficients'])<F(1,10)
        assert F(mass['retained_witness_norm_upper'])<F(11,10)
        assert F(mass['high_witness_component_norm_upper'])<F(1,10)
        move=load(massroot,'RPB108_NF37_'+parity.upper()+'_FREE_CORRECTION_FUNCTIONAL_CERTIFICATE_20261009.json')
        correction=load(massroot,'RPB108_NF36_'+parity.upper()+'_COLLECTIVE_CORRECTION_CERTIFICATE_20261009.json')
        assert HASH[name] in move['NF35_input_sha256']
        assert HASH['RPB108_NF36_'+parity.upper()+'_COLLECTIVE_CORRECTION_CERTIFICATE_20261009.json'] in move['NF36_input_sha256']
        norm=F(correction['correction_norm_upper'])
        assert sum(F(x)**2 for x in move['correction_coefficients'])<=norm**2
        assert all(abs(F(x))*norm<F(1,10) for x in move['selected_rational_functional'])
        # NF35 norms <6/5; the actual NF37 lift movement is <1/10.
        # Hence the current lifted vectors have norm <2, and trace <12.
        physical_packet_gram_upper=F(12)
        if parity=='even':
            d=joined.load(newroot,'RPB108_NF46_EVEN_NEXT_SHELL_CERTIFICATE_20261009.json');count='eight'
        else:
            d=seven.load(parentroot,'RPB108_NF45_ODD_INVERSE_WITNESS_CERTIFICATE_20261009.json');count='seven'
        k=c.matrix(d['conditional_'+count+'_high_joined_Schur_lower_matrix'])
        positive=joined.positive(k);epsilon=F(positive['retained_coordinate_coercivity_lower']);assert epsilon>0
        gamma=c.matrix(move['original_selected_complete_source_Gram'])
        q=c.matrix(move['original_selected_native_energy_Gram'])
        gh=c.matrix(d[count+'_high_complete_source_Gram']);qh=c.matrix(d[count+'_high_native_Gram'])
        n=direct.sub(direct.scale(gh,1/direct.K),qh);ni,rho,error=direct.inverse(n)
        w=direct.sub(c.matrix(d['joined_'+count+'_high_source_crosses']),direct.scale(c.matrix(d['joined_'+count+'_high_native_crosses']),direct.K))
        reaction=direct.sub(direct.scale(gamma,1/direct.K),direct.scale(direct.mm(direct.mm(w,ni),c.transpose(w)),1/direct.K**2))
        reconstructed=direct.sub(q,reaction)
        assert all(c.overlap(reconstructed[i][j],k[i][j]) for i in range(3) for j in range(3))
        trace=sum(gamma[i][i][1] for i in range(3));assert trace>0
        inverse_source_norm_square_upper=trace/direct.K**2
        coefficient=4*(physical_packet_gram_upper+inverse_source_norm_square_upper)
        gap=min(epsilon/coefficient,direct.K/2);assert gap>0
        rows.append(dict(parity=parity,all_three_lifted_vector_norms_less_than_two=True,
            lifted_packet_Gram_operator_upper='12',original_native_and_source_identity_overlap=True,
            complete_source_Gram_trace_upper=c.pair(c.iv(trace))[1],
            inverse_source_operator_norm_square_upper=c.pair(c.iv(inverse_source_norm_square_upper))[1],
            retained_coordinate_coercivity_lower=str(epsilon),
            conditional_physical_gap_lower=c.pair(c.iv(gap))[0],
            background_floor_hypothesis=d['background_floor_hypothesis']))
    gap=min(F(x['conditional_physical_gap_lower']) for x in rows)
    return dict(milestone='CC92',integration_parent='713c1add89672a315a90518258b2f7a108fde4b5',
        read_only_source='6658ff2837838ab00b9b9c605fdd200d473c3293',parity_checks=rows,
        exact_parity_join_from_original_form=True,
        conditional_six_retained_directions_plus_all_F_gap_lower=str(gap),
        exact_controls=controls(),
        restriction_identity='span of original retained x,w,u32 in both parities plus F',
        background_floor_newly_proved=False,original_form_domain_attachment_inherited=True,
        complete_retained_matrix_certified=False,whole_aperture_positive=False,
        highest_certified_whole_aperture='21/20')

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('mass_root',type=Path);ap.add_argument('NF46_root',type=Path);ap.add_argument('NF45_root',type=Path);ap.add_argument('NF44_root',type=Path);ap.add_argument('--output',type=Path,required=True)
    a=ap.parse_args();d=run(a.mass_root,a.NF46_root,a.NF45_root,a.NF44_root);a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(d,indent=2)+'\n')
    print('CC92 PASS: conditional original six-retained-direction plus all-F physical gap',float(F(d['conditional_six_retained_directions_plus_all_F_gap_lower'])))
