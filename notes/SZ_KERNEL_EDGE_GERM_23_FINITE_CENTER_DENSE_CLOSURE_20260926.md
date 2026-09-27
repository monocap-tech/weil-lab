# SZ-KERNEL-EDGE-GERM-23 — Finite arithmetic-center separation and dense log-diagonal closure

**Date:** 2026-09-26  
**Branch:** sz-cross-collar  
**Status:** UNRATIFIED RESIDUE / NF PASS  
**Canonical parent:** SZ-CROSS-COLLAR-3  
**Immediate residue:** SZ-KERNEL-EDGE-GERM-22  
**Target tested:** INCIDENCE-KERNEL LOG-DIAGONAL TEST  
**Public promotion:** forbidden

## 0. Objective

GERM-22 isolated the arithmetic hard branch

\[
W_\infty^{\rm inc},
\]

where first-layer off-hinge ratio germs may carry finite-order mass but cancel
inside the finite ratio-incidence operator.

The proposed next step was to separate those cancellations with strategically
chosen movable-center equations.

This pass gives both a positive and a negative result.

### Positive

Every first-layer ratio germ admits a finite denominator-clearing chain of
movable centers ending at an actual prime-power hinge.

More generally, once at least two prime bases are active, the arithmetic
centers reachable by repeated prime-delay shifts form a dense additive group.

Because \(W_\infty^{\rm inc}\) is finite dimensional, finitely many local
restrictions near reachable arithmetic centers already separate it.

Thus the continuum movable-center family can be reduced, existentially, to a
finite source detector.

### Negative

That finite detector does not close the Weil equation.

Every selected movable center introduces its own logarithmic archimedean
diagonal channel, and recursive prime closure of the new sampled source germs
generates the dense arithmetic center lattice.

Therefore the natural arithmetic closure is not a larger finite graph.

It is a dense center system coupled to the logarithmic diagonal principal
species.

The continuum obstruction of GERM-4 is therefore intrinsic, even though any
fixed finite-dimensional obstruction can be separated by finitely many chosen
centers.

---

# I. Source-coordinate movable-center equation

## 1. Center coordinate

Work in right-oriented source coordinates

\[
s=c-y,
\qquad
0<s<L,
\qquad
L=2c.
\]

Let the physical movable center be

\[
x=c-h,
\qquad
0<h<L.
\]

Then a prime delay

\[
\lambda
\]

probes source locations

\[
\boxed{
h-\lambda
\qquad\text{and}\qquad
h+\lambda,
}
\]

whenever they remain in \((0,L)\).

This is the source-coordinate form of the two tent centers from GERM-4.

---

## 2. Centered identity

For

\[
u\in K_c
\]

and sufficiently small

\[
\delta<\min(h,L-h),
\]

the movable-center equation is

\[
\boxed{
0
=
\mathscr D_h(\delta)f
+
\sum_{\lambda\in\mathscr H_c^\circ}
a_\lambda
\left[
\mathscr V_{h-\lambda,\delta}f
+
\mathscr V_{h+\lambda,\delta}f
\right],
}
\]

where:

- \(\mathscr D_h\) is the archimedean centered second-difference channel,
  singular at the diagonal source point \(s=h\);
- \(\mathscr V_{d,\delta}\) is the compact tent moment centered at source
  location \(d\);
- out-of-support tent centers contribute zero.

Thus every arithmetic attempt to probe one local source germ is coupled to a
new diagonal germ at the chosen center.

---

# II. Denominator-clearing ladders for ratio germs

## 3. One off-hinge ratio

Take

\[
d
=
\log(p^r/q^s),
\qquad
p\ne q,
\qquad
r,s\ge1.
\]

This is an off-hinge arithmetic ratio germ.

The denominator-prime delay

\[
\lambda_q=\log q
\]

is active whenever the ratio itself arises from active prime powers.

Define

\[
\boxed{
d_k
=
\log(p^r/q^k),
\qquad
k=0,\ldots,s.
}
\]

Then

\[
d_s=d
\]

and

\[
\boxed{
d_0=r\log p
}
\]

is an actual prime-power hinge.

---

## 4. One ladder step

Choose the movable center

