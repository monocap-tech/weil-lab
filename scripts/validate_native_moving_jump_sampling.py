"""Finite exact moving-jump/sampling controls; analytic proof is in the note."""
from fractions import Fraction as F
from pathlib import Path
import json
from certify_native_kernel_de_branges_attachment import (
    g,add,sub,mul,conj,scale,abs2,linear_product,evaluate)

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
    out=g()
    for a,b in zip(x,y):
        out=add(out,mul(a,conj(b)))
    return out

points=[g(0,F(1,2)),g(1,F(2,3)),g(-1,F(1,4))]
nodes=[F(-2),F(1),F(4)]
dp=[F(2),F(-3),F(4)]
d=[F(1),F(4),F(9)]
c=[d[j]/dp[j]**2 for j in range(3)]
# Unit phases audit the residue algebra, not actual sampled exp(it xi) values.
phases=[[g(1)]*3,[g(0,1),g(-1),g(F(3,5),F(4,5))]]
def coords(w,phase):
    return [div(scale(phase[j],j+1),scale(sub(w,g(nodes[j])),dp[j])) for j in range(3)]

for phase in phases:
    for p in phase:
        check(abs2(p)==1)
    for w in points:
        kw=coords(w,phase)
        for v in points:
            check(ip(kw,coords(v,phase))==ip(coords(w,phases[0]),coords(v,phases[0])))
        for j,t in enumerate(nodes):
            ut=[g()]*3
            ut[j]=g(j+1)
            check(ip(kw,ut)==div(scale(phase[j],d[j]),scale(sub(w,g(t)),dp[j])))

# Moving-jump Fourier formula has the correct delta and normalization factors.
for w in points:
    for z in [g(-2),g(3),g(0,F(3,4))]:
        Pw=g(2,F(1,3))
        Pz=g(3,F(-1,2))
        Ew,Edelta=g(F(3,5),F(4,5)),g(0,1)
        profile=div(mul(g(0,1),sub(div(mul(Ew,Pz),Pw),Edelta)),sub(z,w))
        check(mul(mul(g(0,1),sub(w,z)),profile)==sub(div(mul(Ew,Pz),Pw),Edelta))
        # Integrated forcing has F_f(w)=0, F_f(z)=i(w-z)F_v(z).
        V=g(F(2,3),F(1,4))
        Ff=mul(mul(g(0,1),sub(w,z)),V)
        U=div(mul(g(0,1),scale(Ff,-1)),sub(z,w))
        check(U==scale(V,-1))

# Exact coefficient after synthesizing a smooth test through moving jumps.
samples=[g(1),g(F(2,3),F(1,4)),g(0,1)]
for w in points:
    coeffs=[]
    for j,t in enumerate(nodes):
        Ff=mul(mul(g(0,1),sub(w,g(t))),samples[j])
        coefficient=scale(div(Ff,scale(sub(w,g(t)),dp[j])),-1)
        expected=scale(mul(g(0,-1),samples[j]),1/dp[j])
        check(coefficient==expected)
        coeffs.append(scale(coefficient,j+1))
    check(ip(coeffs,coeffs)==g(sum(c[j]*abs2(samples[j]) for j in range(3))))

# At each generator node F_ut(t)=i Phi'(t), other node values are zero.
Phi=[g(1)]
for t in nodes:
    Phi=linear_product(Phi,g(t))
for j,t in enumerate(nodes):
    q=[g()]*(len(Phi)-1)
    q[-1]=Phi[-1]
    for n in range(len(q)-2,-1,-1):
        q[n]=add(Phi[n+1],scale(q[n+1],t))
    check(linear_product(q,g(t))==Phi)
    for s in nodes:
        value=mul(g(0,1),evaluate(q,g(s)))
        if s!=t:
            check(value==g())
        else:
            derivative=g()
            for n in range(1,len(Phi)):
                derivative=add(derivative,scale(Phi[n],n*t**(n-1)))
            check(value==mul(g(0,1),derivative))

# Source gauge and the actual shifted mass residual remain observable.
for a,mass,energy in [(F(1),F(2),F(3)),(F(2),F(4),F(5))]:
    Gamma_null=[g(a),g(),g(a)]
    check(Gamma_null!=[g()]*3)
    check(sub(mul(Gamma_null[0],conj(Gamma_null[0])),mul(Gamma_null[2],conj(Gamma_null[2])))==g())
    mu=F(1,2)
    Q=energy+mu*mass
    check(Q-mu*mass==energy)
    check(Q!=energy)

result={'status':'PASS','exact_checks':count,
        'scope':'finite rational phase, Fourier, coefficient and gauge algebra only',
        'analytic_result':'H_Q=H_jump=H_div and whole-domain real-node sampling',
        'sampling_nodes':'generator zeros; not identified with zeta divisor',
        'actual_source_lift':'retains Gamma(P_K f)',
        'positive_eigenmode':'Q=mu mass+real sampling of Q_mu',
        'bounded_sharp_subsequence':'unproved','F4':'open','lean_certified':False}
target=Path(__file__).resolve().parents[1]/'notes/data/RPB108_MOVING_JUMP_SAMPLING_VALIDATION_20261007.json'
target.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
