#!/usr/bin/env python3
"""NF41: signed original boundary/source crosses and fixed-cross response audit."""
import argparse,hashlib,json
from pathlib import Path
from fractions import Fraction as F
import certify_native_boundary_defect_nf40_106 as b
c=b.c;p=b.p;n=b.n;I=b.I;K=b.K
SHA40=['997aba46defbae2127c9d70e187efb9602cab10c5ef6ca20bec3be60c993872c','2f425d32f8779b2fe7b690e15c24a9378e416e00eafc7cce79dfc9d892c603e2','cdb914cdd7e8b8d0575d9f1f997ad0b5d3a22696a77fe0d5f2ce42e542ae949c']
def parents():
    names=['EVEN_BOUNDARY_DEFECT_CERTIFICATE','ODD_BOUNDARY_DEFECT_CERTIFICATE','BOUNDARY_DEFECT_VALIDATION']
    raw=[Path('notes/data/RPB108_NF40_'+v+'_20261009.json').read_bytes() for v in names]
    assert [hashlib.sha256(v).hexdigest() for v in raw]==SHA40
    out=list(map(json.loads,raw));assert out[-1]['status']=='PASS';return out

def im(A):return [[I(v) for v in row] for row in A]
def inverse2_interval(A):
    d=A[0][0]*A[1][1]-n.sq(A[0][1]);assert A[0][0].l>0 and d.l>0
    return [[A[1][1]/d,-A[0][1]/d],[-A[1][0]/d,A[0][0]/d]]
def coupling(idx,YR):
    a,ids,X,P,QY,DY,dd,gap,Pi,QYi,hashes=b.inputs(idx);_,parent=c.packet_inputs(idx)
    QZ=p.prev.matrix(parent['joint_native_high_block']);GZ=p.prev.matrix(parent['joint_complete_source_high_block'])
    B=p.prev.matrix(parent['joint_native_joined_high_crosses']);S=p.prev.matrix(parent['joint_complete_source_joined_high_crosses'])
    C=c.add(QZ,c.scale(im(a['M']),-K));T=c.add(c.add(GZ,c.scale(QZ,-2*K)),c.scale(im(a['M']),K*K))
    N=c.add(C,c.scale(T,1/K));NI=inverse2_interval(N);W=c.add(S,c.scale(B,-K))
    XM=c.mm(im(X),im(c.inverse2(a['M'])))
    yr=c.add(YR,c.scale(c.mm(XM,c.tr(B)),-1));pv=c.add(Pi,c.scale(c.mm(XM,C),-1))
    H=c.add(c.scale(yr,1/K),c.scale(c.mm(c.mm(pv,NI),c.tr(W)),-1/(K*K)))
    h=list(map(F,parent['joint_universal_fixed_rational_witness']));hw=p.mv(H,h);square=sum((n.sq(v) for v in hw),I(0));assert square.l>0
    return H,h,hw,square

def model(idx,YR):
    a,ids,X,P,QY,*_=b.inputs(idx);G7,C,_,_=c.gram_and_surplus(a)
    G=[row+[F(0)]*2 for row in G7]+[[F(0)]*9 for _ in range(2)]
    for i in range(2):
        for j,v in enumerate(X[i]+P[i]+YR[i]):G[i+7][j]=G[j][i+7]=v
        for j in range(2):G[i+7][j+7]=F(int(i==j))
    _,gd=c.ldl(G);assert min(gd)>0
    Z,V,R,Y=(b.basis(9,s,k) for s,k in [(0,2),(2,2),(4,3),(7,2)])
    adj=lambda U:c.mm(c.tr(U),G)
    A0=c.add(c.scale(b.eye(9),K),c.mm(c.mm(V,c.inverse2(C)),adj(V)));AI=b.inverse(A0);AR=c.mm(AI,R)
    SP=[z+ar for z,ar in zip(Z,AR)];SG=c.mm(adj(SP),SP);_,sgd=c.ldl(SG);assert min(sgd)>0
    Yhat=c.add(Y,c.scale(c.mm(c.mm(SP,b.inverse(SG)),c.mm(adj(SP),Y)),-1))
    L=c.mm(adj(Yhat),Yhat);_,ld=c.ldl(L);assert min(ld)>0
    D=c.add(c.add(QY,c.scale(b.eye(2),-K)),c.scale(c.mm(c.mm(P,c.inverse2(C)),c.tr(P)),-1));_,dp=c.ldl(D);assert min(dp)>0
    Dc=c.mm(c.mm(Yhat,c.mm(c.mm(c.inverse2(L),D),c.inverse2(L))),adj(Yhat));A=c.add(A0,Dc)
    assert c.mm(Dc,SP)==[[F(0)]*5 for _ in range(9)] and c.mm(A,AR)==R
    assert c.mm(G,A)==c.tr(c.mm(G,A)) and c.mm(A,Z)==c.add(c.scale(Z,K),V)
    assert c.mm(adj(Y),c.mm(A,Y))==QY
    J=c.mm(adj(R),AR);assert J==c.reaction(a,F(0));Schur=c.add(a['Q'],c.scale(J,-1));_,sd=c.ldl(Schur);assert sd[0]>0 and sd[1]>0 and sd[2]<0
    return dict(exact_nine_vector_Gram=c.strings(G),Gram_LDL_pivots_positive=[v>0 for v in gd],annihilated_span_Gram_LDL_pivots_positive=[v>0 for v in sgd],projected_boundary_Gram=c.strings(L),projected_boundary_Gram_positive=True,
        operator_recipe='S=(Z,A0^-1 R); Yhat=(I-P_span(S))Y; L=Yhat*Yhat; Aminus=A0+Yhat L^-1 D L^-1 Yhat*',
        exact_reaction=c.strings(J),exact_joined_Schur=c.strings(Schur),Schur_LDL_pivots=list(map(str,sd)),
        all_NF39_aggregate_moments_and_NF40_boundary_energy_matched=True,new_signed_boundary_source_crosses_matched=True,zero_inverse_improvement_on_all_three_joined_sources=True,
        abstract_enclosure_compatible_model_only=True,full_Weil_identities_matched=False,actual_unknown_exact_moments_matched=False)

