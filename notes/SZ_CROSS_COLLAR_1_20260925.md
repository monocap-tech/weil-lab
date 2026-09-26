# SZ-CROSS-COLLAR-1 — Spatial residual controls spectral drop

**Date:** 2026-09-25  
**Branch:** `sz-cross-collar`  
**Status:** RATIFIED / CANONICAL — 2026-09-26  
**Depends on:** `SZ_CROSS_COLLAR_0_20260925.md`

**Ratification:** The explicit collar residual identity, the spectral-drop
trial-vector lemma, and the one-way implication
(Delta_{c,b}(u)>0Rightarrowlambda_b<0) are canonical. The displayed
numerical bound is retained as a non-optimized quantitative estimate.

## 0. Objective

Convert the Suzuki cross-collar residual into a quantitative statement about the
lowest localized Weil eigenvalue.

The point is to connect the spatially typed obstruction

```math
r_{c,b;u}
```

to Suzuki's scalar evolution observable

```math
\lambda_b.
```

---

## 1. Setup

Let

```math
H_a=L_0^2(-a,a),
\qquad
G_a=P_aGP_a,
```

as in Suzuki.

Fix (0<c<b), let

```math
J:=J_{c,b}:H_c\hookrightarrow H_b
```

be zero extension, and assume

```math
0\ne u\in\ker G_c.
```

Define

```math
F_u(x)=\int_{-c}^{c}g(x-y)u(y)\,dy
```

and let (C_u) be its constant value on ((-c,c)).

On the collar

```math
\mathcal C_{c,b}=(-b,-c)\cup(c,b)
```

define

```math
r(x):=r_{c,b;u}(x)=F_u(x)-C_u.
```

---

## 2. Explicit enlarged residual vector

Since

```math
G_bJu=P_bF_u,
```

the enlarged operator residual can be written explicitly.

Set

```math
\mu
:=
\frac{1}{2b}
\int_{\mathcal C_{c,b}}r(x)\,dx.
```

Then

```math
\boxed{
(G_bJu)(x)
=
\begin{cases}
-\mu,
& |x|<c,\\
r(x)-\mu,
& x\in\mathcal C_{c,b}.
\end{cases}
}
```

Indeed, the average of (F_u) over ((-b,b)) is

```math
C_u+\mu,
```

and (P_b) subtracts precisely this average.

Consequently,

```math
\boxed{
\|G_bJu\|_2^2
=
\|r\|_{L^2(\mathcal C_{c,b})}^2
-
\frac{1}{2b}
\left|
\int_{\mathcal C_{c,b}}r(x)\,dx
\right|^2.
}
```

Define the **cross-collar defect**

```math
\boxed{
\Delta_{c,b}(u)
:=
\|G_bJu\|_2.
}
```

Then

```math
\Delta_{c,b}(u)=0
\iff
G_bJu=0
\iff
r_{c,b;u}\equiv0.
```

This is the canonical norm of the new-support coupling.

---

## 3. Elementary spectral-drop lemma

Write

```math
h:=G_bJu.
```

Because (u\in\ker G_c),

```math
\langle G_bJu,Ju\rangle=0.
```

Assume (h\ne0), and let

```math
M_b:=\|G_b\|>0.
```

Choose

```math
z
:=
Ju-M_b^{-1}h.
```

Then

```math
\begin{aligned}
\langle G_bz,z\rangle
&=
-\frac{2}{M_b}\|h\|^2
+
\frac{1}{M_b^2}\langle G_bh,h\rangle\\
&\le
-\frac{1}{M_b}\|h\|^2.
\end{aligned}
```

Therefore

```math
\boxed{
\langle G_bz,z\rangle
\le
-\frac{\Delta_{c,b}(u)^2}{\|G_b\|}
<0.
}
```

The strict negativity itself implies (z\ne0). Thus the cross-collar defect
is not merely qualitative: it supplies an explicit negative trial direction.

---

## 4. Transfer to Suzuki's generalized eigenvalue

