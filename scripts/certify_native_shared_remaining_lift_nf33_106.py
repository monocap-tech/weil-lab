#!/usr/bin/env python3
"""NF33: one frozen H2 lift of the full remaining frame, and source tests.
Finite frame positivity and witness tests do not certify the full high Gram.
"""
import argparse,json,hashlib
from pathlib import Path
from fractions import Fraction as F
import certify_native_remaining_source_probe_nf32_106 as probe
prev=probe.prev;n=prev.n;I=n.I;dot=prev.dot;mv=prev.mv
TRIAL32='notes/data/RPB108_NF32_FIXED_REMAINING_SOURCE_PROBES_20261009.json'
SHA32='7e94e46f1f14d8991d44bf1d54b6886f4b7da50a52a0e9ddf6e3c786fb0c3ccc'

def native(source,i,j):return I(*map(F,source[f'{min(i,j)},{max(i,j)}']['full']))

def frame(data,source,idx):
    r=data[0]['authenticated_compensated_targets'][idx];cw=data[2]['parity_certificates'][idx]
    ids=r['retained_indices'];x=list(map(F,r['retained_coefficients']));w=list(map(F,cw['exact_rational_retained_response']))
    T,p,q,free=prev.complement(x,w);hi=[112+idx,114+idx]
    A=[[native(source,i,j) for j in ids] for i in ids]
    AT=[[dot(row,col) for col in zip(*T)] for row in A]
    B=[[dot(col,row) for row in zip(*AT)] for col in zip(*T)]
    C=[[native(source,i,j) for j in hi] for i in hi]
    K=[[dot([native(source,i,j) for j in ids],col) for col in zip(*T)] for i in hi]
    return ids,hi,T,B,C,K

def choose(data,source):
    raw=Path(TRIAL32).read_bytes();assert hashlib.sha256(raw).hexdigest()==SHA32
    tr=json.loads(raw);rows=[]
    assert tr['authenticated_input_sha256']==prev.SHA
    for idx in range(2):
        ids,hi,T,B,C,K=frame(data,source,idx);ci,proof=prev.matrix.inverse(C)
        Z=[[F((z.mid()*10**100).__floor__(),10**100) for z in mv(ci,row)] for row in zip(*K)]
        Z=list(map(list,zip(*Z)))
        a=list(map(F,tr['parities'][idx]['frozen_constraint_coordinates']))
        u=[sum(v*z for v,z in zip(row,a)) for row in T]
        assert list(map(str,u))==tr['parities'][idx]['fixed_rational_probe_coefficients']
        h=[sum(v*z for v,z in zip(row,a)) for row in Z]
        rows.append(dict(parity=['even','odd'][idx],retained_indices=ids,high_indices=hi,
            frozen_shared_lift_map=list(map(lambda row:list(map(str,row)),Z)),
            inherited_constraint_coordinates=list(map(str,a)),
            fixed_probe_coefficients=list(map(str,u+[-v for v in h]))))
    return dict(milestone='NF33',authenticated_input_sha256=prev.SHA,
        NF32_trial_sha256=hashlib.sha256(raw).hexdigest(),parities=rows,
        selection_rule='Z=midpoint(C_H2^-1 K_H2,T), each entry rounded down to denominator 10^100; shared U=T-H2 Z; NF32 coordinates unchanged',
        source_sign_not_inferred_from_selection=True)

def certify_frame(data,source,trial):
    out=[]
    for idx,tr in enumerate(trial['parities']):
        ids,hi,T,B,C,K=frame(data,source,idx);Z=[list(map(F,row)) for row in tr['frozen_shared_lift_map']]
        assert len(Z)==2 and all(len(row)==54 for row in Z)
        CZ=[[dot(row,col) for col in zip(*Z)] for row in C]
        # Full native energy of the exact fixed rational lifted columns.
        L=[[B[i][j]-dot([row[i] for row in K],[row[j] for row in Z])-dot([row[i] for row in Z],[row[j] for row in K])+dot([row[i] for row in Z],[row[j] for row in CZ]) for j in range(54)] for i in range(54)]
        inv,proof=prev.matrix.inverse(L)
        G=[[sum(col[i]*col[j] for col in T)+sum(row[i]*row[j] for row in Z) for j in range(54)] for i in range(54)]
        trace=sum((dot(inv[i],[row[i] for row in G]) for i in range(54)),I(0));assert trace.l>0
        shell=[[K[i][j]-CZ[i][j] for j in range(54)] for i in range(2)]
        maximum=max(z.absupper() for row in shell for z in row)
        a=list(map(F,tr['inherited_constraint_coordinates']));u=[sum(v*z for v,z in zip(row,a)) for row in T];h=[sum(v*z for v,z in zip(row,a)) for row in Z]
        assert list(map(str,u+[-z for z in h]))==tr['fixed_probe_coefficients']
        q=dot(a,mv(L,a));assert q.l>0
        mass=sum(z*z for z in u+h)
        # The 54 free retained coordinates are an identity submatrix of T.
        # Thus lifted physical mass >= coordinate mass, and sqrt(108)<11.
        out.append(dict(parity=tr['parity'],remaining_dimension=54,high_indices=hi,
            original_lifted_finite_energy_positive=True,inverse_verification=proof,
            inverse_physical_trace_upper=str(F(trace.h,n.SCALE)),
            physical_lifted_frame_gap_lower=str(1/F(trace.h,n.SCALE)),
            certified_selected_shell_entry_count=108,selected_shell_max_entry_upper=str(maximum),
            selected_shell_physical_operator_norm_upper=str(11*maximum),
            lifted_probe_native_energy=q.ends(),exact_lifted_probe_mass=str(mass),
            remaining_complete_source_Gram_certified=False,whole_aperture_positive=False))
        print(tr['parity'],'shared lifted native frame PASS; physical gap',float(1/F(trace.h,n.SCALE)),'shell norm upper',float(11*maximum),flush=True)
    return dict(milestone='NF33',authenticated_input_sha256=prev.SHA,parity_certificates=out,
        complete_collective_infinite_high_Schur_certified=False,previous_four_direction_certificate_preserved=True)

