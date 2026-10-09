#!/usr/bin/env python3
"""Paid physical four-retained-direction restriction, both lift families.
The source/native certificates are inherited authenticated proof inputs.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse,json,hashlib,gzip,base64
HASHES={
 'nf27':'2110e07c7a7e39d2b454cff364c0863f6f3e3ff151cf72309999130f5e17fe42',
 'nf29':'069d4acc267a0ac48154427a033cccca96243743dd31e36449f7189de03e895a',
 'nf30':'d0625cefe819f3704dec1d75bf0ad0bcd4ea8a3cd6806ebe6d76056733ac321b',
 'trial':'7460d5ed3b159d34fa002a56382b40f91cde1d7712fe5e2b1b0ff2b4df7cb65b',
 'targets':'6eee61fb4e58ac5be0e95f492f461b289da37ee13aeaa74bbf4acc06f6650c00',
 'nf26':'f2010510bacac64c45ef1825cd5e2c41e395519417815a43530e44e6cfdbf930'}
def read(path,key):
 b=Path(path).read_bytes()
 if path.endswith('.gz.b64'):b=gzip.decompress(base64.b64decode(b))
 assert hashlib.sha256(b).hexdigest()==HASHES[key]
 return json.loads(b)
def interval(x):
 l,h=map(F,x);assert l<=h;return l,h
def run(inputs,floor):
 j27,j29,j30,trial,targets,j26=inputs
 k=F(floor);assert k in (F(11,25),F(207,1000))
 assert trial['parity']=='even' and j30['parity']=='even'
 assert trial['additional_high_indices']==list(range(116,181,2))
 zs=list(map(F,trial['fixed_rational_coefficients']));z2=sum(v*v for v in zs)
 assert len(zs)==33 and j30['fixed_trial_sha256']==HASHES['trial']
 rows=[];checks=5
 for r27,r29,t,n in zip(j27['parity_certificates'],j29['parity_certificates'],targets['authenticated_compensated_targets'],j26['parity_certificates']):
  parity=r27['parity'];assert parity==r29['parity']==t['parity']==n['parity'];checks+=1
  x=list(map(F,t['retained_coefficients']));w=list(map(F,r27['exact_rational_retained_response']))
  assert len(x)==len(w)==56 and sum(a*b for a,b in zip(x,w))==0;checks+=1
  mx=sum(v*v for v in x);mw=sum(v*v for v in w)
  assert mx>0 and mw==F(r27['exact_response_norm_squared'])>0;checks+=1
  # Physical independence from the retained e0/e1 line is separately
  # tested. It is not used to certify the mixed union with that line.
  minor=sum(v*v for v in x[1:])*sum(v*v for v in w[1:])-sum(a*b for a,b in zip(x[1:],w[1:]))**2
  assert minor>0;checks+=1
  hs=list(map(F,t['exact_rational_high_compensation']))
  hx2=2*sum(v*v for v in hs)+2*F(n['correction_norm_upper'])**2
  hw2=sum(F(v)**2 for v in r29['fixed_rational_high_lift'])
  assert F(r29['lifted_response_norm_squared'])==mw+hw2;checks+=1
  for family in ('NF29 two-high response','NF30 expanded even response'):
   if family.startswith('NF30') and parity=='odd':continue
   src=r29 if family.startswith('NF29') else j30
   h2=hw2 if family.startswith('NF29') else hw2+z2
   Q=[[interval(y) for y in row] for row in src['original_finite_energy_Gram']]
   G=[[interval(y) for y in row] for row in src['original_complete_residual_Gram']]
   for i in range(2):
    assert Q[i][i][0]>0 and G[i][i][0]>0;checks+=2
   assert Q[0][1]==Q[1][0] and G[0][1]==G[1][0];checks+=2
   assert Q[0][0][0]*Q[1][1][0]>max(map(abs,Q[0][1]))**2;checks+=1
   assert G[0][0][0]*G[1][1][0]>max(map(abs,G[0][1]))**2;checks+=1
   # Same complete-source envelope supplies a LOWER Hermitian form,
   # not an entrywise approximation to the true inverse covariance.
   U=[[(Q[i][j][0]-G[i][j][1]/k,Q[i][j][1]-G[i][j][0]/k) for j in range(2)] for i in range(2)]
   b=max(map(abs,U[0][1]));det=U[0][0][0]*U[1][1][0]-b*b
   passed=U[0][0][0]>0 and U[1][1][0]>0 and det>0
   if k==F(11,25):assert passed;checks+=1
   elif family.startswith('NF30') or parity=='odd':assert passed;checks+=1
   else:assert U[1][1][1]<0 and det<0;checks+=1
   result={'parity':parity,'family':family,'complete_sufficient_matrix':[[[str(v) for v in entry] for entry in row] for row in U],
    'determinant_strict_lower':str(det),'positive_definite':passed,
    'retained_seed_mass_squared':str(mx),'retained_response_mass_squared':str(mw),
    'retained_e_seed_response_rank_three_minor':str(minor),
    'seed_high_lift_mass_squared_upper':str(hx2),'response_high_lift_mass_squared':str(h2)}
   if passed:
    # trace(U^-1 M) <= (U11_hi Mx+U00_hi Mw)/det_lo.
    mu=det/(U[1][1][1]*mx+U[0][0][1]*mw)
    eta2=(G[0][0][1]/mx+G[1][1][1]/mw)/(k*k)
    xi2=hx2/mx+h2/mw
    massfactor=1+4*eta2+4*xi2
    gap=min(mu/massfactor,k/2)
    assert mu>0 and gap>0;checks+=2
    guard=F(13,10**36) if parity=='even' and family.startswith('NF29') and k==F(11,25) else F(4,10**35) if parity=='even' and k==F(11,25) else F(65,10**33) if parity=='odd' and k==F(207,1000) else F(2,10**31) if parity=='odd' else F(3,10**36)
    assert gap>guard;checks+=1
    result.update({'retained_physical_Schur_gap_strict_lower':str(mu),
     'inverse_source_mass_eta_squared_upper':str(eta2),
     'trial_high_lift_mass_xi_squared_upper':str(xi2),
     'physical_mass_factor_upper':str(massfactor),
     'whole_high_physical_gap_strict_lower':str(gap),'display_gap':float(gap),
     'display_guard':str(guard),'all_original_high_modes_included':True})
   rows.append(result)
 chosen=[next(r for r in rows if r['parity']=='even' and r['family'].startswith('NF30')),next(r for r in rows if r['parity']=='odd')]
 common=min(F(r['whole_high_physical_gap_strict_lower']) for r in chosen)
 if k==F(11,25):assert common>F(4,10**35);checks+=1
 else:assert common>F(3,10**36);checks+=1
 return {'stage':'DNE20','aperture':'53/50','high_floor':str(k),'rows':rows,
  'selected_family':'NF30 expanded even plus NF29 odd','common_physical_gap_strict_lower':str(common),
  'display_common_gap':float(common),'retained_dimension':4,'uncovered_retained_dimension':108,
  'retained_subspace':'span(x_even,w_even,x_odd,w_odd)',
  'actual_null_with_retained_component_in_response_plane_excluded':True,
  'retained_union_with_DNE18_plane_dimension':6,'mixed_six_direction_union_certified':False,
  'exact_rational_assertions':checks,'authenticated_input_sha256':HASHES,
  'complete_source_identities_replayed_here':False,'whole_aperture_positive':False,
  'true_inverse_covariance_evaluated':False,'RH':False,'F4':False,'Lean':False}
if __name__=='__main__':
 p=argparse.ArgumentParser()
 for key in HASHES:p.add_argument(key)
 p.add_argument('--floor',default='11/25');p.add_argument('--output',required=True);args=p.parse_args()
 out=run([read(getattr(args,key),key) for key in HASHES],args.floor)
 Path(args.output).write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({'floor':out['high_floor'],'common_gap':out['display_common_gap'],'checks':out['exact_rational_assertions'],'rows':[{key:r.get(key) for key in ('parity','family','positive_definite','display_gap')} for r in out['rows']]}))
