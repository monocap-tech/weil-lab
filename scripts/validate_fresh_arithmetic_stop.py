"""Exact scalar reallocation and bounded weak observation controls."""
from fractions import Fraction as F
import json

scalar_checks=0
for mass in [F(1,5),F(1),F(7)]:
 for log_weight in [F(1),F(3,2),F(11)]:
  for error in [F(0),F(1,3),F(4)]:
   for pole_bound in [F(0),F(2,5),F(5)]:
    for multiplier_error in [-error,F(0),error]:
     for p in [-pole_bound*mass,F(0),pole_bound*mass]:
      m=log_weight+multiplier_error
      q=p+m*mass
      mu=m-pole_bound
      pi=p+pole_bound*mass
      shift=error+pole_bound
      assert 0<=pi<=2*pole_bound*mass
      assert log_weight<=mu+shift<=(1+2*error)*log_weight
      assert q+shift*mass==pi+(mu+shift)*mass
      assert log_weight*mass<=q+shift*mass<=(1+2*error+2*pole_bound)*log_weight*mass
      assert pi+mu*mass==p+m*mass
      scalar_checks+=1
# Frozen right operator, strict endpoint operator and weak test compression.
# J maps x to (x,0); all right operators here have compressed endpoint value 0.
threshold_checks=0
for flux in [F(-3),F(1,2),F(2)]:
 for correction in [F(0),F(1,4),F(5)]:
  right=[[F(0),flux],[flux,F(1)]]
  equality=[[F(0),correction],[correction,F(0)]]
  strict=[[right[i][j]+equality[i][j] for j in range(2)] for i in range(2)]
  assert right[0][0]==strict[0][0]==0
  assert right[1][0]!=0  # enlarged identity observation sees the residual
  assert (strict==right)==(correction==0)
  # right = strict minus equality correction, as for negative prime terms.
  assert [[strict[i][j]-equality[i][j] for j in range(2)] for i in range(2)]==right
  threshold_checks+=1
print(json.dumps({
 'scope':'rational mass-reallocation and endpoint/enlarged observation algebra only',
 'signed_reallocation_checks':scalar_checks,'threshold_observation_controls':threshold_checks,
 'physical_pole_replaced_by_positive_squares':False,
 'actual_contact_constructed':False,'enlarged_persistence_claimed':False,
 'lean_certified':False,'f4_closed':False,'full_transport_closed':False
},indent=2,sort_keys=True))
