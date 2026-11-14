#!/usr/bin/env python3
"""NF513: source-certified exact original second n9-active J8 edge-cell profile.

Preserves immutable NF494 original 400 H/U response and NF505 original
physical J242 source identity. Reuses NF511 matched analytic/log evaluator,
with a reduced midpoint shift of 85 jets and EXPLICIT exact bound on all
omitted original coefficients 85..399. Computes source W² and pole cross
at H4094, compares with existing NF511 H4095, identifies n9 seam H4093.
Does not compute globally fitted original selected 242D residual or RH.
"""
from __future__ import annotations
import argparse,hashlib,json,math,sys
from fractions import Fraction as F
from pathlib import Path
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
import verify_nf511_original_J8_H4095_local_W_pole_exact as m

NF505='ad4afeaa4c7d8f48dfc270c437362287d8e2a21d9cce5b385c071e358431d2ec'
NF494='39cba367d70243c2d15e5a9323fc8097d58187923dcf0eca2b031136871f0181'
B=F(11,10);BO=F(549,500);M=4096
WIDTH=BO/M;J=4094
DL=B-BO+WIDTH;DR=DL+WIDTH
TRUNC=85

# Original NF511 routines are source-physical; set the ACTUAL new
# original cell before any midpoint reexpansion/integral is attempted.
m.DLO=DL;m.DMAX=DR;m.CENTER=(DL+DR)/2;m.J=J
m.LOG_TERMS=60

def source_preserving_shift(coefs):
    assert len(coefs)==400
    v=[(0,0) for _ in range(m.ORDER+1)]
    for a in reversed(coefs[:TRUNC]):
        vv=[(0,0) for _ in v]
        vv[0]=m.add(m.posmul(v[0],m.CENTER,m.CENTER),a)
        for k in range(1,m.ORDER+1):
            vv[k]=m.add(m.posmul(v[k],m.CENTER,m.CENTER),v[k-1])
        v=vv
    tmax=WIDTH/2
    low=tmax**(m.ORDER+1)*sum((
        F(max(abs(a),abs(b)),m.SCALE)*math.comb(n,m.ORDER+1)*DR**(n-m.ORDER-1)
        for n,(a,b) in enumerate(coefs[:TRUNC]) if n>m.ORDER
    ),F(0))
    high=sum((
        F(max(abs(a),abs(b)),m.SCALE)*DR**n
        for n,(a,b) in enumerate(coefs) if n>=TRUNC
    ),F(0))
    assert low+high<F(1,10**38)
    return v,low+high

def read(p):
    raw=Path(p).read_bytes()
    return json.loads(raw),hashlib.sha256(raw).hexdigest()

