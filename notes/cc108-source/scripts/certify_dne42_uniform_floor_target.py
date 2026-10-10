#!/usr/bin/env python3
"""Enclose the full-packet uniform-floor threshold; no new high-floor claim."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json
from certify_dne39_signed_comparison import read,matrix,quadratic,positive
from certify_dne32_native_remainder import I

PARENT='bae3aa15f5db9beb87feeddf36c33b6d03f9534a'
def run(parity,output):
    up=parity.upper()
    paths=[f'notes/data/RPB108_DNE40_{up}_JOINT_SOURCE_REPLAY_20261010.json.gz.b64',f'notes/data/RPB108_DNE40_{up}_SIGNED_COMPARISON_20261010.json','notes/data/RPB108_DNE40_SIGNED_SOURCE_VALIDATION_20261010.json','notes/data/RPB108_DNE41_POSITIVE_SUBSPACE_VALIDATION_20261010.json']
    inputs=[read(p) for p in paths];s,c,a,b=[x for x,_ in inputs]
    assert a['status']==b['status']=='PASS'
    row=next(r for r in a['rows'] if r['parity']==parity)
    assert row['replay_sha256']==inputs[0][1] and row['comparison_sha256']==inputs[1][1]
    N=matrix(s['native_block']);G=matrix(s['original_projected_source_Gram'])
    v=list(map(F,c['exact_failure_trial']));q=quadratic(N,v);g=quadratic(G,v)
    assert q.l>0 and g.l>0
    lower=g.l/q.h;grid=10**8;upper=F((lower*grid).__ceil__(),grid)
    H=[[I(upper)*x-y for x,y in zip(nr,gr)] for nr,gr in zip(N,G)]
    cert=positive(H);assert cert is not None
    assert 0<upper-lower<=F(1,grid)
    common=F(603,1000);assert upper<common
    mass=sum(map(F,s['exact_masses']));trace=sum(x[i].h for i,x in enumerate(G));d=F(cert['coefficient_floor_lower'])
    gap=min((d/upper)/(4*(mass+trace/upper**2)),upper/2);assert gap>0
    out=dict(stage='DNE42',parent=PARENT,parity=parity,input_paths=paths,input_sha256=[h for _,h in inputs],packet_dimension=36,exact_trial=list(map(str,v)),trial_native_energy=q.box(),trial_source_energy=g.box(),critical_uniform_floor_lower=str(lower),critical_uniform_floor_upper=str(upper),target_bracket_width=str(upper-lower),full_packet_target_certificate=cert,current_original_high_floor='289/500',required_increase_lower=str(lower-F(289,500)),common_sufficient_target=str(common),conditional_physical_mass=str(mass),conditional_source_trace_upper=str(trace),conditional_all_high_physical_gap_lower=str(gap),target_high_floor_established=False,actual_certified_retained_dimension=69,uncovered_retained_dimension=43,conditional_retained_dimension_if_target_established=72,source_integrals_recomputed=False,true_high_inverse_evaluated=False,whole_aperture_positive=False,RH=False,Lean=False)
    Path(output).write_text(json.dumps(out,indent=2)+'\n')
    print(parity,'target',float(lower),float(upper),'conditional gap',float(gap),flush=True)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('parity',choices=['even','odd']);p.add_argument('--output',required=True);a=p.parse_args();run(a.parity,a.output)
