#!/usr/bin/env python3
"""Whole original J470-complement negative leakage via joint Hermite zeros."""
import argparse,hashlib,json,time
from fractions import Fraction as F
from math import factorial
from pathlib import Path
PIN={'native':'c9ee487f8abe7b633c47d2ef7d72e2cc4f7289bc794b2d8fc02bb61520b25e60',
 'negative':'a693261c31f01a4a1e11ea6400e5173435a8260b41b1f6b43aa6f67f784ccb7f',
 'threshold':'4cc8e320de50918965ce1c47acbf7cdd87747bdb373c6a5da6a2ae1b3b0d8ba2'}
B=F(11,10);OMEGA=F(44,7)*B;KAPPA=F(1,1000)

def select(l,r,nodes):
 # For fixed N, nearest repeated nodes minimize this interval product cap.
 ordered=sorted((max(abs(l-c),abs(r-c)),i,p) for i,(c,p) in enumerate(nodes))
 v=F(1);N=0;selected=[0]*len(nodes);best=None
 for d,i,p in ordered:
  for unused in range(p):
   N+=1;selected[i]+=1;v*=OMEGA*d/N;E=2*B*v*v/(2*N+1)
   if best is None or E<best[0]:best=(E,N,selected[:])
 return best

def main():
 p=argparse.ArgumentParser()
 for key in PIN:p.add_argument('--'+key+'-certificate',required=True)
 p.add_argument('--output',default='artifacts/original_full_complement_hermite.json');args=p.parse_args();data={};start=time.monotonic()
 for key,sha in PIN.items():
  raw=Path(getattr(args,key+'_certificate')).read_bytes();assert hashlib.sha256(raw).hexdigest()==sha;data[key]=json.loads(raw)
 z=data['native'];neg=data['negative'];prior=data['threshold']
 assert neg['matched_native_physical_projection_sha256']==PIN['native']
 nodes=[(F(c),p) for c,p in z['original_source_nodes']]
 assert len(nodes)==107 and sum(p for c,p in nodes)==469
 assert len({c for c,p in nodes})==107 and all(p>=1 for c,p in nodes)
 oldtheta=F(prior['same_original_SM40_threshold_exact']);assert 0<oldtheta<F(97,100)
 rows=[];leafrows=[];index=0;epsilon=F(0);whole_cluster_epsilon=F(0)
 leaves=[tuple(map(F,row)) for row in neg['original_leaf_witnesses']];assert len(leaves)==973
 for i,cl in enumerate(neg['cluster_witnesses']):
  l,r=F(cl['lo']),F(cl['hi']);assert nodes[i][0]==(l+r)/2 and nodes[i][1]==cl['order']
  E,N,counts=select(l,r,nodes);selection=[(j,k) for j,k in enumerate(counts) if k]
  fac=2*B*OMEGA**(2*N)/((2*N+1)*factorial(N)**2)
  cluster_pay=F(0);mass=F(0);local_count=0;last=l
  while index<len(leaves) and leaves[index][0]<r:
   a,b,h=leaves[index];assert a==last and l<=a<b<=r and h>=0
   product=F(1)
   for j,k in selection:
    c=nodes[j][0];product*=max(abs(a-c),abs(b-c))**(2*k)
   bound=fac*product;assert 0<bound<=E
   m=2*(b-a)*(h+KAPPA);pay=m*bound;mass+=m;cluster_pay+=pay
   leafrows.append(dict(cluster=i,lo=str(a),hi=str(b),shifted_two_sided_mass=str(m),Fourier_squared_operator_upper=str(bound),negative_payment=str(pay)))
   index+=1;local_count+=1;last=b
  assert last==r and local_count>0 and mass==F(cl['two_sided_mass'])
  epsilon+=cluster_pay;whole_cluster_epsilon+=mass*E
  rows.append(dict(cluster=i,lo=str(l),hi=str(r),total_multiplicity=N,source_multiplicities=selection,whole_cluster_Fourier_squared_upper=str(E),two_sided_mass=str(mass),negative_payment=str(cluster_pay)))
 assert index==973 and len(rows)==107 and epsilon<F(213,10**9)<KAPPA
 theta=1-epsilon/KAPPA;old_epsilon=KAPPA*(1-oldtheta)
 assert theta>F(999787,10**6)>oldtheta and old_epsilon/epsilon>141
 result=dict(status='CONDITIONAL_ORIGINAL_WHOLE_J470_COMPLEMENT_HERMITE_LEAKAGE',
  input_sha256=PIN,physical_half_width=str(B),source_count=470,source_sine_cosine_generators=469,
  original_cluster_count=107,original_negative_leaf_count=973,cluster_witnesses=rows,leaf_witnesses=leafrows,
  whole_cluster_only_negative_upper=str(whole_cluster_epsilon),whole_complement_negative_operator_upper=str(epsilon),
  clean_whole_complement_negative_upper='213/1000000000',
  prior_SM40_complement_negative_upper=str(old_epsilon),full_complement_bound_improvement_factor=str(old_epsilon/epsilon),
  signed_complement_lower=str(KAPPA-epsilon),sufficient_energy_dual_threshold=str(theta),
  clean_sufficient_threshold_lower='999787/1000000',prior_SM40_sufficient_threshold=str(oldtheta),
  uniform_original_space='ALL odd physical f with J470* f=0; not only fourteen SI29 features',
  source_space_changed=False,extra_source_directions_added=0,frequency_integration_repeated=False,
  global_source_monomial_approximation_used=False,extra_reflection_factor_applied=False,
  original_signed_negative_direction_proved=False,new_threshold_Galerkin_cap_gate_evaluated=False,
  original_470_inverse_response_computed=False,original_full_strong_residual_computed=False,
  prior_theta_at_most_97percent_method_stop_overturned=False,
  W_ODD_NEG='OPEN',inherited_original_domain_review='OPEN',elapsed_seconds=time.monotonic()-start)
 out=Path(args.output);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+'\n')
 print('WHOLE ORIGINAL COMPLEMENT HERMITE LEAKAGE PASS: epsilon <2.13e-7; sufficient theta >0.999787; no source added; signed gate OPEN; seconds',round(result['elapsed_seconds'],2))
if __name__=='__main__':main()
