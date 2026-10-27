#!/usr/bin/env python3
"""Exact mixed-column composition and independent Cauchy/physical validation replay."""
import hashlib,json,sys
from fractions import Fraction as Q
from pathlib import Path
from math import factorial
RANK_SHA='9b9820a0163e5e8bf08dd1c2525c757ff67214b49a40cb093d00bc611c9ff9e2'
CRITICAL_SHA='a84b19c1fefc4e680c5c19ea643bbe5badce639374cb0a424211ee980020f922'
def dy(v):return Q(int(v[0]))*Q(2)**int(v[1])
def ball(v):
    m,r=dy(v[0]),dy(v[1]);assert r>=0;return m-r,m+r
def add(x,y):return x[0]+y[0],x[1]+y[1]
def scale(x,c):return (c*x[0],c*x[1]) if c>=0 else (c*x[1],c*x[0])
def mul(x,y):
    a=[v*w for v in x for w in y];return min(a),max(a)
def intersects(x,y):assert x[0]<=y[1] and y[0]<=x[1]
def subset(x,y):assert y[0]<=x[0]<=x[1]<=y[1]
def cball(v):return ball(v[0]),ball(v[1])
def cadd(x,y):return add(x[0],y[0]),add(x[1],y[1])
def cmul(x,y):return add(mul(x[0],y[0]),scale(mul(x[1],y[1]),-1)),add(mul(x[0],y[1]),mul(x[1],y[0]))
def cpow(x,n):
    y=((Q(1),Q(1)),(Q(0),Q(0)))
    for _ in range(n):y=cmul(y,x)
    return y
def hyper_upper(t,odd):
    last=33 if odd else 32
    head=sum((t**n/factorial(n) for n in range(int(odd),last+1,2)),Q(0));n=last+2
    return head+t**n/factorial(n)/(1-t*t/Q((n+1)*(n+2)))
