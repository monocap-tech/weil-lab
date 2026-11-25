# RPB-61 — Analytic-wavefront delay-orbit propagation

**Date:** 2026-09-29  
**Branch:** research/reflected-packet-bridge  
**Status:** **PASS AS PROPAGATION CLASSIFICATION / ANALYTIC SINGULARITIES OBEY AN EXISTENTIAL FINITE-DELAY WITNESS RELATION / DENSE PRIME-LOG GROUP DOES NOT FORCE A DENSE ACTUAL SINGULAR ORBIT / SYMMETRIC DELAYS ADMIT CLOSED TWO-POINT WITNESS CYCLES / LOGARITHMIC ELLIPTIC DOMINANCE YIELDS AT MOST ITERATED LOG-REGULARITY, NOT ANALYTIC EXTINCTION / BLOCKER A REMAINS AS AN INFINITE-LOG DELAY-CYCLE PROBLEM**  
**Dependencies:** RPB-36, RPB-37, RPB-60; RPB-EXT-A1 for the archimedean analytic pseudodifferential component.  
**Promotion status:** none.

## 0. Objective

RPB-60 corrected the historical full-symbol analytic-ellipticity shortcut.

The actual interior equation has the form

~~~math
\mathcal A_\infty h
-
\sum_{j=1}^{J}
a_j
\left(
\tau_{\ell_j}
+
\tau_{-\ell_j}
\right)h
=
g_{\rm an},
~~~

where:

- \(\mathcal A_\infty\) is the diagonal logarithmic archimedean operator;
- \(\ell_j>0\) are the finitely many active prime-power delays;
- \(g_{\rm an}\) is the analytic pole/evaluation datum.

RPB-61 derives the correct analytic-wavefront relation and tests whether compact
support or dense prime-log arithmetic forces every singularity orbit to exit the
support.

It does not.

The correct propagation law is existential, and the symmetric delay graph
admits closed witness cycles.

---

## 1. Archimedean ellipticity gives the local left-hand wavefront

Microlocally away from low frequency, the archimedean multiplier satisfies

~~~math
m_\infty(\xi)
=
\log|\xi|+O(1)
~~~

and is elliptic in the logarithmic pseudodifferential class.

For the archimedean component alone one therefore has the local analytic
wavefront equivalence

~~~math
\boxed{
WF_A(\mathcal A_\infty h)
=
WF_A(h)
}
~~~

on the interior, modulo the usual localization to the elliptic high-frequency
region.

This is the lawful use of the analytic pseudodifferential theorem retained
after RPB-60.

---

## 2. Translation transports analytic wavefront exactly

For one delay,

~~~math
(\tau_\ell h)(x)
=
h(x-\ell).
~~~

Translation is an analytic diffeomorphism, so

~~~math
\boxed{
(x,\xi)\in WF_A(\tau_\ell h)
\iff
(x-\ell,\xi)\in WF_A(h).
}
~~~

Likewise

~~~math
\boxed{
(x,\xi)\in WF_A(\tau_{-\ell}h)
\iff
(x+\ell,\xi)\in WF_A(h).
}
~~~

Thus a prime channel does not create a new cotangent direction.  It transports
the same direction between spatial points separated by the arithmetic delay.

---

## 3. Exact set-level propagation inclusion

Let

~~~math
S
=
WF_A(h).
~~~

The interior equation and analyticity of \(g_{\rm an}\) give

~~~math
WF_A(\mathcal A_\infty h)
\subseteq
\bigcup_j
WF_A(\tau_{\ell_j}h)
\cup
\bigcup_j
WF_A(\tau_{-\ell_j}h).
~~~

Using Section 1,

~~~math
\boxed{
S
\subseteq
\bigcup_{j=1}^{J}
T_{+\ell_j}S
\cup
\bigcup_{j=1}^{J}
T_{-\ell_j}S,
}
~~~

where

~~~math
T_{\ell}(x,\xi)
=
(x+\ell,\xi).
~~~

Equivalently, if

~~~math
(x,\xi)\in S,
~~~

then there exists at least one active delay \(\ell_j\) and one sign
\(\sigma\in\{\pm1\}\) such that

