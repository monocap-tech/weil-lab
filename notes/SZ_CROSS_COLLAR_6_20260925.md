# SZ-CROSS-COLLAR-6 — Correct rank-one re-entry

**Date:** 2026-09-25  
**Branch:** `sz-cross-collar`  
**Status:** PRIVATE LAB / INTERNAL DERIVATION  
**Depends on:** SZ-CROSS-COLLAR-3--5, WD-T04, WD-T05, WD-T38

## 0. Correction

The previous cursor proposed direct re-entry from Suzuki collar failure into
WD-T37.

That is too strong.

WD-T37 begins with the specific boundary-amplification morphology

```math
\varepsilon_n\to0,
\qquad
[z_n,z_n]_J\to-\kappa<0
```

after normalization by a vanishing selected amplitude.

The Suzuki collar perturbation has the opposite local feature:

- the endpoint selected coordinate is nonzero;
- raw selected-coordinate custody is preserved under zero extension;
- the negative perturbations can be chosen with that same nonzero selected
  coordinate;
- as the support shrinks back to the critical endpoint, these negative
  directions return to the attained neutral mode.

So the collar branch is a **critical spectral crossing**, not the WD-T37
vanishing-amplitude entry morphology.

---

## 1. Correct abstract landing point

In the terminal rank-one residual defect, write

```math
D_b
=
S_bS_b^*
-
g\otimes g,
```

where (g) is the fixed residual selected negative source and (S_b) is the
effective positive synthesis after legitimate background elimination/shorting.

At the critical support (c), WD-T38 supplies an attained neutral mode.

In rank-one screening coordinates this is the WD-T04 attained-critical branch:

```math
\|X_c\|=1
```

with an actual norm-attaining direction.

If strict support enlargement fails to preserve that null relation,
SZ-CROSS-COLLAR-3--5 supplies a negative direction carrying the same raw
selected cell.

The correct screening taxonomy is therefore:

```math
\boxed{
\text{attained critical at }c
\quad\longrightarrow\quad
\text{negative rank-one defect at }b>c.
}
```

When exact range inclusion remains valid, this is the WD-T04 **over-budget**
branch

```math
\|X_b\|>1.
```

If range inclusion itself fails, it is instead the WD-T04 range-defect branch.

Thus the first re-entry is WD-T04/WD-T05, not WD-T37.

---

## 2. Why WD-T37 does not follow automatically

Let (x_b) be custody-preserving negative perturbations with

```math
x_b\to k
```

as (b\downarrow c).

Their selected raw coordinate remains

```math
u\ne0.
```

After ordinary unit normalization, the coefficient signature may satisfy

```math
J(x_b)\uparrow0
```

rather than tending to a fixed negative margin.

This is exactly compatible with the attained-neutral side of WD-C4.

Nothing here forces the normalized fixed-margin hypothesis

```math
J(z_n)\to-\kappa,
\qquad
\kappa>0,
```

used in WD-T37.

Therefore no boundary-amplification or representative-blowup claim may be
imported merely from cross-collar nonpersistence.

---

## 3. What *does* survive from the WD-T37 arithmetic half

The selected coordinate is nevertheless a fixed nonzero vector

```math
u\in M_\Pi.
```

Undoing the support-independent pair diagonalization gives a fixed nonzero raw
selected source

```math
v.
```

WD-T26 applies independently of the size of the negative margin:

```math
\boxed{
\mathbf 1^Tv=0,
\qquad
v\ne0.
}
```

Hence the source-side arithmetic conclusions remain available:

```math
R_v(z)=O(|z|^{-2}),
```

the (O((\log R)/R)) far-tail theorem for fixed bounded
selected-preserving multipliers, and the weighted completed-(\Xi) next-jet
representation of the finite/intermediate complement.

These are source theorems. Their proofs do not require
(kappa>0).

What the fixed-margin morphology supplied was the **reason that this source
had to occur as a persistent endpoint negative defect**.

The Suzuki crossing supplies a different reason for the same fixed source to
remain load-bearing.

---

## 4. New morphology: first-crossing selected source

The Suzuki bridge therefore exposes a distinct configuration:

```math
\boxed{
\begin{array}{c}
\text{critical support }c,\\
0\ne k\in\ker A_c,\\
0\ne u=\sigma_\Pi(k),\\
\text{same raw source }v\text{ under strict enlargement},\\
\text{negative selected-cell defect for }b>c.
\end{array}
}
```

Call this the **first-crossing selected-source morphology**.

It is not a fourth Horizon-1 morphology; it is post-Horizon structure obtained
by combining the neutral stop with Suzuki's support family.

Its distinctive datum is not a fixed negative margin. It is the
**same selected source on both sides of the critical support**.

---

## 5. Arithmetic attachment without WD-T37 entry

For that fixed source (v), the following chain is still valid:

```math
\boxed{
v\ne0
\Longrightarrow
\mathbf1^Tv=0
\Longrightarrow
R_v(z)=O(|z|^{-2})
\Longrightarrow
\text{far-tail localization}
\Longrightarrow
\text{weighted near next-jet field}.
}
```

Thus the arithmetic object

```math
\mathcal N_{v,R}[\psi]
```

exists with the same fixed source across the collar crossing.

However, Horizon 1 does **not** provide a theorem identifying the Suzuki
cross-collar functional

```math
\Lambda_{c,b;k}
```

with a particular scalar or derivative of

```math
\mathcal N_{v,R}[\psi].
```

That identification is the real missing bridge.

---

## 6. New bridge target

Define the post-Horizon interface

```text
SZ-COLLAR-NEXTJET-LINK
```

to mean:

> Express the cross-collar functional generated by the critical neutral mode
> and its fixed selected source (v) in the zero-side/explicit-formula
> coordinates of the same source, isolating which part is carried by the near
> completed-(\Xi) next-jet field after the far tail is removed.

A successful identity would connect

```math
\boxed{
\text{physical-space collar leakage}
}
```

to

```math
\boxed{
\text{zero-space next-jet compensation}.
}
```

This would be a genuine spatialization of AZ-NEXTJET-LOC.

---

## 7. Why this target is preferable

Trying to force the collar branch into WD-T37 loses the distinction between:

- fixed-margin endpoint blow-up; and
- infinitesimal negative bifurcation from an attained neutral mode.

The new target preserves that distinction.

It also uses the strongest datum obtained from Suzuki:

```math
\text{the source }v\text{ is fixed while support changes}.
```

So the next question is no longer whether a selected source exists.

It is whether the **support derivative/cross block of its compensation** is
the same object already isolated as the weighted near next-jet field.

---

## 8. Next cursor

```text
SZ-CROSS-COLLAR-7 / COLLAR–NEXTJET IDENTIFICATION
```

Targets:

1. write the polarized Weil form (q_b(Ek,h)) simultaneously in:
   - Suzuki screw-kernel coordinates;
   - zero-side selected/complement coordinates;
   - explicit-formula prime/archimedean coordinates;
2. use selected-preserving (h) to remove direct variation of the fixed
   selected raw source;
3. identify the complementary-zero term as a functional of
   (R_v(\mu)), hence of the completed-(\Xi) next jets;
4. determine whether the far contribution inherits the existing
   (O((\log R)/R)) localization uniformly in a shrinking collar.

**Do not promote to the public repository.**
