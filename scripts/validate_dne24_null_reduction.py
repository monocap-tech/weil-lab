#!/usr/bin/env python3
"""Independent determinant/Cramer basis checks and exact spectral controls."""
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path
import argparse,json,hashlib
import certify_dne24_null_reduction as c
def det(a):
 n=len(a);total=F(0)
 for p in permutations(range(n)):
  sign=(-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n));v=F(sign)
  for i in range(n):v*=a[i][p[i]]
  total+=v
 return total
def validate(paths,certpath,replaypath):
 raw=Path(certpath).read_bytes();replay=Path(replaypath).read_bytes();cert=json.loads(raw);assert raw==replay;checks=1
 data=[c.read(p) for p in paths];assert [h for _,h in data]==c.HASHES;checks+=1
 targets,response,trial,nf31,prior=[v for v,_ in data]
 for idx,row in enumerate(cert['rows']):
  x=list(map(F,targets['authenticated_compensated_targets'][idx]['retained_coefficients']));w=list(map(F,response['parity_certificates'][idx]['exact_rational_retained_response']));u=list(map(F,trial['parities'][idx]['fixed_rational_probe_coefficients']));Z=[[F(1)]+[F(0)]*55,x,w,u]
  piv=row['constraint_pivots'];A=[[z[j] for j in piv] for z in Z];d=det(A);assert d==F(row['pivot_matrix_determinant'])!=0;checks+=1
  inverse=[[F((-1)**(i+j))*det([[A[q][p] for p in range(4) if p!=i] for q in range(4) if q!=j])/d for j in range(4)] for i in range(4)]
  for i in range(4):
   for j in range(4):assert inverse[i][j]==F(row['pivot_matrix_inverse'][i][j]);checks+=1
  free=row['free_coordinates'];assert free==[j for j in range(56) if j not in piv] and len(free)==52;checks+=1
  for j in free:
   b=[z[j] for z in Z];cramer=[]
   for i in range(4):
    replaced=[[b[q] if p==i else A[q][p] for p in range(4)] for q in range(4)];cramer.append(det(replaced)/d)
   v=[F(k==j) for k in range(56)]
   for i,p in enumerate(piv):v[p]=-cramer[i]
   for z in Z:assert sum(a*b for a,b in zip(z,v))==0;checks+=1
   for i in range(4):assert cramer[i]==sum(a*b for a,b in zip(inverse[i],b));checks+=1
   assert v[j]==1;checks+=1
  assert F(row['inherited_raw_complement_physical_native_gap_lower'])==F(nf31['parity_certificates'][idx]['physical_remaining_native_gap_lower'])>0;checks+=1
  assert row['actual_null_dimension_upper']==row['negative_index_upper']==52;checks+=1
 controls=[]
 # A positive eliminated block, native positive remainder, exact full response.
 for b in [F(1),F(2),F(3)]:
  H=F(2);J=F(2);reaction=J*J/H;D=b-reaction;K=reaction/b
  assert (D>0)==(K<1) and (D==0)==(K==1) and (D<0)==(K>1);checks+=1
  assert det([[H,J],[J,b]])==H*D;checks+=1
  # Full original quadratic equals the completed square for each test.
  for z in range(-3,4):
   for y in range(-3,4):
    assert H*z*z+2*J*z*y+b*y*y==H*(F(z)+J*y/H)**2+D*y*y;checks+=1
  # Rescale the remainder coordinate: physical mass is 9, not 1.
  scaledB=9*b;scaledJ=3*J;assert scaledJ*scaledJ/(H*scaledB)==K;checks+=1
  controls.append(dict(native_remainder=str(b),reduced_sign=str(D),normalized_response=str(K),whole_original_null=(D==0)))
 # Positive ground-level control: [[3,2],[2,3]] has ground level 1.
 H=F(3);J=F(2);B=F(3);lam=F(1);shifted=(B-lam)-J*J/(H-lam)
 assert shifted==0 and H-lam>0;checks+=1
 assert H+2*J*(-1)+B==2 and (H-lam)+2*J*(-1)+(B-lam)==0;checks+=1
 retained_only_shift=(B-lam)-J*J/H;assert retained_only_shift==F(2,3);checks+=1
 # Norm >= 1 is not an exact-null test: response diag(2,1/2) has no unit eigenvalue.
 response=[F(2),F(1,2)];assert max(response)>1 and all(v!=1 for v in response);checks+=1
 return dict(stage='DNE24',status='PASS',independent_rational_checks=checks,
  certificate_sha256=hashlib.sha256(raw).hexdigest(),fresh_replay_byte_identical=True,
  independent_cofactor_inverse_and_Cramer_complement_checked=True,
  genuine_crossing_controls=controls,nonorthogonal_coordinate_mass_control_passed=True,
  positive_ground_level_whole_mass_shift_passed=True,retained_only_shift_misses_positive_level_null=True,
  large_true_response_without_unit_eigenvalue_control_passed=True,
  actual_Weil_response_evaluated=False,whole_aperture_positive=False)
if __name__=='__main__':
 p=argparse.ArgumentParser()
 for k in ['targets','response','trial','nf31','dne23','certificate','replay','output']:p.add_argument(k)
 a=p.parse_args();r=validate([getattr(a,k) for k in ['targets','response','trial','nf31','dne23']],a.certificate,a.replay)
 Path(a.output).write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({'status':r['status'],'checks':r['independent_rational_checks']}))
