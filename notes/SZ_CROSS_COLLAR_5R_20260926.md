# SZ-CROSS-COLLAR-5R — Background-or-selected sign transport

**Date:** 2026-09-26  
**Branch:** `sz-cross-collar`  
**Status:** UNRATIFIED RESIDUE / NF PASS  
**Canonical parent:** `SZ-CROSS-COLLAR-3`  
**Uses:** WD-T07, WD-T10, WD-T38; SZ-CROSS-COLLAR-4R only as optional
coordinate residue, not as a premise of the sign theorem.

## 0. Objective

The ratified Suzuki bridge gives, for a strict enlargement (b>c),

```math
\Lambda_{c,b;k}\ne0
\Longrightarrow
\exists x\in\mathcal F_b:
q_b(x)<0.
```

The unresolved question is whether this negative value belongs to the fixed
selected packet or can be attributed entirely to the unselected negative
background.

The wrong route is the forbidden converse

```text
full negativity => selected negativity.
```

The correct route is to **eliminate the background first**, using the exact
WD-T10 identity.

---

## 1. Full selected/background defect at enlarged support

Fix the same finite selected packet (Pi).

At support (b), write

```math
S_{+,b}:K_+\to H_b,
\qquad
S_{M,b}:M_\Pi\to H_b,
\qquad
S_{B,b}:B_\Pi\to H_b.
```

The full zero-side defect is

```math
D_{\mathrm{full},b}
=
S_{+,b}S_{+,b}^*
-
S_{M,b}S_{M,b}^*
-
S_{B,b}S_{B,b}^*.
```

Its quadratic form is

```math
Q_{\mathrm{full},b}(x)
=
\|S_{+,b}^*x\|^2
-
\|S_{M,b}^*x\|^2
-
\|S_{B,b}^*x\|^2.
```

Assume the Suzuki localized form (q_b) is carrier-identified with this full
compact-window Weil form:

```math
\boxed{
q_b(x)=Q_{\mathrm{full},b}(x).
}
```

This is a support-(b) carrier-identification hypothesis. Horizon 1 supplies
the analogous identification at the neutral endpoint (c); it does not by
itself assert the whole collar family.

---

## 2. Legitimate background elimination

Suppose the unselected background at support (b) admits a reduced
contractive screen:

```math
S_{B,b}
=
-
S_{+,b}X_{B,b},
\qquad
\|X_{B,b}\|\le1.
```

Define the residual budget

```math
R_{B,b}
=
I-X_{B,b}X_{B,b}^*
\succeq0
```

and effective positive synthesis

```math
S_{\mathrm{eff},b}
=
S_{+,b}R_{B,b}^{1/2}.
```

WD-T10 gives the exact operator identity

```math
\boxed{
D_{\mathrm{full},b}
=
S_{\mathrm{eff},b}S_{\mathrm{eff},b}^*
-
S_{M,b}S_{M,b}^*.
}
```

Therefore, pointwise,

```math
\boxed{
Q_{\mathrm{full},b}(x)
=
Q_{\mathrm{res},\Pi,b}(x),
}
```

where

```math
Q_{\mathrm{res},\Pi,b}(x)
:=
\|S_{\mathrm{eff},b}^*x\|^2
-
\|S_{M,b}^*x\|^2.
```

This is not the invalid converse from WD-T07. The background has been consumed
by an exact covariance identity before the sign is read.

---

## 3. Sign transport theorem under background admissibility

Assume

```math
\Lambda_{c,b;k}\ne0.
```

By the ratified SZ-CROSS-COLLAR-3 theorem, choose (x\in\mathcal F_b) with

```math
q_b(x)<0.
```

Under the support-(b) carrier identification and legitimate background
elimination,

```math
Q_{\mathrm{res},\Pi,b}(x)
=
Q_{\mathrm{full},b}(x)
=
q_b(x)
<0.
```

Hence

```math
\boxed{
\Lambda_{c,b;k}\ne0
+
\text{legitimate background elimination at }b
\Longrightarrow
\text{negative residual selected defect at }b.
}
```

Moreover,

```math
Q_{\mathrm{res},\Pi,b}(x)<0
```

forces

```math
\boxed{
S_{M,b}^*x\ne0,
}
```

because otherwise the residual form would be
(|S_{\mathrm{eff},b}^*x|^2\ge0).

So after legitimate background elimination the negative direction necessarily
uses the selected packet.

This is a genuine **residual selected-custody** statement.

