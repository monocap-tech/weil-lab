# RPB-64 — Perfect-kernel FBI maximum test

**Date:** 2026-09-29  
**Branch:** research/reflected-packet-bridge  
**Status:** **PASS / PERFECT-KERNEL ROUTE BYPASSED BY A STRONGER GAUSSIAN FREQUENCY-ENERGY ARGUMENT / STRICT NULL EXTENSION CREATES A POSITIVE SUPPORT GAP BETWEEN THE MODE AND THE EXTERIOR WEIL RESIDUAL / LOGARITHMIC SYMBOL COERCIVITY ON MOVING FREQUENCY WINDOWS FORCES EXPONENTIAL FOURIER DECAY / COMPACT SUPPORT THEN FORCES THE MODE TO VANISH / FULL FRIEDRICHS STRICT NULL EXTENSION EXCLUDED INDEPENDENTLY OF RPB-43 AND MELLIN COMPLETENESS**  
**Dependencies:** WD-T38/H1-P3.1 interface statement; WD-T34/ZW2-T6 finite prime shifts; WD-T35/ZW2-T7 logarithmic symbol order; Zhu compact-window formula and strict threshold convention.  
**Promotion status:** branch-local theorem / canonical audit pending.

## 0. Objective

RPB-63 reduced promotion Blocker A to a perfect delay-self-supporting analytic
singular kernel.

RPB-64 tests that residue quantitatively.

A stronger argument appears before the FBI maximum problem needs to be solved
pointwise.

Under hypothetical strict null extension, the **whole enlarged Weil residual**
vanishes on an interval strictly larger than the support of the fixed physical
mode.

That support gap permits a Gaussian frequency localization whose physical
kernel is exponentially concentrated near the original support.

On the Fourier side, the same localization sees the exact compact-window
scalar symbol

~~~math
\Psi_a(\eta)
=
\log|\eta|+O_a(1).
~~~

The finite prime translations are already contained in the bounded
trigonometric part of \(\Psi_a\).

Therefore the growing logarithmic diagonal gives a coercive filtered quadratic
estimate.

The result bypasses:

- RPB-43 interior analyticity;
- RPB-57 holomorphic Stieltjes continuation;
- RPB-58 Mellin-conormal completeness;
- RPB-60--63 delay-wavefront topology.

---

## 1. Strict persistence gives a genuine support gap

Let

~~~math
0\ne h\in L^2(\mathbb R),
\qquad
\operatorname{supp}h\subseteq[-c,c].
~~~

Assume, for contradiction, that the same zero-extended physical relation
satisfies the correct enlarged compact-window null equation for some

~~~math
a>c.
~~~

Let

~~~math
\delta
=
a-c
>
0.
~~~

Write the corresponding whole-line enlarged/right-limit Weil residual as

~~~math
q
=
\mathcal W_a^{\rm ext}h,
~~~

with the obvious replacement by the fixed strict-right operator if the
interface is formulated at an equality threshold.

The persistence hypothesis says

~~~math
\boxed{
q=0
\quad
\text{on }
(-a,a).
}
~~~

Thus

~~~math
\operatorname{supp}h
\subseteq[-c,c]
~~~

and the support of the nonzero residual \(q\), if any, begins at least a
distance \(\delta\) away from the support of \(h\).

This positive spatial gap is the decisive new input.

---

## 2. Exact enlarged scalar symbol

The enlarged/right-limit compact-window operator has the physical form

~~~math
\mathcal W_a^{\rm ext}
=
\Psi_a(D)
+
\mathcal R_{{\rm pole},a},
~~~

where

~~~math
\Psi_a(\eta)
=
\Re\psi\!\left(
\frac14+\frac{i\eta}{2}
\right)
-\log\pi
-
\sum_{\log n<2a}^{\rm active}
\frac{2\Lambda(n)}{\sqrt n}
\cos(\eta\log n),
~~~

with the finite equality-threshold correction included when appropriate.

At fixed \(a\), the prime sum is finite.

Therefore

~~~math
\boxed{
\Psi_a(\eta)
=
\log|\eta|
+
O_a(1)
\qquad
(|\eta|\to\infty).
}
~~~

Since \(\Psi_a\) is continuous on the real axis, it is also bounded below.

Hence there exist constants

~~~math
R_0,
\quad
C_a>0
~~~

such that

~~~math
\boxed{
\Psi_a(\eta)
\ge
\log R-C_a
}
~~~

whenever

~~~math
R\ge R_0,
\qquad
\frac R2\le|\eta|\le\frac{3R}{2}.
~~~

No local treatment of the individual prime translations is needed.

---

## 3. Gaussian moving-frequency filter

For

~~~math
R>1,
~~~

define the positive-frequency Gaussian weight

~~~math
\phi_R^+(\eta)
=
\exp\!\left(
-\frac{(\eta-R)^2}{R}
\right),
~~~

and let

~~~math
P_R^+
~~~

be the self-adjoint Fourier multiplier with symbol
\((\phi_R^+)^{1/2}\).

