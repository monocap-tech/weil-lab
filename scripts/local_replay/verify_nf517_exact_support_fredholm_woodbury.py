#!/usr/bin/env python3
"""NF517 exact rational Woodbury/Fredholm localized refit gain controls.

Finite-dimensional odd physical probes. Not an original-source J242
numerical cell calculation, nor Weil/RH certificate.
"""
import argparse,json
from pathlib import Path
from fractions import Fraction as Q
def dot(a,b):return sum((x*y for x,y in zip(a,b)),Q(0))
def trans(a):return [list(v) for v in zip(*a)]
def mm(a,b):
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))),Q(0))
             for j in range(len(b[0]))] for i in range(len(a))]
def inv(a):
    n=len(a);t=[list(a[i])+[Q(int(i==j)) for j in range(n)] for i in range(n)]
    for j in range(n):
        k=next((k for k in range(j,n) if t[k][j]),None);assert k is not None
        t[j],t[k]=t[k],t[j];p=t[j][j];t[j]=[z/p for z in t[j]]
        for i in range(n):
            if i!=j:
                p=t[i][j];t[i]=[z-p*y for z,y in zip(t[i],t[j])]
    return [r[n:] for r in t]
def mv(a,v):return [dot(row,v) for row in a]
def gram(J,w,index):
    return [[sum((w[t]*J[t][i]*J[t][j] for t in index),Q(0))
             for j in range(len(J[0]))] for i in range(len(J[0]))]
def one(m,offset,remove):
    x=[Q(i+1,m+3) for i in range(m)]
    x=x+[-v for v in x];w=[Q(1,2)]*len(x)
    J=[[v,v**3] for v in x]
    a=[Q(1,7)+offset,-Q(9,23)]
    W=[dot(z,a)+v**5+v**7/Q(11) for v,z in zip(x,J)]
    O=list(range(len(x)))
    D=[k for k in O if k%m in remove]
    keep=[k for k in O if k not in D]
    G=gram(J,w,O);Gi=inv(G)
    b=[sum((w[t]*J[t][i]*W[t] for t in O),Q(0)) for i in range(2)]
    aa=mv(Gi,b)
    r=[W[t]-dot(J[t],aa) for t in O]
    assert all(sum((w[t]*r[t]*J[t][i] for t in O),Q(0))==0 for i in range(2))
    R=sum((w[t]*r[t]**2 for t in O),Q(0))
    Gnew=gram(J,w,keep)
    bnew=[sum((w[t]*J[t][i]*W[t] for t in keep),Q(0)) for i in range(2)]
    Rnew=sum((w[t]*W[t]**2 for t in keep),Q(0))-dot(bnew,mv(inv(Gnew),bnew))
    C=gram(J,w,D)
    k=[sum((w[t]*J[t][i]*r[t] for t in D),Q(0)) for i in range(2)]
    e=sum((w[t]*r[t]**2 for t in D),Q(0))
    gain=e+dot(k,mv(inv(Gnew),k))
    JD=[J[t] for t in D];K=mm(mm(JD,Gi),trans(JD))
    IK=[[int(i==j)-w[D[j]]*K[i][j] for j in range(len(D))] for i in range(len(D))]
    f=mv(inv(IK),[r[t] for t in D])
    operator_gain=sum((w[D[i]]*r[D[i]]*f[i] for i in range(len(D))),Q(0))
    assert 0<=Rnew<R and gain==operator_gain==R-Rnew
    tau=sum((mm(Gi,C)[i][i] for i in range(2)),Q(0))
    return tau,operator_gain
def main():
    cases=0;high=False
    for m in (6,7,8):
        for offset in (Q(0),Q(15,17),Q(10**15)):
            for remove in ((m-1,),tuple(range(m-3,m)),tuple(range(2,m))):
                tau,gain=one(m,offset,remove)
                assert gain>=0
                high|=tau>1;cases+=1
    assert cases==27 and high
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);o=p.parse_args()
    result={'pass':'NF517-exact-Fraction-Fredholm-support-removal-identity',
       'algebraic_controls':cases,'trace_leverage_greater_than_one_tested':True,
       'identity':'R(O\\D)=R(O)-<r_D,(I-K_D)^-1 r_D>_D',
       'kernel':'K_O(x,y)=J(x)^T G_O^-1 J(y)',
       'strict_spectral_gap_condition':'G_(O\\D)>0',
       'scope':'Exact discrete odd-function algebra controls only; original selected J242 kernel and named physical values OPEN',
       'original_selected_dimension':242,'actual_original_J242_local_kernel_integrated':False,
       'original_global_242D_fitted_eH':'OPEN','NF404_named_patch':'OPEN',
       'Weil_source_image_graph_domain':'OPEN','W_ODD_NEG':'OPEN','RH':'OPEN'}
    Path(o.output).write_text(json.dumps(result,indent=2)+'\n')
    print('NF517 27 exact-rational localized kernel refit controls PASS')
    print('Method valid even with trace leverage >1; original J242 values and RH OPEN')
if __name__=='__main__':main()
