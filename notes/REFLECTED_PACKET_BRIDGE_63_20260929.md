# RPB-63 — Accumulating delay-component compactness test

**Date:** 2026-09-29  
**Branch:** research/reflected-packet-bridge  
**Status:** **PASS AS COMPACTNESS CLASSIFICATION / CANTOR--BENDIXSON DERIVATIVES PRESERVE THE DELAY-WITNESS PROPERTY / COUNTABLE COMPACT SELF-SUPPORTING SINGULAR SETS ARE EXCLUDED BY RPB-62 / ANY REMAINING ANALYTIC SINGULAR SET HAS A NONEMPTY PERFECT KERNEL / PERFECT RESIDUE CAN INTERLACE UNCOUNTABLY MANY COUNTABLE PRIME-LOG GRAPH COMPONENTS / COMPACTNESS ALONE DOES NOT CLOSE BLOCKER A**  
**Dependencies:** RPB-37, RPB-61, RPB-62; Cantor--Bendixson theorem for compact subsets of \(\mathbb R\).  
**Promotion status:** none.

## 0. Objective

RPB-62 excludes every finite isolated self-supporting delay component.

RPB-63 asks whether an infinite self-supporting analytic singular component can
survive inside the compact support.

The answer has two parts:

1. every **countable compact** self-supporting singular set is impossible;
2. compactness does not eliminate a **perfect** self-supporting residue.

Thus the remaining obstruction is much more rigid than an arbitrary infinite
orbit, but it is not empty by topology alone.

---

## 1. Fix one analytic cotangent direction

In one space dimension the nonzero cotangent directions have two signs.

Fix one sign and let

~~~math
S
\subset
[-c,c]
~~~

be the projected spatial set of points carrying that analytic wavefront
direction.

After restricting away from endpoint bookkeeping when necessary, \(S\) is
closed in the compact support interval.

The RPB-61 witness relation is

~~~math
\boxed{
x\in S
\Longrightarrow
\exists d\in D:
x+d\in S,
}
~~~

where

~~~math
D
=
\{\pm\ell_1,\dots,\pm\ell_J\}
~~~

is the finite symmetric active-delay set.

Call such a set **delay-self-supporting**.

---

## 2. The first derived set is self-supporting

Let

~~~math
S'
~~~

be the Cantor--Bendixson derived set of accumulation points of \(S\).

Take

~~~math
x\in S'.
~~~

Choose distinct points

~~~math
x_n\in S,
\qquad
x_n\to x.
~~~

For each \(n\), the witness relation supplies

~~~math
d_n\in D
~~~

with

~~~math
x_n+d_n\in S.
~~~

Since \(D\) is finite, pass to a subsequence with

~~~math
d_n=d
~~~

constant.

Then

~~~math
x_n+d\to x+d.
~~~

The points \(x_n+d\) are distinct because translation is injective.

Hence

~~~math
x+d
~~~

is an accumulation point of \(S\):

~~~math
x+d\in S'.
~~~

Therefore

~~~math
\boxed{
S'
\text{ is delay-self-supporting.}
}
~~~

---

## 3. Every transfinite derivative remains self-supporting

Define the Cantor--Bendixson derivatives in the usual way:

~~~math
S^{(0)}=S,
~~~

~~~math
S^{(\alpha+1)}
=
\left(
S^{(\alpha)}
\right)',
~~~

and at a limit ordinal \(\lambda\),

~~~math
S^{(\lambda)}
=
\bigcap_{\alpha<\lambda}
S^{(\alpha)}.
~~~

The successor step follows from Section 2.

For a limit step, take

~~~math
x\in S^{(\lambda)}.
~~~

For every \(\alpha<\lambda\), self-support gives some

~~~math
d_\alpha\in D
~~~

such that

~~~math
x+d_\alpha
\in
S^{(\alpha)}.
~~~

Because \(D\) is finite, one delay \(d\) occurs for a cofinal set of
\(\alpha<\lambda\).

