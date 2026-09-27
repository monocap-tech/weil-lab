# SZ edge recurrence 50 — ejection compensator separation and symmetric first-prime observability

Date: 2026-09-27
Branch: sz-cross-collar
Status: UNRATIFIED RESIDUE / NF PASS
Canonical parent: SZ-CROSS-COLLAR-3
Immediate residue: series-49
Public promotion: forbidden

## Objective

Attack the ejection compensator identity from series-49 on a hypothetical nonzero

V = K_c^{ps} = K_c intersect ker P_c

in the four-delay chamber.

The first attempt was to separate the one-sided first-prime ejection from the compensator by support or moment structure.

That attempt is too optimistic for two exact reasons:

1. opposite orientations can self-cancel the opposite-parity part of a one-sided ejection;
2. the log4 channel is exactly the second iterate of the log2 symmetric shift, so it already contains the next first-prime ejection together with compression curvature and an explicit boundary projector.

However the parity loophole can be repaired.

The symmetric first-prime ejection itself is dynamically observable, because the ambient prime-silent space contains no nonzero eigenvector of the symmetric log2 shift.

This pass proves that exclusion exactly.

No fixed-L prime-silent triviality theorem is claimed yet.

## 1. Source reflection

Work in right-oriented source coordinates

H=L2(0,L).

Let

R f(s)=f(L-s)

be reflection.

The regular screw kernel K_c is reflection-invariant because the screw kernel is even.

The prime translation operator P_c is also reflection-invariant because every delay enters symmetrically as

S_lambda^+ + S_lambda^-.

Therefore

V=K_c^{ps}

is reflection-invariant and decomposes orthogonally as

V=V_+ direct_sum V_-.

If V is nonzero, at least one parity branch V_epsilon is nonzero.

## 2. Why one-sided observability is not directly visible to prime silence

Fix one parity branch

V_epsilon,

epsilon in {+1,-1},

with orthogonal projection Pi_epsilon.

For an active delay lambda define one-sided ejections

E_{lambda,+}
=
(I-Pi_epsilon)S_lambda^+|_{V_epsilon},

E_{lambda,-}
=
(I-Pi_epsilon)S_lambda^-|_{V_epsilon}.

Because

S_lambda^-
=
R S_lambda^+ R

and Pi_epsilon commutes with R,

for f in V_epsilon,

E_{lambda,-}f
=
epsilon R E_{lambda,+}f.

Let

P_epsilon
=
(I+epsilon R)/2

be the ambient parity projection.

Then

E_{lambda,+}f+E_{lambda,-}f
=
2 P_epsilon E_{lambda,+}f.

The opposite-parity component

P_{-epsilon}E_{lambda,+}f

cancels inside the same plus/minus prime pair.

Therefore the dynamic one-sided ejection floor of series-49 does not by itself give a lower bound on the part of the ejection seen by prime silence.

This is a scope correction to the intended use of series-49.

## 3. Symmetric shift and symmetrized ejection

Define the symmetric shift

C_lambda
=
S_lambda^+ + S_lambda^-.

On V_epsilon define its compression and ejection by

B_lambda
=
Pi_epsilon C_lambda|_{V_epsilon},

F_lambda
=
(I-Pi_epsilon)C_lambda|_{V_epsilon}.

Then

F_lambda
=
E_{lambda,+}+E_{lambda,-}

on V_epsilon.

Prime silence gives the exact symmetric ejection balance

F_a
+
beta F_b
+
gamma F_{2a}
+
delta F_d
=
0,

where

a=log2,

b=log3,

2a=log4,

d=log5,

beta=(log3/sqrt3)/(log2/sqrt2),

gamma=1/sqrt2,

delta=(log5/sqrt5)/(log2/sqrt2).

This is the ejection identity that must actually be separated.

## 4. Exact dyadic prime reduction

Set

T=S_a^+.

Then

T^*=S_a^-.

Let

D_a
=
P_(0,a)
+
P_(L-a,L),

the sum of the two boundary-strip multiplication projections.

The truncated shifts satisfy

T^*T
=
I-P_(0,a),

TT^*
=
I-P_(L-a,L).

Therefore

