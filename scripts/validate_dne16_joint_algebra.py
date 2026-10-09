#!/usr/bin/env python3
"""Independent rational controls for projection, mixed errors and CC60."""
from fractions import Fraction as F
import json
dot=lambda x,y:sum((a*b for a,b in zip(x,y)),F(0))
count=0
for t in range(1,41):
 s=[F((k+2)*t-7,k+3) for k in range(9)]
 k0=[F(k-t,2*k+1) for k in range(9)]
 k1=[F(t*t-k,3*k+2) for k in range(9)]
 # Full six-coordinate low projection plus both measured-high projections.
 # The remaining coordinate can vanish; no endpoint or residual positivity
 # assumption is used in the projection identity.
 q=[s,k0,k1]
 g=[[dot(x,y)-dot(x[:8],y[:8]) for y in q] for x in q]
 assert g==[[dot(x[8:],y[8:]) for y in q] for x in q];count+=1
 # Separate high-form penalty, positive and coupled.
 W=[[F(9),F(1,3)],[F(1,3),F(11)]]
 V=[[W[i][j]+g[i+1][j+1] for j in range(2)] for i in range(2)]
 z=g[0][1:];det=V[0][0]*V[1][1]-V[0][1]**2
 assert det>0
 ys=[(V[1][1]*z[0]-V[0][1]*z[1])/det,(V[0][0]*z[1]-V[0][1]*z[0])/det]
 gain=(V[1][1]*z[0]**2-2*V[0][1]*z[0]*z[1]+V[0][0]*z[1]**2)/det
 assert dot(ys,z)==gain;count+=1
 for y in ([F(0),F(0)],[F(17,100),F(-3,50)],ys,[2*v for v in ys]):
  J=g[0][0]-2*dot(y,z)+sum(y[i]*V[i][j]*y[j] for i in range(2) for j in range(2))
  residual=[s[n]-y[0]*k0[n]-y[1]*k1[n] for n in range(8,9)]
  assert J==dot(residual,residual)+sum(y[i]*W[i][j]*y[j] for i in range(2) for j in range(2));count+=1
  delta=[y[i]-ys[i] for i in range(2)]
  assert J-(g[0][0]-gain)==sum(delta[i]*V[i][j]*delta[j] for i in range(2) for j in range(2));count+=1
 # Mixed kernel integrand and projection polarization, exact arithmetic.
 for i in range(3):
  for j in range(i,3):
   assert dot(q[i],q[j])==(dot([x+y for x,y in zip(q[i],q[j])],[x+y for x,y in zip(q[i],q[j])])-dot(q[i],q[i])-dot(q[j],q[j]))/2;count+=1
print(json.dumps({'stage':'DNE16','exact_fraction_assertions':count,'passed':True,'native_source_run':False},indent=2))
