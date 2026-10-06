#!/usr/bin/env python3
"""Exact nonzero moment-null comparison profiles; no actual-null assertion."""
import argparse,json,hashlib
from pathlib import Path
from fractions import Fraction as F
p=argparse.ArgumentParser();p.add_argument('--output',required=True);args=p.parse_args()
root=Path(__file__).resolve().parents[1]
def mul(a,b):
 out=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]+=x*y
 return out
def value(poly,x):return sum(c*x**i for i,c in enumerate(poly))
rows=[]
for L in [F(1),F(81,50),F(2)]:
 z=[F(0),L,F(-1)];power=[F(1)]
 for order in range(1,9):
  power=mul(power,z);c=L*L*order/(2*(2*order+1))
  poly=mul(power,[-c,L,F(-1)])
  moment=sum(poly[k]*L**k/k for k in range(1,len(poly)))
  square=mul(poly,poly)
  norm=sum(q*L**(i+1)/(i+1) for i,q in enumerate(square))
  assert moment==0 and norm>0 and value(poly,F(0))==value(poly,L)==0
  for x in [L/8,L/4,L/2,3*L/4,7*L/8]:assert value(poly,L-x)==value(poly,x)
  assert len(poly)-1==2*order+2 and poly[-1]!=0
  if order==1:assert norm==L**9/7560
  rows.append({'L':[L.numerator,L.denominator],'p':order,'moment':[0,1],'L2_squared':[norm.numerator,norm.denominator],'degree':len(poly)-1})
control_rejected=all(r['moment']==[0,1] and r['L2_squared'][0]>0 for r in rows)
assert control_rejected
inputs=['notes/REFLECTED_PACKET_BRIDGE_108_AVERAGED_CARLEMAN_MOMENT_20261005.md','notes/REFLECTED_PACKET_BRIDGE_108_EXACT_EDGE_FLUX_CHANNELS_20261005.md']
out={'base_commit':'ef46f5691790d06d40cc521ca4434962f2f1643e','profile_cases':rows,'negative_control_zero_moment_implies_zero_mass_rejected':control_rejected,'source_sha256':{x:hashlib.sha256((root/x).read_bytes()).hexdigest() for x in inputs},'controls_are_actual_modes':False,'actual_kernel_moment_injectivity_established':False,'universal_proofs_mechanically_checked':False,'global_endpoint_exclusion':False,'aperture_frontier':'81/100','F4':False,'FULL_TRANSPORT_CLOSED':False,'Lean_changed':False}
Path(args.output).write_text(json.dumps(out,sort_keys=True,indent=2)+'\n')
print(json.dumps({'profile_cases':len(rows),'negative_control_rejected':control_rejected}))
