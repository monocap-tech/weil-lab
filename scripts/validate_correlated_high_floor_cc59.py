#!/usr/bin/env python3
"""Exact correlated high-floor identities and controls; no native Gram evaluation."""
from fractions import Fraction as F
import json,argparse
KAPPA=F(207,1000)
def tr(a):return list(map(list,zip(*a)))
def mul(a,b):return [[sum(x*y for x,y in zip(r,c)) for c in tr(b)] for r in a]
def add(a,b):return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def sc(a,t):return [[x*t for x in r] for r in a]
def eye(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def inv(a):
 n=len(a);v=[r[:]+e for r,e in zip(a,eye(n))]
 for j in range(n):
  p=next(i for i in range(j,n) if v[i][j]);v[j],v[p]=v[p],v[j]
  q=v[j][j];v[j]=[x/q for x in v[j]]
  for i in range(n):
   if i!=j:
    q=v[i][j];v[i]=[x-q*y for x,y in zip(v[i],v[j])]
 return [r[n:] for r in v]
def block(a,b,c,d):return [r+s for r,s in zip(a,b)]+[r+s for r,s in zip(c,d)]
def gram(a):return mul(tr(a),a)
def psd(a):
 # Exact recursive LDL, including the zero-pivot PSD condition.
 a=[r[:] for r in a];assert a==tr(a)
 while a:
  p=a[0][0]
  if p<0:return False
  if p==0:
   if any(a[0][j] for j in range(1,len(a))):return False
   a=[r[1:] for r in a[1:]];continue
  a=[[a[i][j]-a[i][0]*a[0][j]/p for j in range(1,len(a))] for i in range(1,len(a))]
 return True
def validate():
 # Two measured high modes, three unmeasured modes, two retained sources.
 C=[[F(3),F(1,5)],[F(1,5),F(4)]]
 K=[[F(3),F(1,2)],[F(1,3),F(2)],[F(1,7),F(-1,4)]]
 R=[[F(1),F(1,5)],[F(1,4),F(2)],[F(1,9),F(-1,3)]]
 Cshift=add(C,sc(eye(2),-KAPPA));assert psd(Cshift)
 M=mul(inv(C),inv(Cshift));H=gram(K);P=gram(R);Z=mul(tr(K),R)
 V=add(mul(C,Cshift),H)
 U=sc(add(P,sc(mul(mul(tr(Z),inv(V)),Z),-1)),1/KAPPA)
 Dmin=add(sc(eye(3),KAPPA),mul(mul(K,inv(Cshift)),tr(K)))
 Cmin=block(C,tr(K),K,Dmin)
 assert psd(add(Cmin,sc(eye(5),-KAPPA)))
 Seff=add(Dmin,sc(mul(mul(K,inv(C)),tr(K)),-1))
 assert Seff==sc(add(eye(3),mul(mul(K,M),tr(K))),KAPPA)
 assert inv(Seff)==sc(add(eye(3),sc(mul(mul(K,inv(V)),tr(K)),-1)),1/KAPPA)
 actual=mul(mul(tr(R),inv(Seff)),R);assert actual==U
 assert psd(U) and psd(add(sc(P,1/KAPPA),sc(U,-1)))
 # Increasing the unknown high block preserves the floor and reduces response.
 completions=[]
 for d in [F(0),F(1,100),F(1),F(100)]:
  high=block(C,tr(K),K,add(Dmin,sc(eye(3),d)))
  physical=([[F(0),F(0)]]*2)+R
  response=mul(mul(tr(physical),inv(high)),physical)
  assert psd(add(high,sc(eye(5),-KAPPA))) and psd(add(U,sc(response,-1)))
  completions.append({'unknown_high_increment':str(d),'response_below_majorant':True,'equality_at_zero':response==U})
 # Same fixed C,K, residual norm: aligned tail obtains improvement, orthogonal tail does not.
 c=F(3);k=F(3);D=KAPPA+k*k/(c-KAPPA)
 denom=KAPPA*(1+k*k/(c*(c-KAPPA)))
 aligned=1/denom;coarse=1/KAPPA;s=F(4)
 assert aligned<s<coarse
 assert s-aligned>0
 # Orthogonal physical source on an added floor-kappa coordinate, same unit norm.
 assert 1/KAPPA==coarse>s
 crossings=[]
 high=[[c,k],[k,D]];w=mul(inv(high),[[F(0)],[F(1)]])
 assert w[1][0]==aligned
 for eps in [F(1,100),F(0),F(-1,100)]:
  a=aligned+eps
  Q=[[a,F(0),F(1)],[F(0),c,k],[F(1),k,D]]
  h=[[F(1)],[-w[0][0]],[-w[1][0]]]
  q=mul(mul(tr(h),Q),h)[0][0];assert q==eps
  crossings.append({'epsilon':str(eps),'full_Schur':str(eps),'correlated_gate_margin':str(eps),'coarse_gate_fails':a<coarse})
 levels=[]
 # Genuine positive ground levels use original high = Cmin+mu I.
 for mu in [F(1,10**40),F(1,100),F(1,20)]:
  original_high=add(high,sc(eye(2),mu));a=aligned+mu
  Q=[[a,F(0),F(1)],[F(0),original_high[0][0],k],[F(1),k,original_high[1][1]]]
  h=[[F(1)],[-w[0][0]],[-w[1][0]]]
  assert mul(Q,h)==sc(h,mu)
  assert psd(add(Q,sc(eye(3),-mu)))
  assert a-mu-mul(mul([[F(0),F(1)]],inv(original_high)),[[F(0)],[F(1)]])[0][0]>0
  levels.append({'original_positive_ground_level':str(mu),'whole_shift_null':True,'shifted_correlated_gate_exact_contact':True,'retained_only_shift_misses_null':True})
 # Full source-square algebra recovers H and Z from D58 in a finite model.
 A=[[F(5),F(1,4)],[F(1,4),F(6)]];B=[[F(1,3),F(1,5)],[F(-1,7),F(1,4)]]
 low_tail=[[F(1,5),F(1,6)],[F(1,9),F(-1,8)],[F(1,11),F(1,13)]]
 native=block(A,B,tr(B),C);source=native+[r+s for r,s in zip(low_tail,K)]
 sourceD=gram(source);T=eye(2)+sc(mul(inv(C),tr(B)),-1)
 S=add(A,sc(mul(mul(B,inv(C)),tr(B)),-1));residual=mul(source,T)[4:]
 DH=[r[2:] for r in sourceD[2:]]
 Hrecover=add(add(DH,sc(gram(B),-1)),sc(mul(C,C),-1));assert Hrecover==H
 Zrecover=add(mul(sourceD[2:],T),sc(mul(tr(B),S),-1));assert Zrecover==mul(tr(K),residual)
 return {'status':'PASS','milestone':'CC59','exact_Woodbury_identity':True,'least_completion_attains_majorant':True,
  'unknown_high_completions':completions,'native_source_Gram_H_Z_recovery_identity':True,
  'aligned_control':{'P':'1','S2':'4','coarse_response_upper':str(coarse),'correlated_response_upper':str(aligned),'coarse_gate_fails':True,'correlated_gate_passes':True},
  'same_norm_orthogonal_control_has_no_improvement':True,'genuine_crossings':crossings,'positive_ground_levels':levels,
  'native_D_or_P_evaluated':False,'original_Weil_counterexample':False,'all_cap_frame':False,'RH':False,'Lean':False}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args()
 r=validate();open(a.output,'w').write(json.dumps(r,indent=2)+'\n');print('CC59 PASS')
