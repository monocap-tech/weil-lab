# SZ-KERNEL-EDGE-GERM-22 — Ratio-germ filtration and incidence-kernel obstruction

**Date:** 2026-09-26  
**Branch:** sz-cross-collar  
**Status:** UNRATIFIED RESIDUE / NF PASS  
**Canonical parent:** SZ-CROSS-COLLAR-3  
**Immediate residue:** SZ-KERNEL-EDGE-GERM-21  
**Target tested:** RATIO-GERM FILTRATION  
**Public promotion:** forbidden

## 0. Objective

GERM-21 derived the first exact multi-cell threshold system and identified the
finite off-hinge ratio layer

\[
\mathscr R_c^{(1)}.
\]

This pass applies finite-dimensional flatness filtration to that layer and
audits whether its finite-order germs can be eliminated arithmetically.

The answer is mixed and sharper than the previous formulation.

1. The local-mass filtration on the finite ratio layer stabilizes after a
   finite order.
2. There is a second, larger filtration determined by the **ratio incidence
   operator**, because different ratio germs may cancel inside one threshold
   equation.
3. Every off-hinge ratio
   \[
   \log(p^r/q^s),\qquad p\ne q,
   \]
   comes from a unique ordered pair of prime powers.  Therefore that ratio
   germ occurs in exactly one prime-threshold equation.
4. Once a threshold has at least two cross-prime predecessors, its incidence
   row has a nontrivial cancellation kernel.  This already occurs when
   \[
   \log5
   \]
   becomes active.
5. Consequently, multi-cell prime-threshold equations alone do not provide an
   injective detector of the off-hinge ratio layer.

The pass also corrects the scope of GERM-21's reduced equation: for an
arbitrary threshold translate, the nonkernel escape field must remain present.
It vanishes only when that translate itself remains in \(K_c\).

Thus the first ratio layer is finite and typed, but not arithmetically rigid.

---

# I. Setup

## 1. Visible-superflat obstruction

Let

\[
W
=
E_{\rm vis}^\infty
\subseteq E_+
\]

be the right-visible superflat obstruction from GERM-15.

Let

\[
\mathscr R
=
\mathscr R_c^{(1)}
\]

be the finite first ratio layer from GERM-21.

For each

\[
d\in\mathscr R
\]

and sufficiently small \(\varepsilon>0\), define the local ratio restriction

\[
\boxed{
R_{d,\varepsilon}f
=
f(d+\cdot)|_{(0,\varepsilon)}.
}
\]

Choose \(\varepsilon\) small enough that the neighborhoods of distinct ratio
locations are disjoint and remain inside \((0,L)\).

---

# II. Raw ratio-mass filtration

## 2. Definition

For each integer

\[
N\ge0,
\]

define

\[
\boxed{
W_N^{\rm ratio}
=
\left\{
f\in W:
\|R_{d,\varepsilon}f\|_2
=
o(\varepsilon^N)
\text{ for every }d\in\mathscr R
\right\}.
}
\]

Then

\[
W_{N+1}^{\rm ratio}
\subseteq
W_N^{\rm ratio}.
\]

Define

\[
\boxed{
W_\infty^{\rm ratio}
=
\bigcap_{N\ge0}
W_N^{\rm ratio}.
}
\]

Because \(W\) is finite dimensional, the chain stabilizes:

\[
\boxed{
W_\infty^{\rm ratio}
=
W_{N_{\rm ratio}}^{\rm ratio}
}
\]

for some finite

\[
N_{\rm ratio}<\infty.
\]

Thus every obstruction direction is either:

1. finite-order visible at some off-hinge ratio location; or
2. superflat at every first-layer ratio location.

---

# III. Uniformity on the raw hard branch

## 3. Operator-superflat ratio observation

Define the direct-sum ratio observation

\[
\boxed{
\mathcal G_\varepsilon:
W\to
\bigoplus_{d\in\mathscr R}
L^2(0,\varepsilon),
\qquad
(\mathcal G_\varepsilon f)_d
=
R_{d,\varepsilon}f.
}
\]

On

\[
W_\infty^{\rm ratio},
\]

finite-dimensional norm equivalence gives

\[
\boxed{
\|\mathcal G_\varepsilon
|_{W_\infty^{\rm ratio}}\|
=
o(\varepsilon^N)
\qquad
\forall N.
}
\]

So raw ratio-superflatness is uniform on the stabilized branch.

---

# IV. Ratio incidence operator

