# SZ-KERNEL-EDGE-GERM-21 — Multi-cell threshold system and arithmetic ratio germs

**Date:** 2026-09-26  
**Branch:** sz-cross-collar  
**Status:** UNRATIFIED RESIDUE / NF PASS  
**Canonical parent:** SZ-CROSS-COLLAR-3  
**Immediate residue:** SZ-KERNEL-EDGE-GERM-20  
**Target tested:** MULTI-CELL FIRST-KIND COMPATIBILITY  
**Public promotion:** forbidden

## 0. Objective

GERM-20 showed that even the strongest one-cell reflected conditions do not
force a blind source to vanish.

Therefore the next test must use the full finite-delay first-kind system
rather than one blind cell in isolation.

This pass derives the exact threshold equation for an arbitrary active
prime-power delay.

The resulting system is triangular in a more precise sense than before.

For a threshold delay

\[
\ell=\log n,
\]

every smaller active prime delay

\[
\lambda=\log m<\ell
\]

produces a direct source sample at

\[
\boxed{
\ell-\lambda+\eta
=
\log(n/m)+\eta.
}
\]

These are the **arithmetic ratio germs** registered in the terminology
registry.

The arithmetic classification is exact:

\[
\boxed{
\ell-\lambda
\text{ is itself a prime-power hinge}
\iff
n,m
\text{ are powers of the same prime}.
}
\]

Thus:

- same-prime powers form closed triangular hinge chains;
- cross-prime interactions create new **off-hinge ratio germs**.

On the jointly visible-superflat obstruction, all same-prime hinge samples are
superflat.  The only direct rough arithmetic terms left in the multi-cell
threshold equations are the cross-prime ratio germs.

This is the first exact global compatibility system unavailable to the local
GERM-20 countermodel.

It does not yet eliminate the obstruction.

---

# I. Active delay set

## 1. Prime-power delays

Let

\[
L=2c
\]

and define the strict interior active set

\[
\boxed{
\mathscr H_c^\circ
=
\left\{
\ell=\log n:
\Lambda(n)\ne0,\;
0<\ell<L
\right\}.
}
\]

For

\[
\ell=\log n\in\mathscr H_c^\circ,
\]

write

\[
\boxed{
a_\ell
=
\frac{\Lambda(n)}{\sqrt n}.
}
\]

The set is finite.

Write the right-oriented source as

\[
f(s)=u(c-s),
\qquad
0<s<L.
\]

---

# II. General threshold commutator

## 2. Translate by one active delay

Fix

\[
\ell\in\mathscr H_c^\circ.
\]

GERM-8 defines the right boundary commutator

\[
B_{\ell,+}u(x)
=
\int_{c-\ell}^{c}
g_{\rm screw}(x-\ell-z)u(z)\,dz.
\]

Set

\[
x=c-\eta.
\]

With

\[
t=c-z
\]

and then

\[
r=\ell-t,
\]

we obtain the exact source-coordinate form

\[
\boxed{
B_{\ell,+}u(c-\eta)
=
\int_0^\ell
g_{\rm screw}(\eta+r)
f(\ell-r)\,dr.
}
\]

---

# III. Local prime decomposition up to the threshold

## 3. Small \(\eta\)-window

Choose

\[
\eta_0>0
\]

small enough that:

1. \(\eta_0<\log2\);
2. no active prime-power delay lies in
   \[
   (\ell,\ell+\eta_0).
   \]

Then for

\[
0<\eta<\eta_0,
\qquad
0<r<\ell,
\]

the kernel argument satisfies

\[
0<\eta+r<\ell+\eta_0.
\]

Hence Suzuki's positive-axis decomposition contains exactly:

- the archimedean term \(a_\infty\);
- prime hinges with delay
  \[
  \lambda\le\ell.
  \]

Thus

\[
g_{\rm screw}(t)
=
a_\infty(t)
+
\sum_{\substack{\lambda\in\mathscr H_c^\circ\\
\lambda\le\ell}}
a_\lambda(t-\lambda)_+
\]

through this local argument range.

---

# IV. Exact differentiated threshold equation

## 4. Archimedean cell transform

Define

\[
\boxed{
(\mathscr T_\ell f)(\eta)
=
\int_0^\ell
a_\infty''(\eta+r)
f(\ell-r)\,dr.
}
\]

This generalizes the first-prime blind transform from GERM-17/18.

---

## 5. Prime atoms

For one prime hinge \(\lambda\le\ell\),

