"""IV265 odd high-node scalar enclosures, from IV251/253 exact entries.
Fixed point interval kernel IV254, bound proof in the paired report.
All high nodes 513..458751 odd. No finite/infinite Schur sign claimed.
"""
import os, sys, math, time, hashlib, json
from fractions import Fraction as F
from pathlib import Path
os.environ['OPENBLAS_NUM_THREADS']='4'; os.environ['OMP_NUM_THREADS']='4'
import numpy as np
import iv254_intermediate as c
P=Path(__file__).resolve().parent
S=c.S; J=28672; L=8*J; end=2*L; first=513; no=(end-512)//2; nf=(L-512)//2

def sha(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for b in iter(lambda:f.read(1<<20),b''):h.update(b)
    return h.hexdigest()

def gitsha(p):
    b=p.read_bytes();return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()

def fliv(a):
    m=c.mid(a); x=float(m)/S; radius=c.rad(a,m)
    # S is a power of two; conversion of integer midpoint to binary64 is
    # covered by one ulp of x. Round the radius conversion and sum outward.
    assert math.isfinite(x)
    r=math.nextafter(math.nextafter(float(radius)/S,math.inf)+math.ulp(x),math.inf)
    return x,r

def run():
    start=time.time()
    assert gitsha(P/'iv254_intermediate.py')=='d2671f69193ef70515546a91fbb95cb6166cd2b7'
    assert S==1<<80 and c.alpha[0]>3*S//4 and c.alpha[1]<S
    # Rational envelope checks for the analytic trapezoid/variation bounds.
    al=F(3,4); es=F(1,7**5)/(1-F(1,7**4))
    # |A' - (2j+2jb/alpha+1/(2 alpha^2))| < 16/j + 1/1000.
    numer=1/al**3+(F(7,24)+5)/(al**4*512)
    exp_n=2/al**2*es
    assert numer<16 and exp_n<F(1,1000)
    # |gamma-log(j/8)| < 3/j^2; boundary correction < 8/j^2.
    gamma=4*(F(1,32)+F(1,8)+F(1,4))/al**2
    bd=F(9,8)/al**2+es/(2*al**2)+5/(al**4*512**2)
    assert gamma<3 and bd<8 and 2*gamma+bd<14
    # Literal 24 prime powers; exact 80-bit norm-controlled rotations.
    b=[0]*no; pc=[0]*no; berr=perr=0; amp=0; maxE=0
    for pp,p0 in c.BANK:
        lg=c.log(pp);sq=math.isqrt(pp*S*S);a=c.di(c.log(p0),(sq,sq+1))
        alen=c.mu(a,c.su(c.I(4),lg)); A=c.mid(a); H=c.mid(alen)
        sn,co=c.trig(c.mu(c.alpha,lg)); u=c.mid(sn);v=c.mid(co)
        E=max(c.rad(sn,u),c.rad(co,v)); maxE=max(maxE,E)
        assert 0<a[0]<=a[1]<S and 0<alen[0]<=alen[1]<4*S and end*(4*E+2)<S
        amp+=a[1]
        x=0;y=S
        for j in range(end):
            if j>=first and j%2:
                k=(j-first)//2;b[k]+=A*x//S;pc[k]+=H*y//S
            x,y=(x*v+y*u)//S,(y*v-x*u)//S
        # |true amplitude - center| times |true trig| <= amplitude radius.
        # Center amplitude times rotation error plus floor error is charged.
        err=end*(4*E+2)
        berr+=err+c.rad(a,A)+1;perr+=4*err+c.rad(alen,H)+1
    assert amp<13*S and berr<S//(1<<40) and perr<S//(1<<40)
    print('literal odd rotations',time.time()-start,flush=True)
    js=np.arange(first,end,2,dtype=np.int64);assert len(js)==no and js[nf]==L+1 and js[512]==1537
    A=np.empty(no);Ar=np.empty(no);diag=np.empty(no);dr=np.empty(no);bc=np.empty(no);br=np.empty(no)
    lg=c.log(first,8); inv=c.inv; inv2=c.ra(c.mu(inv,inv),1,2)
    for i,j in enumerate(range(first,end,2)):
        bi=(b[i]-berr,b[i]+berr);ci=(pc[i]-perr,pc[i]+perr)
        bc[i],br[i]=fliv(bi)
        assert max(abs(bi[0]),abs(bi[1]))<13*S
        num=c.ad(c.ra(c.ad(c.I(2),c.ra(c.mu(bi,inv),2,1)),j,1),inv2)
        e=c.ad(c.I(16,j),c.I(1,1000))[1];num=(num[0]-e,num[1]+e)
        d=c.ad(c.su(c.ra(lg,2,1),ci),c.ad(c.ra(c.mu(bi,inv),1,j),c.I(1,j)))
        e=c.I(14,j*j)[1];d=(d[0]-e,d[1]+e)
        A[i],Ar[i]=fliv(num);diag[i],dr[i]=fliv(d)
        t=j+1
        lo=sum(2*S//(k*t**k) for k in (1,3,5,7,9))
        hi=sum(c.ce(2*S,k*t**k) for k in (1,3,5,7,9))+c.ce(2*S,11*t**9*(t*t-1))
        lg=c.ad(lg,(lo,hi))
    assert np.all(np.isfinite(A)) and np.all(np.isfinite(diag)) and np.all(Ar>0) and np.all(dr>0)
    assert np.all(np.abs(A)+Ar<41*js) and np.all(np.abs(bc)+br<13)
    out=P/'iv265_scalar.npz';np.savez(out,js=js,A=A,Ar=Ar,diag=diag,dr=dr,b=bc,br=br)
    receipt=dict(scope='original odd high scalar enclosures; analytic constants conditional on IV251/253 definitions, IEEE binary64 conversion',first=int(js[0]),last=int(js[-1]),rows=no,support_rows=nf,prefix_rows=512,cutoff=J,L=L,bank=len(c.BANK),scale=str(S),prime_amplitude_upper_scaled=str(amp),rotation_max_step_error_scaled=str(maxE),sine_error_scaled=str(berr),weighted_cos_error_scaled=str(perr),numerator_inverse_j_constant=str(numer),numerator_exponential_constant=str(exp_n),gamma_inverse_j2_constant=str(gamma),boundary_inverse_j2_constant=str(bd),max_A_radius=float(max(Ar)),max_diag_radius=float(max(dr)),source_git_blob=gitsha(Path(__file__)),scalar_kernel_git_blob=gitsha(P/'iv254_intermediate.py'),npz_bytes=out.stat().st_size,npz_sha256=sha(out),elapsed_seconds=time.time()-start)
    (P/'iv265_scalar.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt,indent=2),flush=True)

if __name__=='__main__':run()
