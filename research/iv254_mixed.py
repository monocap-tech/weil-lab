"""IV254: sharpened infinite tail and rigorous failure of a diagonal-only inverse bound."""
import iv254_intermediate as c
from scipy.linalg import eigh
from fractions import Fraction as F
import numpy as np,json
T=c.T;S=c.S;N=32768;C=F(7979648,1000000)
def up(x):return c.ce(x.numerator*T,x.denominator)
def lower_gamma(j):return F(c.log(j,8)[0],S)-F(8,3*j)
def upper_gamma(j):return F(c.log(j,8)[1],S)+F(8,3*j)+F(2,9*j*j)
def boundary(j):return F(2,j)+F(43,j*j)
# Exact infinite coercivity for j>=23552, with pole loss as in finite certificate.
cut=23552;gap=lower_gamma(cut)-C-F(1,1<<20);assert gap>F(7,1000)
print('tail margin lower',float(gap),flush=True)
c.J=N+2048;dd,pd,_=c.nodes()
# Original normalized prime matrix centers, same bound as finite checker.
def prime(j,k):
 j=np.asarray(j,dtype=np.int64);k=np.asarray(k,dtype=np.int64);jd=j*dd[j-c.M];kd=k*dd[k-c.M]
 assert int(np.max(np.abs(jd)))<2**61 and int(np.max(np.abs(kd)))<2**61
 den=j[:,None]**2-k[None,:]**2;same=den==0;den[same]=1
 q=np.floor_divide(kd[None,:]-jd[:,None],den);q[same]=0
 assert int(np.max(np.abs(q)))*abs(c.ia)<2**63
 z=np.floor_divide(q*c.ia,(c.DS*c.IS)//T);a,b=np.where(same);z[a,b]=pd[j[a]-c.M];return z
# The binary64 candidate is only a proposal, never used to decide the sign.
lo=np.arange(N-1024+1,N,2);hi=np.arange(N+1,N+2048,2)
U=prime(lo,lo);V=prime(hi,lo);g=np.array([up(upper_gamma(int(j))) for j in lo],dtype=np.int64);d=np.array([up(upper_gamma(int(j))-C) for j in hi],dtype=np.int64);assert np.min(d)>0
A=np.diag(g.astype(float)/T)-U.astype(float)/T;B=V.astype(float)/T;D=d.astype(float)/T
F0=A-(B.T/D)@B
_,vec=eigh(F0,subset_by_index=[0,0]);v=vec[:,0];sel=np.sort(np.argsort(abs(v))[-256:]);b=np.rint(v[sel]/max(abs(v))*10000).astype(np.int64);lo=lo[sel];U=U[np.ix_(sel,sel)];V=V[:,sel];g=g[sel];bb=[int(x) for x in b];l1=sum(abs(x) for x in bb);norm=sum(x*x for x in bb)
q=sum(int(g[i])*bb[i]**2 for i in range(len(bb)))-sum(bb[i]*int(U[i,k])*bb[k] for i in range(len(bb)) for k in range(len(bb)))
q+=l1*l1*up(F(1,1<<24)+boundary(int(lo[0])))
pen=0
for i,j in enumerate(hi):
 x=abs(sum(int(a)*b for a,b in zip(V[i,:],bb)));err=l1*up(F(1,1<<24)+boundary(int(j)));z=max(0,x-err);pen+=z*z//int(d[i])
sup=q-pen
print('normalized Q upper, penalty lower, receiver upper',q/T/norm,pen/T/norm,sup/T/norm,flush=True)
assert 20*sup < -T*norm
out={'tail_cutoff':cut,'tail_margin_lower_numerator':str(gap.numerator),'tail_margin_lower_denominator':str(gap.denominator),'tail_margin_gt':'7/1000','diagonal_receiver_cutoff':N,'scale':str(T),'witness_modes':lo.tolist(),'integer_coefficients':bb,'squared_norm':str(norm),'Q_upper_scaled':str(q),'partial_penalty_lower_scaled':str(pen),'receiver_upper_scaled':str(sup),'normalized_receiver_upper_lt':'-1/20','high_rows':len(hi),'classification':'strict failure of diagonal-only receiver using gamma-C, not original Q or actual Schur'}
open('/tmp/iv254_mixed.json','w').write(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('witness_modes','integer_coefficients')}),flush=True)
