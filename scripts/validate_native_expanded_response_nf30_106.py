#!/usr/bin/env python3
"""NF30 rational replay, original signed oracle and crossing controls."""
import argparse,json,hashlib
from pathlib import Path
from fractions import Fraction as F
from math import factorial
import certify_native_expanded_response_nf30_106 as p
n=p.n;I=p.I

def validate(trial,certificate):
    data=p.inputs();r,cv,ch,wi,wc,vi,vc=p.even(data)
    assert certificate['authenticated_input_sha256']==trial['authenticated_input_sha256']==p.HASHES
    zi=trial['additional_high_indices'];assert zi==list(range(116,181,2))
    selected=[I(*map(F,z)) for z in trial['reconstructed_selection_coordinates']]
    coeff=list(map(F,trial['fixed_rational_coefficients']))
    assert coeff==[F((z.mid()/4*10**100).__floor__(),10**100) for z in selected]
    eta_unit=2*n.A*4*F(106,125)**320/(1-F(106,125))+16*(n.A/2)**41/F(factorial(41))
    wh_mass=F(n.sqrt_r(sum(z*z for z in wc)).h,n.SCALE)
    selection_error=eta_unit*wh_mass
    paid_all=[z+I(-selection_error,selection_error) for z in selected]
    assert [z.ends() for z in paid_all]==trial['paid_original_selection_coordinates']
    captured=sum((n.sq(z) for z in paid_all),I(0))
    assert captured.ends()==trial['selected_shell_square']
    assert (captured/I(*map(F,ch['original_complete_residual_Gram'][1][1]))).ends()==trial['selected_shell_fraction_of_NF29_source_square']
    validation_path=Path('notes/data/RPB108_NF29_LIFTED_RESPONSE_VALIDATION_20261009.json')
    raw=validation_path.read_bytes();assert hashlib.sha256(raw).hexdigest()=='108dbf3d91f5cf6794d4004bbf5b1a87a022a44328851d7f02bd0c3c32391f7c'
    old=json.loads(raw);oracle=old['original_native_high_coordinate_checks'][0]
    assert oracle['parity']=='even' and oracle['test_degree']==118 and oracle['paid_overlap']
    expected=I(*map(F,oracle['original_independent_native_pairing']))
    paid=I(*map(F,trial['paid_original_selection_coordinates'][zi.index(118)]))
    assert paid.l<=expected.h and paid.h>=expected.l
    wz=I(*map(F,certificate['original_wh_z_pairing']));zz=I(*map(F,certificate['original_z_energy']));vz=I(*map(F,certificate['original_v_z_pairing']))
    for original,key in [(wz,'transpose_z_wh_pairing'),(vz,'transpose_z_v_pairing')]:
        other=I(*map(F,certificate[key]));assert original.l<=other.h and original.h>=other.l
    assert zz.l>0 and (2*wz-zz).l>0
    energy=[[I(*map(F,z)) for z in row] for row in certificate['original_finite_energy_Gram']]
    q0=I(*map(F,ch['original_finite_energy_Gram'][1][1]));mix0=I(*map(F,ch['original_finite_energy_Gram'][0][1]))
    assert energy[1][1].ends()==(q0-2*wz+zz).ends()
    assert energy[0][1].ends()==energy[1][0].ends()==(mix0-vz).ends()
    assert energy[0][0].ends()==ch['original_finite_energy_Gram'][0][0]
    assert energy[1][1].l>0 and (energy[0][0]*energy[1][1]-n.sq(energy[0][1])).l>0
    gram=[[I(*map(F,z)) for z in row] for row in certificate['reconstructed_residual_Gram']]
    true=[[I(*map(F,z)) for z in row] for row in certificate['original_complete_residual_Gram']]
    eta=list(map(F,certificate['physical_residual_error_bounds']))
    norms=[F(n.sqrt_r(F(gram[i][i].h,n.SCALE)).h,n.SCALE) for i in range(2)]
    for i in range(2):
        for j in range(2):
            e=eta[i]*norms[j]+eta[j]*norms[i]+eta[i]*eta[j]
            assert e==F(certificate['entrywise_source_Gram_errors'][i][j])
            assert true[i][j].ends()==(gram[i][j]+I(-e,e)).ends()
    assert true[0][1].ends()==true[1][0].ends()
    assert (true[0][0]*true[1][1]-n.sq(true[0][1])).l>0
    score=[[energy[i][j]-true[i][j]/F(207,1000) for j in range(2)] for i in range(2)]
    assert [[z.ends() for z in row] for row in score]==certificate['sufficient_collective_matrix']
    det=score[0][0]*score[1][1]-n.sq(score[0][1]);assert det.ends()==certificate['sufficient_matrix_determinant']
    assert (true[1][1]/energy[1][1]).ends()==certificate['expanded_response_square_over_energy']
    status=certificate['sufficient_collective_test_status']
    if status=='PASS':assert min(score[0][0].l,score[1][1].l,det.l)>0
    elif status=='SUFFICIENT_MATRIX_REJECTED':assert score[1][1].h<0 or det.h<0
    odd=data[4]['parity_certificates'][1];assert odd['parity']=='odd' and odd['sufficient_collective_test_status']=='PASS'
    odd_score=[[I(*map(F,z)) for z in row] for row in odd['sufficient_collective_matrix']]
    assert min(odd_score[0][0].l,odd_score[1][1].l,(odd_score[0][0]*odd_score[1][1]-n.sq(odd_score[0][1])).l)>0
    controls=[]
    for s in (F(-1,100),F(0),F(1,100)):
        a,b,d=F(1),F(1,2),F(1,4)+s
        assert a*d-b*b==s and a>0
        controls.append(dict(s=str(s),positive_first_diagonal=True,exact_determinant=str(s),collective_positive=s>0))
    out=dict(milestone='NF30',status='PASS',validated_sufficient_test_status=status,
        authenticated_original_signed_projection118_overlap=True,independent_native_projection_oracle=oracle,
        fixed_rational_trial_rule_replayed=True,paid_bilinear_symmetry_checks_replayed=True,
        energy_and_physical_Gram_error_payments_replayed=True,complete_matrix_sign_replayed=True,
        odd_NF29_success_unchanged=True,removed_native_energy=(2*wz-zz).ends(),
        removed_native_energy_fraction=((2*wz-zz)/q0).ends(),exact_collective_crossing_controls=controls,
        full_retained_background_certified=False,whole_aperture_positive=False)
    if status=='PASS':
        scalar=score[0][0]-n.sq(score[0][1])/score[1][1];assert scalar.l>0
        out['response_eliminated_sufficient_scalar']=scalar.ends()
    return out

if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('trial');a.add_argument('certificate');a.add_argument('--output',required=True);a=a.parse_args()
    traw=Path(a.trial).read_bytes();craw=Path(a.certificate).read_bytes();cert=json.loads(craw)
    assert hashlib.sha256(traw).hexdigest()==cert['fixed_trial_sha256']
    out=validate(json.loads(traw),cert);out['trial_sha256']=hashlib.sha256(traw).hexdigest();out['certificate_sha256']=hashlib.sha256(craw).hexdigest()
    Path(a.output).write_text(json.dumps(out,indent=2)+'\n')
