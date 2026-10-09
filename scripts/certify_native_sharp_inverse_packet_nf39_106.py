#!/usr/bin/env python3
"""NF39: sharp packet envelope and exact moment-preserving opposite signs."""
import argparse,hashlib,json
from pathlib import Path
from fractions import Fraction as F
import certify_native_second_high_direction_nf38_106 as p
n=p.n;I=p.I;iv=p.iv;K=p.K
NAMES=['EVEN_FIXED_SECOND_HIGH_DIRECTION','ODD_FIXED_SECOND_HIGH_DIRECTION','EVEN_SECOND_HIGH_DIRECTION_CERTIFICATE','ODD_SECOND_HIGH_DIRECTION_CERTIFICATE','SECOND_HIGH_DIRECTION_VALIDATION']
SHA38=['05f3bcbc81e8d5f133fc5e49b61d80f8d1d4d6e65f1953d7dc65089b699ab5fd','3580ada8f259f02beeddedef5ab28e08cc96a2928c98cdc99390d337c54bad91','b6f7134f131dc2698868d676494d171e40340e81c453fb67d0e80520e082ce37','d0dee22dd8803b9f9b2545650a3f0ada382e55d10a36c834bf3350288161aa8c','f64f6d2d7f062b7e4306c8c74dc50c8370c266db9e424e79df8e40526b3cda96']
def parents():
    raw=[Path('notes/data/RPB108_NF38_'+v+'_20261009.json').read_bytes() for v in NAMES]
    assert [hashlib.sha256(v).hexdigest() for v in raw]==SHA38
    out=list(map(json.loads,raw));assert out[-1]['status']=='PASS';old=p.parents()[0]
    for i in range(2):assert out[i+2]['NF37_input_sha256']==p.SHA37 and out[i+2]['fixed_trial_sha256']==SHA38[i]
    return out,old
def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def mv(A,x):return [dot(row,x) for row in A]
def tr(A):return list(map(list,zip(*A)))
def mm(A,B):return [[dot(row,col) for col in zip(*B)] for row in A]
def add(A,B):return [[a+b for a,b in zip(x,y)] for x,y in zip(A,B)]
def scale(A,s):return [[s*v for v in row] for row in A]
def inverse2(A):
    d=A[0][0]*A[1][1]-A[0][1]*A[1][0];assert d>0
    return [[A[1][1]/d,-A[0][1]/d],[-A[1][0]/d,A[0][0]/d]]
def ldl(A):
    m=len(A);L=[[F(int(i==j)) for j in range(m)] for i in range(m)];D=[]
    for j in range(m):
        d=A[j][j]-sum((L[j][k]**2*D[k] for k in range(j)),F(0));assert d!=0;D.append(d)
        for i in range(j+1,m):L[i][j]=(A[i][j]-sum((L[i][k]*L[j][k]*D[k] for k in range(j)),F(0)))/d
    assert mm(mm(L,[[D[i] if i==j else F(0) for j in range(m)] for i in range(m)]),tr(L))==A
    return L,D
def strings(A):return [list(map(str,row)) for row in A]
def decode(A):return [list(map(F,row)) for row in A]
def symmetric_mid(A):
    m=len(A);out=[[F(0)]*m for _ in range(m)]
    for i in range(m):
        for j in range(i,m):
            a,b=iv(A[i][j]),iv(A[j][i]);lo=max(a.l,b.l);hi=min(a.h,b.h);assert lo<=hi
            out[i][j]=out[j][i]=F(lo+hi,2*n.SCALE)
    return out
def rectangle_mid(A):return [[iv(v).mid() for v in row] for row in A]
def packet_inputs(idx):
    data,old=parents();trial=data[idx];cert=data[idx+2];prior=old[idx]
    z0=list(map(F,trial['old_correction_coefficients']));z1=list(map(F,trial['fixed_rational_second_correction_coefficients']))
    assert sum(a*b for a,b in zip(z0,z1))==0
    M=[[sum(v*v for v in z0),F(0)],[F(0),sum(v*v for v in z1)]]
    Q=symmetric_mid(prior['original_selected_native_energy_Gram']);G=symmetric_mid(prior['original_selected_complete_source_Gram'])
    QZ=symmetric_mid(cert['joint_native_high_block']);GZ=symmetric_mid(cert['joint_complete_source_high_block'])
    B=rectangle_mid(cert['joint_native_joined_high_crosses']);S=rectangle_mid(cert['joint_complete_source_joined_high_crosses'])
    return dict(M=M,Q=Q,G=G,QZ=QZ,GZ=GZ,B=B,S=S),cert
def gram_and_surplus(a):
    M,QZ,GZ,B,S,G=(a[k] for k in ['M','QZ','GZ','B','S','G'])
    C=add(QZ,scale(M,-K));T=add(add(GZ,scale(QZ,-2*K)),scale(M,K*K));W=add(S,scale(B,-K))
    gram=[[F(0)]*7 for _ in range(7)]
    for i in range(2):
        for j in range(2):gram[i][j]=M[i][j];gram[i][j+2]=gram[j+2][i]=C[i][j];gram[i+2][j+2]=T[i][j]
        for j in range(3):gram[i][j+4]=gram[j+4][i]=B[j][i];gram[i+2][j+4]=gram[j+4][i+2]=W[j][i]
    for i in range(3):
        for j in range(3):gram[i+4][j+4]=G[i][j]
    return gram,C,T,W
