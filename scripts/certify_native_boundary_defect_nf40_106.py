#!/usr/bin/env python3
"""NF40: paid native boundary defect and exact zero-response extension."""
import argparse,hashlib,json,sys
sys.set_int_max_str_digits(0)
from pathlib import Path
from fractions import Fraction as F
import certify_native_sharp_inverse_packet_nf39_106 as c
p=c.p;n=c.n;I=c.I;K=c.K

def eye(m):return [[F(int(i==j)) for j in range(m)] for i in range(m)]
def basis(m,start,count):return [[F(int(i==j+start)) for j in range(count)] for i in range(m)]
def inverse(A):
    m=len(A);B=[row[:]+eye(m)[i] for i,row in enumerate(A)]
    for j in range(m):
        k=next(k for k in range(j,m) if B[k][j]);B[j],B[k]=B[k],B[j]
        d=B[j][j];B[j]=[v/d for v in B[j]]
        for i in range(m):
            if i!=j:
                d=B[i][j];B[i]=[v-d*w for v,w in zip(B[i],B[j])]
    out=[row[m:] for row in B];assert c.mm(A,out)==eye(m) and c.mm(out,A)==eye(m)
    return out

def inputs(idx):
    native,source,hashes=p.p.old.prev.inputs();d38,_=c.parents();d36=p.prev.parents()[0]
    a,parent=c.packet_inputs(idx);trial=d38[idx];ids=[112+idx,114+idx]
    z0=dict(zip(trial['correction_indices'],map(F,trial['old_correction_coefficients'])))
    z1=dict(zip(trial['correction_indices'],map(F,trial['fixed_rational_second_correction_coefficients'])))
    X=[[z0[i],z1[i]] for i in ids];o=d36[idx+2]
    co0=dict(zip(o['correction_source_coordinate_indices'],map(p.iv,o['reconstructed_correction_source_coordinates'])))
    co1=dict(zip(parent['correction_source_coordinate_indices'],map(p.iv,parent['reconstructed_correction_source_coordinates'])))
    errors=[F(o['correction_source_error_upper']),F(parent['correction_source_error_upper'])]
    P=[[co0[i].mid()-K*z0[i],co1[i].mid()-K*z1[i]] for i in ids]
    Pi=[[co0[i]+I(-errors[0],errors[0])-K*z0[i],co1[i]+I(-errors[1],errors[1])-K*z1[i]] for i in ids]
    QYi=[[I(*map(F,source[f'{min(i,j)},{max(i,j)}']['full'])) for j in ids] for i in ids]
    QY=[[v.mid() for v in row] for row in QYi]
    qi=p.prev.matrix(parent['joint_native_high_block']);Ci=[[qi[i][j]-K*a['M'][i][j] for j in range(2)] for i in range(2)]
    det=Ci[0][0]*Ci[1][1]-n.sq(Ci[0][1]);assert Ci[0][0].l>0 and det.l>0
    CI=[[Ci[1][1]/det,-Ci[0][1]/det],[-Ci[1][0]/det,Ci[0][0]/det]]
    DY=[[QYi[i][j]-K*int(i==j)-p.dot(Pi[i],p.mv(CI,Pi[j])) for j in range(2)] for i in range(2)]
    # Symmetric true compression: intersect the two outward off-diagonal enclosures.
    lo=max(DY[0][1].l,DY[1][0].l);hi=min(DY[0][1].h,DY[1][0].h);assert lo<=hi
    DY[0][1]=DY[1][0]=I(F(lo,n.SCALE),F(hi,n.SCALE))
    dd=DY[0][0]*DY[1][1]-n.sq(DY[0][1]);assert DY[0][0].l>0 and dd.l>0
    trace=(DY[0][0]+DY[1][1])/dd;gap=1/F(trace.h,n.SCALE);assert gap>0
    return a,ids,X,P,QY,DY,dd,gap,Pi,QYi,hashes

