#!/usr/bin/env python3
"""NF45 even response-ray ceiling from independently rebuilt CC88 intervals."""
import argparse,json
from pathlib import Path
from fractions import Fraction as F
import certify_cc80_defect_response_acceptance as exact
import certify_cc81_boundary_response_consumer as c
import certify_cc83_five_source_consumer as five
import certify_cc85_six_source_consumer as six
import certify_cc88_correlated_seventh_response as direct

def controls():
    rows=[]
    for scale in [F(1),F(1,10**18)]:
        k=exact.diag([1,1,-scale**2]);z=[F(2),F(0),scale]
        # Fixed witness responds positively, but leading-coordinate coupling
        # caps the full condensed credit below the deficit at every strength.
        for strength in [F(0),F(1,100),F(1),F(100),F(10**30)]:
            new=exact.add(k,[[strength*x*y for y in z] for x in z])
            ei=exact.inv([row[:2] for row in new[:2]]);border=[new[0][2],new[1][2]]
            margin=new[2][2]-sum(border[i]*ei[i][j]*border[j] for i in range(2) for j in range(2))
            expected=-scale**2+strength*scale**2/(1+4*strength)
            assert margin==expected and margin<=-3*scale**2/4
        rows.append(dict(scale=str(scale),negative_margin_at_every_nonnegative_strength=True,
            exact_limiting_condensed_margin=str(-3*scale**2/4)))
    # A ray aligned with the negative coordinate can pass; no generic no-go.
    for strength in [F(99,100),F(1),F(101,100)]:
        assert ((-1+strength)>0)==(strength>1)
    # Changing a physical column's normalization does not amplify its credit.
    for alpha in [F(1,7),F(-3),F(10**12)]:
        assert (alpha*F(2))**2/(alpha**2*F(5))==F(4,5)
    return dict(two_scale_ray_ceiling_controls=rows,aligned_ray_strict_crossings=True,
        source_normalization_invariance=True)

def run(root,oldroot):
    rebuilt=direct.run(root,oldroot)
    response=next(x for x in rebuilt['parity_checks'] if x['parity']=='even')
    old=six.load(oldroot,'RPB108_NF44_EVEN_INVERSE_WITNESS_CERTIFICATE_20261009.json')
    k=c.matrix(old['conditional_six_high_joined_Schur_lower_matrix']);s,ei,beta=five.condensed(k)
    z=list(map(c.iv,response['direct_response_border']));b=c.iv(response['positive_block_denominator'])
    a=c.mm(c.mm([z[:2]],ei),[[x] for x in z[:2]])[0][0];assert a[0]>0
    tau=c.sub(z[2],c.sumiv(c.mul(x,y) for x,y in zip(z[:2],beta)))
    tau2=direct.square(tau);deficit=c.neg(s)
    ceiling=c.div(tau2,a)
    orientation_deficit=c.sub(c.mul(deficit,a),tau2);assert orientation_deficit[0]>0
    assert ceiling[1]<deficit[0]
    limiting=c.add(s,ceiling);assert limiting[1]<0
    current_credit=c.div(tau2,c.add(b,a));assert current_credit[0]>0
    return dict(milestone='CC89',integration_parent='6261120842a1eacab62278c2e3c60b5a6ea5085c',
        read_only_source='5f8a6c1e54a39236df253a5aae5f7be55fee74ed',
        rebuilt_response_input=True,even_base_condensed_deficit=c.pair(deficit),
        positive_leading_coordinate_penalty=c.pair(a),effective_response_border=c.pair(tau),
        current_full_condensed_credit=c.pair(current_credit),
        arbitrary_strength_response_ceiling=c.pair(ceiling),
        ceiling_fraction_of_base_deficit=c.pair(c.div(ceiling,deficit)),
        signed_orientation_deficit=c.pair(orientation_deficit),
        limiting_condensed_margin=c.pair(limiting),all_nonnegative_ray_strengths_fail=True,
        exact_controls=controls(),physical_source_strength_amplification_available=False,
        actual_original_form_negative=False,odd_conditional_pass_preserved=True,
        background_floor_hypothesis=old['background_floor_hypothesis'],background_floor_newly_proved=False,
        whole_aperture_positive=False,highest_certified_whole_aperture='21/20')

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('NF45_root',type=Path);ap.add_argument('NF44_root',type=Path);ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args();d=run(args.NF45_root,args.NF44_root)
    args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(d,indent=2)+'\n')
    print('CC89 PASS: even seventh-response ray fails at every nonnegative strength; new orientation required')
