# SZ edge recurrence 51 — nondyadic spectral separation and seven-step ejection

Date: 2026-09-27
Branch: sz-cross-collar
Status: UNRATIFIED RESIDUE / NF PASS
Canonical parent: SZ-CROSS-COLLAR-3
Immediate residue: series-50
Public promotion: forbidden

## Objective

Separate the genuinely nondyadic log3/log5 compensator from the dyadic log2/log4 block after the exact reduction of series-50.

The principal result is stronger than a support-triangular estimate.

The normalized four-delay prime operator splits into two self-adjoint finite-spectrum blocks

P_c/A2 = D + N,

where

D = C_(log2) + gamma C_(log4)

is the dyadic block and

N = beta C_(log3) + delta C_(log5)

is the nondyadic edge block.

The spectra of D and -N are disjoint for the exact Weil weights.

Consequently a prime-silent vector cannot be an eigenvector of either block.

More strongly, on every closed subspace V of the ambient prime-silent kernel, the common dyadic/nondyadic ejection is dynamically observable in at most seven steps, with a quantitative lower bound depending only on the fixed Weil weights and not on dim(V).

This does not yet prove prime-silent triviality. It converts the remaining problem into custody of a uniformly observable finite-depth ejection.

## 1. Prime operator split

Let

a=log2,
b=log3,
d=log5,

and use

C_lambda=S_lambda^+ + S_lambda^-.

Normalize by the log2 weight A2.

Then

P_c/A2
=
C_a
+
gamma C_(2a)
+
beta C_b
+
delta C_d.

Define

D
=
C_a
+
gamma C_(2a),

and

N
=
beta C_b
+
delta C_d.

Thus

boxed:
P_c/A2=D+N.

On the prime-silent space

Z=ker P_c,

one has the exact pointwise operator relation

boxed:
Nf=-Df

for every f in Z.

## 2. Spectrum of the dyadic block

In the four-delay chamber

log5<L<=log6,

one has

2a<L<3a.

Decompose the source interval into a-residue fibers.

For residues supporting three points

r,r+a,r+2a,

the operator D has the matrix

D_3
=
[0       1       gamma;
 1       0       1;
 gamma   1       0].

The antisymmetric endpoint vector has eigenvalue

-gamma=-1/sqrt2.

On the symmetric endpoint subspace the characteristic equation is

z^2-gamma z-2=0.

Hence the remaining two eigenvalues are

(1+sqrt17)/(2sqrt2),

(1-sqrt17)/(2sqrt2).

For residues supporting only two points, C_(2a)=0 and D is the two-vertex adjacency matrix, with eigenvalues

+1,-1.

Therefore

boxed:
spec(D)
=
{
1,
-1,
-1/sqrt2,
(1+sqrt17)/(2sqrt2),
(1-sqrt17)/(2sqrt2)
}.

Equivalently D satisfies

boxed:
p_D(D)=0,

where

p_D(z)
=
(z^2-1)
(z+gamma)
(z^2-gamma z-2).

## 3. Geometry of the nondyadic block

Both

b>L/2

and

d>L/2.

Set

r=d-b=log(5/3),

u=L-d,

w_b=L-b=r+u.

Across the chamber,

0<u<log(6/5)<r,

so

r<w_b<2r.

The b-shift therefore couples only the two b-edge blocks

(0,w_b)

and

(b,L).

Identify both with

H_b=L2(0,w_b).

In this decomposition,

C_b
=
[0 I;
 I 0].

The d-shift is a narrower partial swap.

Let

T:H_b->H_b

be the truncated left shift by r:

(T phi)(x)
=
phi(x+r)

for 0<x<u,

and zero otherwise.

Then

T^2=0,

and

C_d
=
[0 T;
 T^* 0].

Therefore the nondyadic operator is

boxed:
N
=
[0                 beta I+delta T;
 beta I+delta T^*  0]

on the b-edge space,

and N=0 on the central b-gap.

This is the nondyadic edge operator registered in the terminology file.

## 4. Exact nondyadic spectrum

Split

H_b

into

A=(0,u),

G=(u,r),

B=(r,r+u).

On G,

T=T^*=0.

Therefore the corresponding N-fibers have eigenvalues

+beta,-beta.

On A direct_sum B, the operator

M=beta I+delta T

has the constant two-by-two matrix

[beta  delta;
 0     beta].

The nonzero eigenvalues of

[0 M;
 M^* 0]

are plus/minus the singular values of M.

They are

boxed:
sigma_+ =
( sqrt(delta^2+4 beta^2) + delta )/2,

sigma_- =
( sqrt(delta^2+4 beta^2) - delta )/2.

Thus

boxed:
spec(N)
=
{
0,
+beta,-beta,
+sigma_+,-sigma_+,
+sigma_-,-sigma_-
}.

The equivalent annihilating polynomial is

boxed:
p_N(z)
=
z
(z^2-beta^2)
(
z^4-(2 beta^2+delta^2)z^2+beta^4
).

