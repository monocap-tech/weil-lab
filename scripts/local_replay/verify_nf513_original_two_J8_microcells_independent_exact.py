#!/usr/bin/env python3
"""NF513 independent exact Fraction two-original-J8-cell source receipt audit.

Independently recomputes n=9 prime seam with 95-term rational atanh,
original sinh pole restricted H4094 Gram with distinct 44-term Taylor,
and audits both SHA-pinned original physical H4094/H4095 energy receipts.
Does NOT independently integrate all H400/U400 response source coefficients.
"""
from __future__ import annotations
import argparse,hashlib,json,math,sys
from pathlib import Path
from fractions import Fraction as F
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
NF494='39cba367d70243c2d15e5a9323fc8097d58187923dcf0eca2b031136871f0181'
NF505='ad4afeaa4c7d8f48dfc270c437362287d8e2a21d9cce5b385c071e358431d2ec'
SRC='0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce'
SEAM='c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675'
B=F(11,10);BO=F(549,500);h=BO/4096

def read(path):
    raw=Path(path).read_bytes()
    return json.loads(raw),hashlib.sha256(raw).hexdigest()
def iv(row):
    lo,hi=map(F,row)
    assert lo<=hi
    return lo,hi
def atanh(t,n=95):
    assert 0<=t<=F(1,3)
    val=sum((2*t**(2*k+1)/F(2*k+1) for k in range(n)),F(0))
    return val,val+2*t**(2*n+1)/((2*n+1)*(1-t*t))
def ln9():
    # Independent range reduction: log(9)=3log(2)+log(9/8).
    L2=atanh(F(1,3))
    L9=atanh(F(1,17))
    return 3*L2[0]+L9[0],3*L2[1]+L9[1]
