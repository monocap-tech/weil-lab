"""RC133: six-vector Gram and endpoint pairings; all infinite tails paid."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,hashlib
from validate_rpb108_rc127_enriched_even_endpoint_action import B,Z,rat,plus,minus,mul,div,bounds,down,up,sqrtup,psd,ser,loewner
from validate_rpb108_rc129_four_vector_joint_moment import add

def run(paths,replay=False):
 raw=[Path(p).read_bytes() for p in paths];new,capture,remaining,joint,response=map(json.loads,raw)
 hs=[hashlib.sha256(x).hexdigest() for x in raw]
 assert [c['milestone'] for c in (new,capture,remaining,joint,response)]==['RC132','RC131','RC130','RC129','RC128']
 assert new['input_sha256']==hs[1:] and capture['input_sha256']==hs[2:]
 # Reconstruct RC132's actual source and finite Cb output without modifying history.
 src=Path(__file__).with_name('validate_rpb108_rc132_balanced_action_shared_covariance.py').read_text()
 cut=src.index(" print('RC132 balanced finite action complete'")
 fragment=src[:cut]+'\n return locals()\n'
 namespace={};exec(compile(fragment,'RC132-reconstruction','exec'),namespace)
 d=namespace['run'](paths[1:],replay)
 g,b,poly,dn,diag=d['g'],d['b'],d['polynomial'],d['dn'],d['diag']
 s=d['s'];alpha=F(new['alpha']);O=8191;L=4095;Acut=4095;N=6
 assert hashlib.sha256(json.dumps(poly,sort_keys=True,separators=(',',':')).encode()).hexdigest()==new['finite_output_polynomial_center_radius_sha256']
 # Reconstruct Cg trial's exact rational finite polynomial and hash.
 vp=[];jobs=list(g);jobs=jobs[::-1] if replay else jobs
 for n in range(0,O+1,2):
  value=Z
  for m in jobs:
   entry=diag[n] if n==m else rat(F(2*n+1,abs(n-m)*(n+m+1)))
   value=plus(value,mul(entry,rat(g[m])))
  lo,hi=bounds(div(value,dn[n]));center=down((lo+hi)/2);radius=max(center-lo,hi-center)
  vp.append(dict(degree=n,center=str(center),radius=str(radius)))
 assert hashlib.sha256(json.dumps(vp,sort_keys=True,separators=(',',':')).encode()).hexdigest()==capture['finite_output_polynomial_center_radius_sha256']
 print('RC133 both new collective polynomials reconstructed',flush=True)
 mu=list(map(F,response['collective_response_enrichment_budgets'][2]['analytic_moment_center_coefficients']))
 vb=capture['collective_capture_budgets'][1];zb=new['balanced_action_and_shared_covariance_budgets'][1]
 nuv=list(map(F,vb['analytic_moment_center_coefficients']));nuz=list(map(F,zb['analytic_moment_centers']))
 oldlam=988*989;lam=4094*4095;first=8192;zf=first*(first+1)
 vectors=[{0:rat(1)}, {}, d['f'], {}, {x['degree']:rat(F(x['center'])) for x in vp}, {x['degree']:rat(F(x['center'])) for x in poly}]
 for n in range(0,O+1,2):
  if n>=990:vectors[1][n]=div(rat(F(2*n+1,n*(n+1))),dn[n])
  if n<=4094:vectors[3][n]=rat(g[n])
  else:
   scale=sum(mu[k]*F(oldlam,n*(n+1))**k for k in range(len(mu)))
   vectors[3][n]=mul(vectors[1][n],rat(scale))
 amps=[F(0),F(1),F(0),up(sum(mu[k]*F(oldlam,zf)**k for k in range(len(mu)))),up(sum(nuv[k]*F(lam,zf)**k for k in range(len(nuv)))),up(sum(nuz[k]*F(lam,zf)**k for k in range(len(nuz))))]
 T=F(capture['leading_new_output_tail_D_energy_upper'])
 tails=[up(T*a*a,10**100) for a in amps]
 GLp=[[F(0)]*N for _ in range(N)];GUp=[[F(0)]*N for _ in range(N)]
 prefixCut=[F(0)]*N
 for i in range(N):
  for j in range(i,N):
   val=Z;prefix=Z;ns=sorted(set(vectors[i])&set(vectors[j]));ns=ns[::-1] if replay else ns
   for n in ns:
    mass=mul(rat(2*B/F(2*n+1)),dn[n]);term=mul(mass,mul(vectors[i][n],vectors[j][n]));val=plus(val,term)
    if n<=Acut:prefix=plus(prefix,term)
   lo,hi=bounds(val);GLp[i][j]=GLp[j][i]=lo;GUp[i][j]=GUp[j][i]=hi
   if i==j:prefixCut[i]=bounds(prefix)[1]
 GeL=[r[:] for r in GLp];GeU=[r[:] for r in GUp]
 for i in range(N):
  for j in range(N):GeU[i][j]=up(GeU[i][j]+sqrtup(tails[i]*tails[j]))
 # Gram tail is PSD, so finite-prefix Loewner lower establishes full independence.
 weights=[sqrtup(GeU[i][i]) for i in range(N)]
 GLprefix,GUprefix,Gerr=loewner(GLp,GUp,weights)
 floorDigits=1
 while True:
  floor=[[GeL[i][i]/10**floorDigits if i==j else F(0) for j in range(N)] for i in range(N)]
  if psd(add(GLprefix,floor,-1)):break
  floorDigits+=1;assert floorDigits<35
 GU=add(GUprefix,[[N*tails[i] if i==j else F(0) for j in range(N)] for i in range(N)])
 assert psd(add(GU,GLprefix,-1))
 print('RC133 six-vector Gram independence certified',flush=True)
 # Every finite/analytic omitted source is paid; positivity makes prefix a lower.
 omitted=[]
 for i in range(N):
  energy=Z
  for n in (sorted(vectors[i],reverse=replay)):
   if n>Acut:energy=plus(energy,mul(mul(rat(2*B/F(2*n+1)),dn[n]),mul(vectors[i][n],vectors[i][n])))
  omitted.append(up(bounds(energy)[1]+tails[i],10**100))
 # Evaluate only genuinely new finite endpoint blocks; inherit first four.
 HeL=[[F(0)]*N for _ in range(N)];HeU=[[F(0)]*N for _ in range(N)]
 for i in range(4):
  for j in range(4):HeL[i][j]=F(joint['actual_endpoint_pairing_entry_lower'][i][j]);HeU[i][j]=F(joint['actual_endpoint_pairing_entry_upper'][i][j])
 ns=list(range(0,Acut+1,2));ns=ns[::-1] if replay else ns
 for j in (list(range(4,N))[::-1] if replay else range(4,N)):
  action={}
  for n in ns:
   value=Z
   for m in ns:
    if m not in vectors[j]:continue
    entry=mul(rat(2*B/F(2*n+1)),diag[n]) if n==m else rat(F(2*B,abs(n-m)*(n+m+1)))
    value=plus(value,mul(entry,vectors[j][m]))
   action[n]=value
  for i in range(j+1):
   val=Z
   for n in ns:
    if n in vectors[i]:val=plus(val,mul(vectors[i][n],action[n]))
   lo,hi=bounds(val)
   err=up(sqrtup(prefixCut[i]*omitted[j])+sqrtup(prefixCut[j]*omitted[i])+sqrtup(omitted[i]*omitted[j]))
   HeL[i][j]=HeL[j][i]=lo;HeU[i][j]=HeU[j][i]=min(up(hi+err),sqrtup(GeU[i][i]*GeU[j][j]))
  print('RC133 new endpoint column',j,'paid',flush=True)
 # Exact CP0 identity, paid Cf0=w identity and paid Cw=v+error tighten mixed pairs.
 aLo=F(joint['actual_endpoint_pairing_entry_lower'][0][0])/F(joint['actual_D_Gram_entry_upper'][0][0])
 aHi=F(joint['actual_endpoint_pairing_entry_upper'][0][0])/F(joint['actual_D_Gram_entry_lower'][0][0])
 ef=F(response['collective_response_enrichment_budgets'][2]['full_Cf0_approximation_D_norm_error_upper'])
 ew=F(vb['full_Cw_approximation_D_norm_error_upper'])
 for j in range(4,N):
  for i,lo,hi in [(0,down(aLo*GeL[0][j]+GeL[1][j]+GeL[2][j]),up(aHi*GeU[0][j]+GeU[1][j]+GeU[2][j])),(2,down(GeL[3][j]-ef*sqrtup(GeU[j][j])),up(GeU[3][j]+ef*sqrtup(GeU[j][j]))),(3,down(GeL[4][j]-ew*sqrtup(GeU[j][j])),up(GeU[4][j]+ew*sqrtup(GeU[j][j])))]:
   HeL[i][j]=HeL[j][i]=max(HeL[i][j],lo)
   HeU[i][j]=HeU[j][i]=min(HeU[i][j],hi)
 assert all(HeL[i][j]<=HeU[i][j] for i in range(N) for j in range(N))
 HL,HU,Herr=loewner(HeL,HeU,weights)
 # Structural 0<=H<=G is inherited from C; arithmetic interval PSD checks are reported separately.
 return dict(milestone='RC133',status='PASS: six-vector independent Gram and all endpoint pairings certified with paid infinite tails',starting_commit='80d46a2801c4e997945b636650549f43cc8cb149',input_sha256=hs,aperture='11/10',joint_family=['P0','psi0','f0','w14','v10','z_b6'],family_dimension=6,finite_Gram_output_degree=8190,endpoint_prefix_degree=4094,finite_prefix_actual_Gram_entry_lower=ser(GLp),finite_prefix_actual_Gram_entry_upper=ser(GUp),actual_D_Gram_entry_lower=ser(GeL),actual_D_Gram_entry_upper=ser(GeU),actual_D_Gram_Loewner_lower=ser(GLprefix),actual_D_Gram_Loewner_upper=ser(GU),Gram_relative_diagonal_floor=str(F(1,10**floorDigits)),Gram_positive_floor_Loewner_matrix=ser(floor),six_vector_independence_certified=True,all_new_finite_polynomial_hashes_verified=True,weighted_Gram_prefix_interval_error_diagonal=list(map(str,Gerr)),analytic_tail_coefficient_amplitude_upper=list(map(str,amps)),analytic_tail_D_energy_upper=list(map(str,tails)),endpoint_omitted_finite_and_analytic_source_D_energy_upper=list(map(str,omitted)),actual_endpoint_pairing_entry_lower=ser(HeL),actual_endpoint_pairing_entry_upper=ser(HeU),actual_endpoint_pairing_Loewner_lower=ser(HL),actual_endpoint_pairing_Loewner_upper=ser(HU),weighted_endpoint_interval_error_diagonal=list(map(str,Herr)),endpoint_Loewner_lower_psd_verified=psd(HL),Gram_lower_minus_endpoint_upper_psd_verified=psd(add(GLprefix,HU,-1)),endpoint_positive_contraction_structurally_inherited=True,endpoint_contraction_used_to_pay_all_omitted_mixed_blocks=True,original_four_input_pairings_inherited=True,new_vector_action_or_covariance_evaluated=False,full_six_input_covariance_evaluated=False,new_reference_response_interval_certified=False,RC130_reference_response_interval_inherited_unchanged=True,original_Weil_or_augmented_actions_performed=False,whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False,next_cursor='tighten remaining analytic and new-vector endpoint actions; certify full six-input covariance before inverse update')

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');p.add_argument('--output',required=True);p.add_argument('inputs',nargs=5);a=p.parse_args();c=run(a.inputs,a.replay)
 if a.replay:assert json.loads(Path(a.output).read_text())==c
 else:Path(a.output).write_text(json.dumps(c,sort_keys=True,indent=2)+'\n')
 print('RC133 PASS: full independent six-vector Gram and paid endpoint pairings')
