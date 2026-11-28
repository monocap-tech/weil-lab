"""IV265 exact signed receiver inputs for all 256 rationally rotated directions.
No FFT action, inverse penalty, or Schur sign. Every conversion enclosure is
checked by exact rational comparison; model radii use post-drop row values.
"""
import os, json, math, time
from pathlib import Path
from fractions import Fraction as F
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
from iv265_plan import sha,gitsha,asint
import numpy as np
P=Path(__file__).resolve().parent

def upper(q):
    assert q>=0
    x=float(q)
    if F.from_float(x)<q:x=math.nextafter(x,math.inf)
    assert math.isfinite(x) and F.from_float(x)>=q
    return x

def convert_exact(C,den,R=None):
    C=np.asarray(C,dtype=object); r=None if R is None else np.broadcast_to(np.asarray(R,dtype=object),C.shape)
    c=np.empty(C.shape); e=np.empty(C.shape)
    for idx in np.ndindex(C.shape):
        v=F(int(C[idx]),den); f=float(v); assert math.isfinite(f)
        err=abs(v-F.from_float(f))
        if r is not None:err+=F(int(r[idx]),den)
        c[idx]=f;e[idx]=upper(err)
    return c,e

def main():
    start=time.time(); auth=json.loads((P/'iv265_signed_auth.json').read_text());plan=json.loads((P/'iv265_plan.json').read_text())
    assert sha(P/'signed_replay.json')==auth['signed_replay_sha256']; assert sha(P/'iv265_basis_proposal.npz')==plan['proposal_sha256'];assert gitsha(P/'iv265_finite_congruence.json')=='97928a1ce7b3a7752301146b25c92f1b23b78861'
    d=json.loads((P/'signed_replay.json').read_text());rows=d['rows'];m=d['meta'];assert m['par']==1 and m['active']==456 and len(rows)==256
    c=json.loads((P/'iv265_finite_congruence.json').read_text()); W=asint(c['basis']);ws=int(c['basis_scale']);z=np.load(P/'iv265_basis_proposal.npz'); Vi=z['Vi'].astype(object);vs=int(z['VS']);B=W.T@Vi;bs=ws*vs;U=int(m['scale']);RS=int(m['Rscale']);ab=np.abs(B).T
    q,qr=convert_exact(B.T@asint([r['q'] for r in rows]),bs*U)
    nn,nr=convert_exact(B.T@asint([r['nc'] for r in rows]),bs*U)
    meI=ab@asint([r['Merr'] for r in rows]);neI=ab@asint([r['Nerr'] for r in rows]);me=np.array([upper(F(int(v),bs*U)) for v in meI]);ne=np.array([upper(F(int(v),bs*U)) for v in neI]);
    RrI=ab@asint([r['Rradius'] for r in rows]);R,Rr=convert_exact(B.T@asint([r['R'] for r in rows]),bs*RS,RrI[:,None]);R=R.T;Rr=Rr.T
    print('all exact channel contractions and conversion checks',time.time()-start,flush=True)
    # Retain exact original W-coordinate interval form. Do not transport its
    # radii via an intermediate dense rotation for the eventual sign test.
    f=asint([r['F'] for r in rows]);fr=asint([r['Fr'] for r in rows]);wf=W@f@W.T;wr=np.abs(W)@fr@np.abs(W).T;fs=ws*ws*int(m['Fscale']);assert fs==int(c['scale'])
    gl=min(int(wf[i,i]-wr[i,i])-sum(abs(int(wf[i,j]))+int(wr[i,j]) for j in range(256) if j!=i) for i in range(256));assert gl==int(c['min_row']);F1,F1r=convert_exact(wf,fs,wr)
    out=P/'iv265_receiver_inputs.npz';np.savez(out,q=q,qr=qr,nn=nn,nr=nr,R=R,Rr=Rr,me=me,ne=ne,F1_W=F1,F1r_W=F1r,Vi=z['Vi'],VS=vs)
    receipt=dict(scope='exact full rotated signed coefficient and prefix interval inputs; original W-coordinate finite form; no actual-action certificate',source_git_blob=gitsha(Path(__file__)),signed_source_sha256=auth['signed_replay_sha256'],rotation_source_sha256=plan['proposal_sha256'],retained=256,active=456,prefix=512,all_conversion_enclosures_checked=True,model_radius_M_max=float(max(me)),model_radius_N_max=float(max(ne)),prefix_entry_radius_max=float(np.max(Rr)),finite_margin_numerator=str(gl),finite_margin_denominator=str(fs),input_bytes=out.stat().st_size,input_sha256=sha(out),elapsed_seconds=time.time()-start)
    (P/'iv265_receiver_inputs.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt,indent=2),flush=True)
if __name__=='__main__':main()
