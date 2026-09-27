# SZ edge recurrence 57 — spectral-shadow decomposition and collapse of the diagonal branch

Date: 2026-09-27
Branch: sz-cross-collar
Status: UNRATIFIED RESIDUE / NF PASS
Canonical parent: SZ-CROSS-COLLAR-3
Immediate residue: series-56
Public promotion: forbidden

## Objective

Test whether the six recustodied kernel sources

A_m f
=
Pi_V D^m f,
m=0,...,5,

supply enough cross-source structure to beat the one-source full-Suzuki log-diagonal no-go of GERM-23 through GERM-26.

There are two answers.

First, source multiplicity by itself does not restore local archimedean quasi-analyticity. The six projected dyadic sources reduce to five positive spectral shadows, and the exact full-Suzuki local flat-profile space has arbitrarily large finite dimension.

Second, the same spectral-shadow decomposition produces a stronger ejection theorem: every nonzero dyadic spectral component of a prime-silent source must leave V=K_c^{ps}. The five spectral-shadow ejections are jointly injective.

After the usual two-stage regular-kernel escape, this yields a fifteen-channel K_c^perp detector for the whole prime-silent regular-kernel branch.

Therefore the kernel-custodied log-diagonal branch no longer needs to be closed in order to continue the fixed-L prime-silent route.

No fixed-L injectivity theorem is claimed yet.

## 1. Dyadic finite spectrum

Recall the dyadic block

D
=
C_(log2)
+
gamma C_(log4),

with

gamma=1/sqrt2.

Series-51 proves

spec(D)
=
Lambda_D,

where

Lambda_D
=
{
1,
-1,
-1/sqrt2,
(1+sqrt17)/(2sqrt2),
(1-sqrt17)/(2sqrt2)
}.

The annihilating polynomial is

p_D(z)
=
(z^2-1)
(z+gamma)
(z^2-gamma z-2).

Equivalently,

p_D(z)
=
z^5
-
(7/2)z^3
-
sqrt2 z^2
+
(5/2)z
+
sqrt2.

All five roots are distinct.

## 2. Ambient spectral projections

Let

P_lambda

be the orthogonal spectral projection of D corresponding to

lambda in Lambda_D.

Then

boxed:
D
=
sum_lambda
lambda P_lambda,

and

boxed:
sum_lambda P_lambda=I.

Each P_lambda is a polynomial in D of degree at most four:

P_lambda
=
product_(mu != lambda)
(D-mu I)/(lambda-mu).

Thus every spectral projection belongs to the finite dyadic operator algebra already present in the recustody construction.

## 3. Project the spectral pieces back to V

Let

V=K_c^{ps}

and let

Pi=Pi_V.

Define the dyadic spectral shadows

boxed:
S_lambda
=
Pi P_lambda|_V.

Because P_lambda is an orthogonal projection,

S_lambda

is self-adjoint and positive semidefinite on V.

Indeed,

<f,S_lambda f>
=
<f,P_lambda f>
=
||P_lambda f||^2
>=0.

Also,

boxed:
sum_lambda S_lambda=I_V.

So the five S_lambda form a positive operator-valued resolution of the identity on the prime-silent regular-kernel branch.

## 4. The projected dyadic orbit is a moment sequence of the shadows

For

A_m
=
Pi D^m|_V,

the spectral theorem gives

boxed:
A_m
=
sum_lambda
lambda^m S_lambda.

Therefore the first five projected orbit operators

A_0,...,A_4

are related to the five shadows by the Vandermonde matrix

(lambda^m)_(m=0,...,4).

Because the five lambda are distinct, the Vandermonde matrix is invertible.

Hence:

boxed:
{A_0,...,A_4}
and
{S_lambda}
contain exactly the same linear information.

The sixth recustodied source adds no independent shadow.

Indeed

p_D(D)=0

gives for every m>=0

boxed:
A_(m+5)
-
(7/2)A_(m+3)
-
sqrt2 A_(m+2)
+
(5/2)A_(m+1)
+
sqrt2 A_m
=
0.

Thus the entire projected dyadic orbit is a five-mode spectral-shadow sequence.

