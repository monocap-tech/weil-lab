# SZ-KERNEL-EDGE-QA-2 — Finite local-moment and collar-sample separation

**Date:** 2026-09-26  
**Branch:** sz-cross-collar  
**Status:** UNRATIFIED RESIDUE / NF PASS  
**Canonical parent:** SZ-CROSS-COLLAR-3  
**Immediate parent residue:** SZ_KERNEL_EDGE_QA_1_20260926.md  
**Uses:** finite-dimensional kernel reduction, stabilized persistence/flatness
filtrations, screw-transform finite singular-germ localization.

## 0. Objective

The previous screw-transform pass localized every possible flat-but-leaking
regular kernel mode to the finite arithmetic singular set

~~~math
\Sigma_c
=
\{\pm c\}
\cup
\{
c-\log n,\,
-c+\log n:
n=p^m,\ 0<\log n<2c
\}.
~~~

The present question is whether the first-kind equation forces a canonical
nonzero trace or finite local moment at one of those sites.

No such canonical trace follows from the current regularity.

What does follow is an exact finite-dimensional separation theorem:

> if a superflat leaking edge-defect space exists, it is detected by finitely
> many local \(L^2\) moments supported arbitrarily close to \(\Sigma_c\).

Equivalently, it is also detected by finitely many arbitrarily small collar
samples of the screw-potential residual.

---

## 1. Edge-defect representative space

Recall

~~~math
K_c:=\ker G_c,
~~~

the stabilized persistence subspace

~~~math
P_c^+\subseteq K_c,
~~~

and the stabilized superflat subspace

~~~math
F_\infty\subseteq K_c.
~~~

The finite-dimensional obstruction is

~~~math
\mathcal E_c
=
F_\infty/P_c^+.
~~~

Choose an algebraic/Hilbert complement

~~~math
\boxed{
F_\infty
=
P_c^+
\oplus
E_c,
}
~~~

so that

~~~math
E_c
\simeq
\mathcal E_c.
~~~

Set

~~~math
d:=\dim E_c.
~~~

If \(d=0\), kernel endpoint quasi-analyticity already holds.

The rest of the pass assumes

~~~math
d>0.
~~~

---

## 2. Shrinking singular neighborhoods

For \(r>0\), define

~~~math
U_r
:=
(-c,c)
\cap
\bigcup_{x\in\Sigma_c}
(x-r,x+r).
~~~

Let

~~~math
R_r:
E_c\to L^2(U_r)
~~~

be restriction.

If

~~~math
0<r_1<r_2,
~~~

then

~~~math
\ker R_{r_2}
\subseteq
\ker R_{r_1}.
~~~

Thus, as \(r\downarrow0\), the kernels form an increasing family of subspaces
of the finite-dimensional space \(E_c\).

Define the germ-zero subspace

~~~math
Z_\Sigma
:=
\bigcup_{r>0}\ker R_r.
~~~

A vector belongs to \(Z_\Sigma\) exactly when it vanishes a.e. on some
neighborhood of every point of \(\Sigma_c\).

---

## 3. The screw-transform localization kills the germ-zero defect

Every vector in \(E_c\) is superflat by construction.

The previous screw-transform theorem says:

~~~math
\text{superflat}
+
\text{vanishing near all of }\Sigma_c
\Longrightarrow
\text{collar persistence}.
~~~

Therefore, for

~~~math
u\in E_c\cap Z_\Sigma,
~~~

we obtain

~~~math
u\in P_c^+.
~~~

But

~~~math
E_c\cap P_c^+=\{0\}.
~~~

Hence

~~~math
\boxed{
E_c\cap Z_\Sigma
=
\{0\}.
}
~~~

So no nonzero edge-defect class can vanish on neighborhoods of all singular
sites.

---

## 4. Restriction becomes injective on one fixed arbitrarily small neighborhood

The increasing family

~~~math
\ker R_r
\qquad
(r\downarrow0)
~~~

lies in the finite-dimensional space \(E_c\).

Therefore it stabilizes for sufficiently small \(r\).

Its stabilized value is precisely

~~~math
E_c\cap Z_\Sigma
=
\{0\}.
~~~

Consequently there exists

~~~math
r_*>0
~~~

such that

~~~math
\boxed{
R_r:E_c\to L^2(U_r)
\text{ is injective}
\qquad
(0<r<r_*).
}
~~~

