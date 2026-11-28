"""IV265 odd actual high correction proposal. No numerical stopping criterion is a proof.
Exact signed contractions in the full rational retained basis; solve only first 32
columns, leave other 224 uncorrected for full joint residual verification.
"""
import os, json, time, math
from pathlib import Path
os.environ['OPENBLAS_NUM_THREADS']='4';os.environ['OMP_NUM_THREADS']='4'
from iv265_plan import sha,gitsha,asint,convert
import numpy as np
from scipy.fft import rfft,irfft
from scipy.linalg import solve_triangular
P=Path(__file__).resolve().parent
J=28672; L=8*J; K=1536; p=512; n=14080; nf=(L-512)//2; no=(2*L-512)//2; a=32; Q=1<<40

def main():
    start=time.time(); auth=json.loads((P/'iv265_signed_auth.json').read_text()); sr=json.loads((P/'iv265_scalar.json').read_text()); plan=json.loads((P/'iv265_plan.json').read_text())
    assert sha(P/'signed_replay.json')==auth['signed_replay_sha256']
    assert gitsha(P/'iv265_finite_congruence.json')=='97928a1ce7b3a7752301146b25c92f1b23b78861'
    assert sha(P/'iv265_scalar.npz')==sr['npz_sha256']
    assert sha(P/'iv265_basis_proposal.npz')==plan['proposal_sha256']
    factor=Path('/tmp/iv256_1_factor.npy'); assert sha(factor)=='58ec1836be48df53cc52e3df32c4708fa1782184aa4531018432329476730c88'
    d=json.loads((P/'signed_replay.json').read_text()); m=d['meta']; rows=d['rows']; cert=json.loads((P/'iv265_finite_congruence.json').read_text()); W=asint(cert['basis']); ws=int(cert['basis_scale']); z=np.load(P/'iv265_basis_proposal.npz'); Vi=z['Vi']; VS=int(z['VS']); B=W.T@Vi.astype(object); BS=ws*VS
    assert len(rows)==256 and m['active']==456 and m['par']==1 and Vi.shape==(256,256)
    # Centers only here: contract exact integers before floating conversion.
    def trans(key,den): return convert(B[:,:a].T@asint([r[key] for r in rows]),BS*den)
    q=trans('q',int(m['scale'])); nn=trans('nc',int(m['scale'])); R=trans('R',int(m['Rscale'])).T
    z=np.load(P/'iv265_scalar.npz'); js=z['js']; A=z['A']; diag=z['diag']; assert len(js)==no and js[0]==513 and js[n]==J+1 and js[p]==K+1 and js[nf]==L+1
    rhs=np.empty((nf,a)); rhs[:p]=R
    for i in range(p,nf,2048):
        sl=slice(i,min(i+2048,nf)); j=js[sl]; V=np.polynomial.chebyshev.chebvander(2*(K/j)**2-1,m['active']-1)
        rhs[sl]=(A[sl,None]*(V@q.T)-V@nn.T)/j[:,None]**2
    print('rhs prepared',time.time()-start,flush=True)
    N=1<<(2*nf-1).bit_length(); kt=np.zeros(N);kt[1:nf]=1/(2*np.arange(1,nf));kt[-nf+1:]=-1/(2*np.arange(nf-1,0,-1));kh=np.zeros(N);kh[:2*nf-1]=1/(2*(np.arange(2*nf-1)+513));ft=rfft(kt);fh=rfft(kh)
    def conv(x):return irfft(ft[:,None]*rfft(x,n=N,axis=0,workers=4),n=N,axis=0,workers=4)[:nf]+irfft(fh[:,None]*rfft(x[::-1],n=N,axis=0,workers=4),n=N,axis=0,workers=4)[nf-1:2*nf-1]
    def action(x):return (A[:nf,None]*conv(x)-conv(A[:nf,None]*x))/(2*js[:nf,None])+diag[:nf,None]*x
    fac=np.load(factor,mmap_mode='r'); assert fac.shape==(n,n) and fac.dtype==np.int32
    FM=np.empty((n,n),dtype=float,order='F')
    for i in range(0,n,128):FM[:,i:i+128]=fac[:,i:i+128]/float(1<<23)
    del fac
    def pre(v):
        z=v.copy();z[:n]=solve_triangular(FM.T,solve_triangular(FM,v[:n],lower=True,check_finite=False),lower=False,check_finite=False)/2;z[n:]/=2*np.log(js[n:nf,None]/8);return z
    Xi=np.zeros((nf,a),dtype=np.int64); history=[]
    for i in range(0,a,8):
        sl=slice(i,i+8);r=rhs[:,sl];x=np.zeros_like(r);e=r.copy();v=pre(e);d0=v.copy();rho=np.sum(e*v,axis=0)
        for k in range(100):
            t=action(d0);den=np.sum(d0*t,axis=0);assert np.all(den>0) and np.all(rho>0)
            step=rho/den;x+=d0*step;e-=t*step;v=pre(e);new=np.sum(e*v,axis=0);d0=v+d0*(new/rho);rho=new
            if (k+1)%25==0:print('iteration',i,k+1,float(np.linalg.norm(e)),time.time()-start,flush=True)
        assert np.all(np.isfinite(x)) and np.max(np.abs(x))*Q<2**52
        Xi[:,sl]=np.rint(x*Q).astype(np.int64);rr=np.linalg.norm(r-action(Xi[:,sl].astype(float)/Q),axis=0)
        history.append({'first':i,'last_exclusive':i+8,'iterations':100,'rhs_norms':np.linalg.norm(r,axis=0).tolist(),'center_residual_norms':rr.tolist()})
        print('batch',i,rr.tolist(),time.time()-start,flush=True)
        np.savez(P/'iv265_joint_partial.npz',Xi=Xi,done=i+8)
    del FM
    out=P/'iv265_joint_proposal.npz';np.savez(out,Xi=Xi,Q=Q,Vi=Vi,VS=VS,source_plan_sha256=plan['proposal_sha256'])
    receipt=dict(scope='32-column odd actual high action center solve proposal; all 256 retained; no certified residual or Schur sign',source_git_blob=gitsha(Path(__file__)),source_signed_sha256=auth['signed_replay_sha256'],source_scalar_sha256=sr['npz_sha256'],source_plan_sha256=plan['proposal_sha256'],source_factor_sha256=sha(factor),first_mode=int(js[0]),last_support_mode=int(js[nf-1]),support_rows=nf,retained=256,correction_columns=a,fft_length=N,quantization_denominator=Q,iterations_per_column=100,history=history,proposal_bytes=out.stat().st_size,proposal_sha256=sha(out),center_residual_frobenius_diagnostic=math.sqrt(sum(x*x for b in history for x in b['center_residual_norms'])),elapsed_seconds=time.time()-start)
    (P/'iv265_joint_proposal.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt,indent=2),flush=True)
if __name__=='__main__':main()
