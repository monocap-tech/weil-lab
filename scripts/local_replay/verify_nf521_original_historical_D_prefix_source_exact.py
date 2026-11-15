#!/usr/bin/env python3
"""NF521: certify original historical D-prefix by triangular Cholesky rigidity.

The authentic historical full D is upper-triangular positive-diagonal (from
original 4096-bit Cholesky source code), and archived NF505 source certifies
||D^T G_I D-I||_infinity <1e-900. Any independently reconstructed
upper-positive C with rigorously verified ||C^T Gprefix C-I||_infinity
and a bounded ||C||_infinity has a provable entrywise error to the EXACT
historical D prefix. All acceptance uses exact integers/Fractions; mpmath
chooses only an untrusted candidate C.
The 242D global physical beta and complete cell residual remain OPEN.
"""
import argparse,hashlib,json,pickle,sys
from pathlib import Path
from fractions import Fraction as F
import mpmath as mp
import numpy as np
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
SOURCE='ad4afeaa4c7d8f48dfc270c437362287d8e2a21d9cce5b385c071e358431d2ec'
FRAME='18ac01bba4de7ec432e419db5ed990fbfabad91c10cbcf2f61cf5666e36b430e'
S=10**700;T=10**420

def read(path):
    raw=Path(path).read_bytes()
    return json.loads(raw),hashlib.sha256(raw).hexdigest()

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--nf505',required=True)
    p.add_argument('--rank',type=int,choices=(23,100,140,242),required=True)
    p.add_argument('--workdir',required=True)
    a=p.parse_args()
    old,sh=read(a.nf505)
    assert sh==SOURCE and old['pass']=='NF504-native'
    assert old['original_selected_J_dimension']==242
    assert old['original_original_D_frame_SHA256']==FRAME
    olderr=F(old['original_actual_full_D_normalization_max_row_deviation'][1])
    assert 0<=olderr<F(1,10**900)
    root=Path(a.workdir)
    receipt,srcsha=read(root/f'NF521_original_prefix{a.rank}_gram_custody.json')
    assert receipt['pass']=='NF521-original-source-full-I-prefix-700digit-Gram'
    assert receipt['original_nf505_source_SHA256']==sh
    assert receipt['source_historical_prefix_rank']==a.rank
    raw=(root/f'G_original_full_I_prefix{a.rank}_700.pkl').read_bytes()
    assert hashlib.sha256(raw).hexdigest()==receipt['original_raw_Gram_blob_SHA256']
    G=pickle.loads(raw) # only self-generated local source files; never unpickle untrusted inputs
    n=a.rank
    assert len(G)==n and all(len(row)==i+1 for i,row in enumerate(G))
    # NUMERICAL UNTRUSTED CANDIDATE: no floating acceptance.
    mp.mp.dps=590
    M=mp.matrix(n)
    for i,row in enumerate(G):
        for j,(lo,hi) in enumerate(row):
            M[i,j]=M[j,i]=mp.mpf(lo+hi)/(2*S)
    L=mp.cholesky(M)
    C=mp.inverse(L.transpose())
    Ct=np.zeros((n,n),dtype=object)
    for i in range(n):
        for j in range(i,n):
            sign,mant,exp,bits=C[i,j]._mpf_
            z=mant*T
            z=(z<<exp) if exp>=0 else z//(1<<(-exp))
            Ct[i,j]=-z if sign else z
        assert Ct[i,i]>0
    # Complete ORIGINAL SOURCE interval normalization via exact integer math:
    mid=np.zeros((n,n),dtype=object);rad=0
    for i,row in enumerate(G):
        for j,(lo,hi) in enumerate(row):
            v=(lo+hi)//2
            mid[i,j]=mid[j,i]=v
            rad=max(rad,v-lo,hi-v)
    Z=Ct.T@(mid@Ct)
    q=S*T*T
    deficit=max(sum(abs(Z[i,j]-(q if i==j else 0)) for j in range(n)) for i in range(n))
    row=max(sum(abs(Ct[i,j]) for j in range(n)) for i in range(n))
    col=max(sum(abs(Ct[i,j]) for i in range(n)) for j in range(n))
    fee=row*col*n*rad
    eps=F(deficit+fee,q)
    assert eps<F(1,10**200)
    norm=F(row,T)
    # Rigidity theorem: if ||N-I||_inf<=eps<1/(100n) then its
    # positive-diagonal upper Cholesky R has ||R-I||_inf<=2n*eps.
    # D=CX, X upper positive and R_D=R_C X by uniqueness. Hence
    # ||D-C||inf <= ||C||inf * 2n(eps+eps_old)/(1-2n eps).
    assert 2*n*eps<F(1,100)
    bound=norm*(2*n)*(eps+olderr)/(1-2*n*eps)
    assert bound<F(1,10**14)
    result={
        'pass':'NF521-source-certified-original-historical-D-prefix-rigidity',
        'original_nf505_SHA256':sh,
        'historic_original_D_SHA256':FRAME,
        'original_full_selected_dimension':242,
        'source_certified_historical_D_prefix_columns':n,
        'remaining_historical_D_columns_open':242-n,
        'original_source_prefix_Gram_custody_SHA256':srcsha,
        'original_source_full_D_normalization_row_upper':str(olderr),
        'untrusted_candidate_denominator':str(T),
        'untrusted_candidate_integer_upper_triangular_rows':[[str(Ct[i,j]) for j in range(n)] for i in range(n)],
        'exact_candidate_original_Gram_normalization_center_deficit':str(F(deficit,q)),
        'exact_candidate_source_interval_perturbation':str(F(fee,q)),
        'exact_candidate_original_Gram_normalization_max_row_upper':str(eps),
        'exact_candidate_infinity_norm_upper':str(norm),
        'exact_historical_D_prefix_max_row_error_upper':str(bound),
        'original_historical_D_prefix_error_strict_lt_1e_minus_14':True,
        'full_original_242D_raw_physical_beta':'OPEN',
        'full_original_242D_local_eH':'OPEN',
        'original_NF404_named_physical_patch':'OPEN',
        'Weil_multiplier_image_graph_domain':'OPEN','W_ODD_NEG':'OPEN','RH':'OPEN'}
    target=root/f'NF521_original_D_prefix{n}_source_exact.json'
    target.write_text(json.dumps(result,indent=2)+'\n')
    print('NF521 original HISTORICAL D first',n,'columns SOURCE-EXACT PASS')
    print('Original source frame row error log10 approx',len(str(bound.numerator))-len(str(bound.denominator)))
    print('Remaining',242-n,'historical D columns, full local residual/RH OPEN')
if __name__=='__main__':
    main()
