"""RC225: optimize trial coefficients for the paid inverse enclosure.

The optimizer proposes rational trial maps. The pinned RC224 interval
interface, unchanged canonical action-error ledger, and exact transport
identity decide acceptance; no floating optimization result is a certificate.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,inspect,json,math
import validate_rpb108_rc224_compatible_extended_inverse as parent
p=parent.p;shared=parent.shared;ROOT=Path(__file__).resolve().parents[1]
PINS=dict(parent.PINS)
PINS.update({'certificates/rpb108_rc224_compatible_extended_inverse.json':'33b20d4a9004ad814c0b99081ae9a55265cee78e','certificates/rpb108_rc224_materialized_prefix_interface.json':'75c1232800eb1545af894940dfc098931ff5545a'})
HELPER_PINS=dict(parent.HELPER_PINS)
HELPER_PINS['scripts/validate_rpb108_rc224_compatible_extended_inverse.py']='e759a266d6d232b0bf7a3c9b0446931734394f8d'
def load(reverse=False):
 data={}
 for path,sha in sorted(HELPER_PINS.items(),reverse=reverse):assert p.prev.blob((ROOT/path).read_bytes())==sha,(path,'helper pin')
 for path,sha in sorted(PINS.items(),reverse=reverse):
  raw=(ROOT/path).read_bytes();assert p.prev.blob(raw)==sha,(path,'input pin');data[path]=json.loads(raw)
 get=lambda name:data['certificates/rpb108_rc'+name+'.json']
 base=get('224_compatible_extended_inverse');interface=get('224_materialized_prefix_interface');prior=get('222_shared_tail_error_inverse');refined=get('223_extended_delta_t10_endpoints')
 assert interface['finite_prefix_degree']==65534
 assert interface['complete_column_error_norm_upper']==base['individual_error_decomposition_ledger']['eps']
 assert base['source_D_Gram_lower']==prior['source_D_Gram_lower'] and base['source_D_Gram_upper']==prior['source_D_Gram_upper']
 G=p.mat(base,'source_D_Gram_lower');GH=p.mat(base,'source_D_Gram_upper');Gc=p.mat(get('221_eleven_trial_inverse'),'RC217_comparison_Gram_floor');a=F(32125,230953)
 EH=p.scale(F(prior['smoothing_squared_upper_512'])/F(prior['D_metric_floor_lower']),p.mat(prior,'high_physical_input_Gram_upper'))
 EL=F(prior['smoothing_squared_upper_128'])/F(prior['D_metric_floor_lower'])*F(prior['delta_low_physical_input_energy_upper']);EC=p.scale(F(1,4),p.mat(refined,'matched_omitted_endpoint_input_D_Gram_upper'))
 return dict(base=base,interface=interface,G=G,GH=GH,Gc=Gc,a=a,EH=EH,EL=EL,EC=EC,eps=list(map(F,base['individual_error_decomposition_ledger']['eps'])),remainder=list(map(F,base['individual_error_decomposition_ledger']['remainder'])))
def propose(st):
 import numpy as np
 from scipy.optimize import minimize
 ar=lambda M:np.array([[float(x) for x in row] for row in M]);sym=lambda M:(M+M.T)/2
 def whitening(A):
  s=np.diag(1/np.sqrt(np.diag(A)));L=np.linalg.cholesky(sym(s@A@s));return s@np.linalg.inv(L).T
 base=st['base'];interface=st['interface'];t=next(x for x in base['evaluated_trials'] if x['trial']==base['selected_trial']);Y0=ar(p.mat(t,'trial_coefficients'));WG=whitening(ar(st['G']));Wi=np.linalg.inv(WG)
 mat=lambda k:ar(p.mat(interface,k));GG=(mat('source_Gram_entry_lower')+mat('source_Gram_entry_upper'))/2;BB=(mat('nominal_source_action_entry_lower')+mat('nominal_source_action_entry_upper'))/2;AA=(mat('nominal_action_Gram_entry_lower')+mat('nominal_action_Gram_entry_upper'))/2
 R=whitening(AA);Z0=np.linalg.solve(R,Y0@WG);keep=[0,1,2,3,4,6,8,9];S=np.eye(11)[:,keep]@WG
 GTL=mat('full_source_Gram_lower');GTH=mat('full_source_Gram_upper');ST=mat('source_tail_Gram_upper');g=WG.T@ar(st['G'])@WG;gh=WG.T@ar(st['GH'])@WG
 sl=np.array(list(map(float,map(F,interface['source_tail_signed_leading_coefficients']))));sd=np.array(list(map(float,map(F,interface['source_tail_nonleading_absolute_bounds']))));vl=np.array(list(map(float,map(F,interface['action_tail_signed_leading_coefficients']))));vd=np.array(list(map(float,map(F,interface['action_tail_nonleading_absolute_bounds']))));T=float(F(interface['common_eta_tail_D_energy_upper']));a=float(st['a']);rem=np.array(list(map(float,st['remainder'])))
 EH,EL,EC=ar(st['EH']),float(st['EL']),ar(st['EC']);slead=sl@S
 sourcevectors=S[[i for i in range(11) if sd[i]>0]];sourceradii=sd[sd>0]
 def envelope(vectors,radii):
  norm=np.linalg.norm(vectors,axis=1);w=1/np.maximum(norm,1e-100);factor=(radii/w).sum();return (vectors.T*(factor*radii*w))@vectors
 def objective(z):
  Y=R@(Z0+z[:88].reshape(11,8));l,u,tC,tW=map(math.exp,z[88:92]);lam=list(np.exp(z[92:95]))+[1.]
  cross=S.T@BB@Y;N=sym(S.T@GG@S-cross-cross.T+Y.T@AA@Y);X=sym(Y.T@GG@S-Y.T@BB@Y)
  lead=slead-vl@Y;Q=envelope(np.vstack([sourcevectors,Y]),np.concatenate([sourceradii,vd]));RT=1.5*T*np.outer(lead,lead)+3*T*Q;NH=N+RT
  UT=Y.T@ST@Y;UG=Y.T@GTH@Y;j=S-Y;SUlo=.5*(g+Y.T@GTL@Y-j.T@GTH@j);SUhi=.5*(gh+UG-j.T@GTL@j)
  parts=[Y[shared.REG].T@EH@Y[shared.REG],EL*np.outer(Y[8],Y[8]),Y[shared.END].T@EC@Y[shared.END],envelope(Y,rem)]
  E=sum(1/x for x in lam)*sum(x*A for x,A in zip(lam,parts));C=tC*UT+RT/(4*tC);V=tW*UT+RT/(4*tW);co=2/a
  WL=UG+NH+2*X+2*V;WH=UG+co*co*NH+2*co*X+2*co*V
  gap=SUhi-SUlo+NH/a-N/2+2*C+l*WL+u*WH+(1/a+1/(4*u)+1/(4*l)-.5)*E
  return float(np.linalg.eigvalsh(sym(gap))[-1])
 pp=t['selected_enclosure']['proposal'];z=np.zeros(95);z[88:92]=[math.log(float(F(pp[k]))) for k in ['lower_theta','upper_theta','variational_tail_theta','cross_tail_theta']];z[92:95]=[math.log(float(F(x))) for x in pp['weights'][11:14]]
 print('RC225 numerical proposal initial objective',objective(z),flush=True)
 bounds=[(-.3,.3)]*88+[(-18,math.log(.5)),(-18,3),(-7,7),(-7,7)]+[(-10,10)]*3
 result=minimize(objective,z,method='L-BFGS-B',bounds=bounds,options={'maxiter':400,'maxfun':50000,'ftol':1e-11,'gtol':1e-7,'maxls':30});z=result.x
 print('RC225 numerical proposal final objective',objective(z),'iterations',result.nit,'success',result.success,flush=True)
 Y=R@(Z0+z[:88].reshape(11,8))@Wi
 return [[p.down(F(float(x)),10**30) for x in row] for row in Y],dict(fixed_trial_at_optimized_parameters_objective=objective(np.concatenate([np.zeros(88),z[88:]])),final_objective=objective(z),iterations=int(result.nit),optimizer_success=bool(result.success))
def run(reverse=False,saved=None):
 st=load(reverse);base=st['base'];G,GH,Gc,a=[st[k] for k in ['G','GH','Gc','a']]
 if saved:Y=p.mat(saved,'optimized_trial_coefficients');diagnostic=saved['numerical_proposal_diagnostic']
 else:Y,diagnostic=propose(st)
 ctx=parent.context(st['interface'],Y,G,GH);parts=[p.cong([Y[i] for i in shared.REG],st['EH']),p.scale(st['EL'],p.outer(Y[8])),p.cong([Y[i] for i in shared.END],st['EC'])]
 _,weights=p.envelope(Y,st['remainder'],G);ps=saved['rational_parameter_proposals'] if saved else shared.optimize(ctx,Y,st['remainder'],G,a,weights,parts)
 ns=dict(vars(p));ns['error_matrix']=lambda YY,ee,w:shared.shared_error(YY,st['remainder'],w,parts);src=inspect.getsource(p.transport).replace('inherited_RC217','inherited_RC224');exec(compile(src,'RC225 pinned paid coupled identity','exec'),ns)
 previous=base['selected_enclosure'];chosen=ns['transport'](ctx,Y,st['eps'],G,GH,Gc,a,ps,p.mat(previous,'inverse_response_lower'),p.mat(previous,'inverse_response_upper'),reverse)
 return dict(milestone='RC225',starting_commit='2c9970be8a51d531733768ecd330899c1f03afb2',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,optimized_trial_coefficients=p.ser(Y),numerical_proposal_diagnostic=diagnostic,rational_parameter_proposals=ps,context={k:p.ser(v) for k,v in ctx.items()},fixed_trial_error_components=[p.ser(v) for v in parts],selected_enclosure=chosen,relative_inverse_width_upper=chosen['relative_inverse_width_upper'],canonical_half_Gram_inverse_width_gate_passed=chosen['half_Gram_gate_passed'],previous_eight_source_inverse_width_upper=base['relative_inverse_width_upper'],nominal_residual_relative_Gram_upper=str(p.certified_width(ctx['Nhi'],G)),complete_shared_trial_error_relative_Gram_upper=str(p.certified_width(p.mat(chosen,'action_error_Gram_upper'),G)),response_source_count=8,inverse_trial_count=11,conditioned_response_source_order=base['conditioned_response_source_order'],raw_trial_order=base['raw_trial_order'],source_D_Gram_lower=p.ser(G),source_D_Gram_upper=p.ser(GH),source_and_action_centers_unchanged=True,all_actual_errors_and_tails_paid=True,numerical_optimization_only_proposes_rational_trials=True,accepted_six_source_inverse_width_unchanged='4361/10000',RC216_action_error_gate_unchanged='0.420465',Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC226: refine the remaining certified residual/action error payment or enrich the trial span; source-range and odd-sector coverage remain separate obligations')
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--replay',action='store_true');args=ap.parse_args();expected=json.loads(args.output.read_text()) if args.replay else None
 result=run(args.replay,expected)
 if args.replay:assert result==expected
 else:args.output.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
 print('RC225 PASS: paid optimized-trial inverse width',result['relative_inverse_width_upper'],'gate',result['canonical_half_Gram_inverse_width_gate_passed'],flush=True)
