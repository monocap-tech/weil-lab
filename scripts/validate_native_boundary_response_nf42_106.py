#!/usr/bin/env python3
"""NF42 reverse covariance replay, exact joint Woodbury algebra and controls."""
import argparse,hashlib,itertools,json,random
from pathlib import Path
from fractions import Fraction as F
import certify_native_boundary_response_nf42_106 as r
import validate_native_boundary_source_cross_nf41_106 as v41
f=r.f;b=r.b;c=r.c;p=r.p;n=r.n;I=r.I;K=r.K
OLD_PRODUCT=n.product

def packing_controls():
    rng=random.Random(42);rows=[]
    for m,k in [(1,1),(3,4),(20,17),(80,90)]:
        a=[rng.randrange(-10**50,10**50) for _ in range(m)];bb=[rng.randrange(-10**50,10**50) for _ in range(k)]
        expected=[sum(a[i]*bb[j-i] for i in range(m) if 0<=j-i<k) for j in range(m+k-1)]
        assert r.integer_convolution(a,bb)==expected;rows.append(dict(lengths=[m,k],exact_signed_integer_coefficients_checked=True))
    vertices=0
    for aa,bb in [([(-3,2),(4,5)],[(-2,1),(0,3)]),([(-10,-4),(0,0),(3,7)],[(0,9),(-7,-1)])]:
        out=r.packed_product([I.raw(l,h) for l,h in aa],[I.raw(l,h) for l,h in bb])
        for av in itertools.product(*[(l,h) for l,h in aa]):
            for bv in itertools.product(*[(l,h) for l,h in bb]):
                vertices+=1
                for j,v in enumerate(out):
                    num=sum(av[i]*bv[j-i] for i in range(len(av)) if 0<=j-i<len(bv));assert v.l*n.SCALE<=num<=v.h*n.SCALE
    return dict(exact_integer_controls=rows,all_interval_coefficient_endpoint_vertices_checked=vertices)

def block(A,B,C,D):return [a+bb for a,bb in zip(A,B)]+[cc+d for cc,d in zip(C,D)]
def exact_algebra(cert,idx):
    a,_,X,P,QY,*_=b.inputs(idx);J=c.decode(r.parents()[idx]['chosen_enclosure_compatible_boundary_source_crosses'])
    GYY=c.symmetric_mid(cert['original_boundary_source_Gram']);GYZ=c.rectangle_mid(cert['original_boundary_old_high_source_crosses']);GYR=c.rectangle_mid(cert['original_boundary_joined_source_crosses'])
    _,C,T,W=c.gram_and_surplus(a);C4=block(C,c.tr(P),P,c.add(QY,c.scale(b.eye(2),-K)));_,cp=c.ldl(C4);assert min(cp)>0
    YAZ=c.add(P,c.scale(X,K));E=c.add(GYZ,c.add(c.scale(YAZ,-K),c.scale(P,-K)))
    TY=c.add(c.add(GYY,c.scale(QY,-2*K)),c.scale(b.eye(2),K*K));T4=block(T,c.tr(E),E,TY)
    WR=c.tr(c.add(GYR,c.scale(J,-K)));W4=[row+more for row,more in zip(W,WR)]
    N4=c.add(C4,c.scale(T4,1/K));_,np=c.ldl(N4);assert min(np)>0
    direct=c.add(c.scale(a['G'],1/K),c.scale(c.mm(c.mm(W4,b.inverse(N4)),c.tr(W4)),-1/(K*K)))
    coef=c.mm(c.inverse2(C),c.tr(P));FF=c.add(c.add(TY,c.scale(c.mm(E,coef),-1)),c.scale(c.mm(c.tr(coef),c.tr(E)),-1));FF=c.add(FF,c.mm(c.mm(c.tr(coef),T),coef))
    FR=c.add(c.add(GYR,c.scale(J,-K)),c.scale(c.mm(c.tr(coef),c.tr(W)),-1));FV=c.add(E,c.scale(c.mm(c.tr(coef),T),-1))
    NI=c.inverse2(c.add(C,c.scale(T,1/K)));D=c.add(c.add(QY,c.scale(b.eye(2),-K)),c.scale(c.mm(c.mm(P,c.inverse2(C)),c.tr(P)),-1))
    g=c.add(c.scale(FR,1/K),c.scale(c.mm(c.mm(FV,NI),c.tr(W)),-1/(K*K)))
    metric=c.add(c.scale(FF,1/K),c.scale(c.mm(c.mm(FV,NI),c.tr(FV)),-1/(K*K)));den=c.add(D,metric);_,ds=c.ldl(den);assert min(ds)>0
    delta=c.mm(c.mm(c.tr(g),c.inverse2(den)),g);sequential=c.add(c.reaction(a,F(0)),c.scale(delta,-1));assert direct==sequential
    lower=c.add(a['Q'],c.scale(direct,-1));v41.v40.v39.inside(lower,cert['conditional_improved_joined_Schur_lower_matrix']);v41.v40.v39.inside(delta,cert['conditional_joined_inverse_improvement_lower_matrix'])
    return dict(joint_four_high_surplus_positive=True,joint_four_high_inverse_identity_equals_sequential_defect_update=True,chosen_rational_algebra_inside_original_intervals=True)

