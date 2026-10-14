"""RC220: a finite residual enrichment candidate with complete canonical action.

Nominal residual capture and actual residual capture are distinct obligations.
The old action-error radii are retained even when they prevent an actual
residual lower bound. The new finite polynomial has its own action certificate.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,json
import validate_rpb108_rc219_nominal_trial_span_barrier as prev
from validate_rpb108_rc127_enriched_even_endpoint_action import B,Z,rat,plus,minus,div,mul,bounds,down,up,sqrtup
from validate_rpb108_rc134_correlated_six_input_covariance import smul
from validate_rpb108_rc176_f0_regular_output_carrier import root,lower_root
ROOT=Path(__file__).resolve().parents[1]
PINS=dict(prev.PINS)
PINS.update({
 'certificates/rpb108_rc219_nominal_trial_span_barrier.json':'fa3a97ddb1b2450cab857b0568ed419ebfa9d5da',
 'certificates/rpb108_rc218_materialized_native_carriers.json':'1bc627d0cee338c78dfdcb14e2cbaa041141d175'})
HELPER_PINS=dict(prev.HELPER_PINS)
HELPER_PINS['scripts/validate_rpb108_rc219_nominal_trial_span_barrier.py']='a7e9ebb0803ce10fe1850a511667562f52ed2b69'
def rows(c,key):return {r['degree']:F(r['coefficient_center']) for r in c[key]}
def total(xs):
 out=Z
 for x in xs:out=plus(out,x)
 return out
def prepare(reverse=False):
 data={}
 for p,sha in sorted(HELPER_PINS.items(),reverse=reverse):assert prev.prev.prev.blob((ROOT/p).read_bytes())==sha,(p,'helper pin')
 for p,sha in sorted(PINS.items(),reverse=reverse):
  raw=(ROOT/p).read_bytes();assert prev.prev.prev.blob(raw)==sha,(p,'input pin');data[p]=json.loads(raw)
 get=lambda n:data['certificates/rpb108_rc'+n+'.json']
 c=get('219_nominal_trial_span_barrier');d=get('218_materialized_prefix_interface');native=get('218_materialized_native_carriers')
 w=list(map(F,c['proposed_residual_source_coefficients']));y=list(map(F,c['proposed_residual_trial_coefficients']));keep=[0,1,2,3,4,6,8,9]
 joint=get('129_four_vector_joint_moment');sl=F(joint['actual_D_Gram_entry_lower'][0][0])/(2*B);sh=F(joint['actual_D_Gram_entry_upper'][0][0])/(2*B)
 H=[Z]
 for n in range(1,8191):H.append(plus(H[-1],rat(F(1,n))))
 D={n:(plus(H[n],rat(sl))[0],plus(H[n],rat(sh))[1]) for n in range(0,4095,2)}
 wc=get('183_materialized_w14_canonical_carrier');gw={2*i:F(x) for i,x in enumerate(wc['native_w14_finite_coefficient_centers'])};gv={2*i:F(x) for i,x in enumerate(wc['Cg_finite_coefficient_centers'])}
 vcert=get('197_native_v10_canonical_action');assert all(gv[n]==x for n,x in rows(vcert,'input_prefix_coefficients').items())
 dv={x['degree']:F(x['center']) for x in native['delta_finite_rows']};tv={x['degree']:F(x['center']) for x in native['t10_finite_center_radius_rows']}
 low=get('192_low_polynomial_regular_actions');p0=get('171_regular_legendre_projection');p2=get('172_quadratic_regular_action');fc=get('193_extended_f0_regular_action')
 r0=rows(low['actions'][0]['regular_action'],'D_inverse_regular_polynomial');r2=rows(low['actions'][1]['regular_action'],'D_inverse_regular_polynomial')
 rf=rows(fc['regular_action'],'D_inverse_regular_polynomial');nf=rows(fc,'negative_r_D_inverse_f0_polynomial')
 pc=get('188_materialized_Cpsi_carrier');cw=get('190_materialized_Cw14_carrier');cv=get('200_materialized_Cv10_carrier')
 center=lambda c,key,n:F(int(c[key][n//2]),int(c['finite_center_scale']))
 nw=rows(wc,'negative_r_D_inverse_w14_finite_polynomial');rw=rows(cw,'D_inverse_regular_polynomial')
 nv=rows(vcert,'negative_r_finite_polynomial');rv=rows(vcert['regular_action'],'D_inverse_regular_polynomial')
 qs=[get('185_five_source_focus_action'),get('202_six_source_residual_action')]
 qin=[rows(q,'finite_focus_direction') for q in qs];qact=[]
 for i,qc in enumerate(qs):
  ep=rows(qc,'endpoint_action_polynomial');ng=rows(qc,'negative_r_D_inverse_direction_polynomial');rg=rows(qc['regular_action'],'D_inverse_regular_polynomial')
  qact.append({n:qin[i].get(n,F(0))+ep.get(n,F(0))+ng.get(n,F(0))+rg.get(n,F(0)) for n in range(0,769,2)})
 new=[get('214_correlated_difference_canonical_action'),get('216_refined_t10_canonical_action')]
 cep=[rows(z,'endpoint_action_polynomial') for z in new];creg=[rows(z['regular_action'],'D_inverse_regular_polynomial') for z in new]
 r=F(789,125);qrows=[];prefix_lo=prefix_hi=rounding=F(0);snap={}
 for n in (range(768,-1,-2) if reverse else range(0,769,2)):
  eta=div(rat(F(2*n+1,n*(n+1))),D[n]) if n else Z
  f=eta if n else Z
  u=[rat(F(n==0)),rat(F(n==2)),f,Z,rat(gw[n]),rat(qin[0].get(n,F(0))),rat(gv[n]),rat(qin[1].get(n,F(0))),rat(dv[n]),rat(tv[n])]
  v0=rat(r0.get(n,F(0)))
  v0=plus(v0,rat(1+F(p0['canonical_constant_action_P0_correction_center']))) if n==0 else plus(v0,eta)
  v2=rat(r2.get(n,F(0)))
  if n==0:v2=plus(v2,rat(F(p2['endpoint_P0_coefficient_center'])))
  elif n==2:v2=plus(v2,rat(1+F(p2['endpoint_P2_correction_center'])))
  else:v2=plus(v2,div(rat(F(2*n+1,n*(n+1)-6)),D[n]))
  vf=plus(plus(f,rat(gw[n])),rat(nf.get(n,F(0))+rf.get(n,F(0))))
  vp=rat(center(pc,'finite_Cpsi_coefficient_center_numerators',n))
  vw=rat(gw[n]+center(cw,'finite_Cw14_coefficient_center_numerators',n)+nw.get(n,F(0))+rw.get(n,F(0)))
  vv=rat(gv[n]+center(cv,'finite_Cv10_coefficient_center_numerators',n)+nv.get(n,F(0))+rv.get(n,F(0)))
  if n>=514:vv=minus(vv,smul(div(rat(r),D[n]),rat(gv[n])))
  extra=[minus(rat(src[n]+cep[i].get(n,F(0))+creg[i].get(n,F(0))),smul(div(rat(r),D[n]),rat(src[n]))) for i,src in enumerate([dv,tv])]
  v=[v0,v2,vf,vp,vw,rat(qact[0][n]),vv,rat(qact[1][n])]+extra
  res=minus(total([smul(rat(w[j]),u[keep[j]]) for j in range(8)]),total([smul(rat(y[k]),v[k]) for k in range(10)]))
  lo,hi=bounds(res);cc=down((lo+hi)/2);rad=max(cc-lo,hi-cc);ml,mh=bounds(mul(rat(2*B/F(2*n+1)),D[n]))
  qrows.append(dict(degree=n,coefficient_center=str(cc),coefficient_radius=str(rad)))
  rmin=F(0) if lo<=0<=hi else min(abs(lo),abs(hi))
  snap[n]=(down(ml*rmin*rmin),up(mh*max(abs(lo),abs(hi))**2),up(mh*rad*rad))
 qrows.sort(key=lambda x:x['degree'])
 slv=list(map(F,d['source_tail_signed_leading_coefficients']));sd=list(map(F,d['source_tail_nonleading_absolute_bounds']));vl=list(map(F,d['action_tail_signed_leading_coefficients']));vd=list(map(F,d['action_tail_nonleading_absolute_bounds']))
 lead=sum(w[j]*slv[keep[j]] for j in range(8))-sum(y[k]*vl[k] for k in range(10))
 rem=sum(abs(w[j])*sd[keep[j]] for j in range(8))+sum(abs(y[k])*vd[k] for k in range(10))
 tail=up(F(d['common_eta_tail_D_energy_upper'])*(abs(lead)+rem)**2)
 full_lo,full_hi=map(F,c['proposed_residual_prefix_energy_interval']);nomlo=lower_root(full_lo);actualerr=F(c['proposed_trial_complete_action_error_radius_upper'])
 candidates=[]
 for M in [128,256,512,768]:
  captured=sum(snap[n][0] for n in snap if n<=M);rounding=sum(snap[n][2] for n in snap if n<=M)
  omitted=up(full_hi-captured+tail);assert omitted>=0
  nominal=up(root(omitted+rounding));actual=up(nominal+actualerr);actual_lower=max(F(0),down(nomlo-actualerr))
  rel=up(nominal/nomlo)
  candidates.append(dict(finite_input_degree=M,nominal_residual_D_norm_lower=str(nomlo),nominal_prefix_captured_energy_lower=str(captured),nominal_omitted_prefix_and_tail_energy_upper=str(omitted),nominal_input_rounding_energy_upper=str(rounding),nominal_residual_to_polynomial_D_error_norm_upper=str(nominal),nominal_capture_relative_error_upper=str(rel),nominal_half_norm_capture_passed=rel<F(1,2),inherited_actual_trial_action_error_radius_upper=str(actualerr),actual_residual_D_norm_lower=str(actual_lower),actual_residual_to_polynomial_D_error_norm_upper=str(actual),actual_half_norm_capture_certified=bool(actual_lower and actual<F(1,2)*actual_lower)))
  print('RC220 capture',M,float(rel),'actual lower',float(actual_lower),flush=True)
 chosen=min(candidates,key=lambda c:(F(c['nominal_capture_relative_error_upper']),c['finite_input_degree']))
 qrows=[x for x in qrows if x['degree']<=chosen['finite_input_degree']]
 return locals()
def run(reverse=False):
 st=prepare(reverse);get=st['get'];qrows=st['qrows'];chosen=st['chosen'];q={x['degree']:F(x['coefficient_center']) for x in qrows};M=max(q);D=st['D'];r=st['r'];joint=st['joint']
 # The new trial is an exact finite rational polynomial, whether or not it
 # approximates the actual residual within the separate half-norm budget.
 path=ROOT/'scripts/validate_rpb108_rc179_focus_residual_canonical_action.py';src=path.read_text().split("\nif __name__=='__main__':")[0];assert src.count('K=192;N=768;J=')==1
 src=src.replace('K=192;N=768;J=','K=192;N=2304;J=');ns={'__file__':str(path)};exec(compile(src,'RC220 finite regular action','exec'),ns)
 helper=ROOT/'scripts/validate_rpb108_rc171_regular_legendre_projection.py';hs=helper.read_text().split("\nif __name__=='__main__':")[0];assert hs.count('prec=360')==2 and hs.count("TOL=D('1e-300')")==1
 assert hs.count('for j in range(600):')==1
 hs=hs.replace('prec=360','prec=900').replace("TOL=D('1e-300')","TOL=D('1e-840')").replace('for j in range(600):','for j in range(1000):');private={};exec(compile(hs,'RC220 private directed arithmetic','exec'),private)
 for k in ['ZERO','rat','add','sub','mul','scale','divide','div_int','endpoints','log_point']:ns[k]=private[k]
 ns['root']=lambda x,grid=10**900:root(x,grid)
 reg=ns['regular_action'](q,get('170_poisson_regular_action'),joint,reverse)
 O=4094;H=st['H'];sl=st['sl'];sh=st['sh'];log=(rat(1-F(joint['actual_endpoint_pairing_entry_upper'][0][0])/(2*B))[0],rat(1-F(joint['actual_endpoint_pairing_entry_lower'][0][0])/(2*B))[1])
 endpoint=[];negative=[];ee=ne=qlo=qhi=F(0)
 for n in (range(O,-1,-2) if reverse else range(0,O+1,2)):
  value=Z
  for m in sorted(q,reverse=reverse):
   entry=minus(plus(minus(smul(rat(2),H[2*n]),smul(rat(2),H[n])),rat(F(1,2*n+1))),log) if n==m else rat(F(2*n+1,abs(n-m)*(n+m+1)))
   value=plus(value,smul(entry,rat(q[m])))
  lo,hi=private['endpoints'](private['divide'](value,D[n]));cc=down((lo+hi)/2);rad=max(cc-lo,hi-cc)
  endpoint.append(dict(degree=n,coefficient_center=str(cc),coefficient_radius=str(rad)));ee+=up(2*B/F(2*n+1)*F(D[n][1])*rad*rad)
  if n<=M:
   lo,hi=private['endpoints'](private['divide'](private['rat'](-r*q[n]),D[n]));cc=(lo+hi)/2;rad=(hi-lo)/2
   negative.append(dict(degree=n,coefficient_center=str(cc),coefficient_radius=str(rad)));ne+=up(2*B/F(2*n+1)*F(D[n][1])*rad*rad)
   qlo+=down(2*B/F(2*n+1)*F(D[n][0])*q[n]**2);qhi+=up(2*B/F(2*n+1)*F(D[n][1])*q[n]**2)
  if n%1024==0:print('RC220 endpoint block',n,flush=True)
 endpoint.sort(key=lambda x:x['degree']);negative.sort(key=lambda x:x['degree']);assert qlo>0
 lam=M*(M+1);rho=F(lam,(O+2)*(O+3));moments=[sum(q[m]*F(m*(m+1),lam)**k for m in sorted(q,reverse=reverse)) for k in range(25)]
 A=sum(abs(x) for x in q.values());T=up(B/(F(D[O][0])*(O-1)*O));tailerror=up(root(T)*A*rho**25/(1-rho),10**80)
 epserr=up(root(ee+tailerror*tailerror));err=up(epserr+root(ne)+F(reg['complete_D_inverse_regular_action_error_norm_upper']))
 cp=rows({'x':endpoint},'x');np=rows({'x':negative},'x');rp=rows(reg,'D_inverse_regular_polynomial');pair=Z
 for n in sorted(q,reverse=reverse):pair=plus(pair,smul(rat(2*B/F(2*n+1)*q[n]*(q[n]+cp[n]+np[n]+rp.get(n,F(0)))),D[n]))
 lo,hi=bounds(pair);pay=root(qhi)*err;actualLo=down(lo-pay);actualHi=up(hi+pay);a=F(32125,230953)
 assert actualLo>a*qhi and actualHi<2*qlo
 # Certify improvement of this one nominal witness without inventing an
 # actual-residual lower bound or rebuilding the full eight-source inverse.
 # <r_nom,Mq> >= <q,Mq> - ||r_nom-q|| ||Mq||, with the independently
 # certified actual action of the exact finite polynomial q.
 actionEnergy=sum(up(2*B/F(2*n+1)*F(D[n][1])*(q.get(n,F(0))+cp[n]+np.get(n,F(0))+rp.get(n,F(0)))**2) for n in D)
 actionTail=T*sum(abs(x)*rho**k for k,x in enumerate(moments))**2
 actionNorm=up(root(actionEnergy+actionTail)+err)
 residualQDistance=F(chosen['nominal_residual_to_polynomial_D_error_norm_upper'])
 crossLower=down(actualLo-residualQDistance*actionNorm);assert crossLower>0
 theta=down(crossLower/actionNorm**2,10**24);assert theta>0
 oldLower=st['full_lo'];oldUpper=up(st['full_hi']+st['tail'])
 correctedActualEnergy=up(oldUpper-2*theta*crossLower+theta**2*actionNorm**2);assert correctedActualEnergy>0
 # Pay the new action radius to return to the stored nominal eleven-action
 # span. This is a nominal residual improvement, not an inverse enclosure.
 correctedNominalEnergy=up((root(correctedActualEnergy)+theta*err)**2)
 assert correctedNominalEnergy<oldLower
 reduction=down(1-correctedNominalEnergy/oldLower)
 sourceFloor=prev.prev.mat(get('218_coupled_expanded_inverse'),'source_D_Gram_lower')
 sourceEnergyLower=prev.bil(st['w'],sourceFloor,st['w']);assert sourceEnergyLower>0
 witnessChordUpper=up((1/a-F(1,2))*correctedNominalEnergy/sourceEnergyLower)
 correction=dict(actual_q_action_D_norm_upper=str(actionNorm),nominal_target_actual_q_action_pairing_lower=str(crossLower),
  correction_coefficient=str(theta),old_nominal_residual_energy_lower=str(oldLower),old_nominal_residual_energy_upper=str(oldUpper),
  corrected_actual_q_action_target_residual_energy_upper=str(correctedActualEnergy),
  corrected_nominal_eleven_trial_witness_residual_energy_upper=str(correctedNominalEnergy),
  nominal_witness_residual_energy_reduction_fraction_lower=str(reduction),
  witness_source_D_energy_lower=str(sourceEnergyLower),nominal_witness_residual_chord_relative_width_upper=str(witnessChordUpper),
  nominal_witness_half_Gram_chord_passed=witnessChordUpper<F(1,2),
  one_witness_strict_improvement_proved=True,
  scope='Only the RC219 nominal target direction; no uniform eight-source inverse-width improvement claimed. Both the old actual-action errors and the new q action radius are retained.')
 return dict(milestone='RC220',starting_commit='dc7b695ed4cabfdde7424cb94b371dd74a33ea68',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,
  canonical_operator='M=D^-1 L',norm='D energy',aperture='11/10',source_probe=list(map(str,st['w'])),nominal_residual_trial_coefficients=list(map(str,st['y'])),
  evaluated_capture_candidates=st['candidates'],selected_capture=chosen,finite_focus_direction=qrows,finite_input_degree=M,
  finite_focus_D_energy_lower=str(qlo),finite_focus_D_energy_upper=str(qhi),regular_action=reg,endpoint_action_polynomial=endpoint,endpoint_output_degree=O,
  endpoint_analytic_first_even_degree=O+2,endpoint_analytic_lambda=str(lam),endpoint_exact_signed_moments=list(map(str,moments)),
  endpoint_analytic_remainder_D_norm_upper=str(tailerror),endpoint_action_full_D_error_norm_upper=str(epserr),negative_r_D_inverse_direction_polynomial=negative,
  complete_actual_canonical_q_action_D_error_norm_upper=str(err),complete_actual_canonical_q_action_relative_D_error_norm_upper=str(up(err/lower_root(qlo))),
  actual_q_canonical_pairing_lower=str(actualLo),actual_q_canonical_pairing_upper=str(actualHi),canonical_q_pairing_a_D_to_2_D_verified=True,
  full_input_and_infinite_action_output_tails_paid=True,nominal_half_norm_capture_passed=chosen['nominal_half_norm_capture_passed'],actual_half_norm_capture_certified=chosen['actual_half_norm_capture_certified'],
  enrichment_trial_name='q220',response_source_count_unchanged=8,trial_addition_ready_for_mixed_rows=True,one_witness_correction=correction,enriched_inverse_evaluated=False,RC219_uniform_obstruction_after_enrichment_evaluated=False,
  accepted_six_source_inverse_width_unchanged='4361/10000',RC216_action_error_gate_unchanged='0.420465',eight_source_inverse_gate_passed=False,
  Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC221: certify q220 mixed/action rows and test the eleven-trial eight-source inverse; keep nominal capture separate from actual residual capture')
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);p.add_argument('--replay',action='store_true');p.add_argument('--prepare-only',action='store_true');args=p.parse_args()
 if args.prepare_only:prepare(args.replay)
 else:
  result=run(args.replay)
  if args.replay:assert result==json.loads(args.output.read_text())
  else:args.output.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
  print('RC220 PASS: q220 complete canonical error',result['complete_actual_canonical_q_action_relative_D_error_norm_upper'],'relative; inverse gate open')
