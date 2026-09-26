# SZ-BACKGROUND-ELIMINATION-COLLAR-0 — Stability audit

**Date:** 2026-09-26  
**Branch:** `sz-cross-collar`  
**Status:** UNRATIFIED RESIDUE / NF PASS  
**Canonical parent:** `SZ-CROSS-COLLAR-3`  
**Immediate parent residue:** `SZ_CROSS_COLLAR_5R_20260926.md`

## 0. Objective

Determine when the unselected-background elimination used at the endpoint
remains legitimate for strict support enlargements.

The previous residue formulated this in terms of a factorization

```math
S_{B,b}=-S_{+,b}X_{B,b},
\qquad
\|X_{B,b}\|\le1.
```

For stability, the better object is the covariance difference

```math
\boxed{
K_B(b)
:=
S_{+,b}S_{+,b}^*
-
S_{B,b}S_{B,b}^*.
}
```

By WD-T02 / Douglas,

```math
\boxed{
K_B(b)\succeq0
}
```

is equivalent to contractive background screening, assuming the standard
Douglas theorem interface for the pair.

Thus collar stability is a positivity-stability problem.

---

## 1. Common-carrier formulation

Because the physical support spaces vary with (b), an operator-norm
continuity statement must first put them in one Hilbert carrier.

Assume a common Hilbert space (mathscr H) and isometric embeddings

```math
J_b:H_b\hookrightarrow\mathscr H
```

have been fixed, compatibly with zero extension/restriction.

Transport the background covariance defect to (mathscr H):

```math
\widehat K_B(b)
:=
J_b K_B(b)J_b^*.
```

The exact choice of common carrier is not important for the abstract lemma;
what matters is that all support-(b) covariance defects are compared in one
operator norm.

---

## 2. Strict endpoint slack is open

Assume there exists

```math
\eta>0
```

such that

```math
\boxed{
\widehat K_B(c)\succeq\eta I
}
```

on the relevant common-carrier subspace.

Assume also right operator-norm continuity:

```math
\boxed{
\|\widehat K_B(b)-\widehat K_B(c)\|\to0
\qquad
(b\downarrow c).
}
```

Choose (b>c) close enough that

```math
\|\widehat K_B(b)-\widehat K_B(c)\|
<
\frac{\eta}{2}.
```

For every unit vector (h),

```math
\begin{aligned}
\langle \widehat K_B(b)h,h\rangle
&=
\langle \widehat K_B(c)h,h\rangle
+
\langle
(\widehat K_B(b)-\widehat K_B(c))h,h
\rangle
\\
&\ge
\eta
-
\|\widehat K_B(b)-\widehat K_B(c)\|
\\
&>
\frac{\eta}{2}.
\end{aligned}
```

Hence

```math
\boxed{
\widehat K_B(b)\succeq\frac{\eta}{2}I
}
```

for all sufficiently small strict enlargements.

Therefore the background remains contractively screenable on a right collar.

This avoids proving norm continuity of the Douglas reduced solution itself.

---

## 3. Equivalent strict-screening formulation

If the background reduced solution exists at the endpoint and satisfies

```math
\|X_{B,c}\|=r<1,
```

then WD-A4 gives a uniform positive screening margin on the corresponding
background analysis problem.

However, the inequality

```math
\|X_{B,c}\|<1
```

alone is not enough to transfer the screen to nearby support values unless the
support family is controlled.

One still needs a common-carrier continuity statement for the background
covariance defect, or another theorem that controls the nearby reduced
solutions.

Thus the stable datum is:

```math
\boxed{
\text{strict background slack}
+
\text{right common-carrier continuity}.
}
```

---

## 4. Semidefinite endpoint screening is not open

Suppose only

```math
\widehat K_B(c)\succeq0
```

with no positive lower gap.

No collar stability follows from this alone.

The scalar model already shows the failure:

```math
\widehat K_B(c)=0,
\qquad
\widehat K_B(b)=-(b-c)I
\quad (b>c).
```

Then

```math
\widehat K_B(b)\to\widehat K_B(c)
```

in operator norm, but every strict enlargement is negative.

Therefore even operator-norm continuity does not preserve background
screenability at a saturated endpoint.

The missing datum is precisely a positive spectral gap away from the
background-screening boundary.

---

## 5. First-loss parameter

Assume the common-carrier family

```math
b\longmapsto\widehat K_B(b)
```

is operator-norm continuous on a right interval.

Define the background lower edge

```math
\beta_B(b)
:=
\inf_{\|h\|=1}
\langle\widehat K_B(b)h,h\rangle.
```

For bounded self-adjoint operators,