def check(cert,idx,data,source,hashes):
    parity=['even','odd'][idx];assert cert['NF41_input_sha256']==r.SHA41 and cert['authenticated_native_input_sha256']==hashes and cert['parity']==parity
    o=p.objects(data,source,parity);d38,_=c.parents();d36=p.prev.parents()[0];par38=d38[idx+2];trial=d38[idx];old=[d36[idx+2],par38];ids=[112+idx,114+idx];assert cert['boundary_mode_indices']==ids
    n.product=r.packed_product;m=p.p.old.probe.Moments(1020,parity);ys=[];ey=[];lowY=[]
    for y in ids:
        low=[I(*map(F,source[f'{min(y,j)},{max(y,j)}']['full'])) for j in o['ids']];lowY.append(low);ys.append(r.projection(m.source([y],[F(1)]),low,o['ids']));ey.append(m.eta+8*max(F(v.h-v.l,2*n.SCALE) for v in low))
    assert p.prev.ends(lowY)==cert['boundary_source_low_projection_intervals'] and list(map(str,ey))==cert['boundary_source_physical_errors']
    zs=[];ez=[]
    for coeff,par in zip([trial['old_correction_coefficients'],trial['fixed_rational_second_correction_coefficients']],old):
        coords=dict(zip(par['correction_source_coordinate_indices'],map(p.iv,par['reconstructed_correction_source_coordinates'])))
        zs.append(r.projection(m.source(trial['correction_indices'],list(map(F,coeff))),[coords[j] for j in o['ids']],o['ids']));ez.append(F(par['correction_residual_error_upper']))
    rs=[r.projection(m.source(ii,cc),low,o['ids']) for (ii,cc),low in zip(o['columns'],o['low'])];er=o['physical_source_errors']
    gh=p.prev.matrix(par38['joint_complete_source_high_block']);gr=p.prev.matrix(c.parents()[1][idx]['original_selected_complete_source_Gram'])
    YYhat=[[m.gram(x,y) for y in ys] for x in ys];ny=[r.normupper(YYhat[i][i]) for i in range(2)];nz=[r.normupper(gh[i][i])+ez[i] for i in range(2)];nr=[r.normupper(gr[i][i])+er[i] for i in range(3)]
    assert p.prev.ends(YYhat)==cert['reconstructed_boundary_source_Gram'] and list(map(str,ny))==cert['boundary_approximant_norm_upper']
    payYY=[[ey[i]*ny[j]+ey[j]*ny[i]+ey[i]*ey[j] for j in range(2)] for i in range(2)];YY=[[YYhat[i][j]+I(-payYY[i][j],payYY[i][j]) for j in range(2)] for i in range(2)]
    assert [[str(v) for v in row] for row in payYY]==cert['boundary_source_Gram_payments'] and p.prev.ends(YY)==cert['original_boundary_source_Gram']
    # One independent inherited interval-product source-square check per parity.
    n.product=OLD_PRODUCT;reference=m.gram(ys[0],ys[0]);n.product=r.packed_product
    assert max(reference.l,YYhat[0][0].l)<=min(reference.h,YYhat[0][0].h)
    matrices=[]
    for targets,errors,norms,label,key in [(zs,ez,nz,'old_high','boundary_old_high'),(rs,er,nr,'joined','boundary_joined')]:
        hat=[[m.gram(s,y) for s in targets] for y in ys];pay=[[ey[i]*norms[j]+errors[j]*ny[i]+ey[i]*errors[j] for j in range(len(targets))] for i in range(2)]
        paid=[[v+I(-pay[i][j],pay[i][j]) for j,v in enumerate(row)] for i,row in enumerate(hat)]
        assert p.prev.ends(hat)==cert['reconstructed_'+key+'_source_crosses'] and [[str(v) for v in row] for row in pay]==cert[key+'_source_cross_payments'] and p.prev.ends(paid)==cert['original_'+key+'_source_crosses']
        matrices.append(paid);print(parity,'replayed all signed',label,'source covariances',flush=True)
    assert list(map(str,ez))==cert['old_high_source_physical_errors'] and list(map(str,nz))==cert['old_high_approximant_norm_upper'] and list(map(str,er))==cert['joined_source_physical_errors'] and list(map(str,nr))==cert['joined_approximant_norm_upper']
    result=r.analyze(idx,YY,*matrices)
    for key,value in result.items():assert cert[key]==value
    assert not cert['actual_negative_original_form_claimed'] and not cert['whole_aperture_positive'] and not cert['background_floor_newly_proved']
    return dict(parity=parity,status='PASS',all_original_boundary_source_covariances_replayed=True,independent_inherited_product_reference_square=reference.ends(),exact_joint_Woodbury_algebra=exact_algebra(cert,idx),conditional_inverse_improvement=cert['conditional_frozen_witness_inverse_improvement'],conditional_joined_Schur_certificate_passed=cert['conditional_joined_Schur_certificate_passed'],chosen_four_high_source_minorant_fails_to_certify=cert['chosen_four_high_source_minorant_fails_to_certify'])
if __name__=='__main__':
    q=argparse.ArgumentParser();q.add_argument('--output',required=True);q=q.parse_args();parent=r.parents();assert parent[-1]['status']=='PASS';pack=packing_controls();data,source,hashes=p.p.old.prev.inputs();rows=[]
    for idx,tag in enumerate(['EVEN','ODD']):
        raw=Path('notes/data/RPB108_NF42_'+tag+'_BOUNDARY_RESPONSE_CERTIFICATE_20261009.json').read_bytes();row=check(json.loads(raw),idx,data,source,hashes);row['certificate_sha256']=hashlib.sha256(raw).hexdigest();rows.append(row)
    crossing,levels=v41.v40.v39.controls()
    out=dict(milestone='NF42',status='PASS',NF41_input_sha256=r.SHA41,parity_checks=rows,exact_packing_controls=pack,defect_source_Woodbury_controls=v41.controls(),exact_full_block_crossing_controls=crossing,positive_whole_physical_mass_controls=levels,background_floor_newly_proved=False,whole_aperture_positive=False)
    Path(q.output).write_text(json.dumps(out,indent=2)+'\n');print('NF42 validation PASS',flush=True)
