"""Exact finite algebra controls, not analytic or actual-zeta certification."""
from fractions import Fraction as F
from pathlib import Path
import json
from certify_native_kernel_de_branges_attachment import g,add,sub,mul,conj,scale,abs2,linear_product,evaluate

count=0
def check(b):
    global count
    assert b
    count+=1
def div(a,b):
    assert abs2(b)
    return scale(mul(a,conj(b)),1/abs2(b))
def poly(nodes):
    p=[g(1)]
    for x in nodes: p=linear_product(p,g(x))
    return p
def quotient(p,t):
    q=[g()]*(len(p)-1)
    q[-1]=p[-1]
    for j in range(len(q)-2,-1,-1): q[j]=add(p[j+1],scale(q[j+1],t))
    check(linear_product(q,g(t))==p)
    return q
def total(xs):
    s=g()
    for x in xs:s=add(s,x)
    return s

for r in range(1,5):
    X=[F(2*j+1) for j in range(r)]
    T=[F(-2),F(-4),F(-6)]
    P=poly(X); Phi=poly(T)
    L=[]; dp=[]
    for x in X:
        q=quotient(P,x); d=evaluate(q,g(x)); dp.append(d)
        L.append([div(c,d) for c in q])
        check(abs2(evaluate(Phi,g(x)))>0)
    for i in range(r):
        for j,x in enumerate(X):
            check(evaluate(L[i],g(x))==g(int(i==j)))
            hi=div(mul(evaluate(Phi,g(x)),evaluate(L[i],g(x))),evaluate(Phi,g(X[i])))
            check(hi==g(int(i==j)))
    p=[g(j+1,F(j,3)) for j in range(r)]
    rows=[mul(evaluate(Phi,g(x)),evaluate(p,g(x))) for x in X]
    alphas=[g(j+2,F(1,2)) for j in range(r)]
    for i in range(r):check(div(mul(alphas[i],rows[i]),alphas[i])==rows[i])
    for z in [g(0,F(1,2)),g(8,F(2,3)),g(-9),g(11)]:
        lift=total(div(mul(rows[i],evaluate(L[i],z)),evaluate(Phi,g(X[i]))) for i in range(r))
        check(lift==evaluate(p,z))
        for t in T:
            pt=evaluate(P,g(t));check(abs2(pt)>0)
            a=sub(div(g(1),sub(z,g(t))),total(div(evaluate(L[i],z),g(X[i]-t)) for i in range(r)))
            check(a==div(evaluate(P,z),mul(pt,sub(z,g(t)))))
            raw=div(mul(g(0,1),evaluate(Phi,z)),sub(z,g(t)))
            correction=total(div(mul(mul(g(0,1),evaluate(Phi,z)),evaluate(L[i],z)),g(X[i]-t)) for i in range(r))
            check(sub(raw,correction)==mul(mul(g(0,1),evaluate(Phi,z)),a))
    leading=total(div(rows[i],mul(evaluate(Phi,g(X[i])),dp[i])) for i in range(r))
    check(leading==p[-1])
    phase=g(1)
    for j in range(r-1):phase=mul(phase,g(0,-1))
    kappa=g(F(3,2),F(1,4))
    check(mul(div(kappa,phase),leading)==mul(kappa,div(p[-1],phase)))

# Complete signed graph cancellation and retained positive-eigenmode residual.
# Synthetic finite controls only: these are not actual source packets.
for mu in [F(0),F(1,3),F(2)]:
    for mass in [F(1),F(5,2)]:
        positive=F(7);negative=positive-mu*mass
        check(positive-negative==mu*mass)
        if mu:check(positive-negative!=0)

out={"passed":True,"exact_checks":count,"scope":"finite Gaussian-rational interpolation algebra only","analytic_certification":False,"actual_zeta_nodes_computed":False,"lean_certification":False,"F4_closed":False}
path=Path('notes/data/RPB108_ACTUAL_ROW_INTERPOLATION_VALIDATION_20261007.json')
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
