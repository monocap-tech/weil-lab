#!/usr/bin/env python3
"""Paid mixed four-direction assembly with the original DNE17 high floor.
Uses exact Fraction comparisons; numerical values are output displays only.
"""
from fractions import Fraction as F
from math import isqrt,factorial
from pathlib import Path
import argparse,json,hashlib,gzip,base64
def sqrt_bounds(x,digits):
 assert x>=0
 scale=10**digits;n=isqrt(x.numerator*scale*scale//x.denominator)
 l,h=F(n,scale),F(n+1,scale);assert l*l<=x<h*h
 return l,h
def run(native,targets,low,old,digits=220):
 k=F(11,25);a=F(53,50);rows=[]
 # Reconstruct a conservative UNIT source radius. The factor16 pole term
 # follows eta=2a epsilon+8 R40 with R40=2(a/2)^41/41!.
 eta=2*a*4*F(106,125)**320/(1-F(106,125))+16*(a/2)**41/F(factorial(41))
 for n,t,l,o in zip(native['parity_certificates'],targets['authenticated_compensated_targets'],low['native_parity_gates'],old['parity_rows']):
  parity=n['parity'];assert parity==t['parity']==l['parity']==o['parity']
  theta=F(2,5) if parity=='even' else F(3,5)
  qlo,qhi=map(F,n['corrected_native_energy']);plo,phi=map(F,n['complete_original_corrected_residual_square'])
  alo,ahi=map(F,l['native_Q_diagonal']);elo,ehi=map(F,l['full_F112_source_square'])
  assert 0<qlo<=qhi and 0<plo<=phi and 0<alo<=ahi and 0<elo<=ehi
  # Complete finite pairing Q(e_j,v), paying ONLY the tiny Ly replacement
  # error and the native p-coordinate interval, never a unit source error.
  pl,pu=map(F,t['low_source_coordinates'][0]);yl,yu=map(F,n['retained_approximant_Ly_coordinates'][0])
  paid=F(n['correction_norm_upper'])*eta
  blo,bhi=pl-yu-paid,pu-yl+paid;direct=max(abs(blo),abs(bhi))
  assert blo<=bhi
  ol,oh=map(F,o['original_direct_mixed_pairing']);assert blo<=oh and ol<=bhi
  root=sqrt_bounds(ehi*phi,digits)[1]
  mixed=direct+root/k
  A=alo-ehi/k;D=qlo-phi/k;assert A>0 and D>0
  determinant=A*D-mixed*mixed;assert determinant>0
  weighted_slack=(1-theta)**2*A*D-mixed*mixed;assert weighted_slack>0
  ratio=mixed*mixed/(A*D)
  # The inherited CC69 norm estimator failed at the old .207 floor.
  oldk=F(207,1000)
  oldA=alo-ehi/oldk;oldD=qlo-phi/oldk
  assert oldA>0 and oldD>0 and ehi*phi/oldk**2>oldA*oldD
  # Independence of the two retained coordinates is checked exactly.
  x=list(map(F,t['retained_coefficients']));assert sum(v*v for v in x[1:])>0
  pnorm2=F(t['compensated_norm_squared']);assert pnorm2<F(1001,1000)**2
  ynorm=F(n['correction_norm_upper']);assert ynorm<F(1,10**15)
  mass=F(101,100);assert F(1001,1000)+ynorm<mass
  # Whole high completion h=w-G r_w+z', with Q>=theta*(A|t|²+D|u|²)
  # +k||z'||². Triangle and weighted Cauchy pay the PHYSICAL mass.
  sr0=sqrt_bounds(ehi,digits)[1];srv=sqrt_bounds(phi,digits)[1]
  b0=1+sr0/k;b1=mass+srv/k
  inverse_gap=b0*b0/(theta*A)+b1*b1/(theta*D)+1/k
  physical_gap=1/inverse_gap
  assert physical_gap>F(1,10**35)
  display_guard=F(18,10**36) if parity=='even' else F(11,10**32)
  assert physical_gap>display_guard
  rows.append({'parity':parity,'basis':['e0' if parity=='even' else 'e1','NF24 retained seed x'],
   'exact_retained_basis_independent':True,'new_high_floor':str(k),'theta':str(theta),
   'low_diagonal_Schur_lower':str(A),'seed_diagonal_Schur_lower':str(D),
   'original_direct_mixed_pairing':[str(blo),str(bhi)],
   'conservative_unit_Ly_error_bound':str(eta),'tiny_correction_pairing_radius':str(paid),
   'inverse_response_mixed_norm_upper':str(root/k),
   'actual_Schur_mixed_absolute_upper':str(mixed),
   'determinant_strict_lower':str(determinant),
   'weighted_Schur_slack_strict_lower':str(weighted_slack),
   'mixed_square_over_diagonal_budget_upper':str(ratio),
   'trial_physical_norm_upper':str(mass),
   'whole_subspace_physical_gap_strict_lower':str(physical_gap),
   'display_gap_guard':str(display_guard),
   'display_A_lower':float(A),'display_D_lower':float(D),
   'display_mixed_upper':float(mixed),'display_ratio_upper':float(ratio),
   'display_physical_gap_lower':float(physical_gap),
   'old_norm_estimator_failure_replayed':True,
   'complete_mixed_block_passed':True})
 return {'stage':'DNE18','aperture':'53/50','root_digits':digits,'parity_rows':rows,
  'retained_plane_dimension':4,'excluded_retained_dimension':108,
  'certified_subspace':'span(e0,e1,x_even,x_odd)+F112 in the canonical original form domain',
  'restricted_original_physical_gap':'1/'+str(10**35),
  'all_retained_and_high_mixtures_on_this_subspace_certified':True,
  'actual_null_with_retained_projection_in_plane_excluded':True,
  'complete_112_retained_Schur_certified':False,
  'true_inverse_response_evaluated':False,'whole_aperture_positive':False,
  'RH':False,'F4':False,'Lean':False}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('native');p.add_argument('targets');p.add_argument('low');p.add_argument('old');p.add_argument('--digits',type=int,default=220);p.add_argument('--output',required=True);args=p.parse_args()
 raw=[]
 for v in (args.native,args.targets,args.low,args.old):
  b=Path(v).read_bytes()
  if v.endswith('.gz.b64'):b=gzip.decompress(base64.b64decode(b))
  raw.append(b)
 assert hashlib.sha256(raw[1]).hexdigest()=='6eee61fb4e58ac5be0e95f492f461b289da37ee13aeaa74bbf4acc06f6650c00'
 result=run(*(json.loads(v) for v in raw),digits=args.digits)
 result['input_sha256']=[hashlib.sha256(v).hexdigest() for v in raw]
 Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({'restricted_gap':result['restricted_original_physical_gap'],'rows':[{k:r[k] for k in ('parity','theta','display_A_lower','display_D_lower','display_mixed_upper','display_ratio_upper','display_physical_gap_lower','complete_mixed_block_passed')} for r in result['parity_rows']]},indent=2))
