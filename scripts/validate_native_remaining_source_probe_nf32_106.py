#!/usr/bin/env python3
"""NF32 exact sign/payment replay and independent native source oracle."""
import json,argparse,hashlib,gzip,base64
from pathlib import Path
from fractions import Fraction as F
import certify_native_remaining_source_probe_nf32_106 as p
n=p.n;I=p.I

def det3(a):
    return a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])-a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])+a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0])

def validate(trial,cert,data,source):
    idx=0 if cert['parity']=='even' else 1
    r=data[0]['authenticated_compensated_targets'][idx];w=list(map(F,data[2]['parity_certificates'][idx]['exact_rational_retained_response']))
    x=list(map(F,r['retained_coefficients']));u=list(map(F,trial['parities'][idx]['fixed_rational_probe_coefficients']))
    T,a,b,free=p.prev.complement(x,w)
    coords=list(map(F,trial['parities'][idx]['frozen_constraint_coordinates']))
    assert u==[sum(c*d for c,d in zip(row,coords)) for row in T]
    assert sum(c*d for c,d in zip(x,u))==sum(c*d for c,d in zip(w,u))==0
    assert sum(z*z for z in u)==F(cert['fixed_probe_mass']) and F(999,1000)**2<F(cert['fixed_probe_mass'])<F(1001,1000)**2
    yraw=Path('notes/data/RPB108_NF26_FIXED_HIGH_CORRECTIONS_20261009.json').read_bytes()
    assert hashlib.sha256(yraw).hexdigest()=='814fe0fcc3aff4eecbe4e6c6eead5ce28927043877c0df9cfa03e3a5c71c2336'
    y=json.loads(yraw)['parities'][idx]
    vc=list(map(F,r['retained_coefficients']+r['exact_rational_high_compensation']))+[-F(z) for z in y['rational_correction_coefficients']]
    assert sum(z*z for z in vc)<F(1001,1000)**2
    q=[[I(*map(F,z)) for z in row] for row in cert['original_native_energy_Gram']]
    def Q(i,j):return I(*map(F,source[f'{min(i,j)},{max(i,j)}']['full']))
    native=sum((v*z*Q(i,j) for i,v in zip(r['retained_indices'],u) for j,z in zip(r['retained_indices'],u)),I(0))
    # Independent expansion changes fixed-grid rounding order. Both
    # enclosures must overlap; their serialized endpoints need not match.
    assert native.l>0 and native.l<=q[2][2].h and native.h>=q[2][2].l
    native_det=det3(q);assert min(q[0][0].l,q[1][1].l,q[2][2].l,native_det.l)>0
    gram=[[I(*map(F,z)) for z in row] for row in cert['original_complete_source_Gram']]
    old=data[5] if idx==0 else data[3]['parity_certificates'][idx]
    assert [[z.ends() for z in row[:2]] for row in gram[:2]]==old['original_complete_residual_Gram']
    eta=list(map(F,cert['physical_residual_error_bounds']))
    probe=I(*map(F,cert['new_reconstructed_source_entries']['2,2']));pn=F(n.sqrt_r(F(probe.h,n.SCALE)).h,n.SCALE)
    for i in range(3):
        norm=pn if i==2 else F(n.sqrt_r(F(gram[i][i].h,n.SCALE)).h,n.SCALE)+eta[i]
        err=eta[i]*pn+eta[2]*norm+eta[i]*eta[2]
        assert err==F(cert['new_entrywise_error_payments'][f'{i},2'])
        value=I(*map(F,cert['new_reconstructed_source_entries'][f'{i},2']))
        assert (value+I(-err,err)).ends()==gram[i][2].ends()==gram[2][i].ends()
    score=[[q[i][j]-gram[i][j]/F(207,1000) for j in range(3)] for i in range(3)]
    assert [[z.ends() for z in row] for row in score]==cert['sufficient_matrix']
    ratio=gram[2][2]/q[2][2];assert ratio.ends()==cert['remaining_probe_source_square_over_native_energy']
    if cert['sufficient_frame_status']=='SUFFICIENT_FRAME_REJECTED':assert score[2][2].h<0 and ratio.l>F(207,1000)*n.SCALE
    raw=gzip.decompress(base64.b64decode(Path('notes/data/RPB108_NF24_NATIVE_RESIDUAL_PROJECTIONS_117_118_20261009.json.gz.b64').read_bytes()))
    assert hashlib.sha256(raw).hexdigest()=='4c8b0067088486e20f31a7904d3bf56a9f654e982b15450efa85cd6b25e24346'
    projection=json.loads(raw)['complete_original_signed_source'];j=118 if idx==0 else 117
    oracle=sum((z*I(*map(F,projection[f'{i},{j}']['full'])) for i,z in zip(r['retained_indices'],u)),I(0))
    check=cert['independent_native_projection_check'];assert oracle.ends()==check['original_native_pairing']
    from math import factorial
    unit=2*n.A*4*F(106,125)**320/(1-F(106,125))+16*(n.A/2)**41/F(factorial(41))
    mass=F(n.sqrt_r(F(cert['fixed_probe_mass'])).h,n.SCALE)
    cv=data[1]['parity_certificates'][idx];ch=data[3]['parity_certificates'][idx]
    ids=r['retained_indices'];hi=ch['high_lift_indices']
    wh=w+[-F(z) for z in ch['fixed_rational_high_lift']]
    lv=[I(*map(F,a))-I(*map(F,b)) for a,b in zip(r['low_source_coordinates'],cv['retained_approximant_Ly_coordinates'])]
    lw=[sum((z*Q(i,j) for i,z in zip(ids+hi,wh)),I(0)) for j in ids]
    error=[F(cv['correction_norm_upper'])*unit,F(0),F(0)]
    physical_t=wh[:]
    if idx==0:
        lw=[a-I(*map(F,b)) for a,b in zip(lw,data[5]['retained_approximant_Lz_coordinates'])]
        z=list(map(F,data[4]['fixed_rational_coefficients']));physical_t+=[-v for v in z]
        error[1]=unit*F(n.sqrt_r(sum(v*v for v in z)).h,n.SCALE)
    lu=[sum((z*Q(i,j) for i,z in zip(ids,u)),I(0)) for j in ids]
    low=[lv,lw,lu];masses=[F(1001,1000),F(n.sqrt_r(sum(z*z for z in physical_t)).h,n.SCALE),mass]
    radii=[8*max(F(v.h-v.l,2*n.SCALE) for v in row) for row in low]
    assert [masses[i]*unit+radii[i]+error[i] for i in range(3)]==eta
    for i in range(2):
        expected=p.dot(u,low[i])+I(-error[i]*mass,error[i]*mass)
        assert expected.ends()==q[i][2].ends()==q[2][i].ends()
    paid=I(*map(F,check['reconstructed_pairing']))+I(-unit*mass,unit*mass)
    assert paid.l<=oracle.h and paid.h>=oracle.l
    assert not cert['actual_negative_vector_claimed'] and not cert['all_remaining_source_Gram_entries_certified']
    credit=gram[2][2]/F(207,1000)-q[2][2]
    fraction=I(1)-F(207,1000)*q[2][2]/gram[2][2]
    return dict(parity=cert['parity'],exact_constraint_membership_replayed=True,original_native_energy_replayed=True,native_energy_determinant=native_det.ends(),
        necessary_fixed_probe_inverse_credit=credit.ends(),necessary_fraction_of_floor_response_credit=fraction.ends(),
        source_payments_and_signed_entries_replayed=True,independent_original_native_projection_overlap=True,sufficient_status_replayed=cert['sufficient_frame_status'])

