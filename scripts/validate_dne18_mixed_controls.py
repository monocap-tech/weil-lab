#!/usr/bin/env python3
"""Exact mixed crossing, nonorthogonal lift and physical-mass controls."""
from fractions import Fraction as F
from itertools import product
import json,sys
checks=0
dot=lambda x,y:sum((a*b for a,b in zip(x,y)),F(0))
C=[[F(1),F(1,10)],[F(1,10),F(6,5)]];k=F(11,25)
det=C[0][0]*C[1][1]-C[0][1]**2
assert C[0][0]>k and (C[0][0]-k)*(C[1][1]-k)>C[0][1]**2;checks+=1
G=[[C[1][1]/det,-C[0][1]/det],[-C[1][0]/det,C[0][0]/det]]
r0=[F(1,20),F(1,25)];rv=[F(-1,30),F(1,18)]
P0=dot(r0,r0);Pv=dot(rv,rv)
# Larger rational radii than Euclidean norms, sufficient for the controls.
s0=sum(abs(v) for v in r0);sv=sum(abs(v) for v in rv)
a=F(2);q=F(1);b=F(1,50);theta=F(2,5)
A=a-P0/k;D=q-Pv/k;B=abs(b)+s0*sv/k
assert B*B<(1-theta)**2*A*D;checks+=1
M=F(11,10);assert F(1)+F(1,5)**2+F(1,20)**2+F(1,100)**2<M*M;checks+=1
T=(1+s0/k)**2/(theta*A)+(M+sv/k)**2/(theta*D)+1/k
for t,u,z0,z1 in product((F(-1),F(0),F(1),F(2,3)),repeat=4):
 z=[z0,z1];r=[t*r0[i]+u*rv[i] for i in range(2)]
 energy=a*t*t+2*b*t*u+q*u*u+2*dot(r,z)+sum(z[i]*C[i][j]*z[j] for i in range(2) for j in range(2))
 Gr=[dot(rr,r) for rr in G]
 after=a*t*t+2*b*t*u+q*u*u-dot(r,Gr)
 zp=[z[i]+Gr[i] for i in range(2)]
 assert energy==after+sum(zp[i]*C[i][j]*zp[j] for i in range(2) for j in range(2));checks+=1
 assert after>=theta*(A*t*t+D*u*u);checks+=1
 # el=(1,0,0,0), v=(1/5,1,1/20,1/100); F is the last two
 # physical coordinates. This explicitly tests a nonorthogonal retained lift.
 physical=[t+u/F(5),u,z0+u/F(20),z1+u/F(100)]
 assert dot(physical,physical)<=T*energy;checks+=1
crossings=[]
for beta in (F(99,100),F(1),F(101,100)):
 determinant=1-beta*beta;level=1-beta
 assert (determinant>0)==(level>0)
 assert (determinant==0)==(level==0)
 assert (determinant<0)==(level<0);checks+=3
 crossings.append({'mixed':str(beta),'positive_individual_diagonals':True,'complete_mixed_determinant':str(determinant),'ground_level':str(level)})
levels=[]
for mu in (F(1,10**40),F(1,100),F(1,20)):
 diag=1+mu;off=F(1);high=k+mu
 assert diag-off==mu and diag*diag-off*off>0
 assert (diag-mu)**2-off*off==0 and high-mu==k;checks+=2
 levels.append({'mu':str(mu),'positive_original_ground_level':True,'whole_mass_shift_null':True})
prim=json.load(open(sys.argv[1]));rep=json.load(open(sys.argv[2]))
for p,r in zip(prim['parity_rows'],rep['parity_rows']):
 assert p['parity']==r['parity']
 for field in ('determinant_strict_lower','weighted_Schur_slack_strict_lower','whole_subspace_physical_gap_strict_lower'):
  assert F(p[field])>0 and F(r[field])>0;checks+=2
 assert F(r['whole_subspace_physical_gap_strict_lower'])>=F(p['whole_subspace_physical_gap_strict_lower']);checks+=1
 assert F(r['actual_Schur_mixed_absolute_upper'])<=F(p['actual_Schur_mixed_absolute_upper']);checks+=1
 assert F(p['whole_subspace_physical_gap_strict_lower'])>F(prim['restricted_original_physical_gap']);checks+=1
 assert F(p['mixed_square_over_diagonal_budget_upper'])<F(1);checks+=1
out={'stage':'DNE18','exact_fraction_assertions':checks,'status':'PASS',
 'finite_nonorthogonal_lift_and_physical_mass_controls':256,
 'primary_and_stronger_root_replay_passed':True,
 'genuine_mixed_crossing_controls':crossings,'positive_whole_mass_controls':levels,
 'controls_are_abstract':True,'whole_aperture_positive':False,'RH':False,'Lean':False}
open(sys.argv[3],'w').write(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
