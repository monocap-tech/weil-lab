#!/usr/bin/env python3
"""Exact fixed-arch/global-prime-budget barrier for NF28's raw response.
Inherited source intervals are inputs, not recomputed complete Weil sources.
"""
from fractions import Fraction as F
from pathlib import Path
from itertools import product
import argparse,contextlib,io,runpy,sys,json,hashlib

def run(source,output):
 raw=Path(source).read_bytes()
 assert hashlib.sha256(raw).hexdigest()=='27819654bc8aa7f9e98f1ef8638c99f9afbcac07dabd2d6c079bfbfbde70e8c1'
 helper=Path(__file__).with_name('dne19_prime_input.py')
 assert hashlib.sha256(helper.read_bytes()).hexdigest()=='8695e20210d8e832947d2126855210451083dee3759c3dd2af1c60823ada60a9'
 saved=sys.argv;sys.argv=[str(helper),str(Path(output).with_suffix('.prime.json'))]
 try:
  with contextlib.redirect_stdout(io.StringIO()):d=runpy.run_path(str(helper))
 finally:sys.argv=saved
 I=d['I'];pos=d['position'];bv=d['band_value'];powers=d['powers']
 cuts=d['sort'](powers[1][0]+powers[2][0]);num=I(0);den=I(0)
 checks=0
 for l,h in zip(cuts,cuts[1:]):
  width=pos(h)-pos(l);assert width.lo>0;checks+=1
  x=bv(l,h,*powers[1]);y=bv(l,h,*powers[2])
  num=num+width*x*y;den=den+width*x*x
 assert num.lo>0 and den.lo>0;checks+=2
 ray=num/den
 # Independent signed-word domain enumeration: <1,P^k 1> equals the
 # sum of coefficient products times all-prefix clipped domain lengths.
 steps=[(n,s) for n in d['PRIMES'] for s in (-1,1)]
 moments={};counts={}
 for depth in (2,3):
  total=I(0);surviving=0
  for word in product(steps,repeat=depth):
   q=F(1);l=d['LEFT'];h=d['RIGHT'];amp=I(1)
   for n,s in word:
    q*=F(n)**s;ll=(-1,1/q);hh=(1,1/q)
    if d['before'](l,ll):l=ll
    if d['before'](hh,h):h=hh
    amp=amp*d['amp'][n]
   if l==h or d['before'](h,l):continue
   width=pos(h)-pos(l);assert width.lo>0;checks+=1
   total=total+amp*width;surviving+=1
  moments[depth]=total;counts[depth]=surviving
 assert counts=={2:82,3:464};checks+=1
 for a,b in ((den,moments[2]),(num,moments[3])):
  assert a.lo<=b.hi and b.lo<=a.hi;checks+=1
 ray_words=moments[3]/moments[2]
 assert ray.lo<=ray_words.hi and ray_words.lo<=ray.hi;checks+=1
 # Both are rigorous lower bounds for the full physical operator norm.
 ray_lower=max(ray.lo,ray_words.lo)
 L=F(2772351243732,10**12);ceiling=L-ray_lower;k=F(11,25)
 assert F(2124147,10**6)<ray_lower and ceiling<F(648204,10**6);checks+=2
 rows=[]
 for r in json.loads(raw)['parity_certificates']:
  q=list(map(F,r['original_finite_two_direction_energy'][1][1]))
  p=list(map(F,r['original_complete_mixed_residual_Gram'][1][1]))
  assert 0<q[0]<=q[1] and 0<p[0]<=p[1];checks+=2
  rho=(p[0]/q[1],p[1]/q[0]);inherited=list(map(F,r['retained_response_residual_square_over_native_energy']))
  assert rho[0]<=inherited[1] and inherited[0]<=rho[1];checks+=1
  assert rho[0]>ceiling>k;checks+=1
  # Strictly negative on w throughout every k' in (0,ceiling].
  at_floor=(q[0]-p[1]/k,q[1]-p[0]/k)
  best=q[1]-p[0]/ceiling
  assert at_floor[1]<0 and best<0;checks+=2
  need=1-k/rho[0];arch_need=ray_lower+rho[0]
  guard=F(69827,10**5) if r['parity']=='even' else F(80553,10**5)
  assert rho[0]>guard and arch_need>L;checks+=2
  rows.append({'parity':r['parity'],'w_native_energy':[str(x) for x in q],
   'w_original_full_high_source_square':[str(x) for x in p],
   'necessary_floor_strict_interval':[str(x) for x in rho],
   'coarse_w_diagonal_at_11_over_25':[str(x) for x in at_floor],
   'best_fixed_arch_global_norm_budget_w_diagonal_upper':str(best),
   'source_square_reduction_fraction_necessary_strict_lower':str(need),
   'fixed_global_norm_arch_budget_needed_strict_lower':str(arch_need),
   'display_required_floor_lower':float(rho[0]),'display_current_diagonal_upper':float(at_floor[1]),
   'display_needed_source_reduction_lower':float(need),
   'display_needed_arch_budget_lower':float(arch_need),
   'stronger_floor_still_rejects_raw_w':True,
   'all_global_prime_norm_optimizations_with_fixed_arch_budget_rejected':True})
 # Genuine signed crossings and whole-mass positive-ground-level controls.
 controls=[];b=F(1,10);c=k
 for eps in (F(1,10000),F(0),F(-1,10000)):
  a=b*b/c+eps;s=a-b*b/c
  assert s==eps and (s>0)==(eps>0);checks+=2
  controls.append({'kind':'genuine_crossing','exact_Schur':str(s)})
 for mu in (F(1,10**40),F(1,100),F(1,20)):
  a=b*b/c+mu;cc=c+mu;v=(F(1),-b/c)
  assert a*v[0]+b*v[1]==mu*v[0] and b*v[0]+cc*v[1]==mu*v[1]
  assert a-b*b/cc>0;checks+=2
  controls.append({'kind':'positive_whole_mass_ground_level','mu':str(mu)})
 # Estimator rejection is not negativity of the underlying form.
 assert 1-F(7,10)**2>0 and 1-F(7,10)**2/k<0;checks+=2
 controls.append({'kind':'positive_actual_form_rejected_by_coarse_floor',
  'matrix':[['1','7/10'],['7/10','1']],'actual_Schur':'51/100','coarse_floor':'11/25'})
 return {'stage':'DNE19','aperture':'53/50','grid_digits':d['PREC'],'log_terms':d['TERMS'],
  'source_head':'1b227864aa6398e59922fde470f371fb9b72dc11',
  'coupled_head_read_only':'ae03e419ef9b975ee219806873c755b4d3149982',
  'source_input_sha256':hashlib.sha256(raw).hexdigest(),
  'prime_producer_sha256':hashlib.sha256(helper.read_bytes()).hexdigest(),
  'Rayleigh_trial':'P 1','Rayleigh_numerator':num.data(),'Rayleigh_denominator':den.data(),
  'independent_word_moments':{str(n):v.data() for n,v in moments.items()},
  'surviving_word_counts':counts,'prime_operator_norm_strict_lower':str(ray_lower),
  'fixed_arch_minus_pole_budget':str(L),'fixed_budget_floor_strict_ceiling':str(ceiling),
  'display_prime_norm_lower':float(ray_lower),'display_floor_ceiling':float(ceiling),
  'parity_rows':rows,'exact_rational_assertions':checks,'controls':controls,
  'DNE18_restricted_gap_preserved':'1/'+str(10**35),
  'new_positive_subspace_certified':False,'actual_high_floor_upper_bound_claimed':False,
  'complete_source_identities_replayed':False,'whole_aperture_positive':False,
  'RH':False,'F4':False,'Lean':False}

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('--output',required=True);args=p.parse_args()
 result=run(args.source,args.output);Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({key:result[key] for key in ('stage','display_prime_norm_lower','display_floor_ceiling','exact_rational_assertions')}))
 print(json.dumps([{key:r[key] for key in ('parity','display_required_floor_lower','display_current_diagonal_upper','display_needed_source_reduction_lower','display_needed_arch_budget_lower')} for r in result['parity_rows']]))
