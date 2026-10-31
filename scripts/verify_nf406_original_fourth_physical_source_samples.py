#!/usr/bin/env python3
"""NF406 original fourth *physical source* correlated point oracle.

Reconstructs unchanged original 242D physical J projection on 4 probes,
the NF369 enormous exact dyadic shear and original NF370 T matrix,
then evaluates u4=f_(T e4)-w4 at actual rational support knots.
Every displayed sample includes the correlated 242D subtraction BEFORE
interval export. These are source values, NOT m(D)u4 or its L2 norm.
"""
import argparse,hashlib,json,time
from fractions import Fraction as F
from pathlib import Path
import flint
from flint import arb,arb_mat,ctx
import verify_rpb108_si29_full_J_L2_normalization as m
from verify_rpb108_original_signed_frame_transport import candidate
from verify_nf374_original_matched_curvature import load,RANK_SHA,PR355_SHA,NF369_SHA,TNUM
from verify_nf380_original_archived_signed_dual import FRAME_SHA,interval

def original_generator_value(c,k,x):
    if c is None:return (x/2).sinh()
    z=2*arb.pi()*m.a(c)*x
    s,v=z.sin_cos()
    return x**k*(s if k%2==0 else v)

def point_values(x,nodes,probes,freqs,rawX,M,T):
    gen=arb_mat([[original_generator_value(c,k,x)] for c,k in nodes])
    critical=[]
    for probe in probes:
        v=sum((m.a(F(coef))*((2*arb.pi()*m.a(F(c))*x).sin())
               for c,coef in zip(freqs,probe['sine_coefficients'])),arb(0))
        v+=m.a(F(probe['sinh_coefficient']))*(x/2).sinh()
        critical.append(v)
    ft=sum((T[j,3]*critical[j] for j in range(4)),arb(0))
    c4=arb_mat([[M[j,3]] for j in range(4)])
    r=rawX*c4
    w4=sum((M[j,3]*critical[j] for j in range(4)),arb(0))
    w4-=sum((gen[i,0]*r[i,0] for i in range(242)),arb(0))
    return ft,w4,ft-w4

