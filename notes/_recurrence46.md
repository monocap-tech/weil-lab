# SZ edge recurrence 46 — complete four-delay matrix coordinates

Date: 2026-09-27
Branch: sz-cross-collar
Status: UNRATIFIED RESIDUE / NF PASS
Canonical parent: SZ-CROSS-COLLAR-3
Immediate residue: series-45
Public promotion: forbidden

## Objective

Construct a genuinely finite coordinate system for the complete repaired four-delay matrix before attempting determinant certification.

The relay audit in series 44-45 shows that one must distinguish:

- h-propagation;
- at most two k-moves;
- one one-way p-relay move.

The key result of this pass is that every connected directed dependency component occupies only ten residue classes modulo h.

Therefore the complete folded matrix has a finite, explicit coordinate bound independent of L inside the four-delay chamber.

This pass does not yet certify the final matrix determinants.

## 1. Arithmetic decomposition

Set

h = log(81/80),

k = log(16/15),

p = log(10/9).

Write

k = 5h + kappa,

p = 8h + rho.

Then

kappa
=
log[
(16/15)(80/81)^5
],

rho
=
log[
(10/9)(80/81)^8
].

Direct rational comparison gives

0 < kappa < h,

0 < rho < h.

Numerically,

kappa/h = 0.195284140823...,

rho/h = 0.481412440476....

## 2. Why only two k-moves occur

The repaired transfer uses k in two ways:

- stacked forward k-sheets;
- the causal predecessor y-k.

Across the chamber,

u <= log(6/5) < 3k.

Therefore a directed dependency component can contain at most two k-moves before leaving the support.

Equivalently the net k-residue displacement is

m kappa

with

m in {-2,-1,0,1,2}.

This is the same finite k-depth established structurally in series 41-43.

## 3. Why only one p-move occurs

The p-channel is the lower-defect relay

P(t)=X(p+t),

Q(t)=S(p+t).

Series 44-45 prove:

- the relay is nilpotent;
- it has no independent entrance data;
- after Schur elimination it does not feed into another p-relay.

Thus p occurs as a one-way boundary move at most once in any connected directed dependency component.

Therefore the p-residue displacement is

epsilon rho

with

epsilon in {0,1}.

No second p-layer is generated.

## 4. Four-delay residue alphabet

Combining Sections 2-3, every base argument in one connected dependency component has h-residue

m kappa + epsilon rho mod h,

where

m in {-2,-1,0,1,2},

epsilon in {0,1}.

Hence there are at most ten residue classes.

This is the four-delay residue alphabet registered in the terminology file.

The ten classes are all distinct.

Their exact order on [0,h) is

0,

rho-2kappa,

kappa,

rho-kappa,

2kappa,

rho,

-2kappa mod h,

rho+kappa,

-kappa mod h,

rho+2kappa.

Numerically, divided by h, they are

0,

0.090844158828...,

0.195284140824...,

0.286128299652...,

0.390568281648...,

0.481412440476...,

0.609431718352...,

0.676696581300...,

0.804715859176...,

0.871980722124....

## 5. Exact rational certification of the residue order

Let

E_h=81/80,

E_kappa
=
(16/15)(80/81)^5,

E_rho
=
(10/9)(80/81)^8.

Every exponentiated residue is of the form

E_rho^epsilon
E_kappa^m
E_h^q

for the unique integer q that places the result in

[1,E_h).

Thus every residue comparison is a rational inequality.

Examples:

exp(rho-2kappa)
=
32805/32768,

exp(rho-kappa)
=
1600000/1594323,

exp(-kappa mod h)
=
847288609443/838860800000.

The complete ordering above was checked by exact rational comparison of the ten exponentials.

No floating-point logarithmic ordering is load-bearing.

## 6. Residue fiber coordinates

Fix a master local coordinate r in one open interval of the residue-circle partition determined by the ten alphabet points.

For each residue symbol

g = m kappa + epsilon rho mod h,

and each integer level n for which

x = r + g + n h

lies in the active base-argument domain, introduce the two-state variable

V_g,n(r)
=
(
X(x),
S(x)
)^T.

The integer carry caused by reducing r+g modulo h is constant on each residue-circle atom.

Therefore every shift by h, k, or the single p-relay move acts by a fixed permutation of residue symbols plus a fixed integer level change.

All coefficient matrices are constant.

## 7. Uniform level bound

The base argument domain satisfies

0 < x < u,

and

u < 15h.

Therefore each residue class contains at most fifteen active h-levels.

With ten residue classes and two scalar coordinates per V-state, one connected component requires at most

10 * 15 * 2
=
300

scalar columns before Schur elimination.

This is a deliberately crude uniform bound.

The p-relay variables P,Q require no additional columns:

they are exactly V-states at p-shifted arguments, already represented by the epsilon=1 residue classes.

## 8. Complete row library

The globally valid reduced matrix is assembled from the exact rows already derived in series 34-45.

### A. Lower relay propagation

For

0<t<e-h,

two rows:

mu P(t+h)
-
G X(t)
-
delta S(t)
-
beta S(t+k)
=
0,