\[
\boxed{
h=d_{k-1}
}
\]

and use the prime delay

\[
\lambda_q=\log q.
\]

Then the two \(q\)-prime tent centers are

\[
h-\lambda_q
=
d_k
\]

and

\[
h+\lambda_q
=
d_{k-2}
\]

when \(k\ge2\).

Thus one movable-center equation couples:

\[
\boxed{
d_k
\longleftrightarrow
d_{k-1}
\longleftrightarrow
d_{k-2},
}
\]

where:

- \(d_k\) is the ratio germ one wants to probe;
- \(d_{k-1}\) is the new logarithmic diagonal center;
- \(d_{k-2}\) is a ratio closer to the numerator hinge.

For \(k=1\), the second prime sample lies at

\[
d_{-1}=\log(p^rq),
\]

if that point remains inside the support.

---

## 5. Finite denominator clearing

Repeating the construction for

\[
k=s,s-1,\ldots,1
\]

produces the finite ladder

\[
\boxed{
\log(p^r/q^s),
\;
\log(p^r/q^{s-1}),
\ldots,
\log(p^r/q),
\;
\log(p^r).
}
\]

Therefore every first-layer ratio germ is finitely connected to a genuine
prime-power hinge by denominator-prime recentering.

This is the strongest finite arithmetic reachability statement available for
the ratio layer.

---

# III. Why the ladder does not close by itself

## 6. New diagonal at every rung

At the \(k\)-th step, the archimedean centered channel is singular at

\[
\boxed{
s=d_{k-1}.
}
\]

Except at the terminal numerator hinge

\[
d_0,
\]

these are generally off-hinge ratio locations.

Thus the denominator-clearing ladder trades one ratio germ for:

1. a neighboring ratio germ;
2. a new logarithmic diagonal germ.

The arithmetic denominator decreases, but diagonal custody accumulates.

---

## 7. Other prime delays

The same movable-center equation contains every other active prime delay

\[
\lambda\in\mathscr H_c^\circ.
\]

These probe

\[
d_{k-1}\pm\lambda.
\]

Hence even the denominator-prime ladder is not a closed three-term recurrence
inside the actual Weil equation.

It is only the distinguished arithmetic spine of a larger center system.

---

# IV. Arithmetic center lattice

## 8. Definition

Let

\[
\mathcal P_c
=
\left\{
p\text{ prime}:\log p<L
\right\}.
\]

Define the arithmetic center lattice

\[
\boxed{
\Gamma_c
=
\sum_{p\in\mathcal P_c}
\mathbb Z\log p.
}
\]

Every original prime hinge, first-layer ratio germ, denominator-clearing
center, and every location obtained by finitely many prime-delay recenterings
lies in

\[
\Gamma_c.
\]

---

# V. Density once two prime bases are active

## 9. Irrational logarithmic ratio

Let

\[
p\ne q
\]

be primes.

If

\[
\frac{\log p}{\log q}
=
\frac mn
\in\mathbb Q,
\]

then

\[
p^n=q^m,
\]

contradicting unique factorization.

Therefore

\[
\boxed{
\frac{\log p}{\log q}\notin\mathbb Q.
}
\]

---

## 10. Dense additive subgroup

For two positive numbers \(a,b\) with

\[
a/b\notin\mathbb Q,
\]

the additive subgroup

\[
\mathbb Za+\mathbb Zb
\]

is dense in \(\mathbb R\).

A standard proof uses density of the fractional parts of

\[
na/b
\]

modulo \(1\), or the pigeonhole/Dirichlet approximation argument.

Hence, once two distinct prime bases are active,

\[
\boxed{
\Gamma_c
\text{ is dense in }\mathbb R.
}
\]

In particular,

\[
\boxed{
\Gamma_c\cap(0,L)
\text{ is dense in }(0,L).
}
\]

---

# VI. Sharp support-regime dichotomy

## 11. One-prime-base regime

If

\[
\log2<L\le\log3,
\]

then the only active prime base is \(2\).

All active prime-power delays belong to the dyadic chain.

There is no cross-prime ratio layer.

Therefore the finite arithmetic route reduces to the minimal-hinge / dyadic
system already tested in GERM-17--20.

