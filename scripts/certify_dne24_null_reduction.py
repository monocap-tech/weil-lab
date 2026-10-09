#!/usr/bin/env python3
"""Exact retained complement for DNE23; no inverse response is evaluated."""
from fractions import Fraction as F
from pathlib import Path
import argparse,base64,gzip,hashlib,json
HASHES=['6eee61fb4e58ac5be0e95f492f461b289da37ee13aeaa74bbf4acc06f6650c00','2110e07c7a7e39d2b454cff364c0863f6f3e3ff151cf72309999130f5e17fe42','7e94e46f1f14d8991d44bf1d54b6886f4b7da50a52a0e9ddf6e3c786fb0c3ccc','ee5c3ebab7fe2d015ff92145b5c69b72630d90cb6306530e8bd8769469e21557','0cb636cdf03ad09f57cfce6d4bc67d0b7094dc1c154597cb0d1fe467590a2fd6']
def read(p):
 b=Path(p).read_bytes()
 if p.endswith('.gz.b64'):b=gzip.decompress(base64.b64decode(b))
 return json.loads(b),hashlib.sha256(b).hexdigest()
def dot(a,b):return sum(v*z for v,z in zip(a,b))
def reduce(rows):
 a=[r[:] for r in rows];inv=[[F(i==j) for j in range(4)] for i in range(4)];piv=[];det=F(1)
 for j in range(56):
  i=len(piv)
  if i==4:break
  q=next((q for q in range(i,4) if a[q][j]),None)
  if q is None:continue
  if q!=i:a[q],a[i]=a[i],a[q];inv[q],inv[i]=inv[i],inv[q];det=-det
  z=a[i][j];det*=z;a[i]=[v/z for v in a[i]];inv[i]=[v/z for v in inv[i]]
  for q in range(4):
   if q!=i:
    z=a[q][j];a[q]=[v-z*w for v,w in zip(a[q],a[i])];inv[q]=[v-z*w for v,w in zip(inv[q],inv[i])]
  piv.append(j)
 assert len(piv)==4 and det
 return a,inv,piv,det
def construct(paths):
 data=[read(p) for p in paths];assert [h for _,h in data]==HASHES
 targets,response,trial,nf31,prior=[v for v,_ in data];out=[];checks=1
 assert prior['eight_direction_mixed_union_certified'] and F(prior['common_physical_gap_guard'])==F(1,10**36);checks+=1
 for idx,(t,r,u,n) in enumerate(zip(targets['authenticated_compensated_targets'],response['parity_certificates'],trial['parities'],nf31['parity_certificates'])):
  parity=['even','odd'][idx];assert parity==t['parity']==r['parity']==u['parity']==n['parity'];checks+=1
  e=[F(1)]+[F(0)]*55;x=list(map(F,t['retained_coefficients']));w=list(map(F,r['exact_rational_retained_response']));probe=list(map(F,u['fixed_rational_probe_coefficients']));Z=[e,x,w,probe]
  assert all(len(v)==56 for v in Z);checks+=1
  rr,inv,piv,det=reduce(Z);free=[j for j in range(56) if j not in piv];assert len(free)==52;checks+=1
  columns=[]
  for j in free:
   col=[F(k==j) for k in range(56)]
   for i,p in enumerate(piv):col[p]=-rr[i][j]
   for z in Z:assert dot(z,col)==0;checks+=1
   for k in free:assert col[k]==F(k==j);checks+=1
   columns.append(col)
  p,q=n['retained_constraint_pivots'];dd=x[p]*w[q]-x[q]*w[p];assert dd;checks+=1
  oldfree=n['free_retained_coordinates'];assert len(oldfree)==54;checks+=1
  # Embed every new column in the authenticated positive raw NF31 frame.
  for col in columns:
   v=[F(0)]*56
   for j in oldfree:
    v[j]+=col[j];v[p]+=col[j]*(-x[j]*w[q]+x[q]*w[j])/dd;v[q]+=col[j]*(-x[p]*w[j]+x[j]*w[p])/dd
   for a,b in zip(v,col):assert a==b;checks+=1
  beta=F(n['physical_remaining_native_gap_lower']);assert beta>0;checks+=1
  assert dot(x,w)==dot(x,probe)==dot(w,probe)==0;checks+=1
  out.append(dict(parity=parity,remaining_dimension=52,retained_indices=t['retained_indices'],constraint_column_names=['low','seed','response','probe'],constraint_pivots=piv,free_coordinates=free,
   pivot_matrix_determinant=str(det),pivot_matrix_inverse=[[str(v) for v in row] for row in inv],
   complement_rule='W_j=e_j-sum_i (inverse(pivot_constraint_matrix)*Z[:,j])_i e_pivot_i',
   exact_orthogonality_to_all_four=True,free_coordinate_minor_is_identity=True,
   exact_embedding_in_NF31_positive_raw_remaining_frame=True,
   inherited_raw_complement_physical_native_gap_lower=str(beta),display_native_gap=float(beta),
   actual_null_dimension_upper=52,negative_index_upper=52))
 return dict(stage='DNE24',aperture='53/50',rows=out,input_sha256=HASHES,exact_rational_assertions=checks,
  positive_eliminated_retained_dimension=8,remaining_finite_dimension=104,
  eliminated_infinite_subspace_physical_gap_guard='1/'+str(10**36),
  actual_null_dimension_upper=104,negative_index_upper=104,
  exact_reduced_response_evaluated=False,unit_response_eigenvalue_excluded=False,
  whole_aperture_positive=False,RH=False,F4=False,Lean=False)
if __name__=='__main__':
 p=argparse.ArgumentParser()
 for k in ['targets','response','trial','nf31','dne23']:p.add_argument(k)
 p.add_argument('--output',required=True);a=p.parse_args();r=construct([getattr(a,k) for k in ['targets','response','trial','nf31','dne23']])
 Path(a.output).write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({'checks':r['exact_rational_assertions'],'rows':[{k:v[k] for k in ['parity','constraint_pivots','remaining_dimension','display_native_gap']} for v in r['rows']]}))
