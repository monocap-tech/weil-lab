#!/usr/bin/env python3
"""NF35 inherited-block custody, physical payments and joined sign checks."""
import argparse,json,hashlib
from pathlib import Path
from fractions import Fraction as F
import certify_native_joined_witnesses_nf35_106 as c
n=c.n;I=c.I;iv=c.iv;dot=c.dot
ROOT='notes/data/RPB108_NF35_'
def validate(cert,data,source,hashes):
    o=c.objects(data,source,cert['parity']);old=o['oldblock'];parent=o['parent34']
    assert cert['native_archive_sha256']==hashes and cert['authenticated_input_sha256']==c.prev.old.prev.SHA
    assert cert['NF33_input_sha256']==c.prev.SHA33 and cert['NF34_input_sha256']==c.SHA34
    q=[[iv(v) for v in row] for row in cert['original_joined_native_energy_Gram']]
    g=[[iv(v) for v in row] for row in cert['original_joined_complete_source_Gram']]
    assert [[v.ends() for v in row[:2]] for row in q[:2]]==old['original_finite_energy_Gram']
    assert [[v.ends() for v in row[:2]] for row in g[:2]]==old['original_complete_residual_Gram']
    assert q[2][2].ends()==parent['original_lifted_witness_energy'] and g[2][2].ends()==parent['original_complete_projected_source_square']
    eta=o['physical_source_errors'];assert list(map(str,eta))==cert['physical_source_reconstruction_error_bounds']
    assert list(map(str,o['retained_masses']))==cert['inherited_retained_masses']
    ui,uc=o['columns'][2];u=uc[:56];hm=c.prev.norm(uc[56:]);um=c.prev.norm(u)
    assert str(hm)==cert['high_witness_component_norm_upper'] and str(um)==cert['retained_witness_norm_upper']
    bounds=[F(n.sqrt_r(F(g[i][i].h,n.SCALE)).h,n.SCALE)+eta[i] for i in range(3)]
    assert list(map(str,bounds))==cert['reconstructed_source_norm_upper_bounds']
    for i in range(2):
        cross=cert['new_native_cross_proof'][i]
        # Expand the retained native term with a separate summation order.
        raw=sum((v*z for v,z in zip(u,o['low'][i])),I(0));saved=iv(cross['retained'])
        assert max(raw.l,saved.l)<=min(raw.h,saved.h)
        qpay=o['retained_errors'][i]*um+o['unit']*o['source_norm_mass_upper'][i]*hm
        assert qpay==F(cross['error_payment'])
        paid=saved+iv(cross['high'])+I(-qpay,qpay)
        assert paid.ends()==q[i][2].ends()==q[2][i].ends()
        payment=eta[i]*bounds[2]+eta[2]*bounds[i]+eta[i]*eta[2]
        assert payment==F(cert['new_source_cross_error_payments'][f'{i},2'])
        value=iv(cert['reconstructed_new_source_crosses'][f'{i},2'])+I(-payment,payment)
        assert value.ends()==g[i][2].ends()==g[2][i].ends()
    U=[[q[i][j]-g[i][j]/F(207,1000) for j in range(3)] for i in range(3)]
    assert [[v.ends() for v in row] for row in U]==cert['sufficient_matrix']
    nd=c.det3(q);assert q[0][0].l>0 and (q[0][0]*q[1][1]-n.sq(q[0][1])).l>0 and nd.l>0
    assert nd.ends()==cert['joined_native_energy_determinant']
    determinant=c.det3(U);assert determinant.ends()==cert['joined_sufficient_determinant']
    # A sequential LDL elimination checks the same original joined matrix
    # independently of the producer's two-by-two inverse formula.
    p0=U[0][0];p1=U[1][1]-n.sq(U[0][1])/p0
    mixed=U[1][2]-U[0][1]*U[0][2]/p0
    p2=U[2][2]-n.sq(U[0][2])/p0-n.sq(mixed)/p1
    assert p0.l>0 and p1.l>0
    leading=U[0][0]*U[1][1]-n.sq(U[0][1]);assert leading.ends()==cert['leading_pair_sufficient_determinant']
    reaction=(U[1][1]*n.sq(U[0][2])-2*U[0][1]*U[0][2]*U[1][2]+U[0][0]*n.sq(U[1][2]))/leading
    margin=U[2][2]-reaction
    assert reaction.ends()==cert['joined_floor_reaction'] and margin.ends()==cert['joined_condensed_margin']
    expected='JOINED_THREE_RETAINED_PLUS_ALL_F_PASS' if margin.l>0 and determinant.l>0 else 'JOINED_FLOOR_REJECTED' if margin.h<0 and determinant.h<0 else 'UNRESOLVED'
    assert expected==cert['joined_status']
    result=dict(parity=cert['parity'],status=expected,parent_blocks_preserved=True,physical_source_and_native_cross_payments_checked=True,
        native_three_direction_energy_positive=True,sequential_LDL_last_pivot=p2.ends(),retained_components_exactly_orthogonal=True)
    if expected=='JOINED_THREE_RETAINED_PLUS_ALL_F_PASS':
        assert p2.l>0
        inv,proof=c.prev.old.prev.matrix.inverse(U);assert proof==cert['positive_inverse_verification']
        trace=sum((inv[i][i]*o['retained_masses'][i] for i in range(3)),I(0))
        assert str(1/F(trace.h,n.SCALE))==cert['physical_retained_Schur_gap_lower']
        result['physical_retained_Schur_gap_lower']=cert['physical_retained_Schur_gap_lower']
    elif expected=='JOINED_FLOOR_REJECTED':
        assert p2.h<0
        f=list(map(F,cert['fixed_rational_mixed_floor_witness']))
        value=sum((f[i]*f[j]*U[i][j] for i in range(3) for j in range(3)),I(0))
        native=sum((f[i]*f[j]*q[i][j] for i in range(3) for j in range(3)),I(0))
        assert value.h<0 and native.l>0
        oldvalue=iv(cert['mixed_witness_floor_value']);assert max(value.l,oldvalue.l)<=min(value.h,oldvalue.h)
        result.update(fixed_mixed_witness_floor_negative=True,mixed_witness_original_native_energy_positive=True)
    assert not cert['actual_negative_original_form_claimed'] and not cert['whole_aperture_positive'] and not cert['complete_remaining_shared_source_Gram_certified']
    return result

