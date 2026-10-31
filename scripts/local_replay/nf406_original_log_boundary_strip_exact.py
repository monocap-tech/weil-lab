#!/usr/bin/env python3
"""NF406 source-pinned exact two-boundary logarithmic strip budget.
The bound is for explicit q singular function ONLY, not the entire
unknown regular source or cross term. No RH or full physical norm upper.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,hashlib,sys
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
B=F(11,10)

def load(path):
 v=Path(path).read_bytes()
 return json.loads(v),hashlib.sha256(v).hexdigest()

def main():
 p=argparse.ArgumentParser()
 p.add_argument('--boundary',default='notes/data/provisional/NF406_original_physical_endpoint_log_exact.json')
 p.add_argument('--center',default='notes/data/provisional/NF404_original_selected_pole_shear_exact.json')
 p.add_argument('--output',required=True)
 a=p.parse_args()
 q,sha=load(a.boundary)
 c,csha=load(a.center)
 assert q['pass']=='NF406' and q['physical_endpoint_log_subtraction_required'] is True
 assert q['original_nf404_pole_shear_exact_sha256']==csha
 assert q['original_complete_regular_part_and_cross_integrated'] is False
 assert q['original_full_supported_centered_scalar_upper_computed'] is False
 assert q['W_ODD_NEG']==q['RH']==c['W_ODD_NEG']==c['RH']=='OPEN'
 u_lo,u_hi=map(F,q['original_u4_endpoint_outward'])
 assert u_lo<u_hi<0
 Qhi=F(q['original_exact_log_model_squared_norm_upper'])
 assert Qhi==B*u_lo*u_lo
 gamma2=F(c['exact_source_original_full_complement_power_budget'])
 assert gamma2>0
 cap=gamma2/32
 rows=[]
 first=None
 for k in range(16,33):
  delta=B/(2**k)
  # Exact primitive: two boundary strips of width delta,
  # ||q||²_boundary =u(B)^2/2 *delta*
  # (L²+2L+2), L=log(B/delta)=k log(2).
  # Source-accepted original NF375 inequality log2<7/10.
  log_upper=F(7*k,10)
  qstrip_upper=u_lo*u_lo*delta/2*(log_upper**2+2*log_upper+2)
  assert qstrip_upper>0
  passed=qstrip_upper<cap
  rows.append({'k':k,'delta_two_sided':str(delta),
               'strict_original_q_only_strip_squared_power_upper':str(qstrip_upper),
               'strict_q_only_vs_gamma2_over_32':passed})
  if passed and first is None:first=k
 assert first==24
 assert all(row['strict_q_only_vs_gamma2_over_32']==(row['k']>=24) for row in rows)
 assert F(0)<F(rows[8]['strict_original_q_only_strip_squared_power_upper'])<cap
 out={
   'pass':'NF406',
   'standing':'ORIGINAL LOG SINGULAR MODEL EXACT TWO-BOUNDARY MESH STRIP BUDGET ONLY; REGULAR/CROSS OPEN',
   'original_nf406_endpoint_log_sha256':sha,
   'original_nf404_center_source_sha256':csha,
   'source_log2_upper':'7/10',
   'source_log_integral_identity':'integral_0^delta log^2(B/d) dd = delta*(log(B/delta)^2+2 log(B/delta)+2)',
   'original_boundary_log_model':'q(x)=u4(B)/2 sign(x) log(B/(B-|x|))',
   'two_boundary_strips':'[-B,-B+delta] union [B-delta,B]',
   'strict_original_first_log_only_strip_budget_log2':first,
   'strict_original_first_log_only_strip_width':str(B/2**24),
   'original_exterior_power_budget_gamma2':str(gamma2),
   'allocated_log_singular_strip_budget':str(cap),
   'rows':rows,
   'original_full_response_strip_integrated':False,
   'original_regular_component_strip_integrated':False,
   'original_log_regular_cross_integrated':False,
   'source_exact_log_q_strip_does_not_bound_complete_g_strip':True,
   'W_ODD_NEG':'OPEN','RH':'OPEN'
 }
 target=Path(a.output);target.parent.mkdir(parents=True,exist_ok=True)
 target.write_text(json.dumps(out,indent=2)+'\n')
 print('NF406 exact original q-only boundary strips first k=24 and gamma²/32 PASS')
 print('NF406 full physical g near boundary not controlled by q-only bound')
if __name__=='__main__':main()
