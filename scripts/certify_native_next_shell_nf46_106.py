#!/usr/bin/env python3
"""NF46: eighth even high source on the disjoint degree182..212 shell.

All sign and response statements remain conditional on the original high floor.
Selection midpoints choose only a polynomial, never certify its sign.
"""
import argparse, hashlib, json, sys
from pathlib import Path
from fractions import Fraction as F
sys.set_int_max_str_digits(0)
import certify_native_boundary_response_nf42_106 as r
c=r.c; p=r.p; n=r.n; I=r.I; K=r.K
import certify_native_retained_coupling_nf27_106 as mi

SHA45=['bff2b54764aab1dcd4a1943a3dcd9fb2fd492762abeecb3afaf01f3dce00715b', '4f59c09a453314eae49fcbdf8553f0ce61b1386138d59111c88ab8f752826e4e', '90d03525ee54da02f6e6662460cc18bea2d5740f39f28449de66dea76fa3b5b5', '694204c23b11cfb0af07d26be4a8a0bfe6ab68f8d2e431e2de23390470e28c1c', 'd555f03e507f4b410588bdaa28f851e99ba6aaaf3b85811504e88dccaba12391']
import certify_native_seventh_inverse_source_nf45_106 as prior
def parents():
    prior.parents()
    names=['EVEN_FIXED_INVERSE_WITNESS', 'ODD_FIXED_INVERSE_WITNESS', 'EVEN_INVERSE_WITNESS_CERTIFICATE', 'ODD_INVERSE_WITNESS_CERTIFICATE', 'INVERSE_WITNESS_VALIDATION']
    raw=[Path('notes/data/RPB108_NF45_'+x+'_20261009.json').read_bytes() for x in names]
    assert [hashlib.sha256(v).hexdigest() for v in raw]==SHA45
    out=list(map(json.loads,raw));assert out[4]['status']=='PASS'
    assert out[3]['conditional_joined_sign_certified']
    return out

def block(A,B,C,D): return [a+b for a,b in zip(A,B)]+[a+b for a,b in zip(C,D)]
def symmetry(A):
    for i in range(len(A)):
        for j in range(i):
            lo=max(A[i][j].l,A[j][i].l);hi=min(A[i][j].h,A[j][i].h);assert lo<=hi
            A[i][j]=A[j][i]=I.raw(lo,hi)
    return A
def square(x):return sum(v*v for v in x)
def ceilnorm(x):return p.p.norm(x)
def packet(idx):
    assert idx==0,'NF46 advances only the unresolved even packet'
    d=parents();trial=d[idx];cert=d[idx+2]
    o,H,_,_,_,_,_,Q,G,_,hashes=prior.packet(idx)
    H=H+[(trial['selection_indices'],list(map(F,trial['fixed_rational_seventh_high_coefficients']))) ]
    matrices=[p.prev.matrix(cert[k]) for k in ['seven_high_physical_Gram','seven_high_native_Gram','seven_high_complete_source_Gram','joined_seven_high_native_crosses','joined_seven_high_source_crosses']]
    return (o,H,*matrices,Q,G,cert,hashes)

def high_projection_data(idx,o,old):
    lowH,eh=prior.high_projection_data(idx,o,prior.parents()[idx+2])
    co=dict(zip(old['reconstructed_seventh_source_coordinates_indices'],map(p.iv,old['reconstructed_seventh_source_coordinates'])))
    lowH.append([co[j] for j in o['ids']]);eh.append(F(old['seventh_projected_source_error_upper']))
    return lowH,eh


def inverse_packet(M,QH,GH,B,S,G):
    C=symmetry(c.add(QH,c.scale(M,-K)));CI,cp=mi.inverse(C)
    T=symmetry(c.add(c.add(GH,c.scale(QH,-2*K)),c.scale(M,K*K)))
    W=c.add(S,c.scale(B,-K));N=symmetry(c.add(C,c.scale(T,1/K)));NI,np=mi.inverse(N)
    reaction=symmetry(c.add(c.scale(G,1/K),c.scale(c.mm(c.mm(W,NI),c.tr(W)),-1/(K*K))))
    return C,T,W,N,NI,reaction,cp,np

