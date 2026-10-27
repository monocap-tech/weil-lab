#!/usr/bin/env python3
"""Certified scalar kernel compression for the original full arch mixed block.

No source approximation or original mixed matrix is certified here.
"""
import argparse,hashlib,json,time
from fractions import Fraction as F
from math import comb,factorial
from pathlib import Path
FRAME_SHA='87d6f3ae24cde489adaf9ab3ac7efa612bc82bd78c6c9e94866802fdc550052f'
L=F(11,5);R=F(3);CAP=F(128);N=384;MAX_MOMENT=128

def scalar_bound_checks():
    # Alternating sine series: an odd final Taylor index gives a lower bound.
    sine_lower=sum((F((-1)**j*3**(2*j+1),factorial(2*j+1)) for j in range(12)),F(0))
    assert sine_lower>F(7,50)
    x=F(3,2);K=24
    exp_upper=sum((x**j/factorial(j) for j in range(K+1)),F(0))
    exp_upper+=x**(K+1)/factorial(K+1)/(1-x/F(K+2))
    assert exp_upper<F(9,2)
    assert R*exp_upper/sine_lower<CAP
    return {'sin_3_lower':str(sine_lower),'exp_3_over_2_upper':str(exp_upper),
            'circle_radius':'3','circle_modulus_upper':'128'}

def coefficients():
    # g(s)=s k(s)=exp(s/2)/(sinh(s)/s). Exact formal division.
    h=[F(1,factorial(i+1)) if i%2==0 else F(0) for i in range(N+1)]
    c=[]
    for n in range(N+1):
        c.append(F(1,2**n*factorial(n))-sum((h[j]*c[n-j] for j in range(2,n+1,2)),F(0)))
    assert c[:4]==[F(1),F(1,2),-F(1,24),-F(1,16)]
    # Independent exponential generating identity:
    # ((exp(2s)-1)/(2s))*g(s)=exp(3s/2).
    for n in range(N+1):
        assert sum((F(2**j,factorial(j+1))*c[n-j] for j in range(n+1)),F(0))==F(3,2)**n/factorial(n)
    return c

def overlap(f,g,B):
    # f,g are odd polynomial coefficient dictionaries, physical interval [-B,B].
    assert all(p%2 for p in f) and all(q%2 for q in g)
    A=[F(0)]*(max(f)+max(g)+2)
    for p,fp in f.items():
        for q,gq in g.items():
            for ell in range(p+1):
                m=q+ell+1;v=fp*gq*comb(p,ell)/m;shift=p-ell
                for j in range(m+1):A[shift+j]+=v*comb(m,j)*B**(m-j)*(-1)**j
                A[shift]-=v*(-B)**m
    return A

def regressions(moments):
    B=F(1);f={1:F(1)};g={3:F(1),1:-F(3,5)}
    A=overlap(f,g,B)
    assert A==overlap(g,f,B) and A[0]==0
    assert A[1]==-F(2,5) and sum((v*2**j for j,v in enumerate(A)),F(0))==0
    # Full double-integral of the constant kernel is zero for odd functions.
    assert sum((v*2**(j+1)/(j+1) for j,v in enumerate(A)),F(0))==0
    # Apply the same construction at the ORIGINAL B=11/10.
    B=L/2;g={3:F(1),1:-3*B*B/5};A=overlap(f,g,B)
    assert A[0]==0 and A[1]==-B*(B**3-3*B**3/5)
    a=[v*L**j for j,v in enumerate(A)]
    center=-sum((a[j]*moments[j-1] for j in range(1,len(A))),F(0))
    err=sum((abs(a[j])*moment_error(j) for j in range(1,len(A))),F(0))
    assert err<F(1,2**150)
    return {'orthogonal_odd_polynomial_original_B_arch_center':str(center),
            'polynomial_pair_error_upper':str(err),'cusp_reflection_and_constant_kernel_checked':True}

def moment_error(j):
    q=L/R
    return CAP*q**(N+1)/((1-q)*(N+j+1))

def compute(frame):
    assert frame['status']=='CONDITIONAL_ORIGINAL_FULL_484_TRIAL_PHYSICAL_PRECONDITIONER'
    assert frame['physical_Gram_upper']=='101/100'
    checks=scalar_bound_checks();t=time.monotonic();c=coefficients()
    d=[v*L**n for n,v in enumerate(c)]
    moments=[sum((v/F(j+n) for n,v in enumerate(d)),F(0)) for j in range(1,MAX_MOMENT+1)]
    # ||U*C_s W|| <= ||U|| ||W|| <= 101/100, throughout [0,2B].
    # Integrating the Cauchy geometric remainder after division by s:
    error=F(101,100)*CAP*(L/R)**(N+1)/((1-L/R)*(N+1))
    assert error<F(1,2**170)
    return {'status':'CONDITIONAL_ORIGINAL_COMPLETE_ARCH_KERNEL_COMPRESSION_ERROR',
      'frame_input_sha256':FRAME_SHA,'accepted_source_transform_sha256':frame['exact_dyadic_J_transform_sha256'],
      'kernel':'k(s)=exp(s/2)/sinh(s)', 'regular_kernel':'g(s)=s*k(s)',
      'physical_interval':['0',str(L)],'degree':N,'Cauchy_bound_checks':checks,
      'exact_regular_kernel_coefficients':[str(v) for v in c],
      'normalized_scalar_moment_definition':'mu_j=integral_0^(11/5) k(s)*(s/(11/5))^j ds; j>=1',
      'scalar_moment_centers':[str(v) for v in moments],
      'scalar_moment_error_uppers':[str(moment_error(j)) for j in range(1,MAX_MOMENT+1)],
      'complete_normalized_mixed_kernel_replacement_error_upper':str(error),
      'clean_complete_kernel_replacement_error_upper':'1/'+str(2**170),
      'polynomial_regressions':regressions(moments),'elapsed_seconds':time.monotonic()-t,
      'original_source_polynomial_approximation_certified':False,
      'original_source_polynomial_degree_or_cost_certified':False,
      'original_arch_mixed_matrix_computed':False,'matched_forcing_computed':False,
      'inverse_response_value_certified':False,'W_ODD_NEG':'OPEN','inherited_original_domain_review':'OPEN'}

def main():
    p=argparse.ArgumentParser();p.add_argument('--frame-certificate',required=True);p.add_argument('--output',default='artifacts/si29_arch_kernel_moments.json');a=p.parse_args()
    raw=Path(a.frame_certificate).read_bytes();assert hashlib.sha256(raw).hexdigest()==FRAME_SHA
    z=compute(json.loads(raw));out=Path(a.output);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(z,indent=2)+'\n')
    print('COMPLETE ORIGINAL ARCH KERNEL COMPRESSION ERROR < 2^-170; 128 scalar moments certified; original matrix OPEN; seconds',round(z['elapsed_seconds'],2))
if __name__=='__main__':main()