For every fixed

~~~math
\beta<\lambda,
~~~

choose such an \(\alpha\ge\beta\).

Since the derivative family is decreasing,

~~~math
x+d
\in
S^{(\alpha)}
\subseteq
S^{(\beta)}.
~~~

Thus

~~~math
x+d
\in
\bigcap_{\beta<\lambda}
S^{(\beta)}
=
S^{(\lambda)}.
~~~

Therefore:

~~~math
\boxed{
S^{(\alpha)}
\text{ is delay-self-supporting for every ordinal }\alpha.
}
~~~

---

## 4. Countable compact self-supporting sets are impossible

Suppose

~~~math
S
~~~

is nonempty, compact, and countable.

The Cantor--Bendixson theorem for compact metric spaces says that its derivative
sequence eventually reaches a finite nonempty set before becoming empty.

Thus there is an ordinal \(\alpha\) for which

~~~math
\varnothing
\ne
S^{(\alpha)}
~~~

is finite.

Section 3 says this finite set is still delay-self-supporting.

But RPB-62 excludes every finite isolated self-supporting analytic singular
component: after recentering, the finite matrix logarithmic system is
analytically elliptic.

Contradiction.

Hence:

~~~math
\boxed{
\text{no nonempty countable compact delay-self-supporting analytic singular set exists.}
}
~~~

---

## 5. Any surviving residue has a perfect kernel

For a compact subset of \(\mathbb R\), the Cantor--Bendixson decomposition is

~~~math
S
=
P
\cup
C,
~~~

where:

- \(P\) is perfect;
- \(C\) is countable;
- \(P\cap C=\varnothing\).

If \(S\) is nonempty and delay-self-supporting, Section 4 rules out the case

~~~math
P=\varnothing.
~~~

Therefore any surviving analytic singular set must satisfy

~~~math
\boxed{
P\ne\varnothing.
}
~~~

Moreover the stable terminal derivative which produces \(P\) is itself
delay-self-supporting by Section 3.

Thus the remaining Blocker-A object is a **perfect delay-self-supporting
kernel**.

---

## 6. Perfect means uncountable and nowhere reducible to finite charts

A nonempty perfect subset of \(\mathbb R\) is uncountable.

Every point is an accumulation point.

Consequently there is no finite isolated family of singular charts to which
the RPB-62 matrix reduction can be applied globally.

The obstruction is therefore not merely an "infinite cycle."

It is an accumulation field with singular points arbitrarily close to other
singular points.

---

## 7. Graph components remain countable

The arithmetic delay group is

~~~math
\Gamma_c
=
\sum_{p\in P_c}
\mathbb Z\log p.
~~~

Because there are only finitely many active primes at fixed support,

~~~math
\Gamma_c
~~~

is countable.

For a point \(x\), its graph-connected arithmetic orbit lies in

~~~math
x+\Gamma_c.
~~~

Hence every exact delay-graph component is countable.

Therefore an uncountable perfect singular kernel cannot be one graph component.

Instead it must consist of

~~~math
\boxed{
\text{uncountably many countable graph components whose closures interlace.}
}
~~~

This is the precise topological form of the accumulating residue.

---

## 8. Why an orbit closure does not become one graph component

RPB-37 shows that when at least two distinct prime generators are active,

~~~math
\Gamma_c
~~~

is dense.

Thus one countable orbit

~~~math
x+\Gamma_c
~~~

may be dense in an interval.

But an accumulation point

~~~math
y
=
\lim_n(x+\gamma_n)
~~~

need not satisfy

~~~math
y-x\in\Gamma_c.
~~~

If not, \(y\) belongs to a different exact graph component even though it lies
in the closure of the original one.

This is why an infinite matrix indexed by one arithmetic orbit is not
topologically closed under accumulation.

---

## 9. Formal infinite adjacency does not solve the analytic problem

