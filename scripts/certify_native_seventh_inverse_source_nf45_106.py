#!/usr/bin/env python3
"""NF45: freeze a seventh high polynomial from the updated NF44 inverse witness.

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

SHA44=['d8eb42d7071f6a2c3bc30fe583146fe575035e9fd7a5163789ea3ac59d630d21', '0e684bf3e9edd987cfa5658c13135db92c038df23945e07cb139bfc251aa2e3e', '9a6d58d0b11aa435d32866823beb0f68477b87232bdb99351a91b0cb16521643', '94669181d3d09b682235e4f87b9f623de6a8b55702beedf1cd6330b116d8b5f4', 'ef6cff6db90a4f6683771b4f81ccfefa2b166c2a84a391bff2950b64c84c6e05']
import certify_native_sixth_inverse_source_nf44_106 as prior
def parents():
    prior.parents()
    names=['EVEN_FIXED_INVERSE_WITNESS', 'ODD_FIXED_INVERSE_WITNESS', 'EVEN_INVERSE_WITNESS_CERTIFICATE', 'ODD_INVERSE_WITNESS_CERTIFICATE', 'INVERSE_WITNESS_VALIDATION']
    raw=[Path('notes/data/RPB108_NF44_'+x+'_20261009.json').read_bytes() for x in names]
    assert [hashlib.sha256(v).hexdigest() for v in raw]==SHA44
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
    H=H+[(trial['selection_indices'],list(map(F,trial['fixed_rational_sixth_high_coefficients']))) ]
    matrices=[p.prev.matrix(cert[k]) for k in ['six_high_physical_Gram','six_high_native_Gram','six_high_complete_source_Gram','joined_six_high_native_crosses','joined_six_high_source_crosses']]
    return (o,H,*matrices,Q,G,cert,hashes)

def high_projection_data(idx,o,old):
    lowH,eh=prior.high_projection_data(idx,o,prior.parents()[idx+2])
    co=dict(zip(old['reconstructed_sixth_source_coordinates_indices'],map(p.iv,old['reconstructed_sixth_source_coordinates'])))
    lowH.append([co[j] for j in o['ids']]);eh.append(F(old['sixth_projected_source_error_upper']))
    return lowH,eh


def inverse_packet(M,QH,GH,B,S,G):
    C=symmetry(c.add(QH,c.scale(M,-K)));CI,cp=mi.inverse(C)
    T=symmetry(c.add(c.add(GH,c.scale(QH,-2*K)),c.scale(M,K*K)))
    W=c.add(S,c.scale(B,-K));N=symmetry(c.add(C,c.scale(T,1/K)));NI,np=mi.inverse(N)
    reaction=symmetry(c.add(c.scale(G,1/K),c.scale(c.mm(c.mm(W,NI),c.tr(W)),-1/(K*K))))
    return C,T,W,N,NI,reaction,cp,np

def choose(parity):
    idx=['even','odd'].index(parity);o,H,M,QH,GH,B,S,Q,G,cert44,hashes=packet(idx)
    C,T,W,N,NI,reaction,cp,np=inverse_packet(M,QH,GH,B,S,G)
    h=list(map(F,cert44['updated_frozen_rational_witness']));alpha=p.mv(NI,p.mv(c.tr(W),h))
    n.product=r.packed_product;m=p.p.old.probe.Moments(1020,parity)
    # Reconstruct the source of R h and the original six physical high source columns.
    ii,cc=p.c.merge(o['columns'],h);target=m.source(ii,cc)
    shell=list(range(116+idx,181 if idx==0 else 180,2))
    tf=p.p.functional(m,target,180);coords=[p.dot(n.basis(j),tf) for j in shell]
    te=m.eta*ceilnorm(cc);coords=[v+I(-te,te) for v in coords]
    action=[]
    d38,_=c.parents();d36=p.prev.parents()[0]
    for j,(ids,vs) in enumerate(H):
        if j in [0,1]:
            par=[d36[idx+2],d38[idx+2]][j]
            scale=ceilnorm(list(map(F,d38[idx][['old_correction_coefficients','fixed_rational_second_correction_coefficients'][j]])))
            co=dict(zip(par['correction_source_coordinate_indices'],map(p.iv,par['reconstructed_correction_source_coordinates'])))
            e=F(par['correction_source_error_upper'])/scale
            action.append([co[k]/scale+I(-e,e) for k in shell])
        elif j in [4,5]:
            par=parents()[idx+2] if j==5 else prior.parents()[idx+2]
            label='sixth' if j==5 else 'fifth'
            co=dict(zip(par['reconstructed_'+label+'_source_coordinates_indices'],map(p.iv,par['reconstructed_'+label+'_source_coordinates'])))
            e=F(par[label+'_source_analytic_error_upper'])
            action.append([co[k]+I(-e,e) for k in shell])
        else:
            source=m.source(ids,vs);fun=p.p.functional(m,source,180);e=m.eta*ceilnorm(vs)
            action.append([p.dot(n.basis(k),fun)+I(-e,e) for k in shell])
    vectors=[dict(zip(ids,vs)) for ids,vs in H]
    q=[coords[k]/K-sum((alpha[a]*(action[a][k]-K*vectors[a].get(j,F(0))) for a in range(6)),I(0))/(K*K) for k,j in enumerate(shell)]
    raw=[F((v.mid()*10**100).__floor__(),10**100) for v in q]
    # Boundary coordinates are zero. Project off the four truncated tail directions.
    tails=[[vectors[a].get(j,F(0)) for j in shell] for a in [0,1,4,5]]
    mass=[[c.dot(v,w) for w in tails] for v in tails];inv=r.b.inverse(mass)
    ell=c.mv(inv,[c.dot(t,raw) for t in tails]);y=[v-sum(ell[a]*tails[a][k] for a in range(4)) for k,v in enumerate(raw)]
    norm=ceilnorm(y);assert norm>0;y=[v/norm for v in y]
    assert all(c.dot(t,y)==0 for t in tails)
    assert F(99,100)<square(y)<=1
    paidproj=[q[k]-sum((p.dot([I(v) for v in inv[a]],[p.dot(t,q) for t in tails])*tails[a][k] for a in range(4)),I(0)) for k in range(len(q))]
    capture=sum((n.sq(v) for v in paidproj),I(0));assert capture.l>0
    print(parity,'seventh high polynomial frozen; projected inverse witness square',float(F(capture.l,n.SCALE)),flush=True)
    return dict(milestone='NF45',parity=parity,aperture='53/50',NF44_input_sha256=SHA44,native_input_sha256=hashes,
        frozen_NF44_witness=list(map(str,h)),six_high_columns=[dict(indices=ii,coefficients=list(map(str,cc))) for ii,cc in H],
        inverse_packet_surplus_positive_proof=cp,inverse_packet_denominator_positive_proof=np,
        inverse_witness_high_coefficients=[v.ends() for v in alpha],selection_indices=shell,
        original_inverse_witness_selection_coordinates=[v.ends() for v in q],rounded_selection_coordinates=list(map(str,raw)),
        exact_old_tail_Gram=c.strings(mass),exact_projection_coefficients=list(map(str,ell)),normalizing_rational_upper=str(norm),
        fixed_rational_seventh_high_coefficients=list(map(str,y)),exact_seventh_physical_mass_squared=str(square(y)),
        exact_physical_crosses_with_six_high_directions=['0']*6,projected_inverse_witness_shell_square=capture.ends(),
        selection_rule='q=A3^-1 R h via original NF44 six-column Woodbury packet; physical degrees116..180/117..179; midpoint down-round10^100, exact projection off old two tails, fifth tail and sixth tail, rational upper-norm normalization',
        selection_is_not_a_sign_certificate=True)

def certify(trial):
    parity=trial['parity'];idx=['even','odd'].index(parity);o,H,M,QH,GH,B,S,Q,G,old,hashes=packet(idx)
    assert trial['NF44_input_sha256']==SHA44 and trial['native_input_sha256']==hashes
    ids=trial['selection_indices'];y=list(map(F,trial['fixed_rational_seventh_high_coefficients']));assert ids==list(range(116+idx,181 if idx==0 else 180,2))
    assert square(y)==F(trial['exact_seventh_physical_mass_squared'])
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
    print(parity,'seventh native energy and complete projected source square certified',flush=True)
    # Existing original source errors, scaled with the normalized old columns.
    lowH,eh=high_projection_data(idx,o,old)
    targets=[r.projection(s,lo,o['ids']) for s,lo in zip(rawsources,lowH+o['low'])]
    errors=eh+o['physical_source_errors'];norms=[r.normupper(GH[j][j])+eh[j] for j in range(6)]+[r.normupper(G[j][j])+o['physical_source_errors'][j] for j in range(3)]
    ghats=[];gpay=[];gcross=[]
    for j,(target,ej,nj) in enumerate(zip(targets,errors,norms)):
        val=m.gram(ry,target);pay=ey*nj+ej*ny+ey*ej;ghats.append(val);gpay.append(pay);gcross.append(val+I(-pay,pay))
        print(parity,'seventh complete signed source covariance',j,flush=True)
    def extend(A,cross,last):return [row+[v] for row,v in zip(A,cross)]+[cross+[last]]
    M7=extend(M,[I(0)]*6,I(square(y)));Q7=extend(QH,qcross[:6],qy);G7=extend(GH,gcross[:6],gy)
    B7=[row+[qcross[6+j]] for j,row in enumerate(B)];S7=[row+[gcross[6+j]] for j,row in enumerate(S)]
    C6,T6,W6,N6,NI6,reaction6,_,_=inverse_packet(M,QH,GH,B,S,G)
    C7,T7,W7,N7,NI7,reaction7,cp,np=inverse_packet(M7,Q7,G7,B7,S7,G)
    CI6,_=mi.inverse(C6);defect=qy-K*square(y)-p.dot(qcross[:6],p.mv(CI6,qcross[:6]));assert defect.l>0
    improvement=symmetry(c.add(reaction6,c.scale(reaction7,-1)));lower=symmetry(c.add(Q,c.scale(reaction7,-1)))
    h=list(map(F,old['updated_frozen_rational_witness']));value=p.dot(h,p.mv(improvement,h));witness=p.dot(h,p.mv(lower,h))
    leading=lower[0][0]*lower[1][1]-n.sq(lower[0][1]);assert lower[0][0].l>0 and leading.l>0
    margin=lower[2][2]-(lower[1][1]*n.sq(lower[0][2])-2*lower[0][1]*lower[0][2]*lower[1][2]+lower[0][0]*n.sq(lower[1][2]))/leading
    det=p.c.parent.det3(lower);passed=margin.l>0 and det.l>0;failed=margin.h<0 and det.h<0
    print(parity,'new improvement',[float(F(v)) for v in value.ends()],'new margin',[float(F(v)) for v in margin.ends()],flush=True)
    return dict(milestone='NF45',parity=parity,aperture='53/50',NF44_input_sha256=SHA44,native_input_sha256=hashes,
        reconstructed_seventh_source_coordinates_indices=list(coords),reconstructed_seventh_source_coordinates=[v.ends() for v in coords.values()],
        seventh_source_analytic_error_upper=str(err),seventh_projected_source_error_upper=str(ey),seventh_approximant_norm_upper=str(ny),
        reconstructed_seventh_native_energy=qyhat.ends(),original_seventh_native_energy=qy.ends(),original_seventh_native_crosses=[v.ends() for v in qcross],reverse_seventh_native_crosses=[v.ends() for v in reverse],
        reconstructed_seventh_projected_source_square=gyhat.ends(),seventh_source_square_payment=str(gypay),original_seventh_projected_source_square=gy.ends(),
        reconstructed_seventh_source_crosses=[v.ends() for v in ghats],seventh_source_cross_payments=list(map(str,gpay)),original_seventh_source_crosses=[v.ends() for v in gcross],
        seven_high_physical_Gram=p.prev.ends(M7),seven_high_native_Gram=p.prev.ends(Q7),seven_high_complete_source_Gram=p.prev.ends(G7),
        joined_seven_high_native_crosses=p.prev.ends(B7),joined_seven_high_source_crosses=p.prev.ends(S7),
        seventh_native_defect_after_six_high_minorant=defect.ends(),seven_high_surplus_positive_proof=cp,seven_high_inverse_denominator_positive_proof=np,
        conditional_seven_high_joined_inverse_upper_matrix=p.prev.ends(reaction7),conditional_extra_joined_inverse_improvement=p.prev.ends(improvement),conditional_seven_high_joined_Schur_lower_matrix=p.prev.ends(lower),
        frozen_NF44_witness=list(map(str,h)),conditional_extra_frozen_witness_improvement=value.ends(),conditional_frozen_witness_value=witness.ends(),
        conditional_joined_condensed_margin=margin.ends(),conditional_joined_determinant=det.ends(),conditional_joined_sign_certified=passed,seven_high_minorant_fails_to_certify=failed,
        background_floor_hypothesis='A >= (207/1000) I on the original remaining high space',background_floor_newly_proved=False,
        actual_negative_original_form_claimed=False,whole_aperture_positive=False,highest_certified_whole_aperture='21/20',RH=False,F4=False,Lean=False)

def finish(cert):
    lower=p.prev.matrix(cert['conditional_seven_high_joined_Schur_lower_matrix'])
    h=p.prev.witness(lower);value=p.dot(h,p.mv(lower,h))
    if cert['seven_high_minorant_fails_to_certify']:assert value.h<0
    cert.update(updated_frozen_rational_witness=list(map(str,h)),updated_witness_lower_certificate_value=value.ends(),necessary_further_updated_witness_response_strict_lower=str(-F(value.h,n.SCALE) if value.h<0 else F(0)))
    return cert

if __name__=='__main__':
    q=argparse.ArgumentParser();q.add_argument('mode',choices=['choose','certify']);q.add_argument('--parity',choices=['even','odd']);q.add_argument('--trial');q.add_argument('--output',required=True);q=q.parse_args()
    if q.mode=='choose':out=choose(q.parity)
    else:
        raw=Path(q.trial).read_bytes();out=certify(json.loads(raw));out['fixed_trial_sha256']=hashlib.sha256(raw).hexdigest();finish(out)
    Path(q.output).write_text(json.dumps(out,indent=2)+'\n')
