"""RC188: exact fixed-point materialization of a larger centered Cpsi carrier."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
import numpy as np
from validate_rpb108_rc127_enriched_even_endpoint_action import B,Z,rat,plus,minus,mul,div,bounds,down,up,sqrtup

def inputs():
    root=Path(__file__).resolve().parents[1]/'certificates'
    return [root/('rpb108_rc'+n+'.json') for n in ['187_correlated_variational_refinement','181_psi_action_completion_dashboard','129_four_vector_joint_moment','121_diagonal_metric_equivalence','154_centered_analytic_tail_action']]
def run(paths,replay=False):
    raw=[Path(p).read_bytes() for p in paths];prior,psiCert,joint,metric,old=map(json.loads,raw);hs=[hashlib.sha256(b).hexdigest() for b in raw]
    assert [x['milestone'] for x in [prior,psiCert,joint,metric,old]]==['RC187','RC181','RC129','RC121','RC154']
    assert all(h in prior['input_sha256'] for h in hs[1:])
    assert psiCert['input_sha256'][4:6]==[hs[2],hs[4]] and old['input_sha256'][0]==hs[2]
    assert metric['endpoint_form_bound']=='0 <= h <= J + 2 log(2) I <= D'
    assert metric['whole_supported_canonical_form_domain_covered'] and joint['joint_Gram_positive_and_endpoint_contraction_verified']
    L=32766;O=65534;K=24;S=2**42;Q=2**28;CENTER=10**30
    sl=F(joint['actual_D_Gram_entry_lower'][0][0])/(2*B);sh=F(joint['actual_D_Gram_entry_upper'][0][0])/(2*B)
    loglo=1-F(joint['actual_endpoint_pairing_entry_upper'][0][0])/(2*B);loghi=1-F(joint['actual_endpoint_pairing_entry_lower'][0][0])/(2*B)
    H=[Z]
    for n in range(1,2*O+1):H.append(plus(H[-1],rat(F(1,n))))
    D={n:(plus(H[n],rat(sl))[0],plus(H[n],rat(sh))[1]) for n in range(0,O+1,2)}
    diag={n:minus(plus(minus(mul(rat(2),H[2*n]),mul(rat(2),H[n])),rat(F(1,2*n+1))),(rat(loglo)[0],rat(loghi)[1])) for n in D}
    alpha={};inputEnergy=F(0)
    jobs=list(range(990,L+1,2));jobs=jobs[::-1] if replay else jobs
    for m in jobs:
        eta=div(rat(F(2*m+1,m*(m+1))),D[m]);lo,hi=bounds(eta)
        integer=int(down((lo+hi)/2, S)*S);assert integer>0;alpha[m]=integer
        radius=max(abs(F(integer,S)-lo),abs(hi-F(integer,S)))
        inputEnergy+=up(2*B/F(2*m+1)*F(D[m][1])*radius*radius,10**80)
    # Every entry is nonnegative; prove the entire dot sum fits int64.
    # Off-diagonal entries <=2/|n-m|=1/|n/2-m/2|, so their row
    # sum is <=2 H_N. Kernel floors can only decrease these entries.
    count=len(jobs);hn=sum(F(1,k) for k in range(1,count+1));maxDiag=max(bounds(v)[1] for v in diag.values())
    assert min(bounds(v)[0] for v in diag.values())>0
    intSumUpper=up(max(alpha.values())*Q*(maxDiag+2*hn))
    assert intSumUpper<2**63
    assert (2*O+1)*Q<2**63 and O*(O+L+1)<2**63
    ms=np.array(jobs,dtype=np.int64);av=np.array([alpha[m] for m in jobs],dtype=np.int64)
    inputSum=F(sum(alpha.values()),S);sumInt=sum(alpha.values())
    centers=[None]*(O//2+1);rounding=F(0);dotHashes=[None]*len(centers)
    degrees=list(range(0,O+1,2));degrees=degrees[::-1] if replay else degrees
    for n in degrees:
        den=np.abs(n-ms)*(n+ms+1);den[ms==n]=1
        kernels=((2*n+1)*Q)//den
        dlo,dhi=bounds(diag[n]);diagInteger=int(down(dlo,Q)*Q)
        kernels[ms==n]=diagInteger
        # Integer arithmetic only; positivity and the global sum guard
        # rule out overflow in every product and partial reduction.
        assert kernels.min()>=0
        dot=int(np.sum(kernels*av,dtype=np.int64));assert 0<=dot<=intSumUpper
        lo=F(dot,S*Q);hi=lo+inputSum/Q+F(alpha.get(n,0),S)*(dhi-dlo)
        coefficient=div((rat(lo)[0],rat(hi)[1]),D[n]);cl,ch=bounds(coefficient)
        center=down((cl+ch)/2,CENTER);radius=max(center-cl,ch-center)
        assert radius>=0
        centers[n//2]=str(int(center*CENTER));dotHashes[n//2]=str(dot)
        rounding+=up(2*B/F(2*n+1)*F(D[n][1])*radius*radius,10**80)
        if n%8192==0:print('RC188 exact fixed-point output',n,flush=True)
    lam=L*(L+1);rho=F(lam,(O+2)*(O+3));moments=[]
    for k in range(K+2):
        exact=F(sum(alpha[m]*(m*(m+1))**k for m in jobs),S*lam**k)
        center=down(exact,10**40);radius=exact-center
        moments.append(dict(order=k,lower=str(exact),upper=str(exact),center=str(center),radius=str(radius)))
    T=up(B/(F(D[O][0])*(O-1)*O));inputTail=up(B/(F(D[L][0])*(L-1)*L))
    remainder=up(T*(F(moments[K+1]['upper'])*rho**(K+1)/(1-rho))**2,10**80)
    momentRound=up(T*sum(F(moments[k]['radius'])*rho**k for k in range(K+1))**2,10**80)
    endpointError=up(sqrtup(inputEnergy)+sqrtup(rounding)+sqrtup(momentRound)+sqrtup(remainder)+sqrtup(inputTail)/2)
    oldError=F(old['full_Cpsi_trial_D_norm_error_upper']);assert endpointError<oldError
    regularError=F(psiCert['complete_actual_D_inverse_Rpsi_error_norm_upper'])
    complete=up(endpointError+regularError);oldComplete=F(psiCert['canonical_psi_source_form_full_D_error_norm_upper']);assert complete<oldComplete
    energyLo=F(psiCert['actual_psi_D_energy_lower']);relative=up(complete/(sqrtup(energyLo)-F(1,10**40)))
    carrier=dict(milestone='RC188-Cpsi-carrier',source_prefix_degree=L,output_prefix_degree=O,finite_center_scale=str(CENTER),finite_Cpsi_coefficient_center_numerators=centers,analytic_output_moments=moments,analytic_output_lambda=str(lam),centered_input_tail_first_even_degree=L+2,centered_input_tail_coefficient='1/2',finite_polynomial_input_scale=str(S),finite_polynomial_input_coefficient_sha256=hashlib.sha256(json.dumps([str(alpha[m]) for m in sorted(alpha)],separators=(',',':')).encode()).hexdigest(),finite_kernel_dot_product_sha256=hashlib.sha256(json.dumps(dotHashes,separators=(',',':')).encode()).hexdigest(),whole_Cpsi_error_norm_upper=str(endpointError))
    carrierBytes=(json.dumps(carrier,sort_keys=True,indent=2)+'\n').encode()
    result=dict(milestone='RC188',status='PASS: extended centered psi endpoint carrier and improved complete canonical psi action',starting_commit='81a40cdaac1fec9398a553d74630ee4e356f7503',input_sha256=hs,aperture='11/10',actual_source_definition='eta_n=(2n+1)/(n(n+1)(H_n+s)), even n>=990; unchanged native psi0',source_prefix_degree=L,output_prefix_degree=O,analytic_output_moment_count=K+1,finite_polynomial_input_scale=str(S),fixed_kernel_scale=str(Q),finite_output_center_scale=str(CENTER),input_coefficient_count=count,finite_output_coefficient_count=len(centers),integer_dot_product_upper=str(intSumUpper),integer_arithmetic_overflow_ruled_out=True,no_floating_point_arithmetic_used=True,finite_input_quantization_D_energy_upper=str(inputEnergy),finite_action_interval_and_center_rounding_D_energy_upper=str(rounding),input_tail_D_energy_upper=str(inputTail),centered_input_tail_squared_error_upper=str(inputTail/4),output_moment_rounding_D_energy_upper=str(momentRound),output_geometric_remainder_D_energy_upper=str(remainder),common_eta_output_tail_D_energy_upper=str(T),output_geometric_ratio_upper=str(rho),full_Cpsi_trial_D_norm_error_upper=str(endpointError),previous_same_source_Cpsi_error_norm_upper=str(oldError),endpoint_norm_error_improvement_factor_lower=str(down(oldError/endpointError)),canonical_psi_source_form='psi0 + RC188 Cpsi trial - r D^-1 psi0; exact analytic negative-r correction, inherited paid zero regular trial',canonical_psi_source_form_full_D_error_norm_upper=str(complete),previous_same_source_canonical_psi_error_norm_upper=str(oldComplete),canonical_psi_source_form_relative_D_norm_error_upper=str(relative),inherited_regular_psi_error_norm_upper=str(regularError),materialized_carrier_sha256=hashlib.sha256(carrierBytes).hexdigest(),full_input_output_tails_paid=True,endpoint_cutoff_commutation_assumed=False,canonical_operator_and_native_psi_source_unchanged=True,new_inverse_response_evaluated=False,previous_RC187_inverse_width_upper=prior['relative_inverse_width_upper'],canonical_half_Gram_inverse_width_gate_closed=False,native_seven_source_frame_changed=False,Stage_I_closed=False,original_Weil_or_augmented_actions_performed=False,RH=False,F4=False,Lean=False,next_cursor='use the refined Cpsi carrier and actual psi action error in complete same-family mixed rows and correlated inverse enclosure; tighten w14 carrier precision as needed')
    print('RC188 endpoint error',float(endpointError),'full canonical error',float(complete),'relative',float(relative),flush=True)
    return result,carrier
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);p.add_argument('--carrier-output',required=True);p.add_argument('--replay',action='store_true');args=p.parse_args();result,carrier=run(inputs(),args.replay)
    if args.replay:assert json.loads(Path(args.output).read_text())==result and json.loads(Path(args.carrier_output).read_text())==carrier
    else:Path(args.output).write_text(json.dumps(result,sort_keys=True,indent=2)+'\n');Path(args.carrier_output).write_text(json.dumps(carrier,sort_keys=True,indent=2)+'\n')
    print('RC188 PASS: larger paid centered psi action carrier')
