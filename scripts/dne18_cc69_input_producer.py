#!/usr/bin/env python3
"""Consume NF26 exact moments; test norm-only assembly with CC62.

No floating value participates in a proof comparison.
"""
import argparse, hashlib, json
from fractions import Fraction as F
from math import isqrt
from pathlib import Path

def sqrt_bounds(x):
    scale=10**250
    n=isqrt(x.numerator*scale*scale//x.denominator)
    assert F(n,scale)**2<=x<F(n+1,scale)**2
    return F(n,scale),F(n+1,scale)

def run(native,targets,low):
    k=F(207,1000); rows=[]
    # NF26's regular-kernel and pole remainder, independently reconstructed.
    from math import factorial
    a=F(53,50)
    eta=2*a*4*F(106,125)**320/(1-F(106,125))+8*(a/2)**41/F(factorial(41))
    for n,t,l in zip(native['parity_certificates'],targets['authenticated_compensated_targets'],low['native_parity_gates']):
        assert n['parity']==t['parity']==l['parity']
        qlo,qhi=map(F,n['corrected_native_energy'])
        plo,phi=map(F,n['complete_original_corrected_residual_square'])
        delta=qlo-phi/k
        assert delta>0 and n['directional_sufficient_gate_passed']
        alo,ahi=map(F,l['native_Q_diagonal']); elo,ehi=map(F,l['full_F112_source_square'])
        lowdelta=alo-ehi/k; assert lowdelta>0
        # First retained coordinate is e0 (even) or e1 (odd).
        pl,pu=map(F,t['low_source_coordinates'][0])
        yl,yu=map(F,n['retained_approximant_Ly_coordinates'][0])
        paid=F(n['correction_norm_upper'])*eta
        blo,bhi=pl-yu-paid,pu-yl+paid
        direct=max(abs(blo),abs(bhi))
        rootlo,rootup=sqrt_bounds(ehi*phi)
        mixed=direct+rootup/k
        budget=lowdelta*delta
        assert mixed*mixed>budget
        # Even without the direct term, this estimator cannot assemble.
        assert rootlo*rootlo/(k*k)>budget
        rows.append(dict(parity=n['parity'],seed_Schur_lower=str(delta),low_mode_Schur_lower=str(lowdelta),
            original_direct_mixed_pairing=[str(blo),str(bhi)],norm_only_mixed_absolute_upper=str(mixed),
            determinant_budget=str(budget),norm_only_assembly_gate_passed=False,
            inverse_norm_term_alone_exceeds_budget=True,
            sufficient_signed_inverse_correlation_condition='enclose B=Q(e_j,v)-<r_ej,C^-1 r_v> with |B|^2 < low_lower*seed_lower'))
    controls=[]
    # Genuine crossing at determinant zero while both diagonals stay positive.
    for b in [F(99,100),F(1),F(101,100)]:
        det=1-b*b; ground=1-b
        assert (det>0)==(ground>0) and (det<0)==(ground<0)
        controls.append(dict(mixed=str(b),determinant=str(det),ground_level=str(ground)))
    levels=[]
    for level in [F(1,1000),F(1,10),F(2)]:
        diag=1+level; b=F(1)
        assert diag-b==level and diag*diag-b*b>0
        levels.append(dict(whole_mass_shift=str(level),ground_level=str(diag-b)))
    return dict(milestone='CC69',aperture='53/50',native_seed_span_Schur_positive=True,
        seed_span_dimension=2,parity_rows=rows,genuine_mixed_crossing_controls=controls,
        positive_whole_mass_levels=levels,union_with_low_two_certified=False,
        whole_aperture_positive=False,uniform_defect_relative_frame=False,
        full_Weil_nonimplication_claimed=False,RH=False,F4=False,Lean=False)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('native');p.add_argument('targets');p.add_argument('low');p.add_argument('--output',required=True);args=p.parse_args()
    paths=[args.native,args.targets,args.low]
    raw=[Path(v).read_bytes() for v in paths]
    result=run(*(json.loads(v) for v in raw))
    result['input_sha256']=[hashlib.sha256(v).hexdigest() for v in raw]
    Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
    for row in result['parity_rows']:
        print(row['parity'],'seed lower',float(F(row['seed_Schur_lower'])),'mixed bound',float(F(row['norm_only_mixed_absolute_upper'])),'allowed',float(F(row['determinant_budget']))**.5)
