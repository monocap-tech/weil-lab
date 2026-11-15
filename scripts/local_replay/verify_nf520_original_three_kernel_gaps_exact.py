#!/usr/bin/env python3
"""NF520: ACTUAL ORIGINAL 242D three Fredholm gaps, exact-integer acceptance.

Input: SHA-authenticated source Gram enclosures at the three endpoints,
and ANY (untrusted) integer triangular preconditioner. Certify
T^t [G_keep - gap*G_O] T > 0 by exact Gershgorin plus a rigorously paid
outward source-interval perturbation. No historical D frame needed.
The original full physical local eD and original RH remain OPEN.
"""
import argparse,hashlib,json,pickle,time
from fractions import Fraction as F
from pathlib import Path
import numpy as np
from nf520_original_raw_gram_exact import S,add
N=242;Q=10**200
SRC='ad4afeaa4c7d8f48dfc270c437362287d8e2a21d9cce5b385c071e358431d2ec'
def mulrat(a,r):
    r=F(r);p=r.numerator;q=r.denominator
    z=(a[0]*p,a[1]*p) if p>=0 else (a[1]*p,a[0]*p)
    return z[0]//q,-((-z[1])//q)
def matrix_for(case,gs):
    if case=='union':coeff=[(2,F(1)),(0,-F(1,20000))]
    elif case=='H4095':coeff=[(1,F(1)),(0,-F(1,1000))]
    elif case=='H4094':coeff=[(0,F(3,5)),(1,-F(1)),(2,F(1))]
    else:raise ValueError(case)
    A=np.empty((N,N),dtype=object);E=0
    for i in range(N):
        for j in range(i+1):
            z=(0,0)
            for k,c in coeff:z=add(z,mulrat(gs[k][i][j],c))
            assert z[0]<=z[1]
            mid=(z[0]+z[1])//2
            E=max(E,mid-z[0],z[1]-mid)
            A[i,j]=A[j,i]=mid
    return A,E
def accept(case,root):
    t=time.time();root=Path(root)
    custody_raw=(root/'nf520_original_gram_custody.json').read_bytes()
    custody=json.loads(custody_raw)
    assert custody['pass']=='NF520-original-source-exact-physical-gram-oracle'
    assert custody['nf505_raw_sha256']==SRC
    assert custody['nf407_source_sha256']=='0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce'
    assert custody['nf406_source_sha256']=='c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675'
    assert custody['scale']==str(S) and custody['old_full_selected_dimension']==N
    gs=[]
    for i in range(3):
        raw=(root/f'G{i}_oracle.pkl').read_bytes()
        assert hashlib.sha256(raw).hexdigest()==custody['Gram'][str(i)]['original_source_interval_file_sha256']
        gs.append(pickle.loads(raw))
        assert len(gs[-1])==N and all(len(row)==j+1 for j,row in enumerate(gs[-1]))
    M,e=matrix_for(case,gs)
    trial=(root/f'T_{case}_candidate.pkl').read_bytes()
    T=np.array(pickle.loads(trial),dtype=object)
    assert T.shape==(N,N)
    assert all(T[i,j]==0 for i in range(N) for j in range(i))
    print('NF520 exact congruence starting',case,flush=True)
    W=T.T@(M@T)
    scal=S*Q*Q
    deficit=max(sum(abs(W[i,j]-(scal if i==j else 0))
                    for j in range(N)) for i in range(N))
    row=max(sum(abs(T[i,j]) for j in range(N)) for i in range(N))
    col=max(sum(abs(T[i,j]) for i in range(N)) for j in range(N))
    # SOURCE OUTWARD FEE: each raw interval M_ij centered with
    # |M_ij - M_mid_ij| <= e/S. Thus the operator norm infinity fee
    # after exact T congruence <= ||T^t||inf * N e/S * ||T||inf.
    radius=row*col*N*e
    assert deficit+radius<scal,('SOURCE METHOD STOP',case)
    result={
      'pass':'NF520-original-source-complete-242D-Fredholm-gap-exact',
      'case':case,
      'standing':'Certified original J242 restricted kernel gap only; full local globally fitted eD and original NF404 named physical support remain OPEN',
      'original_selected_dimension':N,
      'original_nf505_source_SHA256':SRC,
      'original_source_gram_custody_SHA256':hashlib.sha256(custody_raw).hexdigest(),
      'untrusted_preconditioner_integer_blob_SHA256':hashlib.sha256(trial).hexdigest(),
      'strict_original_selected_Fredholm_gap_lower':{
          'H4094':'2/5','H4095':'1/1000','union':'1/20000'}[case],
      'exact_Gershgorin_center_deficit_upper':str(F(deficit,scal)),
      'exact_Gershgorin_source_interval_error_upper':str(F(radius,scal)),
      'exact_Gershgorin_remaining_positive_margin':str(F(scal-deficit-radius,scal)),
      'source_trigonometric_phase_exact_fixed_scale':str(S),
      'untrusted_candidate_preconditioner_exact_integer_scale':str(Q),
      'original_Fredholm_spectral_gap_source_certified':True,
      'original_historical_D_frame_reconstruction_required_for_gap':False,
      'original_full_242D_global_fit_local_residual_eD':'OPEN',
      'original_unconditional_NF404_named_patch':'OPEN',
      'Weil_multiplier_image_graph_domain':'OPEN','W_ODD_NEG':'OPEN','RH':'OPEN'}
    (root/f'gap_cert_{case}.json').write_text(json.dumps(result,indent=2)+'\n')
    print('NF520 SOURCE-EXACT 242D original gap',case,
          '>',result['strict_original_selected_Fredholm_gap_lower'],
          'Gershgorin center deficit',float(F(deficit,scal)),
          'source fee',float(F(radius,scal)),
          'PASS in',round(time.time()-t,1),'seconds',flush=True)
    return result
if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--workdir',required=True)
    p.add_argument('--case',choices=('H4094','H4095','union'),required=True)
    a=p.parse_args();accept(a.case,a.workdir)
