#!/usr/bin/env python3
"""NF38: an independent second high direction and its complete response."""
import argparse,hashlib,json
from pathlib import Path
from fractions import Fraction as F
import certify_native_free_correction_functional_nf37_106 as prev
c=prev.c; p=c.p; n=c.n; I=c.I; iv=c.iv; dot=c.dot; mv=p.mv; K=prev.K
SHA37=['ed0827518c5a76c3fc0c56e795518b9e2be9f1edb9860ff78dd1577551cc757d',
       '30c4e46afc86c022d8b867b2cbfaa698b4d5a9441fc7d79200045a0325d3d3af',
       '45de7cb79e330d3e3bc534c2bd179de118924063de7a5987f405cf7b44a0dd78']
def parents():
    names=['EVEN_FREE_CORRECTION_FUNCTIONAL_CERTIFICATE','ODD_FREE_CORRECTION_FUNCTIONAL_CERTIFICATE','FREE_CORRECTION_FUNCTIONAL_VALIDATION']
    raw=[Path('notes/data/RPB108_NF37_'+s+'_20261009.json').read_bytes() for s in names]
    assert [hashlib.sha256(x).hexdigest() for x in raw]==SHA37
    out=list(map(json.loads,raw));assert out[-1]['status']=='PASS'
    prior,old=prev.parents()
    for v in out[:2]:assert v['NF36_input_sha256']==prev.SHA36 and v['NF35_input_sha256']==c.SHA35
    return out,prior,old
def objects(data,source,parity):
    idx=['even','odd'].index(parity);cert37,prior,old=parents();s=cert37[idx];r=prior[idx+2]
    o=c.parent.objects(data,source,parity);zi=prior[idx]['correction_indices'];z0=list(map(F,prior[idx]['fixed_rational_correction_coefficients']))
    lam=list(map(F,s['selected_rational_functional']));base=o['columns']
    columns=[c.merge([col,(zi,z0)],[F(1),-v]) for col,v in zip(base,lam)]
    coordinate=dict(zip(r['correction_source_coordinate_indices'],map(iv,r['reconstructed_correction_source_coordinates'])))
    low=[[a-v*coordinate[j] for a,j in zip(row,o['ids'])] for row,v in zip(o['low'],lam)]
    retained_errors=[a+abs(v)*F(r['correction_source_error_upper']) for a,v in zip(o['retained_errors'],lam)]
    masses=[p.norm(v) for _,v in columns]
    eta=[o['unit']*mass+error+8*max(F(v.h-v.l,2*n.SCALE) for v in row) for mass,error,row in zip(masses,retained_errors,low)]
    o.update(columns=columns,low=low,retained_errors=retained_errors,source_norm_mass_upper=masses,physical_source_errors=eta,
        old_correction_indices=zi,old_correction=z0,old_functional=lam,parent37=s)
    return o
