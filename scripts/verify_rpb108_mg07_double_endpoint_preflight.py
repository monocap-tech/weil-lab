#!/usr/bin/env python3
"""Cheap exact endpoint-jet preflight. No frequency quadrature."""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
from validate_rpb108_si06_negative_band import B,PI
from validate_rpb108_si14_odd_multiband_nogo import cos_sin_pi_multiple
from validate_rpb108_sm42_original_physical_gram_and_low_gate import I,hyperbolic_interval

INPUT_SHA='c787b09536c41bbb3355550f4f4814762dedd0b0ec03155db9e5777b2c1cad0b'
PI_LO=F(333,106)
CENTER=F(37,64)
L=F(12)
DEN=10**12

def up(x):
    return F(-((-x.numerator*DEN)//x.denominator),DEN)

def down(x):
    return F((x.numerator*DEN)//x.denominator,DEN)

def absup(x):
    return max(abs(x.l),abs(x.h))

def interval(x):
    return [str(down(x.l)),str(up(x.h))]

def tail(a,b):
    return 2*sum((x*y*L**(-(i+j+1))*(
        (17+4*F(347,500))/F(i+j+1)+F(1,(i+j+1)**2))
        for i,x in enumerate(a) for j,y in enumerate(b)),F(0))

def exact_schur_coordinate_regression():
    h00,h01,h11=F(2),F(1,3),F(3)
    b0,b1,d=F(1,5),F(-1,7),F(5,4)
    c0,c1=F(2),F(-3)
    det=h00*h11-h01*h01
    def response(x,y):
        return (h11*x*x-2*h01*x*y+h00*y*y)/det
    old=d-response(b0,b1)
    bp0=b0+h00*c0+h01*c1
    bp1=b1+h01*c0+h11*c1
    dp=d+2*(c0*b0+c1*b1)+h00*c0*c0+2*h01*c0*c1+h11*c1*c1
    assert dp-response(bp0,bp1)==old
    return True

def evaluate(path):
    raw=Path(path).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==INPUT_SHA
    old=json.loads(raw)
    assert old['original_lowband_cells']==7168
    assert old['strict_scalar_schur_positive_certified'] is False
    assert B==F(11,10) and PI[0]>PI_LO
    sn,cs=[I(*x) for x in cos_sin_pi_multiple(2*B*CENTER)]
    sh=hyperbolic_interval(B/2,'sinh')
    ch=hyperbolic_interval(B/2,'cosh')
    w=2*I(*PI)*CENTER
    determinant=sn*ch/2-sh*w*cs
    assert determinant.l>F(944,1000) and determinant.h<F(945,1000)
    rhs0=-B*cs
    rhs1=-cs+w*B*sn
    a=(rhs0*ch/2-sh*rhs1)/determinant
    b=(sn*rhs1-rhs0*w*cs)/determinant
    assert a.width()<F(1,10**10) and b.width()<F(1,10**10)
    # Exact REAL coefficients are defined by the endpoint matrix inverse.
    # Their rational interval enclosures rigorously bound all tail constants.
    assert (B*cs+a*sn+b*sh).l<=0<=(B*cs+a*sn+b*sh).h
    assert (cs-w*B*sn+a*w*cs+b*ch/2).l<=0<=(cs-w*B*sn+a*w*cs+b*ch/2).h
    def third_constant(ai,bi):
        endpoint2=-2*w*sn-w*w*B*cs-ai*w*w*sn+bi*sh/4
        third_l1=(6*B*w.h**2+w.h**3*B**2+
                  2*B*absup(ai)*w.h**3+absup(bi)*sh.h/2)
        return up((2*absup(endpoint2)+third_l1)/(8*PI_LO**3))
    C3=third_constant(a,b)
    pure=[F(0),F(0),C3]
    a0=F((a.mid()*10**6+F(1,2)).__floor__(),10**6)
    b0=F((b.mid()*10**6+F(1,2)).__floor__(),10**6)
    endpoint0=B*cs+a0*sn+b0*sh
    endpoint1=cs-w*B*sn+a0*w*cs+b0*ch/2
    rational=[up(absup(endpoint0)/PI_LO),
              up(absup(endpoint1)/(2*PI_LO**2)),
              third_constant(I(a0),I(b0))]
    assert a0==F(1884803,10**6) and b0==F(3707850,10**6)
    assert rational[0]>0 and rational[1]>0
    anchors=[[F(v) for v in row] for row in old['anchor_packet_tail_coefficients']]
    mass=F(old['high12_weighted_negative_mass'])
    records=[]
    for label,coeff in [('exact_real_double_endpoint',pure),
                        ('rational_rounded_double_endpoint',rational)]:
        payments=[up(tail(v,coeff)) for v in anchors]
        beta=sum((v/L**i for i,v in enumerate(coeff)),F(0))
        negative=up(mass*beta*beta)
        ratios=[F(v)/p for v,p in zip(old['high12_complete_cross_absolute_payments'],payments)]
        neg_ratio=F(old['high12_negative_diagonal_payment'])/negative
        assert min(ratios)>10 and neg_ratio>48
        records.append(dict(kind=label,
            uniform_fourier_tail_coefficients=list(map(str,coeff)),
            high12_complete_mixed_absolute_upper=list(map(str,payments)),
            old_to_new_mixed_payment_ratios=list(map(str,ratios)),
            high12_negative_diagonal_upper=str(negative),
            old_to_new_negative_diagonal_ratio=str(neg_ratio)))
    assert exact_schur_coordinate_regression()
    return dict(status='CERTIFIED_CONDITIONAL_ENDPOINT_JET_PREFLIGHT',
        input_run_id=40267592408,input_artifact_id=12627027140,input_json_sha256=INPUT_SHA,
        endpoint_matrix_determinant_interval=interval(determinant),
        exact_real_a_interval=interval(a),exact_real_b_interval=interval(b),
        exact_real_coefficients_defined_by_matrix_inverse=True,
        exact_real_fourier_decay_order=3,
        rational_a=str(a0),rational_b=str(b0),
        rational_endpoint_value_interval=interval(endpoint0),
        rational_endpoint_derivative_interval=interval(endpoint1),
        rational_approximants_have_pure_cubic_decay=False,
        exact_schur_unchanged_under_anchor_addition=True,
        measurements=records,frequency_quadrature_repeated=False,
        payment_comparison_changes_basis_representative=True,
        new_complete_lowband_and_scalar_schur_certified=False,
        full_2x2_inverse_and_mixed_covariance_required=True,
        SI29_normalized_energy_response='OPEN',Birman_Schwinger_supported_inverse='OPEN',
        whole_original_odd_even_CC27_Weil_RH='OPEN')

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--input',required=True)
    p.add_argument('--output',default='artifacts/mg07_double_endpoint_preflight.json')
    args=p.parse_args()
    d=evaluate(args.input)
    out=Path(args.output);out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(d,indent=2)+'\n')
    print('ENDPOINT JET PREFLIGHT PASS',d['exact_real_a_interval'],d['exact_real_b_interval'])
    for r in d['measurements']:
        print(r['kind'],'mixed reductions',*[float(F(x)) for x in r['old_to_new_mixed_payment_ratios']],
              'negative reduction',float(F(r['old_to_new_negative_diagonal_ratio'])))
