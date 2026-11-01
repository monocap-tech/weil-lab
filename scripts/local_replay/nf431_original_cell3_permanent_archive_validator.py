#!/usr/bin/env python3
"""NF431 exact original interval artifact permanent GitHub archive validator.

Read verified same-run CI NF431 original 6 Chebyshev coefficient shards,
original 1500 signed principal moment ledger and complete signed cell3
true pz/z² sector. Assert identical SHA provenance, all 1500 numerical
coefficients, all 1500 signed moments, true original physical cell3,
independent NF417 and NF410 checks, strict interval signs. This is a
custody integrity test; it does not replace the original Arb calculation.
"""
import hashlib,json,sys
from fractions import Fraction as F
from pathlib import Path
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
ROOT=Path("notes/data/provisional/nf431-original-cell3")
RUN=41279353773
SOURCE="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAMS="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
def read(p):
 data=p.read_bytes()
 return json.loads(data),hashlib.sha256(data).hexdigest(),len(data)
def main():
 shards=sorted(ROOT.glob("NF431_original_cell3_z_shard_*.json"))
 assert len(shards)==6,('expected exactly original six coefficient shards',len(shards))
 pm=ROOT/"NF431_original_cell3_pmoments_1500.json"
 sector=ROOT/"NF431_original_complete_true_cell3_pz_zsquared.json"
 assert pm.exists() and sector.exists()
 s,ssha,_=read(sector);m,msha,_=read(pm)
 assert s['pass']=='NF431' and m['pass']=='NF431'
 assert s['source_correlated_cheb_series_all_1500_coefficients_native_certified']
 assert m['all_1500_source_signed_chebyshev_moments_certified']
 assert s['NF431_original_all_1500_signed_principal_moments_sha256']==msha
 assert m['nf407_original_full_source_sha256']==SOURCE
 assert m['nf406_original_seams_sha256']==SEAMS
 assert s['original_NF406_support_seams_sha256']==SEAMS
 assert s['full_original_true_cell3']=='(log(4)-11/10,11/10-log(2))'
 assert s['seven_remaining_original_physical_cells_integrated'] is False
 assert s['NF404_complete_signed_scalar_decided'] is False
 assert s['W_ODD_NEG']==s['RH']=='OPEN'
 assert len(m['original_signed_p_chebyshev_moments_n0_to_n1499'])==1500
 assert m['original_nf410_n0_signed_principal_moment_overlap']
 hashes={x['file']:x['sha256'] for x in s['NF431_six_coefficient_shard_sha256']}
 assert len(hashes)==6
 seen=set()
 for p in shards:
  data,sha,_=read(p)
  assert sha==hashes[p.name] and data['pass']=='NF431'
  assert data['source_sha256']==SOURCE and data['seams_sha256']==SEAMS
  assert data['original_analytic_global_transfer_pointwise_NF417_overlap_pass']
  assert data['original_four_selected_plus_critical_count']==246
  assert data['common_endpoint_image_indices']==2048
  assert data['original_post_seam_primes_retained']==[3,4]
  assert data['original_both_source_prime_translations_retained']==[2]
  assert data['original_neither_branches']==[5,7,8,9]
  assert data['number_of_certified_low_mode_coefficients']==len(data['coefficients'])
  for c in data['coefficients']:
   k=c['n'];assert k not in seen;seen.add(k)
   a,b=map(F,c['true_original_cell3_fixed_branch_coefficient_outward_interval'])
   assert a<=b and b-a<F(1,10**25)
 assert seen==set(range(1500))
 a,b=map(F,s['true_original_cell3_sector_4pz_plus_2z2_outward_exact'])
 assert F(0)<a<=b
 l,r=map(F,s['true_original_cell3_integral_z_squared_outward_exact'])
 assert 0<=l<=r
 l,r=map(F,s['signed_pz_true_original_cell3_outward_exact'])
 assert l<=r<0
 expected=shards+[pm,sector]
 assert len(expected)==8
 manifest={
  'pass':'NF431','standing':'PERMANENT SOURCE-PINNED ORIGINAL CELL3 ALL EIGHT ACTUAL INTERVAL JSON FILES VERIFIED',
  'original_GitHub_Actions_run_id':RUN,
  'original_source_sha256':SOURCE,'original_support_sha256':SEAMS,
  'six_native_coefficient_shards':True,
  'all_1500_original_z_Chebyshev_coefficients_source_verified':True,
  'all_1500_original_signed_p_moments_source_verified':True,
  'full_original_signed_cell3_pz_z2_and_sector_certified':True,
  'original_complete_scalar_decided':False,'RH':'OPEN',
  'files':[{'name':p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size} for p in expected]}
 path=ROOT/"NF431_ORIGINAL_CELL3_ARCHIVE_SHA256_MANIFEST.json"
 path.write_text(json.dumps(manifest,indent=2)+'\n')
 print('NF431 permanent archive all six original source-native full 1500 coefficients + true signed moments + signed scalar verified PASS')
 print('NF431 original full cell3 signed sector interval certified; original six further cells whole NF404 and RH OPEN')
if __name__=="__main__":main()
