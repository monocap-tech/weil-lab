"""RC169: exact native congruence and canonical inverse monotonicity audit."""
from pathlib import Path
from fractions import Fraction as F
from math import ceil
import argparse, hashlib, json
from validate_rpb108_rc127_enriched_even_endpoint_action import psd, ser
from validate_rpb108_rc129_four_vector_joint_moment import add, mm, inv, cong

def run(paths, reverse=False):
    raw=[Path(p).read_bytes() for p in paths]
    response, assembly, interface, metric=map(json.loads,raw[:4])
    assert [d['milestone'] for d in (response,assembly,interface,metric)]==['RC168','RC158','RC155','RC121']
    hashes=[hashlib.sha256(b).hexdigest() for b in raw]
    assert response['input_sha256'][2]==hashes[1] and response['input_sha256'][5]==hashes[2]
    assert assembly['input_sha256'][2]==hashes[2]
    notes=[b.decode() for b in raw[4:]]
    assert 'G_P\\preceq G_c\\preceq a^{-1}G_P' in notes[0]
    assert 'D\\preceq P\\preceq2D' in notes[1]
    assert 'delta=eta/3' in notes[2]
    assert 'do not specify a numerical Stage I matrix tolerance' in notes[3]
    mat=lambda d,k:[[F(x) for x in row] for row in d[k]]
    scale=lambda t,A:[[t*x for x in row] for row in A]
    I=[[F(i==j) for j in range(7)] for i in range(7)]
    W=mat(interface,'source_frame_matrix');X=mat(assembly,'conditioned_source_transform');T=mm(W,X)
    # W has zero natural leading pivots. Permute native rows before inversion.
    order=[0,2,3,4,6,1,5]
    P=[[F(j==order[i]) for j in range(7)] for i in range(7)]
    Ti=mm(inv(mm(P,T)),P)
    assert mm(T,Ti)==I and mm(Ti,T)==I
    Glo=mat(response,'conditioned_source_Gram_lower');Ghi=mat(response,'conditioned_source_Gram_upper')
    lower=mat(response,'conditioned_reference_inverse_lower');upper=mat(response,'conditioned_reference_inverse_upper')
    gap=add(upper,lower,-1);beta=F(response['relative_inverse_width_upper'])
    assert psd(Glo) and psd(lower) and psd(gap)
    assert psd(add(scale(beta,Glo),gap,-1))
    native=[cong(Ti,A) for A in (Glo,Ghi,lower,upper)]
    if reverse:
        for A,N in zip((Glo,Ghi,lower,upper),native):
            assert N==[[sum((Ti[k][i]*A[k][l]*Ti[l][j] for k in range(6,-1,-1) for l in range(6,-1,-1)),F(0)) for j in range(7)] for i in range(7)]
    nGlo,nGhi,nlo,nhi=native
    for A,B in zip(native,(Glo,Ghi,lower,upper)):assert cong(T,A)==B
    assert psd(nGlo) and psd(add(scale(beta,nGlo),add(nhi,nlo,-1),-1))
    gate=add(scale(F(1,2),nGlo),add(nhi,nlo,-1),-1);assert psd(gate)
    a=F(metric['actual_canonical_diagonal_metric_lower']);b=F(metric['actual_canonical_diagonal_metric_upper'])
    assert a==F(32125,230953) and b==2
    assert metric['reference_spectral_equivalence']=='D <= P <= 2 D'
    # a P <= L <= P gives P^-1 <= L^-1 <= a^-1 P^-1.
    # These are dual response bounds, not canonical Riesz vector realizations.
    clo=lower;chi=scale(1/a,upper);cgap=add(chi,clo,-1)
    assert psd(clo) and psd(cgap)
    import numpy as np
    diag=[float(Glo[i][i])**.5 for i in range(7)]
    chol=np.linalg.cholesky([[float(Glo[i][j])/diag[i]/diag[j] for j in range(7)] for i in range(7)])
    A=np.array([[float(cgap[i][j])/diag[i]/diag[j] for j in range(7)] for i in range(7)])
    H=np.linalg.solve(chol,np.linalg.solve(chol,A).T).T
    k=max(1,ceil(float(np.linalg.eigvalsh((H+H.T)/2)[-1])*10**6))
    yes=lambda n:psd(add(scale(F(n,10**6),Glo),cgap,-1))
    while not yes(k):k+=1
    while yes(k-1):k-=1
    cbeta=F(k,10**6);assert yes(k) and not yes(k-1)
    nativeClo,nativeChi=cong(Ti,clo),cong(Ti,chi)
    assert psd(add(scale(cbeta,nGlo),add(nativeChi,nativeClo,-1),-1))
    targets=[F(1,2),F(1,10**6),F(1,10**12),F(1,10**24)]
    if reverse:targets.reverse()
    target_checks=[]
    for eta in targets:
        M=add(scale(eta,Glo),gap,-1)
        target_checks.append(dict(target=str(eta),reference_width_contract_passed=psd(M)))
    target_checks.sort(key=lambda d:F(d['target']))
    # No precision failure here is a lower bound on the true inverse error.
    assert not psd(add(scale(F(1,2),Glo),cgap,-1))
    return dict(milestone='RC169',status='PASS: native reference congruence and canonical dual-response transport audit',
      starting_commit='8a282ee271cd1f1724ef11be33c3bccd3e5019ab',input_sha256=hashes,aperture='11/10',
      native_order=['P0','psi0','f0','w14','v10','z_b6','t10'],conditioned_to_native_source_matrix=ser(T),native_to_conditioned_coefficients=ser(Ti),
      native_source_D_Gram_lower=ser(nGlo),native_source_D_Gram_upper=ser(nGhi),
      native_reference_inverse_lower=ser(nlo),native_reference_inverse_upper=ser(nhi),
      native_half_Gram_gate_matrix=ser(gate),native_half_Gram_gate_passed=True,reference_relative_width_upper=str(beta),
      reference_midpoint_matrix_absolute_error_over_source_D_Gram_upper=str(beta/2),
      canonical_inverse_transport_factor=str(1/a),canonical_transport_uses_actual_full_domain_metric_theorem=True,
      native_canonical_dual_response_lower=ser(nativeClo),native_canonical_dual_response_upper=ser(nativeChi),
      canonical_dual_response_relative_width_upper=str(cbeta),canonical_half_Gram_width_gate_passed=False,
      canonical_width_grid_minimal_for_this_enclosure=True,reference_target_width_checks=target_checks,
      response_input_interpretation='D times each native vector in the D-form dual; physical L2 source membership is not assumed',
      required_Stage_I_matrix_tolerance_specified=False,Stage_I_closed=False,
      source_family_equals_original_augmentation_adjoint_range_certified=False,
      canonical_Riesz_vectors_realized=False,regular_multiplier_action_evaluated=False,
      original_Weil_or_augmented_actions_performed=False,true_inverse_error_lower_bound_inferred=False,
      whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False,
      next_cursor='certify the bounded regular action D^-1(R-rI) on the required physical source family, and attach source-map errors and a requested tolerance to the RC119/RC121 canonical solver; original augmented response remains separate')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');p.add_argument('--output',required=True);p.add_argument('inputs',nargs=8)
    args=p.parse_args();result=run(args.inputs,args.replay)
    if args.replay:assert json.loads(Path(args.output).read_text())==result
    else:Path(args.output).write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print('RC169 PASS: exact native and canonical dual-response transport')