\[
\frac{d^2}{d\eta^2}
(\eta+r-\lambda)_+
=
\delta(\eta+r-\lambda).
\]

Therefore

\[
\int_0^\ell
\delta(\eta+r-\lambda)
f(\ell-r)\,dr
=
f(\ell-\lambda+\eta)
\]

for almost every sufficiently small \(\eta>0\).

For the threshold hinge

\[
\lambda=\ell,
\]

this becomes

\[
f(\eta).
\]

Hence

\[
\boxed{
\frac{d^2}{d\eta^2}
B_{\ell,+}u(c-\eta)
=
\mathscr T_\ell f(\eta)
+
\sum_{\substack{\lambda\in\mathscr H_c^\circ\\
\lambda<\ell}}
a_\lambda
f(\ell-\lambda+\eta)
+
a_\ell f(\eta).
}
\]

This is the exact multi-cell threshold equation.

---

# V. Kernel-contained and escape forms

## 6. If the translated source remains in the kernel

If

\[
T_{\ell,c}u\in K_c,
\]

then GERM-8 gives that

\[
B_{\ell,+}u
\]

is constant on the core zone.

Therefore

\[
\boxed{
0
=
\mathscr T_\ell f(\eta)
+
\sum_{\lambda<\ell}
a_\lambda
f(\ell-\lambda+\eta)
+
a_\ell f(\eta).
}
\]

For

\[
\ell=\log2,
\]

the sum over smaller prime delays is empty, recovering the GERM-17 threshold
equation.

---

## 7. First nonkernel escape

For arbitrary \(u\in K_c\), decompose the translated source into its kernel
projection plus nonkernel part

\[
n_\ell
=
(I-\Pi_K)T_{\ell,c}u.
\]

GERM-13 gives

\[
F_{n_\ell}(c-\eta)
=
\text{constant}
-
B_{\ell,+}u(c-\eta)
\]

on the core zone.

Hence

\[
\boxed{
F_{n_\ell}''(c-\eta)
=
-
\mathscr T_\ell f(\eta)
-
\sum_{\lambda<\ell}
a_\lambda
f(\ell-\lambda+\eta)
-
a_\ell f(\eta).
}
\]

So the exact failure of the multi-cell threshold equation is the local field
of the nonkernel translation escape.

---

# VI. Arithmetic ratio locations

## 8. Definition

For

\[
\ell=\log n,
\qquad
\lambda=\log m<\ell,
\]

the smaller-delay sample occurs at

\[
\boxed{
d_{\ell,\lambda}
=
\ell-\lambda
=
\log(n/m).
}
\]

The local source carrier is

\[
\boxed{
\eta
\longmapsto
f(d_{\ell,\lambda}+\eta).
}
\]

This is the arithmetic ratio germ.

---

# VII. Same-prime closure theorem

## 9. When is a ratio location another prime hinge?

Let

\[
n=p^r,
\qquad
m=q^s
\]

be prime powers with

\[
m<n.
\]

Suppose

\[
\frac{n}{m}
\]

is an integer prime power.

Then

\[
\frac{p^r}{q^s}
\]

must be an integer.

Unique factorization forces

\[
p=q.
\]

Since

\[
m<n,
\]

we then have

\[
s<r
\]

and

\[
\frac{n}{m}
=
p^{r-s}.
\]

Conversely, if

\[
p=q
\quad\text{and}\quad
s<r,
\]

the quotient is a prime power.

Therefore

\[
\boxed{
d_{\ell,\lambda}\in\mathscr H_c^\circ
\iff
\ell=r\log p,\;
\lambda=s\log p
\text{ for one prime }p,\;
s<r.
}
\]

---

# VIII. Prime-chain structure

## 10. Same-base chains

For each prime \(p\), the active powers form a chain

\[
\log p,\;
2\log p,\;
3\log p,\ldots
\]

up to the support cutoff.

Within one such chain,

\[
r\log p-s\log p
=
(r-s)\log p,
\]

so threshold equations remain on prime-hinge sites.

These are the exact arithmetic chains underlying the dyadic spine of
GERM-16--19.

---

## 11. Cross-prime interactions

If

\[
p\ne q,
\]

then

\[
r\log p-s\log q
\]

is not a prime-power logarithm.

Thus every cross-prime term creates an off-hinge ratio germ.

The first example is

\[
\boxed{
\log3-\log2
=
\log(3/2).
}
\]