def extension(a,X,P,QY):
    G,C,_,_=c.gram_and_surplus(a);MI=c.inverse2(a['M']);CI=c.inverse2(C)
    inv7=c.decode(c.model(a,F(0))['exact_high_inverse']);R7=basis(7,4,3);ar7=c.mm(inv7,R7)
    target=c.mm(c.mm(X,MI),c.mm(G[:2],ar7));PV=c.mm(P,ar7[2:4])
    YR=c.scale(c.add(target,c.scale(PV,-1)),K)
    G9=[row+[F(0)]*2 for row in G]+[[F(0)]*9 for _ in range(2)]
    for i in range(2):
        for j,v in enumerate(X[i]+P[i]+YR[i]):G9[i+7][j]=G9[j][i+7]=v
        for j in range(2):G9[i+7][j+7]=F(int(i==j))
    _,gd=c.ldl(G9);assert min(gd)>0
    Z,V,R,Y=(basis(9,s,k) for s,k in [(0,2),(2,2),(4,3),(7,2)])
    adj=lambda B:c.mm(c.tr(B),G9)
    A0=c.add(c.scale(eye(9),K),c.mm(c.mm(V,CI),adj(V)))
    DV=c.scale(V,1/K);N=c.add(C,c.mm(adj(V),DV))
    ai0=c.add(c.scale(eye(9),1/K),c.scale(c.mm(c.mm(DV,c.inverse2(N)),c.scale(adj(V),1/K)),-1))
    assert c.mm(A0,ai0)==eye(9)
    Yt=c.add(Y,c.scale(c.mm(c.mm(Z,MI),c.tr(X)),-1))
    L=c.mm(adj(Yt),Yt);_,ld=c.ldl(L);assert min(ld)>0;LI=c.inverse2(L)
    D=c.add(c.add(QY,c.scale(eye(2),-K)),c.scale(c.mm(c.mm(P,CI),c.tr(P)),-1))
    _,dd=c.ldl(D);assert min(dd)>0
    Dcal=c.mm(c.mm(c.mm(Yt,c.mm(c.mm(LI,D),LI)),c.tr(Yt)),G9)
    assert c.mm(Dcal,Z)==[[F(0)]*2 for _ in range(9)]
    assert c.mm(adj(Y),c.mm(Dcal,Y))==D
    assert c.mm(Dcal,c.mm(ai0,R))==[[F(0)]*3 for _ in range(9)]
    Aminus=c.add(A0,Dcal)
    W=c.mm(ai0,Yt);N=c.add(c.mm(c.mm(L,c.inverse2(D)),L),c.mm(adj(Yt),W))
    aim=c.add(ai0,c.scale(c.mm(c.mm(W,c.inverse2(N)),c.mm(adj(Yt),ai0)),-1))
    assert c.mm(Aminus,aim)==eye(9) and c.mm(aim,Aminus)==eye(9)
    assert c.mm(G9,Aminus)==c.tr(c.mm(G9,Aminus))
    assert c.mm(Aminus,Z)==c.add(c.scale(Z,K),V)
    assert c.mm(adj(Y),c.mm(Aminus,Y))==QY
    J=c.mm(adj(R),c.mm(aim,R));assert J==c.reaction(a,F(0))
    S=c.add(a['Q'],c.scale(J,-1));_,sd=c.ldl(S);assert sd[0]>0 and sd[1]>0 and sd[2]<0
    # All factors below are exact; positive definiteness follows from kappa I plus PSD factors.
    return dict(exact_nine_vector_Gram=c.strings(G9),Gram_LDL_pivots_positive=[v>0 for v in gd],free_boundary_joined_source_crosses=c.strings(YR),
        projected_boundary_Gram=c.strings(L),projected_boundary_Gram_LDL_pivots=list(map(str,ld)),
        exact_boundary_defect=c.strings(D),boundary_defect_LDL_pivots=list(map(str,dd)),
        operator_recipe='Aminus=kappa I+V C^-1 V*+Ytilde L^-1 D L^-1 Ytilde*; Ytilde=Y-Z M^-1 X^T',
        exact_reaction=c.strings(J),exact_joined_Schur=c.strings(S),Schur_LDL_pivots=list(map(str,sd)),
        all_original_aggregate_moments_matched=True,native_boundary_energy_block_matched=True,zero_inverse_improvement_on_all_three_joined_sources=True,
        free_boundary_source_crosses_are_actual_original_pairings=False,abstract_model_only=True,full_Weil_identities_matched=False)

def run(parity):
    idx=['even','odd'].index(parity);a,ids,X,P,QY,DY,dd,gap,Pi,QYi,hashes=inputs(idx)
    model=extension(a,X,P,QY)
    print(parity,'native boundary defect gap >',float(gap),'expanded exact packet still permits zero joined inverse improvement',flush=True)
    return dict(milestone='NF40',parity=parity,aperture='53/50',kappa=str(K),NF38_input_sha256=c.SHA38,native_input_hashes=hashes,
        boundary_mode_indices=ids,exact_boundary_Z_crosses=c.strings(X),paid_boundary_V_crosses=p.prev.ends(Pi),original_native_boundary_energy_intervals=p.prev.ends(QYi),
        actual_boundary_defect_intervals=p.prev.ends(DY),actual_boundary_defect_determinant=dd.ends(),physical_boundary_defect_gap_strict_lower=str(gap),
        exact_aggregate_packet={k:c.strings(v) for k,v in a.items()},chosen_boundary_V_crosses=c.strings(P),chosen_boundary_energy=c.strings(QY),zero_response_extension=model,
        actual_original_inverse_improvement_certified=False,actual_negative_original_form_claimed=False,whole_high_defect_gap_claimed=False,
        whole_aperture_positive=False,highest_certified_whole_aperture='21/20',RH=False,F4=False,Lean=False)
if __name__=='__main__':
    q=argparse.ArgumentParser();q.add_argument('--parity',choices=['even','odd'],required=True);q.add_argument('--output',required=True);q=q.parse_args()
    Path(q.output).write_text(json.dumps(run(q.parity),indent=2)+'\n')
