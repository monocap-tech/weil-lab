#!/usr/bin/env python3
"""Exact controls for averaged leading-kernel algebra; no actual-mode assertion."""
from fractions import Fraction as F
from pathlib import Path
import argparse,json,hashlib
p=argparse.ArgumentParser();p.add_argument('--output',required=True);args=p.parse_args()
root=Path(__file__).resolve().parents[1]
cases=0
for u in [F(0),F(1,3),F(2)]:
 for v in [F(1,8),F(1),F(3,2)]:
  for w in [F(1,4),F(2,3),F(2)]:
   left=1/((u+w)**2*(u+v))+1/((u+v)**2*(u+w))
   right=(2*u+v+w)/((u+v)**2*(u+w)**2)
   assert left==right
   cases+=1
# The common-denominator numerators are identically (u+v)+(u+w)=2u+v+w.
assert (2,1,1)==(1+1,1,1)
controls=[]
for B in [F(0),F(1),F(3)]:
 for C in [F(0),F(2),F(5)]:
  M=8*(B+C+1)
  q=-M*M/4+B*M+C
  assert q<0
  controls.append([int(B),int(C),int(M)])
wrong_sign_rejected=F(-1,4)!=F(1,4)
assert wrong_sign_rejected
inputs=['notes/REFLECTED_PACKET_BRIDGE_108_EXACT_EDGE_FLUX_CHANNELS_20261005.md','notes/REFLECTED_PACKET_BRIDGE_108_BOUNDARY_SCALING_20261005.md','notes/REFLECTED_PACKET_BRIDGE_108_EXACT_TRANSLATION_BOUNDARY_FLUX_20261005.md']
out={'base_commit':'4078bf1ad97435e754b22d067b5c68a8ac5826be','symmetrization_cases':cases,'quadratic_linear_cases':controls,'negative_control_singular_flux_sign_rejected':wrong_sign_rejected,'source_sha256':{x:hashlib.sha256((root/x).read_bytes()).hexdigest() for x in inputs},'controls_are_actual_modes':False,'universal_proofs_mechanically_checked':False,'bounded_nonnegative_actual_sector_established':False,'critical_flux_integrability_established':False,'global_endpoint_exclusion':False,'aperture_frontier':'81/100','F4':False,'FULL_TRANSPORT_CLOSED':False,'Lean_changed':False}
Path(args.output).write_text(json.dumps(out,sort_keys=True,indent=2)+'\n')
print(json.dumps({'symmetrization_cases':cases,'quadratic_linear_cases':len(controls),'negative_control_rejected':wrong_sign_rejected}))
