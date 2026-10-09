#!/usr/bin/env python3
"""NF36: mixed-source correction and full paid three-direction matrix tests."""
import argparse,json,hashlib
from pathlib import Path
from fractions import Fraction as F
import certify_native_joined_witnesses_nf35_106 as parent
n=parent.n;I=n.I;iv=parent.iv;dot=parent.dot;p=parent.prev
SHA35=['68e9c2bb0c9109f6b781781f544b9da1271554819e199041360620ddbf3053c3','eaeb8dff861eab54e3b0cc15457a209c62d4bf8dcbe884b74fef8ea9757e0879','ab9e4ebd605063b6c3a929b96be9f0fc20c380c658f51d6055475e4b3ed1e3c9']
TAUS=[F(1),F(3,4),F(5,4),F(1,2),F(3,2),F(1,4),F(2)]
def parents():
    names=['EVEN_JOINED_WITNESSES_CERTIFICATE','ODD_JOINED_WITNESSES_CERTIFICATE','JOINED_WITNESSES_VALIDATION']
    raw=[Path('notes/data/RPB108_NF35_'+v+'_20261009.json').read_bytes() for v in names]
    assert [hashlib.sha256(v).hexdigest() for v in raw]==SHA35
    out=list(map(json.loads,raw));assert out[-1]['status']=='PASS';return out
def merge(columns,coeff):
    terms={}
    for (ids,vs),a in zip(columns,coeff):
        for i,v in zip(ids,vs):terms[i]=terms.get(i,F(0))+a*v
    ids=sorted(terms);return ids,[terms[i] for i in ids]
def choose(data,source,parity):
    idx=['even','odd'].index(parity);old=parents()[idx];o=parent.objects(data,source,parity)
    f=list(map(F,old['fixed_rational_mixed_floor_witness']));assert f[2]==1
    ids,vs=merge(o['columns'],f);m=p.old.probe.Moments(720,parity);s=m.source(ids,vs)
    shell=list(range(112+idx,181 if idx==0 else 180,2));functional=p.functional(m,s,max(shell))
    coords=[dot(n.basis(i),functional) for i in shell];eta=m.eta*p.norm(vs)
    paid=[v+I(-eta,eta) for v in coords];capture=sum((n.sq(v) for v in paid),I(0))
    oldgamma=[[iv(v) for v in row] for row in old['original_joined_complete_source_Gram']]
    gamma=dot(f,p.mv(oldgamma,f));assert gamma.l>0
    z=[F((v.mid()/4*10**100).__floor__(),10**100) for v in coords]
    checks=[]
    for pos in [0,len(shell)-1]:
        direct=m.pair(s,n.basis(shell[pos]));assert max(direct.l,coords[pos].l)<=min(direct.h,coords[pos].h)
        checks.append(dict(degree=shell[pos],direct=direct.ends(),functional=coords[pos].ends()))
    print(parity,'mixed-target shell fraction',*[float(F(v)) for v in (capture/gamma).ends()],flush=True)
    return dict(milestone='NF36',parity=parity,NF35_input_sha256=SHA35,authenticated_input_sha256=p.old.prev.SHA,
        exact_mixed_target_coefficients=list(map(str,f)),merged_target_indices=ids,merged_target_coefficients=list(map(str,vs)),
        correction_indices=shell,fixed_rational_correction_coefficients=list(map(str,z)),frozen_scalar_candidates=list(map(str,TAUS)),
        reconstructed_selection_coordinates=[v.ends() for v in coords],selection_source_error_upper=str(eta),
        paid_selection_coordinates=[v.ends() for v in paid],mixed_target_original_projected_source_square=gamma.ends(),
        selected_shell_square=capture.ends(),selected_shell_fraction=(capture/gamma).ends(),independent_functional_checks=checks,
        selection_rule='NF35 exact mixed witness source on high112..180 even /113..179 odd, divided by4, down-rounded denominator10^100; joined map (v,t,u)->(v,t,u-tau*z)',
        selection_is_not_a_source_sign_certificate=True)
def update(q,g,beta,qz,zeta,gz,tau):
    Q=[row[:] for row in q];G=[row[:] for row in g]
    for i in range(2):Q[i][2]=Q[2][i]=q[i][2]-tau*beta[i];G[i][2]=G[2][i]=g[i][2]-tau*zeta[i]
    Q[2][2]=q[2][2]-2*tau*beta[2]+tau*tau*qz
    G[2][2]=g[2][2]-2*tau*zeta[2]+tau*tau*gz
    return Q,G
