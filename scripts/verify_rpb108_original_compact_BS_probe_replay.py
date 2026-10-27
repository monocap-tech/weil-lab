#!/usr/bin/env python3
"""Stdlib exact replay of native scalar composition and original BS/cap-stop bounds."""
import hashlib,json,sys
from fractions import Fraction as F
from pathlib import Path
from validate_rpb108_si06_negative_band import PI,WEIGHTS,SHIFTS
CAP_SHA='8b58972bbdd2f9cb5d00275820ab6d6891feeff3bbd584a1c28231770368f514'
def dy(x):return F(int(x[0]))*F(2)**int(x[1])
def ball(v):
    m,r=dy(v[0]),dy(v[1]);assert r>=0;return m-r,m+r
def add(x,y):return x[0]+y[0],x[1]+y[1]
def mul(x,y):
    v=[a*b for a in x for b in y];return min(v),max(v)
def scale(x,c):return mul(x,(c,c))
def square(x):
    a,b=x;return (F(0) if a<=0<=b else min(a*a,b*b),max(a*a,b*b))
def subset(x,y):assert y[0]<=x[0]<=x[1]<=y[1]
def main():
    assert len(sys.argv)==4;z=json.load(open(sys.argv[1]));raw=Path(sys.argv[2]).read_bytes();praw=Path(sys.argv[3]).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==CAP_SHA==z['cap_input_sha256']
    assert hashlib.sha256(praw).hexdigest()==z['probe_sha256'];cap=json.loads(raw);p=json.loads(praw)
    assert z['exact_probe']==p and z['status']=='CONDITIONAL_ORIGINAL_COMPACT_BS_NEAR_CRITICAL_AND_GLOBAL_AFFINE_CAP_STOP'
    assert p['dirichlet_modes']==32 and p['sine_frequencies']==[str(F(5*n,11)) for n in range(1,33)]
    assert len(p['sine_coefficients'])==32 and all((F(c)*10**12).denominator==1 for c in p['sine_coefficients']+[p['sinh_coefficient']])
    assert z['working_precision_bits']==512 and z['flint_version']=='0.8.0'
    v={k:ball(x) for k,x in z['native_balls'].items()};q=tuple(map(F,z['signed_energy_interval']));N=tuple(map(F,z['physical_norm_interval']))
    assert 0<q[0]<=q[1]<F(1,10**10) and F(99,100)<N[0]<=N[1]<F(101,100)
    subset(v['norm'],N);subset(v['signed'],q)
    composed=add(add(mul(add(v['arch_constant'],v['arch_tail']),v['norm']),v['arch_integral']),add(v['prime'],scale(square(v['pole']),-2)))
    subset(composed,q)
    B=F(11,10);l,r,w=[F(p['defect_cell'][k]) for k in ['lo','hi','parent_SM40_height']];d=r-l
    assert l>=F(1,4) and d==F(1,4096)
    matches=[]
    for a,b,height in (tuple(map(F,row)) for row in cap['original_SM40_cells']):
        if a<=l<r<=b and height==w:
            j=16*(l-a)/(b-a)
            if j.denominator==1 and 0<=j<16 and d==(b-a)/16:matches.append((a,b,height))
    assert len(matches)==1
    records={F(q):(F(a),F(b)) for q,a,b in cap['endpoint_multiplier_intervals']}
    H=F(2145);h=H*d*d/8
    endpoints=[F(1,1000)-records[x][0]+h for x in (l,r)]
    assert 0<min(endpoints)<=max(endpoints)<w
    prime2=sum((2*WEIGHTS[n][1]*(2*PI[1]*SHIFTS[n][1])**2 for n in WEIGHTS),F(0))
    # n=0 complex denominator uses pi*xi>=3/4. Tail n>=1 uses
    # 1/(5/4)^3 + integral_1^infinity (t+1/4)^-3 dt =104/125.
    archlocal=2*F(22,7)**2*(F(64,27)+F(104,125))
    assert archlocal==F(z['local_arch_curvature_upper']) and prime2==F(z['prime_curvature_upper'])
    assert archlocal+prime2<F(786)==F(z['local_full_curvature_upper'])
    # Recheck the COMPLETE first-derivative bound used for the negative mass.
    prime1=4*PI[1]*sum((WEIGHTS[n][1]*SHIFTS[n][1] for n in WEIGHTS),F(0))
    assert prime1<69 and 20*F(22,7)+69<132==F(z['multiplier_derivative_upper'])
    assert (F(44,7)*B)**2*2*B*N[1]<11**2 and z['Fourier_derivative_upper']=='11'
    ft=tuple(map(F,z['mid_Fourier_interval']));m=tuple(map(F,z['mid_multiplier_interval']))
    assert ft[0]<=ft[1] and m[0]<=m[1] and ft[0]*ft[1]>0
    flo=min(abs(ft[0]),abs(ft[1]))-11*d/2
    rlo=F(1,1000)-m[1]-132*d/2
    assert flo==F(z['Fourier_on_cell_abs_lower'])>0 and rlo==F(z['negative_multiplier_on_cell_lower'])>0
    Klo=2*d*rlo*flo*flo;defect=(H-786)*d*d/8;gap=2*d*defect*flo*flo-q[1]
    assert Klo==F(z['true_negative_action_lower'])>0
    assert defect==F(z['cap_pointwise_overpayment_on_cell_lower'])>0
    assert gap==F(z['affine_cap_minus_Astar_action_lower'])>F(4,10**9)
    Aupper=F(cap['envelope_operator_norm_upper'])*N[1]+q[1]
    assert Aupper==F(z['Astar_action_upper'])
    true_lower=Klo/(Klo+q[1]);cap_lower=1+gap/Aupper
    assert true_lower==F(z['original_true_BS_norm_lower'])>1-F(6,10**12)
    assert cap_lower==F(z['affine_cap_BS_norm_lower'])>1+F(3,10**10)
    assert F(z['sufficient_coercivity_residual_squared_budget_ceiling'])==F(33621,10**9)*(1-true_lower)<F(33621,10**9)*F(6,10**12)
    assert q[1]/N[0]<F(8,10**18)
    for k in ['whole_odd_affine_cap_comparison_stopped','all_Young_caps_dominating_same_affine_envelope_stopped']:assert z[k] is True
    for k in ['original_J470_membership_claimed','exact_J470_energy_dual_gate_stopped','original_signed_negative_direction_proved','original_true_BS_global_upper_certified','infinite_operator_remainder_certified']:assert z[k] is False
    assert z['W_ODD_NEG']==z['original_domain_review']=='OPEN'
    # Exact local cap-defect sharpness for a quadratic with smaller curvature.
    for local in [F(0),F(786),F(-786)]:
        # m(x)=local*x*(x-d)/2 has zero endpoint interpolant.
        lower=(2145-786)*d*d/8
        actual_mid=-local*d*d/8+2145*d*d/8
        assert actual_mid>=lower>0
    print('INDEPENDENT ORIGINAL BS / GLOBAL AFFINE CAP STOP REPLAY PASS: positive true ray <8e-18 per norm; true BS norm >1-6e-12; affine cap norm >1+3e-10; original whole signed gate OPEN')
if __name__=='__main__':main()