def run(parity):
    idx=['even','odd'].index(parity);parent=parents()[idx];data,source,hashes=p.p.old.prev.inputs();o=p.objects(data,source,parity);ids=parent['boundary_mode_indices']
    m=p.p.old.probe.Moments(720,parity);measured=[[] for _ in ids];reverse=[[] for _ in ids];payments=[]
    for k,(ii,cc) in enumerate(o['columns']):
        s=m.source(ii,cc);error=m.eta*p.p.norm(cc);payments.append(error)
        for j,y in enumerate(ids):measured[j].append(m.pair(s,n.basis(y)))
        # Symmetry control uses the independent boundary source action on the frozen polynomial.
        for j,y in enumerate(ids):
            sy=m.source([y],[F(1)]);reverse[j].append(m.pair(sy,s[0]))
        print(parity,'certified boundary coordinates of joined column',k,flush=True)
    YR=[[v+I(-payments[k],payments[k]) for k,v in enumerate(row)] for row in measured]
    for j in range(2):
        for k in range(3):
            rev=reverse[j][k]+I(-payments[k],payments[k]);assert max(rev.l,YR[j][k].l)<=min(rev.h,YR[j][k].h)
    H,h,hw,square=coupling(idx,YR);chosen=[[v.mid() for v in row] for row in YR];extension=model(idx,chosen)
    print(parity,'nonzero native boundary inverse coupling; fixed-cross packet still permits zero response',flush=True)
    return dict(milestone='NF41',parity=parity,aperture='53/50',kappa=str(K),NF40_input_sha256=SHA40,authenticated_native_input_sha256=hashes,
        interval_grid_digits=500,regular_kernel_N=320,pole_degree=40,original_translation_cells=13,boundary_mode_indices=ids,
        frozen_joined_polynomial_columns=[dict(indices=ii,coefficients=list(map(str,cc))) for ii,cc in o['columns']],
        reconstructed_boundary_source_crosses=p.prev.ends(measured),physical_source_error_payments=list(map(str,payments)),original_signed_boundary_source_crosses=p.prev.ends(YR),reverse_reconstructed_native_crosses=p.prev.ends(reverse),
        original_projected_boundary_A0_inverse_source_coupling=p.prev.ends(H),fixed_NF38_witness=list(map(str,h)),original_witness_boundary_inverse_coupling=[v.ends() for v in hw],original_witness_boundary_inverse_coupling_square=square.ends(),
        NF40_specific_span_boundary_zero_response_model_excluded=True,chosen_enclosure_compatible_boundary_source_crosses=c.strings(chosen),fixed_cross_zero_response_extension=extension,
        actual_inverse_improvement_lower_bound_certified=False,actual_negative_original_form_claimed=False,whole_aperture_positive=False,highest_certified_whole_aperture='21/20',RH=False,F4=False,Lean=False)
if __name__=='__main__':
    q=argparse.ArgumentParser();q.add_argument('--parity',choices=['even','odd'],required=True);q.add_argument('--output',required=True);q=q.parse_args();Path(q.output).write_text(json.dumps(run(q.parity),indent=2)+'\n')
