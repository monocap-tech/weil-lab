#!/usr/bin/env python3
"""NF520 independent exact Fraction audit of THREE accepted original J242 gaps.

Audits source SHA, actual NF517 spectral thresholds, genuine physical
endpoints, exact Gershgorin deficits and source uncertainty payments.
This is a receipt audit, NOT independent original Gram reintegration.
"""
import argparse,hashlib,json,sys
from fractions import Fraction as F
from pathlib import Path
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
SHA='ad4afeaa4c7d8f48dfc270c437362287d8e2a21d9cce5b385c071e358431d2ec'
BO=F(549,500)
def read(p):
    raw=Path(p).read_bytes()
    return json.loads(raw),hashlib.sha256(raw).hexdigest()
def main():
    p=argparse.ArgumentParser()
    p.add_argument('--nf505',required=True)
    p.add_argument('--workdir',required=True)
    p.add_argument('--output',required=True)
    a=p.parse_args();old,sha=read(a.nf505)
    assert sha==SHA and old['pass']=='NF504-native'
    assert old['original_selected_J_dimension']==242
    assert old['original_original_D_frame_SHA256']=='18ac01bba4de7ec432e419db5ed990fbfabad91c10cbcf2f61cf5666e36b430e'
    root=Path(a.workdir)
    cust,ch=read(root/'nf520_original_gram_custody.json')
    assert cust['nf505_raw_sha256']==sha
    assert cust['old_full_selected_dimension']==242
    assert cust['scale']==str(10**420)
    assert [F(cust['Gram'][str(i)]['true_positive_endpoint'])
            for i in range(3)]==[BO-F(i)*BO/4096 for i in range(3)]
    targets={'H4094':F(2,5),'H4095':F(1,1000),'union':F(1,20000)}
    records=[]
    for case,g in targets.items():
        row,rh=read(root/f'gap_cert_{case}.json')
        assert row['case']==case
        assert row['pass']=='NF520-original-source-complete-242D-Fredholm-gap-exact'
        assert row['original_nf505_source_SHA256']==sha
        assert row['original_source_gram_custody_SHA256']==ch
        assert F(row['strict_original_selected_Fredholm_gap_lower'])==g
        assert row['original_selected_dimension']==242
        d=F(row['exact_Gershgorin_center_deficit_upper'])
        e=F(row['exact_Gershgorin_source_interval_error_upper'])
        margin=F(row['exact_Gershgorin_remaining_positive_margin'])
        assert 0<d<F(2,1000) and 0<e<F(5,10**102)
        assert margin>F(99,100) and d+e+margin==1
        assert row['original_full_242D_global_fit_local_residual_eD']=='OPEN'
        assert row['original_unconditional_NF404_named_patch']=='OPEN'
        records.append({'case':case,
           'source_original_gap_strict_lower':str(g),
           'Gershgorin_total_upper':str(d+e),
           'positive_margin':str(margin),
           'original_exact_source_certificate_SHA256':rh})
    R=F(old['original_original_saturated_exterior_residual_outward'][0])
    gamma=F(old['original_original_gamma_squared'])
    assert R>gamma
    for case,energy_upper in (('H4094',F(1,10**27)),
                              ('H4095',F(1,10**27)),
                              ('union',F(3,10**27))):
        assert R-energy_upper/targets[case]>gamma
    out={'pass':'NF520-independent-original-three-gap-exact-Fraction-receipt-audit',
      'original_NF505_native_sha256':sha,
      'original_source_interval_Gram_custody_sha256':ch,
      'original_full_selected_dimension':242,
      'original_certified_three_Fredholm_gap_records':records,
      'original_NF517_IF_energy_upper_THEN_NF404_NO_GO_rational_implication':True,
      'independent_complete_source_Gram_reintegration':False,
      'actual_complete_original_local_eD_certified':False,
      'unconditional_original_NF404_named_patch':'OPEN',
      'Weil_multiplier_image_graph_domain':'OPEN','W_ODD_NEG':'OPEN','RH':'OPEN'}
    Path(a.output).write_text(json.dumps(out,indent=2)+'\n')
    print('NF520 independent original-source three-gap exact Fraction audit PASS')
    print('Original local eD, unconditional NF404 support and RH OPEN')
if __name__=='__main__':main()
