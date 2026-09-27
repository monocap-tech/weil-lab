# SZ edge recurrence 56 — holonomy orbit recustody

Date: 2026-09-27
Branch: sz-cross-collar
Status: UNRATIFIED RESIDUE / NF PASS
Canonical parent: SZ-CROSS-COLLAR-3
Immediate residue: series-55
Public promotion: forbidden

## Objective

Repair the custody defect in the six-step holonomy orbit from series-54/55.

The problem was:

Hhol D^m f

is strongly observable on the ambient prime-silent space, but for m>0 the source D^m f need not lie in the regular kernel K_c.

Therefore one could not legally insert the higher holonomy channels into the movable-center or denominator-clearing equations derived from G_c u=0.

This pass gives an exact finite recustody.

Every D^m f is split into:

- a projected component A_m f that lies back in V=K_c^{ps};
- a finite ejection-word component R_m f carrying at least one exit from V.

The recustody errors are then routed through the two-stage regular-kernel escape detector into K_c^perp.

The result is a quantitative combined observation consisting of:

- six holonomy channels with genuine prime-silent regular-kernel custody;
- fifteen nonkernel ejection channels.

No ambient D^m source is treated as a kernel vector.

This removes the principal logical obstacle identified in series-55.

No fixed-L injectivity extension is claimed.

## 1. Setup

Let

V=K_c^{ps}

inside the four-delay chamber.

Let

Pi=Pi_V,

Q=I-Pi.

Use the dyadic block

D=C_(log2)+gamma C_(log4)

and the transport holonomy

Hhol=[D,N].

Series-54 proves the ambient six-step lower bound

boxed:
(
sum_(m=0)^5
||Hhol D^m f||^2
)^(1/2)
>=
c_hol ||f||

for every

f in ker P_c,

hence in particular for f in V.

## 2. Block decomposition of D

Relative to the orthogonal decomposition

L2(0,L)
=
V direct_sum V^perp,

write

D
=
[ B  C
  F  E ],

where

B
=
Pi D Pi|_V,

C
=
Pi D Q|_(V^perp),

F
=
Q D Pi|_V,

E
=
Q D Q|_(V^perp).

Thus

D|_V=B+F

at one step.

But higher powers may leave V and later return through C, so one must not replace D^m|_V by B^m.

## 3. Exact projected orbit

For m>=0 define

A_m
=
Pi D^m|_V,

R_m
=
Q D^m|_V.

Then

boxed:
D^m|_V
=
A_m+R_m,

with

Ran(A_m) subset V,

Ran(R_m) subset V^perp.

The initial values are

A_0=I_V,

R_0=0.

Multiplying by D gives the exact recursion

boxed:
A_(m+1)
=
B A_m
+
C R_m,

boxed:
R_(m+1)
=
F A_m
+
E R_m.

Hence

boxed:
R_m
=
sum_(j=0)^(m-1)
E^(m-1-j) F A_j

for every m>=1.

Therefore every loss-of-custody term contains at least one explicit ejection F.

There are no hidden ambient terms.

This is the holonomy orbit recustody registered in the terminology file.

## 4. Finite ejection-word space

Only

m=0,...,5

occur in the holonomy theorem.

Therefore all recustody errors lie in the finite-dimensional space

W_rec
=
sum_{m=1}^5 Ran(R_m)

=
sum_{m=1}^5
sum_{j=0}^{m-1}
Ran(
E^(m-1-j) F A_j
).

Since V is finite dimensional and only finitely many bounded operators occur,

W_rec

is finite dimensional.

So the recustody does not recreate the infinite irrational orbit.

The infinite ambient orbit has been replaced by finitely many exact ejection words of bounded length.

## 5. Recustodied holonomy decomposition

For f in V,

Hhol D^m f
=
Hhol A_m f
+
Hhol R_m f.

Define the kernel-custodied holonomy observation

O_cus f
=
(
Hhol A_0 f,
...,
Hhol A_5 f
).

Every source vector

A_m f

lies in

V=K_c^{ps} subset K_c.

Therefore every one of these six channels may legally use:

- the first-kind kernel equation;
- movable-center identities;
- denominator-clearing ladders;
- prime/ratio germ filtrations;
- the ratified singular-site geometry.

This is the principal custody gain of the pass.

## 6. Exact edge ratio formula for every custodied channel

Series-55 gives, for any source g and

0<s<u=L-log5,

the exact holonomy edge formula

(Hhol g)(s)
=
-beta g(r_32+s)
-delta g(r_52+s)
+gamma beta g(r_43+s)
-gamma delta g(r_54+s),

where

r_32=log(3/2),

r_52=log(5/2),

