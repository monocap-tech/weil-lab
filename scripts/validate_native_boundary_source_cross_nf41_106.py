#!/usr/bin/env python3
"""NF41 moment replay and independent fixed-cross zero-response factor audit."""
import argparse,hashlib,json
from pathlib import Path
from fractions import Fraction as F
import certify_native_boundary_source_cross_nf41_106 as f
import validate_native_boundary_defect_nf40_106 as v40
b=f.b;c=f.c;p=f.p;n=f.n;K=f.K;I=f.I

def check(cert,idx,native,source,hashes):
    parity=['even','odd'][idx];assert cert['parity']==parity and cert['NF40_input_sha256']==f.SHA40 and cert['authenticated_native_input_sha256']==hashes
    o=p.objects(native,source,parity);ids=[112+idx,114+idx];assert ids==cert['boundary_mode_indices']
    assert cert['frozen_joined_polynomial_columns']==[dict(indices=ii,coefficients=list(map(str,cc))) for ii,cc in o['columns']]
    engine=p.p.old.probe.Moments(720,parity);sy=[engine.source([y],[F(1)]) for y in ids]
    measured=[[] for _ in ids];reverse=[[] for _ in ids];errors=[]
    for k,(ii,cc) in enumerate(o['columns']):
        s=engine.source(ii,cc);errors.append(engine.eta*p.p.norm(cc))
        for j,y in enumerate(ids):
            measured[j].append(engine.pair(s,n.basis(y)));reverse[j].append(engine.pair(sy[j],s[0]))
        print(parity,'replayed signed boundary source column',k,flush=True)
    assert p.prev.ends(measured)==cert['reconstructed_boundary_source_crosses'] and p.prev.ends(reverse)==cert['reverse_reconstructed_native_crosses']
    assert list(map(str,errors))==cert['physical_source_error_payments']
    YR=[[v+I(-errors[k],errors[k]) for k,v in enumerate(row)] for row in measured]
    assert p.prev.ends(YR)==cert['original_signed_boundary_source_crosses']
    for j in range(2):
        for k in range(3):
            r=reverse[j][k]+I(-errors[k],errors[k]);assert max(r.l,YR[j][k].l)<=min(r.h,YR[j][k].h)
    H,h,hw,square=f.coupling(idx,YR)
    assert p.prev.ends(H)==cert['original_projected_boundary_A0_inverse_source_coupling'] and list(map(str,h))==cert['fixed_NF38_witness']
    assert [v.ends() for v in hw]==cert['original_witness_boundary_inverse_coupling'] and square.ends()==cert['original_witness_boundary_inverse_coupling_square'] and square.l>0
    chosen=c.decode(cert['chosen_enclosure_compatible_boundary_source_crosses']);v40.v39.inside(chosen,cert['original_signed_boundary_source_crosses'])
    a,_,X,P,QY,*_=b.inputs(idx);m=cert['fixed_cross_zero_response_extension'];G=c.decode(m['exact_nine_vector_Gram']);_,gd=c.ldl(G);assert min(gd)>0
    G7,C,_,_=c.gram_and_surplus(a);assert [r[:7] for r in G[:7]]==G7
    assert [r[:7] for r in G[7:]]==[X[i]+P[i]+chosen[i] for i in range(2)] and [r[7:] for r in G[7:]]==b.eye(2)
    Z,V,R,Y=(b.basis(9,s,k) for s,k in [(0,2),(2,2),(4,3),(7,2)])
    adj=lambda U:c.mm(c.tr(U),G)
    A0=c.add(c.scale(b.eye(9),K),c.mm(c.mm(V,c.inverse2(C)),adj(V)));AI=b.inverse(A0);AR=c.mm(AI,R)
    Ytilde=c.add(Y,c.scale(c.mm(c.mm(Z,c.inverse2(a['M'])),c.tr(X)),-1))
    v40.v39.inside(c.mm(adj(Ytilde),AR),cert['original_projected_boundary_A0_inverse_source_coupling'])
    span=[z+ar for z,ar in zip(Z,AR)];SG=c.mm(adj(span),span);_,ds=c.ldl(SG);assert min(ds)>0
    projection=c.mm(c.mm(span,b.inverse(SG)),adj(span));assert c.mm(projection,projection)==projection and c.mm(G,projection)==c.tr(c.mm(G,projection))
    assert c.mm(projection,span)==span
    Yhat=c.mm(c.add(b.eye(9),c.scale(projection,-1)),Y);L=c.mm(adj(Yhat),Yhat);_,lp=c.ldl(L);assert min(lp)>0 and c.strings(L)==m['projected_boundary_Gram']
    D=c.add(c.add(QY,c.scale(b.eye(2),-K)),c.scale(c.mm(c.mm(P,c.inverse2(C)),c.tr(P)),-1));_,dp=c.ldl(D);assert min(dp)>0
    Dc=c.mm(c.mm(Yhat,c.mm(c.mm(c.inverse2(L),D),c.inverse2(L))),adj(Yhat));A=c.add(A0,Dc)
    assert c.mm(Dc,span)==[[F(0)]*5 for _ in range(9)] and c.mm(A,AR)==R
    assert c.mm(G,A)==c.tr(c.mm(G,A)) and c.mm(A,Z)==c.add(c.scale(Z,K),V)
    assert c.mm(adj(Y),c.mm(A,Y))==QY and c.mm(adj(Y),R)==chosen
    AZ=c.mm(A,Z)
    for expected,actual in [(a['M'],c.mm(adj(Z),Z)),(a['QZ'],c.mm(adj(Z),AZ)),(a['GZ'],c.mm(adj(AZ),AZ)),(a['B'],c.mm(adj(R),Z)),(a['S'],c.mm(adj(R),AZ)),(a['G'],c.mm(adj(R),R))]:assert expected==actual
    J=c.mm(adj(R),AR);Schur=c.add(a['Q'],c.scale(J,-1));_,sd=c.ldl(Schur)
    assert J==c.reaction(a,F(0)) and c.strings(J)==m['exact_reaction'] and c.strings(Schur)==m['exact_joined_Schur'] and list(map(str,sd))==m['Schur_LDL_pivots']
    assert sd[0]>0 and sd[1]>0 and sd[2]<0
    assert m['abstract_enclosure_compatible_model_only'] and not m['actual_unknown_exact_moments_matched'] and not m['full_Weil_identities_matched']
    assert not cert['actual_inverse_improvement_lower_bound_certified'] and not cert['actual_negative_original_form_claimed'] and not cert['whole_aperture_positive']
    return dict(parity=parity,status='PASS',new_signed_native_crosses_replayed=True,original_boundary_inverse_witness_coupling_square=square.ends(),NF40_specific_zero_response_model_excluded=True,fixed_cross_nine_vector_Gram_positive=True,fixed_cross_zero_response_model_verified=True)
