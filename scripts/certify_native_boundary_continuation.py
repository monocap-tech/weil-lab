#!/usr/bin/env python3
"""Exact algebra controls for the RPB108 local boundary continuation.

These controls do not certify the universal analytic theorems or actual modes.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

BASE = 'd17a74065324575654cd53ea394957dfa4961ebb'
ROOT = Path(__file__).resolve().parents[1]
p = argparse.ArgumentParser()
p.add_argument('--output', required=True)
args = p.parse_args()
inputs = [
 'notes/REFLECTED_PACKET_BRIDGE_108_ENDPOINT_BOUNDARY_REGULARITY_20261005.md',
 'notes/REFLECTED_PACKET_BRIDGE_108_LOGARITHMIC_BOOTSTRAP_20261005.md',
 'notes/REFLECTED_PACKET_BRIDGE_108_FRACTIONAL_NULL_REGULARITY_20261005.md',
 'notes/REFLECTED_PACKET_BRIDGE_108_FRACTIONAL_OPTIMIZATION_20261005.md',
 'notes/REFLECTED_PACKET_BRIDGE_108_ACTUAL_MOVING_GAUSSIAN_COERCIVITY_20261004.md',
 'notes/REFLECTED_PACKET_BRIDGE_108_GAUSSIAN_FAR_FIELD_BOUNDARY_COLLAR_20261004.md',
]
hashes = {x: hashlib.sha256((ROOT/x).read_bytes()).hexdigest() for x in inputs}
factor_cases = 0
for d in [F(1,2), F(1,4), F(1,8), F(3,4)]:
 s = (1-d)/2
 assert -2*s == -1+d
 for E in [F(2), F(1922), F(2000)]:
  assert E+(E+1) <= 2*E+3
  factor_cases += 1
pole_cases = 0
for z in [F(1), F(3,2), F(2), F(5,4)]:
 for ar,ai,br,bi in [(F(1),F(2),F(3),F(-1)),(F(-2),F(1),F(1),F(4))]:
  # q = conjugate(B)*A; exact complex real/imaginary coordinates.
  qr = br*ar+bi*ai
  qi = br*ai-bi*ar
  real_cross = z*qr+qr/z
  imag_cross = z*qi-qi/z
  ch = (z+1/z)/2
  assert real_cross == ch*(2*qr)
  assert imag_cross == (z-1/z)*qi
  pole_cases += 1
translation_cases = 0
for weights in [(F(1),F(2)),(F(3),F(1))]:
 for m in [(F(-1),F(4)),(F(2),F(3))]:
  for cosine in [(F(3,5),F(-5,13)),(F(0),F(1,2))]:
   for z in [F(3,2),F(5,4)]:
    pole = -sum(x*y for x,y in zip(m,weights))
    ch = (z+1/z)/2
    flux = sum(x*c*y for x,c,y in zip(m,cosine,weights))+ch*pole
    increment = sum(x*(1-c)*y for x,c,y in zip(m,cosine,weights))
    assert flux == -increment+(ch-1)*pole
    translation_cases += 1
m,weights,cosine,z = (F(2),F(3)),(F(1),F(2)),(F(0),F(1,2)),F(3,2)
pole = -sum(x*y for x,y in zip(m,weights))
ch = (z+1/z)/2
inc = sum(x*(1-c)*y for x,c,y in zip(m,cosine,weights))
flux = -inc+(ch-1)*pole
sign_rejected = flux != inc+(ch-1)*pole
assert sign_rejected
out = {
 'base_commit': BASE, 'source_sha256': hashes,
 'two_factor_ceiling_cases': factor_cases, 'complex_pole_cases': pole_cases,
 'translation_identity_cases': translation_cases,
 'negative_control_reversed_increment_sign_rejected': sign_rejected,
 'controls_are_actual_modes': False, 'universal_proofs_mechanically_checked': False,
 'critical_flux_integrability_established': False, 'half_derivative_established': False,
 'exponential_gaussian_decay': False, 'global_endpoint_exclusion': False,
 'aperture_frontier': '81/100', 'F4': False, 'FULL_TRANSPORT_CLOSED': False,
 'Lean_changed': False,
}
Path(args.output).write_text(json.dumps(out, sort_keys=True, indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['two_factor_ceiling_cases','complex_pole_cases','translation_identity_cases','negative_control_reversed_increment_sign_rejected']}))