## 5. Exact spectral separation

Use the certified logarithmic enclosures already employed in series 38-40:

1.5849625
<
log3/log2
<
1.5849626,

2.3219280
<
log5/log2
<
2.3219281,

together with rational square-root enclosures.

They give, conservatively,

1.29<beta<1.30,

1.46<delta<1.48.

Hence

0.747
<
sigma_-
<
0.762,

and

2.212
<
sigma_+
<
2.237.

The positive absolute values occurring in spec(N) therefore lie in the disjoint intervals

(0.747,0.762),

(1.29,1.30),

(2.212,2.237).

The positive absolute values occurring in spec(D) are exactly

1/sqrt2 approximately 0.7071,

1,

(sqrt17-1)/(2sqrt2) approximately 1.1042,

(sqrt17+1)/(2sqrt2) approximately 1.8113.

These sets are disjoint.

Therefore

boxed:
spec(D) intersect (-spec(N)) = emptyset.

Equivalently,

p_D(z)

and

p_N(-z)

are relatively prime.

## 6. Ambient eigenvector exclusion

Suppose

0!=f in ker P_c

and

Nf=lambda f.

Prime silence gives

Df=-Nf=-lambda f.

Thus

lambda in spec(N)

and

-lambda in spec(D),

contradicting Section 5.

Therefore

boxed:
ker P_c contains no nonzero N-eigenvector.

The same argument with D and N reversed gives

boxed:
ker P_c contains no nonzero D-eigenvector.

This is an ambient result; regular-kernel membership is not used.

## 7. Shared compression/ejection pair

Let

V subset ker P_c

be any closed subspace.

Let Pi be orthogonal projection onto V and Q=I-Pi.

Define

B
=
Pi D|_V,

F
=
Q D|_V.

Since

N|_V=-D|_V,

the nondyadic compression and ejection are exactly

Pi N|_V=-B,

Q N|_V=-F.

So the dyadic and nondyadic blocks do not carry two independent ejection families.

They carry one common ejection family with opposite sign.

The question is how deeply that common ejection must be observed.

## 8. Seven-step theorem

Claim:

boxed:
intersection_{m=0}^6 ker(F B^m)
=
{0}.

Take f in the intersection.

For every

0<=m<=6,

D(B^m f)
=
B^(m+1)f,

because the ejection term

F B^m f

vanishes.

Therefore, for every

0<=j<=7,

D^j f
=
B^j f.

Similarly, since

N|_V=-B-F,

the same vanishing gives

N(B^m f)
=
-B^(m+1)f,

hence

N^j f
=
(-1)^j B^j f

for

0<=j<=7.

Now

deg p_D=5,

so

p_D(D)f=0

implies

p_D(B)f=0.

Also

deg p_N=7,

so

p_N(N)f=0

implies

p_N(-B)f=0.

But

p_D

and

p_N(-z)

are relatively prime.

Choose Bezout polynomials U,V_0 with

U(z)p_D(z)
+
V_0(z)p_N(-z)
=
1.

Evaluating at B and applying to f gives

f=0.

Therefore the intersection is trivial.

This is the seven-step spectral ejection property registered in the terminology file.

## 9. Quantitative dimension-free floor

The preceding proof can be made quantitative without choosing a basis of V.

For any polynomial

p(z)=sum_j c_j z^j,

the exact telescoping identity is

D^j f-B^j f
=
sum_{m=0}^{j-1}
D^(j-1-m) F B^m f.

Since

p_D(D)=0,

there exists a constant C_D depending only on p_D and ||D|| such that

||p_D(B)f||
<=
C_D
sum_{m=0}^4
||F B^m f||.

Likewise, using N|_V=-B-F and p_N(N)=0,

||p_N(-B)f||
<=
C_N
sum_{m=0}^6
||F B^m f||,

where C_N depends only on the fixed nondyadic weights.

The Bezout identity gives a fixed constant C_B with

||f||
<=
C_B
(
||p_D(B)f||
+
||p_N(-B)f||
).

Therefore there exists

boxed:
nu_* > 0

depending only on the four exact Weil weights such that

boxed:
(
sum_{m=0}^6
||F B^m f||^2
)^(1/2)
>=
nu_* ||f||

for every closed

V subset ker P_c

and every

f in V.

The important point is:

nu_*

does not depend on

dim V.

This is stronger than the dimension-dependent observability floors of series 49-50.

No explicit optimized value of nu_* is claimed.

## 10. Interpretation for K_c^{ps}

Apply Section 9 to

V=K_c^{ps}.

If V is nonzero, every vector has a finite-depth dynamically observable escape from V under the dyadic block D:

boxed:
D=C_(log2)+gamma C_(log4).

Prime silence forces the nondyadic block N to carry exactly the opposite escape.

Thus the four-delay arithmetic equation has become a spectral matching problem between two finite-spectrum self-adjoint blocks with incompatible individual spectra.

