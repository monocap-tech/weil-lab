# SZ-CROSS-COLLAR-5 — Selected-coordinate consistency

**Date:** 2026-09-25  
**Branch:** `sz-cross-collar`  
**Status:** PRIVATE LAB / INTERNAL DERIVATION  
**Depends on:** `SZ_CROSS_COLLAR_4_20260925.md`, WD-B4, WD-T38

## 0. Objective

Discharge, or reduce to a finite-dimensional normalization issue, the bridge
obligation

```text
SZ-SELECTED-COORD-CONSISTENCY
```

introduced in SZ-CROSS-COLLAR-4.

The issue is whether zero extension of the endpoint neutral mode changes the
coordinate of the same fixed selected off-axis packet.

---

## 1. The selected packet itself does not move with support

The Horizon-1 specialization fixes a finite packet

```math
\Pi
```

and a finite negative coefficient space

```math
M_\Pi\subset K_-.
```

The support parameter changes the physical synthesis maps and the positive
screening problem, but it does not change the abstract packet coordinate
space.

This is already built into the specialization:

```text
M_Π = selected finite packet's negative channels
B_Π = unselected off-axis negative divisor
A_{Π,t} = selected analysis space at support t.
```

Thus support variation changes the analysis relation, not the identity of the
selected zero coordinates.

---

## 2. Background elimination preserves the selected synthesis

WD-B4 is decisive here.

After legitimate elimination of a contractively screened negative background,

```math
D_{\rm full}
=
S_{\rm eff}S_{\rm eff}^{*}
-
S_MS_M^{*}.
```

Only the positive synthesis changes:

```math
S_+
\longmapsto
S_{\rm eff}.
```

The selected negative synthesis

```math
S_M
```

is **not replaced**.

The subsequent screening map (Y) is defined by

```math
S_M=-S_{\rm eff}Y.
```

Hence the WD-T38 notation

```math
N_c=-P_cC_c
```

should be read as a factorization of the retained selected negative synthesis,
not as creation of a new negative channel.

This is the exact reason the selected coordinate can retain custody through
background elimination.

---

## 3. Raw zero coordinates are support-consistent under zero extension

In the compact-window realization, every selected zero channel comes from a
fixed global exponential/Fourier-evaluation mode.

For a global mode (m_\rho), let

```math
m_{\rho,a}
```

denote its restriction to the support interval ((-a,a)).

The selected coefficient of (f\in L^2(-a,a)) is represented by the pairing

```math
\sigma_{\rho,a}(f)
=
\langle f,m_{\rho,a}\rangle.
```

If (0<c<b) and (E_{c,b}f) is zero extension, then

```math
\begin{aligned}
\sigma_{\rho,b}(E_{c,b}f)
&=
\int_{-b}^{b}
(E_{c,b}f)(x)\overline{m_\rho(x)}\,dx\\
&=
\int_{-c}^{c}
f(x)\overline{m_\rho(x)}\,dx\\
&=
\sigma_{\rho,c}(f).
\end{aligned}
```

Therefore, componentwise for the whole fixed packet,

```math
\boxed{
\sigma_{\Pi,b}E_{c,b}
=
\sigma_{\Pi,c}.
}
```

Equivalently, the Fourier transform of the zero-extended physical test is the
same entire transform, so evaluation at every fixed selected zero is
unchanged.

Suzuki's interval convention is exactly compatible with this: functions in
(L^2(-a,a)) are viewed as zero-extended functions on (L^2(\mathbb R)), and
his Fourier formulas use that zero extension.

Thus support consistency is **automatic for canonical raw zero coordinates**.

---

## 4. Pair diagonalization and raw residues are also support-independent

The maps

```math
\text{raw conjugate-pair coordinates}
\longleftrightarrow
\text{positive/negative pair coordinates}
```

in WD-T20 are finite-dimensional algebraic maps depending only on the chosen
zero pair.

Likewise, WD-T26 sends a selected negative pair coefficient (alpha) to raw
residues proportional to

```math
(\alpha,-\alpha).
```

Neither construction contains the support parameter.

Hence

```math
\boxed{
\text{fixed selected coordinate}
\Longrightarrow
\text{fixed selected raw residue source}
}
```

under zero-extension support enlargement.

This is important for later re-entry into the WD-T37 arithmetic chain.

---

## 5. What can still vary: residual normalization

The terminal rank-one specialization is written

