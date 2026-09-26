# SZ-KERNEL-EDGE-QA-1 — Screw first-difference transform and finite singular-germ localization

**Date:** 2026-09-26  
**Branch:** sz-cross-collar  
**Status:** UNRATIFIED RESIDUE / NF PASS  
**Canonical parent:** SZ-CROSS-COLLAR-3  
**Immediate parent residue:** SZ_KERNEL_EDGE_PROP_0_20260926.md  
**Suzuki pin:** Masatoshi Suzuki, *Weil's quadratic form via the screw
function*, arXiv:2606.09096v3, especially (1.3) and §2.2.

## 0. Objective

Avoid differentiating a potentially superflat collar germ.

Instead, use Suzuki's explicit screw function directly and express the two
exterior collar germs as integral transforms of the endpoint-oriented source.

This pass shows that every possible non-quasi-analytic contribution is
localized to finitely many source germs.

---

## 1. Exact first-difference transform

Fix

~~~math
0\ne u\in\ker G_c,
\qquad
L:=2c.
~~~

Let

~~~math
F_u(x)
=
\int_{-c}^{c}
g(x-y)u(y)\,dy,
~~~

with

~~~math
F_u(x)=C_u
\qquad
(|x|<c).
~~~

For the right edge define the endpoint-oriented source

~~~math
f_+(s)
:=
u(c-s),
\qquad
0<s<L.
~~~

Then, for \(\delta>0\),

~~~math
\begin{aligned}
F_u(c+\delta)-C_u
&=
\int_0^L
g(s+\delta)f_+(s)\,ds
-
\int_0^L
g(s)f_+(s)\,ds\\
&=
\boxed{
\int_0^L
\bigl(
g(s+\delta)-g(s)
\bigr)
f_+(s)\,ds.
}
\end{aligned}
~~~

Similarly, with

~~~math
f_-(s)
:=
u(-c+s),
~~~

evenness of \(g\) gives

~~~math
\boxed{
F_u(-c-\delta)-C_u
=
\int_0^L
\bigl(
g(s+\delta)-g(s)
\bigr)
f_-(s)\,ds.
}
~~~

Thus both edge germs are produced by the same scalar first-difference
transform

~~~math
\boxed{
(\mathcal T_c f)(\delta)
:=
\int_0^L
[g(s+\delta)-g(s)]f(s)\,ds.
}
~~~

No derivative of the collar residual appears.

---

## 2. Positive-axis decomposition of Suzuki's screw function

For \(t>0\), Suzuki's explicit formula (1.3) has the structure

~~~math
\boxed{
g(t)
=
a_\infty(t)
+
\sum_{\log n\le t}
\frac{\Lambda(n)}{\sqrt n}
(t-\log n),
}
~~~

where \(a_\infty\) is the archimedean part.

The prime contribution is therefore exactly

~~~math
\sum_{n\ge2}
\frac{\Lambda(n)}{\sqrt n}
(t-\log n)_+.
~~~

Suzuki's §2.2 expansion gives near the origin

~~~math
a_\infty(t)
=
\frac12t\log t
+
At
+
r(t),
\qquad
r\in C^2
~~~

locally.

From the explicit exponential/Hurwitz-Lerch formula in (1.3),
\(a_\infty\) is real-analytic for every \(t>0\).

Therefore the only positive-axis nonsmooth sites of \(g\) are

~~~math
\boxed{
0
\quad\text{and}\quad
\{\log n:n=p^m\}.
}
~~~

The origin is the logarithmic archimedean edge; the positive prime-power logs
are piecewise-linear hinges.

---

## 3. Exact transform of one prime hinge

Fix one prime power \(n\) and write

~~~math
\ell:=\log n,
\qquad
a_n:=\frac{\Lambda(n)}{\sqrt n}.
~~~

For

~~~math
0<\ell<L
~~~

and

~~~math
0<\delta<\min(\ell,L-\ell),
~~~

the contribution of this hinge to \(\mathcal T_cf\) is exactly

~~~math
\boxed{
a_n
\left[
\delta
\int_\ell^L f(s)\,ds
+
\int_{\ell-\delta}^{\ell}
(s+\delta-\ell)f(s)\,ds
\right].
}
~~~

The first term is a linear analytic moment.

The second term is a local Volterra functional depending only on the germ of
\(f\) immediately to the **left** of \(s=\ell\).

With the change \(t=\ell-s\),

~~~math
\boxed{
H_{\ell,f}^{\rm loc}(\delta)
=
a_n
\int_0^\delta
(\delta-t)f(\ell-t)\,dt.
}
~~~

