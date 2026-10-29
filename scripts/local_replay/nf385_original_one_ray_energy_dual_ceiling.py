#!/usr/bin/env python3
"""NF385 exact original n512 one-ray energy-dual ceiling.

Uses original NF380 signed and physical native interval; no new kernel,
no original n513 pairing, no unobserved full inverse or RH conclusion.
"""
import argparse
import hashlib
import json
import sys
from fractions import Fraction as F
from pathlib import Path
sys.set_int_max_str_digits(0)

ORIGINAL_N512_SHA='9d4b07fb2ca42c14ed995ddcd69811201eacb6f13f9f795a70c4b64889e9f83b'
MU=F(49,50000)   # original exterior positive signed form floor
D4=F(49,10**23)  # NF370 exact fourth dyadic form-dual budget
D=F(2401,2*10**28) # NF370 1/4 mu D4 strong-residual budget
SHARE_LO=F(145133,10**6)
SHARE_HI=F(145134,10**6)
ENERGY_CEILING=F(362835,10**7)
COMPLEMENT_NECESSARY=F(9637165,10**7)

def load(path):
    raw=Path(path).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==ORIGINAL_N512_SHA, 'original n512 native SHA mismatched'
    j=json.loads(raw)
    assert j['unfitted_n']==512 and j['selected_rank']==242 and j['critical_count']==4
    assert j['original_physical_16_Gram_overlaps'] is True
    assert j['original_signed_32_CE_BP_overlaps'] is True
    assert j['original_WJJ_WJF_archived_cells_reused']==30371
    assert j['original_lowband_integral_computed'] is False
    assert j['entire_exterior_inverse_computed'] is False
    assert j['W_ODD_NEG']==j['RH']=='OPEN'
    assert F(j['original_direction_four_squared_residual_budget'])==D
    return j

def run(p,output=None):
    j=load(p)
    assert D==MU*D4/4
    g0,g1=map(F,j['outside_E4_norm2_interval'])
    b0,b1=map(F,j['complete_original_signed_u4_qperp_interval'])
    assert F(0)<g0<=g1<F(11,10) and F(0)<b0<=b1
    r0=b0*b0/(g1*D)
    r1=b1*b1/(g0*D)
    assert SHARE_LO<r0<=r1<SHARE_HI
    # For actual exterior energy c(q,q)>=MU*g and b=Wodd(u4,q),
    # one-dimensional c-dual component is b^2/c(q,q) <= b^2/(MU*g).
    one_ray_max_energy=b1*b1/(MU*g0)
    one_ray_max_ratio=one_ray_max_energy/D4
    assert one_ray_max_ratio==r1/4
    assert 0<one_ray_max_ratio<ENERGY_CEILING<F(1,25)
    assert F(1)-ENERGY_CEILING==COMPLEMENT_NECESSARY
    out=dict(
      standing='NF385 ORIGINAL N512 ONE-RAY FORM-DUAL METHOD STOP; INFINITE COMPLEMENT OPEN',
      original_native_n512_sha256=ORIGINAL_N512_SHA,
      certified_exterior_form_floor=str(MU),
      fourth_original_nf370_dyadic_form_dual_budget=str(D4),
      original_nf370_fourth_strong_squared_budget=str(D),
      strong_budget_identity='D = MU*D4/4 EXACT',
      original_n512_strong_dual_squared_share_strictly_gt=str(SHARE_LO),
      original_n512_strong_dual_squared_share_strictly_lt=str(SHARE_HI),
      original_n512_energy_dual_ray_fraction_of_D4_strictly_lt=str(ENERGY_CEILING),
      necessary_unseen_c_orthogonal_energy_if_total_at_least_D4_strictly_gt_fraction=str(COMPLEMENT_NECESSARY),
      original_c_q_q_computed=False,
      original_entire_exterior_form_inverse_computed=False,
      source_domain_and_form_dual_attachment='INHERITED/OPEN',
      original_n513_signed_measurement=False,
      full_four_direction_form_dual_upper=False,
      actual_W_ODD_NEG='OPEN',W_ODD_NEG='OPEN',RH='OPEN')
    if output:
        dest=Path(output);dest.parent.mkdir(parents=True,exist_ok=True)
        dest.write_text(json.dumps(out,indent=2)+'\n')
    print('NF385 PASS original SHA-pinned Fraction: one-ray form-dual <',ENERGY_CEILING,'* d4')
    print('If original direction-4 full form-dual >= d4, unseen c-orthogonal energy >',COMPLEMENT_NECESSARY,'* d4')
    print('This is a METHOD STOP for single q512 as an energy-dual obstruction; full W-ODD-NEG/RH OPEN')
    return out

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--original-512',required=True)
    parser.add_argument('--output')
    args=parser.parse_args()
    run(args.original_512,args.output)
