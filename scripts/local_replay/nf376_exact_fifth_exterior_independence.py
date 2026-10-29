#!/usr/bin/env python3
"""NF376 exact source-inventory lemma: a fifth original sine defines a new QJ exterior orientation.

No native Gram or signed lowband integral. Uses uniqueness of exponential polynomials.
"""
import argparse,hashlib,json
from fractions import Fraction as F
from pathlib import Path
RANK_SHA='9b9820a0163e5e8bf08dd1c2525c757ff67214b49a40cb093d00bc611c9ff9e2'
SOURCE_SHA='abd37707d585dcd54b040f1ae865a7430a9c7cba85df31131661b2e72e560770'
def main():
    p=argparse.ArgumentParser();p.add_argument('--rank',required=True);p.add_argument('--source',required=True);p.add_argument('--report',required=True);a=p.parse_args()
    b=Path(a.rank).read_bytes();c=Path(a.source).read_bytes()
    assert hashlib.sha256(b).hexdigest()==RANK_SHA
    assert hashlib.sha256(c).hexdigest()==SOURCE_SHA
    rank=json.loads(b);probes=json.loads(c)['data']
    nodes=rank['original_nodes'];counts=rank['selected_multiplicities']
    assert len(nodes)==107 and len(nodes)==len(counts)
    selected=[]
    for (center,degree),keep in zip(nodes,counts):
        assert 0<=keep<=degree
        selected.extend([F(center)]*keep)
    assert len(selected)==241 and rank['retained_original_pole']
    critical=[F(s) for s in probes['target_sine_frequencies']]
    assert len(critical)==32 and critical==[F(5*n,11) for n in range(1,33)]
    assert len(probes['target_probes'])==4
    for x in probes['target_probes']:
        assert len(x['sine_coefficients'])==32
    new=F(15)
    assert new==F(5*33,11)
    assert new not in set(selected)
    assert new not in set(critical)
    # Entire finite exponential polynomials x^k exp(2pi i c x) for
    # distinct c, and exp(+-x/2), are linearly independent on an interval.
    # Thus the e^(+2pi i*15*x) coefficient in the new sine cannot be
    # synthesized by any selected original J generator or any F4 probe.
    # If Q f5 belonged to span(Q F4), f5 would lie in J+span(F4), contradiction.
    result=dict(status='EXACT_SOURCE_FREQUENCY_CERTIFIED_NEW_EXTERIOR_ORIENTATION',
      rank_original_sha256=RANK_SHA,pr355_portable_source_sha256=SOURCE_SHA,
      physical_interval='[-11/10,11/10]',selected_original_total=242,
      selected_trigonometric_generator_count=len(selected),selected_pole_count=1,
      original_critical_probe_count=4,original_critical_sine_harmonics=32,
      diagnostic_frequency='15',diagnostic_original_harmonic=33,
      frequency_distinct_from_all_selected_J_and_original_F4=True,
      proof_lemma='Uniqueness of finite exponential polynomials with distinct complex exponents on an open interval; a.e. equality of analytic source functions implies identity',
      consequence='Q sin(2pi 15x) not in span(Q F1,Q F2,Q F3,Q F4)',
      actual_physical_quotient_norm_value_computed=False,
      actual_signed_lowband_integral_computed=False,
      actual_lowband_H_i_norm_computed=False,
      W_ODD_NEG='OPEN',RH='OPEN')
    Path(a.report).parent.mkdir(parents=True,exist_ok=True)
    Path(a.report).write_text(json.dumps(result,indent=2)+'\n')
    print('PASS exact original source-inventory independence: new q5 outside fitted exterior E4; lowband norm OPEN')
if __name__=='__main__':main()
