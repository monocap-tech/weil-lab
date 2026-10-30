#!/usr/bin/env python3
"""NF394 durable attestation of genuine NF393 original selected native moment.

No fabricated result. Fail closed unless the original byte-frozen sources,
direct/reconstructed odd pole, full signed archive, original 16 overlaps and
NF391/392 candidate-specific exact rational verdict are consistent.
No global positivity, lowband upper, or RH certification.
"""
import argparse,hashlib,json,sys
from pathlib import Path
from fractions import Fraction as F
import nf392_original_j387_polynomial_norm_gate as old

ARCHIVE_SHA='f7b64ceead7500fca389e3b994a208a6e8aae5be3270b750ab586e5ebe1fa1d0'
SELECTED_SHA='d705ae312be5324bff64f3a9540e30e8b8bd34dc'
RANK_SHA='9b9820a0163e5e8bf08dd1c2525c757ff67214b49a40cb093d00bc611c9ff9e2'
SOURCE_SHA='abd37707d585dcd54b040f1ae865a7430a9c7cba85df31131661b2e72e560770'
FRAME_SHA='18ac01bba4de7ec432e419db5ed990fbfabad91c10cbcf2f61cf5666e36b430e'

def endpoints(report,key):
    a=tuple(F(v) for v in report[key])
    assert len(a)==2 and a[0]<=a[1],key
    return a

def intersect(a,b):
    return max(a[0],b[0]) <= min(a[1],b[1])

def run(native_path,original512,nf375,j387,output):
    path=Path(native_path)
    raw=path.read_bytes()
    digest=hashlib.sha256(raw).hexdigest()
    n=json.loads(raw)
    assert n['W_ODD_NEG']==n['RH']=='OPEN'
    assert n['original_signed_archive_zip_sha256']==ARCHIVE_SHA
    assert n['original_rank_sha256']==RANK_SHA
    assert n['original_source_sha256']==SOURCE_SHA
    assert n['original_frame_sha256']==FRAME_SHA
    assert n['nf387_selected_raw_candidate_git_blob_sha1']==SELECTED_SHA
    assert n['pole_restored_for_selected_test'] is True
    assert n['original_pole_overlap_source_projection_identity_verified'] is True
    assert n['original_physical_16_Gram_overlaps'] is True
    assert n['original_selected_frame_sha_pass'] is True
    assert n['fresh_original_signed_kernel_cells']==0
    assert n['signed_original_archive_JJ_JF_reused_cells']==30371
    assert n['actual_original_signed_lowband_integral_computed'] is False
    assert n['actual_full_original_lowband_upper_computed'] is False
    assert n['full_original_exterior_infinite_inverse_computed'] is False
    direct=endpoints(n,'original_selected_pole_overlap_direct_original_FT_source_interval')
    via=endpoints(n,'original_selected_pole_overlap_reconstructed_full_match_interval')
    assert intersect(direct,via),'unmatched exact original physical pole identities'
    W=endpoints(n,'original_Wodd_u4_j387_interval')
    C=endpoints(n,'original_pole_correction_plus_2_u4s_js_interval')
    M=endpoints(n,'original_multiplier_m_u4_j387_interval')
    assert intersect((W[0]+C[0],W[1]+C[1]),M),'pole restored wrong sign or source'
    norm2=endpoints(n,'original_j387_physical_norm_squared_interval')
    assert 0<norm2[0]<=norm2[1]
    discrepancy=endpoints(n,'actual_selected_moment_discrepancy_interval')
    assert intersect((M[0]-norm2[1],M[1]-norm2[0]),discrepancy)
    previous=old.evaluate(original512,nf375,j387,native390=native_path)
    assert previous['original_nf390_native_selected_moment_result_supplied'] is True
    assert previous['original_nf390_native_selected_moment_outcome']!='NOT PROVIDED'
    result=previous['fixed_j387_candidate_verdict']
    assert result in ('STOP','INCONCLUSIVE')
    assert previous['W_ODD_NEG']==previous['RH']=='OPEN'
    out={
      'standing':'NF394 VERIFIED ACTUAL ORIGINAL POLE-RESTORED NATIVE J387 SELECTED MOMENT; CANDIDATE METHOD VERDICT ONLY',
      'original_native_report_sha256':digest,
      'original_archive_sha256':ARCHIVE_SHA,
      'original_j387_git_blob_sha1':SELECTED_SHA,
      'physical_pole_independent_overlap_intersection_pass':True,
      'full_odd_pole_restoration_interval_intersection_pass':True,
      'original_j387_physical_norm2_outward_positive_pass':True,
      'original_moment_discrepancy_interval_identity_pass':True,
      'recomputed_nf391_nf392_source_native_exact_verdict':result,
      'actual_fixed_j387_stop_certified':result=='STOP',
      'inconclusive_does_not_prove_candidate_pass':True,
      'actual_selected_moment_discrepancy_interval':n['actual_selected_moment_discrepancy_interval'],
      'original_j387_physical_norm_squared_interval':n['original_j387_physical_norm_squared_interval'],
      'original_selected_pole_interval_direct':n['original_selected_pole_overlap_direct_original_FT_source_interval'],
      'original_selected_pole_interval_reconstructed':n['original_selected_pole_overlap_reconstructed_full_match_interval'],
      'original_complete_lowband_upper_computed':False,
      'whole_exterior_inverse_computed':False,
      'general_operator_domain_review':'OPEN',
      'W_ODD_NEG':'OPEN','RH':'OPEN'
    }
    dst=Path(output)
    dst.parent.mkdir(parents=True,exist_ok=True)
    dst.write_text(json.dumps(out,indent=2)+'\n')
    print('NF394 source-hashed original native selected pole/moment/Gram checks PASS')
    print('NF394 fixed j387 candidate method verdict:',result)
    print('NF394 full lowband upper, complete Weil, RH OPEN')
    return out

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--native',required=True)
    p.add_argument('--original-512',required=True)
    p.add_argument('--nf375',required=True)
    p.add_argument('--j387',required=True)
    p.add_argument('--output',required=True)
    a=p.parse_args()
    run(a.native,a.original_512,a.nf375,a.j387,a.output)
