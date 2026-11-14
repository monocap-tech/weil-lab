#!/usr/bin/env python3
"""NF513 source-exact ORIGINAL projection power + measured local W² yields
quantitative LEVERAGE-ONLY CONDITIONAL named-cell NF404 support no-gos.

The true original complete selected J242 leverage tau_H is still UNKNOWN.
This script does not assert a patch no-go unless that condition is met.
"""
from __future__ import annotations
import argparse,hashlib,json,sys
from pathlib import Path
from fractions import Fraction as F
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
NF505='ad4afeaa4c7d8f48dfc270c437362287d8e2a21d9cce5b385c071e358431d2ec'
NF494='39cba367d70243c2d15e5a9323fc8097d58187923dcf0eca2b031136871f0181'

def read(p):
    raw=Path(p).read_bytes()
    return json.loads(raw),hashlib.sha256(raw).hexdigest()

def screen(E,P,R,gamma,t):
    # Strict exact-Fraction test for
    # (sqrt(E)+sqrt(t*P))² < (1-t)*(R-gamma)
    # without rounded radicals. Requires both a positive margin and
    # margin²>4*t*E*P.
    delta=R-gamma
    assert 0<E and 0<P and 0<gamma<R and 0<t<1
    margin=(1-t)*delta-E-t*P
    surplus=margin*margin-4*t*E*P
    assert margin>0 and surplus>0
    return {'t':str(t),'strict_rational_margin':str(margin),
            'strict_rational_square_surplus':str(surplus),
            'rational_square_comparison_ratio_float':
                float(margin*margin/(4*t*E*P))}

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--nf505',required=True)
    p.add_argument('--nf511',required=True)
    p.add_argument('--nf513',required=True)
    p.add_argument('--output',required=True)
    a=p.parse_args()
    old,old_sha=read(a.nf505)
    prior,prior_sha=read(a.nf511)
    cell,cell_sha=read(a.nf513)
    assert old_sha==NF505 and old['pass']=='NF504-native'
    assert cell['pass']=='NF513-original-source-J8-H4094-local-W-pole-exact'
    assert cell['NF505_SHA256']==old_sha
    assert cell['NF511_H4095_receipt_SHA256']==prior_sha
    assert cell['NF494_SHA256']==NF494
    assert old['source_original_NF407_sha256']==cell['original_NF407_source_SHA256']
    assert old['source_original_NF406_sha256']==cell['original_NF406_seams_SHA256']
    assert old['original_selected_J_dimension']==242
    assert old['original_support_saturated_physical_Hilbert_gate']=='CERTIFIED_PHYSICAL_SUPPORT_NO_GO'
    assert prior['pass'] in (
        'NF511-source-local-W-square-exact',
        'NF511-original-source-exact-local-W-pole-panel')
    P=F(old['original_original_W_exterior_selected_projection_power_outward'][1])
    R=F(old['original_original_saturated_exterior_residual_outward'][0])
    gamma=F(old['original_original_gamma_squared'])
    E4094=F(cell['original_H4094_W_squared_outward'][1])
    E4095=F(prior['original_cell_full_W_sq_outward'][1]
          if 'original_cell_full_W_sq_outward' in prior
          else prior['local_E_H_original_full_W_squared'][1])
    assert 0<E4094<E4095<R
    cases={
      'H4094':(E4094,F(13,100)),
      'H4095':(E4095,F(3,25)),
      'H4094_union_H4095':(E4094+E4095,F(1,10))
    }
    certs={name:screen(E,P,R,gamma,t)
           for name,(E,t) in cases.items()}
    result={
      'pass':'NF513-original-source-conditional-leverage-only-screen',
      'standing':'SOURCE-EXACT CONDITIONAL named support no-gos if original complete tau_D upper <= stated bounds. The actual tau_D is not measured; no unconditional patch decision.',
      'original_nf505_raw_SHA256':old_sha,
      'original_nf511_H4095_receipt_SHA256':prior_sha,
      'original_nf513_H4094_receipt_SHA256':cell_sha,
      'original_original_selected_dimension':242,
      'original_exterior_J_projection_power_upper':str(P),
      'original_exterior_squared_residual_lower':str(R),
      'original_fixed_NF404_gamma_squared':str(gamma),
      'original_H4094_W_squared_upper':str(E4094),
      'original_H4095_W_squared_upper':str(E4095),
      'original_two_cells_W_squared_upper':str(E4094+E4095),
      'exact_original_source_conditional_local_no_go_leverage_thresholds':certs,
      'required_true_selected_242D_leverage_upper_inputs':'OPEN',
      'no_individual_support_no_go_certified_without_tau':True,
      'original_global_242D_local_fitted_eH_computed':False,
      'Weil_source_image_graph_domain':'OPEN','W_ODD_NEG':'OPEN','RH':'OPEN'
    }
    Path(a.output).write_text(json.dumps(result,indent=2)+'\n')
    print('NF513 source-exact leverage-only conditional physical no-go PASS')
    print('tau_H4094 <= 0.13 => unchanged original NF404 patch NO-GO')
    print('tau_H4095 <= 0.12 => unchanged original NF404 patch NO-GO')
    print('tau_union <= 0.10 => unchanged original NF404 two-patch NO-GO')
    print('True original selected local tau remains OPEN, so no named no-go accepted yet.')
if __name__=='__main__':main()