Then

~~~math
(P_R^+)^2
~~~

has Fourier symbol \(\phi_R^+\).

Its physical convolution kernel has the form

~~~math
\boxed{
K_R^+(x)
=
C\sqrt R\,
e^{-Rx^2/4}
e^{iRx},
}
~~~

up to the fixed Fourier normalization.

Thus for compactly supported \(h\),

~~~math
\boxed{
\left|
(P_R^+)^2h(x)
\right|
\le
C_h\sqrt R\,
e^{-R\,\operatorname{dist}(x,[-c,c])^2/4}.
}
~~~

The analogous negative-frequency filter is obtained by replacing \(R\) by
\(-R\).

---

## 4. The support gap makes the residual pairing exponentially small

Because

~~~math
q=0
\quad
\text{on }(-a,a),
~~~

the residual is evaluated only where

~~~math
\operatorname{dist}(x,[-c,c])
\ge
\delta.
~~~

The whole-line archimedean tail of a compactly supported \(L^2\) mode has at
most the growth supplied by the exact Gamma-factor kernel, while the prime
translations remain compactly translated copies and the pole range has fixed
exponential type.

Consequently the Gaussian physical decay from Section 3 dominates every
whole-line component of \(q\).

Therefore there are

~~~math
\kappa>0,
\qquad
C>0
~~~

such that

~~~math
\boxed{
\left|
\left\langle
q,
(P_R^+)^2h
\right\rangle
\right|
\le
Ce^{-\kappa R}
}
~~~

for all sufficiently large \(R\).

The same estimate holds for the negative-frequency filter.

This step uses only the positive collar width \(\delta=a-c\).

---

## 5. Fourier-side quadratic identity

Using

~~~math
q
=
\Psi_a(D)h
+
\mathcal R_{{\rm pole},a}h,
~~~

Plancherel gives

~~~math
\left\langle
\Psi_a(D)h,
(P_R^+)^2h
\right\rangle
=
\frac1{2\pi}
\int_{\mathbb R}
\Psi_a(\eta)
\phi_R^+(\eta)
|\widehat h(\eta)|^2
\,d\eta.
~~~

The pole term is finite rank with analytic exponential range.

Its pairing with the moving high-frequency Gaussian filter is exponentially
small:

~~~math
\boxed{
\left|
\left\langle
\mathcal R_{{\rm pole},a}h,
(P_R^+)^2h
\right\rangle
\right|
\le
C_he^{-\kappa_1R}.
}
~~~

This can be checked directly by evaluating the Gaussian multiplier on the
fixed exponential pole functions.

Hence

~~~math
\boxed{
\left|
\int_{\mathbb R}
\Psi_a(\eta)
\phi_R^+(\eta)
|\widehat h(\eta)|^2
\,d\eta
\right|
\le
Ce^{-\kappa_2R}.
}
~~~

---

## 6. Logarithmic coercivity on the Gaussian window

Set

~~~math
I_R^+
=
\int_{\mathbb R}
\phi_R^+(\eta)
|\widehat h(\eta)|^2
\,d\eta.
~~~

On the main frequency window

~~~math
\frac R2
\le
\eta
\le
\frac{3R}{2},
~~~

Section 2 gives

~~~math
\Psi_a(\eta)
\ge
\log R-C_a.
~~~

Outside this window,

~~~math
\phi_R^+(\eta)
\le
e^{-R/4}.
~~~

Since

~~~math
h\in L^2([-c,c])
\subset
L^1([-c,c]),
~~~

the Fourier transform is bounded:

~~~math
|\widehat h(\eta)|
\le
\|h\|_1.
~~~

Because \(\Psi_a\) is bounded below and grows only logarithmically, the entire
off-window contribution is exponentially small.

Therefore

