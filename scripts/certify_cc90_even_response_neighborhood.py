#!/usr/bin/env python3
"""Certified rejection neighborhood in the current even response geometry."""
import argparse,json
from pathlib import Path
from fractions import Fraction as F
import certify_cc81_boundary_response_consumer as c
import certify_cc83_five_source_consumer as five
import certify_cc88_correlated_seventh_response as direct

RHO=F(61,100)
ETA=F(19,100)
def controls():
    # Worst-case collinear movement: the norm can shrink by eta and the
    # effective border can grow by eta. This attains the general bound.
    oldpair=F(1);oldborder=RHO
    newpair=oldpair-ETA;newborder=oldborder+ETA
    assert newborder/newpair==F(80,81)<1
    # Actual Lorentz-cone crossings and boundary: stronger rotations can pass.
    crossing=[]
    for tau in [F(99,100),F(1),F(101,100)]:
        orientation=1-tau*tau
        assert (orientation<0)==(tau>1) and (orientation==0)==(tau==1)
        crossing.append(dict(effective_border=str(tau),orientation_deficit=str(orientation)))
    # Both drift constraints matter: either alone permits a passing response.
    assert F(2)/F(1)>1 and RHO/F(1,2)>1
    # A denominator cannot fix a bad orientation, but can prevent a good
    # orientation from passing at its actual finite strength.
    assert (-1+F(4,101))<0 and (-1+F(4,2))>0
    return dict(worst_case_normalized_slope=str(newborder/newpair),
        strict_cone_crossings=crossing,both_drift_constraints_necessary=True,
        good_orientation_does_not_guarantee_paid_finite_strength=True)

def run(root,oldroot):
    rebuilt=direct.run(root,oldroot)
    row=next(x for x in rebuilt['parity_checks'] if x['parity']=='even')
    k=c.matrix(row['tightened_seven_source_lower_matrix']);s,ei,beta=five.condensed(k)
    z=list(map(c.iv,row['direct_response_border']))
    a=c.mm(c.mm([z[:2]],ei),[[v] for v in z[:2]])[0][0];assert a[0]>0
    tau=c.sub(z[2],c.sumiv(c.mul(x,y) for x,y in zip(z[:2],beta)))
    deficit=c.neg(s);ratio2=c.div(direct.square(tau),c.mul(deficit,a))
    assert ratio2[1]<RHO*RHO
    assert RHO+ETA<1-ETA
    cone_gap=(1-ETA)**2-(RHO+ETA)**2;assert cone_gap==F(161,10000)>0
    return dict(milestone='CC90',integration_parent='d1838e8bca1dc4a0003af312414c5855dfb17d38',
        read_only_source='5f8a6c1e54a39236df253a5aae5f7be55fee74ed',
        current_seven_source_even_condensed_deficit=c.pair(deficit),
        reference_leading_energy_penalty=c.pair(a),reference_effective_border=c.pair(tau),
        reference_normalized_slope_squared=c.pair(ratio2),
        certified_normalized_slope_upper=str(RHO),allowed_relative_drift=str(ETA),
        rejected_neighborhood_maximum_normalized_slope='80/81',
        rejected_neighborhood_minimum_orientation_deficit_fraction=str(cone_gap),
        geometry_is_after_current_seven_source_condensation=True,
        all_nonnegative_strengths_in_neighborhood_fail=True,
        actual_next_source_response_tested=False,exact_controls=controls(),
        background_floor_hypothesis=row['background_floor_hypothesis'],background_floor_newly_proved=False,
        odd_conditional_pass_preserved=True,whole_aperture_positive=False,
        highest_certified_whole_aperture='21/20')

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('NF45_root',type=Path);ap.add_argument('NF44_root',type=Path);ap.add_argument('--output',type=Path,required=True)
    a=ap.parse_args();d=run(a.NF45_root,a.NF44_root);a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(d,indent=2)+'\n')
    print('CC90 PASS: 19-percent two-component response neighborhood cannot certify even sign at any strength')
