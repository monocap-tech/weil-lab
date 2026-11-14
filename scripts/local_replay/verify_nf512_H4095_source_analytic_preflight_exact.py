#!/usr/bin/env python3
"""NF512 source-authentic EXACT Fraction preliminary analytic remainder gate.

Actually reads and SHA-checks original NF494 H400/U400 4096bit intervals
and NF505 original physical source. Proves the 240-jet local re-expansion
and true source Cauchy/log tails on H4095 are tiny. It does NOT evaluate
the original globally fitted J242 residual e_H, its leverage tau_H or RH.
"""
from __future__ import annotations
import json,hashlib,math,sys,argparse
from fractions import Fraction as F
from pathlib import Path
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
H_SHA='39cba367d70243c2d15e5a9323fc8097d58187923dcf0eca2b031136871f0181'
N_SHA='ad4afeaa4c7d8f48dfc270c437362287d8e2a21d9cce5b385c071e358431d2ec'
B=F(11,10);BO=F(549,500);h=BO/4096;half=h/2;dmax=B-BO+h;d0=dmax-half
R=F(1,25);K=240
def read(p):
    raw=Path(p).read_bytes()
    return json.loads(raw),hashlib.sha256(raw).hexdigest()
def mag(pair):
    a,b=map(F,pair)
    assert a<=b
    return max(abs(a),abs(b))
def shift_tail(co):
    # All omitted terms in shifting complete ORIGINAL 400-series to d0.
    # Identity: binom(n,j)<=binom(n,K+1)binom(n-K-1,j-K-1)
    # for j>=K+1; tmax=half and d0+tmax=dmax.
    return sum((mag(co[n])*math.comb(n,K+1)*half**(K+1)*dmax**(n-K-1)
                for n in range(K+1,400)),F(0))
def full_norm(co):
    return sum((mag(v)*dmax**n for n,v in enumerate(co)),F(0))
def upper_str(x,decimal_digits=100):
    q=10**decimal_digits
    return str(F(-((-x.numerator*q)//x.denominator),q))
def run(hpath,npath,out):
    h,hs=read(hpath);n,ns=read(npath)
    assert (hs,ns)==(H_SHA,N_SHA)
    assert h['pass']=='NF494-native' and n['pass']=='NF504-native'
    assert h['original_nf407_source_sha256']==n['source_original_NF407_sha256']
    assert h['original_nf406_seams_sha256']==n['source_original_NF406_sha256']
    assert n['original_selected_J_dimension']==242
    assert h['original_source_400_jet_order']==400
    assert 0<dmax<R and 0<half/d0<F(1,10)
    H=h['original_H_400_native_outward']
    U=h['original_U_400_native_outward']
    ht,ut=shift_tail(H),shift_tail(U)
    ch=F(10)**420*(dmax/R)**400/(1-dmax/R)
    cu=F(10)**400*(dmax/R)**400/(1-dmax/R)
    rho=half/d0
    logtail=rho**(K+1)/((K+1)*(1-rho))
    assert 0<ht<F(1,10**60) and 0<ut<F(1,10**60)
    assert 0<ch<F(1,10**75) and 0<cu<F(1,10**95)
    assert 0<logtail<F(1,10**250)
    assert full_norm(U)*logtail<F(1,10**50)
    generator_unit_tail=F(3)*B**13/math.factorial(K-13+1)
    assert generator_unit_tail*10**200<F(1,10**40)
    data={
      'pass':'NF512-original-source-exact-preflight',
      'NF494_original_SHA256':hs,'NF505_original_SHA256':ns,
      'old_selected_dimension':242,'original_true_cell_index':4095,
      'physical_half_cell_width':str(half),'exact_d_midpoint':str(d0),
      'exact_d_max':str(dmax),'source_analytic_radius':str(R),
      'source_local_selected_Taylor_order':K,
      'original_H400_shift_tail_lt_1e_minus_60':True,
      'original_U400_shift_tail_lt_1e_minus_60':True,
      'original_H_holomorphic_tail_lt_1e_minus_75':True,
      'original_U_holomorphic_tail_lt_1e_minus_95':True,
      'original_log_series_tail_lt_1e_minus_250':True,
      'original_U_absolute_polynomial_norm_times_logtail_lt_1e_minus_50':True,
      'per_unit_raw_beta_generator_tail_times_1e200_lt_1e_minus_40':True,
      'raw_beta_l1_at_most_1e200_verified':False,
      'true_242D_local_residual_eH':'OPEN',
      'true_242D_cell_selected_leverage_tau':'OPEN',
      'Weil_multiplier_source_image_graph_domain':'OPEN','W_ODD_NEG':'OPEN','RH':'OPEN',
      'bounded_outward_decimal':{
        'H_shift':upper_str(ht,450),'U_shift':upper_str(ut,450),
        'H_cauchy':upper_str(ch,90),'U_cauchy':upper_str(cu,110),
        'log_tail':upper_str(logtail,310),
        'phase_generator_unit_tail':upper_str(generator_unit_tail,500)}
    }
    Path(out).write_text(json.dumps(data,indent=2)+'\n')
    print('NF512 authentic original NF494 H400/U400 EXACT Fraction local remainder preflight PASS')
    print('Original true locally fitted 242D eH/tau and Weil source-domain/RH still OPEN')
if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--nf494',required=True)
    p.add_argument('--nf505',required=True)
    p.add_argument('--output',required=True)
    a=p.parse_args()
    run(a.nf494,a.nf505,a.output)