def certify_source(data,source,trial,parity):
    idx=['even','odd'].index(parity);tr=trial['parities'][idx]
    ids=tr['retained_indices'];hi=tr['high_indices'];coeff=list(map(F,tr['fixed_probe_coefficients']));allids=ids+hi
    assert allids==list(range(idx,116,2)) and len(coeff)==58
    low=[sum((z*native(source,i,j) for i,z in zip(allids,coeff)),I(0)) for j in ids]
    q=dot(coeff,[sum((z*native(source,i,j) for i,z in zip(allids,coeff)),I(0)) for j in allids]);assert q.l>0
    mass=sum(z*z for z in coeff);rootmass=F(n.sqrt_r(mass).h,n.SCALE)
    m=probe.Moments(880,parity);s=m.source(allids,coeff)
    print(parity,'constructed lifted complete physical source',flush=True)
    residual=(s[0],n.add(s[1],n.scale(n.physical(ids,[z.mid() for z in low]),-1)),s[2],s[3])
    eta=m.eta*rootmass+8*max(F(z.h-z.l,2*n.SCALE) for z in low)
    square=m.gram(residual,residual);assert square.l>0
    root=F(n.sqrt_r(F(square.h,n.SCALE)).h,n.SCALE)
    payment=2*eta*root+eta*eta;gamma=square+I(-payment,payment)
    score=q-gamma/F(207,1000);ratio=gamma/q
    # An independently available original native pairing checks the unsquared
    # source, including the signed high lift, rather than a sampled norm.
    import gzip,base64
    raw=gzip.decompress(base64.b64decode(Path('notes/data/RPB108_NF24_NATIVE_RESIDUAL_PROJECTIONS_117_118_20261009.json.gz.b64').read_bytes()))
    assert hashlib.sha256(raw).hexdigest()=='4c8b0067088486e20f31a7904d3bf56a9f654e982b15450efa85cd6b25e24346'
    archive=json.loads(raw)['complete_original_signed_source'];j=118 if idx==0 else 117
    oracle=sum((z*I(*map(F,archive[f'{i},{j}']['full'])) for i,z in zip(allids,coeff)),I(0))
    pairing=m.pair(s,n.basis(j));paid=pairing+I(-m.eta*rootmass,m.eta*rootmass)
    assert paid.l<=oracle.h and paid.h>=oracle.l
    status='LIFTED_PROBE_DIAGONAL_PASSES' if score.l>0 else 'SHARED_LIFT_FLOOR_REJECTED' if score.h<0 else 'UNRESOLVED'
    print(parity,status,'source square / native energy',float(F(ratio.l,n.SCALE)),float(F(ratio.h,n.SCALE)),flush=True)
    return dict(milestone='NF33',parity=parity,aperture='53/50',interval_grid_digits=500,
        regular_kernel_N=320,pole_degree=40,original_translation_cells=13,
        exact_lifted_probe_mass=str(mass),original_native_energy=q.ends(),
        reconstructed_remaining_source_square=square.ends(),physical_residual_error_upper=str(eta),
        source_square_error_payment=str(payment),original_complete_remaining_source_square=gamma.ends(),
        source_square_over_native_energy=ratio.ends(),floor_score=score.ends(),status=status,
        native_projection_check=dict(test_degree=j,reconstructed=pairing.ends(),original=oracle.ends(),paid_overlap=True),
        remaining_complete_source_Gram_certified=False,actual_negative_vector_claimed=False,
        whole_aperture_positive=False,RH=False,F4=False,Lean=False)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('mode',choices=['choose','frame','source']);p.add_argument('--trial');p.add_argument('--parity',choices=['even','odd']);p.add_argument('--output',required=True);a=p.parse_args()
    data,source,hashes=prev.inputs()
    if a.mode=='choose':out=choose(data,source)
    else:
        raw=Path(a.trial).read_bytes();trial=json.loads(raw);assert trial['authenticated_input_sha256']==prev.SHA
        assert hashlib.sha256(Path(TRIAL32).read_bytes()).hexdigest()==trial['NF32_trial_sha256']==SHA32
        out=certify_frame(data,source,trial) if a.mode=='frame' else certify_source(data,source,trial,a.parity)
        out['fixed_trial_sha256']=hashlib.sha256(raw).hexdigest();out['authenticated_input_sha256']=prev.SHA;out['native_archive_sha256']=hashes
    Path(a.output).write_text(json.dumps(out,indent=2)+'\n')