def reaction(a,delta):
    _,C,T,W=gram_and_surplus(a);MI=inverse2(a['M']);B=a['B'];G=a['G']
    alpha=1/(K+delta);beta=1/K-alpha
    X=add(scale(T,alpha),scale(mm(mm(C,MI),C),beta))
    Y=add(scale(W,alpha),scale(mm(mm(B,MI),C),beta))
    R0=add(scale(G,alpha),scale(mm(mm(B,MI),tr(B)),beta))
    N=add(C,X);_,ds=ldl(N);assert min(ds)>0
    return add(R0,scale(mm(mm(Y,inverse2(N)),tr(Y)),-1))
def model(a,delta):
    gram,C,_,_=gram_and_surplus(a);m=7
    eye=[[F(int(i==j)) for j in range(m)] for i in range(m)]
    Z=[[F(int(i==j)) for j in range(2)] for i in range(m)]
    V=[[F(int(i==j+2)) for j in range(2)] for i in range(m)]
    Pz=mm(mm(Z,inverse2(a['M'])),mm(tr(Z),gram));P=add(eye,scale(Pz,-1))
    A=add(add(scale(eye,K),scale(P,delta)),mm(mm(V,inverse2(C)),mm(tr(V),gram)))
    Dinv=add(scale(eye,1/(K+delta)),scale(Pz,1/K-1/(K+delta)))
    DV=mm(Dinv,V);N=add(C,mm(mm(tr(V),gram),DV))
    inv=add(Dinv,scale(mm(mm(DV,inverse2(N)),mm(mm(tr(V),gram),Dinv)),-1))
    assert mm(A,inv)==eye and mm(inv,A)==eye and mm(gram,A)==tr(mm(gram,A))
    assert mm(P,Z)==[[F(0)]*2 for _ in range(7)]
    assert mm(A,Z)==add(scale(Z,K),V)
    R=[[F(int(i==j+4)) for j in range(3)] for i in range(m)]
    J=mm(mm(tr(R),gram),mm(inv,R));assert J==reaction(a,delta)
    Schur=add(a['Q'],scale(J,-1));L,D=ldl(Schur)
    return dict(delta=str(delta),high_operator=strings(A),exact_high_inverse=strings(inv),reaction=strings(J),Schur=strings(Schur),Schur_LDL_pivots=list(map(str,D)))
def run(parity):
    idx=['even','odd'].index(parity);a,cert=packet_inputs(idx);gram,C,T,W=gram_and_surplus(a)
    _,gd=ldl(gram);_,cd=ldl(C);_,qd=ldl(a['Q']);assert min(gd)>0 and min(cd)>0 and min(qd)>0
    negative=model(a,F(0));positive=model(a,F(1))
    assert F(negative['Schur_LDL_pivots'][0])>0 and F(negative['Schur_LDL_pivots'][1])>0 and F(negative['Schur_LDL_pivots'][2])<0
    assert min(map(F,positive['Schur_LDL_pivots']))>0
    # Exact Woodbury/NF38 identity at the chosen rational packet.
    H=add(a['QZ'],scale(a['GZ'],-1/K));E=add(a['B'],scale(a['S'],-1/K))
    ceiling=add(add(a['Q'],scale(a['G'],-1/K)),scale(mm(mm(E,inverse2(H)),tr(E)),-1))
    assert ceiling==decode(negative['Schur'])
    # The actual uncertain packet also has a positive surplus C.
    qi=p.prev.matrix(cert['joint_native_high_block']);Ci=[[qi[i][j]-K*a['M'][i][j] for j in range(2)] for i in range(2)]
    cdet=Ci[0][0]*Ci[1][1]-n.sq(Ci[0][1]);assert Ci[0][0].l>0 and cdet.l>0
    h=list(map(F,cert['joint_universal_fixed_rational_witness']));vi=p.prev.matrix(cert['joint_functional_ceiling']);value=p.dot(h,p.mv(vi,h));assert value.h<0
    necessary=-F(value.h,n.SCALE)
    print(parity,'exact aggregate packet admits opposite Schur signs; necessary witness improvement >',float(necessary),flush=True)
    return dict(milestone='NF39',parity=parity,aperture='53/50',kappa=str(K),NF38_input_sha256=SHA38,NF37_input_sha256=p.SHA37,
        exact_packet={k:strings(v) for k,v in a.items()},exact_seven_vector_high_Gram=strings(gram),exact_Gram_LDL_pivots=list(map(str,gd)),
        exact_positive_high_surplus=strings(C),exact_surplus_LDL_pivots=list(map(str,cd)),actual_high_surplus_intervals=p.prev.ends(Ci),actual_high_surplus_determinant=cdet.ends(),
        negative_minimal_background_model=negative,positive_moment_preserving_background_model=positive,
        sharp_Woodbury_envelope_equals_NF38_ceiling=True,exact_same_aggregate_moments_opposite_schur_signs=True,
        necessary_actual_inverse_improvement_witness=list(map(str,h)),actual_ceiling_witness_value=value.ends(),necessary_inverse_improvement_strict_lower=str(necessary),
        abstract_model_only=True,full_Weil_identities_matched=False,exact_original_polynomial_coordinates_matched=False,
        actual_original_inverse_certified=False,actual_negative_original_form_claimed=False,joined_retained_dimension_certified=4,whole_aperture_positive=False,RH=False,F4=False,Lean=False)
if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('--parity',choices=['even','odd'],required=True);a.add_argument('--output',required=True);a=a.parse_args()
    Path(a.output).write_text(json.dumps(run(a.parity),indent=2)+'\n')