A nonzero survivor is possible only because D and N do not preserve V and their ejections compensate.

The entire remaining obstruction is therefore in the off-diagonal custody of this shared ejection.

## 11. Why spectral disjointness alone does not prove injectivity

Disjoint spectra of two self-adjoint operators do not imply that their sum is invertible when the operators fail to commute.

Here

D+N=P_c/A2.

The relation

(D+N)f=0

can still hold because D and N mix their spectral subspaces.

If D and N preserved a common nonzero finite-dimensional subspace inside ker P_c, self-adjointness would give a common eigenvector after using N=-D on that subspace, contradicting Section 6.

Therefore such a common invariant subspace cannot exist.

But a prime-silent vector may still move between the dyadic and nondyadic spectral sectors through the shared ejection F.

So the unresolved object is not spectral location.

It is spectral transport.

## 12. Relation to the reduced compensator of series-50

Series-50 eliminated log4 in favor of

- one extra first-prime dynamic step;
- compression curvature;
- the explicit a-boundary projector.

The present split keeps log4 inside D instead.

This has one advantage:

both D and N become exact finite-spectrum ambient operators.

The price is that the ejection F packages the dyadic curvature and boundary correction implicitly.

Thus the two formulations are equivalent views of the same obstruction:

series-50:
first-prime dynamics plus explicit curvature/boundary terms;

series-51:
two incompatible finite-spectrum blocks plus one shared ejection.

The latter is better suited to a resultant/Bezout argument.

## 13. Non-dyadic support algebra

The nondyadic pair has an additional finite local algebra.

Let

J
=
C_b C_d
+
C_d C_b.

In b-edge coordinates,

J

is the direct sum of two copies of the symmetric truncated shift by

r=d-b

on an interval of length

w_b=r+u<2r.

Therefore

spec(J) subset {-1,0,1},

and

J^3=J.

Also

C_b^2=D_b,

C_d^2=D_d,

with nested edge projectors

D_d <= D_b <= D_a.

Hence

N^2
=
beta^2 D_b
+
delta^2 D_d
+
beta delta J.

This is the exact finite edge algebra behind the polynomial p_N.

It confirms that the log3/log5 compensator is shallow internally.

Its ability to match the dyadic block comes only from spectral-subspace mixing, not from an unbounded internal recurrence.

## 14. Kernel/nonkernel custody

Now specialize again to

V=K_c^{ps} subset K_c.

Split the shared ejection

F
=
H+M,

where

H
=
(Pi_K-Pi_V)D|_V

lies in

K_c intersect V^perp,

and

M
=
(I-Pi_K)D|_V

lies in

K_c^perp.

Because N|_V=-D|_V, the nondyadic block has exactly the opposite split:

H_N=-H,

M_N=-M.

Therefore the seven-step lower bound is carried jointly by:

- regular-kernel escape outside the prime-silent branch;
- genuine nonkernel escape.

The current result does not force either block separately to be nonzero on every vector.

## 15. What would close the four-delay branch

The seven-step theorem leaves a sharply finite target.

It would suffice to prove one of:

1. nonkernel dominance:
   the seven-step observation remains injective after replacing F by M;

2. kernel-escape rank defect:
   the regular-kernel block H cannot carry a seven-step injective observation on V;

3. field separation:
   GERM-13's screw-field representation of M is incompatible with the nondyadic edge algebra in Section 13;

4. finite-spectrum curvature control:
   the off-diagonal transport between the D and N spectral decompositions has rank or support too small to realize the Bezout-required observation floor;

5. shrinking-collar transfer:
   a nonzero seven-step M component forces a finite-order collar defect.

No such theorem is proved here.

## 16. Fixed-L status

This pass does not prove

K_c^{ps}=0

through the full four-delay chamber.

The last load-bearing continuous prime-channel injectivity range remains

0<L<=log(16/3).

The canonical theorem cursor remains

SZ-CROSS-COLLAR-3.

## Next frontier

Next target:

SZ-KERNEL-EDGE-GERM-52 / SPECTRAL-EJECTION CUSTODY

The next pass should start from the uniform seven-step estimate

sum_{m=0}^6 ||F B^m f||^2
>=
nu_*^2 ||f||^2

on

V=K_c^{ps},

split

F=H+M

into regular-kernel and nonkernel escape, and determine which block must carry a separating subfamily.

Priority:

1. obtain a rank/dimension dichotomy for the seven H-blocks versus seven M-blocks;
2. on the M side use GERM-13 to convert nonkernel escape into explicit boundary-strip screw fields;
3. on the H side use finite kernel dimension and the no-raw-invariant-subspace theorem to seek a forced secondary escape;
4. determine whether iterating this dichotomy yields a finite escape tree ending in K_c^perp with a quantitative detector.

A successful finite escape-tree theorem would finally move the prime-silent problem from spectral transport to the already-isolated shrinking-collar transfer interface.

No public promotion and no canonical cursor movement are asserted.
