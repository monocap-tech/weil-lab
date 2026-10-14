"""RC228: compatible q227 rows and the paid twelve-trial eight-source inverse."""
from pathlib import Path
from fractions import Fraction as F
import argparse,inspect,json,re
import validate_rpb108_rc227_new_residual_trial_action as parent
import validate_rpb108_rc221_eleven_trial_inverse as old
import validate_rpb108_rc224_compatible_extended_inverse as prior
co=parent.parent;p=parent.p;shared=co.shared;ROOT=Path(__file__).resolve().parents[1]
PINS=dict(parent.PINS);PINS['certificates/rpb108_rc227_new_residual_trial_action.json']='ae8fbdc426ad988debac9f819379dcb787768877'
HELPER_PINS=dict(parent.HELPER_PINS);HELPER_PINS['scripts/validate_rpb108_rc227_new_residual_trial_action.py']='a3667c676e087db848c7b457b8b23bff78a52bf2'
replace=parent.replace
def assemble(reverse=False):
 src=inspect.getsource(old.assemble)
 src=replace(src,"old=get('218_materialized_prefix_interface');base=get('218_coupled_expanded_inverse');qc=get('220_barrier_residual_action')","old=get('224_materialized_prefix_interface');base=get('226_coherent_residual_tail_inverse');qc=get('227_new_residual_trial_action')")
 src=replace(src,'qc[\'finite_input_degree\']==768',"qc['finite_input_degree']==1536")
 insertion="""
 qold=get('220_barrier_residual_action');oq=parent.rows(qold,'finite_focus_direction');ocp=parent.rows(qold,'endpoint_action_polynomial');onp=parent.rows(qold,'negative_r_D_inverse_direction_polynomial');orp=parent.rows(qold['regular_action'],'D_inverse_regular_polynomial')
 omu=[rat(F(x)) for x in qold['endpoint_exact_signed_moments']];olam=F(qold['endpoint_analytic_lambda'])
 extension=get('223_materialized_delta_t10_endpoint_carriers')['carriers'];extCp=[[F(int(v),int(z['finite_center_scale'])) for v in z['finite_C_coefficient_center_numerators']] for z in extension]
"""
 src=replace(src," q=parent.rows(qc,'finite_focus_direction');",insertion+" q=parent.rows(qc,'finite_focus_direction');")
 src=replace(src,'rat(q.get(n,F(0)))]','rat(oq.get(n,F(0))),rat(q.get(n,F(0)))]')
 src=replace(src,"av=minus(plus(x,rat(st['cep'][k].get(n,F(0))+st['creg'][k].get(n,F(0)))),smul(div(rat(st['r']),D[n]),x))","av=minus(plus(x,rat(extCp[k][n//2]+st['creg'][k].get(n,F(0)))),smul(div(rat(st['r']),D[n]),x))")
 src=replace(src,'   if n>=4096:av=plus(av,smul(rat(F(1,2)),x))','   if n>=32768:av=plus(av,smul(rat(F(1,2)),x))')
 src=replace(src,'   if n>=8192:av=plus(av,smul(eta,horner(extraMom[k],rat(extraLam[k]/ell))))','   # Extended finite endpoint centers continue through the whole prefix.')
 src=replace(src,'  vq=rat(q.get(n,F(0))+',"  vold=rat(oq.get(n,F(0))+ocp.get(n,F(0))+onp.get(n,F(0))+orp.get(n,F(0)))\n  if n>=4096:vold=plus(vold,smul(eta,horner(omu,rat(olam/ell))))\n  vq=rat(q.get(n,F(0))+")
 src=replace(src,'acts=[v0,v2,vf,vp,vw,vqs[0],vv,vqs[1]]+vx+[vq]','acts=[v0,v2,vf,vp,vw,vqs[0],vv,vqs[1]]+vx+[vold,vq]')
 src=src.replace('range(11)','range(12)').replace('[Z]*11','[Z]*12').replace('[F(0)]*11','[F(0)]*12').replace('[10]','[11]')
 src=src.replace("+['q220']","+['q227']").replace('RC221-prefix-interface','RC228-prefix-interface').replace('RC221 q220 prefix rows','RC228 q227 prefix rows').replace('actual_q220_selfadjoint_mixed_rows','actual_q227_selfadjoint_mixed_rows').replace('old_RC218_prefix_block_preserved_exactly','old_RC224_prefix_block_preserved_exactly').replace('q220_source_finite_no_infinite_input_tail','q227_source_finite_no_infinite_input_tail')
 ns=dict(vars(old));ns.update(PINS=PINS,HELPER_PINS=HELPER_PINS,ROOT=ROOT);exec(compile(src,'RC228 pinned twelve-trial compatible row reconstruction','exec'),ns);interface,base=ns['assemble'](reverse)
 previous=json.loads((ROOT/'certificates/rpb108_rc224_materialized_prefix_interface.json').read_text())
 for key in ['source_Gram_entry_lower','source_Gram_entry_upper','nominal_source_action_entry_lower','nominal_source_action_entry_upper','nominal_action_Gram_entry_lower','nominal_action_Gram_entry_upper']:
  assert all(interface[key][i][j]==previous[key][i][j] for i in range(11) for j in range(11)),key
 qcert=json.loads((ROOT/'certificates/rpb108_rc227_new_residual_trial_action.json').read_text())
 for i in range(12):
  assert F(interface['source_Gram_entry_lower'][i][11])<=F(qcert['enlarged_source_prefix_Gram_entry_upper'][i][11])
  assert F(qcert['enlarged_source_prefix_Gram_entry_lower'][i][11])<=F(interface['source_Gram_entry_upper'][i][11])
 return interface,base
