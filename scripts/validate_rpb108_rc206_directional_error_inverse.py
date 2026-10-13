"""RC206: convex directional/signed error envelopes on fixed RC203 trials."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json,math
import validate_rpb108_rc205_signed_error_inverse as prev
from validate_rpb108_rc127_enriched_even_endpoint_action import psd,ser,down
from validate_rpb108_rc129_four_vector_joint_moment import cong,add
from validate_rpb108_rc177_three_source_canonical_action_gram import mat,scale,width
from validate_rpb108_rc204_signed_error import certify as signed_certify,BETA
ROOT=Path(__file__).resolve().parents[1]
PINS=dict(prev.PINS)
PINS['certificates/rpb108_rc205_signed_error_inverse.json']='460cad6cf77581db35662204d319ab30c9c1c2c7'
HELPER_PINS=dict(prev.HELPER_PINS)
HELPER_PINS['scripts/validate_rpb108_rc205_signed_error_inverse.py']='2953a3b86fc7560b31ec02c6761483d4f6c39fc1'
def outer(v):return [[x*y for y in v] for x in v]
def error_gram(Y,eps,w):
    assert len(w)==len(eps)==8 and min(w)>0
    factor=sum(eps[k]/w[k] for k in range(8))
    diagonal=[[factor*eps[i]*w[i] if i==j else F(0) for j in range(8)] for i in range(8)]
    assert psd(add(diagonal,outer(eps),-1))
    return cong(Y,diagonal)

def discover(c,Y,eps,G,a,trial,prior):
    import numpy as np
    from scipy.linalg import eigh
    from scipy.optimize import minimize
    array=lambda A:np.array([[float(x) for x in row] for row in A])
    ev,V=eigh(array(G));assert min(ev)>0
    W=V@np.diag(1/np.sqrt(ev));wh=lambda A:W.T@array(A)@W
    UG,ut,rt,N,gap=map(wh,[c['UG'],c['Utail'],c['Rtail'],c['Nhi'],add(c['baseHi'],c['baseLo'],-1)])
    y=array(Y)@W;es=np.array(list(map(float,eps)))
    baseline=np.array([float(F(s)) for s in trial['adaptive_triangle_weights']])
    def objective(z):
        w=baseline*np.exp(z[:8]);mix=z[8];theta,tau,tt=map(math.exp,z[9:])
        e=mix*(es/w).sum()*((y.T*(es*w))@y)+(1-mix)*float(BETA)*np.eye(6)
        full=gap+2*theta*UG+e/(2*theta)+2*tt*ut+rt/(2*tt)+((1+tau)*N+(1+1/tau)*e)/float(a)
        return float(np.linalg.eigvalsh((full+full.T)/2)[-1])
    proposals=[]
    def record(z,label):
        w=[down(F(float(baseline[k]*math.exp(z[k]))),10**12) for k in range(8)]
        mix=down(F(float(z[8])),10**12);pars=[down(F(math.exp(x)),10**12) for x in z[9:]]
        assert min(w+pars)>0 and 0<=mix<=1
        proposals.append(dict(label=label,triangle_weights=list(map(str,w)),triangle_mix=str(mix),action_theta=str(pars[0]),residual_tau=str(pars[1]),tail_theta=str(pars[2])))
    inherited=prior['selected_enclosure']
    z=np.array([0.]*8+[0.]+[math.log(float(F(inherited[k]))) for k in ['selected_action_theta','selected_upper_tau','selected_tail_theta']])
    record(z,'RC205_signed_parameters')
    z[8]=1
    bounds=[(-6,6)]*8+[(0,1),(-12,0),(-6,3),(-6,3)]
    for method in ['Powell','SLSQP']:
        res=minimize(objective,z,method=method,bounds=bounds,options={'maxiter':1500,'ftol':1e-11})
        record(res.x,method);print('RC206 proposal',method,objective(res.x),'mix',res.x[8],flush=True);z=res.x
    return proposals

def run(reverse=False,proposals=None):
    for path,sha in HELPER_PINS.items():assert prev.blob((ROOT/path).read_bytes())==sha,(path,'validator Git blob mismatch')
    data={}
    for path,sha in PINS.items():
        raw=(ROOT/path).read_bytes();assert prev.blob(raw)==sha,(path,'input Git blob mismatch');data[path]=json.loads(raw)
    base=data['certificates/rpb108_rc203_residual_enriched_six_source_inverse.json'];prior=data['certificates/rpb108_rc205_signed_error_inverse.json'];metric=data['certificates/rpb108_rc121_diagonal_metric_equivalence.json']
    assert prior['milestone']=='RC205' and prior['relative_inverse_width_upper']=='90089/125000'
    signed=signed_certify(ROOT/'certificates/rpb108_rc203_residual_enriched_six_source_inverse.json',reverse)
    assert signed['selected_uniform_squared_error_factor']==str(BETA)
    trial=base['selected_enclosure'];assert trial['trial']=='least_residual'
    G=mat(base,'source_D_Gram_lower');Y=mat(trial,'trial_basis_coefficients');eps=list(map(F,base['individual_raw_trial_action_error_norm_upper']))
    c=prev.context(base,trial);a=F(metric['actual_canonical_diagonal_metric_lower']);assert a>0
    inheritedLo=mat(prior['selected_enclosure'],'canonical_inverse_response_lower');inheritedHi=mat(prior['selected_enclosure'],'canonical_inverse_response_upper')
    if proposals is None:proposals=discover(c,Y,eps,G,a,trial,prior)
    candidates=[]
    for p in proposals[::-1] if reverse else proposals:
        w=list(map(F,p['triangle_weights']));mix=F(p['triangle_mix']);assert 0<=mix<=1
        theta,tau,tt=[F(p[k]) for k in ['action_theta','residual_tau','tail_theta']];assert min(theta,tau,tt)>0
        tri=error_gram(Y,eps,w);E=add(scale(mix,tri),scale(1-mix,scale(BETA,G)));assert psd(E)
        actionPay=add(scale(theta,c['UG']),scale(1/(4*theta),E));tailPay=add(scale(tt,c['Utail']),scale(1/(4*tt),c['Rtail']));pay=add(actionPay,tailPay)
        Clo=add(c['baseLo'],pay,-1);Chi=add(c['baseHi'],pay);Rhi=add(scale(1+tau,c['Nhi']),scale(1+1/tau,E));upper=add(Chi,scale(1/a,Rhi))
        sigmas=[F(0),F(1,30),F(1,10),F(1,3),F(1,2)]
        for sigma in sigmas[::-1] if reverse else sigmas:
            Rlo=scale(F(0),G) if sigma==0 else add(scale(1-sigma,c['Nlo']),scale(-(1/sigma-1),E))
            if not psd(Rlo):continue
            lower=add(Clo,scale(F(1,2),Rlo))
            for ln,lc in [('refined',lower),('inherited_RC205',inheritedLo)]:
                for hn,hc in [('refined',upper),('inherited_RC205',inheritedHi)]:
                    gap=add(hc,lc,-1)
                    if not psd(lc) or not psd(gap):continue
                    beta=width(gap,G);gate=add(scale(F(1,2),G),gap,-1);assert psd(add(scale(beta,G),gap,-1))
                    candidates.append(dict(proposal_label=p['label'],triangle_mix=str(mix),triangle_weights=list(map(str,w)),selected_action_theta=str(theta),selected_tail_theta=str(tt),selected_upper_tau=str(tau),selected_lower_tau=str(sigma),selected_lower_type=ln,selected_upper_type=hn,action_error_Gram_upper=ser(E),action_error_relative_Gram_upper=str(width(E,G)),variational_response_lower=ser(Clo),variational_response_upper=ser(Chi),relative_variational_width_upper=str(width(add(Chi,Clo,-1),G)),actual_residual_Gram_lower=ser(Rlo),actual_residual_Gram_upper=ser(Rhi),canonical_inverse_response_lower=ser(lc),canonical_inverse_response_upper=ser(hc),relative_inverse_width_upper=str(beta),half_Gram_gate_matrix=ser(gate),half_Gram_gate_passed=psd(gate)))
    selected=min(candidates,key=lambda r:(F(r['relative_inverse_width_upper']),r['proposal_label'],F(r['selected_lower_tau']),r['selected_lower_type'],r['selected_upper_type']))
    beta=F(selected['relative_inverse_width_upper']);old=F(prior['relative_inverse_width_upper']);assert beta<=old
    return dict(milestone='RC206',starting_commit='3a6ecc1f075a19a1b8ae89c5bbf87de4d3ed785a',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,RC204_signed_controls_rebuilt=128,RC204_positive_integer_minors_rebuilt=768,triangle_raw_diagonal_error_majorant_PSD_verified=True,rational_parameter_proposals=proposals,selected_trial='least_residual',selected_enclosure=selected,source_family=base['response_source_order'],trial_family=base['raw_trial_basis_order'],relative_inverse_width_upper=str(beta),previous_same_family_width_upper=str(old),certified_acceptance_ratio_upper=str(2*beta),certified_gate_margin_lower=str(F(1,2)-beta),canonical_half_Gram_inverse_width_gate_passed=selected['half_Gram_gate_passed'],source_trial_action_and_nominal_residual_data_unchanged=True,all_signed_source_and_residual_tails_retained=True,complex_response_mixtures_paid=True,numerical_optimization_used_only_for_parameter_proposals=True,acceptance_verified_by_exact_rational_PSD=True,Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='tighten nominal residual/source-residual cross-tail enclosure or lawfully enrich trials; six-source gate and native coverage remain open')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);p.add_argument('--replay',action='store_true');args=p.parse_args()
    expected=json.loads(args.output.read_text()) if args.replay else None
    result=run(args.replay,None if expected is None else expected['rational_parameter_proposals'])
    if args.replay:assert result==expected,'exact reversed-order replay differs'
    else:args.output.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print('RC206 PASS: inverse width',result['relative_inverse_width_upper'],'half-Gram gate',result['canonical_half_Gram_inverse_width_gate_passed'])