def condensed(q,g,beta,qz,zeta,gz):
    U=[[q[i][j]-g[i][j]/F(207,1000) for j in range(3)] for i in range(3)]
    A,B,D=U[0][0],U[0][1],U[1][1];det=A*D-n.sq(B);assert A.l>0 and det.l>0
    inv=[[D/det,-B/det],[-B/det,A/det]];b=[U[0][2],U[1][2]]
    e=[beta[i]-zeta[i]/F(207,1000) for i in range(3)]
    nu=U[2][2]-dot(b,p.mv(inv,b));alpha=e[2]-dot(b,p.mv(inv,e[:2]));delta=qz-gz/F(207,1000)-dot(e[:2],p.mv(inv,e[:2]))
    return nu,alpha,delta
def test(q,g,masses,tau):
    nd=parent.det3(q)
    if not(q[0][0].l>0 and (q[0][0]*q[1][1]-n.sq(q[0][1])).l>0 and nd.l>0):
        return dict(tau=str(tau),joined_status='NATIVE_ENERGY_UNRESOLVED',joined_native_energy_determinant=nd.ends())
    out=parent.sign_packet(q,g,masses);out['tau']=str(tau);return out
def run(data,source,trial):
    parity=trial['parity'];idx=['even','odd'].index(parity);old=parents()[idx];o=parent.objects(data,source,parity)
    assert trial['NF35_input_sha256']==SHA35 and trial['authenticated_input_sha256']==p.old.prev.SHA
    f=list(map(F,trial['exact_mixed_target_coefficients']));assert list(map(str,f))==old['fixed_rational_mixed_floor_witness']
    assert merge(o['columns'],f)==(trial['merged_target_indices'],list(map(F,trial['merged_target_coefficients'])))
    zi=trial['correction_indices'];z=list(map(F,trial['fixed_rational_correction_coefficients']))
    assert zi==list(range(112+idx,181 if idx==0 else 180,2)) and trial['frozen_scalar_candidates']==list(map(str,TAUS))
    m=p.old.probe.Moments(1020,parity);sources=[m.source(ii,cc) for ii,cc in o['columns']];sz=m.source(zi,z)
    print(parity,'constructed three original sources and mixed correction source',flush=True)
    func=p.functional(m,sz,180);corr={i:dot(n.basis(i),func) for i in range(idx,181 if idx==0 else 180,2)}
    zm=p.norm(z);ez=m.eta*zm;zzhat=m.pair(sz,sz[0]);qz=zzhat+I(-ez*zm,ez*zm)
    beta=[];betahat=[];reverse=[]
    for i,(ii,cc) in enumerate(o['columns']):
        bh=dot(cc,[corr[j] for j in ii]);payment=ez*o['source_norm_mass_upper'][i]
        beta.append(bh+I(-payment,payment));betahat.append(bh)
        rev=m.pair(sources[i],sz[0])+I(-payment,payment);assert max(rev.l,beta[-1].l)<=min(rev.h,beta[-1].h);reverse.append(rev)
    lowz=[corr[i] for i in o['ids']];etz=ez+8*max(F(v.h-v.l,2*n.SCALE) for v in lowz)
    rz=(sz[0],n.add(sz[1],n.scale(n.physical(o['ids'],[v.mid() for v in lowz]),-1)),sz[2],sz[3])
    residual=[(s[0],n.add(s[1],n.scale(n.physical(o['ids'],[v.mid() for v in row]),-1)),s[2],s[3]) for s,row in zip(sources,o['low'])]
    q=[[iv(v) for v in row] for row in old['original_joined_native_energy_Gram']];g=[[iv(v) for v in row] for row in old['original_joined_complete_source_Gram']]
    square=m.gram(rz,rz);assert square.l>0;Nz=F(n.sqrt_r(F(square.h,n.SCALE)).h,n.SCALE)
    zpay=2*etz*Nz+etz*etz;gz=square+I(-zpay,zpay)
    zeta=[];crosshat=[];crosspayments=[];eta=o['physical_source_errors']
    for i in range(3):
        value=m.gram(residual[i],rz);Ni=F(n.sqrt_r(F(g[i][i].h,n.SCALE)).h,n.SCALE)+eta[i]
        payment=eta[i]*Nz+etz*Ni+eta[i]*etz;zeta.append(value+I(-payment,payment));crosshat.append(value);crosspayments.append(payment)
        print(parity,'certified mixed correction covariance',i,flush=True)
    nu,alpha,delta=condensed(q,g,beta,qz,zeta,gz);taus=TAUS[:];peak=None;uniform=None
    if delta.h<0:
        peak=F((alpha.mid()/delta.mid()*10**50).__floor__(),10**50)
        if peak not in taus:taus.append(peak)
        uniform=F(nu.h,n.SCALE)+alpha.absupper()**2/(-F(delta.h,n.SCALE))
    packets=[];selected=None
    for tau in taus:
        Q,G=update(q,g,beta,qz,zeta,gz,tau);packet=test(Q,G,o['retained_masses'],tau)
        # Store compact packets for every frozen candidate; the complete
        # selected matrix is separately retained below.
        packets.append({k:v for k,v in packet.items() if k in ['tau','joined_status','joined_condensed_margin','joined_sufficient_determinant','joined_native_energy_determinant','physical_retained_Schur_gap_lower']})
        if selected is None and packet['joined_status']=='JOINED_THREE_RETAINED_PLUS_ALL_F_PASS':selected=(tau,Q,G,packet)
    if selected is None:
        tau=peak if peak is not None else F(1);Q,G=update(q,g,beta,qz,zeta,gz,tau);selected=(tau,Q,G,test(Q,G,o['retained_masses'],tau))
    tau,Q,G,packet=selected
    print(parity,'selected tau',float(tau),packet['joined_status'],flush=True)
    return dict(milestone='NF36',parity=parity,aperture='53/50',interval_grid_digits=500,regular_kernel_N=320,pole_degree=40,original_translation_cells=13,
        authenticated_input_sha256=p.old.prev.SHA,NF35_input_sha256=SHA35,NF34_input_sha256=parent.SHA34,
        correction_norm_upper=str(zm),correction_source_error_upper=str(ez),correction_residual_error_upper=str(etz),
        correction_source_coordinate_indices=list(corr),reconstructed_correction_source_coordinates=[v.ends() for v in corr.values()],
        reconstructed_native_correction_crosses=[v.ends() for v in betahat],original_native_correction_crosses=[v.ends() for v in beta],reverse_native_correction_crosses=[v.ends() for v in reverse],
        reconstructed_correction_native_energy=zzhat.ends(),original_correction_native_energy=qz.ends(),
        reconstructed_correction_projected_source_square=square.ends(),correction_source_square_payment=str(zpay),original_correction_projected_source_square=gz.ends(),
        reconstructed_correction_source_crosses=[v.ends() for v in crosshat],correction_source_cross_payments=list(map(str,crosspayments)),original_correction_source_crosses=[v.ends() for v in zeta],
        condensed_quadratic_coefficients=dict(nu0=nu.ends(),alpha=alpha.ends(),delta=delta.ends()),rational_peak_candidate=None if peak is None else str(peak),uniform_all_real_tau_margin_upper=None if uniform is None else str(uniform),
        all_real_tau_floor_family_rejected=uniform is not None and uniform<0,candidate_packets=packets,selected_tau=str(tau),
        original_corrected_native_energy_Gram=[[v.ends() for v in row] for row in Q],original_corrected_complete_source_Gram=[[v.ends() for v in row] for row in G],
        selected_joint_sign_packet=packet,inherited_retained_masses=list(map(str,o['retained_masses'])),
        entire_modified_remaining_54_frame_certified=False,complete_remaining_shared_source_Gram_certified=False,
        actual_negative_original_form_claimed=False,whole_aperture_positive=False,RH=False,F4=False,Lean=False)
if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('mode',choices=['choose','certify']);a.add_argument('--parity',choices=['even','odd']);a.add_argument('--trial');a.add_argument('--output',required=True);a=a.parse_args()
    data,source,hashes=p.old.prev.inputs()
    if a.mode=='choose':out=choose(data,source,a.parity)
    else:
        raw=Path(a.trial).read_bytes();out=run(data,source,json.loads(raw));out['fixed_trial_sha256']=hashlib.sha256(raw).hexdigest();out['native_archive_sha256']=hashes
    Path(a.output).write_text(json.dumps(out,indent=2)+'\n')