This point is not an edge prime singular site.

Nevertheless the \(\log2\) prime atom samples its source germ directly inside
the \(\log3\) threshold equation.

So the full first-kind arithmetic system has rough source carriers beyond the
finite edge singular set \(\Sigma_c\).

This does not contradict EDGE-QA localization: \(\Sigma_c\) classified
nonanalytic carriers of the **small exterior edge motion**, whereas the ratio
germs arise only after a finite support translation is inserted into the
multi-cell threshold equations.

---

# IX. First ratio layer

## 12. Finite enlargement

Define

\[
\boxed{
\mathscr R_c^{(1)}
=
\left\{
\ell-\lambda:
\lambda,\ell\in\mathscr H_c^\circ,\;
0<\lambda<\ell,\;
\ell-\lambda\notin\mathscr H_c^\circ
\right\}.
}
\]

This is the first off-hinge ratio layer.

Because the active delay set is finite,

\[
\boxed{
\mathscr R_c^{(1)}
\text{ is finite}.
}
\]

Thus the first exact multi-cell closure enlarges the local carrier set from

\[
\mathscr H_c^\circ
\]

to

\[
\boxed{
\mathscr H_c^\circ
\cup
\mathscr R_c^{(1)}.
}
\]

---

# X. Reduction on the visible-superflat obstruction

## 13. Same-prime terms become superflat

Let

\[
W=E_{\rm vis}^\infty
\]

from GERM-15.

For every active prime hinge \(d\),

\[
\boxed{
\|f\|_{L^2(d,d+\varepsilon)}
=
o(\varepsilon^N)
\qquad
\forall N
}
\]

uniformly on \(W\).

Therefore, if

\[
d_{\ell,\lambda}
\]

is another prime hinge—equivalently, if \(\ell,\lambda\) belong to one
same-prime chain—then

\[
\boxed{
f(d_{\ell,\lambda}+\eta)
}
\]

is a superflat \(L^2\) germ on \(W\).

The threshold endpoint term

\[
f(\eta)
\]

is likewise superflat.

---

## 14. Reduced multi-cell equation

Hence on \(W\), the exact threshold equation reduces to

\[
\boxed{
\mathscr T_\ell f(\eta)
+
\sum_{\substack{\lambda<\ell\\
d_{\ell,\lambda}\in\mathscr R_c^{(1)}}}
a_\lambda
f(d_{\ell,\lambda}+\eta)
=
\text{superflat}
}
\]

for every active threshold \(\ell\).

Thus:

\[
\boxed{
\text{same-prime chains are absorbed by visible superflatness;}
}
\]

the direct rough arithmetic remainder is exactly the finite set of
cross-prime ratio germs.

This is the global compatibility statement sought after GERM-20.

---

# XI. The minimal threshold remains irreducible

## 15. First prime

For

\[
\ell=\log2,
\]

there is no smaller active prime delay.

Therefore

\[
\boxed{
\mathscr T_{\log2}f(\eta)
+
a_{\log2}f(\eta)
=
0
}
\]

at a kernel-contained first-prime step.

No ratio germ enters.

Thus the local GERM-20 no-go is not repaired by a hidden smaller arithmetic
channel at the minimal hinge.

Any global elimination of that branch must occur through equations at larger
delays or through the movable-center/log-diagonal system.

---

# XII. The first genuinely multi-prime regime

## 16. Before \(\log3\)

In the strict support regime

\[
\log2<L<\log3,
\]

the only active interior prime-power delay is

\[
\log2.
\]

Hence there is no cross-prime ratio layer.

The multi-cell threshold system reduces to the one-cell first-prime system
already shown locally non-rigid in GERM-20.

---

## 17. Once \(\log3\) is active

If

\[
L>\log3,
\]

then both

\[
\log2
\quad\text{and}\quad
\log3
\]

are active.

The \(\ell=\log3\) threshold equation contains

\[
\boxed{
a_{\log2}
f(\log(3/2)+\eta).
}
\]

Therefore

\[
\boxed{
\log(3/2)\in\mathscr R_c^{(1)}.
}
\]

So the first off-hinge rough carrier appears immediately when the second prime
base enters.

---

# XIII. Correction to the purely dyadic exceptional picture

## 18. Dyadic-resonant support is not a closed arithmetic subsystem

GERM-19 isolated the reflection geometry

\[
L=N\log2.
\]

If

\[
N=1,
\]

then

\[
L=\log2
\]