~~~math
\boxed{
(x+\sigma\ell_j,\xi)\in S.
}
~~~

This is the **analytic-wavefront delay-witness relation**.

---

## 4. The relation is existential, not group closure

RPB-37 introduced the additive delay group

~~~math
\Gamma_c
=
\sum_{p\in P_c}
\mathbb Z\log p.
~~~

Once two distinct primes are active,

~~~math
\overline{\Gamma_c}
=
\mathbb R.
~~~

That arithmetic fact remains correct.

But Section 3 does **not** imply

~~~math
x+\Gamma_c
\subseteq
\operatorname{sing\,supp}_A(h).
~~~

It says only that every singular point has **some** shifted singular witness.

The equation therefore does not force simultaneous closure under every
generator.

Consequently the density of \(\Gamma_c\) does not imply that one actual
wavefront orbit is dense.

This is a correction to any stronger reading of RPB-37.

---

## 5. Symmetric delays admit closed two-point witness cycles

Fix an active delay \(\ell\) and choose

~~~math
x,
\quad
x+\ell
\in(-c,c).
~~~

The two-point set

~~~math
\boxed{
S_x
=
\{(x,\xi),(x+\ell,\xi)\}
}
~~~

satisfies the set-level witness condition:

- the point at \(x\) is witnessed by the \(+\ell\) shift;
- the point at \(x+\ell\) is witnessed by the \(-\ell\) shift.

Thus compact support does not force a witness path to march monotonically
toward an endpoint.

Even a finite closed cycle is compatible with the **set-valued** propagation
relation.

This does not construct an actual solution of the Weil equation.  It proves
that wavefront-set geometry alone cannot exclude one.

---

## 6. Rightmost-singularity arguments also stop at a cycle

Suppose the analytic singular support has a rightmost point \(x_*\).

The witness relation rules out every \(+\ell_j\) witness that would lie to the
right of \(x_*\), but it still allows an inward witness

~~~math
x_*-\ell_j.
~~~

At that inward point the equation may be witnessed back by

~~~math
x_*.
~~~

Hence the simple argument

~~~text
rightmost singularity
→ inward predecessor
→ eventual support exit
~~~

does not follow.

The symmetric delay graph has no natural orientation.

---

## 7. Quantitative logarithmic dominance gives one log gain per step

The archimedean operator is stronger than a translation by one logarithmic
frequency weight.

Introduce local logarithmic Sobolev strength schematically by

~~~math
h\in H_{\log}^{N}
\quad\Longleftrightarrow\quad
(\log\langle D\rangle)^Nh
\in L^2_{\rm loc}.
~~~

If, near \(x\), every translated source germ appearing on the right-hand side
belongs to \(H_{\log}^{N}\), then logarithmic ellipticity gives

~~~math
\boxed{
h
\in
H_{\log}^{N+1}
\text{ near }x.
}
~~~

Thus every successful pass through the interior equation gains one power of

~~~math
\log\langle\xi\rangle.
~~~

This is the quantitative remnant of the high-frequency dominance noted in
RPB-60.

---

## 8. Closed finite witness cycles force infinite logarithmic regularity

Consider an isolated finite witness component for which every singular source
needed by the equations remains inside the same finite component.

Applying Section 7 successively around the component gives, for every fixed
\(N\),

~~~math
\boxed{
h
\in
H_{\log}^{N}
}
~~~

microlocally on that component.

Thus a finite closed delay cycle cannot support a singularity of merely finite
logarithmic strength.

Any surviving singularity must be **infinitely log-regular**.

This is a genuine narrowing of Blocker A.

---

## 9. Infinite log regularity is still far below analyticity

The class

~~~math
\bigcap_{N\ge0}
H_{\log}^{N}
~~~

is not quasianalytic and does not imply any positive Sobolev order.

At the Fourier-weight level, one can have decay of the schematic form

~~~math
|\widehat u(\xi)|
\approx
|\xi|^{-1/2}
\exp\!\left(
-\sqrt{\log|\xi|}
\right),
~~~

which beats every inverse power of \(\log|\xi|\) in \(L^2\) but does not beat
any positive power of \(|\xi|\).

