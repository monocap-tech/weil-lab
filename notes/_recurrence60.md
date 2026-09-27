# SZ edge recurrence 60 — edge-supported dyadic propagation and parity edge inverse normal form

Date: 2026-09-27
Branch: sz-cross-collar
Status: UNRATIFIED RESIDUE / NF PASS
Canonical parent: SZ-CROSS-COLLAR-3
Immediate residue: series-59
Public promotion: forbidden

## Objective

Exploit the first common source from series-59,

h:=Df=-Nf,

for a four-delay prime-silent source f.

Because N contains only the log3 and log5 symmetric shifts and both delays exceed L/2, h is supported on the two log3 edge blocks.

The initial target was to propagate edge-field vanishing of

G_c h,
G_c D h,
G_c D^2 h,
G_c D^3 h

through the finite dyadic support graph.

The support audit produces a stronger normalization.

Since 0 is not in spec(D), one may solve

f=D^{-1}h

exactly fiberwise.

Substituting into

h=-Nf

reduces the entire ambient four-delay prime-silent equation to a two-edge functional system.

Reflection parity then collapses this to one scalar profile equation.

Thus the remaining post-log(16/3) ambient prime-silent problem is equivalent to two scalar parity recurrences.

This is a much smaller frontier than the twelve-field edge-Runge problem.

No injectivity extension is claimed in this pass.

## 1. Constants

Set

a=log2,
b=log3,
d=log5,

gamma=1/sqrt2.

Use the arithmetic gaps

R=d-b=log(5/3),

r=b-a=log(3/2),

q=2a-b=log(4/3),

s=d-2a=log(5/4),

p=R-r=log(10/9).

Let

u=L-d,

w=L-b=R+u,

omega=L-2a=s+u,

v=w-r=p+u.

Throughout

log5<L<=log6,

one has

0<u<=log(6/5),

0<omega<=r,

0<v<=q,

and

w<=a.

At strict L<log6,

omega<r,
v<q,
w<a.

The three endpoint equalities occur simultaneously at L=log6.

## 2. The first common source is edge supported

Let

f in ker(D+N).

Define

h=Df=-Nf.

Because

N
=
beta C_b
+
delta C_d

and both

b>L/2,
d>L/2,

the output of N is supported on

boxed:
E_b
=
(0,L-b)
union
(b,L).

Therefore

boxed:
supp(h)
subset
(0,w)
union
(b,L).

This is the source-side edge support discovered in series-59.

## 3. Dyadic support propagation

The support graph under

D=C_a+gamma C_(2a)

is finite.

Let S_0 be the edge support of h.

Then, for strict L<log6,

boxed:
S_0
=
(0,w)
union
(b,L).

One application of D gives support contained in

boxed:
S_1
=
(0,omega)
union
(r,L-r)
union
(2a,L).

A second application gives support contained in

boxed:
S_2
=
(0,w)
union
(a,L-a)
union
(b,L).

Further support propagation alternates:

boxed:
supp(D^(2m+1)h) subset S_1,

boxed:
supp(D^(2m+2)h) subset S_2.

At L=log6 the intervals merge and S_1 fills the whole support interval.

For strict L<log6 the union

S_0 union S_1 union S_2

already covers (0,L).

Thus the four common sources have enough support reach to touch every source cell, but support coverage alone does not imply field propagation.

## 4. D is invertible

Series-51 gives

spec(D)
=
{
1,
-1,
-1/sqrt2,
(1+sqrt17)/(2sqrt2),
(1-sqrt17)/(2sqrt2)
}.

Therefore

boxed:
0 notin spec(D),

and D is boundedly invertible.

Hence every prime-silent source is recovered from its edge source by

boxed:
f=D^(-1)h.

Conversely, an edge-supported h satisfying

h=-N D^(-1)h

produces a prime-silent source

f=D^(-1)h.

Thus the ambient four-delay prime-silent problem is exactly an edge-source fixed-point problem.

## 5. Dyadic fiber inverse

Decompose by residue modulo

a=log2.

### Three-point fibers

For

0<t<omega,

the dyadic fiber is

t,
t+a,
t+2a.

The D matrix is

D_3
=
[0 1 gamma;
 1 0 1;
 gamma 1 0].

Its inverse is

boxed:
D_3^(-1)
=
[
-gamma, 1/2, gamma;
1/2, -gamma/2, 1/2;
gamma, 1/2, -gamma
].

Because h is edge supported, the middle node vanishes on every three-point fiber.

Writing the edge values as

x(t)=h(t),

z(t+q)=h(t+2a),

one gets

boxed:
f(t)
=
gamma[z(t+q)-x(t)],

boxed:
f(t+a)
=
(1/2)[x(t)+z(t+q)],

boxed:
f(t+2a)
=
-gamma[z(t+q)-x(t)].