def choose(data,source,parity):
    idx=['even','odd'].index(parity);o=objects(data,source,parity);prior=o['parent37'];h=list(map(F,prior['universal_fixed_rational_witness']))
    ids,vs=c.merge(o['columns'],h);m=p.old.probe.Moments(720,parity);s=m.source(ids,vs)
    shell=o['old_correction_indices'];z0=o['old_correction'];functional=p.functional(m,s,max(shell));coords=[dot(n.basis(i),functional) for i in shell]
    eta=m.eta*p.norm(vs);paid=[v+I(-eta,eta) for v in coords]
    raw=[F((v.mid()/4*10**100).__floor__(),10**100) for v in coords]
    mass0=sum(v*v for v in z0);orth=sum(a*b for a,b in zip(z0,raw))/mass0;z1=[a-orth*b for a,b in zip(raw,z0)]
    mass1=sum(v*v for v in z1);assert mass1>0 and sum(a*b for a,b in zip(z0,z1))==0
    projection=dot(z0,paid)/mass0;orthpaid=[v-a*projection for v,a in zip(paid,z0)];capture=sum((n.sq(v) for v in orthpaid),I(0))
    gamma=dot(h,mv(prev.matrix(prior['original_selected_complete_source_Gram']),h));assert gamma.l>0
    checks=[]
    for pos in [0,len(shell)-1]:
        direct=m.pair(s,n.basis(shell[pos]));assert max(direct.l,coords[pos].l)<=min(direct.h,coords[pos].h)
        checks.append(dict(degree=shell[pos],direct=direct.ends(),functional=coords[pos].ends()))
    print(parity,'independent shell fraction',*[float(F(v)) for v in (capture/gamma).ends()],flush=True)
    return dict(milestone='NF38',parity=parity,NF37_input_sha256=SHA37,NF36_input_sha256=prev.SHA36,authenticated_input_sha256=p.old.prev.SHA,
        exact_moved_target_coefficients=list(map(str,h)),merged_target_indices=ids,merged_target_coefficients=list(map(str,vs)),
        frozen_old_functional=list(map(str,o['old_functional'])),correction_indices=shell,old_correction_coefficients=list(map(str,z0)),
        reconstructed_selection_coordinates=[v.ends() for v in coords],selection_source_error_upper=str(eta),paid_selection_coordinates=[v.ends() for v in paid],
        raw_rational_correction_coefficients=list(map(str,raw)),exact_old_direction_projection_coefficient=str(orth),
        fixed_rational_second_correction_coefficients=list(map(str,z1)),exact_second_correction_mass_squared=str(mass1),exact_old_second_inner_product='0',
        orthogonal_paid_selection_coordinates=[v.ends() for v in orthpaid],orthogonal_shell_square=capture.ends(),moved_target_original_projected_source_square=gamma.ends(),
        orthogonal_shell_fraction=(capture/gamma).ends(),independent_functional_checks=checks,
        selection_rule='NF37 moved witness in frozen selected family; source shell /4, down-round10^100; exact physical projection off NF36 z0',selection_is_not_a_sign_certificate=True)
def analyze(q,g,beta,qz,zeta,gz,masses):
    U=[[q[i][j]-g[i][j]/K for j in range(3)] for i in range(3)];e=[a-b/K for a,b in zip(beta,zeta)];d=qz-gz/K;assert d.h<0
    V=[[U[i][j]-(n.sq(e[i]) if i==j else e[i]*e[j])/d for j in range(3)] for i in range(3)]
    d2=V[0][0]*V[1][1]-n.sq(V[0][1]);assert V[0][0].l>0 and d2.l>0
    reaction=(V[1][1]*n.sq(V[0][2])-2*V[0][1]*V[0][2]*V[1][2]+V[0][0]*n.sq(V[1][2]))/d2
    margin=V[2][2]-reaction;det=c.parent.det3(V)
    extra={};reject=False
    if margin.h<0 and det.h<0:
        h=prev.witness(V);value=dot(h,mv(V,h));a=dot(h,mv(U,h));b=dot(h,e)
        upper=F(a.h,n.SCALE)+b.absupper()**2/(-F(d.h,n.SCALE));reject=upper<0
        extra=dict(universal_fixed_rational_witness=list(map(str,h)),universal_witness_ceiling_value=value.ends(),universal_witness_scalar_coefficients=dict(a=a.ends(),b=b.ends(),d=d.ends()),universal_witness_upper=str(upper))
    lam=[F(((v/d).mid()*10**100).__floor__(),10**100) for v in e];Q,G=prev.update(q,g,beta,qz,zeta,gz,lam)
    packet=c.test(Q,G,masses,F(0));packet.pop('tau',None)
    return dict(correction_floor_crosses=[v.ends() for v in e],correction_floor_diagonal=d.ends(),second_functional_ceiling=prev.ends(V),
        ceiling_leading_pair_determinant=d2.ends(),ceiling_condensed_margin=margin.ends(),ceiling_determinant=det.ends(),
        all_real_second_functionals_floor_rejected_with_old_functional_frozen=reject,selected_rational_second_functional=list(map(str,lam)),
        original_selected_native_energy_Gram=prev.ends(Q),original_selected_complete_source_Gram=prev.ends(G),selected_sign_packet=packet,**extra)
