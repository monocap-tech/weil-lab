#!/usr/bin/env python3
"""Consume NF29: quantitative original positivity on Z3 plus ALL F112."""
import argparse,hashlib,json
from fractions import Fraction as F
from pathlib import Path

def run(nf29,targets,trial,response):
    k=F(207,1000);pieces=[];source_trace=F(0);lift_trace=F(0)
    for z,t,y,w in zip(nf29['parity_certificates'],targets['authenticated_compensated_targets'],trial['parities'],response['parity_certificates']):
        assert z['parity']==t['parity']==y['parity']==w['parity']
        mx=sum(F(x)**2 for x in t['retained_coefficients']);mw=F(w['exact_response_norm_squared'])
        assert mx>0 and mw>0
        assert sum(F(a)*F(b) for a,b in zip(t['retained_coefficients'],w['exact_rational_retained_response']))==0
        S=z['sufficient_collective_matrix'];G=z['original_complete_residual_Gram']
        a=list(map(F,S[0][0]));d=list(map(F,S[1][1]));assert a[0]>0
        hseed=sum(F(x)**2 for x in t['exact_rational_high_compensation'])+sum(F(x)**2 for x in y['rational_correction_coefficients'])
        assert set(t['high_indices']).isdisjoint(y['high_indices'])
        source_trace+=F(G[0][0][1])/mx;lift_trace+=hseed/mx
        if z['parity']=='even':
            mu=a[0]/mx;dimension=1
            assert z['sufficient_collective_test_status']=='SUFFICIENT_MATRIX_REJECTED'
        else:
            determinant=F(z['sufficient_matrix_determinant'][0]);assert determinant>0 and d[0]>0
            # U>0 and M=diag(mx,mw): min generalized eigenvalue
            # >=1/trace(U^-1 M)=det(U)/(d*mx+a*mw).
            mu=determinant/(d[1]*mx+a[1]*mw);dimension=2
            source_trace+=F(G[1][1][1])/mw
            lift_trace+=sum(F(x)**2 for x in z['fixed_rational_high_lift'])/mw
            assert z['sufficient_collective_test_status']=='PASS'
        assert mu>0
        pieces.append(dict(parity=z['parity'],retained_dimension=dimension,physical_retained_Schur_gap_lower=str(mu),
            retained_seed_mass_squared=str(mx),retained_response_mass_squared=str(mw)))
    mu=min(F(z['physical_retained_Schur_gap_lower']) for z in pieces)
    eta2=source_trace/(k*k);xi2=lift_trace
    # For trial lift H and high response C^-1 R, J=H-C^-1 R:
    # ||J||^2 <=2 xi^2+2 eta^2. Physical square completion then
    # costs at most (1+4 xi^2+4 eta^2) on retained physical mass.
    denominator=1+4*eta2+4*xi2
    physical_gap=min(mu/denominator,k/2)
    assert physical_gap>F('3.32e-36')
    crossings=[]
    j=F(1,3)
    for s in [F(-1,100),F(0),F(1,100)]:
        # High floor is exactly one and the actual Schur sign crosses.
        det=s;ground_sign=(s>0)-(s<0)
        proof_gap=min(s/(1+2*j*j),F(1,2)) if s>0 else None
        if proof_gap is not None:
            assert s-proof_gap*(s+j*j+1)+proof_gap**2>0
        crossings.append(dict(retained_diagonal=str(s+j*j),mixed=str(-j),high_diagonal='1',
            actual_Schur=str(s),determinant=str(det),ground_sign=ground_sign,
            physical_gap_lower=str(proof_gap) if proof_gap is not None else None))
    levels=[]
    for level in [F(1,1000),F(1,10),F(2)]:
        # The null crossing has PSD rank one. Adding level I gives
        # exactly that smallest physical eigenvalue.
        det=(j*j+level)*(1+level)-j*j;assert det>0
        levels.append(dict(whole_mass_shift=str(level),physical_ground_level=str(level),determinant=str(det)))
    return dict(milestone='CC73',aperture='53/50',retained_space='span(x_even,x_odd,w_odd)',retained_dimension=3,
        included_high_space='entire F112',excluded_retained_dimension=109,parity_pieces=pieces,
        physical_retained_Schur_gap_lower=str(mu),complete_trial_source_physical_trace_upper=str(source_trace),
        trial_high_lift_physical_trace_upper=str(lift_trace),high_response_operator_square_upper=str(eta2),
        physical_mass_conversion_factor_upper=str(denominator),
        original_Z3_plus_all_F112_physical_gap_lower=str(physical_gap),strict_display_physical_gap='3.32e-36',
        original_null_with_retained_component_in_Z3_excluded=True,old_whole_domain_gap_used=False,
        genuine_crossing_controls=crossings,positive_whole_mass_levels=levels,
        actual_critical_eigenvector_frame_certified=False,whole_aperture_positive=False,full_retained_Schur=False,
        full_Weil_nonimplication_claimed=False,RH=False,F4=False,Lean=False)
if __name__=='__main__':
    p=argparse.ArgumentParser()
    for a in ['source','targets','trial','response']:p.add_argument(a)
    p.add_argument('--output',required=True);a=p.parse_args()
    raw=[Path(v).read_bytes() for v in [a.source,a.targets,a.trial,a.response]]
    assert [hashlib.sha256(v).hexdigest() for v in raw]==['069d4acc267a0ac48154427a033cccca96243743dd31e36449f7189de03e895a','6eee61fb4e58ac5be0e95f492f461b289da37ee13aeaa74bbf4acc06f6650c00','814fe0fcc3aff4eecbe4e6c6eead5ce28927043877c0df9cfa03e3a5c71c2336','2110e07c7a7e39d2b454cff364c0863f6f3e3ff151cf72309999130f5e17fe42']
    r=run(*(json.loads(v) for v in raw));r['input_sha256']=[hashlib.sha256(v).hexdigest() for v in raw]
    Path(a.output).write_text(json.dumps(r,indent=2)+'\n')
    print('Z3+ALL F112 physical gap',float(F(r['original_Z3_plus_all_F112_physical_gap_lower'])))