def generic(src):return re.sub(r'\b11\b','12',re.sub(r'\b14\b','15',src))
def helpers():
 ns=dict(vars(prior));exec(compile(generic(inspect.getsource(prior.context)),'RC228 generic residual context','exec'),ns);context=ns['context']
 ns2=dict(vars(co));ns2['context']=context;src=generic(inspect.getsource(co.coherent)).replace('parent.parent.context(interface,Y,G,GH)','context(interface,Y,G,GH)');exec(compile(src,'RC228 coherent twelve-trial tail context','exec'),ns2)
 ns3=dict(vars(shared));src='\n'.join(generic(inspect.getsource(f)) for f in [shared.remainder_error,shared.shared_error,shared.optimize]);before="NL=wh(ctx['Nlo']);parts=list(map(wh,parts));";src=replace(src,before,"Wlc=wh(ctx['Wlower_Gram_upper']);Wuc=wh(ctx['Wupper_Gram_upper']);"+before);src=replace(src,'wl=UG+N+2*X+2*V;co=2/float(a);wu=UG+co*co*N+2*co*X+2*co*V','wl=Wlc;wu=Wuc');exec(compile(src,'RC228 twelve-column complete shared-error payment','exec'),ns3)
 return ns2['coherent'],ns3['shared_error'],ns3['optimize']