The local quasi-analyticity obstruction remains.

---

## 12. Multi-prime regime

If

\[
L>\log3,
\]

then both prime bases \(2\) and \(3\) are active.

Therefore

\[
\boxed{
\Gamma_c
\text{ is dense}.
}
\]

So as soon as the first cross-prime ratio

\[
\log(3/2)
\]

appears, recursive movable-center arithmetic no longer closes on any natural
finite carrier set.

There is no intermediate finite arithmetic closure regime.

---

# VII. Finite-dimensional source separation by reachable centers

## 13. General finite family

Let

\[
0\ne V
\subset
L^2(0,L)
\]

be finite dimensional.

Assume \(\Gamma_c\cap(0,L)\) is dense.

Consider all local restriction maps

\[
R_{h,\rho}:
V\to
L^2((h-\rho,h+\rho)\cap(0,L))
\]

with

\[
h\in\Gamma_c\cap(0,L),
\qquad
\rho>0.
\]

The family of these restrictions is jointly injective.

Indeed, if \(f\in V\) vanished on every such neighborhood, then it would
vanish on an open basis covering \((0,L)\), hence

\[
f=0
\]

almost everywhere.

---

## 14. Finite extraction

Because \(V\) is finite dimensional, joint injectivity implies that finitely
many such restrictions already have trivial common kernel.

Thus there exist reachable arithmetic centers

\[
\boxed{
h_1,\ldots,h_M\in\Gamma_c\cap(0,L)
}
\]

and radii

\[
\rho_1,\ldots,\rho_M>0
\]

such that

\[
\boxed{
f\longmapsto
\left(
R_{h_1,\rho_1}f,
\ldots,
R_{h_M,\rho_M}f
\right)
}
\]

is injective on \(V\).

One may further extract finitely many scalar \(L^2\) test functionals from
these neighborhoods that separate \(V\).

Hence:

\[
\boxed{
\text{the dense movable-center continuum can be compressed
to finitely many source detectors on any fixed finite-dimensional }V.
}
\]

Apply this in particular to

\[
V=W_\infty^{\rm inc}.
\]

---

# VIII. Why finite source separation is not finite equation closure

## 15. The selected centered equations

At every selected center

\[
h_j,
\]

the actual kernel identity is

\[
\boxed{
\mathscr D_{h_j}(\delta)f
+
\mathscr P_{h_j}(\delta)f
=
0,
}
\]

where \(\mathscr P_{h_j}\) is the finite sum of prime tent channels at

\[
h_j\pm\lambda.
\]

The source restriction near \(h_j\) is part of the singular diagonal carrier
of

\[
\mathscr D_{h_j}.
\]

Thus the detector that separates \(V\) appears precisely inside a new
logarithmic diagonal channel.

---

## 16. No inherited superflatness

Membership in

\[
W_\infty^{\rm inc}
\]

controls:

- the original right-visible hinge germs;
- the weighted first-layer ratio incidence outputs.

It does **not** imply that the local source germ at an arbitrary selected
center

\[
h_j\in\Gamma_c
\]

is superflat.

Nor does it imply that

\[
\mathscr D_{h_j}(\delta)f
\]

is superflat.

Therefore the finite selected-center equations do not yield a contradiction
from the existing collar-flatness data.

They merely relocate the surviving mass into the diagonal channels.

---

# IX. Natural arithmetic closure is dense

## 17. Recursive prime sampling

Starting from one selected center

\[
h\in\Gamma_c,
\]

the prime part samples locations

\[
h\pm\lambda
\]

with

\[
\lambda\in\mathscr H_c^\circ.
\]

These lie again in

\[
\Gamma_c.
\]

If one promotes those newly sampled germs to additional centers, the process
remains in

\[
\Gamma_c
\]

but, in the multi-prime regime, can generate a dense subset of \((0,L)\).

Thus:

\[
\boxed{
\text{recursive arithmetic closure of the movable-center system is dense}.
}
\]

This is the discrete arithmetic realization of the continuum-center
obstruction already identified geometrically in GERM-4.

---

# X. Finite detector versus natural closure

## 18. Two different statements

It is important to distinguish:

### Finite detector existence

For a fixed finite-dimensional obstruction \(V\),

