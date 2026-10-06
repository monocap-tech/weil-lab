"""Exact response and spline controls; analytic proof is in the companion note."""
from fractions import Fraction as F
from math import comb
import json

response_checks=0
for rho in [F(1,3),F(1),F(5,2)]:
 for delta in [F(1,7),F(2),F(11)]:
  for nu in [F(-3),F(0),F(4,5)]:
   g00,g01,g11=rho*rho,rho*nu,delta+nu*nu
   det=g00*g11-g01*g01
   assert det==rho*rho*delta>0
   inverse_source=((g11*rho-g01*nu)/det,(-g01*rho+g00*nu)/det)
   assert inverse_source==(1/rho,F(0))
   assert rho*inverse_source[0]+nu*inverse_source[1]==1
   # B=-G^-1 R*: Rh=-u is the required null-reconstruction sign.
   assert rho*(-inverse_source[0])+nu*(-inverse_source[1])==-1
   response_checks+=1
spline_checks=[]
coefficients=[1]
for r in range(1,9):
 next_coefficients=[0]*(r+1)
 for k,c in enumerate(coefficients):
  next_coefficients[k]+=c
  next_coefficients[k+1]-=c
 coefficients=next_coefficients
 assert coefficients==[(-1)**k*comb(r,k) for k in range(r+1)]
 assert coefficients[0]==1  # noncancellable highest delta derivative at x=0
 flag=[sum(q+j<r for q in range(r)) for j in range(r+2)]
 assert flag==[max(r-j,0) for j in range(r+2)]
 assert all(q+1<r for q in range(r-1))
 spline_checks.append({'r':r,'delta_coefficients':coefficients,'flag_dimensions':flag})
print(json.dumps({
 'scope':'rational inverse-response algebra and compact-spline delta coefficients only',
 'scalar_response_checks':response_checks,
 'spline_controls':spline_checks,
 'actual_null_vector_constructed':False,
 'actual_H1_mapping_proved':False,
 'lean_certified':False,'f4_closed':False,'full_transport_closed':False
},indent=2,sort_keys=True))
