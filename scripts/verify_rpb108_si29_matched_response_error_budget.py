#!/usr/bin/env python3
"""Original matched 470+14 Schur sensitivity and component allocation contract."""
import argparse,hashlib,json
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
SPECS={'frame':'87d6f3ae24cde489adaf9ab3ac7efa612bc82bd78c6c9e94866802fdc550052f',
 'schur':'f1149e27da8a0e1d90e48b8ee0eb8a0a0b8ef51d0910499a7fcd19a082efca07',
 'negative':'a693261c31f01a4a1e11ea6400e5173435a8260b41b1f6b43aa6f67f784ccb7f'}

def sigma(e,g,h,ell):
 gamma=g/ell;assert 0<=gamma<1 and e>=0 and h>=0
 # ||G^-1/2||<174, ||G^-1/2 M||<20/3 and its square <=44.
 return h+(2320*e+30276*e*e+44*gamma)/(1-gamma)

def mm(A,B):return [[sum((a*b for a,b in zip(row,col)),F(0)) for col in zip(*B)] for row in A]
def tr(A):return [list(r) for r in zip(*A)]
def add(A,B,sign=1):return [[a+sign*b for a,b in zip(x,y)] for x,y in zip(A,B)]
def inv(A):
 n=len(A);X=[list(row)+[F(int(i==j)) for j in range(n)] for i,row in enumerate(A)]
 for i in range(n):
  j=next(j for j in range(i,n) if X[j][i]);X[i],X[j]=X[j],X[i]
  p=X[i][i];X[i]=[x/p for x in X[i]]
  for j in range(n):
   if j!=i:
    p=X[j][i];X[j]=[a-p*b for a,b in zip(X[j],X[i])]
 return [r[n:] for r in X]

def regression():
 # Non-diagonal G and M, ALL two-source forcing columns retained.
 G=[[F(2),F(1,2)],[F(1,2),F(3)]]
 M=[[F(1,5),F(1,7)],[F(1,9),F(1,4)]]
 H=[[F(3),F(1,3)],[F(1,3),F(4)]];Gi=inv(G)
 def response(M):
  T=add(H,mm(tr(M),mm(Gi,M)),-1);forcing=[[-v for v in row] for row in mm(tr(M),Gi)]
  R=mm(tr(forcing),mm(inv(T),forcing))
  A=[G[i]+M[i] for i in range(2)]+[tr(M)[i]+H[i] for i in range(2)]
  top=[r[:2] for r in inv(A)[:2]]
  assert add(top,Gi,-1)==R
  return T,forcing,R
 T,h,R=response(M)
 Mp=add(M,[[F(1,100),F(0)],[F(-1,200),F(1,150)]])
 Tp,hp,Rp=response(Mp)
 wrong=mm(tr(h),mm(inv(Tp),h))
 assert h!=hp and Rp!=wrong and Rp!=R
 # If M starts at zero, holding forcing at zero would miss ALL new gain.
 Z=[[F(0),F(0)],[F(0),F(0)]];_,hz,Rz=response(Z)
 assert Rz==Z and response(M)[2]!=Z
 return {'coupled_block_inverse_gain_identity_checked':True,
         'forcing_changes_with_mixed_block_checked':True,
         'fixed_forcing_substitution_rejected':True}

