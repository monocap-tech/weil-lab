#!/usr/bin/env python3
"""Independent path enumeration, inherited arch replay and full-high gates."""
from fractions import Fraction as F
from math import isqrt
from itertools import product
from functools import lru_cache
import json,sys
import dne17_nf10_complement_input as nf10
A=F(53,50);GRID=10**80;steps=[(n,s) for n in (2,3,4,5,7,8) for s in (-1,1)]
checks=0
@lru_cache(None)
def log(q):
 q=F(q)
 if q==1:return F(0),F(0)
 if q<1:
  l,h=log(1/q);return -h,-l
 z=(q-1)/(q+1);p=z;v=F(0)
 for j in range(320):v+=2*p/F(2*j+1);p*=z*z
 h=v+2*p/(F(641)*(1-z*z))
 return F((v*GRID).__floor__(),GRID),F((h*GRID).__ceil__(),GRID)
amp={}
for n in (2,3,4,5,7,8):
 l,h=log(F(2 if n in (4,8) else n));k=isqrt(n*GRID*GRID)
 amp[n]=(l/F(k+1,GRID),h/F(k,GRID))
@lru_cache(None)
def pos(key):
 l,h=log(key[1]);return key[0]*A+l,key[0]*A+h
def le(x,y):
 global checks
 if x==y:return True
 a,b=pos(x);c,d=pos(y);assert b<c or d<a;checks+=1
 return b<c
LEFT=(-1,F(1));RIGHT=(1,F(1))
def terms(depth):
 result=[]
 for word in product(steps,repeat=depth):
  q=F(1);l=LEFT;h=RIGHT;lo=hi=F(1)
  for n,s in word:
   q*=F(n)**s;ll=(-1,1/q);hh=(1,1/q)
   if le(l,ll):l=ll
   if le(hh,h):h=hh
   a,b=amp[n];lo*=a;hi*=b
  if not le(h,l):result.append((l,h,lo,hi))
 return result
paths={k:terms(k) for k in (2,3)}
def value(l,h,k):
 lo=hi=F(0)
 for a,b,x,y in paths[k]:
  if le(a,l) and le(h,b):lo+=x;hi+=y
 return lo,hi
prim=json.load(open(sys.argv[1]));replay=json.load(open(sys.argv[2]));worst=F(0)
assert prim['weight']=='P^2 1' and prim['union_band_count']==81
assert len(prim['rows'])==len(replay['rows'])==81
for row,rr in zip(prim['rows'],replay['rows']):
 l=(row['left'][0],F(row['left'][1]));h=(row['right'][0],F(row['right'][1]));assert le(l,h)
 assert row['left']==rr['left'] and row['right']==rr['right'];checks+=1
 w=value(l,h,2);p=value(l,h,3);assert w[0]>0
 ratio=p[1]/w[0];assert ratio<F(233,100);worst=max(worst,ratio);checks+=2
 for field,v in [('weight',w),('prime_weight',p)]:
  for d in (row,rr):
   a,b=map(F,d[field]);assert a<=v[1] and v[0]<=b;checks+=1
# Fresh execution of the original depth-six mass formulas. Their analytic
# Bessel inequality and arch lower symbol remain the named NF10 dependency.
rate=nf10.rate_lower();assert rate>80
masses={t:nf10.integrated_mass_upper(t) for t in (14,15,16)}
high=lambda t:(nf10.LOG[t][0]-F(7,216*t*t),nf10.LOG[t][1]-F(7,216*t*t))
h14,h15,h16=(high(t) for t in (14,15,16))
arch=h16[0]-(h14[1]+F(27,5))*masses[14]-(h15[1]-h14[0])*masses[15]-(h16[1]-h15[0])*masses[16]
from math import factorial
pole=16*A*(A/2)**224/F(factorial(112)**2)
assert arch-pole>F(2772351243732,10**12);checks+=1
floor=F(11,25);assert F(2772351243732,10**12)-F(233,100)>floor;checks+=1
gates=[]
for parity in ('even','odd'):
 data=json.load(open(sys.argv[3]+'/'+parity+'_replay_certificate.json'))
 el,eh=map(F,data['energy']);pl,ph=map(F,data['P2'])
 lower=el-ph/floor;fraction=1-ph/(floor*el)
 assert lower>0
 assert fraction>(F(1,5) if parity=='even' else F(9,25))
 checks+=1
 gates.append({'parity':parity,'complete_source_ratio_upper':str(ph/el),
  'whole_high_Schur_strict_lower':str(lower),
  'fraction_of_S2_strict_lower':str(fraction),
  'display_Schur_lower':float(lower),'display_fraction_lower':float(fraction),
  'full_high_directional_gate_passed':True})
# Exact crossing and whole-mass-shift controls for the same response gate.
c=floor;b=F(1,10);controls=[]
for eps in (F(1,10000),F(0),F(-1,10000)):
 a=b*b/c+eps;schur=a-b*b/c
 assert schur==eps and (a>b*b/c)==(eps>0);checks+=2
 controls.append({'kind':'genuine_crossing','epsilon':str(eps),'gate_passes':eps>0,'exact_Schur':str(schur)})
for mu in (F(1,10**40),F(1,100),F(1,20)):
 # The rank-one form at mu=0 has null vector (1,-b/c).
 # Adding mu to BOTH diagonals gives that vector true eigenlevel mu.
 a=b*b/c+mu;cc=c+mu;schur=a-b*b/cc
 assert schur>0
 v=(F(1),-b/c)
 assert a*v[0]+b*v[1]==mu*v[0]
 assert b*v[0]+cc*v[1]==mu*v[1]
 assert (a-mu)*(cc-mu)-b*b==0;checks+=4
 controls.append({'kind':'positive_ground_level','mu':str(mu),'whole_shift_null':True,'gate_passes':True})
out={'stage':'DNE17','status':'PASS','independent_word_depths':[2,3],
 'surviving_word_counts':{str(k):len(v) for k,v in paths.items()},
 'all_81_row_bounds_independently_verified':True,
 'independent_max_row_ratio_upper':str(worst),
 'exact_rational_assertions':checks,'fresh_arch_pole_replay_passed':True,
 'arch_minus_pole_strict_lower':'2772351243732/1000000000000',
 'original_infinite_F112_floor':'11/25','directional_gates':gates,'abstract_controls':controls,
 'whole_aperture_positive':False,'RH':False,'Lean':False}
open(sys.argv[4],'w').write(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ('status','surviving_word_counts','exact_rational_assertions','directional_gates')},indent=2))
