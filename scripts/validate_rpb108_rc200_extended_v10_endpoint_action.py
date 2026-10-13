"""RC200: exact fixed-point enlarged centered endpoint action on native v10."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
import numpy as np
from validate_rpb108_rc127_enriched_even_endpoint_action import B,Z,rat,plus,minus,mul,div,bounds,down,up,sqrtup

def inputs():
    base=Path(__file__).resolve().parents[1]/'certificates'
    return [base/('rpb108_rc'+n+'.json') for n in ['199_six_source_canonical_inverse','197_native_v10_canonical_action','183_materialized_w14_canonical_carrier','129_four_vector_joint_moment','121_diagonal_metric_equivalence']]

def run(paths,replay=False):
    raw=[p.read_bytes() for p in paths];prior,old,source,joint,metric=map(json.loads,raw);hs=[hashlib.sha256(b).hexdigest() for b in raw]
    assert [x['milestone'] for x in [prior,old,source,joint,metric]]==['RC199','RC197','RC183-w14-carrier','RC129','RC121']
    assert old['input_sha256'][2]==hs[2] and old['input_sha256'][6:8]==hs[3:]
    assert hs[1] in prior['input_sha256'] and hs[2] in prior['input_sha256']
    assert old['all_native_prefix_coefficients_and_radii_reproduced']
    assert metric['endpoint_form_bound']=='0 <= h <= J + 2 log(2) I <= D'
    assert metric['whole_supported_canonical_form_domain_covered']
    g={2*i:F(c) for i,c in enumerate(source['Cg_finite_coefficient_centers'])};mu=list(map(F,old['native_analytic_moments']));nativeLam=F(old['native_analytic_lambda'])
    assert len(g)==4096 and min(g.values())>0 and len(mu)==11 and min(mu)>0 and nativeLam==4094*4095
    L=32766;O=65534;K=24;S=2**32;Q=2**28;CENTER=10**30
    sl=F(joint['actual_D_Gram_entry_lower'][0][0])/(2*B);sh=F(joint['actual_D_Gram_entry_upper'][0][0])/(2*B)
    loglo=1-F(joint['actual_endpoint_pairing_entry_upper'][0][0])/(2*B);loghi=1-F(joint['actual_endpoint_pairing_entry_lower'][0][0])/(2*B)
    H=[Z]
    for n in range(1,2*O+1):H.append(plus(H[-1],rat(F(1,n))))
    D={n:(plus(H[n],rat(sl))[0],plus(H[n],rat(sh))[1]) for n in range(0,O+1,2)}
    diag={n:minus(plus(minus(mul(rat(2),H[2*n]),mul(rat(2),H[n])),rat(F(1,2*n+1))),(rat(loglo)[0],rat(loghi)[1])) for n in D}
    jobs=list(range(0,L+1,2));jobs=jobs[::-1] if replay else jobs
    alpha={};inputEnergy=F(0)
    for m in jobs:
        if m<=8190:c=rat(g[m])
        else:c=mul(div(rat(F(2*m+1,m*(m+1))),D[m]),rat(sum(mu[k]*F(nativeLam,m*(m+1))**k for k in range(11))))
        lo,hi=bounds(c);integer=int(down((lo+hi)/2,S)*S);assert integer>0;alpha[m]=integer
        radius=max(abs(F(integer,S)-lo),abs(hi-F(integer,S)))
        inputEnergy+=up(2*B/F(2*m+1)*F(D[m][1])*radius*radius,10**80)
    hn=sum(F(1,k) for k in range(1,len(jobs)+1));maxDiag=max(bounds(v)[1] for v in diag.values())
    assert min(bounds(v)[0] for v in diag.values())>0
    guard=up(max(alpha.values())*Q*(maxDiag+2*hn));assert guard<2**63
    assert (2*O+1)*Q<2**63 and O*(O+L+1)<2**63
    ms=np.array(jobs,dtype=np.int64);av=np.array([alpha[m] for m in jobs],dtype=np.int64);inputSum=F(sum(alpha.values()),S)
    centers=[None]*(O//2+1);dots=centers.copy();rounding=F(0)
    for n in (range(O,-1,-2) if replay else range(0,O+1,2)):
        den=np.abs(n-ms)*(n+ms+1);den[ms==n]=1;kernel=((2*n+1)*Q)//den
        dlo,dhi=bounds(diag[n]);kernel[ms==n]=int(down(dlo,Q)*Q);assert kernel.min()>=0
        dot=int(np.sum(kernel*av,dtype=np.int64));assert 0<=dot<=guard
        lo=F(dot,S*Q);hi=lo+inputSum/Q+F(alpha.get(n,0),S)*(dhi-dlo)
        cl,ch=bounds(div((rat(lo)[0],rat(hi)[1]),D[n]));center=down((cl+ch)/2,CENTER);radius=max(center-cl,ch-center)
        centers[n//2]=str(int(center*CENTER));dots[n//2]=str(dot)
        rounding+=up(2*B/F(2*n+1)*F(D[n][1])*radius*radius,10**80)
        if n%8192==0:print('RC200 exact endpoint output',n,flush=True)
    lam=L*(L+1);rho=F(lam,(O+2)*(O+3));moments=[]
    for k in range(K+2):
        exact=F(sum(alpha[m]*(m*(m+1))**k for m in jobs),S*lam**k);center=down(exact,10**40)
        moments.append(dict(order=k,lower=str(exact),upper=str(exact),center=str(center),radius=str(exact-center)))
    T=up(B/(F(D[O][0])*(O-1)*O));inputEta=up(B/(F(D[L][0])*(L-1)*L));first=L+2
    amplitude=sum(mu[k]*F(nativeLam,first*(first+1))**k for k in range(11));inputTail=up(inputEta*amplitude*amplitude)
    remainder=up(T*(F(moments[K+1]['upper'])*rho**(K+1)/(1-rho))**2,10**80)
    momentRound=up(T*sum(F(moments[k]['radius'])*rho**k for k in range(K+1))**2,10**80)
    endpoint=up(sqrtup(inputEnergy)+sqrtup(rounding)+sqrtup(momentRound)+sqrtup(remainder)+sqrtup(inputTail)/2)
    regular=F(old['complete_D_inverse_Rv10_error_norm_upper']);negative=F(old['negative_r_coefficient_error_D_energy_upper'])
    complete=up(endpoint+regular+sqrtup(negative));relative=up(complete/(sqrtup(F(old['native_D_energy_lower']))-F(1,10**40)))
    assert endpoint<F(old['complete_endpoint_action_D_error_norm_upper']) and complete<F(old['complete_canonical_v10_action_D_error_norm_upper'])
    carrier=dict(milestone='RC200-Cv10-carrier',source_prefix_degree=L,output_prefix_degree=O,finite_center_scale=str(CENTER),finite_Cv10_coefficient_center_numerators=centers,analytic_output_moments=moments,analytic_output_lambda=str(lam),centered_input_tail_first_even_degree=L+2,centered_input_tail_coefficient='1/2 times unchanged native v10',finite_polynomial_input_scale=str(S),finite_polynomial_input_coefficient_sha256=hashlib.sha256(json.dumps([str(alpha[m]) for m in sorted(alpha)],separators=(',',':')).encode()).hexdigest(),finite_kernel_dot_product_sha256=hashlib.sha256(json.dumps(dots,separators=(',',':')).encode()).hexdigest(),whole_Cv10_error_norm_upper=str(endpoint),native_source_and_retained_canonical_carrier_sha256=hs[1])
    b=(json.dumps(carrier,sort_keys=True,indent=2)+'\n').encode()
    result=dict(milestone='RC200',status='PASS: enlarged centered native v10 endpoint action and tighter complete canonical action',starting_commit='8651cd0a903e9773a8b139951a2db0d622ba2d8e',input_sha256=hs,aperture='11/10',canonical_operator='M=D^-1 L',norm='D energy',native_v10_source_unchanged=True,source_prefix_degree=L,output_prefix_degree=O,finite_input_quantization_D_energy_upper=str(inputEnergy),finite_output_interval_rounding_D_energy_upper=str(rounding),input_eta_tail_D_energy_upper=str(inputEta),native_input_tail_moment_amplitude_upper=str(amplitude),native_input_tail_D_energy_upper=str(inputTail),centered_input_tail_squared_error_upper=str(inputTail/4),output_moment_rounding_D_energy_upper=str(momentRound),output_geometric_remainder_D_energy_upper=str(remainder),common_eta_output_tail_D_energy_upper=str(T),output_geometric_ratio_upper=str(rho),integer_dot_product_upper=str(guard),integer_arithmetic_overflow_ruled_out=True,endpoint_no_floating_point_arithmetic_used=True,fixed_input_scale=str(S),fixed_kernel_scale=str(Q),complete_endpoint_v10_D_error_norm_upper=str(endpoint),previous_same_source_endpoint_D_error_norm_upper=old['complete_endpoint_action_D_error_norm_upper'],retained_regular_v10_error_norm_upper=str(regular),retained_negative_r_coefficient_error_D_energy_upper=str(negative),complete_canonical_v10_action_D_error_norm_upper=str(complete),previous_same_source_complete_action_D_error_norm_upper=old['complete_canonical_v10_action_D_error_norm_upper'],complete_canonical_v10_relative_D_norm_error_upper=str(relative),materialized_endpoint_carrier_sha256=hashlib.sha256(b).hexdigest(),canonical_action_definition='native v10 + RC200 endpoint carrier + retained RC197 finite/exact-tail negative-r correction + retained RC197 regular carrier',full_native_input_and_infinite_output_tails_paid=True,endpoint_cutoff_commutation_assumed=False,new_inverse_response_evaluated=False,latest_six_source_inverse_width_upper=prior['relative_inverse_width_upper'],six_source_inverse_acceptance_closed=False,Stage_I_closed=False,Stage_I_completion_ratio=None,RH=False,F4=False,Lean=False,next_cursor='rebuild six-source mixed and residual calculations with refined v10 endpoint carrier; tighten regular or enrich residual if still needed')
    print('RC200 endpoint/full/relative',float(endpoint),float(complete),float(relative),flush=True)
    return result,carrier

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);p.add_argument('--carrier-output',required=True);p.add_argument('--replay',action='store_true');a=p.parse_args();r,c=run(inputs(),a.replay)
    if a.replay:assert json.loads(Path(a.output).read_text())==r and json.loads(Path(a.carrier_output).read_text())==c
    else:Path(a.output).write_text(json.dumps(r,sort_keys=True,indent=2)+'\n');Path(a.carrier_output).write_text(json.dumps(c,sort_keys=True,indent=2)+'\n')
    print('RC200 PASS')
