#!/usr/bin/env python3
"""Original physical full-high restriction; native remainder kept separate."""
import argparse,base64,gzip,hashlib,json
from fractions import Fraction as F
from pathlib import Path

def run(expanded,old,targets,seed_trial,response,expanded_trial,remaining):
    k=F(207,1000);pieces=[];source_trace=F(0);lift_trace=F(0)
    for index,t in enumerate(targets['authenticated_compensated_targets']):
        z=expanded if index==0 else old['parity_certificates'][1]
        w=response['parity_certificates'][index];y=seed_trial['parities'][index]
        assert z['sufficient_collective_test_status']=='PASS'
        mx=sum(F(x)**2 for x in t['retained_coefficients']);mw=F(w['exact_response_norm_squared'])
        assert mx>0 and mw>0
        assert sum(F(x)*F(v) for x,v in zip(t['retained_coefficients'],w['exact_rational_retained_response']))==0
        S=z['sufficient_collective_matrix'];a=list(map(F,S[0][0]));d=list(map(F,S[1][1]));det=F(z['sufficient_matrix_determinant'][0])
        assert min(a[0],d[0],det)>0
        mu=det/(d[1]*mx+a[1]*mw)
        gram=z['original_complete_residual_Gram']
        source_trace+=F(gram[0][0][1])/mx+F(gram[1][1][1])/mw
        highseed=sum(F(x)**2 for x in t['exact_rational_high_compensation'])+sum(F(x)**2 for x in y['rational_correction_coefficients'])
        assert set(t['high_indices']).isdisjoint(y['high_indices'])
        oldh=old['parity_certificates'][index]
        highresponse=sum(F(x)**2 for x in oldh['fixed_rational_high_lift'])
        if index==0:
            assert set(oldh['high_lift_indices']).isdisjoint(expanded_trial['additional_high_indices'])
            highresponse+=sum(F(x)**2 for x in expanded_trial['fixed_rational_coefficients'])
        lift_trace+=highseed/mx+highresponse/mw
        native=remaining['parity_certificates'][index]
        assert native['remaining_dimension']==54 and native['finite_full_retained_lifted_family_positive']
        assert not native['remaining_complete_source_Gram_certified']
        assert all(len(v)==54 for v in native['remaining_original_native_couplings'])
        pieces.append(dict(parity=t['parity'],physical_retained_pair_gap_lower=str(mu),
            retained_mass_diagonal=[str(mx),str(mw)],remaining_native_dimension=54,
            remaining_native_physical_gap_lower=native['physical_remaining_native_gap_lower'],
            finite_remaining_reaction_fractions=native['diagonal_finite_reaction_fractions'],
            remaining_high_condensed_gap_certified=False))
    mu=min(F(p['physical_retained_pair_gap_lower']) for p in pieces)
    eta2=source_trace/(k*k);factor=1+4*eta2+4*lift_trace
    gap=min(mu/factor,k/2);assert gap>F('3.1004e-36')
    # Native matrix controls for the false separate-reaction subtraction.
    controls=[]
    b,r,c=F(-1,4),F(1,2),F(1,2)
    joint=(b*b-2*c*b*r+r*r)/(1-c*c)
    separate_reaction=b*b+r*r
    assert joint==F(7,12) and separate_reaction==F(5,16)
    for scale in [F(1),F(1,10**18)]:
        for s in [F(-1,100),F(0),F(1,100)]:
            q=(joint+s)*scale**2
            true=q-joint*scale**2
            separate=q-separate_reaction*scale**2
            assert true==s*scale**2 and separate>0
            controls.append(dict(scale=str(scale),true_joint_Schur=str(true),invalid_separate_subtraction=str(separate),arithmetic_is_not_joint_lower_bound=True))
    null=[F(1),F(2,3),F(-5,6)]
    matrix=[[joint,b,r],[b,F(1),c],[r,c,F(1)]]
    assert all(sum(a*z for a,z in zip(row,null))==0 for row in matrix)
    # Positive lower block and zero Schur prove PSD; this exact null
    # makes each whole-mass shift's physical ground level exactly v.
    levels=[dict(whole_mass_shift=str(v),exact_physical_ground_level=str(v)) for v in [F(1,1000),F(1,10),F(2)]]
    return dict(milestone='CC74',aperture='53/50',retained_space='span(x_even,w_even,x_odd,w_odd)',retained_dimension=4,
        included_high_space='entire F112',excluded_retained_dimension=108,parity_pieces=pieces,
        original_physical_retained_Schur_gap_lower=str(mu),complete_source_physical_trace_upper=str(source_trace),
        trial_high_lift_physical_trace_upper=str(lift_trace),high_response_operator_square_upper=str(eta2),
        physical_mass_conversion_factor_upper=str(factor),original_Z4_plus_all_F112_physical_gap_lower=str(gap),
        strict_display_physical_gap='3.1004e-36',new_restricted_null_exclusion=True,old_whole_domain_gap_used=False,
        all_remaining_signed_native_couplings_certified=216,remaining_complete_high_source_Gram_certified=False,
        genuine_joint_crossing_controls=controls,positive_whole_mass_levels=levels,
        whole_aperture_positive=False,full_retained_Schur=False,uniform_actual_critical_frame=False,
        full_Weil_nonimplication_claimed=False,RH=False,F4=False,Lean=False)
if __name__=='__main__':
    p=argparse.ArgumentParser()
    for name in ['expanded','old','targets','seed_trial','response','expanded_trial','remaining']:p.add_argument(name)
    p.add_argument('--output',required=True);a=p.parse_args()
    paths=[a.expanded,a.old,a.targets,a.seed_trial,a.response,a.expanded_trial,a.remaining]
    raw=[Path(v).read_bytes() for v in paths];raw[-1]=gzip.decompress(base64.b64decode(raw[-1]))
    hashes=[hashlib.sha256(v).hexdigest() for v in raw]
    expected=['d0625cefe819f3704dec1d75bf0ad0bcd4ea8a3cd6806ebe6d76056733ac321b','069d4acc267a0ac48154427a033cccca96243743dd31e36449f7189de03e895a','6eee61fb4e58ac5be0e95f492f461b289da37ee13aeaa74bbf4acc06f6650c00','814fe0fcc3aff4eecbe4e6c6eead5ce28927043877c0df9cfa03e3a5c71c2336','2110e07c7a7e39d2b454cff364c0863f6f3e3ff151cf72309999130f5e17fe42','7460d5ed3b159d34fa002a56382b40f91cde1d7712fe5e2b1b0ff2b4df7cb65b']
    expected.append('ee5c3ebab7fe2d015ff92145b5c69b72630d90cb6306530e8bd8769469e21557')
    assert hashes==expected
    result=run(*(json.loads(v) for v in raw));result['input_sha256']=hashes
    Path(a.output).write_text(json.dumps(result,indent=2)+'\n')
    print('Z4+ALL F112 physical gap',float(F(result['original_Z4_plus_all_F112_physical_gap_lower'])))
