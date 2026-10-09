#!/usr/bin/env python3
"""Exact consumer of original NF28 mixed Gram; no source quadrature."""
import argparse,hashlib,json
from fractions import Fraction as F
from pathlib import Path

def interval(v):return tuple(map(F,v))
def mixed_score(S,alpha):
    a,b,d=interval(S[0][0]),interval(S[0][1]),interval(S[1][1])
    signed=[-2*alpha*x for x in b]
    return (a[0]+min(signed)+alpha**2*d[0],a[1]+max(signed)+alpha**2*d[1])
def strings(v):return list(map(str,v))
def run(native,targets,response):
    rows=[];k=F(207,1000)
    for row,t,w in zip(native['parity_certificates'],targets['authenticated_compensated_targets'],response['parity_certificates']):
        assert row['parity']==t['parity']==w['parity']
        S=row['sufficient_collective_matrix'];Q=row['original_finite_two_direction_energy'];G=row['original_complete_mixed_residual_Gram']
        a,b,d=interval(S[0][0]),interval(S[0][1]),interval(S[1][1])
        assert a[0]>0 and d[1]<0 and F(row['sufficient_matrix_determinant'][1])<0
        # The midpoint selects a fixed rational alpha, not a proof bound.
        optimum=(b[0]+b[1])/(d[0]+d[1]);alpha=F((optimum*10**6).__floor__(),10**6)
        trials=[]
        for label,weight in [('finite_response',F(1)),('signed_source_selected',alpha)]:
            score=mixed_score(S,weight);energy=mixed_score(Q,weight);source=mixed_score(G,weight)
            assert score[0]>0 and energy[0]>0 and source[0]>0
            if label=='signed_source_selected':assert score[0]>a[1]
            mass=sum(F(x)**2 for x in t['retained_coefficients'])+weight**2*F(w['exact_response_norm_squared'])
            assert sum(F(x)*F(y) for x,y in zip(t['retained_coefficients'],w['exact_rational_retained_response']))==0
            # Independent recombination of paid Q and Gamma enclosures.
            recombined=energy[0]-source[1]/k
            assert recombined>0
            trials.append(dict(label=label,alpha=str(weight),native_energy_interval=strings(energy),
                complete_source_square_interval=strings(source),coarse_Schur_score_interval=strings(score),
                independent_energy_minus_source_lower=str(recombined),
                retained_physical_mass_squared=str(mass),retained_physical_Schur_gap_lower=str(score[0]/mass),
                retained_direction='x-alpha*w',positive_original_directional_Schur=True))
        # A complete norm Gram cannot determine a signed inverse Gram.
        # Record the necessary scalar credit on w to repair its diagonal.
        dw=interval(G[1][1]);qw=interval(Q[1][1])
        necessary_credit=dw[0]/k-qw[1];fraction=1-k*qw[1]/dw[0]
        assert necessary_credit>0 and 0<fraction<1
        rows.append(dict(parity=row['parity'],original_seed_score_interval=strings(a),
            trials=trials,strict_improvement_over_original_score_certified=True,
            necessary_w_response_credit_lower=str(necessary_credit),
            necessary_w_fraction_of_floor_response_removed_lower=str(fraction),
            native_joint_form_positive=True,coarse_joint_form_indefinite=True,
            joint_actual_Schur_positive_certified=False))
    controls=[]
    # Actual crossing with fixed positive trial diagonal. The score has
    # a positive direction on both sides; this cannot certify the matrix.
    for sign in [F(-1,100),F(0),F(1,100)]:
        M=[[F(1),F(1,2)],[F(1,2),F(1,4)+sign]]
        det=M[0][0]*M[1][1]-M[0][1]**2;assert det==sign
        assert M[0][0]>0
        controls.append(dict(determinant=str(det),tested_direction_score='1',whole_sign=(sign>0)-(sign<0)))
    scaled=[];eps=F(1,10**18)
    for sign in [F(-1,100),F(0),F(1,100)]:
        det=eps**2*sign
        scaled.append(dict(retained_diagonal=str(eps**2),determinant=str(det),tested_direction_score=str(eps**2),whole_sign=(sign>0)-(sign<0)))
    levels=[]
    for level in [F(1,1000),F(1,10),F(2)]:
        det=(1+level)*(F(1,4)+level)-F(1,4)
        assert det>0
        levels.append(dict(whole_mass_shift=str(level),ground_level=str(level),determinant=str(det)))
    return dict(milestone='CC72',aperture='53/50',parity_certificates=rows,
        finite_response_modified_seed_span_dimension=2,signed_selected_modified_seed_span_dimension=2,
        opposite_parity_mixed_term_zero=True,genuine_crossing_controls=controls,near_critical_crossing_controls=scaled,positive_whole_mass_levels=levels,
        whole_aperture_positive=False,collective_retained_frame=False,full_Weil_nonimplication_claimed=False,RH=False,F4=False,Lean=False)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('targets');p.add_argument('response');p.add_argument('--output',required=True);a=p.parse_args()
    raw=[Path(v).read_bytes() for v in [a.source,a.targets,a.response]]
    assert [hashlib.sha256(v).hexdigest() for v in raw]==['27819654bc8aa7f9e98f1ef8638c99f9afbcac07dabd2d6c079bfbfbde70e8c1','6eee61fb4e58ac5be0e95f492f461b289da37ee13aeaa74bbf4acc06f6650c00','2110e07c7a7e39d2b454cff364c0863f6f3e3ff151cf72309999130f5e17fe42']
    r=run(*(json.loads(v) for v in raw));r['input_sha256']=[hashlib.sha256(v).hexdigest() for v in raw]
    Path(a.output).write_text(json.dumps(r,indent=2)+'\n')
    for z in r['parity_certificates']:
        for t in z['trials']:print(z['parity'],t['label'],t['alpha'],float(F(t['coarse_Schur_score_interval'][0])))
