"""RC219: exact all-coefficient obstruction for the nominal residual chord.

The nominal carriers are not asserted to equal the actual canonical actions.
This is a limitation of the RC218 two-sided residual-chord mechanism in its
unchanged ten-vector span, not a lower bound for the true inverse uncertainty.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse, json
import validate_rpb108_rc218_coupled_expanded_inverse as prev
ROOT=Path(__file__).resolve().parents[1]
PINS=dict(prev.PINS)
PINS.update({
 'certificates/rpb108_rc218_coupled_expanded_inverse.json':'e04d82e18dd81acfca3ecea79270eb562906e1e4',
 'certificates/rpb108_rc218_materialized_prefix_interface.json':'b627378083c4c958fbda320eed56602e1e2ccd25'})
HELPER_PINS=dict(prev.HELPER_PINS)
HELPER_PINS['scripts/validate_rpb108_rc218_coupled_expanded_inverse.py']='b8d3ac315b5b561b5c919f2fb4aff73343b0f834'
def bil(v,A,w):
 return sum(v[i]*A[i][j]*w[j] for i in range(len(v)) for j in range(len(w)))
def lin_interval(v,L,H,w):
 lo=hi=F(0)
 for i in range(len(v)):
  for j in range(len(w)):
   t=v[i]*w[j]
   lo+=t*(L[i][j] if t>=0 else H[i][j])
   hi+=t*(H[i][j] if t>=0 else L[i][j])
 return lo,hi
def run(reverse=False,proposal=None):
 for p,sha in sorted(HELPER_PINS.items(),reverse=reverse):
  assert prev.prev.blob((ROOT/p).read_bytes())==sha,(p,'helper pin')
 data={}
 for p,sha in sorted(PINS.items(),reverse=reverse):
  raw=(ROOT/p).read_bytes();assert prev.prev.blob(raw)==sha,(p,'input pin')
  data[p]=json.loads(raw)
 c=data['certificates/rpb108_rc218_coupled_expanded_inverse.json']
 d=data['certificates/rpb108_rc218_materialized_prefix_interface.json']
 mat=lambda key:prev.mat(d,key)
 gl,gh=mat('source_Gram_entry_lower'),mat('source_Gram_entry_upper')
 bl,bh=mat('nominal_source_action_entry_lower'),mat('nominal_source_action_entry_upper')
 al,ah=mat('nominal_action_Gram_entry_lower'),mat('nominal_action_Gram_entry_upper')
 GH=prev.mat(c,'source_D_Gram_upper');keep=[0,1,2,3,4,6,8,9]
 a=F(32125,230953);chord=1/a-F(1,2)
 mid=lambda L,H:prev.scale(F(1,2),prev.add(L,H))
 AA=mid(al,ah);BB=mid(bl,bh);GG=mid(gl,gh)
 S=[[F(i==keep[j]) for j in range(8)] for i in range(10)]
 if proposal is None:
  # Floating eigenvectors propose only a rational direction. Every asserted
  # inequality below is checked with exact fractions and rational PSD tests.
  import numpy as np
  from scipy.linalg import eigh
  ar=lambda A:np.array([[float(x) for x in row] for row in A])
  N=prev.add(prev.cong(S,GG),prev.mm(prev.trans(S),prev.mm(BB,prev.mm(prev.inv(AA),prev.mm(prev.trans(BB),S)))),-1)
  _,vs=eigh(ar(N),ar(GH));v=vs[:,-1];v=v/max(abs(v))
  proposal=[str(F(round(float(x)*10**9),10**9)) for x in v]
 w=list(map(F,proposal));assert len(w)==8 and any(w)
 sw=[sum(S[i][j]*w[j] for j in range(8)) for i in range(10)]
 q=bil(w,GH,w);assert q>0
 # A single 11x11 block controls every possible trial coefficient x:
 # [1,x]^* K [1,x] = ||f_w - nominal_M(trial_x)||^2 on the prefix.
 lo=[[F(0)]*11 for _ in range(11)];hi=[[F(0)]*11 for _ in range(11)]
 lo[0][0],hi[0][0]=lin_interval(sw,gl,gh,sw)
 for k in range(10):
  e=[F(j==k) for j in range(10)]
  l,h=lin_interval(sw,bl,bh,e)
  lo[0][k+1]=lo[k+1][0]=-h;hi[0][k+1]=hi[k+1][0]=-l
  for j in range(10):lo[k+1][j+1]=al[k][j];hi[k+1][j+1]=ah[k][j]
 weights=[prev.sqrtup(hi[i][i]) for i in range(11)]
 assert min(weights)>0
 K,_,rounding=prev.loewner(lo,hi,weights)
 assert prev.psd(K)
 def test(beta):
  P=[r[:] for r in K];P[0][0]-=beta*q/chord
  return prev.psd(P)
 # Deliberately report a coarse, strictly certified floor, without claiming
 # that a numerical eigenvalue or a failed PSD test proves an upper bound.
 beta=F(65,100);assert test(beta)
 P=[r[:] for r in K];P[0][0]-=beta*q/chord;assert prev.psd(P)
 # Materialize one proposed residual direction for subsequent enrichment.
 y=prev.mm(prev.inv(AA),[[sum(BB[i][k]*sw[i] for i in range(10))] for k in range(10)])
 y=[prev.down(row[0],10**24) for row in y]
 z=[F(1)]+y
 # Entrywise interval quadratic evaluation needs sign-aware arithmetic.
 nominal_prefix_residual_interval=list(lin_interval(z,lo,hi,z))
 assert nominal_prefix_residual_interval[0]>=beta*q/chord
 eps=list(map(F,d['complete_column_error_norm_upper']))
 actual_error_radius=sum(abs(y[k])*eps[k] for k in range(10))
 return dict(milestone='RC219',starting_commit='0dd0af802ac0f7a0c60d102f61d5f3243e32dac7',
  input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,
  response_source_order=c['conditioned_response_source_order'],raw_trial_order=d['raw_trial_order'],
  finite_prefix_degree=d['finite_prefix_degree'],spectral_metric_lower=str(a),residual_chord_coefficient=str(chord),
  rational_witness=proposal,witness_source_D_energy_upper=str(q),
  joint_prefix_residual_block_entry_lower=prev.ser(lo),joint_prefix_residual_block_entry_upper=prev.ser(hi),
  joint_prefix_residual_block_Loewner_lower=prev.ser(K),joint_block_rounding_diagonal=list(map(str,rounding)),
  all_trial_coefficients_PSD_witness=prev.ser(P),
  all_trial_coefficients_nominal_prefix_residual_energy_lower=str(beta*q/chord),
  all_trial_coefficients_nominal_residual_chord_relative_width_lower=str(beta),
  half_Gram_threshold='1/2',nominal_ten_trial_two_sided_residual_chord_obstruction_proved=beta>F(1,2),
  proposed_residual_trial_coefficients=list(map(str,y)),proposed_residual_source_coefficients=list(map(str,w)),
  proposed_residual_prefix_energy_interval=list(map(str,nominal_prefix_residual_interval)),
  proposed_trial_complete_action_error_radius_upper=str(actual_error_radius),
  proposed_residual_definition='sum(w_i source_i) - sum(y_k nominal_action_k); proposal only, no new action certificate',
  scope='Every real or complex trial coefficient in the fixed RC218 nominal ten-action span; only the two-sided spectral residual chord. Actual action errors are not set to zero in an operator certificate. Mixed structural endpoints and other inverse methods are not excluded.',
  ideal_zero_error_test_only=True,true_inverse_failure_claimed=False,
  accepted_six_source_inverse_width_unchanged='4361/10000',RC216_action_error_gate_unchanged='0.420465',
  eight_source_inverse_gate_passed=False,Stage_I_closed=False,RH=False,F4=False,Lean=False,
  next_cursor='RC220: certify residual enrichment along the rational witness, or change the inverse enclosure mechanism; smaller error payments alone cannot make the fixed nominal ten-carrier two-sided residual chord pass. Recomputed carrier centers could change this span.')
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);p.add_argument('--replay',action='store_true');args=p.parse_args()
 expected=json.loads(args.output.read_text()) if args.replay else None
 result=run(args.replay,expected['rational_witness'] if expected else None)
 if args.replay:assert result==expected
 else:args.output.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
 print('RC219 PASS: nominal ten-span residual-chord floor',result['all_trial_coefficients_nominal_residual_chord_relative_width_lower'],'> 1/2; inverse gate remains open')
