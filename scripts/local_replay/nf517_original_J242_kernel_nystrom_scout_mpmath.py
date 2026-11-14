#!/usr/bin/env python3
"""NF517 ORIGINAL source physical 242D Fredholm/Nystrom numerical SCOUT.

Independent analytic raw 242D physical Gram; historic D implicitly via
Cholesky, but NO 4096-bit Arb interval acceptance or quadrature remainder.
All numerical values are research candidates, NEVER source certificates.
"""
from __future__ import annotations
import argparse,hashlib,json,math,time
from fractions import Fraction as F
from pathlib import Path
import mpmath as mp
import numpy as np
from numpy.polynomial.legendre import leggauss

NF505='ad4afeaa4c7d8f48dfc270c437362287d8e2a21d9cce5b385c071e358431d2ec'
NF494='39cba367d70243c2d15e5a9323fc8097d58187923dcf0eca2b031136871f0181'
SRC='0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce'
SEAM='c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675'

def read(p):
    b=Path(p).read_bytes()
    return json.loads(b),hashlib.sha256(b).hexdigest()
def rational(v):
    z=F(v);return mp.mpf(z.numerator)/z.denominator
def bmid(a):return (rational(a[0])+rational(a[1]))/2
def dmid(ball):
    m,e=ball[0];return mp.mpf(m)*mp.power(2,e)
def forward(L,vec):
    y=[mp.mpf(0)]*len(vec)
    for i in range(len(vec)):
        y[i]=(vec[i]-sum((L[i,j]*y[j] for j in range(i)),mp.mpf(0)))/L[i,i]
    return y
def backward(L,vec):
    y=[mp.mpf(0)]*len(vec)
    for i in reversed(range(len(vec))):
        y[i]=(vec[i]-sum((L[j,i]*y[j] for j in range(i+1,len(vec))),mp.mpf(0)))/L[i,i]
    return y
def integrals(frequencies,b):
    freqs=sorted(set(abs(f-g) for f in frequencies for g in frequencies)
                 |set(f+g for f in frequencies for g in frequencies))
    C={};S={}
    for f in freqs:
        if f==0:
            C[f]=[2*b**(n+1)/(n+1) if n%2==0 else mp.mpf(0) for n in range(27)]
            S[f]=[mp.mpf(0)]*27;continue
        w=2*mp.pi*rational(f);sn=mp.sin(w*b);cs=mp.cos(w*b)
        cc=[mp.mpf(0)]*27;ss=[mp.mpf(0)]*27
        cc[0]=2*sn/w
        for n in range(1,27):
            if n%2:ss[n]=-2*b**n*cs/w+n*cc[n-1]/w
            else:cc[n]=2*b**n*sn/w-n*ss[n-1]/w
        C[f]=cc;S[f]=ss
    return C,S
def exponential_moments(z,b):
    ep=mp.exp(z*b);em=mp.exp(-z*b);out=[(ep-em)/z]
    for n in range(1,14):
        out.append((b**n*ep-(-b)**n*em)/z-n*out[-1]/z)
    return out
def physical_gram(nodes,b):
    fs=sorted(set(f for f,k in nodes if f is not None))
    C,S=integrals(fs,b);pole={}
    for f in fs:
        w=2*mp.pi*rational(f)
        u=exponential_moments(mp.mpf('.5')+1j*w,b)
        v=exponential_moments(-mp.mpf('.5')+1j*w,b)
        pole[f]=[(u[i]-v[i])/2 for i in range(14)]
    n=len(nodes);H=mp.matrix(n)
    for i,(f,k) in enumerate(nodes):
        for j in range(i+1):
            g,l=nodes[j]
            if f is None and g is None:val=mp.sinh(b)-b
            elif f is None:
                z=pole[g][l];val=z.imag if l%2==0 else z.real
            elif g is None:
                z=pole[f][k];val=z.imag if k%2==0 else z.real
            else:
                p=k+l;d=abs(f-g);s=f+g
                if k%2==0 and l%2==0:val=(C[d][p]-C[s][p])/2
                elif k%2 and l%2:val=(C[d][p]+C[s][p])/2
                elif k%2==0:val=(S[s][p]+(1 if f>=g else -1)*S[d][p])/2
                else:val=(S[s][p]+(1 if g>=f else -1)*S[d][p])/2
            H[i,j]=H[j,i]=val
    return H
