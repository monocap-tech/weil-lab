#!/usr/bin/env python3
"""Exact finite-source perturbation budget; diagnostics remain non-certifying."""
from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal as D,getcontext
import argparse,json,hashlib
getcontext().prec=90
def dec(q):
 q=F(q);return D(q.numerator)/D(q.denominator)
def center(pair):return (F(pair[0])+F(pair[1]))/2
def run(root,replay):
 root=Path(root);replay=Path(replay)
 c63=json.loads((root/'notes/data/RPB108_FIXED_TRIALS_CC63_CERTIFICATE_20261009.json').read_text())
 c65=json.loads((root/'notes/data/RPB108_OBSERVED_SOURCE_TRIAL_CC65_CERTIFICATE_20261009.json').read_text())
 nf24=json.loads((replay/'RPB108_NF24_COMPENSATED_SOURCE_TARGETS_20261009.json').read_text())
 # Analytic inequalities are justified in the accompanying proof report.
 # sqrt(2n+1)<16 for n<=115; Cauchy |r|<=500/19; |c|<4.
 sector={'singular_difference':F(115*116,2)*16,'endpoint_logs':F(48),
         'constant':F(4),'regular_convolution':F(2)*F(53,50)*F(500,19),
         'six_signed_prime_pairs':F(36),'two_signed_pole_sources':4*F(53,50)*9}
 total=sum(sector.values());B=F(200000);assert total<B
 exact=[]
 for a in c63['fixed_rational_trials']:
  nf=next(w for w in nf24['authenticated_compensated_targets'] if w['parity']==a['parity'])
  ids=a['indices'];coefs=[F(n)/F(a['coefficient_denominator']) for n in a['numerators']]
  ncoefs=list(map(F,nf['retained_coefficients']+nf['exact_rational_high_compensation']))
  assert coefs[:56]==ncoefs[:56]
  delta=sum(abs(x-y) for x,y in zip(coefs[56:],ncoefs[56:]))
  bound=B*delta;assert bound<F(8,10**70)
  floor=F(14,5) if a['parity']=='even' else F(289,100)
  # ||u||²<2e-120 from CC63; sqrt2<2 gives ||u||<2e-60.
  galerkin_error=2*B*F(2,10**60)/floor
  assert galerkin_error<F(4,10**55)
  energy_error=F(2,10**120)/floor;assert energy_error<F(1,10**120)
  exact.append(dict(parity=a['parity'],CC63_NF24_coefficient_l1_difference=str(delta),
   complete_original_source_difference_upper=str(bound),
   fixed_CC63_to_exact_H2_Galerkin_source_difference_upper=str(galerkin_error),
   fixed_CC63_to_exact_H2_Galerkin_energy_difference_upper=str(energy_error),
   no_bounded_full_L_assumption=True))
 diagnostics=[]
 names=['cc65_diag_96_64.json','cc65_diag_128_96.json']
 loaded=[json.loads((replay/n).read_text()) for n in names]
 for index,d in enumerate(loaded):
  assert d['certifying'] is False and d['decimal_precision']==90
  rows=[]
  for w in c65['combined_source_trials']:
   p=w['parity'];r=d[p]
   low=sum((center(z)**2 for z in w['retained_source_projection_intervals'].values()),F(0))
   known=sum((center(z)**2 for z in w['observed_high_coordinate_intervals'].values()),F(0))
   P=D(r['physical_residual_square']);full=D(r['complete_source_square']);Q=dec(center(w['combined_energy']))
   pythagoras=abs(full-P-dec(low))/dec(low)
   assert pythagoras<D('1e-10')
   j=str(w['new_observed_index']);observed=dec(center(w['observed_high_coordinate_intervals'][j]))
   projection_error=abs(D(r['projected_high_source'][j])-observed)/abs(observed)
   assert projection_error<D('1e-10')
   omitted=P-dec(known);budget=dec(w['unseen_source_square_strict_budget_lower'])
   assert omitted>0
   rows.append(dict(parity=p,full_high_source_square_over_Q=str(P/Q),
    omitted_source_square=str(omitted),omitted_source_square_over_certified_budget=str(omitted/budget),
    numerical_Pythagoras_relative_discrepancy=str(pythagoras),
    numerical_authenticated_projection_relative_discrepancy=str(projection_error),
    rigorous_integration_remainder_available=False,coarse_gate_failure_certified=False))
  diagnostics.append(dict(inner_order=d['inner_order'],outer_order=d['outer_order'],rows=rows,certifying=False))
 for p in ['even','odd']:
  x=D(loaded[0][p]['physical_residual_square']);y=D(loaded[1][p]['physical_residual_square'])
  assert abs(x-y)/abs(y)<D('1e-10')
 return dict(milestone='CC67',status='PASS',exact_sector_source_norm_bounds={k:str(v) for k,v in sector.items()},
  all_physical_Legendre_modes_degree_at_most115_source_norm_strict_upper=str(B),
  finite_transfer_certificates=exact,CC65_complete_source_diagnostics=diagnostics,
  diagnostic_producer_SHA256=hashlib.sha256((replay/'diagnose_native_compensated_source_nf24_106.py').read_bytes()).hexdigest(),
  complete_source_norm_certified=False,coarse_gate_failure_certified=False,
  whole_aperture_positive=False,all_cap_frame=False,RH=False,Lean=False)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--root',required=True);p.add_argument('--replay',required=True);p.add_argument('--output',required=True);a=p.parse_args()
 Path(a.output).write_text(json.dumps(run(a.root,a.replay),indent=2)+'\n');print('CC67 finite-source transfer and non-certifying diagnostic checks PASS')
