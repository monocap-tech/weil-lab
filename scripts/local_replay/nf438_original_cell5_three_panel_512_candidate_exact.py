#!/usr/bin/env python3
"""NF438: source-exact three-panel J5 feasibility; true signed J5 OPEN."""
import json,hashlib,math,sys,argparse
from pathlib import Path
from fractions import Fraction as F
from nf425_original_cell6_chebyshev_existence_exact import source
from nf433_original_cell3_cell7_branch_ellipse_router_exact import cheb_source_tail
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
B=F(11,10)
PANELS=[(F(565,1000),F(63,1000)),(F(677,1000),F(63,1000)),(F(789,1000),F(63,1000))]
CUTS=[F(62,100),F(73,100)]
RHOS=[F(2),F(3),F(4),F(5)]
def get(path):
 b=Path(path).read_bytes()
 return json.loads(b),hashlib.sha256(b).hexdigest()
def main():
 a=argparse.ArgumentParser()
 a.add_argument('--source',default='notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json')
 a.add_argument('--seams',default='notes/data/provisional/NF406_original_prime_support_partition_exact.json')
 a.add_argument('--output',required=True)
 args=a.parse_args()
 s,sh=get(args.source);k,kh=get(args.seams)
 assert sh=='0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce'
 assert kh=='c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675'
 assert s['original_dimension']==242 and len(s['original_source_critical_sine_frequencies'])==32
 assert k['certified_ordered_knots'][12]['label']=='-B+log(5)'
 assert k['certified_ordered_knots'][13]['label']=='-B+log(7)'
 L=F(k['certified_ordered_knots'][12]['low'])
 R=F(k['certified_ordered_knots'][13]['high'])
 assert L<CUTS[0]<CUTS[1]<R<B
 ranges=[(L,CUTS[0]),(CUTS[0],CUTS[1]),(CUTS[1],R)]
 c,pole,S0=source(s)
 assert len(c)==273 and S0<F(1,10**700)
 out={'pass':'NF438','standing':'SOURCE-EXACT J5 THREE ANALYTIC PANEL CANDIDATE ONLY',
 'original_source_sha256':sh,'original_seams_sha256':kh,
 'J5':'(log(5)-11/10,log(7)-11/10)',
 'regular_minus':[2,3,4,5],'regular_plus':[],
 'principal_jumps':[2,3,4,5],'internal_rational_cuts':list(map(str,CUTS)),
 'panels':[],'full_true_cell5_signed_integral_certified':False,'W_ODD_NEG':'OPEN','RH':'OPEN'}
 for i,((C,H),(l,r)) in enumerate(zip(PANELS,ranges),1):
  assert C-H<l<r<C+H
  admissible=[]
  for rho in RHOS:
   xmax=C+H*(rho+1/rho)/2
   xmin=C-H*(rho+1/rho)/2
   assert 0<xmin and xmax<B
   admissible.append({'rho':str(rho),'pole_clearance':str(B-xmax)})
  total=F(0);counts={str(x):0 for x in RHOS}
  for (f,j),v in c.items():
   z,rho=min((cheb_source_tail(f,j,v,rho,H),rho) for rho in RHOS)
   total+=z;counts[str(rho)]+=1
  out['panels'].append({'panel':i,'center':str(C),'halfwidth':str(H),
   'true_piece':[str(l),str(r)],'outer_analytic':[str(C-H),str(C+H)],
   'ellipses':admissible,'generator_512_tail':str(total),
   'chosen_rhos':counts,'candidate_less_1e_minus20':total<F(1,10**20),
   'true_z_tail_certified':False})
  print('J5 panel',i,'source candidate',float(total),'rhos',counts,flush=True)
 Path(args.output).parent.mkdir(parents=True,exist_ok=True)
 Path(args.output).write_text(json.dumps(out,indent=2)+'\n')
 print('NF438 J5 overlap-panel geometry PASS; true J5 signed integral OPEN')
if __name__=='__main__':main()
