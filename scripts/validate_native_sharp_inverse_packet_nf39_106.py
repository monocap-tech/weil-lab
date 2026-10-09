#!/usr/bin/env python3
"""NF39 exact packet realizations, inverse identities and sign controls."""
import argparse,hashlib,json
from pathlib import Path
from fractions import Fraction as F
import certify_native_sharp_inverse_packet_nf39_106 as c
import validate_native_second_high_direction_nf38_106 as v38
def inside(A,box):
    for row,brow in zip(A,box):
        for x,b in zip(row,brow):
            lo,hi=map(F,b);assert lo<=x<=hi
def check(cert,idx,data,old):
    assert cert['NF38_input_sha256']==c.SHA38 and cert['NF37_input_sha256']==c.p.SHA37
    a={k:c.decode(v) for k,v in cert['exact_packet'].items()};expected,parent=c.packet_inputs(idx);assert a==expected
    assert cert['parity']==['even','odd'][idx] and cert['kappa']==str(c.K)
    for key,box in [('QZ',parent['joint_native_high_block']),('GZ',parent['joint_complete_source_high_block']),('B',parent['joint_native_joined_high_crosses']),('S',parent['joint_complete_source_joined_high_crosses']),('Q',old[idx]['original_selected_native_energy_Gram']),('G',old[idx]['original_selected_complete_source_Gram'])]:inside(a[key],box)
    gram,C,T,W=c.gram_and_surplus(a);_,gd=c.ldl(gram);_,cd=c.ldl(C);_,qd=c.ldl(a['Q'])
    assert min(gd)>0 and min(cd)>0 and min(qd)>0
    assert c.strings(gram)==cert['exact_seven_vector_high_Gram'] and list(map(str,gd))==cert['exact_Gram_LDL_pivots']
    assert c.strings(C)==cert['exact_positive_high_surplus'] and list(map(str,cd))==cert['exact_surplus_LDL_pivots']
    m=7;eye=[[F(int(i==j)) for j in range(m)] for i in range(m)]
    Z=[[F(int(i==j)) for j in range(2)] for i in range(m)];V=[[F(int(i==j+2)) for j in range(2)] for i in range(m)];R=[[F(int(i==j+4)) for j in range(3)] for i in range(m)]
    Pz=c.mm(c.mm(Z,c.inverse2(a['M'])),c.mm(c.tr(Z),gram));P=c.add(eye,c.scale(Pz,-1))
    assert c.mm(P,P)==P and c.mm(gram,P)==c.tr(c.mm(gram,P)) and c.mm(P,Z)==[[F(0)]*2 for _ in range(m)]
    assert c.mm(c.mm(c.tr(P),gram),P)==c.mm(gram,P)
    base=c.add(c.scale(eye,c.K),c.mm(c.mm(V,c.inverse2(C)),c.mm(c.tr(V),gram)))
    rows=[]
    for name,delta,sign in [('negative_minimal_background_model',F(0),-1),('positive_moment_preserving_background_model',F(1),1)]:
        model=cert[name];A=c.decode(model['high_operator']);inv=c.decode(model['exact_high_inverse'])
        assert model['delta']==str(delta) and A==c.add(base,c.scale(P,delta))
        assert c.mm(A,inv)==eye and c.mm(inv,A)==eye and c.mm(gram,A)==c.tr(c.mm(gram,A))
        # The positive surplus consists of V C^-1 V^* plus delta P.
        surplus=c.add(A,c.scale(eye,-c.K));assert surplus==c.add(c.mm(c.mm(V,c.inverse2(C)),c.mm(c.tr(V),gram)),c.scale(P,delta))
        AZ=c.mm(A,Z);assert AZ==c.add(c.scale(Z,c.K),V)
        # Every named moment, including the signed crosses, is identical.
        assert c.mm(c.mm(c.tr(Z),gram),Z)==a['M']
        assert c.mm(c.mm(c.tr(Z),gram),AZ)==a['QZ']
        assert c.mm(c.mm(c.tr(AZ),gram),AZ)==a['GZ']
        assert c.mm(c.mm(c.tr(R),gram),Z)==a['B']
        assert c.mm(c.mm(c.tr(R),gram),AZ)==a['S']
        assert c.mm(c.mm(c.tr(R),gram),R)==a['G']
        reaction=c.mm(c.mm(c.tr(R),gram),c.mm(inv,R));assert c.strings(reaction)==model['reaction'] and reaction==c.reaction(a,delta)
        schur=c.add(a['Q'],c.scale(reaction,-1));_,piv=c.ldl(schur)
        assert c.strings(schur)==model['Schur'] and list(map(str,piv))==model['Schur_LDL_pivots']
        assert piv[0]>0 and piv[1]>0
        if sign<0:
            assert piv[2]<0
            A2=[row[:2] for row in schur[:2]];border=[schur[i][2] for i in range(2)];w=[-v for v in c.mv(c.inverse2(A2),border)]+[F(1)]
            assert c.dot(w,c.mv(schur,w))==piv[2]
            high=[-v for v in c.mv(inv,c.mv(R,w))]
            fullvalue=c.dot(w,c.mv(a['Q'],w))+2*c.dot(c.mv(R,w),c.mv(gram,high))+c.dot(high,c.mv(c.mm(gram,A),high))
            assert fullvalue==piv[2]<0
        else:assert min(piv)>0
        rows.append(dict(delta=str(delta),all_named_moments_match_exactly=True,positive_high_background_floor=True,Schur_sign='negative' if sign<0 else 'positive'))
    H=c.add(a['QZ'],c.scale(a['GZ'],-1/c.K));E=c.add(a['B'],c.scale(a['S'],-1/c.K))
    ceiling=c.add(c.add(a['Q'],c.scale(a['G'],-1/c.K)),c.scale(c.mm(c.mm(E,c.inverse2(H)),c.tr(E)),-1))
    assert ceiling==c.decode(cert['negative_minimal_background_model']['Schur'])
    qi=c.p.prev.matrix(parent['joint_native_high_block']);Ci=[[qi[i][j]-c.K*a['M'][i][j] for j in range(2)] for i in range(2)]
    det=Ci[0][0]*Ci[1][1]-c.n.sq(Ci[0][1]);assert Ci[0][0].l>0 and det.l>0
    assert c.p.prev.ends(Ci)==cert['actual_high_surplus_intervals'] and det.ends()==cert['actual_high_surplus_determinant']
    h=list(map(F,parent['joint_universal_fixed_rational_witness']));value=c.p.dot(h,c.p.mv(c.p.prev.matrix(parent['joint_functional_ceiling']),h))
    assert value.h<0 and value.ends()==cert['actual_ceiling_witness_value'] and str(-F(value.h,c.n.SCALE))==cert['necessary_inverse_improvement_strict_lower']
    assert cert['abstract_model_only'] and not cert['full_Weil_identities_matched'] and not cert['exact_original_polynomial_coordinates_matched']
    assert not cert['actual_original_inverse_certified'] and not cert['actual_negative_original_form_claimed'] and not cert['whole_aperture_positive']
    return dict(parity=cert['parity'],status='PASS',exact_packet_models=rows,sharp_inverse_identity_checked=True,necessary_actual_witness_improvement=cert['necessary_inverse_improvement_strict_lower'])
