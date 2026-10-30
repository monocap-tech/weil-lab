#!/usr/bin/env python3
"""NF404: original 242D selected projection endpoint jets (true native Arb).

NO fresh signed kernel cells. Reconstructs the certified original physical
H/D/N and original source-pinned NF401 outward D-frame signed+pole column.
Computes raw projection COEFFICIENTS, endpoint value and first derivative,
plus the exact Hilbert point/derivative evaluation-dual norms. The endpoint
is NOT the supported multiplier action endpoint and is NOT a lowband upper.
"""
import argparse,hashlib,json,sys,time
from fractions import Fraction as F
from pathlib import Path
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)

import flint
from flint import arb,arb_mat,ctx
import verify_rpb108_si29_full_J_L2_normalization as phys
from verify_rpb108_original_signed_frame_transport import candidate
from verify_nf374_original_matched_curvature import load,RANK_SHA,PR355_SHA
from verify_nf380_original_archived_signed_dual import interval,FRAME_SHA

NATIVE_SHA='644337986f62a3f25bb6b2005efc82f517975c84629b32b5ae8d1e5b95614515'
ACCEPTED_SOURCE_NF398='bae006e4fb542c4b0c6d184ae8cfbc2e7c924d45c89092ebda89cf0c6057c877'
B=F(11,10)

def read(path):
    b=Path(path).read_bytes()
    return json.loads(b),hashlib.sha256(b).hexdigest()

def rational_ball(span):
    assert len(span)==2
    lo,hi=map(F,span)
    assert lo<=hi
    mid=(lo+hi)/2
    rad=(hi-lo)/2
    # Both rational endpoints are data from ORIGINAL full native outward
    # interval, not a newly recalculated signed moment or point estimate.
    return arb(phys.a(mid),phys.a(rad))

def col(rows):
    return arb_mat([[z] for z in rows])

def endpoint_jets(nodes):
    """Odd original selected generators x^k sin/cos(2*pi*c*x), pole sinh(x/2)."""
    x=phys.a(B);twopi=2*arb.pi()
    values=[];derivatives=[]
    for c,k in nodes:
        if c is None:
            values.append((x/2).sinh())
            derivatives.append((x/2).cosh()/2)
            continue
        assert k>=0 and isinstance(c,F)
        phase=twopi*phys.a(c)*x
        sn,co=phase.sin_cos()
        term=(x**k)
        omega=twopi*phys.a(c)
        if k%2==0:
            values.append(term*sn)
            derivatives.append((k*x**(k-1)*sn if k else arb(0))+term*omega*co)
        else:
            values.append(term*co)
            derivatives.append(k*x**(k-1)*co-term*omega*sn)
    assert len(values)==len(derivatives)==242
    return col(values),col(derivatives)

