#!/usr/bin/env python3
"""NF511 independent exact Fraction source-custody and local pole-panel audit.

This independently checks SHA custody, physical geometry, authentic pole
Gram, Cauchy/Schur necessary relations and the outward original NF511
W²/pole evidence. Does NOT independently re-integrate H400/U400 or
construct the complete 242D local residual.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse, json, hashlib, math, sys
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
SRC='0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce'
SEAM='c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675'
NF494='39cba367d70243c2d15e5a9323fc8097d58187923dcf0eca2b031136871f0181'
NF505='ad4afeaa4c7d8f48dfc270c437362287d8e2a21d9cce5b385c071e358431d2ec'
B=F(11,10);h=F(549,500*4096);xlo=F(549,500)-h;xhi=F(549,500)

def read(p):
    raw=Path(p).read_bytes()
    return json.loads(raw),hashlib.sha256(raw).hexdigest()

def interval(pair):
    l,u=map(F,pair)
    assert l<=u
    return l,u

def sinh_minus_x(x):
    # Independent physical source-true pole Gram with 44 terms;
    # different Taylor order from native 30-term implementation.
    assert 0<=x<B
    n=44
    low=sum((x**(2*k+1)/math.factorial(2*k+1)
             for k in range(1,n+1)),F(0))
    nextterm=x**(2*n+3)/math.factorial(2*n+3)
    ratio=x*x/F((2*n+4)*(2*n+5))
    return low,low+nextterm/(1-ratio)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--nf494',required=True)
    ap.add_argument('--nf505',required=True)
    ap.add_argument('--candidate',required=True)
    ap.add_argument('--output',required=True)
    o=ap.parse_args()
    H,hsha=read(o.nf494);N,nsha=read(o.nf505);c,csha=read(o.candidate)
    assert (hsha,nsha)==(NF494,NF505)
    assert c['pass']=='NF511-original-source-exact-local-W-pole-panel'
    assert N['pass']=='NF504-native' and H['pass']=='NF494-native'
    assert H['original_nf407_source_sha256']==N['source_original_NF407_sha256']==SRC
    assert H['original_nf406_seams_sha256']==N['source_original_NF406_sha256']==SEAM
    assert c['original_nf407_source_SHA256']==SRC
    assert c['original_nf406_seams_SHA256']==SEAM
    assert c['original_nf494_raw_SHA256']==NF494
    assert c['original_nf505_raw_SHA256']==NF505
    assert N['original_source_basis_nodes'][241]==['pole',None]
    assert c['original_sinh_pole_index']==241
    assert c['original_selected_dimension']==242 and c['mirrored_cell_count']==4096
    assert c['mirrored_cell_index']==4095
    assert list(map(F,c['x_positive_cell']))==[xlo,xhi]
    assert list(map(F,c['d_positive_cell']))==[B-xhi,B-xlo]
    assert c['analytic_radius']=='1/25'
    assert c['recentered_taylor_order']==30
    assert c['slabs']>=16
    E=interval(c['local_E_H_original_full_W_squared'])
    b=interval(c['local_b_H_original_sinh_pole_cross'])
    C=interval(c['local_C_H_original_sinh_pole_Gram'])
    assert 0<E[0]<E[1] and b[0]<b[1]<0 and 0<C[0]<C[1]
    sl,sh=sinh_minus_x(xlo)
    tl,th=sinh_minus_x(xhi)
    Cfrom=(tl-sh,th-sl)
    assert max(C[0],Cfrom[0])<=min(C[1],Cfrom[1])
    assert b[0]**2 <= E[1]*C[1] # source Cauchy consistency
    qfloor=b[1]**2/C[1]
    assert 0<qfloor<E[1]
    reported_q=F(c['local_best_scalar_pole_capture_power_lower'])
    reported_r=F(c['local_best_scalar_pole_unexplained_upper'])
    reported_fraction=F(c['local_best_scalar_pole_alignment_fraction_lower'])
    assert 0<reported_q<=qfloor
    assert reported_r>=E[1]-reported_q
    assert 0<reported_fraction<=reported_q/E[1]
    assert reported_fraction>F(96,100)
    assert E[1]/E[0]<F(11,10)
    assert interval(c['coarse_16_slab_W2'])[0]<=E[0]<=E[1]<=interval(c['coarse_16_slab_W2'])[1]
    oldR=interval(N['original_original_saturated_exterior_residual_outward'])
    gamma=F(N['original_original_gamma_squared'])
    assert 0<gamma<oldR[0] and E[0]>gamma
    assert c['original_named_full_242D_bH'] is False
    assert c['original_named_full_242D_CH'] is False
    assert c['original_named_residual_eH']=='OPEN'
    assert c['NF404_named_patch_verdict']=='OPEN'
    assert c['Weil_multiplier_image_graph_domain']=='OPEN'
    assert c['W_ODD_NEG']==c['RH']=='OPEN'
    receipt={
      'pass':'NF511-independent-exact-receipt-audit',
      'standing':'INDEPENDENT SHA/Fraction original H4095 W², sinh-pole cross/Gram and local pole alignment check only; original full 242D eH OPEN',
      'NF511_candidate_raw_SHA256':csha,
      'NF494_source_raw_SHA256':NF494,
      'NF505_source_raw_SHA256':NF505,
      'authentic_odd_sinh_pole_index':241,
      'mirrored_cell_index':4095,
      'independent_pole_Gram_sinh_series_terms':44,
      'native_source_EH_outward':[str(v) for v in E],
      'native_source_bHpole_outward':[str(v) for v in b],
      'native_source_CHpole_outward':[str(v) for v in C],
      'certified_pole_capture_fraction_lower':str(reported_fraction),
      'exact_source_pole_local_alignment_exceeds_96_percent':True,
      'independent_H400_U400_integrator_reimplementation':False,
      'complete_original_J242_local_energy_eH':'OPEN',
      'original_Weil_image_domain':'OPEN','W_ODD_NEG':'OPEN','RH':'OPEN'}
    Path(o.output).write_text(json.dumps(receipt,indent=2)+'\n')
    print('NF511 original-source independent SHA/Fraction pole-local receipt audit PASS')
    print('True original H4095 local W²:',float(E[0]),float(E[1]))
    print('True original H4095 best pole squared alignment >',float(reported_fraction))
    print('Original named full 242D local Schur/eH, Weil domain and RH OPEN')
if __name__=='__main__':main()
