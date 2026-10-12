"""RC154: extended Cpsi trial with centered input-tail and output moments."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
from validate_rpb108_rc127_enriched_even_endpoint_action import (
    B,Z,rat,plus,minus,mul,div,bounds,down,up,sqrtup,psd,ser)
from validate_rpb108_rc129_four_vector_joint_moment import add

def run(paths,reverse=False):
    raw=[Path(p).read_bytes() for p in paths]
    joint,old,conditional,difference=map(json.loads,raw)
    assert [x['milestone'] for x in (joint,old,conditional,difference)]==['RC129','RC130','RC151','RC153']
    assert difference['input_sha256'][0]==hashlib.sha256(raw[0]).hexdigest()
    assert difference['input_sha256'][4]==hashlib.sha256(raw[2]).hexdigest()
    assert old['input_sha256'][0]==hashlib.sha256(raw[0]).hexdigest()
    assert joint['joint_Gram_positive_and_endpoint_contraction_verified']
    L=8190;O=16382;K=24;lam=L*(L+1);rho=F(lam,(O+2)*(O+3))
    s=(rat(F(joint['actual_D_Gram_entry_lower'][0][0])/(2*B))[0],
       rat(F(joint['actual_D_Gram_entry_upper'][0][0])/(2*B))[1])
    log=(rat(1-F(joint['actual_endpoint_pairing_entry_upper'][0][0])/(2*B))[0],
         rat(1-F(joint['actual_endpoint_pairing_entry_lower'][0][0])/(2*B))[1])
    H=[Z]
    for n in range(1,2*O+1):H.append(plus(H[-1],rat(F(1,n))))
    dn={n:plus(H[n],s) for n in range(0,O+1,2)}
    diag={n:minus(plus(minus(mul(rat(2),H[2*n]),mul(rat(2),H[n])),rat(F(1,2*n+1))),log) for n in dn}
    source={n:div(rat(F(2*n+1,n*(n+1))),dn[n]) for n in range(990,L+1,2)}
    jobs=sorted(source,reverse=reverse);payload=[];rounding=F(0)
    for n in range(0,O+1,2):
        value=Z
        for m in jobs:
            entry=diag[n] if n==m else rat(F(2*n+1,abs(n-m)*(n+m+1)))
            value=plus(value,mul(entry,source[m]))
        lo,hi=bounds(div(value,dn[n]));center=down((lo+hi)/2)
        radius=max(center-lo,hi-center)
        rounding+=up(2*B/F(2*n+1)*F(dn[n][1])*radius*radius,10**100)
        payload.append(dict(degree=n,center=str(center),radius=str(radius)))
        if n and n%4096==0:print('RC154 finite output degree',n,'paid',flush=True)
    # For n>O every retained source degree is below n. Expanding
    # 1/(1-m(m+1)/n(n+1)) gives a common eta_n times moments.
    # Positive source coefficients pay the entire geometric remainder.
    moments=[]
    for k in range(K+2):
        value=Z
        for m in jobs:value=plus(value,mul(source[m],rat(F(m*(m+1),lam)**k)))
        lo,hi=bounds(value);center=down((lo+hi)/2)
        moments.append(dict(order=k,lower=str(lo),upper=str(hi),center=str(center),radius=str(max(center-lo,hi-center))))
    T=up(B/(F(dn[O][0])*(O-1)*O))
    outputRemainder=up(T*(F(moments[K+1]['upper'])*rho**(K+1)/(1-rho))**2,10**100)
    momentRounding=up(T*sum(F(moments[k]['radius'])*rho**k for k in range(K+1))**2,10**100)
    inputTail=up(B/(F(dn[L][0])*(L-1)*L))
    # psi=p+t. Trial q=Q(p)+(1/2)t; Q(p) includes the finite action
    # outputs plus paid analytic output moments. Spectral calculus for
    # 0<=C<=I gives ||(C-I/2)t|| <= ||t||/2 on the full carrier.
    # No commutation between C and the degree cutoff is assumed.
    error=up(sqrtup(rounding)+sqrtup(momentRounding)+sqrtup(outputRemainder)+sqrtup(inputTail)/2)
    deltaError=F(difference['full_Cdelta_trial_D_norm_error_upper'])
    E=[[2*error*error,F(0)],[F(0),2*deltaError*deltaError]]
    G=[[F(x) for x in row] for row in conditional['conditional_source_Gram_lower']]
    def accepts(n):return psd(add([[F(n,10**6)*x for x in row] for row in G],E,-1))
    hi=1
    while not accepts(hi):hi*=2
    lo=0
    while hi-lo>1:
        mid=(lo+hi)//2
        if accepts(mid):hi=mid
        else:lo=mid
    beta=F(hi,10**6);assert accepts(hi) and not accepts(lo)
    assert beta<F(1,2)
    psi_floor=2*error*error/(G[0][0]-G[0][1]**2/G[1][1])
    w=list(map(F,conditional['conditional_witness_mixture']))
    quad=lambda M:sum(w[i]*M[i][j]*w[j] for i in range(2) for j in range(2))
    # Exact rational controls for the centered spectral factor, including
    # its endpoint equality cases; midpoint improvement is uniformly sharp.
    controls=[]
    for c in (F(0),F(1,7),F(1,2),F(9,10),F(1)):
        assert (c-F(1,2))**2<=F(1,4)
        controls.append(dict(eigenvalue=str(c),centered_squared_factor=str((c-F(1,2))**2)))
    print('RC154 joint action-error half-Gram gate paid',flush=True)
    return dict(milestone='RC154',status='PASS: centered analytic-tail action and joint half-Gram error envelope',
        starting_commit='4822bd2a711b713811d36dc5ef0905df81816e8a',
        input_sha256=[hashlib.sha256(b).hexdigest() for b in raw],aperture='11/10',
        source_prefix_degree=L,output_prefix_degree=O,analytic_output_moment_count=K+1,
        finite_action_trial_center_radius_sha256=hashlib.sha256(json.dumps(payload,sort_keys=True,separators=(',',':')).encode()).hexdigest(),
        finite_action_trial_coefficient_count=len(payload),
        trial_definition='Q(psi[990..8190]) + (1/2)*psi[8192..infinity]; Q finite outputs through 16382 plus 25 output-tail eta moments beyond 16382',
        output_tail_eta_definition='eta_n=(2*n+1)/(n*(n+1)*D_n), even n>=16384; D_n=s+H_n',
        analytic_output_moment_intervals=moments,
        output_tail_geometric_ratio_upper=str(rho),
        input_tail_D_energy_upper=str(inputTail),
        centered_input_tail_squared_error_upper=str(inputTail/4),
        finite_action_rounding_D_energy_upper=str(rounding),
        output_moment_rounding_D_energy_upper=str(momentRounding),
        output_geometric_remainder_D_energy_upper=str(outputRemainder),
        full_Cpsi_trial_D_norm_error_upper=str(error),
        psi_squared_error_improvement_over_RC130=str(F(old['full_action_D_norm_error_upper'][0])**2/(error*error)),
        inherited_full_Cdelta_trial_D_norm_error_upper=str(deltaError),
        two_column_action_error_envelope_Loewner_upper=ser(E),
        conditional_source_Gram_lower=ser(G),
        envelope_relative_conditional_Gram_upper=str(beta),
        witness_envelope_to_conditional_Gram=str(quad(E)/quad(G)),
        psi_envelope_relative_floor_with_zero_delta_error=str(psi_floor),
        half_Gram_action_error_envelope_gate_passed=True,
        centered_contraction_controls=controls,
        endpoint_operator_commutes_with_cutoff_assumed=False,
        actual_error_lower_bound_inferred=False,mixed_action_error_sign_assumed=False,
        analytic_input_tail_assigned_zero=False,
        mixed_response_rows_evaluated=False,seven_source_inverse_response_certified=False,
        original_Weil_or_augmented_actions_performed=False,
        whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False,
        next_cursor='evaluate the two paid trials mixed with the five-source frame and each other; assemble seven-source variational inverse-response bounds and test their matrix width against an explicit Stage I tolerance')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');p.add_argument('--output',required=True);p.add_argument('inputs',nargs=4)
    a=p.parse_args();r=run(a.inputs,a.replay)
    if a.replay:assert json.loads(Path(a.output).read_text())==r
    else:Path(a.output).write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
    print('RC154 PASS: centered analytic tail action')
