"""RC222: shared R and centered C omitted-input payments in the fixed 11-trial inverse."""
from pathlib import Path
from fractions import Fraction as F
import argparse,inspect,json,math
import validate_rpb108_rc221_eleven_trial_inverse as parent
from validate_rpb108_rc127_enriched_even_endpoint_action import B,Z,rat,plus,mul,div,bounds,down,up,sqrtup,psd,ser,loewner
from validate_rpb108_rc134_correlated_six_input_covariance import smul
from validate_rpb108_rc176_f0_regular_output_carrier import root
p=parent.p;ROOT=Path(__file__).resolve().parents[1]
PINS=dict(parent.PINS)
PINS.update({'certificates/rpb108_rc221_eleven_trial_inverse.json':'efb1c115a14d53df182f9af1f4f07f3e00551699','certificates/rpb108_rc221_materialized_prefix_interface.json':'574faed53b7538fb5965bbe22d8343632007d1cb'})
HELPER_PINS=dict(parent.HELPER_PINS)
HELPER_PINS['scripts/validate_rpb108_rc221_eleven_trial_inverse.py']='0e1ced2dcadd1c167bd52a6deae837f6a6becf4e'
REG=[2,3,4,6,8,9];END=[3,4,6,8,9]
def assembly(reverse=False):
 for path,sha in sorted(HELPER_PINS.items(),reverse=reverse):assert p.prev.blob((ROOT/path).read_bytes())==sha,(path,'helper pin')
 data={}
 for path,sha in sorted(PINS.items(),reverse=reverse):
  raw=(ROOT/path).read_bytes();assert p.prev.blob(raw)==sha,(path,'input pin');data[path]=json.loads(raw)
 get=lambda n:data['certificates/rpb108_rc'+n+'.json']
 base=get('221_eleven_trial_inverse');interface=get('221_materialized_prefix_interface');native=get('218_materialized_native_carriers');st=parent.parent.prepare(reverse)
 assert get('193_extended_f0_regular_action')['regular_input_degree']==get('190_extended_w14_endpoint_action')['retained_regular_input_degree']==get('197_native_v10_canonical_action')['finite_action_input_degree']==512
 assert get('181_psi_action_completion_dashboard')['first_actual_psi_degree']==990 and get('181_psi_action_completion_dashboard')['regular_psi_trial'].startswith('zero')
 assert get('214_correlated_difference_canonical_action')['regular_input_prefix_degree']==128 and get('216_refined_t10_canonical_action')['regular_input_prefix_degree']==512
 for name in ['188_extended_psi_endpoint_action','190_extended_w14_endpoint_action','200_extended_v10_endpoint_action']:assert get(name)['source_prefix_degree']==32766
 for name in ['214_correlated_difference_canonical_action','216_refined_t10_canonical_action']:assert get(name)['endpoint_input_prefix_degree']==4094
 O=interface['finite_prefix_degree'];assert O==65534
 sources=[st['gw'],st['gv'],st['dv'],st['tv']];cuts=[4094,8190,8190,16382]
 moments=[st['wc']['analytic_moment_centers'],st['vcert']['native_analytic_moments'],native['delta_analytic_moments'],native['t10_analytic_moments']]
 lambdas=list(map(F,[st['wc']['analytic_lambda'],st['vcert']['native_analytic_lambda'],native['delta_analytic_lambda'],native['t10_analytic_lambda']]))
 coeff=[[rat(F(x)) for x in row] for row in moments]
 H=[Z]
 for n in range(1,O+3):H.append(plus(H[-1],rat(F(1,n))))
 D={n:(plus(H[n],rat(st['sl']))[0],plus(H[n],rat(st['sh']))[1]) for n in range(0,O+3,2)}
 rr=[[Z]*6 for _ in range(6)];cc=[[Z]*5 for _ in range(5)];low=Z
 degrees=list(range(130,O+1,2));degrees=degrees[::-1] if reverse else degrees
 for n in degrees:
  ell=n*(n+1);eta=div(rat(F(2*n+1,ell)),D[n]);v=[]
  for k in range(4):v.append(rat(sources[k][n]) if n<=cuts[k] else smul(eta,parent.horner(coeff[k],rat(lambdas[k]/ell))))
  us=[eta if n<=988 else Z,eta if n>=990 else Z]+v
  phys=rat(2*B/F(2*n+1));mass=mul(phys,D[n])
  if n<=512:low=plus(low,smul(phys,smul(v[2],v[2])))
  else:
   for i in range(6):
    for j in range(i,6):rr[i][j]=plus(rr[i][j],smul(phys,smul(us[i],us[j])))
  if n>=4096:
   masked=[us[1] if n>=32768 else Z,v[0] if n>=32768 else Z,v[1] if n>=32768 else Z,v[2],v[3]]
   for i in range(5):
    for j in range(i,5):cc[i][j]=plus(cc[i][j],smul(mass,smul(masked[i],masked[j])))
  if n%8192==0:print('RC222 shared input Gram prefix',n,flush=True)
 def matrix(A):
  n=len(A);L=[[F(0)]*n for _ in range(n)];U=[[F(0)]*n for _ in range(n)]
  for i in range(n):
   for j in range(i,n):L[i][j],U[i][j]=bounds(A[i][j]);L[j][i]=L[i][j];U[j][i]=U[i][j]
  _,hi,_=loewner(L,U,[F(1)]*n);return hi
 high=matrix(rr);end=matrix(cc);lowUpper=bounds(low)[1]
 z=(O+2)*(O+3);dl=F(D[O][0]);Tphys=up(B/(dl*dl*(O-1)*O))
 leading=[F(0),F(1)]+[F(row[0]) for row in moments]
 rem=[F(0),F(0)]+[sum(abs(F(x))*F(lambdas[k],z)**j for j,x in enumerate(row) if j) for k,row in enumerate(moments)]
 physicalTail=p.add(p.scale(2*Tphys,p.outer(leading)),[[8*Tphys*rem[i]**2 if i==j else F(0) for j in range(6)] for i in range(6)])
 high=p.add(high,physicalTail)
 sourceTail=p.mat(interface,'source_tail_Gram_upper');endTail=[[sourceTail[i][j] for j in END] for i in END];end=p.add(end,endTail)
 regular=get('170_poisson_regular_action');e=F(regular['e_upper']);pi=F(regular['pi_upper']);I2=up(e*pi*pi/3);r=F(789,125)
 phi=lambda M:up(min(r*r,4*B*I2*up(F(11,12)**(2*(M+1)),10**80)+e*e/(F(M+1)/(6*pi*B))**2))
 phi128=phi(128);phi512=phi(512);dc=get('214_correlated_difference_canonical_action');tc=get('216_refined_t10_canonical_action')
 assert phi128==F(dc['regular_high_input_smoothing_squared_factor_upper']) and phi512==F(tc['regular_high_input_smoothing_squared_factor_upper'])
 EHraw=p.scale(phi512/st['sl'],high);ELscalar=phi128/st['sl']*lowUpper;ECraw=p.scale(F(1,4),end)
 eps=list(map(F,interface['complete_column_error_norm_upper']));removedR=[F(0)]*11;removedC=[F(0)]*11
 completeKeys=[('193_extended_f0_regular_action','canonical_f0_trial_D_error_norm_upper'),('188_extended_psi_endpoint_action','canonical_psi_source_form_full_D_error_norm_upper'),('190_extended_w14_endpoint_action','complete_canonical_w14_action_D_error_norm_upper'),('200_extended_v10_endpoint_action','complete_canonical_v10_action_D_error_norm_upper'),('214_correlated_difference_canonical_action','complete_canonical_delta_action_D_error_norm_upper'),('216_refined_t10_canonical_action','complete_canonical_t10_action_D_error_norm_upper')]
 for i,(name,key) in zip(REG,completeKeys):assert eps[i]==F(get(name)[key])
 rdata=[('193_extended_f0_regular_action','regular_input_tail_D_action_error_norm_upper'),('181_psi_action_completion_dashboard','complete_actual_D_inverse_Rpsi_error_norm_upper'),('190_extended_w14_endpoint_action','regular_input_tail_action_D_error_norm_upper'),('197_native_v10_canonical_action','regular_input_tail_D_error_norm_upper'),('214_correlated_difference_canonical_action','regular_omitted_input_D_action_error_norm_upper'),('216_refined_t10_canonical_action','regular_omitted_input_D_action_error_norm_upper')]
 for i,(name,key) in zip(REG,rdata):removedR[i]=F(get(name)[key])
 cdata=[('188_extended_psi_endpoint_action','input_tail_D_energy_upper'),('190_extended_w14_endpoint_action','input_w14_tail_D_energy_upper'),('200_extended_v10_endpoint_action','native_input_tail_D_energy_upper'),('214_correlated_difference_canonical_action','omitted_native_endpoint_input_D_energy_upper'),('216_refined_t10_canonical_action','omitted_native_endpoint_input_D_energy_upper')]
 for i,(name,key) in zip(END,cdata):removedC[i]=(sqrtup(F(get(name)[key])) if i in [3,4,6] else root(F(get(name)[key])))/2
 remainder=[eps[i]-removedR[i]-removedC[i] for i in range(11)];assert min(remainder)>=0
 for A in [EHraw,ECraw,physicalTail,endTail]:assert psd(A)
 return dict(base=base,interface=interface,regular_high_action_Gram_upper=EHraw,regular_delta_low_action_squared_error_upper=ELscalar,centered_endpoint_action_Gram_upper=ECraw,
  high_physical_input_Gram_upper=high,high_physical_tail_Gram_upper=physicalTail,masked_endpoint_input_D_Gram_upper=end,masked_endpoint_infinite_input_D_Gram_upper=endTail,
  delta_low_physical_input_energy_upper=lowUpper,high_physical_eta_tail_energy_upper=Tphys,phi128=phi128,phi512=phi512,sl=st['sl'],eps=eps,removedR=removedR,removedC=removedC,remainder=remainder)