def main():
    assert len(sys.argv)==5
    z=json.load(open(sys.argv[1]));v=json.load(open(sys.argv[2]));raw=Path(sys.argv[3]).read_bytes();cr=Path(sys.argv[4]).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==RANK_SHA==z['rank_input_sha256'] and hashlib.sha256(cr).hexdigest()==CRITICAL_SHA==z['critical_input_sha256']
    rank,critical=json.loads(raw),json.loads(cr)
    assert v['column_sha256']==hashlib.sha256(Path(sys.argv[1]).read_bytes()).hexdigest() and v['working_precision_bits']==512
    assert z['status']=='CONDITIONAL_ORIGINAL_COMPLETE_RAW_SIGNED_CRITICAL_MIXED_BLOCK' and z['working_precision_bits']==512 and z['flint_version']=='0.8.0'
    assert z['target_probe']==critical['exact_candidates']['probes'][0] and z['target_sine_frequencies']==critical['exact_candidates']['sine_frequencies']
    assert z['target_probes']==critical['exact_candidates']['probes'] and z['critical_target_count']==4 and z['complete_mixed_entry_count']==968
    prior=tuple(map(Q,critical['complete_scalar_witnesses'][0]['signed_energy_interval']));assert list(map(str,prior))==z['target_prior_signed_interval']
    qsum=(Q(0),Q(0))
    for key in ['arch','prime','pole']:qsum=add(qsum,ball(z['target_signed_components_native'][key]))
    subset(qsum,prior);subset(ball(z['target_signed_kernel_native']),prior)
    for i in range(4):
        for j in range(4):
            priorij=tuple(map(Q,critical['complete_signed_Gram_intervals'][i][j]));subset(ball(z['target_signed_kernel_Gram_native'][i][j]),priorij)
            parts=z['target_signed_kernel_Gram_components_native'][i][j]
            subset(add(add(ball(parts['arch']),ball(parts['prime'])),ball(parts['pole'])),priorij)
    expected=[];offset=0
    for j,((c,p),n) in enumerate(zip(rank['original_nodes'],rank['selected_multiplicities'])):
        for k in range(n):expected.append((offset+k,j,c,k))
        offset+=p
    expected.append((469,None,None,None));assert offset==469 and len(expected)==z['retained_source_count']==242
    maxrad=Q(0);rawsums=[Q(0)]*4
    for row,meta in zip(z['rows'],expected):
        assert tuple(row[k] for k in ['original_source_index','cluster','center','order'])==meta
        norm=tuple(map(Q,row['source_norm_squared_interval']));assert norm[0]>0 and all((x*10**80).denominator==1 for x in norm)
        assert len(row['entries'])==4
        for t,e in enumerate(row['entries']):
            assert e['target_index']==t;interval=tuple(map(Q,e['signed_interval']));assert all((x*10**80).denominator==1 for x in interval)
            parts={key:ball(x) for key,x in e['components_native'].items()}
            total=add(add(parts['arch'],parts['prime']),parts['pole']);subset(total,interval);subset(ball(e['signed_native']),interval)
            intersects(parts['prime'],ball(e['independent_prime_native']));intersects(parts['pole'],ball(e['independent_pole_native']))
            maxrad=max(maxrad,dy(e['signed_native'][1]));rawsums[t]+=max(map(abs,interval))**2
    assert maxrad==Q(z['maximum_native_block_radius'])<Q(1,10**70)
    assert rawsums==list(map(Q,z['raw_coordinate_column_squared_uppers'])) and z['max_required_frequency_derivative_order']==13
    assert z['Laplace_terms']==64 and z['analytic_tail_strip_imaginary_bound']=='3/4' and z['Cauchy_radius']=='1/4'
    # Exact elementary proof of the CLEAN infinite Laplace remainder.
    x=Q(7,10);assert sum((x**k/factorial(k) for k in range(5)),Q(0))>2
    assert Q(511,4)*Q(11,5)>401*x and Q(22,5)>6*x
    tail_rough=2*Q(1,2**401)/(Q(511,4)*(1-Q(1,64)))
    assert tail_rough<Q(1,2**406)==Q(z['Laplace_tail_Cauchy_base_upper'])
    assert z['all_968_seven_prime_and_true_pole_cross_checks_passed'] is True
    assert rank['retained_original_pole'] is True
    assert Q(z['signed_physical_selected_complement_floor'])==Q(1,1000)-Q(rank['pruned_physical_complement_negative_upper'])>Q(98,10**5)
    for k in ['production_block_quadrature_used','global_source_monomial_expansion_used','full_physical_frame_transform_applied','raw_block_is_BS_mixed_block','raw_block_is_strong_residual','finite_BS_block_or_inverse_computed','critical_physical_projection_computed','augmented_frame_condition_certified','signed_Schur_or_global_sign_certified']:assert z[k] is False
    assert z['W_ODD_NEG']==z['inherited_original_domain_review']=='OPEN'
    # Entirely independent ORIGINAL physical scalar form comparisons.
    assert v['status']=='CONDITIONAL_SIGNED_KERNEL_PHYSICAL_AND_CAUCHY_VALIDATION' and len(v['anchor_cases'])==3
    assert [(x['sine'],x['pole']) for x in v['anchor_cases']]==[(1,0),(0,1),(1,1)]
    for case in v['anchor_cases']:
        for a,b in zip(case['kernel_components'],case['direct_physical_components']):intersects(ball(a),ball(b))
    B=Q(11,10);a=list(map(Q,z['target_probe']['sine_coefficients']));b=Q(z['target_probe']['sinh_coefficient']);cs=list(map(Q,z['target_sine_frequencies']))
    assert hyper_upper(B/2,True)<Q(3,5) and hyper_upper(B/2,False)/2<Q(3,5) and hyper_upper(B,True)-B<1
    assert 2*B*Q(rank['original_SM40_two_sided_mass'])<37
    S=sum(map(abs,a),Q(0))+Q(3,5)*abs(b);D=Q(44,7)*sum((abs(x)*c for x,c in zip(a,cs)),Q(0))+Q(3,5)*abs(b)
    Nf=2*B*S*S;Aof=36*Nf+8*S*S+8*B*B*D*D
    Nu=2*B*Q(3,2)**2;Aou=36*Nu+8*Q(3,2)**2+8*B*B*6**2
    assert Q(44,7)*Q(37,64)+Q(1,4)<4 and 1/(1-B/4)<Q(3,2)
    majorant=(Aof+Aou)/2+Q(39,2)*(Nf+Nu);M=Q(10**8)
    assert majorant==Q(v['analytic_majorant_composed_upper'])<M==Q(v['analytic_majorant'])
    assert [S,D,Nf,Aof,Nu,Aou]==[Q(v[k]) for k in ['source_probe_amplitude_upper','source_probe_derivative_amplitude_upper','source_probe_norm_upper','source_probe_Ao_upper','circle_sine_norm_upper','circle_sine_Ao_upper']]
    n=256;k=13;r=Q(1,8);R=Q(1,4)
    assert (v['Cauchy_nodes'],v['Cauchy_order'],Q(v['Cauchy_radius']),Q(v['analytic_radius']))==(n,k,r,R)
    alias=M/R**k*(r/R)**n/(1-(r/R)**n)*factorial(k)
    assert alias==Q(v['Cauchy_derivative_alias_error_upper'])
    total=((Q(0),Q(0)),(Q(0),Q(0)));assert len(v['Cauchy_points'])==256
    for j,point in enumerate(v['Cauchy_points']):
        assert point['index']==j
        omega=cball(point['omega_native']);phase=cball(point['inverse_phase_native']);value=cball(point['mixed_value_native'])
        identity=cmul(cpow(omega,k),phase)
        assert identity[0][0]<=1<=identity[0][1] and identity[1][0]<=0<=identity[1][1]
        total=cadd(total,cmul(value,phase))
    factor=Q(factorial(k),n)/r**k*(-1)**(k//2)
    estimate=(scale(total[0],factor),scale(total[1],factor));recorded=cball(v['Cauchy_derivative_estimate_native'])
    intersects(estimate[0],recorded[0]);intersects(estimate[1],recorded[1])
    wanted=next(row for row in z['rows'] if row['original_source_index']==13)
    intersects((estimate[0][0]-alias,estimate[0][1]+alias),tuple(map(Q,wanted['entries'][0]['signed_interval'])))
    assert estimate[1][0]-alias<=0<=estimate[1][1]+alias
    assert v['compared_column_original_source_index']==13 and v['compared_column_target_index']==0 and v['global_mixed_or_inverse_bound_certified'] is False and v['W_ODD_NEG']=='OPEN'
    print('INDEPENDENT SIGNED CRITICAL MIXED BLOCK REPLAY PASS: 242x4 complete raw entries, all prime/pole checks, accepted full critical Gram, physical anchor and Cauchy order13 checks; physical complementary floor >0.00098; transformed/global gate OPEN')
if __name__=='__main__':main()
