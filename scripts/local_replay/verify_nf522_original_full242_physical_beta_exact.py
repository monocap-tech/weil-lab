#!/usr/bin/env python3
"""NF522: complete original 242D physical beta=(historical D)*a_star.

The full original 242D D source was certified by upper-positive triangular
rigidity against the genuine full-carrier 242×242 physical Gram, not by
asserting exact historical dyadic SHA reproduction. The original NF518
global selected fit a_star is independently source-certified.

All beta products and acceptance comparisons are exact integers/Fractions.
The resulting physical coefficient envelope is valid for EVERY x in old O.
This alone does not claim the signed Weil form or RH.
"""
from __future__ import annotations
import argparse,hashlib,json,sys
from pathlib import Path
from fractions import Fraction as F
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
NF505='ad4afeaa4c7d8f48dfc270c437362287d8e2a21d9cce5b385c071e358431d2ec'
NF518='926f8d00d28212f542351760e0c1d814413e8a36a3367d6a58bf837c53865438'
FRAME='18ac01bba4de7ec432e419db5ed990fbfabad91c10cbcf2f61cf5666e36b430e'
N=242;BO=F(549,500);R=10**210
def read(p):
    z=Path(p).read_bytes()
    return json.loads(z),hashlib.sha256(z).hexdigest()
def main():
    p=argparse.ArgumentParser()
    for k in ('nf505','nf518','frame','output'):
        p.add_argument('--'+k,required=True)
    a=p.parse_args()
    old,sh=read(a.nf505)
    fit,fs=read(a.nf518)
    frame,fr=read(a.frame)
    assert sh==NF505 and fs==NF518
    assert old['pass']=='NF504-native'
    assert old['original_selected_J_dimension']==N
    assert old['original_original_D_frame_SHA256']==FRAME
    assert fit['original_nf505_native_SHA256']==sh
    assert fit['original_exact_historical_D_frame_SHA256']==FRAME
    assert frame.get('pass') in (
        'NF521-source-certified-original-historical-D-prefix-rigidity',
        'NF521-original-23D-historic-D-prefix-source-exact-rigidity')
    assert frame.get('original_nf505_SHA256',frame.get('original_nf505_source_SHA256'))==sh
    assert frame.get('historic_original_D_SHA256',frame.get('original_historic_D_frame_SHA256'))==FRAME
    n=frame.get('source_certified_historical_D_prefix_columns',frame.get('historic_D_certified_first_columns'))
    assert n==N
    assert frame.get('remaining_historical_D_columns_open',frame.get('historic_D_remaining_columns_unrecovered'))==0
    matrix=frame.get('untrusted_candidate_integer_upper_triangular_rows',
                    frame.get('firstN_rational_trial_matrix_integer_upper_rows'))
    denC=int(frame.get('untrusted_candidate_denominator',
                       frame.get('firstN_rational_trial_matrix_integer_denominator')))
    v=list(map(int,fit['original_selected_D_frame_coefficients_exact_rational_candidates_numerators']))
    denA=int(fit['original_selected_D_frame_coefficients_exact_rational_denominator'])
    err=F(frame.get('exact_historical_D_prefix_max_row_error_upper',
                    frame.get('historic_original_D_firstN_prefix_max_row_error_upper')))
    assert len(matrix)==len(v)==N and denC==10**420 and denA==10**105
    assert err<F(1,10**14)
    coeffs=[]
    for i,row in enumerate(matrix):
        assert len(row)==N
        assert all(int(row[j])==0 for j in range(i))
        assert int(row[i])>0
        coeffs.append(sum(int(row[j])*v[j] for j in range(i,N)))
    weights=[BO**int(k) if f!='pole' else F(3,5)
             for f,k in old['original_source_basis_nodes']]
    assert len(weights)==N and sum(weights,F(0))<293
    maxa=F(max(map(abs,v)),denA)
    assert maxa<F(5,10**8)
    frame_fee=sum(weights,F(0))*err*maxa
    rounded=[(x*R)//(denC*denA) for x in coeffs]
    rounding_fee=sum(weights,F(0))/R
    epsilon=frame_fee+rounding_fee
    assert epsilon<F(1,10**19)
    result={
        'pass':'NF522-original-242D-raw-physical-beta-source-exact',
        'original_nf505_sha256':sh,
        'original_nf518_galerkin_sha256':fs,
        'original_NF522_full_frame_sha256':fr,
        'historical_D_sha256':FRAME,
        'original_full_selected_rank':N,
        'original_original_basis_nodes':old['original_source_basis_nodes'],
        'original_raw_physical_beta_numerators':list(map(str,rounded)),
        'original_raw_physical_beta_denominator':str(R),
        'source_raw_original_C_times_a_exact_denominator':str(denC*denA),
        'source_raw_original_C_times_a_exact_numerators':list(map(str,coeffs)),
        'source_historical_D_weighted_beta_error_upper':str(frame_fee),
        'source_raw_beta_round_error_upper':str(rounding_fee),
        'source_original_weighted_beta_error_upper':str(epsilon),
        'NF519_weighted_beta_error_gate_1e_minus_19':'PASS',
        'original_local_physical_eD':'OPEN',
        'original_NF404_named_support':'OPEN',
        'Weil_multiplier_image_graph_domain':'OPEN',
        'W_ODD_NEG':'OPEN','RH':'OPEN'}
    Path(a.output).write_text(json.dumps(result,indent=2)+'\n')
    print('NF522 SOURCE EXACT original physical 242 raw beta PASS,',
          'weighted error <1e-19; local eD, Weil/RH still OPEN')
if __name__=='__main__':main()
