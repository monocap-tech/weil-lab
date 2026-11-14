#!/usr/bin/env python3
"""NF512 actual original full W first 14 selected RAW cell moments.

Uses genuine source-certified NF511 W<0 on H4095, immutable original NF505
authentic selected generator order, exact rational Machin pi, alternating
sine/cosine envelopes and source Cauchy checks. Does not transport the
coarse raw intervals through old 242D D frame or claim local e_H/RH.
"""
from __future__ import annotations
import argparse,json,hashlib,math,sys
from pathlib import Path
from fractions import Fraction as F
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
NF494='39cba367d70243c2d15e5a9323fc8097d58187923dcf0eca2b031136871f0181'
NF505='ad4afeaa4c7d8f48dfc270c437362287d8e2a21d9cce5b385c071e358431d2ec'
SRC='0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce'
SEAM='c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675'
FRAME='18ac01bba4de7ec432e419db5ed990fbfabad91c10cbcf2f61cf5666e36b430e'
BO=F(549,500);H=BO/4096;L=BO-H;R=BO;FREQ=F(37,64);ROUND=70

def read(path):
    raw=Path(path).read_bytes()
    return json.loads(raw),hashlib.sha256(raw).hexdigest()
def alt_series(q,kind,n):
    assert F(0)<q<1
    if kind=='atan':
        p=sum(((-1)**j*q**(2*j+1)/F(2*j+1) for j in range(n)),F(0))
        tail=q**(2*n+1)/F(2*n+1)
    elif kind=='sin':
        p=sum(((-1)**j*q**(2*j+1)/math.factorial(2*j+1) for j in range(n)),F(0))
        tail=q**(2*n+1)/math.factorial(2*n+1)
    else:
        assert kind=='cos'
        p=sum(((-1)**j*q**(2*j)/math.factorial(2*j) for j in range(n)),F(0))
        tail=q**(2*n)/math.factorial(2*n)
    # For n even the n-term alternating sum is lower; for n odd upper.
    return (p-tail,p) if n%2 else (p,p+tail)
def floor(x):return x.numerator//x.denominator
def down(x):return F(floor(x*10**ROUND),10**ROUND)
def up(x):return F(-floor(-x*10**ROUND),10**ROUND)

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--nf505',required=True)
    p.add_argument('--nf511',required=True)
    p.add_argument('--output',required=True)
    args=p.parse_args()
    n,ns=read(args.nf505);j,js=read(args.nf511)
    assert ns==NF505 and n['pass']=='NF504-native'
    assert n['source_original_NF407_sha256']==SRC and n['source_original_NF406_sha256']==SEAM
    assert n['original_selected_J_dimension']==242 and n['original_original_D_frame_SHA256']==FRAME
    assert n['original_source_basis_nodes'][:14]==[['37/64',k] for k in range(14)]
    if j['pass']=='NF511-source-local-W-square-exact':
        assert j['original_NF494_full_H400_U400_json_sha256']==NF494
        assert j['original_NF505_native_sha256']==NF505
        assert j['cell_index']==4095
        assert j['source_original_NF407_sha256']==SRC
        assert j['source_original_NF406_sha256']==SEAM
        wl,wh=map(F,j['original_cell_full_W_pointwise_negative_interval'])
        Ehi=F(j['original_cell_full_W_sq_outward'][1])
    else:
        assert j['pass']=='NF511-original-source-exact-local-W-pole-panel'
        assert j['original_nf494_raw_SHA256']==NF494
        assert j['original_nf505_raw_SHA256']==NF505
        assert j['mirrored_cell_index']==4095
        assert j['original_nf407_source_SHA256']==SRC
        assert j['original_nf406_seams_SHA256']==SEAM
        wl,wh=map(F,j['local_W_pointwise_negative_outward'])
        Ehi=F(j['local_E_H_original_full_W_squared'][1])
    assert wl<wh<0 and Ehi>0
    a=alt_series(F(1,5),'atan',90)
    b=alt_series(F(1,239),'atan',90)
    pi_lo=16*a[0]-4*b[1];pi_hi=16*a[1]-4*b[0]
    assert 3<pi_lo<pi_hi<F(22,7)
    u_lo=pi_lo*(2*FREQ*L-1)
    u_hi=pi_hi*(2*FREQ*R-1)
    assert 0<u_lo<u_hi<1
    sl=alt_series(u_lo,'sin',45)[0]
    su=alt_series(u_hi,'sin',45)[1]
    cl=alt_series(u_hi,'cos',45)[0]
    cu=alt_series(u_lo,'cos',45)[1]
    assert 0<sl<su<1 and 0<cl<cu<1
    rows=[]
    for k in range(14):
        tlo,thi=(sl,su) if k%2==0 else (cl,cu)
        rawlo=2*H*(-wh)*L**k*tlo
        rawhi=2*H*(-wl)*R**k*thi
        assert 0<rawlo<rawhi
        # Original physical Cauchy: ||j_k||² <= 2H R^(2k).
        assert rawlo**2<=Ehi*(2*H*R**(2*k))
        lo,hi=down(rawlo),up(rawhi)
        assert 0<lo<=rawlo<rawhi<=hi
        rows.append({
          'raw_selected_index':k,'source_node':['37/64',k],
          'source_basis_kind':'x^k sin(2*pi*f*x)' if k%2==0 else 'x^k cos(2*pi*f*x)',
          'true_original_local_raw_mixed_outward':[str(lo),str(hi)],
          'true_original_local_raw_mixed_display':[float(lo),float(hi)]})
    assert len(rows)==14
    receipt={
      'pass':'NF512-first-authentic-source-14-raw-selected-H4095-moments',
      'scope':'SOURCE-EXACT first 14 original RAW selected mixed cell moments; NOT correlation-preserved historic D-frame b_H or globally fitted original e_H',
      'original_NF511_source_local_receipt_sha256':js,
      'original_NF505_native_source_sha256':ns,
      'original_NF494_source_sha256':NF494,
      'original_NF407_source_sha256':SRC,'original_NF406_seams_sha256':SEAM,
      'original_selected_dimension':242,'original_D_frame_sha256':FRAME,
      'true_original_mirrored_cell_index':4095,
      'Machin_pi_arctan_terms':90,'sine_cosine_series_terms':45,
      'first_14_original_selected_raw_source_moments_all_strict_positive':True,
      'genuine_original_raw_first_frequency_block14':rows,
      'historical_D_frame_source_correlated_local_moments':'OPEN',
      'original_globally_fitted_J242_local_eH':'OPEN',
      'original_J242_leverage_tauH':'OPEN',
      'original_Weil_multiplier_image_graph_domain':'OPEN','W_ODD_NEG':'OPEN','RH':'OPEN'}
    Path(args.output).write_text(json.dumps(receipt,indent=2)+'\n')
    print('NF512 source-original first 14 RAW H4095 selected mixed W moments EXACT FRACTION PASS')
    print('All 14 genuine first-frequency moments strictly positive')
    print('Historic D-frame selected response, globally fitted eH and RH OPEN')

if __name__=='__main__':main()
