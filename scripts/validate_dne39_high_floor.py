#!/usr/bin/env python3
"""Independent positive band recurrence audit, not an event-sweep replay."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from math import isqrt
from bisect import bisect_right
import argparse,json,hashlib
from dne17_nf10_complement_input import rate_lower,integrated_mass_upper,LOG,A,PI,K

GRID=10**100
def outward(l,h):return (F((l*GRID).__floor__(),GRID),F((h*GRID).__ceil__(),GRID))
def add(a,b):return outward(a[0]+b[0],a[1]+b[1])
def mul(a,b):
 v=[x*y for x in a for y in b];return outward(min(v),max(v))
def exact(x):return (F(x),F(x))
def series(q):
 z=(q-1)/(q+1);p=z;s=F(0)
 for j in range(160):s+=2*p/F(2*j+1);p*=z*z
 return outward(s,s+2*p/(F(321)*(1-z*z)))
@lru_cache(None)
def logarithm(q):
 q=F(q)
 if q<1:
  l,h=logarithm(1/q);return (-h,-l)
 k=0
 while q>=2:q/=2;k+=1
 return add(series(q),mul(exact(k),series(F(2))))
@lru_cache(None)
def position(key):return add(exact(key[0]*A),logarithm(key[1]))
def keys(raw):return [(s,F(q)) for s,q in raw]
def read(p):
 b=Path(p).read_bytes();return json.loads(b),hashlib.sha256(b).hexdigest()
def run(paths,output):
 checks=0;rows=[]
 def check(v):
  nonlocal checks
  assert v;checks+=1
 def encloses(a,b):check(a[0]<=b[0]<=b[1]<=a[1])
 steps=(2,3,4,5,7,8);left=(-1,F(1));right=(1,F(1));amp={}
 for n in steps:
  k=isqrt(n*GRID*GRID);sq=(F(k,GRID),F(k+1,GRID));amp[n]=mul(logarithm(F(2 if n in (4,8) else n)),(1/sq[1],1/sq[0]))
 for path in paths:
  d,dh=read(path);check(d['stage']=='DNE39');check(d['prime_powers']==list(steps));check(d['both_orientations']);check(d['weight']=='P^7 1');check(len(d['power_bands'])==9)
  priorcuts=[left,right];priorvals=[exact(1)];allpowers=[(priorcuts,priorvals)]
  for depth,level in enumerate(d['power_bands']):
   cuts=keys(level['cuts']);vals=[tuple(map(F,v)) for v in level['values']];check(len(cuts)==len(vals)+1);check(cuts[0]==left and cuts[-1]==right)
   for l,h in zip(cuts,cuts[1:]):check(position(l)[1]<position(h)[0])
   if depth==0:check(cuts==priorcuts);check(vals==priorvals);continue
   expected={left,right}
   for c in priorcuts:
    for n in steps:
     for sign in (-1,1):
      key=(c[0],c[1]/F(n)**sign);l,h=position(key)
      if h<-A or l>A:continue
      check(l>-A and h<A or key in (left,right));expected.add(key)
   check(set(cuts)==expected);points=[float(position(k)[0]) for k in priorcuts];computed=[]
   for l,h,saved in zip(cuts,cuts[1:],vals):
    midpoint=(position(l)[1]+position(h)[0])/2;value=exact(0)
    for n in steps:
     for sign in (-1,1):
      y=add(exact(midpoint),mul(exact(sign),logarithm(F(n))))
      if y[1]<-A or y[0]>A:continue
      check(y[0]>-A and y[1]<A);j=bisect_right(points,float((y[0]+y[1])/2))-1;check(0<=j<len(priorvals));check(position(priorcuts[j])[1]<y[0]<=y[1]<position(priorcuts[j+1])[0]);value=add(value,mul(amp[n],priorvals[j]))
    encloses(saved,value);check(value[0]>0);computed.append(value)
   priorcuts,priorvals=cuts,computed;allpowers.append((cuts,computed))
  wc,wv=allpowers[7];pc,pv=allpowers[8];union=set(wc+pc);check(len(d['rows'])==len(union)-1);worst=F(0)
  ordered=sorted(union,key=lambda k:float(position(k)[0]));check([(keys([r['left']])[0],keys([r['right']])[0]) for r in d['rows']]==list(zip(ordered,ordered[1:])))
  wi=pi=0
  for row in d['rows']:
   l=keys([row['left']])[0];h=keys([row['right']])[0];check(l in union and h in union);check(position(l)[1]<position(h)[0])
   while wi+1<len(wv) and (wc[wi+1]==l or position(wc[wi+1])[1]<position(l)[0]):wi+=1
   while pi+1<len(pv) and (pc[pi+1]==l or position(pc[pi+1])[1]<position(l)[0]):pi+=1
   check(l==wc[wi] or position(wc[wi])[1]<position(l)[0]);check(h==wc[wi+1] or position(h)[1]<position(wc[wi+1])[0]);check(l==pc[pi] or position(pc[pi])[1]<position(l)[0]);check(h==pc[pi+1] or position(h)[1]<position(pc[pi+1])[0]);encloses(tuple(map(F,row['weight'])),wv[wi]);encloses(tuple(map(F,row['prime_weight'])),pv[pi]);ratio=pv[pi][1]/wv[wi][0];check(ratio<F(21941,10000));check(F(row['row_ratio_upper'])>=ratio);worst=max(worst,ratio)
  check(F(d['rigorous_max_row_ratio_upper'])>=worst);check(d['certified_prime_norm_strict_upper']=='21941/10000');check(d['certified_original_F112_lower']=='289/500');rows.append(dict(path=path,sha256=dh,independent_max_row_ratio_upper=str(worst),all_rows_verified=True,band_count=len(d['rows'])))
 rate=rate_lower();check(rate>80);masses={t:integrated_mass_upper(t) for t in (14,15,16)};check(masses[14]<masses[15]<masses[16])
 high=lambda t:(LOG[t][0]-F(7,216*t*t),LOG[t][1]-F(7,216*t*t));h14,h15,h16=(high(t) for t in (14,15,16));arch=h16[0]-(h14[1]+F(27,5))*masses[14]-(h15[1]-h14[0])*masses[15]-(h16[1]-h15[0])*masses[16]
 from math import factorial
 pole=16*A*(A/2)**(2*K)/factorial(K)**2;bound=F(2772351243732,10**12);check(arch-pole>bound);check(bound-F(21941,10000)>F(289,500))
 for path in paths:
  d,_=read(path);check(F(d['inherited_arch_minus_pole_strict_lower'])==bound);check(F(d['derived_high_raw_strict_lower'])==bound-F(21941,10000));check(d['high_floor_guard_passed'] and d['norm_guard_passed'])
 out=dict(stage='DNE39',status='PASS',exact_rational_checks=checks,rows=rows,arch_pole_replay_passed=True,arch_minus_pole_strict_lower=str(bound),original_infinite_F112_floor='289/500',helper_sha256=hashlib.sha256(Path('scripts/dne17_nf10_complement_input.py').read_bytes()).hexdigest(),whole_aperture_positive=False,RH=False,Lean=False)
 Path(output).write_text(json.dumps(out,indent=2)+'\n');print('PASS',checks,'high-floor checks')
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('inputs',nargs=2);p.add_argument('--output',required=True);a=p.parse_args();run(a.inputs,a.output)