r_43=log(4/3),

r_54=log(5/4).

Apply this with

g=A_m f in V.

Then for every m=0,...,5,

boxed:
(Hhol A_m f)(s)
=
-beta (A_m f)(r_32+s)
-delta (A_m f)(r_52+s)
+gamma beta (A_m f)(r_43+s)
-gamma delta (A_m f)(r_54+s),

0<s<u.

These are now genuine ratio-incidence observations of regular prime-silent kernel vectors.

Unlike the ambient channels Hhol D^m f, all six are legally eligible for the GERM-21/22/23 arithmetic machinery.

## 7. Split the recustody error by K_c

Let

Pi_K

be the orthogonal projection onto the full regular kernel K=K_c, and

Q_K=I-Pi_K.

For

m=1,...,5,

split

R_m
=
H_m+N_m,

where

H_m
=
Pi_K R_m
in K,

N_m
=
Q_K R_m
in K^perp.

The two pieces are orthogonal.

## 8. Route the K-valued error into K^perp

Let

T=S_(log2)^+.

Series-52 proves that on K,

J_K g
=
(
Q_K T g,
Q_K T^2 g
)

is injective, with

boxed:
||Q_K T g||^2
+
||Q_K T^2 g||^2
>=
nu_K^2 ||g||^2

for some

nu_K>0.

Define

mu_K=min(1,nu_K).

For each m=1,...,5 define three nonkernel error channels:

N_m,

Q_K T H_m,

Q_K T^2 H_m.

All lie in K^perp.

The resulting fifteen-channel observation is

O_ej f
=
(
N_m,
Q_K T H_m,
Q_K T^2 H_m
)_(m=1,...,5).

Then

boxed:
||O_ej f||^2
>=
mu_K^2
sum_(m=1)^5
||R_m f||^2.

Equivalently,

boxed:
(
sum_(m=1)^5
||R_m f||^2
)^(1/2)
<=
mu_K^(-1)
||O_ej f||.

## 9. Quantitative combined recustody detector

Let

Rbullet(f)
=
(R_0f,...,R_5f),

with R_0=0.

The six-step ambient holonomy floor gives

c_hol ||f||
<=
||
(
Hhol D^m f
)_(m=0)^5
||.

By the recustody decomposition and the triangle inequality in the direct-sum target,

<=
||O_cus f||
+
||
(
Hhol R_m f
)_(m=0)^5
||.

Since Hhol is bounded,

<=
||O_cus f||
+
||Hhol||
||
Rbullet(f)
||.

Section 8 gives

<=
||O_cus f||
+
(
||Hhol||/mu_K
)
||O_ej f||.

Set

q
=
||Hhol||/mu_K.

Then Cauchy-Schwarz gives

||O_cus f||
+
q ||O_ej f||

<=
sqrt(1+q^2)
sqrt(
||O_cus f||^2
+
||O_ej f||^2
).

Therefore

boxed:
sqrt(
||O_cus f||^2
+
||O_ej f||^2
)
>=
c_rec ||f||,

where

boxed:
c_rec
=
c_hol
/
sqrt(
1+
(||Hhol||/mu_K)^2
)
>
0.

This is the recustodied holonomy detector registered in the terminology file.

## 10. Exact channel count

The combined observation has:

- six kernel-custodied holonomy channels
  Hhol A_m, m=0,...,5;

- five primary nonkernel recustody channels
  N_m;

- five first-secondary channels
  Q_K T H_m;

- five second-secondary channels
  Q_K T^2 H_m.

Thus there are

boxed:
21

channels in total.

The number 21 appears again, but the architecture is different from series-52:

series-52 recustodied the seven-step projection-ejection detector;

series-56 recustodies the six-step ambient transport-holonomy detector.

## 11. Dichotomy form

The combined estimate may be read as a quantitative dichotomy.

For every nonzero f in V, at least one of the following occurs.

### Branch K — kernel-custodied holonomy

The six genuine kernel channels satisfy

||O_cus f||
>=
(c_rec/sqrt2) ||f||.

Then a positive fraction of the detector is carried by ratio-cell holonomy of actual vectors

A_m f in K_c^{ps}.

All kernel-specific arithmetic and movable-center equations are available.

### Branch NK — nonkernel recustody

The fifteen K^perp channels satisfy

||O_ej f||
>=
(c_rec/sqrt2) ||f||.

Then the detector is already in the finite-dimensional nonkernel regime.

Applying G_c to their finite-dimensional range gives a fixed-scale H1 field floor, and the arithmetic field-return theorem of series-53 produces a shrinking local interior-field detector.

Thus every direction is assigned to a mathematically legal custody branch.