def sinh_minus_x(x,n=44):
    assert 0<x<B
    val=sum((x**(2*k+1)/math.factorial(2*k+1) for k in range(1,n+1)),F(0))
    first=x**(2*n+3)/math.factorial(2*n+3)
    ratio=x*x/F((2*n+4)*(2*n+5))
    return val,val+first/(1-ratio)

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--nf513',required=True)
    p.add_argument('--nf511',required=True)
    p.add_argument('--nf494',required=True)
    p.add_argument('--nf505',required=True)
    p.add_argument('--output',required=True)
    o=p.parse_args()
    now,nowsha=read(o.nf513)
    prior,prsha=read(o.nf511)
    h,shH=read(o.nf494)
    n,shN=read(o.nf505)
    assert (shH,shN)==(NF494,NF505)
    assert now['pass']=='NF513-original-source-J8-H4094-local-W-pole-exact'
    assert now['NF494_SHA256']==NF494 and now['NF505_SHA256']==NF505
    assert now['NF511_H4095_receipt_SHA256']==prsha
    assert now['original_NF407_source_SHA256']==n['source_original_NF407_sha256']==SRC
    assert now['original_NF406_seams_SHA256']==n['source_original_NF406_sha256']==SEAM
    assert h['original_nf407_source_sha256']==SRC and h['original_nf406_seams_sha256']==SEAM
    assert n['pass']=='NF504-native' and h['pass']=='NF494-native'
    assert prior['pass'] in ('NF511-source-local-W-square-exact',
                             'NF511-original-source-exact-local-W-pole-panel')
    assert prior['cell_index' if 'cell_index' in prior else 'mirrored_cell_index']==4095
    assert now['selected_original_dimension']==242 and now['cell_index']==4094
    assert list(map(F,now['cell_positive_x']))==[BO-2*h,BO-h]
    assert list(map(F,now['cell_d']))==[B-BO+h,B-BO+2*h]
    assert now['analytic_source_400_jets_retained'] is True
    assert now['original_source_H400_high_order_85through399_paid'] is True
    assert now['original_source_U400_high_order_85through399_paid'] is True
    assert now['recentered_source_H400_HU_prefix_terms']==85
    assert now['recentered_jet_order']==30 and now['slabs']>=128
    Enew=iv(now['original_H4094_W_squared_outward'])
    bnew=iv(now['original_H4094_W_pole_cross_outward'])
    Cnew=iv(now['original_H4094_pole_Gram_outward'])
    wnew=iv(now['original_H4094_W_pointwise_negative_outward'])
    Eold=iv(prior['original_cell_full_W_sq_outward'] if 'original_cell_full_W_sq_outward' in prior
            else prior['local_E_H_original_full_W_squared'])
    bold=iv(prior['original_cell_complete_W_cross_authentic_sinh_pole_outward']
            if 'original_cell_complete_W_cross_authentic_sinh_pole_outward' in prior
            else prior['local_b_H_original_sinh_pole_cross'])
    assert 0<Enew[0]<Enew[1]<Eold[0]<Eold[1]
    assert wnew[1]<0 and bnew[1]<0
    assert abs(bnew[0])<abs(bold[1])
    # Independent physical original selected sinh-pole Gram.
    right=sinh_minus_x(BO-h)
    left=sinh_minus_x(BO-2*h)
    Cind=right[0]-left[1],right[1]-left[0]
    assert max(Cind[0],Cnew[0])<=min(Cind[1],Cnew[1])
    assert bnew[0]**2<=Enew[1]*Cnew[1]
    pole_floor=F(now['original_H4094_best_pole_alignment_lower'])
    assert 0<pole_floor<=bnew[1]**2/(Cnew[1]*Enew[1])
    assert pole_floor>F(95,100)
    # Independent source seam: H4094 valid whole n9 branch, H4093 split.
    l9,u9=ln9()
    seam=(2*B-u9,2*B-l9)
    assert B-BO+2*h<seam[0]<seam[1]<B-BO+3*h
    assert list(map(F,now['exact_source_n9_seam_d_interval']))[0]<=seam[1]
    assert now['H4094_no_prime_seam'] and now['H4093_crosses_n9_prime_seam']
    assert iv(now['coarse16_W_squared_outward'])[0]<=Enew[0]
    assert Enew[1]<=iv(now['coarse16_W_squared_outward'])[1]
    # Independent exact source analytic Cauchy check, no floating gate.
    dmax=B-BO+2*h
    rho=dmax/F(1,25)
    CH=F(10)**420*rho**400/(1-rho)
    CU=F(10)**400*rho**400/(1-rho)
    assert CH<=F(now['holomorphic_H400_cauchy_upper'])<F(1,10**55)
    assert CU<=F(now['holomorphic_U400_cauchy_upper'])<F(1,10**75)
    ratio=(Enew[0]/Eold[1],Enew[1]/Eold[0])
    assert ratio[0]>F(55,100) and ratio[1]<F(60,100)
    result={
      'pass':'NF513-independent-exact-two-real-n9-microcells',
      'standing':'Independent source SHA, original second cell pole Gram and n9 seam, 2-cell strict W2 ratio. Not independent original H400/U400 re-integration or 242D fitted residual.',
      'source_NF494_SHA256':shH,'source_NF505_SHA256':shN,
      'source_NF511_H4095_SHA256':prsha,'source_NF513_H4094_SHA256':nowsha,
      'source_nf407_sha256':SRC,'source_nf406_seams_sha256':SEAM,
      'two_original_whole_n9_active_cells':[4094,4095],
      'adjacent_n9_seam_crossing_cell':4093,
      'original_H4094_W2_outward':list(map(str,Enew)),
      'original_H4095_W2_outward':list(map(str,Eold)),
      'original_H4094_W2_strictly_less_than_H4095':True,
      'original_H4094_to_H4095_W2_ratio_outward':list(map(str,ratio)),
      'original_two_cell_combined_W2_outward':[
          str(Enew[0]+Eold[0]),str(Enew[1]+Eold[1])],
      'H4094_original_sinh_pole_best_local_squared_capture_lower':str(pole_floor),
      'independent_44term_original_sinh_pole_H4094_Gram_checked':True,
      'independent_95term_original_n9_seam_checked':True,
      'genuine_original_J242_fitted_eH':'OPEN',
      'original_Weil_source_image_domain':'OPEN','W_ODD_NEG':'OPEN','RH':'OPEN'
    }
    Path(o.output).write_text(json.dumps(result,indent=2)+'\n')
    print('NF513 source-custody original two-cell independent Fraction audit PASS')
    print('H4094/H4095 true source W squared ratio',float(ratio[0]),float(ratio[1]))
    print('H4093 crosses original n9 seam; J242 fitted local energy / RH OPEN')

if __name__=='__main__':
    main()
