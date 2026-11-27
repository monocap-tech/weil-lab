"""IV256: rigorous tapered joint-coercivity certificate on H_512.
Requires the pinned IV254 interval kernel, numpy, scipy, standard binary64 BLAS.
Usage: python iv256_taper.py 0   (or 1). Run parities separately.
"""
import os,sys,math,json,time,hashlib
os.environ['OPENBLAS_NUM_THREADS']='4';os.environ['OMP_NUM_THREADS']='4'
import numpy as np
from scipy.linalg import lapack,blas
from fractions import Fraction as F
args=sys.argv[:];sys.argv=[args[0]]
import iv254_intermediate as c
sys.argv=args
S=c.S;T=c.T;DS=c.DS;IS=c.IS;FS=c.FS
M=512;J=28672;L=8*J;m=32;r=2*m;HS=1<<22;WS=1<<30;XS=1<<30
C=F(7979648,10**6);delta=F(1,5);eta=F(1,1000);shift=F(1,100)
Heta=F(1,200);Reta=F(1,100);Zeta=F(1,1000)
c.J=J

def ceilq(x):return c.ce(x.numerator,x.denominator)
def quant(a,s):
 z=c.mid(a)*s//S
 assert max(abs(a[0]*s-z*S),abs(a[1]*s-z*S))<=2*S
 return z

def sqrtiv(a):
 assert a[0]>0
 return math.isqrt(a[0]*S),math.isqrt(a[1]*S)+1

def abslo(a):
 assert a[0]>0 or a[1]<0
 return min(abs(a[0]),abs(a[1]))

def bases():
 out=[];mean=c.I(0);osc=c.I(0)
 for n,p in c.BANK:
  a=c.di(c.log(p),(math.isqrt(n*S*S),math.isqrt(n*S*S)+1));sn,co=c.trig(c.mu(c.alpha,c.log(n)))
  assert a[0]>0 and a[1]<S
  out.append((a,sn,co));mean=c.ad(mean,c.ra(c.mu(a,a),1,2))
 for i,(a,s,t) in enumerate(out):
  for k,(b,u,v) in enumerate(out):
   z=c.ra(c.mu(a,b),1,2);sv=c.mu(s,v);tu=c.mu(t,u)
   if i!=k:osc=c.ad(osc,c.di(z,(abslo(c.su(sv,tu)),)*2))
   osc=c.ad(osc,c.di(z,(abslo(c.ad(sv,tu)),)*2))
 assert mean[1]<4*S and osc[1]<600*S
 return out,mean[1],osc[1]

