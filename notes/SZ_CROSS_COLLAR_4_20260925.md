# SZ-CROSS-COLLAR-4 — Selected-coordinate factorization residue (not custody)

**Date:** 2026-09-25  
**Branch:** `sz-cross-collar`  
**Status:** AUDITED RESIDUE / NOT RATIFIED — 2026-09-26  
**Depends on:** `SZ_CROSS_COLLAR_3_20260925.md`, WD-T38 / P3-U2

**Ratification decision:** The finite-dimensional factorization lemma is
correct, but the application does **not** establish selected-sector negativity
or selected ownership. Holding the selected coordinate fixed is weaker than
proving that the selected defect itself is negative. This note is preserved as
useful residue and is excluded from the canonical theorem spine.

## 0. Objective

The full form-domain cross-collar theorem gives

```math
\Lambda_{c,b;k}(h)
=
q_b(E_{c,b}k,h).
```

If this functional is nonzero, strict enlargement is already indefinite.

That conclusion alone is not enough for the Horizon-1 negative morphology,
because aggregate negativity does not determine selected-packet ownership.

This pass asks whether the negative perturbation can be made while keeping the
finite selected coordinate fixed.

---

## 1. Selected-coordinate map

In the WD-T38 finite-exception neutral realization,

```math
N_c=-P_cC_c
```

and Lean certifies

```math
N_c^*k=-u,
\qquad
u\ne0.
```

Thus the natural physical-to-selected-coordinate map is

```math
\sigma_c(h):=-N_c^*h.
```

At the endpoint,

```math
\boxed{
\sigma_c(k)=u.
}
```

For a strict enlargement (b>c), let

```math
\sigma_b:\mathcal F_b\to M
```

denote the corresponding fixed-packet selected-coordinate map.

The bridge requires the explicit **selected-coordinate consistency**
hypothesis

```math
\boxed{
\sigma_b(E_{c,b}k)=u.
}
```

This is not supplied by abstract form-domain nesting alone. It must come from
the carrier identification of the same fixed selected packet across the
support enlargement.

A perturbation (h\in\mathcal F_b) is **selected-preserving** when

```math
\boxed{
\sigma_b(h)=0.
}
```

Then

```math
\sigma_b(Ek+t h)=u
```

for every scalar (t).

---

## 2. Abstract finite-dimensional dichotomy

Let (X) be a complex vector space, (M) a finite-dimensional complex
vector space,

```math
\sigma:X\to M
```

linear, and

```math
\Lambda:X\to\mathbb C
```

linear.

Exactly one of the following structural alternatives holds.

### A. Selected-coordinate-preserving coupling

There exists

```math
h\in\ker\sigma
```

such that

```math
\Lambda(h)\ne0.
```

### B. Finite selected factorization

```math
\Lambda|_{\ker\sigma}=0.
```

Then (Lambda) factors uniquely through (operatorname{im}\sigma):

```math
\boxed{
\Lambda=\ell\circ\sigma
}
```

for a unique

```math
\ell:\operatorname{im}\sigma\to\mathbb C.
```

The proof is elementary: define

```math
\ell(\sigma x):=\Lambda(x).
```

Vanishing on (ker\sigma) is exactly the condition needed for this to be
well-defined.

Because (M) is finite-dimensional, alternative B compresses the entire
cross-collar functional to finite selected data.

---

## 3. Application to the neutral collar

Take

```math
X=\mathcal F_b,
\qquad
\sigma=\sigma_b,
\qquad
\Lambda(h)=q_b(Ek,h).
```

The old neutral mode satisfies

```math
q_b(Ek)=0
```

and, under selected-coordinate consistency,

```math
\sigma_b(Ek)=u\ne0.
```

### Alternative A

Suppose there exists selected-preserving (h) with

```math
q_b(Ek,h)\ne0,
\qquad
\sigma_b(h)=0.
```

Choose a unit complex phase (omega) so that

```math
\operatorname{Re}
\bigl(
\omega q_b(Ek,h)
\bigr)<0.
```

Then for sufficiently small (t>0),

```math
q_b(Ek+t\omega h)<0,
```

while

```math
\boxed{
\sigma_b(Ek+t\omega h)=u.
}
```

Thus the enlarged negative test vector retains the **same nonzero selected
packet coordinate**.

This is a coordinate-preservation statement only. It does not imply

```math
Q_{\Pi,b}(Ek+t\omega h)<0,
```

and therefore does not by itself establish selected-sector ownership of the
negative full Weil value.

To feed this directly into WD-T37 still requires the carrier-specific
statement that (q_b) is the same selected/residual defect used by the
fixed-packet morphology and that the perturbed vector is admissible in its
analysis space.

---

## 4. Alternative B: leakage factors through the packet

Suppose instead

