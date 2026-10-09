#!/usr/bin/env python3
"""Coherent complete-source bound for the joint eight-direction restriction."""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import argparse,json,gzip,base64,hashlib
def root(x,d):
 s=10**d;n=isqrt(x.numerator*s*s//x.denominator);h=F(n+1,s);assert F(n,s)**2<=x<h*h;return h
def read(path):
 b=Path(path).read_bytes()
 if path.endswith('.gz.b64'):b=gzip.decompress(base64.b64decode(b))
 return json.loads(b),hashlib.sha256(b).hexdigest()
def run(paths,d):
 inputs=[read(p) for p in paths];nf31,low,even,odd,prior,pe,po=[v[0] for v in inputs]
 expected=['ee5c3ebab7fe2d015ff92145b5c69b72630d90cb6306530e8bd8769469e21557','ebca74e6237cf401b7480afe08b91caba2c3412dc08e55ac2ac55f1970d8f788','316ea81720e0992699ee8a37c5cc48b1170d811ef6d88bbdf19d46d03860c7a9','96a4f1448b0aa0d347ce79345e222d260c70af22cc86e7cd998626883e6fdb90','6f1adeb39792345e857806ce4128c72b9b08dabd4d21f6f3bde8a8463bd94671']
 assert [v[1] for v in inputs[:5]]==expected
 allowed=[{'a51ff14f2d4f2d041253746f3ce79231f58810047f5bc1b71a80c13de55f752a','c63e5b696d1765b2027eb3edb13b85e517952db0eef890e74ec0433aff3b844d'}, {'4fe9ceccf07b64273d724af42c201ac5b6489fb4a43ac6c3f2112ed803a1e8e4','d958d4be005842d6b4a0ba237e3f17e045777a0ddb56bced81444a65c9227d29'}]
 assert all(v[1] in s for v,s in zip(inputs[5:],allowed))
 k=F(11,25);theta=F(1,10);rows=[];checks=2
 for n,l,src,r,pair in zip(nf31['parity_certificates'],low['native_parity_gates'],(even,odd),prior['rows'],(pe,po)):
  parity=n['parity'];assert parity==l['parity']==src['parity']==r['parity']==pair['parity'];checks+=1
  assert pair['helper_sha256']=='e4539b941f3768f177a469c68f58d34b11d3ea863247c14c1a6a59d81b2f91d8' and pair['fixed_trial_sha256']==src['fixed_trial_sha256'];checks+=1
  assert pair['CC62_low_diagonal_overlap'] and pair['regular_order']>=360 and pair['precision']>=600;checks+=1
  Q=[[[F(z) for z in v] for v in row] for row in src['original_native_energy_Gram']]
  G=[[[F(z) for z in v] for v in row] for row in src['original_complete_source_Gram']]
  V=[[(Q[i][j][0]-G[i][j][1]/k,Q[i][j][1]-G[i][j][0]/k) for j in range(3)] for i in range(3)]
  assert V==[[tuple(map(F,z)) for z in row] for row in r['complete_coarse_matrix_intervals']];checks+=1
  scales=list(map(F,r['congruence_scales']));g=F(r['scaled_positive_margin'])
  # Certify the entire source Gram <= V, not three unrelated diagonal tests.
  W=[[(V[i][j][0]-G[i][j][1],V[i][j][1]-G[i][j][0]) for j in range(3)] for i in range(3)]
  margins=[scales[i]**2*W[i][i][0]-sum(scales[i]*scales[j]*max(map(abs,W[i][j])) for j in range(3) if i!=j) for i in range(3)]
  assert min(margins)>0;checks+=1
  p=[]
  for i in range(2):
   lo,hi=map(F,n['retained_approximant_source_coordinates'][i][0]);e=F(n['source_coordinate_reconstruction_error_bounds'][i]);p.append((lo-e,hi+e))
  p.append(tuple(map(F,pair['original_low_probe_pairing'])))
  dual=sum(scales[i]**2*max(map(abs,p[i]))**2 for i in range(3))/g
  alo,ahi=map(F,l['native_Q_diagonal']);P0=F(l['full_F112_source_square'][1]);A=alo-P0/k
  # The actual joint source Gram enforces |g0 z|²<=P0 z*Gamma3 z.
  # Gamma3<=V converts this into the SAME V norm as the native row p.
  M=root(dual,d)+root(P0,d)/k
  alpha=A-M*M/(1-theta);assert alpha>0;checks+=1
  assert F(r['low_seed_response_probe_rank_four_Gram_determinant'])>0;checks+=1
  masses=list(map(F,r['lift_column_mass_upper']));completed=[m+root(G[i][i][1],d)/k for i,m in enumerate(masses)]
  b0=1+root(P0,d)/k
  inversegap=b0*b0/alpha+sum((scales[i]*completed[i])**2/(theta*g) for i in range(3))+1/k
  gap=1/inversegap;guard=F(1,10**36) if parity=='even' else F(1,10**32)
  assert gap>guard;checks+=1
  rows.append({'parity':parity,'basis':['e0' if parity=='even' else 'e1','NF24 seed x','NF27 response w','NF32 probe u'],
   'original_low_lift_pairings':[[str(z) for z in v] for v in p],
   'source_Gram_dominated_by_coarse_three_direction_form':True,
   'scaled_V_minus_Gamma_margins':list(map(str,margins)),
   'native_low_mixed_V_dual_square_upper':str(dual),
   'coherent_source_mixed_V_dual_norm_upper':str(root(P0,d)/k),
   'combined_mixed_V_dual_norm_upper':str(M),
   'original_low_coarse_diagonal_lower':str(A),'joint_low_diagonal_lower':str(alpha),
   'theta':str(theta),'joint_remaining_coordinate_lower':str(theta*g),
   'congruence_scales':list(map(str,scales)),
   'high_completed_low_column_mass_upper':str(b0),
   'high_completed_other_column_masses_upper':list(map(str,completed)),
   'whole_high_physical_gap_strict_lower':str(gap),
   'display_joint_low_lower':float(alpha),'display_gap':float(gap),
   'display_gap_guard':str(guard),'all_original_high_modes_included':True})
 common=min(F(r['whole_high_physical_gap_strict_lower']) for r in rows);assert common>F(1,10**36);checks+=1
 return {'stage':'DNE23','aperture':'53/50','root_digits':d,'high_floor':'11/25','rows':rows,
  'retained_dimension':8,'uncovered_retained_dimension':104,
  'retained_plane':'span(e0,e1,x_even,w_even,u_even,x_odd,w_odd,u_odd)',
  'common_physical_gap_guard':'1/'+str(10**36),'common_physical_gap_strict_lower':str(common),
  'eight_direction_mixed_union_certified':True,'actual_null_with_retained_component_in_union_excluded':True,
  'fresh_original_low_probe_pairings_used':True,'uncomputed_low_source_crosses_paid_coherently':True,
  'exact_rational_assertions':checks,'input_sha256':[v[1] for v in inputs],
  'complete_three_direction_source_certificates_inherited':True,
  'true_inverse_response_evaluated':False,'whole_aperture_positive':False,'RH':False,'F4':False,'Lean':False}
if __name__=='__main__':
 p=argparse.ArgumentParser()
 for key in ('nf31','low','even','odd','dne22','pair_even','pair_odd'):p.add_argument(key)
 p.add_argument('--digits',type=int,default=160);p.add_argument('--output',required=True);a=p.parse_args()
 out=run([getattr(a,k) for k in ('nf31','low','even','odd','dne22','pair_even','pair_odd')],a.digits)
 Path(a.output).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'checks':out['exact_rational_assertions'],'rows':[{k:r[k] for k in ('parity','display_joint_low_lower','display_gap')} for r in out['rows']]}))