Thus all nonanalytic dependence contributed by an already-active prime power is
localized to one interior source germ.

---

## 4. Threshold hinge

If

~~~math
\ell=L=2c,
~~~

the endpoint hinge contributes

~~~math
\boxed{
H_{L,f}^{\rm thr}(\delta)
=
a_n
\int_{L-\delta}^{L}
(s+\delta-L)f(s)\,ds
=
a_n
\int_0^\delta
(\delta-t)f(L-t)\,dt.
}
~~~

For the right-oriented source \(f_+\),

~~~math
f_+(L-t)
=
u(-c+t).
~~~

So this is exactly the opposite-edge coupling found in the preceding
delay-system pass.

For the left-oriented source \(f_-\), the same threshold samples the right
endpoint.

No other prime power can enter a sufficiently small strict collar because the
set of prime-power logarithms is discrete.

---

## 5. Archimedean transform

Define

~~~math
A_f(\delta)
:=
\int_0^L
[a_\infty(s+\delta)-a_\infty(s)]f(s)\,ds.
~~~

If \(f\) vanishes on a neighborhood of \(s=0\), then its support is contained
in some

~~~math
[\eta,L],
\qquad
\eta>0.
~~~

On a sufficiently small \(\delta\)-interval,
\(a_\infty(s+\delta)\) is jointly real-analytic in \((s,\delta)\) on the
relevant compact set.

Dominated differentiation then gives

~~~math
\boxed{
A_f
\text{ is real-analytic in }\delta
\text{ near }0.
}
~~~

Hence the only possible nonanalytic archimedean contribution is the source
germ at the endpoint \(s=0\).

This recovers the Stieltjes obstruction without differentiating the collar
flatness.

---

## 6. Finite singular set for one edge

For fixed \(c\), define the positive-axis hinge set

~~~math
\boxed{
\mathscr S_c
:=
\{0\}
\cup
\{\log n:
n=p^m,\ 0<\log n<2c\}
\cup
\bigl(
\{2c\}
\text{ if }2c=\log n_0
\bigr).
}
~~~

This set is finite.

The transform decomposition is therefore

~~~math
\boxed{
\mathcal T_cf
=
\text{real-analytic moment part}
+
\sum_{\ell\in\mathscr S_c}
\text{local germ functional at }\ell.
}
~~~

More explicitly:

- \(s=0\): logarithmic archimedean germ;
- \(0<\ell<2c\): one local prime-hinge Volterra germ plus a linear tail
  moment;
- \(\ell=2c\): the threshold opposite-edge germ.

There are no other small-collar singular sources.

---

## 7. Physical singular sites

Translate the \(s\)-locations back to the physical source variable.

For the right edge,

~~~math
s=0
\leftrightarrow
y=c,
~~~

and

~~~math
s=\log n
\leftrightarrow
y=c-\log n.
~~~

For the left edge,

~~~math
s=0
\leftrightarrow
y=-c,
~~~

and

~~~math
s=\log n
\leftrightarrow
y=-c+\log n.
~~~

Therefore define the finite physical arithmetic edge set

~~~math
\boxed{
\Sigma_c
:=
\{ -c,c\}
\cup
\{
c-\log n,\,
-c+\log n:
n=p^m,\ 0<\log n<2c
\}.
}
~~~

At an exact threshold the opposite endpoints are already included in
\(\{-c,c\}\).

Every possible nonanalytic edge contribution is generated by the local
\(L^2\) germ of \(u\) at one of the finitely many points in \(\Sigma_c\).

---

## 8. Analytic-gap lemma

Assume

~~~math
u=0
~~~

almost everywhere on a neighborhood of every point of \(\Sigma_c\).

Then both endpoint-oriented profiles \(f_+\) and \(f_-\) vanish on
neighborhoods of every point of \(\mathscr S_c\).

Consequently:

1. every local hinge functional vanishes for sufficiently small \(\delta\);
2. the archimedean transform is real-analytic near \(\delta=0\);
3. the remaining prime tail moments contribute only analytic linear terms.

Therefore

~~~math
\boxed{
F_u(c+\delta)-C_u
\quad\text{and}\quad
F_u(-c-\delta)-C_u
}
~~~

are real-analytic functions of \(\delta\) for sufficiently small
\(\delta\ge0\).

---

## 9. Superflat analytic edge germs must vanish

Assume the analytic-gap hypothesis of Section 8 and suppose

