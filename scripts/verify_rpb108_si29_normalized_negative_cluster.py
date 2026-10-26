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
p=argparse.ArgumentParser();p.add_argument('--certificate',required=True);p.add_argument('--output',default='artifacts/si29_normalized_negative_cluster.json');a=p.parse_args()
raw=Path(a.certificate).read_bytes();assert hashlib.sha256(raw).hexdigest()==SHA
z=json.loads(raw);ctx.prec=z['working_precision_bits'];assert ctx.prec==4096
nodes=[(F(c),p) for c,p in z['original_source_nodes']];features=[(F(c),F(r),d) for c,r,d in z['feature_definitions']]
assert len(nodes)==107 and sum(p for c,p in nodes)==469 and len(features)==14
X=arb_mat([[ball(v) for v in row] for row in z['full_physical_projection_coefficient_balls']]);C=arb_mat([[dy(v) for v in row] for row in z['exact_dyadic_feature_transform']])
terms=[m.source_terms(c,k) for c,p in nodes for k in range(p)]+[m.pole_terms()]+[m.feature_terms(f) for f in features]
kernel=m.Integrals()
# Check the first omitted generator (order 15) as well as all true features.
m.independent_series_check([(nodes[0][0],nodes[0][1]+1)]+nodes[1:],features,kernel)
from validate_rpb108_si10_complement_positivity import protected_inner_cover,KAPPA
clusters,_,_,leaves,_=protected_inner_cover()
assert len(clusters)==107 and leaves==973 and KAPPA==F(1,1000)
Q=arb_mat([[-X[i,j] for j in range(14)] for i in range(470)]+[[arb(int(i==j)) for j in range(14)] for i in range(14)])*C
rows=[];total=F(0)
for index,((lo,hi,mass),(center,p)) in enumerate(zip(clusters,nodes)):
 assert center==(lo+hi)/2 and p==m.taylor_order(hi-lo,9)[0]
 radius=(hi-lo)/2;shifted=mass+2*KAPPA*(hi-lo)
 phi=m.source_terms(center,p)
 jet=arb_mat([[m.gram(phi,t,kernel) for t in terms]])*Q
 scale=(2*kernel.pi)**p/m.factorial(p)
 vector=[jet[0,j]*scale for j in range(14)]
 norm=sum((v*v for v in vector),arb(0))
 # Extract an exact dyadic upper endpoint, avoiding decimal serialization.
 norm_upper=rat(m.dyadic(norm.upper()))
 assert norm_upper>=0
 first=radius**(2*p)*norm_upper
 error2=2*m.B*F(101,100)*(F(44,7)*m.B*radius)**(2*p+2)/m.factorial(p+1)**2
 choices=[((1+d)*first+(1+1/d)*error2,d) for d in [F(2)**k for k in range(-16,17)]]
 bound,delta=min(choices);total+=shifted*bound
 rows.append(dict(cluster=index,lo=str(lo),hi=str(hi),order=p,shifted_two_sided_mass=str(shifted),first_omitted_jet_balls=[m.ball(v) for v in vector],jet_norm_squared_upper=str(norm_upper),remainder_norm_squared_upper=str(error2),young_parameter=str(delta),cluster_negative_operator_upper=str(shifted*bound)))
 if index%25==0:print('Actual negative cluster',index,flush=True)
baseline=F(101,100)*F(1,15000)
assert total<F(1,500000)
r=dict(status='ACTUAL_NORMALIZED_FULL_J_NEGATIVE_CLUSTER_LOEWNER_UPPER',native_input_sha256=SHA,original_J_count=470,actual_feature_count=14,cluster_count=107,negative_leaf_count=973,cluster_witnesses=rows,exact_negative_operator_upper=str(total),rational_negative_operator_upper='1/500000',inherited_universal_complement_upper=str(baseline),strict_improvement_over_universal=total<baseline,basis='W=(I-P_J470)FC without endpoint alignment',negative_multiplier='(kappa-m)_+ with SI10 kappa=1/1000',energy_projected_negative_operator_computed=False,actual_Astar_projection_computed=False,matched_forcing_computed=False,inverse_response_certified=False,W_ODD_NEG='OPEN',inherited_original_domain_review='OPEN')
out=Path(a.output);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(r,indent=2)+'\n')
print('ACTUAL COMPLETE NEGATIVE CLUSTER UPPER',float(total),'universal',float(baseline),'improved',total<baseline)
