# SZ-KERNEL-EDGE-GERM-31 — First post-log5 recurrence chamber

**Date:** 2026-09-26  
**Branch:** sz-cross-collar  
**Status:** UNRATIFIED RESIDUE / NF PASS  
**Canonical parent:** SZ-CROSS-COLLAR-3  
**Immediate residue:** SZ-KERNEL-EDGE-GERM-30  
**Public promotion:** forbidden

## Result

This pass closes the first four-delay chamber

[
log5<Llelog(16/3).
]

The active delays are (log2,log3,log4,log5). For the all-center translation operator

[
(mathsf P_cf)(x)=sum_lambda a_lambda[f(x-lambda)+f(x+lambda)]
]

with zero extension outside ((0,L)),

[
oxed{kermathsf P_c={0}}.
]

Hence (K_c^{m ps}=0) and the fixed-scale prime norm gap persists.

The proof reduces the source to two boundary fibers and then to a scalar second-order recurrence whose terminal gain is nonresonant for the exact Weil weights.

## Chamber geometry

Set

[
a=log2,quad b=log3,quad c=log4=2a,quad d=log5,
]

write (u=L-d), and set

[
s=d-c,quad q=c-b,quad r=b-a,quad ell=L-c=s+u.
]

The chamber condition is

[
0<ule q-s=log(16/15),
]

hence

[
s<ellle q<r<a.
]

Write

[
A=rac{log2}{sqrt2},quad
B=rac{log3}{sqrt3},quad
C=rac{log2}{2},quad
D=rac{log5}{sqrt5},
]

and (eta=B/A, gamma=C/A=1/sqrt2, delta=D/A).

## Two-fiber reduction

Define

[
H(t)=f(t),qquad U(t)=f(a+t),qquad 0<t<ell.
]

Boundary propagation gives

[
f(c+t)=-H(t),
]

[
f=0quad	ext{on }(ell,r),
]

[
f(r+t)=-eta H(t),qquad 0<t<ell,
]

[
f=0quad	ext{on }(r+ell,a).
]

Set

[
p=a+d-2b=log(10/9),qquad
j=2b-3a=log(9/8),
]

so (p+j=s), and

[
d_0=3a-b=log(8/3).
]

The (+a,+b) strip gives

[
f=0quad	ext{on }(a+ell,d_0),
]

and

[
f(d_0+t)=eta H(t),qquad 0<t<ell.
]

Thus (H,U) determine the whole source.

## Exact fiber equations

From the interior boundary strips,

[
U(y)=-gamma H(y),qquad 0<y<j,
]

[
U(y)=-gamma H(y)+eta^2H(y-j),qquad j<y<s,
]

[
U(t)=gamma H(t)-eta^2H(t+j),qquad u<t<u+p,
]

[
U(t)=gamma H(t),qquad u+p<t<ell.
]

The extreme boundaries give

[
U(t)=gamma H(t)+delta H(s+t)-eta^2H(j+t),
qquad 0<t<u,
]

[
U(s+t)=-gamma H(s+t)-delta H(t)+eta^2H(p+t),
qquad 0<t<u.
]

## Eliminate the middle fiber

Put

[
mu=eta^2,qquad G=2gamma=sqrt2,qquad
Delta=mu^2-G^2.
]

Since (9>8), (log3/log2>3/2), so (mu>3/2>G) and (Delta>0).

Define

[
R=rac{Gdelta}{Delta},quad
Q=rac{mu^2}{Delta},quad
T=rac{Delta}{mu^2},quad
E=rac{Gdelta}{mu^2}.
]

Then (EQ/R=1).

For (0<x<u), write

[
X(x)=H(x),qquad S(x)=H(s+x).
]

The fiber system becomes

[
S(x)=RX(x),qquad 0<x<h,
]

[
S(x)=RX(x)-QX(x-h),qquad h<x<u,
]

[
S(x+h)=-TX(x)+ES(x),qquad 0<x<u-h,
]

and

[
S(x)=R^{-1}X(x),qquad u-h<x<u,
]

where

[
h=j-p=log(81/80).
]

Therefore each residue fiber modulo (h) satisfies

[
X(x+h)=Theta X(x)-X(x-h)
]

after the first step, with

[
X(x+h)=Theta X(x)
]

at the start, where

[
Theta=rac{Q-T+ER}{R}.
]

The terminal strip requires

[
X(x)=arrho X(x-h),
qquad
arrho=rac{Q}{R-R^{-1}}.
]

Equivalently,

[
Theta=
rac{G(2mu^2+delta^2-G^2)}{mu^2delta},
]

[
arrho=
rac{mu^2delta G}{delta^2G^2-(mu^2-G^2)^2}.
]

## Nonresonance

Elementary logarithmic bounds from

[
3^{12}>2^{19},quad 3^5<2^8,
]

and

[
5^{10}>2^{23},quad 5^3<2^7
]

give the strict enclosure

[
1.5<arrho<1.8<Theta<2.
]

Also

[
Theta-Theta^{-1}<1.5<arrho.
]

Let

[
P_0=1,quad P_1=Theta,quad
P_{n+1}=Theta P_n-P_{n-1}.
]

A nonzero residue fiber would have to satisfy

[
P_{N+1}=arrho P_N
]

at the terminal strip.

Since

[
ulelog(16/15)<6log(81/80),
]

only (N=0,1,2,3,4) can occur.

For (N=0), resonance would require (Theta=arrho), impossible.

For later steps, (P_0,ldots,P_5>0) in the exact range (1.8<Theta<2). The ratios

[
r_n=P_{n+1}/P_n
]

satisfy

[
r_1=Theta-Theta^{-1}<arrho,
qquad
r_{n+1}=Theta-rac1{r_n},
]

and decrease while positive. Thus (r_n<arrho) for (n=1,ldots,4).

No terminal resonance exists. Every residue fiber vanishes, hence (H=U=0), so (f=0).

Therefore

[
oxed{kermathsf P_c={0}}
qquad
(log5<Llelog(16/3)).
]

Combining with GERM-27--30,

[
oxed{K_c^{m ps}={0}}
qquad
(0<Llelog(16/3)).
]

For every nonzero finite-dimensional (K_c) in this range,

[
|mathsf P_cf|_2gekappa_c|f|_2
]

for some (kappa_c>0). No uniformity in (c), and no shrinking-collar rate, is asserted.

## Next frontier

At (L=log(16/3)), the overlap ordering changes. The next target is

[
oxed{	ext{SZ-KERNEL-EDGE-GERM-32 / SECOND POST-LOG5 RECURRENCE CHAMBER}},
]

covering

[
log(16/3)<Llelog6.
]

The canonical theorem cursor remains (oxed{	ext{SZ-CROSS-COLLAR-3}}).

No public promotion and no canonical cursor movement are asserted.
