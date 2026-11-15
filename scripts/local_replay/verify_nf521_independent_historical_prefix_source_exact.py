#!/usr/bin/env python3
"""NF521 independently verify original historical 140-column D recovery.

Independent exact integer matrix multiplication grouping, authenticated
NF505 old 4096-bit normalization bound, and exact Cholesky uniqueness
inequality. It does not re-integrate the source Gram independently.
"""
import argparse,hashlib,json,pickle,sys
from fractions import Fraction as F
from pathlib import Path
import numpy as np
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
SHA='ad4afeaa4c7d8f48dfc270c437362287d8e2a21d9cce5b385c071e358431d2ec'
FRAME='18ac01bba4de7ec432e419db5ed990fbfabad91c10cbcf2f61cf5666e36b430e'
N=140;S=10**700
def read(p):
    raw=Path(p).read_bytes()
    return json.loads(raw),hashlib.sha256(raw).hexdigest()
def main():
    p=argparse.ArgumentParser()
    p.add_argument('--nf505',required=True)
    p.add_argument('--workdir',required=True)
    a=p.parse_args()
    old,sh=read(a.nf505);assert sh==SHA and old['pass']=='NF504-native'
    assert old['original_original_D_frame_SHA256']==FRAME
    root=Path(a.workdir)
    cert,cs=read(root/'NF521_original_D_prefix140_source_exact.json')
    custody,ct=read(root/'NF521_original_prefix140_gram_custody.json')
    assert cert['pass']=='NF521-source-certified-original-historical-D-prefix-rigidity'
    assert cert['source_certified_historical_D_prefix_columns']==N
    assert cert['remaining_historical_D_columns_open']==102
    assert cert['original_source_prefix_Gram_custody_SHA256']==ct
    assert cert['original_nf505_SHA256']==SHA
    raw=(root/'G_original_full_I_prefix140_700.pkl').read_bytes()
    assert hashlib.sha256(raw).hexdigest()==custody['original_raw_Gram_blob_SHA256']
    G=pickle.loads(raw) # this is a trusted locally generated source artifact
    den=int(cert['untrusted_candidate_denominator'])
    A=np.array([[int(x) for x in row] for row in cert['untrusted_candidate_integer_upper_triangular_rows']],dtype=object)
    assert A.shape==(N,N)
    assert all(A[i,j]==0 for i in range(N) for j in range(i))
    assert all(A[i,i]>0 for i in range(N))
    mid=np.zeros((N,N),dtype=object);rad=0
    for i,row in enumerate(G):
        assert len(row)==i+1
        for j,(lo,hi) in enumerate(row):
            v=(lo+hi)//2;mid[i,j]=mid[j,i]=v
            rad=max(rad,v-lo,hi-v)
    # Independence: change associative order of exact integer congruence.
    Z=(A.T@mid)@A
    Q=S*den*den
    deficit=max(sum(abs(Z[i,j]-(Q if i==j else 0)) for j in range(N)) for i in range(N))
    norm_inf=max(sum(abs(A[i,j]) for j in range(N)) for i in range(N))
    norm_one=max(sum(abs(A[i,j]) for i in range(N)) for j in range(N))
    fee=norm_inf*norm_one*N*rad
    eps=F(deficit+fee,Q)
    assert eps==F(cert['exact_candidate_original_Gram_normalization_max_row_upper'])
    assert eps<F(1,10**200)
    olderr=F(old['original_actual_full_D_normalization_max_row_deviation'][1])
    assert olderr==F(cert['original_source_full_D_normalization_row_upper'])
    assert 0<olderr<F(1,10**900)
    bound=F(norm_inf,den)*2*N*(eps+olderr)/(1-2*N*eps)
    assert bound==F(cert['exact_historical_D_prefix_max_row_error_upper'])
    assert bound<F(1,10**14)
    output={'pass':'NF521-independent-original-historical-140D-prefix-source-exact-audit',
        'original_nf505_SHA256':sh,
        'original_source_140D_certificate_SHA256':cs,
        'original_source_prefix_Gram_SHA256':hashlib.sha256(raw).hexdigest(),
        'independent_exact_140x140_associative_matrix_congruence':True,
        'source_700digit_normalization_bound':str(eps),
        'original_historical_140D_max_row_error_bound':str(bound),
        'historical_D_first140_columns_source_certified':True,
        'historical_D_remaining102_columns':'OPEN',
        'original_full_J242_physical_beta':'OPEN',
        'original_full_J242_local_eH':'OPEN',
        'original_NF404_named_support':'OPEN',
        'Weil_multiplier_image_graph_domain':'OPEN','W_ODD_NEG':'OPEN','RH':'OPEN'}
    dest=root/'NF521_independent_original_D_prefix140_audit.json'
    dest.write_text(json.dumps(output,indent=2)+'\n')
    print('NF521 independent source exact original first140 historical D audit PASS')
    print('Other 102 historical columns, full physical eH and RH OPEN')
if __name__=='__main__':
    main()
