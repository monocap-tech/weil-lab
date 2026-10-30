#!/usr/bin/env python3
"""NF401 original selected-projection candidate localization, exact Fraction.

Uses accepted *original* 242D selected source norm, NF398 source-pinned
highband H and NF375 tau. Necessary consequence only, no lowband upper.
"""
import hashlib,json,argparse
from fractions import Fraction as F
from pathlib import Path

NATIVE_SOURCE_SHA='644337986f62a3f25bb6b2005efc82f517975c84629b32b5ae8d1e5b95614515'
NF398_SHA='bae006e4fb542c4b0c6d184ae8cfbc2e7c924d45c89092ebda89cf0c6057c877'
CENTER_LO=F(702871967,10**9) # 0.702871967, strict
BALL_CAP=F(329,10**15)       # 3.29e-13, strict

def read(path):
    raw=Path(path).read_bytes()
    return json.loads(raw), hashlib.sha256(raw).hexdigest()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--nf401',default='notes/data/provisional/NF401_original_242D_selected_column_independent_acceptance.json')
    ap.add_argument('--receipt',default='notes/data/provisional/NF401_original_242D_execution_receipt.json')
    ap.add_argument('--nf398',default='notes/data/provisional/NF398_original_j387_selected_signed_native.json')
    ap.add_argument('--output',default=None)
    args=ap.parse_args()
    selected,selected_hash=read(args.nf401)
    receipt,_=read(args.receipt)
    source,source_hash=read(args.nf398)

    assert selected['pass']=='NF401'
    assert selected['native_sha256']==receipt['original_native_json_sha256']==NATIVE_SOURCE_SHA
    assert selected['source_nf398_sha256']==source_hash==NF398_SHA
    assert receipt['source_nf400_run_id']==41024355742
    assert receipt['source_artifact_id']==12964112303
    assert receipt['native_column_accepted'] is True
    assert receipt['independent_native_recovery_job_result']=='success'
    assert selected['independent_raw_two_coefficient_j387_contraction_intersection_pass'] is True
    assert selected['independent_242_component_interval_parse_pass'] is True
    assert selected['physical_norm2_interval_compatible'] is True
    assert receipt['full_lowband_upper'] is False
    assert selected['complete_original_lowband_upper'] is False
    assert source['W_ODD_NEG']==source['RH']==selected['W_ODD_NEG']==selected['RH']=='OPEN'

    lo,hi=map(F,selected['selected_projection_norm_interval'])
    assert 0 < lo <= hi
    H=F(source['original_NF375_fourth_highband_action_norm_upper'])
    tau=F(source['original_NF375_fourth_lowband_future_target'])
    assert tau==F(7,25000000000000) and H>0
    R=H+tau
    assert R<BALL_CAP
    assert lo>CENTER_LO+R
    assert hi<F(702872,10**6)

    # For true w=m(D)u4, t_L=w-e and original physical projection P:
    #  ||j-Pw||<=||j-Pt_L||+||Pe|| <= tau+H, if ||t_L-j||<=tau.
    #  ||j|| >= ||Pw||-||j-Pw|| > CENTER_LO.
    result={
      'pass':'NF401',
      'standing':'EXACT SOURCE-PINNED ORIGINAL 242D SELECTED PROJECTION LOCALIZATION; CONDITIONAL ON INHERITED STRONG DOMAIN',
      'original_native_sha256':NATIVE_SOURCE_SHA,
      'original_nf398_native_sha256':NF398_SHA,
      'source_nf401_accepted_report_sha256':selected_hash,
      'source_run_id':receipt['source_nf400_run_id'],
      'projection_norm_greater_than':'702871967/1000000000',
      'projection_norm_less_than':'702872/1000000',
      'candidate_center':'P_J m(D)u4',
      'candidate_close_fit_requires':
         '||j-P_J m(D)u4|| <= H+tau <329/1000000000000000 AND ||j||>702871967/1000000000',
      'candidate_center_ball_radius_upper':'329/1000000000000000',
      'source_lowband_target':str(tau),
      'source_highband_bound':str(H),
      'strict_original_rational_comparisons_pass':True,
      'lowband_complement_upper_measured':False,
      'candidate_fourier_tail_certified':False,
      'complete_original_lowband_upper':False,
      'W_ODD_NEG':'OPEN','RH':'OPEN'
    }
    data=json.dumps(result,indent=2)+'\n'
    if args.output:Path(args.output).write_text(data)
    print(data,end='')

if __name__=='__main__':main()
