# SZ-KERNEL-EDGE-GERM-11 — Spectral mismatch and finite defect observability

**Date:** 2026-09-26  
**Branch:** sz-cross-collar  
**Status:** UNRATIFIED RESIDUE / NF PASS  
**Canonical parent:** SZ-CROSS-COLLAR-3  
**Immediate residue:** SZ-KERNEL-EDGE-GERM-10  
**Target tested:** ENDPOINT-MOMENT MATCHING  
**Public promotion:** forbidden

## 0. Objective

GERM-10 derived the exact projected endpoint-moment defect

\[
\mathfrak R_\ell
=
\mathcal M A_\ell
-
D_\ell^+\mathcal M,
\]

where

\[
A_\ell
=
\Pi S_\ell|_{E_+}
\]

is the canonical compression of the truncated shift to the orthogonal
edge-obstruction representative

\[
E_+
\simeq
\mathcal E_c,
\]

and

\[
D_\ell^+
=
\operatorname{diag}
\left(
e^{(2m+1/2)\ell}
\right)_{m\ge1}.
\]

The previous pass asked whether canonical projection can reproduce the
discarded endpoint-prefix moments.

This pass answers the finite-dimensional algebraic part sharply.

If

\[
d=\dim E_+>0,
\]

then:

1. exact endpoint-moment matching can occur in at most \(d\) nonzero
   archimedean moment rows;
2. infinitely many moment rows necessarily exhibit a nonzero matching defect;
3. the iterated defect family
   \[
   \mathfrak R_\ell,
   \mathfrak R_\ell A_\ell,
   \ldots,
   \mathfrak R_\ell A_\ell^{d-1}
   \]
   separates \(E_+\).

Thus the boundary-moment mismatch is not an accidental residue.

It is a finite-dimensional observable of every nonzero edge obstruction.

What remains is to connect the original collar superflatness to this mismatch
observable.

---

# I. Full moment map is injective on the compact source interval

## 1. Moment coordinates

Let

\[
H=L^2(0,L),
\qquad
L=2c,
\]

and define

\[
\lambda_m
=
2m+\frac12,
\qquad
m\ge1.
\]

For

\[
f\in H,
\]

set

\[
\boxed{
M_m(f)
=
\int_0^L
e^{-\lambda_m s}f(s)\,ds.
}
\]

Although GERM-2 used intervals separated from \(s=0\) for the analytic
archimedean transform, the **moment completeness** argument itself works on
the full compact interval \((0,L)\).

Indeed, with

\[
x=e^{-2s},
\]

the interval becomes

\[
J=[e^{-2L},1].
\]

Since \(J\) is bounded away from zero, the fixed Jacobian/fractional-power
weight is bounded and nonvanishing.

Therefore

\[
M_m(f)=0
\qquad
\forall m\ge m_0
\]

for any fixed \(m_0\) implies

\[
f=0.
\]

Hence

\[
\boxed{
\mathcal M:
H\to\mathbb C^{\mathbb N},
\qquad
\mathcal M f=(M_m(f))_{m\ge1},
}
\]

is injective, and every moment tail is already separating.

---

# II. Matrix form of the canonical compression

## 2. Quotient representative

Let

\[
E_+
\subset H
\]

be the right-oriented image of the canonical orthogonal representative

\[
E
=
F_\infty\cap(P_c^+)^\perp.
\]

Assume

\[
d=\dim E_+>0.
\]

Choose an orthonormal basis

\[
e_1,\ldots,e_d.
\]

Let

\[
C_\ell
\in
M_d(\mathbb C)
\]

be the matrix of

\[
A_\ell
=
\Pi S_\ell|_{E_+}
\]

in this basis.

---

## 3. Moment rows

For every \(m\ge1\), define the row vector

\[
\boxed{
B_m
=
\bigl(
M_m(e_1),
\ldots,
M_m(e_d)
\bigr).
}
\]

Collectively, the infinite matrix

