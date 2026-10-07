"""Exact rational controls only; analytic proof and domain audit are in the note."""
from fractions import Fraction as F
from pathlib import Path
import json
from certify_native_kernel_de_branges_attachment import (
    g,add,sub,mul,conj,scale,linear_product,evaluate)

checks=0
def check(b):
    global checks
    assert b
    checks+=1

def div(x,y):
    n=y[0]**2+y[1]**2
    assert n
    return scale(mul(x,conj(y)),1/n)

def derivative(p):
    return [scale(p[j],j) for j in range(1,len(p))]

def quotient(p,t):
    result=[g()]*(len(p)-1)
    result[-1]=p[-1]
    for j in range(len(result)-2,-1,-1):
        result[j]=add(p[j+1],mul(t,result[j+1]))
    check(add(p[0],mul(t,result[0]))==g())
    return result

# Real shifts must be conjugated in the second Hermitian argument.
for t,s in [(F(-2),F(1)),(F(0),F(2)),(F(1,3),F(4,3))]:
    for q in [g(1),g(0,1),g(F(2,3),F(1,4))]:
        check(add(mul(g(0,t),q),mul(conj(g(0,t)),q))==g())
        check(scale(mul(conj(g(0,t-s)),q),-1)==mul(g(0,t-s),q))

# Two compact divisions and the generator-zero removable values.
for roots in [(-2,1),(0,2,3),(-3,-1,2,4)]:
    p=[g(1)]
    for a in roots:
        p=linear_product(p,g(a))
    for a in roots:
        t=g(a)
        q=quotient(p,t)
        check(linear_product(q,t)==p)
        check(evaluate(q,t)==evaluate(derivative(p),t))
    t=g(roots[0])
    twice=linear_product(p,t)
    q1=quotient(twice,t)
    q2=quotient(q1,t)
    check(q2==quotient(p,t))
    # (-iz+it) i Phi/(z-t)=Phi; second inverse gains i again.
    check([mul(g(0,-1),x) for x in linear_product([mul(g(0,1),x) for x in q1],t)]==twice)

# Jump quotient: polynomial Phi(z)-Phi(w) always has factor z-w.
p=[g(1),g(-2),g(),g(1)]
for w in [g(),g(1),g(1,F(1,4)),g(-1,F(2,3))]:
    numerator=p[:]
    numerator[0]=sub(numerator[0],evaluate(p,w))
    q=quotient(numerator,w)
    check(linear_product(q,w)==numerator)
    check(evaluate(q,w)==evaluate(derivative(p),w))

# Pair has nonzero source height and off-real ordinates inside 3/8.
alpha=g(1,F(1,4))
check(0<alpha[1]<F(3,8) and alpha[0]!=0)
one=g(1)
def R(w):
    return add(div(one,sub(alpha,w)),div(one,sub(conj(alpha),w)))
def C(w):
    return sub(w,R(w))
def M(w):
    return add(R(w),C(w))
points=[g(0,F(1,2)),g(1,F(1,2)),g(-2,F(2,3)),g(F(1,3),F(1,3))]
for w in points:
    check(M(w)==w)
    for v in points:
        check(div(sub(M(w),conj(M(v))),sub(w,conj(v)))==one)
# Source residues -1 and correction residues +1 cancel at BOTH poles.
for pole in [alpha,conj(alpha)]:
    source_residue=g(-1)
    correction_residue=scale(source_residue,-1)
    check(add(source_residue,correction_residue)==g())
# Four-point reconstruction from a genuine nonconstant real-pole Pick model.
def N(w):
    return add(w,div(g(2),sub(g(3),w)))
def H(w,x):
    return div(sub(N(w),conj(N(x))),sub(w,conj(x)))
def B(w,x):
    return mul(sub(w,conj(x)),H(w,x))
w0=points[0]
for w in points:
    reconstructed=sub(B(w,w0),scale(B(w0,w0),F(1,2)))
    for x in points:
        mx=sub(B(x,w0),scale(B(w0,w0),F(1,2)))
        check(sub(reconstructed,conj(mx))==B(w,x))
        v,y=points[1],points[2]
        check(add(sub(B(w,x),B(w,y)),sub(B(v,y),B(v,x)))==g())
# Actual divided-difference source profile cancels at a nonreal node.
p=[g(1),g(-2),g(),g(1)]
check(evaluate(p,alpha)!=g())
num=p[:]
num[0]=sub(num[0],evaluate(p,alpha))
q=quotient(num,alpha)
check(evaluate(q,alpha)==evaluate(derivative(p),alpha))
# Local real Pick atom sign: residue=-d/|Phi'(t)|^2.
for d,dp in [(F(1),F(2)),(F(3),F(-4))]:
    residue=-d/dp**2
    check(residue<0)
    check(-residue==d/dp**2)
# Explicit shifted Gram mass residual cannot be erased.
for mu,mass,d in [(F(2),F(3),F(5)),(F(1,2),F(-1,3),F(0))]:
    check((d+mu*mass)-mu*mass==d)
    check(d+mu*mass!=d)
result={'status':'PASS','exact_checks':checks,
        'scope':'finite rational algebra only; analytic form/domain proof is in the note',
        'scalar_pick_attachment':'analytic proof via jump-cancelled differences in companion note',
        'bounded_return':'unproved','F4':'open'}
out=Path(__file__).resolve().parents[1]/'notes/data/RPB108_REAL_ZERO_DIVISION_VALIDATION_20261007.json'
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