def main():
    p=argparse.ArgumentParser()
    p.add_argument('--nf505',required=True);p.add_argument('--nf494',required=True)
    p.add_argument('--output',required=True);p.add_argument('--dps',type=int,default=550)
    p.add_argument('--orders',default='12,18,24')
    args=p.parse_args();assert args.dps>=400
    start=time.time();mp.mp.dps=args.dps
    old,sha=read(args.nf505);h,hs=read(args.nf494)
    assert (sha,hs)==(NF505,NF494)
    assert old['pass']=='NF504-native' and h['pass']=='NF494-native'
    assert old['source_original_NF407_sha256']==h['original_nf407_source_sha256']==SRC
    assert old['source_original_NF406_sha256']==h['original_nf406_seams_sha256']==SEAM
    assert old['original_selected_J_dimension']==242 and old['original_exterior_center_radius']=='549/500'
    nodes=[(None,None) if x[0]=='pole' else (F(x[0]),x[1])
           for x in old['original_source_basis_nodes']]
    assert len(nodes)==242 and nodes[-1]==(None,None)
    B=mp.mpf('1.1');BO=mp.mpf('1.098')
    Gfull=physical_gram(nodes,B);Lfull=mp.cholesky(Gfull)
    Nout=mp.matrix(242)
    for i in range(242):
        for j in range(242):
            Nout[i,j]=dmid(old['original_actual_exterior_J242_D_Gram_rows_outward'][i][j])
    d=mp.matrix([bmid(z) for z in old['original_actual_exterior_W_moments_D_outward']])
    a=mp.lu_solve(Nout,d)
    assert max(abs((Nout*a-d)[i]) for i in range(242))<mp.mpf('1e-200')
    beta=backward(Lfull,[a[i] for i in range(242)])
    psource=bmid(old['original_original_W_exterior_selected_projection_power_outward'])
    pcalc=(d.T*a)[0]
    assert abs(psource-pcalc)<mp.mpf('1e-100')
    Gout=physical_gram(nodes,BO);Lout=mp.cholesky(Gout)
    sample_max=mp.mpf(0)
    colcache={}
    for c in (0,1,7,50,99,100,241):
        v=[mp.mpf(int(i==c)) for i in range(242)]
        colcache[c]=backward(Lfull,v)
    for i,j in ((0,0),(1,0),(50,7),(100,99),(241,241)):
        ci=mp.matrix(colcache[i]);cj=mp.matrix(colcache[j])
        q=(ci.T*Gout*cj)[0]
        sample_max=max(sample_max,abs(q-Nout[i,j]))
    assert sample_max<mp.mpf('1e-200')
    print('NF517 original raw physical full/exterior Gram + historic selected moments numerical consistency PASS',flush=True)
    ws={f:2*mp.pi*rational(f) for f,k in nodes if f is not None}
    c8=sum(mp.log(base)/mp.sqrt(n) for n,base in
           ((2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3)))
    Hjet=[bmid(z) for z in h['original_H_400_native_outward']]
    Ujet=[bmid(z) for z in h['original_U_400_native_outward']]
    assert Ujet[0]<0
    def W(x):
        t=B-x;H=U=mp.mpf(0)
        for v in reversed(Hjet):H=H*t+v
        for v in reversed(Ujet):U=U*t+v
        return H+Ujet[0]*c8+U*mp.log(B/t)/2
    def J(x):
        return [mp.sinh(x/2) if f is None else
                x**k*(mp.sin(ws[f]*x) if k%2==0 else mp.cos(ws[f]*x))
                for f,k in nodes]
    assert 4094*BO/4096>mp.log(9)-B
    Rlo,Rhi=map(rational,old['original_original_saturated_exterior_residual_outward'])
    gamma=rational(old['original_original_gamma_squared'])
    out=[]
    for order in map(int,args.orders.split(',')):
        assert 8<=order<=64
        xs,weights=leggauss(order);Fcols=[];bvec=[]
        for cell in (4094,4095):
            low=cell*BO/4096;high=(cell+1)*BO/4096
            rad=(high-low)/2;center=(high+low)/2
            for x0,w0 in zip(xs,weights):
                x=center+rad*mp.mpf(float(x0))
                weight=2*rad*mp.mpf(float(w0))
                jj=J(x);v=forward(Lout,jj)
                s=mp.sqrt(weight)
                Fcols.append([z*s for z in v])
                bvec.append(s*(W(x)-sum((z*y for z,y in zip(beta,jj)),mp.mpf(0))))
        n=len(Fcols);K=mp.matrix(n)
        for i in range(n):
            for j in range(i+1):
                q=sum((x*y for x,y in zip(Fcols[i],Fcols[j])),mp.mpf(0))
                K[i,j]=K[j,i]=q
        results={}
        for name,inds in (('H4094',range(order)),('H4095',range(order,2*order)),('union',range(2*order))):
            ids=list(inds);N=len(ids)
            M=mp.matrix(N);rhs=mp.matrix([bvec[i] for i in ids])
            for i in range(N):
                for j in range(N):M[i,j]=mp.mpf(int(i==j))-K[ids[i],ids[j]]
            gain=(rhs.T*mp.lu_solve(M,rhs))[0]
            e=(rhs.T*rhs)[0]
            tau=sum((K[i,i] for i in ids),mp.mpf(0))
            eig=np.linalg.eigvalsh(np.array([[float(K[i,j]) for j in ids] for i in ids]))
            gap=1-float(eig[-1])
            assert 0<e<gain<Rlo and gap>0
            results[name]={'original_full_242D_local_eD_NUMERICAL_SCOUT':float(e),
             'original_full_242D_support_liberation_gain_NUMERICAL_SCOUT':float(gain),
             'original_full_242D_trace_leverage_NUMERICAL_SCOUT':float(tau),
             'source_kernel_gap_NUMERICAL_SCOUT':gap,
             'original_new_residual_lower_using_SOURCE_Rlo_but_UNCERTIFIED_gain':float(Rlo-gain),
             'candidate_above_unchanged_nf404_gamma':bool(Rlo-gain>gamma)}
        out.append({'Gauss_Legendre_nodes_per_mirrored_pair':order,'candidates':results})
        print('NF517 ORIGINAL FULL J242 NYSTROM SCOUT order',order,results,flush=True)
    result={'pass':'NF517-UNVERIFIED-550digit-source-numerical-scout',
      'status':'NOT SOURCE INTERVAL CERTIFIED, DO NOT PROMOTE ORIGINAL NF404 CELL NO-GO',
      'original_nf505_sha256':sha,'original_nf494_sha256':hs,
      'original_nf407_sha256':SRC,'original_nf406_sha256':SEAM,
      'original_dimension':242,'original_selected_solver_precision_decimal_digits':mp.mp.dps,
      'old_global_projection_power_source_check_float':float(pcalc),
      'independent_raw_vs_native_selected_Gram_sample_max_error_float':float(sample_max),
      'original_source_Gauss_Nystrom_candidates':out,
      'all_quadrature_order_error_certificates':False,
      'original_full_242D_selected_source_Arb_interval_eD':'OPEN',
      'original_source_operator_spectral_gap_interval':'OPEN',
      'unconditional_original_nf404_named_support_decision':'OPEN',
      'Weil_multiplier_image_graph_domain':'OPEN','W_ODD_NEG':'OPEN','RH':'OPEN',
      'elapsed_seconds':time.time()-start}
    Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
    print('Original 242D SCOUT only. No independent interval quadrature or certified named support result.')
if __name__=='__main__':main()