\[
B
=
(B_m)_{m\ge1}
\]

represents

\[
\mathcal M|_{E_+}.
\]

Since the full moment map is injective on \(E_+\),

\[
\boxed{
\operatorname{rank}B=d
}
\]

in the algebraic sense that its rows separate the \(d\)-dimensional source
space.

---

# III. Sylvester-row form of the defect

## 4. One moment channel

The \(m\)-th row of

\[
\mathcal M A_\ell
\]

is

\[
B_m C_\ell.
\]

The \(m\)-th row of

\[
D_\ell^+\mathcal M
\]

is

\[
e^{\lambda_m\ell}B_m.
\]

Therefore the \(m\)-th defect row is exactly

\[
\boxed{
R_{\ell,m}
=
B_m
\left(
C_\ell-e^{\lambda_m\ell}I_d
\right).
}
\]

This is a Sylvester-type residual.

The endpoint-prefix/projection formula from GERM-10 is therefore equivalent,
row by row, to this finite matrix identity.

---

# IV. At most \(d\) active rows can match

## 5. Matching row implies eigenvalue

Suppose

\[
B_m\ne0
\]

and

\[
R_{\ell,m}=0.
\]

Then

\[
B_m C_\ell
=
e^{\lambda_m\ell}B_m.
\]

Thus \(B_m\) is a nonzero left eigenvector of \(C_\ell\) with eigenvalue

\[
\boxed{
e^{\lambda_m\ell}.
}
\]

For fixed

\[
\ell>0,
\]

the numbers

\[
e^{\lambda_m\ell}
\]

are pairwise distinct as \(m\) varies.

A \(d\times d\) matrix has at most \(d\) distinct eigenvalues.

Therefore:

\[
\boxed{
\#\left\{
m:
B_m\ne0,\;
R_{\ell,m}=0
\right\}
\le d.
}
\]

So exact endpoint-moment matching can occur in at most \(d\) **active**
moment channels.

---

# V. There are infinitely many active moment rows

## 6. Tail nonvanishing

Suppose only finitely many rows \(B_m\) were nonzero.

Then there would exist

\[
m_0
\]

such that

\[
B_m=0
\qquad
\forall m\ge m_0.
\]

This means

\[
M_m(f)=0
\qquad
\forall f\in E_+,\;
m\ge m_0.
\]

By tail completeness of the moment system,

\[
f=0
\]

for every \(f\in E_+\).

Hence

\[
E_+=0,
\]

contradicting \(d>0\).

Therefore:

\[
\boxed{
d>0
\Longrightarrow
B_m\ne0
\text{ for infinitely many }m.
}
\]

Combined with Section IV:

\[
\boxed{
d>0
\Longrightarrow
R_{\ell,m}\ne0
\text{ for infinitely many }m.
}
\]

Thus a nonzero edge obstruction necessarily fails endpoint-moment matching in
infinitely many archimedean channels for every fixed \(\ell>0\).

---

# VI. A finite matching bound

## 7. \(d+1\)-channel criterion

Take any \(d+1\) distinct indices

\[
m_1,\ldots,m_{d+1}
\]

such that

\[
B_{m_j}\ne0.
\]

It is impossible that

\[
R_{\ell,m_j}=0
\qquad
(j=1,\ldots,d+1).
\]

Hence:

\[
\boxed{
\text{among any }d+1\text{ active moment channels, at least one has
nonzero endpoint-matching defect.}
}
\]

This is a finite spectral obstruction.

It uses no endpoint trace, no Sobolev regularity, and no quasi-analyticity.

---

# VII. Dynamic defect observability

## 8. Statement

Define

\[
R
=
\mathfrak R_\ell
=
\mathcal M A_\ell-D_\ell^+\mathcal M.
\]

Let

\[
d=\dim E_+.
\]

Then

\[
\boxed{
\bigcap_{k=0}^{d-1}
\ker(RA_\ell^k)
=
\{0\}.
}
\]

