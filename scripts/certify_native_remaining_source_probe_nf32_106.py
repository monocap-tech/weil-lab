#!/usr/bin/env python3
"""NF32: original complete source and signed crosses on a remaining T probe.
Negative sufficient values reject this unlifted frame, not original positivity.
"""
import argparse,json,gzip,base64,hashlib
from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal as D,localcontext
import certify_native_remaining_background_nf31_106 as prev
import certify_native_expanded_response_nf30_106 as engine
n=prev.n;I=n.I;dot=prev.dot;mv=prev.mv

def dec(v):
    v=F(v);return D(v.numerator)/D(v.denominator)

class Moments(engine.Moments):
    def __init__(self,degree,parity):self.parity=parity;super().__init__(degree)
    def source(self,ids,coeff):
        p,b,l=engine.base.source(ids,coeff,self.c,self.parity)
        shifted=[n.scale(n.shifted(p,t),-w) for t,w in self.shifts]
        return p,b,l,[engine.base.sum_polys([shifted[j] for j in a]) for a in self.active]

def choose(data,source):
    targets,nf26,nf27,nf29,trial,nf30=data;out=[]
    for r,cw in zip(targets['authenticated_compensated_targets'],nf27['parity_certificates']):
        ids=r['retained_indices'];x=list(map(F,r['retained_coefficients']));w=list(map(F,cw['exact_rational_retained_response']))
        T,p,q,free=prev.complement(x,w)
        A=[[I(*map(F,source[f'{min(i,j)},{max(i,j)}']['full'])) for j in ids] for i in ids]
        AT=[[dot(row,col) for col in zip(*T)] for row in A]
        C=[[dot(col,row) for row in zip(*AT)] for col in zip(*T)]
        inverse,proof=prev.matrix.inverse(C)
        # The largest physical inverse diagonal chooses an inverse-column
        # trial only. No eigenvector identity or eigenvalue is assumed.
        diagonal=[dot(row,mv(inverse,row)) for row in T]
        coordinate=max(range(56),key=lambda i:diagonal[i].mid())
        raw=[v.mid() for v in mv(inverse,T[coordinate])]
        physical=[sum(a*b for a,b in zip(row,raw)) for row in T]
        with localcontext() as ctx:
            ctx.prec=200
            mass=sum((dec(v)**2 for v in physical),D(0)).sqrt()
            frozen=[F((dec(v)/mass*D(10)**100).to_integral_value(rounding='ROUND_FLOOR'))/10**100 for v in raw]
        coeff=[sum(a*b for a,b in zip(row,frozen)) for row in T]
        assert sum(a*b for a,b in zip(x,coeff))==sum(a*b for a,b in zip(w,coeff))==0
        norm=sum(v*v for v in coeff);assert F(999,1000)**2<norm<F(1001,1000)**2
        out.append(dict(parity=r['parity'],retained_indices=ids,selected_inverse_column=coordinate,
            frozen_constraint_coordinates=list(map(str,frozen)),fixed_rational_probe_coefficients=list(map(str,coeff)),
            exact_physical_probe_mass=str(norm),exact_probe_orthogonal_to_seed_and_response=True))
    return dict(milestone='NF32',selection_rule='largest physical inverse diagonal; normalize its fixed midpoint inverse-column trial and round constraint coefficients down to denominator10^100',
        authenticated_input_sha256=prev.SHA,parities=out,selection_is_not_a_source_sign_certificate=True)

