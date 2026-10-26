import argparse,json,hashlib,sys
from fractions import Fraction as F
from pathlib import Path
from flint import arb,acb,arb_mat,ctx
import verify_rpb108_si29_full_J_L2_normalization as m
SHA='c9ee487f8abe7b633c47d2ef7d72e2cc4f7289bc794b2d8fc02bb61520b25e60'
def dy(x):return arb((int(x[0]),int(x[1])))
def ball(x):return arb(dy(x[0]),dy(x[1]))
class Kernel(m.Integrals):
 def _get(self,p,kind,f):
  if p>=-4 or f==(0,0):return super()._get(p,kind,f)
  assert p in (-5,-6)
  w=self.w(f);b=self.b;n=-p;t=w*b
  reg=(t.sin() if kind=='s' else t.cos())
  for k in range(1 if kind=='s' else 0,n-1,2):
   reg-=(-1)**(k//2)*t**k/m.factorial(k)
  return -reg/((n-1)*b**(n-1))+(w if kind=='s' else -w)*self._get(p+1,'c' if kind=='s' else 's',f)/(n-1)
def derivative(terms,kernel):
 out=[]
 for p,t,f,c in terms:
  if p:out.append((p-1,t,f,c*p))
  out.append((p,'c' if t=='s' else 's',f,c*kernel.w(f)*(1 if t=='s' else -1)))
 return out
def endpoint(terms,kernel):
 z=acb(0)
 for p,t,f,c in terms:
  w=kernel.w(f)*kernel.b
  z+=c*kernel.b**p*(w.sin() if t=='s' else w.cos())
 assert z.imag.contains(0)
 return z.real
def rat(x):
 n,e=int(x[0]),int(x[1]);return F(n*2**max(e,0),2**max(-e,0))
def exact_bound(D,v):
 trace=sum((rat(D[i][i][0])+rat(D[i][i][1]) for i in range(14)),F(0))
 e=sum(((abs(rat(x[0]))+rat(x[1]))**2 for x in v),F(0))
 return F(36)*F(101,100)+8*e+4*m.B*trace
p=argparse.ArgumentParser();p.add_argument('--certificate',required=True);p.add_argument('--output',default='artifacts/si29_normalized_energy_upper.json');a=p.parse_args()
raw=Path(a.certificate).read_bytes();assert hashlib.sha256(raw).hexdigest()==SHA
z=json.loads(raw);ctx.prec=z['working_precision_bits'];assert ctx.prec==4096
nodes=[(F(c),p) for c,p in z['original_source_nodes']];features=[(F(c),F(r),d) for c,r,d in z['feature_definitions']]
assert len(nodes)==107 and sum(p for c,p in nodes)==469 and len(features)==14
X=arb_mat([[ball(v) for v in row] for row in z['full_physical_projection_coefficient_balls']]);C=arb_mat([[dy(v) for v in row] for row in z['exact_dyadic_feature_transform']])
terms=[m.source_terms(c,k) for c,p in nodes for k in range(p)]+[m.pole_terms()]+[m.feature_terms(f) for f in features]
kernel=Kernel();ds=[derivative(t,kernel) for t in terms]
# Independent entire-series derivative Gram for all actual 14 features.
K=255; powers=list(range(1,K+1,2)); V=arb_mat(128,14); eps=[]; amps=[]
for j,f in enumerate(features):
 c,r,d=f; mu=m.band_moments(f,K); t=F(44,7)*m.B*(c+r); scale=F(44,7)*(c+r)*(F(3,2) if d else 1)
 for i,n in enumerate(powers):V[i,j]=(-1)**((n-1)//2)*m.a(mu[n])*(2*kernel.pi)**n*kernel.b**(n-1)/m.factorial(n-1)
 eps.append(m.a(scale*t**255/m.factorial(255)));amps.append(m.a(scale))
M=arb_mat([[2*kernel.b/(i+j-1) for j in powers] for i in powers])
poly=V.transpose()*M*V
for i in range(14):
 for j in range(i+1):
  payment=2*kernel.b*(eps[i]*amps[j]+eps[j]*amps[i]+eps[i]*eps[j])
  assert abs(m.gram(ds[470+i],ds[470+j],kernel)-poly[i,j])<payment,('derivative series',i,j)
print('Independent actual 14-feature derivative Gram series PASS',flush=True)
G=arb_mat(484,484)
for i in range(484):
 for j in range(i+1):G[i,j]=G[j,i]=m.gram(ds[i],ds[j],kernel)
 if i%100==0:print('Derivative Gram row',i,flush=True)
Q=arb_mat([[-X[i,j] for j in range(14)] for i in range(470)]+[[arb(int(i==j)) for j in range(14)] for i in range(14)])*C
D=Q.transpose()*G*Q;D=(D+D.transpose())/2
v=arb_mat([[endpoint(t,kernel) for t in terms]])*Q
Db=m.balls(D);vb=[m.ball(v[0,j]) for j in range(14)]
u=exact_bound(Db,vb);assert u>0
U=1
while U<u:U*=2
floor=F(z['normalized_Astar_energy_Schur_lower']);assert floor==F(3328479,10**11)
r=dict(status='CONDITIONAL_ACTUAL_NORMALIZED_FULL_J_ENERGY_UPPER',native_input_sha256=SHA,working_precision_bits=4096,independent_derivative_series_check=True,normalized_derivative_Gram_balls=Db,normalized_endpoint_balls=vb,exact_variation_energy_upper=str(u),rational_energy_operator_upper=U,conditional_energy_lower=str(floor),conditional_energy_condition_number_upper=str(F(U)/floor),physical_basis='W=(I-P_J470) F C',actual_Astar_projection_computed=False,normalized_forcing_computed=False,inverse_response_certified=False,W_ODD_NEG='OPEN',inherited_original_domain_review='OPEN')
out=Path(a.output);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(r,indent=2)+'\n')
print('NORMALIZED ENERGY UPPER PASS',U,'condition upper',float(F(U)/floor))