## 4. Threshold rows

Let

\[
\mathscr H
=
\mathscr H_c^\circ.
\]

For each threshold

\[
\ell\in\mathscr H
\]

and ratio location

\[
d\in\mathscr R,
\]

there is at most one smaller delay

\[
\lambda=\ell-d.
\]

Define the finite weighted incidence matrix

\[
\boxed{
(\mathsf A_c)_{\ell,d}
=
\begin{cases}
a_{\ell-d},
&
\ell-d\in\mathscr H,\;
0<\ell-d<\ell,\\[3pt]
0,
&
\text{otherwise}.
\end{cases}
}
\]

Here

\[
a_\lambda
=
\frac{\Lambda(e^\lambda)}{e^{\lambda/2}}.
\]

Pointwise in the local variable \(\eta\),

\[
\mathsf A_c
\]

acts on the vector of ratio germs.

---

## 5. Incidence output

Define

\[
\boxed{
\mathcal I_\varepsilon
=
\mathsf A_c\mathcal G_\varepsilon.
}
\]

Its \(\ell\)-component is

\[
\boxed{
(\mathcal I_\varepsilon f)_\ell(\eta)
=
\sum_{\substack{\lambda<\ell\\
\ell-\lambda\in\mathscr R}}
a_\lambda
f(\ell-\lambda+\eta).
}
\]

This is exactly the off-hinge arithmetic term in the GERM-21 threshold
equation.

---

# V. Incidence-flat filtration

## 6. Definition

For

\[
N\ge0,
\]

define

\[
\boxed{
W_N^{\rm inc}
=
\left\{
f\in W:
\|\mathcal I_\varepsilon f\|
=
o(\varepsilon^N)
\right\}.
}
\]

Again this is a descending chain of subspaces, so it stabilizes:

\[
\boxed{
W_\infty^{\rm inc}
=
W_{N_{\rm inc}}^{\rm inc}
}
\]

for some finite

\[
N_{\rm inc}.
\]

Because

\[
\mathcal I_\varepsilon
=
\mathsf A_c\mathcal G_\varepsilon
\]

with fixed finite \(\mathsf A_c\),

\[
\boxed{
W_\infty^{\rm ratio}
\subseteq
W_\infty^{\rm inc}.
}
\]

The inclusion may be strict.

That strictness is the arithmetic cancellation problem.

---

# VI. Unique-pair theorem for off-hinge ratios

## 7. Statement

Suppose

\[
p^r/q^s
=
p'^{\,r'}/q'^{\,s'}
\]

with

\[
p\ne q,
\qquad
p'\ne q',
\]

and all four symbols denote primes with positive exponents.

Both fractions are already in lowest terms.

Uniqueness of prime factorization gives

\[
\boxed{
p=p',
\qquad
q=q',
\qquad
r=r',
\qquad
s=s'.
}
\]

Therefore every off-hinge ratio

\[
\boxed{
d=\log(p^r/q^s)
}
\]

determines a unique ordered pair

\[
(\ell,\lambda)
=
(r\log p,\;s\log q).
\]

---

## 8. Consequence for incidence columns

Each off-hinge ratio column of

\[
\mathsf A_c
\]

has exactly one nonzero entry.

Equivalently:

\[
\boxed{
\text{an off-hinge ratio germ appears in exactly one threshold equation}.
}
\]

This is a decisive correction to the hope that multiple threshold equations
might independently constrain the same ratio germ.

They do not.

The multi-cell coupling occurs because one threshold row may contain several
different ratio germs, not because one ratio germ reappears in several rows.

---

# VII. Rowwise cancellation geometry

## 9. Cross-prime predecessors of one threshold

Let

\[
\ell=r\log p.
\]

Every smaller active delay

\[
\lambda=s\log q
\]

with

\[
q\ne p
\]

produces one off-hinge ratio column in the \(\ell\)-row.

Let

\[
m_\ell
\]

be the number of such cross-prime predecessors.

Then the ratio incidence row has the form

\[
\boxed{
(g_1,\ldots,g_{m_\ell})
\longmapsto
\sum_{j=1}^{m_\ell}
a_{\lambda_j}g_j.
}
\]

At the abstract germ level its kernel has codimension one whenever

\[
m_\ell\ge1.
\]

Thus if

\[
m_\ell\ge2,
\]

there is a nontrivial cancellation family.

---

# VIII. First explicit incidence kernel

## 10. Threshold \(\log5\)

Assume