Equivalently, the map

\[
\boxed{
\mathcal O_\ell^{\rm def}:
E_+
\to
(\mathbb C^{\mathbb N})^d,
\qquad
f\mapsto
\left(
Rf,\,
RA_\ell f,\,
\ldots,\,
RA_\ell^{d-1}f
\right)
}
\]

is injective.

---

## 9. Proof: extend vanishing to all iterates

Assume

\[
RA_\ell^k f=0
\qquad
k=0,\ldots,d-1.
\]

Let

\[
p(z)
=
z^d+c_{d-1}z^{d-1}+\cdots+c_0
\]

be the characteristic polynomial of \(A_\ell\).

By Cayley--Hamilton,

\[
p(A_\ell)=0.
\]

Therefore

\[
A_\ell^d
=
-\sum_{j=0}^{d-1}
c_jA_\ell^j.
\]

Applying \(R\) to \(A_\ell^d f\) gives

\[
RA_\ell^d f=0.
\]

Repeating the same recurrence shows

\[
\boxed{
RA_\ell^k f=0
\qquad
\forall k\ge0.
}
\]

---

## 10. Exact diagonal evolution of moments

Since

\[
R
=
\mathcal M A_\ell-D_\ell^+\mathcal M,
\]

the identities

\[
RA_\ell^k f=0
\]

give

\[
\mathcal M A_\ell^{k+1}f
=
D_\ell^+\mathcal M A_\ell^kf.
\]

Inductively,

\[
\boxed{
\mathcal M A_\ell^k f
=
(D_\ell^+)^k\mathcal M f
\qquad
\forall k\ge0.
}
\]

---

## 11. Cayley--Hamilton on the moment side

Apply \(\mathcal M\) to

\[
p(A_\ell)f=0.
\]

Using the exact diagonal evolution,

\[
\boxed{
p(D_\ell^+)\mathcal M f=0.
}
\]

Coordinatewise,

\[
\boxed{
p(e^{\lambda_m\ell})M_m(f)=0
\qquad
\forall m\ge1.
}
\]

The numbers

\[
e^{\lambda_m\ell}
\]

are pairwise distinct.

The degree-\(d\) polynomial \(p\) has at most \(d\) roots.

Therefore

\[
M_m(f)=0
\]

for all but at most \(d\) indices \(m\).

In particular, the moment tail vanishes.

Tail completeness gives

\[
f=0.
\]

Thus

\[
\boxed{
\bigcap_{k=0}^{d-1}
\ker(RA_\ell^k)=\{0\}.
}
\]

---

# VIII. Finite scalar defect certificate

## 12. Reduction from sequence outputs

The dynamic defect map

\[
\mathcal O_\ell^{\rm def}
\]

takes values in an infinite product of scalar moment channels.

Its kernel is zero.

Because the domain \(E_+\) is finite dimensional, finitely many scalar
coordinates among

\[
\left\{
\left(RA_\ell^k f\right)_m:
0\le k<d,\;
m\ge1
\right\}
\]

already separate \(E_+\).

Thus there exist finitely many pairs

\[
(k_j,m_j),
\qquad
0\le k_j<d,
\]

such that

\[
\boxed{
f\longmapsto
\left(
(RA_\ell^{k_j}f)_{m_j}
\right)_j
}
\]

is injective on \(E_+\).

One may choose at most \(d\) scalar functionals after extracting a basis of
the dual span.

This gives a finite dynamic mismatch matrix for every nonzero obstruction.

The choice of scalar coordinates is not canonical; the full operator family
\(\{RA_\ell^k\}_{k<d}\) is canonical once the Hilbert quotient representative
and orientation are fixed.

---

# IX. Relation to the endpoint-prefix formula

## 13. Explicit mismatch at each iterate

GERM-10 gives

\[
R
=
-D_\ell^+\mathcal J_\ell
-
\mathcal M Q S_\ell.
\]

