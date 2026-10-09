#!/usr/bin/env python3
"""Authenticated NF45 certificate consumer; no native integration replay."""
import argparse, hashlib, json
from pathlib import Path
from fractions import Fraction as F
import certify_cc81_boundary_response_consumer as c
import certify_cc83_five_source_consumer as five
import certify_cc85_six_source_consumer as six

HASH={
'RPB108_NF45_EVEN_INVERSE_WITNESS_CERTIFICATE_20261009.json':'90d03525ee54da02f6e6662460cc18bea2d5740f39f28449de66dea76fa3b5b5',
'RPB108_NF45_ODD_INVERSE_WITNESS_CERTIFICATE_20261009.json':'694204c23b11cfb0af07d26be4a8a0bfe6ab68f8d2e431e2de23390470e28c1c',
'RPB108_NF45_INVERSE_WITNESS_VALIDATION_20261009.json':'d555f03e507f4b410588bdaa28f851e99ba6aaaf3b85811504e88dccaba12391'}
def load(root,name):
    raw=(root/'notes/data'/name).read_bytes();assert hashlib.sha256(raw).hexdigest()==HASH[name]
    return json.loads(raw)

def run(root,oldroot):
    val=load(root,'RPB108_NF45_INVERSE_WITNESS_VALIDATION_20261009.json')
    assert val['status']=='PASS' and not val['background_floor_newly_proved'] and not val['whole_aperture_positive']
    rows=[]
    for parity in ['even','odd']:
        name='RPB108_NF45_'+parity.upper()+'_INVERSE_WITNESS_CERTIFICATE_20261009.json'
        d=load(root,name);old=six.load(oldroot,'RPB108_NF44_'+parity.upper()+'_INVERSE_WITNESS_CERTIFICATE_20261009.json')
        proof=next(x for x in val['parity_checks'] if x['parity']==parity)
        assert proof['certificate_sha256']==HASH[name] and proof['trial_sha256']==d['fixed_trial_sha256']
        assert d['NF44_input_sha256']==val['NF44_input_sha256']
        assert old['fixed_trial_sha256'] in d['NF44_input_sha256']
        assert six.HASH['RPB108_NF44_'+parity.upper()+'_INVERSE_WITNESS_CERTIFICATE_20261009.json'] in d['NF44_input_sha256']
        assert not any(d[k] for k in ['background_floor_newly_proved','actual_negative_original_form_claimed','whole_aperture_positive','RH','F4','Lean'])
        for suffix in ['physical_Gram','native_Gram','complete_source_Gram']:
            new=d['seven_high_'+suffix];previous=old['six_high_'+suffix]
            assert [[v for v in row[:6]] for row in new[:6]]==previous
        for suffix in ['native_crosses','source_crosses']:
            assert [row[:6] for row in d['joined_seven_high_'+suffix]]==old['joined_six_high_'+suffix]
        mass=c.matrix(d['seven_high_physical_Gram'])
        assert all(mass[6][j]==c.iv(0) and mass[j][6]==c.iv(0) for j in range(6))
        assert F(99,100)<mass[6][6][0]<=mass[6][6][1]<=1
        assert c.iv(d['seventh_native_defect_after_six_high_minorant'])[0]>0
        for field in ['seven_high_surplus_positive_proof','seven_high_inverse_denominator_positive_proof']:
            assert F(d[field]['congruence_Gershgorin_lower'])>0 and 0<=F(d[field]['inverse_residual_row_norm'])<1
        k=c.matrix(d['conditional_seven_high_joined_Schur_lower_matrix'])
        assert k==c.transpose(k)
        kold=c.matrix(old['conditional_six_high_joined_Schur_lower_matrix'])
        credit=c.matrix(d['conditional_extra_joined_inverse_improvement'])
        assert all(c.overlap(k[i][j],c.add(kold[i][j],credit[i][j])) for i in range(3) for j in range(3))
        h=list(map(F,d['frozen_NF44_witness']));assert h==list(map(F,old['updated_frozen_rational_witness']))
        gain=c.quad(credit,h);assert c.overlap(gain,c.iv(d['conditional_extra_frozen_witness_improvement']))
        assert c.overlap(c.quad(k,h),c.iv(d['conditional_frozen_witness_value']))
        updated=list(map(F,d['updated_frozen_rational_witness']));assert updated[2]==1
        witness=c.quad(k,updated);assert c.overlap(witness,c.iv(d['updated_witness_lower_certificate_value']))
        e=[row[:2] for row in k[:2]];ei=five.inverse2(e)
        r=[[k[0][2]],[k[1][2]]];beta=c.mm(c.transpose(r),ei)[0]
        s=c.sub(k[2][2],c.mm(c.mm(c.transpose(r),ei),r)[0][0]);det=c.det3(k)
        edet=c.det2(e)
        assert k[0][0][0]>0 and edet[0]>0
        assert c.overlap(s,c.iv(d['conditional_joined_condensed_margin'])) and c.overlap(det,c.iv(d['conditional_joined_determinant']))
        passing=parity=='odd';assert d['conditional_joined_sign_certified']==passing
        assert d['seven_high_minorant_fails_to_certify']==(not passing)
        epsilon=None
        if passing:
            assert s[0]>0 and det[0]>0 and witness[0]>0 and gain[0]>0
            assert F(d['necessary_further_updated_witness_response_strict_lower'])==0
            # E >= det(E)/trace(E) I, then bound the inverse triangular
            # condensation map by its Frobenius norm (see CC87 proof).
            trace_upper=e[0][0][1]+e[1][1][1]
            leading=edet[0]/trace_upper
            inverse_map_norm_square=3+sum(max(abs(v[0]),abs(v[1]))**2 for v in beta)
            epsilon=min(leading,s[0])/inverse_map_norm_square;assert epsilon>0
        else:
            assert s[1]<0 and det[1]<0 and witness[1]<0
            assert gain[0]<0<gain[1]
            assert 0<F(d['necessary_further_updated_witness_response_strict_lower'])<=-witness[1]
        rows.append(dict(parity=parity,prior_packet_entries_preserved_exactly=True,
            physical_orthogonality_to_six=True,selection_witness_is_NF44_updated_witness=True,
            signed_matrix_update_consistent=True,extra_response_at_selection_witness=c.pair(gain),
            condensed_margin=c.pair(s),determinant=c.pair(det),conditional_positive_definite=passing,
            rational_retained_coordinate_coercivity_lower=c.pair(c.iv(epsilon))[0] if epsilon else None,
            next_even_witness_necessary_credit_lower=c.pair(c.iv(-witness[1]))[0] if not passing else None,
            background_floor_hypothesis=d['background_floor_hypothesis']))
    return dict(milestone='CC87',integration_parent='a793a8eb4703046ff06956416cb00a3fe378b228',
        read_only_source='5f8a6c1e54a39236df253a5aae5f7be55fee74ed',parity_checks=rows,
        native_integrations_replayed=False,inverse_proof_reconstructed=False,
        background_floor_newly_proved=False,simultaneous_six_retained_direction_sign=False,
        whole_aperture_positive=False,highest_certified_whole_aperture='21/20')

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('NF45_root',type=Path);ap.add_argument('NF44_root',type=Path);ap.add_argument('--output',type=Path,required=True)
    a=ap.parse_args();d=run(a.NF45_root,a.NF44_root);a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(d,indent=2)+'\n')
    print('CC87 PASS: odd joined matrix conditionally positive definite; even remains indefinite')
