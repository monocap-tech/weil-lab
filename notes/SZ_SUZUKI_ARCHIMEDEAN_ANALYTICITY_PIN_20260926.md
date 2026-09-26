# SZ-SUZUKI-ARCHIMEDEAN-ANALYTICITY-PIN — C5 source normalization

**Date:** 2026-09-26  
**Branch:** sz-cross-collar  
**Status:** SOURCE-PINNED DERIVED AUXILIARY  
**Canonical parent:** SZ-CROSS-COLLAR-3  
**Purpose:** discharge audit item C5  
**External source:** Masatoshi Suzuki, *Weil's quadratic form via the screw
function*, arXiv:2606.09096v3, equation (1.3) and §2.2, equation (2.2)  
**Traversal movement:** none

## 0. Objective

The post-SZ-3 audit left one source-normalization gate for the screw
first-difference localization:

> pin the exact source statement from which the non-prime component of
> Suzuki's screw function is real-analytic on compact subsets of
> \((0,\infty)\).

Suzuki does not need to state this as a named theorem.

It follows directly from his explicit formula (1.3).

This note records the derivation and its exact scope.

---

## 1. Suzuki's explicit screw function

Suzuki defines the continuous real-valued even screw function \(g\) by

\[
\begin{aligned}
g(t)
={}&
-4\left(e^{|t|/2}+e^{-|t|/2}-2\right)
\\
&+
\sum_{n\le e^{|t|}}
\frac{\Lambda(n)}{\sqrt n}
\left(|t|-\log n\right)
\\
&-
\frac{|t|}{2}
\left(
\psi(1/4)-\log\pi
\right)
\\
&-
\frac14
\left[
\Phi(1,2,1/4)
-
e^{-|t|/2}
\Phi(e^{-2|t|},2,1/4)
\right].
\end{aligned}
\]

This is equation (1.3) of arXiv:2606.09096v3.

For \(t>0\), define the non-prime component

\[
\boxed{
a_\infty(t)
:=
-4\left(e^{t/2}+e^{-t/2}-2\right)
-
\frac t2
\left(
\psi(1/4)-\log\pi
\right)
-
\frac14
\left[
\Phi(1,2,1/4)
-
e^{-t/2}
\Phi(e^{-2t},2,1/4)
\right].
}
\]

Then

\[
\boxed{
g(t)
=
a_\infty(t)
+
\sum_{n\le e^t}
\frac{\Lambda(n)}{\sqrt n}
(t-\log n),
\qquad t>0.
}
\]

Equivalently,

\[
\boxed{
g(t)
=
a_\infty(t)
+
\sum_{n\ge2}
\frac{\Lambda(n)}{\sqrt n}
(t-\log n)_+.
}
\]

Only prime powers contribute because \(\Lambda(n)=0\) otherwise.

---

## 2. Analyticity of the Hurwitz-Lerch factor

Suzuki uses

\[
\Phi(z,2,1/4)
=
\sum_{m=0}^{\infty}
\frac{z^m}{(m+1/4)^2}.
\]

For every

\[
t>0,
\]

we have

\[
0<e^{-2t}<1.
\]

The defining series for

\[
z\longmapsto \Phi(z,2,1/4)
\]

therefore converges absolutely and locally uniformly on the open unit disk

\[
|z|<1.
\]

Consequently it is holomorphic there.

Since

\[
t\longmapsto e^{-2t}
\]

and

\[
t\longmapsto e^{-t/2}
\]

are real-analytic on \(\mathbb R\), the composition

\[
\boxed{
t
\longmapsto
e^{-t/2}
\Phi(e^{-2t},2,1/4)
}
\]

is real-analytic for every

\[
t>0.
\]

The remaining terms in \(a_\infty(t)\) are exponentials, constants, and a
linear function of \(t\).

Therefore

\[
\boxed{
a_\infty\in C^\omega((0,\infty)).
}
\]

In particular, for every compact interval

\[
I\Subset(0,\infty),
\]

\(a_\infty\) is real-analytic on an open neighborhood of \(I\).

---

## 3. The origin is excluded

The statement above deliberately excludes

\[
t=0.
\]

Suzuki §2.2 derives the local expansion

\[
\boxed{
g(t)
=
\frac12|t|\log|t|
+
A|t|
+
\sum_{n\le e^{|t|}}
\frac{\Lambda(n)}{\sqrt n}
(|t|-\log n)
+
r(t),
}
\]

where \(r\) is even and \(C^2\) near the origin.

This is equation (2.2).

