# SZ-CROSS-COLLAR-3 — Full form-domain cross-collar theorem

**Date:** 2026-09-25  
**Branch:** `sz-cross-collar`  
**Status:** PRIVATE LAB / INTERNAL DERIVATION  
**Depends on:** Horizon-1 neutral interface; Suzuki arXiv:2606.09096v3

## 0. Correction of emphasis

The explicit (G_a)-coordinate results in SZ-CROSS-COLLAR-0/1/2 require a
regular derivative source

```math
u=Dk\in L_0^2.
```

That coordinate may fail for a general neutral mode because Suzuki's
self-adjoint domain is strictly larger than (H_0^1).

However, the **cross-collar mechanism itself does not require that
regularity**.

Suzuki defines the closed localized form directly by

```math
q_a:=Q_W^{,a}=Q_W|_{L^2(-a,a)}
```

with form domain

```math
\mathcal F_a:=\mathfrak D(q_a)
=
\{v\in L^2(-a,a):|q_a(v)|<\infty\}.
```

This gives an exact full-domain formulation.

---

## 1. Zero-extension nesting of form domains

Fix

```math
0<c<b
```

and let

```math
E_{c,b}:L^2(-c,c)\hookrightarrow L^2(-b,b)
```

be zero extension.

If

```math
k\in\mathcal F_c,
```

then the same global compactly supported function satisfies

```math
q_b(E_{c,b}k)=q_c(k).
```

In particular the value is finite, so

```math
\boxed{
E_{c,b}\mathcal F_c
\subseteq
\mathcal F_b.
}
```

Thus zero extension is legitimate at the native closed-form level.

This uses only that the localized forms are restrictions of the same global
Weil form.

---

## 2. Endpoint null mode

Assume

```math
0\ne k\in\ker A_c.
```

By the representation theorem for the closed form associated with (A_c),

```math
q_c(k,\phi)=0
\qquad
\forall\phi\in\mathcal F_c.
```

Let

```math
\widetilde k:=E_{c,b}k.
```

Then

```math
q_b(\widetilde k)=q_c(k)=0.
```

Moreover, for every old test direction

```math
\phi\in\mathcal F_c,
```

one has

```math
\boxed{
q_b(\widetilde k,E_{c,b}\phi)
=
q_c(k,\phi)
=
0.
}
```

So the endpoint null mode already annihilates the entire old form domain after
enlargement.

Only genuinely new support directions can detect failure of persistence.

---

## 3. Cross-collar functional on the quotient

Define the new-direction quotient

```math
\mathcal Q_{c,b}
:=
\mathcal F_b/
E_{c,b}\mathcal F_c.
```

For (h\in\mathcal F_b), define

```math
\boxed{
\Lambda_{c,b;k}([h])
:=
q_b(\widetilde k,h).
}
```

This is well-defined on the quotient because adding an old direction changes
the pairing by

```math
q_b(\widetilde k,E\phi)=0.
```

Therefore the full native neutral interface is

```math
\boxed{
\Lambda_{c,b;k}
\text{ on }
\mathcal Q_{c,b}.
}
```

No (H^1), pointwise trace, or derivative-source hypothesis is required.

---

## 4. Exact persistence criterion

The closed-form representation theorem gives

```math
\boxed{
\widetilde k\in\ker A_b
\iff
q_b(\widetilde k,h)=0
\quad
\forall h\in\mathcal F_b.
}
```

Since the old directions already vanish, this becomes

```math
\boxed{
\widetilde k\in\ker A_b
\iff
\Lambda_{c,b;k}\equiv0
\text{ on }\mathcal Q_{c,b}.
}
```

Thus `AZ-FIN-WEIL-NULL-EXTENSION` is exactly a quotient cross-coupling
problem on the **full** Suzuki form domain.

The (G_a) collar residual from the preceding notes is a concrete
realization of this functional on the regular (H_0^1/L_0^2) carrier.

---

## 5. Nonzero cross coupling forces negativity

Assume

```math
\Lambda_{c,b;k}\ne0.
```

Choose (h\in\mathcal F_b) with

```math
q_b(\widetilde k,h)\ne0.
```

Choose a complex phase (omega) so that

```math
\operatorname{Re}
\bigl(
\omega q_b(\widetilde k,h)
\bigr)
<0.
```

For sufficiently small (t>0),

```math
\begin{aligned}
q_b(\widetilde k+t\omega h)
&=
q_b(\widetilde k)
+
2t\operatorname{Re}
\bigl(
\omega q_b(\widetilde k,h)
\bigr)
+
t^2q_b(h)\\
&<0.
\end{aligned}
```

Therefore

```math
\boxed{
\Lambda_{c,b;k}\ne0
\Longrightarrow
\lambda_b<0.
}
```

This implication holds at the native closed-form level.

---

## 6. Zero plateau forces exact persistence

If

```math
\lambda_b=0,
```

then (q_b) is nonnegative.

Since

```math
q_b(\widetilde k)=0,
```

Cauchy-Schwarz for the nonnegative form gives

```math
q_b(\widetilde k,h)=0
\qquad
\forall h\in\mathcal F_b.
```

Hence

```math
\boxed{
\lambda_b=0
\Longrightarrow
\Lambda_{c,b;k}=0
\Longrightarrow
\widetilde k\in\ker A_b.
}
```

Also, because (widetilde k) itself is an admissible zero-valued trial
vector,

```math
\boxed{
\lambda_b\le0
}
```

for every strict enlargement after the endpoint null mode has formed.

Thus a localized neutral mode cannot be followed by a return to strict
positivity under support enlargement.

---

## 7. Relation to the regular (G_a) carrier

If additionally

```math
k\in H_0^1(-c,c),
\qquad
u=Dk\in L_0^2(-c,c),
```

then the full quotient functional admits the explicit screw-potential
coordinate developed in SZ-CROSS-COLLAR-0:

```math
\Lambda
\longleftrightarrow
r_{c,b;u}
=
F_u-C_u
\text{ on the new collar}.
```

The hierarchy is therefore:

```text
full form-domain cross functional     [always available]
            |
            | extra H_0^1 regularity
            v
continuous screw-potential residual   [explicit spatial coordinate]
            |
            | endpoint trace regularity
            v
logarithmic collar jet                [conditional asymptotic]
```

The general theorem does not depend on the lower two levels.

---

## 8. What this does and does not close

This result proves:

```math
\boxed{
\text{failure of neutral null persistence}
\Longrightarrow
\text{strict enlarged Weil negativity}.
}
```

It does **not** yet identify the ownership of that new negative direction.

In particular, full negativity alone does not imply that the original selected
finite packet owns the negativity; Horizon 1 explicitly separates selected
custody from aggregate negativity.

Therefore this result does not automatically re-enter WD-T37.

The next task is to preserve selected-packet custody through the cross-collar
perturbation.

---

## 9. Next cursor

```text
SZ-CROSS-COLLAR-4 / SELECTED-CUSTODY LIFT
```

Target:

Let the endpoint neutral mode come from the WD-T38 finite selected packet.
Restrict the quotient cross functional to **selected-preserving new support
directions**.

Determine whether:

1. the restricted functional is nonzero, in which case one can create enlarged
   negativity without changing the selected packet coordinate; or
2. it vanishes identically, in which case the cross coupling is forced through
   directions that alter selected custody and must be analyzed separately.

This is the point where the Suzuki spatial collar should reconnect to the
Horizon-1 selected/background calculus.

**Do not promote to the public repository.**
