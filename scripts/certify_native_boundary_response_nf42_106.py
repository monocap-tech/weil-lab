#!/usr/bin/env python3
"""NF42: paid boundary source covariances and conditional inverse improvement."""
import argparse,hashlib,json
from pathlib import Path
from fractions import Fraction as F
import certify_native_boundary_source_cross_nf41_106 as f
b=f.b;c=f.c;p=f.p;n=f.n;I=f.I;K=f.K
SHA41=['162bf4668b75b783b978b633f32b166774fd5ecd75fb6dcb0282d7ab111a6ec8','392b4b38d5ce51263bff6b7c8248f90598c837ff750d673e301e899daa286eb0','21fe1825a090bb37135fe2d34ae68502f242b3567467ea8289e2ea736fbb3450']
def parents():
    names=['EVEN_BOUNDARY_SOURCE_CROSS_CERTIFICATE','ODD_BOUNDARY_SOURCE_CROSS_CERTIFICATE','BOUNDARY_SOURCE_CROSS_VALIDATION'];raw=[Path('notes/data/RPB108_NF41_'+v+'_20261009.json').read_bytes() for v in names]
    assert [hashlib.sha256(v).hexdigest() for v in raw]==SHA41;out=list(map(json.loads,raw));assert out[-1]['status']=='PASS';return out

def integer_convolution(a,b):
    """Exact signed integer convolution by carry-free binary packing."""
    assert a and b
    aa=max(0,-min(a));bb=max(0,-min(b));u=[v+aa for v in a];v=[w+bb for w in b]
    bound=max(u)*max(v)*min(len(a),len(b));bits=max(1,bound.bit_length()+1)
    x=y=0
    for z in reversed(u):x=(x<<bits)+z
    for z in reversed(v):y=(y<<bits)+z
    z=x*y;mask=(1<<bits)-1;pa=[0];pb=[0]
    for w in a:pa.append(pa[-1]+w)
    for w in b:pb.append(pb[-1]+w)
    out=[]
    for k in range(len(a)+len(b)-1):
        lo=max(0,k-len(b)+1);hi=min(len(a)-1,k);lo2=max(0,k-len(a)+1);hi2=min(len(b)-1,k)
        out.append((z&mask)-bb*(pa[hi+1]-pa[lo])-aa*(pb[hi2+1]-pb[lo2])-aa*bb*(hi-lo+1));z>>=bits
    assert z==0;return out

