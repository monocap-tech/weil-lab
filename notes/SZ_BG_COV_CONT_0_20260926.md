# SZ-BG-COV-CONT-0 — Native common-carrier covariance continuity

**Date:** 2026-09-26  
**Branch:** `sz-cross-collar`  
**Status:** UNRATIFIED RESIDUE / NF PASS  
**Canonical parent:** `SZ-CROSS-COLLAR-3`  
**Immediate parent residue:** `SZ_BG_ELIMINATION_COLLAR_0_20260926.md`  
**Uses:** ZW1-T9 / WD-T28, the direct Dirichlet-resolvent column estimate,
and the fixed finite-dimensional pair-coordinate transforms WD-T20.

## 0. Objective

The previous pass isolated

```text
SZ-BG-COV-CONT
```

as the question whether the actual support-dependent background covariance is
right operator-norm continuous after all support spaces are embedded in one
common Hilbert carrier.

This pass answers that question at the **native Problem-1
(H^{-1}_L) zero-side carrier**.

It does not yet identify that carrier uniformly with Suzuki's
(L^2(-a,a)) closed-form realization.

---

## 1. Fix one common carrier

Choose

```math
A>c
```

and restrict attention to support parameters

```math
0<t\le A.
```

Let

```math
L_A=-\partial_u^2+\frac14
```

on ((-A,A)) with Dirichlet boundary conditions, and let

```math
\mathscr H_A:=H^{-1}_{L_A}(-A,A)
```

be the corresponding negative-order Hilbert carrier.

For each zeta ordinate coordinate (gamma), define the common-carrier
support-truncated column

```math
f_{\gamma,t}(u)
:=
\mathbf 1_{(-t,t)}(u)e^{-i\gamma u},
```

viewed as an element of (mathscr H_A).

Define

```math
\widehat E_t e_\gamma:=f_{\gamma,t}.
```

Unlike the moving-space maps

```math
E_t:\ell^2(\Gamma)\to H^{-1}_{L_t}(-t,t),
```

all maps (widehat E_t) now have the same codomain.

---

## 2. Columnwise support continuity

Fix one (gamma).

As (t\to s),

```math
f_{\gamma,t}-f_{\gamma,s}
```

is supported on the symmetric difference of the two intervals.

Since every zeta ordinate lies in the fixed strip

```math
|\Im\gamma|<\frac12,
```

the exponential is uniformly bounded on ((-A,A)). Therefore

```math
\|f_{\gamma,t}-f_{\gamma,s}\|_{L^2(-A,A)}
\longrightarrow0.
```

The embedding

```math
L^2(-A,A)\hookrightarrow H^{-1}_{L_A}(-A,A)
```

is bounded, hence

```math
\boxed{
\|f_{\gamma,t}-f_{\gamma,s}\|_{\mathscr H_A}
\longrightarrow0.
}
```

Thus every individual zero-side synthesis column varies continuously with the
support radius in the common carrier.

---

## 3. Uniform high-height majorant

Columnwise convergence is not enough; to obtain Hilbert-Schmidt continuity we
need a summable majorant uniform for (t\le A).

Let

```math
V_A=H_0^1(-A,A)
```

with the energy norm associated to (L_A).

For (gamma\ne0) and (phi\in V_A),

```math
\langle f_{\gamma,t},\phi\rangle
=
\int_{-t}^{t}
e^{-i\gamma u}\overline{\phi(u)}\,du.
```

Integrating by parts on ((-t,t)),

```math
\begin{aligned}
\left|
\int_{-t}^{t}
e^{-i\gamma u}\overline{\phi(u)}\,du
\right|
\le
\frac{1}{|\gamma|}
\Big(
|e^{-i\gamma t}\phi(t)|
+
|e^{i\gamma t}\phi(-t)|
+
\int_{-t}^{t}
|e^{-i\gamma u}|\,|\phi'(u)|\,du
\Big).
\end{aligned}
```

On the fixed interval ((-A,A)),

- the zeta-strip bound gives
  [
  |e^{-i\gamma u}|\le e^{A/2};
  ]
- interior trace evaluation
  [
  \phi\mapsto\phi(x)
  ]
  is bounded on (H_0^1(-A,A)), uniformly for (x\in[-A,A]);
- the derivative term is bounded by Cauchy-Schwarz.

Hence there is a constant

```math
C_A<\infty
```

such that, uniformly in (0<t\le A),

```math
\boxed{
\|f_{\gamma,t}\|_{\mathscr H_A}
\le
\frac{C_A}{|\gamma|}
}
```

for the high-height coordinates.

After absorbing the finitely many low coordinates into the constant, one may
write

```math
\boxed{
\|f_{\gamma,t}\|_{\mathscr H_A}^2
\le
\frac{C_A'}{1+|\gamma|^2}
}
```

uniformly for (t\le A).

This is the common-carrier analogue of the fixed-window inverse-square column
estimate already used in WD-T28.

---

## 4. Hilbert-Schmidt continuity

The unit-height zeta zero count gives

```math
N(T+1)-N(T)=O(\log(2+T)).
```

Therefore

```math
\sum_{\gamma}
\frac{1}{1+|\gamma|^2}
<
\infty.
```

For fixed (s\le A),

```math
\|f_{\gamma,t}-f_{\gamma,s}\|_{\mathscr H_A}^2
\longrightarrow0
```

for every (gamma), while

