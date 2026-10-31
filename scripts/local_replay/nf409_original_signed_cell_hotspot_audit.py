#!/usr/bin/env python3
"""NF409 original NF408 physical 16-cell provisional quadrature hotspot audit.

Only exact arithmetic ON QUOTED *uncertified decimal pilot values*; not an
exact source multiplier quadrature. Identifies where the two screen meshes
disagree, preserving signed z² and z·(q+r) correlation rather than
inspecting noncorrelated contributions separately.
"""
import argparse,json,hashlib,sys
from fractions import Fraction as F
from pathlib import Path
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
def read(p):
 b=Path(p).read_bytes();return json.loads(b),hashlib.sha256(b).hexdigest()
def main():
 pa=argparse.ArgumentParser()
 pa.add_argument('--pilot',default='notes/data/provisional/NF408_original_16cell_norm_pilot.json')
 pa.add_argument('--principal',default='notes/data/provisional/NF409_original_principal_cell_integrals_exact.json')
 pa.add_argument('--center',default='notes/data/provisional/NF404_original_selected_pole_shear_exact.json')
 pa.add_argument('--output',required=True)
 a=pa.parse_args()
 pilot,p_sha=read(a.pilot)
 pilot_bytes=Path(a.pilot).read_bytes()
 assert hashlib.sha1(b'blob '+str(len(pilot_bytes)).encode()+b'\x00'+pilot_bytes).hexdigest()=='70ae4fac5061b6d4583c22097f9fe9fed687d482'
 weights,w_sha=read(a.principal)
 center,c_sha=read(a.center)
 assert pilot['pass']=='NF408'
 assert pilot['original_complete_centered_physical_L2_upper_CERTIFIED'] is False
 assert pilot['original_source_accurate_full_integral_error_enclosed'] is False
 assert len(pilot['pilot_resolutions'])==2
 assert pilot['original_nf406_original_seam_sha256']==weights['original_nf406_seams_sha256']
 assert pilot['original_nf407_exact_principal_sha256']==weights['original_nf407_principal_source_sha256']
 assert weights['original_nf404_center_source_sha256']==c_sha
 assert weights['actual_original_full_centered_supported_power_upper_computed'] is False
 assert all(x['W_ODD_NEG']==x['RH']=='OPEN' for x in (pilot,weights,center))
 low,high=pilot['pilot_resolutions']
 assert low['outer_nodes_per_original_positive_seam_cell']==2
 assert high['outer_nodes_per_original_positive_seam_cell']==4
 assert len(low['cells'])==len(high['cells'])==8
 cells=[]
 for i,(p,q,orig) in enumerate(zip(low['cells'],high['cells'],weights['original_eight_positive_source_principal_integrals'])):
  assert i==p['cell']-1==q['cell']-1==orig['cell']-1
  assert p['left']==q['left']==orig['left_label']
  assert p['right']==q['right']==orig['right_label']
  d_z2=F(q['z2_positive_half_pilot'])-F(p['z2_positive_half_pilot'])
  d_zp=F(q['z_p_positive_half_pilot'])-F(p['z_p_positive_half_pilot'])
  d_E=2*d_z2+4*d_zp
  cells.append({'cell':i+1,'from':p['left'],'to':p['right'],
    'pilot_two_resolution_signed_delta_z2_two_sided_exact_decimal':str(2*d_z2),
    'pilot_two_resolution_signed_delta_2_zp_two_sided_exact_decimal':str(4*d_zp),
    'pilot_two_resolution_signed_delta_full_E_exact_decimal':str(d_E),
    'pilot_two_resolution_absolute_delta_full_E_exact_decimal':str(abs(d_E)),
    'full_cell_inner_and_outer_quadrature_error_enclosed':False,
    'relative_priority_only_not_a_proof_of_true_error':True})
 net=sum((F(r['pilot_two_resolution_signed_delta_full_E_exact_decimal']) for r in cells),F(0))
 reported=F(high['original_uncertified_reconstructed_full_centered_physical_power'])-F(low['original_uncertified_reconstructed_full_centered_physical_power'])
 assert abs(net-reported)<F(1,10**55)
 assert abs(abs(net)-F(pilot['original_two_outer_resolution_difference_absolute']))<F(1,10**55)
 abs_total=sum((F(r['pilot_two_resolution_absolute_delta_full_E_exact_decimal']) for r in cells),F(0))
 ranked=sorted(cells,key=lambda z:abs(F(z['pilot_two_resolution_signed_delta_full_E_exact_decimal'])),reverse=True)
 top3=[r['cell'] for r in ranked[:3]]
 assert top3==[6,3,7]
 top3fraction=sum((F(r['pilot_two_resolution_absolute_delta_full_E_exact_decimal']) for r in ranked[:3]),F(0))/abs_total
 assert top3fraction>F(4,5)
 assert abs_total>abs(net)>F(1,10**22)
 C=F(center['exact_sufficient_new_full_supported_centered_scalar_power_upper_target'])
 assert F(low['original_uncertified_reconstructed_full_centered_physical_power'])<C
 assert F(high['original_uncertified_reconstructed_full_centered_physical_power'])>C
 # This observation does NOT establish the original norm is inside
 # the numerical bracket. No monotone convergence or valid error bar.
 out={'pass':'NF409',
  'standing':'UNCERTIFIED ORIGINAL NF408 TWO-MESH SIGNED CELL HOTSPOT RECONCILIATION; NO INTERVAL NOR ENCLOSING NORM',
  'nf408_original_16cell_pilot_sha256':p_sha,
  'nf409_original_source_exact_p_cell_weights_sha256':w_sha,
  'nf404_original_center_source_sha256':c_sha,
  'all_original_eight_positive_cells':cells,
  'source_original_refinement_priority_by_unsigned_intermesh_difference':[r['cell'] for r in ranked],
  'original_source_intermesh_top_three_cells':[6,3,7],
  'intermesh_top_three_absolute_variation_fraction_exact':str(top3fraction),
  'strict_top_three_more_than_eighty_percent_of_absolute_cell_disagreement':True,
  'original_original_nf408_two_mesh_signed_global_difference_exact_decimal':str(net),
  'original_original_nf408_total_absolute_cell_variation_exact_decimal':str(abs_total),
  'source_original_2_node_norm_below_cap_4_node_above_cap':True,
  'neither_source_original_mesh_estimate_is_proved_lower_or_upper':True,
  'source_original_true_complete_centered_norm_rigorously_measured':False,
  'source_original_error_limit_via_mesh_comparison':False,
  'original_full_W_odd_obligation':'OPEN',
  'new_signed_kernel_cells':0,'W_ODD_NEG':'OPEN','RH':'OPEN'
 }
 dst=Path(a.output);dst.parent.mkdir(parents=True,exist_ok=True)
 dst.write_text(json.dumps(out,indent=2)+'\n')
 print('NF409 original two-mesh true source screen comparison reproduced EXACTLY in reported decimals')
 print('NF409 3 largest signed-cell E discrepancies: 6,3,7; >80% L1 disagreement')
 print('NF409 original full norm not enclosed; two sample values straddle target')
if __name__=='__main__':main()