def main(args):
    start=time.monotonic()
    assert flint.__version__=='0.8.0'
    ctx.prec=args.bits
    assert args.bits>=4096
    rank=load(args.rank,RANK_SHA)
    source=load(args.source,PR355_SHA)['data']
    parent=load(args.nf369,NF369_SHA)['data']
    nf374,nsha=read(args.nf374)
    nf405,esha=read(args.nf405)
    assert nf374['working_precision_bits']==4096
    assert nf374['native_parent_physical_quotient_overlap_pass'] is True
    assert nsha==nf405['nf374_native_sha256']
    assert source['target_sine_frequencies']==[str(F(5*j,11)) for j in range(1,33)]
    assert parent['selected_rank']==242
    assert nf405['original_source_exact_half_budget_with_endpoint_extraction_pass'] is True
    nodes=[]
    for (c,maxk),count in zip(rank['original_nodes'],rank['selected_multiplicities']):
        assert 0<=count<=maxk
        nodes.extend((F(c),k) for k in range(count))
    assert len(nodes)==241 and rank['retained_original_pole']
    nodes.append((None,None))
    assert len(nodes)==242
    J=[m.pole_terms() if c is None else m.source_terms(c,k) for c,k in nodes]
    probes=source['target_probes']
    freqs=source['target_sine_frequencies']
    Fs=[]
    for probe in probes:
        terms=[]
        for c,coef in zip(freqs,probe['sine_coefficients']):
            terms.extend((n,kind,f,v*m.a(F(coef)))
                         for n,kind,f,v in m.source_terms(F(c),0))
        terms.extend((n,kind,f,v*m.a(F(probe['sinh_coefficient'])))
                     for n,kind,f,v in m.pole_terms())
        Fs.append(terms)
    kern=m.Integrals()
    H=arb_mat(242,242)
    for i in range(242):
        for j in range(i+1):H[i,j]=H[j,i]=m.gram(J[i],J[j],kern)
    D=candidate(H)
    N=D.transpose()*H*D
    assert max(sum((abs(N[i,j]-int(i==j)) for j in range(242)),arb(0))
               for i in range(242))<arb('0.01')
    digest=hashlib.sha256()
    for i in range(242):
        for j in range(242):
            digest.update((json.dumps(m.dyadic(D[i,j]),separators=(',',':'))+'\n').encode())
    assert digest.hexdigest()==FRAME_SHA
    V=arb_mat([[m.gram(s,f,kern) for f in Fs] for s in J])
    rawX=D*N.solve(D.transpose()*V,algorithm='lu')
    assert max(abs((H*rawX-V)[i,j]).upper() for i in range(242) for j in range(4))<arb('1e-80')
    Y0=parent['nf369_quotient_response_exact_dyadic_coefficients']
    T=arb_mat([[m.a(F(v,2**20)) for v in row] for row in TNUM])
    C=arb_mat([[m.a(F(int(v[0]),1)*F(2)**int(v[1]))+int(i==j)
                for j,v in enumerate(row)] for i,row in enumerate(Y0)])
    M=C*T
    sampled=[]
    for t in [F(0),F(1,8),F(1,4),F(1,2),F(3,4),F(7,8),F(15,16),F(1)]:
        x=m.a(F(11,10)*t)
        f,w,u=point_values(x,nodes,probes,freqs,rawX,M,T)
        fn,wn,un=point_values(-x,nodes,probes,freqs,rawX,M,T)
        assert (f+fn).contains(0) and (w+wn).contains(0) and (u+un).contains(0)
        if t==0:assert u.contains(0)
        if t==1:
            lo,hi=map(F,nf405['original_actual_matched_u4_endpoint_interval'])
            assert u.lower()<=m.a(hi) and u.upper()>=m.a(lo)
            jet=nf374['boundary_jets'][3]['w_endpoint_interval']
            low=m.a(jet[0]).lower();up=m.a(jet[1]).upper()
            assert w.lower()<=up and w.upper()>=low
        sampled.append({'x_over_B':str(t),
                        'original_full_critical_fTe4_value_outward':interval(f),
                        'original_full_exterior_w4_value_outward':interval(w),
                        'original_true_u4_value_outward':interval(u),
                        'odd_reflection_native_overlaps':True})
        print('NF406 original source x/B',t,'f,w,u',str(f)[:50],str(w)[:50],str(u)[:50],flush=True)
    out={
       'pass':'NF406',
       'standing':'TRUE ORIGINAL FOURTH PHYSICAL SOURCE CORRELATED RATIONAL POINT ENCLOSURES; MULTIPLIER RESPONSE UNMEASURED',
       'nf369_parent_sha256':NF369_SHA,
       'original_rank_sha256':RANK_SHA,
       'original_source_sha256':PR355_SHA,
       'original_nf374_native_sha256':nsha,
       'original_nf405_endpoint_exact_sha256':esha,
       'original_frame_sha256':FRAME_SHA,
       'original_dimension':242,
       'original_original_critical_probe_count':4,
       'source_true_correlated_reconstruction':'u4=F T e4 -[F-J X](I+Y0)T e4, X=D (D^T H D)^-1 D^T V',
       'source_rational_samples':sampled,
       'original_selected_basis_and_critical_four_count':246,
       'original_odd_physical_parity_native_reproduced':True,
       'original_u4_endpoint_matches_nf405_exact_signed_bounds':True,
       'original_whole_supported_centered_action_norm_integrated':False,
       'original_original_mD_u4_point_evaluated':False,
       'new_signed_kernel_cells':0,
       'W_ODD_NEG':'OPEN','RH':'OPEN',
       'elapsed_seconds':round(time.monotonic()-start,2)
    }
    dest=Path(args.output);dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(out,indent=2)+'\n')
    print('NF406 original true physical source x-point enclosure PASS; compact multiplier action/norm remains OPEN')

def read(p):
 b=Path(p).read_bytes()
 return json.loads(b),hashlib.sha256(b).hexdigest()

if __name__=='__main__':
 p=argparse.ArgumentParser()
 p.add_argument('--rank',default='notes/data/provisional/parents/pr350_original_BS_pruned_rank_bound.json')
 p.add_argument('--source',default='notes/data/provisional/nf372_pr355_fields.json')
 p.add_argument('--nf369',default='notes/data/provisional/nf372_nf369_fields.json')
 p.add_argument('--nf374',default='notes/data/provisional/NF374_original_correlated_curvature_native.json')
 p.add_argument('--nf405',default='notes/data/provisional/NF405_original_endpoint_extracted_tail_exact.json')
 p.add_argument('--bits',type=int,default=4096)
 p.add_argument('--output',required=True)
 main(p.parse_args())
