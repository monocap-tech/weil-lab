#!/usr/bin/env python3
"""Exact interval Schur certificate, adaptive positive power weight, original six clipped primes.
Cut locations remain symbolic +/-a+log(q), q rational. Every ordering and
support-clipping decision is verified by rational log enclosures.
"""
from fractions import Fraction as F
from math import isqrt
from functools import lru_cache
import json,sys,os,hashlib,gzip,base64
PREC=int(os.environ.get('DNE43_GRID_DIGITS','60'));GRID=10**PREC
TERMS=int(os.environ.get('DNE43_LOG_TERMS','220'))
A=F(53,50);PRIMES=(2,3,4,5,7,8);LIMIT=F(216935,100000)
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
def base_log(q):
 q=F(q);assert q>0
 if q==1:return I(0)
 if q<1:return -base_log(1/q)
 z=(q-1)/(q+1);p=z;v=F(0)
 for j in range(TERMS):v+=2*p/F(2*j+1);p*=z*z
 e=2*p/(F(2*TERMS+1)*(1-z*z));return I(v,v+e)
@lru_cache(None)
def log(q):
 q=F(q)
 if q<1:return -log(1/q)
 k=0
 while q>=2:q/=2;k+=1
 return base_log(q)+k*base_log(F(2))
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
 cuts=[LEFT,RIGHT];vals=[I(1)];powers=[(cuts,vals)];term_counts=[];diagnostics=[]
 for k in range(25):
  cuts,vals,terms=apply(cuts,vals);powers.append((cuts,vals));term_counts.append(terms)
  if k<7:continue
  wc,wv=powers[-2];pc,pv=powers[-1];union=sort(wc+pc);rows=[];worst=F(0);wi=pi=0
  for l,h in zip(union,union[1:]):
   while wi+1<len(wv) and (wc[wi+1]==l or before(wc[wi+1],l)):wi+=1
   while pi+1<len(pv) and (pc[pi+1]==l or before(pc[pi+1],l)):pi+=1
   den=wv[wi];num=pv[pi];assert den.lo>0;ratio=num/den;worst=max(worst,ratio.hi)
   rows.append(dict(left=[l[0],str(l[1])],right=[h[0],str(h[1])],weight=den.data(),prime_weight=num.data(),row_ratio_upper=str(ratio.hi)))
  diagnostics.append(dict(weight_power=k,bands=len(rows),max_row_ratio_upper=str(worst)))
  print('power',k,'bands',len(rows),'upper',float(worst),flush=True)
  if worst<LIMIT:break
 assert worst<LIMIT,'target not reached within configured power cap'
 out=dict(stage='DNE43',parent='b6b5cbe5a9f59dbf9f03ae931083289dbf11bf13',aperture=str(A),grid_digits=PREC,log_terms=TERMS,prime_powers=list(PRIMES),both_orientations=True,weight_power=k,weight=f'P^{k} 1',power_band_counts=[len(v) for c,v in powers],clipped_term_counts=term_counts,union_band_count=len(rows),minimum_weight_lower=str(min(v.lo for v in wv)),rigorous_max_row_ratio_upper=str(worst),certified_prime_norm_strict_upper=str(LIMIT),inherited_arch_minus_pole_strict_lower='2772351243732/1000000000000',derived_high_raw_strict_lower=str(F(2772351243732,10**12)-LIMIT),certified_original_F112_lower='603/1000',power_bands=[dict(cuts=[[k[0],str(k[1])] for k in c],values=[v.data() for v in vv]) for c,vv in powers],rows=rows,power_diagnostics=diagnostics,symbolic_cut_order_verified=True,all_clipped_bands_included=True,norm_guard_passed=True,high_floor_guard_passed=F(2772351243732,10**12)-LIMIT>F(603,1000),whole_aperture_positive=False,RH=False,Lean=False)
 b=(json.dumps(out,indent=2)+'\n').encode();open(output,'wb').write(base64.b64encode(gzip.compress(b,mtime=0))+b'\n' if output.endswith('.gz.b64') else b)
if __name__=='__main__':run(sys.argv[1])
