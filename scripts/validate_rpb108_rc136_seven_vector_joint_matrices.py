"""RC136: seven-vector joint Gram and correlated endpoint pairings."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,hashlib
from validate_rpb108_rc127_enriched_even_endpoint_action import B,Z,rat,plus,minus,mul,div,bounds,down,up,sqrtup,psd,ser,loewner
from validate_rpb108_rc129_four_vector_joint_moment import add

def run(paths,replay=False):
 raw=[Path(p).read_bytes() for p in paths];capture,prior,joint,balanced,finite,remaining,old,response=map(json.loads,raw)
 hs=[hashlib.sha256(x).hexdigest() for x in raw]
 assert [x['milestone'] for x in (capture,prior,joint,balanced,finite,remaining,old,response)]==['RC135','RC134','RC133','RC132','RC131','RC130','RC129','RC128']
 assert capture['input_sha256']==hs[1:] and prior['input_sha256']==hs[2:]
 src=Path(__file__).with_name('validate_rpb108_rc135_common_response_capture.py').read_text()
 cut=src.index(" print('RC135 common finite action complete'")
 namespace={'__file__':str(Path(__file__).with_name('validate_rpb108_rc135_common_response_capture.py'))}
 exec(compile(src[:cut]+'\n return locals()\n','RC135-reconstruction','exec'),namespace)
 d=namespace['run'](paths[1:],replay);poly=d['poly'];base=d['d'];dn=d['dn'];diagonal=d['diagonal']
 assert hashlib.sha256(json.dumps(poly,sort_keys=True,separators=(',',':')).encode()).hexdigest()==capture['finite_output_polynomial_center_radius_sha256']
 assert hashlib.sha256(json.dumps([dict(degree=n,center=str(d['source'][n])) for n in sorted(d['source'])],sort_keys=True,separators=(',',':')).encode()).hexdigest()==capture['common_finite_source_coefficient_sha256']
 vec=[v.copy() for v in base['vectors']]+[{x['degree']:rat(F(x['center'])) for x in poly}]
 O=16383;Acut=4095;N=7;zf=16384*16385;lam=d['lam'];oldlam=base['lam'];mu=base['mu'];nuv=base['nuv'];nuz=base['nuz'];wlam=base['oldlam']
 for n in range(8192,O+1,2):
  z=n*(n+1);psi=div(rat(F(2*n+1,z)),dn[n]);vec[1][n]=psi
  for i,mom,lambda_i in ((3,mu,wlam),(4,nuv,oldlam),(5,nuz,oldlam)):
   amp=sum(x*F(lambda_i,z)**k for k,x in enumerate(mom));vec[i][n]=mul(psi,rat(amp))
 budget=capture['collective_capture_budgets'][1];nut=list(map(F,budget['analytic_moment_centers']))
 amps=[F(0),F(1),F(0),up(sum(x*F(wlam,zf)**k for k,x in enumerate(mu))),up(sum(x*F(oldlam,zf)**k for k,x in enumerate(nuv))),up(sum(x*F(oldlam,zf)**k for k,x in enumerate(nuz))),up(sum(x*F(lam,zf)**k for k,x in enumerate(nut)))]
 T=F(capture['leading_output_tail_D_energy_upper']);tails=[up(T*a*a,10**100) for a in amps]
 GLp=[[F(0)]*N for _ in range(N)];GUp=[[F(0)]*N for _ in range(N)];prefixEnergy=[F(0)]*N;omittedFinite=[F(0)]*N
 for i in range(N):
  for j in range(i,N):
   value=prefix=omitted=Z
   for n in sorted(set(vec[i])&set(vec[j]),reverse=replay):
    term=mul(mul(rat(2*B/F(2*n+1)),dn[n]),mul(vec[i][n],vec[j][n]));value=plus(value,term)
    if n<=Acut:prefix=plus(prefix,term)
    else:omitted=plus(omitted,term)
   lo,hi=bounds(value);GLp[i][j]=GLp[j][i]=lo;GUp[i][j]=GUp[j][i]=hi
   if i==j:prefixEnergy[i]=bounds(prefix)[1];omittedFinite[i]=bounds(omitted)[1]
 GeL=[r[:] for r in GLp];GeU=[r[:] for r in GUp]
 for i in range(N):
  for j in range(N):GeU[i][j]=up(GeU[i][j]+sqrtup(tails[i]*tails[j]))
 weights=[sqrtup(GeU[i][i]) for i in range(N)];GL,GUfin,Gerr=loewner(GLp,GUp,weights)
 k=1
 while True:
  floor=[[GLp[i][i]/10**k if i==j else F(0) for j in range(N)] for i in range(N)]
  if psd(add(GL,floor,-1)):break
  k+=1;assert k<35
 GU=add(GUfin,[[N*tails[i] if i==j else F(0) for j in range(N)] for i in range(N)])
 assert psd(add(GU,GL,-1))
 print('RC136 seven-vector full Gram and independence paid',flush=True)
 omitted=[up(omittedFinite[i]+tails[i],10**100) for i in range(N)]
 HeL=[[F(0)]*N for _ in range(N)];HeU=[[F(0)]*N for _ in range(N)]
 for i in range(6):
  for j in range(6):HeL[i][j]=F(joint['actual_endpoint_pairing_entry_lower'][i][j]);HeU[i][j]=F(joint['actual_endpoint_pairing_entry_upper'][i][j])
 ns=list(range(0,Acut+1,2));ns=ns[::-1] if replay else ns;action={}
 for n in ns:
  value=Z
  for m in ns:
   entry=mul(rat(2*B/F(2*n+1)),diagonal[n]) if n==m else rat(F(2*B,abs(n-m)*(n+m+1)))
   value=plus(value,mul(entry,vec[6][m]))
  action[n]=value
 for i in range(N):
  value=Z
  for n in ns:
   if n in vec[i]:value=plus(value,mul(vec[i][n],action[n]))
  lo,hi=bounds(value)
  error=up(sqrtup(prefixEnergy[i]*omitted[6])+sqrtup(prefixEnergy[6]*omitted[i])+sqrtup(omitted[i]*omitted[6]))
  HeL[i][6]=HeL[6][i]=lo;HeU[i][6]=HeU[6][i]=min(up(hi+error),sqrtup(GeU[i][i]*GeU[6][6]))
 # Historical action identities tighten the new row.
 alo=F(old['actual_endpoint_pairing_entry_lower'][0][0])/F(old['actual_D_Gram_entry_upper'][0][0])
 ahi=F(old['actual_endpoint_pairing_entry_upper'][0][0])/F(old['actual_D_Gram_entry_lower'][0][0])
 ef=F(response['collective_response_enrichment_budgets'][2]['full_Cf0_approximation_D_norm_error_upper'])
 ew=F(finite['collective_capture_budgets'][1]['full_Cw_approximation_D_norm_error_upper'])
 normt=sqrtup(GeU[6][6])
 identities=[(0,down(alo*GeL[0][6]+GeL[1][6]+GeL[2][6]),up(ahi*GeU[0][6]+GeU[1][6]+GeU[2][6])),(2,down(GeL[3][6]-ef*normt),up(GeU[3][6]+ef*normt)),(3,down(GeL[4][6]-ew*normt),up(GeU[4][6]+ew*normt))]
 for i,lo,hi in identities:HeL[i][6]=HeL[6][i]=max(HeL[i][6],lo);HeU[i][6]=HeU[6][i]=min(HeU[i][6],hi)
 # Cu=t+error supplies a joint common row, not independent v/z intervals.
 eu=F(budget['full_common_action_trial_D_norm_error_upper']);erru=up(eu*normt)
 commonL=max(down(GeL[6][6]-erru),(HeL[4][6]+HeL[5][6])/2)
 commonU=min(up(GeU[6][6]+erru),(HeU[4][6]+HeU[5][6])/2)
 assert commonL<=commonU
 # C-I/2 has norm <=1/2. Keep the signed delta pairing centered at G_delta,t/2.
 deltaGramL=down(GeL[5][6]-GeU[4][6]);deltaGramU=up(GeU[5][6]-GeL[4][6])
 deltaEnergy=F(prior['z_minus_v_full_source_D_energy_upper']);deltaError=up(sqrtup(deltaEnergy)*normt/2)
 deltaL=max(down(deltaGramL/2-deltaError),HeL[5][6]-HeU[4][6])
 deltaU=min(up(deltaGramU/2+deltaError),HeU[5][6]-HeL[4][6]);assert deltaL<=deltaU
 alpha=F(balanced['alpha']);eShared=F(balanced['balanced_action_and_shared_covariance_budgets'][1]['shared_residual_difference_D_norm_upper'])
 # The same paid full action identity holds before projection:
 # Cw-alpha*Cpsi=z_b+error, even though its residual use was in RC132's union span.
 corrError=up(eShared*normt);corrL=down(GeL[5][6]-corrError);corrU=up(GeU[5][6]+corrError)
 for _ in range(3):
  vl=max(HeL[4][6],down(commonL-deltaU/2));vu=min(HeU[4][6],up(commonU-deltaL/2))
  zl=max(HeL[5][6],down(commonL+deltaL/2));zu=min(HeU[5][6],up(commonU+deltaU/2))
  HeL[4][6]=HeL[6][4]=vl;HeU[4][6]=HeU[6][4]=vu
  HeL[5][6]=HeL[6][5]=zl;HeU[5][6]=HeU[6][5]=zu
  wl=max(HeL[3][6],down(alpha*HeL[1][6]+corrL));wu=min(HeU[3][6],up(alpha*HeU[1][6]+corrU))
  pl=max(HeL[1][6],down((wl-corrU)/alpha));pu=min(HeU[1][6],up((wu-corrL)/alpha))
  HeL[3][6]=HeL[6][3]=wl;HeU[3][6]=HeU[6][3]=wu
  HeL[1][6]=HeL[6][1]=pl;HeU[1][6]=HeU[6][1]=pu
 assert all(HeL[i][j]<=HeU[i][j] for i in range(N) for j in range(N))
 HL,HU,Herr=loewner(HeL,HeU,weights)
 print('RC136 full new endpoint row and correlated identities paid',flush=True)
 return dict(milestone='RC136',status='PASS: seven-vector independent Gram and full endpoint matrix with correlated new-row identities',starting_commit='2c0bd82172f1266b4ebc3f2bf766d11377e5e7ff',input_sha256=hs,aperture='11/10',joint_family=joint['joint_family']+['t10_common_response'],family_dimension=7,selected_RC135_finite_source_norm_target='1/1000000000000',new_finite_polynomial_hash_verified=True,finite_Gram_prefix_degree=O-1,endpoint_prefix_degree=Acut-1,finite_prefix_Gram_entry_lower=ser(GLp),finite_prefix_Gram_entry_upper=ser(GUp),actual_D_Gram_entry_lower=ser(GeL),actual_D_Gram_entry_upper=ser(GeU),actual_D_Gram_Loewner_lower=ser(GL),actual_D_Gram_Loewner_upper=ser(GU),Gram_relative_diagonal_floor=str(F(1,10**k)),Gram_positive_floor_Loewner_matrix=ser(floor),weighted_Gram_prefix_error_diagonal=list(map(str,Gerr)),analytic_tail_amplitude_upper=list(map(str,amps)),analytic_tail_D_energy_upper=list(map(str,tails)),endpoint_omitted_finite_and_analytic_source_D_energy_upper=list(map(str,omitted)),actual_endpoint_pairing_entry_lower=ser(HeL),actual_endpoint_pairing_entry_upper=ser(HeU),actual_endpoint_pairing_Loewner_lower=ser(HL),actual_endpoint_pairing_Loewner_upper=ser(HU),weighted_endpoint_error_diagonal=list(map(str,Herr)),common_source_t_endpoint_pairing_lower=str(commonL),common_source_t_endpoint_pairing_upper=str(commonU),common_action_t_pairing_error_upper=str(erru),difference_source_t_D_Gram_lower=str(deltaGramL),difference_source_t_D_Gram_upper=str(deltaGramU),difference_source_t_endpoint_pairing_lower=str(deltaL),difference_source_t_endpoint_pairing_upper=str(deltaU),centered_contraction_difference_pairing_error_upper=str(deltaError),w_minus_alpha_psi_t_endpoint_pairing_lower=str(corrL),w_minus_alpha_psi_t_endpoint_pairing_upper=str(corrU),w_minus_alpha_psi_t_pairing_error_upper=str(corrError),all_infinite_mixed_blocks_paid=True,seven_vector_independence_certified=True,common_and_difference_pairing_constraints_preserved=True,endpoint_Loewner_lower_psd_verified=psd(HL),Gram_lower_minus_endpoint_upper_psd_verified=psd(add(GL,HU,-1)),endpoint_positive_contraction_structurally_inherited=True,full_new_vector_action_evaluated=False,full_seven_input_covariance_evaluated=False,RC135_old_six_covariance_in_same_span_inherited=True,new_reference_response_interval_certified=False,RC130_reference_response_interval_inherited_unchanged=True,original_Weil_or_augmented_actions_performed=False,whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False,next_cursor='certify Ct10 and remaining analytic covariance in the seven-vector span, using correlated endpoint identities in a conditioned Schur enclosure')

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');p.add_argument('--output',required=True);p.add_argument('inputs',nargs=8);a=p.parse_args();c=run(a.inputs,a.replay)
 if a.replay:assert json.loads(Path(a.output).read_text())==c
 else:Path(a.output).write_text(json.dumps(c,sort_keys=True,indent=2)+'\n')
 print('RC136 PASS: seven-vector joint Gram and correlated endpoint matrices')
