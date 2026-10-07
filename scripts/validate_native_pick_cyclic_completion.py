"""Exact finite controls for NF46. Infinite/domain proofs are in the note."""
from fractions import Fraction as F
from pathlib import Path
import json
from certify_native_kernel_de_branges_attachment import g,add,sub,mul,conj,scale,abs2

count=0
def check(b):
    global count
    assert b
    count+=1

def div(x,y):
    d=abs2(y)
    assert d
    return scale(mul(x,conj(y)),1/d)

def ip(x,y):
    r=g()
    for a,b in zip(x,y):
        r=add(r,mul(a,conj(b)))
    return r

nodes=[F(-2),F(1),F(4)]
dp=[F(2),F(-3),F(4)]
d=[F(1),F(4),F(9)]
c=[d[j]/dp[j]**2 for j in range(3)]
points=[g(0,F(1,2)),g(1,F(2,3)),g(-1,F(1,4)),g(2,F(1,3))]

def kw(w):
    # Q-coordinate amplitudes of u_t/[(w-t)Phi'(t)].
    return [div(g(j+1),scale(sub(w,g(nodes[j])),dp[j])) for j in range(3)]

def M(w,b=F(0)):
    r=scale(w,b)
    for j,t in enumerate(nodes):
        r=add(r,sub(div(g(c[j]),sub(g(t),w)),g(c[j]*t/(1+t*t))))
    return r

for w in points:
    k=kw(w)
    for v in points:
        H=ip(k,kw(v))
        check(H==div(sub(M(w),conj(M(v))),sub(w,conj(v))))
        # The linear coefficient produces an additional positive constant Gram.
        check(div(sub(M(w,F(2)),conj(M(v,F(2)))),sub(w,conj(v)))==add(H,g(2)))
    check(ip(k,k)==g(sum(abs2(x) for x in k)))
    # Exact reconstruction from each finite atom coordinate.
    reconstructed=[]
    for j,t in enumerate(nodes):
        ut=[g()] * 3
        ut[j]=g(j+1)
        coefficient=div(ip(k,ut),g(d[j]))
        check(coefficient==div(g(1),scale(sub(w,g(t)),dp[j])))
        reconstructed.append(mul(coefficient,ut[j]))
    check(reconstructed==k)
    # A whole positive direct summand can remain invisible to the Pick response.
    extended=k+[g()]
    check(ip(extended,extended)==ip(k,k))
    check(ip(extended,[g(),g(),g(),g(1)])==g())

# Fourier resolvent formula has exact support-matching normalization.
for y in [F(2),F(3),F(5)]:
    for eta in [F(-2),F(0),F(7,3)]:
        P=g(2,F(1,3))
        Phiy=g(3,F(-1,2))
        old=div(mul(g(0,1),sub(div(P,Phiy),g(1))),sub(g(eta),g(0,y)))
        new=div(sub(g(1),div(P,Phiy)),g(y,eta))
        check(old==new)
        check(abs2(div(g(1),g(y,eta)))<=1/y**2)

# Complete signed analysis is injective, but cannot descend unchanged to Q quotient.
def Gamma(x):
    return x+[x[0]]
def signed(x,y):
    return sub(ip(x[:4],y[:4]),mul(x[4],conj(y[4])))
for x in [[g(1),g(2),g(3),g(4)], [g(0,1),g(1),g(),g(2)]]:
    pi=[g()]+x[1:]
    pk=[x[0],g(),g(),g()]
    check(signed(Gamma(x),Gamma(x))==ip(x[1:],x[1:]))
    check(signed(Gamma(pi),Gamma(pi))==signed(Gamma(x),Gamma(x)))
    check(Gamma(pk)!=[g()]*5)
    check([add(a,b) for a,b in zip(Gamma(pi),Gamma(pk))]==Gamma(x))
    check(Gamma(x)!=Gamma(pi))

result={'status':'PASS','exact_checks':count,
        'scope':'finite atom/resolvent/gauge algebra only; analytic proofs in note',
        'actual_infinity_coefficient':'zero by analytic norm estimate',
        'completeness':'jump-generated Q quotient only',
        'whole_native_generation':'unproved',
        'original_source_lift':'retains Gamma(P_K k_w)',
        'bounded_sharp_subsequence':'unproved','F4':'open','lean_certified':False}
out=Path(__file__).resolve().parents[1]/'notes/data/RPB108_PICK_CYCLIC_COMPLETION_VALIDATION_20261007.json'
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
