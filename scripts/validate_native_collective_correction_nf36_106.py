#!/usr/bin/env python3
"""NF36 exact selection, response payments, candidate and quadratic replay."""
import argparse,json,hashlib
from pathlib import Path
from fractions import Fraction as F
import certify_native_collective_correction_nf36_106 as c
n=c.n;I=c.I;iv=c.iv;dot=c.dot;p=c.p
ROOT='notes/data/RPB108_NF36_'
def read(name):
    raw=Path(ROOT+name+'_20261009.json').read_bytes();return json.loads(raw),hashlib.sha256(raw).hexdigest()
def validate(trial,cert,data,source,hashes,trialhash):
    parity=trial['parity'];idx=['even','odd'].index(parity);old=c.parents()[idx];o=c.parent.objects(data,source,parity)
    assert cert['fixed_trial_sha256']==trialhash and cert['native_archive_sha256']==hashes
    assert cert['authenticated_input_sha256']==trial['authenticated_input_sha256']==p.old.prev.SHA
    assert cert['NF35_input_sha256']==trial['NF35_input_sha256']==c.SHA35
    assert cert['NF34_input_sha256']==c.parent.SHA34
    f=list(map(F,trial['exact_mixed_target_coefficients']));assert list(map(str,f))==old['fixed_rational_mixed_floor_witness'] and f[2]==1
    target_ids,target=c.merge(o['columns'],f)
    assert target_ids==trial['merged_target_indices'] and list(map(str,target))==trial['merged_target_coefficients']
    zi=trial['correction_indices'];z=list(map(F,trial['fixed_rational_correction_coefficients']))
    assert zi==list(range(112+idx,181 if idx==0 else 180,2)) and trial['frozen_scalar_candidates']==list(map(str,c.TAUS))
    coords=[iv(v) for v in trial['reconstructed_selection_coordinates']]
    assert z==[F((v.mid()/4*10**100).__floor__(),10**100) for v in coords]
    error=o['unit']*p.norm(target);assert error==F(trial['selection_source_error_upper'])
    paid=[v+I(-error,error) for v in coords];assert [v.ends() for v in paid]==trial['paid_selection_coordinates']
    captured=sum((n.sq(v) for v in paid),I(0));assert captured.ends()==trial['selected_shell_square']
    q=[[iv(v) for v in row] for row in old['original_joined_native_energy_Gram']];g=[[iv(v) for v in row] for row in old['original_joined_complete_source_Gram']]
    gw=dot(f,p.mv(g,f));assert gw.ends()==trial['mixed_target_original_projected_source_square'] and (captured/gw).ends()==trial['selected_shell_fraction']
    for check in trial['independent_functional_checks']:
        a,b=iv(check['direct']),iv(check['functional']);assert max(a.l,b.l)<=min(a.h,b.h)
    zm=p.norm(z);ez=o['unit']*zm
    assert str(zm)==cert['correction_norm_upper'] and str(ez)==cert['correction_source_error_upper']
    coordinate=dict(zip(cert['correction_source_coordinate_indices'],[iv(v) for v in cert['reconstructed_correction_source_coordinates']]))
    assert list(coordinate)==list(range(idx,181 if idx==0 else 180,2))
    etz=ez+8*max(F(coordinate[i].h-coordinate[i].l,2*n.SCALE) for i in o['ids'])
    assert str(etz)==cert['correction_residual_error_upper']
    beta=[]
    for i,(ii,cc) in enumerate(o['columns']):
        bh=dot(cc,[coordinate[j] for j in ii]);assert bh.ends()==cert['reconstructed_native_correction_crosses'][i]
        payment=ez*o['source_norm_mass_upper'][i];b=bh+I(-payment,payment)
        assert b.ends()==cert['original_native_correction_crosses'][i]
        rev=iv(cert['reverse_native_correction_crosses'][i]);assert max(b.l,rev.l)<=min(b.h,rev.h);beta.append(b)
    qz=iv(cert['reconstructed_correction_native_energy'])+I(-ez*zm,ez*zm);assert qz.ends()==cert['original_correction_native_energy']
    square=iv(cert['reconstructed_correction_projected_source_square']);assert square.l>0
    Nz=F(n.sqrt_r(F(square.h,n.SCALE)).h,n.SCALE);zpay=2*etz*Nz+etz*etz
    assert str(zpay)==cert['correction_source_square_payment'];gz=square+I(-zpay,zpay);assert gz.ends()==cert['original_correction_projected_source_square']
    zeta=[]
    for i in range(3):
        eta=o['physical_source_errors'][i];Ni=F(n.sqrt_r(F(g[i][i].h,n.SCALE)).h,n.SCALE)+eta
        payment=eta*Nz+etz*Ni+eta*etz;assert str(payment)==cert['correction_source_cross_payments'][i]
        value=iv(cert['reconstructed_correction_source_crosses'][i])+I(-payment,payment)
        assert value.ends()==cert['original_correction_source_crosses'][i];zeta.append(value)
    nu,alpha,delta=c.condensed(q,g,beta,qz,zeta,gz)
    assert dict(nu0=nu.ends(),alpha=alpha.ends(),delta=delta.ends())==cert['condensed_quadratic_coefficients']
    taus=c.TAUS[:];peak=None;uniform=None
    if delta.h<0:
        peak=F((alpha.mid()/delta.mid()*10**50).__floor__(),10**50)
        if peak not in taus:taus.append(peak)
        uniform=F(nu.h,n.SCALE)+alpha.absupper()**2/(-F(delta.h,n.SCALE))
    assert cert['rational_peak_candidate']==(None if peak is None else str(peak))
    assert cert['uniform_all_real_tau_margin_upper']==(None if uniform is None else str(uniform))
    assert cert['all_real_tau_floor_family_rejected']==(uniform is not None and uniform<0)
    packets=[];selected=None
    for tau in taus:
        Q,G=c.update(q,g,beta,qz,zeta,gz,tau);packet=c.test(Q,G,o['retained_masses'],tau)
        packets.append({k:v for k,v in packet.items() if k in ['tau','joined_status','joined_condensed_margin','joined_sufficient_determinant','joined_native_energy_determinant','physical_retained_Schur_gap_lower']})
        if packet['joined_status']!='NATIVE_ENERGY_UNRESOLVED':
            direct=iv(packet['joined_condensed_margin']);quadratic=nu-2*alpha*tau+delta*tau*tau
            assert max(direct.l,quadratic.l)<=min(direct.h,quadratic.h)
            U=[[Q[i][j]-G[i][j]/F(207,1000) for j in range(3)] for i in range(3)]
            # Sequential LDL has a separate arithmetic order.
            p0=U[0][0];p1=U[1][1]-n.sq(U[0][1])/p0;assert p0.l>0 and p1.l>0
            p2=U[2][2]-n.sq(U[0][2])/p0-n.sq(U[1][2]-U[0][1]*U[0][2]/p0)/p1
            if packet['joined_status']=='JOINED_THREE_RETAINED_PLUS_ALL_F_PASS':assert p2.l>0
            elif packet['joined_status']=='JOINED_FLOOR_REJECTED':
                cf=list(map(F,packet['fixed_rational_mixed_floor_witness']));value=dot(cf,p.mv(U,cf));native=dot(cf,p.mv(Q,cf))
                assert value.h<0 and native.l>0
        if selected is None and packet['joined_status']=='JOINED_THREE_RETAINED_PLUS_ALL_F_PASS':selected=(tau,Q,G,packet)
    assert packets==cert['candidate_packets']
    if selected is None:
        tau=peak if peak is not None else F(1);Q,G=c.update(q,g,beta,qz,zeta,gz,tau);selected=(tau,Q,G,c.test(Q,G,o['retained_masses'],tau))
    tau,Q,G,packet=selected
    assert str(tau)==cert['selected_tau'] and packet==cert['selected_joint_sign_packet']
    assert [[v.ends() for v in row] for row in Q]==cert['original_corrected_native_energy_Gram']
    assert [[v.ends() for v in row] for row in G]==cert['original_corrected_complete_source_Gram']
    assert list(map(str,o['retained_masses']))==cert['inherited_retained_masses']
    assert not cert['actual_negative_original_form_claimed'] and not cert['whole_aperture_positive'] and not cert['complete_remaining_shared_source_Gram_certified']
    return dict(parity=parity,status=packet['joined_status'],selected_tau=str(tau),fixed_trial_sha256=trialhash,
        merged_mixed_target_and_rational_selection_checked=True,all_native_and_complete_source_response_payments_checked=True,
        full_candidate_matrices_replayed=True,independent_quadratic_and_LDL_checks=True,
        all_real_tau_floor_family_rejected=cert['all_real_tau_floor_family_rejected'])
