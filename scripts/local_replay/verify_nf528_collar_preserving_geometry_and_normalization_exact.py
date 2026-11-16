#!/usr/bin/env python3
"""NF528 exact-Fraction collar geometry and source normalization; NOT a Lean build."""
from fractions import Fraction as F
from pathlib import Path
import argparse,json
B=F(11,10);D=F(1,500);a=B-D;c=B-D/2
def add(x,y):return(x[0]+y[0],x[1]+y[1])
def sub(x,y):return(x[0]-y[0],x[1]-y[1])
def mul(x,y):return(x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def cj(x):return(x[0],-x[1])
def half(x):return(x[0]/2,x[1]/2)
Z=(F(0),F(0))
def main():
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);args=p.parse_args()
 geometry=[]
 for n in [2,3,4,5,10,20,100,1000]:
  s=F(n-1,n);eps=(1-s)*D/4
  lo=c-s*D/2-eps;hi=c+s*D/2+eps
  assert a<lo<hi<B and lo-a==B-hi==(1-s)*D/4
  assert 0<eps<(1-s)*D/2 and 0<s<=1
  geometry.append({'s':str(s),'eps':str(eps),'margin':str(lo-a)})
 assert a<c-D/8<c+D/8<B
 originals=[
  ((F(1,3),F(2,7)),(F(-3,5),F(1,11)),(F(4,9),F(-1,7)),(F(2,3),F(3,8)),3),
  ((F(6,5),F(-2,7)),(F(1,13),F(2,5)),(F(3,5),F(-1,2)),(F(7,11),F(1,4)),2)]
 rows=[]
 for Af,Bf,Ag,Bg,m in originals:
  for _ in range(m):
   rows.extend([(Af,Bf,Ag,Bg),(Bf,Af,Bg,Ag)])
 signed=Z;zero=Z
 for Af,Bf,Ag,Bg in rows:
  Pf=half(add(Af,Bf));Nf=half(sub(Af,Bf))
  Pg=half(add(Ag,Bg));Ng=half(sub(Ag,Bg))
  signed=add(signed,sub(mul(cj(Pf),Pg),mul(cj(Nf),Ng)))
  zero=add(zero,mul(cj(Af),Bg))
 assert signed==zero
 def tail(n):return F(2*(n+2)**3+6*(n+2)**2+18*(n+2)+26,2**n)
 for n in [0,1,2,8,16,32,64,128]:assert tail(n)-tail(n+1)==F((n+2)**3,2**n)
 assert F(133,250)-F(2,5)-F(4,125)==F(1,10)
 data={
  'pass':'NF528-E-preserving-geometry-and-two-source-normalization-exact',
  'date':'2026-11-15 PT','B':str(B),'delta':str(D),'geometry':geometry,
  'sample_pattern_rows_with_all_partner_multiplicity_copies':len(rows),
  'signed_Hilbert_source_mixed':list(map(str,signed)),
  'all_copy_zero_side_mixed':list(map(str,zero)),
  'coercivity_margin':str(F(1,10)),
  'full_original_242_Gram_rank':'INHERITED_NF523_NOT_REPLAYED',
  'original_NF494_U400_sha':'39cba367d70243c2d15e5a9323fc8097d58187923dcf0eca2b031136871f0181',
  'new_Lean_compilation':False,'original_source_replay':False,
  'status':'Finite arithmetic LOCAL PASS; E-preserving graph and direct EF ANALYTIC UNCOMPILED',
  'RH':'OPEN','W_ODD_NEG':'OPEN'
 }
 Path(args.output).write_text(json.dumps(data,indent=2)+'\n')
 print(json.dumps({k:data[k] for k in ['pass','sample_pattern_rows_with_all_partner_multiplicity_copies','signed_Hilbert_source_mixed','all_copy_zero_side_mixed','coercivity_margin']},indent=2))
if __name__=='__main__':main()
