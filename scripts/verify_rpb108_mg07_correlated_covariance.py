#!/usr/bin/env python3
"""Reuse accepted lowband covariance; no integration or source-count campaign."""
import argparse
from fractions import Fraction as F
from itertools import product
import hashlib,json
from pathlib import Path

PINS=[
 '264fd853ca006a578d76369ac5bd4588a2097145b829fbba7036693f29b04044',
 'c787b09536c41bbb3355550f4f4814762dedd0b0ec03155db9e5777b2c1cad0b',
 'fa9b4224c75b45411915beb93c0217746693780588d728ef144fefde15fe4793']
OFFS=((0,1),(0,2),(1,2))
DEN=10**15

def outward(v,upper=False):
    v=F(v);n=v.numerator*DEN
    return F(-((-n)//v.denominator) if upper else n//v.denominator,DEN)

def congruence(h,p):
    return [[sum((p[x][i]*h[x][y]*p[y][j]
                  for x in range(3) for y in range(3)),F(0))
             for j in range(3)] for i in range(3)]

def schur(h):
    a,d,b=h[0][0],h[1][1],h[0][1]
    det=a*d-b*b
    assert a>0 and det>0
    x,y=h[0][2],h[1][2]
    return h[2][2]-(d*x*x-2*b*x*y+a*y*y)/det

def serialize(h):
    return [[str(v) for v in row] for row in h]

def run(paths):
    data=[]
    for path,pin in zip(paths,PINS):
        raw=Path(path).read_bytes()
        assert hashlib.sha256(raw).hexdigest()==pin
        data.append(json.loads(raw))
    anchor,mixed,jet=data
    assert anchor['positive_high12_form_discarded_as_psd'] is True
    assert anchor['cross_bound_scope']=='lowband_plus_pole_minus_negative_high_tail'
    assert F(anchor['lowband_baseline_rounding_upper_payment'])==F(7168,10**9)
    assert mixed['original_lowband_cells']==7168
    assert mixed['strict_scalar_schur_positive_certified'] is False
    assert jet['frequency_quadrature_repeated'] is False
    assert jet['exact_schur_unchanged_under_anchor_addition'] is True
    intervals=[[[F(0),F(0)] for _ in range(3)] for _ in range(3)]
    def enclosure(row):
        return [outward(row[0]),outward(row[1],True)]
    for i in range(2):
        for j in range(2):
            intervals[i][j]=enclosure(anchor['signed_lowband_plus_pole_intervals'][i][j])
    for k,(i,j) in enumerate(((0,2),(1,2),(2,2))):
        intervals[i][j]=intervals[j][i]=enclosure(mixed['lowband_signed_plus_pole_intervals'][k])
    a=F(jet['rational_a'])
    b=F(jet['rational_b'])-F(mixed['rational_sinh_alignment'])
    t=F(4096,3013)
    c0=(a+b)/(1+t);c1=a-c0
    assert c0+c1==a and t*c0-c1==b
    p=[[F(1),F(0),c0],[F(0),F(1),c1],[F(0),F(0),F(1)]]
    rec=next(r for r in jet['measurements'] if r['kind']=='rational_rounded_double_endpoint')
    beta=[sum((F(v)/F(12)**i for i,v in enumerate(row)),F(0))
          for row in mixed['anchor_packet_tail_coefficients']]
    beta.append(sum((F(v)/F(12)**i for i,v in enumerate(rec['uniform_fourier_tail_coefficients'])),F(0)))
    beta=[outward(v,True) for v in beta]
    mass=outward(mixed['high12_weighted_negative_mass'],True)
    assert all(v>0 for v in beta) and 0<mass<F(423,25000)
    # For real z, the joint negative-tail form is at most
    # mass*(sum beta_i*|z_i|)^2 = max_s mass*(sum s_i beta_i z_i)^2.
    # Four sign vectors suffice up to common sign. Real source matrices
    # also control complex coefficients by splitting real/imaginary parts.
    for z in [(F(1),F(-2),F(3)),(F(0),F(2),F(-1)),(F(-1),F(-1),F(-1))]:
        lhs=mass*sum((b*abs(x) for b,x in zip(beta,z)),F(0))**2
        rhs=max(mass*(beta[0]*z[0]+s*beta[1]*z[1]+q*beta[2]*z[2])**2
                for s,q in product((-1,1),repeat=2))
        assert lhs==rhs
    cases=[];zero_cases=[]
    for k,off in enumerate(product(*[intervals[i][j] for i,j in OFFS])):
        h=[[F(0)]*3 for _ in range(3)]
        for i in range(3):h[i][i]=intervals[i][i][0]
        for (i,j),v in zip(OFFS,off):h[i][j]=h[j][i]=v
        g=congruence(h,p)
        zero_cases.append(dict(corner=k,matrix=serialize(g),schur_lower=str(schur(g))))
        for signs in product((-1,1),repeat=2):
            v=[beta[0],signs[0]*beta[1],signs[1]*beta[2]]
            lower=[[g[i][j]-mass*v[i]*v[j] for j in range(3)] for i in range(3)]
            cases.append(dict(corner=k,tail_signs=list(signs),
                              matrix=serialize(lower),schur_lower=str(schur(lower))))
    assert len(cases)==32 and len(zero_cases)==8
    worst=min(cases,key=lambda r:F(r['schur_lower']))
    zero=min(zero_cases,key=lambda r:F(r['schur_lower']))
    gamma=F(worst['schur_lower']);zero_gamma=F(zero['schur_lower'])
    assert gamma<zero_gamma<0
    old=F(mixed['complete_signed_scalar_schur_lower'])
    assert gamma>old and abs(old/gamma)>300
    return dict(status='CERTIFIED_CONDITIONAL_CORRELATED_COVARIANCE_REPLAY_INCONCLUSIVE',
        input_json_sha256=PINS,original_source_count_changed=False,
        frequency_quadrature_repeated=False,
        rational_basis_congruence=serialize(p),
        lowband_original_interval_matrix=[[[str(v) for v in row] for row in rows] for rows in intervals],
        joint_negative_mass_upper=str(mass),joint_packet_betas=list(map(str,beta)),
        vertex_cases=cases,zero_negative_tail_cases=zero_cases,
        correlated_complete_signed_schur_lower=str(gamma),
        optimistic_zero_negative_tail_box_schur_lower=str(zero_gamma),
        previous_complete_mixed_schur_lower=str(old),
        scalar_schur_positive_certified=False,
        fixed_interval_box_and_tail_only_refinement_can_certify_PSD=False,
        corner_negative_is_not_original_negative_witness=True,
        unmeasured_positive_high_form_discarded_as_whole_PSD=True,
        complete_original_remaining_Schur='OPEN',SI29_normalized_response='OPEN',
        independent_original_domain_review='OPEN',odd_even_CC27_Weil_RH='OPEN')

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--anchor',required=True)
    p.add_argument('--mixed',required=True)
    p.add_argument('--jet',required=True)
    p.add_argument('--output',default='artifacts/mg07_correlated_covariance_replay.json')
    args=p.parse_args()
    z=run([args.anchor,args.mixed,args.jet])
    out=Path(args.output);out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(z,indent=2)+'\n')
    print('CORRELATED COVARIANCE REPLAY PASS; Schur lower',
          float(F(z['correlated_complete_signed_schur_lower'])),
          'zero-tail fixed-box floor',float(F(z['optimistic_zero_negative_tail_box_schur_lower'])))
