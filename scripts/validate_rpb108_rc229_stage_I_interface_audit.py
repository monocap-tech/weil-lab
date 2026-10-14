"""RC229: exact native-frame transfer, parity witness, and Stage I scope audit."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
import validate_rpb108_rc228_twelve_trial_inverse as parent
p=parent.p;ROOT=Path(__file__).resolve().parents[1]
PINS=dict(parent.PINS);HELPER_PINS=dict(parent.HELPER_PINS)
PINS.update({'certificates/rpb108_rc228_twelve_trial_inverse.json':'ff3525870ad34c37b5836f19fdd52debc346760a','certificates/rpb108_rc228_materialized_prefix_interface.json':'ccdd43ff98a7b4f1e588af9fda647d8fd6695b7c','certificates/rpb108_rc112_parity_spectral_coverage.json':'d0155c1a15d5a98f17df42d25168c10b4bd7aef4','certificates/rpb108_rc114_positive_augmentation.json':'609d7770e2a5a16e407a0a41903ac1e349b5c144','notes/RPB108_RC112_PARITY_SPECTRAL_COVERAGE_AND_CERTIFIED_STRONG_FLOOR_20261011.md':'ea61a1237c5953c564e9ba9855d596ba37ff9e73','notes/RPB108_RC114_PROJECTION_FREE_POSITIVE_AUGMENTATION_AND_FINITE_RESPONSE_20261011.md':'a62b95e03ce6c02fa5c6f1d79e535ad1d35dc925','notes/RPB108_RC115_RATIONAL_FOURIER_ADJOINT_SOURCE_CONSTRUCTION_20261012.md':'bf0a21926acdf51d515a0cab0676cc02aa3f85fd','notes/RPB108_RC121_GLOBAL_DIAGONAL_METRIC_EQUIVALENCE_20261012.md':'9b33ea3bb19240dc20bcd1a83a0f623e692ca772','notes/RPB108_RC136_SEVEN_VECTOR_JOINT_MATRICES_20261012.md':'95cdec39bc144f2fb41411e7c2e98d3094862c2e'})
HELPER_PINS['scripts/validate_rpb108_rc228_twelve_trial_inverse.py']='2125d6dc0d7ede94220f2ce4d0daf443cd225f45'
def run(reverse=False):
 data={}
 for path,sha in sorted(dict(PINS,**HELPER_PINS).items(),reverse=reverse):
  raw=(ROOT/path).read_bytes();assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==sha,(path,'pin')
  data[path]=json.loads(raw) if path.endswith('.json') else raw.decode()
 get=lambda name:data['certificates/rpb108_rc'+name+'.json']
 c=get('228_twelve_trial_inverse');interface=get('228_materialized_prefix_interface');coverage=get('112_parity_spectral_coverage');aug=get('114_positive_augmentation')
 assert c['response_source_count']==8 and c['inverse_trial_count']==12 and c['canonical_half_Gram_inverse_width_gate_passed']
 G=p.mat(c,'source_D_Gram_lower');GH=p.mat(c,'source_D_Gram_upper');L=p.mat(c['selected_enclosure'],'inverse_response_lower');H=p.mat(c['selected_enclosure'],'inverse_response_upper');gap=p.add(H,L,-1);beta=F(c['relative_inverse_width_upper']);margin=F(1,2)-beta
 assert beta==F(485647,10**6) and margin>0 and p.psd(L) and p.psd(gap) and p.psd(p.add(p.scale(beta,G),gap,-1)) and p.psd(p.add(p.scale(F(1,2),G),gap,-1))
 assert c['selected_enclosure']['lower_type']==c['selected_enclosure']['upper_type']=='coupled'
 # Native seven-frame: P0,psi,f,w,v,z,t. z=v+delta is an exact SOURCE
 # identity. Congruence transfers the new enclosure, not old z action radii.
 assert get('214_correlated_difference_canonical_action')['native_source'].startswith('delta=z_b6-v10, unchanged native')
 T=[[F(0)]*7 for _ in range(8)]
 for j,i in enumerate([0,3,2,4,5,6,7]):T[i][j]=F(1)
 T[5][5]=F(1)
 NG=p.cong(T,G);NL=p.cong(T,L);NH=p.cong(T,H);Ngap=p.add(NH,NL,-1)
 assert p.psd(NG) and p.inv(NG) and p.psd(p.add(p.scale(beta,NG),Ngap,-1)) and p.psd(p.add(p.scale(F(1,2),NG),Ngap,-1))
 native=get('218_materialized_native_carriers');assert all(r['degree']%2==0 for k in ['delta_finite_rows','t10_finite_center_radius_rows'] for r in native[k])
 for name,key in [('185_five_source_focus_action','finite_focus_direction'),('202_six_source_residual_action','finite_focus_direction'),('220_barrier_residual_action','finite_focus_direction'),('227_new_residual_trial_action','finite_focus_direction')]:assert all(r['degree']%2==0 for r in get(name)[key])
 assert c['conditioned_response_source_order']==['P0','P2','f0','psi0','w14','v10','delta=z_b6-v10','t10']
 B=F(11,10);sl=F(get('129_four_vector_joint_moment')['actual_D_Gram_entry_lower'][0][0])/(2*B);oddNorm=2*B*(1+sl)/3;assert oddNorm>0
 assert coverage['explicit_exceptional_space_dimension']==639 and coverage['inherited_effective_strong_dimension']==611
 dimensions={r['parity']:r['parity_exceptional_dimension'] for r in coverage['parity_coverage_certificates']};assert dimensions==dict(even=248,odd=391)
 assert F(coverage['original_floor_on_canonical_exceptional_orthogonal_complement'])==F(5001251,500000000)>F(1,100)
 assert aug['finite_auxiliary_response_rank_upper']==639 and aug['positive_augmentation_of_full_original_operator_certified'] and not aug['auxiliary_response_norm_below_one_certified']
 # Exact abstract control, not an arithmetic Weil counterexample: the
 # canonical inverse and an eight-dimensional augmentation restriction
 # pass, while the unseen odd original direction is negative.
 MQ=p.zeros(9);HQ=p.zeros(9);QQ=p.zeros(9)
 for i in range(9):MQ[i][i]=HQ[i][i]=F(1);QQ[i][i]=F(1,2) if i<8 else F(3,2)
 BB=p.mm(p.trans(QQ),QQ);AQ=p.add(HQ,BB,-1);restriction=[row[:8] for row in BB[:8]]
 assert p.psd(MQ) and p.inv(MQ)==MQ and p.psd(p.add(p.scale(F(1,2),[row[:8] for row in MQ[:8]]),p.zeros(8),-1)) and p.psd(p.add([row[:8] for row in HQ[:8]],restriction,-1))
 assert BB[8][8]==F(9,4) and AQ[8][8]==-F(5,4) and not p.psd(AQ)
 obligations=[dict(id='original_operator_action',status='open',required='Actual original Weil A_Q or augmented H/Hhat actions, with prime, signed pole and augmentation errors; canonical metric L actions are not those actions.'),dict(id='full_augmentation_source_range',status='open',required='A proved factorization/exhaustive range or a uniformly paid discarded-range bound for the chosen original augmentation; no eight-source exhaustiveness follows from trial count.'),dict(id='odd_response_realization',status='open',required='Actual odd canonical source/action/inverse responses for the chosen augmentation; retain the established odd complement and source-construction results.'),dict(id='auxiliary_metric',status='open',required='Frequency Gram or an equivalent metric-free full-range operator bound, including factor, rounding and truncation errors.'),dict(id='original_response_norm',status='open',required='For a fixed chosen H and Q, certify Q H^-1 Q* <= (1-zeta) I_aux with zeta>0, or an equivalent complete signed original Schur certificate. The augmentation residual is added.'),dict(id='Stage_I_assembly',status='open',required='Compose the native source/metric, actual original action, both parity, full response and positivity contracts in their exact norms and domains.')]
 return dict(milestone='RC229',starting_commit='80d52fc70f5b61008f36413457ca91c0dbf2f9ce',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,accepted_eight_source_inverse_width=str(beta),accepted_gate_margin=str(margin),accepted_gate_exactly_rechecked=True,source_count=8,trial_count=12,native_seven_source_order=['P0','psi0','f0','w14','v10','z_b6','t10'],native_seven_source_embedding=p.ser(T),native_seven_source_Gram_lower=p.ser(NG),native_seven_source_inverse_lower=p.ser(NL),native_seven_source_inverse_upper=p.ser(NH),native_seven_source_relative_inverse_width_upper=str(beta),native_seven_source_gate_transferred_by_exact_congruence=True,old_independent_z_action_radii_reused=False,all_tested_sources_and_trials_even=True,odd_P1_D_energy_lower=str(oddNorm),odd_P1_pairings_with_every_tested_source=['0']*8,odd_P1_outside_tested_span_proved=True,original_exceptional_head_dimension=639,inherited_effective_strong_dimension=611,original_complement_floor=str(F(5001251,500000000)),original_native_parity_head_dimensions=dimensions,tested_metric_operator='M=D^-1 L, with L the canonical Fourier metric action',original_operator='A_Q=I+i* K i',chosen_augmentation_required='H=A_Q+Q*Q, or a separately paid rational Hhat',operator_identity_L_equals_A_Q_or_H_claimed=False,abstract_nonimplication_control=dict(canonical_inverse_width='0',restricted_eight_auxiliary_response_upper='1/4',hidden_odd_auxiliary_response='9/4',hidden_odd_original_form='-5/4',is_actual_Weil_counterexample=False),remaining_obligations=obligations,minimum_additional_source_or_trial_count_claimed=False,dense_639_response_evaluation_required=False,existing_odd_spectral_coverage_rejected=False,Stage_I_closed=False,original_augmented_response_norm_below_one_certified=False,RH=False,F4=False,Lean=False,next_cursor='RC230: establish the chosen original augmentation source-range/operator interface, then certify odd source/action responses and the auxiliary metric; retain the passed canonical inverse gate rather than repeat its parameter tuning')
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--replay',action='store_true');a=ap.parse_args();result=run(a.replay)
 if a.replay:assert result==json.loads(a.output.read_text())
 else:a.output.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
 print('RC229 PASS: native-seven gate transferred; odd/source-range and original augmentation obligations remain open',flush=True)