def compute(frame,schur,negative):
 assert frame['physical_Gram_lower']=='99/100' and frame['physical_Gram_upper']=='101/100'
 ell=F(frame['conditional_Astar_trial_energy_lower']);t=F(schur['normalized_actual_Astar_energy_Schur_clean_lower'])
 assert ell==F(3328479,10**11) and t==F(9,9091)
 assert F(frame['rational_Astar_trial_energy_upper'])==44 and F(schur['normalized_actual_Astar_energy_Schur_upper'])==44
 assert schur['accepted_full_trial_input_sha256']==SPECS['frame']
 assert negative['frame_input_sha256']==SPECS['frame'] and negative['schur_input_sha256']==SPECS['schur']
 assert 174**2*ell>1 and F(20,3)**2>44 and F(174*101,100)<176
 eps=F(1,250000000);s=sigma(eps,F(0),F(0),ell)
 rho=s/t;assert rho<F(1,101) and rho/(1-rho)<F(1,100)
 rows=[]
 for name,e in [('illustrative_1_percent_inverse_contract',eps),('half_floor_contract',F(1,5000000)),('negative_component_if_centered_at_zero',F(negative['normalized_negative_mixed_operator_upper']))]:
  ss=sigma(e,F(0),F(0),ell)
  rows.append(dict(case=name,normalized_total_mixed_error=str(e),Schur_error_upper=str(ss),
    this_sufficient_bound_preserves_positive_Schur=ss<t,
    this_sufficient_bound_preserves_half_floor=ss<=t/2,
    this_sufficient_bound_pays_one_percent_inverse=(ss<t and ss/(t-ss)<=F(1,100))))
 assert rows[-1]['this_sufficient_bound_preserves_positive_Schur'] is False
 # Recompose the inherited #339 small-shift formula from the SAME frame.
 E=F(frame['full_trial_endpoint_vector_squared_upper']);D=F(frame['full_trial_derivative_Gram_trace_upper']);r=isqrt((E*D).numerator//(E*D).denominator)+1
 delta=F(1,2**36);q=F(1,2**18)
 small=E*(delta+delta*delta)/2+r*(F(4,9)*delta*q+F(8,15)*delta*delta*q)+D*(delta*delta/4+delta**3/3)
 assert small>eps and small<F(1,2500000)
 # Forced change when source synthesis is U, f=U*U, g_rhs=W*U=0.
 dh=176*174*eps
 return dict(status='CONDITIONAL_ORIGINAL_MATCHED_SCHUR_ERROR_ALLOCATION_CONTRACT',
   input_sha256=SPECS,source_coordinates='U=JD',quotient_coordinates='W=(I-P_J470)FC',
   full_trial_lower=str(ell),full_trial_upper='44',actual_14_Schur_lower=str(t),
   inverse_anchor_sqrt_upper='174',whitened_mixed_norm_upper='20/3',
   exact_anchor_and_diagonal_example_total_mixed_error=str(eps),
   example_Schur_error_upper=str(s),example_inverse_relative_error_upper=str(s/(t-s)),
   example_matched_forcing_error_upper_for_source_U=str(dh),
   illustrative_error_allocations=rows,
   inherited_small_shift_cutoff=str(delta),recomputed_inherited_small_shift_error=str(small),
   small_shift_bound_exceeds_illustrative_total_error=True,
   complete_M_error_formula='epsilon <= epsilon_arch + epsilon_prime_after_D + epsilon_negative + epsilon_arithmetic; same coordinates',
   Schur_error_formula='sigma = delta_H + (2320*epsilon + 30276*epsilon^2 + 44*gamma)/(1-gamma); gamma=delta_G/ell<1',
   matched_forcing_error_formula='d_h <= chi*(174*epsilon + (20/3)*gamma)/(1-gamma); chi=||G^-1/2 f||; exact right hand side',
   response_error_formula='if sigma<t: ||Rtilde-R|| <= sigma*||h||^2/(t*(t-sigma)) + (2*||h||*d_h+d_h^2)/(t-sigma)',
   regressions=regression(),
   numerical_examples_are_final_positivity_tolerances=False,
   final_signed_gate_margin_available=False,final_arch_tolerance_selected=False,
   negative_mixed_entries_computed=False,anchor_energy_G_computed=False,quotient_energy_H_computed=False,
   actual_arch_mixed_matrix_computed=False,matched_forcing_computed=False,inverse_response_value_certified=False,
   large_arch_run_justified_by_this_result=False,
   W_ODD_NEG='OPEN',inherited_original_domain_review='OPEN')

def main():
 p=argparse.ArgumentParser()
 for key in SPECS:p.add_argument('--'+key+'-certificate',required=True)
 p.add_argument('--output',default='artifacts/si29_matched_response_error_budget.json');args=p.parse_args();z={}
 for key,sha in SPECS.items():
  raw=Path(getattr(args,key+'_certificate')).read_bytes();assert hashlib.sha256(raw).hexdigest()==sha;z[key]=json.loads(raw)
 result=compute(**z);out=Path(args.output);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+'\n')
 print('MATCHED SCHUR ERROR CONTRACT PASS; forcing covariance retained; zero-centered negative budget exceeds illustrative stability allocation; final margin OPEN')
if __name__=='__main__':main()
