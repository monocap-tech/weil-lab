"""RC226: combine signed trial/residual tails before their Young payments.

For W_c=U+c(s-Ahat U), reconstruct its finite Gram and bound its common-eta
tail directly. This replaces the independent U/R cross-tail envelope in
the unchanged actual inverse identity. All canonical action errors remain.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,inspect,json,math
import validate_rpb108_rc225_paid_trial_optimization as parent
p=parent.p;shared=parent.shared;ROOT=Path(__file__).resolve().parents[1]
PINS=dict(parent.PINS)
PINS['certificates/rpb108_rc225_paid_trial_optimization.json']='750b43592f692c04680ce6a455640f400ec096a4'
HELPER_PINS=dict(parent.HELPER_PINS)
HELPER_PINS['scripts/validate_rpb108_rc225_paid_trial_optimization.py']='4200a50e0fee6893db0ce5d757010ac0890a59fd'
def state(reverse=False):
 for path,sha in sorted(dict(PINS,**HELPER_PINS).items(),reverse=reverse):assert p.prev.blob((ROOT/path).read_bytes())==sha,(path,'immutable pin')
 st=parent.load(reverse);st['previous']=json.loads((ROOT/'certificates/rpb108_rc225_paid_trial_optimization.json').read_text());return st
def envelope(leading,vectors,radii,T,G):
 vectors=[leading]+vectors;radii=[F(1)]+radii
 E,weights=p.envelope(vectors,radii,G)
 # This weighted triangle majorizes every allowed signed pointwise tail.
 D=[[sum(radii[k]/weights[k] for k in range(len(radii)))*radii[i]*weights[i] if i==j else F(0) for j in range(len(radii))] for i in range(len(radii))]
 assert p.psd(p.add(D,p.outer(radii),-1))
 return p.scale(T,E),dict(leading=list(map(str,leading)),nonleading_vectors=p.ser(vectors[1:]),nonleading_absolute_bounds=list(map(str,radii[1:])),positive_triangle_weights=list(map(str,weights)))
def coherent(st,Y):
 interface=st['interface'];G,GH,a=st['G'],st['GH'],st['a'];ctx=parent.parent.context(interface,Y,G,GH);keep=[0,1,2,3,4,6,8,9];S=[[F(i==keep[j]) for j in range(8)] for i in range(11)]
 sl=list(map(F,interface['source_tail_signed_leading_coefficients']));sd=list(map(F,interface['source_tail_nonleading_absolute_bounds']));vl=list(map(F,interface['action_tail_signed_leading_coefficients']));vd=list(map(F,interface['action_tail_nonleading_absolute_bounds']));T=F(interface['common_eta_tail_D_energy_upper'])
 lead=[sl[keep[k]]-sum(vl[i]*Y[i][k] for i in range(11)) for k in range(8)];vectors=[];radii=[]
 for i in range(11):
  if sd[i] and any(S[i]):vectors.append(S[i]);radii.append(sd[i])
  if vd[i] and any(Y[i]):vectors.append(Y[i]);radii.append(vd[i])
 oldTail=ctx['Rtail'];RT,audit=envelope(lead,vectors,radii,T,G);ctx['Rtail']=RT;ctx['Nhi']=p.add(p.add(ctx['Nhi'],oldTail,-1),RT);assert p.psd(RT) and p.psd(ctx['Nhi'])
 iGG=p.imat(p.mat(interface,'source_Gram_entry_lower'),p.mat(interface,'source_Gram_entry_upper'));iBB=p.imat(p.mat(interface,'nominal_source_action_entry_lower'),p.mat(interface,'nominal_source_action_entry_upper'));iAA=p.imat(p.mat(interface,'nominal_action_Gram_entry_lower'),p.mat(interface,'nominal_action_Gram_entry_upper'));iy=p.iconst(Y)
 rows=[]
 for name,c in [('Wlower',F(1)),('Wupper',2/a)]:
  J=p.add(Y,p.scale(c,S));iJ=p.iconst(J);cross=p.iprod(p.iprod(p.trans(iJ),iBB),iy)
  finite=p.iadd(p.iadd(p.iprod(p.iprod(p.trans(iJ),iGG),iJ),[[p.smul(p.rat(c),x) for x in row] for row in p.iadd(cross,p.trans(cross))],-1),[[p.smul(p.rat(c*c),x) for x in row] for row in p.iprod(p.iprod(p.trans(iy),iAA),iy)])
  lo,hi=p.interval_matrix(finite);_,prefix,_=p.loewner(lo,hi,[p.sqrtup(GH[i][i]) for i in range(8)])
  leading=[sum((sl[i]*J[i][k]-c*vl[i]*Y[i][k]) for i in range(11)) for k in range(8)];v=[];r=[]
  for i in range(11):
   if sd[i] and any(J[i]):v.append(J[i]);r.append(sd[i])
   if vd[i] and any(Y[i]):v.append(Y[i]);r.append(c*vd[i])
  tail,ledger=envelope(leading,v,r,T,G);bound=p.add(prefix,tail);assert p.psd(bound) and p.psd(tail)
  ctx[name+'_Gram_upper']=bound;rows.append(dict(name=name,c=str(c),finite_Gram_entry_lower=p.ser(lo),finite_Gram_entry_upper=p.ser(hi),finite_Gram_upper=p.ser(prefix),signed_tail_Gram_upper=p.ser(tail),combined_Gram_upper=p.ser(bound),signed_tail_payment=ledger))
 return ctx,dict(residual_tail_payment=audit,previous_residual_tail_Gram_upper=p.ser(oldTail),coherent_residual_tail_Gram_upper=p.ser(RT),combined_trial_residual_rows=rows)
def optimize(ctx,Y,remainder,G,a,weights,parts):
 src=inspect.getsource(shared.optimize)
 before="NL=wh(ctx['Nlo']);parts=list(map(wh,parts));";assert src.count(before)==1
 src=src.replace(before,"Wlc=wh(ctx['Wlower_Gram_upper']);Wuc=wh(ctx['Wupper_Gram_upper']);"+before)
 before='wl=UG+N+2*X+2*V;co=2/float(a);wu=UG+co*co*N+2*co*X+2*co*V';assert src.count(before)==1;src=src.replace(before,'wl=Wlc;wu=Wuc')
 ns=dict(vars(shared));exec(compile(src,'RC226 paid proposal with coherent W Grams','exec'),ns);return ns['optimize'](ctx,Y,remainder,G,a,weights,parts)
def payment_audit(ctx,EC,G,a,chosen,probe=None):
 # The four-component Young model always has E >= EC. For fixed x,
 # t A + B/(4t) >= sqrt(A B), independently of every positive parameter.
 assert p.psd(EC) and p.psd(p.add(ctx['baseHi'],ctx['baseLo'],-1))
 assert p.psd(p.add(ctx['Nhi'],ctx['Nlo'],-1)) and p.psd(ctx['Nlo'])
 assert p.psd(p.add(p.mat(chosen,'action_error_Gram_upper'),EC,-1))
 B=p.add(p.add(p.add(p.add(ctx['baseHi'],ctx['baseLo'],-1),p.scale(1/a,ctx['Nhi'])),p.scale(F(1,2),ctx['Nlo']),-1),p.scale(1/a-F(1,2),EC))
 bil=lambda x,A:sum(x[i]*A[i][j]*x[j] for i in range(8) for j in range(8))
 def lower_sqrt(q):
  assert q>=0;grid=10**120;v=F(math.isqrt(q.numerator*grid*grid//q.denominator),grid);assert v*v<=q;return v
 def evaluate(x):
  energies={k:bil(x,A) for k,A in dict(source=G,base=B,endpoint=EC,Utail=ctx['Utail'],Rtail=ctx['Rtail'],Wlower=ctx['Wlower_Gram_upper'],Wupper=ctx['Wupper_Gram_upper']).items()}
  assert energies['source']>0 and min(energies.values())>=0
  roots=[2*lower_sqrt(energies['Utail']*energies['Rtail']),lower_sqrt(energies['Wlower']*energies['endpoint']),lower_sqrt(energies['Wupper']*energies['endpoint'])]
  return (energies['base']+sum(roots))/energies['source'],energies,roots
 if probe is None:
  import numpy as np
  from scipy.linalg import eigh
  ar=lambda M:np.array([[float(x) for x in row] for row in M]);gap=p.add(p.mat(chosen,'inverse_response_upper'),p.mat(chosen,'inverse_response_lower'),-1);_,vectors=eigh(ar(gap),ar(G));candidates=[]
  for k in range(8):
   x=vectors[:,k];x=x/max(abs(x));x=[p.down(F(float(v)),10**12) for v in x];candidates.append((evaluate(x)[0],k,x))
  _,_,probe=max(candidates,key=lambda v:(v[0],-v[1]))
 else:probe=list(map(F,probe))
 ratio,energies,roots=evaluate(probe);floor=p.down(ratio,10**6);assert floor>F(1,2)
 return dict(probe_coefficients=list(map(str,probe)),probe_paid_energy_terms={k:str(v) for k,v in energies.items()},geometric_mean_payment_terms_lower=list(map(str,roots)),two_sided_coupled_payment_model_width_floor_lower=str(floor),fixed_trial_two_sided_coupled_payment_model_cannot_pass_half=True,scope='Fixed RC225 trial, RC226 coherent W bounds and residual/source-tail bounds, and the retained four-component Young upper-error model. Every positive payment parameter is covered; other trial maps, error models, and mixed structural/inherited endpoints are not excluded.',true_operator_error_lower_bound_claimed=False,actual_inverse_failure_claimed=False)
def run(reverse=False,saved=None):
 st=state(reverse);previous=st['previous'];G,GH,Gc,a=[st[k] for k in ['G','GH','Gc','a']];Y=p.mat(previous,'optimized_trial_coefficients');ctx,audit=coherent(st,Y)
 parts=[p.cong([Y[i] for i in shared.REG],st['EH']),p.scale(st['EL'],p.outer(Y[8])),p.cong([Y[i] for i in shared.END],st['EC'])]
 _,weights=p.envelope(Y,st['remainder'],G);ps=saved['rational_parameter_proposals'] if saved else optimize(ctx,Y,st['remainder'],G,a,weights,parts)
 ns=dict(vars(p));ns['error_matrix']=lambda YY,ee,w:shared.shared_error(YY,st['remainder'],w,parts);src=inspect.getsource(p.transport).replace('inherited_RC217','inherited_RC225')
 before="W=lambda c:add(add(add(ctx['UGhi'],scale(c*c,ctx['Nhi'])),scale(2*c,ctx['Xhi'])),scale(2*c,V))";assert src.count(before)==1
 src=src.replace(before,"W=lambda c:ctx['Wlower_Gram_upper'] if c==1 else ctx['Wupper_Gram_upper']")
 exec(compile(src,'RC226 unchanged actual inverse identity with coherent W Grams','exec'),ns);fallback=previous['selected_enclosure'];chosen=ns['transport'](ctx,Y,st['eps'],G,GH,Gc,a,ps,p.mat(fallback,'inverse_response_lower'),p.mat(fallback,'inverse_response_upper'),reverse)
 modelAudit=payment_audit(ctx,parts[2],G,a,chosen,saved['shared_payment_audit']['probe_coefficients'] if saved and 'shared_payment_audit' in saved else None)
 return dict(milestone='RC226',starting_commit='6815889c836ed9c28fc33bfa65237451c1776be2',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,trial_coefficients=p.ser(Y),trial_map_unchanged_from_RC225=True,source_and_action_centers_and_radii_unchanged=True,source_normalization_unchanged=True,response_source_count=8,inverse_trial_count=11,source_D_Gram_lower=p.ser(G),source_D_Gram_upper=p.ser(GH),raw_trial_order=previous['raw_trial_order'],conditioned_response_source_order=previous['conditioned_response_source_order'],context={k:p.ser(v) for k,v in ctx.items()},signed_tail_audit=audit,shared_payment_audit=modelAudit,rational_parameter_proposals=ps,selected_enclosure=chosen,relative_inverse_width_upper=chosen['relative_inverse_width_upper'],canonical_half_Gram_inverse_width_gate_passed=chosen['half_Gram_gate_passed'],previous_eight_source_inverse_width_upper=previous['relative_inverse_width_upper'],nominal_residual_relative_Gram_upper=str(p.certified_width(ctx['Nhi'],G)),complete_shared_trial_error_relative_Gram_upper=str(p.certified_width(p.mat(chosen,'action_error_Gram_upper'),G)),all_actual_errors_and_infinite_tails_paid=True,finite_interval_uncertainty_paid=True,common_eta_signed_combinations_taken_before_envelope=True,no_tail_orthogonality_or_cutoff_commutation_assumed=True,cross_tail_theta_retained_for_parameter_schema_but_not_used_in_W_bound=True,numerical_optimization_only_proposes_rationals=True,accepted_six_source_inverse_width_unchanged='4361/10000',RC216_action_error_gate_unchanged='0.420465',Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC227: change the fixed trial or retained endpoint-error/residual model; positive scalar payment retuning cannot clear the audited fixed two-sided coupled model. Preserve separate source-range/odd-sector obligations')
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--replay',action='store_true');args=ap.parse_args();expected=json.loads(args.output.read_text()) if args.replay else None
 result=run(args.replay,expected)
 if args.replay:assert result==expected
 else:args.output.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
 print('RC226 PASS: coherent tail inverse width',result['relative_inverse_width_upper'],'gate',result['canonical_half_Gram_inverse_width_gate_passed'],flush=True)
