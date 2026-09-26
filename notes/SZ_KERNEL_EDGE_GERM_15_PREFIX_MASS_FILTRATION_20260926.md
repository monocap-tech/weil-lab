# SZ-KERNEL-EDGE-GERM-15 — Prefix-mass filtration and forced linear ejection

**Date:** 2026-09-26  
**Branch:** sz-cross-collar  
**Status:** UNRATIFIED RESIDUE / NF PASS  
**Canonical parent:** SZ-CROSS-COLLAR-3  
**Immediate residue:** SZ-KERNEL-EDGE-GERM-14  
**Target tested:** PREFIX-MASS FILTRATION  
**Public promotion:** forbidden

## 0. Objective

GERM-14 proved:

- fixed-width boundary-prefix coercivity;
- but no abstract power-law lower bound as the prefix width shrinks.

The correct next use of finite dimensionality is therefore not to force a
uniform rate on every vector.

It is to split the actual finite-dimensional edge obstruction into:

1. directions whose endpoint prefix has some finite-order mass;
2. directions whose endpoint prefix is superflat to every algebraic order.

This pass constructs that filtration.

The main new theorem is:

\[
\boxed{
\text{every nonzero endpoint-superflat finite-dimensional source family
is ejected from itself at least linearly by the truncated translation.}
}
\]

Thus a superflat endpoint germ cannot remain superflatly closed under support
translation.

For the actual edge obstruction, the remaining problem is to identify where
that forced linear ejection lands:

- persistent kernel;
- nonflat kernel;
- nonkernel support-loss carrier;
- or another singular-site germ.

---

# I. Endpoint prefix-mass filtration

## 1. Canonical edge representative

Let

\[
E
=
F_\infty\cap(P_c^+)^\perp
\]

and transport it to right-edge source coordinates

\[
E_+
=
U_+E
\subset
H:=L^2(0,L),
\qquad
L=2c.
\]

Let

\[
d=\dim E_+.
\]

For

\[
0<\varepsilon<L,
\]

write

\[
R_\varepsilon f
=
f|_{(0,\varepsilon)}.
\]

---

## 2. Filtration

For each integer

\[
N\ge0,
\]

define

\[
\boxed{
E_N^+
=
\left\{
f\in E_+:
\|R_\varepsilon f\|_2
=
o(\varepsilon^N)
\text{ as }\varepsilon\downarrow0
\right\}.
}
\]

Each \(E_N^+\) is a linear subspace.

Also,

\[
\boxed{
E_{N+1}^+\subseteq E_N^+.
}
\]

Define

\[
\boxed{
E_{\rm ep}^\infty
=
\bigcap_{N\ge0}E_N^+.
}
\]

These are the obstruction directions whose physical right-endpoint
\(L^2\)-mass is superflat to every algebraic order.

---

# II. Finite stabilization

## 3. Dimension argument

The chain

\[
E_0^+
\supseteq
E_1^+
\supseteq
E_2^+
\supseteq\cdots
\]

lies in the \(d\)-dimensional space \(E_+\).

Every strict inclusion lowers dimension.

Therefore there exists

\[
\boxed{
N_+<\infty
}
\]

such that

\[
\boxed{
E_N^+
=
E_{N_+}^+
\qquad
(N\ge N_+).
}
\]

Hence

\[
\boxed{
E_{\rm ep}^\infty
=
E_{N_+}^+.
}
\]

So infinite-order endpoint-prefix flatness on the actual obstruction is
already detected by one finite, though presently unknown, filtration level.

This is the exact analogue of the canonical collar-flatness stabilization

\[
F_\infty=F_{N_c}.
\]

---

# III. Finite-order versus superflat endpoint directions

## 4. Canonical split

Using the \(L^2\) metric on \(E_+\), define

\[
\boxed{
E_{\rm ep}^{\rm fin}
=
E_+\cap(E_{\rm ep}^\infty)^\perp.
}
\]

Then

\[
\boxed{
E_+
=
E_{\rm ep}^\infty
\oplus^\perp
E_{\rm ep}^{\rm fin}.
}
\]

Every nonzero vector in

\[
E_{\rm ep}^{\rm fin}
\]

fails the \(N_+\)-flat endpoint condition:

\[
\boxed{
f\in E_{\rm ep}^{\rm fin}\setminus\{0\}
\Longrightarrow
\|R_\varepsilon f\|_2
\ne
o(\varepsilon^{N_+}).
}
\]

This is a finite-order **membership** statement.

It does not assert an all-small-\(\varepsilon\) lower bound.

---

