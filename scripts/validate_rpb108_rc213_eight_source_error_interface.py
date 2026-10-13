"""RC213: expanded native-plus-P2 Gram and complete marginal action-error interface."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,hashlib
from validate_rpb108_rc127_enriched_even_endpoint_action import B,loewner,psd,ser,up,down,sqrtup
from validate_rpb108_rc129_four_vector_joint_moment import inv,add
ROOT=Path(__file__).resolve().parents[1]
PINS={'certificates/rpb108_rc136_seven_vector_joint_matrices.json': '84ed91819c32053ae78caf340758e7d0c07a9568', 'certificates/rpb108_rc129_four_vector_joint_moment.json': '33e681e688450c987993603354544fe3919b435f', 'certificates/rpb108_rc183_materialized_w14_canonical_carrier.json': '4469fa1b92e6e1e9f08598ce707cfb43b240784a', 'certificates/rpb108_rc211_native_z_canonical_action.json': 'c31df9de830b60938ae0bf2aedde50d90ab52a7b', 'certificates/rpb108_rc212_native_t10_canonical_action.json': '442f9963189a32fa8185daf5558e0673753ed0f1', 'certificates/rpb108_rc203_residual_enriched_six_source_inverse.json': '5d321b659367ba459682b557b12ef63451f63e49', 'certificates/rpb108_rc210_collective_regular_inverse.json': '01ebe8d6f490476ddbcf2fdb80a1a2d768504a06'}
HELPER_PINS={'scripts/validate_rpb108_rc127_enriched_even_endpoint_action.py': 'd5d82bf70c1a178f0fe1da61f27b8623e42ed361', 'scripts/validate_rpb108_rc129_four_vector_joint_moment.py': '1229dc4a9db7509b9f6afea7116349891b618f4c'}
def blob(raw):return hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
def run(reverse=False):
    for path,sha in HELPER_PINS.items():assert blob((ROOT/path).read_bytes())==sha,(path,'helper Git blob mismatch')
    data={}
    for path,sha in PINS.items():
        raw=(ROOT/path).read_bytes();assert blob(raw)==sha,(path,'input Git blob mismatch');data[path]=json.loads(raw)
    get=lambda name:data['certificates/rpb108_rc'+name+'.json']
    n=get('136_seven_vector_joint_matrices');j=get('129_four_vector_joint_moment');w=get('183_materialized_w14_canonical_carrier');z=get('211_native_z_canonical_action');t=get('212_native_t10_canonical_action');b=get('203_residual_enriched_six_source_inverse');accepted=get('210_collective_regular_inverse')
    assert z['complete_native_z_canonical_action_certified'] and t['complete_native_t10_canonical_action_certified']
    assert accepted['canonical_half_Gram_inverse_width_gate_passed'] and accepted['relative_inverse_width_upper']=='4361/10000'
    sl=F(j['actual_D_Gram_entry_lower'][0][0])/(2*B);sh=F(j['actual_D_Gram_entry_upper'][0][0])/(2*B);coeff=[F(0),F(0),F(0),F(w['native_w14_finite_coefficient_centers'][1]),F(w['Cg_finite_coefficient_centers'][1]),F(z['native_source_low_prefix'][1]['center']),F(t['native_source_low_prefix'][1]['center'])]
    L=[[F(v) for v in row]+[F(0)] for row in n['finite_prefix_Gram_entry_lower']]+[[F(0)]*8];H=[[F(v) for v in row]+[F(0)] for row in n['finite_prefix_Gram_entry_upper']]+[[F(0)]*8];AH=[[F(v) for v in row]+[F(0)] for row in n['actual_D_Gram_entry_upper']]+[[F(0)]*8]
    for i in range(7):
     lo=F(2*B,6) if i==2 else 2*B/5*(sl+F(3,2))*coeff[i];hi=F(2*B,6) if i==2 else 2*B/5*(sh+F(3,2))*coeff[i]
     L[i][7]=L[7][i]=lo;H[i][7]=H[7][i]=AH[i][7]=AH[7][i]=hi
    L[7][7]=2*B/5*(sl+F(3,2));H[7][7]=AH[7][7]=2*B/5*(sh+F(3,2))
    G,_,_=loewner(L,H,[F(1)]*8);_,U,_=loewner(L,AH,[F(1)]*8);assert psd(G)
    scale=10**50;floor=[[F(x.numerator*scale//x.denominator-(8 if i==k else 0),scale) for k,x in enumerate(row)] for i,row in enumerate(G)];assert psd(floor);K=inv(floor)
    eps=list(map(F,b['individual_raw_trial_action_error_norm_upper']));eps=[eps[i] for i in [0,3,2,4,6]]+[F(z['complete_canonical_z_action_D_error_norm_upper']),F(t['complete_canonical_t10_action_D_error_norm_upper']),eps[1]]
    worst=F(0);maskworst=0;controls=[]
    order=list(range(128))
    if reverse:order.reverse()
    for mask in order:
     v=[eps[i]*(1 if i==0 or mask>>(i-1)&1 else -1) for i in range(8)];q=sum(v[i]*K[i][k]*v[k] for i in range(8) for k in range(8))
     controls.append(dict(mask=mask,rank_one_relative_factor=str(q)))
     if q>worst or (q==worst and mask<maskworst):worst=q;maskworst=mask

    assert min(eps)>0
    # G-floor has diagonal >=8/scale and off-diagonal absolute defects <1/scale.
    # Strict diagonal dominance makes the symmetric defect positive definite.
    assert all(G[i][i]-floor[i][i]>=F(8,scale) for i in range(8))
    assert all(abs(G[i][k]-floor[i][k])<F(1,scale) for i in range(8) for k in range(8) if i!=k)
    assert psd(add(G,floor,-1))
    beta=up(worst,10**6);assert beta>=worst
    controls.sort(key=lambda c:c['mask'])
    for c in controls:assert F(c['rank_one_relative_factor'])<=beta
    sign=[1 if i==0 or maskworst>>(i-1)&1 else -1 for i in range(8)];wv=[eps[i]*sign[i] for i in range(8)];x=[sum(K[i][k]*wv[k] for k in range(8)) for i in range(8)]
    q=lambda A:sum(x[i]*A[i][k]*x[k] for i in range(8) for k in range(8))
    rank=worst*worst;gram=q(floor);assert gram==worst
    control_gate=gram/2-rank;assert control_gate<0
    # These are absolute error payments for a future mixed-row enclosure;
    # no nominal pairing centers or actual inverse endpoints are fabricated.
    norms=[sqrtup(U[i][i]) for i in range(8)]
    sourcePay=[[up(norms[i]*eps[k]) for k in range(8)] for i in range(8)]
    actionPay=[[up(2*norms[i]*eps[k]+2*norms[k]*eps[i]+eps[i]*eps[k]) for k in range(8)] for i in range(8)]
    return dict(milestone='RC213',starting_commit='39cec66481545e1996a8f160797175e76e9f0e78',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,response_source_order=['P0','psi0','f0','w14','v10','z_b6','t10','P2'],native_source_count=7,auxiliary_P2_included=True,expanded_family_dimension=8,source_finite_prefix_last_degree=16382,expanded_source_D_Gram_lower=ser(G),expanded_source_D_Gram_upper=ser(U),source_D_Gram_rational_floor=ser(floor),source_Gram_floor_scale=scale,eight_response_source_independence_certified=True,full_source_and_infinite_analytic_Gram_tails_paid=True,complete_canonical_column_error_norm_upper=list(map(str,eps)),signed_rank_one_control_count=128,signed_rank_one_controls=controls,exact_worst_signed_error_factor=str(worst),certified_independent_marginal_error_factor_upper=str(beta),worst_signed_mask=maskworst,half_Gram_marginal_action_error_test_passed=False,failed_rank_one_half_Gram_probe_coefficients=list(map(str,x)),failed_rank_one_half_Gram_probe_value=str(control_gate),source_action_pairing_absolute_error_payment=ser(sourcePay),represented_action_pairing_absolute_error_payment=ser(actionPay),all_64_pairing_error_payments_supplied=True,complex_response_mixtures_paid=True,error_correlation_or_orthogonality_assumed=False,true_action_error_lower_bound_inferred=False,actual_operator_or_inverse_failure_inferred=False,expanded_inverse_response_evaluated=False,accepted_six_source_inverse_width_unchanged='4361/10000',accepted_six_source_half_Gram_margin_unchanged='639/10000',Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC214: certify correlated common/difference canonical action bounds, especially z_b6-v10; then assemble enlarged nominal mixed/residual rows and test the expanded inverse separately')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);p.add_argument('--replay',action='store_true');a=p.parse_args();result=run(a.replay)
    if a.replay:assert json.loads(a.output.read_text())==result
    else:a.output.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print('RC213 PASS: eight-source Gram independent; marginal error factor',result['certified_independent_marginal_error_factor_upper'],'expanded inverse untested')