C_a^2
=
T^2+(T^*)^2+TT^*+T^*T

=
C_{2a}
+
2I
-
D_a.

Hence

boxed:
C_{2a}
=
C_a^2
-
2I
+
D_a.

Since log4=2log2, the four-delay prime-silent equation is equivalent to

boxed:
gamma C_a^2
+
C_a
+
beta C_b
+
delta C_d
+
gamma D_a
-
2gamma I
=
0

on every prime-silent source.

This is the dyadic prime reduction registered in the terminology file.

## 5. Dyadic relation at the compressed/ejected level

Let

B
=
Pi_epsilon C_a|_{V_epsilon},

F
=
(I-Pi_epsilon)C_a|_{V_epsilon}.

Using

C_a|_V=B+F,

one obtains

Pi_epsilon C_{2a}|_V
=
B^2
+
Pi_epsilon C_a F
-
2I
+
Pi_epsilon D_a|_V,

and

boxed:
F_{2a}
=
F B
+
(I-Pi_epsilon)C_a F
+
(I-Pi_epsilon)D_a|_V.

Therefore the log4 ejection already contains the next dynamic first-prime term

F B,

plus propagated ejection curvature and an explicit boundary-strip term.

Consequently a pure rank-counting argument cannot separate the log2 ejection from the log4 compensator.

The compensator has the correct dynamic depth to track the first-prime observable sequence.

## 6. Moment-spectrum version of the same resonance

For a whole-line symmetric translation, the ideal exponential-moment multiplier at spectral parameter z is

q_lambda(z)
=
e^(z lambda)+e^(-z lambda)
=
2 cosh(z lambda).

Hence

q_{2a}(z)
=
q_a(z)^2-2.

So the log4 ideal moment spectrum is polynomial in the log2 spectrum.

The boundary correction in Section 4 is exactly the compact-support defect of this polynomial identity.

Thus simple-spectrum separation between the log2 and log4 channels is impossible in principle.

Any moment argument must first eliminate the dyadic resonance and control the boundary correction.

## 7. Fiber decomposition of the symmetric first-prime shift

Now use only the four-delay support geometry.

In the chamber

log5 < L <= log6,

we have

2a<L<3a.

Set

w=L-2a,

so

0<w<a.

Decompose H by the residue coordinate

r in (0,a).

For

0<r<w,

the a-chain has three points

r,

r+a,

r+2a.

On this fiber C_a is the path-adjacency matrix

P_3
=
[0 1 0;
 1 0 1;
 0 1 0],

with eigenvalues

sqrt2,

0,

-sqrt2.

For

w<r<a,

the chain has two points

r,

r+a.

On this fiber C_a is

P_2
=
[0 1;
 1 0],

with eigenvalues

1,

-1.

Therefore

boxed:
spec(C_a)
=
{sqrt2,0,-sqrt2,1,-1}.

Every eigenfunction has one of five explicit fiber patterns.

## 8. Exclude the ±sqrt2 eigenpatterns

Suppose

C_a f=lambda f,

lambda in {sqrt2,-sqrt2}.

Then f is supported on the three-chain region and has the form

f(r)=phi(r),

f(r+a)=lambda phi(r),

f(r+2a)=phi(r),

for 0<r<w.

Consider the middle interval

M=(a,a+w).

For x in M:

- C_b f(x)=0 because x lies in the middle gap of the b-shift;
- C_d f(x)=0 because d>L/2 and M lies in its middle gap;
- C_{2a}f(x)=0 because neither x-2a nor x+2a lies in the support interval.

Thus prime silence reduces on M to

C_a f(x)=0.

But

C_a f=lambda f,

with lambda nonzero.

Hence

f=0

on M.

Since

f(r+a)=lambda phi(r),

this forces

phi=0,

hence f=0.

Therefore no nonzero ±sqrt2 eigenvector is prime-silent.

## 9. Exclude the ±1 eigenpatterns

Suppose

lambda in {1,-1}.

Then f is supported on the two-chain region:

f(r)=psi(r),

f(r+a)=lambda psi(r),

for

w<r<a.

On this support,

C_{2a}f=0.

Also

C_df=0,

