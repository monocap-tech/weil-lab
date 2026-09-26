# SZ-PRECOND-FORM-BRIDGE-1 — Exact regular-core derivative bridge

**Date:** 2026-09-26  
**Branch:** \`sz-cross-collar\`  
**Status:** UNRATIFIED RESIDUE / NF PASS  
**Canonical parent:** \`SZ-CROSS-COLLAR-3\`  
**Immediate parent residue:** \`SZ_CARRIER_METRIC_COMPAT_0_20260926.md\`  
**External pin:** Masatoshi Suzuki, *Weil's quadratic form via the screw function*,
arXiv:2606.09096v3, §§8.1–8.5, especially (8.6)–(8.7).

## 0. Objective

Derive the exact PFB-1 common-core preconditioner.

The previous residue correctly rejected a boundedly invertible equivalence
between the compact auxiliary Problem-1 covariance realization and Suzuki's
unbounded localized Weil operator.

This pass identifies the exact bridge Suzuki actually proves.

The result is simpler:

\`\`\`math
\boxed{
T_a=D=i\,\frac{d}{dx}.
}
\`\`\`

But this bridge goes from the regular localized Weil form on
\(H_0^1(-a,a)\) to Suzuki's screw-kernel operator \(G_a\) on
\(L_0^2(-a,a)\).

It does **not** directly identify the repo's auxiliary
\(H^{-1}_{-\partial^2+1/4}\) synthesis metric with \(G_a\).

---

## 1. Suzuki's regular carriers

For \(a>0\), let

\`\`\`math
D
=
i\,\frac{d}{dx}
:
H_0^1(-a,a)
\longrightarrow
L_0^2(-a,a).
\`\`\`

Suzuki proves that \(D\) is bijective.

If the \(H_0^1\) norm is taken to be the derivative norm,

\`\`\`math
\|v\|_{H_0^1,*}
:=
\|v'\|_{L^2},
\`\`\`

then \(D\) is an isometric isomorphism:

\`\`\`math
\boxed{
\|Dv\|_{L^2}
=
\|v\|_{H_0^1,*}.
}
\`\`\`

Let

\`\`\`math
G_a
=
P_aGP_a
:
L_0^2(-a,a)
\to
L_0^2(-a,a)
\`\`\`

be Suzuki's compact screw-kernel operator.

---

## 2. Exact quadratic identity

Suzuki's equation (8.6) gives, for

\`\`\`math
v\in C_c^\infty(-a,a),
\`\`\`

the exact identity

\`\`\`math
\boxed{
Q_W(v)
=
\langle G_aDv,Dv\rangle_{L^2}.
}
\`\`\`

Equivalently, on this regular core,

\`\`\`math
Q_W
=
D^*G_aD
\`\`\`

in quadratic-form notation.

This is the concrete form of the symmetric operator

\`\`\`math
B_a
=
D^*G_aD,
\qquad
\mathfrak D(B_a)=H_0^1(-a,a),
\`\`\`

whose Friedrichs extension is Suzuki's \(A_a\).

---

## 3. Polarized identity

Both sides define Hermitian sesquilinear forms.

Therefore the diagonal identity polarizes.

For

\`\`\`math
v_1,v_2
\in
C_c^\infty(-a,a),
\`\`\`

one obtains

\`\`\`math
\boxed{
Q_W(v_1,v_2)
=
\langle
G_aDv_1,
Dv_2
\rangle_{L^2}.
}
\`\`\`

By the regular \(H_0^1\) extension used in Suzuki's construction, the same
identity holds on the regular form carrier wherever both sides are defined.

Thus PFB-1 for the **full Weil form** is not conjectural:

\`\`\`text
PFB-1 / FULL CORE POLARIZATION — DISCHARGED on Suzuki's regular carrier.
\`\`\`

No fractional Green power has to be guessed.

---

## 4. The inverse Neumann Laplacian has a different role

Suzuki also introduces

\`\`\`math
K_a
=
(-\Delta_N)^{-1}
\`\`\`

on \(L_0^2(-a,a)\).

Its role is not to define the Weil numerator.

Instead, if

\`\`\`math
u=Dv,
\`\`\`

then

\`\`\`math
\boxed{
\|v\|_{L^2}^2
=
\langle K_au,u\rangle_{L^2}.
}
\`\`\`

Therefore Suzuki's localized \(L^2\) Rayleigh quotient becomes

\`\`\`math
\boxed{
\frac{Q_W^a(v)}
{\|v\|_{L^2}^2}
=
\frac{
\langle G_au,u\rangle
}{
\langle K_au,u\rangle
},
\qquad
u=Dv.
}
\`\`\`

This yields the generalized eigenvalue problem

\`\`\`math
G_au
=
\lambda K_au.
\`\`\`

At \(\lambda=0\), only

\`\`\`math
G_au=0
\`\`\`

remains.

This is exactly why the ratified cross-collar null analysis can be performed
using \(G_a\).

---

## 5. Critical distinction from the repo's auxiliary Green metric

Horizon 1 also introduced a different operator:

\`\`\`math
L_D
=
-\partial_x^2+\frac14
\`\`\`

with Dirichlet boundary conditions, and its inverse

\`\`\`math
R_D
=
L_D^{-1}.
\`\`\`

The associated auxiliary norm is

\`\`\`math
\|f\|_{H^{-1}_{L_D}}^2
=
\langle f,R_Df\rangle.
\`\`\`

This is the metric used in WD-T28 to prove inverse-height decay,
Hilbert-Schmidt synthesis, and trace-class covariance.

It is **not** Suzuki's \(G_a\).

It is also **not** Suzuki's

\`\`\`math
K_a=(-\Delta_N)^{-1}.
\`\`\`

The three objects have different functions:

\`\`\`text
G_a
    = Weil/screw quadratic numerator;

K_a=(-Δ_N)^{-1}
    = pullback of the L² denominator through D;

R_D=(-∂²+1/4)_D^{-1}
    = auxiliary Dirichlet resolvent used by the repo's compactness estimate.
\`\`\`

Conflating them would create a false carrier bridge.

---

## 6. Correction to the previous PFB framing

The previous residue proposed a schematic identity

\`\`\`math
D_a^{\rm P1}
=
T_a^*A_aT_a.
\`\`\`

That is too coarse if \(D_a^{\rm P1}\) denotes the repo's
\(H^{-1}_{L_D}\)-metric covariance defect.

The exact Suzuki identity is instead

\`\`\`math
\boxed{
B_a
=
D^*G_aD
}
\`\`\`

on \(H_0^1(-a,a)\), followed by Friedrichs closure

\`\`\`math
B_a
\leadsto
A_a.
\`\`\`

So PFB-1 splits into two different questions:

### PFB-1S — Suzuki regular-core bridge

\`\`\`math
Q_W(v_1,v_2)
=
\langle G_aDv_1,Dv_2\rangle.
\`\`\`

**Status:** discharged by Suzuki (8.6) plus polarization.

### PFB-1H — Horizon auxiliary-metric bridge

Relate the repo's \(H^{-1}_{L_D}\) zero-side channel covariance model to the
\(G_a\) form on \(L_0^2(-a,a)\), if such a relation exists with the channel
decomposition preserved.

**Status:** open.

Only PFB-1H is a project-specific comparison problem.

---

## 7. What can already move across the Suzuki bridge

For every regular \(v\in H_0^1(-a,a)\), writing

\`\`\`math
u=Dv,
\`\`\`

the sign is exactly preserved:

\`\`\`math
\boxed{
Q_W(v)<0
\iff
\langle G_au,u\rangle<0,
}
\`\`\`

and likewise for equality and positivity.

Thus on the regular carrier, there is no remaining **full-sign** compatibility
problem between Suzuki's localized Weil form and \(G_a\).

In particular, the cross-collar residual

\`\`\`math
G_bJ_{c,b}u
\`\`\`

really is a regular-coordinate representation of the same Weil-form
null-persistence problem.

This validates the conceptual relation used in
SZ-CROSS-COLLAR-0/1 without invoking the auxiliary \(H^{-1}_{L_D}\) metric.

---

## 8. What does not move yet: owner labels

The selected/background decomposition

\`\`\`math
K_-
=
M_\Pi\oplus B_\Pi
\`\`\`

belongs to the zero-side coefficient representation.

Suzuki's \(G_a\) is the **total** screw-kernel operator.

Equation (8.6) identifies the full form, but does not by itself decompose
\(G_a\) as

\`\`\`math
\text{positive covariance}
-
\text{selected covariance}
-
\text{background covariance}
\`\`\`

in the Hilbert metric used by the Horizon screening calculus.

Therefore

\`\`\`text
PFB-3 / CHANNEL CUSTODY
\`\`\`

remains open.

This is now the only bridge needed to transfer the pointwise owner labels
SR-R / SR-B / BG-R / BG-B to Suzuki's strict-support carrier.

---

## 9. Relation to closure

Suzuki's Theorem 1.1 states that

\`\`\`math
A_a
\`\`\`

is the Friedrichs extension of

\`\`\`math
B_a=D^*G_aD.
\`\`\`

So the **full-form closure problem** is already handled in Suzuki's theory.

For the full Weil form, PFB-2 is therefore substantially discharged by the
Friedrichs-extension theorem and the form-core results surrounding it.

What remains project-specific is not closure of the total Weil form, but
closure/compatibility of any proposed **channelwise decomposition**.

Thus the three-part bridge should be revised to:

\`\`\`text
PFB-1S  full regular-core identity        — CLOSED externally
PFB-2S  full Friedrichs/form closure      — CLOSED externally
PFB-3H  Horizon channel-custody bridge    — OPEN internally
PFB-1H  auxiliary H^{-1}_L comparison     — optional/open unless needed
\`\`\`

---

## 10. Practical consequence for the collar traversal

The ratified Suzuki branch and the full Weil sign no longer need a generic
"carrier metric compatibility" placeholder.

For full sign:

\`\`\`math
\boxed{
Q_W(v)
=
\langle G_aDv,Dv\rangle
}
\`\`\`

on the regular carrier, and Suzuki supplies the closed extension.

The unresolved step is specifically:

> recover the Horizon positive / selected-negative / background-negative
> ownership decomposition inside the \(G_a\) representation, or prove an
> equivalent channelwise polarization identity.

That target is strictly narrower than the previous carrier-compatibility
interface.

---

## 11. Result of this NF pass

PFB-1 has split and partially closed:

\`\`\`math
\boxed{
\text{Suzuki full-form PFB-1 is exact with }T_a=D.
}
\`\`\`

The exact identity is

\`\`\`math
\boxed{
Q_W(v_1,v_2)
=
\langle G_aDv_1,Dv_2\rangle_{L^2}.
}
\`\`\`

The auxiliary Dirichlet-resolvent metric used by WD-T28 is a separate
compactness device and must not be substituted for \(G_a\) or \(K_a\).

Accordingly, the principal remaining bridge is now

\`\`\`text
SZ-PRECOND-FORM-BRIDGE / CHANNEL CUSTODY
\`\`\`

rather than full-form carrier compatibility.

---

## 12. Candidate follow-on if ratified

\`\`\`text
SZ-PRECOND-FORM-BRIDGE / PFB-3 CHANNEL CUSTODY
\`\`\`

A future NF should attempt to derive the positive/negative pair decomposition
directly at the polarized \(G_a\) level, using the canonical zero-side pair
coordinates and the finite/infinite divisor splitting, without passing through
the auxiliary \(H^{-1}_{L_D}\) norm.

**No canonical cursor movement is asserted by this residue.**