lies in the Bombieri--Yoshida trivial-kernel window used by GERM-8.

So no nonzero edge obstruction exists there.

If

\[
N\ge2,
\]

then

\[
L\ge2\log2=\log4>\log3.
\]

Hence

\[
\log3
\]

is an active interior prime delay.

Therefore the cross-prime ratio germ

\[
\boxed{
\log(3/2)
}
\]

is present.

Thus:

\[
\boxed{
\text{nontrivial dyadic reflection closure does not produce a pure dyadic
first-kind subsystem}.
}
\]

Even when the entire dyadic spine is reflection-closed, the full Weil
arithmetic introduces cross-prime ratio carriers.

This is a scope correction to any attempt to close the exceptional branch
using dyadic cells alone.

---

# XIV. Why the first ratio layer does not yet close the system

## 19. Ratio germs are not edge-visible hinges

For

\[
d\in\mathscr R_c^{(1)},
\]

there is no prime hinge at \(d\).

Therefore the visible-germ filtration of GERM-15 supplies no direct
superflatness statement for

\[
f(d+\eta).
\]

These germs belong to the interior/bulk part reconstructed by the one-sided
Schur map of GERM-3.

At every fixed collar radius, they are bounded linear functions of visible
data because \(K_c\) is finite dimensional.

But no controlled rate as the visible collars shrink has been established.

Thus the ratio layer is exactly another manifestation of the Schur
reconstruction-rate problem.

---

# XV. Relation to movable-center reachability

## 20. Why ratio germs cannot simply be promoted to new prime cells

One might try to treat each

\[
d\in\mathscr R_c^{(1)}
\]

as a new cell center and repeat the triangular arithmetic argument.

But \(d\) is not a screw-kernel prime delay.

There is no corresponding prime hinge whose threshold equation is based at
\(d\).

To probe it directly one must use the movable-center identity of GERM-4.

That maneuver introduces the logarithmic archimedean diagonal singularity at
the new center.

Therefore:

\[
\boxed{
\text{prime-threshold closure stops at the ratio layer;}
}
\]

continuing beyond it re-enters the log-diagonal continuum.

---

# XVI. Result of this NF pass

The full finite-delay first-kind compatibility system has now been written
explicitly.

For every active threshold \(\ell\),

\[
\boxed{
B_{\ell,+}''(\eta)
=
\mathscr T_\ell f(\eta)
+
\sum_{\lambda<\ell}
a_\lambda f(\ell-\lambda+\eta)
+
a_\ell f(\eta).
}
\]

On the jointly visible-superflat obstruction:

- endpoint terms are superflat;
- same-prime ratio terms are superflat because they land on visible
  prime-hinge germs;
- cross-prime terms land on the finite off-hinge ratio set
  \[
  \mathscr R_c^{(1)}.
  \]

Thus the one-cell GERM-20 counterprofiles cannot be pasted independently.

Their exact global compatibility is mediated by:

\[
\boxed{
\text{blind archimedean cell transforms}
+
\text{off-hinge arithmetic ratio germs}.
}
\]

The first ratio germ appears as soon as \(\log3\) is active:

\[
\boxed{
\log(3/2).
}
\]

And even the dyadic-resonant support geometry is not closed under the full
arithmetic system.

This is a genuine multi-cell structural reduction, but not an elimination.

---

# XVII. Next traversal target

The next genuinely new target is

\[
\boxed{
\text{SZ-KERNEL-EDGE-GERM-22 / RATIO-GERM FILTRATION}.
}
\]

The next pass should apply the finite-dimensional local-mass filtration to the
finite first ratio layer

\[
\mathscr R_c^{(1)}.
\]

For each ratio location \(d\), split the obstruction into:

1. directions with finite-order \(L^2\) mass near \(d\);
2. directions superflat at \(d\).

Then insert that split into the reduced threshold equations of Section X.

If every ratio germ is superflat, the entire finite prime-delay contribution
becomes superflat and the remaining compatibility is purely archimedean /
log-diagonal.

If some ratio germ has finite-order mass, the next task is to determine
whether its coefficient survives cancellation across the finitely many
threshold equations.

No ratio-germ filtration theorem is proved in this pass.

---

# XVIII. Cursor status

The canonical theorem cursor remains

\[
\boxed{\text{SZ-CROSS-COLLAR-3}}.
\]

This is an unratified multi-cell threshold / ratio-germ structural result.

No public promotion and no canonical cursor movement are asserted.