Suzuki defines

```math
K_b=(-\Delta_N)^{-1}
```

on (H_b) and rewrites the localized Weil Rayleigh quotient as

```math
\frac{\langle G_bw,w\rangle}
{\langle K_bw,w\rangle}.
```

The operator (K_b) is positive. Its operator norm on the zero-mean Neumann
space is

```math
\boxed{
\|K_b\|
=
\left(\frac{2b}{\pi}\right)^2,
}
```

because the first nonzero Neumann eigenvalue on an interval of length (2b)
is ((\pi/(2b))^2).

Hence

```math
\langle K_bz,z\rangle
\le
\left(\frac{2b}{\pi}\right)^2
\|z\|^2.
```

Also,

```math
\|z\|
\le
\|u\|
+
\frac{\Delta_{c,b}(u)}{\|G_b\|}.
```

Therefore the generalized Rayleigh quotient of (z) satisfies

```math
\boxed{
\lambda_b
\le
-
\frac{
\Delta_{c,b}(u)^2
}{
\|G_b\|
\left(\frac{2b}{\pi}\right)^2
\left(
\|u\|
+
\frac{\Delta_{c,b}(u)}{\|G_b\|}
\right)^2
}
<0.
}
```

whenever

```math
\Delta_{c,b}(u)>0.
```

The numerical constant is not currently optimized. Its role is to show that
the spatial residual gives an explicit spectral drop.

---

## 5. Exact one-way implication

We therefore have

```math
\boxed{
\Delta_{c,b}(u)>0
\Longrightarrow
\lambda_b<0.
}
```

Equivalently,

```math
\boxed{
\lambda_b=0
\Longrightarrow
\Delta_{c,b}(u)=0.
}
```

The converse is **not** asserted:

```math
\lambda_b<0
```

can coexist with

```math
G_bJu=0,
```

because an enlarged operator may have both a negative eigenspace and a
separate zero eigenspace.

Thus the correct relation is one-way.

---

## 6. Interpretation

Suzuki tracks

```math
b\longmapsto\lambda_b.
```

The Weil traversal identifies the spatial variable hidden behind a downward
departure from zero:

```math
\boxed{
\Delta_{c,b}(u)
=
\|G_bJ_{c,b}u\|.
}
```

At an endpoint neutral mode,

```math
\lambda_c=0.
```

If the old mode acquires any nonzero coupling to the newly available support
directions, the ground-state energy is forced strictly negative.

So the bridge is now

```math
\boxed{
\text{new collar coupling}
\Longrightarrow
\text{negative spectral motion}.
}
```

This is the precise sense in which the spatial decomposition can aim Suzuki's
parameter evolution.

---

## 7. Small-collar target

The remaining problem is to understand the asymptotic behavior

```math
\Delta_{c,c+\varepsilon}(u)
\qquad
(\varepsilon\downarrow0).
```

Since

```math
\Delta_{c,b}(u)^2
=
\|r\|_2^2
-
\frac{1}{2b}
\left|\int r\right|^2,
```

the target is now completely local to the two thin collars.

The questions are:

1. can (Delta_{c,c+\varepsilon}(u)) vanish identically for all sufficiently
   small (\varepsilon>0)?
2. if not, what is its first nonzero order in (\varepsilon)?
3. can that order be bounded below using the exterior Cauchy-transform term in
   the distributional formula for (-g'')?
4. how do prime-power thresholds alter that first nonzero collar order?

---

## 8. Historical handoff

```text
SZ-CROSS-COLLAR-2 / FIRST NONZERO COLLAR JET
```

Goal:

Extract the first nonzero small-(\varepsilon) term of
(Delta_{c,c+\varepsilon}(u)), or prove that vanishing of every collar jet
forces a stronger rigidity condition on (u).

This was the original proposed handoff from SZ-CROSS-COLLAR-1. The ratified
canonical head after review is SZ-CROSS-COLLAR-3; this historical handoff does
not itself advance the live cursor.

**Do not promote to the public repository.**