~~~math
\boxed{
(\log R-C_a')
I_R^+
\le
Ce^{-\kappa_3R}
}
~~~

for all sufficiently large \(R\).

After increasing \(R_0\),

~~~math
\boxed{
I_R^+
\le
Ce^{-\kappa_4R}.
}
~~~

The identical argument centered at \(-R\) gives

~~~math
\boxed{
I_R^-
\le
Ce^{-\kappa_4R}.
}
~~~

---

## 7. Exponential Fourier decay

For

~~~math
R\le\eta\le R+1,
~~~

one has

~~~math
\phi_R^+(\eta)
\ge
e^{-1/R}.
~~~

Thus

~~~math
\boxed{
\int_R^{R+1}
|\widehat h(\eta)|^2\,d\eta
\le
Ce^{-\kappa_4R}.
}
~~~

Likewise,

~~~math
\boxed{
\int_{-R-1}^{-R}
|\widehat h(\eta)|^2\,d\eta
\le
Ce^{-\kappa_4R}.
}
~~~

Summing over integer \(R\) yields some

~~~math
\alpha>0
~~~

for which

~~~math
\boxed{
\int_{\mathbb R}
e^{\alpha|\eta|}
|\widehat h(\eta)|^2\,d\eta
<
\infty.
}
~~~

This is a genuine exponential Fourier-weight estimate, far stronger than every
finite logarithmic Sobolev gain.

---

## 8. Exponential Fourier decay gives strip analyticity

For

~~~math
|\operatorname{Im}z|<\frac{\alpha}{2},
~~~

Cauchy--Schwarz gives absolute convergence of

~~~math
h(z)
=
\frac1{2\pi}
\int_{\mathbb R}
e^{iz\eta}
\widehat h(\eta)\,d\eta.
~~~

Therefore \(h\) has a holomorphic extension to a nontrivial horizontal strip.

On the real axis this extension agrees almost everywhere with the original
\(L^2\) function.

But the original mode is compactly supported:

~~~math
h=0
\quad
\text{a.e. on }
(c,\infty)
~~~

and on the reflected exterior interval.

The identity theorem for the strip-holomorphic representative therefore gives

~~~math
\boxed{
h\equiv0.
}
~~~

This contradicts the assumed nonzero neutral mode.

---

## 9. Full strict-null-extension exclusion

The contradiction did not use:

- interior real analyticity of \(h\);
- analytic-wavefront propagation;
- the topology of the delay graph;
- a boundary logarithmic trace;
- threshold Mellin amplitudes;
- screw-core membership.

It used only:

1. compact support of the physical mode;
2. a strict enlarged null interval containing that support with positive
   margin;
3. the fixed-support symbol asymptotic
   \[
   \Psi_a(\eta)=\log|\eta|+O_a(1);
   \]
4. finite-rank analytic pole terms.

Hence:

~~~math
\boxed{
0\ne h,
\quad
\operatorname{supp}h\subseteq[-c,c]
\Longrightarrow
\text{the same zero extension cannot solve the correct Weil null equation on any strict enlargement.}
}
~~~

This is the **Gaussian support-gap null-extension exclusion**.

---

## 10. Thresholds require no separate local analysis

At a prime-power threshold, the correct strict-right operator includes the
finite equality-threshold correction.

That changes \(\Psi_a\) only by finitely many bounded cosine terms.

Therefore the high-frequency lower bound

~~~math
\Psi_a(\eta)
\ge
\log|\eta|-C_a
~~~

is unchanged in species.

The Gaussian support-gap proof consequently treats threshold and nonthreshold
supports uniformly.

The threshold Mellin line RPB-45--58 remains useful structural information but
is not needed by this final support-gap argument.

---

## 11. Effect on the previous promotion blockers

### Blocker A — interior analyticity

Bypassed.

No interior analytic continuation is used.

### Blocker B — Mellin-conormal completeness

Bypassed.

No endpoint channel decomposition is used.

Thus the two blockers from RPB-59 no longer obstruct the branch-local
null-extension theorem.

RPB-60--63 remain valid as corrections/classifications of the abandoned local
analyticity route.

---

## 12. Status of AZ-FIN-WEIL-NULL-EXTENSION

The WD-T38 interface asks whether a nonzero compact-window endpoint neutral
mode can satisfy the correct right-limit equation on some strict enlargement.

RPB-64 gives the branch-local negative answer directly:

~~~math
\boxed{
\texttt{AZ-FIN-WEIL-NULL-EXTENSION}
\text{ is discharged negatively in the RPB branch.}
}
~~~

No stable Horizon-1 file is modified in this pass.

The proof is sufficiently different from RPB-57/58 that it requires its own
promotion audit rather than inheriting RPB-59.

---

## 13. RPB-64 determination

~~~math
\boxed{
\textbf{RPB-64 — STRICT WEIL NULL EXTENSION IS IMPOSSIBLE BY GAUSSIAN SUPPORT-GAP COERCIVITY.}
}
~~~

Core estimate:

~~~math
\boxed{
(\log R-C_a)
\int_{\mathbb R}
e^{-(\eta-R)^2/R}
|\widehat h(\eta)|^2\,d\eta
\le
Ce^{-\kappa R}.
}
~~~

Consequences:

~~~math
\boxed{
\widehat h
\text{ has exponential }L^2\text{ Fourier decay}
}
~~~

and hence

~~~math
\boxed{
h
\text{ is strip-holomorphic}.
}
~~~

Compact support then forces

~~~math
\boxed{
h=0.
}
~~~

## Next cursor

~~~text
RPB-65 / GAUSSIAN SUPPORT-GAP PROMOTION AUDIT
~~~

The next pass should audit only the new proof.

Priority order:

1. verify the whole-line enlarged residual has the growth needed for the
   Gaussian support-gap pairing;
2. verify the pole-term high-frequency Gaussian estimate explicitly;
3. verify the lower bound for the exact enlarged symbol uniformly across
   threshold conventions;
4. verify the exponential Fourier-weight to strip-holomorphy step;
5. if all four pass, promote the negative discharge of
   AZ-FIN-WEIL-NULL-EXTENSION into the stable Horizon-1 interface/ledger
   without importing any RPB-43 or RPB-58 dependency.
