#!/usr/bin/env python3
"""NF393 exact-source Y0T dynamic range and direct pole correction identity.

No native signed selected moment is produced. A native NF390 producer must
restore the rank-one odd pole via <u4,s>=<F*T*e4,s>, using original physical
E=(I-P_J)F orthogonal to s in J242. Exact Y0T raw coefficients are inspected
as a cancellation risk, not a new theorem-sign observation.
"""
import argparse,hashlib,json,sys
from pathlib import Path
from fractions import Fraction as F
sys.set_int_max_str_digits(0)
NF369_GIT_SHA='22a214ac2dff90960c35613aafaad1f44d5011a6'
ORIG_J_GIT_SHA='d705ae312be5324bff64f3a9540e30e8b8bd34dc'
RANK_SHA='9b9820a0163e5e8bf08dd1c2525c757ff67214b49a40cb093d00bc611c9ff9e2'
SOURCE_SHA='abd37707d585dcd54b040f1ae865a7430a9c7cba85df31131661b2e72e560770'
T4=(-2271087,-1621433,1115405,1048576)

def read(path,blob):
    b=Path(path).read_bytes()
    actual=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\x00'+b).hexdigest()
    assert actual==blob,(path,'git blob SHA mismatch')
    return json.loads(b)

def run(nf369,j387,output=None):
    p=read(nf369,NF369_GIT_SHA)
    j=read(j387,ORIG_J_GIT_SHA)
    parent=p['data']
    assert parent['selected_rank']==242
    assert parent['existing_critical_witness_count']==4
    assert parent['nf369_actual_full_complement_upper_computed'] is False
    assert j['original_rank_sha256']==RANK_SHA
    assert j['original_nf375_source_sha256']==SOURCE_SHA
    assert j['nonzero_raw_source_indices']==[0,2]
    assert len(j['coefficients_raw_source_numerators'])==242
    assert j['W_ODD_NEG']==j['RH']=='OPEN'
    Y=parent['nf369_quotient_response_exact_dyadic_coefficients']
    assert len(Y)==4 and all(len(row)==4 for row in Y)
    assert parent['input_sha256']['rank']==RANK_SHA
    v=[]
    for i in range(4):
        f=F(0)
        for k in range(4):
            n,e=Y[i][k]
            f-=F(int(n))*F(2)**int(e)*F(T4[k],2**20)
        assert F(2*10**92)<abs(f)<F(10**93)
        v.append(f)
    # This is a raw-coordinate dynamic-range observation, NOT a proved
    # norm or signed-moment interval for the actual physically cancelled u4.
    ratio_floor=F(2*10**92)/F(131,10**22)   # > 10^112 (raw/diagnostic)
    assert ratio_floor>10**112
    out={
      'standing':'NF393 EXACT ORIGINAL NF369 RAW Y0T DYNAMIC RANGE AND CANCELLATION-FREE SELECTED ODD POLE IDENTITY',
      'original_nf369_git_blob_sha1':NF369_GIT_SHA,
      'original_j387_git_blob_sha1':ORIG_J_GIT_SHA,
      'original_rank_sha256':RANK_SHA,
      'original_source_sha256':SOURCE_SHA,
      'original_T_fourth_column_numerators':list(T4),
      'original_T_column_common_dyadic_denominator_power':20,
      'original_minus_Y0_T_fourth_column_exact_fraction':[str(a) for a in v],
      'each_absolute_raw_F_coefficient_in_open_interval':['2*10^92','10^93'],
      'raw_source_coordinate_to_candidate_moment_threshold_decimal_orders_exceed':112,
      'this_is_only_a_coordinate_cancellation_precision_diagnostic':True,
      'original_pole_source_identity':'<u4,s>=<F*T*e4,s>; u4=F*T*e4 - E*(I+Y0)*T*e4; E perpendicular to J242 and s in J242',
      'original_pole_correction_must_be':'2*<F*T*e4,s>*<j387,s>',
      'native_selected_pole_source_identity_verified':False,
      'original_selected_signed_moment_computed':False,
      'original_j387_candidate_stop':'UNDECIDED',
      'actual_original_lowband_upper_computed':False,
      'full_original_exterior_inverse_computed':False,
      'original_operator_domain_review':'OPEN',
      'W_ODD_NEG':'OPEN','RH':'OPEN'
    }
    if output:
        p=Path(output);p.parent.mkdir(parents=True,exist_ok=True)
        p.write_text(json.dumps(out,indent=2)+'\n')
    print('NF393 original four raw -Y0T fourth column magnitudes: all >2e92 and <1e93')
    print('NF393 direct pole identity structural PASS; native selected moment pending')
    return out

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--nf369',required=True)
    p.add_argument('--j387',required=True)
    p.add_argument('--output')
    a=p.parse_args()
    run(a.nf369,a.j387,a.output)