def remainder_error(Y,eps,w):
 assert len(w)==len(eps)==len(Y)==11 and min(w)>0
 factor=sum(eps[i]/w[i] for i in range(11));D=[[factor*eps[i]*w[i] if i==j else F(0) for j in range(11)] for i in range(11)]
 assert psd(p.add(D,p.outer(eps),-1));return p.cong(Y,D)
def shared_error(Y,remainder,w,parts):
 assert len(w)==14 and min(w)>0
 lambdas=w[11:]+[F(1)];allparts=parts+[remainder_error(Y,remainder,w[:11])]
 total=p.zeros(8);factor=sum(1/x for x in lambdas)
 for lam,A in zip(lambdas,allparts):total=p.add(total,p.scale(factor*lam,A))
 assert psd(total);return total
def optimize(ctx,Y,remainder,G,a,weights,parts):
 import numpy as np
 from scipy.optimize import minimize
 ar=lambda M:np.array([[float(x) for x in row] for row in M]);g=ar(G);s=np.diag(1/np.sqrt(np.diag(g)));L=np.linalg.cholesky(s@g@s);W=s@np.linalg.inv(L).T
 wh=lambda A:W.T@ar(A)@W
 UG,N,X,UT,RT,gap=map(wh,[ctx['UGhi'],ctx['Nhi'],ctx['Xhi'],ctx['Utail'],ctx['Rtail'],p.add(ctx['baseHi'],ctx['baseLo'],-1)])
 NL=wh(ctx['Nlo']);parts=list(map(wh,parts));y=ar(Y)@W;es=np.array(list(map(float,remainder)));ws=np.array(list(map(float,weights)))
 def objective(z):
  w=ws*np.exp(z[:11]);lam=list(np.exp(z[11:14]))+[1.];l,u,tC,tW=map(math.exp,z[14:]);ER=(es/w).sum()*((y.T*(es*w))@y)
  E=sum(1/x for x in lam)*sum(x*A for x,A in zip(lam,parts+[ER]));C=tC*UT+RT/(4*tC);V=tW*UT+RT/(4*tW)
  wl=UG+N+2*X+2*V;co=2/float(a);wu=UG+co*co*N+2*co*X+2*co*V
  full=gap+N/float(a)-NL/2+2*C+l*wl+u*wu+(1/float(a)+1/(4*u)+1/(4*l)-.5)*E
  return float(np.linalg.eigvalsh((full+full.T)/2)[-1])
 z=np.array([0.]*14+[math.log(.004),math.log(.003),0.,0.]);bs=[(-4,4)]*11+[(-10,10)]*3+[(-18,math.log(.5)),(-18,3),(-7,7),(-7,7)];out=[]
 def record(z,label):
  w=[max(F(1,10**24),down(F(float(ws[i]*math.exp(z[i]))),10**24)) for i in range(11)]+[max(F(1,10**24),down(F(math.exp(v)),10**24)) for v in z[11:14]]
  pars=[max(F(1,10**12),down(F(math.exp(v)),10**12)) for v in z[14:]];pars[0]=min(F(1,2),pars[0])
  out.append(dict(label=label,weights=list(map(str,w)),lower_theta=str(pars[0]),upper_theta=str(pars[1]),variational_tail_theta=str(pars[2]),cross_tail_theta=str(pars[3])))
 record(z,'initial')
 for method in ['Powell','SLSQP']:
  result=minimize(objective,z,method=method,bounds=bs,options={'maxiter':600,'ftol':1e-10});z=result.x;record(z,method);print('RC222 proposal',method,objective(z),flush=True)
 return out
