#!/usr/bin/env python3
"""NF40 independent factor reconstruction, interval replay and response controls."""
import argparse,hashlib,json
from pathlib import Path
from fractions import Fraction as F
import certify_native_boundary_defect_nf40_106 as b
import validate_native_sharp_inverse_packet_nf39_106 as v39
c=b.c;p=b.p;n=b.n;K=b.K
SHA39=['ed9f383aa7231936e150b70c4232b736b957c291b1ef74d451dab55e4fd68d46','9aeb95f78a36fd1e45f08e8a92d677e7f60654fbe322d9c2a386c73d923804a2','4397d18a78fe8bf56d6928e7c4e438874ce4607e6d81c4418b4d989d67ee476c']
def check(cert,idx):
    a,ids,X,P,QY,DY,dd,gap,Pi,QYi,hashes=b.inputs(idx)
    assert cert['NF38_input_sha256']==c.SHA38 and cert['native_input_hashes']==hashes
    assert cert['boundary_mode_indices']==ids and cert['exact_boundary_Z_crosses']==c.strings(X)
    assert cert['paid_boundary_V_crosses']==p.prev.ends(Pi) and cert['original_native_boundary_energy_intervals']==p.prev.ends(QYi)
    assert cert['actual_boundary_defect_intervals']==p.prev.ends(DY) and cert['actual_boundary_defect_determinant']==dd.ends()
    assert cert['physical_boundary_defect_gap_strict_lower']==str(gap)
    # Independently test D-gap I positive by the 2x2 determinant criterion.
    shifted=[[DY[i][j]-gap*int(i==j) for j in range(2)] for i in range(2)]
    assert shifted[0][0].l>0 and (shifted[0][0]*shifted[1][1]-n.sq(shifted[0][1])).l>0
    assert cert['exact_aggregate_packet']=={k:c.strings(v) for k,v in a.items()}
    assert cert['chosen_boundary_V_crosses']==c.strings(P) and cert['chosen_boundary_energy']==c.strings(QY)
    m=cert['zero_response_extension'];G=c.decode(m['exact_nine_vector_Gram']);_,gd=c.ldl(G);assert min(gd)>0
    assert m['Gram_LDL_pivots_positive']==[True]*9
    G7,C,_,_=c.gram_and_surplus(a);assert [row[:7] for row in G[:7]]==G7
    assert [row[:4] for row in G[7:]]==[X[i]+P[i] for i in range(2)]
    assert [row[7:] for row in G[7:]]==b.eye(2)
    assert [row[4:7] for row in G[7:]]==c.decode(m['free_boundary_joined_source_crosses'])
    Z,V,R,Y=(b.basis(9,s,k) for s,k in [(0,2),(2,2),(4,3),(7,2)])
    adj=lambda U:c.mm(c.tr(U),G)
    Yt=c.add(Y,c.scale(c.mm(c.mm(Z,c.inverse2(a['M'])),c.tr(X)),-1))
    L=c.mm(adj(Yt),Yt);_,ld=c.ldl(L);assert min(ld)>0
    assert c.strings(L)==m['projected_boundary_Gram'] and list(map(str,ld))==m['projected_boundary_Gram_LDL_pivots']
    D=c.add(c.add(QY,c.scale(b.eye(2),-K)),c.scale(c.mm(c.mm(P,c.inverse2(C)),c.tr(P)),-1))
    _,ds=c.ldl(D);assert min(ds)>0 and c.strings(D)==m['exact_boundary_defect'] and list(map(str,ds))==m['boundary_defect_LDL_pivots']
    Dc=c.mm(c.mm(Yt,c.mm(c.mm(c.inverse2(L),D),c.inverse2(L))),adj(Yt))
    A0=c.add(c.scale(b.eye(9),K),c.mm(c.mm(V,c.inverse2(C)),adj(V)))
    # Reconstruct inverse actions by solving A0, rather than the producer's Woodbury formula.
    inv0=b.inverse(A0);AR=c.mm(inv0,R)
    assert c.mm(Dc,Z)==[[F(0)]*2 for _ in range(9)] and c.mm(Dc,AR)==[[F(0)]*3 for _ in range(9)]
    A=c.add(A0,Dc);assert c.mm(A,AR)==R and c.mm(G,A)==c.tr(c.mm(G,A))
    assert c.mm(adj(Y),c.mm(A,Y))==QY
    AZ=c.mm(A,Z);assert AZ==c.add(c.scale(Z,K),V)
    for expected,actual in [(a['M'],c.mm(adj(Z),Z)),(a['QZ'],c.mm(adj(Z),AZ)),(a['GZ'],c.mm(adj(AZ),AZ)),(a['B'],c.mm(adj(R),Z)),(a['S'],c.mm(adj(R),AZ)),(a['G'],c.mm(adj(R),R))]:assert expected==actual
    J=c.mm(adj(R),AR);assert J==c.reaction(a,F(0)) and c.strings(J)==m['exact_reaction']
    S=c.add(a['Q'],c.scale(J,-1));_,sd=c.ldl(S);assert sd[0]>0 and sd[1]>0 and sd[2]<0
    assert c.strings(S)==m['exact_joined_Schur'] and list(map(str,sd))==m['Schur_LDL_pivots']
    assert m['abstract_model_only'] and not m['full_Weil_identities_matched'] and not m['free_boundary_source_crosses_are_actual_original_pairings']
    assert not cert['actual_original_inverse_improvement_certified'] and not cert['actual_negative_original_form_claimed'] and not cert['whole_high_defect_gap_claimed'] and not cert['whole_aperture_positive']
    return dict(parity=cert['parity'],status='PASS',physical_boundary_defect_gap_strict_lower=str(gap),native_boundary_defect_positive=True,nine_vector_Gram_positive=True,all_named_moments_and_boundary_energy_match=True,zero_joined_inverse_improvement=True,abstract_joined_Schur_negative=True)