\[
\boxed{
\text{some finite reachable center set separates }V.
}
\]

This is true.

### Finite natural closure

There exists a finite set of source carriers closed under all prime-delay
couplings and containing the ratio-incidence branch.

This is false in the generic multi-prime regime.

The arithmetic center lattice is dense.

Therefore the positive finite-dimensional extraction is noncanonical and does
not define a finite closed Weil subsystem.

---

# XI. Abstract finite-center no-go

## 19. One new diagonal channel per selected center

Suppose one selects finitely many centers

\[
h_1,\ldots,h_M.
\]

At the local carrier level, each equation has the form

\[
\boxed{
\text{diagonal channel at }h_j
=
-\text{finite prime-shift combination}.
}
\]

Unless the diagonal source germs are independently controlled, each selected
center introduces one new local principal carrier capable of absorbing the
finite arithmetic combination.

This is exactly the failure already seen in:

- GERM-4 for arbitrary movable centers;
- GERM-5 for ordinary regularity bootstrap;
- GERM-20 for one-cell Stieltjes quasi-analyticity.

Thus finite center selection alone does not cross the existing
quasi-analyticity barrier.

---

# XII. Impact on the incidence kernel

## 20. What has been gained

The ratio-incidence cancellation is not invisible to the full source.

Every nonzero vector in

\[
W_\infty^{\rm inc}
\]

is detected by finitely many reachable arithmetic center neighborhoods.

So the incidence kernel is not an independent hidden sector.

It necessarily carries source mass at finitely many selected movable centers.

---

## 21. What remains missing

The current first-kind equation supplies only

\[
\mathscr D_{h_j}
=
-\mathscr P_{h_j}.
\]

There is no theorem converting nonzero local source mass near \(h_j\) into a
finite-order nonzero diagonal field.

Generic logarithmic/Stieltjes flatness countermodels show that such a
conversion cannot come from \(L^2\) locality alone.

Therefore the remaining statement is again kernel-restricted
log-diagonal rigidity.

---

# XIII. Result of this NF pass

The incidence-kernel log-diagonal test has a precise answer.

### Positive finite-dimensional result

Every ratio germ has a finite denominator-clearing ladder ending at a genuine
prime hinge.

In the multi-prime regime, reachable arithmetic centers form the dense group

\[
\boxed{
\Gamma_c
=
\sum_{p:\log p<L}
\mathbb Z\log p.
}
\]

For the finite-dimensional incidence branch

\[
W_\infty^{\rm inc},
\]

finitely many reachable centers already give an injective source detector.

### Negative closure result

Those selected equations necessarily introduce logarithmic diagonal carriers.

Recursive prime closure generates a dense set of centers rather than a finite
closed arithmetic graph.

Thus:

\[
\boxed{
\text{finite-dimensional center separation}
\not\Rightarrow
\text{finite Weil subsystem closure}.
}
\]

The incidence kernel is observable, but only through the same log-diagonal
species that has survived every previous route.

---

# XIV. Next traversal target

The next genuinely new target is

\[
\boxed{
\text{SZ-KERNEL-EDGE-GERM-24 / FINITE-CENTER DIAGONAL FILTRATION}.
}
\]

The next pass should take a finite reachable center detector

\[
\{h_1,\ldots,h_M\}
\]

for

\[
W_\infty^{\rm inc}
\]

and build a joint flatness filtration for the corresponding diagonal channels

\[
\mathscr D_{h_j}(\delta)f.
\]

The target is to split the incidence branch into:

1. directions exposing a finite-order diagonal field at at least one selected
   center;
2. directions whose selected diagonal fields are all superflat.

The second branch would be a finite-dimensional, multi-center analogue of the
GERM-20 Stieltjes-flat counterspace.

The decisive question is whether simultaneous superflatness at finitely many
arithmetically related diagonal centers is still locally realizable.

No such finite-center diagonal filtration is proved in this pass.

---

# XV. Cursor status

The canonical theorem cursor remains

\[
\boxed{\text{SZ-CROSS-COLLAR-3}}.
\]

This is an unratified finite-center reduction / dense-closure no-go result.

No public promotion and no canonical cursor movement are asserted.
