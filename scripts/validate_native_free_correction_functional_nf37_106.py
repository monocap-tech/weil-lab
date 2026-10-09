#!/usr/bin/env python3
"""NF37: authenticated response replay and universal fixed-witness checks."""
import argparse, hashlib, json
from pathlib import Path
from fractions import Fraction as F
import certify_native_free_correction_functional_nf37_106 as p
import validate_native_collective_correction_nf36_106 as v36
n=p.n; I=p.I; iv=p.iv; dot=p.dot; mv=p.mv
def overlap(a,b): assert max(a.l,b.l)<=min(a.h,b.h)
def check(cert,idx,data,old):
    response=data[idx+2]; prior=old[idx]
    assert cert['NF36_input_sha256']==p.SHA36 and cert['NF35_input_sha256']==p.c.SHA35
    assert cert['parity']==['even','odd'][idx] and cert['aperture']=='53/50' and cert['kappa']==str(p.K)
    assert cert['correction_indices']==data[idx]['correction_indices']
    assert cert['correction_coefficients']==data[idx]['fixed_rational_correction_coefficients']
    Q=p.matrix(prior['original_joined_native_energy_Gram']); G=p.matrix(prior['original_joined_complete_source_Gram'])
    beta=list(map(iv,response['original_native_correction_crosses'])); zeta=list(map(iv,response['original_correction_source_crosses']))
    qz=iv(response['original_correction_native_energy']); gz=iv(response['original_correction_projected_source_square'])
    U=[[Q[i][j]-G[i][j]/p.K for j in range(3)] for i in range(3)]
    e=[a-b/p.K for a,b in zip(beta,zeta)]; d=qz-gz/p.K
    assert d.h<0 and d.ends()==cert['correction_floor_diagonal']
    assert p.ends(U)==cert['original_floor_matrix'] and [v.ends() for v in e]==cert['correction_floor_crosses']
    V=[[U[i][j]-(n.sq(e[i]) if i==j else e[i]*e[j])/d for j in range(3)] for i in range(3)]
    assert p.ends(V)==cert['all_real_functional_Loewner_ceiling']
    d2=V[0][0]*V[1][1]-n.sq(V[0][1]); det=p.c.parent.det3(V)
    assert V[0][0].l>0 and d2.l>0 and det.h<0
    assert d2.ends()==cert['ceiling_leading_pair_determinant'] and det.ends()==cert['ceiling_determinant']
    reaction=(V[1][1]*n.sq(V[0][2])-2*V[0][1]*V[0][2]*V[1][2]+V[0][0]*n.sq(V[1][2]))/d2
    margin=V[2][2]-reaction; assert margin.h<0 and margin.ends()==cert['ceiling_condensed_margin']
    # Independent elimination order, rather than using the producer witness selector.
    p0=V[0][0]; p1=V[1][1]-n.sq(V[0][1])/p0; assert p0.l>0 and p1.l>0
    p2=V[2][2]-n.sq(V[0][2])/p0-n.sq(V[1][2]-V[0][1]*V[0][2]/p0)/p1
    assert p2.h<0; overlap(p2,margin)
    h=list(map(F,cert['universal_fixed_rational_witness'])); assert len(h)==3 and h[2]==1
    value=dot(h,mv(V,h)); assert value.h<0 and value.ends()==cert['universal_witness_ceiling_value']
    a=dot(h,mv(U,h)); b=dot(h,e)
    assert dict(a=a.ends(),b=b.ends(),d=d.ends())==cert['universal_witness_scalar_coefficients']
    # Direct symmetric sum is a separately ordered fixed-witness calculation.
    direct=sum((n.sq(I(h[i]))*U[i][i] for i in range(3)),I(0))
    direct+=sum((2*h[i]*h[j]*U[i][j] for i in range(3) for j in range(i)),I(0)); overlap(a,direct)
    a_upper=F(a.h,n.SCALE); b_upper=max(abs(F(b.l,n.SCALE)),abs(F(b.h,n.SCALE))); minus_d_upper=-F(d.h,n.SCALE)
    upper=a_upper+b_upper*b_upper/minus_d_upper
    assert upper<0 and str(upper)==cert['universal_witness_all_real_functional_upper']
    # Exact rational envelope is a negative constant minus a nonnegative square:
    # aU+2 bU |x|-m x^2 = upper-m (|x|-bU/m)^2.
    assert upper-minus_d_upper*(b_upper/minus_d_upper)**2==a_upper
    assert minus_d_upper>0 and cert['every_real_three_coordinate_functional_floor_rejected']
    lam=list(map(F,cert['selected_rational_functional']))
    assert lam==[F(((x/d).mid()*10**100).__floor__(),10**100) for x in e]
    q,g=p.update(Q,G,beta,qz,zeta,gz,lam)
    assert p.ends(q)==cert['original_selected_native_energy_Gram'] and p.ends(g)==cert['original_selected_complete_source_Gram']
    packet=p.c.parent.sign_packet(q,g,list(map(F,prior['inherited_retained_masses'])))
    assert packet==cert['selected_sign_packet'] and packet['joined_status']=='JOINED_FLOOR_REJECTED'
    selectedU=p.matrix(packet['sufficient_matrix'])
    # Floor-level update provides an independent path to the selected matrix.
    for i in range(3):
        for j in range(3): overlap(selectedU[i][j],U[i][j]-e[i]*lam[j]-lam[i]*e[j]+d*lam[i]*lam[j])
    for w,floor_key,native_key,sign in [
        (h,'universal_witness_selected_floor_value','universal_witness_selected_native_energy',-1),
        (list(map(F,prior['fixed_rational_mixed_floor_witness'])),'NF35_original_mixed_witness_selected_floor_value','NF35_original_mixed_witness_selected_native_energy',1)]:
        floor=dot(w,mv(selectedU,w)); native=dot(w,mv(q,w))
        assert floor.ends()==cert[floor_key] and native.ends()==cert[native_key] and native.l>0
        assert floor.h<0 if sign<0 else floor.l>0
        x=sum((a*b for a,b in zip(lam,w)),F(0)); overlap(floor,dot(w,mv(U,w))-2*dot(w,e)*x+d*x*x)
    assert cert['joined_retained_dimension_certified']==4 and not cert['independent_high_directions_certified']
    for key in ['actual_negative_original_form_claimed','whole_aperture_positive','RH','F4','Lean']: assert not cert[key]
    return dict(parity=cert['parity'],status='ALL_REAL_FUNCTIONALS_FLOOR_REJECTED',
        universal_witness_upper=str(upper),authenticated_complete_source_responses=True,
        independent_LDL_and_scalar_envelope_checked=True,selected_native_energy_positive=True,
        original_mixed_witness_positive_but_universal_witness_negative=True)