# IV. Superflatness becomes uniform on the stabilized subspace

## 5. Operator-superflat prefix restriction

Let

\[
W
=
E_{\rm ep}^\infty.
\]

Assume

\[
r=\dim W>0.
\]

Choose a fixed basis

\[
w_1,\ldots,w_r
\]

of \(W\).

For every \(N\),

\[
\|R_\varepsilon w_j\|
=
o(\varepsilon^N)
\qquad
(j=1,\ldots,r).
\]

Finite-dimensional norm equivalence therefore gives

\[
\boxed{
\|R_\varepsilon|_W\|
=
o(\varepsilon^N)
\qquad
\forall N.
}
\]

Thus on the stabilized endpoint-superflat subspace, prefix superflatness is
uniform in operator norm.

This is stronger than vectorwise flatness.

---

# V. General compressed-shift mismatch theorem

## 6. Any finite-dimensional source family

The next argument does not use the Weil kernel equation.

Let

\[
0\ne W\subset L^2(0,L)
\]

be any finite-dimensional source family with

\[
r=\dim W.
\]

Let

\[
\Pi_W
\]

be the orthogonal projection onto \(W\).

For the truncated left shift

\[
S_\varepsilon,
\]

define the compression

\[
\boxed{
A_\varepsilon^W
=
\Pi_WS_\varepsilon|_W.
}
\]

Then

\[
\|A_\varepsilon^W\|\le1.
\]

---

## 7. Finite archimedean chart on \(W\)

The full moment family

\[
M_m(f)
=
\int_0^L
e^{-(2m+1/2)s}f(s)\,ds
\]

is injective on \(L^2(0,L)\).

Choose

\[
r
\]

indices

\[
m_1<\cdots<m_r
\]

such that

\[
\boxed{
B_W:
W\to\mathbb C^r
}
\]

given by these moments is an isomorphism.

Write

\[
\lambda_j
=
2m_j+\frac12
\]

and

\[
D_W(\varepsilon)
=
\operatorname{diag}
\left(
e^{\lambda_j\varepsilon}
\right).
\]

Define

\[
\boxed{
\mathfrak R_W(\varepsilon)
=
B_WA_\varepsilon^W
-
D_W(\varepsilon)B_W.
}
\]

---

# VI. Linear mismatch floor on every nonzero finite family

## 8. Trace proof

Exactly as in GERM-12,

\[
\operatorname{tr}
\left(
\mathfrak R_W(\varepsilon)B_W^{-1}
\right)
=
\operatorname{tr}A_\varepsilon^W
-
\sum_{j=1}^{r}
e^{\lambda_j\varepsilon}.
\]

Since

\[
\Re\operatorname{tr}A_\varepsilon^W
\le r,
\]

we obtain

\[
\boxed{
\|\mathfrak R_W(\varepsilon)\|
\ge
c_W\varepsilon
}
\]

with

\[
\boxed{
c_W
=
\frac{
\sum_{j=1}^{r}\lambda_j
}{
r\|B_W^{-1}\|
}
>0.
}
\]

Thus every nonzero finite-dimensional compact source family has a
first-order truncated-translation/moment mismatch.

---

# VII. Exact source decomposition of the mismatch

## 9. Prefix plus ejection

Let

\[
Q_W=I-\Pi_W.
\]

The exact GERM-10 calculation applies verbatim:

\[
\boxed{
\mathfrak R_W(\varepsilon)
=
-D_W(\varepsilon)\mathcal J_{\varepsilon,W}
-
B_WQ_WS_\varepsilon|_W,
}
\]

where

\[
\mathcal J_{\varepsilon,W}f
=
\left(
\int_0^\varepsilon
e^{-\lambda_j s}f(s)\,ds
\right)_{j=1}^{r}.
\]

The prefix moments satisfy

\[
\boxed{
\|\mathcal J_{\varepsilon,W}f\|
\lesssim_W
\varepsilon^{1/2}
\|R_\varepsilon f\|_2.
}
\]

---

# VIII. Forced linear ejection of an endpoint-superflat family

## 10. Apply to \(W=E_{\rm ep}^\infty\)

On

\[
W=E_{\rm ep}^\infty,
\]

Section IV gives

\[
\|R_\varepsilon|_W\|
=
o(\varepsilon^N)
\qquad
\forall N.
\]

Therefore

\[
\boxed{
\|\mathcal J_{\varepsilon,W}\|
=
o(\varepsilon^N)
\qquad
\forall N.
}
\]

The finite diagonal family

\[
D_W(\varepsilon)
\]

remains bounded as