if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('--output',required=True);a=a.parse_args();data,source,hashes=p.old.prev.inputs();rows=[]
    for parity in ['even','odd']:
        trial,th=read(parity.upper()+'_FIXED_COLLECTIVE_CORRECTION');cert,ch=read(parity.upper()+'_COLLECTIVE_CORRECTION_CERTIFICATE')
        row=validate(trial,cert,data,source,hashes,th);row['certificate_sha256']=ch;rows.append(row)
    from validate_native_joined_witnesses_nf35_106 import controls
    crossing,levels=controls()
    peak_controls=[]
    for s in [F(-1,100),F(0),F(1,100)]:
        # The genuine joined control A=I, b=(tau-1,1), d=1+s
        # has nu(tau)=s-(tau-1)^2 and positive diagonals throughout.
        nu0=I(s-1);alpha=I(-1);delta=I(-1)
        peak=alpha.mid()/delta.mid();upper=F(nu0.h,n.SCALE)+alpha.absupper()**2/(-F(delta.h,n.SCALE))
        assert peak==1 and upper==s
        for tau in c.TAUS+[peak]:
            matrix=[[I(1),I(0),I(tau-1)],[I(0),I(1),I(1)],[I(tau-1),I(1),I(1+s)]]
            determinant=c.parent.det3(matrix);expected=s-(tau-1)**2
            assert determinant.l==determinant.h==int(expected*n.SCALE)
        peak_controls.append(dict(peak='1',exact_all_real_margin_maximum=str(s),positive_diagonals=True))
    out=dict(milestone='NF36',status='PASS',parity_checks=rows,exact_joined_crossing_controls=crossing,positive_full_mass_shift_controls=levels,
        exact_concave_peak_crossing_controls=peak_controls,
        joined_retained_dimension_certified=4+sum(v['status']=='JOINED_THREE_RETAINED_PLUS_ALL_F_PASS' for v in rows),
        six_retained_direction_plus_all_F_certified=all(v['status']=='JOINED_THREE_RETAINED_PLUS_ALL_F_PASS' for v in rows),whole_aperture_positive=False)
    Path(a.output).write_text(json.dumps(out,indent=2)+'\n')