## 5. Diagonal superflatness in shadow coordinates

Let

W_diag
subset V

be any finite-center all-orders-superflat diagonal branch, for example the stabilized hard branch produced by the GERM-24 selected movable-center Suzuki diagonal observations.

For f in V, the following are equivalent:

1.
A_m f in W_diag
for
m=0,...,4;

2.
S_lambda f in W_diag
for every
lambda in Lambda_D.

This follows immediately by Vandermonde inversion.

Define

boxed:
W_sh
=
{
f in V:
S_lambda f in W_diag
for every lambda
}.

This is the spectral-shadow diagonal hard core registered in the terminology file.

Because the A_m satisfy the exact p_D recurrence,

f in W_sh

implies

boxed:
A_m f in W_diag
for every m>=0.

So the six-source diagonal problem reduces exactly to five spectral shadows.

## 6. Full-Suzuki local flatness has arbitrary finite multiplicity

GERM-26 constructed a nonzero local source with superflat exact full-Suzuki centered diagonal field.

The construction in fact has arbitrarily large finite multiplicity.

Use the inverse-Mellin family

M_j(sigma)
=
sigma^j
sin(pi sigma)
e^(sigma^2),

j=0,1,2,...

and let

mu_j

be the inverse Mellin transforms used in GERM-20/26.

Every mu_j is:

- smooth;
- flat at zero;
- rapidly decreasing at infinity;
- polynomial-momentless:
  integral y^k mu_j(y)dy=0 for every k>=0.

The functions mu_j are linearly independent because their Mellin transforms are linearly independent.

After shifting to the exact lower Stieltjes endpoint t_rho and mapping back to the local source coordinate, every finite linear combination has all polynomial Stieltjes moments zero.

The only additional condition needed in GERM-26 is the one scalar functional

A_+(b)=0.

Take any finite span

M_R
=
span{
mu_0,...,mu_R
}.

It has dimension R+1.

The A_+ condition is one linear functional, so its kernel inside M_R has dimension at least R.

Mapping that kernel back to the local source interval gives an R-dimensional space

boxed:
U_R

of nonzero local source profiles such that every

b in U_R

has:

- source mass flat at the diagonal endpoint;
- exact one-sided full-Suzuki transform flat to every order;
- exact even centered full-Suzuki field flat to every order.

Since R is arbitrary,

boxed:
the exact local full-Suzuki flat-profile space has arbitrarily large finite dimension.

## 7. Consequence for the five-shadow experiment

The five-shadow structure therefore does not, by source multiplicity alone, restore local diagonal rigidity.

At one selected center, five linearly independent local source profiles can simultaneously lie in the exact full-Suzuki superflat class.

So an argument of the form

five recustodied sources
+
same local archimedean diagonal
=>
one source has finite order

is false at the local-model level.

This does not construct an actual nonzero vector in W_sh.

It proves only that the finite shadow count and Vandermonde relation do not cross the local quasi-analyticity barrier.

Any positive multi-source theorem would still have to use global prime/kernel coupling.

## 8. Spectral-shadow ejections

Define

boxed:
J_lambda
=
(I-Pi)P_lambda|_V.

Then

P_lambda|_V
=
S_lambda+J_lambda,

with orthogonal V and V^perp components.

This is the spectral-shadow ejection detector registered in the terminology file.

## 9. Exact kernel equality

Claim:

boxed:
ker J_lambda
=
ker(P_lambda|_V)
=
ker S_lambda.

First,

P_lambda f=0

obviously implies

J_lambda f=0

and

S_lambda f=0.

Also,

S_lambda f=0

implies

0
=
<f,S_lambda f>
=
||P_lambda f||^2,

so

P_lambda f=0.

It remains to prove that

J_lambda f=0

forces

P_lambda f=0.

If

J_lambda f=0,

then

P_lambda f
=
S_lambda f
belongs to V.

But

D P_lambda f
=
lambda P_lambda f.

Thus any nonzero P_lambda f would be a nonzero D-eigenvector lying in

V subset ker P_c.

