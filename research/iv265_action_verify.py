"""IV265 independent odd high action enclosures, conditional on IV262 FFT error analysis.
Enclose Q_H X on every explicit high row for the 32 quantized correction columns.
Does not certify residuals, the infinite remainder, inverse lift, or Schur sign.
"""
import os, math, json, time
from pathlib import Path
os.environ['OPENBLAS_NUM_THREADS']='4';os.environ['OMP_NUM_THREADS']='4'
import numpy as np
import iv254_intermediate as c
from iv265_plan import sha,gitsha
P=Path(__file__).resolve().parent
S=c.S; eps=2.**-52; tiny=2.**-450
# For <= 2^23 summands, standard binary64 dot/sum bounds are <2^-29;
# this extra slack also covers the square root and norm conversion.
def norm(x):return math.nextafter(float(np.linalg.norm(x))*(1+2.**-28)+tiny,math.inf)
def l1(x):return math.nextafter(float(np.sum(np.abs(x)))*(1+2.**-28)+tiny,math.inf)
def up(x):return np.nextafter(np.asarray(x)*(1+2.**-40)+tiny,np.inf)

def main():
    start=time.time(); r=json.loads((P/'iv265_joint_proposal.json').read_text()); sc=json.loads((P/'iv265_scalar.json').read_text())
    assert sha(P/'iv265_joint_proposal.npz')==r['proposal_sha256'] and sha(P/'iv265_scalar.npz')==r['source_scalar_sha256']==sc['npz_sha256']
    assert gitsha(P/'iv254_intermediate.py')=='d2671f69193ef70515546a91fbb95cb6166cd2b7'
    z=np.load(P/'iv265_scalar.npz');js=z['js'];A=z['A'];Ar=z['Ar'];diag=z['diag'];dr=z['dr'];b=np.load(P/'iv265_joint_proposal.npz');Xi=b['Xi'];Q=int(b['Q']);nf,a=Xi.shape;no=len(js)
    assert nf==114432 and a==32 and no==229120 and js[0]==513 and js[nf]==229377 and Q==1<<40 and np.max(np.abs(Xi))<2**52
    X=Xi.astype(float)/Q;N=1<<(no+nf-1).bit_length();levels=N.bit_length()-1;assert levels<=20 and N>=no+nf-1
    # Same fixed-point twiddle construction and independent radix-2 error budget as IV262.
    ss,cc=c.trig(c.ra(c.pi,2,N));s0=-c.mid(ss);c0=c.mid(cc);E=max(c.rad(ss,-s0),c.rad(cc,c0));assert N*(4*E+2)<S//(1<<48)
    roots=np.empty(N//2,dtype=np.complex128);u=0;v=S
    for k in range(N//2):roots[k]=complex(float(v)/S,float(u)/S);u,v=(u*c0+v*s0)//S,(v*c0-u*s0)//S
    rev=np.zeros(N,dtype=np.int64);ii=np.arange(N,dtype=np.int64)
    for _ in range(levels):rev=(rev<<1)|(ii&1);ii>>=1
    def fft(a,inverse=False):
        b=np.zeros(N,dtype=np.complex128);b[:len(a)]=a;b=b[rev]
        for k in range(1,levels+1):
            h=1<<(k-1);g=b.reshape(-1,2*h);u=g[:,:h].copy();w=roots[::N//(2*h)];v=g[:,h:]*(np.conjugate(w) if inverse else w);g[:,:h]=u+v;g[:,h:]=u-v
        return b/N if inverse else b
    kt=np.zeros(N);kt[1:no]=1/(2*np.arange(1,no));kt[-nf+1:]=-1/(2*np.arange(nf-1,0,-1));kh=np.zeros(N);kh[:no+nf-1]=1/(2*(np.arange(no+nf-1)+513));kabs=np.abs(kt)
    ft=fft(kt);fa=fft(kabs);fh=fft(kh)
    def budget(k):return float(up(2.**-34*(l1(k)+math.sqrt(N)*norm(k))))
    bt=budget(kt);ba=budget(kabs);bh=budget(kh);kl=float(up(l1(kt)+l1(kh)))
    def conv(v,absolute=False):
        q=fft(v);a=fft((fa if absolute else ft)*q,True).real[:no];b=fft(fh*fft(v[::-1]),True).real[nf-1:nf-1+no];y=a+b
        return y,float(up(((ba if absolute else bt)+bh)*norm(v)+8*eps*(norm(a)+norm(b))))
    ai=float(up(np.max(np.abs(A)/(2*js))));ari=float(up(np.max(Ar/(2*js))));ji=float(up(1/(2*int(js[0]))))
    acts=np.empty((no,a));rads=np.empty_like(acts);ae=np.empty(a)
    for i in range(a):
        x=X[:,i];y,e=conv(x);ax=A[:nf]*x;w,we=conv(ax);we=float(up(we+kl*(8*eps*norm(ax)+tiny)))
        p=A*y/(2*js);q=w/(2*js);dx=diag[:nf]*x;act=p-q+np.pad(dx,(0,no-nf));aerr=float(up(ai*e+ji*we+64*eps*(norm(p)+norm(q)+norm(dx))))
        y,e=conv(np.abs(x),True);arx=Ar[:nf]*np.abs(x);w,we=conv(arx,True);we=float(up(we+kl*(8*eps*norm(arx)+tiny)))
        rad=up((Ar*np.abs(y)+np.abs(w))/(2*js)+np.pad(dr[:nf]*np.abs(x),(0,no-nf)))
        acts[:,i]=act;rads[:,i]=rad;ae[i]=float(up(aerr+ari*e+ji*we))
        assert np.all(np.isfinite(act)) and np.all(np.isfinite(rad)) and np.all(rad>=0) and np.isfinite(ae[i]) and ae[i]>=0
        if (i+1)%8==0:print('independent columns',i+1,time.time()-start,flush=True)
    out=P/'iv265_action.npz';np.savez(out,acts=acts,rads=rads,ae=ae)
    rec=dict(scope='independent odd actual action enclosure on all explicit rows for 32 correction columns; inherited FFT analytic and IEEE/BLAS assumptions; not residual or Schur certificate',source_git_blob=gitsha(Path(__file__)),proposal_sha256=r['proposal_sha256'],scalar_sha256=sc['npz_sha256'],first=int(js[0]),last=int(js[-1]),rows=no,columns=a,fft_length=N,fft_stages=levels,twiddle_step_error_scaled=str(E),action_norm_error_fro_upper=norm(ae),max_action_norm_error=float(max(ae)),entry_radius_fro_upper=norm(rads.ravel()),action_bytes=out.stat().st_size,action_sha256=sha(out),elapsed_seconds=time.time()-start)
    (P/'iv265_action.json').write_text(json.dumps(rec,indent=2)+'\n');print(json.dumps(rec,indent=2),flush=True)
if __name__=='__main__':main()