def joint_update(q,g,B,QZ,S,GZ,C):
    Q=[[q[i][j]-sum((B[i][a]*C[a][j]+C[a][i]*B[j][a] for a in range(2)),I(0))
        +sum((C[a][i]*QZ[a][b]*C[b][j] for a in range(2) for b in range(2)),I(0)) for j in range(3)] for i in range(3)]
    G=[[g[i][j]-sum((S[i][a]*C[a][j]+C[a][i]*S[j][a] for a in range(2)),I(0))
        +sum((C[a][i]*GZ[a][b]*C[b][j] for a in range(2) for b in range(2)),I(0)) for j in range(3)] for i in range(3)]
    return Q,G
def joint_analyze(q,g,beta,qz,zeta,gz,q01,g01,prior,oldlam,masses):
    q0=iv(prior['original_correction_native_energy']);g0=iv(prior['original_correction_projected_source_square'])
    b0=list(map(iv,prior['original_native_correction_crosses']));s0=list(map(iv,prior['original_correction_source_crosses']))
    B=[[a-v*q0,b] for a,v,b in zip(b0,oldlam,beta)]
    S=[[a-v*g0,b] for a,v,b in zip(s0,oldlam,zeta)]
    QZ=[[q0,q01],[q01,qz]];GZ=[[g0,g01],[g01,gz]]
    H=[[QZ[i][j]-GZ[i][j]/K for j in range(2)] for i in range(2)]
    hd=H[0][0]*H[1][1]-n.sq(H[0][1]);assert H[0][0].h<0 and hd.l>0
    inv=[[H[1][1]/hd,-H[0][1]/hd],[-H[0][1]/hd,H[0][0]/hd]]
    E=[[B[i][j]-S[i][j]/K for j in range(2)] for i in range(3)]
    U=[[q[i][j]-g[i][j]/K for j in range(3)] for i in range(3)]
    V=[[U[i][j]-dot(E[i],mv(inv,E[j])) for j in range(3)] for i in range(3)]
    d2=V[0][0]*V[1][1]-n.sq(V[0][1]);assert V[0][0].l>0 and d2.l>0
    reaction=(V[1][1]*n.sq(V[0][2])-2*V[0][1]*V[0][2]*V[1][2]+V[0][0]*n.sq(V[1][2]))/d2
    margin=V[2][2]-reaction;det=c.parent.det3(V);extra={};reject=False
    if margin.h<0 and det.h<0:
        h=prev.witness(V);a=dot(h,mv(U,h));b=[dot(h,[E[i][j] for i in range(3)]) for j in range(2)]
        upper=a-dot(b,mv(inv,b));reject=upper.h<0
        extra=dict(joint_universal_fixed_rational_witness=list(map(str,h)),joint_universal_witness_ceiling_value=dot(h,mv(V,h)).ends(),
            joint_universal_witness_constant=a.ends(),joint_universal_witness_cross_vector=[v.ends() for v in b],joint_universal_witness_upper=upper.ends())
    C=[[F((dot(inv[a],E[j]).mid()*10**100).__floor__(),10**100) for j in range(3)] for a in range(2)]
    Q,G=joint_update(q,g,B,QZ,S,GZ,C);packet=c.test(Q,G,masses,F(0));packet.pop('tau',None)
    return dict(joint_native_high_block=prev.ends(QZ),joint_complete_source_high_block=prev.ends(GZ),
        joint_native_joined_high_crosses=prev.ends(B),joint_complete_source_joined_high_crosses=prev.ends(S),
        joint_correction_floor_block=prev.ends(H),joint_correction_floor_block_determinant=hd.ends(),joint_correction_floor_inverse=prev.ends(inv),
        joint_floor_joined_high_crosses=prev.ends(E),joint_functional_ceiling=prev.ends(V),joint_ceiling_leading_pair_determinant=d2.ends(),
        joint_ceiling_condensed_margin=margin.ends(),joint_ceiling_determinant=det.ends(),
        all_real_joint_two_direction_functionals_floor_rejected=reject,selected_rational_joint_functionals=[list(map(str,row)) for row in C],
        original_selected_native_energy_Gram=prev.ends(Q),original_selected_complete_source_Gram=prev.ends(G),selected_sign_packet=packet,**extra)