```math
|\beta_B(b)-\beta_B(c)|
\le
\|\widehat K_B(b)-\widehat K_B(c)\|.
```

Hence (eta_B) is continuous.

Background screening is legitimate exactly when

```math
\beta_B(b)\ge0.
```

If it is valid at (c) and fails at some later support, continuity gives a
first boundary value (b_*) with

```math
\boxed{
\beta_B(b_*)=0.
}
```

Thus first loss of legitimate background elimination cannot jump directly
from strict positivity to negative background defect under norm-continuous
support variation; it passes through a **background critical boundary**.

---

## 6. What the critical boundary means

At

```math
\beta_B(b_*)=0,
```

two distinct infinite-dimensional possibilities remain.

### Attained background criticality

There exists (0\ne h) with

```math
\langle\widehat K_B(b_*)h,h\rangle=0.
```

Then the background screening problem has an actual neutral direction.

If the corresponding reduced screening problem has finite negative domain, or
otherwise attains its critical norm, this is the WD-A4 attained-neutral
boundary.

### Non-attained background criticality

The infimum is zero but no nonzero vector attains it.

Then the background may sit at the WD-A4 approximate-neutral boundary.

Thus the first loss of background elimination is itself a complete screening
morphology:

```math
\boxed{
\text{background criticality}
=
\text{attained neutral}
\quad\text{or}\quad
\text{non-attained approximate neutral},
}
```

before any later range/over-budget failure is entered.

This is more precise than classifying only the already-failed support value.

---

## 7. Interaction with the Suzuki collar crossing

Combine this stability audit with SZ-CROSS-COLLAR-5R.

If

```math
\Lambda_{c,b;k}\ne0,
```

then the enlarged full Weil form is negative.

There are now two structurally different regimes.

### Regime A — background has strict slack at the endpoint

If

```math
\widehat K_B(c)\succeq\eta I
```

and the background covariance family is right operator-norm continuous, then
background elimination remains valid on some strict collar.

Therefore any Suzuki cross-collar leakage occurring inside that collar gives

```math
\boxed{
\text{negative residual selected defect}.
}
```

The background cannot be the first obstruction there.

### Regime B — no background gap

If the endpoint background covariance is only semidefinite, Horizon 1 does not
prevent the background from becoming critical or negative immediately to the
right.

Then selected sign transport cannot be asserted until the background boundary
is resolved.

The neutral selected mode and the background screening boundary may coincide.

---

## 8. Exact surviving interface

The previous broad interface

```text
SZ-BACKGROUND-ELIMINATION-COLLAR
```

splits into two sharply typed questions:

```text
SZ-BG-COV-CONT
```

**Common-carrier continuity:** is
(b\mapsto\widehat K_B(b)) right operator-norm continuous for the actual
compact-window zeta background?

and

```text
SZ-BG-GAP
```

**Endpoint gap:** does the endpoint background covariance satisfy a strict
positive lower bound on the relevant carrier?

If both hold, background elimination is automatically collar-stable.

If continuity holds but the gap fails, the background itself lies on a
screening boundary and must be treated as a competing critical morphology.

---

## 9. What Horizon 1 supplies

Horizon 1 supplies:

- the exact background/selected decomposition;
- Douglas equivalence between covariance positivity and contractive screening;
- residual-budget elimination once a contractive screen is available;
- the complete abstract critical morphology for a screening problem.

It does **not** supply:

- operator-norm continuity of the actual support-dependent background
  covariance family;
- a strict positive background gap at the neutral selected endpoint.

Therefore neither `SZ-BG-COV-CONT` nor `SZ-BG-GAP` may be silently assumed.

---

## 10. Result of this NF pass

The background-stability problem has been reduced to an ordinary perturbation
criterion:

```math
\boxed{
\widehat K_B(c)\succeq\eta I
\quad+\quad
\widehat K_B(b)\to\widehat K_B(c)
\text{ in operator norm}
\Longrightarrow
\text{collar-stable background elimination}.
}
```

Without the gap, even norm continuity is insufficient.

Hence the next actual obstruction is not an unspecified failure of the
Douglas map. It is one of:

```math
\boxed{
\text{lack of common-carrier norm continuity},
\qquad
\text{or}
\qquad
\text{background criticality at the endpoint}.
}
```

No claim is made that either obstruction occurs for actual zeta.

---

## 11. Candidate follow-on if ratified

```text
SZ-BG-COV-CONT / ACTUAL COMPACT-WINDOW CONTINUITY
```

A future NF should determine the strongest topology in which the actual
positive/background covariance family varies with support, and whether it is
strong enough to preserve a strict background gap.

**No canonical cursor movement is asserted by this residue.**