### Two-point fibers

For

omega<t<a,

D is the swap matrix

[0 1;
 1 0],

hence D^(-1)=D.

These formulas determine the two edge restrictions of f exactly.

## 6. Edge profile coordinates

Define

boxed:
x(t)=h(t),

boxed:
z(t)=h(b+t),

for

0<t<w.

Write

f_L(t)=f(t),

f_R(t)=f(b+t).

The dyadic inverse gives the exact piecewise formulas

boxed:
f_L(t)
=
gamma[z(t+q)-x(t)],
0<t<omega;

boxed:
f_L(t)=0,
omega<t<r;

boxed:
f_L(t)=z(t-r),
r<t<w.

Likewise

boxed:
f_R(t)=x(r+t),
0<t<v;

boxed:
f_R(t)=0,
v<t<q;

boxed:
f_R(t)
=
gamma[x(t-q)-z(t)],
q<t<w.

No approximation is involved.

## 7. N on the two edge blocks

Identify the two log3 edge blocks with L2(0,w).

Series-51 gives

N
=
[0, beta I+delta T;
 beta I+delta T^*, 0],

where

T

is the truncated left shift by

R=d-b=log(5/3).

Because

w=R+u,

the shift is nonzero only on an interval of length u.

Thus the equation

h=-Nf

is

boxed:
x(t)
+
beta f_R(t)
+
delta 1_(t<u) f_R(t+R)
=
0,

and

boxed:
z(t)
+
beta f_L(t)
+
delta 1_(t>R) f_L(t-R)
=
0.

Substitute Section 6.

## 8. Closed two-profile edge inverse system

The left-edge equation becomes

boxed:
x(t)
+
beta x(r+t)
+
delta gamma
[
x(s+t)-z(R+t)
]
=
0,
0<t<u;

boxed:
x(t)+beta x(r+t)=0,
u<t<v;

boxed:
x(t)=0,
v<t<q;

boxed:
x(t)
+
beta gamma
[
x(t-q)-z(t)
]
=
0,
q<t<w.

The right-edge equation is

boxed:
z(t)
+
beta gamma
[
z(t+q)-x(t)
]
=
0,
0<t<omega;

boxed:
z(t)=0,
omega<t<r;

boxed:
z(t)+beta z(t-r)=0,
r<t<R;

boxed:
z(t)
+
beta z(t-r)
+
delta gamma
[
z(t-s)-x(t-R)
]
=
0,
R<t<w.

This system is exactly equivalent to

(D+N)f=0.

It is the prime-silent edge inverse system registered in the terminology file.

## 9. Reflection parity

Both D and N commute with the source reflection

(Rho g)(t)=g(L-t).

Hence ker(D+N) decomposes into even and odd parity sectors.

Take one parity

epsilon in {+1,-1}.

For h of parity epsilon,

h(L-s)
=
epsilon h(s).

In edge coordinates this is

boxed:
z(t)
=
epsilon x(w-t).

Therefore the two-profile system reduces to one scalar profile x.

The right-edge equations are the reflected copies of the left-edge equations, so one may retain only the four x-equations.

## 10. Scalar parity edge recurrence

For each

epsilon in {+1,-1},

a parity prime-silent source is equivalent to

x in L2(0,w)

satisfying

boxed:
x(t)
+
beta x(r+t)
+
delta gamma
[
x(s+t)-epsilon x(u-t)
]
=
0,
0<t<u;

boxed:
x(t)+beta x(r+t)=0,
u<t<v;

boxed:
x(t)=0,
v<t<q;

boxed:
x(t)
+
beta gamma
[
x(t-q)-epsilon x(w-t)
]
=
0,
q<t<w.

Conversely every solution x reconstructs:

1. z(t)=epsilon x(w-t);
2. the edge source h;
3. f=D^(-1)h;
4. a parity solution of (D+N)f=0.

Thus:

boxed:
ker(D+N)=0

if and only if both parity edge recurrences have only the zero solution.

This is the parity edge recurrence registered in the terminology file.

## 11. Exact dead interval

The scalar system contains the hard zero strip

boxed:
x(t)=0,
v<t<q.

Its length is

q-v.

Now introduce

j
=
r-q
=
log(9/8),

k
=
q-s
=
log(16/15).

One checks

p+k=q-j.

Set

boxed:
e
=
u-k
=
L-log(16/3).

Then

boxed:
q-v
=
j-e.

Hence the forced zero interval has exactly length

boxed:
j-e.

At the last previously proved positive threshold

L=log(16/3),

e=0

and the dead interval has full length j.

At the top of the four-delay chamber

L=log6,

e=j

and the dead interval closes exactly.

This identifies the geometric source of the increasing difficulty near log6.

## 12. Remaining chamber normalization

