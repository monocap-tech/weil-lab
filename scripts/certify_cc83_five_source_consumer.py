#!/usr/bin/env python3
"""Independent signed matrix and witness custody checks for NF43."""
import argparse,hashlib,json
from pathlib import Path
from fractions import Fraction as F
import certify_cc81_boundary_response_consumer as c
from certify_cc82_rank_one_join_cone import inverse2

HASH={
'RPB108_NF43_EVEN_INVERSE_WITNESS_CERTIFICATE_20261009.json':'d46a4f1d52dc208b409a2de057283934b4a1d1808209a3068c59c38cad5502fe',
'RPB108_NF43_ODD_INVERSE_WITNESS_CERTIFICATE_20261009.json':'6f649ec13a3795ba24b28ab7aa0a89f7d4c7eafae15d7433bcd6906d1fa76ac7',
'RPB108_NF43_INVERSE_WITNESS_VALIDATION_20261009.json':'19d4d98fdc7a076450828380705fc3e7e618013bbc053c55e6496a6a895eb206'}
def load(root,name):
    raw=(root/'notes/data'/name).read_bytes();assert hashlib.sha256(raw).hexdigest()==HASH[name]
    return json.loads(raw)
def condensed(k):
    a=[r[:2] for r in k[:2]];ai=inverse2(a)
    assert a[0][0][0]>0
    r=[[k[0][2]],[k[1][2]]];beta=c.mm(c.transpose(r),ai)[0]
    s=c.sub(k[2][2],c.mm(c.mm(c.transpose(r),ai),r)[0][0]);assert s[1]<0
    return s,ai,beta
def run(root,parent):
    v=load(root,'RPB108_NF43_INVERSE_WITNESS_VALIDATION_20261009.json');assert v['status']=='PASS'
    assert not v['whole_aperture_positive'] and not v['background_floor_newly_proved']
    rows=[]
    for parity in ['even','odd']:
        d=load(root,'RPB108_NF43_'+parity.upper()+'_INVERSE_WITNESS_CERTIFICATE_20261009.json')
        old=c.load(parent,'RPB108_NF42_'+parity.upper()+'_BOUNDARY_RESPONSE_CERTIFICATE_20261009.json')
        assert d['NF42_input_sha256']==v['NF42_input_sha256']
        assert d['NF42_input_sha256']==[c.EXPECTED['RPB108_NF42_'+p+'_BOUNDARY_RESPONSE_CERTIFICATE_20261009.json'] for p in ['EVEN','ODD']]
        assert not d['conditional_joined_sign_certified'] and not d['actual_negative_original_form_claimed']
        proof=next(x for x in v['parity_checks'] if x['parity']==parity)
        assert proof['certificate_sha256']==HASH['RPB108_NF43_'+parity.upper()+'_INVERSE_WITNESS_CERTIFICATE_20261009.json']
        assert not d['background_floor_newly_proved'] and not d['whole_aperture_positive']
        mass=c.matrix(d['five_high_physical_Gram'])
        assert all(mass[4][i]==c.iv(0) and mass[i][4]==c.iv(0) for i in range(4))
        assert mass[4][4][0]>F(99,100) and mass[4][4][1]<=1
        assert c.iv(d['fifth_native_defect_after_four_high_minorant'])[0]>0
        for name in ['five_high_surplus_positive_proof','five_high_inverse_denominator_positive_proof']:
            assert F(d[name]['congruence_Gershgorin_lower'])>0
            assert 0<=F(d[name]['inverse_residual_row_norm'])<1
        k=c.matrix(d['conditional_five_high_joined_Schur_lower_matrix'])
        kold=c.matrix(old['conditional_improved_joined_Schur_lower_matrix'])
        credit=c.matrix(d['conditional_extra_joined_inverse_improvement'])
        assert all(c.overlap(k[i][j],c.add(kold[i][j],credit[i][j])) for i in range(3) for j in range(3))
        oldh=list(map(F,d['frozen_NF38_witness']));assert oldh==list(map(F,old['frozen_NF38_witness']))
        imp=c.quad(credit,oldh);assert imp[0]>0 and c.overlap(imp,c.iv(d['conditional_extra_frozen_witness_improvement']))
        oldvalue=c.quad(k,oldh);assert oldvalue[1]<0 and c.overlap(oldvalue,c.iv(d['conditional_frozen_witness_value']))
        newh=list(map(F,d['updated_frozen_rational_witness']));assert newh[2]==1 and newh!=oldh
        newvalue=c.quad(k,newh);assert newvalue[1]<0 and c.overlap(newvalue,c.iv(d['updated_witness_lower_certificate_value']))
        necessary=F(d['necessary_further_updated_witness_response_strict_lower'])
        assert 0<necessary<=-newvalue[1]
        s,ai,beta=condensed(k);sold,_,_=condensed(kold)
        det=c.det3(k);assert det[1]<0 and c.overlap(det,c.iv(d['conditional_joined_determinant']))
        assert c.overlap(s,c.iv(d['conditional_joined_condensed_margin']))
        remaining=c.div(c.neg(s),c.neg(sold))
        oldresponse=c.iv(old['conditional_frozen_witness_inverse_improvement'])
        gain_ratio=c.div(imp,oldresponse)
        if parity=='odd':assert gain_ratio[0]>5
        rows.append(dict(parity=parity,signed_update_intervals_consistent=True,
            fifth_physical_column_orthogonal_and_mass_certified=True,
            old_frozen_witness_unchanged=True,new_frozen_witness_distinct=True,
            additional_response_at_old_witness=c.pair(imp),new_witness_value=c.pair(newvalue),
            necessary_updated_witness_credit_lower=c.pair(c.iv(-newvalue[1]))[0],
            fifth_response_over_fourth_response_at_same_old_witness=c.pair(gain_ratio),
            condensed_deficit_fraction_remaining=c.pair(remaining),
            five_source_condensed_deficit=c.pair(c.neg(s)),
            next_source_cone_leading_inverse=[[c.pair(x) for x in row] for row in ai],
            next_source_cone_signed_border=[c.pair(x) for x in beta],
            background_floor_hypothesis=d['background_floor_hypothesis']))
    return dict(milestone='CC83',integration_parent='0e23cb1bc644786cd46dcd9bbe806601ff4b8473',
        read_only_source='b21b3df8e026db1b8b253325442b6dfaa63f05ef',input_sha256=HASH,
        verification_scope='independent certificate-level signed update, witness and cone arithmetic; source integrations not replayed',
        parity_checks=rows,simultaneous_six_direction_certificate=False,whole_aperture_positive=False)
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('source_root',type=Path);ap.add_argument('NF42_root',type=Path);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args()
    d=run(a.source_root,a.NF42_root);a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(d,indent=2)+'\n')
    for r in d['parity_checks']:
        print(r['parity'],'deficit fraction remaining',*[float(F(x)) for x in r['condensed_deficit_fraction_remaining']], 'next deficit',*[float(F(x)) for x in r['five_source_condensed_deficit']])
