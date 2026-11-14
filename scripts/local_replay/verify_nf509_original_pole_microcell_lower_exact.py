#!/usr/bin/env python3
"""NF509 actual original sinh-pole microcell leverage lower, exact Fraction.

Computes genuine source-specific lower bounds for each sampled true J242
leverage, NOT the complete 242D leverage or local W residual energy e_j.
"""
from __future__ import annotations
import argparse,hashlib,json,math
from fractions import Fraction as F
from pathlib import Path

SRC='0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce'
SEAM='c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675'
NATIVE='ad4afeaa4c7d8f48dfc270c437362287d8e2a21d9cce5b385c071e358431d2ec'
B=F(549,500);M=4096
SAMPLES=(0,1,15,63,255,511,1023,2047,3071,3583,4031,4094,4095)
TERMS=33

def read(path):
    raw=Path(path).read_bytes()
    return json.loads(raw),hashlib.sha256(raw).hexdigest()

def sinh_minus_x_bounds(x):
    # Positive power series S(x)=sinh(x)-x for 0<=x<=B.
    # The tail after k=TERMS is bounded by geometric ratio
    # x^2/((2*TERMS+4)*(2*TERMS+5)).
    assert F(0)<=x<=B
    lo=sum((x**(2*k+1)/math.factorial(2*k+1)
            for k in range(1,TERMS+1)),F(0))
    first=x**(2*TERMS+3)/math.factorial(2*TERMS+3)
    ratio=x*x/F((2*TERMS+4)*(2*TERMS+5))
    assert ratio<1
    return lo,lo+first/(1-ratio)

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--native',required=True)
    p.add_argument('--output',required=True)
    o=p.parse_args()
    n,sha=read(o.native)
    assert sha==NATIVE and n['pass']=='NF504-native'
    assert n['source_original_NF407_sha256']==SRC
    assert n['source_original_NF406_sha256']==SEAM
    assert n['original_source_basis_nodes'][241]==['pole',None]
    assert n['original_selected_J_dimension']==242
    assert n['original_exterior_center_radius']==str(B)
    assert n['original_support_saturated_physical_Hilbert_gate']=='CERTIFIED_PHYSICAL_SUPPORT_NO_GO'
    # Original pole s(x)=sinh(x/2):
    # ||s||^2_{[-B,B]} = sinh(B)-B.
    denlo,denhi=sinh_minus_x_bounds(B)
    assert 0<denlo<=denhi
    h=B/M
    rows=[];prev=None
    for j in SAMPLES:
        a,b=j*h,(j+1)*h
        alo,ahi=sinh_minus_x_bounds(a)
        blo,bhi=sinh_minus_x_bounds(b)
        numlo,numhi=blo-ahi,bhi-alo
        assert 0<numlo<=numhi
        lower,upper=numlo/denhi,numhi/denlo
        assert F(0)<lower<=upper<F(1)
        if prev is not None:
            assert prev['upper']<lower, (
                'METHOD STOP original pole local leverage not spatially increasing')
        prev={'upper':upper}
        rows.append({
           'j':j,'pair_half_left':str(a),'pair_half_right':str(b),
           'genuine_original_pole_partial_leverage_lower':str(lower),
           'genuine_original_pole_partial_leverage_upper':str(upper),
           'pole_partial_leverage_lower_approx':format(float(lower),'.16g'),
           'pole_partial_leverage_upper_approx':format(float(upper),'.16g'),
           'full_original_J242_leverage_lower_via_pole':str(lower),
           'full_original_J242_leverage_upper':'UNKNOWN'})
    assert sum((F(z['genuine_original_pole_partial_leverage_upper'])
                for z in rows),F(0))<1
    out={
      'pass':'NF509-genuine-original-pole-local-leverage-exact',
      'scope':'SOURCE-CERTIFIED EXACT RATIONAL LOWER bound on true 242D leverage from authentic sinh pole only; full J242 leverage and W residual energy e_j OPEN',
      'original_nf505_native_sha256':sha,'original_nf407_source_sha256':SRC,
      'original_nf406_seam_sha256':SEAM,'selected_rank':242,
      'authentic_pole_index':241,'original_exterior_radius':str(B),
      'original_pole_norm_squared_outward':[str(denlo),str(denhi)],
      'mirror_pair_count':M,'half_pair_width':str(h),
      'sinh_minus_x_rational_terms':TERMS,
      'sampled_original_microcell_pole_leverage':rows,
      'strict_sampled_positive_pole_contribution_monotone_in_j':True,
      'original_full_242D_microcell_leverage_computed':False,
      'original_W_local_energy_computed':False,
      'individual_NF404_patch_verdict':'OPEN',
      'Weil_source_image_graph_domain':'OPEN',
      'W_ODD_NEG':'OPEN','RH':'OPEN'}
    Path(o.output).write_text(json.dumps(out,indent=2)+'\n')
    print('NF509 actual original sinh pole physical microcell lower enclosures SOURCE-EXACT PASS')
    for z in rows:
        print('H',z['j'],'pole floor full tau_j >=',
              z['pole_partial_leverage_lower_approx'])
    print('No original full 242D tau_j upper or response-energy e_j certified')

if __name__=='__main__':
    main()
