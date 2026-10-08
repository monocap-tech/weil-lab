"""NF71 exact residual-row and parity inference controls, not zeta evidence."""
from fractions import Fraction as F
import json
from validate_native_critical_output_reaction import mm,tr,eye,add,inv,inertia

def run():
 checks=cases=0
 def check(v):
  nonlocal checks
  assert v;checks+=1
 for p in [F(1),F(2),F(4)]:
  for q in [F(0),F(1,3)]:
   for b in [F(0),F(1,5),F(2,3)]:
    C=[[p,q],[q,F(3)]]
    c=F(1,2);check(inertia(add(C,[[c*x for x in row]for row in eye(2)],-1))==(2,0,0))
    B=[[b,F(1,3),F(1,5)],[F(1,7),b,F(1,4)]]
    A=[[F(1),F(1,8),F(1,9)],[F(1,8),F(2),F(1,11)],[F(1,9),F(1,11),F(3)]]
    U=[[F(1,9)],[F(1,13)]]
    Bweak=[[row[0]] for row in B]
    res=add(Bweak,mm(C,U),-1)
    S=add(A,mm(mm(tr(B),inv(C)),B),-1)
    a=[[x] for x in A[0]]
    native=add(a,mm(tr(B),U),-1)
    reaction=mm(mm(tr(B),inv(C)),res)
    check(add(native,reaction,-1)==[[row[0]] for row in S])
    M2=sum((x*x for row in B for x in row),F(0));r2=sum((row[0]**2 for row in res),F(0))
    bound=M2*r2/(c*c)
    check(inertia(add([[bound*x for x in row] for row in eye(3)],mm(reaction,tr(reaction)),-1))[1]==0)
    # Omitting the actual whole residual changes the completed row.
    check(native!=[[row[0]] for row in S])
    cases+=1
 # Upper odd native energy is enough for the even-plane lower conversion.
 for oddS in [F(-1,5),F(0),F(1,8)]:
  oddQ=F(1,4);evenS=F(2)
  full=evenS+oddS;check(evenS>=full-oddQ)
 # Exact parity decoupling says nothing about positivity of the odd block.
 Q=[[F(1),F(0)],[F(0),F(-1)]]
 check(Q[0][1]==0 and inertia(Q)==(1,1,0))
 return {'passed':True,'exact_checks':checks,'genuine_mixed_operator_cases':cases,
         'complete_residual_retained':True,'odd_positivity_not_inferred':True,
         'lean_certified':False,'new_zeta_bound_from_controls':False}
if __name__=='__main__':print(json.dumps(run(),indent=2))
