#!/usr/bin/env python3
"""NF: original signed Wodd 2D SPAN(u,s), not merely two positive rays.

Interval-accumulate all 7168 complete original [0,12] signed m Fourier
matrix entries in the near-null/complementary basis
    f=u+(4096/3013)s,   g=u-s,
with exact rational physical pole Gram, and pay the ENTIRE high-negative
tail by SI10 cluster-resolved mass sum M2=sum_j mass_j/left_j^2.

Acceptance requires both positive diagonals and a strict determinant.
An honest inconclusive JSON is emitted if interval bounds are too loose.
Original complete odd/even/RH remain open regardless of 2D result.
"""
import json
from fractions import Fraction as F
from pathlib import Path

from validate_rpb108_si06_negative_band import B,PI
from validate_rpb108_si10_complement_positivity import protected_inner_cover
from validate_rpb108_si12_even_supported_inverse import sinh_bounds,cosh_bounds
from validate_rpb108_si14_odd_multiband_nogo import cos_sin_pi_multiple
from validate_rpb108_sm43_positive_affine_error import LOWARCH
from validate_rpb108_mg07_two_source_original_physical_pole_input import (
  CENTER,add,scl,mul,evaluate as physical_anchor)
from validate_rpb108_mg07_two_source_endpoint_log_tail import (
  PI_LO,PI_UP,abs_upper)
from validate_rpb108_mg07_two_source_original_low32_affine_stop import (
  D2,below,above,signed_m_at,qbasis,qinterval,
  hyperbolic_interval)
from validate_rpb108_mg07_signed_two_ray_5120cell import REGIONS

ROOT=Path(__file__).resolve().parents[1]
CUT=F(12)
CURVE=F(2300)
BASIS=((F(1),F(4096,3013),'near_null'),(F(1),F(-1),'complement'))

def mul_i(a,b):
  p=[a[i]*b[j] for i in range(2) for j in range(2)]
  return min(p),max(p)

def sum_i(a,b):
  return a[0]+b[0],a[1]+b[1]

def scalar_i(x,a):
  return mul_i((F(x),F(x)),a)

def negate_i(a):
  return -a[1],-a[0]

def sub_i(a,b):
  return a[0]-b[1],a[1]-b[0]

def maximum_abs(a):
  return max(abs(a[0]),abs(a[1]))

def gamma_for_high_tail():
  # SI10 signed-negative original cover covers all frequency support
  # of Knegative; already includes + and - frequencies in its mass.
  cl,_,mass,leaves,_=protected_inner_cover()
  assert len(cl)==107 and leaves==973 and mass<F(38)
  assert all(not (l<CUT<r) for l,r,_ in cl)
  M2=sum((mass/(l*l) for l,r,mass in cl if l>=CUT),F(0))
  assert F(0)<M2<F(17,1000)
  sn,cs=cos_sin_pi_multiple(2*B*CENTER)
  sh=sinh_bounds(B/2);ch=cosh_bounds(B/2)
  om=(2*PI[0]*CENTER,2*PI[1]*CENTER)
  wup=2*PI_UP*CENTER
  kmin=2*PI_LO*CUT
  denom=kmin*kmin-wup*wup
  assert denom>0
  betas=[]
  for a,b,name in BASIS:
    endpoint=add(scl(a,sn),scl(b,sh))
    der=add(scl(a,mul(om,cs)),scl(b/2,ch))
    ep=above(abs_upper(endpoint),10**12)
    dv=above(abs_upper(der),10**12)
    n1=abs(a)*abs_upper(sn)*wup*wup+abs(b)*sh[1]/4
    n2=abs(a)*wup**3*abs_upper(cs)+abs(b)*ch[1]/8
    beta=above((ep+dv/kmin+n1/denom+n2/(kmin*denom))/PI_LO,10**10)
    assert beta>0
    betas.append(beta)
  return M2,betas

