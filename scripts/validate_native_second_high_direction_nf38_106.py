#!/usr/bin/env python3
"""NF38 exact independence, signed response payments and joined sign replay."""
import argparse,hashlib,json
from pathlib import Path
from fractions import Fraction as F
import certify_native_second_high_direction_nf38_106 as c
import validate_native_free_correction_functional_nf37_106 as v37
n=c.n;I=c.I;iv=c.iv;dot=c.dot;mv=c.mv
def validate(trial,cert,data,source,hashes,trialhash):
    parity=trial['parity'];o=c.objects(data,source,parity);prior=o['parent37']
    assert trial['NF37_input_sha256']==cert['NF37_input_sha256']==c.SHA37
    assert trial['NF36_input_sha256']==cert['NF36_input_sha256']==c.prev.SHA36
    assert trial['authenticated_input_sha256']==cert['authenticated_input_sha256']==c.p.old.prev.SHA
    assert cert['fixed_trial_sha256']==trialhash and cert['native_archive_sha256']==hashes
    h=list(map(F,prior['universal_fixed_rational_witness'])); assert trial['exact_moved_target_coefficients']==list(map(str,h))
    ids,vs=c.c.merge(o['columns'],h)
    assert ids==trial['merged_target_indices'] and list(map(str,vs))==trial['merged_target_coefficients']
    assert trial['frozen_old_functional']==list(map(str,o['old_functional']))
    assert trial['correction_indices']==o['old_correction_indices'] and trial['old_correction_coefficients']==list(map(str,o['old_correction']))
    coords=list(map(iv,trial['reconstructed_selection_coordinates'])); eta=o['unit']*c.p.norm(vs)
    assert str(eta)==trial['selection_source_error_upper']
    paid=[v+I(-eta,eta) for v in coords];assert [v.ends() for v in paid]==trial['paid_selection_coordinates']
    raw=[F((v.mid()/4*10**100).__floor__(),10**100) for v in coords]
    assert list(map(str,raw))==trial['raw_rational_correction_coefficients']
    z0=o['old_correction'];mass0=sum(v*v for v in z0);projection=sum(a*b for a,b in zip(z0,raw))/mass0
    z=[a-projection*b for a,b in zip(raw,z0)];assert list(map(str,z))==trial['fixed_rational_second_correction_coefficients']
    assert str(projection)==trial['exact_old_direction_projection_coefficient']
    mass1=sum(v*v for v in z);assert mass1>0 and str(mass1)==trial['exact_second_correction_mass_squared']
    inner=sum(a*b for a,b in zip(z0,z));assert inner==0 and trial['exact_old_second_inner_product']=='0'
    # Exact two-vector physical Gram: positive determinant proves independence.
    assert mass0>0 and mass0*mass1-inner*inner>0
    proj=dot(z0,paid)/mass0;orthpaid=[v-a*proj for v,a in zip(paid,z0)]
    capture=sum((n.sq(v) for v in orthpaid),I(0));gamma=dot(h,mv(c.prev.matrix(prior['original_selected_complete_source_Gram']),h))
    assert [v.ends() for v in orthpaid]==trial['orthogonal_paid_selection_coordinates']
    assert capture.ends()==trial['orthogonal_shell_square'] and gamma.ends()==trial['moved_target_original_projected_source_square']
    assert gamma.l>0 and (capture/gamma).ends()==trial['orthogonal_shell_fraction']
    for check in trial['independent_functional_checks']:
        a,b=iv(check['direct']),iv(check['functional']);v37.overlap(a,b)
    assert cert['source_norm_mass_upper']==list(map(str,o['source_norm_mass_upper']))
    assert cert['frozen_family_retained_projection_errors']==list(map(str,o['retained_errors']))
    assert cert['frozen_family_source_errors']==list(map(str,o['physical_source_errors']))
    zm=c.p.norm(z);ez=o['unit']*zm
    assert cert['correction_norm_upper']==str(zm) and cert['correction_source_error_upper']==str(ez)
    coordinate=dict(zip(cert['correction_source_coordinate_indices'],map(iv,cert['reconstructed_correction_source_coordinates'])))
    idx=['even','odd'].index(parity);assert list(coordinate)==list(range(idx,181 if idx==0 else 180,2))
    etz=ez+8*max(F(coordinate[i].h-coordinate[i].l,2*n.SCALE) for i in o['ids'])
    assert cert['correction_residual_error_upper']==str(etz)
    beta=[]
    for i,(ii,cc) in enumerate(o['columns']):
        bh=dot(cc,[coordinate[j] for j in ii]);assert bh.ends()==cert['reconstructed_native_correction_crosses'][i]
        payment=ez*o['source_norm_mass_upper'][i];value=bh+I(-payment,payment)
        assert value.ends()==cert['original_native_correction_crosses'][i];v37.overlap(value,iv(cert['reverse_native_correction_crosses'][i]));beta.append(value)
    qz=iv(cert['reconstructed_correction_native_energy'])+I(-ez*zm,ez*zm)
    assert qz.ends()==cert['original_correction_native_energy']
    square=iv(cert['reconstructed_correction_projected_source_square']);assert square.l>0
    Nz=F(n.sqrt_r(F(square.h,n.SCALE)).h,n.SCALE);payment=2*etz*Nz+etz*etz
    assert str(payment)==cert['correction_source_square_payment'];gz=square+I(-payment,payment)
    assert gz.ends()==cert['original_correction_projected_source_square']
    q=c.prev.matrix(prior['original_selected_native_energy_Gram']);g=c.prev.matrix(prior['original_selected_complete_source_Gram'])
    zeta=[]
    for i in range(3):
        eta=o['physical_source_errors'][i];Ni=F(n.sqrt_r(F(g[i][i].h,n.SCALE)).h,n.SCALE)+eta
        payment=eta*Nz+etz*Ni+eta*etz;assert str(payment)==cert['correction_source_cross_payments'][i]
        value=iv(cert['reconstructed_correction_source_crosses'][i])+I(-payment,payment)
        assert value.ends()==cert['original_correction_source_crosses'][i];zeta.append(value)
    frozen=cert['frozen_old_functional_analysis']
    result=c.analyze(q,g,beta,qz,zeta,gz,o['retained_masses'])
    assert result==frozen
    e=[a-b/c.K for a,b in zip(beta,zeta)];d=qz-gz/c.K;assert d.h<0
    U=[[q[i][j]-g[i][j]/c.K for j in range(3)] for i in range(3)];V=c.prev.matrix(frozen['second_functional_ceiling'])
    p0=V[0][0];p1=V[1][1]-n.sq(V[0][1])/p0;assert p0.l>0 and p1.l>0
    p2=V[2][2]-n.sq(V[0][2])/p0-n.sq(V[1][2]-V[0][1]*V[0][2]/p0)/p1
    v37.overlap(p2,iv(frozen['ceiling_condensed_margin']))
    rejected=frozen['all_real_second_functionals_floor_rejected_with_old_functional_frozen']
    if rejected:
        w=list(map(F,frozen['universal_fixed_rational_witness']));a=dot(w,mv(U,w));b=dot(w,e)
        bound=F(a.h,n.SCALE)+max(abs(F(b.l,n.SCALE)),abs(F(b.h,n.SCALE)))**2/(-F(d.h,n.SCALE))
        assert bound<0 and str(bound)==frozen['universal_witness_upper'] and p2.h<0
    lam=list(map(F,frozen['selected_rational_second_functional']));Q,G=c.prev.update(q,g,beta,qz,zeta,gz,lam)
    packet=frozen['selected_sign_packet'];status=packet['joined_status']
    if status!='NATIVE_ENERGY_UNRESOLVED':
        selectedU=c.prev.matrix(packet['sufficient_matrix']);p0=selectedU[0][0];p1=selectedU[1][1]-n.sq(selectedU[0][1])/p0;assert p0.l>0 and p1.l>0
        p2=selectedU[2][2]-n.sq(selectedU[0][2])/p0-n.sq(selectedU[1][2]-selectedU[0][1]*selectedU[0][2]/p0)/p1
        if status=='JOINED_THREE_RETAINED_PLUS_ALL_F_PASS':assert p2.l>0
        elif status=='JOINED_FLOOR_REJECTED':
            w=list(map(F,packet['fixed_rational_mixed_floor_witness']));assert dot(w,mv(selectedU,w)).h<0 and dot(w,mv(Q,w)).l>0
        for i in range(3):
            for j in range(3):v37.overlap(selectedU[i][j],U[i][j]-e[i]*lam[j]-lam[i]*e[j]+d*lam[i]*lam[j])
    par36=c.prev.parents()[0][idx+2]
    z0norm=c.p.norm(z0);cross=dot(z0,[coordinate[i] for i in trial['correction_indices']]);qpay=ez*z0norm
    assert cross.ends()==cert['reconstructed_old_second_native_cross'] and str(qpay)==cert['old_second_native_cross_payment']
    q01=cross+I(-qpay,qpay);assert q01.ends()==cert['original_old_second_native_cross'];v37.overlap(q01,iv(cert['reverse_old_second_native_cross']))
    eta0=F(par36['correction_residual_error_upper']);N0=F(n.sqrt_r(F(iv(par36['original_correction_projected_source_square']).h,n.SCALE)).h,n.SCALE)+eta0
    gpay=eta0*Nz+etz*N0+eta0*etz;assert str(gpay)==cert['old_second_source_cross_payment']
    g01=iv(cert['reconstructed_old_second_source_cross'])+I(-gpay,gpay);assert g01.ends()==cert['original_old_second_source_cross']
    joint=c.joint_analyze(q,g,beta,qz,zeta,gz,q01,g01,par36,o['old_functional'],o['retained_masses'])
    assert all(cert[k]==v for k,v in joint.items())
    H=c.prev.matrix(cert['joint_correction_floor_block']);inv=c.prev.matrix(cert['joint_correction_floor_inverse']);E=c.prev.matrix(cert['joint_floor_joined_high_crosses'])
    assert H[0][0].h<0 and (H[1][1]-n.sq(H[0][1])/H[0][0]).h<0
    V=c.prev.matrix(cert['joint_functional_ceiling']);p0=V[0][0];p1=V[1][1]-n.sq(V[0][1])/p0;assert p0.l>0 and p1.l>0
    p2=V[2][2]-n.sq(V[0][2])/p0-n.sq(V[1][2]-V[0][1]*V[0][2]/p0)/p1;v37.overlap(p2,iv(cert['joint_ceiling_condensed_margin']))
    joint_reject=cert['all_real_joint_two_direction_functionals_floor_rejected']
    if joint_reject:
        w=list(map(F,cert['joint_universal_fixed_rational_witness']));a=dot(w,mv(U,w));b=[dot(w,[E[i][j] for i in range(3)]) for j in range(2)]
        bound=a-dot(b,mv(inv,b));assert bound.h<0 and bound.ends()==cert['joint_universal_witness_upper'] and p2.h<0
        # Direct symmetric expansion has a separate arithmetic order.
        reaction=inv[0][0]*n.sq(b[0])+2*inv[0][1]*b[0]*b[1]+inv[1][1]*n.sq(b[1]);v37.overlap(a-reaction,bound)
    C=[list(map(F,row)) for row in cert['selected_rational_joint_functionals']]
    B=c.prev.matrix(cert['joint_native_joined_high_crosses']);S=c.prev.matrix(cert['joint_complete_source_joined_high_crosses'])
    QZ=c.prev.matrix(cert['joint_native_high_block']);GZ=c.prev.matrix(cert['joint_complete_source_high_block'])
    Q,G=c.joint_update(q,g,B,QZ,S,GZ,C);packet=cert['selected_sign_packet'];status=packet['joined_status']
    assert c.prev.ends(Q)==cert['original_selected_native_energy_Gram'] and c.prev.ends(G)==cert['original_selected_complete_source_Gram']
    if status!='NATIVE_ENERGY_UNRESOLVED':
        selectedU=c.prev.matrix(packet['sufficient_matrix']);p0=selectedU[0][0];p1=selectedU[1][1]-n.sq(selectedU[0][1])/p0;assert p0.l>0 and p1.l>0
        p2=selectedU[2][2]-n.sq(selectedU[0][2])/p0-n.sq(selectedU[1][2]-selectedU[0][1]*selectedU[0][2]/p0)/p1
        if status=='JOINED_THREE_RETAINED_PLUS_ALL_F_PASS':assert p2.l>0
        elif status=='JOINED_FLOOR_REJECTED':
            w=list(map(F,packet['fixed_rational_mixed_floor_witness']));assert dot(w,mv(selectedU,w)).h<0 and dot(w,mv(Q,w)).l>0
        for i in range(3):
            for j in range(3):
                direct=U[i][j]-sum((E[i][a]*C[a][j]+C[a][i]*E[j][a] for a in range(2)),I(0))+sum((C[a][i]*H[a][b]*C[b][j] for a in range(2) for b in range(2)),I(0))
                v37.overlap(selectedU[i][j],direct)
    assert cert['both_high_functionals_varied_jointly']
    for key in ['entire_modified_remaining_54_frame_certified','actual_negative_original_form_claimed','whole_aperture_positive','RH','F4','Lean']:assert not cert[key]
    return dict(parity=parity,status=status,physical_high_directions_exactly_independent=True,
        all_original_response_payments_checked=True,independent_ceiling_and_selected_LDL_checked=True,
        all_real_second_functionals_rejected_with_old_functional_frozen=rejected,
        all_real_joint_two_direction_functionals_rejected=joint_reject,old_second_signed_source_cross_checked=True,fixed_trial_sha256=trialhash)