\[
L>\log5.
\]

Then the active smaller delays include

\[
\log2,\qquad
\log3,\qquad
\log4.
\]

All have prime base different from \(5\).

Therefore the \(\log5\) threshold row contains the three off-hinge germs

\[
\log(5/2),
\qquad
\log(5/3),
\qquad
\log(5/4).
\]

In particular it contains

\[
a_{\log2}g_{5/2}
+
a_{\log3}g_{5/3}
+
a_{\log4}g_{5/4}.
\]

Take any nonzero local profile

\[
h(\eta)
\]

and set, abstractly,

\[
g_{5/2}
=
a_{\log3}h,
\]

\[
g_{5/3}
=
-a_{\log2}h,
\]

\[
g_{5/4}=0.
\]

Then

\[
\boxed{
a_{\log2}g_{5/2}
+
a_{\log3}g_{5/3}
+
a_{\log4}g_{5/4}
=
0.
}
\]

Thus the ratio incidence operator is not injective once \(\log5\) is active.

This is an abstract local-germ cancellation model, not an actual vector of
\(K_c\).

It proves that arithmetic row structure alone cannot recover the individual
ratio germs.

---

# IX. Low-support regime

## 11. Before \(\log5\)

If

\[
L\le\log5,
\]

with strict activation convention \(\ell<L\), then \(\log5\) is not active.

In the regime

\[
\log3<L\le\log5,
\]

the active prime powers may include

\[
2,\;3,\;4,
\]

and the off-hinge ratio rows are:

- \(\log3\) sees \(\log(3/2)\);
- \(\log4\) sees \(\log(4/3)\);

while

\[
\log4-\log2=\log2
\]

is a same-prime hinge term.

Thus each off-hinge ratio column lies alone in its threshold row.

In this restricted regime,

\[
\boxed{
\mathsf A_c
\text{ is injective on the abstract first ratio layer}.
}
\]

This does not close the Weil problem because each threshold equation still
contains its archimedean cell transform and possibly a nonkernel escape field.

---

# X. Scope correction to GERM-21

## 12. General threshold identity on \(W\)

GERM-21 correctly derived

\[
F_{n_\ell}''(c-\eta)
=
-
\mathscr T_\ell f(\eta)
-
\sum_{\lambda<\ell}
a_\lambda f(\ell-\lambda+\eta)
-
a_\ell f(\eta),
\]

where

\[
n_\ell
=
(I-\Pi_K)T_{\ell,c}u.
\]

On

\[
W=E_{\rm vis}^\infty,
\]

the endpoint term and every same-prime difference term are superflat.

Therefore the correct reduced identity is

\[
\boxed{
F_{n_\ell}''(c-\eta)
+
\mathscr T_\ell f(\eta)
+
(\mathcal I_\varepsilon f)_\ell(\eta)
=
\text{superflat}.
}
\]

This is the load-bearing multi-cell equation.

---

## 13. Kernel-contained special case

Only when

\[
T_{\ell,c}u\in K_c
\]

do we have

\[
n_\ell=0.
\]

Then the reduced identity becomes

\[
\boxed{
\mathscr T_\ell f
+
(\mathcal I_\varepsilon f)_\ell
=
\text{superflat}.
}
\]

Thus the sentence in GERM-21 that omitted the escape field must be read in
this kernel-contained scope.

This pass records the correction explicitly.

---

# XI. What raw ratio-superflatness gives

## 14. All ratio germs superflat

If

\[
f\in W_\infty^{\rm ratio},
\]

then

\[
\mathcal I_\varepsilon f
\]

is operator-superflat.

Hence for every threshold \(\ell\),

\[
\boxed{
F_{n_\ell}''
+
\mathscr T_\ell f
=
\text{superflat}.
}
\]

Consequences:

- at kernel-contained thresholds,
  \[
  \mathscr T_\ell f
  \]
  is superflat;
- at escaping thresholds, the archimedean cell transform and the nonkernel
  escape field cancel to all algebraic orders.

This is a clean reduction to the archimedean/log-diagonal plus escape
channels.

---

# XII. What incidence-superflatness gives

## 15. Arithmetic cancellation branch

More generally, if

\[
f\in W_\infty^{\rm inc},
\]

the same conclusion holds:

\[
\boxed{
F_{n_\ell}''
+
\mathscr T_\ell f
=
\text{superflat}
}
\]

for every threshold.

