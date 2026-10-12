"""RC153: nonzero correlated C(z_b6-v10) trial, with paid full tails."""
from pathlib import Path
from fractions import Fraction as F
import argparse, hashlib, json
from validate_rpb108_rc127_enriched_even_endpoint_action import (
    B,Z,GRID,rat,plus,minus,mul,div,bounds,down,up,sqrtup,psd,ser)
from validate_rpb108_rc129_four_vector_joint_moment import add

def run(paths, reverse=False):
    raw=[Path(p).read_bytes() for p in paths]
    joint,balanced,capture,cov,conditional,old=map(json.loads,raw)
    assert [d['milestone'] for d in (joint,balanced,capture,cov,conditional,old)]==['RC129','RC132','RC131','RC134','RC151','RC152']
    assert balanced['input_sha256'][0]==hashlib.sha256(raw[2]).hexdigest()
    assert cov['input_sha256'][1]==hashlib.sha256(raw[1]).hexdigest()
    assert old['input_sha256'][0]==hashlib.sha256(raw[4]).hexdigest()
    alpha=F(balanced['alpha']); L=4094; O=8190
    s=(rat(F(joint['actual_D_Gram_entry_lower'][0][0])/(2*B))[0],
       rat(F(joint['actual_D_Gram_entry_upper'][0][0])/(2*B))[1])
    log=(rat(1-F(joint['actual_endpoint_pairing_entry_upper'][0][0])/(2*B))[0],
         rat(1-F(joint['actual_endpoint_pairing_entry_lower'][0][0])/(2*B))[1])
    H=[Z]
    for n in range(1,2*O+1): H.append(plus(H[-1],rat(F(1,n))))
    dn={n:plus(H[n],s) for n in range(0,O+1,2)}
    diag={n:minus(plus(minus(mul(rat(2),H[2*n]),mul(rat(2),H[n])),rat(F(1,2*n+1))),log) for n in dn}
    psi={n:div(rat(F(2*n+1,n*(n+1))),dn[n]) for n in range(990,L+1,2)}
    jobs=sorted(psi,reverse=reverse)
    # Exact Cb-Cg=-alpha*C(psi prefix). Reconstruct the two stored
    # center polynomials separately, then subtract their rational
    # coefficients before applying C. Their rounding does not cancel.
    f={n:div(rat(F(2*n+1,n*(n+1))),dn[n]) for n in range(2,989,2)}
    g={}
    for n in range(0,L+1,2):
        val=Z
        for m in sorted(f,reverse=reverse):
            entry=diag[n] if n==m else rat(F(2*n+1,abs(n-m)*(n+m+1)))
            val=plus(val,mul(entry,f[m]))
        lo,hi=bounds(div(val,dn[n])); g[n]=down((lo+hi)/2)
    b={n:minus(rat(g[n]),mul(rat(alpha),psi[n])) if n in psi else rat(g[n]) for n in g}
    delta={}; delta_payload=[]; omittedFinite=F(0)
    vp_payload=[];zp_payload=[];finiteDelta=F(0)
    for n in range(0,O+1,2):
        vp=Z;zp=Z
        for m in sorted(g,reverse=reverse):
            entry=diag[n] if n==m else rat(F(2*n+1,abs(n-m)*(n+m+1)))
            vp=plus(vp,mul(entry,rat(g[m])))
            zp=plus(zp,mul(entry,b[m]))
        vl,vh=bounds(div(vp,dn[n])); zl,zh=bounds(div(zp,dn[n]))
        vc=down((vl+vh)/2); zc=down((zl+zh)/2)
        vp_payload.append(dict(degree=n,center=str(vc),radius=str(max(vc-vl,vh-vc))))
        zp_payload.append(dict(degree=n,center=str(zc),radius=str(max(zc-zl,zh-zc))))
        delta[n]=zc-vc
        assert delta[n]<0
        delta_payload.append(dict(degree=n,center=str(delta[n])))
        finiteDelta+=up(2*B/F(2*n+1)*F(dn[n][1])*delta[n]**2,10**100)
        if n>L: omittedFinite+=up(2*B/F(2*n+1)*F(dn[n][1])*delta[n]**2,10**100)
    hash_payload=lambda p:hashlib.sha256(json.dumps(p,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    assert hash_payload(vp_payload)==capture['finite_output_polynomial_center_radius_sha256']
    assert hash_payload(zp_payload)==balanced['finite_output_polynomial_center_radius_sha256']
    assert finiteDelta==F(cov['z_minus_v_finite_source_D_energy_upper'])
    print('RC153 signed difference centers reconstructed and both predecessor hashes verified',flush=True)
    # Pay the existing analytic difference tail after combining moments.
    q=list(map(F,cov['z_minus_v_combined_tail_polynomial']))
    rho=F(L*(L+1),(O+2)*(O+3))
    amp=up(sum(abs(v)*rho**k for k,v in enumerate(q)))
    tail=up(F(capture['leading_new_output_tail_D_energy_upper'])*amp*amp,10**100)
    omittedInput=up(omittedFinite+tail,10**100)
    source={n:rat(-v) for n,v in delta.items() if n<=L}
    output=[]; rounding=F(0); trialEnergy=F(0)
    for n in range(0,O+1,2):
        val=Z
        for m in sorted(source,reverse=reverse):
            entry=diag[n] if n==m else rat(F(2*n+1,abs(n-m)*(n+m+1)))
            val=plus(val,mul(entry,source[m]))
        lo,hi=bounds(div(val,dn[n])); center=down((lo+hi)/2)
        radius=max(center-lo,hi-center)
        mass=2*B/F(2*n+1)*F(dn[n][1])
        rounding+=up(mass*radius*radius,10**100)
        trialEnergy+=up(mass*center*center,10**100)
        output.append(dict(degree=n,center=str(-center),radius=str(radius)))
    # Infinite output from finite source: geometric denominator bound
    # with signed coefficients combined before taking absolute values.
    total=sum(-v for n,v in delta.items() if n<=L)
    factor=up(total/(1-rho))
    outputTail=up(F(capture['leading_new_output_tail_D_energy_upper'])*factor*factor,10**100)
    error=up(sqrtup(rounding)+sqrtup(outputTail)+sqrtup(omittedInput))
    print('RC153 nonzero difference action and full tail budget paid',flush=True)
    eps=F(old['psi_full_action_D_norm_error_upper'])
    E=[[2*eps*eps,F(0)],[F(0),2*error*error]]
    G=[[F(x) for x in row] for row in conditional['conditional_source_Gram_lower']]
    def accepts(n):return psd(add([[F(n,10**6)*v for v in row] for row in G],E,-1))
    hi=1
    while not accepts(hi):hi*=2
    lo=0
    while hi-lo>1:
        mid=(hi+lo)//2
        if accepts(mid):hi=mid
        else:lo=mid
    beta=F(hi,10**6);assert accepts(hi) and not accepts(lo)
    psi_conditional=G[0][0]-G[0][1]*G[1][0]/G[1][1]
    psi_envelope_floor=2*eps*eps/psi_conditional
    assert psi_conditional>0 and psi_envelope_floor>F(1,2)
    assert error*error<F(old['delta_zero_trial_action_D_energy_error_upper'])
    assert trialEnergy>0
    witness=list(map(F,conditional['conditional_witness_mixture']))
    quad=lambda M:sum(witness[i]*M[i][j]*witness[j] for i in range(2) for j in range(2))
    payload_hash=lambda p:hashlib.sha256(json.dumps(p,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    return dict(milestone='RC153',status='PASS: nonzero correlated difference action with paid full tails',
        starting_commit='76cda833f81684183b55a656878436cb8510fa81',
        input_sha256=[hashlib.sha256(x).hexdigest() for x in raw],aperture='11/10',
        source='delta=z_b6-v10',source_prefix_degree=L,output_prefix_degree=O,
        reconstructed_finite_delta_center_sha256=payload_hash(delta_payload),
        finite_Cdelta_trial_center_radius_sha256=payload_hash(output),
        finite_Cdelta_trial_coefficient_count=len(output),
        finite_Cdelta_trial_D_energy_upper=str(trialEnergy),
        source_omitted_finite_D_energy_upper=str(omittedFinite),
        source_combined_analytic_tail_D_energy_upper=str(tail),
        source_omitted_full_D_energy_upper=str(omittedInput),
        finite_action_rounding_D_energy_upper=str(rounding),
        infinite_action_output_D_energy_upper=str(outputTail),
        full_Cdelta_trial_D_norm_error_upper=str(error),
        squared_error_improvement_over_RC152_zero_trial=str(F(old['delta_zero_trial_action_D_energy_error_upper'])/(error*error)),
        two_column_error_envelope_Loewner_upper=ser(E),
        envelope_relative_conditional_Gram_upper=str(beta),
        inherited_psi_envelope_relative_floor_even_with_zero_delta_error=str(psi_envelope_floor),
        inherited_psi_envelope_alone_fails_half_Gram_gate=True,
        witness_envelope_to_conditional_Gram=str(quad(E)/quad(G)),
        half_Gram_action_error_envelope_gate_passed=beta<F(1,2),
        all_finite_delta_coefficients_combined_before_action=True,
        both_predecessor_output_polynomial_hashes_verified=True,
        full_delta_action_trial_evaluated=True,mixed_action_error_sign_assumed=False,
        mixed_response_rows_evaluated=False,seven_source_inverse_response_certified=False,
        original_Weil_or_augmented_actions_performed=False,
        whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False,
        next_cursor='refine Cpsi0 and joint correlated error; evaluate mixed pairings of the paid Cdelta trial with the five-source frame and psi0 before seven-source inverse assembly')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');p.add_argument('--output',required=True);p.add_argument('inputs',nargs=6)
    a=p.parse_args();result=run(a.inputs,a.replay)
    if a.replay:assert json.loads(Path(a.output).read_text())==result
    else:Path(a.output).write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print('RC153 PASS: correlated difference action')
