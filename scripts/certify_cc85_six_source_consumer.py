#!/usr/bin/env python3
"""Authenticated certificate-level consumer of NF44's six-source update."""
import argparse,hashlib,json
from pathlib import Path
from fractions import Fraction as F
import certify_cc81_boundary_response_consumer as c
import certify_cc83_five_source_consumer as five

HASH={
'RPB108_NF44_EVEN_INVERSE_WITNESS_CERTIFICATE_20261009.json':'9a6d58d0b11aa435d32866823beb0f68477b87232bdb99351a91b0cb16521643',
'RPB108_NF44_ODD_INVERSE_WITNESS_CERTIFICATE_20261009.json':'94669181d3d09b682235e4f87b9f623de6a8b55702beedf1cd6330b116d8b5f4',
'RPB108_NF44_INVERSE_WITNESS_VALIDATION_20261009.json':'ef6cff6db90a4f6683771b4f81ccfefa2b166c2a84a391bff2950b64c84c6e05'}
def load(root,name):
    raw=(root/'notes/data'/name).read_bytes();assert hashlib.sha256(raw).hexdigest()==HASH[name]
    return json.loads(raw)
def run(root,root43,root42):
    val=load(root,'RPB108_NF44_INVERSE_WITNESS_VALIDATION_20261009.json')
    assert val['status']=='PASS' and not val['background_floor_newly_proved'] and not val['whole_aperture_positive']
    rows=[]
    for parity in ['even','odd']:
        name='RPB108_NF44_'+parity.upper()+'_INVERSE_WITNESS_CERTIFICATE_20261009.json';d=load(root,name)
        prior=five.load(root43,'RPB108_NF43_'+parity.upper()+'_INVERSE_WITNESS_CERTIFICATE_20261009.json')
        anchor=c.load(root42,'RPB108_NF42_'+parity.upper()+'_BOUNDARY_RESPONSE_CERTIFICATE_20261009.json')
        proof=next(x for x in val['parity_checks'] if x['parity']==parity)
        assert proof['certificate_sha256']==HASH[name] and d['NF43_input_sha256']==val['NF43_input_sha256']
        assert prior['fixed_trial_sha256'] in d['NF43_input_sha256']
        assert five.HASH['RPB108_NF43_'+parity.upper()+'_INVERSE_WITNESS_CERTIFICATE_20261009.json'] in d['NF43_input_sha256']
        assert not d['conditional_joined_sign_certified'] and not d['actual_negative_original_form_claimed']
        assert not d['background_floor_newly_proved'] and not d['whole_aperture_positive']
        mass=c.matrix(d['six_high_physical_Gram'])
        assert all(mass[5][i]==c.iv(0) and mass[i][5]==c.iv(0) for i in range(5))
        assert mass[5][5][0]>F(99,100) and mass[5][5][1]<=1
        assert c.iv(d['sixth_native_defect_after_five_high_minorant'])[0]>0
        for p in ['six_high_surplus_positive_proof','six_high_inverse_denominator_positive_proof']:
            assert F(d[p]['congruence_Gershgorin_lower'])>0 and 0<=F(d[p]['inverse_residual_row_norm'])<1
        k=c.matrix(d['conditional_six_high_joined_Schur_lower_matrix'])
        oldk=c.matrix(prior['conditional_five_high_joined_Schur_lower_matrix'])
        credit=c.matrix(d['conditional_extra_joined_inverse_improvement'])
        assert all(c.overlap(k[i][j],c.add(oldk[i][j],credit[i][j])) for i in range(3) for j in range(3))
        oldh=list(map(F,d['frozen_NF43_witness']))
        assert oldh==list(map(F,prior['updated_frozen_rational_witness']))
        gain=c.quad(credit,oldh);assert gain[0]>0 and c.overlap(gain,c.iv(d['conditional_extra_frozen_witness_improvement']))
        oldval=c.quad(k,oldh);assert oldval[1]<0 and c.overlap(oldval,c.iv(d['conditional_frozen_witness_value']))
        newh=list(map(F,d['updated_frozen_rational_witness']));assert newh!=oldh and newh[2]==1
        newval=c.quad(k,newh);assert newval[1]<0 and c.overlap(newval,c.iv(d['updated_witness_lower_certificate_value']))
        assert 0<F(d['necessary_further_updated_witness_response_strict_lower'])<=-newval[1]
        s,ei,beta=five.condensed(k);s5,_,_=five.condensed(oldk)
        s4,_,_=five.condensed(c.matrix(anchor['conditional_improved_joined_Schur_lower_matrix']))
        det=c.det3(k);assert det[1]<0 and c.overlap(det,c.iv(d['conditional_joined_determinant']))
        assert c.overlap(s,c.iv(d['conditional_joined_condensed_margin']))
        rows.append(dict(parity=parity,sixth_column_physically_orthogonal_to_all_five=True,
            signed_update_intervals_consistent=True,selection_witness_is_NF43_updated_witness=True,
            new_witness_is_distinct=True,additional_response_at_selection_witness=c.pair(gain),
            six_source_condensed_deficit=c.pair(c.neg(s)),fraction_of_five_source_deficit_remaining=c.pair(c.div(c.neg(s),c.neg(s5))),
            fraction_of_four_source_deficit_remaining=c.pair(c.div(c.neg(s),c.neg(s4))),
            necessary_new_witness_credit_lower=c.pair(c.iv(-newval[1]))[0],
            next_source_cone_leading_inverse=[[c.pair(x) for x in row] for row in ei],
            next_source_cone_signed_border=[c.pair(x) for x in beta],
            background_floor_hypothesis=d['background_floor_hypothesis']))
    return dict(milestone='CC85',integration_parent='67839d94626ff463d02fe2c1a872a84210c868b1',
        read_only_source='7bd6fbda5e156fbd009b6de0aeee6f41b1823c5c',input_sha256=HASH,parity_checks=rows,
        verification_scope='independent certificate matrix arithmetic and witness custody; native source integrations and inverse proof reconstruction not replayed',
        simultaneous_six_retained_direction_certificate=False,whole_aperture_positive=False)
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('NF44_root',type=Path);ap.add_argument('NF43_root',type=Path);ap.add_argument('NF42_root',type=Path);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args()
    d=run(a.NF44_root,a.NF43_root,a.NF42_root);a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(d,indent=2)+'\n')
    for r in d['parity_checks']:
        print(r['parity'],'remaining versus five',*[float(F(x)) for x in r['fraction_of_five_source_deficit_remaining']], 'versus four',*[float(F(x)) for x in r['fraction_of_four_source_deficit_remaining']])
