# SZ-COLLAR-BRANCH-CLASSIFICATION-0 — Pointwise owner taxonomy

**Date:** 2026-09-26  
**Branch:** `sz-cross-collar`  
**Status:** UNRATIFIED RESIDUE / NF PASS  
**Canonical parent:** `SZ-CROSS-COLLAR-3`  
**Immediate parent residue:** `SZ_BG_RELATIVE_GAP_0_20260926.md`  
**Uses:** WD-A2–A5, WD-B1, WD-B4/WD-T10, WD-B5, WD-T37, WD-T39.

## 0. Objective

Classify the strict-support branches produced by the ratified Suzuki
cross-collar theorem without assuming continuity of Douglas maps.

Fix

```math
b>c
```

and assume cross-collar nonpersistence:

```math
\Lambda_{c,b;k}\ne0.
```

By SZ-CROSS-COLLAR-3,

```math
\boxed{
q_b\not\succeq0.
}
```

Assume the support-(b) carrier identification

```math
q_b
=
Q_{\mathrm{full},b}.
```

The task is to determine which negative sector can be assigned responsibility
without using the false converse

```text
full negativity => selected negativity.
```

---

## 1. First split: can the background be eliminated?

Write

```math
D_{\mathrm{full},b}
=
S_{+,b}S_{+,b}^*
-
S_{M,b}S_{M,b}^*
-
S_{B,b}S_{B,b}^*.
```

There are exactly two pointwise cases.

### Case BG-A — background admissible

There exists a contraction

```math
X_{B,b}:B_\Pi\to K_+
```

such that

```math
S_{B,b}
=
-
S_{+,b}X_{B,b}.
```

WD-T10 then defines

```math
S_{\mathrm{eff},b}
=
S_{+,b}
\left(I-X_{B,b}X_{B,b}^*\right)^{1/2}
```

and gives the exact identity

```math
\boxed{
D_{\mathrm{full},b}
=
S_{\mathrm{eff},b}S_{\mathrm{eff},b}^*
-
S_{M,b}S_{M,b}^*.
}
```

Since the left side is negative somewhere, the **residual selected defect**
is negative somewhere.

### Case BG-F — background inadmissible

No contractive exact factorization of (S_{B,b}) through (S_{+,b}) exists.

By WD-A2/A4 applied to the background screening problem itself, this is already
a background negative defect.

Thus the cross-collar branch has an exhaustive first owner split:

```math
\boxed{
\text{collar leakage}
\Longrightarrow
\begin{cases}
\text{residual selected defect},&
\text{if BG-A},\\
\text{background defect},&
\text{if BG-F}.
\end{cases}
}
```

The cases are mutually exclusive by definition.

---

## 2. Selected-residual branch: exact H1 classification

Assume BG-A.

Set

```math
D_{M|B,b}
:=
S_{\mathrm{eff},b}S_{\mathrm{eff},b}^*
-
S_{M,b}S_{M,b}^*.
```

We know

```math
D_{M|B,b}\not\succeq0.
```

Apply the WD-A4 taxonomy to the pair

```math
(S_{\mathrm{eff},b},S_{M,b}).
```

There are only two strict-negative possibilities.

### SR-R — selected residual range defect

```math
\boxed{
\operatorname{Ran}S_{M,b}
\not\subseteq
\operatorname{Ran}S_{\mathrm{eff},b}.
}
```

Then the selected packet cannot be exactly screened by the positive budget
remaining after the background has been paid.

### SR-B — selected residual over-budget defect

If range inclusion holds, let

```math
Y_b:M_\Pi\to K_+
```

be the Douglas reduced solution

```math
S_{M,b}
=
-
S_{\mathrm{eff},b}Y_b.
```

Then negativity forces

```math
\boxed{
\|Y_b\|>1.
}
```

Because (M_\Pi) is finite dimensional, WD-B5 sharpens this to a genuine
finite singular-value defect:

