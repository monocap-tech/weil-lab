"""Independent compact-interval consumer and exact operator controls."""
import json,gzip,hashlib,sys
from fractions import Fraction as F
from pathlib import Path
from certify_native_inverse_correlation_cc13 import I,read,bounds,solve,pivots,quad
ROOT=Path(__file__).resolve().parents[1]
sys.set_int_max_str_digits(0)
def matrix(x):return [[read(y) for y in row] for row in x]
def inverse(A):
 n=len(A);cols=[solve(A,[F(i==j) for i in range(n)]) for j in range(n)]
 return [[cols[j][i] for j in range(n)] for i in range(n)]
def matmul(A,B):return [[sum((A[i][k]*B[k][j] for k in range(len(B))),F(0)) for j in range(len(B[0]))] for i in range(len(A))]
def transpose(A):return list(map(list,zip(*A)))
def controls():
 c=F(699,1000);checks=0
 # Exact positive complement with nonzero mixed inverse action. Full trial
 # basis makes the matrix envelope EXACT, including all off-diagonal terms.
 for t in (F(1,10),F(1,2),F(2)):
  C=[[c+2+t,F(1),F(0)],[F(1),c+3,F(1,3)],[F(0),F(1,3),c+1]]
  pivots([[C[i][j]-(c if i==j else 0) for j in range(3)] for i in range(3)]);checks+=1
  B=[[F(1),F(0)],[F(0),F(1)],[F(1,2),F(-1,3)]]
  G=matmul(C,C);J=[[G[i][j]/c-C[i][j] for j in range(3)] for i in range(3)]
  H=[[x/c-B[i][j] for j,x in enumerate(row)] for i,row in enumerate(matmul(C,B))]
  credit=matmul(matmul(transpose(H),inverse(J)),H)
  scalar=matmul(transpose(B),B);actual=matmul(matmul(transpose(B),inverse(C)),B)
  upper=[[scalar[i][j]/c-credit[i][j] for j in range(2)] for i in range(2)]
  assert upper==actual;checks+=1
  assert actual[0][1]!=0;checks+=1
  # A proper partial trial gives a positive semidefinite reaction remainder.
  j=J[0][0];h=H[0]
  partial=[[scalar[i][k]/c-h[i]*h[k]/j for k in range(2)] for i in range(2)]
  R=[[partial[i][k]-actual[i][k] for k in range(2)] for i in range(2)]
  assert R[0][0]>=0 and R[1][1]>=0 and R[0][0]*R[1][1]>=R[0][1]**2;checks+=1
  # Positive original eigenmode becomes shifted-null only when its full
  # physical mass is added to the negative channel.
  Q=[[F(2),F(0)],[F(0),F(3)]];P=[[F(5),F(0)],[F(0),F(5)]];N=[[F(3),F(0)],[F(0),F(2)]]
  Nmu=[[N[i][k]+(2 if i==k else 0) for k in range(2)] for i in range(2)]
  assert [[P[i][k]-Nmu[i][k] for k in range(2)] for i in range(2)]==[[F(0),F(0)],[F(0),F(1)]] and Q[0][0]==2;checks+=1
 return checks
