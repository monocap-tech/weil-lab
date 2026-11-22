#!/usr/bin/env python3
"""UOI047 exact finite rational illustration. Does NOT prove the infinite tail theorem or Lean acceptance."""
from pathlib import Path
from fractions import Fraction as Q
import json, hashlib
root=Path(__file__).resolve().parent
src=root.parent/'uoi044'/'UOI044_stage10_exact_arithmetic_receipt.json'
b=json.loads(src.read_text())['matrix_upper_microgrid_int']
assert len(b)==10 and all(len(x)==10 for x in b)
assert all(b[j][k]==b[k][j] and (j!=k or b[j][k]==0) for j in range(10) for k in range(10))

out=[]
for M in range(10):
  ratios=[]
  for j in range(M,10):
    g=Q(859+600*j,1000)
    row=Q(sum(b[j][k] for k in range(M,10) if k!=j),10**6)
    ratios.append((j,row/g))
  worst=max(ratios,key=lambda p:p[1])
  out.append({'M':M, 'largest_row_index':worst[0], 'largest_ratio_exact':str(worst[1]),'largest_ratio_decimal':float(worst[1])})
  if M>0:
    assert worst[1] < Q(43,100)
assert out[1]['largest_ratio_exact'] == str(max((Q(sum(b[j][k] for k in range(1,10) if k!=j),10**6)/Q(859+600*j,1000) for j in range(1,10))))
proof={'schema':'uoi047-finite-envelope-illustration-v1',
       'status':'exact finite rational matrix illustration only; all-stage BT/Gamma/Schur proof NOT checked by this script',
       'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),
       'ten_stage_tail_rows':out,
       'claim_finite_S10_collars_1_to_9':'P(f) < 43/100 Gamma(f); W_lit(f) > 57/100 Gamma(f)',
       'verified_infinite_stage':False,
       'verified_Lean_kernel':False}
p=root/'UOI047_finite_rational_receipt.json'
p.write_text(json.dumps(proof,indent=2,sort_keys=True)+'\n')
print('PASS: exact 10x10 finite-stage tail rational envelope')
print('S10 tails j=1..9: max row/g=',out[1]['largest_ratio_exact'],'≈',out[1]['largest_ratio_decimal'])
print('Receipt:',p)