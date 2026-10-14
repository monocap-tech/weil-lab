"""RC224: compatible extended delta/t10 matrices and shared-error inverse.

The pinned RC221 reconstruction is specialized by checked textual changes.
Only columns 8/9 of the mixed matrix and rows/columns 8/9 of the nominal
action Gram change. All source matrices and the reference Gram are retained.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,inspect,json
import validate_rpb108_rc223_extended_delta_t10_endpoints as parent
import validate_rpb108_rc221_eleven_trial_inverse as old
p=parent.p;shared=parent.prev;ROOT=Path(__file__).resolve().parents[1]
PINS=dict(parent.PINS)
PINS.update({'certificates/rpb108_rc223_extended_delta_t10_endpoints.json':'8fe624740732d6d15ce9181a1a039bd5be0cd561','certificates/rpb108_rc223_materialized_delta_t10_endpoint_carriers.json':'8333512e1b499e6adffbbd2ae3943be3f1bbe180'})
HELPER_PINS=dict(parent.HELPER_PINS)
HELPER_PINS['scripts/validate_rpb108_rc223_extended_delta_t10_endpoints.py']='b8404d58431747694b68e8bf4debbcb67a0c7499'
def replace(src,before,after):
 assert src.count(before)==1,(before,src.count(before));return src.replace(before,after)
def assemble(reverse=False):
 src=inspect.getsource(old.assemble)
 src=replace(src,"old=get('218_materialized_prefix_interface');base=get('218_coupled_expanded_inverse')","old=get('221_materialized_prefix_interface');base=get('222_shared_tail_error_inverse')")
 src=replace(src," st=parent.prepare(reverse);O=old['finite_prefix_degree'];assert O==65534 and qc['finite_input_degree']==768", " st=parent.prepare(reverse);O=old['finite_prefix_degree'];assert O==65534 and qc['finite_input_degree']==768\n extension=get('223_materialized_delta_t10_endpoint_carriers')['carriers'];action223=get('223_extended_delta_t10_endpoints')\n assert [x['source'] for x in extension]==['delta','t10']\n extCp=[[F(int(v),int(c['finite_center_scale'])) for v in c['finite_C_coefficient_center_numerators']] for c in extension]\n extMom=[[F(v['center']) for v in c['analytic_output_moments']] for c in extension]\n extLam=[F(c['analytic_output_lambda']) for c in extension]\n assert all(c['source_prefix_degree']==32766 and c['output_prefix_degree']==O for c in extension)")
 src=replace(src,"gg=[Z]*11;left=[Z]*11;right=[Z]*11;aa=[Z]*11","gg=[Z]*11;left=[[Z]*11 for _ in range(2)];right=[[Z]*11 for _ in range(2)];aa=[[Z]*11 for _ in range(2)]")
 src=replace(src,"av=minus(plus(x,rat(st['cep'][k].get(n,F(0))+st['creg'][k].get(n,F(0)))),smul(div(rat(st['r']),D[n]),x))","av=minus(plus(x,rat(extCp[k][n//2]+st['creg'][k].get(n,F(0)))),smul(div(rat(st['r']),D[n]),x))")
 src=replace(src,"   if n>=4096:av=plus(av,smul(rat(F(1,2)),x))","   if n>=32768:av=plus(av,smul(rat(F(1,2)),x))")
 src=replace(src,"   if n>=8192:av=plus(av,smul(eta,horner(extraMom[k],rat(extraLam[k]/ell))))", "   # The new endpoint analytic output begins at 65536, above this prefix.")
 src=replace(src,"  for i in range(11):\n   gg[i]=plus(gg[i],smul(mass,smul(u[i],u[10])))\n   left[i]=plus(left[i],smul(mass,smul(u[i],vq)))\n   right[i]=plus(right[i],smul(mass,smul(u[10],acts[i])))\n   aa[i]=plus(aa[i],smul(mass,smul(acts[i],vq)))", "  for k,J in enumerate([8,9]):\n   for i in range(11):\n    left[k][i]=plus(left[k][i],smul(mass,smul(u[i],acts[J])))\n    right[k][i]=plus(right[k][i],smul(mass,smul(u[J],acts[i])))\n    aa[k][i]=plus(aa[k][i],smul(mass,smul(acts[i],acts[J])))")
 src=replace(src," expand=lambda A:[row+[F(0)] for row in A]+[[F(0)]*11]"," expand=lambda A:[row[:] for row in A]")
 src=replace(src," for i in range(11):\n  gl[i][10],gh[i][10]=bounds(gg[i]);gl[10][i]=gl[i][10];gh[10][i]=gh[i][10]\n  bl[i][10],bh[i][10]=bounds(left[i]);bl[10][i],bh[10][i]=bounds(right[i])\n  al[i][10],ah[i][10]=bounds(aa[i]);al[10][i]=al[i][10];ah[10][i]=ah[i][10]", " for k,J in enumerate([8,9]):\n  for i in range(11):\n   bl[i][J],bh[i][J]=bounds(left[k][i])\n   al[i][J],ah[i][J]=bounds(aa[k][i]);al[J][i]=al[i][J];ah[J][i]=ah[i][J]")
 src=replace(src," sl=list(map(F,old['source_tail_signed_leading_coefficients']))+[F(0)];sd=list(map(F,old['source_tail_nonleading_absolute_bounds']))+[F(0)]", " sl=list(map(F,old['source_tail_signed_leading_coefficients']));sd=list(map(F,old['source_tail_nonleading_absolute_bounds']))")
 src=replace(src," vl=list(map(F,old['action_tail_signed_leading_coefficients']))+[F(qc['endpoint_exact_signed_moments'][0])]", " vl=list(map(F,old['action_tail_signed_leading_coefficients']))")
 src=replace(src," vd=list(map(F,old['action_tail_nonleading_absolute_bounds']))+[sum(abs(F(x))*F(qlam,(O+2)*(O+3))**k for k,x in enumerate(qc['endpoint_exact_signed_moments']) if k)]", " vd=list(map(F,old['action_tail_nonleading_absolute_bounds']))\n z=(O+2)*(O+3);dl=F(D[O][0])\n for k,J in enumerate([8,9]):\n  vl[J]=(F(3,2)-st['r']/(2*dl))*sl[J]+extMom[k][0]\n  vd[J]=F(3,2)*sd[J]+st['r']*abs(sl[J])/(2*dl)+sum(abs(x)*F(extLam[k],z)**j for j,x in enumerate(extMom[k]) if j)")
 src=replace(src,"eps=list(map(F,old['complete_column_error_norm_upper']))+[F(qc['complete_actual_canonical_q_action_D_error_norm_upper'])]", "eps=list(map(F,old['complete_column_error_norm_upper']))\n for k,J in enumerate([8,9]):eps[J]=F(action223['evaluated_endpoint_actions'][k]['complete_canonical_action_error_norm_upper'])")
 start=src.index(' actualRows=[];fullNorms=');end=src.index('\n interface=dict(',start)
 src=src[:start]+''' actualRows=[];fullNorms=[sqrtup(GThi[i][i]) for i in range(11)]
 for J in [8,9,10]:
  for i in range(11):
   tailLeft=T*(abs(sl[i])+sd[i])*(abs(vl[J])+vd[J])
   tailRight=T*(abs(sl[J])+sd[J])*(abs(vl[i])+vd[i])
   l=down(bl[i][J]-tailLeft-fullNorms[i]*eps[J]);h=up(bh[i][J]+tailLeft+fullNorms[i]*eps[J])
   l2=down(bl[J][i]-tailRight-fullNorms[J]*eps[i]);h2=up(bh[J][i]+tailRight+fullNorms[J]*eps[i])
   lower=max(l,l2);upper=min(h,h2);assert lower<=upper,(i,J,'actual selfadjoint extended-row intersection')
   actualRows.append(dict(raw_index=i,target_raw_index=J,actual_pairing_lower=str(lower),actual_pairing_upper=str(upper),target_action_orientation=[str(l),str(h)],other_action_orientation=[str(l2),str(h2)]))
''' +src[end:]
 src=replace(src,"raw_trial_order=old['raw_trial_order']+['q220']", "raw_trial_order=old['raw_trial_order']")
 src=src.replace('RC221-prefix-interface','RC224-prefix-interface').replace('RC221 q220 prefix rows','RC224 compatible extended prefix rows').replace('actual_q220_selfadjoint_mixed_rows','actual_extended_selfadjoint_mixed_rows').replace('old_RC218_prefix_block_preserved_exactly=True','source_blocks_preserved_exactly=True,unchanged_action_subblock_preserved_exactly=True,new_endpoint_centers_and_radii_attached_together=True')
 ns=dict(vars(old));ns.update(PINS=PINS,HELPER_PINS=HELPER_PINS,ROOT=ROOT);exec(compile(src,'RC224 pinned specialized extended action reconstruction','exec'),ns);interface,base=ns['assemble'](reverse)
 prior=json.loads((ROOT/'certificates/rpb108_rc221_materialized_prefix_interface.json').read_text())
 for key in ['source_Gram_entry_lower','source_Gram_entry_upper','source_tail_Gram_upper','full_source_Gram_lower','full_source_Gram_upper']:assert interface[key]==prior[key],key
 for key in ['nominal_action_Gram_entry_lower','nominal_action_Gram_entry_upper']:
  assert all(interface[key][i][j]==prior[key][i][j] for i in range(11) for j in range(11) if i not in [8,9] and j not in [8,9])
 for key in ['nominal_source_action_entry_lower','nominal_source_action_entry_upper']:assert all(interface[key][i][j]==prior[key][i][j] for i in range(11) for j in range(11) if j not in [8,9])
 return interface,base
def context(interface,Y,G,GH):
 gl,gh=p.mat(interface,'source_Gram_entry_lower'),p.mat(interface,'source_Gram_entry_upper');bl,bh=p.mat(interface,'nominal_source_action_entry_lower'),p.mat(interface,'nominal_source_action_entry_upper');al,ah=p.mat(interface,'nominal_action_Gram_entry_lower'),p.mat(interface,'nominal_action_Gram_entry_upper')
 GTlo=p.mat(interface,'full_source_Gram_lower');GThi=p.mat(interface,'full_source_Gram_upper');sourceTail=p.mat(interface,'source_tail_Gram_upper');keep=[0,1,2,3,4,6,8,9];S=[[F(i==keep[j]) for j in range(8)] for i in range(11)]
 iy=p.iconst(Y);iyt=p.iconst(p.trans(Y));iS=p.iconst(S);iSt=p.iconst(p.trans(S));iGG=p.imat(gl,gh);iBB=p.imat(bl,bh);iAA=p.imat(al,ah)
 cross=p.iprod(p.iprod(iSt,iBB),iy);N=p.iadd(p.iadd(p.iprod(p.iprod(iSt,iGG),iS),p.iadd(cross,p.trans(cross)),-1),p.iprod(p.iprod(iyt,iAA),iy));UR=p.iadd(p.iprod(p.iprod(iyt,iGG),iS),p.iprod(p.iprod(iyt,iBB),iy),-1)
 nl,nh=p.interval_matrix(N);xl,xh=p.interval_matrix(p.isym(UR));sw=[p.sqrtup(GH[i][i]) for i in range(8)];Nlo,NprefixHi,_=p.loewner(nl,nh,sw);Xlo,Xhi,_=p.loewner(xl,xh,sw)
 if not p.psd(Nlo):Nlo=p.zeros(8)
 sl=list(map(F,interface['source_tail_signed_leading_coefficients']));sd=list(map(F,interface['source_tail_nonleading_absolute_bounds']));vl=list(map(F,interface['action_tail_signed_leading_coefficients']));vd=list(map(F,interface['action_tail_nonleading_absolute_bounds']));T=F(interface['common_eta_tail_D_energy_upper'])
 lead=[sl[keep[k]]-sum(vl[i]*Y[i][k] for i in range(11)) for k in range(8)];vectors=[];radii=[]
 for i in range(8):
  if sd[keep[i]]:vectors.append([F(i==k) for k in range(8)]);radii.append(sd[keep[i]])
 for i in range(11):
  if vd[i] and any(Y[i]):vectors.append(Y[i]);radii.append(vd[i])
 Qrem,_=p.envelope(vectors,radii,G);Rtail=p.add(p.scale(F(3,2)*T,p.outer(lead)),p.scale(3*T,Qrem));Nhi=p.add(NprefixHi,Rtail);Utail=p.cong(Y,sourceTail);UGhi=p.cong(Y,GThi)
 j=[[S[i][k]-Y[i][k] for k in range(8)] for i in range(11)];SUlo=p.scale(F(1,2),p.add(p.add(G,p.cong(Y,GTlo)),p.cong(j,GThi),-1));SUhi=p.scale(F(1,2),p.add(p.add(GH,UGhi),p.cong(j,GTlo),-1))
 return dict(UGhi=UGhi,Nlo=Nlo,Nhi=Nhi,Xlo=Xlo,Xhi=Xhi,Utail=Utail,Rtail=Rtail,baseLo=p.add(SUlo,Xlo),baseHi=p.add(SUhi,Xhi))
def run(reverse=False,proposals=None):
 interface,base=assemble(reverse);get=lambda name:json.loads((ROOT/('certificates/rpb108_rc'+name+'.json')).read_text());previous221=get('221_eleven_trial_inverse');refined=get('223_extended_delta_t10_endpoints')
 G=p.mat(base,'source_D_Gram_lower');GH=p.mat(base,'source_D_Gram_upper');Gc=p.mat(previous221,'RC217_comparison_Gram_floor');a=F(32125,230953);keep=[0,1,2,3,4,6,8,9];S=[[F(i==keep[j]) for j in range(8)] for i in range(11)]
 mid=lambda L,H:p.scale(F(1,2),p.add(L,H));AM=mid(p.mat(interface,'nominal_action_Gram_entry_lower'),p.mat(interface,'nominal_action_Gram_entry_upper'));BM=mid(p.mat(interface,'nominal_source_action_entry_lower'),p.mat(interface,'nominal_source_action_entry_upper'));full=p.mm(p.inv(AM),p.mm(p.trans(BM),S));full=[[p.down(x,10**30) for x in row] for row in full]
 prior=next(x for x in previous221['evaluated_trials'] if x['trial']=='least_residual_11');trials={'extended_least_residual_11':full,'fixed_RC221_trial_11':p.mat(prior,'trial_coefficients')}
 eps=list(map(F,interface['complete_column_error_norm_upper']));removedR=list(map(F,base['individual_error_decomposition_ledger']['removedR']));removedC=list(map(F,base['individual_error_decomposition_ledger']['removedC']))
 for k,J in enumerate([8,9]):removedC[J]=p.sqrtup(F(refined['evaluated_endpoint_actions'][k]['omitted_input_D_energy_upper']))/2
 remainder=[eps[i]-removedR[i]-removedC[i] for i in range(11)];assert min(remainder)>=0
 EHraw=p.scale(F(base['smoothing_squared_upper_512'])/F(base['D_metric_floor_lower']),p.mat(base,'high_physical_input_Gram_upper'));ELscalar=F(base['smoothing_squared_upper_128'])/F(base['D_metric_floor_lower'])*F(base['delta_low_physical_input_energy_upper']);ECraw=p.scale(F(1,4),p.mat(refined,'matched_omitted_endpoint_input_D_Gram_upper'))
 results=[];proposalMap={};previous=base['selected_enclosure']
 for name in sorted(trials,reverse=reverse):
  Y=trials[name];ctx=context(interface,Y,G,GH);parts=[p.cong([Y[i] for i in shared.REG],EHraw),p.scale(ELscalar,p.outer(Y[8])),p.cong([Y[i] for i in shared.END],ECraw)]
  _,weights=p.envelope(Y,remainder,G);ps=proposals[name] if proposals else shared.optimize(ctx,Y,remainder,G,a,weights,parts);proposalMap[name]=ps
  ns=dict(vars(p));ns['error_matrix']=lambda YY,ee,w:shared.shared_error(YY,remainder,w,parts);src=inspect.getsource(p.transport).replace('inherited_RC217','inherited_RC222');exec(compile(src,'RC224 unchanged coupled identity and paid shared-error model','exec'),ns)
  chosen=ns['transport'](ctx,Y,eps,G,GH,Gc,a,ps,p.mat(previous,'inverse_response_lower'),p.mat(previous,'inverse_response_upper'),reverse)
  residual=p.certified_width(ctx['Nhi'],G);error=p.certified_width(p.mat(chosen,'action_error_Gram_upper'),G)
  results.append(dict(trial=name,trial_coefficients=p.ser(Y),context={k:p.ser(v) for k,v in ctx.items()},fixed_trial_error_components=[p.ser(v) for v in parts],nominal_residual_relative_Gram_upper=str(residual),complete_shared_trial_error_relative_Gram_upper=str(error),selected_enclosure=chosen))
  print('RC224 trial',name,'nominal residual',float(residual),'error',float(error),'inverse',float(F(chosen['relative_inverse_width_upper'])),'gate',chosen['half_Gram_gate_passed'],flush=True)
 results.sort(key=lambda x:x['trial']);best=min(results,key=lambda x:(F(x['selected_enclosure']['relative_inverse_width_upper']),x['trial']));chosen=best['selected_enclosure']
 result=dict(milestone='RC224',starting_commit='3fa09b6ae92f79c65201242e4854ac1c5a0efd5b',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,raw_trial_order=interface['raw_trial_order'],conditioned_response_source_order=base['conditioned_response_source_order'],response_source_count=8,inverse_trial_count=11,
  source_D_Gram_lower=p.ser(G),source_D_Gram_upper=p.ser(GH),source_normalization_unchanged=True,actual_extended_selfadjoint_mixed_rows=interface['actual_extended_selfadjoint_mixed_rows'],new_centers_and_new_radii_used_together=True,all_affected_mixed_and_action_rows_rebuilt=True,
  individual_error_decomposition_ledger=dict(eps=list(map(str,eps)),removedR=list(map(str,removedR)),removedC=list(map(str,removedC)),remainder=list(map(str,remainder))),rational_parameter_proposals=proposalMap,evaluated_trials=results,selected_trial=best['trial'],selected_enclosure=chosen,
  relative_inverse_width_upper=chosen['relative_inverse_width_upper'],relative_width_on_RC217_Gram_floor=chosen['relative_width_on_RC217_Gram_floor'],canonical_half_Gram_inverse_width_gate_passed=chosen['half_Gram_gate_passed'],previous_eight_source_inverse_width_upper=base['relative_inverse_width_upper'],
  no_actual_errors_artificially_zeroed=True,all_input_output_and_residual_tails_paid=True,complex_response_mixtures_paid=True,numerical_optimization_only_proposes_rationals=True,accepted_six_source_inverse_width_unchanged='4361/10000',RC216_action_error_gate_unchanged='0.420465',Stage_I_closed=False,RH=False,F4=False,Lean=False,
  next_cursor='RC225: inspect the rebuilt nominal residual tails and actual shared error components; preserve the accepted gates and address the dominant certified payment or remaining source-range/coverage obligations')
 return result,interface
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--interface',type=Path,required=True);ap.add_argument('--replay',action='store_true');args=ap.parse_args();expected=json.loads(args.output.read_text()) if args.replay else None
 result,interface=run(args.replay,expected['rational_parameter_proposals'] if expected else None)
 if args.replay:assert result==expected and interface==json.loads(args.interface.read_text())
 else:
  args.output.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n');args.interface.write_text(json.dumps(interface,sort_keys=True,indent=2)+'\n')
 print('RC224 PASS: compatible actual inverse width',result['relative_inverse_width_upper'],'gate',result['canonical_half_Gram_inverse_width_gate_passed'])