def run(data,source,trial):
    parity=trial['parity'];o=objects(data,source,parity);prior=o['parent37'];h=list(map(F,prior['universal_fixed_rational_witness']))
    assert trial['NF37_input_sha256']==SHA37 and trial['NF36_input_sha256']==prev.SHA36 and trial['authenticated_input_sha256']==p.old.prev.SHA
    assert trial['exact_moved_target_coefficients']==list(map(str,h))
    assert c.merge(o['columns'],h)==(trial['merged_target_indices'],list(map(F,trial['merged_target_coefficients'])))
    zi=trial['correction_indices'];z=list(map(F,trial['fixed_rational_second_correction_coefficients']));z0=o['old_correction']
    assert zi==o['old_correction_indices'] and sum(a*b for a,b in zip(z,z0))==0 and sum(v*v for v in z)>0
    m=p.old.probe.Moments(1020,parity);sources=[m.source(ii,cc) for ii,cc in o['columns']];sz=m.source(zi,z)
    print(parity,'constructed frozen joined sources and independent second source',flush=True)
    idx=['even','odd'].index(parity);func=p.functional(m,sz,180);corr={i:dot(n.basis(i),func) for i in range(idx,181 if idx==0 else 180,2)}
    zm=p.norm(z);ez=m.eta*zm;zzhat=m.pair(sz,sz[0]);qz=zzhat+I(-ez*zm,ez*zm)
    beta=[];betahat=[];reverse=[]
    for i,(ii,cc) in enumerate(o['columns']):
        bh=dot(cc,[corr[j] for j in ii]);payment=ez*o['source_norm_mass_upper'][i];beta.append(bh+I(-payment,payment));betahat.append(bh)
        rev=m.pair(sources[i],sz[0])+I(-payment,payment);assert max(rev.l,beta[-1].l)<=min(rev.h,beta[-1].h);reverse.append(rev)
    lowz=[corr[i] for i in o['ids']];etz=ez+8*max(F(v.h-v.l,2*n.SCALE) for v in lowz)
    rz=(sz[0],n.add(sz[1],n.scale(n.physical(o['ids'],[v.mid() for v in lowz]),-1)),sz[2],sz[3])
    residual=[(s[0],n.add(s[1],n.scale(n.physical(o['ids'],[v.mid() for v in row]),-1)),s[2],s[3]) for s,row in zip(sources,o['low'])]
    q=prev.matrix(prior['original_selected_native_energy_Gram']);g=prev.matrix(prior['original_selected_complete_source_Gram'])
    square=m.gram(rz,rz);assert square.l>0;Nz=F(n.sqrt_r(F(square.h,n.SCALE)).h,n.SCALE);zpay=2*etz*Nz+etz*etz;gz=square+I(-zpay,zpay)
    zeta=[];crosshat=[];crosspayments=[];eta=o['physical_source_errors']
    for i in range(3):
        value=m.gram(residual[i],rz);Ni=F(n.sqrt_r(F(g[i][i].h,n.SCALE)).h,n.SCALE)+eta[i]
        payment=eta[i]*Nz+etz*Ni+eta[i]*etz;zeta.append(value+I(-payment,payment));crosshat.append(value);crosspayments.append(payment)
        print(parity,'certified second-direction covariance',i,flush=True)
    par36=prev.parents()[0][idx+2]
    z0norm=p.norm(z0);q01hat=dot(z0,[corr[i] for i in zi]);q01pay=ez*z0norm;q01=q01hat+I(-q01pay,q01pay)
    s0=m.source(zi,z0);low0=list(map(iv,par36['reconstructed_correction_source_coordinates'][:56]))
    r0=(s0[0],n.add(s0[1],n.scale(n.physical(o['ids'],[v.mid() for v in low0]),-1)),s0[2],s0[3])
    reverse01=m.pair(s0,sz[0])+I(-q01pay,q01pay);assert max(reverse01.l,q01.l)<=min(reverse01.h,q01.h)
    eta0=F(par36['correction_residual_error_upper']);N0=F(n.sqrt_r(F(iv(par36['original_correction_projected_source_square']).h,n.SCALE)).h,n.SCALE)+eta0
    cross01=m.gram(r0,rz);pay01=eta0*Nz+etz*N0+eta0*etz;g01=cross01+I(-pay01,pay01)
    print(parity,'certified old-second source covariance',flush=True)
    frozen=analyze(q,g,beta,qz,zeta,gz,o['retained_masses'])
    result=joint_analyze(q,g,beta,qz,zeta,gz,q01,g01,par36,o['old_functional'],o['retained_masses'])
    print(parity,result['selected_sign_packet']['joined_status'],flush=True)
    return dict(milestone='NF38',parity=parity,aperture='53/50',interval_grid_digits=500,regular_kernel_N=320,pole_degree=40,original_translation_cells=13,
        NF37_input_sha256=SHA37,NF36_input_sha256=prev.SHA36,authenticated_input_sha256=p.old.prev.SHA,
        source_norm_mass_upper=list(map(str,o['source_norm_mass_upper'])),frozen_family_retained_projection_errors=list(map(str,o['retained_errors'])),frozen_family_source_errors=list(map(str,eta)),
        correction_norm_upper=str(zm),correction_source_error_upper=str(ez),correction_residual_error_upper=str(etz),
        correction_source_coordinate_indices=list(corr),reconstructed_correction_source_coordinates=[v.ends() for v in corr.values()],
        reconstructed_native_correction_crosses=[v.ends() for v in betahat],original_native_correction_crosses=[v.ends() for v in beta],reverse_native_correction_crosses=[v.ends() for v in reverse],
        reconstructed_correction_native_energy=zzhat.ends(),original_correction_native_energy=qz.ends(),
        reconstructed_correction_projected_source_square=square.ends(),correction_source_square_payment=str(zpay),original_correction_projected_source_square=gz.ends(),
        reconstructed_correction_source_crosses=[v.ends() for v in crosshat],correction_source_cross_payments=list(map(str,crosspayments)),original_correction_source_crosses=[v.ends() for v in zeta],
        reconstructed_old_second_native_cross=q01hat.ends(),old_second_native_cross_payment=str(q01pay),original_old_second_native_cross=q01.ends(),reverse_old_second_native_cross=reverse01.ends(),
        reconstructed_old_second_source_cross=cross01.ends(),old_second_source_cross_payment=str(pay01),original_old_second_source_cross=g01.ends(),
        frozen_old_functional_analysis=frozen,
        inherited_retained_masses=list(map(str,o['retained_masses'])),entire_modified_remaining_54_frame_certified=False,
        both_high_functionals_varied_jointly=True,actual_negative_original_form_claimed=False,whole_aperture_positive=False,RH=False,F4=False,Lean=False,**result)
if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('mode',choices=['choose','certify']);a.add_argument('--parity',choices=['even','odd']);a.add_argument('--trial');a.add_argument('--output',required=True);a=a.parse_args()
    data,source,hashes=p.old.prev.inputs()
    if a.mode=='choose':out=choose(data,source,a.parity)
    else:
        raw=Path(a.trial).read_bytes();out=run(data,source,json.loads(raw));out['fixed_trial_sha256']=hashlib.sha256(raw).hexdigest();out['native_archive_sha256']=hashes
    Path(a.output).write_text(json.dumps(out,indent=2)+'\n')