def choose(parity):
    assert parity=='even';idx=0;o,H,M,QH,GH,B,S,Q,G,old,hashes=packet(idx)
    C,T,W,N,NI,reaction,cp,np=inverse_packet(M,QH,GH,B,S,G)
    h=list(map(F,old['updated_frozen_rational_witness']));alpha=p.mv(NI,p.mv(c.tr(W),h))
    n.product=r.packed_product;m=p.p.old.probe.Moments(1100,parity);shell=list(range(182,213,2))
    ii,cc=p.c.merge(o['columns'],h);target=m.source(ii,cc);fun=p.p.functional(m,target,212);e=m.eta*ceilnorm(cc)
    coords=[p.dot(n.basis(j),fun)+I(-e,e) for j in shell];action=[]
    for a,(ii,cc) in enumerate(H):
        source=m.source(ii,cc);fun=p.p.functional(m,source,212);e=m.eta*ceilnorm(cc)
        action.append([p.dot(n.basis(j),fun)+I(-e,e) for j in shell])
        print('even NF46 next-shell original action reconstructed',a,flush=True)
    assert all(max(ii)<182 for ii,cc in H)
    q=[coords[k]/K-sum((alpha[a]*action[a][k] for a in range(7)),I(0))/(K*K) for k in range(len(shell))]
    raw=[F((v.mid()*10**100).__floor__(),10**100) for v in q];norm=ceilnorm(raw);assert norm>0;y=[v/norm for v in raw]
    assert F(99,100)<square(y)<=1
    capture=sum((n.sq(v) for v in q),I(0));assert capture.l>0
    print('even eighth next-shell polynomial frozen; inverse witness shell square',float(F(capture.l,n.SCALE)),flush=True)
    return dict(milestone='NF46',parity=parity,aperture='53/50',NF45_input_sha256=SHA45,native_input_sha256=hashes,
        frozen_NF45_witness=list(map(str,h)),seven_high_columns=[dict(indices=ii,coefficients=list(map(str,cc))) for ii,cc in H],
        inverse_packet_surplus_positive_proof=cp,inverse_packet_denominator_positive_proof=np,
        inverse_witness_high_coefficients=[v.ends() for v in alpha],selection_indices=shell,
        original_inverse_witness_selection_coordinates=[v.ends() for v in q],rounded_selection_coordinates=list(map(str,raw)),normalizing_rational_upper=str(norm),
        fixed_rational_eighth_high_coefficients=list(map(str,y)),exact_eighth_physical_mass_squared=str(square(y)),
        exact_physical_crosses_with_seven_high_directions=['0']*7,projected_inverse_witness_shell_square=capture.ends(),
        selection_rule='q=A4^-1 R h at updated NF45 even witness; degrees182..212 disjoint from all seven old physical columns; midpoint down-round10^100 and rational upper-norm normalization',
        selection_is_not_a_sign_certificate=True)

