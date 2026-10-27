#!/usr/bin/env python3
"""Coupled four-mode ORIGINAL min-max lower bound; no global BS upper."""
import argparse,hashlib,json,time
from fractions import Fraction as F
from pathlib import Path
import flint
from verify_rpb108_original_critical_block_physical import physical_form
PRIOR_SHA='2cd494b1558c43790f683d21926e1d1a83cc68a4edfdebd0d6074ac968f85919'
KSTAR=F(33621,10**9)
def main():
    p=argparse.ArgumentParser();p.add_argument('--prior',required=True);p.add_argument('--candidates',required=True);p.add_argument('--output',default='artifacts/original_four_mode_critical_block.json');args=p.parse_args();start=time.monotonic()
    raw=Path(args.prior).read_bytes();assert hashlib.sha256(raw).hexdigest()==PRIOR_SHA;prior=json.loads(raw)
    cr=Path(args.candidates).read_bytes();spec=json.loads(cr);assert len(spec['probes'])==4 and spec['coefficient_denominator']==10**12
    assert spec['sine_frequencies']==prior['exact_probe']['sine_frequencies']==[str(F(5*n,11)) for n in range(1,33)]
    assert spec['probes'][0]['sine_coefficients']==prior['exact_probe']['sine_coefficients'] and spec['probes'][0]['sinh_coefficient']==prior['exact_probe']['sinh_coefficient']
    probes=[list(map(F,v['sine_coefficients']))+[F(v['sinh_coefficient'])] for v in spec['probes']]
    assert all(len(v)==33 and all((x*10**12).denominator==1 for x in v) for v in probes)
    assert flint.__version__=='0.8.0'
    witnesses=[];diag=[]
    def run(v,label):
        z=physical_form(v[:-1],v[-1]);z['label']=label;witnesses.append(z)
        assert time.monotonic()-start<90,'bounded 90-second four-mode scalar guard'
        return tuple(map(F,z['physical_norm_interval'])),tuple(map(F,z['signed_energy_interval']))
    for i,v in enumerate(probes):diag.append(run(v,[i,i]))
    assert list(map(str,diag[0][1]))==prior['signed_energy_interval']
    G=[[None]*4 for _ in range(4)];Q=[[None]*4 for _ in range(4)]
    for i in range(4):G[i][i],Q[i][i]=diag[i]
    for i in range(4):
        for j in range(i+1,4):
            n,q=run([a+b for a,b in zip(probes[i],probes[j])],[i,j])
            G[i][j]=G[j][i]=((n[0]-diag[i][0][1]-diag[j][0][1])/2,(n[1]-diag[i][0][0]-diag[j][0][0])/2)
            Q[i][j]=Q[j][i]=((q[0]-diag[i][1][1]-diag[j][1][1])/2,(q[1]-diag[i][1][0]-diag[j][1][0])/2)
    absup=lambda v:max(abs(v[0]),abs(v[1]))
    gram_error=max(sum(absup((G[i][j][0]-(i==j),G[i][j][1]-(i==j))) for j in range(4)) for i in range(4))
    assert gram_error<F(1,100);gfloor=F(99,100)
    qrows=[sum((absup(v) for v in row),F(0)) for row in Q];qbound=max(qrows)
    eta=qbound/(KSTAR*gfloor);assert eta<F(3,10**12)
    # All mixed entries are paid; no positivity of Q outside this subspace,
    # no exact spectral multiplicity, and no inverse norm upper is inferred.
    enc=lambda mat:[[[str(v) for v in interval] for interval in row] for row in mat]
    out=dict(status='CONDITIONAL_ORIGINAL_FOUR_NEAR_CRITICAL_BS_MODES',prior_native_sha256=PRIOR_SHA,candidates_sha256=hashlib.sha256(cr).hexdigest(),exact_candidates=spec,
      working_precision_bits=512,flint_version=flint.__version__,complete_scalar_witnesses=witnesses,scalar_evaluations=len(witnesses),
      physical_Gram_intervals=enc(G),complete_signed_Gram_intervals=enc(Q),physical_Gram_identity_error_upper=str(gram_error),physical_Gram_lower=str(gfloor),
      signed_Gram_absolute_row_uppers=list(map(str,qrows)),signed_Gram_operator_absolute_upper=str(qbound),inherited_Astar_floor=str(KSTAR),
      fourth_BS_eigenvalue_lower=str(1-eta),fourth_BS_distance_from_one_upper=str(eta),near_critical_dimension_lower=4,
      arbitrary_orthogonal_deflation_rank_up_to=3,deflated_BS_norm_lower=str(1-eta),
      exact_near_critical_multiplicity_certified=False,complement_spectral_floor_certified=False,full_signed_positivity_certified=False,
      global_true_BS_norm_upper_certified=False,original_J470_membership_claimed=False,W_ODD_NEG='OPEN',original_domain_review='OPEN',elapsed_seconds=time.monotonic()-start)
    path=Path(args.output);path.parent.mkdir(exist_ok=True,parents=True);path.write_text(json.dumps(out,separators=(',',':'))+'\n')
    print('FOUR-MODE ORIGINAL BS MIN-MAX PASS: all SIX mixed entries; lambda4 >1-3e-12; every rank<=3 deflated norm >1-3e-12; whole signed gate OPEN; seconds',round(out['elapsed_seconds'],2))
    print('Actual eta upper',float(eta),'signed block norm upper',float(qbound))
if __name__=='__main__':main()
