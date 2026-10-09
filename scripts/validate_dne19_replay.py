#!/usr/bin/env python3
from fractions import Fraction as F
from pathlib import Path
import json,sys
a,b=(json.loads(Path(p).read_text()) for p in sys.argv[1:3]);checks=0
assert a['source_input_sha256']==b['source_input_sha256'];checks+=1
for field in ('Rayleigh_numerator','Rayleigh_denominator'):
 l,h=map(F,a[field]);ll,hh=map(F,b[field]);assert l<=ll<=hh<=h;checks+=1
assert F(b['prime_operator_norm_strict_lower'])>=F(a['prime_operator_norm_strict_lower']);checks+=1
assert F(b['fixed_budget_floor_strict_ceiling'])<=F(a['fixed_budget_floor_strict_ceiling']);checks+=1
for r,s in zip(a['parity_rows'],b['parity_rows']):
 assert r==s or r['parity']==s['parity'];checks+=1
 for field in ('w_native_energy','w_original_full_high_source_square','necessary_floor_strict_interval','coarse_w_diagonal_at_11_over_25'):
  assert r[field]==s[field];checks+=1
 assert F(s['best_fixed_arch_global_norm_budget_w_diagonal_upper'])<=F(r['best_fixed_arch_global_norm_budget_w_diagonal_upper'])<0;checks+=1
 assert F(s['fixed_global_norm_arch_budget_needed_strict_lower'])>=F(r['fixed_global_norm_arch_budget_needed_strict_lower']);checks+=1
assert a['controls']==b['controls'] and len(a['controls'])==7;checks+=1
assert a['surviving_word_counts']==b['surviving_word_counts']=={'2':82,'3':464};checks+=1
out={'stage':'DNE19','status':'PASS','replay_comparisons':checks,
 'primary_exact_rational_assertions':a['exact_rational_assertions'],
 'replay_exact_rational_assertions':b['exact_rational_assertions'],
 'both_raw_response_directions_rejected_at_DNE17_floor':True,
 'fixed_arch_global_prime_norm_strategy_barrier_verified':True,
 'new_positive_subspace_certified':False,'whole_aperture_positive':False,'RH':False}
Path(sys.argv[3]).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
