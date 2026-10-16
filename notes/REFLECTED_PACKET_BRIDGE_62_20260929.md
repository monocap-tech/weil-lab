# RPB-62 — Infinite-log delay-cycle extinction test

**Date:** 2026-09-29  
**Branch:** research/reflected-packet-bridge  
**Status:** **PASS FOR FINITE COMPONENTS / FINITE SELF-SUPPORTING DELAY CYCLES ARE ANALYTICALLY ELLIPTIC AFTER RECENTERING AND CANNOT CARRY ANALYTIC WAVEFRONT / INFINITE-LOG FINITE-CYCLE RESIDUE ELIMINATED / ONLY INFINITE OR ACCUMULATING DELAY COMPONENTS REMAIN FOR BLOCKER A**  
**Dependencies:** RPB-60, RPB-61; digamma high-frequency asymptotics; analytic pseudodifferential parametrix for the recentered finite matrix system.  
**Promotion status:** none.

## 0. Objective

RPB-61 showed that wavefront-set geometry alone permits finite closed witness
cycles and that scalar iteration only visibly yields

~~~math
\bigcap_{N\ge0}H_{\log}^N.
~~~

RPB-62 asks whether the **actual coupled high-frequency equations** on a finite
self-supporting component are stronger than this scalar iteration.

They are.

Once a finite component is isolated and all of its points are recentered to one
common local coordinate, the internal prime translations cease to be
off-diagonal FIOs between different spatial charts.

They become a finite constant matrix coupling.

The resulting matrix logarithmic operator has an analytic high-frequency
parametrix, so no finite component can carry analytic wavefront.

---

## 1. Finite isolated delay component

Let

~~~math
\mathcal C
=
\{x_1,\dots,x_N\}
\subset(-c,c)
~~~

be a finite component of the projected analytic singular support under the
active-delay witness graph.

Assume the component is isolated in the following local sense.

Choose a small radius \(\rho>0\) such that the intervals

~~~math
I_j
=
(x_j-\rho,x_j+\rho)
~~~

are pairwise disjoint, contained in \((-c,c)\), and satisfy:

- if
  \[
  x_j+\sigma\ell_\nu=x_k
  \]
  for two points of \(\mathcal C\), then
  \[
  I_j+\sigma\ell_\nu=I_k;
  \]
- every translated interval not landing on another \(I_k\) lies in an
  analytic region of \(h\).

Such a choice is possible precisely because \(\mathcal C\) is finite and
isolated from the rest of the projected analytic singular set.

---

## 2. Recenter all component germs

For

~~~math
|s|<\rho,
~~~

define

~~~math
U_j(s)
=
h(x_j+s).
~~~

Collect them into

~~~math
U(s)
=
\begin{pmatrix}
U_1(s)\\
\vdots\\
U_N(s)
\end{pmatrix}.
~~~

If a delay edge connects

~~~math
x_j+\sigma\ell_\nu=x_k,
~~~

then

~~~math
h(x_j+s+\sigma\ell_\nu)
=
h(x_k+s)
=
U_k(s).
~~~

Thus every translation internal to the finite component becomes a **local
zeroth-order matrix coupling** in the common coordinate \(s\).

No oscillatory phase remains after recentering.

---

## 3. External translated germs become analytic forcing

Consider a translated sample from \(I_j\) which does not land in another
component interval \(I_k\).

By the choice of \(\rho\), that translated interval lies in an analytic region
of \(h\).

Therefore every such term contributes a real-analytic function of \(s\).

The pole/evaluation range is analytic as before.

The only potentially nonanalytic unknowns remaining in the localized system
are the \(N\) recentered component germs themselves.

---

## 4. The archimedean operator has the same diagonal singular part in every chart

The archimedean operator is translation invariant.

Near each \(x_j\), split its kernel into:

1. a near-diagonal logarithmic singular part acting on \(U_j\);
2. a far part with separation bounded away from zero.

After shrinking \(\rho\), the far kernel is analytic jointly in the local
coordinate and the source coordinate.