def controls():
    out=[]
    for d in [F(1,1000),F(1),F(100)]:
        A0=[[F(2),F(0)],[F(0),K]];r=[F(1),F(0)];Y=[F(0),F(1)];D=[[F(0),F(0)],[F(0),d]];A=c.add(A0,D)
        response=c.dot(r,c.mv(c.add(c.inverse2(A0),c.scale(c.inverse2(A),-1)),r))
        assert c.dot(Y,c.mv(D,Y))==d and response==0
        coupled=c.add(A,[[d,F(0)],[F(0),F(0)]])
        improved=c.dot(r,c.mv(c.add(c.inverse2(A0),c.scale(c.inverse2(coupled),-1)),r));assert improved>0
        out.append(dict(boundary_defect=str(d),uncoupled_inverse_improvement='0',coupled_inverse_improvement=str(improved)))
    return out
if __name__=='__main__':
    q=argparse.ArgumentParser();q.add_argument('--output',required=True);q=q.parse_args()
    names=['EVEN_SHARP_INVERSE_PACKET_CERTIFICATE','ODD_SHARP_INVERSE_PACKET_CERTIFICATE','SHARP_INVERSE_PACKET_VALIDATION']
    raw=[Path('notes/data/RPB108_NF39_'+v+'_20261009.json').read_bytes() for v in names]
    assert [hashlib.sha256(v).hexdigest() for v in raw]==SHA39 and json.loads(raw[2])['status']=='PASS'
    data,old=c.parents();inherited=[v39.check(json.loads(raw[i]),i,data,old) for i in range(2)]
    rows=[]
    for idx,tag in enumerate(['EVEN','ODD']):
        raw40=Path('notes/data/RPB108_NF40_'+tag+'_BOUNDARY_DEFECT_CERTIFICATE_20261009.json').read_bytes();row=check(json.loads(raw40),idx);row['certificate_sha256']=hashlib.sha256(raw40).hexdigest();rows.append(row)
    crossing,levels=v39.controls()
    out=dict(milestone='NF40',status='PASS',NF39_input_sha256=SHA39,parity_checks=rows,inherited_NF39_packet_replay=inherited,boundary_response_controls=controls(),exact_full_block_crossing_controls=crossing,positive_whole_physical_mass_controls=levels,whole_aperture_positive=False,actual_original_inverse_improvement_certified=False)
    Path(q.output).write_text(json.dumps(out,indent=2)+'\n');print('NF40 validation PASS',flush=True)
