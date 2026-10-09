#!/usr/bin/env python3
"""NF43: freeze a fifth high polynomial from the NF42 inverse witness.

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
SHA42=['e58c3ea1160fc1c632d50c6d61d7f1595919ed0707bb77a1109662b6830d50c4','24655cd64c0bf8b6b7b9dce654ff10ad3085eb3b56879bc123873cde54df1d9f']

def parents():
    r.parents()
    raw=[Path('notes/data/RPB108_NF42_'+s+'_BOUNDARY_RESPONSE_CERTIFICATE_20261009.json').read_bytes() for s in ['EVEN','ODD']]
    assert [hashlib.sha256(v).hexdigest() for v in raw]==SHA42
    return list(map(json.loads,raw))

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
    parity=['even','odd'][idx];cert42=parents()[idx];data,source,hashes=p.p.old.prev.inputs()
    o=p.objects(data,source,parity);d38,old=c.parents();trial=d38[idx];par=d38[idx+2]
    a,ids,X,P,QY,DY,_,_,Pi,QYi,_=r.b.inputs(idx)
    zs=[list(map(F,trial[k])) for k in ['old_correction_coefficients','fixed_rational_second_correction_coefficients']]
    shell=trial['correction_indices'];H=[(shell,z) for z in zs]+[([y],[F(1)]) for y in ids]
    scales=[ceilnorm(z) for z in zs]+[F(1),F(1)]
    H=[(ii,[v/d for v in cc]) for (ii,cc),d in zip(H,scales)]
    M=block(r.f.im(a['M']),c.tr(r.f.im(X)),r.f.im(X),r.f.im(r.b.eye(2)))
    QZ=p.prev.matrix(par['joint_native_high_block']);GZ=p.prev.matrix(par['joint_complete_source_high_block'])
    QH=block(QZ,c.tr(c.add(Pi,c.scale(r.f.im(X),K))),c.add(Pi,c.scale(r.f.im(X),K)),QYi)
    GH=block(GZ,c.tr(p.prev.matrix(cert42['original_boundary_old_high_source_crosses'])),p.prev.matrix(cert42['original_boundary_old_high_source_crosses']),p.prev.matrix(cert42['original_boundary_source_Gram']))
    B=[x+y for x,y in zip(p.prev.matrix(par['joint_native_joined_high_crosses']),c.tr(p.prev.matrix(r.parents()[idx]['original_signed_boundary_source_crosses'])))]
    S=[x+y for x,y in zip(p.prev.matrix(par['joint_complete_source_joined_high_crosses']),c.tr(p.prev.matrix(cert42['original_boundary_joined_source_crosses'])))]
    for A in [M,QH,GH]:
        for i in range(4):
            for j in range(4): A[i][j]=A[i][j]/(scales[i]*scales[j])
    for A in [B,S]:
        for row in A:
            for j in range(4):row[j]=row[j]/scales[j]
    Q=p.prev.matrix(old[idx]['original_selected_native_energy_Gram']);G=p.prev.matrix(old[idx]['original_selected_complete_source_Gram'])
    return o,H,M,QH,GH,B,S,Q,G,cert42,hashes

def inverse_packet(M,QH,GH,B,S,G):
    C=symmetry(c.add(QH,c.scale(M,-K)));CI,cp=mi.inverse(C)
    T=symmetry(c.add(c.add(GH,c.scale(QH,-2*K)),c.scale(M,K*K)))
    W=c.add(S,c.scale(B,-K));N=symmetry(c.add(C,c.scale(T,1/K)));NI,np=mi.inverse(N)
    reaction=symmetry(c.add(c.scale(G,1/K),c.scale(c.mm(c.mm(W,NI),c.tr(W)),-1/(K*K))))
    return C,T,W,N,NI,reaction,cp,np

def choose(parity):
    idx=['even','odd'].index(parity);o,H,M,QH,GH,B,S,Q,G,cert42,hashes=packet(idx)
    C,T,W,N,NI,reaction,cp,np=inverse_packet(M,QH,GH,B,S,G)
    h=list(map(F,cert42['frozen_NF38_witness']));alpha=p.mv(NI,p.mv(c.tr(W),h))
    n.product=r.packed_product;m=p.p.old.probe.Moments(1020,parity)
    # Reconstruct the source of R h and all four physical high source columns.
    ii,cc=p.c.merge(o['columns'],h);target=m.source(ii,cc)
    shell=list(range(116+idx,181 if idx==0 else 180,2))
    tf=p.p.functional(m,target,180);coords=[p.dot(n.basis(j),tf) for j in shell]
    te=m.eta*ceilnorm(cc);coords=[v+I(-te,te) for v in coords]
    action=[];errors=[]
    for ids,vs in H:
        s=m.source(ids,vs);fun=p.p.functional(m,s,180);e=m.eta*ceilnorm(vs)
        action.append([p.dot(n.basis(j),fun)+I(-e,e) for j in shell]);errors.append(e)
    vectors=[dict(zip(ids,vs)) for ids,vs in H]
    q=[coords[k]/K-sum((alpha[a]*(action[a][k]-K*vectors[a].get(j,F(0))) for a in range(4)),I(0))/(K*K) for k,j in enumerate(shell)]
    raw=[F((v.mid()*10**100).__floor__(),10**100) for v in q]
    # Boundary coordinates are zero. Project off the two truncated old directions.
    tails=[[vectors[a].get(j,F(0)) for j in shell] for a in range(2)]
    mass=[[c.dot(v,w) for w in tails] for v in tails];inv=c.inverse2(mass)
    ell=c.mv(inv,[c.dot(t,raw) for t in tails]);y=[v-sum(ell[a]*tails[a][k] for a in range(2)) for k,v in enumerate(raw)]
    norm=ceilnorm(y);assert norm>0;y=[v/norm for v in y]
    assert all(c.dot(t,y)==0 for t in tails)
    assert F(99,100)<square(y)<=1
    paidproj=[q[k]-sum((p.dot([I(v) for v in inv[a]],[p.dot(t,q) for t in tails])*tails[a][k] for a in range(2)),I(0)) for k in range(len(q))]
    capture=sum((n.sq(v) for v in paidproj),I(0));assert capture.l>0
    print(parity,'fifth high polynomial frozen; projected inverse witness square',float(F(capture.l,n.SCALE)),flush=True)
    return dict(milestone='NF43',parity=parity,aperture='53/50',NF42_input_sha256=SHA42,native_input_sha256=hashes,
        frozen_NF38_witness=list(map(str,h)),four_high_columns=[dict(indices=ii,coefficients=list(map(str,cc))) for ii,cc in H],
        inverse_packet_surplus_positive_proof=cp,inverse_packet_denominator_positive_proof=np,
        inverse_witness_high_coefficients=[v.ends() for v in alpha],selection_indices=shell,
        original_inverse_witness_selection_coordinates=[v.ends() for v in q],rounded_selection_coordinates=list(map(str,raw)),
        exact_old_tail_Gram=c.strings(mass),exact_projection_coefficients=list(map(str,ell)),normalizing_rational_upper=str(norm),
        fixed_rational_fifth_high_coefficients=list(map(str,y)),exact_fifth_physical_mass_squared=str(square(y)),
        exact_physical_crosses_with_four_high_directions=['0']*4,projected_inverse_witness_shell_square=capture.ends(),
        selection_rule='q=A1^-1 R h via original NF42 four-column Woodbury packet; physical degrees116..180/117..179; midpoint down-round10^100, exact projection off old high tails, rational upper-norm normalization',
        selection_is_not_a_sign_certificate=True)

def certify(trial):
    parity=trial['parity'];idx=['even','odd'].index(parity);o,H,M,QH,GH,B,S,Q,G,old,hashes=packet(idx)
    assert trial['NF42_input_sha256']==SHA42 and trial['native_input_sha256']==hashes
    ids=trial['selection_indices'];y=list(map(F,trial['fixed_rational_fifth_high_coefficients']));assert ids==list(range(116+idx,181 if idx==0 else 180,2))
    assert square(y)==F(trial['exact_fifth_physical_mass_squared'])
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
    print(parity,'fifth native energy and complete projected source square certified',flush=True)
    # Existing original source errors, scaled with the normalized old columns.
    d38,_=c.parents();d36=p.prev.parents()[0];pars=[d36[idx+2],d38[idx+2]]
    scales=[ceilnorm(list(map(F,d38[idx][k]))) for k in ['old_correction_coefficients','fixed_rational_second_correction_coefficients']]
    lowH=[];eh=[]
    for a,par in enumerate(pars):
        co=dict(zip(par['correction_source_coordinate_indices'],map(p.iv,par['reconstructed_correction_source_coordinates'])))
        lowH.append([co[j]/scales[a] for j in o['ids']]);eh.append(F(par['correction_source_error_upper'])/scales[a]+8*max(F(v.h-v.l,2*n.SCALE) for v in lowH[-1]))
    lowH+=p.prev.matrix(old['boundary_source_low_projection_intervals']);eh+=list(map(F,old['boundary_source_physical_errors']))
    targets=[r.projection(s,lo,o['ids']) for s,lo in zip(rawsources,lowH+o['low'])]
    errors=eh+o['physical_source_errors'];norms=[r.normupper(GH[j][j])+eh[j] for j in range(4)]+[r.normupper(G[j][j])+o['physical_source_errors'][j] for j in range(3)]
    ghats=[];gpay=[];gcross=[]
    for j,(target,ej,nj) in enumerate(zip(targets,errors,norms)):
        val=m.gram(ry,target);pay=ey*nj+ej*ny+ey*ej;ghats.append(val);gpay.append(pay);gcross.append(val+I(-pay,pay))
        print(parity,'fifth complete signed source covariance',j,flush=True)
    def extend(A,cross,last):return [row+[v] for row,v in zip(A,cross)]+[cross+[last]]
    M5=extend(M,[I(0)]*4,I(square(y)));Q5=extend(QH,qcross[:4],qy);G5=extend(GH,gcross[:4],gy)
    B5=[row+[qcross[4+j]] for j,row in enumerate(B)];S5=[row+[gcross[4+j]] for j,row in enumerate(S)]
    C4,T4,W4,N4,NI4,reaction4,_,_=inverse_packet(M,QH,GH,B,S,G)
    C5,T5,W5,N5,NI5,reaction5,cp,np=inverse_packet(M5,Q5,G5,B5,S5,G)
    CI4,_=mi.inverse(C4);defect=qy-K*square(y)-p.dot(qcross[:4],p.mv(CI4,qcross[:4]));assert defect.l>0
    improvement=symmetry(c.add(reaction4,c.scale(reaction5,-1)));lower=symmetry(c.add(Q,c.scale(reaction5,-1)))
    h=list(map(F,old['frozen_NF38_witness']));value=p.dot(h,p.mv(improvement,h));witness=p.dot(h,p.mv(lower,h))
    leading=lower[0][0]*lower[1][1]-n.sq(lower[0][1]);assert lower[0][0].l>0 and leading.l>0
    margin=lower[2][2]-(lower[1][1]*n.sq(lower[0][2])-2*lower[0][1]*lower[0][2]*lower[1][2]+lower[0][0]*n.sq(lower[1][2]))/leading
    det=p.c.parent.det3(lower);passed=margin.l>0 and det.l>0;failed=margin.h<0 and det.h<0
    print(parity,'new improvement',[float(F(v)) for v in value.ends()],'new margin',[float(F(v)) for v in margin.ends()],flush=True)
    return dict(milestone='NF43',parity=parity,aperture='53/50',NF42_input_sha256=SHA42,native_input_sha256=hashes,
        reconstructed_fifth_source_coordinates_indices=list(coords),reconstructed_fifth_source_coordinates=[v.ends() for v in coords.values()],
        fifth_source_analytic_error_upper=str(err),fifth_projected_source_error_upper=str(ey),fifth_approximant_norm_upper=str(ny),
        reconstructed_fifth_native_energy=qyhat.ends(),original_fifth_native_energy=qy.ends(),original_fifth_native_crosses=[v.ends() for v in qcross],reverse_fifth_native_crosses=[v.ends() for v in reverse],
        reconstructed_fifth_projected_source_square=gyhat.ends(),fifth_source_square_payment=str(gypay),original_fifth_projected_source_square=gy.ends(),
        reconstructed_fifth_source_crosses=[v.ends() for v in ghats],fifth_source_cross_payments=list(map(str,gpay)),original_fifth_source_crosses=[v.ends() for v in gcross],
        five_high_physical_Gram=p.prev.ends(M5),five_high_native_Gram=p.prev.ends(Q5),five_high_complete_source_Gram=p.prev.ends(G5),
        joined_five_high_native_crosses=p.prev.ends(B5),joined_five_high_source_crosses=p.prev.ends(S5),
        fifth_native_defect_after_four_high_minorant=defect.ends(),five_high_surplus_positive_proof=cp,five_high_inverse_denominator_positive_proof=np,
        conditional_five_high_joined_inverse_upper_matrix=p.prev.ends(reaction5),conditional_extra_joined_inverse_improvement=p.prev.ends(improvement),conditional_five_high_joined_Schur_lower_matrix=p.prev.ends(lower),
        frozen_NF38_witness=list(map(str,h)),conditional_extra_frozen_witness_improvement=value.ends(),conditional_frozen_witness_value=witness.ends(),
        conditional_joined_condensed_margin=margin.ends(),conditional_joined_determinant=det.ends(),conditional_joined_sign_certified=passed,five_high_minorant_fails_to_certify=failed,
        background_floor_hypothesis='A >= (207/1000) I on the original remaining high space',background_floor_newly_proved=False,
        actual_negative_original_form_claimed=False,whole_aperture_positive=False,highest_certified_whole_aperture='21/20',RH=False,F4=False,Lean=False)

def finish(cert):
    lower=p.prev.matrix(cert['conditional_five_high_joined_Schur_lower_matrix'])
    h=p.prev.witness(lower);value=p.dot(h,p.mv(lower,h))
    if cert['five_high_minorant_fails_to_certify']:assert value.h<0
    cert.update(updated_frozen_rational_witness=list(map(str,h)),updated_witness_lower_certificate_value=value.ends(),necessary_further_updated_witness_response_strict_lower=str(-F(value.h,n.SCALE) if value.h<0 else F(0)))
    return cert

if __name__=='__main__':
    q=argparse.ArgumentParser();q.add_argument('mode',choices=['choose','certify']);q.add_argument('--parity',choices=['even','odd']);q.add_argument('--trial');q.add_argument('--output',required=True);q=q.parse_args()
    if q.mode=='choose':out=choose(q.parity)
    else:
        raw=Path(q.trial).read_bytes();out=certify(json.loads(raw));out['fixed_trial_sha256']=hashlib.sha256(raw).hexdigest();finish(out)
    Path(q.output).write_text(json.dumps(out,indent=2)+'\n')
