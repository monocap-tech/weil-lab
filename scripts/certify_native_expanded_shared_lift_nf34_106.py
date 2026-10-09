#!/usr/bin/env python3
"""NF34: shared rank-one expanded-shell lift, finite frame and source test."""
import json,hashlib,argparse,gzip,base64
from pathlib import Path
from fractions import Fraction as F
import certify_native_shared_remaining_lift_nf33_106 as old
n=old.n;I=n.I;dot=old.dot;mv=old.mv
PATH33='notes/data/RPB108_NF33_'
SHA33=['89683af32013c4bfc3ed3bd66d90ff889131a4ccdd03dd769523a7dfbbcd9cff','9bdf992dda4aca110f2c776183ce9e6f614623fdc373389485cf25e06711a9dd','ce8c97c61db0ade92d2b10d2bed56775eb07d0bb66ae956654c94716a4febac5']
def parents():
    paths=[PATH33+'FIXED_SHARED_REMAINING_LIFT_20261009.json',PATH33+'EVEN_LIFTED_PROBE_CERTIFICATE_20261009.json',PATH33+'ODD_LIFTED_PROBE_CERTIFICATE_20261009.json']
    raw=[Path(p).read_bytes() for p in paths];assert [hashlib.sha256(r).hexdigest() for r in raw]==SHA33
    return list(map(json.loads,raw))
def norm(v):return F(n.sqrt_r(sum(z*z for z in v)).h,n.SCALE)
def iv(v):return I(*map(F,v))

def functional(m,s,degree):
    # Exact monomial source moments reuse one functional for many Legendre
    # tests. All operations are outward; no sampled transform is used.
    p,b,l,cells=s;out=[]
    for k in range(degree+1):
        value=dot(b,m.M[k:k+len(b)])+dot(l,m.ML[k:k+len(l)])
        for cell,(mp,ml) in zip(cells,m.cm):value+=dot(cell,mp[k:k+len(cell)])
        out.append(value)
    return out

def choose(data,source,parity):
    idx=['even','odd'].index(parity);par=parents();tr=par[0]['parities'][idx];cert=par[idx+1]
    ids,hi,T,B,C,K=old.frame(data,source,idx);a=list(map(F,tr['inherited_constraint_coordinates']))
    u=list(map(F,tr['fixed_probe_coefficients'][:56]));mass=sum(z*z for z in u)
    ell=[sum(v*z for v,z in zip(u,col))/mass for col in zip(*T)]
    assert sum(v*z for v,z in zip(ell,a))==1
    # One exact physical functional acts on all 54 columns; the direction
    # targeted here is inherited rather than reselected after lifting.
    zi=list(range(116+idx,181 if idx==0 else 180,2))
    coeff=list(map(F,tr['fixed_probe_coefficients']));m=old.probe.Moments(720,parity)
    s=m.source(ids+hi,coeff);f=functional(m,s,max(zi))
    coords=[dot(n.basis(i),f) for i in zi]
    eta=m.eta*norm(coeff);paid=[z+I(-eta,eta) for z in coords]
    captured=sum((n.sq(z) for z in paid),I(0));gamma=iv(cert['original_complete_remaining_source_square'])
    z=[F((v.mid()/4*10**100).__floor__(),10**100) for v in coords]
    # Independent multiplication order checks the reusable functional.
    checks=[]
    for pos in [0,len(zi)-1]:
        direct=m.pair(s,n.basis(zi[pos]));assert max(direct.l,coords[pos].l)<=min(direct.h,coords[pos].h)
        checks.append(dict(degree=zi[pos],direct=direct.ends(),functional=coords[pos].ends(),overlap=True))
    print(parity,'expanded shell fraction',float(F((captured/gamma).l,n.SCALE)),float(F((captured/gamma).h,n.SCALE)),flush=True)
    return dict(milestone='NF34',parity=parity,authenticated_input_sha256=old.prev.SHA,NF33_input_sha256=SHA33,
        retained_indices=ids,old_high_indices=hi,additional_high_indices=zi,
        exact_shared_constraint_functional=list(map(str,ell)),fixed_rational_additional_coefficients=list(map(str,z)),
        exact_functional_on_inherited_probe='1',reconstructed_selection_coordinates=[v.ends() for v in coords],
        selection_source_error_upper=str(eta),paid_original_selection_coordinates=[v.ends() for v in paid],
        selected_shell_square=captured.ends(),selected_shell_fraction_of_NF33_source_square=(captured/gamma).ends(),
        selection_functional_checks=checks,
        selection_rule='shared U34=U33-z ell; z is NF33 inherited lifted-probe source on high116..180 even /117..179 odd divided by4 and rounded down denominator10^100; ell(a)=<u32,T a>/||u32||^2',
        complete_collective_source_sign_not_inferred_from_selection=True)

