#!/usr/bin/env python3
"""NF376 exact rational audit of why the FOUR FITTED exterior modes are not a new lowband test.

Archives: NF369 SHA-verified strict field slice. No new native/whole operator proof.
"""
import argparse,hashlib,json
from fractions import Fraction as F
from pathlib import Path
PARENT_JSON_SHA='1b22cd77dd555749b8dcc41f92ddd91d982f2eca23ebf3a7638e512147b39d18'
PARENT_ZIP_SHA='1bacc7ae7967d1282eb28fd9d8566204eb21ba93246f6e81b174a18cc2ab1e96'
SLICE_SHA='8148dfed729816d3af4a5ca20798f2a3454cfd99eb53621c8cd4646f24237df8'
TNUM=[[1048576,-83468,750212,-2271087],[0,1048576,-1546322,-1621433],[0,0,1048576,1115405],[0,0,0,1048576]]
def rat(p):return F(int(p[0]))*F(2)**int(p[1])
def ball(z):return (rat(z[0])-rat(z[1]),rat(z[0])+rat(z[1]))
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def neg(a):return -a[1],-a[0]
def mul(a,b):
    v=[a[i]*b[j] for i in range(2) for j in range(2)]
    return min(v),max(v)
def dot(a):
    x=y=F(0)
    for lo,hi in a:x+=lo;y+=hi
    return x,y
def MM(a,b):return [[dot([mul(a[i][k],b[k][j]) for k in range(len(b))]) for j in range(len(b[0]))] for i in range(len(a))]
def tr(a):return [list(x) for x in zip(*a)]
def sub(a,b):return [[add(a[i][j],neg(b[i][j])) for j in range(len(a[0]))] for i in range(len(a))]
def run(slice_path,out_path=None):
    b=Path(slice_path).read_bytes();assert hashlib.sha256(b).hexdigest()==SLICE_SHA
    obj=json.loads(b);p=obj['custody'];assert p['original_nf369_json_sha256']==PARENT_JSON_SHA and p['original_nf369_zip_sha256']==PARENT_ZIP_SHA
    a=obj['data']
    BP=[[ball(z) for z in row] for row in a['nf369_selected_to_original_quotient_signed_coupling_native']]
    CE=[[ball(z) for z in row] for row in a['actual_exterior_signed_Gram_native']]
    S=[[ball(z) for z in row] for row in a['physical_quotient_Gram_native']]
    Y=[[(rat(z),rat(z)) for z in row] for row in a['nf369_quotient_response_exact_dyadic_coefficients']]
    T=[[(F(x,2**20),F(x,2**20)) for x in row] for row in TNUM]
    # E*W u = (BP^T - CE*Y0)T on the same four original fitted E=QF modes.
    R=MM(sub(tr(BP),MM(CE,Y)),T)
    assert len(R)==4 and len(R[0])==4
    diagonal=[]
    for k in range(4):
        assert S[k][k][0]>0
        diagonal.append(S[k][k][0])
        for i in range(4):
            upper=max(abs(R[k][i][0]),abs(R[k][i][1]))
            assert upper**2< S[k][k][0]/F(10**442), ('normalization',k,i)
    out=dict(status='EXACT_RATIONAL_CERTIFIED_FITTED_FOUR_PROBE_CANCEL_ONLY',
      original_parent_json_sha256=PARENT_JSON_SHA,original_parent_zip_sha256=PARENT_ZIP_SHA,portable_parent_slice_sha256=SLICE_SHA,
      original_selected_count=242,critical_trial_count=4,old_exterior_probe_count=4,
      original_fit_coefficient_formula='Y0≈CE^-1 BP^T; R_E=(BP^T-CE Y0)T',
      strict_all_16_original_signed_fitted_pairings_normalized_less_than='1e-221',
      squared_residual_test='max_absolute_R_ki^2 < S_kk.lower/10^442',
      actual_new_outside_four_probe_measured=False,
      lowband_continuum_integrated=False,
      selected_lowband_j_i_constructed=False,
      full_lowband_norm_certified=False,
      original_domain_review='OPEN',W_ODD_NEG='OPEN',RH='OPEN')
    if out_path:Path(out_path).write_text(json.dumps(out,indent=2)+'\n')
    print('PASS all 16 original four-probe matched signed action normalizations <10^-221',flush=True)
    return out
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--slices',required=True);p.add_argument('--report',required=True);a=p.parse_args()
    run(a.slices,a.report)