In particular, the entire edge-defect space is already visible inside
arbitrarily small fixed neighborhoods of the finite singular set.

---

## 5. Fixed-radius quantitative local-mass bound

Fix any

~~~math
0<r<r_*.
~~~

Because \(E_c\) is finite dimensional and \(R_r\) is injective, the unit sphere
of \(E_c\) is compact and

~~~math
u\longmapsto
\|R_ru\|_{L^2(U_r)}
~~~

is continuous and strictly positive there.

Hence

~~~math
\boxed{
\exists\,\eta_r>0:
\qquad
\|u\|_{L^2(U_r)}
\ge
\eta_r\|u\|_{L^2(-c,c)}
\qquad
(u\in E_c).
}
~~~

This is a genuine finite-dimensional localization estimate.

However,

~~~math
\eta_r
~~~

may tend to zero arbitrarily rapidly as

~~~math
r\downarrow0.
~~~

Therefore this does not create a power-law collar jet.

---

## 6. Finitely many local \(L^2\) moments separate the edge-defect space

Again fix

~~~math
0<r<r_*.
~~~

The image

~~~math
R_r(E_c)
\subset L^2(U_r)
~~~

is a \(d\)-dimensional subspace.

Choose a basis

~~~math
u_1,\ldots,u_d
~~~

of \(E_c\).

Because \(R_r\) is injective,

~~~math
R_ru_1,\ldots,R_ru_d
~~~

are linearly independent in \(L^2(U_r)\).

Hence there exist

~~~math
\phi_1,\ldots,\phi_d
\in L^2(U_r)
~~~

such that the moment matrix

~~~math
\boxed{
M_r
=
\left(
\langle
R_ru_i,
\phi_j
\rangle_{L^2(U_r)}
\right)_{i,j=1}^{d}
}
~~~

is invertible.

Extending each \(\phi_j\) by zero gives test functions supported entirely in
the \(r\)-neighborhood of \(\Sigma_c\).

Therefore the finite local-moment map

~~~math
\boxed{
\mathcal M_r:
E_c\to\mathbb C^d,
\qquad
\mathcal M_r(u)
=
\left(
\int_{U_r}
u(x)\overline{\phi_j(x)}\,dx
\right)_{j=1}^{d}
}
~~~

is an isomorphism onto its image.

So:

~~~math
\boxed{
\text{every nonzero flat leaking class is detected by finitely many
local }L^2\text{ moments arbitrarily close to }\Sigma_c.
}
~~~

No pointwise trace is needed.

---

## 7. No canonical trace follows

The separating functions

~~~math
\phi_j
~~~

depend on

- the actual finite-dimensional edge-defect space \(E_c\);
- the chosen radius \(r\);
- the chosen basis.

They are not canonical point evaluations.

Thus the theorem does **not** imply

~~~math
u(x_0)\ne0
~~~

for some

~~~math
x_0\in\Sigma_c,
~~~

nor does it imply a nonzero Lebesgue trace.

A one-dimensional edge-defect space could, in principle, be generated by a
smooth function flat to infinite order at each singular point but nonzero in
every neighborhood of one of them.

Finite dimensionality separates such a germ by an \(L^2\) moment, not by a
finite Taylor jet.

---

## 8. Finite collar-sample separation

There is a second, complementary finite-dimensional separation.

For \(u\in E_c\), define the two-component collar germ

~~~math
\Gamma_u(\delta)
:=
\left(
F_u(c+\delta)-m_u(c+\delta),
F_u(-c-\delta)-m_u(c+\delta)
\right),
~~~

where

~~~math
m_u(b)
=
\frac1{2b}
\int_{-b}^{b}F_u(x)\,dx.
~~~

For \(u\in E_c\setminus\{0\}\),

~~~math
\Gamma_u
~~~

cannot vanish identically on any interval

~~~math
(0,\varepsilon).
~~~

If it did, \(u\) would persist to that collar and hence belong to \(P_c^+\),
contradicting

~~~math
E_c\cap P_c^+=\{0\}.
~~~

Therefore, for every

~~~math
\varepsilon_0>0,
~~~

the family of evaluation functionals

~~~math
u\mapsto
(\Gamma_u(\delta))_+
,\qquad
u\mapsto
(\Gamma_u(\delta))_-
,
\qquad
0<\delta<\varepsilon_0,
~~~

separates points of \(E_c\).

---

## 9. Only finitely many arbitrarily small collar samples are needed

