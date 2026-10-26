import argparse,json,hashlib
from pathlib import Path
from fractions import Fraction as F
from flint import arb,arb_mat,ctx
import verify_rpb108_si29_full_J_L2_normalization as m
p=argparse.ArgumentParser();p.add_argument('--certificate',required=True);p.add_argument('--output',default='artifacts/si29_normalized_endpoint_alignment.json');args=p.parse_args()
raw=Path(args.certificate).read_bytes();assert hashlib.sha256(raw).hexdigest()=='c9ee487f8abe7b633c47d2ef7d72e2cc4f7289bc794b2d8fc02bb61520b25e60'
z=json.loads(raw);ctx.prec=4096
nodes=[(F(c),p) for c,p in z['original_source_nodes']];features=[(F(c),F(r),d) for c,r,d in z['feature_definitions']]
def dy(x):return arb((int(x[0]),int(x[1])))
def ball(x):return arb(dy(x[0]),dy(x[1]))
X=arb_mat([[ball(v) for v in row] for row in z['full_physical_projection_coefficient_balls']]);C=arb_mat([[dy(v) for v in row] for row in z['exact_dyadic_feature_transform']])
assert X.nrows()==470 and X.ncols()==C.nrows()==C.ncols()==14
ker=m.Integrals()
terms=[m.source_terms(c,k) for c,p in nodes for k in range(p)]+[m.pole_terms()]+[m.feature_terms(f) for f in features]
def derivative(ts):
 out=[]
 for p,t,f,c in ts:
  if p:out.append((p-1,t,f,c*p))
  out.append((p,'c' if t=='s' else 's',f,c*ker.w(f)*(1 if t=='s' else -1)))
 return out
def endpoint(ts):
 v=m.acb(0)
 for p,t,f,c in ts:
  q=ker.w(f)*ker.b;v+=c*ker.b**p*(q.sin() if t=='s' else q.cos())
 assert v.imag.contains(0)
 return v.real
Q=arb_mat([[-X[i,j] for j in range(14)] for i in range(470)]+[[arb(int(i==j)) for j in range(14)] for i in range(14)])*C
E=arb_mat([[endpoint(t) for t in terms],[endpoint(derivative(t)) for t in terms]])
V=E*Q
A=arb_mat([[E[i,j] for j in (0,469)] for i in range(2)])
det=A[0,0]*A[1,1]-A[0,1]*A[1,0];assert arb('944/1000')<det<arb('945/1000')
L=A.solve(-V,algorithm='lu')
Qa=arb_mat(Q)
for j in range(14):Qa[0,j]+=L[0,j];Qa[469,j]+=L[1,j]
res=E*Qa
assert all(res[i,j].contains(0) for i in range(2) for j in range(14))
r=dict(status='ACTUAL_FULL_J_NORMALIZED_14_DOUBLE_ENDPOINT_ALIGNMENT',native_input_sha256=hashlib.sha256(raw).hexdigest(),actual_feature_count=14,original_J_count=470,anchor_J_indices=[0,469],anchor_endpoint_matrix=m.balls(A),anchor_determinant=m.ball(det),original_normalized_endpoint_jets=m.balls(V),alignment_coefficient_balls=m.balls(L),aligned_endpoint_jet_enclosures=m.balls(res),exact_definition='L=-A_endpoint^-1 * [W(B);Wprime(B)] with W=(I-P_J470)FC',endpoint_value_and_derivative_exactly_zero_by_definition=True,physical_L2_quotient_Gram_unchanged=True,actual_Astar_energy_Schur_unchanged=True,matched_forcing_unchanged_for_JstarR0_zero=True,Fourier_decay_order=3,explicit_cubic_tail_constant_computed=False,actual_Astar_projection_computed=False,matched_forcing_computed=False,inverse_response_certified=False,W_ODD_NEG='OPEN',inherited_original_domain_review='OPEN')
out=Path(args.output);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(r,indent=2)+'\n');print('ACTUAL NORMALIZED 14 DOUBLE ENDPOINT ALIGNMENT PASS; cubic decay; quantitative tail and response OPEN')