## 12. Finite-dimensional nonkernel field return

Let

W_ej,NK

be the sum of the ranges of the fifteen nonkernel recustody channels.

Then

W_ej,NK subset K_c^perp

and is finite dimensional.

Hence

G_c|_(W_ej,NK)

is injective.

As in series-53, there are finitely many reachable arithmetic centers

x_1,...,x_M

and constants

epsilon_0>0,

c_ej>0

such that

boxed:
sum_i sum_j
||
G_c L_i^ej f
||^2_
{L2((x_j-epsilon,x_j+epsilon) intersect (-c,c))}
>=
c_ej epsilon ||f||^2

on the Branch-NK subspace, after replacing c_ej by the corresponding branch floor.

Thus the ejection-containing part of the ambient D-orbit is fully routed to a quantitative shrinking H1-field observation.

## 13. Custodied branch and denominator clearing

On Branch K, every relevant source

g_m=A_m f

belongs to K_c^{ps}.

The four ratio locations in the edge holonomy row satisfy the one-step arithmetic identities

r_32+a=b,

r_52+a=d,

r_43+b=2a,

r_54+2a=d.

Therefore the denominator-clearing ladders from GERM-23 are legal for every one of the six g_m.

This removes the specific custody objection of series-55.

However it does not automatically produce an edge contradiction.

Every selected movable-center equation introduces its logarithmic archimedean diagonal channel.

The earlier GERM-23 through GERM-26 no-go results therefore remain relevant.

The recustody theorem permits those equations to be used correctly; it does not make the diagonal channel disappear.

## 14. Recustodied holonomy boundary filtration

One may now form the canonical boundary filtration using only the six legal kernel-custodied channels

Hhol A_m f.

Because the maps A_m:V->V are finite dimensional, the joint filtration at the holonomy atlas Xi_L again stabilizes.

Outside the terminal subspace, one obtains a finite-order ratio/prime/edge germ of an actual kernel vector.

On the terminal subspace, all six custodied holonomy boundary germs are superflat.

The combined detector then forces either:

- positive interior holonomy mass in the kernel-custodied channels;
- or quantitative nonkernel field return through O_ej.

Thus the former single ambient interior-core obstruction has split into two typed hard branches.

## 15. What recustody resolves

This pass resolves the load-bearing logical issue from series-55:

boxed:
no ratio germ of an ambient D^m f
needs to be treated as if D^m f were a kernel vector.

Every six-step holonomy channel is replaced by:

1. a holonomy channel generated by an actual g_m in K_c^{ps};
2. finitely many ejection terms that are explicitly routed toward K_c^perp.

So all subsequent use of:

- denominator clearing;
- movable centers;
- singular-germ localization;
- or kernel-specific first-kind equations

can be restricted to genuine kernel-custodied sources.

## 16. What remains missing

The recustody does not yet prove

V=0.

On the kernel-custodied branch, the ratio sites are now legally connected to prime hinges, but the movable-center equations reintroduce the log-diagonal archimedean carrier.

On the nonkernel branch, shrinking interior H1-field detection is quantitative, but transport to the physical edge or Sigma_c still requires the finite edge Runge/local-range gate.

Thus the two surviving interfaces are:

boxed:
kernel-custodied ratio germ
->
log-diagonal rigidity,

and

boxed:
nonkernel H1 field
->
finite edge Runge / edge transport.

These are precisely the two local species already isolated earlier in the project.

The present pass proves that there is no third hidden ambient-custody obstruction between them.

## 17. Fixed-L status

No extension of

K_c^{ps}=0

is claimed.

The last load-bearing continuous prime-channel injectivity range remains

0<L<=log(16/3).

The canonical theorem cursor remains

SZ-CROSS-COLLAR-3.

## Next frontier

Next target:

SZ-KERNEL-EDGE-GERM-57 / RECUSTODIED RATIO-TO-DIAGONAL RETURN

The next pass should focus on Branch K.

Priority:

1. apply the one-step denominator-clearing equations to the four ratio germs of each g_m=A_m f;

2. assemble the resulting finite family of movable-center diagonal channels across m=0,...,5;

3. use the quantitative Branch-K holonomy floor to test whether those diagonal channels can all lie in the previously identified superflat log-diagonal hard subspace;

4. determine whether the six recustodied sources supply enough cross-relations to improve on the one-source GERM-23 through GERM-26 no-go;

5. if not, state the exact finite-dimensional multi-source log-diagonal rigidity theorem still missing.

A positive cross-source diagonal theorem would close the kernel-custodied branch.

The nonkernel branch remains assigned to the finite edge Runge interface.

No public promotion and no canonical cursor movement are asserted.