Series-51 proves that the ambient four-delay prime-silent space contains no nonzero D-eigenvector.

Therefore

P_lambda f=0.

This proves the claim.

## 10. Joint spectral-shadow ejection is injective

Define

J_sh:
V
->
direct_sum_(lambda in Lambda_D)
V^perp

by

J_sh f
=
(
J_lambda f
)_lambda.

If

J_sh f=0,

then

P_lambda f=0

for every lambda by Section 9.

Since the spectral projections sum to the identity,

f
=
sum_lambda P_lambda f
=
0.

Hence

boxed:
J_sh
is injective on V.

Because V is finite dimensional, there exists

boxed:
nu_sh(V)>0

such that

boxed:
sum_lambda
||J_lambda f||^2
>=
nu_sh(V)^2 ||f||^2

for every f in V.

The constant may depend on the particular regular kernel branch V.

No chamber-uniform lower bound is asserted.

## 11. The shadow ejections are already recustodied finite words

Each spectral projection P_lambda is a polynomial in D of degree at most four.

Therefore

J_lambda
=
Q P_lambda|_V

is a fixed linear combination of

R_0,...,R_4,

where

R_m
=
Q D^m|_V

are the exact recustody errors from series-56.

Since R_0=0,

boxed:
Ran(J_lambda)
subset
W_rec,

the finite recustody-error space.

Thus the spectral-shadow detector introduces no new infinite ambient orbit.

It is a finite recombination of already-typed ejection words.

## 12. Split every shadow ejection by the full regular kernel

Let

K=K_c,

Pi_K

be the orthogonal projection onto K, and

Q_K=I-Pi_K.

For each lambda write

J_lambda
=
H_lambda+N_lambda,

where

H_lambda
=
(Pi_K-Pi)P_lambda|_V

lies in

K intersect V^perp,

and

N_lambda
=
Q_K P_lambda|_V

lies in

K^perp.

The two parts are orthogonal.

Therefore

||J_lambda f||^2
=
||H_lambda f||^2
+
||N_lambda f||^2.

## 13. Route every regular-kernel shadow escape into K^perp

Let

T=S_(log2)^+.

Series-52 gives the two-stage full-kernel estimate

||Q_K T g||^2
+
||Q_K T^2 g||^2
>=
nu_K^2 ||g||^2

for

g in K.

Set

mu_K=min(1,nu_K).

Apply this to

g=H_lambda f.

For every lambda define three K^perp outputs:

N_lambda f,

Q_K T H_lambda f,

Q_K T^2 H_lambda f.

There are five dyadic eigenvalues, hence exactly fifteen outputs.

Their total squared norm satisfies

boxed:
sum_lambda
[
||N_lambda f||^2
+
||Q_K T H_lambda f||^2
+
||Q_K T^2 H_lambda f||^2
]
>=
mu_K^2
sum_lambda
||J_lambda f||^2.

Using Section 10,

boxed:
sum_(15 channels)
||L_i^sh f||^2
>=
mu_K^2 nu_sh(V)^2 ||f||^2.

Therefore the fifteen-channel spectral-shadow escape detector lands entirely in

K_c^perp

and is injective on all of V.

## 14. Finite-dimensional field floor

Let

W_sh,NK

be the sum of the ranges of the fifteen K_c^perp channels.

This space is finite dimensional.

Because

K_c=ker G_c,

the restriction

G_c|_(W_sh,NK)

is injective.

Hence there exists

tau_sh>0

such that

||G_c w||
>=
tau_sh ||w||

for

w in W_sh,NK.

Consequently

boxed:
sum_i
||G_c L_i^sh f||^2
>=
tau_sh^2
mu_K^2
nu_sh(V)^2
||f||^2.

So every nonzero prime-silent regular-kernel vector is detected by a finite family of nonkernel screw fields generated directly from its dyadic spectral components.

## 15. Shrinking arithmetic-field return

The field family

G_c(W_sh,NK)

is finite dimensional and lies in H1(-c,c).

Therefore the arithmetic field-return theorem of series-53 applies.

There exist finitely many reachable arithmetic centers

