#!/usr/bin/env python3
"""Rational geometry controls; does not certify actual weak-null existence."""
import argparse,hashlib,json
from fractions import Fraction as F
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--output',required=True);args=p.parse_args()
root=Path(__file__).resolve().parents[1]
L=F(2);a=L/2;cases=0;parity_cases=0
for t in [F(1,8),F(1,16),F(1,32)]:
 for u in [t/4,t/2,3*t/4]:
  for ell in [F(3,4),F(3,2),L]:
   x=a+u;y=x-ell;v=a-y
   assert v==ell-u
   if ell<L:
    assert t<ell and t<L-ell and 0<ell-t<v<ell<L
   else:
    assert y==-a+u and v==L-u
   assert a-(x-t)==t-u
   cases+=1
  for sigma in [1,-1]:
   def f(z): return F(1) if sigma==1 else z-L/2
   assert f(L-u)==sigma*f(u)
   parity_cases+=1
# Constant even profile has nonzero threshold echo alpha*t.
alpha=F(3,5);t=F(1,8);echo=alpha*t
drop_threshold_rejected=echo!=0
assert drop_threshold_rejected
inputs=['notes/REFLECTED_PACKET_BRIDGE_108_EXACT_TRANSLATION_BOUNDARY_FLUX_20261005.md','notes/REFLECTED_PACKET_BRIDGE_108_ENDPOINT_BOUNDARY_REGULARITY_20261005.md','notes/REFLECTED_PACKET_BRIDGE_108_BOUNDARY_SCALING_20261005.md']
out={'base_commit':'1ef926fcd11525c80395beac0560ddfc8920b245','coordinate_cases':cases,'reflection_parity_cases':parity_cases,'negative_control_drop_threshold_echo_rejected':drop_threshold_rejected,'source_sha256':{x:hashlib.sha256((root/x).read_bytes()).hexdigest() for x in inputs},'controls_are_actual_modes':False,'universal_proofs_mechanically_checked':False,'critical_flux_integrability_established':False,'global_endpoint_exclusion':False,'aperture_frontier':'81/100','F4':False,'FULL_TRANSPORT_CLOSED':False,'Lean_changed':False}
Path(args.output).write_text(json.dumps(out,sort_keys=True,indent=2)+'\n')
print(json.dumps({'coordinate_cases':cases,'reflection_parity_cases':parity_cases,'negative_control_rejected':drop_threshold_rejected}))
