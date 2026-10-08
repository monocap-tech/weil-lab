"""Independent exact inverse/covariance controls for CC13; not zeta evidence."""
from fractions import Fraction as F
from pathlib import Path
import json,sys
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[1]
def inv2(A):
 a,b=A[0];c,d=A[1];det=a*d-b*c;assert det>0
 return [[d/det,-b/det],[-c/det,a/det]]
def quad(A,x,y=None):
 y=x if y is None else y
 return sum((x[i]*A[i][j]*y[j] for i in range(len(x)) for j in range(len(y))),F(0))
def psd2(A):return A[0][0]>=0 and A[1][1]>=0 and A[0][0]*A[1][1]>=A[0][1]*A[1][0]
def run():
 c=F(699,1000);beta=1/c;checks=0;cases=0
 def ck(v):
  nonlocal checks
  assert v;checks+=1
 vectors=[[F(a),F(b)] for a in (-2,-1,0,1,2) for b in (-2,-1,0,1,2) if a or b]
 for theta in (F(0),F(1,3),F(3,5),F(9,10),F(99,100)):
  C=[[c/(1-theta),theta*c/(1-theta)],[theta*c/(1-theta),c/(1-theta)]]
  H=inv2(C);ck(psd2([[C[i][j]-(c if i==j else 0) for j in range(2)] for i in range(2)]))
  ck(psd2(H));ck(psd2([[(beta if i==j else 0)-H[i][j] for j in range(2)] for i in range(2)]))
  for x in vectors:
   for y in vectors:
    xy=sum((a*b for a,b in zip(x,y)),F(0));xn=sum((a*a for a in x),F(0));yn=sum((b*b for b in y),F(0))
    ck((quad(H,x,y)-beta*xy/2)**2<=beta*beta*xn*yn/4);cases+=1
 d=json.loads((ROOT/'notes/data/RPB108_INVERSE_CORRELATION_CC13_CERTIFICATE_20261008.json').read_text())
 ctrl=d['summary_countercontrol'];A=[[F(x) for x in row] for row in ctrl['native_residual_chart']]
 s,b=F(ctrl['residual_scale']),F(ctrl['test_source_scale']);B=[[s,F(0)],[F(0),b]]
 dets=[]
 for tag in ('C_good','C_bad'):
  C=[[F(x) for x in row] for row in ctrl[tag]];H=inv2(C)
  S=[[A[i][j]-B[i][i]*H[i][j]*B[j][j] for j in range(2)] for i in range(2)]
  ck(S[0][0]==F(d['even_weak_margin']));ck(S[1][1]==F(ctrl['remaining_lower_form_in_both'])>0)
  det=S[0][0]*S[1][1]-S[0][1]*S[1][0];dets.append(det)
 ck(dets[0]==F(ctrl['positive_completed_determinant'])>0)
 ck(dets[1]==F(ctrl['negative_completed_determinant'])<0)
 # Off-diagonal inverse reaction survives a COMPLETE zero ordinary source
 # correlation. A diagonal-only treatment would give the same sign twice.
 ck(quad(inv2([[F(x) for x in row] for row in ctrl['C_bad']]),[s,F(0)],[F(0),b])==F(ctrl['inverse_correlation_bad'])!=0)
 # Whole 54-dimensional remaining even chart: the two controls append 53
 # untouched positive directions. This cannot be repaired by their signs.
 ck(d['exact_even_quotient_dimension']==54 and d['protected_codimension']==107)
 # Full positive/negative covariance and genuine positive-eigenmode shift.
 # These are declared synthetic source controls, not zeta source replacements.
 Q=[[F(2),F(0)],[F(0),F(3)]];P=[[F(5),F(0)],[F(0),F(5)]];N=[[F(3),F(0)],[F(0),F(2)]]
 ck([[P[i][j]-N[i][j] for j in range(2)] for i in range(2)]==Q)
 mu=F(2);Nmu=[[N[i][j]+(mu if i==j else 0) for j in range(2)] for i in range(2)]
 shifted=[[P[i][j]-Nmu[i][j] for j in range(2)] for i in range(2)]
 ck(shifted==[[F(0),F(0)],[F(0),F(1)]])
 ck(Q[0][0]>0 and shifted[0][0]==0 and Nmu[0][0]-N[0][0]==mu)
 return {'passed':True,'exact_checks':checks,'sharp_interval_vector_cases':cases,
 'coupled_inverse_controls':5,'entire_even_quotient_embedding':54,
 'same_ordinary_gram_different_completed_sign':True,
 'compatible_positive_remainder_in_both_controls':True,
 'positive_eigenmode_full_mass_source_shift':True,
 'synthetic_controls_are_original_arithmetic':False,'lean_certified':False}
if __name__=='__main__':
 out=run();(ROOT/'notes/data/RPB108_INVERSE_CORRELATION_CC13_VALIDATION_20261008.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
