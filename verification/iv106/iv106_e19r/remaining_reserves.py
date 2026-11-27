"""E19R: exact directional pole reuse and bump-independent packed proxy reserve.
Conditional on E19Q's analytic and integer contraction attachments.
"""
from fractions import Fraction as F
from math import factorial,isqrt
from pathlib import Path
import numpy as np, hashlib,json
p=Path(__file__).parent; h=F(11,3325); N=665; D=10**12; P=2**20; Hout=2**16; L=F(257,2)
base=p.parent/'iv106_e19p'/'row_bank.npz'; mat=p.parent/'iv106_e19q'/'joint_matrix.npz'; cert=p.parent/'iv106_e19q'/'joint_certificate.json'
assert hashlib.sha256(base.read_bytes()).hexdigest()=='e55b8992e769d09ee83fdd66a9d6a3cbaf592933f7d85d3ca0d8dd9a2e4d886e'
assert hashlib.sha256(mat.read_bytes()).hexdigest()=='24e37cd533c5efbc554c926695fc89f64d39d60aee90cb6643c5aa3a69da23e7'
assert hashlib.sha256(cert.read_bytes()).hexdigest()=='d61da378760ca11e21c7e828b46a717d810116d35dfc03d5ec325f1f6ddbb8c9'
j=json.loads(cert.read_text()); z=np.load(base); X=z['X'].astype(object); G=z['G'].astype(object); M=np.load(mat)['M'].astype(object)
def sqrtup(v,scale=10**12):
    assert v>=0; z=(v.numerator*scale**2+v.denominator-1)//v.denominator; a=isqrt(z); return F(a+(a*a<z),scale)
# p(x)=2sinh(x/2), midpoint rational odd Taylor to degree 15.
# e^.55<2 via exp series geometric upper; cosh(.55)<6/5.
t=F(11,20); cosh=sum(t**(2*n)/factorial(2*n) for n in range(9)); cosh+=t**18/factorial(18)/(1-t*t/F(19*20)); assert cosh<F(6,5)
rem=2*t**17/factorial(17)/(1-t*t/F(18*19)); assert rem<F(1,10**12)
c=[]
for i in range(N):
    t=(-F(11,10)+(F(i)+F(1,2))*h)/2
    a=2*sum(t**(2*n+1)/factorial(2*n+1) for n in range(8)); c.append(round(D*a))
c=np.array(c,dtype=object); assert all(c[i]==-c[N-1-i] for i in range(N)); c2=F(sum(a*a for a in c),D*D)
# E19Q exact midpoint contraction and matrix error in this direction.
mid0=h*F(int(c@M@c),2*Hout*P*P*D*D)
mid=mid0+(F(j['gram_error'])+F(j['intermediate_rounding_upper']))*c2
assert mid>=0
pert=F(j['quantization_norm'])*sqrtup(c2)
finite=(sqrtup(mid)+pert)**2
# Direction-specific jump tails, using Parseval on aggregate coefficients.
x=X@c; g=G@c; q=np.concatenate([-g[:64],D*c,-g[64:]])
def jump2(a):
    a=[0]+list(a)+[0];return F(sum((b-a)**2 for a,b in zip(a,a[1:])),D**4)