def certify(trial):
    parity=trial['parity'];idx=['even','odd'].index(parity);o,H,M,QH,GH,B,S,Q,G,old,hashes=packet(idx)
    assert trial['NF45_input_sha256']==SHA45 and trial['native_input_sha256']==hashes
    ids=trial['selection_indices'];y=list(map(F,trial['fixed_rational_eighth_high_coefficients']));assert ids==list(range(182,213,2))
    assert square(y)==F(trial['exact_eighth_physical_mass_squared'])
    ydict=dict(zip(ids,y));assert all(sum(v*ydict.get(j,F(0)) for j,v in zip(ii,cc))==0 for ii,cc in H)
    n.product=r.packed_product;m=p.p.old.probe.Moments(1100,parity);sy=m.source(ids,y);norm=ceilnorm(y);err=m.eta*norm
    fun=p.p.functional(m,sy,212);coords={j:p.dot(n.basis(j),fun) for j in range(0,213,2)}
    qyhat=p.dot(y,[coords[j] for j in ids]);qy=qyhat+I(-err*norm,err*norm)
    qcross=[];reverse=[];rawsources=[]
    allcols=H+o['columns']
    for ii,cc in allcols:
        val=p.dot(cc,[coords[j] for j in ii]);pay=err*ceilnorm(cc);qcross.append(val+I(-pay,pay))
        s=m.source(ii,cc);rawsources.append(s);print(parity,'NF46 covariance source reconstructed',len(rawsources)-1,flush=True);rev=m.pair(s,sy[0]);ep=m.eta*ceilnorm(cc)*norm;rev=rev+I(-ep,ep)
        assert max(rev.l,qcross[-1].l)<=min(rev.h,qcross[-1].h);reverse.append(rev)
    low=[coords[j] for j in o['ids']];ry=r.projection(sy,low,o['ids']);ey=err+8*max(F(v.h-v.l,2*n.SCALE) for v in low)
    gyhat=m.gram(ry,ry);ny=r.normupper(gyhat);gypay=2*ey*ny+ey*ey;gy=gyhat+I(-gypay,gypay)
    print(parity,'eighth native energy and complete projected source square certified',flush=True)
    # Existing original source errors, scaled with the normalized old columns.
    lowH,eh=high_projection_data(idx,o,old)
    targets=[r.projection(s,lo,o['ids']) for s,lo in zip(rawsources,lowH+o['low'])]
    errors=eh+o['physical_source_errors'];norms=[r.normupper(GH[j][j])+eh[j] for j in range(7)]+[r.normupper(G[j][j])+o['physical_source_errors'][j] for j in range(3)]
    ghats=[];gpay=[];gcross=[]
    for j,(target,ej,nj) in enumerate(zip(targets,errors,norms)):
        val=m.gram(ry,target);pay=ey*nj+ej*ny+ey*ej;ghats.append(val);gpay.append(pay);gcross.append(val+I(-pay,pay))
        print(parity,'eighth complete signed source covariance',j,flush=True)
    def extend(A,cross,last):return [row+[v] for row,v in zip(A,cross)]+[cross+[last]]
    M8=extend(M,[I(0)]*7,I(square(y)));Q8=extend(QH,qcross[:7],qy);G8=extend(GH,gcross[:7],gy)
    B8=[row+[qcross[7+j]] for j,row in enumerate(B)];S8=[row+[gcross[7+j]] for j,row in enumerate(S)]
    C7,T7,W7,N7,NI7,reaction7,_,_=inverse_packet(M,QH,GH,B,S,G)
    C8,T8,W8,N8,NI8,reaction8,cp,np=inverse_packet(M8,Q8,G8,B8,S8,G)
    CI7,_=mi.inverse(C7);defect=qy-K*square(y)-p.dot(qcross[:7],p.mv(CI7,qcross[:7]));assert defect.l>0
    improvement=symmetry(c.add(reaction7,c.scale(reaction8,-1)));lower=symmetry(c.add(Q,c.scale(reaction8,-1)))
    h=list(map(F,old['updated_frozen_rational_witness']));value=p.dot(h,p.mv(improvement,h));witness=p.dot(h,p.mv(lower,h))
    leading=lower[0][0]*lower[1][1]-n.sq(lower[0][1]);assert lower[0][0].l>0 and leading.l>0
    margin=lower[2][2]-(lower[1][1]*n.sq(lower[0][2])-2*lower[0][1]*lower[0][2]*lower[1][2]+lower[0][0]*n.sq(lower[1][2]))/leading
    det=p.c.parent.det3(lower);passed=margin.l>0 and det.l>0;failed=margin.h<0 and det.h<0
    print(parity,'new improvement',[float(F(v)) for v in value.ends()],'new margin',[float(F(v)) for v in margin.ends()],flush=True)
    return dict(milestone='NF46',parity=parity,aperture='53/50',NF45_input_sha256=SHA45,native_input_sha256=hashes,
        reconstructed_eighth_source_coordinates_indices=list(coords),reconstructed_eighth_source_coordinates=[v.ends() for v in coords.values()],
        eighth_source_analytic_error_upper=str(err),eighth_projected_source_error_upper=str(ey),eighth_approximant_norm_upper=str(ny),
        reconstructed_eighth_native_energy=qyhat.ends(),original_eighth_native_energy=qy.ends(),original_eighth_native_crosses=[v.ends() for v in qcross],reverse_eighth_native_crosses=[v.ends() for v in reverse],
        reconstructed_eighth_projected_source_square=gyhat.ends(),eighth_source_square_payment=str(gypay),original_eighth_projected_source_square=gy.ends(),
        reconstructed_eighth_source_crosses=[v.ends() for v in ghats],eighth_source_cross_payments=list(map(str,gpay)),original_eighth_source_crosses=[v.ends() for v in gcross],
        eight_high_physical_Gram=p.prev.ends(M8),eight_high_native_Gram=p.prev.ends(Q8),eight_high_complete_source_Gram=p.prev.ends(G8),
        joined_eight_high_native_crosses=p.prev.ends(B8),joined_eight_high_source_crosses=p.prev.ends(S8),
        eighth_native_defect_after_seven_high_minorant=defect.ends(),eight_high_surplus_positive_proof=cp,eight_high_inverse_denominator_positive_proof=np,
        conditional_eight_high_joined_inverse_upper_matrix=p.prev.ends(reaction8),conditional_extra_joined_inverse_improvement=p.prev.ends(improvement),conditional_eight_high_joined_Schur_lower_matrix=p.prev.ends(lower),
        frozen_NF45_witness=list(map(str,h)),conditional_extra_frozen_witness_improvement=value.ends(),conditional_frozen_witness_value=witness.ends(),
        conditional_joined_condensed_margin=margin.ends(),conditional_joined_determinant=det.ends(),conditional_joined_sign_certified=passed,eight_high_minorant_fails_to_certify=failed,
        background_floor_hypothesis='A >= (207/1000) I on the original remaining high space',background_floor_newly_proved=False,
        actual_negative_original_form_claimed=False,whole_aperture_positive=False,highest_certified_whole_aperture='21/20',RH=False,F4=False,Lean=False)

def finish(cert):
    lower=p.prev.matrix(cert['conditional_eight_high_joined_Schur_lower_matrix'])
    h=p.prev.witness(lower);value=p.dot(h,p.mv(lower,h))
    if cert['eight_high_minorant_fails_to_certify']:assert value.h<0
    cert.update(updated_frozen_rational_witness=list(map(str,h)),updated_witness_lower_certificate_value=value.ends(),necessary_further_updated_witness_response_strict_lower=str(-F(value.h,n.SCALE) if value.h<0 else F(0)))
    return cert

if __name__=='__main__':
    q=argparse.ArgumentParser();q.add_argument('mode',choices=['choose','certify']);q.add_argument('--parity',choices=['even']);q.add_argument('--trial');q.add_argument('--output',required=True);q=q.parse_args()
    if q.mode=='choose':out=choose(q.parity)
    else:
        raw=Path(q.trial).read_bytes();out=certify(json.loads(raw));out['fixed_trial_sha256']=hashlib.sha256(raw).hexdigest();finish(out)
    Path(q.output).write_text(json.dumps(out,indent=2)+'\n')