Because

~~~math
\dim E_c=d,
~~~

a finite subfamily of those evaluation functionals already separates \(E_c\).

More explicitly, one can choose at most \(d\) scalar edge evaluations

~~~math
\ell_j(u)
=
F_u(\epsilon_j(c+\delta_j))-m_u(c+\delta_j),
~~~

where

~~~math
\epsilon_j\in\{+1,-1\},
\qquad
0<\delta_j<\varepsilon_0,
~~~

such that

~~~math
\boxed{
u\longmapsto
(\ell_1(u),\ldots,\ell_d(u))
}
~~~

is injective on \(E_c\).

The proof is iterative:

1. start with \(V_0=E_c\);
2. choose \(0\ne u_1\in V_0\);
3. because \(u_1\) is nonpersistent, some edge evaluation with
   \(0<\delta_1<\varepsilon_0\) is nonzero;
4. its kernel cuts \(V_0\) to a proper subspace \(V_1\);
5. repeat until the kernel is zero.

At most \(d\) steps are required.

Thus

~~~math
\boxed{
\text{the entire flat edge-defect space is finitely certifiable at
arbitrarily small strict supports.}
}
~~~

---

## 10. Finite edge matrix

Choose a basis

~~~math
u_1,\ldots,u_d
~~~

of \(E_c\) and separating collar samples from Section 9.

Define the \(d\times d\) matrix

~~~math
\boxed{
\mathsf E_c
=
(\ell_j(u_i))_{i,j=1}^{d}.
}
~~~

Then

~~~math
\boxed{
\det\mathsf E_c\ne0.
}
~~~

Conversely, if no such full-rank finite edge matrix can be formed in an
arbitrarily small collar, then

~~~math
E_c=0,
~~~

and kernel endpoint quasi-analyticity holds.

So the abstract obstruction admits a finite linear-algebraic certificate.

The entries may be extremely small; invertibility gives no uniform asymptotic
lower bound.

---

## 11. Relation between local moments and collar samples

The screw first-difference formula gives each collar sample as

~~~math
\ell_j(u)
=
\int_0^{2c}
\left[
g(s+\delta_j)-g(s)
\right]
f_{\epsilon_j,u}(s)\,ds
-
\text{mean correction}.
~~~

By the previous singular-site decomposition, this scalar functional is a sum
of

- analytic bulk moments;
- finitely many local germ functionals near \(\Sigma_c\).

Hence the finite edge matrix can, in principle, be rewritten as a finite
matrix of local screw-kernel moments.

What is missing is a **canonical** choice whose leading asymptotics can be
read off from the first-kind equation.

---

## 12. What the first-kind equation has and has not forced

The interior equation

~~~math
G_cu=0
~~~

has forced enough global rigidity to make the flat leaking obstruction
finite-dimensional.

Combined with the screw-transform localization, it also forces every nonzero
edge-defect class to be visible arbitrarily close to the finite arithmetic
singular set.

But it has **not** forced any one of the following from the present data:

- a nonzero endpoint trace;
- a nonzero finite Taylor coefficient;
- a canonical local moment;
- a universal power/logarithmic lower jet.

So singular-germ separation succeeds only in the finite-dimensional
\(L^2\)-moment sense.

---

## 13. Result of this NF pass

If the stabilized flat edge-defect space is nonzero, then for every
sufficiently small singular neighborhood \(U_r\),

~~~math
\boxed{
R_r:E_c\to L^2(U_r)
\text{ is injective}.
}
~~~

Consequently:

~~~math
\boxed{
\text{finitely many local }L^2\text{ moments supported arbitrarily close to }
\Sigma_c
\text{ separate }E_c,
}
~~~

and independently,

~~~math
\boxed{
\text{finitely many arbitrarily small collar samples separate }E_c.
}
~~~

This gives a finite matrix certificate for the existence of a flat-but-leaking
kernel obstruction.

It does not yet force an explicit first collar jet.

---

## 14. Candidate follow-on if ratified

~~~text
SZ-KERNEL-EDGE-QA / CANONICAL EDGE MATRIX
~~~

A future NF should seek a canonical finite family of screw-kernel moments or
collar functionals—preferably derived from the interior equation itself—whose
matrix on \(\ker G_c/P_c^+\) can be related to zero-side/arithmetic data rather
than to an arbitrary chosen basis.

**No canonical cursor movement is asserted by this residue.**
