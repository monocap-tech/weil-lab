#!/usr/bin/env python3
"""NF522 independent exact Fraction acceptance of original finite physical NO-GO.

Cross-authenticates NF494,NF505,NF518, full 242 historical frame candidate,
all 242 raw physical beta_i (recomputed exactly), two true source-local
complete globally fitted eH receipt/error payments, and three NF520
original 242D Fredholm gap proof receipts. Proves original NF404 finite
physical sufficient-gate NO-GO, NOT original Weil signed positivity or RH.

This is an independent algebraic/source-custody audit, not an independent
re-integration of original NF494 H400/U400 or NF520 Gram sources.
"""
from __future__ import annotations
import argparse,hashlib,json,sys
from fractions import Fraction as F
from pathlib import Path
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
NF494='39cba367d70243c2d15e5a9323fc8097d58187923dcf0eca2b031136871f0181'
NF505='ad4afeaa4c7d8f48dfc270c437362287d8e2a21d9cce5b385c071e358431d2ec'
NF518='926f8d00d28212f542351760e0c1d814413e8a36a3367d6a58bf837c53865438'
FRAME='18ac01bba4de7ec432e419db5ed990fbfabad91c10cbcf2f61cf5666e36b430e'
BO=F(549,500)
def read(p):
    raw=Path(p).read_bytes()
    return json.loads(raw),hashlib.sha256(raw).hexdigest()
