"""IV265: residual covariance proposal on the exact IV264 rational basis.
Every retained direction is preserved. Covariance is a numerical proposal,
not a residual or Schur certificate. Authenticated source banks mandatory.
"""
import os, json, hashlib, time
from pathlib import Path
os.environ['OPENBLAS_NUM_THREADS']='4';os.environ['OMP_NUM_THREADS']='4'
import numpy as np
P=Path(__file__).resolve().parent

def sha(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for b in iter(lambda:f.read(1<<20),b''):h.update(b)
    return h.hexdigest()

def gitsha(p):
    b=p.read_bytes();return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()

def asint(x):
    a=np.array(x,dtype=object)
    return np.array([int(y) for y in a.flat],dtype=object).reshape(a.shape)

def convert(X,den):
    # Binary64 proposal centers only. Verifier must contract exact rationals.
    return np.asarray(X,dtype=np.float64)/float(den)

def main():
    start=time.time()
    a=json.loads((P/'iv265_signed_auth.json').read_text());s=json.loads((P/'iv265_scalar.json').read_text())
    assert sha(P/'signed_replay.json')==a['signed_replay_sha256']
    assert gitsha(P/'iv265_finite_congruence.json')=='97928a1ce7b3a7752301146b25c92f1b23b78861'
    assert sha(P/'iv265_scalar.npz')==s['npz_sha256']
    data=json.loads((P/'signed_replay.json').read_text());rows=data['rows'];m=data['meta']
    cert=json.loads((P/'iv265_finite_congruence.json').read_text());W=asint(cert['basis']);ws=int(cert['basis_scale']);n=256;ac=m['active'];p=512;K=m['K'];U=int(m['scale']);RS=int(m['Rscale'])
    assert W.shape==(n,n) and ac==456 and K==1536 and m['par']==1
    # Exact signed contractions, then convert proposal centers.
    q=convert(W@asint([r['q'] for r in rows]),ws*U)
    nn=convert(W@asint([r['nc'] for r in rows]),ws*U)
    R=convert(W@asint([r['R'] for r in rows]),ws*RS)
    z=np.load(P/'iv265_scalar.npz');js=z['js'];A=z['A'];assert js[0]==513 and js[p]==1537
    G=R@R.T;sample=np.arange(p,len(js),8,dtype=np.int64)
    for i in range(0,len(sample),2048):
        idx=sample[i:i+2048];j=js[idx];x=2*(K/j)**2-1
        V=np.polynomial.chebyshev.chebvander(x,ac-1)
        C=(A[idx,None]*(V@q.T)-V@nn.T)/j[:,None]**2
        G+=8*(C.T@C)
    ev,V=np.linalg.eigh((G+G.T)/2)
    VS=1<<40;Vi=np.rint(V[:,::-1]*VS).astype(np.int64)
    assert Vi.shape==(n,n) and np.max(np.abs(Vi))<=VS
    # Exact invertibility certificate for the quantized rotation.
    Z=Vi.astype(object);gram=Z.T@Z
    margins=[int(gram[i,i])-sum(abs(int(gram[i,j])) for j in range(n) if j!=i) for i in range(n)]
    gl=min(margins);assert 100*gl>99*VS*VS
    out=P/'iv265_basis_proposal.npz';np.savez(out,Vi=Vi,VS=VS,ev=ev,gram_row_lower=np.array(margins,dtype=str),source_basis_sha256=a['finite_congruence_sha256'])
    receipt=dict(scope='all 256 retained odd directions; sample covariance proposal only; exact invertibility of rational rotation',basis_source_git_blob=gitsha(P/'iv265_finite_congruence.json'),signed_source_sha256=a['signed_replay_sha256'],scalar_source_sha256=s['npz_sha256'],samples=len(sample),sample_stride=8,retained=n,selected_corrections=32,rotation_denominator=VS,gram_margin_numerator=str(gl),gram_margin_denominator=str(VS*VS),top_eigenvalues_diagnostic=ev[-16:][::-1].tolist(),inactive_trace_diagnostic=float(ev[:-32].sum()),sample_trace_diagnostic=float(ev.sum()),proposal_sha256=sha(out),proposal_bytes=out.stat().st_size,elapsed_seconds=time.time()-start,source_git_blob=gitsha(Path(__file__)))
    (P/'iv265_plan.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt,indent=2),flush=True)
if __name__=='__main__':main()
