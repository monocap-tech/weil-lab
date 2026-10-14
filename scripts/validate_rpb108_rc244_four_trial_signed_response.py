"""RC244: paid four-trial responses with certified residual-shaped actions."""
from pathlib import Path
from fractions import Fraction as F
from copy import deepcopy
import argparse,hashlib,json
import validate_rpb108_rc243_residual_augmented_actions as parent
oldtrial=parent.parent.parent.parent;trial=oldtrial.trial
orig=parent.orig;p=parent.p;B=parent.B
up=parent.up;down=parent.down;root=parent.root;rootdown=oldtrial.rootdown
loewner=oldtrial.loewner;quadratic=oldtrial.quadratic
ROOT=Path(__file__).resolve().parents[1];CUT=128
PINS=dict(parent.PINS);HELPER_PINS=dict(parent.HELPER_PINS)
PINS.update({'certificates/rpb108_rc243_residual_augmented_actions.json':'12067c055c270f277f9c070e84dbbe79890ecfe6','notes/RPB108_RC243_RESIDUAL_AUGMENTED_ACTIONS_20261014.md':'50ea735a4a5c109c2b5efcefe9f9d15719f639fb'})
HELPER_PINS['scripts/validate_rpb108_rc243_residual_augmented_actions.py']='0a092cbb7efee3784855fff29bd65f94a3a715be'
def pad(rows):
 rows=deepcopy(rows)
 return rows+[dict(degree=n,coefficient='0',radius='0') for n in range(len(rows),CUT+1)]
def poly_form(a,column,sl,sh):
 lo=hi=energy=F(0)
 for n,c in enumerate(a):
  if not c:continue
  x=column['finite_original_D_action'][n];v=F(x['coefficient']);rad=F(x['radius'])
  wl=orig.mass(n)*(orig.H(n)+sl);wh=orig.mass(n)*(orig.H(n)+sh);values=[c*t*w for t in [v-rad,v+rad] for w in [wl,wh]]
  lo+=min(values);hi+=max(values);energy+=wh*c*c
 fault=root(energy)*sum((root(F(column['D_energy_component_squared_errors'][k])) for k in ['regular_kernel','prime_arithmetic','pole_Taylor']),F(0))
 return down(lo-fault),up(hi+fault)
def pair_band(a,column):
 lo=hi=F(0)
 for n,c in enumerate(a):
  if c:
   x=column[n];v=[c*F(x['lower']),c*F(x['upper'])];lo+=min(v);hi+=max(v)
 return down(lo),up(hi)
def controls():
 D=[[F(i+2) if i==k else F(0) for k in range(4)] for i in range(4)]
 F0=[[F(i+1) if i==k else F(1,i+k+7) for k in range(4)] for i in range(4)]
 Gy=[[F(i+2) if i==k else -F(1,i+k+9) for k in range(4)] for i in range(4)];lam=F(3);G=p.add(F0,p.scale(lam,Gy));N=p.mm(p.inv(D),G);N0=p.mm(p.inv(D),F0)
 assert p.psd(G) and p.mm(N,N0)!=p.mm(N0,N)
 q=[[F(1)],[F(0)],[F(0)],[F(0)]];y=[[F(1,7)],[-F(1,11)],[F(2,13)],[-F(3,17)]];u=p.add(q,y,-1);O=p.mm(N0,q);e=p.add(O,p.mm(N,y),-1)
 T=p.mm(p.mm(p.trans(O),D),p.mm(p.inv(N),O))[0][0];R=p.mm(p.mm(p.trans(e),D),p.mm(p.inv(N),e))[0][0]
 C=2*p.mm(p.trans(y),p.mm(F0,q))[0][0]-p.mm(p.trans(y),p.mm(G,y))[0][0]
 assert T==C+R
 assert p.mm(p.trans(q),p.mm(F0,q))[0][0]-T==p.mm(p.trans(u),p.mm(F0,u))[0][0]+lam*p.mm(p.trans(y),p.mm(Gy,y))[0][0]-R
 return dict(four_dimensional_nonidentity_metric_noncommuting_signed_residual_identity=True,all_four_trial_coordinates_present=True)
