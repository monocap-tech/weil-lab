#!/usr/bin/env python3
"""Pure Fraction deterministic small-system independent proof regression for NF380.

No assertion about original Weil operator or new native signed coupling.
Checks general algebra that using archived WJJ, WJF and WFF with new WJv/WFv
recovers the full exact signed bilinear on an exterior corrected trial.
"""
import json,argparse
from pathlib import Path
from fractions import Fraction as F

def dot(x,y):return sum((a*b for a,b in zip(x,y)),F(0))
def mv(A,x):return [dot(r,x) for r in A]
def matmul(A,B):return [mv([list(row) for row in zip(*B)],row) for row in A]
def tr(A):return [list(r) for r in zip(*A)]
def add(x,y):return [a+b for a,b in zip(x,y)]
def sub(x,y):return [a-b for a,b in zip(x,y)]
def scale(x,c):return [c*t for t in x]
def blip(M,x,y):return dot(x,mv(M,y))

def run(output=None):
 checked=0
 for shift in (0,1,2,3):
  # A, U symmetric; L full. No positivity of the signed form is assumed.
  A=[[F(3+shift),F(-2,3)],[F(-2,3),F(-5-shift)]]
  U=[[F(2),F(1,5)],[F(1,5),F(-7,4)]]
  L=[[F(1,2+shift),F(5,3)],[F(-7,6),F(3,5+shift)]]
  w=[F(1,8+shift),F(-9,7)];h=[F(-3,10),F(11,9+shift)]
  X=[[F(1,4),F(-1,3)],[F(2,5),F(1,7)]]
  Y0=[[F(1,11),F(1,12)],[F(-1,13),F(1,17)]]
  t=[F(4,9),F(-3,8)]
  eta=[F(7,18),F(-1,6)]
  xv=[F(4,5),F(-2,7)]
  coeff=add(t,mv(Y0,t))
  a=mv(X,coeff)
  f=scale(mv(Y0,t),-1)
  beta=sub(xv,mv(X,eta))
  # W(u,qperp) with qperp=v-Feta-Jbeta.
  joined=a+f
  Wold=[A[i]+L[i] for i in range(2)]+[tr(L)[i]+U[i] for i in range(2)]
  oldpair=blip(Wold,joined,scale(beta,-1)+scale(eta,-1))
  direct=oldpair+dot(a,w)+dot(f,h)
  fast=(dot(a,w)+dot(f,h)-dot(a,mv(L,eta))-dot(f,mv(U,eta))
        -blip(A,a,beta)-dot(f,mv(tr(L),beta)))
  assert direct==fast,('block identity',shift,direct,fast)
  # Independent alternative rearrangement: evaluate original u4 against v,
  # each F_j and each J_i separately, then correct.
  old_by_j=add(mv(A,a),mv(L,f))
  old_by_f=add(mv(tr(L),a),mv(U,f))
  second=dot(a,w)+dot(f,h)-dot(old_by_j,beta)-dot(old_by_f,eta)
  assert second==direct,('response identity',shift)
  checked+=2
 report=dict(status='PURE_FRACTION_ARCHIVED_SIGNED_BLOCK_REUSE_IDENTITY_PASS',
   exact_independent_block_identity_checks=checked,
   finite_source_algebra_model_count=4,
   original_WJJ_and_WJF_recomputed=False,
   true_original_Weil_signed_new_pairing_computed=False,
   true_original_physical_J242_Gram_recomputed=False,
   original_operator_domains_reviewed=False,W_ODD_NEG='OPEN',RH='OPEN')
 if output:Path(output).write_text(json.dumps(report,sort_keys=True,indent=2)+'\n')
 print('PASS pure Fraction archived signed-reuse identity 8/8 (toy source matrices, not original Weil)')
 return report
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);run(p.parse_args().output)
