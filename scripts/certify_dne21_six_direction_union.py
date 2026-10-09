#!/usr/bin/env python3
"""Six retained directions with every high mode: exact outward consumer."""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import json,gzip,base64,hashlib,argparse
def root(x,d):
 scale=10**d;n=isqrt(x.numerator*scale*scale//x.denominator)
 lo,hi=F(n,scale),F(n+1,scale);assert lo*lo<=x<hi*hi;return hi
def read(path):
 b=Path(path).read_bytes()
 if path.endswith('.gz.b64'):b=gzip.decompress(base64.b64decode(b))
 return json.loads(b),hashlib.sha256(b).hexdigest()
def run(paths,digits):
 values=[read(p) for p in paths];nf31,low,nf29,nf30,d20,d18=[v[0] for v in values]
 assert values[0][1]=='ee5c3ebab7fe2d015ff92145b5c69b72630d90cb6306530e8bd8769469e21557'
 assert values[1][1]=='ebca74e6237cf401b7480afe08b91caba2c3412dc08e55ac2ac55f1970d8f788'
 assert values[2][1]=='069d4acc267a0ac48154427a033cccca96243743dd31e36449f7189de03e895a'
 assert values[3][1]=='d0625cefe819f3704dec1d75bf0ad0bcd4ea8a3cd6806ebe6d76056733ac321b'
 assert values[4][1]=='5d669562c49ef8bacb74fe9817a3952160cd5868954dbef8160112eca1a748ab'
 assert values[5][1]=='0420e4993e6347eddeec47095887a6216bf10d17cfe6628bed4261cd36763297'
 assert nf31['authenticated_input_sha256'][3]==values[2][1] and nf31['authenticated_input_sha256'][5]==values[3][1]
 k=F(11,25);rows=[];checks=7
 for n,l,n29,d18row in zip(nf31['parity_certificates'],low['native_parity_gates'],nf29['parity_certificates'],d18['parity_rows']):
  parity=n['parity'];assert parity==l['parity']==n29['parity']==d18row['parity'];checks+=1
  src=nf30 if parity=='even' else n29
  form=[[[F(z) for z in y] for y in x] for x in src['original_finite_energy_Gram']]
  gram=[[[F(z) for z in y] for y in x] for x in src['original_complete_residual_Gram']]
  U=[[None]*3 for _ in range(3)]
  alo,ahi=map(F,l['native_Q_diagonal']);plo,phi=map(F,l['full_F112_source_square'])
  assert 0<alo<=ahi and 0<plo<=phi;checks+=2
  U[0][0]=(alo-phi/k,ahi-plo/k)
  pairings=[];norm_response=[]
  for i in range(2):
   qlo,qhi=map(F,n['retained_approximant_source_coordinates'][i][0])
   error=F(n['source_coordinate_reconstruction_error_bounds'][i]);assert error>=0;checks+=1
   qlo-=error;qhi+=error;pairings.append([str(qlo),str(qhi)])
   radius=root(phi*gram[i][i][1],digits)/k
   U[0][i+1]=(qlo-radius,qhi+radius);U[i+1][0]=U[0][i+1]
   norm_response.append(radius)
   if i==0:
    a,b=map(F,d18row['original_direct_mixed_pairing']);assert qlo<=b and a<=qhi;checks+=1
  for i in range(2):
   for j in range(2):
    U[i+1][j+1]=(form[i][j][0]-gram[i][j][1]/k,form[i][j][1]-gram[i][j][0]/k)
  assert U[1][2]==U[2][1];checks+=1
  scales=[F(5),F(10**17),F(10**18)] if parity=='even' else [F(3),F(10**15),F(2*10**16)]
  margins=[scales[i]**2*U[i][i][0]-sum(scales[i]*scales[j]*max(map(abs,U[i][j])) for j in range(3) if j!=i) for i in range(3)]
  g=min(margins);assert g>0;checks+=1
  # Physical completion uses column masses, never orthonormal coordinates.
  family='NF30 expanded even response' if parity=='even' else 'NF29 two-high response'
  r=next(r for r in d20['rows'] if r['parity']==parity and r['family']==family)
  assert F(r['retained_e_seed_response_rank_three_minor'])>0;checks+=1
  response_mass=F(r['retained_response_mass_squared'])+F(r['response_high_lift_mass_squared'])
  masses=[F(1),F(101,100),root(response_mass,digits)]
  rs=[phi,gram[0][0][1],gram[1][1][1]]
  columns=[m+root(p,digits)/k for m,p in zip(masses,rs)]
  inverse_gap=sum((scales[i]*columns[i])**2/g for i in range(3))+1/k
  gap=1/inverse_gap
  guard=F(1,10**35) if parity=='even' else F(1,10**32)
  assert gap>guard;checks+=1
  rows.append({'parity':parity,'retained_basis':['e0' if parity=='even' else 'e1','NF24 seed x','NF27 response w'],
   'original_low_lift_pairings':pairings,
   'coarse_three_direction_matrix_intervals':[[[str(v) for v in y] for y in x] for x in U],
   'rational_congruence_scales':list(map(str,scales)),
   'scaled_Gershgorin_margins':list(map(str,margins)),
   'scaled_positive_margin':str(g),'lift_column_mass_upper':list(map(str,masses)),
   'inverse_source_corrected_column_mass_upper':list(map(str,columns)),
   'whole_high_inverse_gap_upper':str(inverse_gap),'whole_high_physical_gap_strict_lower':str(gap),
   'display_positive_margin':float(g),'display_physical_gap':float(gap),
   'display_guard':str(guard),'all_high_modes_included':True,'mixed_union_positive':True})
 common=min(F(r['whole_high_physical_gap_strict_lower']) for r in rows)
 assert common>F(1,10**35);checks+=1
 return {'stage':'DNE21','aperture':'53/50','root_digits':digits,'high_floor':'11/25',
  'rows':rows,'retained_dimension':6,'uncovered_retained_dimension':106,
  'retained_plane':'span(e0,e1,x_even,w_even,x_odd,w_odd)',
  'common_physical_gap_guard':'1/'+str(10**35),'common_physical_gap_strict_lower':str(common),
  'mixed_six_direction_union_certified':True,'actual_null_with_retained_component_in_union_excluded':True,
  'exact_rational_assertions':checks,'input_sha256':[v[1] for v in values],
  'complete_source_producers_replayed_here':False,'true_inverse_covariance_evaluated':False,
  'complete_retained_Schur_certified':False,'whole_aperture_positive':False,'RH':False,'F4':False,'Lean':False}
if __name__=='__main__':
 p=argparse.ArgumentParser()
 for key in ('nf31','low','nf29','nf30','dne20','dne18'):p.add_argument(key)
 p.add_argument('--digits',type=int,default=160);p.add_argument('--output',required=True);args=p.parse_args()
 out=run([getattr(args,k) for k in ('nf31','low','nf29','nf30','dne20','dne18')],args.digits)
 Path(args.output).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'checks':out['exact_rational_assertions'],'rows':[{k:r[k] for k in ('parity','display_positive_margin','display_physical_gap')} for r in out['rows']]}))