```math
\mathcal K_C(t)
=
\widetilde S_t\widetilde S_t^*
-
\widetilde g_C\otimes\widetilde g_C.
```

It is obtained only after positive/background elimination and shorting.

The underlying selected negative cell remains the same raw packet channel, but
a chosen **normalized residual coordinate** may acquire a support-dependent
finite-dimensional change of basis.

Therefore there are two coordinate levels:

### Canonical/raw coordinate

```math
\sigma^{\rm raw}_{\Pi,b}E
=
\sigma^{\rm raw}_{\Pi,c}.
```

This is automatic.

### Residual normalized coordinate

Write

```math
\sigma^{\rm res}_{\Pi,a}
=
T_a\sigma^{\rm raw}_{\Pi,a},
```

where

```math
T_a:M_\Pi\to M_\Pi
```

is the finite-dimensional coordinate transport induced by the chosen residual
normalization.

Then

```math
\boxed{
\sigma^{\rm res}_{\Pi,b}E
=
T_bT_c^{-1}
\sigma^{\rm res}_{\Pi,c}
}
```

whenever (T_c,T_b) are invertible on the active selected sector.

Thus the unresolved part of selected-coordinate consistency is at worst a
finite-dimensional transport problem, not an analytic support problem.

For a rank-one residual cell,

```math
T_bT_c^{-1}
```

is just multiplication by a nonzero scalar.

---

## 6. Coordinate-free custody formulation

SZ-CROSS-COLLAR-4 asked for the literal identity

```math
\sigma_b(Ek)=u.
```

That is stronger than necessary.

The custody dichotomy only requires a **fixed identification of the selected
sector across support**.

Use canonical raw coordinates and set

```math
u_{\rm raw}
:=
\sigma^{\rm raw}_{\Pi,c}(k).
```

Then automatically

```math
\boxed{
\sigma^{\rm raw}_{\Pi,b}(Ek)
=
u_{\rm raw}\ne0.
}
```

Selected-preserving perturbations are simply

```math
h\in
\ker\sigma^{\rm raw}_{\Pi,b}.
```

This removes support-dependent residual normalization from the custody
question completely.

The rank-one dichotomy of SZ-CROSS-COLLAR-4 therefore applies directly in
canonical raw packet coordinates.

---

## 7. Rank-one terminal consequence

Assume the terminal selected sector is one-dimensional after the legitimate
Horizon-1 reductions.

Then, at every strict enlargement (b>c), exactly one of the following holds:

1. the endpoint neutral mode remains an exact enlarged null mode; or
2. there exists an enlarged negative perturbation whose canonical selected
   raw coordinate is **exactly the same nonzero coordinate** as at the
   endpoint.

Symbolically,

```math
\boxed{
\text{rank-one endpoint neutral}
\Longrightarrow
\begin{cases}
\text{null persistence},\\
\text{same-cell custody-preserving negativity}.
\end{cases}
}
```

No additional analytic theorem is needed merely to identify the selected
coordinate.

The analytic burden has moved entirely into deciding whether the cross-collar
functional vanishes.

---

## 8. Higher-rank consequence

For a finite packet with

```math
m=\dim M_\Pi>1,
```

the raw-coordinate consistency is still automatic.

If no selected-preserving cross direction exists, SZ-CROSS-COLLAR-4 confines
the leakage to

```math
M_\Pi/\mathbb C u.
```

This is a genuine finite-dimensional residual packet problem.

For a simple functional-equation quartet the unreduced negative pair count is
two, so one neutral selected coordinate leaves at most one transverse selected
leakage direction before any further parity/cell reduction.

---

## 9. Status of the bridge obligation

```text
SZ-SELECTED-COORD-CONSISTENCY
```

is therefore:

```math
\boxed{
\text{SOLVED at canonical raw zero-coordinate level;}
}
```

with only optional finite-dimensional bookkeeping required to translate to a
particular normalized residual coordinate system.

This is not a new actual-zeta interface.

---

## 10. Next cursor

```text
SZ-CROSS-COLLAR-6 / RANK-ONE REENTRY
```

Target:

1. formulate the rank-one persistence-or-negative dichotomy directly in the
   terminal WD-A5/WD-B4 residual defect;
2. determine whether the custody-preserving negative perturbation already
   satisfies the support-filtration hypotheses needed to enter WD-T37;
3. if yes, connect failure of Suzuki null persistence to
   `AZ-NEXTJET-LOC`;
4. if no, isolate the exact missing filtration hypothesis.

**Do not promote to the public repository.**