The open post-series-31 range is

log(16/3)<L<=log6.

In the new variable e this becomes

boxed:
0<e<=j=log(9/8).

So the entire unresolved four-delay chamber is encoded by one scalar parity recurrence with a parameter in the short interval

boxed:
0<e<=0.117783....

All other shift lengths and coefficients are fixed arithmetic constants.

This is substantially smaller than the previous ambient matrix/cocycle descriptions.

## 13. Tail elimination identity

For later use, write the final recurrence with

t=q+y.

Since

w-q
=
omega,

one obtains

boxed:
x(q+y)
=
-beta gamma
[
x(y)-epsilon x(omega-y)
],
0<y<omega.

Thus the entire tail

(q,w)

is determined by values in

(0,omega).

Substituting this identity into the second equation yields

boxed:
x(t)
=
beta^2 gamma
[
x(j+t)-epsilon x(v-t)
],
u<t<v.

Substituting it into the first equation yields

boxed:
x(t)
=
beta^2 gamma
[
x(j+t)-epsilon x(v-t)
]
-
delta gamma
[
x(s+t)-epsilon x(u-t)
],
0<t<u,

whenever the displayed arguments are read through the same tail identity if they cross q.

These are the scalar analogues of the old lower-defect recurrences.

## 14. Relation to the previous recurrence chain

The constants that dominated GERM-31 through GERM-46 reappear canonically:

j=log(9/8),

k=log(16/15),

p=log(10/9),

s=log(5/4),

with

j-p
=
log(81/80).

The earlier small recurrence step

h=log(81/80)

is therefore

boxed:
h=j-p,

the difference between the parity-tail reflection scale j and the one-prime edge offset p.

So the old scalar recurrence was not accidental.

It was a coordinate shadow of this exact parity edge inverse system.

The present formulation obtains it directly from D^(-1), without introducing the p-relay or the ten-residue global column model.

## 15. Why this does not yet prove injectivity

The zero strip

(v,q)

shrinks to zero as

e up to j.

For e>0 the remaining equations transport data across the short arithmetic shifts

j,
k,
p,
s,

and reflected arguments.

Near e=j there is no open dead interval from which a naive support induction can start.

Therefore the scalar reduction is not itself a proof of triviality.

It removes:

- ambient spectral-shadow bookkeeping;
- field-to-edge Runge;
- nonkernel field transport;
- and global residue closure

from the ambient prime-silent classification problem.

But it leaves a finite scalar arithmetic recurrence to solve.

## 16. Relation to K_c^{ps}

If both parity recurrences are trivial, then the ambient prime translation operator is injective:

boxed:
ker P_c
=
ker(D+N)
=
{0}

through the four-delay chamber.

This would immediately imply

boxed:
K_c^{ps}=0

without any edge-Runge theorem.

If a nonzero parity recurrence solution exists, it gives an explicit ambient prime-silent source, after which the regular-kernel intersection remains the next question.

So the new scalar system cleanly separates the ambient arithmetic issue from the Weil-kernel issue.

## 17. Result

The edge-supported dyadic propagation experiment has pivoted to an exact inverse normal form.

Positive:

1. h=Df is supported on two edge blocks;
2. D is invertible;
3. D^(-1) is explicit on every two-/three-point dyadic fiber;
4. the ambient prime-silent equation becomes a closed two-edge functional system;
5. parity reduces it to one scalar recurrence;
6. the entire remaining support interval is parameterized by
   0<e<=log(9/8);
7. the forced zero strip has exact length log(9/8)-e;
8. the earlier recurrence constants emerge directly from this inverse system.

No claim of four-delay injectivity is made.

The fixed-L arithmetic frontier has become:

boxed:
solve the two parity edge recurrences for
0<e<=log(9/8).

## Fixed-L status

The last load-bearing continuous prime-channel injectivity range remains

0<L<=log(16/3).

The canonical theorem cursor remains

SZ-CROSS-COLLAR-3.

## Next frontier

Next target:

SZ-KERNEL-EDGE-GERM-61 / PARITY EDGE RECURRENCE CLOSURE

The next pass should work only with the scalar recurrence of Section 10.

Priority:

1. partition 0<e<=j by the finite crossing thresholds of the arguments
   t+j,
   t+s,
   v-t,
   u-t
   against q and the dead interval;

2. eliminate the tail using Section 13;

3. derive the minimal scalar transfer on the base interval;

4. exploit the exact reflection sign epsilon=+-1 separately;

5. certify nonresonance throughout 0<e<=j, or isolate the first genuine resonance value if one exists.

A successful closure would prove ambient four-delay prime-channel injectivity all the way to L=log6 and therefore settle K_c^{ps}=0 throughout the chamber.

No public promotion and no canonical cursor movement are asserted.
