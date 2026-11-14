#!/usr/bin/env python3
"""NF517 exact SHA-pinned ORIGINAL source spectral-gap conditional NF404 gates.

A validated e_D bound and validated 1-lambda_max(K_D) bound would imply
named physical support NO-GO. Neither is asserted source interval-certified
here: 550-digit mpmath/Nystrom evidence is UNVERIFIED scouting.
"""
from fractions import Fraction as Q
import argparse,hashlib,json
from pathlib import Path
SHA='ad4afeaa4c7d8f48dfc270c437362287d8e2a21d9cce5b385c071e358431d2ec'
SRC='0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce'
SEAM='c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675'
def main():
    p=argparse.ArgumentParser()
    p.add_argument('--native',required=True);p.add_argument('--output',required=True)
    o=p.parse_args();data=Path(o.native).read_bytes()
    j=json.loads(data);assert hashlib.sha256(data).hexdigest()==SHA
    assert j['pass']=='NF504-native' and j['original_selected_J_dimension']==242
    assert j['source_original_NF407_sha256']==SRC
    assert j['source_original_NF406_sha256']==SEAM
    assert j['original_exterior_center_radius']=='549/500'
    assert j['original_support_saturated_physical_Hilbert_gate']=='CERTIFIED_PHYSICAL_SUPPORT_NO_GO'
    rlo,rhi=map(Q,j['original_original_saturated_exterior_residual_outward'])
    gamma=Q(j['original_original_gamma_squared'])
    assert 0<gamma<rlo<=rhi
    gates=(('H4094',Q(1,10**27),Q(2,5)),
           ('H4095',Q(1,10**27),Q(1,1000)),
           ('H4094_union_H4095',Q(3,10**27),Q(1,20000)))
    results=[]
    for name,e_upper,gap_lower in gates:
        max_gain=e_upper/gap_lower
        remain=rlo-max_gain
        assert 0<gamma<remain
        results.append({'original_physical_D':name,
           'CONDITIONAL_required_original_source_eD_upper':str(e_upper),
           'CONDITIONAL_required_source_KD_gap_lower':str(gap_lower),
           'original_source_max_gain_if_both_proved':str(max_gain),
           'original_source_new_residual_lower_if_both_proved':str(remain),
           'original_NF404_gamma_squared':str(gamma),
           'exact_conditional_original_physical_NO_GO_implication_proved':True,
           'actual_eD_and_KD_gap_not_source_certified':True})
    output={'pass':'NF517-original-source-exact-conditional-Fredholm-gates',
      'original_nf505_SHA256':SHA,'original_nf407_SHA256':SRC,
      'original_nf406_SHA256':SEAM,'original_selected_J242_dimension':242,
      'original_source_residual_interval':[str(rlo),str(rhi)],
      'unchanged_nf404_gamma_squared':str(gamma),
      'conditional_gates':results,
      'source_original_true_cell_eD_upper_certified':False,
      'original_selected_KD_operator_gap_certified':False,
      'unconditional_original_NF404_named_support_result':'OPEN',
      'Weil_multiplier_image_graph_domain':'OPEN','W_ODD_NEG':'OPEN','RH':'OPEN'}
    Path(o.output).write_text(json.dumps(output,indent=2)+'\n')
    print('NF517 original-source exact conditional Fredholm NO-GO gates PASS')
    print('Original true kernel gap and eD remain unverified; NF404/RH OPEN')
if __name__=='__main__':main()
