#!/usr/bin/env python3
"""Exact NF38 fixed-frame transfer to the independently certified .44 floor."""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import argparse,json,hashlib,gzip,base64
SHA=['b6f7134f131dc2698868d676494d171e40340e81c453fb67d0e80520e082ce37','d0dee22dd8803b9f9b2545650a3f0ada382e55d10a36c834bf3350288161aa8c','05f3bcbc81e8d5f133fc5e49b61d80f8d1d4d6e65f1953d7dc65089b699ab5fd','3580ada8f259f02beeddedef5ab28e08cc96a2928c98cdc99390d337c54bad91','6f1adeb39792345e857806ce4128c72b9b08dabd4d21f6f3bde8a8463bd94671']
def read(p):
 b=Path(p).read_bytes()
 if p.endswith('.gz.b64'):b=gzip.decompress(base64.b64decode(b))
 return json.loads(b),hashlib.sha256(b).hexdigest()
def root(x,d):
 s=10**d;n=isqrt(x.numerator*s*s//x.denominator);v=F(n+1,s);assert v*v>x;return v
def coarse(Q,G,k):
 def sym(M,i,j):
  lo=max(F(M[i][j][0]),F(M[j][i][0]));hi=min(F(M[i][j][1]),F(M[j][i][1]));assert lo<=hi;return lo,hi
 return [[(sym(Q,i,j)[0]-sym(G,i,j)[1]/k,sym(Q,i,j)[1]-sym(G,i,j)[0]/k) for j in range(3)] for i in range(3)]
def quadratic(U,h):
 lo=hi=F(0)
 for i in range(3):
  for j in range(3):
   v=sorted(z*h[i]*h[j] for z in U[i][j]);lo+=v[0];hi+=v[1]
 return lo,hi
def run(paths,d):
 data=[read(p) for p in paths];assert [h for _,h in data]==SHA;checks=1
 even,odd,te,to,prior=[v for v,_ in data];k=F(11,25);rows=[]
 for idx,(s,t,r) in enumerate(zip((even,odd),(te,to),prior['rows'])):
  assert s['parity']==t['parity']==r['parity'];checks+=1
  assert s['fixed_trial_sha256']==SHA[idx+2];checks+=1
  assert list(map(F,s['inherited_retained_masses']))==list(map(F,r['retained_physical_masses_squared']));checks+=1
  assert all(j>=112 for j in t['correction_indices']);checks+=1
  z0=list(map(F,t['old_correction_coefficients']));z1=list(map(F,t['fixed_rational_second_correction_coefficients']));m0=sum(v*v for v in z0);m1=sum(v*v for v in z1)
  assert m0>0 and m1==F(t['exact_second_correction_mass_squared'])>0 and sum(a*b for a,b in zip(z0,z1))==0;checks+=1
  Q=s['original_selected_native_energy_Gram'];G=s['original_selected_complete_source_Gram'];U=coarse(Q,G,k);sc=list(map(F,r['congruence_scales']))
  for i in range(3):
   for j in range(3):assert U[i][j]==U[j][i];checks+=1
  margins=[sc[i]**2*U[i][i][0]-sum(sc[i]*sc[j]*max(map(abs,U[i][j])) for j in range(3) if j!=i) for i in range(3)];g=min(margins);assert g>0;checks+=1
  sufficient=F(3,10) if idx==0 else F(1,4);V=coarse(Q,G,sufficient)
  smaller=[sc[i]**2*V[i][i][0]-sum(sc[i]*sc[j]*max(map(abs,V[i][j])) for j in range(3) if j!=i) for i in range(3)];assert min(smaller)>0;checks+=1
  h=list(map(F,s['joint_universal_fixed_rational_witness']));old=quadratic(coarse(Q,G,F(207,1000)),h);new=quadratic(U,h)
  assert old[1]<0<new[0];checks+=1
  C=[list(map(F,row)) for row in s['selected_rational_joint_functionals']];zn=[root(m0,d),root(m1,d)]
  masses=[F(v)+sum(abs(C[j][i])*zn[j] for j in range(2)) for i,v in enumerate(s['source_norm_mass_upper'])]
  completed=[masses[i]+root(F(G[i][i][1]),d)/k for i in range(3)]
  gap=1/(sum((sc[i]*completed[i])**2/g for i in range(3))+1/k);guard=F(1,10**35) if idx==0 else F(1,10**31);assert gap>guard;checks+=1
  credit=F(1,100) if idx==0 else F(3,50);mu=credit/k
  qrows=[sc[i]**2*F(Q[i][i][1])+sum(sc[i]*sc[j]*max(abs(F(z)) for z in Q[i][j]) for j in range(3) if j!=i) for i in range(3)]
  creditm=[g-mu*v for v in qrows];assert min(creditm)>0;checks+=1
  rows.append(dict(parity=s['parity'],scaled_positive_margins=list(map(str,margins)),scaled_margin=str(g),
   sufficient_smaller_floor=str(sufficient),smaller_floor_scaled_margins=list(map(str,smaller)),
   old_universal_witness_value_on_same_selected_frame=list(map(str,old)),new_value_on_same_selected_frame=list(map(str,new)),
   physical_selected_column_mass_upper=list(map(str,masses)),high_completed_column_mass_upper=list(map(str,completed)),
   whole_high_physical_gap_strict_lower=str(gap),physical_gap_guard=str(guard),display_gap=float(gap),
   paid_three_direction_native_source_credit=str(credit),native_comparison_scaled_margins=list(map(str,creditm)),
   same_rational_frame_passes_at_new_floor=True,all_original_high_vectors_included=True))
 return dict(stage='DNE26',aperture='53/50',high_floor=str(k),root_digits=d,rows=rows,input_sha256=SHA,
  exact_rational_assertions=checks,six_direction_restriction_retained_span_unchanged=True,
  old_floor_universal_rejection_preserved=True,new_floor_universal_rejection_false=True,
  positive_retained_dimension_already_certified=8,uncovered_retained_dimension=104,
  low_mode_union_with_this_new_frame_certified=False,complete_remaining_source_Gram_computed=False,
  whole_aperture_positive=False,RH=False,F4=False,Lean=False)
if __name__=='__main__':
 p=argparse.ArgumentParser()
 for key in ['even','odd','trial_even','trial_odd','dne22']:p.add_argument(key)
 p.add_argument('--digits',type=int,default=160);p.add_argument('--output',required=True);a=p.parse_args();r=run([getattr(a,k) for k in ['even','odd','trial_even','trial_odd','dne22']],a.digits);Path(a.output).write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({'checks':r['exact_rational_assertions'],'rows':[{k:v[k] for k in ['parity','display_gap','sufficient_smaller_floor','paid_three_direction_native_source_credit']} for v in r['rows']]}))