```math
\boxed{
\exists j:\sigma_j(Y_b)>1.
}
```

For a terminal rank-one selected cell, this is simply

```math
\boxed{
\|Y_b\|>1.
}
```

So in the background-admissible branch the collar crossing lands exactly in
the already-classified **selected range/over-budget** side of Horizon-1
screening theory.

No new sign morphology is needed.

---

## 3. Background-failure branch: exact H1 classification

Assume BG-F.

Apply WD-A4 directly to

```math
(S_{+,b},S_{B,b}).
```

Again there are only two strict-negative possibilities.

### BG-R — background range defect

```math
\boxed{
\operatorname{Ran}S_{B,b}
\not\subseteq
\operatorname{Ran}S_{+,b}.
}
```

The unselected background contains a physical direction not reproducible by
the positive synthesis.

### BG-B — background over-budget defect

If exact range inclusion holds, let (X_{B,b}) be the reduced solution. Then
background inadmissibility means

```math
\boxed{
\|X_{B,b}\|>1.
}
```

Thus the background branch is also not a new morphology: it lands in the
existing WD-A4 range/over-budget taxonomy, but with the **unselected
background** as the negative sector.

---

## 4. Four pointwise terminal cells

At a strict support (b>c) where the endpoint neutral mode fails to persist,
the complete pointwise owner classification is therefore

```math
\boxed{
\begin{array}{ll}
\textbf{SR-R}:&
\text{selected residual range defect},\\[1mm]
\textbf{SR-B}:&
\text{selected residual over-budget defect},\\[1mm]
\textbf{BG-R}:&
\text{background range defect},\\[1mm]
\textbf{BG-B}:&
\text{background over-budget defect}.
\end{array}
}
```

The first two occur after legitimate background elimination.

The second two occur because legitimate background elimination itself fails.

This classification is exhaustive at the abstract screening level.

It does not assert which cell actual zeta occupies.

---

## 5. Relation to WD-T37 negative morphology

The selected-residual cells SR-R/SR-B are **pointwise negative defects**.

They do not automatically satisfy the stronger sequential entry hypotheses of
WD-T37.

WD-T37 requires, along a sequence (b_n\downarrow c),

- a fixed selected packet;
- normalized selected vectors;
- a negative margin converging to
  [
  -\kappa
  ]
  with (kappa>0);
- the specific vanishing-amplitude/boundary-amplification setup.

A collar crossing can instead satisfy

```math
Q_{M|B,b_n}(x_n)<0
```

for every (n) while the normalized negative margin tends to zero as
(b_n\downarrow c).

That is an infinitesimal crossing into the selected-negative side, not the
fixed-margin P3-N1 morphology.

Therefore

```math
\boxed{
\text{SR-R/SR-B}
\not\Rightarrow
\text{WD-T37}.
}
```

If a uniform normalized negative margin is separately established, then the
existing WD-T37 machinery becomes available. Without it, no representative
blow-up or AZ-NEXTJET-LOC conclusion may be imported.

---

## 6. Relation to WD-T39 noncompact background morphology

Likewise BG-R/BG-B are **pointwise screening failures**.

They are not the same thing as the WD-T39 background-escape regimes

```text
B∞, BT, BF.
```

WD-T39 classifies the compactness behavior of a sequence of normalized
background coefficient vectors after a fixed selected negative ray has already
been anchored.

By contrast, BG-R/BG-B say that at one support the background itself cannot be
contractively screened through the positive channel.

Along a sequence (b_n\downarrow c), a BG branch may later refine into:

- norm escape of background screening coefficients;
- bounded weak/tail escape;
- or a bounded compact background limit.

But that requires a separately chosen coefficient sequence and the hypotheses
of WD-T39.

Therefore

```math
\boxed{
\text{BG-R/BG-B}
\not\Rightarrow
\text{WD-T39 background escape}.
}
```

The pointwise screening taxonomy sits **upstream** of the sequential
noncompactness taxonomy.