def run(data,source,trial,parity):
    idx=0 if parity=='even' else 1
    targets,nf26,nf27,nf29,ztrial,nf30=data
    r=targets['authenticated_compensated_targets'][idx];cv=nf26['parity_certificates'][idx];cw=nf27['parity_certificates'][idx];ch=nf29['parity_certificates'][idx];tr=trial['parities'][idx]
    assert tr['parity']==parity and trial['authenticated_input_sha256']==prev.SHA
    ids=r['retained_indices'];u=list(map(F,tr['fixed_rational_probe_coefficients']))
    x=list(map(F,r['retained_coefficients']));w=list(map(F,cw['exact_rational_retained_response']))
    assert sum(a*b for a,b in zip(x,u))==sum(a*b for a,b in zip(w,u))==0
    assert sum(z*z for z in u)==F(tr['exact_physical_probe_mass'])
    h=ch['high_lift_indices'];wi=ids+h;wc=w+[-F(z) for z in ch['fixed_rational_high_lift']]
    # NF26 fixed high correction is authenticated by NF30's parent inputs.
    yraw=Path('notes/data/RPB108_NF26_FIXED_HIGH_CORRECTIONS_20261009.json').read_bytes()
    assert hashlib.sha256(yraw).hexdigest()=='814fe0fcc3aff4eecbe4e6c6eead5ce28927043877c0df9cfa03e3a5c71c2336'
    y=json.loads(yraw)['parities'][idx]
    vi=ids+r['high_indices']+y['high_indices'];vc=list(map(F,r['retained_coefficients']+r['exact_rational_high_compensation']))+[-F(z) for z in y['rational_correction_coefficients']]
    assert len(vi)==len(set(vi)) and sum(z*z for z in vc)<F(1001,1000)**2
    if parity=='even':wi+=ztrial['additional_high_indices'];wc+=[-F(z) for z in ztrial['fixed_rational_coefficients']]
    m=Moments(1020,parity)
    columns=[m.source(vi,vc),m.source(wi,wc),m.source(ids,u)]
    print(parity,'constructed all three original sources',flush=True)
    def Q(i,j):return I(*map(F,source[f'{min(i,j)},{max(i,j)}']['full']))
    lv=[I(*map(F,a))-I(*map(F,b)) for a,b in zip(r['low_source_coordinates'],cv['retained_approximant_Ly_coordinates'])]
    # L(w-h) has exact original finite116 retained native coordinates.
    lw=[sum((z*Q(i,j) for i,z in zip(ids+h,w+[-F(z) for z in ch['fixed_rational_high_lift']])),I(0)) for j in ids]
    error=[F(cv['correction_norm_upper'])*m.eta,F(0),F(0)]
    if parity=='even':
        lw=[a-I(*map(F,b)) for a,b in zip(lw,nf30['retained_approximant_Lz_coordinates'])]
        error[1]=m.eta*F(n.sqrt_r(sum(F(z)**2 for z in ztrial['fixed_rational_coefficients'])).h,n.SCALE)
        old=nf30
    else:old=ch
    lu=[sum((z*Q(i,j) for i,z in zip(ids,u)),I(0)) for j in ids]
    low=[lv,lw,lu]
    masses=[F(1001,1000),F(n.sqrt_r(sum(z*z for z in wc)).h,n.SCALE),F(n.sqrt_r(sum(z*z for z in u)).h,n.SCALE)]
    archive_raw=gzip.decompress(base64.b64decode(Path('notes/data/RPB108_NF24_NATIVE_RESIDUAL_PROJECTIONS_117_118_20261009.json.gz.b64').read_bytes()))
    assert hashlib.sha256(archive_raw).hexdigest()=='4c8b0067088486e20f31a7904d3bf56a9f654e982b15450efa85cd6b25e24346'
    native_projection=json.loads(archive_raw)['complete_original_signed_source'];j=118 if parity=='even' else 117
    oracle=sum((z*I(*map(F,native_projection[f'{i},{j}']['full'])) for i,z in zip(ids,u)),I(0))
    measured=m.pair(columns[2],n.basis(j));paid=measured+I(-m.eta*masses[2],m.eta*masses[2])
    assert paid.l<=oracle.h and paid.h>=oracle.l
    radii=[8*max(F(v.h-v.l,2*n.SCALE) for v in row) for row in low]
    eta=[masses[i]*m.eta+radii[i]+error[i] for i in range(3)]
    residual=[]
    for s,row in zip(columns,low):
        p,b,l,cells=s;residual.append((p,n.add(b,n.scale(n.physical(ids,[z.mid() for z in row]),-1)),l,cells))
    energy=[[I(0) for j in range(3)] for i in range(3)]
    for i in range(2):
        for j in range(2):energy[i][j]=I(*map(F,old['original_finite_energy_Gram'][i][j]))
        energy[i][2]=energy[2][i]=dot(u,low[i])+I(-error[i]*masses[2],error[i]*masses[2])
    energy[2][2]=dot(u,lu);assert energy[2][2].l>0
    gram=[[I(0) for j in range(3)] for i in range(3)]
    # Retain previous paid source block, integrate only three missing entries.
    for i in range(2):
        for j in range(2):gram[i][j]=I(*map(F,old['original_complete_residual_Gram'][i][j]))
    reconstructed={};payments={}
    probe=m.gram(residual[2],residual[2]);assert probe.l>0
    probe_norm=F(n.sqrt_r(F(probe.h,n.SCALE)).h,n.SCALE)
    for i in range(3):
        value=probe if i==2 else m.gram(residual[i],residual[2])
        # Prior norms are true norm upper bounds. Reconstructed norms are
        # bounded by true norm plus the paid reconstruction error.
        norm=probe_norm if i==2 else F(n.sqrt_r(F(gram[i][i].h,n.SCALE)).h,n.SCALE)+eta[i]
        payment=eta[i]*probe_norm+eta[2]*norm+eta[i]*eta[2]
        paid=value+I(-payment,payment);gram[i][2]=gram[2][i]=paid
        reconstructed[f'{i},2']=value.ends();payments[f'{i},2']=str(payment)
        print(parity,'certified source Gram entry',i,2,flush=True)
    score=[[energy[i][j]-gram[i][j]/F(207,1000) for j in range(3)] for i in range(3)]
    status='SUFFICIENT_FRAME_REJECTED' if score[2][2].h<0 else 'PROBE_DIAGONAL_PASSES' if score[2][2].l>0 else 'UNRESOLVED'
    ratio=gram[2][2]/energy[2][2]
    print(parity,status,'probe source square / native energy',float(F(ratio.l,n.SCALE)),float(F(ratio.h,n.SCALE)),flush=True)
    return dict(milestone='NF32',parity=parity,aperture='53/50',interval_grid_digits=500,regular_kernel_N=320,pole_degree=40,original_translation_cells=13,
        fixed_probe_mass=tr['exact_physical_probe_mass'],original_native_energy_Gram=[[z.ends() for z in row] for row in energy],
        independent_native_projection_check=dict(test_degree=j,reconstructed_pairing=measured.ends(),original_native_pairing=oracle.ends(),paid_overlap=True),
        original_complete_source_Gram=[[z.ends() for z in row] for row in gram],new_reconstructed_source_entries=reconstructed,new_entrywise_error_payments=payments,
        physical_residual_error_bounds=list(map(str,eta)),sufficient_matrix=[[z.ends() for z in row] for row in score],
        remaining_probe_source_square_over_native_energy=ratio.ends(),sufficient_frame_status=status,
        complete_source_of_probe_certified=True,signed_source_crosses_with_successful_pair_certified=True,
        all_remaining_source_Gram_entries_certified=False,unchanged_frame_floor_test_rejected=score[2][2].h<0,
        actual_negative_vector_claimed=False,previous_four_direction_high_certificate_preserved=True,whole_aperture_positive=False,RH=False,F4=False,Lean=False)

if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('mode',choices=['choose','certify']);a.add_argument('--trial');a.add_argument('--parity',choices=['even','odd']);a.add_argument('--output',required=True);a=a.parse_args()
    data,source,hashes=prev.inputs()
    if a.mode=='choose':out=choose(data,source)
    else:
        raw=Path(a.trial).read_bytes();out=run(data,source,json.loads(raw),a.parity);out['fixed_trial_sha256']=hashlib.sha256(raw).hexdigest();out['authenticated_input_sha256']=prev.SHA;out['native_archive_sha256']=hashes
    Path(a.output).write_text(json.dumps(out,indent=2)+'\n')