\[
\varepsilon\downarrow0.
\]

Hence the prefix term in the mismatch is superflat:

\[
\boxed{
\|D_W(\varepsilon)\mathcal J_{\varepsilon,W}\|
=
o(\varepsilon^N)
\qquad
\forall N.
}
\]

But Section VI gives

\[
\|\mathfrak R_W(\varepsilon)\|
\ge
c_W\varepsilon.
\]

Therefore, for sufficiently small \(\varepsilon\),

\[
\boxed{
\|B_WQ_WS_\varepsilon|_W\|
\ge
\frac{c_W}{2}\varepsilon.
}
\]

Since

\[
B_W
\]

is bounded,

\[
\boxed{
\|Q_WS_\varepsilon|_W\|
\ge
c_W'\varepsilon
}
\]

for some

\[
c_W'>0.
\]

This proves:

\[
\boxed{
\text{endpoint-superflat finite-dimensional family}
\Longrightarrow
\text{at least linear translation ejection}.
}
\]

---

# IX. Interpretation for the Weil obstruction

## 11. Two branches

The canonical obstruction now admits a finite-dimensional endpoint
classification.

### Branch A — finite-order endpoint-visible

If

\[
f\notin E_{\rm ep}^\infty,
\]

then

\[
f
\]

has non-superflat \(L^2\) mass at the physical right endpoint, detected at the
finite filtration order \(N_+\).

### Branch B — endpoint-superflat

If

\[
0\ne f\in E_{\rm ep}^\infty,
\]

then the endpoint prefix itself is operator-superflat on the entire stabilized
subspace, but support translation ejects that subspace from itself at least
linearly:

\[
\boxed{
\|(I-\Pi_W)S_\varepsilon|_W\|
\gtrsim
\varepsilon.
}
\]

Thus endpoint invisibility is paid for by finite-order source ejection.

---

# X. Exact norm ledger

## 12. One-step identity

For

\[
f\in W
\]

we have

\[
S_\varepsilon f
=
A_\varepsilon^Wf
+
Q_WS_\varepsilon f
\]

orthogonally.

Also,

\[
\|S_\varepsilon f\|^2
=
\|f\|^2
-
\|R_\varepsilon f\|^2.
\]

Therefore

\[
\boxed{
\|f\|^2
-
\|A_\varepsilon^Wf\|^2
=
\|R_\varepsilon f\|^2
+
\|Q_WS_\varepsilon f\|^2.
}
\]

On an endpoint-superflat family, the first term is superflat.

Hence all finite-order norm loss of the compressed translation is carried by
the ejection term.

This is the norm-level version of the moment mismatch theorem.

---

# XI. Finite-step dynamic energy ledger

## 13. Iteration

Let

\[
r=\dim W.
\]

For

\[
0\le k<r,
\]

apply Section X to

\[
(A_\varepsilon^W)^kf\in W.
\]

Summing gives

\[
\boxed{
\|f\|^2
-
\|(A_\varepsilon^W)^rf\|^2
=
\sum_{k=0}^{r-1}
\left[
\|R_\varepsilon(A_\varepsilon^W)^kf\|^2
+
\|Q_WS_\varepsilon(A_\varepsilon^W)^kf\|^2
\right].
}
\]

If the right side vanished for a nonzero \(f\), then

\[
S_\varepsilon(A_\varepsilon^W)^kf
=
(A_\varepsilon^W)^{k+1}f
\]

for \(0\le k<r\).

Cayley--Hamilton would then make the cyclic span of \(f\) a nonzero
\(S_\varepsilon\)-invariant finite-dimensional subspace.

For

\[
0<\varepsilon\le\log2,
\]

GERM-8 excludes such a subspace inside the regular kernel setting.

Thus, when \(W\subset K_c\), the dynamic energy ledger is strictly positive on
every nonzero vector for every fixed admissible \(\varepsilon\).

No uniform power lower bound for that full dynamic energy is asserted.

---

# XII. Visible singular-site filtration

## 14. Prime-hinge half-germs

Let the active right-oriented hinge locations in source coordinates be

\[
\ell_1,\ldots,\ell_M.
\]

Include

\[
\ell_0=0.
\]

For each site define the right-visible local mass

\[
\boxed{
m_j(f;\varepsilon)
=
\|f\|_{L^2(\ell_j,\ell_j+\varepsilon)}.
}
\]

For

\[
N\ge0,
\]

define

\[
\boxed{
E_N^{\rm vis}
=
\left\{
f\in E_+:
m_j(f;\varepsilon)
=
o(\varepsilon^N)
\text{ for every }j=0,\ldots,M
\right\}.
}
\]

