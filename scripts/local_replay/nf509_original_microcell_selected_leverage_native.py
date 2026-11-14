#!/usr/bin/env python3
"""NF509 genuine original-source microcell selected-leverage numerical probe.

Reconstruct original source J242, 4096-bit full and exterior Grams and the
historical SHA-pinned selected D frame. Numerically integrate *actual*
pair-mirrored microcell restricted Gram matrices via closed-form physical
basis product integrals and contract with the true original exterior inverse.

Unlike prior NF508 aggregate counting, this produces per-index numerical
leverage evidence. It does NOT yet evaluate local original response energy,
so it cannot certify individual local-patch NO_GO / FEASIBLE status.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction as F
from pathlib import Path

from flint import arb, arb_mat, ctx

sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import verify_nf504_original_J8_support_saturated_exterior_native as source
from verify_nf374_original_matched_curvature import load,RANK_SHA
from verify_rpb108_original_signed_frame_transport import candidate
from verify_nf380_original_archived_signed_dual import interval
import verify_rpb108_si29_full_J_L2_normalization as phys

B=F(11,10)
BO=F(549,500)
M=4096
SAMPLES=(0,1,15,63,255,511,1023,2047,3071,3583,4031,4094,4095)
FRAME='18ac01bba4de7ec432e419db5ed990fbfabad91c10cbcf2f61cf5666e36b430e'
NF505_RAW='ad4afeaa4c7d8f48dfc270c437362287d8e2a21d9cce5b385c071e358431d2ec'

def read(path):
    raw=Path(path).read_bytes()
    return json.loads(raw),hashlib.sha256(raw).hexdigest()

def true_basis():
    rank=load('notes/data/provisional/parents/pr350_original_BS_pruned_rank_bound.json',RANK_SHA)
    nodes=[]
    for (freq,kmax),count in zip(rank['original_nodes'],rank['selected_multiplicities']):
        assert 0<=count<=kmax
        for k in range(count):nodes.append((F(freq),k))
    assert len(nodes)==241 and rank['retained_original_pole']
    nodes.append((None,None))
    return nodes

def integral_gram(nodes,b):
    assert F(0)<=b<=B
    K=phys.Integrals()
    K.b=source.native.A(b)
    J=[phys.pole_terms() if freq is None else phys.source_terms(freq,k) for freq,k in nodes]
    H=arb_mat(242,242)
    for i in range(242):
        for j in range(i+1):
            H[i,j]=H[j,i]=phys.gram(J[i],J[j],K)
    return H

def overlap_ball(value,dyadic_ball):
    # Exact converted dyadic interval, no centroid-only comparisons.
    (m,e),(r,f)=dyadic_ball
    m=F(int(m))*F(2)**int(e)
    r=F(int(r))*F(2)**int(f)
    assert r>=0
    return value.lower()<=source.native.A(m+r) and value.upper()>=source.native.A(m-r)

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--nf505-native',required=True)
    p.add_argument('--output',required=True)
    p.add_argument('--bits',type=int,default=4096)
    p.add_argument('--indices',default=','.join(map(str,SAMPLES)))
    o=p.parse_args()
    assert o.bits==4096
    ctx.prec=4096
    indices=sorted(set(map(int,o.indices.split(','))))
    assert indices and all(0<=j<M for j in indices)
    old,oldsha=read(o.nf505_native)
    assert oldsha==NF505_RAW and old['pass']=='NF504-native'
    assert old['source_original_NF407_sha256']==source.SRC
    assert old['source_original_NF406_sha256']==source.SEAM
    assert old['original_selected_J_dimension']==242
    assert old['original_original_D_frame_SHA256']==FRAME
    assert old['original_exterior_center_radius']=='549/500'
    assert old['original_terminal_two_collar_delta']=='1/500'
    assert old['original_support_saturated_physical_Hilbert_gate']=='CERTIFIED_PHYSICAL_SUPPORT_NO_GO'
    assert old['original_weil_multiplier_source_image_domain']=='OPEN'
    orig,srcsha=read('notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json')
    seam,seamsha=read('notes/data/provisional/NF406_original_prime_support_partition_exact.json')
    assert srcsha==source.SRC and seamsha==source.SEAM
    nodes=true_basis()
    basis=[['pole',None] if freq is None else [str(freq),k] for freq,k in nodes]
    assert basis==old['original_source_basis_nodes']
    H=integral_gram(nodes,B)
    D=candidate(H)
    normalized,frameerr=source.source_norm_check(H,D)
    print('NF509 original 242D historic D frame independently reconstructed and SHA checked',flush=True)
    Hout=integral_gram(nodes,BO)
    Nout=D.transpose()*Hout*D
    Nout=(Nout+Nout.transpose())/2
    # Cross-check fresh source-original 4096-bit Gram with NF505 source
    # artifact, including genuine off-diagonals in old selected order.
    for i,j in ((0,0),(1,0),(50,7),(100,99),(241,241)):
        assert overlap_ball(Nout[i,j],old['original_actual_exterior_J242_D_Gram_rows_outward'][i][j]), (
            'METHOD STOP original NF509 exterior Gram vs archived NF505 source',i,j)
    ident=arb_mat([[int(i==j) for j in range(242)] for i in range(242)])
    inverse=Nout.solve(ident,algorithm='lu')
    norm_check=inverse*Nout
    inverse_defect=max(sum((abs(norm_check[i,j]-int(i==j)) for j in range(242)),arb(0))
                       for i in range(242))
    assert inverse_defect.upper()<arb('1e-30'), (
        'METHOD STOP original high-precision inverse independent residual',inverse_defect)
    print('NF509 original exterior 242D inverse 4096-bit posterior source checked',flush=True)
    h=BO/M
    needed={F(j)*h for j in indices}|{F(j+1)*h for j in indices}
    cumul={F(0):arb_mat(242,242),BO:Nout}
    for endpoint in sorted(needed):
        if endpoint in cumul:continue
        Hi=integral_gram(nodes,endpoint)
        Ni=D.transpose()*Hi*D
        Ni=(Ni+Ni.transpose())/2
        cumul[endpoint]=Ni
        print('NF509 original source mirrored endpoint',endpoint,'built',flush=True)
    rows=[]
    for j in indices:
        left=F(j)*h;right=F(j+1)*h
        C=cumul[right]-cumul[left]
        # tr(Nout^-1 * C): authentic source selected projector
        # leverage over both reflected microcell pieces.
        PC=inverse*C
        tau=sum((PC[i,i] for i in range(242)),arb(0))
        assert tau.lower()>0 and tau.upper()<arb(242), (
            'METHOD STOP source actual physical cell leverage',j)
        status=('CERTIFIED_LEVERAGE_LT_27_29' if tau.upper()<source.native.A(F(27,29))
                else 'CERTIFIED_LEVERAGE_GE_27_29' if tau.lower()>=source.native.A(F(27,29))
                else 'LEVERAGE_THRESHOLD_INDETERMINATE')
        rows.append({'j':j,'half_left':str(left),'half_right':str(right),
                     'mirrored_pair_total_width':str(2*h),
                     'true_original_J242_selected_leverage_outward':interval(tau),
                     'leverage_vs_NF508_theta':status})
        print('NF509 true source microcell pair',j,status,tau.str(16),flush=True)
    result={
        'pass':'NF509-original-source-leverage-native',
        'standing':'SOURCE-NATIVE 4096BIT TRUE SELECTED J242 PHYSICAL MICROCELL LEVERAGE; residual e_j and full local-support decisions OPEN',
        'original_nf505_raw_sha256':oldsha,
        'original_nf407_source_sha256':srcsha,
        'original_nf406_seam_sha256':seamsha,
        'original_selected_D_frame_sha256':FRAME,
        'original_selected_dimension':242,
        'original_microcell_count':M,'original_sampled_cell_indices':indices,
        'original_total_pair_half_width':str(h),
        'original_full_frame_normalization_error':interval(frameerr),
        'original_exterior_inverse_4096bit_residual_inf':interval(inverse_defect),
        'original_source_real_microcell_leverage_measurements':rows,
        'original_W_minus_Ja_local_energy_integrated':False,
        'individual_local_support_acceptance_certified':False,
        'original_weil_multiplier_image_graph_domain':'OPEN',
        'W_ODD_NEG':'OPEN','RH':'OPEN'
    }
    Path(o.output).write_text(json.dumps(result,indent=2)+'\n')
    print('NF509 stage complete: genuine original-source selected-leverage measurements, full local energy still OPEN',flush=True)

if __name__=='__main__':
    main()