because the support lies inside the middle gap of the d-shift.

Therefore prime silence becomes

lambda f
+
beta C_b f
=
0.

Thus

C_b f
=
-(lambda/beta)f.

But

L<2b,

so C_b is itself a two-point partial swap with spectrum

{-1,0,1}.

Since

beta>1,

the number

-lambda/beta

is not in that spectrum.

Therefore f=0.

So no nonzero ±1 eigenvector is prime-silent.

## 10. Exclude the zero eigenpattern

Suppose

C_a f=0.

Then on the three-chain region

0<r<w,

f has the form

f(r)=phi(r),

f(r+a)=0,

f(r+2a)=-phi(r).

Also

C_{2a}f=-f.

Set

s=d-2a=log(5/4),

q=2a-b=log(4/3),

k=q-s=log(16/15),

u=L-d,

so

w=s+u.

The chamber gives

0<u<q,

and

u<3k.

Evaluate the prime-silent equation on the left edge

0<x<w.

The b-shift contributes only for x>q and the d-shift only for x<u.

One obtains

boxed:
gamma phi(x)
+
beta 1_(x>q) phi(x-q)
+
delta 1_(x<u) phi(x+s)
=
0.

There is an immediate dead interval

u<x<min(q,w),

on which

phi(x)=0.

### Case A: w<=q

Then u<=k.

For 0<x<u,

the equation is

gamma phi(x)+delta phi(x+s)=0.

But

x+s in (s,w)

lies in the already-zero interval

(u,w),

because

s>u.

Hence phi(x)=0 for 0<x<u.

Together with the dead interval,

phi=0 on (0,w).

### Case B: w>q

Then u>k.

The dead interval is

(u,q).

Since

s>u,

the interval

(s,q)

is zero.

For

0<x<k=q-s,

the relation

gamma phi(x)+delta phi(x+s)=0

therefore gives

phi(x)=0.

Now let

0<t<u-k.

At x=t+k,

the d-relation gives

phi(q+t)
=
-(gamma/delta)phi(t+k).

At x=q+t,

the b-relation gives

phi(q+t)
=
-(beta/gamma)phi(t).

Hence

boxed:
phi(t+k)
=
(beta delta/gamma^2) phi(t).

Since

phi=0 on (0,k),

and

u<3k,

finite iteration gives

phi=0

on the whole interval

(0,u).

The dead interval already gives

phi=0 on

(u,q).

Finally, for

q<x<w,

the b-relation expresses

phi(x)

through

phi(x-q),

and

0<x-q<w-q=u-k<u.

Thus phi=0 there as well.

Therefore

phi=0

on all of (0,w).

So the zero eigenpattern is also excluded.

## 11. Ambient eigenvector exclusion theorem

Sections 8-10 prove:

boxed:
ker P_c
contains no nonzero eigenvector of C_a

through the four-delay chamber

log5 < L <= log6.

This statement is ambient: it does not use regular-kernel membership.

It is stronger than the parity repair originally sought.

## 12. Symmetric first-prime observability

Let

0 != V subset ker P_c

be finite dimensional.

Let

Pi

be orthogonal projection onto V,

B
=
Pi C_a|_V,

F
=
(I-Pi)C_a|_V,

and

d=dim V.

Claim:

boxed:
intersection_{m=0}^{d-1}
ker(F B^m)
=
{0}.

Proof.

Suppose f belongs to the intersection.

Cayley-Hamilton extends

F B^m f=0

to every m>=0.

The cyclic span

W_f
=
span{B^m f:m>=0}

lies in V subset ker P_c.

For every m,

C_a(B^m f)
=
B^(m+1)f.

Hence W_f is a nonzero finite-dimensional C_a-invariant subspace if f is nonzero.

Since C_a is self-adjoint, its restriction to W_f has an eigenvector.

That would give a nonzero C_a-eigenvector in ker P_c, contradicting Section 11.

Therefore f=0.

This is symmetric first-prime observability, registered in the terminology file.

## 13. Quantitative symmetric ejection floor

Finite dimensionality now gives a fixed-scale constant

nu_sym(V)>0

such that