def response(base,columns,F0,Gy,lam,mu,nu,sl,sh,prior,reverse):
 O=[[F(r['coefficient']) for r in c['original']['finite_original_D_action']] for c in columns];A=[[F(r['coefficient']) for r in c['finite_complete_augmented_D_action']] for c in columns]
 Eo=[F(c['original']['complete_original_action_D_error_squared_upper']) for c in columns];Ea=[F(c['augmentation_action_D_error_squared_upper']) for c in columns];sm=(sl+sh)/2
 AG=[[sum((orig.mass(n)*(orig.H(n)+sm)*A[i][n]*A[k][n] for n in range(CUT+1)),F(0)) for k in range(4)] for i in range(4)]
 rhs=[sum((orig.mass(n)*(orig.H(n)+sm)*O[0][n]*A[i][n] for n in range(CUT+1)),F(0)) for i in range(4)];source=sum((orig.mass(n)*(orig.H(n)+sm)*O[0][n]**2 for n in range(CUT+1)),F(0));assert p.psd(AG)
 least_exact=[r[0] for r in p.mm(p.inv(AG),[[v] for v in rhs])];least=[down(v) for v in least_exact]
 twoGram=[row[:3] for row in AG[:3]];two=[r[0] for r in p.mm(p.inv(twoGram),[[v] for v in rhs[:3]])]
 twofit=source-sum((rhs[i]*two[i] for i in range(3)),F(0));threefit=source-sum((rhs[i]*least_exact[i] for i in range(4)),F(0));assert 0<=threefit<=twofit
 GM=[[(F0[i][k][0]+F0[i][k][1]+lam*(Gy[i][k][0]+Gy[i][k][1]))/2 for k in range(4)] for i in range(4)];fm=[(F0[i][0][0]+F0[i][0][1])/2 for i in range(4)];gal=[down(r[0]) for r in p.mm(p.inv(GM),[[v] for v in fm])]
 old=list(map(F,prior['selected_inverse_upper_trial']['trial_coefficients']))+[F(0)];assert len(old)==4
 choices={tuple(old),(F(0),)*4,tuple(least),tuple(gal)}
 for k in range(-10,21):choices.add(tuple(down(old[i]+F(k,10)*(least[i]-old[i])) for i in range(4)))
 for k in range(8,13):
  choices.add(tuple(down(F(k,10)*v) for v in least));choices.add(tuple(down(F(k,10)*v) for v in gal))
 def evaluate(y):
  v=[O[0][n]-sum((y[i]*A[i][n] for i in range(4)),F(0)) for n in range(CUT+1)];terms=[(n,orig.mass(n)*x*x) for n,x in enumerate(v)]
  if reverse:terms.reverse()
  nl=sum((x*(orig.H(n)+sl) for n,x in terms),F(0));nh=sum((x*(orig.H(n)+sh) for n,x in terms),F(0))
  fault=abs(1-y[0])*root(Eo[0])+sum((abs(y[i])*root(Eo[i]) for i in [1,2,3]),F(0))+sum((abs(y[i])*root(Ea[i]) for i in range(4)),F(0))
  rl=down(max(F(0),rootdown(nl)-fault)**2);rh=up((root(nh)+fault)**2);u=[1-y[0],-y[1],-y[2],-y[3]];qlo,qhi=quadratic(F0,u);alo,ahi=quadratic(Gy,y)
  cl=ch=F(0)
  for i in range(4):
   for k in range(4):
    w=(y[k] if i==0 else 0)+(y[i] if k==0 else 0)-y[i]*y[k];a,b=F0[i][k];cl+=min(w*a,w*b);ch+=max(w*a,w*b)
    w=-lam*y[i]*y[k];a,b=Gy[i][k];cl+=min(w*a,w*b);ch+=max(w*a,w*b)
  return dict(trial_coefficients=list(map(str,y)),retained_center_residual_D_energy_lower=str(down(nl)),retained_center_residual_D_energy_upper=str(up(nh)),shared_complete_fault_D_norm_upper=str(up(fault)),actual_residual_D_energy_lower=str(rl),actual_residual_D_energy_upper=str(rh),original_action_inverse_response_lower=str(down(cl+rl/nu)),original_action_inverse_response_upper=str(up(ch+rh/mu)),coupled_signed_gap_lower=str(down(qlo+lam*alo-rh/mu)),coupled_signed_gap_upper=str(up(qhi+lam*ahi-rl/nu)))
 candidates=[evaluate(y) for y in sorted(choices)];lower=max(candidates,key=lambda r:F(r['original_action_inverse_response_lower']));upper=min(candidates,key=lambda r:F(r['original_action_inverse_response_upper']))
 tl=max(F(prior['actual_original_action_inverse_response_lower']),F(lower['original_action_inverse_response_lower']));th=min(F(prior['actual_original_action_inverse_response_upper']),F(upper['original_action_inverse_response_upper']));dl=max(F(prior['actual_signed_gap_lower']),max(F(r['coupled_signed_gap_lower']) for r in candidates),down(F0[0][0][0]-th));dh=min(F(prior['actual_signed_gap_upper']),min(F(r['coupled_signed_gap_upper']) for r in candidates),up(F0[0][0][1]-tl));assert tl<=th and dl<=dh
 return dict(source='N0 P'+str(base),response_trial_basis=['P'+str(base),'P'+str(base+2),'P'+str(base+4),'R'+str(base)],candidate_count=len(candidates),nominal_least_residual_proposal=list(map(str,least)),nominal_Galerkin_proposal=list(map(str,gal)),three_trial_nominal_minimum_retained_Dmid_residual_energy=str(twofit),four_trial_nominal_minimum_retained_Dmid_residual_energy=str(threefit),nominal_fit_is_actual_response_certificate=False,selected_inverse_lower_trial=lower,selected_inverse_upper_trial=upper,actual_original_action_inverse_response_lower=str(tl),actual_original_action_inverse_response_upper=str(th),previous_original_action_inverse_response_upper=prior['actual_original_action_inverse_response_upper'],actual_signed_gap_lower=str(dl),actual_signed_gap_upper=str(dh),previous_signed_gap_lower=prior['actual_signed_gap_lower'],original_action_inverse_upper_improved=th<F(prior['actual_original_action_inverse_response_upper']),signed_gap_lower_improved=dl>F(prior['actual_signed_gap_lower']),signed_gap_positive_certified=dl>0,actual_negative_gap_proved=dh<0)
