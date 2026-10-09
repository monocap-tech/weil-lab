#!/usr/bin/env python3
"""NF34 independent frame replay, exact selection and physical payments."""
import argparse,json,hashlib,gzip,base64
from pathlib import Path
from fractions import Fraction as F
from math import factorial
import certify_native_expanded_shared_lift_nf34_106 as c
n=c.n;I=c.I;dot=c.dot;mv=c.mv;iv=c.iv
ROOT='notes/data/RPB108_NF34_'
def read(p):
    raw=Path(ROOT+p+'_20261009.json').read_bytes();return json.loads(raw),hashlib.sha256(raw).hexdigest()
def validate():
    data,source,hashes=c.old.prev.inputs();parents=c.parents();rows=[]
    etaunit=2*n.A*4*F(106,125)**320/(1-F(106,125))+16*(n.A/2)**41/F(factorial(41))
    for idx,parity in enumerate(['even','odd']):
        trial,th=read(parity.upper()+'_FIXED_EXPANDED_SHARED_LIFT');cert,ch=read(parity.upper()+'_EXPANDED_SHARED_LIFT_CERTIFICATE')
        assert cert['fixed_trial_sha256']==th and cert['native_archive_sha256']==hashes
        assert cert['authenticated_input_sha256']==trial['authenticated_input_sha256']==c.old.prev.SHA
        assert cert['NF33_input_sha256']==trial['NF33_input_sha256']==c.SHA33
        oldtr=parents[0]['parities'][idx];oldcert=parents[idx+1]
        ids,hi,T,B,C,K=c.old.frame(data,source,idx);Z=[list(map(F,row)) for row in oldtr['frozen_shared_lift_map']]
        a=list(map(F,oldtr['inherited_constraint_coordinates']));v=list(map(F,oldtr['fixed_probe_coefficients']));u=v[:56]
        ell=list(map(F,trial['exact_shared_constraint_functional']));z=list(map(F,trial['fixed_rational_additional_coefficients']))
        zi=trial['additional_high_indices'];assert zi==list(range(116+idx,181 if idx==0 else 180,2))
        mass=sum(t*t for t in u);assert ell==[sum(t*s for t,s in zip(u,col))/mass for col in zip(*T)]
        assert sum(t*s for t,s in zip(ell,a))==1
        x=list(map(F,data[0]['authenticated_compensated_targets'][idx]['retained_coefficients']))
        w=list(map(F,data[2]['parity_certificates'][idx]['exact_rational_retained_response']))
        assert sum(t*s for t,s in zip(x,u))==sum(t*s for t,s in zip(w,u))==0
        selection=[iv(v) for v in trial['reconstructed_selection_coordinates']]
        assert z==[F((t.mid()/4*10**100).__floor__(),10**100) for t in selection]
        selection_error=etaunit*c.norm(v);assert selection_error==F(trial['selection_source_error_upper'])
        selected=[t+I(-selection_error,selection_error) for t in selection]
        assert [t.ends() for t in selected]==trial['paid_original_selection_coordinates']
        captured=sum((n.sq(t) for t in selected),I(0));assert captured.ends()==trial['selected_shell_square']
        assert (captured/iv(oldcert['original_complete_remaining_source_square'])).ends()==trial['selected_shell_fraction_of_NF33_source_square']
        for check in trial['selection_functional_checks']+cert['correction_functional_checks']:
            a0,b0=iv(check['direct']),iv(check['functional']);assert max(a0.l,b0.l)<=min(a0.h,b0.h)
        coords=[iv(t) for t in cert['reconstructed_correction_source_coordinates']]
        ez=etaunit*c.norm(z);assert ez==F(cert['correction_source_error_upper'])
        zz=iv(cert['reconstructed_correction_energy'])+I(-ez*c.norm(z),ez*c.norm(z));assert zz.ends()==cert['original_correction_energy']
        beta=dot(v,coords)+I(-ez*c.norm(v),ez*c.norm(v));assert beta.ends()==cert['original_witness_correction_cross']
        reverse=iv(cert['reverse_witness_correction_cross']);assert max(beta.l,reverse.l)<=min(beta.h,reverse.h)
        q=iv(oldcert['original_native_energy'])-2*beta+zz;assert q.ends()==cert['original_lifted_witness_energy'] and q.l>0
        # Independently assemble each graph column's 58 native coefficients,
        # rather than using the producer's four-term Schur expansion.
        graph=[list(col)+[-row[j] for row in Z] for j,col in enumerate(zip(*T))]
        native=[[c.old.native(source,i,j) for j in ids+hi] for i in ids+hi]
        images=[mv(native,col) for col in graph]
        original=[[dot(col,image) for image in images] for col in graph]
        paidb=[dot(col,coords)+I(-ez*c.norm(col),ez*c.norm(col)) for col in graph]
        L=[[original[i][j]-paidb[i]*ell[j]-ell[i]*paidb[j]+zz*ell[i]*ell[j] for j in range(54)] for i in range(54)]
        inv,proof=c.old.prev.matrix.inverse(L)
        # Different interval arithmetic order need not reproduce endpoints;
        # both certified matrices enclose the same original finite graph.
        zsquare=sum(t*t for t in z)
        G=[[sum(t*s for t,s in zip(graph[i],graph[j]))+zsquare*ell[i]*ell[j] for j in range(54)] for i in range(54)]
        trace=sum((dot(inv[i],[row[i] for row in G]) for i in range(54)),I(0));assert trace.l>0
        fq=dot(a,mv(L,a));prod=iv(cert['expanded_frame_witness_energy']);assert max(fq.l,prod.l,q.l)<=min(fq.h,prod.h,q.h)
        assert F(cert['physical_expanded_shared_frame_gap_lower'])>0
        assert F(cert['expanded_shared_frame_inverse_verification']['congruence_Gershgorin_lower'])>0
        assert F(cert['expanded_shared_frame_inverse_verification']['inverse_residual_row_norm'])<1
        actualmass=sum(t*t for t in v+z);assert actualmass==F(cert['exact_lifted_witness_mass'])
        low0=[sum((t*c.old.native(source,i,j) for i,t in zip(ids+hi,v)),I(0)) for j in ids]
        eta=etaunit*c.norm(v)+ez+8*max(F(t.h-t.l,2*n.SCALE) for t in low0)+8*max(F(t.h-t.l,2*n.SCALE) for t in coords[:56])
        assert eta==F(cert['physical_residual_error_upper'])
        square=iv(cert['reconstructed_projected_source_square']);root=F(n.sqrt_r(F(square.h,n.SCALE)).h,n.SCALE)
        payment=2*eta*root+eta*eta;assert payment==F(cert['source_square_error_payment'])
        gamma=square+I(-payment,payment);assert gamma.ends()==cert['original_complete_projected_source_square']
        score=q-gamma/F(207,1000);assert score.ends()==cert['floor_score'] and (gamma/q).ends()==cert['source_square_over_native_energy']
        expected='LIFTED_WITNESS_WITH_ALL_F_PASSES' if score.l>0 else 'EXPANDED_SHARED_FLOOR_REJECTED' if score.h<0 else 'UNRESOLVED';assert cert['status']==expected
        raw=gzip.decompress(base64.b64decode(Path('notes/data/RPB108_NF24_NATIVE_RESIDUAL_PROJECTIONS_117_118_20261009.json.gz.b64').read_bytes()))
        assert hashlib.sha256(raw).hexdigest()=='4c8b0067088486e20f31a7904d3bf56a9f654e982b15450efa85cd6b25e24346'
        archive=json.loads(raw)['complete_original_signed_source'];degree=118 if idx==0 else 117
        oracle=sum((t*iv(archive[f'{i},{degree}']['full']) for i,t in zip(ids+hi,v)),I(0))
        check=cert['inherited_independent_native_projection_check'];assert oracle.ends()==check['original']
        paid=iv(check['reconstructed'])+I(-etaunit*c.norm(v),etaunit*c.norm(v));assert max(paid.l,oracle.l)<=min(paid.h,oracle.h)
        assert not cert['whole_aperture_positive'] and not cert['complete_remaining_source_Gram_certified'] and not cert['simultaneous_six_retained_direction_certificate_claimed']
        rows.append(dict(parity=parity,status=expected,trial_sha256=th,certificate_sha256=ch,
            exact_selection_functional_membership_and_mass=True,independent_full_native_graph_positive=True,
            independent_graph_inverse_verification=proof,independent_graph_physical_gap_lower=str(1/F(trace.h,n.SCALE)),
            three_way_energy_overlap=True,all_source_error_payments_checked=True,original_native_projection_overlap_checked=True,
            collective_remaining_infinite_high_sign_claimed=False))
        print(parity,'independent expanded native frame and physical payments PASS',flush=True)
    return dict(milestone='NF34',status='PASS',parity_checks=rows,whole_aperture_positive=False)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args()
    Path(a.output).write_text(json.dumps(validate(),indent=2)+'\n')