def packed_product(a,b):
    # An interval coefficient is enclosed by center +/- radius on the integer grid.
    ac=[(v.l+v.h)//2 for v in a];bc=[(v.l+v.h)//2 for v in b]
    ar=[max(v.h-x,x-v.l) for v,x in zip(a,ac)];br=[max(v.h-x,x-v.l) for v,x in zip(b,bc)]
    centers=integer_convolution(ac,bc)
    parts=[integer_convolution(list(map(abs,ac)),br),integer_convolution(ar,list(map(abs,bc))),integer_convolution(ar,br)]
    out=[]
    for k,x in enumerate(centers):
        rad=sum(row[k] for row in parts);out.append(I.raw((x-rad)//n.SCALE,-((-(x+rad))//n.SCALE)))
    return n.trim(out)

def normupper(box):return F(n.sqrt_r(F(box.h,n.SCALE)).h,n.SCALE)
def projection(s,low,ids):return (s[0],n.add(s[1],n.scale(n.physical(ids,[v.mid() for v in low]),-1)),s[2],s[3])
def analyze(idx,GYY,GYZ,GYR):
    a,ids,X,P,QY,DY,_,_,Pi,QYi,_=b.inputs(idx);_,par=c.packet_inputs(idx);prior=c.parents()[1][idx]
    QZ=p.prev.matrix(par['joint_native_high_block']);GZ=p.prev.matrix(par['joint_complete_source_high_block'])
    B=p.prev.matrix(par['joint_native_joined_high_crosses']);S=p.prev.matrix(par['joint_complete_source_joined_high_crosses'])
    C=c.add(QZ,c.scale(f.im(a['M']),-K));T=c.add(c.add(GZ,c.scale(QZ,-2*K)),c.scale(f.im(a['M']),K*K));W=c.add(S,c.scale(B,-K))
    CI=f.inverse2_interval(C);N=c.add(C,c.scale(T,1/K));NI=f.inverse2_interval(N);coef=c.mm(CI,c.tr(Pi))
    J=p.prev.matrix(parents()[idx]['original_signed_boundary_source_crosses'])
    YAZ=c.add(Pi,c.scale(f.im(X),K));YV=c.add(GYZ,c.scale(YAZ,-K));E=c.add(YV,c.scale(Pi,-K))
    FF=c.add(c.add(GYY,c.scale(QYi,-2*K)),c.scale(f.im(b.eye(2)),K*K))
    FF=c.add(c.add(FF,c.scale(c.mm(E,coef),-1)),c.scale(c.mm(c.tr(coef),c.tr(E)),-1));FF=c.add(FF,c.mm(c.mm(c.tr(coef),T),coef))
    FR=c.add(c.add(GYR,c.scale(J,-K)),c.scale(c.mm(c.tr(coef),c.tr(W)),-1))
    FV=c.add(E,c.scale(c.mm(c.tr(coef),T),-1))
    coupling=c.add(c.scale(FR,1/K),c.scale(c.mm(c.mm(FV,NI),c.tr(W)),-1/(K*K)))
    metric=c.add(c.scale(FF,1/K),c.scale(c.mm(c.mm(FV,NI),c.tr(FV)),-1/(K*K)))
    den=c.add(DY,metric)
    # The true denominator is symmetric; intersect redundant enclosures.
    lo=max(den[0][1].l,den[1][0].l);hi=min(den[0][1].h,den[1][0].h);assert lo<=hi;den[0][1]=den[1][0]=I.raw(lo,hi)
    di=f.inverse2_interval(den);improvement=c.mm(c.mm(c.tr(coupling),di),coupling)
    baseline=p.prev.matrix(par['joint_functional_ceiling']);lower=c.add(baseline,improvement)
    h=list(map(F,par['joint_universal_fixed_rational_witness']));gh=p.mv(coupling,h);value=p.dot(gh,p.mv(di,gh));assert value.l>0
    oldvalue=p.dot(h,p.mv(baseline,h));newvalue=p.dot(h,p.mv(lower,h));threshold=-F(oldvalue.h,n.SCALE)
    d2=lower[0][0]*lower[1][1]-n.sq(lower[0][1]);assert lower[0][0].l>0 and d2.l>0
    margin=lower[2][2]-(lower[1][1]*n.sq(lower[0][2])-2*lower[0][1]*lower[0][2]*lower[1][2]+lower[0][0]*n.sq(lower[1][2]))/d2
    det=p.c.parent.det3(lower);passed=margin.l>0 and det.l>0;failed=margin.h<0 and det.h<0
    return dict(original_defect_source_Gram=p.prev.ends(FF),original_defect_source_joined_crosses=p.prev.ends(FR),original_defect_source_surplus_crosses=p.prev.ends(FV),
        original_defect_source_inverse_coupling=p.prev.ends(coupling),original_defect_source_inverse_metric=p.prev.ends(metric),positive_Woodbury_denominator=p.prev.ends(den),
        conditional_joined_inverse_improvement_lower_matrix=p.prev.ends(improvement),conditional_improved_joined_Schur_lower_matrix=p.prev.ends(lower),
        frozen_NF38_witness=list(map(str,h)),conditional_frozen_witness_inverse_improvement=value.ends(),necessary_NF39_frozen_witness_threshold=str(threshold),
        baseline_witness_value=oldvalue.ends(),improved_lower_witness_value=newvalue.ends(),improved_lower_leading_pair_determinant=d2.ends(),improved_lower_condensed_margin=margin.ends(),improved_lower_determinant=det.ends(),
        conditional_joined_Schur_certificate_passed=passed,chosen_four_high_source_minorant_fails_to_certify=failed,
        background_floor_hypothesis='A >= (207/1000) I on the original remaining high space',background_floor_newly_proved=False)

def run(parity):
    idx=['even','odd'].index(parity);par41=parents()[idx];data,source,hashes=p.p.old.prev.inputs();o=p.objects(data,source,parity);d38,_=c.parents();d36=p.prev.parents()[0];par38=d38[idx+2];par36=d36[idx+2];trial=d38[idx]
    n.product=packed_product;m=p.p.old.probe.Moments(1020,parity);ids=par41['boundary_mode_indices'];lowids=o['ids']
    Y=[];EY=[];lowY=[]
    for y in ids:
        low=[I(*map(F,source[f'{min(y,j)},{max(y,j)}']['full'])) for j in lowids];lowY.append(low)
        Y.append(projection(m.source([y],[F(1)]),low,lowids));EY.append(m.eta+8*max(F(v.h-v.l,2*n.SCALE) for v in low))
    Z=[];EZ=[]
    for coeff,par in [(trial['old_correction_coefficients'],par36),(trial['fixed_rational_second_correction_coefficients'],par38)]:
        coords=dict(zip(par['correction_source_coordinate_indices'],map(p.iv,par['reconstructed_correction_source_coordinates'])))
        Z.append(projection(m.source(trial['correction_indices'],list(map(F,coeff))),[coords[j] for j in lowids],lowids));EZ.append(F(par['correction_residual_error_upper']))
    R=[projection(m.source(ii,cc),low,lowids) for (ii,cc),low in zip(o['columns'],o['low'])];ER=o['physical_source_errors']
    GZ=p.prev.matrix(par38['joint_complete_source_high_block']);GR=p.prev.matrix(c.parents()[1][idx]['original_selected_complete_source_Gram'])
    NY=[];YY=[[None]*2 for _ in range(2)];YYhat=[[None]*2 for _ in range(2)];paymentsYY=[[None]*2 for _ in range(2)]
    for i in range(2):
        v=m.gram(Y[i],Y[i]);assert v.l>0;NY.append(normupper(v));pay=2*EY[i]*NY[i]+EY[i]**2;YYhat[i][i]=v;paymentsYY[i][i]=pay;YY[i][i]=v+I(-pay,pay)
        print(parity,'certified original boundary source square',i,flush=True)
    v=m.gram(Y[0],Y[1]);pay=EY[0]*NY[1]+EY[1]*NY[0]+EY[0]*EY[1];YYhat[0][1]=YYhat[1][0]=v;paymentsYY[0][1]=paymentsYY[1][0]=pay;YY[0][1]=YY[1][0]=v+I(-pay,pay)
    NZ=[normupper(GZ[i][i])+EZ[i] for i in range(2)];NR=[normupper(GR[i][i])+ER[i] for i in range(3)]
    def crosses(targets,errors,norms,label):
        hat=[];paid=[];payments=[]
        for i in range(2):
            hr=[];pr=[];er=[]
            for j in range(len(targets)):
                v=m.gram(Y[i],targets[j]);pay=EY[i]*norms[j]+errors[j]*NY[i]+EY[i]*errors[j];hr.append(v);pr.append(v+I(-pay,pay));er.append(pay)
                print(parity,'certified boundary covariance',label,i,j,flush=True)
            hat.append(hr);paid.append(pr);payments.append(er)
        return hat,paid,payments
    YZhat,YZ,YZpay=crosses(Z,EZ,NZ,'Z');YRhat,YR,YRpay=crosses(R,ER,NR,'R');result=analyze(idx,YY,YZ,YR)
    print(parity,'conditional inverse improvement',[float(F(v)) for v in result['conditional_frozen_witness_inverse_improvement']],'joined pass',result['conditional_joined_Schur_certificate_passed'],flush=True)
    return dict(milestone='NF42',parity=parity,aperture='53/50',NF41_input_sha256=SHA41,authenticated_native_input_sha256=hashes,interval_grid_digits=500,regular_kernel_N=320,pole_degree=40,original_translation_cells=13,
        boundary_mode_indices=ids,boundary_source_low_projection_intervals=p.prev.ends(lowY),boundary_source_physical_errors=list(map(str,EY)),boundary_approximant_norm_upper=list(map(str,NY)),
        old_high_source_physical_errors=list(map(str,EZ)),old_high_approximant_norm_upper=list(map(str,NZ)),joined_source_physical_errors=list(map(str,ER)),joined_approximant_norm_upper=list(map(str,NR)),
        reconstructed_boundary_source_Gram=p.prev.ends(YYhat),boundary_source_Gram_payments=[[str(v) for v in row] for row in paymentsYY],original_boundary_source_Gram=p.prev.ends(YY),
        reconstructed_boundary_old_high_source_crosses=p.prev.ends(YZhat),boundary_old_high_source_cross_payments=[[str(v) for v in row] for row in YZpay],original_boundary_old_high_source_crosses=p.prev.ends(YZ),
        reconstructed_boundary_joined_source_crosses=p.prev.ends(YRhat),boundary_joined_source_cross_payments=[[str(v) for v in row] for row in YRpay],original_boundary_joined_source_crosses=p.prev.ends(YR),
        actual_negative_original_form_claimed=False,whole_aperture_positive=False,highest_certified_whole_aperture='21/20',RH=False,F4=False,Lean=False,**result)
if __name__=='__main__':
    q=argparse.ArgumentParser();q.add_argument('--parity',choices=['even','odd'],required=True);q.add_argument('--output',required=True);q=q.parse_args();Path(q.output).write_text(json.dumps(run(q.parity),indent=2)+'\n')
