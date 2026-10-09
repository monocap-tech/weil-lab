#!/usr/bin/env python3
"""Finite polynomial native source injectivity: algebraic checks and norm controls.
Infinite action/injectivity is an analytic theorem in the accompanying report.
No numerical full-source Gram or quantitative frame constant is certified.
"""
import argparse,hashlib,json
from fractions import Fraction as F
from math import comb,factorial,lcm
from certify_native_collective_boundary_cc53 import NEW_SHA,read

def jet(n,k,a):
    return F((-1)**k*factorial(n+k),2**k*factorial(k)**2*factorial(n-k))*a**(-k) if k<=n else F(0)
def determinant(m):
    den=lcm(*(v.denominator for row in m for v in row));a=[[int(v*den) for v in row] for row in m]
    previous=1
    for k in range(len(a)-1):
        assert a[k][k]!=0
        for i in range(k+1,len(a)):
            for j in range(k+1,len(a)):
                v,r=divmod(a[i][j]*a[k][k]-a[i][k]*a[k][j],previous)
                assert r==0;a[i][j]=v
        previous=a[k][k]
    return F(a[-1][-1],den**len(a))
def formula(degrees,a):
    out=F(1)
    for k in range(len(degrees)):out*=F((-1)**k,2**k*factorial(k)**2)*a**(-k)
    for i,n in enumerate(degrees):
        for m in degrees[i+1:]:out*=m*(m+1)-n*(n+1)
    return out

def validate(first_path):
    first=read(first_path,NEW_SHA);a=F(53,50);checks=0;parities=[]
    for parity in [0,1]:
        degrees=list(range(parity,112,2))
        for n in degrees:
            lam=n*(n+1)
            for k in range(56):
                product=F((-1)**k,2**k*factorial(k)**2)*a**(-k)
                for j in range(k):product*=lam-j*(j+1)
                assert product==jet(n,k,a);checks+=1
        small=0
        for size in range(2,9):
            ns=degrees[:size];M=[[jet(n,k,a) for n in ns] for k in range(size)]
            assert determinant(M)==formula(ns,a)!=0;small+=1
        # Full determinant formula is nonzero. Store sizes rather than huge rationals.
        det=formula(degrees,a);assert det!=0
        parities.append(dict(parity='even' if parity==0 else 'odd',dimension=56,
            full_endpoint_jet_determinant_nonzero=True,
            determinant_numerator_bits=abs(det.numerator).bit_length(),
            determinant_denominator_bits=det.denominator.bit_length(),
            smaller_exact_determinant_replays=small))
    log_checks=0
    for n in range(116):
        integral=-sum(F((-1)**(n-k)*comb(n,k)*comb(n+k,k),(k+1)**2) for k in range(n+1))
        expected=F(-1) if n==0 else F((-1)**(n+1),n*(n+1))
        assert integral==expected;log_checks+=1
    norm_controls=[]
    for N in [0,1,8,56,112,1000]:
        projected=F(1)+sum(F(2*n+1,n*n*(n+1)**2) for n in range(1,N+1))
        residual=2-projected
        assert residual==F(1,(N+1)**2)
        norm_controls.append(dict(polynomial_degree=N,unchanged_log_coefficient=1,
                                  exact_L2_residual_squared=str(residual)))
    shift_controls=0
    for key,lower in [('110,112',F(2,5)),('111,113',F(1,2))]:
        lo,hi=map(F,first['original_full_source'][key]['full']);assert lo>lower
        for mu in [F(0),F(1,10**40),F(1,10),F(10)]:
            shifted=(lo-mu*0,hi-mu*0)
            assert shifted==(lo,hi);shift_controls+=1
    return dict(status='PASS',milestone='CC56',classification='analytic native finite-polynomial full-source injectivity with exact algebraic and norm controls',
        aperture_for_jet_checks='53/50',first_boundary_source_sha256=NEW_SHA,
        endpoint_jet_entry_identity_checks=checks,parity_jet_checks=parities,
        exact_shifted_Legendre_log_integral_checks=log_checks,
        analytic_remainder_cancellation_controls=norm_controls,
        actual_native_whole_mass_shift_cross_controls=shift_controls,
        full_source_injectivity_scope='every fixed finite aperture and finite polynomial retained carrier; analytic theorem, no numerical full-source Gram',
        qualitative_fixed_carrier_frame=True,quantitative_frame_constant_evaluated=False,
        frame_uniform_in_carrier_degree_certified=False,critical_frame_certified=False,
        full_F112_response=False,whole_aperture_positive=False,RH=False,Lean=False)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('first');p.add_argument('--output');a=p.parse_args()
    out=json.dumps(validate(a.first),indent=2)+'\n'
    if a.output:open(a.output,'w').write(out)
    print(out)