```math
\|f_{\gamma,t}-f_{\gamma,s}\|_{\mathscr H_A}^2
\le
2\|f_{\gamma,t}\|^2
+
2\|f_{\gamma,s}\|^2
\le
\frac{4C_A'}{1+|\gamma|^2}.
```

Dominated convergence for the basis-square sum gives

```math
\boxed{
\|\widehat E_t-\widehat E_s\|_{\mathrm{HS}}
\longrightarrow0.
}
```

Thus the full zero-side Problem-1 synthesis is continuous in the
Hilbert-Schmidt topology on a fixed larger native carrier.

---

## 5. Positive and background channel continuity

The positive/negative pair diagonalization of WD-T20 and the selected/background
coordinate projections are fixed bounded maps on coefficient space; they do
not depend on (t).

Therefore every fixed channel restriction of (widehat E_t) inherits
Hilbert-Schmidt continuity.

In particular,

```math
\boxed{
\|\widehat S_{+,t}-\widehat S_{+,s}\|_{\mathrm{HS}}
\to0,
}
```

and for the unselected negative background,

```math
\boxed{
\|\widehat S_{B,t}-\widehat S_{B,s}\|_{\mathrm{HS}}
\to0.
}
```

This conclusion applies to a fixed selected packet (Pi), hence to its fixed
complementary background (B_\Pi).

---

## 6. Covariance continuity is trace-norm continuity

For Hilbert-Schmidt operators (S,T),

```math
SS^*-TT^*
=
(S-T)S^*
+
T(S^*-T^*).
```

Hence the trace-ideal estimate gives

```math
\boxed{
\|SS^*-TT^*\|_1
\le
(\|S\|_{\mathrm{HS}}+\|T\|_{\mathrm{HS}})
\|S-T\|_{\mathrm{HS}}.
}
```

Applying this separately to the positive and background syntheses,

```math
\widehat K_B(t)
:=
\widehat S_{+,t}\widehat S_{+,t}^*
-
\widehat S_{B,t}\widehat S_{B,t}^*
```

satisfies

```math
\boxed{
\|\widehat K_B(t)-\widehat K_B(s)\|_1
\longrightarrow0.
}
```

Since operator norm is bounded by trace norm,

```math
\boxed{
\|\widehat K_B(t)-\widehat K_B(s)\|
\longrightarrow0.
}
```

So the desired common-carrier covariance continuity is actually obtained in a
topology stronger than operator norm.

---

## 7. Consequence for background stability

At the native Problem-1 carrier, the continuity half of the previous
background-stability criterion is therefore discharged:

```text
SZ-BG-COV-CONT — SOLVED at native H^{-1}_L carrier.
```

Consequently, if the endpoint background covariance has a strict gap

```math
\widehat K_B(c)\succeq\eta I,
\qquad
\eta>0,
```

then

```math
\widehat K_B(t)\succeq\frac\eta2 I
```

for all sufficiently small strict right enlargements.

Thus, in this carrier,

```math
\boxed{
\text{the only remaining background-stability issue is }SZ\text{-}BG\text{-}GAP.
}
```

---

## 8. Important carrier warning

Suzuki's localized closed Weil form is represented on

```math
L^2(-a,a),
```

with a self-adjoint operator (A_a). Suzuki proves continuity of the lowest
eigenvalue (lambda_a) as the support parameter varies, while explicitly
noting that continuity questions for the unbounded operator family are
delicate.

The continuity proved in this pass is a different statement:

```math
\boxed{
\text{bounded zero-side synthesis/covariance continuity}
\text{ in the native Problem-1 }H^{-1}_L\text{ metric}.
}
```

It must not be promoted to norm continuity of Suzuki's unbounded
(A_a) family.

To use it inside the ratified cross-collar theorem, one still needs a
metric/carrier comparison showing that the background elimination performed in
the native zero-side carrier is the same elimination entering the
support-(a) closed Weil form.

Call that remaining bridge

```text
SZ-CARRIER-METRIC-COMPAT
```

rather than reopening the already-solved covariance continuity problem.

---

## 9. Relation to Suzuki's support theorem

Suzuki's current paper fixes (L^2(-a,a)) as a zero-extended subspace of
(L^2(\mathbb R)), defines (G_a=P_aGP_a), and proves continuity of the
lowest eigenvalue (lambda_a) in the support parameter.

That result confirms that support variation is analytically tractable, but it
does not by itself provide the channelwise covariance continuity proved here.

Conversely, the Hilbert-Schmidt argument here does not replace Suzuki's
closed-form/eigenvalue continuity theorem. The two statements live on different
operator layers.

---

## 10. Result of this NF pass

The previous two-interface background seam

```text
SZ-BG-COV-CONT
SZ-BG-GAP
```

has reduced to

```math
\boxed{
SZ\text{-}BG\text{-}COV\text{-}CONT
\text{ is solved on the native zero-side carrier;}
}
```

and the remaining issues are

```text
SZ-BG-GAP
```

and

```text
SZ-CARRIER-METRIC-COMPAT.
```

Thus lack of support continuity is no longer the primary obstruction in the
native Problem-1 geometry.

No claim is made here that the endpoint background gap is positive.

---

## 11. Candidate follow-on if ratified

```text
SZ-BG-GAP / ENDPOINT BACKGROUND SATURATION
```

A future NF should determine whether the attained selected-neutral endpoint can
coexist with a simultaneously saturated unselected-background screening
budget, or whether the Horizon-1 joint-budget geometry forces residual positive
slack for the background alone.

**No canonical cursor movement is asserted by this residue.**