On a countable orbit one may formally introduce a bounded adjacency operator

~~~math
M_\Gamma
~~~

whose degree is bounded by

~~~math
2J
~~~

and whose operator norm is controlled by the finite sum of prime coefficients.

Formally,

~~~math
m_\infty(\xi)I-M_\Gamma
~~~

is invertible at sufficiently high frequency because

~~~math
m_\infty(\xi)\sim\log|\xi|.
~~~

This resembles the finite RPB-62 matrix argument.

However the formal inversion does not yet yield a lawful analytic parametrix
for the ambient function \(h\).

The reason is geometric:

- one orbit is countable and may be dense;
- its chart centers have no positive separation;
- their closures contain singular points from other orbit components;
- there is no uniform isolated common chart in which every external translated
  germ becomes analytic forcing.

Thus the finite matrix argument does not extend by simply replacing
\(\mathbb C^N\) with \(\ell^2(\Gamma_c)\).

---

## 10. Weighted orbit spaces do not remove the common-radius obstruction

One could force summability by assigning rapidly decaying weights to orbit
vertices and working in a weighted sequence space.

Because the delay graph has bounded degree, the adjacency operator can be made
bounded under reasonable edge-comparable weights.

But analytic regularity requires a common complex/local radius for the
vector-valued germ.

In a dense accumulating orbit, the radii separating one chart from other
singular components can tend to zero.

Weights control norm size.

They do not create a positive common analytic radius.

Therefore weighted \(\ell^2\) or \(\ell^\infty\) packaging does not by itself
repair the accumulation problem.

---

## 11. Compactness alone cannot exclude a perfect self-supporting set

The witness relation is only existential.

At the purely set-theoretic level a perfect continuum may satisfy it.

For example, with one delay

~~~math
0<\ell<2c,
~~~

the whole interval

~~~math
[-c,c]
~~~

is self-supporting in the interior sense:

- points sufficiently left may use \(+\ell\);
- points sufficiently right may use \(-\ell\).

Thus compactness, perfectness, and finite graph degree are not enough to force a
support exit.

The remaining contradiction must use quantitative analytic data from the
actual equation, not topology alone.

---

## 12. RPB-63 determination

~~~math
\boxed{
\textbf{RPB-63 — COUNTABLE ACCUMULATING DELAY RESIDUES ARE IMPOSSIBLE; ANY SURVIVING BLOCKER-A SET HAS A NONEMPTY PERFECT SELF-SUPPORTING KERNEL.}
}
~~~

Refined residue:

~~~text
FINITE SELF-SUPPORTING COMPONENT:
    EXCLUDED BY RPB-62

COUNTABLE COMPACT SELF-SUPPORTING SINGULAR SET:
    EXCLUDED BY CANTOR--BENDIXSON DESCENT + RPB-62

NONEMPTY PERFECT SELF-SUPPORTING KERNEL:
    OPEN

ONE EXACT GRAPH COMPONENT:
    COUNTABLE

PERFECT RESIDUE:
    UNCOUNTABLY MANY INTERLACING COUNTABLE COMPONENTS
~~~

Thus promotion Blocker A has become a **perfect-kernel microlocal problem**.

## Next cursor

~~~text
RPB-64 / PERFECT-KERNEL FBI MAXIMUM TEST
~~~

The next pass should use quantitative analytic microlocal amplitudes rather than
set-valued wavefront topology.

Priority order:

1. choose an FBI/analytic localization adapted to one cotangent sign;
2. derive the high-frequency inequality
   \[
   \log\lambda\,A(x,\lambda)
   \lesssim
   \sum_j A(x\pm\ell_j,\lambda)
   +
   e^{-c\lambda};
   \]
3. take a suitable supremum over the compact perfect kernel;
4. determine whether logarithmic diagonal growth beats the finite-degree delay
   coupling uniformly;
5. audit boundary/localization errors carefully, since a naive global maximum
   argument can import endpoint singularities.
