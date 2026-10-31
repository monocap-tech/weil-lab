#!/usr/bin/env python3
"""NF407 exact source-dependent necessary cancellation for NF404 scalar gate.

CONDITIONAL: only if the as-yet-UNMEASURED full centered physical norm
satisfies NF404's cap. This is not a lower/upper measurement of z or
the signed cross. Requires accepted original q+r source exact certificate.
"""
import argparse,hashlib,json,sys
from pathlib import Path
from fractions import Fraction as F
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
def read(p):
 b=Path(p).read_bytes()
 return json.loads(b),hashlib.sha256(b).hexdigest()
def run(args):
 p,sha=read(args.principal)
 c,csha=read(args.center)
 assert p['pass']=='NF407' and p['source_all_original_prime_jumps_cancelled_from_z'] is True
 assert p['original_nf404_center_sha256']==csha
 assert c['W_ODD_NEG']==c['RH']==p['W_ODD_NEG']==p['RH']=='OPEN'
 Slo,Shi=map(F,p['original_known_q_plus_all_seven_prime_jumps_power_interval'])
 target=F(c['exact_sufficient_new_full_supported_centered_scalar_power_upper_target'])
 assert F(0)<Slo<Shi
 assert c['actual_original_full_supported_centered_scalar_integrated'] is False
 # Root-free exact rational norms:
 principal_floor=F(461,10**13)
 complete_cap=F(331,10**13)
 z_min=principal_floor-complete_cap
 assert Slo>principal_floor**2
 assert target<complete_cap**2
 assert z_min==F(13,10**12)
 cross_cap=(target-Slo)/2
 assert cross_cap < -F(515,10**24)
 # If ||g||²<=target, g=p+z; triangle =>
 # ||z||>||p||-||g||>1.3e-11.
 # Also 2<z,p> =||g||²-||p||²-||z||²<=target-Slo,
 # and therefore <z,p><-5.15e-22.
 out={
  'pass':'NF407',
  'standing':'EXACT SOURCE-BASED CONDITIONAL NECESSARY CANCELLATION GATE; ORIGINAL CONTINUOUS PHYSICAL RESPONSE UNMEASURED',
  'original_q_plus_prime_jumps_source_sha256':sha,
  'original_nf404_center_source_sha256':csha,
  'original_principal_power_lower_exact':str(Slo),
  'original_principal_power_upper_exact':str(Shi),
  'original_full_centered_power_conditional_cap':str(target),
  'source_strict_principal_norm_floor':str(principal_floor),
  'source_strict_full_norm_conditional_ceiling':str(complete_cap),
  'necessary_continuous_regularized_z_norm_strict_lower_if_cap_passes':str(z_min),
  'necessary_signed_z_principal_inner_product_upper_if_cap_passes':str(cross_cap),
  'strict_required_negative_cross_less_than':'-515/1000000000000000000000000',
  'conditional_gate_statement':'IF ||g||²<=the unmeasured NF404 centered power cap, THEN ||z||>1.3e-11 and <z,q+r><-5.15e-22, where z=g-q-r',
  'original_actual_continuous_z_norm_measured':False,
  'original_actual_signed_z_principal_cross_measured':False,
  'original_full_centered_power_upper_computed':False,
  'original_lowband_upper_computed':False,
  'W_ODD_NEG':'OPEN','RH':'OPEN'
 }
 path=Path(args.output);path.parent.mkdir(parents=True,exist_ok=True)
 path.write_text(json.dumps(out,indent=2)+'\n')
 print('NF407 exact necessary cancellation IF future original centered cap succeeds, NOT measured')
if __name__=='__main__':
 pa=argparse.ArgumentParser()
 pa.add_argument('--principal',default='notes/data/provisional/NF407_original_prime_jump_log_power_exact.json')
 pa.add_argument('--center',default='notes/data/provisional/NF404_original_selected_pole_shear_exact.json')
 pa.add_argument('--output',required=True)
 run(pa.parse_args())
