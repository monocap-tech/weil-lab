#!/usr/bin/env python3
"""NF48: original remaining-53 native block and all signed joined couplings.

Finite native transport only: no subtraction of an infinite-high response
from a separately eliminated finite block is presented as a Schur bound.
"""
import argparse, base64, gzip, hashlib, json, sys
from pathlib import Path
from fractions import Fraction as F
sys.set_int_max_str_digits(0)
import certify_native_next_shell_nf46_106 as v
import certify_native_floor_transport_nf47_106 as f
n=v.n; I=v.I; dot=v.p.dot; mv=v.p.mv


def decode(path):
    raw=Path(path).read_bytes()
    if str(path).endswith('.b64'): raw=gzip.decompress(base64.b64decode(raw))
    return json.loads(raw)


def constraint_frame(row):
    ids,retained,columns=f.original_columns(['even','odd'].index(row['parity']))
    base,p,q,free=f.frame.complement(*retained[:2])
    ell=list(map(F,row['third_constraint_coordinates']));k=row['third_constraint_pivot_in_old_free_coordinates']
    remaining=[j for j in range(54) if j!=k]
    T=[[r[j]-ell[j]/ell[k]*r[k] for j in remaining] for r in base]
    assert all(sum(a*b for a,b in zip(r,col))==0 for r in retained for col in zip(*T))
    return ids,T,retained,columns


def run():
    nf47raw=Path('notes/data/RPB108_NF47_FLOOR_TRANSPORT_CERTIFICATE_20261009.json').read_bytes()
    nf47=json.loads(nf47raw)
    data,source,archive_hashes=f.frame.inputs()
    rows=[]
    for idx,row in enumerate(nf47['parity_frames']):
        parity=row['parity'];ids,T,retained,columns=constraint_frame(row)
        o,*_=v.prior.packet(idx)
        assert columns==o['columns'] and ids==o['ids']
        sparse=[[(ids[j],z) for j,z in enumerate(col) if z] for col in zip(*T)]
        def native(i,j): return I(*map(F,source[f'{min(i,j)},{max(i,j)}']['full']))
        C=[[sum((a*b*native(i,j) for i,a in left for j,b in right),I(0)) for right in sparse] for left in sparse]
        C=v.symmetry(C)
        print(parity,'all 1431 remaining native entries reconstructed',flush=True)
        inv,proof=v.mi.inverse(C)
        M=[[sum(a*b for a,b in zip(left,right)) for right in zip(*T)] for left in zip(*T)]
        trace=sum((inv[i][j]*M[j][i] for i in range(53) for j in range(53)),I(0));assert trace.l>0
        print(parity,'remaining physical native gap',float(1/F(trace.h,n.SCALE)),flush=True)
        lows=o['low'];errors=o['retained_errors']
        radii=[errors[i]+8*max(F(z.h-z.l,2*n.SCALE) for z in lows[i]) for i in range(3)]
        masses=[f.packet.ceilnorm(col) for col in zip(*T)]
        raw=[[dot(col,low) for col in zip(*T)] for low in lows]
        paid=[[z+I(-errors[i]*mass,errors[i]*mass) for z,mass in zip(raw[i],masses)] for i in range(3)]
        centers=[[z.mid() for z in low] for low in lows]
        B=[[sum(a*b for a,b in zip(col,center)) for col in zip(*T)] for center in centers]
        hat=[[dot(B[i],mv(inv,B[j])) for j in range(3)] for i in range(3)]
        assert min(hat[i][i].l for i in range(3))>0
        norms=[v.r.normupper(hat[i][i]) for i in range(3)]
        e=[radius*v.r.normupper(trace) for radius in radii]
        payments=[[e[i]*norms[j]+e[j]*norms[i]+e[i]*e[j] for j in range(3)] for i in range(3)]
        reaction=v.symmetry([[hat[i][j]+I(-payments[i][j],payments[i][j]) for j in range(3)] for i in range(3)])
        old=f.data(parity.upper()+'_FREE_CORRECTION_FUNCTIONAL_CERTIFICATE',37)
        Q=v.p.prev.matrix(old['original_selected_native_energy_Gram'])
        finite=v.symmetry(v.c.add(Q,v.c.scale(reaction,-1)))
        first=finite[0][0];leading=first*finite[1][1]-n.sq(finite[0][1])
        det=v.p.c.parent.det3(finite)
        if first.l>0 and leading.l>0:
            margin=finite[2][2]-(finite[1][1]*n.sq(finite[0][2])-2*finite[0][1]*finite[0][2]*finite[1][2]+finite[0][0]*n.sq(finite[1][2]))/leading
        else: margin=I(-1,1)
        status='CERTIFIED_POSITIVE' if min(first.l,leading.l,margin.l,det.l)>0 else 'UNRESOLVED'
        print(parity,'finite full-retained graph',status,'last margin',*[float(F(z)) for z in margin.ends()],flush=True)
        rows.append(dict(parity=parity,remaining_dimension=53,original_remaining_native_Gram=v.p.prev.ends(C),
            physical_constraint_Gram_reconstructed_exactly=True,
            inverse_verification=proof,physical_inverse_trace=trace.ends(),physical_native_gap_lower=str(1/F(trace.h,n.SCALE)),
            retained_source_approximant_coordinates=[[z.ends() for z in low] for low in lows],
            retained_source_reconstruction_errors=list(map(str,errors)),physical_retained_source_ball_radii=list(map(str,radii)),
            remaining_native_couplings_approximant=v.p.prev.ends(raw),original_remaining_native_couplings=v.p.prev.ends(paid),
            midpoint_finite_reaction_Gram=v.p.prev.ends(hat),reaction_sqrt_error_bounds=list(map(str,e)),
            finite_reaction_error_payments=[list(map(str,r)) for r in payments],original_finite_remaining_reaction_Gram=v.p.prev.ends(reaction),
            joined_native_Gram=v.p.prev.ends(Q),finite_joined_after_remaining_elimination=v.p.prev.ends(finite),
            finite_leading_pair_determinant=leading.ends(),finite_condensed_margin=margin.ends(),finite_determinant=det.ends(),
            finite_full_retained_graph_status=status,
            high_condensed_remaining_block_certified=False,remaining_complete_high_source_Gram_certified=False))
    return dict(milestone='NF48',aperture='53/50',NF47_certificate_sha256=hashlib.sha256(nf47raw).hexdigest(),
        original_native_archive_uncompressed_sha256=archive_hashes,
        parity_certificates=rows,all_original_remaining_native_entries_paid=2862,all_original_signed_joined_couplings_paid=318,
        classification='finite native transport on the exact remaining-53 frame; no whole high response assembly',
        original_frozen_vectors_changed=False,original_native_inputs_regenerated=False,
        complete_high_transport_certified=False,whole_aperture_positive=False,highest_certified_whole_aperture='21/20',RH=False,F4=False,Lean=False)


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',required=True);args=parser.parse_args()
    raw=(json.dumps(run(),indent=2,sort_keys=True)+'\n').encode()
    if args.output.endswith('.b64'): raw=base64.b64encode(gzip.compress(raw,mtime=0))+b'\n'
    Path(args.output).write_bytes(raw)
