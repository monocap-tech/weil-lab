#!/usr/bin/env python3
"""NF386: original source-matched Fourier-primal lowband upper ENTRY, not an actual upper.

Shows that one fully original, dyadic selected trial j can be tested by one
nonnegative signed-Fourier residual integral plus an elementary tail bound.
No original Fourier integral, j coefficient vector, full inverse, RH or
original domain attachment is certified by this regression.
"""
import argparse, hashlib, json, sys
from fractions import Fraction as F
from pathlib import Path
sys.set_int_max_str_digits(0)
GIT_BLOB_NF375='03c709571046d3f09307614aaded9749f5a15ba1'
SRC_SHA='abd37707d585dcd54b040f1ae865a7430a9c7cba85df31131661b2e72e560770'
NATIVE_SHA='a725a6da6bf29ce21b1955df8f4d0b35b87ff8f003d09cdff13581d1b82f7559'
MU=F(49,50000)
D=(F(65,10**19),F(27,10**20),F(21,10**22),F(49,10**23))
# Certified NF384 lower floors, not actual lowband measurements.
LOWER=(F(0),F(21,10**16),F(385,10**16),
       F(646,10**16),F(834,10**16))

def tail_upper(boundary_abs, derivative_plus_curvature, cutoff):
    """For odd compact supported C^2 j, ||jhat||^2_{|xi|>L} strict upper.

    By 2 integrations by parts and pi>3:
    |jhat(xi)| < a/|xi| + b/|xi|^2,
    a=|j(B)|/3, b=(2|j'(B)|+||j''||_L1)/36.
    """
    a=F(boundary_abs)/3
    b=F(derivative_plus_curvature)/36
    L=F(cutoff)
    assert a>=0 and b>=0 and L>=1
    return 2*(a*a/L + a*b/(L*L) + b*b/(3*L**3))

def check_fixture():
    # Abstract toy example, NOT Weil data:
    # J=(1,0) in R^2, bandlimited f=(1/2,1/3), j=J/2,
    # whole-line error squared=1/9 and physical restriction P=(1,0)
    # has exactly zero error.
    f=(F(1,2),F(1,3))
    j=(F(1,2),F(0))
    full=sum(((x-y)**2 for x,y in zip(f,j)),F(0))
    physical=(f[0]-j[0])**2
    assert full==F(1,9) and physical==0 and physical<=full
    # Equivalent exact source-data quadratics: A - 2 <f,j> + ||j||²
    A=sum((x*x for x in f),F(0))
    v=sum((x*y for x,y in zip(f,j)),F(0))
    gram=sum((y*y for y in j),F(0))
    assert A-2*v+gram==full
    # Mandatory independent positive tail scalar in the Fourier surrogate.
    assert tail_upper(0,F(1,10),2**24) < (F(28,10**14)**2)/64
    # Generic nonzero endpoint and curvature formula is increasing in caps.
    assert tail_upper(F(1,100),F(1,10),2**24) >= tail_upper(0,F(1,10),2**24)
    print('NF386 abstract exact source-difference fixture and endpoint-tail identity PASS')

def evaluate_original(report_path,output=None):
    raw=Path(report_path).read_bytes()
    digest=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\x00'+raw).hexdigest()
    assert digest==GIT_BLOB_NF375, 'NF375 frozen Git blob mismatch'
    a=json.loads(raw)
    assert a['source_sha256']==SRC_SHA and a['native_report_sha256']==NATIVE_SHA
    assert a['measured_original_lowband'] is False
    assert a['original_whole_residual_certified'] is False
    assert len(a['directions'])==4
    assert a['W_ODD_NEG']==a['RH']=='OPEN'
    checks=[]
    for i,direction in enumerate(a['directions']):
        assert direction['direction']==i+1
        for v in direction['dyadic_cutoff_options']:
            k=v['log2_cutoff']
            assert k in (20,21,22,23,24) and v['cutoff']==2**k
            h=F(v['highband_upper'])
            target=F(v['chosen_future_lowband_target'])
            budget=MU*D[i]/4
            assert F(direction['original_residual_squared_budget'])==budget
            assert (h+target)**2<budget and v['exact_squared_original_individual_gate'] is True
            if i==3 and k>20: assert LOWER[k-20] < target
            checks.append(dict(direction=i+1,log2_cutoff=k,
               original_highband_upper=str(h),original_future_lowband_target=str(target),
               future_one_scalar_original_spectral_mismatch_squared_must_be_strictly_below=str(target*target),
               full_residual_budget=str(budget),
               actual_original_spectral_integral_computed=False,
               selected_dyadic_j_construction_pending=True))
    assert len(checks)==20
    # For a hypothetical odd trial j with j(B)=0 and
    # 2|j'(B)|+||j''||_1<=1/10 at L=2^24:
    # the j Fourier tail is < 1/64 of original future direction-four
    # lowband upper target squared. It is a design gate, not an actual j.
    t=F(28,10**14)
    qtail=tail_upper(F(0),F(1,10),2**24)
    assert qtail<t*t/64
    out=dict(
       standing='NF386 EXACT ORIGINAL FOURIER-PRIMAL LOWBAND SUFFICIENT ENTRY; NO ORIGINAL LOWBAND UPPER COMPUTED',
       frozen_NF375_git_blob_sha1=GIT_BLOB_NF375,
       frozen_original_NF375_source_sha256=SRC_SHA,
       frozen_original_NF374_native_sha256=NATIVE_SHA,
       theorem='For explicit supported j in unchanged J242, lowband H_i(L;j)^2 <= int_|xi|<=L |m(xi) uhat_i(xi)-jhat(xi)|^2 dxi + int_|xi|>L |jhat(xi)|^2 dxi.',
       source_matched_trial='fixed original u_i=f_(T e_i)-w_i and selected trial j=J242*z, dyadic z must be supplied and source-checked separately',
       full_four_direction_NF375_acceptance_checks=checks,
       hypothetical_dir4_cutoff_2pow24_j_endpoint_zero_and_derivative_plus_curvature_at_most='1/10',
       hypothetical_dir4_j_high_frequency_squared_tail_upper=str(qtail),
       hypothetical_dir4_j_squared_tail_less_than_fraction_of_original_target='1/64',
       actual_original_selected_j_constructed=False,
       actual_original_signed_lowband_integrated=False,
       actual_original_fourier_error_upper_computed=False,
       actual_original_exterior_form_dual_upper=False,
       inherited_original_multiplier_domain_review='OPEN',
       original_n513_signed_measurement=False,W_ODD_NEG='OPEN',RH='OPEN')
    if output:
        p=Path(output);p.parent.mkdir(parents=True,exist_ok=True)
        p.write_text(json.dumps(out,indent=2)+'\n')
    print('NF386 pinned original NF375 20 high-plus-future-lowband gates PASS')
    print('NF386 conditional direction-four endpoint tail square < target²/64 (no j constructed)')
    print('NF386 actual original signed lowband upper, domain, W-ODD-NEG, RH OPEN')
    return out

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--self-test',action='store_true')
    p.add_argument('--nf375')
    p.add_argument('--output')
    a=p.parse_args()
    if a.self_test: check_fixture()
    if a.nf375: evaluate_original(a.nf375,a.output)
    elif a.output:p.error('output requires --nf375')
    elif not a.self_test:p.error('use --self-test and/or --nf375')