~~~math
\Delta_{c,c+\varepsilon}(u)
=
o(\varepsilon^N)
\qquad
\forall N.
~~~

The variance-growth identity from the preceding pass gives

~~~math
\Delta(c+\varepsilon)^2
=
\int_0^\varepsilon
\left(
|F_u(c+s)-m(c+s)|^2
+
|F_u(-c-s)-m(c+s)|^2
\right)ds.
~~~

Under Section 8, both integrands are squared moduli of real-analytic germs.

If either analytic germ had first nonzero Taylor order \(k<\infty\), the
integral would have finite leading order

~~~math
\asymp
\varepsilon^{2k+1},
~~~

contradicting superflatness.

Hence both analytic germs vanish identically near \(0\).

Therefore

~~~math
\boxed{
\Delta_{c,c+\varepsilon}(u)=0
}
~~~

for all sufficiently small \(\varepsilon>0\).

So:

~~~math
\boxed{
\text{analytic gap around }\Sigma_c
+
\text{superflat collar residual}
\Longrightarrow
\text{actual collar persistence}.
}
~~~

---

## 10. Contrapositive localization of a flat-but-leaking mode

Suppose

~~~math
u\in K_c
~~~

is superflat but nonpersistent.

Then the analytic-gap hypothesis must fail.

Thus

~~~math
\boxed{
\operatorname{ess\,supp}u
\text{ meets every sufficiently small union of neighborhoods of }
\Sigma_c.
}
~~~

Equivalently, there exists at least one point

~~~math
x_0\in\Sigma_c
~~~

such that

~~~math
\boxed{
u
\text{ is not a.e. zero on any neighborhood of }x_0.
}
~~~

Therefore the finite-dimensional edge-defect space from the previous pass is
supported, in the only relevant local sense, at the finite arithmetic edge set
\(\Sigma_c\).

A superflat defect cannot be carried solely by source mass separated from all
edge/hinge sites.

---

## 11. What this does not prove

This pass does **not** prove that an actual kernel vector has a nonzero trace,
Lebesgue value, or any prescribed local asymptotic at a point of
\(\Sigma_c\).

An \(L^2\) germ may be nontrivial in every neighborhood of a point while
remaining arbitrarily flat in averaged senses.

Thus localization to \(\Sigma_c\) is weaker than a lower collar jet.

The remaining obstruction has become finite-site local regularity/rigidity,
not a global integral-transform problem.

---

## 12. Relation to the first-kind kernel equation

The old-interior equation

~~~math
G_cu=0
~~~

still couples the germs at the points of \(\Sigma_c\) to the rest of the
source.

The present transform decomposition shows exactly where a future proof must
extract additional information:

~~~math
\boxed{
\text{kernel equation}
\quad+\quad
\text{local germs at }\Sigma_c.
}
~~~

There is no need to seek quasi-analyticity of an arbitrary whole-interval
Stieltjes transform.

It suffices to show that a nonzero class in \(K_c/P_c^+\) cannot have all of
its finitely many singular germs simultaneously superflat enough to cancel the
analytic moment part.

---

## 13. Result of this NF pass

The screw-kernel transform gives the exact non-differentiated edge formula

~~~math
\boxed{
(\mathcal T_cf)(\delta)
=
\int_0^{2c}
[g(s+\delta)-g(s)]f(s)\,ds.
}
~~~

Suzuki's explicit screw function decomposes this into:

~~~math
\boxed{
\text{analytic part}
+
\text{finitely many local singular-germ functionals}.
}
~~~

The only singular source sites are

~~~math
\boxed{
\Sigma_c
=
\{\pm c\}
\cup
\{c-\log n,\,-c+\log n:
n=p^m,\ 0<\log n<2c\}.
}
~~~

At a prime-power threshold, the endpoint coupling is already represented by
the two points \(\pm c\).

If \(u\) vanishes near all of \(\Sigma_c\), superflatness forces exact collar
persistence.

Hence any flat-but-leaking kernel mode must be locally nontrivial at at least
one point of this finite arithmetic edge set.

This is the first Weil-specific quasi-analytic localization obtained from the
explicit screw transform.

---

## 14. Candidate follow-on if ratified

~~~text
SZ-KERNEL-EDGE-QA / SINGULAR-GERM SEPARATION
~~~

A future NF should use the interior equation \(G_cu=0\) to determine whether
the finitely many local \(L^2\) germs at \(\Sigma_c\) are independent, or
whether the first-kind equation forces one of them to carry a nonzero
trace/moment that produces an explicit collar jet.

**No canonical cursor movement is asserted by this residue.**