if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('trial');a.add_argument('even');a.add_argument('odd');a.add_argument('--output',required=True);a=a.parse_args()
    traw=Path(a.trial).read_bytes();trial=json.loads(traw);data,source,hashes=p.prev.inputs()
    raw=[Path(path).read_bytes() for path in (a.even,a.odd)];certs=list(map(json.loads,raw))
    assert all(c['fixed_trial_sha256']==hashlib.sha256(traw).hexdigest() for c in certs)
    result=[validate(trial,c,data,source) for c in certs]
    # Scalar and mixed controls: a negative diagonal excludes positivity,
    # while positive diagonals alone do not control a mixed determinant.
    controls=[]
    for b in (F(99,100),F(1),F(101,100)):
        controls.append(dict(positive_diagonals=True,mixed=str(b),exact_determinant=str(1-b*b)))
    levels=[]
    for s in (F(1,1000),F(1,10),F(2)):
        assert (1+s)**2-1==s*(2+s) and (1+s)-1==s
        levels.append(dict(mass_shift=str(s),shifted_null_matrix=[[str(1+s),'1'],['1',str(1+s)]],exact_ground_level=str(s)))
    out=dict(milestone='NF32',status='PASS',parity_validations=result,exact_positive_null_negative_controls=controls,positive_mass_shift_of_null_matrix_controls=levels,
        fixed_trial_sha256=hashlib.sha256(traw).hexdigest(),certificate_sha256=[hashlib.sha256(b).hexdigest() for b in raw],whole_aperture_positive=False)
    Path(a.output).write_text(json.dumps(out,indent=2)+'\n')
