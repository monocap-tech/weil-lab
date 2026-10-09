#!/usr/bin/env python3
"""NF45: exact selection custody, reverse covariance replay, rank-one algebra."""
import argparse,hashlib,json
from pathlib import Path
from fractions import Fraction as F
import certify_native_seventh_inverse_source_nf45_106 as v
c=v.c;p=v.p;n=v.n;I=v.I;K=v.K
import validate_native_boundary_response_nf42_106 as old

def selection(trial):
    idx=['even','odd'].index(trial['parity']);o,H,*rest=v.packet(idx);shell=trial['selection_indices']
    q=list(map(p.iv,trial['original_inverse_witness_selection_coordinates']))
    raw=[F((z.mid()*10**100).__floor__(),10**100) for z in q]
    assert list(map(str,raw))==trial['rounded_selection_coordinates']
    vectors=[dict(zip(ii,cc)) for ii,cc in H];tails=[[vectors[a].get(j,F(0)) for j in shell] for a in [0,1,4,5]]
    M=[[c.dot(x,y) for y in tails] for x in tails];assert c.strings(M)==trial['exact_old_tail_Gram']
    ell=c.mv(v.r.b.inverse(M),[c.dot(t,raw) for t in tails]);assert list(map(str,ell))==trial['exact_projection_coefficients']
    y=[z-sum(ell[a]*tails[a][k] for a in range(4)) for k,z in enumerate(raw)];norm=v.ceilnorm(y)
    assert str(norm)==trial['normalizing_rational_upper'];y=[z/norm for z in y]
    assert list(map(str,y))==trial['fixed_rational_seventh_high_coefficients'] and str(v.square(y))==trial['exact_seventh_physical_mass_squared']
    assert all(c.dot(t,y)==0 for t in tails)
    assert all(sum(v*dict(zip(shell,y)).get(j,F(0)) for j,v in zip(ii,cc))==0 for ii,cc in H)
    inv=v.r.b.inverse(M)
    paid=[q[k]-sum((p.dot([I(z) for z in inv[a]],[p.dot(t,q) for t in tails])*tails[a][k] for a in range(4)),I(0)) for k in range(len(q))]
    assert sum((n.sq(z) for z in paid),I(0)).ends()==trial['projected_inverse_witness_shell_square']
    # A nonzero old-tail coordinate perturbation must break exact orthogonality.
    k=next(k for k in range(len(y)) if tails[0][k]);bad=y[:];bad[k]+=F(1,10**100);assert c.dot(tails[0],bad)!=0
    return dict(exact_downround_projection_and_normalization_replayed=True,physical_orthogonality_to_six_high_columns=True,nonorthogonal_mutation_rejected=True)

def exact_algebra(cert):
    M=c.symmetric_mid(cert['seven_high_physical_Gram']);Q=c.symmetric_mid(cert['seven_high_native_Gram']);G=c.symmetric_mid(cert['seven_high_complete_source_Gram'])
    B=c.rectangle_mid(cert['joined_seven_high_native_crosses']);S=c.rectangle_mid(cert['joined_seven_high_source_crosses'])
    C=c.add(Q,c.scale(M,-K));T=c.add(c.add(G,c.scale(Q,-2*K)),c.scale(M,K*K));W=c.add(S,c.scale(B,-K))
    C6=[row[:6] for row in C[:6]];T6=[row[:6] for row in T[:6]];W6=[row[:6] for row in W]
    N6=c.add(C6,c.scale(T6,1/K));N=c.add(C,c.scale(T,1/K));CI=v.r.b.inverse(C6);NI=v.r.b.inverse(N6)
    col=[row[6] for row in C[:6]];coef=c.mv(CI,col);D=C[6][6]-c.dot(col,coef);assert D>0
    ty=[row[6] for row in T[:6]];ff=T[6][6]-2*c.dot(ty,coef)+c.dot(coef,c.mv(T6,coef))
    fv=[ty[j]-c.dot(coef,[row[j] for row in T6]) for j in range(6)]
    fr=[row[6]-c.dot(row[:6],coef) for row in W]
    g=[fr[j]/K-c.dot(c.mv(NI,fv),W6[j])/(K*K) for j in range(3)]
    metric=ff/K-c.dot(fv,c.mv(NI,fv))/(K*K);den=D+metric;assert den>0
    delta=[[x*y/den for y in g] for x in g]
    direct=c.scale(c.add(c.mm(c.mm(W,v.r.b.inverse(N)),c.tr(W)),c.scale(c.mm(c.mm(W6,NI),c.tr(W6)),-1)),1/(K*K))
    assert direct==delta
    old.v41.v40.v39.inside(delta,cert['conditional_extra_joined_inverse_improvement'])
    return dict(exact_seven_vs_six_Woodbury_equals_scalar_defect_update=True,exact_scalar_defect_and_denominator_positive=True,exact_rational_delta_inside_paid_original_intervals=True)