ax=jump2(x); aq=jump2(q)
tail=2*h/F(36)*(2*(11/L**2+12/L)*ax+2*(1/L**2+1/L)/9*aq)
# L2 error of piecewise midpoint approximation: derivative <=6/5,
# squared integral of distance to midpoint is N*h^3/12; Taylor + rounding < 2/D.
physical=sqrtup(F(6,5)**2*N*h**3/12)+F(2,D)*sqrtup(N*h)
pole=sqrtup(finite+tail)+physical
# Packed columns: actual profile 1 on central width 1/(2000k), 0 outside
# total width 3/(2000k); half-height on transition strips is a proxy.
# Pointwise error <=1/2 on transition width 1/(1000k), supports disjoint.
k=34; packed_proxy=F(1,4000*k); packed_zero=F(1,1000*k)
# Joint combined reserve from cell synthesis and pole using same bank:
# ||E_cell c+E_cell a d|| <= eps ||c+a*d||. No independence assumed.
# A safe joint norm via separate column-map bounds (Cauchy-Schwarz).
combined=F(j['total_upper'])+pole**2+packed_zero
out=dict(status='conditional analytic arithmetic; no packed proxy Riesz enclosure yet',pole_coefficients=[str(F(a,D)) for a in c],pole_coefficient_norm_sq=str(c2),midpoint_direction=str(mid0),finite_upper=str(finite),tail_upper=str(tail),physical_approximation_norm=str(physical),pole_norm_upper=str(pole),packed_zero_squared=str(packed_zero),packed_proxy_physical_squared=str(packed_proxy),combined_700_row_squared_upper=str(combined),combined_700_row_norm_upper=str(sqrtup(combined)))
(p/'remaining_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
for k,v in out.items():
    if k not in ['status','pole_coefficients']:print(k,float(F(v)),v)
# Dedicated joint solve in the same original basis (floating-point only for candidate selection).
from scipy.linalg import solve
zz=np.load(mat); H=2**30; wa,wv,wc=[zz[n] for n in ['wa','wv','wc']]; ids=np.arange(N); ext=z['ext']; allids=np.arange(-64,N+64)
def toep(v,a,b):return v[np.abs(a[:,None]-b)]
A=toep(wa,ids,ids); V=toep(wv,allids,allids); C=toep(wc,ids,allids)
ci=np.arange(64,64+N); ei=np.r_[np.arange(64),np.arange(64+N,64+N+64)]
cfloat=np.array(c,dtype=float)/D
system=np.block([[A,C[:,ei]],[C[:,ei].T,V[np.ix_(ei,ei)]]]).astype(float)/H
rhs=np.r_[C[:,ci]@cfloat,V[np.ix_(ei,ci)]@cfloat]/H
sol=solve(system,rhs,assume_a='pos'); xx=np.rint(D*sol[:N]).astype(np.int64).astype(object); gg=np.rint(D*sol[N:]).astype(np.int64).astype(object)
qq=np.concatenate([-gg[:64],c,-gg[64:]])
# No coefficient quantization or intermediate rounding in replay: direct arbitrary precision integers.
qint=int(xx@A.astype(object)@xx+qq@V.astype(object)@qq-2*(xx@C.astype(object)@qq))
lx=F(sum(abs(a) for a in xx),D); lq=F(sum(abs(a) for a in qq),D)
ea,ev,ec=j['gram_errors']; reserve=h/H*(ea*lx*lx+ev*lq*lq+2*ec*lx*lq)
finite2=h*F(qint,H*D*D)+reserve
assert finite2>=0
ax2=jump2(xx*D); aq2=jump2(qq*D)
tail2=2*h/F(36)*(2*(11/L**2+12/L)*ax2+2*(1/L**2+1/L)/9*aq2)
pole2=sqrtup(finite2+tail2)+physical
combined2=F(j['total_upper'])+pole2**2+packed_zero
out.update(dedicated_pole_interior=[str(F(a,D)) for a in xx],dedicated_pole_exterior=[str(F(a,D)) for a in gg],dedicated_finite_upper=str(finite2),dedicated_gram_error=str(reserve),dedicated_tail_upper=str(tail2),dedicated_pole_norm_upper=str(pole2),dedicated_combined_700_row_squared_upper=str(combined2),dedicated_combined_700_row_norm_upper=str(sqrtup(combined2)))
(p/'remaining_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
for k in ['dedicated_finite_upper','dedicated_gram_error','dedicated_tail_upper','dedicated_pole_norm_upper','dedicated_combined_700_row_squared_upper','dedicated_combined_700_row_norm_upper']:print(k,float(F(out[k])),out[k])