x_1,...,x_M,

epsilon_0>0,

and

c_sh>0

such that for every

0<epsilon<epsilon_0,

boxed:
sum_i sum_j
||
G_c L_i^sh f
||^2_
{L2((x_j-epsilon,x_j+epsilon) intersect (-c,c))}
>=
c_sh epsilon ||f||^2.

Thus the entire regular prime-silent branch has now been routed into a shrinking-scale H1 nonkernel field observation.

There is no remaining kernel-custodied diagonal alternative required for the fixed-L prime-silent route.

## 16. What happened to the ratio-to-diagonal branch

The original target of this pass was to close the Branch-K ratio-to-diagonal system.

The spectral-shadow analysis changes the route.

Even if

f in W_sh

and all five spectral shadows have exact full-Suzuki superflat diagonal behavior at the selected centers, every nonzero spectral component

P_lambda f

must eject from V.

Those ejections jointly detect f and can be routed to K_c^perp.

Therefore:

boxed:
failure of local log-diagonal rigidity
does not protect a nonzero prime-silent regular-kernel vector from spectral-shadow escape.

The diagonal branch is no longer terminal for this fixed-L problem.

It remains relevant to the canonical shrinking-collar edge obstruction, but it need not be solved before the prime-silent four-delay classification proceeds.

## 17. Remaining obstruction

The route now has only one surviving interface:

boxed:
finite-dimensional K_c^perp H1 field detector
->
physical edge / Sigma_c local observation.

Series-53 provides shrinking detection at adaptively chosen reachable arithmetic centers.

Series-54 identifies the exact finite edge Runge gate needed to move that detection into a prescribed edge or singular-site neighborhood.

The spectral-shadow theorem does not by itself prove that gate.

So K_c^{ps}=0 remains unproved in the full four-delay chamber.

## 18. Result

This pass gives both a negative and a positive resolution of the recustodied ratio-to-diagonal experiment.

Negative:

1. the six projected dyadic sources contain only five independent spectral shadows;
2. the exact full-Suzuki local superflat source class has arbitrarily large finite dimension;
3. finite shadow multiplicity therefore does not restore local archimedean quasi-analyticity.

Positive:

1. every nonzero dyadic spectral component must leave V, because V contains no D-eigenvector;
2. the five spectral-shadow ejections are jointly injective;
3. after at most two additional first-prime steps, fifteen channels land in K_c^perp with a positive norm floor;
4. their finite-dimensional screw-field image has a positive fixed-scale floor;
5. the arithmetic field-return theorem upgrades this to a shrinking local interior-field estimate.

Thus the kernel-custodied diagonal hard branch collapses into the nonkernel field branch.

## Fixed-L status

This pass does not yet prove

K_c^{ps}=0

through the entire four-delay chamber.

The last load-bearing continuous prime-channel injectivity range remains

0<L<=log(16/3).

The canonical theorem cursor remains

SZ-CROSS-COLLAR-3.

## Next frontier

Next target:

SZ-KERNEL-EDGE-GERM-58 / SPECTRAL-SHADOW EDGE RUNGE

The next pass should exploit the additional structure of the new finite nonkernel range.

Unlike the generic escape range of series-53/54, each primary source comes from an ambient dyadic spectral projection

P_lambda f,

with

D P_lambda f=lambda P_lambda f.

Priority:

1. derive the exact first-prime / log4 fiber pattern of each P_lambda f;
2. express the nonkernel field
   G_c P_lambda f
   directly through those finite dyadic patterns and the kernel equation for f;
3. test the finite edge Runge gate on the spectral-shadow escape range using the explicit five dyadic eigenpatterns;
4. determine whether vanishing of these fields on a physical edge neighborhood forces the corresponding P_lambda f to enter K_c, which would contradict ambient D-eigenvector exclusion;
5. if successful, conclude K_c^{ps}=0 throughout log5<L<=log6.

A positive spectral-shadow edge-Runge theorem would close the fixed-L four-delay prime-silent branch without solving the local log-diagonal quasi-analyticity problem.

No public promotion and no canonical cursor movement are asserted.
