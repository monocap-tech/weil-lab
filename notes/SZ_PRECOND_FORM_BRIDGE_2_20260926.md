# SZ-PRECOND-FORM-BRIDGE-2 — Regular screw-carrier channel custody

**Date:** 2026-09-26  
**Branch:** \`sz-cross-collar\`  
**Status:** UNRATIFIED RESIDUE / NF PASS  
**Canonical parent:** \`SZ-CROSS-COLLAR-3\`  
**Immediate parent residue:** \`SZ_PRECOND_FORM_BRIDGE_1_20260926.md\`  
**Uses:** Suzuki (8.6), H1-P2.0 zero-side specialization, WD-T20 pair
diagonalization, EXT-3 zero counting.

## 0. Objective

PFB-1 established the exact regular-core identity

~~~math
Q_W(v_1,v_2)
=
\langle G_a Dv_1,Dv_2\rangle,
\qquad
D=i\,\frac{d}{dx}.
~~~

The remaining PFB-3 question is whether the positive / selected-negative /
background-negative ownership split can be realized directly on Suzuki's
screw carrier

~~~math
L_0^2(-a,a),
~~~

without passing through the auxiliary Problem-1 \(H^{-1}_{L_D}\) metric.

For the regular screw carrier, the answer is yes.

The full logarithmic form-domain extension remains a separate question.

---

## 1. Zero-side coefficient map on the regular carrier

Let

~~~math
v\in H_0^1(-a,a)
~~~

and let

~~~math
u:=Dv\in L_0^2(-a,a).
~~~

For every nontrivial zero ordinate \(\gamma\), let

~~~math
z_\gamma(v)
~~~

denote the canonical raw zero-side coefficient/evaluation used in the H1-P2
specialization of the Weil form.

Up to the fixed Fourier normalization convention, this is the compact-window
Fourier evaluation of \(v\) at \(\gamma\).

Define

~~~math
\mathcal Z_a v
:=
(z_\gamma(v))_{\gamma\in\Gamma}.
~~~

H1-P2.0 records the corresponding coefficient-space Weil form as the
fundamental-symmetry form

~~~math
\boxed{
Q_W(v_1,v_2)
=
\langle
J\mathcal Z_a v_1,
\mathcal Z_a v_2
\rangle.
}
~~~

After multiplicity-null directions are quotiented, \(J\) is diagonalized by
WD-T20.

---

## 2. Boundedness after the derivative change of variables

The crucial point is that

~~~math
\mathcal Z_aD^{-1}
~~~

is bounded into the zero-coordinate \(\ell^2\) space.

Indeed, since \(v(\pm a)=0\), integration by parts gives, for a nonzero
ordinate \(\gamma\),

~~~math
z_\gamma(v)
=
\frac{c_{\rm FT}}{\gamma}
\int_{-a}^{a}
u(x)e^{i\gamma x}\,dx
~~~

with the fixed Fourier-normalization scalar \(c_{\rm FT}\) and the harmless
phase convention absorbed into it.

Because all zeta ordinates lie in the fixed horizontal strip,

~~~math
|e^{i\gamma x}|
\le
e^{a/2}
\qquad
(|x|\le a),
~~~

hence

~~~math
\boxed{
|z_\gamma(D^{-1}u)|
\le
\frac{C_a}{1+|\gamma|}
\|u\|_{L^2}.
}
~~~

The finitely many low ordinates are absorbed into \(C_a\).

Using the unit-height zero count

~~~math
N(T+1)-N(T)=O(\log T),
~~~

one has

~~~math
\sum_{\gamma\in\Gamma}
\frac{1}{(1+|\gamma|)^2}
<
\infty.
~~~

Therefore

~~~math
\boxed{
\sum_{\gamma}
|z_\gamma(D^{-1}u)|^2
\le
C_a'
\|u\|_2^2.
}
~~~

So the regular screw-coordinate analysis map

~~~math
\boxed{
\mathcal A_a
:=
\mathcal Z_aD^{-1}
:
L_0^2(-a,a)
\longrightarrow
\ell^2(\Gamma)
}
~~~

is bounded.

In fact the estimate is the same inverse-height mechanism behind the project's
compact zero-side synthesis, but it is obtained here directly from the
Dirichlet boundary condition and \(D^{-1}\), not from the auxiliary
\(H^{-1}_{L_D}\) metric.

---

## 3. Canonical pair diagonalization

For one nonreal conjugate pair

~~~math
\gamma=T+i\delta,
\qquad
\bar\gamma=T-i\delta,
~~~

write its two raw coefficients as

~~~math
(z_\gamma,z_{\bar\gamma}).
~~~

Define

~~~math
p
=
\frac{z_\gamma+z_{\bar\gamma}}{\sqrt2},
\qquad
n
=
\frac{z_\gamma-z_{\bar\gamma}}{\sqrt2}.
~~~

The zero-side Hermitian block becomes

~~~math
\boxed{
|p|^2-|n|^2.
}
~~~

Critical-line coordinates contribute positive squares only.

Thus the fixed pair transform gives an orthogonal decomposition

~~~math
K
=
K_+\oplus K_-,
~~~

with

~~~math
K_+
=
K_{\rm crit}\oplus K_{{\rm off},+},
\qquad
K_-
=
K_{{\rm off},-}.
~~~

Let

~~~math
\mathcal A_{+,a}
:
L_0^2(-a,a)\to K_+,
~~~

and

~~~math
\mathcal A_{-,a}
:
L_0^2(-a,a)\to K_-
~~~

be the corresponding bounded components of \(\mathcal A_a\).

Then

~~~math
\boxed{
Q_W(D^{-1}u_1,D^{-1}u_2)
=
\langle
\mathcal A_{+,a}u_1,
\mathcal A_{+,a}u_2
\rangle
-
\langle
\mathcal A_{-,a}u_1,
\mathcal A_{-,a}u_2
\rangle.
}
~~~

---

## 4. Direct decomposition of Suzuki's screw operator

PFB-1 gives

~~~math
Q_W(D^{-1}u_1,D^{-1}u_2)
=
\langle
G_au_1,u_2
\rangle.
~~~

Combining with Section 3,

~~~math
\boxed{
\langle
G_au_1,u_2
\rangle
=
\langle
\mathcal A_{+,a}u_1,
\mathcal A_{+,a}u_2
\rangle
-
\langle
\mathcal A_{-,a}u_1,
\mathcal A_{-,a}u_2
\rangle.
}
~~~

Since all operators here are bounded on \(L_0^2(-a,a)\), the identity extends
from the regular dense core to the whole screw carrier.

Define synthesis maps by adjunction:

~~~math
S_{+,a}
:=
\mathcal A_{+,a}^*,
\qquad
S_{-,a}
:=
\mathcal A_{-,a}^*.
~~~

Then the operator identity is

~~~math
\boxed{
G_a
=
S_{+,a}S_{+,a}^*
-
S_{-,a}S_{-,a}^*.
}
~~~

Thus Suzuki's \(G_a\) is itself a physical defect operator in the exact H1-P1
sense, on the regular screw-coordinate carrier.

No auxiliary carrier congruence is required for this statement.

---

## 5. Selected packet and background directly inside \(G_a\)

Fix a finite selected off-axis packet \(\Pi\).

Split the negative pair-coordinate space orthogonally:

~~~math
K_-
=
M_\Pi
\oplus
B_\Pi.
~~~

Let

~~~math
\mathcal A_{M,a}
=
P_{M_\Pi}\mathcal A_{-,a},
\qquad
\mathcal A_{B,a}
=
P_{B_\Pi}\mathcal A_{-,a},
~~~

and define

~~~math
S_{M,a}
=
\mathcal A_{M,a}^*,
\qquad
S_{B,a}
=
\mathcal A_{B,a}^*.
~~~

Then

~~~math
\boxed{
G_a
=
S_{+,a}S_{+,a}^*
-
S_{M,a}S_{M,a}^*
-
S_{B,a}S_{B,a}^*.
}
~~~

Equivalently,

~~~math
\boxed{
\langle G_au,u\rangle
=
\|S_{+,a}^*u\|^2
-
\|S_{M,a}^*u\|^2
-
\|S_{B,a}^*u\|^2.
}
~~~

This is exactly the positive / selected-negative / background-negative
polarization required by PFB-3.

---

## 6. Consequence: pointwise owner taxonomy transfers on the screw carrier

For a regular support-\(a\) problem, the H1 screening calculus may now be
applied directly to \(G_a\):

- test \(S_{B,a}\) against \(S_{+,a}\);
- if the background is contractively screenable, eliminate it by WD-T10;
- then classify any residual selected negativity as range defect or over-budget
  defect;
- otherwise classify the background itself as range defect or over-budget
  defect.

Thus the four pointwise cells

~~~text
SR-R
SR-B
BG-R
BG-B
~~~

are legitimate owner labels directly in Suzuki's \(L_0^2\) screw
representation.

This closes PFB-3 at the regular screw-carrier level.

---

## 7. Why this does not use the auxiliary \(H^{-1}_{L_D}\) carrier

The analysis map above is built from

~~~math
u
\overset{D^{-1}}{\longmapsto}
v
\overset{\text{zero evaluations}}{\longmapsto}
(z_\gamma(v)).
~~~

Its inverse-height decay comes from integration by parts using

~~~math
v(\pm a)=0.
~~~

The repo's WD-T28 compactness theorem instead uses

~~~math
(-\partial^2+1/4)^{-1}
~~~

to construct a different negative-order Hilbert metric.

The two arguments share a decay scale but are analytically distinct.

Therefore PFB-3 on \(G_a\) does not depend on identifying those two metrics.

---

## 8. Remaining full-form-domain obstruction

The ratified SZ-CROSS-COLLAR-3 theorem is stronger than the regular
\(H_0^1/L_0^2\) bridge.

Its endpoint null vector may live only in the closed logarithmic form domain,
with no assumption that

~~~math
k\in H_0^1(-a,a).
~~~

For such a vector, the derivative coordinate

~~~math
Dk
~~~

need not lie in \(L^2\).

Therefore the decomposition of Section 5 cannot yet be applied to every
full-form-domain neutral mode.

One would need either:

1. an extension of the zero-coordinate analysis map to the closed logarithmic
   form domain with sufficient square-summability; or
2. an independent theorem that the specific attained neutral mode under study
   lies in \(H_0^1\).

Horizon 1 explicitly forbids assuming such a positive-Sobolev bootstrap for
free.

So:

~~~text
PFB-3S — channel custody on Suzuki screw carrier: DISCHARGED
PFB-3F — channel custody on full logarithmic form domain: OPEN
~~~

---

## 9. Why compact support alone does not close PFB-3F

For a compactly supported \(L^2\) function \(v\), every individual Fourier
evaluation is well defined because \(L^2(-a,a)\subset L^1(-a,a)\).

But the crude estimate is only

~~~math
|z_\gamma(v)|
\le
C_a\|v\|_2,
~~~

with no inverse-height decay.

Since there are infinitely many zeros, this does not imply

~~~math
(z_\gamma(v))_\gamma\in\ell^2.
~~~

The \(1/|\gamma|\) gain in Section 2 came specifically from one derivative and
the Dirichlet endpoint condition.

Thus the regular bridge cannot be extended to the whole form domain by a
formal density argument unless the coefficient analysis is first shown to be
closable/bounded in the logarithmic form norm.

This is a genuine regularity seam.

---

## 10. Refined remaining interface

The post-PFB-3 bridge is now

~~~text
SZ-CHANNEL-CUSTODY-FORMDOMAIN
~~~

> Extend the canonical zero-coordinate positive/selected/background
> polarization from the regular \(H_0^1/L_0^2\) screw carrier to the closed
> logarithmic form domain used by Suzuki's \(A_a\), without importing a
> positive-Sobolev estimate.

Equivalent target:

~~~math
\boxed{
\text{prove a logarithmic-form-domain Bessel bound for the zero-coordinate map.}
}
~~~

If that succeeds, the pointwise owner taxonomy transfers to every neutral mode
covered by the ratified full-domain cross-collar theorem.

If it fails, the regular and singular neutral sectors must remain distinct.

---

## 11. Result of this NF pass

The positive / selected-negative / background-negative decomposition can be
recovered **directly** inside Suzuki's bounded screw operator:

~~~math
\boxed{
G_a
=
S_{+,a}S_{+,a}^*
-
S_{M,a}S_{M,a}^*
-
S_{B,a}S_{B,a}^*.
}
~~~

This follows from:

1. Suzuki's exact derivative bridge;
2. the canonical zero-side Weil coefficient form;
3. the \(1/|\gamma|\) coefficient decay supplied by \(H_0^1\) integration by
   parts;
4. zero counting;
5. canonical pair diagonalization.

So PFB-3 is closed on the regular screw carrier.

The only remaining custody extension is the closed logarithmic form-domain
case.

---

## 12. Candidate follow-on if ratified

~~~text
SZ-CHANNEL-CUSTODY-FORMDOMAIN / LOG-BESSEL
~~~

A future NF should test whether the logarithmic form norm itself controls the
square-sum of zero evaluations strongly enough to extend the channel analysis
map without an \(H^1\) bootstrap.

**No canonical cursor movement is asserted by this residue.**
