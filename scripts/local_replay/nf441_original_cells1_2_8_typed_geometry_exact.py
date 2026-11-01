#!/usr/bin/env python3
"""NF441: exact ORIGINAL positive physical J1/J2/J8 support and method topology.

Separate NF405 regular translated u4 activation from NF407 principal r jump
at the genuine NF406 irrational seams. J1, J2 source-analytic overlapping
coverings preserve the source's original signed support; J8 terminates at
+B, where endpoint log and 2048 image convergence prevent old uniform
Bernstein transfer. No sign from a candidate source-generator triangle.
"""
import argparse,hashlib,json,sys
from fractions import Fraction as F
from pathlib import Path
from nf425_original_cell6_chebyshev_existence_exact import source
from nf433_original_cell3_cell7_branch_ellipse_router_exact import branch_for_cell,cheb_source_tail
from nf438_original_cells4_5_regular_principal_geometry_exact import principal_jump
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
B=F(11,10)
PRIMES=(2,3,4,5,7,8,9)
SRC='0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce'
SEAM='c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675'
GEOM={
 1:((F(7,10000),F(8,10000)),),
 2:((F(55,1000),F(55,1000)),(F(148,1000),F(58,1000)),(F(243,1000),F(53,1000)))}
CUTS={1:(),2:(F(1,10),F(39,200))}
def load(path):
 raw=Path(path).read_bytes()
 return json.loads(raw),hashlib.sha256(raw).hexdigest()
