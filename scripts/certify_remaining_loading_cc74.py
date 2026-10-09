#!/usr/bin/env python3
"""Original remaining-background witness against unchanged scalar floor."""
import argparse,base64,gzip,json,hashlib
from pathlib import Path
from fractions import Fraction as F
import certify_native_remaining_background_nf31_106 as p

def run(cert):
    data,source,_=p.inputs();targets,_,responses,*_=data;rows=[]
    for row,wc,native in zip(targets['authenticated_compensated_targets'],responses['parity_certificates'],cert['parity_certificates']):
        ids=row['retained_indices'];x=list(map(F,row['retained_coefficients']));w=list(map(F,wc['exact_rational_retained_response']))
        T,pivot,q,free=p.complement(x,w)
        assert [pivot,q]==native['retained_constraint_pivots'] and free==native['free_retained_coordinates']
        def Q(i,j):return p.I(*map(F,source[f'{min(i,j)},{max(i,j)}']['full']))
        A=[[Q(i,j) for j in ids] for i in ids]
        AT0=[[p.dot(a,col) for col in zip(*T)] for a in A]
        AT=[[p.dot(col,v) for v in zip(*AT0)] for col in zip(*T)]
        inv,proof=p.matrix.inverse(AT);assert proof==native['remaining_inverse_verification']
        h=112 if row['parity']=='even' else 113
        g=[Q(i,h) for i in ids];gt=[p.dot(col,g) for col in zip(*T)]
        reaction=p.dot(gt,p.mv(inv,gt))
        loading=reaction/F(207,1000);assert loading.l>p.n.SCALE
        true_loading_lower=F(reaction.l,p.n.SCALE)/F(Q(h,h).h,p.n.SCALE)
        rows.append(dict(parity=row['parity'],remaining_dimension=54,original_high_mode=h,
            inverse_proof_reproduced_identically=True,observed_native_floor_loading_interval=loading.ends(),
            true_response_remaining_loading_lower=str(true_loading_lower),
            unchanged_unlifted_remaining_scalar_floor_Gram_cannot_pass=True,
            actual_remaining_Schur_negative_claimed=False))
        print(row['parity'],'remaining native loading lower',float(F(loading.l,p.n.SCALE)),flush=True)
    return dict(milestone='CC74',status='unchanged remaining-background floor estimator rejected',parity_certificates=rows,
        remaining_complete_source_Gram_computed=False,full_Weil_nonimplication_claimed=False,whole_aperture_positive=False)
if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('remaining');a.add_argument('--output',required=True);a=a.parse_args()
    encoded=Path(a.remaining).read_bytes();raw=gzip.decompress(base64.b64decode(encoded));cert=json.loads(raw)
    assert hashlib.sha256(raw).hexdigest()=='ee5c3ebab7fe2d015ff92145b5c69b72630d90cb6306530e8bd8769469e21557'
    r=run(cert);r['authenticated_remaining_certificate_sha256']=hashlib.sha256(raw).hexdigest()
    r['authenticated_prior_input_sha256']=p.SHA
    Path(a.output).write_text(json.dumps(r,indent=2)+'\n')
