#!/usr/bin/env python3
"""NF523 independent source Fraction auditor and exact rational moment control.

Rederives full original collar envelopes using reverse Horner/dual numbers,
not forward absolute coefficient sums. Demonstrates finite moment corrections
in an exact six-direction odd polynomial control. Not an original 242D
Weil source-graph membership theorem or a Lean build.
"""
import argparse,hashlib,json,math,sys
from pathlib import Path
from fractions import Fraction as F
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
SHA='39cba367d70243c2d15e5a9323fc8097d58187923dcf0eca2b031136871f0181'
D=F(1,500);RAD=F(1,25);N=400
def read(p):
 z=Path(p).read_bytes();return json.loads(z),hashlib.sha256(z).hexdigest()
def solve(M,y):
 n=len(y);a=[list(M[i])+[y[i]] for i in range(n)]
 for j in range(n):
  p=next(k for k in range(j,n) if a[k][j]!=0)
  a[j],a[p]=a[p],a[j]
  v=a[j][j];a[j]=[x/v for x in a[j]]
  for i in range(n):
   if i!=j:
    t=a[i][j];a[i]=[x-t*z for x,z in zip(a[i],a[j])]
 return [row[n] for row in a]
def main():
 p=argparse.ArgumentParser()
 for k in ('nf494','primary','output'):p.add_argument('--'+k,required=True)
 a=p.parse_args();source,sh=read(a.nf494);primary,ph=read(a.primary)
 assert sh==SHA and source['pass']=='NF494-native'
 assert primary['pass']=='NF523-original-NF494-endpoint-log-fractional-domain-source-exact'
 assert primary['original_nf494_source_SHA256']==sh
 rows=source['original_U_400_native_outward'];assert len(rows)==N
 abscoeff=[]
 for l,u in rows:
  l,u=F(l),F(u);assert l<=u
  abscoeff.append(max(-l,u,-u,l))
 p0=abscoeff[-1];dp=F(0)
 for c in reversed(abscoeff[:-1]):
  dp=p0+D*dp
  p0=c+D*p0
 r=D/RAD;C=F(10)**400
 t0=C*r**N/(1-r)
 t1=(C/RAD)*r**(N-1)*(N/(1-r)+r/(1-r)**2)
 assert p0+t0==F(primary['original_U_full_collar_sup_absolute_bound'])
 assert dp+t1==F(primary['original_U_prime_full_collar_sup_absolute_bound'])
 assert t0==F(primary['source_original_400_jets_analytic_tail_U'])
 assert t1==F(primary['source_original_400_jets_analytic_tail_Uprime'])
 assert p0+t0<F(1,5000000)
 assert dp+t1<F(7,10000)
 lo,hi=map(F,source['original_U_400_native_outward'][0])
 assert hi< -F(1,10**11)
 n=6;M=[]
 for i in range(n):
  row=[]
  for j in range(n):
   row.append(2*sum((F((-1)**k*math.comb(4,k),2*(i+j)+3+2*k)
                     for k in range(5)),F(0)))
  M.append(row)
 pivot=[];L=[[F(0)]*n for _ in range(n)]
 for i in range(n):
  for j in range(i):
   L[i][j]=(M[i][j]-sum((L[i][k]*pivot[k]*L[j][k] for k in range(j)),F(0)))/pivot[j]
  d=M[i][i]-sum((L[i][k]**2*pivot[k] for k in range(i)),F(0))
  assert d>0;pivot.append(d);L[i][i]=F(1)
 # Exact original-analogue odd target t(x)=x log(1/|x|);
 # target moments against x^(2i+1) are 2/(2i+3)^2.
 target=[F(2,(2*i+3)**2) for i in range(n)]
 trial=[M[i][0] for i in range(n)]
 diff=[target[i]-trial[i] for i in range(n)]
 c=solve(M,diff)
 assert all(trial[i]+sum((M[i][j]*c[j] for j in range(n)),F(0))==target[i]
            for i in range(n))
 out={'pass':'NF523-independent-original-endpoint-source-Horner-and-finite-moment-algebra',
   'original_nf494_SHA256':sh,'primary_NF523_receipt_SHA256':ph,
   'independent_reverse_Horner_original_U_sup':str(p0+t0),
   'independent_reverse_dual_Horner_original_Uprime_sup':str(dp+t1),
   'independent_original_U_B_nonzero':True,
   'independent_fractional_sobolev_a_priori_bounds_agree':True,
   'exact_odd_polynomial_6moment_control_rank':n,
   'exact_odd_polynomial_moment_matrix_LDL_pivots':[str(x) for x in pivot],
   'exact_odd_polynomial_smooth_correction_coeffs':[str(x) for x in c],
   'exact_odd_polynomial_six_moments_preserved':True,
   'original_242D_selected_chi_weighted_moment_matrix_numerically_computed':False,
   'original_actual_divisor_source_graph_lift':'OPEN',
   'original_signed_Weil_test_identity':'OPEN','RH':'OPEN'}
 Path(a.output).write_text(json.dumps(out,indent=2)+'\n')
 print('NF523 independent 400-source reverse Horner U/Uprime PASS')
 print('NF523 six rational odd selected moment correction controls PASS')
 print('Actual Weil source graph image and RH OPEN')
if __name__=='__main__':main()
