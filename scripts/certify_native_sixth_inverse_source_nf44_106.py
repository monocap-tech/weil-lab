#!/usr/bin/env python3
"""NF44: freeze a sixth high polynomial from the updated NF43 inverse witness.

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

SHA43=['8e3bdd803c3c3a9423ed702bebf52618be2b58f41263f549622d1a3dcbdf94ce','0707a00966313144f38482564573ee978d12bd17d2cd8326f58cb0c021d0d66d','d46a4f1d52dc208b409a2de057283934b4a1d1808209a3068c59c38cad5502fe','6f649ec13a3795ba24b28ab7aa0a89f7d4c7eafae15d7433bcd6906d1fa76ac7','19d4d98fdc7a076450828380705fc3e7e618013bbc053c55e6496a6a895eb206']
import certify_native_inverse_witness_nf43_106 as prior
from functools import cache
n.kernel.kernel_coefficients=cache(n.kernel.kernel_coefficients)
def parents():
    prior.parents()
    names=['EVEN_FIXED_INVERSE_WITNESS','ODD_FIXED_INVERSE_WITNESS','EVEN_INVERSE_WITNESS_CERTIFICATE','ODD_INVERSE_WITNESS_CERTIFICATE','INVERSE_WITNESS_VALIDATION']
    raw=[Path('notes/data/RPB108_NF43_'+x+'_20261009.json').read_bytes() for x in names]
    assert [hashlib.sha256(v).hexdigest() for v in raw]==SHA43
    out=list(map(json.loads,raw));assert out[4]['status']=='PASS'
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
    d=parents();trial=d[idx];cert=d[idx+2]
    o,H,_,_,_,_,_,Q,G,_,hashes=prior.packet(idx)
    H=H+[(trial['selection_indices'],list(map(F,trial['fixed_rational_fifth_high_coefficients']))) ]
    matrices=[p.prev.matrix(cert[k]) for k in ['five_high_physical_Gram','five_high_native_Gram','five_high_complete_source_Gram','joined_five_high_native_crosses','joined_five_high_source_crosses']]
    return (o,H,*matrices,Q,G,cert,hashes)

def high_projection_data(idx,o,old):
    d38,_=c.parents();d36=p.prev.parents()[0];pars=[d36[idx+2],d38[idx+2]]
    scales=[ceilnorm(list(map(F,d38[idx][k]))) for k in ['old_correction_coefficients','fixed_rational_second_correction_coefficients']]
    lowH=[];eh=[]
    for a,par in enumerate(pars):
        co=dict(zip(par['correction_source_coordinate_indices'],map(p.iv,par['reconstructed_correction_source_coordinates'])))
        lowH.append([co[j]/scales[a] for j in o['ids']]);eh.append(F(par['correction_source_error_upper'])/scales[a]+8*max(F(v.h-v.l,2*n.SCALE) for v in lowH[-1]))
    cert42=prior.parents()[idx]
    lowH+=p.prev.matrix(cert42['boundary_source_low_projection_intervals']);eh+=list(map(F,cert42['boundary_source_physical_errors']))
    co=dict(zip(old['reconstructed_fifth_source_coordinates_indices'],map(p.iv,old['reconstructed_fifth_source_coordinates'])))
    lowH.append([co[j] for j in o['ids']]);eh.append(F(old['fifth_projected_source_error_upper']))
    return lowH,eh

def inverse_packet(M,QH,GH,B,S,G):
    C=symmetry(c.add(QH,c.scale(M,-K)));CI,cp=mi.inverse(C)
    T=symmetry(c.add(c.add(GH,c.scale(QH,-2*K)),c.scale(M,K*K)))
    W=c.add(S,c.scale(B,-K));N=symmetry(c.add(C,c.scale(T,1/K)));NI,np=mi.inverse(N)
    reaction=symmetry(c.add(c.scale(G,1/K),c.scale(c.mm(c.mm(W,NI),c.tr(W)),-1/(K*K))))
    return C,T,W,N,NI,reaction,cp,np

def choose(parity):
    idx=['even','odd'].index(parity);o,H,M,QH,GH,B,S,Q,G,cert43,hashes=packet(idx)
    C,T,W,N,NI,reaction,cp,np=inverse_packet(M,QH,GH,B,S,G)
    h=list(map(F,cert43['updated_frozen_rational_witness']));alpha=p.mv(NI,p.mv(c.tr(W),h))
    n.product=r.packed_product;m=p.p.old.probe.Moments(1020,parity)
    # Reconstruct the source of R h and all five physical high source columns.
    ii,cc=p.c.merge(o['columns'],h);target=m.source(ii,cc)
    shell=list(range(116+idx,181 if idx==0 else 180,2))
    tf=p.p.functional(m,target,180);coords=[p.dot(n.basis(j),tf) for j in shell]
    te=m.eta*ceilnorm(cc);coords=[v+I(-te,te) for v in coords]
    action=[];errors=[]
    for ids,vs in H:
        s=m.source(ids,vs);fun=p.p.functional(m,s,180);e=m.eta*ceilnorm(vs)
        action.append([p.dot(n.basis(j),fun)+I(-e,e) for j in shell]);errors.append(e)
    vectors=[dict(zip(ids,vs)) for ids,vs in H]
    q=[coords[k]/K-sum((alpha[a]*(action[a][k]-K*vectors[a].get(j,F(0))) for a in range(5)),I(0))/(K*K) for k,j in enumerate(shell)]
    raw=[F((v.mid()*10**100).__floor__(),10**100) for v in q]
    # Boundary coordinates are zero. Project off the three truncated tail directions.
    tails=[[vectors[a].get(j,F(0)) for j in shell] for a in [0,1,4]]
    mass=[[c.dot(v,w) for w in tails] for v in tails];inv=r.b.inverse(mass)
    ell=c.mv(inv,[c.dot(t,raw) for t in tails]);y=[v-sum(ell[a]*tails[a][k] for a in range(3)) for k,v in enumerate(raw)]
    norm=ceilnorm(y);assert norm>0;y=[v/norm for v in y]
    assert all(c.dot(t,y)==0 for t in tails)
    assert F(99,100)<square(y)<=1
    paidproj=[q[k]-sum((p.dot([I(v) for v in inv[a]],[p.dot(t,q) for t in tails])*tails[a][k] for a in range(3)),I(0)) for k in range(len(q))]
    capture=sum((n.sq(v) for v in paidproj),I(0));assert capture.l>0
    print(parity,'sixth high polynomial frozen; projected inverse witness square',float(F(capture.l,n.SCALE)),flush=True)
    return dict(milestone='NF44',parity=parity,aperture='53/50',NF43_input_sha256=SHA43,native_input_sha256=hashes,
        frozen_NF43_witness=list(map(str,h)),five_high_columns=[dict(indices=ii,coefficients=list(map(str,cc))) for ii,cc in H],
        inverse_packet_surplus_positive_proof=cp,inverse_packet_denominator_positive_proof=np,
        inverse_witness_high_coefficients=[v.ends() for v in alpha],selection_indices=shell,
        original_inverse_witness_selection_coordinates=[v.ends() for v in q],rounded_selection_coordinates=list(map(str,raw)),
        exact_old_tail_Gram=c.strings(mass),exact_projection_coefficients=list(map(str,ell)),normalizing_rational_upper=str(norm),
        fixed_rational_sixth_high_coefficients=list(map(str,y)),exact_sixth_physical_mass_squared=str(square(y)),
        exact_physical_crosses_with_five_high_directions=['0']*5,projected_inverse_witness_shell_square=capture.ends(),
        selection_rule='q=A2^-1 R h via original NF43 five-column Woodbury packet; physical degrees116..180/117..179; midpoint down-round10^100, exact projection off old two tails and fifth tail, rational upper-norm normalization',
        selection_is_not_a_sign_certificate=True)

def certify(trial):
    parity=trial['parity'];idx=['even','odd'].index(parity);o,H,M,QH,GH,B,S,Q,G,old,hashes=packet(idx)
    assert trial['NF43_input_sha256']==SHA43 and trial['native_input_sha256']==hashes
    ids=trial['selection_indices'];y=list(map(F,trial['fixed_rational_sixth_high_coefficients']));assert ids==list(range(116+idx,181 if idx==0 else 180,2))
    assert square(y)==F(trial['exact_sixth_physical_mass_squared'])
    ydict=dict(zip(ids,y));assert all(sum(v*ydict.get(j,F(0)) for j,v in zip(ii,cc))==0 for ii,cc in H)
    n.product=r.packed_product;m=p.p.old.probe.Moments(1020,parity);sy=m.source(ids,y);norm=ceilnorm(y);err=m.eta*norm
    fun=p.p.functional(m,sy,180);coords={j:p.dot(n.basis(j),fun) for j in range(idx,181 if idx==0 else 180,2)}
    qyhat=p.dot(y,[coords[j] for j in ids]);qy=qyhat+I(-err*norm,err*norm)
    qcross=[];reverse=[];rawsources=[]
    allcols=H+o['columns']
    for ii,cc in allcols:
        val=p.dot(cc,[coords[j] for j in ii]);pay=err*ceilnorm(cc);qcross.append(val+I(-pay,pay))
        s=m.source(ii,cc);rawsources.append(s);rev=m.pair(s,sy[0]);ep=m.eta*ceilnorm(cc)*norm;rev=rev+I(-ep,ep)
        assert max(rev.l,qcross[-1].l)<=min(rev.h,qcross[-1].h);reverse.append(rev)
    low=[coords[j] for j in o['ids']];ry=r.projection(sy,low,o['ids']);ey=err+8*max(F(v.h-v.l,2*n.SCALE) for v in low)
    gyhat=m.gram(ry,ry);ny=r.normupper(gyhat);gypay=2*ey*ny+ey*ey;gy=gyhat+I(-gypay,gypay)
    print(parity,'sixth native energy and complete projected source square certified',flush=True)
    # Existing original source errors, scaled with the normalized old columns.
    lowH,eh=high_projection_data(idx,o,old)
    targets=[r.projection(s,lo,o['ids']) for s,lo in zip(rawsources,lowH+o['low'])]
    errors=eh+o['physical_source_errors'];norms=[r.normupper(GH[j][j])+eh[j] for j in range(5)]+[r.normupper(G[j][j])+o['physical_source_errors'][j] for j in range(3)]
    ghats=[];gpay=[];gcross=[]
    for j,(target,ej,nj) in enumerate(zip(targets,errors,norms)):
        val=m.gram(ry,target);pay=ey*nj+ej*ny+ey*ej;ghats.append(val);gpay.append(pay);gcross.append(val+I(-pay,pay))
        print(parity,'sixth complete signed source covariance',j,flush=True)
    def extend(A,cross,last):return [row+[v] for row,v in zip(A,cross)]+[cross+[last]]
    M6=extend(M,[I(0)]*5,I(square(y)));Q6=extend(QH,qcross[:5],qy);G6=extend(GH,gcross[:5],gy)
    B6=[row+[qcross[5+j]] for j,row in enumerate(B)];S6=[row+[gcross[5+j]] for j,row in enumerate(S)]
    C5,T5,W5,N5,NI5,reaction5,_,_=inverse_packet(M,QH,GH,B,S,G)
    C6,T6,W6,N6,NI6,reaction6,cp,np=inverse_packet(M6,Q6,G6,B6,S6,G)
    CI5,_=mi.inverse(C5);defect=qy-K*square(y)-p.dot(qcross[:5],p.mv(CI5,qcross[:5]));assert defect.l>0
    improvement=symmetry(c.add(reaction5,c.scale(reaction6,-1)));lower=symmetry(c.add(Q,c.scale(reaction6,-1)))
    h=list(map(F,old['updated_frozen_rational_witness']));value=p.dot(h,p.mv(improvement,h));witness=p.dot(h,p.mv(lower,h))
    leading=lower[0][0]*lower[1][1]-n.sq(lower[0][1]);assert lower[0][0].l>0 and leading.l>0
    margin=lower[2][2]-(lower[1][1]*n.sq(lower[0][2])-2*lower[0][1]*lower[0][2]*lower[1][2]+lower[0][0]*n.sq(lower[1][2]))/leading
    det=p.c.parent.det3(lower);passed=margin.l>0 and det.l>0;failed=margin.h<0 and det.h<0
    print(parity,'new improvement',[float(F(v)) for v in value.ends()],'new margin',[float(F(v)) for v in margin.ends()],flush=True)
    return dict(milestone='NF44',parity=parity,aperture='53/50',NF43_input_sha256=SHA43,native_input_sha256=hashes,
        reconstructed_sixth_source_coordinates_indices=list(coords),reconstructed_sixth_source_coordinates=[v.ends() for v in coords.values()],
        sixth_source_analytic_error_upper=str(err),sixth_projected_source_error_upper=str(ey),sixth_approximant_norm_upper=str(ny),
        reconstructed_sixth_native_energy=qyhat.ends(),original_sixth_native_energy=qy.ends(),original_sixth_native_crosses=[v.ends() for v in qcross],reverse_sixth_native_crosses=[v.ends() for v in reverse],
        reconstructed_sixth_projected_source_square=gyhat.ends(),sixth_source_square_payment=str(gypay),original_sixth_projected_source_square=gy.ends(),
        reconstructed_sixth_source_crosses=[v.ends() for v in ghats],sixth_source_cross_payments=list(map(str,gpay)),original_sixth_source_crosses=[v.ends() for v in gcross],
        six_high_physical_Gram=p.prev.ends(M6),six_high_native_Gram=p.prev.ends(Q6),six_high_complete_source_Gram=p.prev.ends(G6),
        joined_six_high_native_crosses=p.prev.ends(B6),joined_six_high_source_crosses=p.prev.ends(S6),
        sixth_native_defect_after_five_high_minorant=defect.ends(),six_high_surplus_positive_proof=cp,six_high_inverse_denominator_positive_proof=np,
        conditional_six_high_joined_inverse_upper_matrix=p.prev.ends(reaction6),conditional_extra_joined_inverse_improvement=p.prev.ends(improvement),conditional_six_high_joined_Schur_lower_matrix=p.prev.ends(lower),
        frozen_NF43_witness=list(map(str,h)),conditional_extra_frozen_witness_improvement=value.ends(),conditional_frozen_witness_value=witness.ends(),
        conditional_joined_condensed_margin=margin.ends(),conditional_joined_determinant=det.ends(),conditional_joined_sign_certified=passed,six_high_minorant_fails_to_certify=failed,
        background_floor_hypothesis='A >= (207/1000) I on the original remaining high space',background_floor_newly_proved=False,
        actual_negative_original_form_claimed=False,whole_aperture_positive=False,highest_certified_whole_aperture='21/20',RH=False,F4=False,Lean=False)

def finish(cert):
    lower=p.prev.matrix(cert['conditional_six_high_joined_Schur_lower_matrix'])
    h=p.prev.witness(lower);value=p.dot(h,p.mv(lower,h))
    if cert['six_high_minorant_fails_to_certify']:assert value.h<0
    cert.update(updated_frozen_rational_witness=list(map(str,h)),updated_witness_lower_certificate_value=value.ends(),necessary_further_updated_witness_response_strict_lower=str(-F(value.h,n.SCALE) if value.h<0 else F(0)))
    return cert

if __name__=='__main__':
    q=argparse.ArgumentParser();q.add_argument('mode',choices=['choose','certify']);q.add_argument('--parity',choices=['even','odd']);q.add_argument('--trial');q.add_argument('--output',required=True);q=q.parse_args()
    if q.mode=='choose':out=choose(q.parity)
    else:
        raw=Path(q.trial).read_bytes();out=certify(json.loads(raw));out['fixed_trial_sha256']=hashlib.sha256(raw).hexdigest();finish(out)
    Path(q.output).write_text(json.dumps(out,indent=2)+'\n')
