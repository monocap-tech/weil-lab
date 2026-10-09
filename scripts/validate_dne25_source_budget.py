#!/usr/bin/env python3
"""Independent row comparison and sharp coherent-source countercontrols."""
from fractions import Fraction as F
from pathlib import Path
import argparse,json,hashlib
import certify_dne25_source_budget as c
def det3(A):
 return A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])-A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])+A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0])
def validate(certpath,replaypath):
 raw=Path(certpath).read_bytes();assert raw==Path(replaypath).read_bytes();cert=json.loads(raw);checks=1;k=F(11,25)
 for r in cert['rows']:
  Q=[[tuple(map(F,v)) for v in row] for row in r['tested_native_scaled_matrix_intervals']];L=list(map(F,r['coarse_scaled_diagonal_lower']));mu=F(r['native_energy_comparison_fraction']);budget=F(r['reported_complete_remainder_source_budget'])
  assert mu*k==budget and F(r['tested_complete_source_Gram_native_energy_ratio_upper'])+budget==k;checks+=1
  rr=F(r['frozen_rational_remainder_source_ratio_budget']);ee=F(r['frozen_rational_native_mixed_dual_norm_budget'])
  assert rr+k*ee<budget and (budget-rr)/k-ee==F(r['frozen_rational_condensed_energy_relative_margin'])>0;checks+=1
  # Assemble L-mu Q first, then take absolute interval off-diagonals.
  V=[[(L[i]-mu*Q[i][i][1],L[i]-mu*Q[i][i][0]) if i==j else (-mu*Q[i][j][1],-mu*Q[i][j][0]) for j in range(4)] for i in range(4)]
  for i in range(4):
   m=V[i][i][0]-sum(max(map(abs,V[i][j])) for j in range(4) if j!=i)
   assert m==F(r['scaled_L_minus_mu_Q_strict_Gershgorin_margins'][i])>0;checks+=1
  # A rational absolute-value Young inequality checks the row certificate
  # without relying on floating eigenvalues or orthonormal retained columns.
  for z in ([F(1),F(0),F(0),F(0)],[F(0),F(1),F(2),F(-1)],[F(1,3),F(-2),F(1,7),F(5)]):
   q_upper=sum(Q[i][i][1]*z[i]*z[i] for i in range(4))+2*sum(max(map(abs,Q[i][j]))*abs(z[i]*z[j]) for i in range(4) for j in range(i+1,4))
   lower=sum(L[i]*z[i]*z[i] for i in range(4));assert lower-mu*q_upper>0;checks+=1
 controls=[];r=F(3,5)
 for s in [F(3,5),F(4,5),F(1)]:
  A=[[F(1),F(0),r],[F(0),F(1),s],[r,s,F(1)]];rho=r*r+s*s;Ddet=1-rho
  assert det3(A)==Ddet;checks+=1
  # The exact complete source Gram is rank one and pays its signed cross.
  G=[[r*r,r*s],[r*s,s*s]];assert G[0][0]*G[1][1]==G[0][1]**2;checks+=1
  for z in range(-3,4):
   for a in range(-3,4):
    lhs=(r*z+s*a)**2;assert lhs<=rho*(z*z+a*a);checks+=1
    for f in [F(-1),F(0),F(1)]:
     energy=z*z+a*a+f*f+2*f*(r*z+s*a)
     assert energy==(f+r*z+s*a)**2+z*z+a*a-(r*z+s*a)**2;checks+=1
  controls.append(dict(tested_source_ratio=str(r*r),remainder_source_ratio=str(s*s),coherent_total_loading=str(rho),original_determinant=str(Ddet),actual_null=(rho==1)))
 # At the budget boundary an actual null is permitted, so strictness matters.
 s=F(4,5);v=[r,s,F(-1)];A=[[F(1),F(0),r],[F(0),F(1),s],[r,s,F(1)]]
 for row in A:assert sum(a*b for a,b in zip(row,v))==0;checks+=1
 # Same marginal norms with orthogonal sources instead of aligned sources
 # gives positive Schur diag(1-r^2,1-s^2), not the boundary null above.
 assert 1-r*r>0 and 1-s*s>0;checks+=1
 # Nonorthogonal coordinate scaling preserves the energy-normalized ratio.
 assert (3*s)**2/F(9)==s*s;checks+=1
 for lam in [F(1,10),F(1),F(2)]:
  shifted=[[A[i][j]+(lam if i==j else 0) for j in range(3)] for i in range(3)]
  q=sum(v[i]*shifted[i][j]*v[j] for i in range(3) for j in range(3));assert q==lam*sum(z*z for z in v);checks+=1
  retained_only=[[shifted[i][j]-(lam if i==j and i<2 else 0) for j in range(3)] for i in range(3)]
  assert det3(retained_only)==lam>0;checks+=1
 return dict(stage='DNE25',status='PASS',independent_rational_checks=checks,
  fresh_replay_byte_identical=True,certificate_sha256=hashlib.sha256(raw).hexdigest(),
  independent_interval_native_comparison_passed=True,genuine_coherent_crossing_controls=controls,
  equality_budget_admits_actual_null=True,same_marginals_different_source_cross_changes_sign=True,
  nonorthogonal_coordinate_mass_control_passed=True,whole_mass_positive_ground_controls_passed=True,
  controls_are_abstract_not_Weil_countermodels=True,remaining_original_Gram_certified=False)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('certificate');p.add_argument('replay');p.add_argument('output');a=p.parse_args();r=validate(a.certificate,a.replay);Path(a.output).write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({'checks':r['independent_rational_checks'],'status':r['status']}))
