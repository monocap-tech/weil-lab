"""Exact compression controls for fresh right packet custody; no actual contact computation."""
from fractions import Fraction as F
import json

def transpose(a):
 return [list(x) for x in zip(*a)]
def multiply(a,b):
 return [[sum((a[i][k]*b[k][j] for k in range(len(b))),F(0))
          for j in range(len(b[0]))] for i in range(len(a))]
def subtract(a,b):
 return [[a[i][j]-b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
def inverse2(a):
 det=a[0][0]*a[1][1]-a[0][1]*a[1][0]
 assert det>0
 return [[a[1][1]/det,-a[0][1]/det],[-a[1][0]/det,a[0][0]/det]]

checks=0
enlarged_failures=0
for alpha in [F(1,2),F(1),F(3)]:
 for s in [F(-2),F(0),F(1)]:
  for tau in [F(1,3),F(1),F(2)]:
   for nu in [F(-1),F(0),F(1)]:
    factor=[[alpha,s],[F(0),tau]]
    row=[[alpha,nu]]
    inc=[[F(1)],[F(0)]]
    g=multiply(transpose(factor),factor)
    assert g[0][0]>0 and g[0][0]*g[1][1]-g[0][1]**2==alpha**2*tau**2>0
    a=subtract(g,multiply(transpose(row),row))
    gc=multiply(multiply(transpose(inc),g),inc)
    rc=multiply(row,inc)
    pc=multiply(transpose(inc),transpose(factor))
    cc=[[-multiply(factor,inc)[i][0]*rc[0][0]/gc[0][0]] for i in range(2)]
    assert multiply(pc,transpose(pc))==gc
    assert multiply(pc,cc)==[[-alpha]]
    assert multiply(transpose(cc),cc)==[[F(1)]]
    assert multiply(multiply(transpose(inc),a),inc)==[[F(0)]]
    positive=multiply(factor,inc)
    assert multiply(cc,[[-alpha]])==positive
    assert sum(x[0]**2 for x in positive)==alpha**2
    # Squared pair normalization divides by d^2=2 alpha^2.
    assert alpha**2/(2*alpha**2)==F(1,2)
    enlarged_residual=multiply(a,inc)
    cb=multiply(multiply(factor,inverse2(g)),transpose(row))
    cb=[[-x[0]] for x in cb]
    enlarged_adjoint=multiply(cb,[[-alpha]])
    assert (enlarged_adjoint==positive)==(s==nu)
    assert (enlarged_residual==[[F(0)],[F(0)]])==(s==nu)
    if s!=nu: enlarged_failures+=1
    checks+=1
times=[F(1)+F(1, n+2) for n in range(20)]
assert all(F(1)<t<F(2) for t in times)
assert all(times[i+1]<times[i] for i in range(19))
print(json.dumps({
 'scope':'rational endpoint/ambient operator controls and right-approach orientation; analytic filtration proved in note',
 'operator_controls':checks,'nonzero_enlarged_residual_controls':enlarged_failures,
 'normalized_positive_squared_norm':'1/2','normalized_negative_squared_norm':'1/2',
 'right_sequence_strictly_decreasing':True,
 'actual_contact_constructed':False,'prescribed_historical_packet_identified':False,
 'lean_certified':False,'f4_closed':False,'full_transport_closed':False
},indent=2,sort_keys=True))