def run(reverse=False):
 data={}
 for path,sha in sorted(dict(PINS,**HELPER_PINS).items(),reverse=reverse):
  b=(ROOT/path).read_bytes();assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==sha,(path,'pin');data[path]=json.loads(b) if path.endswith('.json') else b.decode()
 get=lambda s:data['certificates/rpb108_rc'+s+'.json']
 prior=get('240_three_trial_signed_response');a243=get('243_residual_augmented_actions');o242=get('242_residual_original_actions');old=get('237_two_trial_signed_response');ref=get('239_exterior_band_leakage');weighted=get('238_weighted_action_tails');baseorig=get('231_original_polynomial_action');baseaug=get('234_materialized_band_action');bounds=get('232_augmented_polynomial_action');metric=get('129_four_vector_joint_moment')
 sl=F(metric['actual_D_Gram_entry_lower'][0][0])/(2*B);sh=F(metric['actual_D_Gram_entry_upper'][0][0])/(2*B);rows=[]
 for base in [0,1]:
  pr=prior['parity_three_trial_signed_response_certificates'][base];rr=ref['parity_exterior_tail_response_certificates'][base];ar=old['parity_two_trial_signed_response_certificates'][base];wr=weighted['parity_weighted_tail_response_certificates'][base];bound=bounds['polynomial_augmented_action_certificates'][base];newaug=a243['parity_residual_augmented_action_certificates'][base];neworig=o242['parity_residual_original_action_certificates'][base]
  lam=F(bound['augmentation_coefficient']);epsilon=F(bound['physical_Fhat_star_Fhat_to_J_star_J_operator_norm_upper']);a=list(map(F,neworig['exact_input_Legendre_coefficients']));columns=[];bandcols=[]
  for k in range(3):
   if k==0:original=deepcopy(baseorig['polynomial_original_action_certificates'][base]);action=baseaug['parity_materialized_augmented_action_certificates'][base]['finite_complete_augmented_D_action'];bandcol=baseaug['parity_materialized_augmented_action_certificates'][base]['actual_band_Gram_column']
   elif k==1:original=deepcopy(ar['new_complete_original_action']);action=ar['new_complete_augmented_D_action'];bandcol=ar['new_band_Gram_column']
   else:original=deepcopy(pr['new_complete_original_action']);action=pr['new_complete_augmented_D_action'];bandcol=pr['new_band_Gram_column']
   if k<2:
    r=rr['action_exterior_tail_refinements'][k];OE=r['original_action_D_error_squared_upper'];AE=r['refined_augmentation_action_D_error_squared_upper'];E=r['refined_complete_augmented_action_D_error_squared_upper'];original['D_energy_component_squared_errors']['endpoint_omitted_output']=wr['action_tail_refinements'][k]['accepted_endpoint_omitted_output_D_energy_upper']
   else:OE=original['complete_original_action_D_error_squared_upper'];AE=pr['new_augmentation_action_D_error_squared_upper'];E=pr['new_complete_augmented_action_D_error_squared_upper']
   original['complete_original_action_D_error_squared_upper']=OE;original['finite_original_D_action']=pad(original['finite_original_D_action'])
   columns.append(dict(original=original,finite_complete_augmented_D_action=pad(action),augmentation_action_D_error_squared_upper=AE,complete_augmented_action_D_error_squared_upper=E));bandcols.append(bandcol)
  original=deepcopy(neworig);original['finite_original_D_action']=original['finite_complete_original_D_action']
  columns.append(dict(original=original,finite_complete_augmented_D_action=newaug['finite_complete_augmented_D_action'],augmentation_action_D_error_squared_upper=newaug['complete_rational_augmentation_action_D_error_squared_upper'],complete_augmented_action_D_error_squared_upper=newaug['complete_augmented_action_D_error_squared_upper']))
  inputs=[]
  for k in range(3):
   v=[F(0)]*65;v[base+2*k]=F(1);inputs.append(v)
  inputs.append(a);masses=[sum((orig.mass(n)*c*c for n,c in enumerate(v)),F(0)) for v in inputs]
  F0=[[(F(0),F(0))]*4 for _ in range(4)];Gy=[[(F(0),F(0))]*4 for _ in range(4)]
  for i in range(3):
   for k in range(3):
    F0[i][k]=tuple(map(F,pr['original_trial_form_intervals'][i][k]));Gy[i][k]=tuple(map(F,pr['frequency_trial_Gram_intervals'][i][k]))
  for i in range(4):
   x=poly_form(inputs[i],columns[3]['original'],sl,sh);y=poly_form(a,columns[i]['original'],sl,sh);v=(max(x[0],y[0]),min(x[1],y[1]));assert v[0]<=v[1];F0[i][3]=F0[3][i]=v
   if i<3:bandlo,bandhi=pair_band(a,bandcols[i])
   else:proof=newaug['aggregate_fourier_leakage_certificate'];bandlo=F(proof['physical_band_energy_lower']);bandhi=F(proof['physical_band_energy_upper'])
   fault=up(epsilon*root(masses[i]*masses[3]));v=(down(bandlo-fault),up(bandhi+fault));Gy[i][3]=Gy[3][i]=v
  assert F0[3][3]==(F(neworig['original_test_form_lower']),F(neworig['original_test_form_upper']))
  FL,FH=loewner(F0);YL,YH=loewner(Gy);GL=p.add(FL,p.scale(lam,YL));GH=p.add(FH,p.scale(lam,YH))
  assert p.psd(YL) and p.inv(YL) and p.psd(GL) and p.inv(GL)
  result=response(base,columns,F0,Gy,lam,F(bound['fresh_augmented_N_D_lower']),F(bound['fresh_augmented_N_D_upper']),sl,sh,pr['source_inverse_response'],reverse)
  errors=[[str(4*F(columns[i]['complete_augmented_action_D_error_squared_upper'])) if i==k else '0' for k in range(4)] for i in range(4)]
  rows.append(dict(parity=pr['parity'],response_trial_basis=['P'+str(base),'P'+str(base+2),'P'+str(base+4),'R'+str(base)],original_trial_form_intervals=[[[str(a),str(b)] for a,b in row] for row in F0],frequency_trial_Gram_intervals=[[[str(a),str(b)] for a,b in row] for row in Gy],original_trial_form_Loewner_lower=p.ser(FL),original_trial_form_Loewner_upper=p.ser(FH),frequency_trial_Gram_Loewner_lower=p.ser(YL),frequency_trial_Gram_Loewner_upper=p.ser(YH),augmented_trial_form_Loewner_lower=p.ser(GL),augmented_trial_form_Loewner_upper=p.ser(GH),complete_four_trial_action_error_D_Gram_upper=errors,source_inverse_response=result,old_degree_64_centers_padded_by_exact_zeros=True,padding_does_not_claim_old_omitted_output_zero=True,old_three_trial_form_blocks_preserved=True))
 return dict(milestone='RC244',starting_commit='43522d039f456eace818be86cee8544d585addca',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,actual_response_source_count=2,actual_response_source_order=['N0 P0','N0 P1'],response_trials_per_parity=4,retained_joint_action_center_degree=128,parity_four_trial_signed_response_certificates=rows,exact_controls=controls(),all_same_parity_cross_terms_paid=True,same_parity_action_errors_assumed_orthogonal=False,shared_source_original_action_error_coupled=True,full_action_errors_preserved_when_centers_zero_padded=True,new_response_enclosures_intersected_with_RC240=True,RC241_obstruction_scope_remains_fixed_three_trial_interface=True,full_639_signed_response_matrix_evaluated=False,full_signed_gap_positive_certified=False,original_full_auxiliary_norm_below_one_certified=False,finite_eight_canonical_inverse_width_preserved='485647/1000000',Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC245: reduce remaining residual action errors or build the next residual-shaped actions; full signed positivity remains required')
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--replay',action='store_true');a=ap.parse_args();c=run(a.replay)
 if a.replay:assert c==json.loads(a.output.read_text())
 else:a.output.write_text(json.dumps(c,sort_keys=True,indent=2)+'\n')
 print('RC244 VALIDATED: paid four-trial signed responses; full signed gate open',flush=True)