def main(args):
    begin=time.monotonic()
    assert flint.__version__=='0.8.0'
    ctx.prec=args.bits
    assert args.bits>=4096
    rank=load(args.rank,RANK_SHA)
    source=load(args.source,PR355_SHA)['data']
    accepted,accepted_sha=read(args.native)
    acceptance,acceptance_sha=read(args.acceptance)
    receipt,_=read(args.receipt)
    assert accepted_sha==NATIVE_SHA
    assert receipt['native_column_accepted'] is True
    assert receipt['original_native_json_sha256']==acceptance['native_sha256']==NATIVE_SHA
    assert accepted['original_native_NF398_selected_scalar_source_sha256']==acceptance['source_nf398_sha256']==ACCEPTED_SOURCE_NF398
    assert accepted['original_rank_sha256']==RANK_SHA
    assert accepted['original_frame_sha256']==FRAME_SHA
    assert accepted['original_dimension']==242 and accepted['original_pole_restored'] is True
    assert accepted['new_signed_kernel_cells']==0
    assert accepted['original_242D_multiplier_column_scalar_contraction_pass'] is True
    assert accepted['original_complete_lowband_upper_computed'] is False
    assert accepted['W_ODD_NEG']==accepted['RH']=='OPEN'
    nodes=[];offset=0
    for (c,maxk),count in zip(rank['original_nodes'],rank['selected_multiplicities']):
        assert 0<=count<=maxk
        for k in range(count):nodes.append((F(c),k))
        offset+=maxk
    assert offset==469 and len(nodes)==241 and rank['retained_original_pole']
    nodes.append((None,None))
    J=[phys.pole_terms() if c is None else phys.source_terms(c,k) for c,k in nodes]
    kernel=phys.Integrals()
    print('NF404 source-pinned accepted D-frame original 242D response:',accepted_sha,flush=True)
    print('NF404 reconstructing ORIGINAL physical 242D Gram; no signed kernel work',flush=True)
    H=arb_mat(242,242)
    for i in range(242):
        for j in range(i+1):
            H[i,j]=H[j,i]=phys.gram(J[i],J[j],kernel)
    D=candidate(H)
    N=D.transpose()*H*D
    assert max(sum((abs(N[i,k]-int(i==k)) for k in range(242)),arb(0))
               for i in range(242)) < arb('0.01')
    digest=hashlib.sha256()
    for i in range(242):
        for j in range(242):
            digest.update((json.dumps(phys.dyadic(D[i,j]),separators=(',',':'))+'\n').encode())
    assert digest.hexdigest()==FRAME_SHA
    d=col([rational_ball(x) for x in accepted['original_selected_D_frame_moment_column_outward']])
    assert d.nrows()==242
    response=N.solve(d,algorithm='lu')
    coeff=D*response
    source_projection_norm2=(d.transpose()*response)[0,0]
    assert source_projection_norm2.lower()>0
    stored_norm=accepted['original_projected_norm_interval_outward']
    known_lo,known_hi=map(F,stored_norm)
    assert source_projection_norm2.lower()<=phys.a(known_hi*known_hi)
    assert source_projection_norm2.upper()>=phys.a(known_lo*known_lo)
    assert acceptance['physical_norm2_interval_compatible'] is True
    # Original RAW physical moment enclosure also must be reproduced from
    # the newly reconstructed Gram and accepted transformed column.
    r=H*coeff
    for i,original_span in enumerate(accepted['original_selected_raw_J_basis_moment_column_outward']):
        lo,hi=map(F,original_span)
        assert r[i,0].lower()<=phys.a(hi) and r[i,0].upper()>=phys.a(lo),('original raw moment overlap',i)
    print('NF404 original physical 242D selected norm and 242 raw-moment overlaps PASS',flush=True)
    ev,ed=endpoint_jets(nodes)
    v=(ev.transpose()*coeff)[0,0]
    deriv=(ed.transpose()*coeff)[0,0]
    # Finite-dimensional Riesz duals verify the numerical sensitivity
    # of endpoint traces; original interval column already pays archive
    # error, and native Gram/solve uncertainty is in Arb.
    Ev=D.transpose()*ev
    Ed=D.transpose()*ed
    repr_v=N.solve(Ev,algorithm='lu')
    repr_d=N.solve(Ed,algorithm='lu')
    eval_dual2=(Ev.transpose()*repr_v)[0,0]
    deriv_dual2=(Ed.transpose()*repr_d)[0,0]
    assert eval_dual2.lower()>0 and deriv_dual2.lower()>0
    # independent trace isometry bound, not claiming pointwise operator norm
    # on all L2(I) (evaluation is unbounded there).
    assert (v*v).lower()<=source_projection_norm2.upper()*eval_dual2.upper()
    assert (deriv*deriv).lower()<=source_projection_norm2.upper()*deriv_dual2.upper()
    report={
      'pass':'NF404',
      'standing':'TRUE ORIGINAL 242D SELECTED PROJECTION ENDPOINT TRACE; NOT FULL MULTIPLIER RESPONSE',
      'parent_nf401_native_sha256':accepted_sha,
      'parent_nf401_independent_acceptance_sha256':acceptance_sha,
      'original_rank_sha256':RANK_SHA,
      'original_source_sha256':PR355_SHA,
      'original_physical_frame_sha256':FRAME_SHA,
      'original_rank':242,
      'original_support_half_width':'11/10',
      'real_multiplier_pole_restored':True,
      'all_original_selected_raw_moments_interval_reproduced':True,
      'accepted_original_selected_projection_norm_interval':stored_norm,
      'native_reconstructed_selected_power_interval':interval(source_projection_norm2),
      'original_selected_endpoint_value_interval':interval(v),
      'original_selected_endpoint_derivative_interval':interval(deriv),
      'original_selected_endpoint_eval_dual_squared_interval':interval(eval_dual2),
      'original_selected_endpoint_derivative_dual_squared_interval':interval(deriv_dual2),
      'original_endpoint_trace_is_not_full_multiplier_response_trace':True,
      'new_signed_kernel_cells':0,
      'original_full_supported_multiplier_scalar_norm_upper_computed':False,
      'original_J_perpendicular_full_action_upper_computed':False,
      'original_lowband_upper_computed':False,
      'original_operator_domain_independently_audited':False,
      'W_ODD_NEG':'OPEN','RH':'OPEN',
      'elapsed_seconds':round(time.monotonic()-begin,2)
    }
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(report,indent=2)+'\n')
    print('NF404 original selected J242 endpoint value:',v,flush=True)
    print('NF404 original selected J242 endpoint derivative:',deriv,flush=True)
    print('NF404 trace DUAL norms:',eval_dual2,deriv_dual2,flush=True)
    print('NF404 genuine source result wrote',p,flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--rank',default='notes/data/provisional/parents/pr350_original_BS_pruned_rank_bound.json')
    p.add_argument('--source',default='notes/data/provisional/nf372_pr355_fields.json')
    p.add_argument('--native',default='notes/data/provisional/NF401_original_242D_selected_column_source_native.json')
    p.add_argument('--acceptance',default='notes/data/provisional/NF401_original_242D_selected_column_independent_acceptance.json')
    p.add_argument('--receipt',default='notes/data/provisional/NF401_original_242D_execution_receipt.json')
    p.add_argument('--output',required=True)
    p.add_argument('--bits',type=int,default=4096)
    main(p.parse_args())