def run(reverse=False,saved=None):
 interface,base=assemble(reverse);st=co.parent.load(reverse);st['interface']=interface;G,GH,Gc,a=[st[k] for k in ['G','GH','Gc','a']];get=lambda n:json.loads((ROOT/('certificates/rpb108_rc'+n+'.json')).read_text());qc=get('227_new_residual_trial_action')
 eps=list(map(F,interface['complete_column_error_norm_upper']));assert eps[:11]==st['eps'] and eps[11]==F(qc['complete_actual_canonical_q_action_D_error_norm_upper'])
 assert eps[11]>=F(qc['regular_action']['regular_omitted_finite_input_D_error_norm_upper'])
 assert p.ser(G)==base['source_D_Gram_lower'] and p.ser(GH)==base['source_D_Gram_upper']
 remainder=st['remainder']+[eps[11]];assert len(remainder)==12 and min(remainder)>=0
 keep=[0,1,2,3,4,6,8,9];S=[[F(i==keep[j]) for j in range(8)] for i in range(12)];mid=lambda L,H:p.scale(F(1,2),p.add(L,H));AM=mid(p.mat(interface,'nominal_action_Gram_entry_lower'),p.mat(interface,'nominal_action_Gram_entry_upper'));BM=mid(p.mat(interface,'nominal_source_action_entry_lower'),p.mat(interface,'nominal_source_action_entry_upper'));Y=p.mm(p.inv(AM),p.mm(p.trans(BM),S));Y=[[p.down(x,10**30) for x in row] for row in Y]
 coherent,error,opt=helpers();ctx,audit=coherent(st,Y);parts=[p.cong([Y[i] for i in shared.REG],st['EH']),p.scale(st['EL'],p.outer(Y[8])),p.cong([Y[i] for i in shared.END],st['EC'])]
 _,weights=p.envelope(Y,remainder,G);ps=saved['rational_parameter_proposals'] if saved else opt(ctx,Y,remainder,G,a,weights,parts)
 ns=dict(vars(p));ns['error_matrix']=lambda YY,ee,w:error(YY,remainder,w,parts);src=inspect.getsource(p.transport).replace('inherited_RC217','inherited_RC226');src=replace(src,"W=lambda c:add(add(add(ctx['UGhi'],scale(c*c,ctx['Nhi'])),scale(2*c,ctx['Xhi'])),scale(2*c,V))","W=lambda c:ctx['Wlower_Gram_upper'] if c==1 else ctx['Wupper_Gram_upper']");exec(compile(src,'RC228 unchanged paid inverse identity','exec'),ns);fallback=base['selected_enclosure'];chosen=ns['transport'](ctx,Y,eps,G,GH,Gc,a,ps,p.mat(fallback,'inverse_response_lower'),p.mat(fallback,'inverse_response_upper'),reverse)
 result=dict(milestone='RC228',starting_commit='05feda400d51720bbc715776934cfb22756f5d0d',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,response_source_count=8,inverse_trial_count=12,raw_trial_order=interface['raw_trial_order'],conditioned_response_source_order=base['conditioned_response_source_order'],source_D_Gram_lower=p.ser(G),source_D_Gram_upper=p.ser(GH),source_normalization_unchanged=True,old_eleven_trial_prefix_blocks_preserved_exactly=True,actual_q227_selfadjoint_mixed_rows=interface['actual_q227_selfadjoint_mixed_rows'],trial_coefficients=p.ser(Y),context={k:p.ser(v) for k,v in ctx.items()},signed_tail_audit=audit,complete_column_error_norm_upper=list(map(str,eps)),remaining_individual_column_error_norm_upper=list(map(str,remainder)),q227_complete_action_error_paid_without_removing_high_regular_input_error=True,fixed_trial_error_components=[p.ser(v) for v in parts],rational_parameter_proposals=ps,selected_enclosure=chosen,relative_inverse_width_upper=chosen['relative_inverse_width_upper'],canonical_half_Gram_inverse_width_gate_passed=chosen['half_Gram_gate_passed'],previous_eight_source_inverse_width_upper=base['relative_inverse_width_upper'],nominal_residual_relative_Gram_upper=str(p.certified_width(ctx['Nhi'],G)),complete_shared_trial_error_relative_Gram_upper=str(p.certified_width(p.mat(chosen,'action_error_Gram_upper'),G)),all_actual_errors_and_source_action_residual_tails_paid=True,accepted_six_source_inverse_width_unchanged='4361/10000',RC216_action_error_gate_unchanged='0.420465',Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC229: inspect the twelve-trial residual and actual endpoint/regular-error payments; preserve the accepted gates and separate source-range/odd-sector obligations')
 print('RC228 actual inverse width',result['relative_inverse_width_upper'],'gate',result['canonical_half_Gram_inverse_width_gate_passed'],flush=True);return result,interface
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--interface',type=Path,required=True);ap.add_argument('--replay',action='store_true');args=ap.parse_args();expected=json.loads(args.output.read_text()) if args.replay else None;result,interface=run(args.replay,expected)
 if args.replay:assert result==expected and interface==json.loads(args.interface.read_text())
 else:args.output.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n');args.interface.write_text(json.dumps(interface,sort_keys=True,indent=2)+'\n')
 print('RC228 PASS: twelve-trial paid inverse certificate; Stage I remains open',flush=True)
