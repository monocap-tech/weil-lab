"""RC223: signed extended C-delta/C-t10 carriers, with all omitted inputs paid.

Three base-2^16 limbs permit exact NumPy int64 dot products for a 48-bit
input quantization and a 40-bit kernel. Final reconstruction uses Python
integers. Every limb's absolute dot-sum is bounded before arithmetic.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
import numpy as np
import validate_rpb108_rc222_shared_tail_error_inverse as prev
from validate_rpb108_rc127_enriched_even_endpoint_action import B,Z,rat,plus,minus,mul,div,bounds,down,up,sqrtup,psd,ser,loewner
from validate_rpb108_rc134_correlated_six_input_covariance import smul
p=prev.p;ROOT=Path(__file__).resolve().parents[1]
PINS=dict(prev.PINS)
PINS['certificates/rpb108_rc222_shared_tail_error_inverse.json']='dc3ad1a6d25707d123f212b1fca0410809450975'
HELPER_PINS=dict(prev.HELPER_PINS)
HELPER_PINS['scripts/validate_rpb108_rc222_shared_tail_error_inverse.py']='e32e9a6735e95e33f68acced5019d0462b5488ca'
def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def run(reverse=False):
 for path,sha in sorted(HELPER_PINS.items(),reverse=reverse):assert p.prev.blob((ROOT/path).read_bytes())==sha,(path,'helper pin')
 data={}
 for path,sha in sorted(PINS.items(),reverse=reverse):
  raw=(ROOT/path).read_bytes();assert p.prev.blob(raw)==sha,(path,'input pin');data[path]=json.loads(raw)
 get=lambda n:data['certificates/rpb108_rc'+n+'.json']
 native=get('218_materialized_native_carriers');interface=get('221_materialized_prefix_interface');base=get('222_shared_tail_error_inverse');joint=get('129_four_vector_joint_moment')
 L=32766;O=65534;K=24;S=2**48;Q=2**40;LIMB=2**16;CENTER=10**40
 sl=F(joint['actual_D_Gram_entry_lower'][0][0])/(2*B);sh=F(joint['actual_D_Gram_entry_upper'][0][0])/(2*B)
 log=(rat(1-F(joint['actual_endpoint_pairing_entry_upper'][0][0])/(2*B))[0],rat(1-F(joint['actual_endpoint_pairing_entry_lower'][0][0])/(2*B))[1])
 H=[Z]
 for n in range(1,2*O+1):H.append(plus(H[-1],rat(F(1,n))))
 D={n:(plus(H[n],rat(sl))[0],plus(H[n],rat(sh))[1]) for n in range(0,O+1,2)}
 diag={n:minus(plus(minus(mul(rat(2),H[2*n]),mul(rat(2),H[n])),rat(F(1,2*n+1))),log) for n in D}
 assert min(bounds(x)[0] for x in diag.values())>0
 source=[{r['degree']:F(r['center']) for r in native['delta_finite_rows']},{r['degree']:F(r['center']) for r in native['t10_finite_center_radius_rows']}]
 moments=[list(map(F,native['delta_analytic_moments'])),list(map(F,native['t10_analytic_moments']))];nlambda=list(map(F,[native['delta_analytic_lambda'],native['t10_analytic_lambda']]))
 coeff=[[rat(x) for x in row] for row in moments];cuts=[8190,16382]
 jobs=list(range(0,L+1,2));walk=jobs[::-1] if reverse else jobs;alpha=[{},{}];inputEnergy=[F(0),F(0)]
 for n in walk:
  for k in range(2):
   value=rat(source[k][n]) if n<=cuts[k] else smul(div(rat(F(2*n+1,n*(n+1))),D[n]),prev.parent.horner(coeff[k],rat(nlambda[k]/(n*(n+1)))))
   lo,hi=bounds(value);integer=int(down((lo+hi)/2,S)*S);alpha[k][n]=integer;radius=max(abs(F(integer,S)-lo),abs(hi-F(integer,S)))
   inputEnergy[k]+=up(2*B/F(2*n+1)*F(D[n][1])*radius*radius,10**80)
 # Each signed input integer is represented exactly by two nonnegative low
 # limbs and one signed high limb; this also handles negative floor values.
 bank=[];guards=[];hn=sum(F(1,j) for j in range(1,len(jobs)+1));maxDiag=max(bounds(x)[1] for x in diag.values())
 for k in range(2):
  rows=[[],[],[]]
  for n in walk:
   a=alpha[k][n];v=[a%LIMB,(a//LIMB)%LIMB,a//(LIMB**2)]
   assert a==sum(v[j]*LIMB**j for j in range(3)) and abs(a)<2**63
   for j in range(3):rows[j].append(v[j])
  for row in rows:
   guard=up(max(map(abs,row))*Q*(maxDiag+2*hn));assert guard<2**63;guards.append(guard)
  bank.extend(rows)
 assert (2*O+1)*Q<2**63 and O*(O+L+1)<2**63
 ms=np.array(walk,dtype=np.int64);av=np.array(bank,dtype=np.int64);inputAbs=[F(sum(abs(v) for v in a.values()),S) for a in alpha]
 centers=[[None]*(O//2+1) for _ in range(2)];dots=[[None]*(O//2+1) for _ in range(2)];rounding=[F(0),F(0)]
 # The same output loop also constructs the source-only endpoint tail budget
 # after all five endpoint input cutoffs have been aligned at L.
 wm=list(map(F,get('183_materialized_w14_canonical_carrier')['analytic_moment_centers']));vm=list(map(F,get('197_native_v10_canonical_action')['native_analytic_moments']))
 allmom=[wm,vm]+moments;alllam=[F(get('183_materialized_w14_canonical_carrier')['analytic_lambda']),F(get('197_native_v10_canonical_action')['native_analytic_lambda'])]+nlambda
 allcoeff=[[rat(x) for x in row] for row in allmom];gg=[[Z]*5 for _ in range(5)]
 for n in (range(O,-1,-2) if reverse else range(0,O+1,2)):
  den=np.abs(n-ms)*(n+ms+1);den[ms==n]=1;kernel=((2*n+1)*Q)//den;dlo,dhi=bounds(diag[n]);kernel[ms==n]=int(down(dlo,Q)*Q);assert kernel.min()>=0
  limbDots=np.sum(av*kernel,axis=1,dtype=np.int64)
  for j,dot in enumerate(limbDots):assert abs(int(dot))<=guards[j]
  for k in range(2):
   dot=sum(int(limbDots[3*k+j])*LIMB**j for j in range(3));dots[k][n//2]=str(dot)
   centerNumerator=F(dot,S*Q);error=inputAbs[k]/Q+F(abs(alpha[k].get(n,0)),S)*(dhi-dlo)
   value=(rat(centerNumerator-error)[0],rat(centerNumerator+error)[1]);value=smul(value,div(rat(1),D[n]))
   lo,hi=bounds(value);cc=down((lo+hi)/2,CENTER);radius=max(cc-lo,hi-cc);centers[k][n//2]=str(int(cc*CENTER))
   rounding[k]+=up(2*B/F(2*n+1)*F(D[n][1])*radius*radius,10**80)
  if n>=L+2:
   eta=div(rat(F(2*n+1,n*(n+1))),D[n]);us=[eta]+[smul(eta,prev.parent.horner(allcoeff[k],rat(alllam[k]/(n*(n+1))))) for k in range(4)];mass=mul(rat(2*B/F(2*n+1)),D[n])
   for i in range(5):
    for j in range(i,5):gg[i][j]=plus(gg[i][j],smul(mass,smul(us[i],us[j])))
  if n%8192==0:print('RC223 exact signed endpoint output',n,flush=True)
 lam=L*(L+1);rho=F(lam,(O+2)*(O+3));T=up(B/(F(D[O][0])*(O-1)*O));inputEta=up(B/(F(D[L][0])*(L-1)*L));first=(L+2)*(L+3)
 carriers=[];summary=[]
 for k,name in enumerate(['delta','t10']):
  tailmom=[]
  for j in range(K+2):
   exact=F(sum(alpha[k][n]*(n*(n+1))**j for n in jobs),S*lam**j);cc=down(exact,10**40)
   tailmom.append(dict(order=j,exact_signed_coefficient=str(exact),center=str(cc),radius=str(exact-cc)))
  amplitude=sum(abs(x)*F(nlambda[k],first)**j for j,x in enumerate(moments[k]));inputTail=up(inputEta*amplitude*amplitude)
  absoluteMoment=F(sum(abs(alpha[k][n])*(n*(n+1))**(K+1) for n in jobs),S*lam**(K+1))
  remainder=up(T*(absoluteMoment*rho**(K+1)/(1-rho))**2,10**80);momentRound=up(T*sum(F(x['radius'])*rho**j for j,x in enumerate(tailmom[:K+1]))**2,10**80)
  endpoint=up(sqrtup(inputEnergy[k])+sqrtup(rounding[k])+sqrtup(momentRound)+sqrtup(remainder)+sqrtup(inputTail)/2)
  old=get('214_correlated_difference_canonical_action' if k==0 else '216_refined_t10_canonical_action');oldEndpoint=F(old['complete_endpoint_delta_D_error_norm_upper' if k==0 else 'complete_endpoint_t10_D_error_norm_upper']);reg=F(old['complete_D_inverse_Rdelta_error_norm_upper' if k==0 else 'complete_D_inverse_Rt10_error_norm_upper']);complete=up(endpoint+reg)
  oldComplete=F(old['complete_canonical_delta_action_D_error_norm_upper' if k==0 else 'complete_canonical_t10_action_D_error_norm_upper']);assert endpoint<oldEndpoint and complete<oldComplete
  carriers.append(dict(source=name,source_prefix_degree=L,output_prefix_degree=O,finite_center_scale=str(CENTER),finite_C_coefficient_center_numerators=centers[k],analytic_output_lambda=str(lam),analytic_output_moments=tailmom[:K+1],centered_input_tail_first_even_degree=L+2,centered_input_tail_coefficient='1/2 times the unchanged actual native source coefficients',finite_input_scale=str(S),fixed_kernel_scale=str(Q),limb_base=str(LIMB),limb_count=3,input_signed_integer_sha256=digest([str(alpha[k][n]) for n in jobs]),output_exact_integer_dot_sha256=digest(dots[k]),whole_endpoint_D_error_norm_upper=str(endpoint)))
  summary.append(dict(source=name,finite_input_quantization_D_energy_upper=str(inputEnergy[k]),finite_output_rounding_D_energy_upper=str(rounding[k]),analytic_moment_rounding_D_energy_upper=str(momentRound),analytic_geometric_remainder_D_energy_upper=str(remainder),omitted_input_D_energy_upper=str(inputTail),whole_endpoint_D_error_norm_upper=str(endpoint),previous_endpoint_D_error_norm_upper=str(oldEndpoint),endpoint_error_improvement_factor_lower=str(down(oldEndpoint/endpoint)),retained_complete_regular_action_error_norm_upper=str(reg),complete_canonical_action_error_norm_upper=str(complete),previous_complete_canonical_action_error_norm_upper=str(oldComplete),new_radii_apply_only_to_new_centers=True))
 lo=[[F(0)]*5 for _ in range(5)];hi=[[F(0)]*5 for _ in range(5)]
 for i in range(5):
  for j in range(i,5):lo[i][j],hi[i][j]=bounds(gg[i][j]);lo[j][i]=lo[i][j];hi[j][i]=hi[i][j]
 _,prefixHi,_=loewner(lo,hi,[F(1)]*5);idx=[3,4,6,8,9];oldTail=p.mat(interface,'source_tail_Gram_upper');tail=[[oldTail[i][j] for j in idx] for i in idx];matched=p.add(prefixHi,tail);ECraw=p.scale(F(1,4),matched)
 oldtrial=next(x for x in get('221_eleven_trial_inverse')['evaluated_trials'] if x['trial']=='least_residual_11');Y=p.mat(oldtrial,'trial_coefficients');G=p.mat(base,'source_D_Gram_lower');EC=p.cong([Y[i] for i in idx],ECraw);beta=p.certified_width(EC,G);assert psd(matched) and psd(EC)
 oldEC=p.mat(base,'fixed_trial_centered_endpoint_error_Gram_upper');oldBeta=F(base['shared_component_payment_audit']['component_relative_error_Gram_upper']['centered_endpoint']);assert beta<oldBeta
 carrier=dict(milestone='RC223-endpoint-carriers',carriers=carriers,native_source_definitions_unchanged=True)
 result=dict(milestone='RC223',starting_commit='402fdbe0c5c2df4fe345b90cb91f3b57d9b7bb7c',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,
  endpoint_input_degree=L,endpoint_output_degree=O,input_quantization_bits=48,kernel_quantization_bits=40,limb_bits=16,limb_count=3,integer_limb_dot_absolute_guards=list(map(str,guards)),signed_integer_arithmetic_overflow_ruled_out=True,
  actual_native_source_carriers_unchanged=True,evaluated_endpoint_actions=summary,matched_endpoint_tail_source_order=['psi0','w14','v10','delta','t10'],matched_omitted_endpoint_input_D_Gram_upper=ser(matched),matched_endpoint_infinite_input_D_Gram_upper=ser(tail),matched_fixed_trial_centered_endpoint_error_Gram_upper=ser(EC),
  matched_centered_endpoint_component_relative_Gram_upper=str(beta),previous_centered_endpoint_component_relative_Gram_upper=str(oldBeta),endpoint_component_reduced_on_same_fixed_trial_map=True,
  actual_eight_source_inverse_width_unchanged=base['relative_inverse_width_upper'],new_mixed_action_rows_assembled=False,new_inverse_evaluated=False,new_endpoint_error_radii_not_attached_to_old_centers=True,endpoint_cutoff_commutation_not_assumed=True,all_input_and_output_tails_paid=True,
  response_source_count=8,inverse_trial_count=11,accepted_six_source_inverse_width_unchanged='4361/10000',RC216_action_error_gate_unchanged='0.420465',eight_source_inverse_gate_passed=False,Stage_I_closed=False,RH=False,F4=False,Lean=False,
  next_cursor='RC224: rebuild compatible delta/t10 mixed/action and residual rows with these new endpoint centers, then rerun the shared-error eight-source inverse; do not reuse improved radii with old centers')
 return result,carrier
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--carriers',type=Path,required=True);ap.add_argument('--replay',action='store_true');args=ap.parse_args();result,carrier=run(args.replay)
 if args.replay:assert result==json.loads(args.output.read_text()) and carrier==json.loads(args.carriers.read_text())
 else:
  args.output.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n');args.carriers.write_text(json.dumps(carrier,sort_keys=True,indent=2)+'\n')
 print('RC223 PASS: matched endpoint component',result['matched_centered_endpoint_component_relative_Gram_upper'],'inverse not reevaluated')