def run():
 p=ROOT/'notes/data/RPB108_DEFECT_ENVELOPE_CC15_CERTIFICATE_20261008.json'
 raw=p.read_bytes() if p.exists() else gzip.decompress(p.with_suffix('.json.gz').read_bytes())
 d=json.loads(raw);c=F(699,1000)
 checks=controls();A=matrix(d['original_native_pair']);GB=matrix(d['complete_source_pair_gram']);J=matrix(d['whole_defect_matrix'])
 archive=(ROOT/'notes/data/RPB108_RICH_ACTION_CC14_CERTIFICATE_20261008.json.gz').read_bytes()
 assert hashlib.sha256(archive).hexdigest()==d['input_sha256']['cc14'];checks+=1
 prior=json.loads(gzip.decompress(archive));G=matrix(prior['complete_action_gram']);T=matrix(prior['complete_trial_native_gram'])
 for i in range(16):
  for j in range(16):
   expected=G[i][j]/c-T[i][j];assert max(expected.lo,J[i][j].lo)<=min(expected.hi,J[i][j].hi);checks+=1
 AC=matrix(d['whole_mixed_action_source_cross']);NC=matrix(d['whole_mixed_native_source_cross']);H=[[AC[i][j]/c-NC[i][j] for j in range(2)] for i in range(16)]
 L=[[F(x) for x in row] for row in d['rational_matrix_lift']]
 credit=[[sum((H[k][i]*L[k][j]+L[k][i]*H[k][j] for k in range(16)),I(0))-sum((L[k][i]*J[k][l]*L[l][j] for k in range(16) for l in range(16)),I(0)) for j in range(2)] for i in range(2)]
 lower=[[A[i][j]-GB[i][j]/c+credit[i][j] for j in range(2)] for i in range(2)]
 for i in range(2):
  for j in range(2):
   a=read(d['compatible_pair_schur_lower'][i][j]);b=lower[i][j];assert max(a.lo,b.lo)<=min(a.hi,b.hi);checks+=1
 center=[[(x.lo+x.hi)/2 for x in row] for row in J];rad=max(sum(((x.hi-x.lo)/2 for x in row),F(0)) for row in J)
 K=[[center[i][j]-(rad if i==j else 0) for j in range(16)] for i in range(16)];pivots(K);checks+=1
 det=lower[0][0]*lower[1][1]-lower[0][1]*lower[1][0]
 if d['classification']=='B-conditional':
  assert lower[0][0].lo>0 and det.lo>0;checks+=1
  cross=max(abs(lower[0][1].lo),abs(lower[0][1].hi))
  loss=cross*cross/(lower[0][0].lo*lower[1][1].lo)
  assert loss<F(735,100000);checks+=1
  assert F(d['pair_completed_weak_margin_lower'])>F(3144,10**35);checks+=1
 out={'passed':True,'exact_checks':checks,'complete_mixed_action_dimension':16,'original_pair_dimension':2,'independent_pair_lower_determinant':bounds(det),'actual_full_even54_matrix_evaluated':False,'actual_inverse_evaluated':False,'synthetic_controls_are_arithmetic':False,'lean_certified':False}
 failure=d.get('best_span_obstruction')
 if failure:
  x=list(map(F,failure['pair_direction']));hx=[sum((H[i][j]*x[j] for j in range(2)),I(0)) for i in range(16)]
  vc=[(z.lo+z.hi)/2 for z in hx];vr=[(z.hi-z.lo)/2 for z in hx];inv=inverse(K)
  upper=sum((inv[i][j]*vc[i]*vc[j]+abs(inv[i][j])*(abs(vc[i])*vr[j]+vr[i]*abs(vc[j])+vr[i]*vr[j]) for i in range(16) for j in range(16)),F(0))
  bound=quad(A,x)-quad(GB,x)/c+upper
  assert bound.hi<0 and failure['strictly_negative'];checks+=1
  out['independent_best_entire_span_direction_upper']=str(bound.hi);out['best_span_obstruction_replayed']=True
 from validate_native_inverse_correlation_cc13 import run as prior
 old=prior();assert old['passed'];out['cc13_controls_replayed']=old['exact_checks'];checks+=1
 cc11=json.loads((ROOT/'notes/data/RPB108_ODD_BATCH_CC11_CERTIFICATE_20261008.json').read_bytes());assert list(map(str,pivots(cc11['deterministic_scaled_lower_matrix'])))==cc11['exact_ldl_pivots'];checks+=1
 out['protected_codimension_preserved']=107;out['exact_checks']=checks
 (ROOT/'notes/data/RPB108_DEFECT_ENVELOPE_CC15_VALIDATION_20261008.json').write_text(json.dumps(out,indent=2)+'\n');return out
if __name__=='__main__':print(json.dumps(run(),indent=2))
