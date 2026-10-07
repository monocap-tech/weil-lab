"""Exact projection, residual energy and negative-trial controls."""
from fractions import Fraction as F
import json

def tr(a): return [list(row) for row in zip(*a)]
def mm(a,b):
 return [[sum((a[i][k]*b[k][j] for k in range(len(b))),F(0))
          for j in range(len(b[0]))] for i in range(len(a))]
def sub(a,b): return [[x-y for x,y in zip(ar,br)] for ar,br in zip(a,b)]
def neg(a): return [[-x for x in row] for row in a]
def inv(a):
 d=a[0][0]*a[1][1]-a[0][1]*a[1][0]
 assert d>0
 return [[a[1][1]/d,-a[0][1]/d],[-a[1][0]/d,a[0][0]/d]]
def norm2(v): return sum((x[0]**2 for x in v),F(0))
def quad(a,v): return mm(mm(tr(v),a),v)[0][0]

checks=nonzero=nonreduced=0
for alpha in [F(1,2),F(1),F(3)]:
 for s in [F(-2),F(0),F(1)]:
  for tau in [F(1,3),F(1),F(2)]:
   for nu in [F(-1),F(0),F(1)]:
    factor=[[alpha,s],[F(0),tau]]
    row=[[alpha,nu]]
    k=[[F(1)],[F(0)]]
    g=mm(tr(factor),factor)
    gi=inv(g)
    a=sub(g,mm(tr(row),row))
    c=neg(mm(mm(factor,gi),tr(row)))
    c_old=[[F(-1)],[F(0)]]
    positive=mm(factor,k)
    u=[[-alpha]]
    cu=mm(c,u)
    delta=sub(cu,positive)
    r=mm(a,k)
    v=mm(gi,r)
    e=mm(tr(r),v)[0][0]
    assert e==alpha**2*(s-nu)**2/tau**2>=0
    assert c[0][0]==c_old[0][0]  # projection onto old positive carrier
    assert delta[0][0]==0
    assert norm2(cu)-alpha**2==norm2(delta)==e
    assert delta==neg(mm(factor,v))
    assert mm(tr(factor),delta)==neg(r)
    trial=sub(k,v)
    assert trial==neg(mm(mm(gi,tr(row)),u))
    assert quad(a,trial)==-e-norm2(mm(row,v))
    if s!=nu:
     assert e>0 and quad(a,trial)<0
     nonzero+=1
    for z in [F(-2),F(0),F(3,5)]:
     # Endpoint P=(alpha,0); invisible factor component is (0,z).
     alternative=[[F(-1)],[z]]
     assert mm([[alpha,F(0)]],alternative)==[[-alpha]]
     assert norm2(mm(alternative,u))==norm2(mm(c_old,u))+z*z*alpha*alpha
     nonreduced+=1
    checks+=1
print(json.dumps({
 'scope':'rational factor/projection/residual controls only; actual identities proved analytically in note',
 'operator_controls':checks,'strict_gain_and_negative_trial_controls':nonzero,
 'nonreduced_factor_controls':nonreduced,
 'actual_contact_constructed':False,'contact_exclusion_proved':False,
 'lean_certified':False,'f4_closed':False,'full_transport_closed':False
},indent=2,sort_keys=True))