Thus

~~~math
\boxed{
\bigcap_NH_{\log}^{N}
\not\subset
H^\varepsilon
\quad
\text{for any fixed }\varepsilon>0
}
~~~

at the level of available frequency control.

A fortiori it does not imply real analyticity.

Therefore iterating logarithmic dominance around a delay cycle does not close
the analytic-wavefront obstruction.

---

## 10. Infinite and dense witness paths are no better at set level

An infinite witness path

~~~math
x_0,
x_1,
x_2,
\dots
~~~

with

~~~math
x_{n+1}-x_n
\in
\{\pm\ell_1,\dots,\pm\ell_J\}
~~~

may remain inside a bounded interval by repeated returns and cancellations of
steps.

With at least two incommensurable prime delays, such paths can have complicated
or dense accumulation behavior.

But the witness relation does not require the whole additive group orbit to be
singular, and density of possible arithmetic locations supplies no vanishing
principle for an \(L^2\) or infinitely log-regular germ.

Hence the multi-prime dense-orbit fact does not repair Blocker A.

---

## 11. Relation to recent analytic-FIO regularity results

Recent analytic/ultradifferentiable microlocal theory confirms that analytic
Fourier-integral operators transport the corresponding wavefront sets along
their canonical relations.

That supports the operator typing in RPB-60/61.

It does not provide a unique-continuation theorem for a sum of one logarithmic
elliptic pseudodifferential operator and several translation FIO channels.

No currently identified external theorem turns the witness relation of
Section 3 into analytic extinction.

---

## 12. Consequence for the RPB-57/58 promotion candidate

RPB-61 does not restore the withdrawn interior analyticity claim.

What it establishes is the exact replacement:

~~~math
\boxed{
\text{analytic singularities must lie in a self-supporting finite-delay witness graph.}
}
~~~

Finite closed components are forced into infinite logarithmic regularity, but
that is still below the regularity needed by RPB-57's holomorphic shifted-germ
argument.

Therefore:

~~~text
RPB-57 FULL NONTHRESHOLD FRIEDRICHS EXCLUSION:
    STILL CONDITIONAL

RPB-58 FULL THRESHOLD FRIEDRICHS EXCLUSION:
    STILL CONDITIONAL

PROMOTION BLOCKER A:
    NARROWED TO INFINITE-LOG SELF-SUPPORTING DELAY COMPONENTS
~~~

---

## 13. RPB-61 determination

~~~math
\boxed{
\textbf{RPB-61 — DELAY-WAVEFRONT PROPAGATION IS EXISTENTIAL; COMPACT SUPPORT AND DENSE PRIME-LOG ARITHMETIC DO NOT BY THEMSELVES EXCLUDE CLOSED SINGULAR CYCLES.}
}
~~~

Exact propagation law:

~~~math
\boxed{
(x,\xi)\in WF_A(h)
\Longrightarrow
\exists j,\sigma:
(x+\sigma\ell_j,\xi)\in WF_A(h).
}
~~~

New narrowing:

~~~math
\boxed{
\text{finite self-supporting delay cycles}
\Longrightarrow
\text{infinite logarithmic regularity}.
}
~~~

But

~~~math
\boxed{
\text{infinite logarithmic regularity}
\not\Longrightarrow
\text{analyticity}.
}
~~~

## Next cursor

~~~text
RPB-62 / INFINITE-LOG DELAY-CYCLE EXTINCTION TEST
~~~

The next pass should test whether the **actual equation**, beyond wavefront-set
geometry, excludes an infinitely log-regular self-supporting delay component.

Priority order:

1. localize a finite delay cycle and derive the coupled microlocal matrix
   equation at high frequency;
2. exploit the \(\log|\xi|\) diagonal growth against the bounded translation
   matrix;
3. determine whether localization commutators are sufficiently smoothing to
   upgrade infinite-log regularity to \(C^\infty\), Gevrey, or analytic
   regularity;
4. if finite cycles die, analyze whether an infinite/dense witness component
   can evade the same matrix coercivity;
5. stop if only super-logarithmic, nonquasianalytic regularity is obtained.
