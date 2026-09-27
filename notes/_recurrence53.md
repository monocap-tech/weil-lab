# SZ edge recurrence 53 — nonkernel field return to shrinking arithmetic neighborhoods

Date: 2026-09-27
Branch: sz-cross-collar
Status: UNRATIFIED RESIDUE / NF PASS
Canonical parent: SZ-CROSS-COLLAR-3
Immediate residue: series-52
Public promotion: forbidden

## Objective

Start from the 21-channel nonkernel escape detector of series-52 and determine whether its fixed-scale field floor can be returned to a genuinely shrinking observation.

The answer is positive, but only at finitely many interior arithmetic centers.

The finite-dimensional nonkernel field family admits finitely many point evaluations at reachable arithmetic centers that separate it. Because the fields lie in H^1, those point evaluations upgrade to a uniform local L2 lower bound on neighborhoods of radius epsilon.

Consequently a nonzero prime-silent regular-kernel branch cannot make all 21 escape fields superflat at every reachable arithmetic center.

This crosses the fixed-scale-to-shrinking-scale barrier for the auxiliary nonkernel fields.

It does not yet cross the remaining geometric barrier from those interior arithmetic centers to the physical edge or to the canonical singular-site set Sigma_c.

No fixed-L prime-silent triviality theorem is claimed.

## 1. Input from series-52

Let

V=K_c^{ps}.

Series-52 constructs 21 linear maps

L_i:V -> K_c^perp,

i=1,...,21,

with

boxed:
sum_i ||L_i f||_2^2
>=
c_0^2 ||f||_2^2,

where

c_0
=
nu_* min(1,nu_K)
>
0.

Let

W_NK
=
sum_i Ran(L_i)
subset
K_c^perp.

This is finite dimensional.

Series-52 also gives a finite-dimensional screw-field floor.

Because

K_c=ker G_c,

the restriction

G_c|_(W_NK)

is injective.

Hence there is

tau_NK>0

such that

boxed:
||G_c w||_2
>=
tau_NK ||w||_2

for every w in W_NK.

## 2. The field family

Define

Y
=
G_c(W_NK).

Then

Y

is finite dimensional and

Y subset H^1(-c,c).

Use the continuous representative of each H^1 field.

The map

G_c:W_NK -> Y

is an isomorphism onto its image.

The previous fixed-scale lower bound becomes

boxed:
sum_i
||G_c L_i f||_2^2
>=
tau_NK^2 c_0^2 ||f||_2^2.

The problem is now to replace the global L2 norm of these fields by shrinking local norms.

## 3. Reachable arithmetic centers

GERM-23 defines the arithmetic center lattice

Gamma_c
=
sum_{p: log p<L}
Z log p.

In the four-delay chamber the prime bases 2 and 3 are active.

Therefore

Gamma_c

is dense in R.

In right-oriented source coordinates,

Gamma_c intersect (0,L)

is dense in (0,L).

Transport these source centers to physical coordinates by

x=c-h.

Thus the physical reachable-center set

A_c
=
{
c-h:
h in Gamma_c intersect (0,L)
}

is dense in (-c,c).

## 4. Joint point-evaluation injectivity

For

x in A_c,

let

ev_x:Y->C

be point evaluation.

The full family

{ev_x}_{x in A_c}

is jointly injective on Y.

Indeed, if

y in Y

vanishes at every x in A_c, then continuity and density imply

y=0

on (-c,c).

Therefore y=0 in H^1.

Since Y is finite dimensional, finitely many evaluations already separate it.

Hence there exist distinct reachable arithmetic centers

x_1,...,x_M in A_c,

with

M<=dim Y,

such that

boxed:
E_arith:Y->C^M,

E_arith(y)
=
(
y(x_1),...,y(x_M)
)

is injective.

This is the point-evaluation form of the arithmetic field-return detector registered in the terminology file.

## 5. Fixed point-evaluation floor

Because Y is finite dimensional and E_arith is injective, there exists

