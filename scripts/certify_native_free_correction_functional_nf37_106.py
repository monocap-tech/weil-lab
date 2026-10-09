#!/usr/bin/env python3
"""NF37: all real correction functionals along each exact NF36 polynomial."""
import argparse, hashlib, json
from pathlib import Path
from fractions import Fraction as F
import certify_native_collective_correction_nf36_106 as c
n=c.n; I=c.I; iv=c.iv; dot=c.dot; mv=c.p.mv
K=F(207,1000)
NAMES=['EVEN_FIXED_COLLECTIVE_CORRECTION','ODD_FIXED_COLLECTIVE_CORRECTION',
       'EVEN_COLLECTIVE_CORRECTION_CERTIFICATE','ODD_COLLECTIVE_CORRECTION_CERTIFICATE',
       'COLLECTIVE_CORRECTION_VALIDATION']
SHA36=['2c02d0a5f89275c02d217df1b59a268a386f7ddd95d5ab6c3f590ebe5b2851a3',
       'f8fc52d72276f43fd318ec929795bb88b55cb0a3c88c0ca572702362ce37f578',
       'af7409645c5d28e56799ab56dbd862d0ae8e3b126ce56713e61f69277bcb5b18',
       '50e2cfa384d599daf3ea82d6602b0c1a84e3a86bbe738fb2e80b93177f25573f',
       '51720dd0aa541f4d91c1dcbbc7ccc80d4b8b8d426bb998a0113377f0c8bd396d']
def parents():
    raw=[Path('notes/data/RPB108_NF36_'+s+'_20261009.json').read_bytes() for s in NAMES]
    assert [hashlib.sha256(v).hexdigest() for v in raw]==SHA36
    out=list(map(json.loads,raw)); assert out[-1]['status']=='PASS'
    old=c.parents()
    for i in range(2):
        assert out[i+2]['fixed_trial_sha256']==SHA36[i]
        assert out[i+2]['NF35_input_sha256']==c.SHA35
        assert out[i+2]['all_real_tau_floor_family_rejected']
    return out,old
def matrix(v): return [[iv(x) for x in row] for row in v]
def ends(v): return [[x.ends() for x in row] for row in v]
def update(q,g,beta,qz,zeta,gz,lam):
    Q=[[q[i][j]-beta[i]*lam[j]-lam[i]*beta[j]+qz*lam[i]*lam[j] for j in range(3)] for i in range(3)]
    G=[[g[i][j]-zeta[i]*lam[j]-lam[i]*zeta[j]+gz*lam[i]*lam[j] for j in range(3)] for i in range(3)]
    return Q,G
def witness(v):
    a,b,d=v[0][0].mid(),v[0][1].mid(),v[1][1].mid()
    p,q=v[0][2].mid(),v[1][2].mid(); det=a*d-b*b
    assert det>0
    return [-F((x*10**100).__floor__(),10**100) for x in [(d*p-b*q)/det,(a*q-b*p)/det]]+[F(1)]
def run(parity):
    data,old=parents(); idx=['even','odd'].index(parity); cert=data[idx+2]; prior=old[idx]
    q=matrix(prior['original_joined_native_energy_Gram']); g=matrix(prior['original_joined_complete_source_Gram'])
    beta=list(map(iv,cert['original_native_correction_crosses'])); zeta=list(map(iv,cert['original_correction_source_crosses']))
    qz=iv(cert['original_correction_native_energy']); gz=iv(cert['original_correction_projected_source_square'])
    U=[[q[i][j]-g[i][j]/K for j in range(3)] for i in range(3)]
    e=[beta[i]-zeta[i]/K for i in range(3)]; d=qz-gz/K; assert d.h<0
    V=[[U[i][j]-(n.sq(e[i]) if i==j else e[i]*e[j])/d for j in range(3)] for i in range(3)]
    det2=V[0][0]*V[1][1]-n.sq(V[0][1]); assert V[0][0].l>0 and det2.l>0
    det=c.parent.det3(V); assert det.h<0
    reaction=(V[1][1]*n.sq(V[0][2])-2*V[0][1]*V[0][2]*V[1][2]+V[0][0]*n.sq(V[1][2]))/det2
    margin=V[2][2]-reaction; assert margin.h<0
    h=witness(V); value=dot(h,mv(V,h)); assert value.h<0
    a=dot(h,mv(U,h)); b=dot(h,e)
    upper=F(a.h,n.SCALE)+b.absupper()**2/(-F(d.h,n.SCALE)); assert upper<0
    # Diagnostic selection only: the candidate sign uses full paid matrices.
    lam=[F(((v/d).mid()*10**100).__floor__(),10**100) for v in e]
    Q,G=update(q,g,beta,qz,zeta,gz,lam)
    packet=c.parent.sign_packet(Q,G,list(map(F,prior['inherited_retained_masses'])))
    assert packet['joined_status']=='JOINED_FLOOR_REJECTED'
    selectedU=matrix(packet['sufficient_matrix']); selectedvalue=dot(h,mv(selectedU,h)); native=dot(h,mv(Q,h))
    assert selectedvalue.h<0 and native.l>0
    oldh=list(map(F,prior['fixed_rational_mixed_floor_witness'])); oldvalue=dot(oldh,mv(selectedU,oldh)); oldnative=dot(oldh,mv(Q,oldh))
    assert oldvalue.l>0 and oldnative.l>0
    print(parity,'all free functionals rejected; universal witness upper',float(upper),flush=True)
    return dict(milestone='NF37',parity=parity,aperture='53/50',kappa=str(K),interval_grid_digits=500,
        NF36_input_sha256=SHA36,NF35_input_sha256=c.SHA35,
        correction_indices=data[idx]['correction_indices'],correction_coefficients=data[idx]['fixed_rational_correction_coefficients'],
        original_floor_matrix=ends(U),correction_floor_crosses=[v.ends() for v in e],correction_floor_diagonal=d.ends(),
        all_real_functional_Loewner_ceiling=ends(V),ceiling_leading_pair_determinant=det2.ends(),ceiling_determinant=det.ends(),ceiling_condensed_margin=margin.ends(),
        universal_fixed_rational_witness=list(map(str,h)),universal_witness_ceiling_value=value.ends(),
        universal_witness_scalar_coefficients=dict(a=a.ends(),b=b.ends(),d=d.ends()),
        universal_witness_all_real_functional_upper=str(upper),every_real_three_coordinate_functional_floor_rejected=True,
        selected_rational_functional=list(map(str,lam)),original_selected_native_energy_Gram=ends(Q),original_selected_complete_source_Gram=ends(G),selected_sign_packet=packet,
        universal_witness_selected_floor_value=selectedvalue.ends(),universal_witness_selected_native_energy=native.ends(),
        NF35_original_mixed_witness_selected_floor_value=oldvalue.ends(),NF35_original_mixed_witness_selected_native_energy=oldnative.ends(),
        source_moments_reused_without_new_approximation=True,source_terms='complete original archimedean, prime and pole; all signed crosses and physical error payments inherited from NF36',
        independent_high_directions_certified=False,joined_retained_dimension_certified=4,
        actual_negative_original_form_claimed=False,whole_aperture_positive=False,RH=False,F4=False,Lean=False)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--parity',choices=['even','odd'],required=True);p.add_argument('--output',required=True);p=p.parse_args()
    Path(p.output).write_text(json.dumps(run(p.parity),indent=2)+'\n')