For sufficiently small \(|t|\), the prime sum vanishes, so the leading
non-smooth behavior at the origin is

\[
\boxed{
\frac12|t|\log|t|.
}
\]

Thus the correct regularity split is

\[
\boxed{
a_\infty\in C^\omega((0,\infty)),
\qquad
g(t)\text{ has a logarithmic singular jet at }t=0.
}
\]

No claim of analyticity through the origin is made.

---

## 4. Prime-power singular sites

For \(t>0\), the arithmetic contribution is

\[
g_{\rm prime}(t)
=
\sum_{n\ge2}
\frac{\Lambda(n)}{\sqrt n}
(t-\log n)_+.
\]

Each summand is

- zero for \(t<\log n\);
- linear for \(t>\log n\);
- continuous with a derivative jump at \(t=\log n\).

Therefore the only positive-axis nonanalytic sites outside the origin are

\[
\boxed{
\{\log n:\Lambda(n)\ne0\}
=
\{\log p^m:p\text{ prime},\ m\ge1\}.
}
\]

On any compact interval

\[
[0,L],
\]

there are only finitely many such sites.

Thus

\[
\boxed{
g
\text{ is real-analytic on every connected component of }
(0,\infty)\setminus
\{\log p^m\}.
}
\]

---

## 5. Consequence for the screw first-difference transform

For

\[
(\mathcal T_cf)(\delta)
=
\int_0^{2c}
[g(s+\delta)-g(s)]f(s)\,ds,
\]

suppose the support of \(f\) is separated by positive distance from

\[
0
\quad\text{and}\quad
\{\log p^m:0<\log p^m\le2c\}.
\]

Then, after choosing \(\delta\) sufficiently small, both \(s\) and
\(s+\delta\) remain in compact subsets of the same analytic components of
\(g\).

The map

\[
(s,\delta)
\longmapsto
g(s+\delta)-g(s)
\]

is therefore jointly real-analytic on the relevant compact support
neighborhood.

Termwise/dominated differentiation in \(\delta\) gives

\[
\boxed{
\mathcal T_cf
\in C^\omega
}
\]

for \(\delta\) in a sufficiently small neighborhood of \(0\).

Hence the analytic-gap step used in
SZ-KERNEL-EDGE-QA-1 is source-supported once the local prime-hinge terms are
separated explicitly.

---

## 6. Threshold case

If

\[
2c=\log n_0
\]

for a prime power \(n_0\), the corresponding hinge is exactly at the far
endpoint \(s=2c\).

Its first-difference contribution is not part of the analytic bulk.

It is the explicit local Volterra term

\[
\boxed{
\frac{\Lambda(n_0)}{\sqrt{n_0}}
\int_{2c-\delta}^{2c}
(s+\delta-2c)f(s)\,ds.
}
\]

For the right-oriented source

\[
f_+(s)=u(c-s),
\]

this is the opposite-edge germ

\[
u(-c+t).
\]

Thus the source pin is fully consistent with the threshold two-edge geometry
already isolated in SZ-KERNEL-EDGE-PROP-0.

---

## 7. Exact source status

The external statements consumed are:

1. Suzuki equation (1.3): explicit global formula for \(g\);
2. Suzuki definition of the Hurwitz-Lerch function by its convergent power
   series;
3. Suzuki §2.2 / equation (2.2): the logarithmic origin expansion.

The conclusion

\[
\boxed{
a_\infty\in C^\omega((0,\infty))
}
\]

is a project derivation from those displayed formulas.

Therefore its correct label is

\[
\boxed{
\text{SOURCE-PINNED DERIVED},
}
\]

not “quoted theorem of Suzuki.”

---

## 8. Audit determination

Audit item C5 is discharged.

The statement needed by the screw-transform localization is now pinned:

\[
\boxed{
\text{outside }0\text{ and the prime-power hinges, Suzuki's screw kernel is
real-analytic.}
}
\]

Accordingly, the source-normalization gate identified for
SZ-KERNEL-EDGE-QA-1 is closed.

This does **not** by itself ratify QA-1; its remaining proof steps still belong
to the later residue audit.

After C5, the remaining post-SZ-3 audit obligations are:

- C2 — parity/reality-sector scope of same-source surjectivity;
- C3 — compact-collar uniformity of \(\sigma_b\) and \(G_b\);
- C4 — keep the superflat Stieltjes construction non-load-bearing unless its
  jump representation is expanded or source-pinned.

**No canonical cursor movement is asserted by this source-normalization pass.**