def run(data,source,trial):
    parity=trial['parity'];idx=['even','odd'].index(parity);par=parents();tr=par[0]['parities'][idx];oldcert=par[idx+1]
    assert trial['authenticated_input_sha256']==old.prev.SHA and trial['NF33_input_sha256']==SHA33
    ids,hi,T,B,C,K=old.frame(data,source,idx);Z=[list(map(F,row)) for row in tr['frozen_shared_lift_map']]
    ell=list(map(F,trial['exact_shared_constraint_functional']));a=list(map(F,tr['inherited_constraint_coordinates']))
    zi=trial['additional_high_indices'];z=list(map(F,trial['fixed_rational_additional_coefficients']))
    assert zi==list(range(116+idx,181 if idx==0 else 180,2))
    oldcoeff=list(map(F,tr['fixed_probe_coefficients']));u=oldcoeff[:56];mass=sum(v*v for v in u)
    assert ell==[sum(v*t for v,t in zip(u,col))/mass for col in zip(*T)] and sum(v*t for v,t in zip(ell,a))==1
    m=old.probe.Moments(1020,parity);s=m.source(ids+hi,oldcoeff);sz=m.source(zi,z);zm=norm(z);om=norm(oldcoeff)
    print(parity,'constructed old and correction complete sources',flush=True)
    f=functional(m,sz,max(ids+hi));corr=[dot(n.basis(i),f) for i in ids+hi];error_z=m.eta*zm
    qzzhat=m.pair(sz,sz[0]);qzz=qzzhat+I(-error_z*zm,error_z*zm)
    beta_hat=dot(oldcoeff,corr);beta=beta_hat+I(-error_z*om,error_z*om)
    reverse=m.pair(s,sz[0])+I(-m.eta*om*zm,m.eta*om*zm)
    assert max(beta.l,reverse.l)<=min(beta.h,reverse.h)
    q0=iv(oldcert['original_native_energy']);q=q0-2*beta+qzz;assert q.l>0
    # Original finite shared graph energy, with every correction coupling
    # paid using the small correction source norm, not a unit source error.
    CZ=[[dot(row,col) for col in zip(*Z)] for row in C]
    L0=[[B[i][j]-dot([row[i] for row in K],[row[j] for row in Z])-dot([row[i] for row in Z],[row[j] for row in K])+dot([row[i] for row in Z],[row[j] for row in CZ]) for j in range(54)] for i in range(54)]
    bhat=[dot(col,corr[:56])-dot([row[j] for row in Z],corr[56:]) for j,col in enumerate(zip(*T))]
    masses=[norm(list(col)+[-row[j] for row in Z]) for j,col in enumerate(zip(*T))]
    b=[v+I(-error_z*mass,error_z*mass) for v,mass in zip(bhat,masses)]
    L=[[L0[i][j]-b[i]*ell[j]-ell[i]*b[j]+qzz*ell[i]*ell[j] for j in range(54)] for i in range(54)]
    inverse,proof=old.prev.matrix.inverse(L)
    zsquare=sum(v*v for v in z)
    G=[[sum(col[i]*col[j] for col in T)+sum(row[i]*row[j] for row in Z)+zsquare*ell[i]*ell[j] for j in range(54)] for i in range(54)]
    trace=sum((dot(inverse[i],[row[i] for row in G]) for i in range(54)),I(0));assert trace.l>0
    frameq=dot(a,mv(L,a));assert max(frameq.l,q.l)<=min(frameq.h,q.h)
    print(parity,'expanded full finite frame PASS; physical gap',float(1/F(trace.h,n.SCALE)),flush=True)
    low0=[sum((v*old.native(source,i,j) for i,v in zip(ids+hi,oldcoeff)),I(0)) for j in ids]
    oldround=8*max(F(v.h-v.l,2*n.SCALE) for v in low0)
    zround=8*max(F(v.h-v.l,2*n.SCALE) for v in corr[:56])
    r0=(s[0],n.add(s[1],n.scale(n.physical(ids,[v.mid() for v in low0]),-1)),s[2],s[3])
    rz=(sz[0],n.add(sz[1],n.scale(n.physical(ids,[v.mid() for v in corr[:56]]),-1)),sz[2],sz[3])
    residual=old.probe.engine.subtract(r0,rz)
    # PF contraction pays the correction source error once; its retained
    # coordinates are taken from the same complete approximating source.
    eta=m.eta*om+error_z+oldround+zround
    square=m.gram(residual,residual);assert square.l>0
    root=F(n.sqrt_r(F(square.h,n.SCALE)).h,n.SCALE);payment=2*eta*root+eta*eta
    gamma=square+I(-payment,payment);score=q-gamma/F(207,1000);ratio=gamma/q
    # Check inherited unsquared source against the independent native archive.
    raw=gzip.decompress(base64.b64decode(Path('notes/data/RPB108_NF24_NATIVE_RESIDUAL_PROJECTIONS_117_118_20261009.json.gz.b64').read_bytes()))
    assert hashlib.sha256(raw).hexdigest()=='4c8b0067088486e20f31a7904d3bf56a9f654e982b15450efa85cd6b25e24346'
    archive=json.loads(raw)['complete_original_signed_source'];j=118 if idx==0 else 117
    oracle=sum((v*iv(archive[f'{i},{j}']['full']) for i,v in zip(ids+hi,oldcoeff)),I(0))
    measured=m.pair(s,n.basis(j));paid=measured+I(-m.eta*om,m.eta*om);assert max(paid.l,oracle.l)<=min(paid.h,oracle.h)
    # Reusable correction functional is also checked by direct pairing order.
    fc=[]
    for pos in [0,len(ids+hi)-1]:
        direct=m.pair(sz,n.basis((ids+hi)[pos]));assert max(direct.l,corr[pos].l)<=min(direct.h,corr[pos].h)
        fc.append(dict(degree=(ids+hi)[pos],direct=direct.ends(),functional=corr[pos].ends(),overlap=True))
    status='LIFTED_WITNESS_WITH_ALL_F_PASSES' if score.l>0 else 'EXPANDED_SHARED_FLOOR_REJECTED' if score.h<0 else 'UNRESOLVED'
    print(parity,status,'ratio',float(F(ratio.l,n.SCALE)),float(F(ratio.h,n.SCALE)),flush=True)
    return dict(milestone='NF34',parity=parity,aperture='53/50',interval_grid_digits=500,regular_kernel_N=320,pole_degree=40,original_translation_cells=13,
        authenticated_input_sha256=old.prev.SHA,NF33_input_sha256=SHA33,additional_correction_norm_upper=str(zm),
        original_correction_energy=qzz.ends(),reconstructed_correction_energy=qzzhat.ends(),
        original_witness_correction_cross=beta.ends(),reverse_witness_correction_cross=reverse.ends(),
        reconstructed_correction_source_coordinates=[v.ends() for v in corr],correction_source_error_upper=str(error_z),
        expanded_shared_frame_inverse_verification=proof,physical_expanded_shared_frame_gap_lower=str(1/F(trace.h,n.SCALE)),
        expanded_shared_inverse_physical_trace_upper=str(F(trace.h,n.SCALE)),expanded_shared_finite_frame_positive=True,
        original_lifted_witness_energy=q.ends(),expanded_frame_witness_energy=frameq.ends(),
        exact_lifted_witness_mass=str(sum(v*v for v in oldcoeff)+zsquare),
        reconstructed_projected_source_square=square.ends(),physical_residual_error_upper=str(eta),
        source_square_error_payment=str(payment),original_complete_projected_source_square=gamma.ends(),
        source_square_over_native_energy=ratio.ends(),floor_score=score.ends(),status=status,
        inherited_independent_native_projection_check=dict(degree=j,original=oracle.ends(),reconstructed=measured.ends(),paid_overlap=True),
        correction_functional_checks=fc,complete_remaining_source_Gram_certified=False,
        signed_mixed_source_covariance_with_successful_pair_certified=False,
        simultaneous_six_retained_direction_certificate_claimed=False,whole_aperture_positive=False,RH=False,F4=False,Lean=False)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('mode',choices=['choose','certify']);p.add_argument('--parity',choices=['even','odd']);p.add_argument('--trial');p.add_argument('--output',required=True);a=p.parse_args()
    data,source,hashes=old.prev.inputs()
    if a.mode=='choose':out=choose(data,source,a.parity)
    else:
        raw=Path(a.trial).read_bytes();out=run(data,source,json.loads(raw));out['fixed_trial_sha256']=hashlib.sha256(raw).hexdigest();out['native_archive_sha256']=hashes
    Path(a.output).write_text(json.dumps(out,indent=2)+'\n')
