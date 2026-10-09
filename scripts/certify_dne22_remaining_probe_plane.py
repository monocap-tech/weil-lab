#!/usr/bin/env python3
"""Exact consumer: successful probe plane and remaining loading obstruction."""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import json,hashlib,argparse
HASHES=['316ea81720e0992699ee8a37c5cc48b1170d811ef6d88bbdf19d46d03860c7a9','96a4f1448b0aa0d347ce79345e222d260c70af22cc86e7cd998626883e6fdb90','7e94e46f1f14d8991d44bf1d54b6886f4b7da50a52a0e9ddf6e3c786fb0c3ccc','eaf18cdbe6b5da0994b4ca884afc42fa53e8ccb5dc1d0d4815c8434021a70f24','5d669562c49ef8bacb74fe9817a3952160cd5868954dbef8160112eca1a748ab','6eee61fb4e58ac5be0e95f492f461b289da37ee13aeaa74bbf4acc06f6650c00','2110e07c7a7e39d2b454cff364c0863f6f3e3ff151cf72309999130f5e17fe42']
def root(x,d):
 s=10**d;n=isqrt(x.numerator*s*s//x.denominator);hi=F(n+1,s)
 assert F(n,s)**2<=x<hi*hi;return hi
def determinant(M):
 a=[row[:] for row in M];out=F(1)
 for i in range(len(a)):
  assert a[i][i]>0;v=a[i][i];out*=v
  for j in range(i+1,len(a)):
   f=a[j][i]/v
   for l in range(i+1,len(a)):a[j][l]-=f*a[i][l]
 return out
def run(paths,d):
 data=[]
 for path,sha in zip(paths,HASHES):
  b=Path(path).read_bytes();assert hashlib.sha256(b).hexdigest()==sha;data.append(json.loads(b))
 even,odd,trial,loading,d20,targets,nf27=data;k=F(11,25);rows=[];checks=7
 for src,t,L,target,response in zip((even,odd),trial['parities'],loading['parity_certificates'],targets['authenticated_compensated_targets'],nf27['parity_certificates']):
  parity=src['parity'];assert parity==t['parity']==L['parity']==target['parity']==response['parity'];checks+=1
  assert src['fixed_trial_sha256']==HASHES[2];checks+=1
  x=list(map(F,target['retained_coefficients']));w=list(map(F,response['exact_rational_retained_response']));u=list(map(F,t['fixed_rational_probe_coefficients']))
  dot=lambda a,b:sum(v*z for v,z in zip(a,b))
  assert len(x)==len(w)==len(u)==56 and dot(x,w)==dot(x,u)==dot(w,u)==0;checks+=1
  m=[dot(x,x),dot(w,w),dot(u,u)];assert all(v>0 for v in m);checks+=1
  assert m[2]==F(t['exact_physical_probe_mass'])==F(src['fixed_probe_mass']);checks+=1
  e=[F(1)]+[F(0)]*55;cols=[e,x,w,u]
  gram4=[[dot(a,b) for b in cols] for a in cols];rankminor=determinant(gram4);assert rankminor>0;checks+=1
  Q=[[[F(z) for z in y] for y in row] for row in src['original_native_energy_Gram']]
  G=[[[F(z) for z in y] for y in row] for row in src['original_complete_source_Gram']]
  U=[[(Q[i][j][0]-G[i][j][1]/k,Q[i][j][1]-G[i][j][0]/k) for j in range(3)] for i in range(3)]
  assert all(U[i][i][0]>0 for i in range(3));checks+=1
  assert all(U[i][j]==U[j][i] for i in range(3) for j in range(3));checks+=1
  scales=[F(10**17),F(10**18),F(10**11)] if parity=='even' else [F(10**15),F(2*10**16),F(10**9)]
  margins=[scales[i]**2*U[i][i][0]-sum(scales[i]*scales[j]*max(map(abs,U[i][j])) for j in range(3) if j!=i) for i in range(3)]
  g=min(margins);assert g>0;checks+=1
  family='NF30 expanded even response' if parity=='even' else 'NF29 two-high response'
  prior=next(r for r in d20['rows'] if r['parity']==parity and r['family']==family)
  assert m[0]==F(prior['retained_seed_mass_squared']) and m[1]==F(prior['retained_response_mass_squared']);checks+=1
  masses=[F(101,100),root(m[1]+F(prior['response_high_lift_mass_squared']),d),root(m[2],d)]
  completed=[mass+root(G[i][i][1],d)/k for i,mass in enumerate(masses)]
  inv=sum((scales[i]*completed[i])**2/g for i in range(3))+1/k;gap=1/inv
  guard=F(1,10**35) if parity=='even' else F(1,10**31);assert gap>guard;checks+=1
  # One native high coordinate supplies a lower bound for complete
  # energy-normalized loading. Rescale the SAME object to the new floor.
  ll,lh=map(F,L['observed_native_floor_loading_interval']);newload=(ll*F(207,1000)/k,lh*F(207,1000)/k)
  required=ll*F(207,1000);assert newload[0]>1 and required>k;checks+=2
  rows.append({'parity':parity,'basis':['NF24 seed x','NF27 response w','NF32 remaining probe u'],
   'complete_coarse_matrix_intervals':[[list(map(str,z)) for z in row] for row in U],
   'retained_physical_masses_squared':list(map(str,m)),
   'low_seed_response_probe_rank_four_Gram_determinant':str(rankminor),
   'congruence_scales':list(map(str,scales)),'scaled_Gershgorin_margins':list(map(str,margins)),
   'scaled_positive_margin':str(g),'lift_column_mass_upper':list(map(str,masses)),
   'inverse_source_completed_column_mass_upper':list(map(str,completed)),
   'whole_high_physical_gap_strict_lower':str(gap),'physical_gap_guard':str(guard),
   'display_gap':float(gap),'display_margin':float(g),
   'unchanged_full_remaining_loading_at_new_floor_interval':list(map(str,newload)),
   'necessary_floor_from_single_remaining_high_row_lower':str(required),
   'display_remaining_loading_lower':float(newload[0]),
   'display_necessary_remaining_floor_lower':float(required),
   'whole_three_direction_probe_restriction_passed':True,
   'full_unlifted_remaining_floor_estimator_rejected':True})
 common=min(F(r['whole_high_physical_gap_strict_lower']) for r in rows);assert common>F(1,10**35);checks+=1
 return {'stage':'DNE22','aperture':'53/50','root_digits':d,'high_floor':'11/25','rows':rows,
  'retained_subspace':'span(x_even,w_even,u_even,x_odd,w_odd,u_odd)',
  'retained_dimension':6,'uncovered_retained_dimension':106,
  'common_physical_gap_guard':'1/'+str(10**35),
  'common_physical_gap_strict_lower':str(common),
  'actual_null_with_retained_component_in_probe_plane_excluded':True,
  'union_with_DNE21_retained_dimension':8,'eight_direction_mixed_union_certified':False,
  'exact_rational_assertions':checks,'input_sha256':HASHES,
  'complete_source_producers_replayed_here':False,'actual_negative_Weil_vector_claimed':False,
  'whole_aperture_positive':False,'RH':False,'F4':False,'Lean':False}
if __name__=='__main__':
 p=argparse.ArgumentParser()
 for key in ('even','odd','trial','loading','dne20','targets','nf27'):p.add_argument(key)
 p.add_argument('--digits',type=int,default=160);p.add_argument('--output',required=True);args=p.parse_args()
 out=run([getattr(args,k) for k in ('even','odd','trial','loading','dne20','targets','nf27')],args.digits)
 Path(args.output).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'checks':out['exact_rational_assertions'],'rows':[{k:r[k] for k in ('parity','display_gap','display_margin','display_remaining_loading_lower')} for r in out['rows']]}))
