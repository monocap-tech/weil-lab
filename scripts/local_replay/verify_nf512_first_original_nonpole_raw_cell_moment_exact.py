#!/usr/bin/env python3
"""NF512 genuine first nonpole selected raw local moment on original H4095.

Uses uniform ORIGINAL NF511 source-certified signed W(x) bounds on
mirrored H4095 and independent all-rational Machin pi plus alternating
arctan/sine Taylor bounds. This is one actual original raw mixed
moment, not the 242D D-correlated local source response or e_H.
"""
from __future__ import annotations
import argparse,json,hashlib,math,sys
from fractions import Fraction as F
from pathlib import Path
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
NF494='39cba367d70243c2d15e5a9323fc8097d58187923dcf0eca2b031136871f0181'
NF505='ad4afeaa4c7d8f48dfc270c437362287d8e2a21d9cce5b385c071e358431d2ec'
SRC='0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce'
SEAM='c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675'
BO=F(549,500);H=BO/4096;L=BO-H;R=BO;FREQ=F(37,64)

def read(p):
    b=Path(p).read_bytes()
    return json.loads(b),hashlib.sha256(b).hexdigest()
def alt_arctan(q,n=90):
    assert F(0)<q<1
    part=sum(((-1)**j*q**(2*j+1)/F(2*j+1) for j in range(n)),F(0))
    tail=q**(2*n+1)/F(2*n+1)
    # n even: partial is lower; n odd: partial is upper.
    return (part-tail,part) if n%2 else (part,part+tail)
def machin_pi():
    a=alt_arctan(F(1,5))
    b=alt_arctan(F(1,239))
    return 16*a[0]-4*b[1],16*a[1]-4*b[0]
def alt_sin(z,n=45):
    assert 0<z<1
    part=sum(((-1)**j*z**(2*j+1)/math.factorial(2*j+1) for j in range(n)),F(0))
    tail=z**(2*n+1)/math.factorial(2*n+1)
    return (part-tail,part) if n%2 else (part,part+tail)
def run(p,out):
    src,sh=read(p)
    style=src['pass']
    if style=='NF511-source-local-W-square-exact':
        assert src['source_original_NF407_sha256']==SRC
        assert src['source_original_NF406_sha256']==SEAM
        assert src['original_NF494_full_H400_U400_json_sha256']==NF494
        assert src['original_NF505_native_sha256']==NF505
        assert src['cell_index']==4095
        wl,wh=map(F,src['original_cell_full_W_pointwise_negative_interval'])
        Ehi=F(src['original_cell_full_W_sq_outward'][1])
    else:
        assert style=='NF511-original-source-exact-local-W-pole-panel'
        assert src['original_nf407_source_SHA256']==SRC
        assert src['original_nf406_seams_SHA256']==SEAM
        assert src['original_nf494_raw_SHA256']==NF494
        assert src['original_nf505_raw_SHA256']==NF505
        assert src['mirrored_cell_index']==4095
        wl,wh=map(F,src['local_W_pointwise_negative_outward'])
        Ehi=F(src['local_E_H_original_full_W_squared'][1])
    assert wl<wh<0 and Ehi>0
    pl,ph=machin_pi()
    assert 3<pl<ph<F(22,7)
    # Authentic original generator j0=sin(2*pi*(37/64)*x).
    # 2*pi*f*x=pi+u where 0<u<1 on entire H4095 positive side.
    # Thus j0(x)=-sin(u(x)), sin increases on u∈(0,1).
    ulo=pl*(2*FREQ*L-1)
    uhi=ph*(2*FREQ*R-1)
    assert 0<ulo<uhi<1
    sine_lower=alt_sin(ulo)[0]
    sine_upper=alt_sin(uhi)[1]
    assert 0<sine_lower<sine_upper<1
    # W and j0 are both odd and negative on the positive half;
    # W*j0 is strictly positive on BOTH reflected lobes.
    blo=2*H*(-wh)*sine_lower
    bhi=2*H*(-wl)*sine_upper
    assert 0<blo<bhi<F(1,10**12)
    # Original physical source Cauchy consistency, using the
    # rigorous geometric bound ||j0||_H²<=|H|=2h.
    assert blo**2<=Ehi*(2*H)
    # Expose a compact 70-decimal-place exact outward receipt, while
    # all original sine/Machin proof comparisons above use full Fractions.
    scale=10**70
    blo=F(blo.numerator*scale//blo.denominator,scale)
    bhi=F(-((-bhi.numerator*scale)//bhi.denominator),scale)
    assert 0<blo<bhi
    receipt={
      'pass':'NF512-source-exact-first-nonpole-local-moment',
      'NF511_source_local_receipt_sha256':sh,
      'NF511_source_local_receipt_schema':style,
      'NF494_source_sha256':NF494,'NF505_source_sha256':NF505,
      'NF407_original_source_sha256':SRC,'NF406_original_source_sha256':SEAM,
      'original_raw_selected_basis_index':0,
      'original_raw_selected_basis_node':['37/64',0],
      'source_generator':'sin(2*pi*(37/64)*x)',
      'genuine_original_physical_microcell_index':4095,
      'independent_exact_Machin_arctan_terms':90,
      'independent_exact_sine_Taylor_terms':45,
      'original_complete_W_certified_negative_on_cell':True,
      'original_nonpole_raw_source_W_mixed_moment_outward':[str(blo),str(bhi)],
      'original_nonpole_raw_source_W_mixed_moment_float_display':[float(blo),float(bhi)],
      'original_nonpole_raw_mixed_moment_strictly_positive':True,
      'source_moment_historical_D_frame_transported':False,
      'original_entire_242D_local_selected_column':'OPEN',
      'original_J242_globally_fitted_local_eH':'OPEN',
      'original_J242_local_selected_leverage_tauH':'OPEN',
      'Weil_multiplier_image_graph_domain':'OPEN','W_ODD_NEG':'OPEN','RH':'OPEN'}
    Path(out).write_text(json.dumps(receipt,indent=2)+'\n')
    print('NF512 actual original first NONPOLE local raw source moment EXACT FRACTION PASS')
    print('Original H4095 <j0,W> interval',float(blo),float(bhi))
    print('Historical D-frame correlated 242D local residual, source-domain and RH OPEN')
if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--nf511',required=True)
    p.add_argument('--output',required=True)
    a=p.parse_args()
    run(a.nf511,a.output)
