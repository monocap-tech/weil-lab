#!/usr/bin/env python3
"""Bounded NUMERICAL original Birman-Schwinger/Galerkin feasibility diagnostic.

No quadrature error or infinite operator-norm remainder is certified here.
"""
import argparse,hashlib,json,time
from pathlib import Path
from fractions import Fraction
import numpy as np
import scipy
from scipy.special import digamma,roots_legendre
from scipy.linalg import eigh,solve,solve_triangular,cholesky
from scipy.optimize import brentq

PIN={'cap':'8b58972bbdd2f9cb5d00275820ab6d6891feeff3bbd584a1c28231770368f514',
     'negative':'a693261c31f01a4a1e11ea6400e5173435a8260b41b1f6b43aa6f67f784ccb7f'}
B=1.1;L=2*B;NP=np.sinh(B)-B;KAPPA=.001;KSTAR=33621/1e9
NS=(32,64,128);NMAX=max(NS)
PAIRS=((2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3))

def gram(n):
    nu=np.pi*np.arange(1,n+1)/B
    v=-2*nu*np.sinh(B/2)*(-1.)**np.arange(1,n+1)/((.25+nu**2)*np.sqrt(B*NP))
    G=np.eye(n+1);G[:-1,-1]=v;G[-1,:-1]=v
    return G

def correlation(s,n):
    """Exact-form physical translated Gram, evaluated in ordinary binary64."""
    s=np.asarray(s);nu=np.pi*np.arange(1,n+1)/B
    minus=nu[:,None]-nu[None,:];plus=nu[:,None]+nu[None,:]
    length=L-s
    c=(length[:,None,None]/(2*B))*(
      np.sinc(minus[None,:,:]*length[:,None,None]/(2*np.pi))*np.cos(plus[None,:,:]*s[:,None,None]/2)
      -np.sinc(plus[None,:,:]*length[:,None,None]/(2*np.pi))*np.cos(minus[None,:,:]*s[:,None,None]/2))
    out=np.empty((len(s),n+1,n+1));out[:,:n,:n]=c
    cross=np.zeros((len(s),n),complex)
    for sign in (-1,1):
        lam=sign*1j*nu;ci=sign/(2j*np.sqrt(B))
        for pole_sign in (-1,1):
            mu=pole_sign*.5;cj=pole_sign/(2*np.sqrt(NP))
            z=(lam[None,:]+mu)*length[:,None]/2
            cross+=ci*cj*length[:,None]*np.exp((mu-lam[None,:])*s[:,None]/2)*np.sinc(z/(1j*np.pi))
    assert np.max(np.abs(cross.imag))<1e-13
    out[:,:n,n]=cross.real;out[:,n,:n]=cross.real
    out[:,n,n]=(np.sinh(B-s/2)-(B-s/2)*np.cosh(s/2))/NP
    return out

def signed_physical(n,order):
    G=gram(n);nodes,weights=roots_legendre(order);nodes=(nodes+1)*B;weights*=B
    arch=np.zeros_like(G)
    for offset in range(0,order,16):
        s=nodes[offset:offset+16];ws=weights[offset:offset+16]
        dif=G[None,:,:]-correlation(s,n)
        arch+=np.einsum('q,qij->ij',ws*np.exp(s/2)/np.sinh(s),dif)
    tail=sum(2*np.exp(-(2*j+.5)*L)/(2*j+.5) for j in range(64))
    c0=-np.euler_gamma-np.pi/2-3*np.log(2)-np.log(np.pi)
    arch+=(c0+tail)*G
    prime=np.zeros_like(G)
    for power,p in PAIRS:
        prime-=2*np.log(p)/np.sqrt(power)*correlation([np.log(power)],n)[0]
    pole=np.sqrt(NP)*G[:,-1];Qo=arch+prime-2*np.outer(pole,pole)
    return (Qo+Qo.T)/2,arch,prime

def fourier(q,n):
    q=np.asarray(q);t=2*np.pi*q;nu=np.pi*np.arange(1,n+1)/B
    fs=np.sqrt(B)*(np.sinc((nu[None,:]-t[:,None])*B/np.pi)-np.sinc((nu[None,:]+t[:,None])*B/np.pi))
    fp=2*(.5*np.cosh(B/2)*np.sin(t*B)-t*np.sinh(B/2)*np.cos(t*B))/(.25+t*t)/np.sqrt(NP)
    return np.column_stack((fs,fp))