def main():
    p=argparse.ArgumentParser()
    for k in ('nf494','nf505','nf518','frame','beta','energy',
              'gap4094','gap4095','gapunion','output'):
        p.add_argument('--'+k,required=True)
    a=p.parse_args()
    old,os=read(a.nf505);source,hs=read(a.nf494)
    fit,fs=read(a.nf518);frame,ds=read(a.frame)
    beta,bs=read(a.beta);energy,es=read(a.energy)
    assert (os,hs,fs)==(NF505,NF494,NF518)
    assert old['pass']=='NF504-native' and source['pass']=='NF494-native'
    assert old['original_selected_J_dimension']==242
    assert old['original_original_D_frame_SHA256']==FRAME
    assert fit['original_exact_historical_D_frame_SHA256']==FRAME
    assert frame.get('source_certified_historical_D_prefix_columns',
                     frame.get('historic_D_certified_first_columns'))==242
    assert frame.get('remaining_historical_D_columns_open',
                     frame.get('historic_D_remaining_columns_unrecovered'))==0
    assert beta['pass']=='NF522-original-242D-raw-physical-beta-source-exact'
    assert beta['original_NF522_full_frame_sha256']==ds
    assert energy['pass']=='NF522-original-source-certified-full242D-named-local-residual-energy'
    assert energy['source_original_nf494_SHA256']==hs
    assert energy['source_original_nf505_SHA256']==os
    assert energy['source_original_full242D_physical_beta_SHA256']==bs
    assert beta['original_original_basis_nodes']==old['original_source_basis_nodes']
    C=frame.get('untrusted_candidate_integer_upper_triangular_rows',
                frame.get('firstN_rational_trial_matrix_integer_upper_rows'))
    denC=int(frame.get('untrusted_candidate_denominator',
                       frame.get('firstN_rational_trial_matrix_integer_denominator')))
    v=list(map(int,fit['original_selected_D_frame_coefficients_exact_rational_candidates_numerators']))
    denA=int(fit['original_selected_D_frame_coefficients_exact_rational_denominator'])
    den=int(beta['original_raw_physical_beta_denominator'])
    assert len(C)==len(v)==242 and denC==10**420 and denA==10**105 and den==10**210
    assert len(beta['original_raw_physical_beta_numerators'])==242
    weights=[BO**int(k) if f!='pole' else F(3,5)
             for f,k in old['original_source_basis_nodes']]
    assert sum(weights,F(0))<293
    err=F(frame.get('exact_historical_D_prefix_max_row_error_upper',
                    frame.get('historic_original_D_firstN_prefix_max_row_error_upper')))
    assert 0<err<F(1,10**14)
    weighted=err*F(max(map(abs,v)),denA)*sum(weights,F(0))+sum(weights,F(0))/den
    assert weighted==F(beta['source_original_weighted_beta_error_upper'])
    assert weighted<F(1,10**19)
    for i,row in enumerate(C):
        assert len(row)==242
        assert all(int(row[j])==0 for j in range(i))
        z=sum(int(row[j])*v[j] for j in range(i,242))
        assert str(z)==beta['source_raw_original_C_times_a_exact_numerators'][i]
        assert (z*den)//(denC*denA)==int(beta['original_raw_physical_beta_numerators'][i])
    H=BO/4096
    cells={}
    for z in energy['true_original_two_cells']:
        cell=z['cell'];assert cell in (4094,4095) and cell not in cells
        lo,hi=map(F,z['original_full242D_source_r2_outward'])
        assert 0<lo<=hi<F(1,10**27)
        tail=F(z['source_total_local_function_error'])
        env=F(z['source_local_r_polynomial_abssum'])
        fee=F(z['source_local_polynomial_sq_error_fee'])
        assert fee>=2*H*(2*env*tail+tail**2)
        assert 0<tail<F(1,10**29)
        assert F(z['physical_p160_analytic_tail'])<F(1,10**100)
        assert F(z['source_correlated_p_over44_tail'])<F(1,10**14)
        assert 0<F(z['source_global_fit_and_frame_error_fee'])<F(2,10**93)
        cells[cell]=(lo,hi)
    assert sorted(cells)==[4094,4095]
    union=(sum(cells[k][0] for k in cells),
           sum(cells[k][1] for k in cells))
    assert union==tuple(map(F,energy['original_two_cell_union_eD_outward']))
    assert union[1]<F(3,10**27)
    Rlo=F(old['original_original_saturated_exterior_residual_outward'][0])
    gamma=F(old['original_original_gamma_squared'])
    assert Rlo>gamma>0
    checks=(('H4094',a.gap4094,F(2,5),cells[4094][1]),
            ('H4095',a.gap4095,F(1,1000),cells[4095][1]),
            ('union',a.gapunion,F(1,20000),union[1]))
    result=[]
    for name,path,gap,eupper in checks:
        gate,gs=read(path)
        assert gate['pass']=='NF520-original-source-complete-242D-Fredholm-gap-exact'
        assert gate['original_nf505_source_SHA256']==os
        assert gate['original_selected_dimension']==242
        assert gate['case']==name
        assert F(gate['strict_original_selected_Fredholm_gap_lower'])==gap
        d=F(gate['exact_Gershgorin_center_deficit_upper'])
        e=F(gate['exact_Gershgorin_source_interval_error_upper'])
        assert d+e<1
        assert 1-d-e==F(gate['exact_Gershgorin_remaining_positive_margin'])
        lower=Rlo-eupper/gap
        assert lower>gamma
        result.append({'original_physical_support_addition':name,
          'full_original_242D_true_e_upper':str(eupper),
          'full_original_242D_kernel_gap_certified_strict_lower':str(gap),
          'original_NF520_Fredholm_source_proof_SHA256':gs,
          'original_NF404_support_refit_gain_strict_upper':str(eupper/gap),
          'original_surviving_exterior_physical_residual_strict_lower':str(lower),
          'original_unmodified_NF404_gamma_squared':str(gamma),
          'named_finite_selected_original_NF404_physical_sufficient_gate':'CERTIFIED_NO_GO'})
    out={
      'pass':'NF522-independent-original-source-242D-physical-local-NF404-exact-audit',
      'original_nf505_source_SHA256':os,
      'original_nf494_source_SHA256':hs,
      'original_nf518_Galerkin_SHA256':fs,
      'original_nf522_historical_frame_SHA256':ds,
      'original_nf522_source_physical_beta_SHA256':bs,
      'original_nf522_local_energy_SHA256':es,
      'independently_verified_raw_beta_integer_rows':242,
      'original_source_certified_three_named_finite_selected_physical_NO_GO':result,
      'independent_NF494_source_analytic_reintegration':False,
      'Weil_multiplier_source_image_graph_domain':'OPEN',
      'W_ODD_NEG':'OPEN','RH':'OPEN'}
    Path(a.output).write_text(json.dumps(out,indent=2)+'\n')
    print('NF522 ORIGINAL full J242, all THREE finite selected physical NO-GO source-exact audit PASS')
    print('No Weil source image/domain, signed form or RH promotion')
if __name__=='__main__':main()