def verify():
  assert B==F(11,10) and CENTER==F(37,64)
  assert D2<F(900) and LOWARCH<F(1400) and D2+LOWARCH<CURVE
  assert sum(int((r-l)/h) for l,r,h in REGIONS)==7168
  M2,betas=gamma_for_high_tail()
  phys=physical_anchor()
  q=tuple(map(F,phys['physical_sine_sinh_cross_Gram_interval']))
  S=tuple(map(F,phys['physical_sinh_self_Gram_interval']))
  po=[sum_i(scalar_i(a,q),scalar_i(b,S)) for a,b,_ in BASIS]
  pole=[[scalar_i(2,mul_i(po[i],po[j]))
          for j in range(2)] for i in range(2)]
  sh=hyperbolic_interval(B/2,'sinh')
  ch=hyperbolic_interval(B/2,'cosh')
  d2=[
    above(4*PI[1]**2*(abs(a)*2*B**3/3+
                      abs(b)*2*B**3/3*sh.h))
    for a,b,_ in BASIS
  ]
  mat=[[F(0),F(0)],[F(0),F(0)]]
  errors=[[F(0),F(0)],[F(0),F(0)]]
  count=0
  for left,right,h in REGIONS:
    n=int((right-left)/h)
    assert left+n*h==right
    for j in range(n):
      l=left+j*h;mid=l+h/2;r=l+h
      li=signed_m_at(l);ri=signed_m_at(r)
      lo=(li[0]+li[1])/2
      hi=(ri[0]+ri[1])/2
      m0=(lo+hi)/2
      m1=(hi-lo)/h
      eps=above(max((li[1]-li[0])/2,(ri[1]-ri[0])/2)
               +CURVE*h*h/8)
      wabs=abs(m0)+abs(m1)*h/2+eps
      base=qbasis(mid,sh,ch)
      val=[];der=[];err=[];mx=[]
      for idx,(a,b,name) in enumerate(BASIS):
        Tv,Dv=qinterval(base,a,b)
        v=(Tv[0]+Tv[1])/2
        d=(Dv[0]+Dv[1])/2
        E=above((Tv[1]-Tv[0])/2+(Dv[1]-Dv[0])*h/4
                 +d2[idx]*h*h/8)
        val.append(v);der.append(d);err.append(E)
        mx.append(abs(v)+abs(d)*h/2)
      for i in range(2):
        for k in range(i,2):
          v,d=val[i],der[i]
          w,e=val[k],der[k]
          baseline=2*(h*m0*v*w+
                     h**3/F(12)*(m0*d*e+m1*(v*e+d*w)))
          error=2*h*(eps*mx[i]*mx[k]+
                     wabs*(err[i]*mx[k]+err[k]*mx[i]+err[i]*err[k]))
          mat[i][k]+=below(baseline,10**9)
          errors[i][k]+=above(error,10**9)
      count+=1
  assert count==7168
  for i in range(2):
    for j in range(i):
      mat[i][j]=mat[j][i]
      errors[i][j]=errors[j][i]
  signed=[
    [(
      mat[i][j]-errors[i][j]-pole[i][j][1],
      mat[i][j]+errors[i][j]-pole[i][j][0]
    ) for j in range(2)] for i in range(2)
  ]
  # The high negative form is PSD, and its quadratic satisfies
  # Qneg(z) <= M2 (|z0| beta0+|z1| beta1)^2.
  # Lower the diagonal and bound absolute offdiagonal accordingly.
  A=signed[0][0][0]-M2*betas[0]**2
  D=signed[1][1][0]-M2*betas[1]**2
  off=maximum_abs(signed[0][1])+M2*betas[0]*betas[1]
  determinant=A*D-off*off
  lower=determinant/(A+D) if A>0 and D>0 else F(-1)
  ok=A>0 and D>0 and determinant>0
  result={
    'status':('CERTIFIED_TRUE_ORIGINAL_SIGNED_2D_SINE_POLE_POSITIVITY'
              if ok else 'HONEST_INCONCLUSIVE_ORIGINAL_SIGNED_2D'),
    'span':'original SI10 sine at 37/64 and true sinh pole',
    'original_basis':[(str(a),str(b),n) for a,b,n in BASIS],
    'original_lowband_cell_count':count,
    'high12_negative_mass_weighted_inverse_square':str(M2),
    'whole_high12_Fourier_betas':[str(x) for x in betas],
    'lowband_matrix_baseline':[[str(v) for v in row] for row in mat],
    'lowband_matrix_entry_error':[[str(v) for v in row] for row in errors],
    'signed_lowband_plus_pole_intervals':[[[str(u),str(v)] for u,v in row] for row in signed],
    'full_signed_A_diagonal_lower':str(A),
    'full_signed_D_diagonal_lower':str(D),
    'full_signed_cross_abs_upper':str(off),
    'full_signed_2D_determinant_lower':str(determinant),
    'full_signed_2D_min_eigenvalue_lower':str(lower),
    'positive_original_signed_2D_certified':ok,
    'original_global_signed_Wodd':'OPEN',
    'SI29_augmented_Ritz':'OPEN',
    'even_CC27_Weil_RH':'OPEN'
  }
  return result

if __name__=='__main__':
  result=verify()
  out=ROOT/'artifacts/mg07_original_signed_two_dimensional_SPD.json'
  out.parent.mkdir(parents=True,exist_ok=True)
  out.write_text(json.dumps(result,indent=2)+'\n')
  print('MG07 ORIGINAL 2D SIGNED SPD',
        result['status'],
        'A=',float(F(result['full_signed_A_diagonal_lower'])),
        'D=',float(F(result['full_signed_D_diagonal_lower'])),
        'B<=',float(F(result['full_signed_cross_abs_upper'])),
        'det>=',float(F(result['full_signed_2D_determinant_lower'])),
        flush=True)
  # Keep an honest inconclusive artifact: the workflow decides promotion.
