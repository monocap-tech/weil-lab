#!/usr/bin/env python3
"""Independent coefficient, mass, rational-log and shell-transfer audit."""
from pathlib import Path
from fractions import Fraction as F
from math import factorial
import argparse,json
from certify_dne39_signed_comparison import read

def run(path,output):
 checks=0
 def check(v):
  nonlocal checks
  assert v;checks+=1
 def enclose(a,b):check(a[0]<=b[0]<=b[1]<=a[1])
 def pi():
  def arctan(q):
   s=sum((-1)**j*q**(2*j+1)/F(2*j+1) for j in range(65));e=q**131/F(131);return s-e,s+e
  x,y=arctan(F(1,5)),arctan(F(1,239));return (16*x[0]-4*y[1],16*x[1]-4*y[0])
 def log(q):
  q=F(q);k=0
  while q>=2:q/=2;k+=1
  def ser(q):
   z=(q-1)/(q+1);s=sum(2*z**(2*j+1)/F(2*j+1) for j in range(180));return s,s+2*z**361/(F(361)*(1-z*z))
  u,v=ser(q),ser(F(2));return (u[0]+k*v[0],u[1]+k*v[1])
 def coeff(n):
  c=[F(1,2*n+3)]
  for step in range(6):
   c=[F(1,2*n+3)]+[sum(c[j]*c[t-j] for j in range(len(c)) if 0<=t-j<len(c))/F(2*n+2*t+5) for t in range(2*len(c)-1)]
  return c
 d,dh=read(path);check(d['stage']=='DNE46' and d['parent']=='a9eda40b874163be980da517d3dda87942f83533');A=F(53,50);K=112;check(d['aperture']==str(A) and d['retained_cutoff']==K)
 ts=list(map(F,d['cutoffs']));check(ts==[F(14),F(15),F(16),F(65,4),F(33,2),F(67,4)]);p=pi();check(tuple(map(F,d['pi_interval']))==p);check(F(314159,10**5)<p[0]<p[1]<F(314160,10**5))
 base=coeff(K);check(len(base)==64 and all(x>0 for x in base));cs={K:base}
 for n in range(K+1,K+48):
  c=coeff(n);check(len(c)==64)
  for x,y in zip(c,cs[n-1]):check(0<x<=y)
  cs[n]=c
 top=F((2*A*p[1]*ts[-1]*10**8).__ceil__(),10**8);check(top==F(d['max_scaled_cutoff_upper']) and top*top<K*(K+1));rate=2*K+1-2*sum(base[j]*top**(2*j+2) for j in range(64));check(rate==F(d['depth6_rate_lower'])>d['conservative_rate']==50)
 masses=[]
 for T,saved in zip(ts,d['masses_upper']):
  lo=F((2*A*p[0]*T*10**8).__floor__(),10**8);hi=F((2*A*p[1]*T*10**8).__ceil__(),10**8);check(0<lo<hi<=top and hi*hi<K*(K+1));total=F(0)
  df=factorial(2*K+1)//(2**K*factorial(K));check(df==factorial(225)//(2**112*factorial(112)))
  for n in range(K,K+48):
   c=cs[n];raw=sum(c[j]*lo**(2*j+2)/F(j+1) for j in range(12));exponent=F((raw*1000).__floor__(),1000);check(0<exponent<=raw)
   exp=sum(exponent**j/F(factorial(j)) for j in range(155));check(exp>1)
   term=4*A*T*(2*n+1)*hi**(2*n)/(50*df**2*exp);rounded=F((term*10**18).__ceil__(),10**18);check(term<=rounded<term+F(1,10**18));total+=rounded;df*=2*n+3
  y=2*A*F(22,7)*T;ratio=y*y/F(321*323);check(0<ratio<1)
  tail=4*A*T*y**320/(df**2*(1-ratio));total+=F((tail*10**18).__ceil__(),10**18);check(total==F(saved));masses.append(total)
 check(all(0<x<y for x,y in zip(masses,masses[1:])))
 bands=[tuple(map(F,x)) for x in d['arch_multiplier_intervals']]
 for t,b in zip(ts,bands):
  l=log(t);enclose(b,(l[0]-F(7,216)/t**2,l[1]-F(7,216)/t**2))
 loss=(bands[0][1]+F(27,5))*masses[0]+sum((bands[i][1]-bands[i-1][0])*masses[i] for i in range(1,len(ts)));check(loss==F(d['arch_shell_loss_upper']))
 check(all(bands[i][0]>bands[i-1][1] for i in range(1,len(ts))));arch=bands[-1][0]-loss;pole=16*A*(A/2)**(2*K)/factorial(K)**2;check(arch==F(d['arch_lower']) and pole==F(d['pole_upper']));check(arch-pole==F(d['arch_minus_pole_lower']))
 h,hh=read(d['high_validation_path']);check(hh==d['high_validation_sha256'] and h['status']=='PASS' and h['arch_pole_replay_passed']);prime=F(d['prime_norm_strict_upper']);check(prime==F(43387,20000))
 # Authenticate the already independently audited global prime certificates.
 for row in h['rows']:
  pc,ph=read(row['path']);check(ph==row['sha256'] and row['all_rows_verified']);check(F(pc['certified_prime_norm_strict_upper'])==prime and pc['prime_powers']==[2,3,4,5,7,8] and pc['both_orientations'] and pc['aperture']=='53/50')
 raw=arch-pole-prime;k=F(d['certified_original_F112_lower']);check(raw==F(d['original_high_raw_strict_lower'])>k>F(6199377,10**7));check(k==F((raw*1000).__floor__(),1000))
 for key in ('source_integrals_recomputed','true_high_inverse_evaluated','whole_aperture_positive','RH','Lean'):check(d[key] is False)
 out=dict(stage='DNE46',status='PASS',exact_rational_checks=checks,certificate_path=path,certificate_sha256=dh,inherited_high_validation_sha256=hh,cutoffs=d['cutoffs'],depth6_positive_region_checked=True,fresh_rate_checked=True,arch_minus_pole_lower=d['arch_minus_pole_lower'],original_infinite_F112_floor=str(k),source_integrals_recomputed=False,true_high_inverse_evaluated=False,whole_aperture_positive=False,RH=False,Lean=False)
 Path(output).write_text(json.dumps(out,indent=2)+'\n');print('PASS',checks,'high checks; original floor',str(k),flush=True)
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('input');ap.add_argument('--output',required=True);a=ap.parse_args();run(a.input,a.output)