alpha_Y>0

such that

boxed:
sum_(j=1)^M
|y(x_j)|^2
>=
alpha_Y^2 ||y||_2^2

for every y in Y.

Also, finite-dimensional norm equivalence gives a constant

C_Y>0

such that

boxed:
||y||_(H^1)
<=
C_Y ||y||_2

for every y in Y.

Thus the point detector is quantitatively stable in the L2 field norm.

## 6. Uniform continuity on the finite field family

For y in H^1(-c,c),

|y(x)-y(x_j)|
<=
||y'||_2 |x-x_j|^(1/2).

Hence on Y,

|y(x)-y(x_j)|
<=
C_Y |x-x_j|^(1/2) ||y||_2.

From Section 5, for every nonzero y there exists at least one j such that

|y(x_j)|
>=
alpha_Y/sqrt(M) ||y||_2.

Choose

epsilon_0>0

small enough that:

1. every interval
   (x_j-epsilon_0,x_j+epsilon_0)
   lies inside (-c,c);

2.
   C_Y sqrt(epsilon_0)
   <=
   alpha_Y/(2 sqrt(M)).

Then for the index j selected above and every

|x-x_j|<epsilon_0,

one has

|y(x)|
>=
alpha_Y/(2 sqrt(M)) ||y||_2.

Therefore, for every

0<epsilon<epsilon_0,

boxed:
sum_(j=1)^M
||y||^2_(L2(x_j-epsilon,x_j+epsilon))
>=
c_Y epsilon ||y||_2^2,

where one may take

c_Y
=
alpha_Y^2/(2M)

after a harmless outward adjustment of constants.

Thus the finite point detector automatically yields a shrinking local L2 detector with the expected first-order measure factor epsilon.

## 7. Compose with the 21 escape channels

Apply Section 6 to

y_i
=
G_c L_i f
in Y.

Sum over

i=1,...,21.

Then

sum_i sum_j
||G_c L_i f||^2_(L2(x_j-epsilon,x_j+epsilon))

>=

c_Y epsilon
sum_i
||G_c L_i f||_2^2.

Use the fixed-scale field floor from Section 2.

This gives

boxed:
sum_(i=1)^21 sum_(j=1)^M
||G_c L_i f||^2_(L2(x_j-epsilon,x_j+epsilon))
>=
c_ret epsilon ||f||_2^2

for every

f in V

and every

0<epsilon<epsilon_0,

with

boxed:
c_ret
=
c_Y tau_NK^2 c_0^2
>
0.

Equivalently,

boxed:
(
sum_(i,j)
||G_c L_i f||^2_(local)
)^(1/2)
>=
sqrt(c_ret) epsilon^(1/2) ||f||_2.

This is a genuine shrinking-scale power-law estimate.

## 8. What superflatness is now impossible

Suppose

0!=f in V.

Then it is impossible that every one of the 21 escape fields satisfy

||G_c L_i f||_(L2(x_j-epsilon,x_j+epsilon))
=
o(epsilon^N)

for every

i,j,N.

Indeed the sum of their squared local norms is bounded below by

c_ret epsilon ||f||^2.

Thus at least one field/center pair has local mass at finite algebraic order.

In fact the aggregate detector has exactly the natural H^1-continuous scaling

epsilon^(1/2)

in norm.

So the generic smooth-flat/Stieltjes countermodels do not survive simultaneously at all selected arithmetic field centers.

## 9. Primary-channel double custody

For the seven primary channels, set

g_m=B^m f in V.

Recall

D
=
C_(log2)+gamma C_(log4),

N
=
beta C_(log3)+delta C_(log5).

Prime silence gives

D g_m
=
-N g_m.

The primary nonkernel escape is

M_m
=
Q_K D g_m.

Therefore

M_m
=
-Q_K N g_m.

Since

G_c Pi_K=0,

the associated nonkernel field has the exact two descriptions

boxed:
G_c M_m
=
G_c D g_m
=
-G_c N g_m.