def replay(trial,cert):
    parity=trial['parity'];idx=['even','odd'].index(parity);o,H,M,QH,GH,B,S,Q,G,par,hashes=v.packet(idx)
    assert cert['NF44_input_sha256']==v.SHA44 and trial['NF44_input_sha256']==v.SHA44 and cert['native_input_sha256']==trial['native_input_sha256']==hashes
    assert trial['six_high_columns']==[dict(indices=ii,coefficients=list(map(str,cc))) for ii,cc in H]
    assert trial['frozen_NF44_witness']==par['updated_frozen_rational_witness']==cert['frozen_NF44_witness']
    assert not any(cert[k] for k in ['RH','F4','Lean']) and cert['highest_certified_whole_aperture']=='21/20'
    assert not cert['background_floor_newly_proved'] and not cert['actual_negative_original_form_claimed'] and not cert['whole_aperture_positive']
    n.product=v.r.packed_product;m=p.p.old.probe.Moments(1020,parity);ids=trial['selection_indices'];y=list(map(F,trial['fixed_rational_seventh_high_coefficients']))
    sy=m.source(ids,y);coords=dict(zip(cert['reconstructed_seventh_source_coordinates_indices'],map(p.iv,cert['reconstructed_seventh_source_coordinates'])))
    fun=p.p.functional(m,sy,180);fresh=[p.dot(n.basis(j),fun) for j in coords];assert [z.ends() for z in fresh]==cert['reconstructed_seventh_source_coordinates']
    err=m.eta*v.ceilnorm(y);assert str(err)==cert['seventh_source_analytic_error_upper']
    low=[coords[j] for j in o['ids']];ry=v.r.projection(sy,low,o['ids']);ey=err+8*max(F(z.h-z.l,2*n.SCALE) for z in low)
    assert str(ey)==cert['seventh_projected_source_error_upper']
    square=m.gram(ry,ry);assert square.ends()==cert['reconstructed_seventh_projected_source_square'];ny=v.r.normupper(square)
    pay=2*ey*ny+ey*ey;assert str(pay)==cert['seventh_source_square_payment'] and (square+I(-pay,pay)).ends()==cert['original_seventh_projected_source_square']
    loH,eh=v.high_projection_data(idx,o,par)
    rawtargets=[]
    for j,(ii,cc) in enumerate(H+o['columns']):
        rawtargets.append(m.source(ii,cc))
        print(parity,'NF45 independent original source reconstructed',j,flush=True)
    qy=p.dot(y,[coords[j] for j in ids]);assert qy.ends()==cert['reconstructed_seventh_native_energy']
    assert (qy+I(-err*v.ceilnorm(y),err*v.ceilnorm(y))).ends()==cert['original_seventh_native_energy']
    for j,((ii,cc),source) in enumerate(zip(H+o['columns'],rawtargets)):
        value=p.dot(cc,[coords[k] for k in ii]);pay=err*v.ceilnorm(cc)
        native=value+I(-pay,pay);assert native.ends()==cert['original_seventh_native_crosses'][j]
        ep=m.eta*v.ceilnorm(cc)*v.ceilnorm(y);reverse=m.pair(source,sy[0])+I(-ep,ep)
        assert reverse.ends()==cert['reverse_seventh_native_crosses'][j]
        assert max(native.l,reverse.l)<=min(native.h,reverse.h)
    targets=[v.r.projection(s,lo,o['ids']) for s,lo in zip(rawtargets,loH+o['low'])]
    _,_,W6,_,NI6,_,_,_=v.inverse_packet(M,QH,GH,B,S,G)
    hold=list(map(F,trial['frozen_NF44_witness']));alpha=p.mv(NI6,p.mv(c.tr(W6),hold))
    assert [z.ends() for z in alpha]==trial['inverse_witness_high_coefficients']
    hd=[dict(zip(ii,cc)) for ii,cc in H]
    selectioncoords=list(map(p.iv,trial['original_inverse_witness_selection_coordinates']))
    for pos in [0,len(ids)//2,len(ids)-1]:
        j=ids[pos];test=n.basis(j);rv=I(0)
        for a,(ii,cc) in enumerate(o['columns']):
            e=m.eta*v.ceilnorm(cc);rv+=hold[a]*(m.pair(rawtargets[6+a],test)+I(-e,e))
        qcoord=rv/K
        for a,(ii,cc) in enumerate(H):
            e=m.eta*v.ceilnorm(cc);av=m.pair(rawtargets[a],test)+I(-e,e)
            qcoord-=alpha[a]*(av-K*hd[a].get(j,F(0)))/(K*K)
        assert max(qcoord.l,selectioncoords[pos].l)<=min(qcoord.h,selectioncoords[pos].h)

    errors=eh+o['physical_source_errors'];norms=[v.r.normupper(GH[j][j])+eh[j] for j in range(6)]+[v.r.normupper(G[j][j])+errors[6+j] for j in range(3)]
    for j,(target,ej,nj) in enumerate(zip(targets,errors,norms)):
        print(parity,'NF45 independent covariance replay',j,flush=True)
        value=m.gram(target,ry);assert value.ends()==cert['reconstructed_seventh_source_crosses'][j]
        pay=ey*nj+ej*ny+ey*ej;assert str(pay)==cert['seventh_source_cross_payments'][j]
        assert (value+I(-pay,pay)).ends()==cert['original_seventh_source_crosses'][j]
    M7=p.prev.matrix(cert['seven_high_physical_Gram']);Q7=p.prev.matrix(cert['seven_high_native_Gram']);G7=p.prev.matrix(cert['seven_high_complete_source_Gram']);B7=p.prev.matrix(cert['joined_seven_high_native_crosses']);S7=p.prev.matrix(cert['joined_seven_high_source_crosses'])
    # The enlarged packet must be exactly the authenticated old packet plus paid new entries.
    for full,base,last in [(M7,M,I(v.square(y))),(Q7,QH,p.iv(cert['original_seventh_native_energy'])),(G7,GH,p.iv(cert['original_seventh_projected_source_square']))]:
        assert [[z.ends() for z in row[:6]] for row in full[:6]]==p.prev.ends(base)
        assert full[6][6].ends()==last.ends()
    assert all(M7[j][6].ends()==I(0).ends() for j in range(6))
    for full,key in [(Q7,'original_seventh_native_crosses'),(G7,'original_seventh_source_crosses')]:
        assert [full[j][6].ends() for j in range(6)]==cert[key][:6]
        assert [full[6][j].ends() for j in range(6)]==cert[key][:6]
    for full,base,key in [(B7,B,'original_seventh_native_crosses'),(S7,S,'original_seventh_source_crosses')]:
        assert p.prev.ends([row[:6] for row in full])==p.prev.ends(base)
        assert [row[6].ends() for row in full]==cert[key][6:]
    C,_,_,_,_,oldreaction,*_=v.inverse_packet(M,QH,GH,B,S,G)
    CI,_=v.mi.inverse(C);cross=list(map(p.iv,cert['original_seventh_native_crosses'][:6]))
    defect=p.iv(cert['original_seventh_native_energy'])-K*v.square(y)-p.dot(cross,p.mv(CI,cross))
    assert defect.ends()==cert['seventh_native_defect_after_six_high_minorant'] and defect.l>0
    _,_,_,_,_,reaction,cp,np=v.inverse_packet(M7,Q7,G7,B7,S7,G)
    assert p.prev.ends(reaction)==cert['conditional_seven_high_joined_inverse_upper_matrix'] and cp==cert['seven_high_surplus_positive_proof'] and np==cert['seven_high_inverse_denominator_positive_proof']
    improvement=v.symmetry(c.add(oldreaction,c.scale(reaction,-1)))
    assert p.prev.ends(improvement)==cert['conditional_extra_joined_inverse_improvement']
    assert p.dot(hold,p.mv(improvement,hold)).ends()==cert['conditional_extra_frozen_witness_improvement']
    lower=v.symmetry(c.add(Q,c.scale(reaction,-1)));assert p.prev.ends(lower)==cert['conditional_seven_high_joined_Schur_lower_matrix']
    h=list(map(F,cert['frozen_NF44_witness']));assert p.dot(h,p.mv(lower,h)).ends()==cert['conditional_frozen_witness_value']
    leading=lower[0][0]*lower[1][1]-n.sq(lower[0][1]);assert lower[0][0].l>0 and leading.l>0
    margin=lower[2][2]-(lower[1][1]*n.sq(lower[0][2])-2*lower[0][1]*lower[0][2]*lower[1][2]+lower[0][0]*n.sq(lower[1][2]))/leading
    det=p.c.parent.det3(lower)
    assert margin.ends()==cert['conditional_joined_condensed_margin'] and det.ends()==cert['conditional_joined_determinant']
    assert cert['conditional_joined_sign_certified']==(margin.l>0 and det.l>0)
    assert cert['seven_high_minorant_fails_to_certify']==(margin.h<0 and det.h<0)
    newer=p.prev.witness(lower);newvalue=p.dot(newer,p.mv(lower,newer))
    assert list(map(str,newer))==cert['updated_frozen_rational_witness'] and newvalue.ends()==cert['updated_witness_lower_certificate_value']
    assert str(-F(newvalue.h,n.SCALE) if newvalue.h<0 else F(0))==cert['necessary_further_updated_witness_response_strict_lower']
    print(parity,'NF45 independent replay PASS',flush=True)
    return dict(parity=parity,status='PASS',selection=selection(trial),independent_inverse_witness_source_coordinate_controls_passed=True,all_seventh_source_coordinates_and_reverse_covariances_replayed=True,all_physical_source_payments_replayed=True,exact_Woodbury_algebra=exact_algebra(cert),conditional_joined_sign_certified=cert['conditional_joined_sign_certified'])

def finish_manifest(out):
    for idx,row in enumerate(out['parity_checks']):
        o,H,M,QH,GH,B,S,Q,G,cert,hashes=v.packet(idx)
        _,_,_,_,_,reaction,*_=v.inverse_packet(M,QH,GH,B,S,G)
        lower=c.add(Q,c.scale(reaction,-1));prior=p.prev.matrix(cert['conditional_six_high_joined_Schur_lower_matrix'])
        assert all(max(a.l,b.l)<=min(a.h,b.h) for r,s in zip(lower,prior) for a,b in zip(r,s))
        row['six_source_baseline_matches_NF44_entrywise']=True
    return out

def replay_file(tag):
    tb=Path('notes/data/RPB108_NF45_'+tag+'_FIXED_INVERSE_WITNESS_20261009.json').read_bytes();cb=Path('notes/data/RPB108_NF45_'+tag+'_INVERSE_WITNESS_CERTIFICATE_20261009.json').read_bytes()
    tr=json.loads(tb);cert=json.loads(cb);assert cert['fixed_trial_sha256']==hashlib.sha256(tb).hexdigest()
    row=replay(tr,cert);row.update(trial_sha256=hashlib.sha256(tb).hexdigest(),certificate_sha256=hashlib.sha256(cb).hexdigest());return row

if __name__=='__main__':
    q=argparse.ArgumentParser();q.add_argument('--output',required=True);q=q.parse_args();rows=[]
    from concurrent.futures import ProcessPoolExecutor
    with ProcessPoolExecutor(2) as pool:rows=list(pool.map(replay_file,['EVEN','ODD']))
    crossing,levels=old.v41.v40.v39.controls()
    out=dict(milestone='NF45',status='PASS',NF44_input_sha256=v.SHA44,parity_checks=rows,exact_packing_controls=old.packing_controls(),defect_response_controls=old.v41.controls(),full_block_crossing_controls=crossing,positive_whole_physical_mass_controls=levels,background_floor_newly_proved=False,whole_aperture_positive=False)
    finish_manifest(out);Path(q.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
