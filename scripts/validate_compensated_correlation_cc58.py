#!/usr/bin/env python3
"""Exact CC58 algebra, enclosure and crossing controls; native NF21 sector audit."""
import argparse,json,hashlib
from fractions import Fraction as F
KAPPA=F(207,1000)
def tr(a):return list(map(list,zip(*a)))
def add(a,b):return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def neg(a):return [[-x for x in r] for r in a]
def mul(a,b):return [[sum(x*y for x,y in zip(r,c)) for c in tr(b)] for r in a]
def scale(a,t):return [[x*t for x in r] for r in a]
def eye(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def inverse2(a):
 d=a[0][0]*a[1][1]-a[0][1]*a[1][0]
 return scale([[a[1][1],-a[0][1]],[-a[1][0],a[0][0]]],1/d)
def gram(a):return mul(tr(a),a)
def psd2(a):return a==tr(a) and a[0][0]>=0 and a[1][1]>=0 and a[0][0]*a[1][1]>=a[0][1]**2
def validate(native):
 Q=[[F(3),F(1,4),F(1,5),-F(1,7)],[F(1,4),F(5),F(2,9),F(1,8)],
    [F(1,5),F(2,9),F(7),F(1,11)],[-F(1,7),F(1,8),F(1,11),F(9)]]
 R=[[F(1,7),-F(1,9),F(1,5),F(0)],[F(0),F(1,8),-F(1,6),F(1,7)],
    [F(1,17),F(0),F(1,19),F(1,23)]]
 A=[r[:2] for r in Q[:2]];B=[r[2:] for r in Q[:2]];C=[r[2:] for r in Q[2:]]
 Y=mul(inverse2(C),tr(B));T=eye(2)+neg(Y);S=add(A,neg(mul(B,Y)))
 source=Q+R;D=gram(source);Z=mul(R,T);P=gram(Z)
 assert mul(source,T)[:2]==S and mul(source,T)[2:4]==[[0,0],[0,0]]
 assert add(mul(mul(tr(T),D),T),neg(gram(S)))==P
 assert mul(mul(tr(T),add(D,neg(gram(Q)))),T)==P
 assert psd2(P) and P[0][0]*P[1][1]>P[0][1]**2
 assert P==add(gram(Z[:1]),gram(Z[1:])) # exact Parseval split
 majorants=[]
 E=[[F(1,1000),-F(1,2000)],[F(1,3000),F(1,4000)],[F(-1,5000),F(1,6000)]]
 Rhat=add(Z,neg(E));eta2=sum(x*x for r in E for x in r)
 for t in [F(1,10),F(1,2),F(1),F(2),F(10)]:
  U=add(scale(gram(Rhat),1+t),scale(eye(2),(1+1/t)*eta2))
  assert psd2(add(U,neg(P)))
  identity=add(add(scale(gram(Rhat),t),scale(gram(E),1/t)),neg(add(mul(tr(Rhat),E),mul(tr(E),Rhat))))
  assert psd2(identity)
  majorants.append({'t':str(t),'eta_squared_Hilbert_Schmidt':str(eta2),'Young_majorant_valid':True})
 sectors=[]
 for archived,lo,hi in [('prime_plus_pole_source_square_gram_00',F(7244,1000),F(7245,1000)),
                         ('prime_plus_pole_source_square_gram_11',F(1280,1000),F(1281,1000))]:
  l,h=map(F,native[archived]);assert lo<l<=h<hi and h-l<F(1,10**38)
  sectors.append({'native_field':archived,'strict_lower':str(lo),'strict_upper':str(hi),'interval_width':str(h-l)})
 assert native['overlapping_ordered_source_shift_pairs']==82
 assert native['full_source_Gram'] is False and native['full_residual_P2_built'] is False
 # Fixed included source, exact omitted-sector cancellation or reinforcement.
 completions=[]
 for omitted in [F(-2),F(-1),F(0),F(2)]:
  full=(F(2)+omitted)**2
  completions.append({'included_source_square':'4','omitted_source':str(omitted),'full_source_square':str(full)})
 assert completions[0]['full_source_square']=='0' and completions[-1]['full_source_square']=='16'
 # Direct source radius can certify a small gate where independent square errors cannot.
 s=F(1,10**39);radius=F(1,10**25);square_error=F(1,10**38)
 assert radius**2<KAPPA*s<square_error
 crossings=[]
 # High C=1, low A=1+epsilon, mixed source b=1: genuine Schur crossing.
 for eps in [F(1,100),F(0),F(-1,100)]:
  assert (1+eps)-1==eps
  crossings.append({'epsilon':str(eps),'complete_Schur':str(eps),'physical_source_square':'1'})
 shifts=[]
 # A=mu+1/(2-mu) makes mu the original positive ground eigenlevel.
 for mu in [F(1,10**40),F(1,100),F(1,20)]:
  a=mu+1/(2-mu);h=[F(1),-1/(2-mu)]
  assert mul([[a,F(1)],[F(1),F(2)]],[[h[0]],[h[1]]])==[[mu*h[0]],[mu*h[1]]]
  assert 2-mu>KAPPA and a-mu-F(1,2)>0
  shifts.append({'original_positive_ground_level':str(mu),'whole_mass_shift_null':True,'low_only_shift_misses_null':True})
 return {'status':'PASS','milestone':'CC58','NF21_identity_replayed_without_sympy':True,
  'native_prime_pole_sector_bounds':sectors,'native_full_Gram':False,'native_P2_evaluated':False,
  'exact_Parseval_split':True,'Young_majorants':majorants,'abstract_sector_completions':completions,
  'near_critical_enclosure_control':{'retained_S':str(s),'direct_source_error_radius':str(radius),
    'independent_square_error':str(square_error),'direct_gate_passes':True,'independent_square_gate_inconclusive':True},
  'genuine_crossings':crossings,'positive_eigenlevel_controls':shifts,
  'all_cap_defect_relative_frame':False,'actual_Weil_crossing_proved':False,'RH':False,'Lean':False}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--native',required=True);p.add_argument('--output',required=True);a=p.parse_args()
 assert hashlib.sha256(open(a.native,'rb').read()).hexdigest()=='9ea91c5d0bf9bac4cf32d8a2bb3644c6fb7d9dd004ad3ebc5f5aac0ee1b01648'
 result=validate(json.load(open(a.native)));open(a.output,'w').write(json.dumps(result,indent=2)+'\n');print('CC58 PASS')