boxed:
sum_{m=0}^{d-1}
||F B^m f||^2
>=
nu_sym(V)^2 ||f||^2

for all f in V.

Unlike the one-sided floor of series-49, this quantity is directly visible to the symmetric prime-silent equation.

Apply this in particular to

V=K_c^{ps}.

## 14. Reduced compensator identity

For

V=K_c^{ps},

prime silence gives

F
+
beta F_b
+
gamma F_{2a}
+
delta F_d
=
0.

Use the dyadic ejection identity:

F_{2a}
=
F B
+
Q C_a F
+
Q D_a|_V.

Therefore

boxed:
gamma F B
+
F
=
-
[
beta F_b
+
delta F_d
+
gamma Q C_a F
+
gamma Q D_a|_V
].

Apply this to

B^m f.

Then the dynamically observable sequence

F B^m f,

F B^(m+1)f

must be reproduced by only:

- the non-dyadic log3 ejection;
- the log5 ejection;
- propagated first-prime compression curvature;
- the explicit two-edge boundary projector.

This is the sharp compensator equation after all parity and dyadic self-resonance are removed.

## 15. Support-triangular route status

The nested boundary-strip widths do not by themselves prove separation.

Reasons:

1. the projected ejections are global source vectors;
2. their nonkernel screw fields come from nested boundary strips, but kernel-valued escape remains moment-visible and field-invisible;
3. the log4 channel is not independent; it exactly contains the next first-prime dynamic ejection plus curvature;
4. the explicit D_a boundary projector remains after dyadic elimination.

Therefore a simple support-ordering contradiction is not obtained in this pass.

## 16. Moment-separation route status

The moment route also requires the dyadic reduction first.

The ideal log4 multiplier is a polynomial in the log2 multiplier:

q_(2a)=q_a^2-2.

So simple-spectrum incompatibility between those two channels is unavailable.

The genuinely new spectral content is carried by the non-dyadic delays

b=log3

and

d=log5,

together with the boundary/curvature terms.

No theorem in this pass separates those terms from the dynamically observable first-prime ejection family.

## 17. Result

The ejection-compensator problem is now substantially sharper.

Negative:

- one-sided dynamic ejection observability is not directly visible to prime silence because opposite-parity ejection self-cancels within a prime pair;
- log4 is dynamically resonant with log2 and cannot be treated as an independent compensator;
- nested support and simple moment-spectrum ordering do not close the problem by themselves.

Positive:

- the symmetric first-prime shift has only five possible eigenvalues;
- every one of those eigenpatterns is excluded by the exact four-delay prime-silent equation;
- therefore the symmetrized first-prime ejection is dynamically observable on every finite-dimensional prime-silent branch;
- after exact dyadic elimination, only the log3/log5 channels, compression curvature, and an explicit boundary projector remain as genuine compensators.

This is the first finite-dimensional observability statement aligned exactly with the symmetric prime-silent operator.

## Fixed-L status

This pass does not yet prove

K_c^{ps}=0

through the full four-delay chamber.

The last load-bearing continuous prime-channel injectivity range remains

0<L<=log(16/3).

The canonical theorem cursor remains

SZ-CROSS-COLLAR-3.

## Next frontier

Next target:

SZ-KERNEL-EDGE-GERM-51 / NONDYADIC COMPENSATOR SEPARATION

The next pass should attack

gamma F B
+
F
=
-
[
beta F_b
+
delta F_d
+
gamma Q C_a F
+
gamma Q D_a
]

on

V=K_c^{ps}.

Priority:

1. split every term into K_c-perpendicular and regular-kernel escape blocks;
2. use the exact GERM-13 screw-field representation on the nonkernel pieces;
3. exploit the fact that b and d exceed L/2, so C_b and C_d are two-point partial swaps with spectrum {-1,0,1};
4. test whether the non-dyadic channels can reproduce the dynamically observable B-Krylov sequence;
5. alternatively, compress the reduced identity into a finite moment chart and use the algebraic independence of log3/log2 and log5/log2 after the dyadic polynomial has been removed.

A separation theorem here would prove prime-silent triviality in the full four-delay chamber.

No public promotion and no canonical cursor movement are asserted.