def controls():
    rows=[]
    for scale in [F(1),F(1,10**18)]:
        for s in [F(-1,100),F(0),F(1,100)]:
            V=[[F(1),F(1,2),F(1,4)],[F(1,2),F(1),F(-1,4)],[F(1,4),F(-1,4),F(1,4)+s]]
            V=[[scale*v for v in row] for row in V]; e=[scale*F(1,10),-scale*F(1,20),scale*F(1,20)]; d=-scale
            U=[[V[i][j]+e[i]*e[j]/d for j in range(3)] for i in range(3)]
            h=[F(-1,2),F(1,2),F(1)]; a=sum(h[i]*U[i][j]*h[j] for i in range(3) for j in range(3)); b=sum(h[i]*e[i] for i in range(3))
            assert a+b*b/(-d)==scale*s and all(U[i][i]>0 and V[i][i]>0 for i in range(3))
            opt=[v/d for v in e]
            for lam in [[F(0)]*3,opt,[opt[i]+F(i+1,7) for i in range(3)],[F(2),F(-3),F(5)]]:
                C=[[U[i][j]-e[i]*lam[j]-lam[i]*e[j]+d*lam[i]*lam[j] for j in range(3)] for i in range(3)]
                R=[[V[i][j]+d*(lam[i]-e[i]/d)*(lam[j]-e[j]/d) for j in range(3)] for i in range(3)]
                assert C==R
                x=sum(lam[i]*h[i] for i in range(3)); value=sum(h[i]*C[i][j]*h[j] for i in range(3) for j in range(3))
                assert value==a-2*b*x+d*x*x and value<=scale*s
            ci=[[I(v) for v in row] for row in V]; det=p.c.parent.det3(ci)
            assert ci[0][0].l>0 and (ci[0][0]*ci[1][1]-n.sq(ci[0][1])).l>0
            assert det.l==det.h==int(F(3,4)*scale**3*s*n.SCALE)
            if s==0: assert all(sum(V[i][j]*h[j] for j in range(3))==0 for i in range(3))
            rows.append(dict(scale=str(scale),exact_best_witness_value=str(scale*s),
                positive_original_and_ceiling_diagonals=True,completion_square_identity_checked=True,
                exact_positive_null_negative_crossing=True))
    from validate_native_joined_witnesses_nf35_106 import controls as prior_controls
    _,levels=prior_controls()
    return rows,levels
if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('--output',required=True);a=a.parse_args()
    data,old=p.parents(); native,source,hashes=p.c.p.old.prev.inputs(); inherited=[]
    for idx in range(2):
        inherited.append(v36.validate(data[idx],data[idx+2],native,source,hashes,p.SHA36[idx]))
    rows=[]
    for idx,tag in enumerate(['EVEN','ODD']):
        raw=Path('notes/data/RPB108_NF37_'+tag+'_FREE_CORRECTION_FUNCTIONAL_CERTIFICATE_20261009.json').read_bytes()
        row=check(json.loads(raw),idx,data,old);row['certificate_sha256']=hashlib.sha256(raw).hexdigest();rows.append(row)
    crossings,levels=controls()
    out=dict(milestone='NF37',status='PASS',NF36_input_sha256=p.SHA36,parity_checks=rows,
        inherited_NF36_payment_and_candidate_replay=inherited,
        exact_free_functional_crossing_controls=crossings,positive_full_mass_shift_controls=levels,
        joined_retained_dimension_certified=4,every_fixed_NF36_high_polynomial_free_functional_floor_rejected=True,
        actual_negative_original_form_claimed=False,whole_aperture_positive=False)
    Path(a.output).write_text(json.dumps(out,indent=2)+'\n')