def controls():
    rows=[];levels=[];h=[F(-1,2),F(1,2),F(1)]
    for scale in [F(1),F(1,10**18)]:
        A=[[2*scale,F(0)],[F(0),c.K*scale]];AI=c.inverse2(A);R=[[scale,F(0)],[F(0),scale],[scale,scale]]
        for s in [F(-1,100),F(0),F(1,100)]:
            S=[[F(1),F(1,2),F(1,4)],[F(1,2),F(1),F(-1,4)],[F(1,4),F(-1,4),F(1,4)+s]];S=c.scale(S,scale)
            assert S[0][0]>0 and S[0][0]*S[1][1]-S[0][1]**2>0
            Q=c.add(S,c.mm(c.mm(R,AI),c.tr(R)));_,qd=c.ldl(Q);assert min(qd)>0
            assert c.dot(h,c.mv(S,h))==scale*s
            di=c.p.c.parent.det3([[c.I(v) for v in row] for row in S]);assert di.l==di.h==int(F(3,4)*scale**3*s*c.n.SCALE)
            full=[[F(0)]*5 for _ in range(5)]
            for i in range(3):
                for j in range(3):full[i][j]=Q[i][j]
                for j in range(2):full[i][j+3]=full[j+3][i]=R[i][j]
            for i in range(2):
                for j in range(2):full[i+3][j+3]=A[i][j]
            if s==0:
                null=h+[-v for v in c.mv(AI,c.mv(c.tr(R),h))];assert c.mv(full,null)==[F(0)]*5
                if scale==1:
                    for delta in [F(1,1000),F(1,10),F(2)]:
                        shifted=c.add(full,[[delta if i==j else F(0) for j in range(5)] for i in range(5)]);_,pd=c.ldl(shifted);assert min(pd)>0
                        assert c.dot(null,c.mv(shifted,null))==delta*c.dot(null,null)
                        levels.append(dict(full_physical_mass_shift=str(delta),exact_ground_level=str(delta),exact_five_coordinate_null_vector=list(map(str,null))))
            rows.append(dict(scale=str(scale),exact_condensed_witness_value=str(scale*s),positive_native_retained_matrix=True,positive_high_background=True,exact_positive_null_negative_full_block_crossing=True))
    return rows,levels
if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('--output',required=True);a=a.parse_args()
    data,old=c.parents();native,source,hashes=c.p.p.old.prev.inputs();inherited=[]
    for idx in range(2):inherited.append(v38.validate(data[idx],data[idx+2],native,source,hashes,c.SHA38[idx]))
    rows=[]
    for idx,tag in enumerate(['EVEN','ODD']):
        raw=Path('notes/data/RPB108_NF39_'+tag+'_SHARP_INVERSE_PACKET_CERTIFICATE_20261009.json').read_bytes();row=check(json.loads(raw),idx,data,old);row['certificate_sha256']=hashlib.sha256(raw).hexdigest();rows.append(row)
    crossing,levels=controls()
    out=dict(milestone='NF39',status='PASS',NF38_input_sha256=c.SHA38,parity_checks=rows,inherited_NF38_response_replay=inherited,
        exact_full_block_crossing_controls=crossing,positive_whole_physical_mass_controls=levels,
        actual_original_inverse_certified=False,actual_negative_original_form_claimed=False,joined_retained_dimension_certified=4,whole_aperture_positive=False)
    Path(a.output).write_text(json.dumps(out,indent=2)+'\n')
