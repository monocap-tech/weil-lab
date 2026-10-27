#!/usr/bin/env python3
"""Independent exact products/multiplicities/masses and Hermite regressions."""
import hashlib,json,sys
from fractions import Fraction as F
from math import factorial
from pathlib import Path

def mul(A,B):
 C=[F(0)]*(len(A)+len(B)-1)
 for i,a in enumerate(A):
  for j,b in enumerate(B):C[i+j]+=a*b
 return C
def evaluate(P,x):return sum((v*x**i for i,v in enumerate(P)),F(0))
def derivative(P):return [(i+1)*v for i,v in enumerate(P[1:])]
def regressions():
 # Repeated-node Rolle remainder saturates for a monic nodal polynomial.
 ns=[(F(0),2),(F(1),3),(F(-1,2),1)];P=[F(1)];N=6
 for c,n in ns:
  for k in range(n):P=mul(P,[-c,F(1)])
 for c,n in ns:
  D=P[:]
  for k in range(n):assert evaluate(D,c)==0;D=derivative(D)
 D=P[:]
 for k in range(N):D=derivative(D)
 assert D==[F(factorial(N))]
 x=F(2,3);product=F(1)
 for c,n in ns:product*=(x-c)**n
 assert evaluate(P,x)==product
 # Derivative L2-moment factor and reflected +kappa mass.
 B=F(11,10)
 for n in (2,7,11):assert 2*B**(2*n+1)/(2*n+1)==2*B*B**(2*n)/(2*n+1)
 assert 2*F(1,16)*(F(3,2)+F(1,1000))==F(1501,8000)
 return True

def main():
 z=json.load(open(sys.argv[1]));native=json.load(open(sys.argv[2]));neg=json.load(open(sys.argv[3]));old=json.load(open(sys.argv[4]))
 expected=['c9ee487f8abe7b633c47d2ef7d72e2cc4f7289bc794b2d8fc02bb61520b25e60','a693261c31f01a4a1e11ea6400e5173435a8260b41b1f6b43aa6f67f784ccb7f','4cc8e320de50918965ce1c47acbf7cdd87747bdb373c6a5da6a2ae1b3b0d8ba2']
 for key,path,sha in zip(['native','negative','threshold'],sys.argv[2:5],expected):
  assert hashlib.sha256(Path(path).read_bytes()).hexdigest()==z['input_sha256'][key]==sha
 assert z['status']=='CONDITIONAL_ORIGINAL_WHOLE_J470_COMPLEMENT_HERMITE_LEAKAGE'
 nodes=[(F(c),p) for c,p in native['original_source_nodes']];assert len(nodes)==107 and sum(n for c,n in nodes)+1==470
 assert len({c for c,n in nodes})==107 and all(n>=1 for c,n in nodes)
 assert z['source_count']==470 and z['source_sine_cosine_generators']==469
 B=F(11,10);omega=F(44,7)*B;eps=F(0);whole=F(0);idx=0
 assert len(z['cluster_witnesses'])==107 and len(z['leaf_witnesses'])==973
 for i,(r,o) in enumerate(zip(z['cluster_witnesses'],neg['cluster_witnesses'])):
  assert r['cluster']==i and r['lo']==o['lo'] and r['hi']==o['hi']
  a,b=F(r['lo']),F(r['hi']);sel=r['source_multiplicities'];assert len({j for j,n in sel})==len(sel)
  assert all(0<=j<107 and isinstance(n,int) and 1<=n<=nodes[j][1] for j,n in sel)
  N=sum(n for j,n in sel);assert N==r['total_multiplicity'] and 1<=N<=469
  product=F(1)
  for j,n in sel:product*=max(abs(a-nodes[j][0]),abs(b-nodes[j][0]))**(2*n)
  prefactor=2*B*omega**(2*N)/((2*N+1)*factorial(N)**2);E=prefactor*product
  assert E==F(r['whole_cluster_Fourier_squared_upper'])
  mass=F(0);pay=F(0);last=a
  while idx<973 and int(z['leaf_witnesses'][idx]['cluster'])==i:
   v=z['leaf_witnesses'][idx];l,h,height=map(F,neg['original_leaf_witnesses'][idx]);assert F(v['lo'])==l==last and F(v['hi'])==h and a<=l<h<=b
   d=F(1)
   for j,n in sel:d*=max(abs(l-nodes[j][0]),abs(h-nodes[j][0]))**(2*n)
   local=prefactor*d;m=2*(h-l)*(height+F(1,1000))
   assert local==F(v['Fourier_squared_operator_upper'])<=E and m==F(v['shifted_two_sided_mass'])
   assert m*local==F(v['negative_payment']);pay+=m*local;mass+=m;last=h;idx+=1
  assert last==b and mass==F(o['two_sided_mass'])==F(r['two_sided_mass'])
  assert pay==F(r['negative_payment']);eps+=pay;whole+=mass*E
 assert idx==973 and eps==F(z['whole_complement_negative_operator_upper'])<F(z['clean_whole_complement_negative_upper'])==F(213,10**9)
 assert whole==F(z['whole_cluster_only_negative_upper']) and eps<whole
 kappa=F(1,1000);theta=1-eps/kappa;oldtheta=F(old['same_original_SM40_threshold_exact'])
 assert theta==F(z['sufficient_energy_dual_threshold'])>F(z['clean_sufficient_threshold_lower'])==F(999787,10**6)>oldtheta
 assert kappa-eps==F(z['signed_complement_lower'])>0
 assert kappa*(1-oldtheta)/eps==F(z['full_complement_bound_improvement_factor'])>141
 for key in ('source_space_changed','frequency_integration_repeated','global_source_monomial_approximation_used','extra_reflection_factor_applied','original_signed_negative_direction_proved','new_threshold_Galerkin_cap_gate_evaluated','prior_theta_at_most_97percent_method_stop_overturned'):
  assert z[key] is False
 assert z['extra_source_directions_added']==0 and z['W_ODD_NEG']=='OPEN' and z['inherited_original_domain_review']=='OPEN' and regressions()
 print('INDEPENDENT WHOLE-COMPLEMENT REPLAY PASS: all multiplicities, 973 leaf payments, complete operator epsilon and threshold; actual signed gate OPEN')
if __name__=='__main__':main()
