#!/usr/bin/env python3
"""NF400 exact source receipt for original 242D projected response.

Validates immutable original NF398 pole-restored selected native outcome
and performs a second, raw-coefficient interval contraction with j387.
Does not assert complete original lowband upper or original operator domain.
"""
import argparse, hashlib, json, re
from decimal import Decimal
from pathlib import Path
from fractions import Fraction as F

SOURCE_NATIVE_SHA='bae006e4fb542c4b0c6d184ae8cfbc2e7c924d45c89092ebda89cf0c6057c877'
ARCHIVE='f7b64ceead7500fca389e3b994a208a6e8aae5be3270b750ab586e5ebe1fa1d0'
MAT='33b52b01e813982bd1a73b9bb81b0ca79f76e4bfd5af0821c4e13b4360bb40fa'
MIX='19356d4be60ee492896083c1bf6be18cd8ce2da058ff60008181f56a4c3ccc23'
FRAME='18ac01bba4de7ec432e419db5ed990fbfabad91c10cbcf2f61cf5666e36b430e'

def load(path):
    raw=Path(path).read_bytes()
    return json.loads(raw),hashlib.sha256(raw).hexdigest()

def ends(v):
    assert len(v)==2
    a,b=map(F,v)
    assert a<=b
    return a,b

def int_add(a,b):return a[0]+b[0],a[1]+b[1]
def int_mul_const(a,c):
    return (a[0]*c,a[1]*c) if c>=0 else (a[1]*c,a[0]*c)
def overlap(a,b):return max(a[0],b[0])<=min(a[1],b[1])

def exact_arb_upper(text):
    """Read recorded Arb ball in exact decimal rational arithmetic.

    Historical NF400 native serialized an Arb upper bound as
      '[decimal_scientific_midpoint +/- decimal_scientific_radius]'
    rather than a single Fraction. The independent receipt must parse the
    original unchanged source, and take midpoint+radius (never midpoint).
    """
    try:
        return F(text)
    except ValueError:
        pattern = r"^\[([^\s\[\]]+)\s+\+/-\s+([^\s\[\]]+)\]$"
        match = re.fullmatch(pattern, text.strip())
        assert match is not None, 'unknown source interval representation'
        mid, rad = (F(Decimal(piece)) for piece in match.groups())
        assert rad >= 0
        assert mid - rad <= mid + rad
        return mid + rad


def run(args):
    native,nsha=load(args.native)
    old,oldsha=load(args.nf398)
    dec,_=load(args.decision)
    assert oldsha==SOURCE_NATIVE_SHA
    assert dec['original_native_report_sha256']==SOURCE_NATIVE_SHA
    assert dec['recomputed_nf391_nf392_source_native_exact_verdict']=='STOP'
    assert native['original_native_NF398_selected_scalar_source_sha256']==SOURCE_NATIVE_SHA
    assert native['original_signed_archive_zip_sha256']==old['original_signed_archive_zip_sha256']==ARCHIVE
    assert native['original_signed_archive_matrix_sha256']==MAT
    assert native['original_signed_archive_mixed_sha256']==MIX
    assert native['original_frame_sha256']==old['original_frame_sha256']==FRAME
    assert native['original_rank_sha256']==old['original_rank_sha256']
    assert native['original_nf369_sha256']==old['original_nf369_sha256']
    assert native['nf387_selected_raw_candidate_git_blob_sha1']==old['nf387_selected_raw_candidate_git_blob_sha1']
    assert native['original_dimension']==242
    assert native['original_archived_reflector_count']==old['original_archived_householder_count']==4
    assert native['source_signed_cells_reused']==30371
    assert native['new_signed_kernel_cells']==0
    assert native['original_242D_signed_column_scalar_contraction_pass'] is True
    assert native['original_242D_multiplier_column_scalar_contraction_pass'] is True
    assert native['original_pole_restored'] is True
    assert native['full_original_physical_selected_Gram_checked'] is True
    assert native['original_16_physical_quotient_Gram_checks'] is True
    assert native['original_complete_lowband_upper_computed'] is False
    assert native['whole_infinite_exterior_inverse_computed'] is False
    assert native['general_operator_domain_independently_audited'] is False
    assert native['W_ODD_NEG']==native['RH']=='OPEN'
    raw=native['original_selected_raw_J_basis_moment_column_outward']
    coord=native['original_selected_D_frame_moment_column_outward']
    assert len(raw)==len(coord)==242
    for item in raw+coord:ends(item)

    # Independent rational contraction of the FULL original raw J242 column
    # with two exact nonzero dyadic entries of original frozen j387.
    z0=F(-10753633,2**48)
    z2=F(8887300,2**48)
    selected=int_add(int_mul_const(ends(raw[0]),z0),
                     int_mul_const(ends(raw[2]),z2))
    original=ends(old['original_multiplier_m_u4_j387_interval'])
    assert overlap(selected,original), 'raw 242D column does not reproduce original signed pole-restored j387 moment'
    assert overlap(ends(native['frozen_j387_selected_moment_check_interval']),original)
    pnorm=ends(native['original_projected_norm_interval_outward'])
    pn2=ends(native['original_projected_norm_squared_native_interval'])
    assert 0<pnorm[0]<=pnorm[1]
    assert 0<pn2[0] and pnorm[0]**2<=pn2[1] and pn2[0]<=pnorm[1]**2
    err=exact_arb_upper(native['certified_global_source_archive_D_frame_l2_error_upper'])
    assert 0<=err<F(1,10**150)
    assert native['normalization_N_row_sum_off_identity_upper']=='1/100'
    # Source-only NF399 dual norm lower must agree with full projected norm:
    assert pnorm[1]>F(3153944,10000000)
    out={
       'pass':'NF401','standing':'INDEPENDENT EXACT ORIGINAL NF400 242D ARCHIVED COLUMN RECEIPT; ORIGINAL LOWBAND UPPER OPEN',
       'native_sha256':nsha,'source_nf398_sha256':oldsha,
       'independent_raw_two_coefficient_j387_contraction_intersection_pass':True,
       'independent_242_component_interval_parse_pass':True,
       'physical_norm2_interval_compatible':True,
       'selected_projection_norm_interval':native['original_projected_norm_interval_outward'],
       'complete_original_lowband_upper':False,'full_J242_necessary_obstruction':False,
       'W_ODD_NEG':'OPEN','RH':'OPEN'
    }
    Path(args.output).parent.mkdir(parents=True,exist_ok=True)
    Path(args.output).write_text(json.dumps(out,indent=2)+'\n')
    print('NF401 original archived NF400 242D raw-column/j387 and Arb-ball error PASS',flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--native',required=True)
    p.add_argument('--nf398',default='notes/data/provisional/NF398_original_j387_selected_signed_native.json')
    p.add_argument('--decision',default='notes/data/provisional/NF398_original_j387_exact_candidate_decision.json')
    p.add_argument('--output',required=True)
    run(p.parse_args())
