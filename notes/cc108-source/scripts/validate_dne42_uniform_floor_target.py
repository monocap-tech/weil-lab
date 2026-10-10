#!/usr/bin/env python3
"""Independent exact interval audit of conditional full-packet targets."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json
from certify_dne39_signed_comparison import read
from validate_dne34_source_block import boxes,add,mul,neg,mm,sum_box

def run(paths,output):
    checks=0;rows=[]
    def check(v):
        nonlocal checks
        assert v;checks+=1
    def enclose(a,b):check(a[0]<=b[0]<=b[1]<=a[1])
    def positive(c,M):
        O=boxes(c['original_matrix']);U=[list(map(F,r)) for r in c['exact_congruence_U']];n=len(M)
        check(len(O)==len(U)==n and all(len(r)==n for r in O+U))
        for i in range(n):
            check(U[i][i]!=0)
            for j in range(n):
                check(i<=j or U[i][j]==0);enclose(O[i][j],M[i][j])
        UI=[[(x,x) for x in r] for r in U];K=mm([list(x) for x in zip(*UI)],mm(O,UI));S=boxes(c['congruence_matrix']);m=[]
        for i in range(n):
            for j in range(n):enclose(S[i][j],K[i][j])
            d=S[i][i][0]-sum(max(abs(x),abs(y)) for j,(x,y) in enumerate(S[i]) if j!=i)
            check(d==F(c['Gershgorin_margins'][i]) and d>0);m.append(d)
        d=min(m)/sum(x*x for r in U for x in r);check(d==F(c['coefficient_floor_lower']) and d>0);return d
    for path in paths:
        c,ch=read(path);check(c['stage']=='DNE42' and c['parent']=='bae3aa15f5db9beb87feeddf36c33b6d03f9534a')
        inputs=[read(p) for p in c['input_paths']];check([h for _,h in inputs]==c['input_sha256']);s,prior,a,b=[x for x,_ in inputs]
        check(a['status']==b['status']=='PASS');ar=next(r for r in a['rows'] if r['parity']==c['parity'])
        check(ar['replay_sha256']==inputs[0][1] and ar['comparison_sha256']==inputs[1][1]);br=next(r for r in b['rows'] if r['parity']==c['parity']);check(br['input_sha256'][0]==inputs[0][1] and br['input_sha256'][1]==inputs[1][1])
        check(s['parity']==prior['parity']==c['parity']);N=boxes(s['native_block']);G=boxes(s['original_projected_source_Gram']);check(len(N)==len(G)==c['packet_dimension']==36 and all(len(r)==36 for r in N+G));positive(prior['joint_native_positive_control'],N)
        v=list(map(F,c['exact_trial']));check(v==list(map(F,prior['exact_failure_trial'])) and len(v)==36 and any(v))
        def quadratic(M):return sum_box(mul((x*y,x*y),M[i][j]) for i,x in enumerate(v) for j,y in enumerate(v))
        q=quadratic(N);g=quadratic(G);sq=tuple(map(F,c['trial_native_energy']));sg=tuple(map(F,c['trial_source_energy']));enclose(sq,q);enclose(sg,g);check(sq[0]>0 and sg[0]>0)
        lo=F(c['critical_uniform_floor_lower']);hi=F(c['critical_uniform_floor_upper']);check(lo==sg[0]/sq[1]);check(0<hi-lo==F(c['target_bracket_width'])<=F(1,10**8));check(hi==F((lo*10**8).__ceil__(),10**8))
        H=[[add(mul((hi,hi),x),neg(y)) for x,y in zip(nr,gr)] for nr,gr in zip(N,G)];d=positive(c['full_packet_target_certificate'],H)
        k=F(c['current_original_high_floor']);check(k==F(289,500)==F(prior['original_high_floor']));check(lo-k==F(c['required_increase_lower'])>0);common=F(c['common_sufficient_target']);check(hi<common==F(603,1000))
        mass=sum(map(F,s['exact_masses']));trace=sum(G[i][i][1] for i in range(36));saved=F(c['conditional_source_trace_upper']);check(mass==F(c['conditional_physical_mass']) and mass>0);check(saved>=trace>0)
        gap=min((d/hi)/(4*(mass+saved/hi**2)),hi/2);check(gap==F(c['conditional_all_high_physical_gap_lower']) and gap>0)
        check(c['actual_certified_retained_dimension']==b['all_high_positive_retained_dimension']==69);check(c['uncovered_retained_dimension']==43);check(c['conditional_retained_dimension_if_target_established']==72)
        for key in ('target_high_floor_established','source_integrals_recomputed','true_high_inverse_evaluated','whole_aperture_positive','RH','Lean'):check(c[key] is False)
        rows.append(dict(parity=c['parity'],certificate_sha256=ch,input_sha256=c['input_sha256'],critical_uniform_floor_lower=str(lo),critical_uniform_floor_upper=str(hi),bracket_width=str(hi-lo),full_packet_target_positive=True,conditional_all_high_physical_gap_lower=str(gap)))
    check({r['parity'] for r in rows}=={'even','odd'})
    out=dict(stage='DNE42',status='PASS',exact_rational_checks=checks,rows=rows,common_sufficient_target='603/1000',target_high_floor_established=False,current_original_high_floor='289/500',actual_certified_retained_dimension=69,uncovered_retained_dimension=43,conditional_retained_dimension_if_target_established=72,source_integrals_recomputed=False,true_high_inverse_evaluated=False,whole_aperture_positive=False,RH=False,Lean=False)
    Path(output).write_text(json.dumps(out,indent=2)+'\n');print('PASS',checks,'checks; conditional target .603; actual retained rank 69',flush=True)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('inputs',nargs=2);p.add_argument('--output',required=True);a=p.parse_args();run(a.inputs,a.output)
