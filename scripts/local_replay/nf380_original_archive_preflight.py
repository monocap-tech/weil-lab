#!/usr/bin/env python3
"""Independent exact-source custody/precision preflight for archived original signed response reuse.

This does NOT recompute or certify a new Weil signed pairing; it verifies the
unaltered full original selected-sign and signed-mixed source records that a
future native fast path may conditionally reuse.
"""
import argparse,hashlib,json,zipfile
from pathlib import Path
from fractions import Fraction as F

ZIP_SHA='f7b64ceead7500fca389e3b994a208a6e8aae5be3270b750ab586e5ebe1fa1d0'
M_SHA='33b52b01e813982bd1a73b9bb81b0ca79f76e4bfd5af0821c4e13b4360bb40fa'
MIX_SHA='19356d4be60ee492896083c1bf6be18cd8ce2da058ff60008181f56a4c3ccc23'
RANK='9b9820a0163e5e8bf08dd1c2525c757ff67214b49a40cb093d00bc611c9ff9e2'
FRAME='18ac01bba4de7ec432e419db5ed990fbfabad91c10cbcf2f61cf5666e36b430e'

def run(path,output):
    b=Path(path).read_bytes();assert hashlib.sha256(b).hexdigest()==ZIP_SHA
    with zipfile.ZipFile(path) as z:
        mb=z.read('original_selected_signed_matrix.json'); lb=z.read('original_exterior_refined_mixed.json')
    assert hashlib.sha256(mb).hexdigest()==M_SHA
    assert hashlib.sha256(lb).hexdigest()==MIX_SHA
    m=json.loads(mb);l=json.loads(lb)
    assert m['input_sha256']['rank']==RANK and l['rank_input_sha256']==RANK
    assert m['exact_dyadic_frame_transform_sha256']==FRAME
    assert m['selected_rank']==242 and m['complete_upper_triangle_entries']==242*243//2
    assert m['all_prime_pole_physical_cross_checks']==242*243//2
    assert l['retained_source_count']==242 and l['complete_mixed_entry_count']==242*4
    assert l['all_968_seven_prime_and_true_pole_cross_checks_passed'] is True
    assert len(m['householder_vectors'])==4
    assert [v['start'] for v in m['householder_vectors']]==list(range(4))
    assert all(len(v['vector'])==242-v['start'] for v in m['householder_vectors'])
    tris=m['finite_transformed_signed_matrix_upper_native'];assert len(tris)==242
    assert all(len(r)==i+1 for i,r in enumerate(tris))
    assert len(l['rows'])==242 and all(len(r['entries'])==4 for r in l['rows'])
    assert all(r['entries'][j]['target_index']==j for r in l['rows'] for j in range(4))
    assert len(l['target_signed_kernel_Gram_native'])==4
    assert all(len(r)==4 for r in l['target_signed_kernel_Gram_native'])
    for r in tris:
        for entry in r:
            assert len(entry)==2 and all(len(x)==2 for x in entry)
    err_frame=F(m['double_frame_uniform_error_Frobenius_squared_upper'])
    err_round=F(m['native_matrix_radius_Frobenius_squared_upper'])
    assert F(0)<=err_frame<F(1,10**780)
    assert F(0)<=err_round<F(1,10**810)
    # Rigorous source-error+rounded-matrix uniform Frobenius envelope.
    err_total=err_frame+err_round
    assert err_total<F(1,10**779)
    out=dict(standing='EXACT SHA-PINNED ORIGINAL REUSE PREFLIGHT; NEW SIGNED RESPONSE NOT MEASURED',
        original_parent_archive_sha256=ZIP_SHA,selected_matrix_json_sha256=M_SHA,
        original_mixed_json_sha256=MIX_SHA,original_rank_sha256=RANK,
        exact_native_physical_frame_sha256=FRAME,
        original_selected_count=242,original_target_count=4,
        selected_signed_native_upper_triangle_cells=242*243//2,
        original_mixed_native_cells=968,
        certified_arch_seven_prime_pole_cross_checks=242*243//2+968,
        certified_householder_reflector_count=4,
        old_full_selected_signed_matrix_recomputation_needed=False,
        genuinely_new_unfitted_native_signed_Jv_cells=242,
        genuinely_new_original_basis_signed_base_v_cells=33,
        old_full_WJJ_and_WJF_signed_cells_avoided=242*243//2+968,
        archived_frame_independent_error_frobenius_squared_strict_upper='1e-780',
        archived_matrix_rounding_error_frobenius_squared_strict_upper='1e-810',
        conservative_combined_error_frobenius_squared_strict_upper='1e-779',
        exact_new_signed_coupling_computed=False,
        original_n512_physical_orientation_certified=False,
        original_nf369_native_overlap_recomputed=False,
        original_W_ODD_NEG='OPEN',RH='OPEN')
    s=json.dumps(out,indent=2,sort_keys=True)+'\n'
    if output:Path(output).write_text(s)
    print('PASS archived original J242 signed matrix+mixed identity and Frobenius error control; 275 new signed cells versus 30371 old cells (NOT new signed coupling)')
    return out

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--archive',required=True);p.add_argument('--output',required=True)
 a=p.parse_args();run(a.archive,a.output)