def multiplier(q):
    q=np.asarray(q);m=digamma(.25+1j*np.pi*q).real-np.log(np.pi)
    for power,p in PAIRS:m-=2*np.log(p)/np.sqrt(power)*np.cos(2*np.pi*q*np.log(power))
    return m

def split_clipping(negative,cap):
    # Numerical root splitting, NOT a certified enumeration or root enclosure.
    rows=cap['endpoint_multiplier_intervals'];qs=np.array([float(Fraction(v[0])) for v in rows]);ys=np.array([KAPPA-(float(Fraction(v[1]))+float(Fraction(v[2])))/2 for v in rows])
    intervals=[];roots=[]
    for row in negative['original_leaf_witnesses']:
        a,b=float(Fraction(row[0])),float(Fraction(row[1]));lo=np.searchsorted(qs,a);hi=np.searchsorted(qs,b,side='right');knots=[a,b]
        for j in range(lo,hi-1):
            if ys[j]*ys[j+1]<0:
                root=float(brentq(lambda x:KAPPA-multiplier(x),qs[j],qs[j+1],xtol=1e-13));knots.append(root);roots.append(root)
        knots=sorted(set(knots));intervals.extend(zip(knots,knots[1:]))
    return np.array(intervals),roots

def negative_matrix(leaf,n,order):
    nodes,weights=roots_legendre(order)
    q=((leaf[:,0,None]+leaf[:,1,None])/2+(leaf[:,1,None]-leaf[:,0,None])*nodes/2).ravel()
    ws=((leaf[:,1,None]-leaf[:,0,None])*weights/2).ravel()
    m=multiplier(q)
    r=np.maximum(0,KAPPA-m);F=fourier(q,n)
    K=F.T@((2*ws*r)[:,None]*F)
    return (K+K.T)/2,len(q)

def whiten(matrix,G):
    C=cholesky(G,lower=True);Y=solve_triangular(C,matrix,lower=True)
    return solve_triangular(C,Y.T,lower=True).T

def report(Qo,K,G,payment,n):
    A=Qo+K;Aw=whiten(A,G);Kw=whiten(K,G);Qw=whiten(Qo,G)
    amin=float(eigh(Aw,eigvals_only=True,subset_by_index=[0,0])[0]);assert amin>0
    evals,vecs=eigh(Kw,Aw);rho=float(evals[-1]);signedmin=float(eigh(Qw,eigvals_only=True,subset_by_index=[0,0])[0])
    # An actual matched inverse solve for the inherited normalized pole RHS.
    rhs=G[:,-1];x=solve(A,rhs,assume_a='pos');response=float(rhs@x)
    anchor=A[:-1,:-1];mixed=A[:-1,-1];h=A[-1,-1]
    u=solve(anchor,mixed,assume_a='pos');v=solve(anchor,rhs[:-1],assume_a='pos')
    schur=float(h-mixed@u);forcing=float(rhs[-1]-mixed@v)
    base=float(rhs[:-1]@v);extra=forcing**2/schur
    identity_error=abs(response-base-extra);assert schur>0 and identity_error<1e-8*max(1,abs(response))
    assert np.linalg.norm(A@x-rhs,np.inf)<1e-10
    cap_upper=rho+payment/amin
    # This uses a numerical rho as an ILLUSTRATIVE budget, never an accepted margin.
    budget=KSTAR*max(0,1-cap_upper)
    return dict(dirichlet_modes=n,trial_dimension=n+1,finite_BS_largest=rho,
      finite_Astar_physical_min=amin,finite_signed_physical_min=signedmin,
      affine_Young_BS_uniform_error_payment=payment/amin,finite_cap_BS_upper_screen=cap_upper,
      pole_inverse_response=response,pole_base_response=base,pole_extra_matched_response=extra,
      pole_positive_Schur=schur,pole_matched_forcing=forcing,matched_inverse_identity_error=identity_error,
      provisional_strong_residual_squared_budget=budget,physical_Gram_condition=float(np.linalg.cond(G)),
      finite_eigenpair_residual=float(np.linalg.norm(Kw@vecs[:,-1]-rho*(Aw@vecs[:,-1]),np.inf)))