mu Q(t+h)
+
mu P(t)
-
G S(t)
-
delta X(t)
-
beta 1_(t>k) X(t-k)
=
0.

### B. Relay terminal closure

For

max(0,e-h)<t<e,

one row:

mu P(t)
-
G S(t)
-
delta X(t)
-
beta 1_(t>k) X(t-k)
=
0.

### C. P-overlap entrance/bulk rows

For

e<x<h,

when nonempty:

S(x)-R X(x)=0.

For

max(e,h)<x<j:

S(x)
-
R X(x)
+
Q X(x-h)
-
Z 1_(x>k) X(x-k)
=
0.

### D. J-overlap rows

For

e-h<x<u-h:

S(x+h)
+
T X(x)
-
E S(x)
-
F 1_(x<alpha) S(x+k)
=
0.

### E. Terminal J row

When

e<h,

for

u-h<x<p:

S(x)-R^(-1)X(x)=0.

Series 41 proves the terminal k-gate is absent.

These rows are necessary conditions for every actual four-delay source solution.

Therefore injectivity of this enlarged reduced matrix is sufficient for injectivity of the actual arithmetic-delay operator.

No consistency relation beyond the actual source reconstruction is needed for this sufficient test.

## 9. Matrix-size bound

There are at most 150 two-state V-nodes.

A crude row bound is:

- at most 300 lower-relay propagation rows;
- at most 150 relay terminal rows;
- at most 150 P rows;
- at most 150 J rows;
- at most 150 terminal rows.

Thus every fiber matrix can be embedded in a rectangular system with at most

900 rows

and

300 columns.

Most chambers are much smaller.

After the nilpotent relay and locally pivotable rows are Schur-eliminated, the effective square matrix is substantially smaller.

The point of this bound is finiteness, not optimality.

## 10. Parameter-cell structure

The matrix coefficients do not depend on L.

Only row/node presence changes.

Every node coordinate is

r + g + n h

with g in the ten-residue alphabet.

Every gate or support test compares such a coordinate with one of the affine boundaries

0,

e,

e-h,

u=p+e,

u-h,

alpha=u-k,

p,

h,

j,

k.

Hence every combinatorial change occurs on an affine line in the two parameters

(e,r).

For example,

r+g+n h=e,

r+g+n h=e-h,

r+g+n h=p+e-h,

r+g+n h=e+p-k.

The rectangle

0<e<=k+h,

0<r<h

is therefore cut by finitely many affine lines into finitely many open cells.

On each cell:

- the active node set is fixed;
- every indicator is fixed;
- the row pattern is fixed;
- the coefficient matrix is one constant matrix depending only on the Weil weights.

This is the complete-matrix chamber theorem.

## 11. Exact chamber generation

A reliable certification procedure is now mechanical.

For each residue-circle atom:

1. enumerate the at-most-fifteen h-levels of each of the ten residue symbols;
2. form every gate/support affine equality generated by the row library;
3. sort the resulting e-r crossing lines by exact exponentiated rational comparison;
4. choose one symbolic cell representative;
5. assemble the constant reduced matrix;
6. Schur-eliminate the relay rows and other known local pivots;
7. certify full column rank using outward rational weight intervals.

No threshold-by-threshold source derivation is required.

The only remaining work is finite matrix generation and rank certification.

## 12. Scope and relation to earlier atomizations

This pass does not rely on the globally overextended K_r recurrence from series 42-43.

Instead it uses only row identities on their proved domains.

The K_1,K_2,K_3 scattering blocks remain useful Schur-compression tools inside the matrix generator.

The causal-path and relay analyses remain useful for bounding the residue alphabet and matrix size.

Thus the audits in series 41-45 are incorporated rather than bypassed.

## 13. Fixed-L injectivity status

No final determinant list is certified in this pass.

Therefore the load-bearing continuous positive range remains

0<L<=log(16/3).

The post-log(16/3) problem has now been reduced to a finite family of explicit constant matrices with a uniform 300-column bound.

## 14. Quantitative status

If every final cell matrix M_cell has full column rank, then

sigma_cell
=
sigma_min(M_cell)
>
0.

Because there are finitely many cells, the minimum over the full four-delay chamber would give a chamber-uniform fixed-scale boundary floor for this reduced prime-channel system.

That would still be a fixed-scale result.

No shrinking-collar power law follows automatically.

## Next frontier

Next target:

SZ-KERNEL-EDGE-GERM-47 / MATRIX GENERATOR AND RANK AUDIT

The next pass should implement the finite cell generator described above and produce:

1. the exact number of distinct matrix types;
2. their dimensions after Schur elimination;
3. determinant or full-column-rank certificates;
4. the minimum certified fixed-scale singular-value margin.

If all matrices are transverse, this would establish the first globally complete fixed-L four-delay prime-channel injectivity theorem.

Even then, SZ-CROSS-COLLAR-3 must remain fixed until the shrinking-collar drilling interface is controlled.

No public promotion and no canonical cursor movement are asserted.