---

## 4. What has and has not been localized

The result localizes the sign to the selected sector **after** the unselected
background has been legitimately consumed.

It does not yet prove that

```math
S_{M,b}^*x
```

equals the endpoint coordinate

```math
u=S_{M,c}^*k.
```

Thus two different questions must remain separate:

### Sign custody

```text
Does the negative enlarged residual defect require the selected sector?
```

Under legitimate background elimination, **yes**.

### Source identity

```text
Is the selected coordinate/raw residue source exactly the same source as at
the endpoint?
```

That requires the coordinate-naturality statement of SZ-CROSS-COLLAR-4R plus,
for the perturbed negative vector, a selected-preserving perturbation or another
source-transport theorem.

This NF pass does not claim source identity.

---

## 5. Failure of background elimination is itself typed

Suppose the background cannot be legitimately eliminated at support (b).

Then at least one of the WD-T10 prerequisites fails. In particular, one cannot
supply a reduced map satisfying both

```math
S_{B,b}=-S_{+,b}X_{B,b}
```

and

```math
\|X_{B,b}\|\le1.
```

This splits naturally into the WD-T04-style failure types:

1. **background range defect** — the unselected background is not exactly
   screenable through the positive synthesis; or
2. **background over-budget defect** — exact screening exists but requires
   norm (>1).

Either case is already a mathematically typed obstruction. It is not legitimate
to continue calling the ensuing full negativity “selected-owned.”

So cross-collar nonpersistence produces the following conditional dichotomy:

```math
\boxed{
\begin{array}{c}
\Lambda_{c,b;k}\ne0
\\[1mm]
\Downarrow
\\[1mm]
\begin{cases}
\text{background screen remains admissible}
&
\Rightarrow
\text{negative residual selected defect},
\\[1mm]
\text{background screen ceases to be admissible}
&
\Rightarrow
\text{background screening obstruction}.
\end{cases}
\end{array}
}
```

This is the correct replacement for the rejected
“full negativity implies selected custody” inference.

---

## 6. Relation to the terminal rank-one normal form

Horizon 1 records that the rank-one cell operator

```math
\mathcal K_C(b)
=
\widetilde S_b\widetilde S_b^*
-
\widetilde g_C\otimes\widetilde g_C
```

appears only **after**

1. permitted background elimination,
2. complement shorting where required, and
3. retention of the residual selected negative source.

Therefore, if the Suzuki (q_b) family can be identified on a collar with this
terminal normal form for the same selected cell, then the first branch above
has already been implemented: negativity of (q_b) is negativity of the
residual selected-cell defect by definition.

What is not supplied by Horizon 1 is a theorem that the endpoint terminal
normal form persists as the same legitimate reduction for every
(b\downarrow c).

---

## 7. New exact bridge obligation

The surviving support-dependent issue is therefore not “custody” in the
abstract.

It is:

```text
SZ-BACKGROUND-ELIMINATION-COLLAR
```

> For the fixed selected packet used by the attained neutral endpoint mode,
> does the legitimate unselected-background elimination/shorting that produces
> the endpoint residual defect remain valid on a strict right collar?

Concretely, one needs either:

```math
S_{B,b}
=
-
S_{+,b}X_{B,b},
\qquad
\|X_{B,b}\|\le1
```

with the required reduced-solution/shorting hypotheses for (b>c) near (c),

or a theorem showing that their failure is itself incompatible with the
actual-zeta configuration under consideration.

This is strictly more precise than asking whether a negative full form value
has selected ownership.

---

## 8. Result of this NF pass

The selected-defect sign problem is reduced to a **background-elimination
stability problem**:

```math
\boxed{
\text{cross-collar leakage}
+
\text{collar-stable legitimate background elimination}
\Longrightarrow
\text{negative residual selected defect}.
}
```

If collar-stable elimination fails, the failure is typed as a background
range/over-budget obstruction rather than silently reassigned to the selected
packet.

No fixed negative margin, representative blow-up, WD-T37 entry, or same-source
claim follows from this pass.

---

## 9. Candidate follow-on if ratified

```text
SZ-BACKGROUND-ELIMINATION-COLLAR / STABILITY AUDIT
```

A future NF should determine whether the background factorization and
contractivity used at the endpoint are open/stable under Suzuki support
variation, or whether a first loss of that property yields an independent
actual-zeta obstruction.

**No canonical cursor movement is asserted by this residue.**
