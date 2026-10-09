#!/usr/bin/env python3
"""NF45: exact selection custody, reverse covariance replay, rank-one algebra."""
import argparse,hashlib,json
from pathlib import Path
from fractions import Fraction as F
import certify_native_next_shell_nf46_106 as v
c=v.c;p=v.p;n=v.n;I=v.I;K=v.K
import validate_native_boundary_response_nf42_106 as old

def selection(trial):
    o,H,*_=v.packet(0);shell=trial['selection_indices'];assert shell==list(range(182,213,2))
    assert trial['seven_high_columns']==[dict(indices=ii,coefficients=list(map(str,cc))) for ii,cc in H]
    q=list(map(p.iv,trial['original_inverse_witness_selection_coordinates']))
    raw=[F((z.mid()*10**100).__floor__(),10**100) for z in q]
    assert list(map(str,raw))==trial['rounded_selection_coordinates']
    norm=v.ceilnorm(raw);assert str(norm)==trial['normalizing_rational_upper'];y=[z/norm for z in raw]
    assert list(map(str,y))==trial['fixed_rational_eighth_high_coefficients'] and str(v.square(y))==trial['exact_eighth_physical_mass_squared']
    assert all(max(ii)<min(shell) for ii,cc in H)
    yd=dict(zip(shell,y));assert all(sum(z*yd.get(i,F(0)) for i,z in zip(ii,cc))==0 for ii,cc in H)
    assert sum((n.sq(z) for z in q),I(0)).ends()==trial['projected_inverse_witness_shell_square']
    # Adding an old-direction coordinate breaks physical orthogonality.
    bad=yd.copy();bad[H[2][0][0]]=F(1,10**100)
    assert sum(z*bad.get(i,F(0)) for i,z in zip(*H[2]))!=0
    return dict(exact_downround_and_normalization_replayed=True,disjoint_shell_orthogonality_to_seven_high_columns=True,old_direction_mutation_rejected=True)

def exact_algebra(cert):
    M=c.symmetric_mid(cert['eight_high_physical_Gram']);Q=c.symmetric_mid(cert['eight_high_native_Gram']);G=c.symmetric_mid(cert['eight_high_complete_source_Gram'])
    B=c.rectangle_mid(cert['joined_eight_high_native_crosses']);S=c.rectangle_mid(cert['joined_eight_high_source_crosses'])
    C=c.add(Q,c.scale(M,-K));T=c.add(c.add(G,c.scale(Q,-2*K)),c.scale(M,K*K));W=c.add(S,c.scale(B,-K))
    C7=[row[:7] for row in C[:7]];T7=[row[:7] for row in T[:7]];W7=[row[:7] for row in W]
    N7=c.add(C7,c.scale(T7,1/K));N=c.add(C,c.scale(T,1/K));CI=v.r.b.inverse(C7);NI=v.r.b.inverse(N7)
    col=[row[7] for row in C[:7]];coef=c.mv(CI,col);D=C[7][7]-c.dot(col,coef);assert D>0
    ty=[row[7] for row in T[:7]];ff=T[7][7]-2*c.dot(ty,coef)+c.dot(coef,c.mv(T7,coef))
    fv=[ty[j]-c.dot(coef,[row[j] for row in T7]) for j in range(7)]
    fr=[row[7]-c.dot(row[:7],coef) for row in W]
    g=[fr[j]/K-c.dot(c.mv(NI,fv),W7[j])/(K*K) for j in range(3)]
    metric=ff/K-c.dot(fv,c.mv(NI,fv))/(K*K);den=D+metric;assert den>0
    delta=[[x*y/den for y in g] for x in g]
    direct=c.scale(c.add(c.mm(c.mm(W,v.r.b.inverse(N)),c.tr(W)),c.scale(c.mm(c.mm(W7,NI),c.tr(W7)),-1)),1/(K*K))
    assert direct==delta
    old.v41.v40.v39.inside(delta,cert['conditional_extra_joined_inverse_improvement'])
    return dict(exact_eight_vs_seven_Woodbury_equals_scalar_defect_update=True,exact_scalar_defect_and_denominator_positive=True,exact_rational_delta_inside_paid_original_intervals=True)