def run(reverse=False,proposals=None):
 state=assembly(reverse);base=state['base'];t=next(x for x in base['evaluated_trials'] if x['trial']=='least_residual_11');Y=p.mat(t,'trial_coefficients');G=p.mat(base,'source_D_Gram_lower');GH=p.mat(base,'source_D_Gram_upper');Gc=p.mat(base,'RC217_comparison_Gram_floor');a=F(32125,230953)
 keys={'UGhi':'trial_source_Gram_upper','Nlo':'nominal_residual_Gram_lower','Nhi':'nominal_residual_Gram_upper','Xlo':'finite_trial_residual_cross_lower','Xhi':'finite_trial_residual_cross_upper','Utail':'trial_source_tail_Gram_upper','Rtail':'nominal_residual_tail_Gram_upper','baseLo':'base_variational_lower','baseHi':'base_variational_upper'};ctx={k:p.mat(t,v) for k,v in keys.items()}
 EH=p.cong([Y[i] for i in REG],state['regular_high_action_Gram_upper']);EL=p.scale(state['regular_delta_low_action_squared_error_upper'],p.outer(Y[8]));EC=p.cong([Y[i] for i in END],state['centered_endpoint_action_Gram_upper']);parts=[EH,EL,EC]
 _,weights=p.envelope(Y,state['remainder'],G);ps=proposals if proposals else optimize(ctx,Y,state['remainder'],G,a,weights,parts)
 ns=dict(vars(p));ns['error_matrix']=lambda YY,eps,w:shared_error(YY,state['remainder'],w,parts)
 src=inspect.getsource(p.transport).replace('inherited_RC217','inherited_RC221');exec(compile(src,'RC222 pinned coupled identity with shared input-error Gram','exec'),ns)
 previous=base['selected_enclosure'];chosen=ns['transport'](ctx,Y,state['eps'],G,GH,Gc,a,ps,p.mat(previous,'inverse_response_lower'),p.mat(previous,'inverse_response_upper'),reverse)
 error=p.mat(chosen,'action_error_Gram_upper');betaE=p.certified_width(error,G)
 ER=remainder_error(Y,state['remainder'],list(map(F,chosen['proposal']['weights']))[:11])
 componentWidths={name:str(p.certified_width(A,G)) for name,A in zip(['regular_high','regular_delta_low','centered_endpoint','remainder'],parts+[ER])}
 # An obstruction to this PAYMENT MODEL, not a lower bound on actual error:
 # every four-component Young sum is >= EC. The two-sided coupled gap is
 # >= E/a whenever its other required matrix terms are positive semidefinite.
 assert psd(p.add(ctx['baseHi'],ctx['baseLo'],-1)) and psd(p.add(ctx['Nhi'],ctx['Nlo'],-1))
 assert psd(p.add(error,EC,-1))
 Gi=p.inv(G);probes=[]
 for k in range(8):
  v=[sum(Gi[i][j]*EC[j][k] for j in range(8)) for i in range(8)];size=max(map(abs,v))
  if not size:continue
  v=[down(x/size,10**9) for x in v];qG=sum(v[i]*G[i][j]*v[j] for i in range(8) for j in range(8));qC=sum(v[i]*EC[i][j]*v[j] for i in range(8) for j in range(8))
  assert qG>0;probes.append((qC/(a*qG),k,v,qG,qC))
 floor,k,probe,qG,qC=max(probes,key=lambda x:(x[0],-x[1]));floor=down(floor,10**6);assert floor>F(1,2) and qC/a>=floor*qG
 paymentAudit=dict(component_relative_error_Gram_upper=componentWidths,probe_coefficients=list(map(str,probe)),probe_source_reference_energy=str(qG),probe_centered_endpoint_payment_energy=str(qC),
  two_sided_coupled_endpoint_payment_model_width_floor_lower=str(floor),endpoint_payment_model_floor_exceeds_half=True,
  scope='Fixed RC221 least_residual_11 trial map and this four-component upper-error payment model, for admissible two-sided coupled endpoints; mixed structural endpoints and other error models are not excluded.',
  true_operator_error_lower_bound_claimed=False,actual_inverse_failure_claimed=False)
 ledger={k:list(map(str,state[k])) for k in ['eps','removedR','removedC','remainder']}
 return dict(milestone='RC222',starting_commit='10ea35bd0aa320ee4c55657a7fcdf5826217df62',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,raw_trial_order=base['raw_trial_order'],conditioned_response_source_order=base['conditioned_response_source_order'],response_source_count=8,inverse_trial_count=11,
  source_D_Gram_lower=ser(G),source_D_Gram_upper=ser(GH),source_and_action_centers_unchanged=True,source_normalization_unchanged=True,
  regular_high_input_first_degree=514,regular_delta_low_input_band=[130,512],endpoint_input_first_degrees=dict(zip(['psi0','w14','v10','delta','t10'],[32768,32768,32768,4096,4096])),finite_prefix_degree=65534,
  high_physical_input_Gram_upper=ser(state['high_physical_input_Gram_upper']),high_physical_tail_Gram_upper=ser(state['high_physical_tail_Gram_upper']),masked_endpoint_input_D_Gram_upper=ser(state['masked_endpoint_input_D_Gram_upper']),masked_endpoint_infinite_input_D_Gram_upper=ser(state['masked_endpoint_infinite_input_D_Gram_upper']),
  delta_low_physical_input_energy_upper=str(state['delta_low_physical_input_energy_upper']),high_physical_eta_tail_energy_upper=str(state['high_physical_eta_tail_energy_upper']),smoothing_squared_upper_128=str(state['phi128']),smoothing_squared_upper_512=str(state['phi512']),D_metric_floor_lower=str(state['sl']),
  individual_error_decomposition_ledger=ledger,fixed_trial_regular_high_error_Gram_upper=ser(EH),fixed_trial_regular_delta_low_error_Gram_upper=ser(EL),fixed_trial_centered_endpoint_error_Gram_upper=ser(EC),
  error_parameter_schema='weights[0:11]: remaining-column triangle weights; weights[11:14]: high-R, low-R, centered-C component Young weights; remainder component weight=1',
  rational_parameter_proposals=ps,selected_enclosure=chosen,relative_inverse_width_upper=chosen['relative_inverse_width_upper'],relative_width_on_RC217_Gram_floor=chosen['relative_width_on_RC217_Gram_floor'],complete_shared_trial_error_relative_Gram_upper=str(betaE),canonical_half_Gram_inverse_width_gate_passed=chosen['half_Gram_gate_passed'],previous_eight_source_inverse_width_upper=base['relative_inverse_width_upper'],
  shared_component_payment_audit=paymentAudit,
  no_actual_error_radii_artificially_zeroed=True,common_operator_applied_after_signed_input_combination=True,output_error_orthogonality_not_assumed=True,all_rounding_projection_and_infinite_tails_paid=True,endpoint_cutoff_commutation_not_assumed=True,
  accepted_six_source_inverse_width_unchanged='4361/10000',RC216_action_error_gate_unchanged='0.420465',Stage_I_closed=False,RH=False,F4=False,Lean=False,
  next_cursor='RC223: refine or explicitly realize the shared centered-endpoint omitted inputs, especially delta/t10 currently truncated at 4094 versus 32766 for psi/w14/v10; parameter tuning alone cannot clear the fixed two-sided endpoint payment model. Actual inverse acceptance and Stage I remain open')
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--replay',action='store_true');args=ap.parse_args();expected=json.loads(args.output.read_text()) if args.replay else None
 result=run(args.replay,expected['rational_parameter_proposals'] if expected else None)
 if args.replay:assert result==expected
 else:args.output.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
 print('RC222 PASS: shared-input inverse width',result['relative_inverse_width_upper'],'actual gate',result['canonical_half_Gram_inverse_width_gate_passed'])