def joint_controls():
    rows=[]
    def inner(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
    def product(A,x):return [inner(row,x) for row in A]
    for scale in [F(1),F(1,10**18)]:
        for s in [F(-1,100),F(0),F(1,100)]:
            V=[[F(1),F(1,2),F(1,4)],[F(1,2),F(1),F(-1,4)],[F(1,4),F(-1,4),F(1,4)+s]]
            V=[[scale*x for x in row] for row in V]
            H=[[-2*scale,-scale/2],[-scale/2,-scale]];det=H[0][0]*H[1][1]-H[0][1]**2
            inv=[[H[1][1]/det,-H[0][1]/det],[-H[0][1]/det,H[0][0]/det]]
            E=[[scale/10,-scale/50],[-scale/20,2*scale/25],[scale/20,3*scale/100]]
            U=[[V[i][j]+inner(E[i],product(inv,E[j])) for j in range(3)] for i in range(3)]
            assert H[0][0]<0 and det>0 and all(U[i][i]>0 and V[i][i]>0 for i in range(3))
            h=[F(-1,2),F(1,2),F(1)];a=inner(h,product(U,h));b=[inner(h,[E[i][j] for i in range(3)]) for j in range(2)]
            assert a-inner(b,product(inv,b))==scale*s
            C0=[[inner(inv[a],[E[j][b] for b in range(2)]) for j in range(3)] for a in range(2)]
            for C in [[[F(0)]*3 for _ in range(2)],C0,[[C0[a][j]+F((a+1)*(j+1),7) for j in range(3)] for a in range(2)]]:
                direct=[[U[i][j]-sum(E[i][a]*C[a][j]+C[a][i]*E[j][a] for a in range(2))
                    +sum(C[a][i]*H[a][b]*C[b][j] for a in range(2) for b in range(2)) for j in range(3)] for i in range(3)]
                diff=[[C[a][j]-C0[a][j] for j in range(3)] for a in range(2)]
                completed=[[V[i][j]+sum(diff[a][i]*H[a][b]*diff[b][j] for a in range(2) for b in range(2)) for j in range(3)] for i in range(3)]
                assert direct==completed
                x=product(C,h);value=inner(h,product(direct,h))
                assert value==a-2*inner(b,x)+inner(x,product(H,x)) and value<=scale*s
                if C==C0:assert value==scale*s and direct==V
            vi=[[I(x) for x in row] for row in V];de=c.c.parent.det3(vi)
            assert de.l==de.h==int(F(3,4)*scale**3*s*n.SCALE)
            assert (vi[0][0]*vi[1][1]-n.sq(vi[0][1])).l>0
            if s==0:assert product(V,h)==[F(0)]*3
            native=[[I(U[i][j]+(scale if i==j else 0)) for j in range(3)] for i in range(3)]
            assert native[0][0].l>0 and (native[0][0]*native[1][1]-n.sq(native[0][1])).l>0 and c.c.parent.det3(native).l>0
            rows.append(dict(scale=str(scale),exact_joint_ceiling_witness_value=str(scale*s),negative_definite_high_block=True,
                nonzero_signed_high_cross=True,positive_original_and_ceiling_diagonals=True,exact_completion_and_positive_null_negative_crossing=True,native_control_positive=True))
    return rows
if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('--output',required=True);a=a.parse_args()
    data,source,hashes=c.p.old.prev.inputs();par37,par36,old=c.parents()
    inherited=[v37.check(par37[i],i,par36,old) for i in range(2)];rows=[]
    for tag in ['EVEN','ODD']:
        tr=Path('notes/data/RPB108_NF38_'+tag+'_FIXED_SECOND_HIGH_DIRECTION_20261009.json').read_bytes()
        raw=Path('notes/data/RPB108_NF38_'+tag+'_SECOND_HIGH_DIRECTION_CERTIFICATE_20261009.json').read_bytes()
        row=validate(json.loads(tr),json.loads(raw),data,source,hashes,hashlib.sha256(tr).hexdigest());row['certificate_sha256']=hashlib.sha256(raw).hexdigest();rows.append(row)
    crossings,levels=v37.controls()
    out=dict(milestone='NF38',status='PASS',parity_checks=rows,inherited_NF37_free_functional_replay=inherited,
        exact_free_functional_crossing_controls=crossings,exact_joint_two_direction_crossing_controls=joint_controls(),positive_full_mass_shift_controls=levels,
        joined_retained_dimension_certified=4+sum(v['status']=='JOINED_THREE_RETAINED_PLUS_ALL_F_PASS' for v in rows),
        six_retained_direction_plus_all_F_certified=all(v['status']=='JOINED_THREE_RETAINED_PLUS_ALL_F_PASS' for v in rows),
        both_high_functionals_varied_jointly=True,actual_negative_original_form_claimed=False,whole_aperture_positive=False)
    Path(a.output).write_text(json.dumps(out,indent=2)+'\n')