def controls():
    out=[]
    for d in [F(1,1000),F(1),F(100)]:
        A0=[[F(2),F(0),F(0)],[F(0),K,F(0)],[F(0),F(0),K]];r=[F(1),F(0),F(0)];Y=[F(3,5),F(0),F(4,5)];Z=[F(0),F(1),F(0)]
        D=[[F(0)]*3 for _ in range(3)];D[2][2]=d;A=c.add(A0,D);ar=c.mv(b.inverse(A0),r)
        assert c.dot(Y,Y)==1 and c.dot(Y,Z)==0 and c.dot(Y,ar)==F(3,10) and c.dot(Y,c.mv(D,Y))==F(16,25)*d and c.mv(D,ar)==[F(0)]*3
        assert c.dot(r,c.mv(c.add(b.inverse(A0),c.scale(b.inverse(A),-1)),r))==0
        D[0][0]=d;coupled=c.add(A0,D);response=c.dot(r,c.mv(c.add(b.inverse(A0),c.scale(b.inverse(coupled),-1)),r));assert response>0
        fcol=c.mv(D,Y);dy=c.dot(Y,fcol);g=c.dot(fcol,ar);den=dy+c.dot(fcol,c.mv(b.inverse(A0),fcol));bound=g*g/den
        minorant=c.add(A0,[[x*y/dy for y in fcol] for x in fcol]);woodbury=c.dot(r,c.mv(c.add(b.inverse(A0),c.scale(b.inverse(minorant),-1)),r))
        assert woodbury==bound and 0<bound<=response
        remainder=c.add(D,c.scale([[x*y/dy for y in fcol] for x in fcol],-1))
        assert remainder[1]==[F(0)]*3 and remainder[0][0]>=0 and remainder[2][2]>=0 and remainder[0][0]*remainder[2][2]-remainder[0][2]**2==0
        out.append(dict(boundary_inverse_coupling='3/10',positive_boundary_defect=str(F(16,25)*d),uncoupled_inverse_improvement='0',coupled_inverse_improvement=str(response),defect_source_Woodbury_lower_bound=str(bound),positive_defect_remainder_checked=True))
    return out
if __name__=='__main__':
    q=argparse.ArgumentParser();q.add_argument('--output',required=True);q=q.parse_args();parent=f.parents();inherited=[v40.check(parent[i],i) for i in range(2)]
    native,source,hashes=p.p.old.prev.inputs();rows=[]
    for idx,tag in enumerate(['EVEN','ODD']):
        raw=Path('notes/data/RPB108_NF41_'+tag+'_BOUNDARY_SOURCE_CROSS_CERTIFICATE_20261009.json').read_bytes();r=check(json.loads(raw),idx,native,source,hashes);r['certificate_sha256']=hashlib.sha256(raw).hexdigest();rows.append(r)
    crossing,levels=v40.v39.controls();out=dict(milestone='NF41',status='PASS',NF40_input_sha256=f.SHA40,parity_checks=rows,inherited_NF40_replay=inherited,nonzero_boundary_coupling_zero_response_controls=controls(),exact_full_block_crossing_controls=crossing,positive_whole_physical_mass_controls=levels,actual_inverse_improvement_lower_bound_certified=False,whole_aperture_positive=False)
    Path(q.output).write_text(json.dumps(out,indent=2)+'\n');print('NF41 validation PASS',flush=True)