Since \(h\in L^2\subset L^1\) on the fixed compact support, the far part gives
an analytic forcing germ.

Thus every component equation has the same local diagonal operator

~~~math
\mathcal A_{\infty,\rm loc}
~~~

acting on \(U_j\), modulo analytic forcing.

---

## 5. Finite matrix system

Let \(M\) be the constant \(N\times N\) matrix whose entry \(M_{jk}\) is the
sum of the prime coefficients of all active delay edges sending the \(k\)-th
component germ into the \(j\)-th equation, with the fixed sign convention of
the Weil operator.

Then the localized system is

~~~math
\boxed{
\left(
\mathcal A_{\infty,\rm loc}I_N
-
M
\right)U
=
G_{\rm an},
}
~~~

where

~~~math
G_{\rm an}
\in
C^\omega((-\rho,\rho);\mathbb C^N).
~~~

This is now an ordinary **matrix pseudodifferential system in one local
coordinate**.

The off-diagonal FIO character of the original translations has disappeared
because the finitely many source and target charts have been recentered
simultaneously.

---

## 6. High-frequency matrix symbol

The high-frequency symbol is

~~~math
\boxed{
P(\xi)
=
m_\infty(\xi)I_N
-
M.
}
~~~

Since

~~~math
m_\infty(\xi)
=
\log|\xi|
-
\log(2\pi)
+
O(|\xi|^{-2}),
~~~

there exists \(R\) such that, for

~~~math
|\xi|>R,
~~~

~~~math
|m_\infty(\xi)|
>
2\|M\|.
~~~

Hence

~~~math
\boxed{
P(\xi)
\text{ is invertible for }|\xi|>R
}
~~~

and

~~~math
\boxed{
\|P(\xi)^{-1}\|
\le
\frac{2}{|m_\infty(\xi)|}
=
O\!\left(
\frac1{\log|\xi|}
\right).
}
~~~

So the bounded delay matrix cannot create a high-frequency characteristic
root against the growing logarithmic diagonal.

---

## 7. The inverse is an analytic order-zero symbol

Write

~~~math
Q(\xi)
=
P(\xi)^{-1}.
~~~

For high frequency,

~~~math
Q(\xi)
=
\frac1{m_\infty(\xi)}
\left(
I_N-\frac{M}{m_\infty(\xi)}
\right)^{-1}.
~~~

The resolvent factor is a uniformly convergent finite-dimensional Neumann
series.

The digamma multiplier is analytic on the real high-frequency region and its
derivatives satisfy the standard factorial high-frequency bounds

~~~math
|\partial_\xi^k m_\infty(\xi)|
\le
C^{k+1}k!\,|\xi|^{-k}
\qquad
(k\ge1,\ |\xi|\gg1).
~~~

Differentiating the matrix resolvent therefore gives

~~~math
\boxed{
\|\partial_\xi^kQ(\xi)\|
\le
C_1^{k+1}k!\,|\xi|^{-k}
}
~~~

after increasing \(R\).

The zeroth derivative is bounded because

~~~math
Q(\xi)=O(1/\log|\xi|).
~~~

Hence \(Q\) is an analytic order-zero matrix symbol at high frequency.

After inserting a high-frequency cutoff, it defines an analytic
pseudodifferential parametrix for the finite recentered system.

---

## 8. Localization does not reintroduce a singular forcing

Choose a smooth localization equal to one on a smaller common coordinate
interval and supported inside the chart radius \(\rho\).

The commutator with the near-diagonal archimedean operator is supported where
the localization changes.

For the germ equation evaluated on the smaller interval, source points in that
commutator region are a positive distance away from the evaluation point.

Equivalently, one may perform the near/far kernel split before localizing.

In either formulation, the commutator/far contribution has an analytic kernel
on the smaller interval.

Because all noncomponent translated germs are analytic there as well, the
localized matrix forcing remains analytic.

Thus there is no hidden nonanalytic commutator term capable of sustaining the
finite component.

