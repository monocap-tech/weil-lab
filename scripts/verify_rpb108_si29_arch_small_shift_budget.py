#!/usr/bin/env python3
"""Exact all-source small-shift budget for original archimedean coupling."""
import argparse,hashlib,json
from fractions import Fraction as F
from math import comb,isqrt
from pathlib import Path

FRAME_SHA='87d6f3ae24cde489adaf9ab3ac7efa612bc82bd78c6c9e94866802fdc550052f'
NATIVE_SHA='c9ee487f8abe7b633c47d2ef7d72e2cc4f7289bc794b2d8fc02bb61520b25e60'
B=F(11,10)

def regressions():
    # Factor 2 from t=2s in the original quarter-digamma formula.
    for n in (0,2,31):
        a=F(n)+F(1,4);lam=2*a
        for b in (F(0),F(1,3),F(5,2)):
            laplace=2*(1/lam-lam/(lam*lam+4*b*b))
            assert laplace==b*b/(a*(a*a+b*b))
    # Positive Gram [[1,1],[1,1]] has norm 2. Its offdiagonal
    # block saturates t/2, so the correlation bound is t/4.
    t=F(2);cross=F(-1,2)
    assert abs(cross)==t/4 and abs(cross)>t/8
    # Exact orthogonal odd polynomials f=x, g=x^3-3x/5 on [-1,1].
    assert F(2,5)-F(3,5)*F(2,3)==0
    terms=[(4,[F(1)]),(3,[F(0),F(3)]),
           (2,[F(-3,5),F(0),F(3)]),(1,[F(0),F(-3,5),F(0),F(1)])]
    poly=[F(0)]*7
    for power,coefs in terms:
        primitive=[F(comb(power+1,k)*(-1)**k,power+1) for k in range(power+2)]
        primitive[0]-=F((-1)**(power+1),power+1)
        for i,c in enumerate(coefs):
            for j,v in enumerate(primitive):poly[i+j]+=c*v
    assert poly[0]==0 and poly[1]==-F(2,5) # boundary cusp sign/factor
    E=F(29,25);D=F(98,25);root=F(3);assert root*root>E*D
    for k in (2,3,4):
        s=F(1,2**(2*k));sqrt_s=F(1,2**k)
        value=sum((c*s**i for i,c in enumerate(poly)),F(0))
        cap=E*s/2+F(2,3)*root*s*sqrt_s+D*s*s/2
        assert abs(value)<=cap
    return dict(original_quarter_digamma_factor_checked=True,
                PSD_offdiagonal_quarter_factor_checked=True,
                exact_orthogonal_odd_polynomial_cusp_and_bound_checked=True)

def compute(frame):
    assert frame['status']=='CONDITIONAL_ORIGINAL_FULL_484_TRIAL_PHYSICAL_PRECONDITIONER'
    assert frame['native_input_sha256']==NATIVE_SHA
    assert frame['full_trial_dimension']==484 and frame['original_source_count']==470
    E=F(frame['full_trial_endpoint_vector_squared_upper'])
    D=F(frame['full_trial_derivative_Gram_trace_upper'])
    assert E>0 and D>0
    root=isqrt((E*D).numerator//(E*D).denominator)+1
    assert F(root*root)>E*D
    choices=[]
    for k in range(1,41):
        s=F(1,2**(2*k));q=F(1,2**k)
        error=E*(s+s*s)/2+root*(F(4,9)*s*q+F(8,15)*s*s*q)+D*(s*s/4+s*s*s/3)
        choices.append((k,s,error))
    k,s,error=next(x for x in choices if x[2]<F(1,10**6))
    assert k==18 and s==F(1,2**36) and error<F(1,2500000)
    assert all(e>=F(1,10**6) for kk,ss,e in choices if kk<k)
    return dict(status='CONDITIONAL_COMPLETE_ARCH_MIXED_SMALL_SHIFT_ERROR_BOUND',
      frame_input_sha256=FRAME_SHA,matched_native_projection_sha256=NATIVE_SHA,
      accepted_source_transform_sha256=frame['exact_dyadic_J_transform_sha256'],
      original_J_count=470,actual_feature_count=14,
      full_trial_endpoint_squared_upper=str(E),full_trial_derivative_HS_squared_upper=str(D),
      sqrt_endpoint_times_derivative_upper=root,small_shift_cutoff=str(s),
      exact_small_shift_mixed_operator_error_upper=str(error),
      clean_small_shift_mixed_operator_error_upper='1/2500000',
      remaining_physical_shift_interval=[str(s),str(2*B)],
      arch_translation_kernel='2 exp(-s/2)/(1-exp(-2s))',
      mixed_integral='(JD)star Harch W = - integral_0^(2B) kernel(s) (JD)star C_s W ds',
      normalization='U=JD, W=(I-P_J470)FC, exact Ustar W=0',
      independent_exact_regressions=regressions(),
      remaining_finite_arch_integral_computed=False,full_Astar_mixed_computed=False,
      energy_projection_computed=False,matched_forcing_computed=False,inverse_response_value_certified=False,
      quadrature_node_count_certified=False,W_ODD_NEG='OPEN',inherited_original_domain_review='OPEN')

def main():
    p=argparse.ArgumentParser();p.add_argument('--frame-certificate',required=True)
    p.add_argument('--output',default='artifacts/si29_arch_small_shift_budget.json');a=p.parse_args()
    raw=Path(a.frame_certificate).read_bytes();assert hashlib.sha256(raw).hexdigest()==FRAME_SHA
    result=compute(json.loads(raw));out=Path(a.output);out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('COMPLETE ARCH MIXED SMALL-SHIFT BUDGET PASS: delta=2^-36; operator error < 4e-7; finite integral remains OPEN')
if __name__=='__main__':main()
