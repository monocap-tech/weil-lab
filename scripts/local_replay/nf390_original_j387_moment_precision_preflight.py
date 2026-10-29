#!/usr/bin/env python3
"""NF390 exact source-only rational preflight for original selected h=j387.

This is an acceptance SENSITIVITY calculation, NOT an actual Wodd selected
moment, not a lowband integration, and not a proof j387 fails or succeeds.
"""
import argparse, hashlib, json
from pathlib import Path
from fractions import Fraction as F

J_SHA='d705ae312be5324bff64f3a9540e30e8b8bd34dc'
NF375_SHA='03c709571046d3f09307614aaded9749f5a15ba1'
ALPHA=F(-88873,2**48)
B=F(11,10)
NORM_CAP=F(363,2)*abs(ALPHA)
MOMENT_CAP=F(19,10**21)

def load_git_blob(path,expected):
    raw=Path(path).read_bytes()
    digest=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\x00'+raw).hexdigest()
    assert digest==expected,('original Git blob mismatch',path)
    return json.loads(raw)

def run(jpath,nfpath,output=None):
    j=load_git_blob(jpath,J_SHA)
    t=load_git_blob(nfpath,NF375_SHA)
    assert j['W_ODD_NEG']==j['RH']=='OPEN' and t['W_ODD_NEG']==t['RH']=='OPEN'
    assert j['scale_alpha']==str(ALPHA)
    assert j['cutoff']==2**24
    assert j['selected_original_first_center']=='37/64'
    assert j['original_j_is_nonzero'] if 'original_j_is_nonzero' in j else j['nonzero_raw_source_indices']==[0,2]
    assert j['coefficients_raw_source_numerators'][0]==-10753633
    assert j['coefficients_raw_source_numerators'][2]==8887300
    assert len(j['coefficients_raw_source_numerators'])==242
    assert sum(bool(x) for x in j['coefficients_raw_source_numerators'])==2
    assert j['endpoint_value_exact']=='0'
    assert j['original_nf375_git_blob_sha1']==NF375_SHA
    assert j['original_nf375_source_sha256']==t['source_sha256']
    assert 2*B < F(9,4)
    assert (121*abs(ALPHA)*F(3,2)) == NORM_CAP
    row=[o for o in t['directions'][3]['dyadic_cutoff_options'] if o['log2_cutoff']==24]
    assert len(row)==1 and row[0]['cutoff']==2**24
    tau=F(row[0]['chosen_future_lowband_target'])
    high=F(row[0]['highband_upper'])
    assert tau==F(7,25*10**12) and high>0
    threshold_cap=(tau+high)*NORM_CAP
    assert threshold_cap < MOMENT_CAP
    out={
      'standing':'NF390 ORIGINAL J387 MOMENT-STOP PRECISION PREFLIGHT; ACTUAL NATIVE SIGNED MOMENT NOT MEASURED',
      'original_j387_git_blob_sha1':J_SHA,
      'original_nf375_git_blob_sha1':NF375_SHA,
      'original_j387_physical_norm_strict_upper':str(NORM_CAP),
      'original_nf375_fourth_highband_upper':str(high),
      'original_nf375_fourth_lowband_future_target':str(tau),
      'moment_stop_threshold_strict_upper_exact':str(threshold_cap),
      'moment_stop_threshold_rational_ceiling':str(MOMENT_CAP),
      'strictly_enough_to_stop_fixed_j387_if_abs_selected_pole_corrected_discrepancy_exceeds_ceiling':True,
      'actual_original_signed_selected_moment_measured':False,
      'actual_original_j387_candidate_stopped':False,
      'candidate_must_match_original_multiplier_moment_if_accepts':True,
      'original_full_lowband_upper_computed':False,
      'W_ODD_NEG':'OPEN','RH':'OPEN'}
    if output:
        dest=Path(output);dest.parent.mkdir(parents=True,exist_ok=True)
        dest.write_text(json.dumps(out,indent=2)+'\n')
    print('NF390 original source-only dyadic j387 norm <',NORM_CAP)
    print('NF390 candidate-specific selected moment acceptance sensitivity <',MOMENT_CAP)
    print('NF390 actual selected Wodd/pole-corrected moment UNMEASURED; W-ODD-NEG/RH OPEN')
    return out

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--j387',required=True)
    p.add_argument('--nf375',required=True)
    p.add_argument('--output')
    a=p.parse_args()
    run(a.j387,a.nf375,a.output)
