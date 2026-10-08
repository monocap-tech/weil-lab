"""NF69: exact protected physical-to-source charts, without source eigenvectors.
Rational finite controls audit constructions; they do not enclose actual zeta.
"""
from fractions import Fraction as F
import json
from validate_native_critical_output_reaction import tr,mm,eye,add,inv,inertia

def cols(a,ids): return [[row[j] for j in ids] for row in a]
def orthogonal_basis(vectors,n):
 out=[]
 for v in vectors:
  w=v[:]
  for b in out:
   alpha=sum(x*y for x,y in zip(w,b))/sum(x*x for x in b)
   w=[x-alpha*y for x,y in zip(w,b)]
  if any(w): out.append(w)
 return out
def rows_to_cols(vectors,n): return [[v[i] for v in vectors] for i in range(n)]
def schur(a,d):
 if not d: return a
 lo=[r[d:] for r in a[d:]]; cross=[r[d:] for r in a[:d]]
 return add([r[:d] for r in a[:d]],mm(mm(cross,inv(lo)),tr(cross)),-1)
def run():
 checks=cases=0;rank_counts={0:0,1:0,2:0}; signs={'positive':0,'negative':0,'unit':0}
 def check(v):
  nonlocal checks
  assert v; checks+=1
 P=[[F(1),F(1,5),F(1,7),F(0)],
    [F(0),F(1),F(1,8),F(1,9)],
    [F(0),F(0),F(1),F(1,6)],
    [F(0),F(0),F(0),F(1)]]
 L=mm(tr(P),P); PF=cols(P,[2,3]); LF=mm(tr(PF),PF)
 # Positive covariance solve is protected by complement Q, not whole gap.
 check(inertia(add(LF,[[F(1,4)*x for x in row] for row in eye(2)],-1))==(2,0,0))
 for mode in range(3):
  for a in [F(0),F(1,4),F(1),F(2)]:
   for b in [F(0),F(1,3),F(3,2)]:
    for v in [F(0),F(1,10)]:
     E=[[a,F(0)],[F(0),b],[a/F(3),b/F(4)]]
     if mode==0: E=[[F(0),F(0)] for _ in range(3)]
     if mode==1: E=[[a,a/F(2)],[F(0),F(0)],[a/F(3),a/F(6)]]
     NF=[[v,F(1,12)],[F(1,14),v],[F(1,16),F(1,18)]]
     N=[x+y for x,y in zip(E,NF)]
     if mode==0: N=[[F(0)]*4 for _ in range(3)]
     if mode==1: N=[N[0],[F(0)]*4,[F(0)]*4]
     Q=add(L,mm(tr(N),N),-1); QF=[row[2:] for row in Q[2:]]
     check(inertia(QF)==(2,0,0))
     solve=mm(inv(LF),mm(tr(PF),cols(P,[0,1])))
     h=eye(2)+[[-x for x in row] for row in solve]
     u=mm(P,h); y=mm(N,h)
     check(mm(tr(PF),u)==[[F(0),F(0)],[F(0),F(0)]])
     # h spans the same physical quotient and uses no Q inverse.
     check(h[:2]==eye(2))
     Ys=orthogonal_basis(tr(y),3);r=len(Ys)
     standard=eye(3)
     all_basis=orthogonal_basis(Ys+standard,3)
     Fs=all_basis[r:]
     O=rows_to_cols(all_basis,3)
     A=mm(mm(N,inv(L)),tr(N));D=add(eye(3),A,-1)
     chart=mm(mm(tr(O),D),O)
     low=[row[r:] for row in chart[r:]]
     check(inertia(low)==(3-r,0,0))
     if r:
      H=schur(chart,r);ih=inertia(H)
     else: H=[];ih=(0,0,0)
     S=schur(Q,2);is_=inertia(S)
     check(is_==(ih[0]+2-r,ih[1],ih[2]))
     check(inertia(Q)==(is_[0]+2,is_[1],is_[2]))
     check(inertia(D)==(ih[0]+3-r,ih[1],ih[2]))
     # A whole projected positive-covariance residual bounds all solve columns.
     U=[[F(1,9),F(1,11)],[F(1,13),F(1,15)]]
     rhs=mm(tr(PF),cols(P,[0,1]));res=add(rhs,mm(LF,U),-1)
     err=add(solve,U,-1)
     error_gram=mm(tr(err),err)
     bound=[[F(16)*x for x in row] for row in mm(tr(res),res)]
     check(inertia(add(bound,error_gram,-1))[1]==0)
     rank_counts[r]+=1;cases+=1
     signs['negative' if ih[1] else 'unit' if ih[2] else 'positive']+=1
 # Exact positive/contact/crossing family with a protected complement.
 for level in [F(4,5),F(1),F(6,5)]:
  P=eye(3);N=[[level,F(0),F(0)]]
  Q=add(eye(3),mm(tr(N),N),-1)
  check(Q[1][1]==1 and Q[2][2]==1)
  check(inertia(Q)[1]==(level>1))
  check(inertia(Q)[2]==(level==1))
 # Non-spectral output charts must retain the old mixed block.
 D=[[F(1,4),F(1,2)],[F(1,2),F(1,2)]]
 check(inertia(add(eye(2),D,-1))==(2,0,0))
 check(D[0][0]>0 and D[1][1]>0 and schur(D,1)[0][0]<0)
 # A physical positive eigenlevel has a different extended negative ambient.
 N=[[F(4,5),F(1,2)]];Q=add(eye(2),mm(tr(N),N),-1);h=tr(N);mu=F(11,100)
 check(mm(Q,h)==[[mu*x[0]] for x in h])
 check(mm(add(Q,[[mu*x for x in row] for row in eye(2)],-1),h)==[[F(0)],[F(0)]])
 check(signs['positive']>0 and signs['negative']>0)
 return {'passed':True,'exact_checks':checks,'coupled_cases':cases,'output_ranks':rank_counts,
 'sign_cases':signs,'source_eigenvectors_required':False,
 'positive_covariance_solve_uses_whole_Q_gap':False,
 'whole_source_and_physical_schur_inertia_agree':True,
 'actual_zeta_source_coordinates_enclosed':False,'new_aperture':False,
 'arithmetic_nondivergence':False,'lean_certified':False}
if __name__=='__main__': print(json.dumps(run(),indent=2))
