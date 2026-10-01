# RPB-48 — Threshold Birman--Schwinger boundary-transfer matrix

**Date:** 2026-09-28  
**Branch:** \`research/reflected-packet-bridge\`  
**Status:** **PASS AS RETYPING / SELECTED-COLUMN BOUNDARY MATRIX IDENTIFIED / BIRMAN--SCHWINGER GRAM DATA DO NOT DETERMINE IT / FULL-RANK AMPLITUDE IS NOT THE PERSISTENCE OBSTRUCTION / EXACT STOP IS THE BACKGROUND RESOLVENT ENDPOINT SYMBOL**  
**Dependencies:** RPB-22, RPB-24, RPB-30, RPB-33, RPB-47; RPB-EXT-A6 contextual boundary regularity.  
**Promotion status:** none.

## 0. Objective

RPB-47 reduced the exceptional prime-threshold branch to finite-dimensional
boundary data on the unit-gain/core eigenspace.

The proposed RPB-48 task was:

1. derive a boundary Mellin formula for
   \[
   h_v=A_{B,c}^{-1}\Phi_c^*v;
   \]
2. express the first admissible Mellin amplitude row in selected coordinates;
3. determine whether the resulting finite matrix has full column rank on the
   unit-gain space;
4. if that cannot be done from the current package, isolate the exact missing
   resolvent boundary datum.

RPB-48 completes items 2 and 4 exactly, and corrects item 3.

The selected-coordinate boundary matrix is explicit once the endpoint Mellin
coefficient of each background-resolvent column is known.

But the Birman--Schwinger matrix stores only finite interior Gram pairings of
those columns.

It does not determine their endpoint Mellin residues.

Moreover, full rank of the **allowed amplitude matrix** would not obstruct
persistence: a persistent nonzero threshold mode is required to have nonzero
allowed Mellin amplitude.

The genuine obstruction is the complementary boundary defect.

Thus the exact remaining object is the endpoint boundary symbol / parametrix
of the actual background resolvent \(A_{B,c}^{-1}\).

---

## 1. Finite selected forcing columns

Let

\`\`\`math
M'
\`\`\`

be the finite selected coefficient space used in the background
Birman--Schwinger reduction.

Choose an orthonormal basis

\`\`\`math
e_1,\dots,e_d.
\`\`\`

Define the selected physical forcing columns

\`\`\`math
\boxed{
g_j
=
\Phi_c^*e_j
}
\`\`\`

and the background resolvent columns

\`\`\`math
\boxed{
h_j
=
A_{B,c}^{-1}g_j.
}
\`\`\`

Then for

\`\`\`math
v
=
\sum_{j=1}^d
v_j e_j,
\`\`\`

the resolvent extremizer is

\`\`\`math
\boxed{
h_v
=
A_{B,c}^{-1}\Phi_c^*v
=
\sum_{j=1}^d
v_j h_j.
}
\`\`\`

On the screw-visible/core subspace,

\`\`\`math
u_v
=
Dh_v.
\`\`\`

---

## 2. Birman--Schwinger matrix in these columns

The endpoint Birman--Schwinger matrix is

\`\`\`math
\mathsf K_c
=
\Phi_cA_{B,c}^{-1}\Phi_c^*.
\`\`\`

Therefore

\`\`\`math
\boxed{
(\mathsf K_c)_{kj}
=
\langle
h_j,
g_k
\rangle.
}
\`\`\`

Thus \(\mathsf K_c\) records the finite family of interior pairings between:

- the resolvent columns \(h_j\); and
- the selected forcing columns \(g_k\).

At the neutral edge,

\`\`\`math
E_*
=
\ker(\mathsf K_c-I).
\`\`\`

If

\`\`\`math
v\in E_*,
\`\`\`

then

\`\`\`math
\Phi_ch_v
=
\Phi_cA_{B,c}^{-1}\Phi_c^*v
=
v.
\`\`\`

Hence the selected coordinate of the physical neutral mode is exactly the
unit-gain vector itself.

This does not yet determine the endpoint germ of \(Dh_v\).

---

## 3. Boundary Mellin rows of the resolvent columns

Fix an admissible threshold channel \(\beta\).

Whenever the column \(h_j\) is threshold-compatible, RPB-47 defines

\`\`\`math
\mathfrak a_\beta(Dh_j)
=
\operatorname*{Res}_{z=-\beta}
\int_0^\delta
(Dh_j)(c-s)s^{z-1}\,ds.
\`\`\`

Define the row entries

\`\`\`math
\boxed{
b_{\beta,j}
=
\mathfrak a_\beta(Dh_j).
}
\`\`\`

Then linearity gives

\`\`\`math
\boxed{
\mathfrak T_{\beta,c}(v)
=
\sum_{j=1}^d
b_{\beta,j}v_j.
}
\`\`\`

Thus the threshold Mellin row is an ordinary finite selected-coordinate row.

No infinite-dimensional ambiguity remains once the endpoint coefficient of
each resolvent column is known.

---

## 4. Selected-column boundary matrix

Choose finitely many admissible channels

\`\`\`math
\beta_1,\dots,\beta_M
\`\`\`

whose rows span all threshold Mellin amplitudes on the finite
threshold-compatible unit-gain space.

Define

\`\`\`math
\boxed{
(\mathbf B_c)_{\ell j}
=
\mathfrak a_{\beta_\ell}
\left(
D A_{B,c}^{-1}\Phi_c^*e_j
\right).
}
\`\`\`

Then

\`\`\`math
\boxed{
\mathbf T_c
=
\mathbf B_c
\big|_{E_*^{\rm tc}}.
}
\`\`\`

This is the exact threshold boundary-transfer matrix in selected coordinates.

It is basis-covariant in the expected way.

So the matrix asked for by RPB-47 exists and is finite.

---

## 5. Background resolvent boundary symbol

The unresolved part is the scalar functional

\`\`\`math
\boxed{
\mathcal B_{\beta,c}(g)
=
\mathfrak a_\beta
\left(
D A_{B,c}^{-1}g
\right).
}
\`\`\`

Then

\`\`\`math
\boxed{
\mathfrak T_{\beta,c}
=
\mathcal B_{\beta,c}\Phi_c^*.
}
\`\`\`

This \(\mathcal B_{\beta,c}\) is the endpoint Mellin boundary symbol of the
background resolvent.

The current RPB package supplies:

- the background operator \(A_{B,c}\);
- its positive inverse in the abstract operator sense;
- the finite selected forcing map \(\Phi_c^*\);
- the compressed Gram matrix
  \[
  \Phi_cA_{B,c}^{-1}\Phi_c^*;
  \]
- interior analytic regularity of core-neutral modes;
- the threshold Carleman indicial family.

It does **not** supply an endpoint Green/Poisson kernel or conormal boundary
expansion for

\`\`\`math
A_{B,c}^{-1}g.
\`\`\`

That is exactly the missing input needed to evaluate
\(\mathcal B_{\beta,c}\).

---

## 6. Why ordinary logarithmic-Laplacian boundary regularity is insufficient

The available general Dirichlet theory for the logarithmic Laplacian gives the
optimal boundary size scale

\`\`\`math
|u(x)|
\lesssim
\ell^{1/2}
\left(
\operatorname{dist}(x,\partial\Omega)
\right)
\`\`\`

for bounded forcing.

The same literature shows that this scale is sharp for the torsion problem.

This is valuable regularity information, but it is not a source-dependent
boundary coefficient formula.

In particular, it does not compute

\`\`\`math
g
\longmapsto
\operatorname*{Res}_{z=-\beta}
\mathcal M
\left[
D A_{B,c}^{-1}g
\right](z)
\`\`\`

for the actual Weil background operator, which also contains:

- finite prime translations;
- finite-rank selected/background corrections;
- the exact compact-window support geometry.

Therefore the known \(\ell^{1/2}\) boundary estimate does not determine
\(\mathbf B_c\).

### External scope pin

RPB-EXT-A6 records Hernández-Santamaría--López Ríos--Saldaña,
Theorems 1.1 and 1.2.

---

## 7. Gram data and boundary data are differently typed

The Birman--Schwinger matrix consists of

\`\`\`math
\boxed{
\langle
A_{B,c}^{-1}\Phi_c^*e_j,
\Phi_c^*e_k
\rangle.
}
\`\`\`

The boundary-transfer matrix consists of

\`\`\`math
\boxed{
\mathfrak a_{\beta_\ell}
\left(
D A_{B,c}^{-1}\Phi_c^*e_j
\right).
}
\`\`\`

The first is an interior Gram compression.

The second is an endpoint conormal trace.

There is no algebraic identity converting one into the other in the current
operator package.

This is the Gram/boundary data separation.

---

## 8. Abstract nonidentifiability model

The failure above is not merely an accident of notation.

Consider an abstract Hilbert space \(H\), finite-dimensional \(M\), a map

\`\`\`math
\Phi:H\to M,
\`\`\`

and a boundary functional

\`\`\`math
B:H\to\mathbb C.
\`\`\`

Let \(X\) be a positive invertible bounded operator.

Choose

\`\`\`math
w\in\ker\Phi,
\qquad
y\in\operatorname{Ran}\Phi^*,
\qquad
B(w)\ne0.
\`\`\`

Define the finite-rank self-adjoint operator

\`\`\`math
Q
=
w\otimes y
+
y\otimes w.
\`\`\`

Because

\`\`\`math
\Phi w=0
\`\`\`

and

\`\`\`math
w\perp\operatorname{Ran}\Phi^*,
\`\`\`

we have

\`\`\`math
\boxed{
\Phi Q\Phi^*
=
0.
}
\`\`\`

Hence for sufficiently small \(\varepsilon\) in a bounded positive model,

\`\`\`math
X_\varepsilon
=
X+\varepsilon Q
\`\`\`

remains positive invertible and

\`\`\`math
\boxed{
\Phi X_\varepsilon\Phi^*
=
\Phi X\Phi^*.
}
\`\`\`

But generically

\`\`\`math
\boxed{
B X_\varepsilon\Phi^*
\ne
B X\Phi^*.
}
\`\`\`

Thus identical compressed Gram data can coexist with different boundary
transfer rows.

This is an abstract scope/no-go theorem:

\`\`\`math
\boxed{
\text{Birman--Schwinger Gram data alone cannot determine endpoint boundary data.}
}
\`\`\`

The construction is not asserted to be a perturbation of the actual Weil
background operator.

Its purpose is to prove data-type insufficiency.

---

## 9. Consequence for rank tests

The cursor proposed testing whether

\`\`\`math
\mathbf T_c
\`\`\`

has full column rank on the unit-gain space.

This is not the correct exclusion test.

RPB-47 proved that a nonzero persistent threshold mode must have a nonzero
admissible amplitude vector.

Therefore full column rank would imply only

\`\`\`math
v\ne0
\Longrightarrow
\mathbf T_cv\ne0,
\`\`\`

which is compatible with persistence.

Indeed, such a result would say that every nonzero threshold-compatible
unit-gain vector carries some conormal amplitude.

So:

\`\`\`math
\boxed{
\text{full rank of the allowed amplitude matrix does not exclude persistence}.
}
\`\`\`

This is the allowed-amplitude rank no-gain.

---

## 10. The actual boundary obstruction

For an arbitrary unit-gain/core vector, the endpoint expansion of the
right-limit equation may contain:

1. admissible threshold indicial modes;
2. forbidden Mellin channels;
3. integer-power/logarithmic singular terms;
4. an analytic exterior remainder germ.

The admissible coefficients are the rows of \(\mathbf T_c\).

They are not defects.

Strict persistence instead requires every **forbidden/nonmatching** coefficient
and the residual analytic germ to vanish.

Define schematically

\`\`\`math
\boxed{
\mathbf D_c:
E_*^{\rm core}
\to
\mathcal Y_c
}
\`\`\`

to collect these boundary defects.

Then a nonzero persistent vector must satisfy

\`\`\`math
\boxed{
\mathbf D_cv=0,
\qquad
\mathbf T_cv\ne0.
}
\`\`\`

Thus the rank question belongs to \(\mathbf D_c\), not to the admissible
amplitude matrix \(\mathbf T_c\).

---

## 11. Why \(\mathbf D_c\) also requires the resolvent boundary symbol

To construct \(\mathbf D_c\), one needs the full endpoint conormal expansion
of

\`\`\`math
D A_{B,c}^{-1}\Phi_c^*v.
\`\`\`

That expansion must identify:

- the generic logarithmic boundary layer;
- all forbidden Mellin residues;
- the admissible indicial residues;
- the analytic remainder germ.

The abstract inverse

\`\`\`math
A_{B,c}^{-1}
\`\`\`

and the Gram compression

\`\`\`math
\mathsf K_c
\`\`\`

do not contain this expansion.

Therefore the same missing endpoint parametrix blocks both:

- explicit computation of \(\mathbf T_c\); and
- construction of the actual persistence defect \(\mathbf D_c\).

---

## 12. Exact selected-coordinate formula that is already available

Although the endpoint coefficients are unknown, their dependence on selected
coordinates is completely normalized.

Let

\`\`\`math
U_E:
\mathbb C^r
\to
E_*^{\rm tc}
\subseteq M'
\`\`\`

be a matrix whose columns form a basis of the threshold-compatible unit-gain
space.

Then the allowed boundary matrix on this space is

\`\`\`math
\boxed{
\mathbf T_c^{(E)}
=
\mathbf B_c U_E.
}
\`\`\`

Every entry is

\`\`\`math
\boxed{
(\mathbf T_c^{(E)})_{\ell q}
=
\mathfrak a_{\beta_\ell}
\left(
D A_{B,c}^{-1}
\Phi_c^*
U_Ee_q
\right).
}
\`\`\`

So there is no remaining ambiguity about what has to be computed.

The unknown is the boundary action of the actual background resolvent.

---

## 13. Relation to the neutral-resolvent isomorphism

RPB-30 gives

\`\`\`math
J_*:
E_*
\overset{\sim}{\longrightarrow}
\ker A_{\rm full},
\qquad
J_*v
=
A_{B,c}^{-1}\Phi_c^*v.
\`\`\`

Therefore the boundary symbol may equivalently be viewed as a boundary trace
on the full neutral nullspace:

\`\`\`math
\boxed{
\mathfrak T_{\beta,c}
=
\mathfrak a_\beta D J_*.
}
\`\`\`

This shows exactly what extra structure is missing from the neutral-resolvent
isomorphism.

The isomorphism is algebraic/operator-theoretic.

It does not include a boundary trace theorem for its image.

RPB-48 therefore does not weaken RPB-30; it identifies a new boundary datum
not present there.

---

## 14. RPB-48 determination

\`\`\`math
\boxed{
\textbf{RPB-48 — THE THRESHOLD BOUNDARY MATRIX IS THE ENDPOINT MELLIN TRACE OF THE BACKGROUND RESOLVENT; BIRMAN--SCHWINGER GRAM DATA DO NOT DETERMINE IT.}
}
\`\`\`

Exact selected-column formula:

\`\`\`math
\boxed{
(\mathbf B_c)_{\ell j}
=
\mathfrak a_{\beta_\ell}
\left(
D A_{B,c}^{-1}\Phi_c^*e_j
\right).
}
\`\`\`

Exact type separation:

\`\`\`math
\boxed{
\mathsf K_c
=
\Phi_cA_{B,c}^{-1}\Phi_c^*
\quad\text{does not determine}\quad
\mathbf B_c.
}
\`\`\`

The cursor's proposed full-rank amplitude test is corrected:

\`\`\`math
\boxed{
\operatorname{rank}\mathbf T_c
\text{ is not the persistence obstruction}.
}
\`\`\`

The exact remaining object is the **background resolvent boundary symbol**

\`\`\`math
\boxed{
\mathcal B_{\beta,c}(g)
=
\mathfrak a_\beta
\left(
D A_{B,c}^{-1}g
\right).
}
\`\`\`

Next cursor:

\`\`\`text
RPB-49 / BACKGROUND RESOLVENT ENDPOINT PARAMETRIX
\`\`\`

The next pass should attack the missing boundary symbol itself:

1. write the actual background operator near \(x=c\) in endpoint coordinates;
2. separate the universal logarithmic-Laplacian boundary kernel from bounded
   prime/fixed-rank terms;
3. construct the local Mellin/Wiener--Hopf parametrix for
   \(A_{B,c}^{-1}\);
4. identify the coefficient map from analytic selected forcing to the allowed
   and forbidden endpoint channels;
5. determine whether the resulting threshold boundary-defect matrix
   \(\mathbf D_c\) has trivial kernel on the unit-gain/core space.