def main():
 a=argparse.ArgumentParser()
 a.add_argument('--source',default='notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json')
 a.add_argument('--seams',default='notes/data/provisional/NF406_original_prime_support_partition_exact.json')
 a.add_argument('--physical',default='notes/data/provisional/NF405_original_compact_physical_kernel_exact.json')
 a.add_argument('--principal',default='notes/data/provisional/NF407_original_prime_jump_log_power_exact.json')
 a.add_argument('--nf410',default='notes/data/provisional/NF410_original_signed_taylor_moments.json')
 a.add_argument('--output',required=True)
 args=a.parse_args()
 s,sha=load(args.source);k,ksha=load(args.seams)
 physical,psha=load(args.physical);p,prsha=load(args.principal);nf410,nfsha=load(args.nf410)
 assert sha==SRC and ksha==SEAM
 assert k['original_nf405_compact_kernel_sha256']==psha
 assert p['original_nf406_seams_sha256']==ksha
 assert nf410['original_nf406_source_sha256']==ksha
 assert nf410['original_nf407_source_sha256']==prsha
 assert len(k['certified_ordered_knots'])==17
 assert physical['actual_original_prime_power_shifts']==list(PRIMES)
 assert s['original_dimension']==242 and len(s['original_exact_native_original_four_critical_coefficients_mid_radius'])==4
 assert len(s['original_source_critical_sine_frequencies'])==32
 assert all(z['W_ODD_NEG']==z['RH']=='OPEN' for z in (s,k,physical,p,nf410))
 knots=k['certified_ordered_knots']
 assert [knots[i]['label'] for i in (8,9,10,15,16)]==['0','B-log(3)','-B+log(4)','-B+log(9)','+B']
 logs={int(v['n']):(F(v['log_lower']),F(v['log_upper'])) for v in k['original_prime_power_log_shifts']}
 assert set(logs)==set(PRIMES)
 coeff,pole,S0=source(s)
 assert len(coeff)==273 and S0<F(1,10**700)
 assert max(f for f,k in coeff)<883 and max(k for f,k in coeff)<=13
 assert sum((abs(q)*B**j for (f,j),q in coeff.items()),abs(pole))<10**160
 out={'pass':'NF441','standing':'SOURCE-EXACT ORIGINAL J1/J2/J8 REGULAR/PRINCIPAL TYPES; J1/J2 ANALYTIC PANEL SOURCE TAIL CANDIDATES; J8 +B ENDPOINT METHOD STOP',
 'source_sha256':sha,'seams_sha256':ksha,'physical_sha256':psha,'principal_sha256':prsha,
 'original_NF410_sha256':nfsha,'original_246_source_count':246,'original_273_group_count':273,
 'source_physical_cells':{},'original_signed_J1_J2_J8_certified':False,
 'W_ODD_NEG':'OPEN','RH':'OPEN'}
 for cell,leftidx,rightidx in ((1,8,9),(2,9,10),(8,15,16)):
  left,right=knots[leftidx],knots[rightidx]
  lo,lu=F(left['low']),F(left['high'])
  rl,ru=F(right['low']),F(right['high'])
  assert 0<=lo<=lu<rl<=ru<=B
  minus=[];plus=[];jump=[];inact=[]
  for n in PRIMES:
   m,q=branch_for_cell(n,lu,rl,logs,left['label'],right['label'])
   if m:minus.append(n)
   if q:plus.append(n)
   (jump if principal_jump(n,lu,rl,left['label'],right['label'],logs) else inact).append(n)
  expected={
   1:([2,3],[2,3],[],list(PRIMES)),
   2:([2,3],[2],[3],[2,4,5,7,8,9]),
   8:(list(PRIMES),[],list(PRIMES),[])}[cell]
  assert (minus,plus,jump,inact)==expected,(cell,minus,plus,jump,inact)
  old=nf410['original_positive_original_physical_cells'][cell-1]
  assert old['cell']==cell and old['left_label']==left['label'] and old['right_label']==right['label']
  p0=tuple(map(F,old['signed_original_p_moments_by_degree_0_to_3'][0]))
  assert p0[1]<0
  data={'cell':cell,'true_left_seam':left['label'],'true_right_seam':right['label'],
   'original_regular_minus':minus,'original_regular_plus':plus,
   'original_principal_jump_active':jump,'original_principal_jump_inactive':inact,
   'original_NF410_p0_interval':list(map(str,p0)),
   'true_principal_p0_negative_NF410':True,'panels':[],
   'original_complete_signed_pz_z2_certified':False}
  if cell in (1,2):
   cuts=CUTS[cell]
   pieces=[(lu,*cuts),(cuts[0],cuts[1],rl)] if False else None
   endpoints=[lo]+list(cuts)+[ru]
   assert len(endpoints)==len(GEOM[cell])+1
   for idx,((C,H),a0,b0) in enumerate(zip(GEOM[cell],endpoints[:-1],endpoints[1:]),1):
    assert C-H<a0<b0<C+H and C+H<B
    # Original fixed source analytic extension is allowed to leave the
    # positive physical cell as long as integration stays inside it.
    # Do not equate this continuation with the physically switched z.
    admissible=[]
    for rho in (F(2),F(3),F(4),F(5)):
     xlo=C-H*(rho+1/rho)/2
     xhi=C+H*(rho+1/rho)/2
     assert -B<xlo<xhi<B
     admissible.append({'rho':str(rho),'left':str(xlo),'right':str(xhi),
                        'B_pole_clearance':str(B-xhi)})
    tri=F(0);choice={str(x):0 for x in (2,3,4,5)}
    for (f,j),c in coeff.items():
     v,rho=min((cheb_source_tail(f,j,c,rho,H),rho) for rho in (F(2),F(3),F(4),F(5)))
     tri+=v;choice[str(rho)]+=1
    assert sum(choice.values())==273
    data['panels'].append({
      'panel':idx,'center':str(C),'halfwidth':str(H),
      'original_true_integration_piece_bounds':[str(a0),str(b0)],
      'analytic_ellipse_source_fixed_branch_admissible':admissible,
      'candidate_512_generator_tail_exact':str(tri),
      'candidate_512_generator_tail_lt_1e_minus20':tri<F(1,10**20),
      'source_optimal_rho_counts':choice,'original_complete_native_response':False})
    print('NF441 original cell',cell,'panel',idx,'generator tail upper',float(tri),'mode choices',choice,flush=True)
  else:
   assert ru==B
   data['whole_interval_B_endpoint_singular']=True
   data['original_principal_q_has_log_B_over_B_minus_x_unbounded']=True
   data['original_2048_image_geometric_ratio_tends_to_1_as_x_to_B']=True
   data['old_uniform_elliptic_full_cell_certificate_available']=False
   data['endpoint_weighted_or_geometric_pieces_required']=True
   data['standing']='METHOD STOP on whole-cell8 fixed uniform Bernstein / 2048 image bound, not a failure of positivity'
  out['source_physical_cells'][str(cell)]=data
  print('NF441 original cell',cell,'regular',minus,plus,'principal',jump,'p0 old sign',float(p0[0]),flush=True)
 dest=Path(args.output);dest.parent.mkdir(parents=True,exist_ok=True)
 dest.write_text(json.dumps(out,indent=2)+'\n')
 print('NF441 PASS exact original J1/J2/J8 source types; original signed cells OPEN')
if __name__=='__main__': main()