---

## 9. Analytic parametrix kills the finite component

Apply the analytic matrix parametrix to

~~~math
\left(
\mathcal A_{\infty,\rm loc}I_N-M
\right)U
=
G_{\rm an}.
~~~

Analytic pseudolocality gives

~~~math
\boxed{
U\in C^\omega
}
~~~

on a smaller common interval.

Therefore every \(x_j\) is analytic for \(h\).

This contradicts the assumption that

~~~math
x_j
~~~

belongs to the projected analytic singular support.

Hence:

~~~math
\boxed{
\text{no finite isolated self-supporting delay component can occur.}
}
~~~

In particular the two-point witness cycles allowed by the set-level relation
of RPB-61 are not realizable as actual analytic singular components of a Weil
null mode.

---

## 10. Correction to the RPB-61 finite-cycle residue

RPB-61 stopped finite cycles at

~~~math
\bigcap_NH_{\log}^N.
~~~

That stop was an artifact of iterating scalar regularity estimates rather than
solving the finite coupled system at once.

The matrix formulation gives the stronger result

~~~math
\boxed{
\text{finite self-supporting delay component}
\Longrightarrow
\text{analytic}
\Longrightarrow
\text{not singular}.
}
~~~

Thus the **finite infinite-log delay-cycle residue is empty**.

---

## 11. What remains: infinite or accumulating components

The finite matrix reduction requires:

- finitely many singular points in the component;
- positive separation between those points and the rest of the singular set;
- finitely many local charts that can be recentered simultaneously.

It does not apply to a singular component with infinitely many points
accumulating in the support.

With two incommensurable prime delays, RPB-37 shows that the arithmetic graph
has ample room for such infinite configurations.

RPB-61 also shows that the set-level witness relation does not force all
arithmetic translates to be present, so density alone neither constructs nor
eliminates them.

Therefore Blocker A is now reduced to

~~~math
\boxed{
\text{infinite / accumulating self-supporting delay components}.
}
~~~

---

## 12. Consequence for endpoint-collar propagation

If a future exterior argument forces \(h\) to vanish on an endpoint collar,
any remaining analytic singular set must lie in the interior.

RPB-62 now rules out every finite isolated singular component there.

However an infinite accumulating component could remain, and without a
separate unique-continuation or compactness argument one cannot yet infer

~~~math
h\equiv0.
~~~

Thus RPB-57 is still not promotion-ready.

---

## 13. RPB-62 determination

~~~math
\boxed{
\textbf{RPB-62 — FINITE DELAY CYCLES DIE AFTER RECENTERING; ONLY INFINITE OR ACCUMULATING DELAY COMPONENTS REMAIN.}
}
~~~

Refined blocker:

~~~text
FINITE TWO-POINT / FINITE-N DELAY CYCLES:
    EXCLUDED BY MATRIX ANALYTIC ELLIPTICITY

INFINITE-LOG FINITE-CYCLE RESIDUE:
    EMPTY

INFINITE OR ACCUMULATING DELAY COMPONENT:
    OPEN

RPB-57/58 FULL-FRIEDRICHS EXCLUSION:
    STILL CONDITIONAL

AZ-FIN-WEIL-NULL-EXTENSION:
    OPEN
~~~

## Next cursor

~~~text
RPB-63 / ACCUMULATING DELAY-COMPONENT COMPACTNESS TEST
~~~

The next pass should test whether an infinite self-supporting analytic singular
component can exist inside a compact interval.

Priority order:

1. exploit compactness of the projected analytic singular set and finite
   degree of the delay graph;
2. analyze accumulation points under fixed nonzero delay edges;
3. determine whether an infinite component necessarily contains a locally
   finite repeated pattern that can be vectorized, or instead accumulates
   through incommensurable near-returns;
4. test whether near-return arithmetic plus logarithmic matrix dominance gives
   a compactness contradiction;
5. stop if an infinite-dimensional almost-periodic matrix system is genuinely
   required.