---

## 7. Boundary behavior as support returns to (c)

The endpoint itself is neutral:

```math
0\ne k\in\ker A_c.
```

Hence a sequence of strict supports

```math
b_n\downarrow c
```

may remain in any strict-negative pointwise cell while the amount of
negativity tends to zero.

This creates no new Horizon-1 morphology.

It is simply a support-parameter trajectory approaching an attained critical
boundary from a negative cell.

Schematically,

```text
SR-R or SR-B  ----                   >---- attained neutral endpoint
BG-R or BG-B  ----/
```

The endpoint does not determine which negative owner appears immediately to
the right.

---

## 8. What happens to source custody?

SZ-CROSS-COLLAR-4R showed that zero extension preserves the **endpoint**
selected raw coordinate under restriction-compatible synthesis.

That statement applies to (Ek).

The negative witness supplied by cross-collar leakage is generally

```math
Ek+t h,
```

and its selected coordinate is

```math
S_{M,b}^*(Ek)
+
tS_{M,b}^*h.
```

Unless

```math
S_{M,b}^*h=0,
```

the selected source changes.

Therefore the pointwise owner classification above does not yet identify one
fixed raw source across the negative collar.

This is why the arithmetic source chain from WD-T26 onward cannot yet be
attached automatically to the collar branch.

---

## 9. Exact post-Horizon branch map

Combining the ratified cross-collar theorem with the pointwise H1 screening
taxonomy gives

```math
\boxed{
\begin{array}{c}
0\ne k\in\ker A_c
\\
\downarrow\quad b>c
\\
\Lambda_{c,b;k}=0
\quad\text{or}\quad
\Lambda_{c,b;k}\ne0
\\
\begin{array}{c|c}
\Lambda=0 & \Lambda\ne0\\
\hline
Ek\in\ker A_b &
\begin{array}{c}
\text{BG admissible}\Rightarrow
\text{SR-R or SR-B},\\
\text{BG inadmissible}\Rightarrow
\text{BG-R or BG-B}.
\end{array}
\end{array}
\end{array}
}
```

So strict support enlargement has only:

1. **null persistence**, or
2. one of four already-typed screening defects.

There is no fifth anonymous “full negativity” branch once the background test
is performed.

---

## 10. What remains genuinely new

This classification reuses Horizon-1 completely for sign ownership.

The genuinely post-Horizon issues are now relational rather than taxonomic:

1. **carrier compatibility** — identify the Suzuki closed-form realization
   with the zero-side selected/background decomposition at strict support;
2. **source transport** — determine whether a negative collar witness can be
   chosen with the same raw selected source as the endpoint;
3. **branch exclusion** — determine what actual-zeta structure forbids, if
   anything, among SR-R, SR-B, BG-R, BG-B.

The first is the previously isolated

```text
SZ-CARRIER-METRIC-COMPAT.
```

The second is stronger than raw-coordinate naturality of the zero-extended
endpoint vector.

The third is where actual arithmetic must eventually enter.

---

## 11. Result of this NF pass

The collar crossing creates **no new abstract defect morphology**.

Once each strict support is tested pointwise, every failure of null persistence
lands in an existing Horizon-1 screening cell:

```math
\boxed{
\text{SR-R},\ \text{SR-B},\ \text{BG-R},\ \text{BG-B}.
}
```

WD-T37 and WD-T39 remain downstream sequential refinements and cannot be
entered merely from pointwise negativity.

This is the exact branch classification requested by the preceding cursor.

---

## 12. Candidate follow-on if ratified

```text
SZ-CARRIER-METRIC-COMPAT / STRICT-SUPPORT IDENTIFICATION
```

A future NF should determine whether the Suzuki localized closed Weil form and
the native zero-side selected/background defect are the same support-(b)
form on a common dense core, with enough closure control to transfer the
pointwise branch classification to Suzuki's (A_b).

**No canonical cursor movement is asserted by this residue.**
