# SZ-CROSS-COLLAR-4R — Raw selected-coordinate naturality

**Date:** 2026-09-26  
**Branch:** `sz-cross-collar`  
**Status:** UNRATIFIED RESIDUE / NF PASS  
**Canonical parent:** `SZ-CROSS-COLLAR-3`  
**Purpose:** recover the valid coordinate-consistency content suggested by
SZ-CROSS-COLLAR-4/5 without importing the rejected custody inference.

## 0. Scope

This pass asks only:

> When the support window grows from (c) to (b>c), does zero extension of
> an old physical vector preserve its coordinate in one fixed selected packet?

No sign-ownership statement is claimed.

In particular,

```text
same selected coordinate
```

is **not** identified with

```text
selected packet owns the negative full Weil value.
```

That converse remains forbidden by Horizon 1.

---

## 1. Abstract support-restriction setup

Let

```math
E:H_c\to H_b
```

be a bounded embedding of the smaller physical carrier into the larger one.
For the compact-support model, (E) is zero extension and (E^*) is
restriction back to the smaller window.

Let (M) be the fixed finite selected coefficient space and let

```math
S_b:M\to H_b,
\qquad
S_c:M\to H_c
```

be the selected synthesis maps at the two supports.

Assume only the exact restriction-compatibility law

```math
\boxed{
S_c=E^*S_b.
}
```

This says that the smaller-window selected synthesis is obtained by
restricting the same fixed selected modes from the larger window.

---

## 2. Adjoint naturality lemma

Taking adjoints gives

```math
S_c^*
=
(E^*S_b)^*
=
S_b^*E.
```

Therefore, for every (h\in H_c),

```math
\boxed{
S_b^*(Eh)=S_c^*h.
}
```

Thus the selected adjoint coordinate is **exactly preserved** by zero
extension whenever the selected synthesis family is restriction-compatible.

No compactness, positivity, screening, or zeta-specific estimate is used.

This is an operator identity.

---

## 3. Finite packet version

For a fixed finite packet

```math
\Pi
```

with coefficient space

```math
M_\Pi,
```

write

```math
S_{\Pi,b}:M_\Pi\to H_b,
\qquad
S_{\Pi,c}:M_\Pi\to H_c.
```

If

```math
S_{\Pi,c}=E^*S_{\Pi,b},
```

then

```math
\boxed{
S_{\Pi,b}^*E
=
S_{\Pi,c}^*.
}
```

Hence an endpoint vector (k\in H_c) with selected coordinate

```math
u:=S_{\Pi,c}^*k
```

satisfies

```math
\boxed{
S_{\Pi,b}^*(Ek)=u
}
```

for every strict enlargement (b>c) on which the same selected packet is
used.

This is the exact support-consistency statement required at the **raw selected
coordinate** level.

---

## 4. Direct compact-window realization

Suppose a selected coordinate is represented by pairing against one fixed
global mode (m_\rho).

Let

```math
m_{\rho,a}
=
m_\rho|_{(-a,a)}.
```

For (h\in L^2(-c,c)), zero extension gives

```math
\begin{aligned}
\langle Eh,m_{\rho,b}\rangle_{(-b,b)}
&=
\int_{-b}^{b}
(Eh)(x)\overline{m_\rho(x)}\,dx\\
&=
\int_{-c}^{c}
h(x)\overline{m_\rho(x)}\,dx\\
&=
\langle h,m_{\rho,c}\rangle_{(-c,c)}.
\end{aligned}
```

So for synthesis built from restrictions of fixed global modes, the
restriction-compatibility hypothesis above is automatic.

The finite packet result follows componentwise.

This is the correct sense in which the selected **raw zero coordinate** is
support-independent.

---

## 5. Pair and residue coordinates

WD-T20's pair diagonalization is finite-dimensional algebra on the selected
zero coordinates and contains no support parameter.

Likewise WD-T26's map from a selected negative pair coefficient (alpha) to
its antisymmetric raw residues

```math
(\alpha,-\alpha)
```

is support-independent.

Therefore, once the raw selected coordinate (u) is preserved,

```math
\boxed{
\text{its associated raw selected residue source }v
\text{ is preserved as well.}
}
```

In particular, the zero-moment law

```math
\mathbf 1^Tv=0
```

remains attached to the same source under support enlargement.

---

## 6. What this pass does not prove

This pass does **not** prove that a negative enlarged full-Weil perturbation has
negative selected defect.

Specifically, from

```math
S_{\Pi,b}^*x=u\ne0
```

and

```math
Q_W(x)<0
```

one may not infer

```math
Q_{\Pi,b}(x)<0.
```

The sign may still be supplied by:

- the changed positive compensator;
- unselected negative background;
- or both.

So the rejected SZ-CROSS-COLLAR-4 custody inference remains rejected.

---

## 7. Result of this NF pass

The candidate bridge obligation called

```text
SZ-SELECTED-COORD-CONSISTENCY
```

reduces to the exact operator identity

```math
\boxed{
S_{\Pi,c}=E^*S_{\Pi,b}
\Longrightarrow
S_{\Pi,b}^*E=S_{\Pi,c}^*.
}
```

For compact-window synthesis by restrictions of fixed global selected modes,
the premise is satisfied directly.

Thus the **coordinate-consistency problem is algebraic rather than analytic**.

The remaining unsolved custody question is strictly stronger:

```text
Does collar-induced full negativity produce negativity of the selected defect
itself, after the support-dependent positive/background terms are separated?
```

That question is not answered in this pass.

---

## 8. Candidate follow-on if ratified

```text
SZ-CROSS-COLLAR / SELECTED-DEFECT SIGN TRANSPORT
```

A future NF should compare the enlarged polarized/full form with the selected
defect decomposition while holding the ratified raw selected coordinate fixed.

**No canonical cursor movement is asserted by this residue.**
