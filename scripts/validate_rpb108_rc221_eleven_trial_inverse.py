"""RC221: paid q220 mixed/action rows and eleven-trial eight-source inverse."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,inspect,json
import validate_rpb108_rc220_barrier_residual_action as parent
import validate_rpb108_rc218_coupled_expanded_inverse as p
from validate_rpb108_rc127_enriched_even_endpoint_action import B,Z,rat,plus,minus,div,mul,bounds,down,up,sqrtup,psd,ser,loewner
from validate_rpb108_rc134_correlated_six_input_covariance import smul
ROOT=Path(__file__).resolve().parents[1]
PINS=dict(parent.PINS)
PINS['certificates/rpb108_rc220_barrier_residual_action.json']='a4c558b7866daae6b195142a674914a58dfe1d30'
HELPER_PINS=dict(parent.HELPER_PINS)
HELPER_PINS['scripts/validate_rpb108_rc220_barrier_residual_action.py']='ad5e7214d4abf84f671ec66330c323f4fe42293b'
def horner(coeff,x):
 v=Z
 for c in reversed(coeff):v=plus(c,smul(x,v))
 return v
def assemble(reverse=False):
 for path,sha in sorted(HELPER_PINS.items(),reverse=reverse):assert p.prev.blob((ROOT/path).read_bytes())==sha,(path,'helper pin')
 data={}
 for path,sha in sorted(PINS.items(),reverse=reverse):
  raw=(ROOT/path).read_bytes();assert p.prev.blob(raw)==sha,(path,'input pin');data[path]=json.loads(raw)
 get=lambda n:data['certificates/rpb108_rc'+n+'.json']
 old=get('218_materialized_prefix_interface');base=get('218_coupled_expanded_inverse');qc=get('220_barrier_residual_action');native=get('218_materialized_native_carriers')
 st=parent.prepare(reverse);O=old['finite_prefix_degree'];assert O==65534 and qc['finite_input_degree']==768
 q=parent.rows(qc,'finite_focus_direction');qcp=parent.rows(qc,'endpoint_action_polynomial');qnp=parent.rows(qc,'negative_r_D_inverse_direction_polynomial');qrp=parent.rows(qc['regular_action'],'D_inverse_regular_polynomial')
 qmu=[rat(F(x)) for x in qc['endpoint_exact_signed_moments']];qlam=F(qc['endpoint_analytic_lambda'])
 srcmom=[st['wc']['analytic_moment_centers'],st['vcert']['native_analytic_moments'],native['delta_analytic_moments'],native['t10_analytic_moments']]
 srcmom=[[rat(F(x)) for x in row] for row in srcmom]
 srclam=[F(st['wc']['analytic_lambda']),F(st['vcert']['native_analytic_lambda']),F(native['delta_analytic_lambda']),F(native['t10_analytic_lambda'])]
 qm185=[rat(F(x['exact_signed_coefficient'])) for x in get('194_q185_analytic_endpoint_tail')['analytic_tail_moments']]
 qm202=[rat(F(x)) for x in st['qs'][1]['endpoint_exact_signed_moments']]
 qlams=[F(get('194_q185_analytic_endpoint_tail')['analytic_tail_lambda']),F(st['qs'][1]['endpoint_analytic_lambda'])]
 qep=[parent.rows(z,'endpoint_action_polynomial') for z in st['qs']]
 qneg=[parent.rows(z,'negative_r_D_inverse_direction_polynomial') for z in st['qs']]
 qreg=[parent.rows(z['regular_action'],'D_inverse_regular_polynomial') for z in st['qs']]
 extraMom=[[rat(F(x)) for x in z['endpoint_signed_moment_coefficients']] for z in st['new']]
 extraLam=[F(z['endpoint_analytic_lambda']) for z in st['new']]
 # Parse immutable fixed-point arrays once. No source or nominal action
 # center is changed; Horner evaluation encloses the same signed polynomial.
 ctr=lambda z,key:[F(int(x),int(z['finite_center_scale'])) for x in z[key]]
 cps=[ctr(st['pc'],'finite_Cpsi_coefficient_center_numerators'),ctr(st['cw'],'finite_Cw14_coefficient_center_numerators'),ctr(st['cv'],'finite_Cv10_coefficient_center_numerators')]
 H=[Z]
 for n in range(1,O+3):H.append(plus(H[-1],rat(F(1,n))))
 D={n:(plus(H[n],rat(st['sl']))[0],plus(H[n],rat(st['sh']))[1]) for n in range(0,O+3,2)}
 gg=[Z]*11;left=[Z]*11;right=[Z]*11;aa=[Z]*11
 degrees=list(range(0,O+1,2));degrees=degrees[::-1] if reverse else degrees
 for n in degrees:
  ell=n*(n+1);eta=div(rat(F(2*n+1,ell)),D[n]) if n else Z
  f=eta if 2<=n<=988 else Z;psi=eta if n>=990 else Z
  s=[]
  for k,(finite,cut) in enumerate([(st['gw'],4094),(st['gv'],8190),(st['dv'],8190),(st['tv'],16382)]):
   s.append(rat(finite[n]) if n<=cut else smul(eta,horner(srcmom[k],rat(srclam[k]/ell))))
  w,v,delta,t=s
  u=[rat(F(n==0)),rat(F(n==2)),f,psi,w,rat(st['qin'][0].get(n,F(0))),v,rat(st['qin'][1].get(n,F(0))),delta,t,rat(q.get(n,F(0)))]
  v0=rat(st['r0'].get(n,F(0)));v2=rat(st['r2'].get(n,F(0)))
  v0=plus(v0,rat(1+F(st['p0']['canonical_constant_action_P0_correction_center']))) if n==0 else plus(v0,eta)
  if n==0:v2=plus(v2,rat(F(st['p2']['endpoint_P0_coefficient_center'])))
  elif n==2:v2=plus(v2,rat(1+F(st['p2']['endpoint_P2_correction_center'])))
  else:v2=plus(v2,div(rat(F(2*n+1,ell-6)),D[n]))
  vf=plus(plus(f,w),rat(st['nf'].get(n,F(0))+st['rf'].get(n,F(0))))
  vp=plus(rat(cps[0][n//2]),smul(minus(rat(F(3,2) if n>=32768 else F(1)),div(rat(st['r']),D[n])),psi))
  vw=plus(w,rat(cps[1][n//2]+st['nw'].get(n,F(0))+st['rw'].get(n,F(0))))
  if n>=4096:vw=minus(vw,smul(div(rat(st['r']),D[n]),w))
  if n>=32768:vw=plus(vw,smul(rat(F(1,2)),w))
  vv=plus(v,rat(cps[2][n//2]+st['nv'].get(n,F(0))+st['rv'].get(n,F(0))))
  if n>=514:vv=minus(vv,smul(div(rat(st['r']),D[n]),v))
  if n>=32768:vv=plus(vv,smul(rat(F(1,2)),v))
  vqs=[]
  for k,mom in enumerate([qm185,qm202]):
   av=rat(st['qin'][k].get(n,F(0))+qep[k].get(n,F(0))+qneg[k].get(n,F(0))+qreg[k].get(n,F(0)))
   if n>=4096:av=plus(av,smul(eta,horner(mom,rat(qlams[k]/ell))))
   vqs.append(av)
  vx=[]
  for k,x in enumerate([delta,t]):
   av=minus(plus(x,rat(st['cep'][k].get(n,F(0))+st['creg'][k].get(n,F(0)))),smul(div(rat(st['r']),D[n]),x))
   if n>=4096:av=plus(av,smul(rat(F(1,2)),x))
   if n>=8192:av=plus(av,smul(eta,horner(extraMom[k],rat(extraLam[k]/ell))))
   vx.append(av)
  vq=rat(q.get(n,F(0))+qcp.get(n,F(0))+qnp.get(n,F(0))+qrp.get(n,F(0)))
  if n>=4096:vq=plus(vq,smul(eta,horner(qmu,rat(qlam/ell))))
  acts=[v0,v2,vf,vp,vw,vqs[0],vv,vqs[1]]+vx+[vq]
  mass=mul(rat(2*B/F(2*n+1)),D[n])
  for i in range(11):
   gg[i]=plus(gg[i],smul(mass,smul(u[i],u[10])))
   left[i]=plus(left[i],smul(mass,smul(u[i],vq)))
   right[i]=plus(right[i],smul(mass,smul(u[10],acts[i])))
   aa[i]=plus(aa[i],smul(mass,smul(acts[i],vq)))
  if n%8192==0:print('RC221 q220 prefix rows',n,flush=True)
 expand=lambda A:[row+[F(0)] for row in A]+[[F(0)]*11]
 gl=expand(p.mat(old,'source_Gram_entry_lower'));gh=expand(p.mat(old,'source_Gram_entry_upper'))
 bl=expand(p.mat(old,'nominal_source_action_entry_lower'));bh=expand(p.mat(old,'nominal_source_action_entry_upper'))
 al=expand(p.mat(old,'nominal_action_Gram_entry_lower'));ah=expand(p.mat(old,'nominal_action_Gram_entry_upper'))
 for i in range(11):
  gl[i][10],gh[i][10]=bounds(gg[i]);gl[10][i]=gl[i][10];gh[10][i]=gh[i][10]
  bl[i][10],bh[i][10]=bounds(left[i]);bl[10][i],bh[10][i]=bounds(right[i])
  al[i][10],ah[i][10]=bounds(aa[i]);al[10][i]=al[i][10];ah[10][i]=ah[i][10]
 sourceTail=expand(p.mat(old,'source_tail_Gram_upper'))
 weights=[sqrtup(gh[i][i]) for i in range(11)];GTlo,prefixHi,_=loewner(gl,gh,weights);GThi=p.add(prefixHi,sourceTail);assert psd(GTlo)
 sl=list(map(F,old['source_tail_signed_leading_coefficients']))+[F(0)];sd=list(map(F,old['source_tail_nonleading_absolute_bounds']))+[F(0)]
 vl=list(map(F,old['action_tail_signed_leading_coefficients']))+[F(qc['endpoint_exact_signed_moments'][0])]
 vd=list(map(F,old['action_tail_nonleading_absolute_bounds']))+[sum(abs(F(x))*F(qlam,(O+2)*(O+3))**k for k,x in enumerate(qc['endpoint_exact_signed_moments']) if k)]
 T=F(old['common_eta_tail_D_energy_upper']);eps=list(map(F,old['complete_column_error_norm_upper']))+[F(qc['complete_actual_canonical_q_action_D_error_norm_upper'])]
 actualRows=[];fullNorms=[sqrtup(GThi[i][i]) for i in range(11)]
 for i in range(11):
  pairTail=T*(abs(sl[i])+sd[i])*(abs(vl[10])+vd[10])
  l=down(bl[i][10]-pairTail-fullNorms[i]*eps[10]);h=up(bh[i][10]+pairTail+fullNorms[i]*eps[10])
  l2=down(bl[10][i]-fullNorms[10]*eps[i]);h2=up(bh[10][i]+fullNorms[10]*eps[i])
  lower=max(l,l2);upper=min(h,h2);assert lower<=upper,(i,'actual selfadjoint mixed-row intersection')
  actualRows.append(dict(raw_index=i,actual_pairing_lower=str(lower),actual_pairing_upper=str(upper),q_action_orientation=[str(l),str(h)],old_action_orientation=[str(l2),str(h2)]))
 interface=dict(milestone='RC221-prefix-interface',raw_trial_order=old['raw_trial_order']+['q220'],finite_prefix_degree=O,
  source_Gram_entry_lower=ser(gl),source_Gram_entry_upper=ser(gh),nominal_source_action_entry_lower=ser(bl),nominal_source_action_entry_upper=ser(bh),nominal_action_Gram_entry_lower=ser(al),nominal_action_Gram_entry_upper=ser(ah),
  source_tail_signed_leading_coefficients=list(map(str,sl)),source_tail_nonleading_absolute_bounds=list(map(str,sd)),action_tail_signed_leading_coefficients=list(map(str,vl)),action_tail_nonleading_absolute_bounds=list(map(str,vd)),
  common_eta_tail_D_energy_upper=str(T),source_tail_Gram_upper=ser(sourceTail),full_source_Gram_lower=ser(GTlo),full_source_Gram_upper=ser(GThi),complete_column_error_norm_upper=list(map(str,eps)),actual_q220_selfadjoint_mixed_rows=actualRows,
  old_RC218_prefix_block_preserved_exactly=True,q220_source_finite_no_infinite_input_tail=True)
 return interface,base
def generic_transport():
 # Generalize only the pinned ten-column loop/slice counts. The coupled
 # identity, error payments, exact PSD tests, and selection rule are retained.
 ns=dict(vars(p));err=inspect.getsource(p.error_matrix).replace('range(10)','range(len(eps))')
 opt=inspect.getsource(p.optimize).replace('    import numpy as np','    n=len(eps)\n    import numpy as np').replace('range(10)','range(n)').replace('z[:10]','z[:n]').replace('z[10:]','z[n:]').replace(']*10',']*n').replace('RC218 proposal','RC221 proposal')
 transport=inspect.getsource(p.transport).replace('inherited_RC217','inherited_RC218')
 exec(compile(err+'\n'+opt+'\n'+transport,'RC221 pinned generic coupled transport','exec'),ns)
 return ns['optimize'],ns['transport']
def run(reverse=False,proposals=None):
 interface,base=assemble(reverse);mat=lambda key:p.mat(interface,key)
 gl,gh=mat('source_Gram_entry_lower'),mat('source_Gram_entry_upper');bl,bh=mat('nominal_source_action_entry_lower'),mat('nominal_source_action_entry_upper');al,ah=mat('nominal_action_Gram_entry_lower'),mat('nominal_action_Gram_entry_upper')
 GTlo,GThi=mat('full_source_Gram_lower'),mat('full_source_Gram_upper');sourceTail=mat('source_tail_Gram_upper');G=p.mat(base,'source_D_Gram_lower');GH=p.mat(base,'source_D_Gram_upper');Gcmp=p.mat(base,'RC217_comparison_Gram_floor')
 keep=[0,1,2,3,4,6,8,9];S=[[F(i==keep[j]) for j in range(8)] for i in range(11)]
 mid=lambda L,H:p.scale(F(1,2),p.add(L,H));AM=mid(al,ah);BM=mid(bl,bh)
 full=p.mm(p.inv(AM),p.mm(p.trans(BM),S));full=[[down(x,10**30) for x in row] for row in full]
 prior=next(x for x in base['evaluated_trials'] if x['trial']=='least_residual_10');embedded=p.mat(prior,'trial_coefficients')+[[F(0)]*8]
 trials={'least_residual_11':full,'embedded_RC218_10':embedded}
 inherited=base['selected_enclosure'];inheritedL=p.mat(inherited,'inverse_response_lower');inheritedH=p.mat(inherited,'inverse_response_upper');a=F(32125,230953)
 sl=list(map(F,interface['source_tail_signed_leading_coefficients']));sd=list(map(F,interface['source_tail_nonleading_absolute_bounds']));vl=list(map(F,interface['action_tail_signed_leading_coefficients']));vd=list(map(F,interface['action_tail_nonleading_absolute_bounds']));T=F(interface['common_eta_tail_D_energy_upper']);eps=list(map(F,interface['complete_column_error_norm_upper']))
 iGG=p.imat(gl,gh);iBB=p.imat(bl,bh);iAA=p.imat(al,ah);iS=p.iconst(S);iSt=p.iconst(p.trans(S));optimize,transport=generic_transport();results=[];proposalMap={}
 for name in sorted(trials,reverse=reverse):
  Y=trials[name];iy=p.iconst(Y);iyt=p.iconst(p.trans(Y));j=[[S[i][k]-Y[i][k] for k in range(8)] for i in range(11)]
  cross=p.iprod(p.iprod(iSt,iBB),iy);N=p.iadd(p.iadd(p.iprod(p.iprod(iSt,iGG),iS),p.iadd(cross,p.trans(cross)),-1),p.iprod(p.iprod(iyt,iAA),iy))
  UR=p.iadd(p.iprod(p.iprod(iyt,iGG),iS),p.iprod(p.iprod(iyt,iBB),iy),-1)
  nl,nh=p.interval_matrix(N);xl,xh=p.interval_matrix(p.isym(UR));sw=[sqrtup(GH[i][i]) for i in range(8)]
  Nlo,NprefixHi,_=loewner(nl,nh,sw);Xlo,Xhi,_=loewner(xl,xh,sw)
  if not psd(Nlo):Nlo=p.zeros(8)
  lead=[sl[keep[k]]-sum(vl[i]*Y[i][k] for i in range(11)) for k in range(8)];vectors=[];radii=[]
  for i in range(8):
   if sd[keep[i]]:vectors.append([F(i==k) for k in range(8)]);radii.append(sd[keep[i]])
  for i in range(11):
   if vd[i]:vectors.append(Y[i]);radii.append(vd[i])
  Qrem,_=p.envelope(vectors,radii,G);Rtail=p.add(p.scale(F(3,2)*T,p.outer(lead)),p.scale(3*T,Qrem));Nhi=p.add(NprefixHi,Rtail);Utail=p.cong(Y,sourceTail);UGhi=p.cong(Y,GThi)
  SUlo=p.scale(F(1,2),p.add(p.add(G,p.cong(Y,GTlo)),p.cong(j,GThi),-1));SUhi=p.scale(F(1,2),p.add(p.add(GH,UGhi),p.cong(j,GTlo),-1))
  ctx=dict(UGhi=UGhi,Nlo=Nlo,Nhi=Nhi,Xlo=Xlo,Xhi=Xhi,Utail=Utail,Rtail=Rtail,baseLo=p.add(SUlo,Xlo),baseHi=p.add(SUhi,Xhi))
  _,weights=p.envelope(Y,eps,G);ps=proposals[name] if proposals else optimize(ctx,Y,eps,G,a,weights);proposalMap[name]=ps
  chosen=transport(ctx,Y,eps,G,GH,Gcmp,a,ps,inheritedL,inheritedH,reverse)
  # The nominal-only width is a geometry diagnostic, never an actual inverse
  # acceptance claim. Its upper bound is independently checked by exact PSD.
  nominal=p.certified_width(Nhi,G)
  nominalChord=up((1/a-F(1,2))*nominal)
  assert psd(p.add(p.scale(nominalChord,G),p.scale(1/a-F(1,2),Nhi),-1))
  results.append(dict(trial=name,trial_coefficients=ser(Y),nominal_residual_Gram_lower=ser(Nlo),nominal_residual_Gram_upper=ser(Nhi),nominal_residual_relative_Gram_upper=str(nominal),nominal_only_chord_relative_width_upper=str(nominalChord),nominal_only_chord_half_Gram_geometry_passed=nominalChord<F(1,2),nominal_residual_tail_Gram_upper=ser(Rtail),trial_source_tail_Gram_upper=ser(Utail),trial_source_Gram_upper=ser(UGhi),finite_trial_residual_cross_lower=ser(Xlo),finite_trial_residual_cross_upper=ser(Xhi),base_variational_lower=ser(ctx['baseLo']),base_variational_upper=ser(ctx['baseHi']),selected_enclosure=chosen))
  print('RC221 trial',name,'nominal residual',float(nominal),'inverse width',float(F(chosen['relative_inverse_width_upper'])),'gate',chosen['half_Gram_gate_passed'],flush=True)
  if name=='least_residual_11':
   # An explicitly artificial payment model isolates the action-error
   # contribution. This is NOT a certificate with smaller actual errors.
   zero=[F(0)]*11;_,zw=p.envelope(Y,zero,G);label='ideal_zero_action_error_11'
   zp=proposals[label] if proposals else optimize(ctx,Y,zero,G,a,zw);proposalMap[label]=zp
   ideal=transport(ctx,Y,zero,G,GH,Gcmp,a,zp,inheritedL,inheritedH,reverse)
   ideal=dict(ideal,counterfactual_not_actual_operator_certificate=True,action_error_radii_artificially_zero=True,source_and_output_tails_still_paid=True)
   print('RC221 counterfactual only width',float(F(ideal['relative_inverse_width_upper'])),'geometry/payment gate',ideal['half_Gram_gate_passed'],flush=True)
 results.sort(key=lambda x:x['trial']);best=min(results,key=lambda x:(F(x['selected_enclosure']['relative_inverse_width_upper']),x['trial']));chosen=best['selected_enclosure']
 result=dict(milestone='RC221',starting_commit='ae3045e1ca42b6ec0e7f5ec121b753297146c5c9',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,
  raw_trial_order=interface['raw_trial_order'],conditioned_response_source_order=base['conditioned_response_source_order'],response_source_count=8,inverse_trial_count=11,
  source_D_Gram_lower=ser(G),source_D_Gram_upper=ser(GH),RC217_comparison_Gram_floor=ser(Gcmp),source_normalization_unchanged_from_RC218=True,
  actual_q220_selfadjoint_mixed_rows=interface['actual_q220_selfadjoint_mixed_rows'],rational_parameter_proposals=proposalMap,evaluated_trials=results,selected_trial=best['trial'],selected_enclosure=chosen,
  relative_inverse_width_upper=chosen['relative_inverse_width_upper'],relative_width_on_RC217_Gram_floor=chosen['relative_width_on_RC217_Gram_floor'],canonical_half_Gram_inverse_width_gate_passed=chosen['half_Gram_gate_passed'],previous_eight_source_inverse_width_upper=base['relative_inverse_width_upper'],
  idealized_zero_action_error_payment_enclosure=ideal,idealized_payment_gate_not_actual_acceptance=ideal['half_Gram_gate_passed'],
  q220_mixed_and_action_rows_complete=True,all_infinite_signed_tails_paid=True,same_action_error_combined_before_Young=True,numerical_optimization_proposes_rationals_only=True,
  accepted_six_source_inverse_width_unchanged='4361/10000',RC216_action_error_gate_unchanged='0.420465',actual_residual_capture_not_assumed=True,
  Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC222: refine shared/correlated action-error payments in the eleven-trial transport; the zero-action-error payment model passes, but the actual inverse gate remains open. Preserve both earlier passed gates')
 return result,interface
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--interface',type=Path,required=True);ap.add_argument('--replay',action='store_true');args=ap.parse_args()
 expected=json.loads(args.output.read_text()) if args.replay else None
 result,interface=run(args.replay,expected['rational_parameter_proposals'] if expected else None)
 if args.replay:assert result==expected and interface==json.loads(args.interface.read_text())
 else:
  args.output.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n');args.interface.write_text(json.dumps(interface,sort_keys=True,indent=2)+'\n')
 print('RC221 PASS: complete eleven-trial inverse evaluation; gate',result['canonical_half_Gram_inverse_width_gate_passed'])