```math
q_b(Ek,h)=0
\qquad
\forall h\in\ker\sigma_b.
```

Then

```math
\boxed{
q_b(Ek,h)
=
\ell(\sigma_b h)
}
```

for a linear functional

```math
\ell:\operatorname{im}\sigma_b\to\mathbb C.
```

But

```math
0
=
q_b(Ek)
=
\ell(\sigma_b(Ek))
=
\ell(u).
```

Hence

```math
\boxed{
\ell(u)=0.
}
```

So even when no selected-preserving cross direction exists, the entire
failure of persistence is confined to selected-coordinate directions
transverse to the endpoint coordinate (u).

Equivalently, (ell) descends to

```math
\boxed{
\operatorname{im}\sigma_b
/
\mathbb C u.
}
```

The cross-collar obstruction therefore loses at least one selected degree of
freedom.

---

## 5. Rank-one closure

Assume

```math
\dim_{\mathbb C}M=1.
```

Because

```math
u\ne0
```

and

```math
u\in\operatorname{im}\sigma_b,
```

we have

```math
\operatorname{im}\sigma_b=M=\mathbb C u.
```

In alternative B,

```math
\ell(u)=0
```

therefore forces

```math
\ell=0.
```

Thus

```math
\Lambda=0,
```

and by SZ-CROSS-COLLAR-3 the endpoint neutral mode persists:

```math
\boxed{
Ek\in\ker A_b.
}
```

Consequently, for a rank-one selected packet and a support-consistent selected
coordinate map, there are only two possibilities:

```math
\boxed{
\begin{array}{ll}
\textbf{(P)}&
\text{the old neutral mode persists exactly},\\[1mm]
\textbf{(N)}&
\text{there exists an enlarged negative perturbation}
\\
&\text{with the same nonzero selected coordinate }u.
\end{array}
}
```

There is no third **algebraic cross-functional** alternative in rank one.
This is not yet a selected-custody dichotomy: the negative perturbation may
still owe its sign to changes in the positive compensator or unselected
background.

---

## 6. Higher selected rank

For

```math
m:=\dim_{\mathbb C}M<\infty,
```

alternative B leaves a factorization through at most

```math
\boxed{
m-1
}
```

selected dimensions:

```math
\operatorname{im}\sigma_b/\mathbb C u.
```

Thus one attained endpoint neutral coordinate eliminates one selected leakage
degree.

If a neutral endpoint kernel supplies selected coordinates spanning a subspace

```math
U\subseteq M,
```

and the old-old form pairing vanishes on that whole neutral kernel, then the
same factorization argument forces the leakage functional to annihilate (U).
The residual selected obstruction is confined to

```math
M/U.
```

In particular, if the endpoint neutral selected coordinates span all of
(M), alternative B collapses and exact persistence follows.

This multi-mode statement requires a common selected-coordinate map and should
be formulated carefully before theorem status is assigned.

---

## 7. Relation to Horizon-1 custody

This pass does **not** use the false converse

```text
full negativity => selected negativity.
```

Instead it asks a stronger, correctly typed question:

```text
Can the negative perturbation be produced inside
the kernel of selected-coordinate change?
```

If yes, the selected coordinate is preserved by construction, but selected
negativity is not established.

If no, the cross functional factors through finite selected-coordinate data.

Neither branch alone supplies the Horizon-1 custody conclusion.

This is exactly the information that a lowest-eigenvalue trajectory by itself
forgets.

---

## 8. Proposed residue interface (noncanonical)

The only new carrier-specific datum needed to instantiate the abstract
dichotomy is the strict-support selected-coordinate map

```math
\boxed{
\sigma_b:\mathcal F_b\to M
}
```

with

```math
\boxed{
\sigma_b(Ek)=u.
}
```

Call this bridge obligation

```text
SZ-SELECTED-COORD-CONSISTENCY
```

It is conceptually smaller than the original null-extension interface:
identify the same fixed selected packet coordinate under support enlargement.

Even if this map is available, rank-one selected packets yield only a
persistence-or-selected-coordinate-preserving-negative-perturbation dichotomy.
A separate selected-defect sign statement is still required before any custody
claim or WD-T37 re-entry.

---

## 9. Unratified proposed handoff

```text
SZ-CROSS-COLLAR-5 / SELECTED-COORDINATE CONSISTENCY
```

Targets:

1. identify (sigma_b) in the actual compact-window Weil realization;
2. determine whether zero extension preserves the selected raw residue
   coordinate automatically for a fixed off-line pair/quartet packet;
3. separate the dependence of the positive compensator from the fixed negative
   packet coordinate;
4. if consistency is automatic, instantiate the rank-one dichotomy and test
   direct re-entry into WD-T37.

This handoff is not canonical and does not move the ratified cursor beyond
SZ-CROSS-COLLAR-3.

**Do not promote to the public repository.**