def main():
    p=argparse.ArgumentParser()
    for k in PIN:p.add_argument('--'+k,required=True)
    p.add_argument('--output',default='artifacts/original_compact_BS_feasibility.json');args=p.parse_args();data={};start=time.monotonic()
    assert np.__version__=='2.3.5' and scipy.__version__=='1.17.0'
    for k,h in PIN.items():
        raw=Path(getattr(args,k)).read_bytes();assert hashlib.sha256(raw).hexdigest()==h;data[k]=json.loads(raw)
    z=data['cap'];assert z['W_ODD_NEG']=='OPEN'
    payment=float(Fraction(z['uniform_cap_minus_true_negative_upper'])+Fraction(z['Young_cap_minus_affine_operator_upper']))
    G=gram(NMAX);zero=correlation([0.],NMAX)[0];assert np.max(np.abs(G-zero))<1e-13
    assert np.max(np.abs(correlation([L],NMAX)))<1e-13
    stages=[];rawmodels=[];intervals,roots=split_clipping(data['negative'],data['cap'])
    for archorder,negorder in [(512,8),(1024,16)]:
        Qo,arch,prime=signed_physical(NMAX,archorder);K,count=negative_matrix(intervals,NMAX,negorder)
        rows=[]
        for n in NS:
            indices=list(range(n))+[NMAX];ix=np.ix_(indices,indices)
            rows.append(report(Qo[ix],K[ix],G[ix],payment,n))
        stages.append(dict(arch_Gauss_order=archorder,negative_Gauss_order_per_leaf=negorder,negative_frequency_points=count,rows=rows))
        rawmodels.append(dict(signed=Qo.tolist(),negative=K.tolist()))
        print('Numerical stage',archorder,negorder,'seconds',round(time.monotonic()-start,2),flush=True)
        assert time.monotonic()-start<120,'bounded 120-second feasibility guard'
    # Compare FULL preconditioned blocks, not just plotted eigenvalue digits.
    qdiff=whiten(np.array(rawmodels[1]['signed'])-np.array(rawmodels[0]['signed']),G)
    kdiff=whiten(np.array(rawmodels[1]['negative'])-np.array(rawmodels[0]['negative']),G)
    variation=dict(signed_block_spectral=float(np.linalg.norm(qdiff,2)),negative_block_spectral=float(np.linalg.norm(kdiff,2)),
      BS_largest_max_difference=max(abs(a['finite_BS_largest']-b['finite_BS_largest']) for a,b in zip(stages[0]['rows'],stages[1]['rows'])))
    stable=max(variation.values())<1e-7
    passed=stable and all(row['finite_cap_BS_upper_screen']<1 for row in stages[-1]['rows'])
    near=stable and all(row['finite_BS_largest']>1-1e-10 for row in stages[-1]['rows'])
    out=dict(status='NUMERICAL_COMPACT_BS_NEAR_CRITICAL_STOP' if near else 'NUMERICAL_COMPACT_BS_FEASIBILITY_ENCOURAGING' if passed else 'NUMERICAL_COMPACT_BS_FEASIBILITY_INCONCLUSIVE',
      input_sha256=PIN,numpy_version=np.__version__,scipy_version=scipy.__version__,arithmetic='ordinary binary64; NOT interval quadrature',
      physical_half_width='11/10',basis='sin(n*pi*x/B)/sqrt(B), n=1..N; and true sinh(x/2)/sqrt(sinh(B)-B)',
      original_Astar_identity='Astar=complete original signed physical form + original Kminus',
      original_negative_cover_leaves=973,numerically_split_clipping_roots=roots,numerical_frequency_intervals=intervals.tolist(),stages=stages,physical_Gram=G.tolist(),raw_matrix_models=rawmodels,
      quadrature_variation=variation,quadrature_stability_screen_passed=stable,cap_screen_passed=passed,
      accepted_cap_operator_overpayment=str(Fraction(z['uniform_cap_minus_true_negative_upper'])+Fraction(z['Young_cap_minus_affine_operator_upper'])),
      quadrature_error_certified=False,global_BS_norm_upper_certified=False,infinite_operator_remainder_certified=False,
      full_J470_or_SI29_14_response_computed=False,original_domain_review='OPEN',W_ODD_NEG='OPEN',elapsed_seconds=time.monotonic()-start)
    path=Path(args.output);path.parent.mkdir(exist_ok=True,parents=True);path.write_text(json.dumps(out,separators=(',',':'))+'\n')
    for row in stages[-1]['rows']:print(row)
    print(out['status'],variation,'seconds',out['elapsed_seconds'])
if __name__=='__main__':main()