Hence each primary field is simultaneously:

- a dyadic log2/log4 boundary-strip field;
- a nondyadic log3/log5 edge field.

This is stronger custody than the generic secondary channels possess.

It is the natural interface for transporting the arithmetic-center detector back toward the original prime-silent source.

## 10. Secondary-channel custody

The secondary channels are

Q_K T H_m,

Q_K T^2 H_m,

where

H_m in K_c

and

T=S_(log2)^+.

GERM-13 gives their exact one-sided boundary-strip interpretations:

- Q_K T H_m is carried by the discarded log2 strip of H_m;
- Q_K T^2 H_m is carried by the discarded log4 strip of H_m.

Thus every local field appearing in Section 7 remains a concrete fixed-width boundary-strip field of a kernel vector.

No abstract nonkernel component remains.

## 11. Why this does not yet reach Sigma_c

The ratified singular-site set

Sigma_c

is finite.

The arithmetic field-return centers

{x_1,...,x_M}

were extracted from a dense set because density guarantees joint evaluation injectivity on the continuous field family Y.

Finite dimensionality alone does not imply that evaluation on a prescribed finite set is injective.

In particular, one can have a nonzero finite-dimensional subspace of continuous functions all vanishing on every point of a prescribed finite set.

Therefore the present argument does not justify replacing

{x_j}

by

Sigma_c.

No claim of singular-site localization is made.

## 12. Why this does not yet reach the physical edge

For the same reason, nothing yet proves that restriction of Y to every sufficiently small physical edge neighborhood is injective.

A nonzero finite-dimensional continuous field family may vanish identically on one fixed edge neighborhood while remaining nonzero in the interior.

Therefore the estimate of Section 7 is not a collar estimate.

The selected centers may lie anywhere in the old interior.

This is the remaining geometric return problem.

## 13. Relation to GERM-23

GERM-23 proved:

finite-dimensional source obstruction
=>
finitely many reachable arithmetic centers detect the source,

but its exact centered equations reintroduced uncontrolled diagonal carriers.

The present pass obtains a stronger statement for the nonkernel field family:

- the fields are H^1 and continuous;
- point evaluations are legitimate;
- finite arithmetic-center detection upgrades automatically to a power-law shrinking local estimate.

Thus the old finite-center detection mechanism becomes quantitative after the spectral escape has moved the problem into a finite-dimensional H^1 field family.

What remains is not rate control.

What remains is geometric transport of those interior field detections back to the canonical edge/singular-site observations.

## 14. Fixed-L status

This pass does not prove

K_c^{ps}=0

through the full four-delay chamber.

The last load-bearing continuous prime-channel injectivity range remains

0<L<=log(16/3).

The canonical theorem cursor remains

SZ-CROSS-COLLAR-3.

## Next frontier

Next target:

SZ-KERNEL-EDGE-GERM-54 / ARITHMETIC FIELD-TO-EDGE TRANSPORT

The next pass should start from the shrinking interior estimate

sum_(i,j)
||G_c L_i f||^2_(L2(x_j-epsilon,x_j+epsilon))
>=
c_ret epsilon ||f||^2

at finitely many reachable arithmetic centers.

Priority:

1. use the primary double-custody identity
   G_c D g_m=-G_c N g_m
   to express each selected arithmetic-center field value in both dyadic and nondyadic boundary-strip coordinates;

2. determine whether arithmetic recentering can move the finite detector to:
   - the physical edge,
   - the ratified singular set Sigma_c,
   - or a finite visible-germ family;

3. exploit continuity/H^1 regularity of the field side to avoid the source-side diagonal-carrier failure from GERM-23;

4. if transport still regenerates uncontrolled source diagonal carriers, isolate that failure as the terminal distinction between interior-field coercivity and canonical collar coercivity.

A positive transport theorem would give the first finite-order shrinking observation tied directly to the original canonical edge package.

No public promotion and no canonical cursor movement are asserted.