def tail_centers(base,par):
 d=[0]*((L-J)//2);err=0
 for a,s,t in base:
  A=c.mid(a);b=c.mid(s);v=c.mid(t);E=max(c.rad(s,b),c.rad(t,v));Ea=c.rad(a,A)
  assert L*(4*E+2)<S and abs(A)<S
  x=0;y=S
  for j in range(L):
   if j>=J and j%2==par:d[(j-J)//2]+=(A*x)//S
   x,y=(x*v+y*b)//S,(y*v-x*b)//S
  err+=L*(4*E+2)+Ea+1
 assert err<S//(1<<40)
 return d,err

def sumsquares(a,axis):
 # Exact int64 accumulation on the short axis or in chunks on the long axis.
 z=np.zeros(a.shape[1-axis],dtype=np.int64)
 if axis==1:
  mx=int(np.max(np.abs(a)));assert a.shape[1]*mx*mx<2**62
  return np.sum(a*a,axis=1,dtype=np.int64)
 for k in range(0,a.shape[0],1024):
  b=a[k:k+1024];mx=int(np.max(np.abs(b)));assert len(b)*mx*mx<2**62
  q=np.sum(b*b,axis=0,dtype=np.int64);assert int(z.max())+int(q.max())<2**62;z+=q
 return z

def tail_gram(base,par):
 d,err=tail_centers(base,par);N=len(d);H=np.empty((N,r),dtype=np.int64)
 lg=c.log(J+par,J);sqrtJ=sqrtiv(c.I(J));baseH=c.di(sqrtJ,c.alpha)
 # log((l+2)/l)=2 atanh(1/(l+1)); 3 terms plus <1 scaled unit.
 assert 2*S*(J+1)**2<7*(J+1)**7*((J+1)**2-1)
 for i,l in enumerate(range(J+par,L,2)):
  h=c.di(baseH,c.ra(sqrtiv(c.ad(c.I(1,5),lg)),l,1));q=c.I(J,l);q2=c.mu(q,q)
  a=c.ne(c.mu(h,(d[i]-err,d[i]+err)));b=c.mu(h,q)
  for k in range(m):
   H[i,k]=quant(a,HS);H[i,k+m]=quant(b,HS);a=c.mu(a,q2);b=c.mu(b,q2)
  v=l+1;lo=hi=0
  for k in (1,3,5):lo+=2*S//(k*v**k);hi+=c.ce(2*S,k*v**k)
  lg=c.ad(lg,(lo,hi+1))
 del d
 bound=int(sumsquares(H,0).max());assert bound<2**52
 hf=H.astype(float);del H;V=hf.T@hf;del hf
 Vint=V.astype(np.int64);assert np.array_equal(V,Vint) and int(np.max(np.abs(Vint)))<=bound
 dfar=delta+F(c.log(8)[0],S)
 mass=(F(J,L*L)+F(J,2*L))/(F(3,4)**2*dfar);osc=F(600*J,L*L)/(F(3,4)**2*dfar)
 far=[F(128,63)*F(1,8)**(2*k)*(4*mass+osc) for k in range(m)]+[F(128,63)*F(1,8)**(2*k+2)*mass for k in range(m)]
 herror=F(4*N*r,HS*HS);Gc=np.empty((r,r),dtype=np.int64)
 for i in range(r):
  for j in range(r):
   q=(1+Heta)*F(int(Vint[i,j]),HS*HS)
   if i==j:q+=(1+1/Heta)*herror+far[i]
   q*=(1+Reta)*T;Gc[i,j]=q.numerator//q.denominator
 # Exact upper factor for G (centers with entry error <=1/T).
 A=Gc.astype(float)/T;A.flat[::r+1]+=.0001
 Li=np.rint(np.linalg.cholesky(A)*FS).astype(np.int64)
 assert int(sumsquares(Li,1).max())<2**60
 LL=Li@Li.T;E=LL-Gc;assert r*int(np.max(np.abs(E)))<2**62 and r*int(np.max(np.diag(LL)))<2**62;dlo=int(np.min(2*np.diag(E)-np.sum(np.abs(E),axis=1,dtype=np.int64)))
 assert dlo>r
 trace=int(np.trace(LL));assert trace>0
 return Li,trace,{'tail_rows':N,'d_error_scaled':str(err),'H_column_square_max':str(bound),'G_factor_dominance_scaled':str(dlo),'G_factor_trace_scaled':str(trace),'far_mass':str(mass),'far_oscillation':str(osc)}

def features(j,d,Li,trace):
 n=len(j);X=np.empty((n,r),dtype=np.int64);w=np.empty(n,dtype=np.int64);sqrtJ=sqrtiv(c.I(J))
 for i,k in enumerate(j):
  k=int(k);wi=c.I((J*J-k*k)**3,J**6);w[i]=wi[0]*WS//S
  assert max(abs(wi[0]*WS-int(w[i])*S),abs(wi[1]*WS-int(w[i])*S))<=2*S
  # w floor uses exact rational, no compounded error (checked below).
  w[i]=((J*J-k*k)**3*WS)//J**6
  q=c.I(k,J);q2=c.mu(q,q);a=c.di(wi,sqrtJ)
  center=int(d[i])*S//DS;di=(center-2*S//DS,center+2*S//DS);b=c.mu(c.mu(a,di),q)
  for k0 in range(m):
   X[i,k0]=quant(a,XS);X[i,k0+m]=quant(b,XS);a=c.mu(a,q2);b=c.mu(b,q2)
 # Exact integer matmul: Cauchy-Schwarz proves no int64 overflow.
 assert int(sumsquares(X,1).max())*int(sumsquares(Li,0).max())<2**124
 assert math.isqrt(int(sumsquares(X,1).max())*int(sumsquares(Li,0).max()))<2**62
 Z=(X@Li)//XS;zerr=2*F(4*n*r,XS*XS)*F(trace,T)+2*F(n*r,T)
 zb=int(sumsquares(Z,1).max());assert zb<2**52
 return w,Z,(1+1/Zeta)*zerr,zb

def run(par):
 start=time.time();base,mean,osc=bases()
 assert F(c.log(J,8)[0],S)-F(8,3*J)-F(1,1<<20)-C-eta>delta
 Li,trace,meta=tail_gram(base,par);print('tail Gram verified',par,time.time()-start,flush=True)
 dd,pd,gg=c.nodes();j=np.arange(M+par,J,2,dtype=np.int64);n=len(j);d=dd[par::2];p=pd[par::2];g=gg[par::2];jd=j*d;jj=j*j
 w,Z,zloss,zb=features(j,d,Li,trace);zf=Z.astype(float)
 maxpoly=F(4*m**m,(m+2)**(m+2));rem=F(26,1)**2/F(3,4)**2/delta*n*maxpoly**2*(F(1,J*J)+F(1,2*J*(4*m+1)))
 loss=(1+1/Reta)*rem+zloss
 C0=(C*T).numerator//(C*T).denominator;subdiag=ceilq((eta+shift+loss)*T)
 entryerr=F(1,1<<24)+F(51,WS)+F(4,T)
 def target(k):
  den=jj[:,None]-jj[None,k];same=den==0;den[same]=1
  q=np.floor_divide(jd[None,k]-jd[:,None],den);q[same]=0
  assert int(np.max(np.abs(q)))*abs(c.ia)<2**63
  R=-np.floor_divide(q*c.ia,(DS*IS)//T);ii,kk=np.where(same);R[ii,kk]=C0-p[ii]
  assert int(np.max(np.abs(R)))<17*T
  coeff=w[:,None]+w[None,k]-(w[:,None]*w[None,k])//WS
  assert int(coeff.min())>=0 and int(coeff.max())<=WS
  out=(R//WS)*coeff+((R%WS)*coeff)//WS
  out[ii,kk]+=g[ii]-C0-subdiag
  z=zf@zf[k].T;zi=z.astype(np.int64);assert np.array_equal(z,zi) and int(np.max(np.abs(zi)))<=zb
  out-=zi+zi//1000
  assert int(np.max(np.abs(out)))<2**52
  return out
 A=np.empty((n,n),order='F');bs=128
 for i in range(0,n,bs):k=slice(i,min(i+bs,n));A[:,k]=target(k).astype(float)/T
 print('built',par,n,time.time()-start,flush=True)
 R,info=lapack.dpotrf(A,lower=1,overwrite_a=1,clean=0);assert info==0 and np.shares_memory(A,R),(par,info)
 print('factored',par,time.time()-start,flush=True)
 for i in range(0,n,bs):
  k=slice(i,min(i+bs,n));R[k,:]=np.rint(R[k,:]*FS);R[k,:][np.arange(n)[None,:]>np.arange(n)[k,None]]=0
 assert all(np.isfinite(R[:,i:i+bs]).all() for i in range(0,n,bs))
 print('quantized',par,time.time()-start,flush=True)
 row2=np.zeros(n,dtype=np.int64)
 for i in range(0,n,bs):
  k=slice(i,min(i+bs,n));x=R[:,k].astype(np.int64);assert np.array_equal(x,R[:,k]);q=sumsquares(x,1);assert int(row2.max())+int(q.max())<2**52;row2+=q
 bound=int(row2.max());assert bound<2**52
 # Local replay checkpoints. Their SHA-256 values bind every separately executed residual block.
 prefix=f'/tmp/iv256_{par}'
 fac=np.lib.format.open_memmap(prefix+'_factor.npy',mode='w+',dtype=np.int32,shape=(n,n),fortran_order=True)
 for i in range(0,n,bs):
  k=slice(i,min(i+bs,n));x=R[:,k];assert np.max(np.abs(x))<2**31;fac[:,k]=x.astype(np.int32)
 fac.flush();del fac,R,A
 np.savez(prefix+'_target.npz',j=j,d=d,p=p,g=g,w=w,Z=Z,subdiag=np.int64(subdiag),C0=np.int64(C0))
 result={'parity':par,'cutoff':J,'dimension':n,'rank':r,'coercivity':'1/1000','scale':str(T),'tail':meta,'mean_upper_scaled':str(mean),'oscillation_upper_scaled':str(osc),'series_remainder_squared':str(rem),'feature_penalty_loss':str(zloss),'total_penalty_loss':str(loss),'Z_row_square_max':str(zb),'factor_row_square_max':str(bound),'entry_error':str(entryerr),'factor_sha256':sha(prefix+'_factor.npy'),'target_sha256':sha(prefix+'_target.npz'),'stage':'factor prepared; NOT certified','elapsed_seconds':time.time()-start}
 open(prefix+'_stage.json','w').write(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)

def sha(path):
 h=hashlib.sha256()
 with open(path,'rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()

def verify(par,block):
 start=time.time();prefix=f'/tmp/iv256_{par}';meta=json.load(open(prefix+'_stage.json'))
 assert sha(prefix+'_factor.npy')==meta['factor_sha256'] and sha(prefix+'_target.npz')==meta['target_sha256']
 R=np.load(prefix+'_factor.npy',mmap_mode='r');data=np.load(prefix+'_target.npz');j,d,p,g,w,Z=[data[k] for k in ('j','d','p','g','w','Z')];subdiag=int(data['subdiag']);C0=int(data['C0']);n=len(j);jd=j*d;jj=j*j;zf=Z.astype(float);zb=int(meta['Z_row_square_max']);bound=int(meta['factor_row_square_max'])
 def target(k):
  den=jj[:,None]-jj[None,k];same=den==0;den[same]=1
  q=np.floor_divide(jd[None,k]-jd[:,None],den);q[same]=0
  assert int(np.max(np.abs(q)))*abs(c.ia)<2**63
  R0=-np.floor_divide(q*c.ia,(DS*IS)//T);ii,kk=np.where(same);R0[ii,kk]=C0-p[ii]
  assert int(np.max(np.abs(R0)))<17*T
  coeff=w[:,None]+w[None,k]-(w[:,None]*w[None,k])//WS
  assert int(coeff.min())>=0 and int(coeff.max())<=WS
  out=(R0//WS)*coeff+((R0%WS)*coeff)//WS;out[ii,kk]+=g[ii]-C0-subdiag
  z=zf@zf[k].T;zi=z.astype(np.int64);assert np.array_equal(z,zi) and int(np.max(np.abs(zi)))<=zb
  out-=zi+zi//1000;assert int(np.max(np.abs(out)))<2**52
  return out
 big=2048;i=block*big;end=min(i+big,n);assert 0<=i<end
 # For every lower entry in this block the complete dot product needs only columns < end.
 V=blas.dgemm(1.,np.array(R[i:,:end],dtype=float,order='F'),np.array(R[i:end,:end],dtype=float,order='F'),trans_b=True)
 er=np.zeros(n,dtype=np.int64);mx=0;bs=128
 for b in range(i,end,bs):
  k=slice(b,min(b+bs,end));v=V[:,b-i:k.stop-i].astype(np.int64);mask=np.arange(i,n)[:,None]>=np.arange(n)[None,k]
  assert np.array_equal(V[:,b-i:k.stop-i][mask],v[mask]) and int(np.max(np.abs(v[mask])))<=bound
  x=np.abs(target(k)[i:,:]-v);x[~mask]=0;mx=max(mx,int(x.max()));assert n*mx<2**62
  er[i:]+=np.sum(x,axis=1,dtype=np.int64);er[k]+=np.sum(x,axis=0,dtype=np.int64)-x[np.arange(n)[k]-i,np.arange(k.stop-k.start)]
 path=prefix+f'_residual_{block}.npy';np.save(path,er);rec={'block':block,'first':i,'last_exclusive':end,'max_entry':str(mx),'max_partial_row':str(int(er.max())),'sha256':sha(path),'factor_sha256':meta['factor_sha256'],'target_sha256':meta['target_sha256'],'elapsed_seconds':time.time()-start};open(prefix+f'_residual_{block}.json','w').write(json.dumps(rec,indent=2)+'\n');print(json.dumps(rec),flush=True)

def finish(par):
 prefix=f'/tmp/iv256_{par}';meta=json.load(open(prefix+'_stage.json'));n=meta['dimension'];er=np.zeros(n,dtype=np.int64);records=[];mx=0
 for b in range((n+2047)//2048):
  rec=json.load(open(prefix+f'_residual_{b}.json'));path=prefix+f'_residual_{b}.npy';assert rec['block']==b and rec['first']==b*2048 and rec['last_exclusive']==min((b+1)*2048,n) and sha(path)==rec['sha256'] and rec['factor_sha256']==meta['factor_sha256'] and rec['target_sha256']==meta['target_sha256'];x=np.load(path);assert x.shape==(n,) and x.dtype==np.int64 and int(x.min())>=0 and int(x.max())==int(rec['max_partial_row']);mx=max(mx,int(rec['max_entry']));assert n*mx<2**62 and int(er.max())+int(x.max())<2**63;er+=x;records.append(rec)
 maxerr=int(er.max());lb=shift-F(maxerr,T)-n*F(meta['entry_error']);assert lb>0,(par,lb)
 meta.update({'stage':'complete','max_residual_row_scaled':str(maxerr),'schur_surplus_lower':str(lb),'certified':True,'residual_blocks':records});print(json.dumps(meta),flush=True);open(f'/tmp/iv256_parity_{par}.json','w').write(json.dumps(meta,indent=2)+'\n')
if __name__=='__main__':
 par=int(sys.argv[1]);mode=sys.argv[2] if len(sys.argv)>2 else 'prepare'
 if mode=='prepare':run(par)
 elif mode=='verify':verify(par,int(sys.argv[3]))
 elif mode=='finish':finish(par)
 else:raise ValueError(mode)
