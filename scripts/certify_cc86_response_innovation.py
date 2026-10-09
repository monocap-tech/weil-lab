#!/usr/bin/env python3
"""Exact response innovation controls; authenticated NF44 deficit attachment."""
import argparse, itertools, json
from pathlib import Path
from fractions import Fraction as F
import certify_cc80_defect_response_acceptance as m
import certify_cc81_boundary_response_consumer as c
import certify_cc83_five_source_consumer as five
import certify_cc84_source_span_compression as span
import certify_cc85_six_source_consumer as six

def score(metric,t,indices):
    if not indices: return F(0)
    a=[[metric[i][j] for j in indices] for i in indices]
    return span.q(m.inv(a),[t[i] for i in indices])

def innovation(metric,t,selected,j):
    if not selected: return t[j]**2/metric[j][j]
    a=[[metric[i][k] for k in selected] for i in selected]
    ai=m.inv(a); border=[metric[i][j] for i in selected]
    ts=[t[i] for i in selected]
    denominator=metric[j][j]-span.q(ai,border)
    numerator=t[j]-span.dot(border,[span.dot(row,ts) for row in ai])
    assert denominator>0
    return numerator**2/denominator

def controls():
    metric=m.mat([[2,1,F(1,3)],[1,2,F(1,5)],[F(1,3),F(1,5),3]])
    t=list(map(F,[1,0,2]));assert all(x>0 for x in m.pivots(metric))
    total=score(metric,t,[0,1,2])
    traces=[]
    for order in itertools.permutations(range(3)):
        selected=[];running=F(0);increments=[]
        for j in order:
            inc=innovation(metric,t,selected,j);increments.append(str(inc))
            running+=inc;selected.append(j)
            assert running==score(metric,t,selected)
        assert running==total
        traces.append(dict(order=list(order),increments=increments,total=str(total)))
    # A physically orthogonal candidate can have zero raw border response,
    # while signed denominator correlations make its conditional credit positive.
    assert t[1]==0 and innovation(metric,t,[0],1)==F(1,6)
    assert score(metric,t,[0,1])==F(2,3)
    assert sum(t[i]**2/metric[i][i] for i in [0,1])==F(1,2)
    # A finite shell can exhaust without passing; equality is not strict sign.
    shell_scores=[score(metric,t,list(range(n))) for n in [1,2,3]]
    assert all(v<=total for v in shell_scores)
    crossings=[dict(deficit=str(d),passes=total>d) for d in [total-F(1,100),total,total+F(1,100)]]
    assert [x['passes'] for x in crossings]==[True,False,False]
    # Arbitrarily delayed response: no universal column count follows from
    # a finite initial sequence of failed candidates.
    for delay in [1,4,12]:
        a=m.diag([1]*(delay+1));v=[F(0)]*delay+[F(2)]
        assert score(a,v,list(range(delay)))==0
        assert score(a,v,list(range(delay+1)))==4
    return dict(permutation_traces=traces,zero_raw_response_positive_innovation=True,
        signed_correlations_change_credit=True,strict_crossings=crossings,
        arbitrary_delay_controls=[1,4,12],native_source_replayed=False)

def run(root):
    rows=[]
    for parity in ['even','odd']:
        d=six.load(root,'RPB108_NF44_'+parity.upper()+'_INVERSE_WITNESS_CERTIFICATE_20261009.json')
        k=c.matrix(d['conditional_six_high_joined_Schur_lower_matrix'])
        s,_,_=five.condensed(k);assert s[1]<0 and c.det3(k)[1]<0
        rows.append(dict(parity=parity,starting_condensed_deficit=c.pair(c.neg(s)),
            background_floor_hypothesis=d['background_floor_hypothesis']))
    return dict(milestone='CC86',integration_parent='e00358705a56882ae3d223139da822969ecced33',
        read_only_source='7bd6fbda5e156fbd009b6de0aeee6f41b1823c5c',
        parity_checks=rows,exact_controls=controls(),actual_candidate_span_available=False,
        shell_exhaustion_certified=False,new_source_column_certified=False,
        simultaneous_six_direction_certificate=False,whole_aperture_positive=False,
        background_floor_newly_proved=False)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('NF44_root',type=Path);ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args();data=run(args.NF44_root)
    args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(data,indent=2)+'\n')
    print('CC86 PASS: exact innovation, order independence, strict exhaustion controls; NF44 deficits authenticated')