def source_seam():
    lo,hi=m.log_positive(F(9))
    seam=2*B-hi,2*B-lo
    assert DR<seam[0]                    # H4094 entirely n9 active
    assert B-BO+2*WIDTH<seam[0]<seam[1]<B-BO+3*WIDTH  # H4093 straddles seam
    return seam

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--nf494',required=True)
    p.add_argument('--nf505',required=True)
    p.add_argument('--nf511',required=True)
    p.add_argument('--output',required=True)
    p.add_argument('--slabs',type=int,default=128)
    a=p.parse_args()
    assert 16<=a.slabs<=1024 and a.slabs&(a.slabs-1)==0
    old494,sha494=read(a.nf494)
    old505,sha505=read(a.nf505)
    old511,sha511=read(a.nf511)
    assert (sha494,sha505)==(NF494,NF505)
    assert old494['pass']=='NF494-native' and old505['pass']=='NF504-native'
    assert old494['original_nf407_source_sha256']==old505['source_original_NF407_sha256']==m.SRC
    assert old494['original_nf406_seams_sha256']==old505['source_original_NF406_sha256']==m.SEAM
    assert old505['original_selected_J_dimension']==242
    assert old505['original_source_basis_nodes'][241]==['pole',None]
    assert old511['pass'] in (
        'NF511-source-local-W-square-exact',
        'NF511-original-source-exact-local-W-pole-panel'
    )
    assert old511['cell_index' if 'cell_index' in old511 else 'mirrored_cell_index']==4095
    assert old494['original_source_400_jet_order']==400
    assert DR<F(1,25)
    seam=source_seam()
    weights={2:2,3:3,4:2,5:5,7:7,8:2,9:3}
    CLo=CHi=F(0)
    for n,pbase in weights.items():
        ln=m.log_positive(F(pbase))
        sqrt=m.sqrt_bounds(n)
        CLo+=ln[0]/sqrt[1];CHi+=ln[1]/sqrt[0]
    assert 3<CLo<CHi<5
    Hraw=m.coeffs(old494,'original_H_400_native_outward')
    Uraw=m.coeffs(old494,'original_U_400_native_outward')
    Hjets,hfee=source_preserving_shift(Hraw)
    Ujets,ufee=source_preserving_shift(Uraw)
    U0=m.as_fr(Uraw[0]);assert U0[1]<0
    rho=DR/F(1,25)
    h_cauchy=F(10)**420*rho**400/(1-rho)
    u_cauchy=F(10)**400*rho**400/(1-rho)
    assert h_cauchy<F(1,10**55) and u_cauchy<F(1,10**75)
    panel=lambda n:m.panel(
        Hjets,Ujets,U0,(CLo,CHi),hfee+h_cauchy,ufee+u_cauchy,n)
    coarse,fine=panel(16),panel(a.slabs)
    assert coarse[0]<=fine[0]<=fine[1]<=coarse[1]
    assert coarse[2]<=fine[2]<=fine[3]<=coarse[3]
    assert fine[1]/fine[0]<F(105,100)
    aa=m.sinh_minus_x(B-DL);bb=m.sinh_minus_x(B-DR)
    C0,C1=aa[0]-bb[1],aa[1]-bb[0]
    assert 0<C0<C1 and fine[2]<fine[3]<0
    capture=fine[3]**2/(C1*fine[1])
    assert capture>F(95,100)
    pair=lambda x,y:[m.dec_lo(x),m.dec_hi(y)]
    # Only serialized outward receipt inputs may authorize this ratio:
    e_out=F(m.dec_hi(fine[1]))
    b_out=F(m.dec_hi(fine[3]))
    c_out=F(m.dec_hi(C1))
    capture_out=F(m.dec_lo(b_out**2/(c_out*e_out)))
    assert F(95,100)<capture_out<=capture
    result={
      'pass':'NF513-original-source-J8-H4094-local-W-pole-exact',
      'standing':'Original source W squared and pole cross on second n9-active J8 edge microcell. Globally fitted J242 eH OPEN.',
      'NF494_SHA256':sha494,'NF505_SHA256':sha505,
      'NF511_H4095_receipt_SHA256':sha511,
      'original_NF407_source_SHA256':m.SRC,'original_NF406_seams_SHA256':m.SEAM,
      'selected_original_dimension':242,
      'cell_index':J,'mirror_pair_count':M,
      'cell_positive_x':[str(B-DR),str(B-DL)],
      'cell_d':[str(DL),str(DR)],
      'analytic_source_400_jets_retained':True,
      'recentered_jet_order':m.ORDER,
      'recentered_source_H400_HU_prefix_terms':TRUNC,
      'original_source_H400_high_order_85through399_paid':True,
      'original_source_U400_high_order_85through399_paid':True,
      'recentered_H400_total_remainder_upper':m.dec_hi(hfee,95),
      'recentered_U400_total_remainder_upper':m.dec_hi(ufee,95),
      'holomorphic_H400_cauchy_upper':m.dec_hi(h_cauchy,100),
      'holomorphic_U400_cauchy_upper':m.dec_hi(u_cauchy,120),
      'exact_source_n9_seam_d_interval':pair(seam[0],seam[1]),
      'H4094_no_prime_seam':True,'H4093_crosses_n9_prime_seam':True,
      'source_C8_prime_power_rational_interval':pair(CLo,CHi),
      'original_H4094_W_squared_outward':pair(fine[0],fine[1]),
      'original_H4094_W_pole_cross_outward':pair(fine[2],fine[3]),
      'original_H4094_pole_Gram_outward':pair(C0,C1),
      'original_H4094_W_pointwise_negative_outward':pair(fine[4],fine[5]),
      'original_H4094_best_pole_alignment_lower':str(capture_out),
      'coarse16_W_squared_outward':pair(coarse[0],coarse[1]),
      'coarse16_W_pole_outward':pair(coarse[2],coarse[3]),
      'slabs':a.slabs,
      'original_full_242D_globally_fitted_local_residual_eH':'OPEN',
      'original_selected_full_leverage_tauH':'OPEN',
      'Weil_source_image_graph_domain':'OPEN','W_ODD_NEG':'OPEN','RH':'OPEN'
    }
    Path(a.output).write_text(json.dumps(result,indent=2)+'\n')
    print('NF513 original source H4094 W squared:',float(fine[0]),float(fine[1]))
    print('NF513 original source H4094 W/pole cross:',float(fine[2]),float(fine[3]))
    print('NF513 original source H4094 best local pole capture >',float(capture_out))
    print('NF513 H4093 crosses n9 seam; fitted J242 eH, source domain and RH OPEN')

if __name__=='__main__':
    main()
