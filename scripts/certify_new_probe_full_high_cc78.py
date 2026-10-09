#!/usr/bin/env python3
"""Original physical gap for the two opposite-parity expanded probes + F."""
import argparse,hashlib,json
from pathlib import Path
from fractions import Fraction as F

def run(oldtrial,trials,certs):
    k=F(207,1000);rows=[];eta2=F(0);xi2=F(0)
    for old,tr,c in zip(oldtrial['parities'],trials,certs):
        assert old['parity']==tr['parity']==c['parity']
        v=list(map(F,old['fixed_probe_coefficients']));z=list(map(F,tr['fixed_rational_additional_coefficients']))
        mass=sum(t*t for t in v[:56]);high=sum(t*t for t in v[56:])+sum(t*t for t in z)
        assert mass>0 and mass+high==F(c['exact_lifted_witness_mass'])
        assert set(old['high_indices']).isdisjoint(tr['additional_high_indices'])
        score=F(c['floor_score'][0]);gamma=F(c['original_complete_projected_source_square'][1])
        assert c['status']=='LIFTED_WITNESS_WITH_ALL_F_PASSES' and score>0 and gamma>0
        mu=score/mass;eta2+=gamma/(k*k*mass);xi2+=high/mass
        rows.append(dict(parity=c['parity'],exact_retained_mass=str(mass),exact_high_lift_mass=str(high),
            retained_directional_Schur_physical_gap_lower=str(mu),
            expanded_finite_frame_physical_gap_lower=c['physical_expanded_shared_frame_gap_lower']))
    # Exact parity diagonalizes retained mass, source and the high operator.
    mu=min(F(p['retained_directional_Schur_physical_gap_lower']) for p in rows)
    factor=1+4*eta2+4*xi2
    gap=min(mu/factor,k/2);assert gap>F('1.6476e-22')
    return dict(milestone='CC78',aperture='53/50',retained_space='span(u32_even,u32_odd)',
        retained_dimension=2,included_high_space='entire original F112',parity_certificates=rows,
        complete_high_response_norm_square_upper=str(eta2),fixed_high_lift_norm_square_upper=str(xi2),
        physical_mass_conversion_factor_upper=str(factor),
        original_two_probe_plus_all_high_physical_gap_lower=str(gap),strict_display_gap='1.6476e-22',
        new_original_restricted_null_exclusion=True,old_whole_domain_gap_used=False,
        simultaneous_six_retained_direction_certificate=False,complete_remaining_source_Gram_certified=False,
        whole_aperture_positive=False,uniform_defect_relative_critical_frame=False,
        full_Weil_nonimplication_claimed=False)

if __name__=='__main__':
    a=argparse.ArgumentParser()
    for name in ['oldtrial','even_trial','odd_trial','even_cert','odd_cert']:a.add_argument(name)
    a.add_argument('--output',required=True);a=a.parse_args()
    raw=[Path(getattr(a,name)).read_bytes() for name in ['oldtrial','even_trial','odd_trial','even_cert','odd_cert']]
    hashes=[hashlib.sha256(v).hexdigest() for v in raw]
    assert hashes==['89683af32013c4bfc3ed3bd66d90ff889131a4ccdd03dd769523a7dfbbcd9cff',
        '4fa44e021ffd3b408703911c2b4d222c30bde1ac70581eafae81d5d3fbc589a2',
        '5080c348c39f870fe554609ded27748326078f6bd944794ec5f80862e6aaa73c',
        '7327c2f3d89327ed1cef95404646c059c3ded4d4881486b1b3beb15651337d4f',
        '17ae9ec6757cd29443fc77af28b86fb3d4b7f9449317886c5aec75bf92a9fb89']
    d=list(map(json.loads,raw));r=run(d[0],d[1:3],d[3:]);r['input_sha256']=hashes
    Path(a.output).write_text(json.dumps(r,indent=2)+'\n')
    print('original two probes + entire high physical gap',float(F(r['original_two_probe_plus_all_high_physical_gap_lower'])))
