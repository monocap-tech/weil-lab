"""RC205: exact inverse transport of RC204's fixed-trial signed error envelope.
Numerical optimization proposes positive rational Young parameters only.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse, hashlib, json, math
from validate_rpb108_rc127_enriched_even_endpoint_action import psd,ser,down
from validate_rpb108_rc129_four_vector_joint_moment import cong,add
from validate_rpb108_rc177_three_source_canonical_action_gram import mat,scale,width
from validate_rpb108_rc204_signed_error import certify as signed_certify, BETA

ROOT=Path(__file__).resolve().parents[1]
PINS={
 'certificates/rpb108_rc203_residual_enriched_six_source_inverse.json':'5d321b659367ba459682b557b12ef63451f63e49',
 'certificates/rpb108_rc121_diagonal_metric_equivalence.json':'089664ca7eb9139fec1ba0f58b4cfbf25902f51a',
}
HELPER_PINS={"scripts/validate_rpb108_rc127_enriched_even_endpoint_action.py": "d5d82bf70c1a178f0fe1da61f27b8623e42ed361", "scripts/validate_rpb108_rc129_four_vector_joint_moment.py": "1229dc4a9db7509b9f6afea7116349891b618f4c", "scripts/validate_rpb108_rc134_correlated_six_input_covariance.py": "ac0d5ba0acb48182f0eed3ef452ddca1fbef2f0e", "scripts/validate_rpb108_rc177_three_source_canonical_action_gram.py": "d9d0575e6dda8e0b6f66ffaf83d0474b2715ba5b", "scripts/validate_rpb108_rc204_signed_error.py": "5362ddfbfaf443875fa7914aa90bb00b58b00281"}
def blob(b):return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()

def context(prior,trial):
    Y=mat(trial,'trial_basis_coefficients');UG=cong(Y,mat(prior,'raw_trial_D_Gram_Loewner_upper'))
    pay=mat(trial,'variational_uncertainty_payment')
    baseLo=add(mat(trial,'variational_response_lower'),pay);baseHi=add(mat(trial,'variational_response_upper'),pay,-1)
    E=mat(trial,'adaptive_action_error_Gram_upper');theta=F(trial['selected_action_theta']);tt=F(trial['selected_tail_theta'])
    Utail=mat(trial,'trial_source_tail_Gram_upper');Rtail=mat(trial,'nominal_residual_tail_Gram_upper')
    rebuilt=add(add(scale(theta,UG),scale(1/(4*theta),E)),add(scale(tt,Utail),scale(1/(4*tt),Rtail)))
    assert rebuilt==pay
    return dict(UG=UG,baseLo=baseLo,baseHi=baseHi,Utail=Utail,Rtail=Rtail,Nlo=mat(trial,'nominal_residual_Gram_lower'),Nhi=mat(trial,'nominal_residual_Gram_upper'))

def discover(c,E,a,G,trial):
    import numpy as np
    from scipy.linalg import eigh
    from scipy.optimize import minimize
    array=lambda A:np.array([[float(x) for x in row] for row in A])
    ev,V=eigh(array(G));assert min(ev)>0
    W=V@np.diag(1/np.sqrt(ev));wh=lambda A:W.T@array(A)@W
    UG,ut,rt,N,e,gap=map(wh,[c['UG'],c['Utail'],c['Rtail'],c['Nhi'],E,add(c['baseHi'],c['baseLo'],-1)])
    def objective(z):
        theta,tau,tt=map(math.exp,z)
        full=gap+2*theta*UG+e/(2*theta)+2*tt*ut+rt/(2*tt)+((1+tau)*N+(1+1/tau)*e)/float(a)
        return float(np.linalg.eigvalsh((full+full.T)/2)[-1])
    z=np.array([math.log(float(F(trial[k]))) for k in ['selected_action_theta','selected_upper_tau','selected_tail_theta']])
    proposals=[]
    def record(z,label):
        vals=[down(F(math.exp(t)),10**12) for t in z];assert min(vals)>0
        proposals.append(dict(label=label,action_theta=str(vals[0]),residual_tau=str(vals[1]),tail_theta=str(vals[2])))
    record(z,'inherited_parameters')
    for method in ['Powell','SLSQP']:
        res=minimize(objective,z,method=method,bounds=[(-12,0),(-6,3),(-6,3)],options={'maxiter':1500,'ftol':1e-11})
        record(res.x,method);print('RC205 proposal',method,objective(res.x),flush=True);z=res.x
    return proposals

def run(reverse=False,proposals=None):
    for path,sha in HELPER_PINS.items():
        assert blob((ROOT/path).read_bytes())==sha,(path,"validator Git blob mismatch")
    data={}
    for path,sha in PINS.items():
        raw=(ROOT/path).read_bytes();assert blob(raw)==sha,(path,'Git blob mismatch');data[path]=json.loads(raw)
    prior=data[next(iter(PINS))];metric=data['certificates/rpb108_rc121_diagonal_metric_equivalence.json']
    proof=signed_certify(ROOT/next(iter(PINS)),reverse)
    assert proof['selected_uniform_squared_error_factor']==str(BETA)
    assert prior['selected_trial']=='least_residual' and prior['milestone']=='RC203'
    trial=prior['selected_enclosure'];G=mat(prior,'source_D_Gram_lower');a=F(metric['actual_canonical_diagonal_metric_lower'])
    assert a>0 and psd(G)
    c=context(prior,trial);E=scale(BETA,G)
    inheritedLo=mat(trial,'canonical_inverse_response_lower');inheritedHi=mat(trial,'canonical_inverse_response_upper')
    if proposals is None:proposals=discover(c,E,a,G,trial)
    candidates=[]
    for p in proposals[::-1] if reverse else proposals:
        theta,tau,tt=[F(p[k]) for k in ['action_theta','residual_tau','tail_theta']];assert min(theta,tau,tt)>0
        actionPay=add(scale(theta,c['UG']),scale(1/(4*theta),E))
        tailPay=add(scale(tt,c['Utail']),scale(1/(4*tt),c['Rtail']));pay=add(actionPay,tailPay)
        Clo=add(c['baseLo'],pay,-1);Chi=add(c['baseHi'],pay)
        Rhi=add(scale(1+tau,c['Nhi']),scale(1+1/tau,E));upper=add(Chi,scale(1/a,Rhi))
        sigmas=[F(0),F(1,30),F(1,10),F(1,3),F(1,2)]
        for sigma in sigmas[::-1] if reverse else sigmas:
            Rlo=scale(F(0),G) if sigma==0 else add(scale(1-sigma,c['Nlo']),scale(-(1/sigma-1),E))
            if not psd(Rlo):continue
            lower=add(Clo,scale(F(1,2),Rlo))
            for ln,lc in [('refined',lower),('inherited',inheritedLo)]:
                for hn,hc in [('refined',upper),('inherited',inheritedHi)]:
                    gap=add(hc,lc,-1)
                    if not psd(lc) or not psd(gap):continue
                    beta=width(gap,G);gate=add(scale(F(1,2),G),gap,-1)
                    assert psd(add(scale(beta,G),gap,-1))
                    candidates.append(dict(proposal_label=p['label'],selected_action_theta=str(theta),selected_tail_theta=str(tt),selected_upper_tau=str(tau),selected_lower_tau=str(sigma),selected_lower_type=ln,selected_upper_type=hn,variational_action_payment=ser(actionPay),variational_tail_payment=ser(tailPay),variational_response_lower=ser(Clo),variational_response_upper=ser(Chi),relative_variational_width_upper=str(width(add(Chi,Clo,-1),G)),actual_residual_Gram_lower=ser(Rlo),actual_residual_Gram_upper=ser(Rhi),canonical_inverse_response_lower=ser(lc),canonical_inverse_response_upper=ser(hc),relative_inverse_width_upper=str(beta),half_Gram_gate_matrix=ser(gate),half_Gram_gate_passed=psd(gate)))
    selected=min(candidates,key=lambda r:(F(r['relative_inverse_width_upper']),r['proposal_label'],F(r['selected_lower_tau']),r['selected_lower_type'],r['selected_upper_type']))
    beta=F(selected['relative_inverse_width_upper']);old=F(prior['relative_inverse_width_upper']);assert beta<=old
    return dict(milestone='RC205',starting_commit='e2f28614ebf037efa7db567afc57d2ddb103665a',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,RC204_signed_controls_rebuilt=128,RC204_positive_integer_minors_rebuilt=768,source_D_Gram_lower=prior['source_D_Gram_lower'],source_D_Gram_upper=prior['source_D_Gram_upper'],response_source_order=prior['response_source_order'],raw_trial_basis_order=prior['raw_trial_basis_order'],selected_trial='least_residual',trial_basis_coefficients=trial['trial_basis_coefficients'],signed_action_error_Gram_upper=ser(E),signed_action_error_relative_factor=str(BETA),rational_parameter_proposals=proposals,selected_enclosure=selected,relative_inverse_width_upper=str(beta),previous_same_family_width_upper=str(old),certified_acceptance_ratio_upper=str(2*beta),certified_gate_margin_lower=str(F(1,2)-beta),canonical_half_Gram_inverse_width_gate_passed=selected['half_Gram_gate_passed'],source_trial_action_and_nominal_residual_data_unchanged=True,complete_signed_tail_data_retained=True,complex_response_mixtures_paid=True,numerical_optimization_used_only_for_parameter_proposals=True,acceptance_and_enclosure_verified_by_exact_rational_PSD=True,Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='refine six-source variational/cross-tail enclosure if gate remains open; native action coverage remains subsequent')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);p.add_argument('--replay',action='store_true');args=p.parse_args()
    expected=json.loads(args.output.read_text()) if args.replay else None
    result=run(args.replay,None if expected is None else expected['rational_parameter_proposals'])
    if args.replay:assert result==expected,'exact reversed-order replay differs'
    else:args.output.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print('RC205 PASS: inverse width',result['relative_inverse_width_upper'],'half-Gram gate',result['canonical_half_Gram_inverse_width_gate_passed'])