def replay(trial,cert):
    parity=trial['parity'];idx=['even','odd'].index(parity);o,H,M,QH,GH,B,S,Q,G,par,hashes=v.packet(idx)
    assert cert['NF45_input_sha256']==v.SHA45 and trial['NF45_input_sha256']==v.SHA45 and cert['native_input_sha256']==trial['native_input_sha256']==hashes
    assert trial['seven_high_columns']==[dict(indices=ii,coefficients=list(map(str,cc))) for ii,cc in H]
    assert trial['frozen_NF45_witness']==par['updated_frozen_rational_witness']==cert['frozen_NF45_witness']
    assert not any(cert[k] for k in ['RH','F4','Lean']) and cert['highest_certified_whole_aperture']=='21/20'
    assert not cert['background_floor_newly_proved'] and not cert['actual_negative_original_form_claimed'] and not cert['whole_aperture_positive']
    n.product=v.r.packed_product;m=p.p.old.probe.Moments(1100,parity);ids=trial['selection_indices'];y=list(map(F,trial['fixed_rational_eighth_high_coefficients']))
    sy=m.source(ids,y);coords=dict(zip(cert['reconstructed_eighth_source_coordinates_indices'],map(p.iv,cert['reconstructed_eighth_source_coordinates'])))
    fun=p.p.functional(m,sy,212);fresh=[p.dot(n.basis(j),fun) for j in coords];assert [z.ends() for z in fresh]==cert['reconstructed_eighth_source_coordinates']
    err=m.eta*v.ceilnorm(y);assert str(err)==cert['eighth_source_analytic_error_upper']
    low=[coords[j] for j in o['ids']];ry=v.r.projection(sy,low,o['ids']);ey=err+8*max(F(z.h-z.l,2*n.SCALE) for z in low)
    assert str(ey)==cert['eighth_projected_source_error_upper']
    square=m.gram(ry,ry);assert square.ends()==cert['reconstructed_eighth_projected_source_square'];ny=v.r.normupper(square)
    pay=2*ey*ny+ey*ey;assert str(pay)==cert['eighth_source_square_payment'] and (square+I(-pay,pay)).ends()==cert['original_eighth_projected_source_square']
    loH,eh=v.high_projection_data(idx,o,par)
    rawtargets=[]
    for j,(ii,cc) in enumerate(H+o['columns']):
        rawtargets.append(m.source(ii,cc))
        print(parity,'NF46 independent original source reconstructed',j,flush=True)
    qy=p.dot(y,[coords[j] for j in ids]);assert qy.ends()==cert['reconstructed_eighth_native_energy']
    assert (qy+I(-err*v.ceilnorm(y),err*v.ceilnorm(y))).ends()==cert['original_eighth_native_energy']
    for j,((ii,cc),source) in enumerate(zip(H+o['columns'],rawtargets)):
        value=p.dot(cc,[coords[k] for k in ii]);pay=err*v.ceilnorm(cc)
        native=value+I(-pay,pay);assert native.ends()==cert['original_eighth_native_crosses'][j]
        ep=m.eta*v.ceilnorm(cc)*v.ceilnorm(y);reverse=m.pair(source,sy[0])+I(-ep,ep)
        assert reverse.ends()==cert['reverse_eighth_native_crosses'][j]
        assert max(native.l,reverse.l)<=min(native.h,reverse.h)
    targets=[v.r.projection(s,lo,o['ids']) for s,lo in zip(rawtargets,loH+o['low'])]
    _,_,W7,_,NI7,_,_,_=v.inverse_packet(M,QH,GH,B,S,G)
    hold=list(map(F,trial['frozen_NF45_witness']));alpha=p.mv(NI7,p.mv(c.tr(W7),hold))
    assert [z.ends() for z in alpha]==trial['inverse_witness_high_coefficients']
    hd=[dict(zip(ii,cc)) for ii,cc in H]
    selectioncoords=list(map(p.iv,trial['original_inverse_witness_selection_coordinates']))
    for pos in [0,len(ids)//2,len(ids)-1]:
        j=ids[pos];test=n.basis(j);rv=I(0)
        for a,(ii,cc) in enumerate(o['columns']):
            e=m.eta*v.ceilnorm(cc);rv+=hold[a]*(m.pair(rawtargets[7+a],test)+I(-e,e))
        qcoord=rv/K
        for a,(ii,cc) in enumerate(H):
            e=m.eta*v.ceilnorm(cc);av=m.pair(rawtargets[a],test)+I(-e,e)
            qcoord-=alpha[a]*(av-K*hd[a].get(j,F(0)))/(K*K)
        assert max(qcoord.l,selectioncoords[pos].l)<=min(qcoord.h,selectioncoords[pos].h)

    errors=eh+o['physical_source_errors'];norms=[v.r.normupper(GH[j][j])+eh[j] for j in range(7)]+[v.r.normupper(G[j][j])+errors[7+j] for j in range(3)]
    for j,(target,ej,nj) in enumerate(zip(targets,errors,norms)):
        print(parity,'NF46 independent covariance replay',j,flush=True)
        value=m.gram(target,ry);assert value.ends()==cert['reconstructed_eighth_source_crosses'][j]
        pay=ey*nj+ej*ny+ey*ej;assert str(pay)==cert['eighth_source_cross_payments'][j]
        assert (value+I(-pay,pay)).ends()==cert['original_eighth_source_crosses'][j]
    M8=p.prev.matrix(cert['eight_high_physical_Gram']);Q8=p.prev.matrix(cert['eight_high_native_Gram']);G8=p.prev.matrix(cert['eight_high_complete_source_Gram']);B8=p.prev.matrix(cert['joined_eight_high_native_crosses']);S8=p.prev.matrix(cert['joined_eight_high_source_crosses'])
    # The enlarged packet must be exactly the authenticated old packet plus paid new entries.
    for full,base,last in [(M8,M,I(v.square(y))),(Q8,QH,p.iv(cert['original_eighth_native_energy'])),(G8,GH,p.iv(cert['original_eighth_projected_source_square']))]:
        assert [[z.ends() for z in row[:7]] for row in full[:7]]==p.prev.ends(base)
        assert full[7][7].ends()==last.ends()
    assert all(M8[j][7].ends()==I(0).ends() for j in range(7))
    for full,key in [(Q8,'original_eighth_native_crosses'),(G8,'original_eighth_source_crosses')]:
        assert [full[j][7].ends() for j in range(7)]==cert[key][:7]
        assert [full[7][j].ends() for j in range(7)]==cert[key][:7]
    for full,base,key in [(B8,B,'original_eighth_native_crosses'),(S8,S,'original_eighth_source_crosses')]:
        assert p.prev.ends([row[:7] for row in full])==p.prev.ends(base)
        assert [row[7].ends() for row in full]==cert[key][7:]
    C,_,_,_,_,oldreaction,*_=v.inverse_packet(M,QH,GH,B,S,G)
    CI,_=v.mi.inverse(C);cross=list(map(p.iv,cert['original_eighth_native_crosses'][:7]))
    defect=p.iv(cert['original_eighth_native_energy'])-K*v.square(y)-p.dot(cross,p.mv(CI,cross))
    assert defect.ends()==cert['eighth_native_defect_after_seven_high_minorant'] and defect.l>0
    _,_,_,_,_,reaction,cp,np=v.inverse_packet(M8,Q8,G8,B8,S8,G)
    assert p.prev.ends(reaction)==cert['conditional_eight_high_joined_inverse_upper_matrix'] and cp==cert['eight_high_surplus_positive_proof'] and np==cert['eight_high_inverse_denominator_positive_proof']
    improvement=v.symmetry(c.add(oldreaction,c.scale(reaction,-1)))
    assert p.prev.ends(improvement)==cert['conditional_extra_joined_inverse_improvement']
    assert p.dot(hold,p.mv(improvement,hold)).ends()==cert['conditional_extra_frozen_witness_improvement']
    lower=v.symmetry(c.add(Q,c.scale(reaction,-1)));assert p.prev.ends(lower)==cert['conditional_eight_high_joined_Schur_lower_matrix']
    h=list(map(F,cert['frozen_NF45_witness']));assert p.dot(h,p.mv(lower,h)).ends()==cert['conditional_frozen_witness_value']
    leading=lower[0][0]*lower[1][1]-n.sq(lower[0][1]);assert lower[0][0].l>0 and leading.l>0
    margin=lower[2][2]-(lower[1][1]*n.sq(lower[0][2])-2*lower[0][1]*lower[0][2]*lower[1][2]+lower[0][0]*n.sq(lower[1][2]))/leading
    det=p.c.parent.det3(lower)
    assert margin.ends()==cert['conditional_joined_condensed_margin'] and det.ends()==cert['conditional_joined_determinant']
    assert cert['conditional_joined_sign_certified']==(margin.l>0 and det.l>0)
    assert cert['eight_high_minorant_fails_to_certify']==(margin.h<0 and det.h<0)
    newer=p.prev.witness(lower);newvalue=p.dot(newer,p.mv(lower,newer))
    assert list(map(str,newer))==cert['updated_frozen_rational_witness'] and newvalue.ends()==cert['updated_witness_lower_certificate_value']
    assert str(-F(newvalue.h,n.SCALE) if newvalue.h<0 else F(0))==cert['necessary_further_updated_witness_response_strict_lower']
    print(parity,'NF46 independent replay PASS',flush=True)
    return dict(parity=parity,status='PASS',selection=selection(trial),independent_inverse_witness_source_coordinate_controls_passed=True,all_eighth_source_coordinates_and_reverse_covariances_replayed=True,all_physical_source_payments_replayed=True,exact_Woodbury_algebra=exact_algebra(cert),conditional_joined_sign_certified=cert['conditional_joined_sign_certified'])

def finish_manifest(out):
    o,H,M,QH,GH,B,S,Q,G,cert,hashes=v.packet(0)
    _,_,_,_,_,reaction,*_=v.inverse_packet(M,QH,GH,B,S,G)
    lower=c.add(Q,c.scale(reaction,-1));prior=p.prev.matrix(cert['conditional_seven_high_joined_Schur_lower_matrix'])
    assert all(max(a.l,b.l)<=min(a.h,b.h) for r,s in zip(lower,prior) for a,b in zip(r,s))
    out['even_check']['seven_source_baseline_matches_NF45_entrywise']=True
    odd=v.parents()[3]
    lo=p.prev.matrix(odd['conditional_seven_high_joined_Schur_lower_matrix'])
    leading=lo[0][0]*lo[1][1]-n.sq(lo[0][1]);det=p.c.parent.det3(lo)
    assert lo[0][0].l>0 and leading.l>0 and det.l>0 and odd['conditional_joined_sign_certified']
    assert v.parents()[4]['parity_checks'][1]['status']=='PASS'
    out['preserved_odd_NF45_certificate']=dict(sha256=v.SHA45[3],conditional_joined_sign_certified=True,positive_leading_minor_and_determinant_rechecked=True,full_source_replay_inherited_from_authenticated_NF45=True)
    return out

if __name__=='__main__':
    q=argparse.ArgumentParser();q.add_argument('--output',required=True);q=q.parse_args()
    tb=Path('notes/data/RPB108_NF46_EVEN_FIXED_NEXT_SHELL_20261009.json').read_bytes();cb=Path('notes/data/RPB108_NF46_EVEN_NEXT_SHELL_CERTIFICATE_20261009.json').read_bytes()
    tr=json.loads(tb);cert=json.loads(cb);assert cert['fixed_trial_sha256']==hashlib.sha256(tb).hexdigest()
    row=replay(tr,cert);row.update(trial_sha256=hashlib.sha256(tb).hexdigest(),certificate_sha256=hashlib.sha256(cb).hexdigest())
    crossing,levels=old.v41.v40.v39.controls()
    out=dict(milestone='NF46',status='PASS',NF45_input_sha256=v.SHA45,even_check=row,exact_packing_controls=old.packing_controls(),defect_response_controls=old.v41.controls(),full_block_crossing_controls=crossing,positive_whole_physical_mass_controls=levels,background_floor_newly_proved=False,whole_aperture_positive=False)
    finish_manifest(out);Path(q.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
