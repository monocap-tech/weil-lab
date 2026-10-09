#!/usr/bin/env python3
"""Exact restriction of CC71's shared high lift to the NF31 complement."""
import argparse,base64,gzip,hashlib,json
from pathlib import Path
from fractions import Fraction as F
import certify_native_remaining_background_nf31_106 as p

def run(old,remaining):
    data,source,archive_hashes=p.inputs();targets,_,responses,*_=data;rows=[]
    for r,wc,lift,native in zip(targets['authenticated_compensated_targets'],responses['parity_certificates'],old['parity_certificates'],remaining['parity_certificates']):
        ids=r['retained_indices'];x=list(map(F,r['retained_coefficients']));w=list(map(F,wc['exact_rational_retained_response']))
        T,a,b,free=p.complement(x,w)
        assert [a,b]==native['retained_constraint_pivots'] and free==native['free_retained_coordinates']
        assert lift['parity']==r['parity'] and lift['fixed_lift_all_55_directions_positive']
        assert x[0]!=0
        W=[[F(0)]*55 for _ in ids]
        for j in range(55):W[0][j]=-x[j+1]/x[0];W[j+1][j]=1
        V=T[1:]
        assert [[sum(c*d for c,d in zip(row,col)) for col in zip(*V)] for row in W]==T
        Z=list(map(lambda row:list(map(F,row)),lift['fixed_rational_high_lift_coefficients']))
        ZT=[[sum(c*d for c,d in zip(row,col)) for col in zip(*V)] for row in Z]
        hs=lift['high_indices']
        def Q(i,j):return p.I(*map(F,source[f'{min(i,j)},{max(i,j)}']['full']))
        C=[[Q(h,k) for k in hs] for h in hs]
        residual=[]
        for i,h in enumerate(hs):
            line=[]
            for j,col in enumerate(zip(*T)):
                v=sum((z*Q(k,h) for k,z in zip(ids,col)),p.I(0))
                v-=sum((C[i][k]*ZT[k][j] for k in range(2)),p.I(0));line.append(v)
            residual.append(line)
        bound=sum((v.absupper()**2 for row in residual for v in row),F(0))
        root=F(p.n.sqrt_r(bound).h,p.n.SCALE)
        # T contains a free-coordinate identity, hence ||Ta||>=||a||.
        # The Frobenius residual norm bounds source coordinates for every
        # physical unit retained vector of T, independently of old gaps.
        assert root<F(1,10**65)
        gap=F(lift['fixed_lift_physical_gap_lower']);assert gap>0
        # Native energy of the inherited graph dominates gap*||Ta||^2.
        measured_loading=bound/(F(207,1000)*gap)
        assert measured_loading<F(1,10**100)
        rows.append(dict(parity=r['parity'],remaining_dimension=54,high_indices=hs,
            exact_remaining_basis=[[str(v) for v in row] for row in T],
            fixed_shared_remaining_high_lift=[[str(v) for v in row] for row in ZT],
            exact_transfer_WV_equals_T=True,exact_seed_and_response_orthogonality=True,
            inherited_original_finite_graph_physical_gap_lower=str(gap),
            all_measured_high_coordinates=[[v.ends() for v in row] for row in residual],
            measured_high_source_operator_norm_upper=str(root),
            measured_high_floor_loading_upper=str(measured_loading),
            complete_remaining_source_Gram_certified=False,full_high_positive=False))
        print(r['parity'],'graph gap',float(gap),'measured source norm',float(root),'loading',float(measured_loading),flush=True)
    return dict(milestone='CC76',aperture='53/50',shared_remaining_lift_dimension=108,
        measured_source_coordinates=216,parity_certificates=rows,native_archive_sha256=archive_hashes,
        previous_four_direction_full_high_certificate_preserved=True,old_whole_domain_gap_used=False,
        whole_aperture_positive=False,full_retained_infinite_high_sign=False,
        full_Weil_nonimplication_claimed=False)

if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('prior');a.add_argument('remaining');a.add_argument('--output',required=True);a=a.parse_args()
    raw=Path(a.prior).read_bytes();encoded=Path(a.remaining).read_bytes();rem=gzip.decompress(base64.b64decode(encoded))
    assert hashlib.sha256(raw).hexdigest()=='732fe27f7061bbe702f108363cd22848ce61daa93d381cd73c54d9dfa297b7b0'
    assert hashlib.sha256(rem).hexdigest()=='ee5c3ebab7fe2d015ff92145b5c69b72630d90cb6306530e8bd8769469e21557'
    r=run(json.loads(raw),json.loads(rem));r['input_sha256']=[hashlib.sha256(raw).hexdigest(),hashlib.sha256(rem).hexdigest()]
    Path(a.output).write_text(json.dumps(r,indent=2)+'\n')