Again,

\[
E_{N+1}^{\rm vis}
\subseteq
E_N^{\rm vis},
\]

so finite dimensionality gives a stabilization index

\[
\boxed{
N_{\rm vis}<\infty
}
\]

with

\[
\boxed{
E_{\rm vis}^\infty
:=
\bigcap_NE_N^{\rm vis}
=
E_{N_{\rm vis}}^{\rm vis}.
}
\]

---

## 15. Relation to GERM-3

GERM-3 proved that exact vanishing on sufficiently small right-visible
half-collars forces

\[
f=0.
\]

That is:

\[
\boxed{
\text{exact visible-germ zero}
\Longrightarrow
f=0.
}
\]

The present filtration shows the remaining loophole precisely:

\[
\boxed{
E_{\rm vis}^\infty
}
\]

consists of vectors whose mass is nonzero in arbitrarily small visible
half-collars, when required by injectivity, but can be smaller than every
algebraic power there.

Thus the unresolved problem is no longer an unspecified local regularity
issue.

It is the possible nonzero jointly-superflat visible-germ subspace

\[
E_{\rm vis}^\infty.
\]

---

# XIII. Translate visible hinges to the endpoint

## 16. Arithmetic relocation

For a fixed active hinge

\[
\ell_j,
\]

the truncated left shift

\[
S_{\ell_j}
\]

takes the right-visible germ

\[
f|_{(\ell_j,\ell_j+\varepsilon)}
\]

to the endpoint prefix

\[
(S_{\ell_j}f)|_{(0,\varepsilon)}.
\]

Therefore:

\[
\boxed{
f\in E_{\rm vis}^\infty
\Longrightarrow
S_{\ell_j}f
\text{ has superflat endpoint-prefix mass}
}
\]

for every active visible hinge \(j\), modulo the fixed support truncation at
the far end.

So every jointly-superflat visible germ becomes an endpoint-superflat germ
after the corresponding arithmetic relocation.

The forced-linear-ejection theorem of Section VIII can therefore be applied
to each finite-dimensional relocated family

\[
S_{\ell_j}(E_{\rm vis}^\infty)
\]

after quotienting any kernel of the relocation.

Thus a nonzero jointly-superflat visible family cannot remain
superflatly closed under all of its arithmetic relocations.

---

# XIV. Result of this NF pass

The actual edge obstruction now has a finite prefix-mass filtration.

There is a finite index

\[
N_+
\]

such that

\[
\boxed{
E_{\rm ep}^\infty
=
E_{N_+}^+.
}
\]

Hence every obstruction direction is either:

1. finite-order endpoint-visible; or
2. endpoint-superflat.

For the second branch, one has the quantitative theorem

\[
\boxed{
\|(I-\Pi_W)S_\varepsilon|_W\|
\gtrsim
\varepsilon,
\qquad
W=E_{\rm ep}^\infty\ne0.
}
\]

Thus superflat endpoint mass forces finite-order translation ejection.

The same construction at all right-visible singular sites produces the
stabilized joint subspace

\[
\boxed{
E_{\rm vis}^\infty.
}
\]

This is now the terminal local-mass obstruction:

- exact visible-germ vanishing is impossible by GERM-3;
- finite-order visible mass is already detected by the filtration;
- only jointly superflat but locally nonzero visible germs remain.

---

# XV. Next traversal target

The next genuinely new target is

\[
\boxed{
\text{SZ-KERNEL-EDGE-GERM-16 / VISIBLE-GERM EJECTION GRAPH}.
}
\]

The next pass should track the forced linear ejection of

\[
E_{\rm vis}^\infty
\]

under the finite set of arithmetic relocations

\[
S_{\ell_j}.
\]

The key questions are:

1. does the ejection necessarily enter the nonflat-kernel block
   \[
   H^{\rm nf}
   \]
   at finite order;
2. can persistent and nonkernel ejection absorb every relocated
   superflat germ;
3. does the finite prime-delay graph force a dimension drop after finitely many
   relocations;
4. can the one-sided observability of GERM-3 convert repeated ejection into a
   contradiction.

A successful graph argument would eliminate

\[
E_{\rm vis}^\infty
\]

without requiring pointwise endpoint traces.

No such graph closure is proved in this pass.

---

# XVI. Cursor status

The canonical theorem cursor remains

\[
\boxed{\text{SZ-CROSS-COLLAR-3}}.
\]

This is an unratified prefix-filtration / forced-ejection result.

No public promotion and no canonical cursor movement are asserted.