Thus a source may have finite-order mass at individual ratio sites and still
be invisible to the threshold vector because its ratio germs cancel through
\(\mathsf A_c\).

The genuinely hard arithmetic branch is therefore

\[
\boxed{
W_\infty^{\rm inc},
}
\]

not merely

\[
W_\infty^{\rm ratio}.
\]

---

# XIII. Finite-order ratio mass does not automatically survive

## 16. Failure of the naive dichotomy

Suppose

\[
f\notin W_\infty^{\rm ratio}.
\]

Then at least one ratio germ has finite-order local mass.

This does **not** imply

\[
f\notin W_\infty^{\rm inc}.
\]

The \(\log5\) cancellation of Section VIII shows the abstract mechanism.

Therefore:

\[
\boxed{
\text{finite-order ratio mass}
\not\Rightarrow
\text{finite-order arithmetic threshold output}.
}
\]

A valid closure must either:

1. prove that the actual kernel family cannot realize the incidence kernel;
2. or use non-arithmetic equations—movable centers / log-diagonal coupling—to
   separate the cancelling ratio germs.

---

# XIV. Why further prime thresholds do not help

## 17. Unique-column obstruction

Because every off-hinge ratio germ belongs to exactly one threshold row, no
additional prime-threshold equation supplies a second independent coefficient
for that same local germ.

Thus enlarging the active prime set does not directly overdetermine an
existing ratio germ.

It only creates new ratio germs in new rows.

Therefore repeated prime-threshold closure does not produce an injective
finite arithmetic matrix on the off-hinge carrier set.

This is the exact obstruction to a purely finite prime-cell closure.

---

# XV. Relation to movable-center equations

## 18. Only remaining separator

To distinguish two ratio germs that cancel inside one threshold row, one must
observe them through an equation centered elsewhere.

GERM-4 gives exactly such movable-center equations.

But each movable center introduces the logarithmic archimedean diagonal
singularity at that center.

Hence:

\[
\boxed{
\text{incidence-kernel separation}
\Longrightarrow
\text{re-entry into the log-diagonal continuum}.
}
\]

So the ratio filtration does not evade the log-diagonal obstruction.

It identifies precisely why the finite arithmetic subsystem cannot close
without it.

---

# XVI. Result of this NF pass

The first ratio layer now has a complete finite-dimensional filtration and
incidence classification.

There are stabilized subspaces

\[
\boxed{
W_\infty^{\rm ratio}
\subseteq
W_\infty^{\rm inc}
\subseteq
W.
}
\]

- \(W_\infty^{\rm ratio}\): every individual off-hinge ratio germ is
  superflat;
- \(W_\infty^{\rm inc}\): only the weighted threshold combinations are
  superflat, allowing finite-order ratio germs to cancel.

Every off-hinge ratio germ occurs in exactly one threshold row.

Once a row contains at least two cross-prime predecessors, the arithmetic
incidence operator has a nontrivial cancellation kernel.

This occurs explicitly when

\[
\boxed{
L>\log5.
}
\]

Therefore the finite prime-delay system cannot, by itself, separate all
off-hinge source germs.

The correct reduced threshold equation is

\[
\boxed{
F_{n_\ell}''
+
\mathscr T_\ell f
+
(\mathsf A_c\mathcal G_\varepsilon f)_\ell
=
\text{superflat}.
}
\]

The remaining separator is necessarily the movable-center/log-diagonal
system or an equivalent global kernel constraint.

---

# XVII. Next traversal target

The next genuinely new target is

\[
\boxed{
\text{SZ-KERNEL-EDGE-GERM-23 / INCIDENCE-KERNEL LOG-DIAGONAL TEST}.
}
\]

The next pass should take the finite-dimensional incidence-kernel branch

\[
W_\infty^{\rm inc}
\]

and insert it into selected movable-center equations.

The target is to determine whether the continuum log-diagonal channel can
separate ratio-germ cancellations with a **finite** set of strategically
chosen centers on the actual finite-dimensional obstruction.

A positive result would convert the continuum obstruction into a finite
injective observation problem.

A negative result would show that the log-diagonal channel itself admits a
finite-dimensional superflat cancellation family compatible with the ratio
incidence kernel.

No such separation theorem is proved in this pass.

---

# XVIII. Cursor status

The canonical theorem cursor remains

\[
\boxed{\text{SZ-CROSS-COLLAR-3}}.
\]

This is an unratified ratio-filtration / incidence-no-go result.

No public promotion and no canonical cursor movement are asserted.
