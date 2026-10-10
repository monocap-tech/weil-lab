#!/usr/bin/env python3
"""Paid native-relative source credit for CC97's complete collective packet."""
import argparse,json
from pathlib import Path
from fractions import Fraction as F
import numpy as np
import certify_cc81_boundary_response_consumer as c
import certify_cc88_correlated_seventh_response as r
import certify_cc97_collective_signed_consumer as prior

def controls():
 cases=[];kap=F(11,25);credit=F(1,4);remainder=F(1,9)
 for scale in [F(1),F(1,10**18)]:
  for cross in [F(1,7),F(1,6),F(1,5)]:
   # Q=diag(1,scale²), H=kap Q-Gamma. Both source diagonals
   # and the complete source Gram are positive throughout crossing.
   gd1=kap-credit;gd2=(kap-remainder)*scale**2;gc=-cross*scale
   assert gd1>0 and gd2>0 and gd1*gd2-gc*gc>0
   margin=(remainder-cross*cross/credit)*scale**2
   determinant=(credit*remainder-cross*cross)*scale**2
   assert (margin>0)==(cross*cross<credit*remainder)
   cases.append(dict(scale=str(scale),signed_dual_coupling=str(cross),remaining_Schur_margin=str(margin),joint_signed_determinant=str(determinant),native_and_complete_source_Gram_positive=True))
 return cases
def run(root):
 previous=prior.run(root);rows=[]
 for parity,credit in [('even',F(23,500)),('odd',F(8,125))]:
  source,_=prior.rawread(root,'notes/data/RPB108_DNE35_'+parity.upper()+'_JOINT_SOURCE_REPLAY_20261009.json.gz.b64')
  proof,_=prior.rawread(root,'notes/data/RPB108_DNE35_'+parity.upper()+'_SIGNED_COMPARISON_20261009.json')
  U=[[F(x) for x in row] for row in proof['positive_joint_prefix_certificate']['exact_congruence_U']];ui=[[c.iv(x) for x in row] for row in U]
  Q=c.matrix(source['native_block']);G=c.matrix(source['original_projected_source_Gram'])
  H=[[c.sub(c.mul(c.iv(prior.K),q),g) for q,g in zip(qr,gr)] for qr,gr in zip(Q,G)]
  h=r.mm(c.transpose(ui),r.mm(H,ui));q=r.mm(c.transpose(ui),r.mm(Q,ui))
  shifted=r.sub(h,r.scale(q,credit))
  midpoint=np.array([[float((a+b)/2) for a,b in row] for row in shifted])
  # Floating Cholesky selects a fixed rational congruence only.
  candidate=np.linalg.inv(np.linalg.cholesky((midpoint+midpoint.T)/2)).T
  V=[[F(round(F(float(x))*10**30),10**30) for x in row] for row in candidate]
  vi=[[c.iv(x) for x in row] for row in V]
  paid=r.mm(c.transpose(vi),r.mm(shifted,vi))
  margins=[paid[i][i][0]-sum(r.absmax(paid[i][j]) for j in range(12) if i!=j) for i in range(12)]
  assert min(margins)>0
  rows.append(dict(parity=parity,native_relative_source_credit=str(credit),
   complete_source_to_native_ratio_upper=str(prior.K-credit),
   frozen_rational_credit_congruence=list(map(lambda row:list(map(str,row)),V)),
   original_DNE_congruence_then_credit_congruence=True,
   paid_positive_row_margin_lower=c.pair(c.iv(min(margins)))[0],
   signed_source_credit_matrix='(11/25-credit)*Q-Gamma',
   certified_retained_rank=12,source_errors_and_all_mixed_entries_preserved=True))
 return dict(milestone='CC98',integration_parent='1e0ac7d82e5e6493259ec9f5bbd07d868854d805',
  read_only_DNE=previous['read_only_DNE'],read_only_Native_Source=previous['read_only_Native_Source'],
  parity_checks=rows,exact_positive_null_negative_extension_controls=controls(),
  extension_sufficient_criterion='t^2<c*d for signed native-relative mixed coupling t and remaining signed credit d',
  new_retained_directions=0,current_collective_retained_rank=24,remaining_uncovered_retained_dimension=88,
  complete_remaining_source_Gram_certified=False,whole_aperture_positive=False,highest_certified_whole_aperture='21/20')
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('source_root',type=Path);ap.add_argument('--output',type=Path,required=True)
 a=ap.parse_args();d=run(a.source_root);a.output.write_text(json.dumps(d,indent=2)+'\n')
 print('CC98 PASS: collective native-relative source credits 0.046 even, 0.064 odd')