Therefore

\[
RA_\ell^k
=
-D_\ell^+\mathcal J_\ell A_\ell^k
-
\mathcal M Q S_\ell A_\ell^k.
\]

The observability theorem says that for every nonzero

\[
f\in E_+,
\]

there exists

\[
0\le k<d
\]

such that

\[
\boxed{
D_\ell^+\mathcal J_\ell A_\ell^k f
+
\mathcal M Q S_\ell A_\ell^k f
\ne0.
}
\]

So canonical projection cannot reproduce the discarded endpoint-prefix
moments along the entire finite compressed orbit of any nonzero obstruction.

That is the exact endpoint-moment matching theorem obtained in this pass.

---

# X. What this does and does not close

## 14. What is now impossible

For a nonzero obstruction \(E_+\):

- exact matching cannot hold in all active moment rows;
- exact matching cannot hold in more than \(d\) active rows at one step;
- exact matching cannot hold along the first \(d\) compressed iterates of any
  nonzero vector.

Thus the endpoint-prefix defect is dynamically unavoidable.

---

## 15. What is still missing

The original flat obstruction is defined by the collar residual

\[
\Gamma_u(\delta)
\]

being superflat as

\[
\delta\downarrow0.
\]

The present defect

\[
\mathfrak R_\ell
\]

is a fixed-width source/moment mismatch at translation scale \(\ell\).

No theorem yet shows that collar superflatness forces

\[
\mathfrak R_\ell
\]

or its first \(d\) compressed iterates to vanish.

Therefore the new observability theorem does not by itself prove

\[
\mathcal E_c=0.
\]

It identifies the precise contradiction that a future
**superflat-to-defect transfer** theorem would need to create.

---

# XI. Result of this NF pass

Endpoint-moment matching is now spectrally constrained.

In a \(d\)-dimensional edge obstruction:

\[
\boxed{
R_{\ell,m}
=
B_m
(C_\ell-e^{\lambda_m\ell}I_d).
}
\]

Hence:

\[
\boxed{
\text{at most }d\text{ active moment rows can match exactly};
}
\]

\[
\boxed{
\text{infinitely many moment rows must mismatch if }d>0;
}
\]

and

\[
\boxed{
\bigcap_{k=0}^{d-1}
\ker(\mathfrak R_\ell A_\ell^k)
=
\{0\}.
}
\]

So the boundary/projection defect is a canonical finite-dimensional
observable of every nonzero obstruction.

The remaining question is no longer whether mismatch exists.

It is whether the original all-orders collar flatness can coexist with this
forced finite mismatch.

---

# XII. Next traversal target

The next genuinely new target is

\[
\boxed{
\text{SZ-KERNEL-EDGE-GERM-12 / SUPERFLAT-TO-DEFECT TRANSFER}.
}
\]

The next pass should test whether

\[
u\in F_\infty
\]

forces any vanishing or superflat estimate on:

\[
\mathfrak R_\ell u,
\qquad
\mathfrak R_\ell A_\ell u,
\qquad
\ldots,
\qquad
\mathfrak R_\ell A_\ell^{d-1}u.
\]

Promising interfaces are:

1. let the translation width \(\ell\downarrow0\) and compare the prefix moments
   with the collar observation;
2. use the centered second-difference identity to relate endpoint-prefix
   moments to exterior leakage;
3. test whether the canonical Gramian superflatness controls the compressed
   shift defect;
4. or construct a countermodel showing that source-prefix mismatch can remain
   large while collar leakage is superflat.

A positive transfer theorem would contradict the dynamic observability result
above and force

\[
\mathcal E_c=0.
\]

No such transfer is proved in this pass.

---

# XIII. Cursor status

The canonical theorem cursor remains

\[
\boxed{\text{SZ-CROSS-COLLAR-3}}.
\]

This is an unratified endpoint-matching / observability result.

No public promotion and no canonical cursor movement are asserted.
