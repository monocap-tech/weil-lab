"""E19B: literal consecutive-cell Gram numerical pilot and exact rational reserve.
Requires sympy, mpmath, numpy. The rational reserve is conditional on the
centered kernel identity, physical carrier admission and source moment cancellation.
It does not enclose the E16 residual Gram or certify RH.
"""
import sympy as S
import mpmath as m
import numpy as np

h=S.Rational(11,3325)
t,u=S.symbols('t u')
b=t**5*(1-t)**5
v=S.expand(S.diff(b,t,3)-h*h/4*S.diff(b,t))
C=S.integrate(S.expand(v*v.subs(t,t+u)),(t,0,1-u)).expand()
c0=C.subs(u,0)
assert S.expand(v.subs(t,1-t)+v)==0
assert S.integrate(v,(t,0,1))==0
assert C.subs(u,1)==0 and S.diff(C,u).subs(u,0)==0
assert S.degree(C,u)==19
assert h*c0==S.Rational(12994320639248774641,98293908912022687500000)
assert 34*h<S.Rational(693147180,10**9)

# Exact lower log(2), by the positive atanh series.
log2lo=2*sum((S.Rational(1,3)**(2*n+1)/(2*n+1) for n in range(12)),S.Integer(0))
log2hi=log2lo+2*S.Rational(1,3)**25/(25*(1-S.Rational(1,9)))
assert log2lo>S.Rational(693147180,10**9)
assert log2hi<S.Rational(7,10)
assert S.Rational(2,3)+S.Rational(11,7)+5*log2hi<6 # -A(0)<6, pi<22/7<4
assert h< S.Rational(1,243) # log(1/h)>5 since e<3
assert 2*h<S.Rational(1,100)

# C0-C(u)>=0 by Cauchy-Schwarz.
# K(s)>=1/(2s)-1/4 for s>0. Integrate tail only from h to 1.
# Therefore G0 > -3/2*h*C0 + h*int((C0-C)/u) - h^2/2*int(C0-C).
diaglo=S.Rational(-3,2)*h*c0+h*S.integrate(S.cancel((c0-C)/u),(u,0,1))-h*h/2*S.integrate(c0-C,(u,0,1))
assert diaglo==S.Rational(11117912002666471466334236369,57205226720091440503012500000000)
assert diaglo>S.Rational(19,100000)

# For adjacent cells, |K(s)-1/(2s)|<=1 for 0<s<=2h.
# |C(u)|<=C0 so the deviation from the singular rational/log integral
# is at most 2*h^2*C0. The log coefficient is negative.
sing=-h/2*S.integrate(S.cancel(C/(1+u)+C/(1-u)),(u,0,1))
L=S.log(2)
coef=sing.coeff(L)
const=sing-coef*L
assert coef<0 and const.is_Rational
offhi=const+coef*log2lo+2*h*h*c0
assert offhi<S.Rational(18,10**7)
# For d>=1, exponential factorization and v(1-t)=-v(t) imply
# 0<=G_d<=G_1; integrability at contact follows from C's endpoint zeros.
# Therefore every row has at most 33 off-diagonals (66 is conservative).
reserve=diaglo-33*offhi
assert reserve>S.Rational(13,100000)
print("rational diagonal lower",diaglo)
print("rational off-diagonal upper",offhi)
print("rational Gershgorin lower",reserve, float(reserve))

# Independent arbitrary-precision diagnostic, not an interval proof.
for dps in [45,70]:
    m.mp.dps=dps
    H=m.mpf(11)/3325
    c=m.mpf(int(c0.p))/int(c0.q)
    def poly(p):
        co=[m.mpf(int(x.p))/int(x.q) for x in S.Poly(p,u).all_coeffs()]
        return lambda x:m.polyval(co,x)
    cp=poly(S.cancel(C/(1-u)**5))
    dp=poly(S.cancel((c0-C)/u**2))
    cf=lambda x:(1-x)**5*cp(x)
    cd=lambda x:x*x*dp(x)
    K=lambda s:m.exp(-s/2)/(-m.expm1(-2*s))
    A0=m.digamma(m.mpf(1)/4)-m.log(m.pi)
    tail=m.atanh(m.exp(-H/2))+m.atan(m.exp(-H/2))
    g0=A0*H*c+2*H**2*m.quad(lambda x:K(H*x)*cd(x) if x else 0,[0,.25,.5,.75,1])+2*H*c*tail
    gs=[g0]
    for d in range(1,34):
        def fn(x):
            if x==1 and d==1:
                return m.mpf(0)
            return cf(x)*(K(H*(d+x))+K(H*(d-x)))
        gs.append(-H**2*m.quad(fn,[0,.25,.5,.75,1]))
    A=np.array([[float(gs[abs(i-j)]) for j in range(34)] for i in range(34)])
    eig=np.linalg.eigvalsh(A)
    print("precision",dps,"diagonal",m.nstr(gs[0],25),"lag1",m.nstr(gs[1],25))
    print("eigenvalues",eig[0],eig[-1])
    print("numerical Gershgorin",min(A[i,i]-sum(abs(A[i,j]) for j in range(34) if i!=j) for i in range(34)))
    print("all lags",[m.nstr(x,25) for x in gs])
