#!/usr/bin/env python3
"""Actual prime-5 translation panels after the log(6)/2 ordering change."""
import argparse
import json
from certify_native_legendre_small_window import F, I
from certify_native_exact_logarithm import log_rational


def geometry(a):
    shifts = {n:log_rational(F(n),220)/(2*a) for n in (2,3,4,5)}
    assert log_rational(F(5),220).hi < 2*a < log_rational(F(7),220).lo
    cuts = [('0',I(0)),('1',I(1))]
    for n,shift in shifts.items():
        cuts += [('ell_'+str(n),shift),('1-ell_'+str(n),I(1)-shift)]
    cuts.sort(key=lambda item:item[1].lo)
    assert all(x[1].hi < y[1].lo for x,y in zip(cuts,cuts[1:]))
    rows = []
    for left,right in zip(cuts,cuts[1:]):
        t = (left[1].hi+right[1].lo)/2
        active = []
        for sign in (1,-1):
            for n,shift in shifts.items():
                image = I(t)+sign*shift
                if 0 < image.lo and image.hi < 1:
                    active.append(('+' if sign == 1 else '-')+str(n))
                else:
                    assert image.hi < 0 or image.lo > 1
        rows.append({'left':left[0],'right':right[0],
                     'interior_test_point':str(t),'active_translations':active})
    return {'aperture':str(a),'ordered_cuts':[name for name,_ in cuts],
            'cut_enclosures':{name:[str(x.lo),str(x.hi)] for name,x in cuts},
            'panels':rows}


def certificate():
    I.grid = 10**80
    before = [geometry(a) for a in (F(81,100),F(41,50),F(89,100))]
    after = [geometry(a) for a in (F(9,10),F(19,20))]
    old_order = ['0','1-ell_5','1-ell_4','1-ell_3','ell_2',
                 '1-ell_2','ell_3','ell_4','ell_5','1']
    new_order = ['0','1-ell_5','1-ell_4','ell_2','1-ell_3',
                 'ell_3','1-ell_2','ell_4','ell_5','1']
    assert all(g['ordered_cuts'] == old_order for g in before)
    assert all(g['ordered_cuts'] == new_order for g in after)
    changed = after[-1]
    assert changed['panels'][3]['active_translations'] == ['+2','+3','-2']
    assert changed['panels'][5]['active_translations'] == ['+2','-2','-3']
    assert changed['panels'][3]['active_translations'] != before[0]['panels'][3]['active_translations']
    crossing = log_rational(F(6),220)/2
    assert F(89,100) < crossing.lo < crossing.hi < F(9,10)
    return {'status':'certified actual nine-panel reordering; no source approximation',
            'ordering_crossing':'log(6)/2','crossing_enclosure':[str(crossing.lo),str(crossing.hi)],
            'prime_terms':[2,3,4,5],'prime4_amplitude':'log(2)/2',
            'prime5_amplitude':'log(5)/sqrt(5)','before_crossing':before,
            'after_crossing':after,'old_panel_reuse_control_rejected':True,
            'whole_domain_positivity_frontier':'81/100',
            'new_native_matrix_certified':False,'new_source_approximation_certified':False,
            'new_residual_gram_certified':False,'f4_entry_closed':False,
            'full_transport_closed':False,'lean_formalized':False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',required=True)
    args = parser.parse_args()
    from pathlib import Path
    Path(args.output).write_text(json.dumps(certificate(),indent=2)+'\n')