def controls():
    out=[]
    for scale in [F(1),F(1,10**18)]:
        for s in [F(-1,100),F(0),F(1,100)]:
            U=[[I(1),I(F(1,2)),I(F(1,4))],[I(F(1,2)),I(1),I(F(-1,4))],[I(F(1,4)),I(F(-1,4)),I(F(1,4)+s)]]
            determinant=c.det3(U);assert determinant.l==determinant.h==int(F(3,4)*s*n.SCALE)
            f=[F(-1,2),F(1,2),F(1)];value=dot(f,c.prev.mv(U,f));assert value.l==value.h==int(s*n.SCALE)
            scaled=[[scale*v for v in row] for row in U]
            sd=c.det3(scaled);sv=dot(f,c.prev.mv(scaled,f))
            assert sd.l==sd.h==int(scale**3*F(3,4)*s*n.SCALE) and sv.l==sv.h==int(scale*s*n.SCALE)
            Q=[[scale*(U[i][j]+I(int(i==j))) for j in range(3)] for i in range(3)]
            assert c.det3(Q).l>0 and Q[0][0].l>0
            out.append(dict(scale=str(scale),positive_floor_diagonals=True,condensed_floor_margin=str(scale*s),
                floor_determinant=str(scale**3*F(3,4)*s),exact_positive_null_negative_crossing=True,native_control_positive=True))
    # At s=0 the completion-square identity is PSD and f is an exact null.
    # Adding delta times the full physical identity has exact ground delta.
    M=[[I(1),I(F(1,2)),I(F(1,4))],[I(F(1,2)),I(1),I(F(-1,4))],[I(F(1,4)),I(F(-1,4)),I(F(1,4))]]
    assert all(v.l==v.h==0 for v in c.prev.mv(M,f)) and c.det3(M).l==c.det3(M).h==0
    assert (M[0][0]*M[1][1]-n.sq(M[0][1])).l>0
    levels=[]
    for delta in [F(1,1000),F(1,10),F(2)]:
        shifted=[[M[i][j]+I(delta if i==j else 0) for j in range(3)] for i in range(3)]
        assert c.det3(shifted).l>0 and (shifted[0][0]*shifted[1][1]-n.sq(shifted[0][1])).l>0
        ray=dot(f,c.prev.mv(shifted,f));expected=delta*sum(v*v for v in f)
        assert ray.l==ray.h==int(expected*n.SCALE)
        levels.append(dict(full_physical_mass_shift=str(delta),exact_ground_level=str(delta),null_vector=['-1/2','1/2','1']))
    return out,levels

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args()
    data,source,hashes=c.prev.old.prev.inputs();rows=[]
    for parity in ['even','odd']:
        raw=Path(ROOT+parity.upper()+'_JOINED_WITNESSES_CERTIFICATE_20261009.json').read_bytes()
        row=validate(json.loads(raw),data,source,hashes);row['certificate_sha256']=hashlib.sha256(raw).hexdigest();rows.append(row)
    crossing,levels=controls()
    out=dict(milestone='NF35',status='PASS',parity_checks=rows,exact_joined_crossing_controls=crossing,positive_full_mass_shift_controls=levels,
        six_retained_direction_plus_all_F_certified=all(row['status']=='JOINED_THREE_RETAINED_PLUS_ALL_F_PASS' for row in rows),whole_aperture_positive=False)
    Path(a.output).write_text(json.dumps(out,indent=2)+'\n')
