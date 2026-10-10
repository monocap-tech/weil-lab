#!/usr/bin/env python3
"""Exact interval Schur certificate, w=P^7 1, original six clipped primes.
Cut locations remain symbolic +/-a+log(q), q rational. Every ordering and
support-clipping decision is verified by rational log enclosures.
"""
from fractions import Fraction as F
from math import isqrt
from functools import lru_cache
import json,sys,os,hashlib
PREC=int(os.environ.get('DNE39_GRID_DIGITS','60'));GRID=10**PREC
TERMS=int(os.environ.get('DNE39_LOG_TERMS','220'))
A=F(53,50);PRIMES=(2,3,4,5,7,8);LIMIT=F(21941,10000)
class I:
 def __init__(s,l,h=None):
  if isinstance(l,I):s.lo,s.hi=l.lo,l.hi;return
  l=F(l);h=l if h is None else F(h);assert l<=h
  s.lo=F((l*GRID).__floor__(),GRID);s.hi=F((h*GRID).__ceil__(),GRID)
 def __add__(s,t):
  t=I(t);return I(s.lo+t.lo,s.hi+t.hi)
 __radd__=__add__
 def __neg__(s):return I(-s.hi,-s.lo)
 def __sub__(s,t):return s+-I(t)
 def __mul__(s,t):
  t=I(t);v=[x*y for x in (s.lo,s.hi) for y in (t.lo,t.hi)];return I(min(v),max(v))
 __rmul__=__mul__
 def __truediv__(s,t):
  t=I(t);assert t.lo>0;return s*I(1/t.hi,1/t.lo)
 def data(s):return [str(s.lo),str(s.hi)]
@lru_cache(None)
def log(q):
 q=F(q);assert q>0
 if q==1:return I(0)
 if q<1:return -log(1/q)
 z=(q-1)/(q+1);p=z;v=F(0)
 for j in range(TERMS):v+=2*p/F(2*j+1);p*=z*z
 e=2*p/(F(2*TERMS+1)*(1-z*z));return I(v,v+e)
def sqrt(n):
 k=isqrt(n*GRID*GRID);return I(F(k,GRID),F(k+1,GRID))
amp={n:log(2 if n in (4,8) else n)/sqrt(n) for n in PRIMES}
LEFT=(-1,F(1));RIGHT=(1,F(1))
@lru_cache(None)
def position(key):return I(key[0]*A)+log(key[1])
def before(x,y):
 if x==y:return False
 assert position(x).hi<position(y).lo or position(y).hi<position(x).lo
 return position(x).hi<position(y).lo
def sort(keys):
 # Floating values propose an order; exact nonoverlap alone accepts it.
 keys=sorted(set(keys),key=lambda k:float(position(k).lo))
 for x,y in zip(keys,keys[1:]):assert before(x,y)
 return keys
def shifted(key,n,sign):return key[0],key[1]/F(n)**sign
def apply(cuts,vals):
 events={LEFT:I(0),RIGHT:I(0)};terms=0
 for n in PRIMES:
  for sign in (-1,1):
   for l,h,v in zip(cuts,cuts[1:],vals):
    l=shifted(l,n,sign);h=shifted(h,n,sign)
    if l!=LEFT and before(l,LEFT):l=LEFT
    if h!=RIGHT and before(RIGHT,h):h=RIGHT
    if l==h or before(h,l):continue
    assert (l==LEFT or before(LEFT,l)) and (h==RIGHT or before(h,RIGHT))
    vv=amp[n]*v
    events[l]=events.get(l,I(0))+vv;events[h]=events.get(h,I(0))-vv;terms+=1
 cuts=sort(events);v=I(0);vals=[]
 for x in cuts[:-1]:
  v=v+events[x];assert v.lo>0;vals.append(v)
 return cuts,vals,terms
def band_value(l,h,cuts,vals):
 # Union bands have endpoints in the symbolic cuts. No midpoint probing or
 # rounded boundary is used to choose their exact containing source band.
 for a,b,v in zip(cuts,cuts[1:],vals):
  if (l==a or before(a,l)) and (h==b or before(h,b)):return v
 raise AssertionError('Uncovered symbolic band')
def run(output):
 cuts=[LEFT,RIGHT];vals=[I(1)];powers=[(cuts,vals)];term_counts=[]
 for k in range(8):
  cuts,vals,terms=apply(cuts,vals);powers.append((cuts,vals));term_counts.append(terms)
 wcuts,wvals=powers[7];pcuts,pvals=powers[8]
 union=sort(wcuts+pcuts);rows=[];worst=F(0)
 for l,h in zip(union,union[1:]):
  den=band_value(l,h,wcuts,wvals);num=band_value(l,h,pcuts,pvals)
  assert den.lo>0
  ratio=num/den;assert ratio.hi<LIMIT;worst=max(worst,ratio.hi)
  rows.append({'left':[l[0],str(l[1])],'right':[h[0],str(h[1])],
   'weight':den.data(),'prime_weight':num.data(),'row_ratio_upper':str(ratio.hi)})
 out={'stage':'DNE39','aperture':str(A),'grid_digits':PREC,'log_terms':TERMS,
  'prime_powers':list(PRIMES),'both_orientations':True,'weight':'P^7 1',
  'weight_is_actual_positive_step_function':True,
  'symbolic_cut_order_verified':True,'all_clipped_bands_included':True,
  'power_band_counts':[len(v) for c,v in powers], 'clipped_term_counts':term_counts,
  'union_band_count':len(rows),'minimum_weight_lower':str(min(v.lo for v in wvals)),
  'rigorous_max_row_ratio_upper':str(worst),'certified_prime_norm_strict_upper':str(LIMIT),
  'inherited_arch_minus_pole_strict_lower':'2772351243732/1000000000000',
  'derived_high_raw_strict_lower':str(F(2772351243732,10**12)-LIMIT),
  'certified_original_F112_lower':'289/500',
  'norm_guard_passed':worst<LIMIT,
  'high_floor_guard_passed':F(2772351243732,10**12)-LIMIT>F(289,500),
  'power_bands':[{'cuts':[[k[0],str(k[1])] for k in c],'values':[v.data() for v in vv]} for c,vv in powers], 'rows':rows,'whole_aperture_positive':False,'RH':False,'Lean':False}
 open(output,'w').write(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:out[k] for k in ('power_band_counts','union_band_count','minimum_weight_lower','rigorous_max_row_ratio_upper','derived_high_raw_strict_lower','norm_guard_passed','high_floor_guard_passed')},indent=2))
 
if __name__=='__main__':run(sys.argv[1])
