# RPB-65 — Gaussian support-gap promotion audit

**Date:** 2026-09-29  
**Branch:** research/reflected-packet-bridge  
**Status:** **AUDIT PASS / RPB-64 GAUSSIAN SUPPORT-GAP PROOF SURVIVES WHOLE-LINE RESIDUAL, POLE, SYMBOL, AND STRIP-HOLOMORPHY AUDITS / AZ-FIN-WEIL-NULL-EXTENSION DISCHARGED NEGATIVELY UNDER WD-T38 CARRIER HYPOTHESES / PROMOTED ADDITIVELY AS WD-T40**  
**Dependencies:** RPB-64; WD-T34, WD-T35, WD-T38; EXT-4 compact-window formula; EXT-5 digamma asymptotic.  
**Promotion status:** **PROMOTED / P4-AUDIT-PASSED**.

## 0. Objective

RPB-64 proved, branch-locally, that a nonzero compactly supported physical Weil
mode cannot satisfy the correct compact-window null equation on a strict larger
support.

RPB-65 audits the four load-bearing steps requested at the previous cursor:

1. whole-line residual growth and Gaussian support-gap pairing;
2. finite-rank pole Gaussian estimate;
3. exact symbol lower bound across threshold conventions;
4. exponential Fourier decay to strip holomorphy.

All four pass.

The result is promoted additively as

~~~text
WD-T40 / Gaussian support-gap null-extension exclusion.
~~~

---

## 1. Audit A — whole-line residual pairing

Let

~~~math
\operatorname{supp}h\subseteq[-c,c],
\qquad
a>c,
\qquad
\delta=a-c>0.
~~~

Assume the correct enlarged null equation holds on

~~~math
(-a,a).
~~~

Set

~~~math
q
=
\mathcal W_a^{\rm ext}h.
~~~

Then, distributionally,

~~~math
q=0
\quad
\text{on }(-a,a).
~~~

Thus the residual is supported outside a set at positive distance \(\delta\)
from the support of \(h\).

The Gaussian filter with symbol

~~~math
\phi_R^+(\eta)
=
e^{-(\eta-R)^2/R}
~~~

has physical kernel

~~~math
K_R^+(x)
=
C\sqrt R\,
e^{-Rx^2/4}
e^{iRx}.
~~~

Hence

~~~math
\left|
(\phi_R^+(D)h)(x)
\right|
\le
C_h\sqrt R\,
e^{-R\,\operatorname{dist}(x,[-c,c])^2/4}.
~~~

Outside \((-a,a)\), the distance is at least \(\delta\).

### Archimedean tail

The exact Gauss/digamma kernel from EXT-4/RPB-EXT-A8 has exponentially
controlled off-diagonal tail.  Applied to compactly supported \(h\), the
archimedean residual grows at worst exponentially of fixed rate and in fact the
off-diagonal kernel itself decays exponentially.

### Prime terms

Every prime contribution is a finite translated copy of \(h\), hence compactly
supported.

### Pole term

The pole/evaluation contribution lies in a fixed finite-dimensional span of
real exponential functions.

Therefore the residual \(q\) is a distribution/function of at most fixed
exponential growth outside the null interval.

The Gaussian factor

~~~math
e^{-R\,\operatorname{dist}(x,[-c,c])^2/4}
~~~

dominates every such fixed exponential growth.

Consequently

~~~math
\boxed{
\left|
\left\langle
q,\phi_R^+(D)h
\right\rangle
\right|
\le
C R^M e^{-R\delta^2/8}
}
~~~

for some fixed \(M\).

After absorbing the polynomial factor,

~~~math
\boxed{
\left|
\left\langle
q,\phi_R^+(D)h
\right\rangle
\right|
\le
Ce^{-\kappa R}.
}
~~~

The same holds for the \(-R\) window.

**Disposition:** PASS.

---

## 2. Audit B — exact pole Gaussian estimate

The compact-window form contains the finite-rank evaluation term

~~~math
2|F(i/2)|^2
~~~

up to the retained real/complex convention.

In physical space its range is spanned by fixed exponentials of the form

~~~math
e^{\sigma x/2},
\qquad
\sigma\in\{\pm1\}
~~~

as required by the chosen Hermitian convention.

For one such exponential, Gaussian convolution may be evaluated exactly:

~~~math
\phi_R^+(D)e^{\sigma x/2}
=
\phi_R^+\!\left(-\frac{i\sigma}{2}\right)
e^{\sigma x/2},
~~~

in the analytic-continuation sense appropriate to the Gaussian entire symbol.

Now

~~~math
\phi_R^+\!\left(-\frac{i\sigma}{2}\right)
=
\exp\!\left[
-\frac{
(-i\sigma/2-R)^2
}{
R
}
\right],
~~~

and therefore

~~~math
\boxed{
\left|
\phi_R^+\!\left(-\frac{i\sigma}{2}\right)
\right|
=
e^{-R+1/(4R)}.
}
~~~

Since the input \(h\) is compactly supported, the remaining exponential
pairing is finite.

Thus

~~~math
\boxed{
\left|
\left\langle
\mathcal R_{{\rm pole},a}h,
\phi_R^+(D)h
\right\rangle
\right|
\le
C_h e^{-R+1/(4R)}.
}
~~~

The negative-frequency window has the same modulus estimate.

The pole term is therefore exponentially negligible at the moving Gaussian
frequencies.

**Disposition:** PASS.

---

## 3. Audit C — exact enlarged symbol lower bound

By EXT-4 and EXT-5,

~~~math
\Psi_a(\eta)
=
\Re\psi\!\left(
\frac14+\frac{i\eta}{2}
\right)
-\log\pi
-
\sum_{\log n<2a}
\frac{2\Lambda(n)}{\sqrt n}
\cos(\eta\log n),
~~~

with the finite equality-threshold correction included in the correct
right-limit convention.

For each fixed \(a\), the prime sum is finite and uniformly bounded in
\(\eta\).

The digamma asymptotic gives

~~~math
\Re\psi\!\left(
\frac14+\frac{i\eta}{2}
\right)
=
\log|\eta|
+
O(1).
~~~

Hence there is \(C_a\) such that

~~~math
\boxed{
\Psi_a(\eta)
\ge
\log|\eta|-C_a
}
~~~

for all sufficiently large \(|\eta|\).

Moreover \(\Psi_a\) is continuous on \(\mathbb R\) and tends to \(+\infty\) at
both frequency ends, so it has a finite global lower bound

~~~math
\Psi_a(\eta)\ge-B_a.
~~~

For the main Gaussian window

~~~math
\frac R2\le\eta\le\frac{3R}{2},
~~~

this gives

~~~math
\Psi_a(\eta)
\ge
\log R-C_a'.
~~~

Outside that window,

~~~math
\phi_R^+(\eta)
\le
e^{-R/4}
~~~

at the window boundary and has Gaussian decay thereafter.

Since compact support gives

~~~math
|\widehat h(\eta)|
\le
\|h\|_1,
~~~

the off-window negative contribution is

~~~math
O\!\left(
R^M e^{-R/4}
\right)
~~~

for a fixed \(M\).

Therefore the Fourier-side identity yields

~~~math
\boxed{
(\log R-C_a'')
\int_{\mathbb R}
\phi_R^+(\eta)
|\widehat h(\eta)|^2\,d\eta
\le
Ce^{-\kappa R}.
}
~~~

after increasing \(R\).

A finite threshold correction merely changes \(C_a\).

**Disposition:** PASS.

---

## 4. Audit D — exponential Fourier weight and strip holomorphy

On

~~~math
R\le\eta\le R+1,
~~~

the Gaussian satisfies

~~~math
\phi_R^+(\eta)
\ge
e^{-1/R}.
~~~

Thus

~~~math
\int_R^{R+1}
|\widehat h(\eta)|^2\,d\eta
\le
Ce^{-\kappa R}.
~~~

The \(-R\) window gives the reflected estimate.

Choose

~~~math
0<\alpha<\kappa.
~~~

Summing over integer unit intervals gives

~~~math
\boxed{
\int_{\mathbb R}
e^{\alpha|\eta|}
|\widehat h(\eta)|^2\,d\eta
<
\infty.
}
~~~

For

~~~math
|\operatorname{Im}z|<\frac{\alpha}{2},
~~~

Cauchy--Schwarz gives

~~~math
\int_{\mathbb R}
\left|
e^{iz\eta}
\widehat h(\eta)
\right|\,d\eta
<
\infty.
~~~

The inverse Fourier integral therefore defines a holomorphic function on that
strip.

Its real boundary values agree almost everywhere with \(h\).

Because the original \(h\) is compactly supported, the holomorphic
representative is zero almost everywhere on a nonempty real interval.  By
continuity it is zero on that interval, and the identity theorem gives

~~~math
\boxed{
h\equiv0.
}
~~~

**Disposition:** PASS.

---

## 5. Domain/form audit

The argument does not require \(q\in L^2(\mathbb R)\).

The enlarged equation is used distributionally on the null interval, and the
Gaussian-filtered mode is an entire rapidly decaying test function.

The archimedean multiplier pairing

~~~math
\left\langle
\Psi_a(D)h,\phi_R(D)h
\right\rangle
~~~

is well-defined from the compact support of \(h\), boundedness of
\(\widehat h\), and Gaussian frequency decay.

The pole term is paired directly in physical space as in Section 2.

Thus the proof is valid at the compact-window operator/form regularity retained
by WD-T38 and does not silently assume a positive Sobolev domain.

**Disposition:** PASS.

---

## 6. Dependency audit

WD-T40 consumes:

- WD-T38's carrier-identified nonzero compact-window physical null mode;
- the definition of strict right persistence from P3-U7;
- WD-T34 / EXT-4: finitely many active prime translations and strict threshold
  convention;
- WD-T35 / EXT-5: logarithmic symbol asymptotic.

It does **not** consume:

- RPB-33;
- RPB-43 interior analyticity;
- RPB-45--58 threshold Mellin theory;
- RPB-60--63 delay-wavefront theory;
- positive-Sobolev or quasianalytic regularity of the endpoint mode.

Thus the corrected historical RPB branches are not hidden premises of the
promoted theorem.

**Disposition:** PASS.

---

## 7. Stable theorem

### WD-T40 — Gaussian support-gap null-extension exclusion

Assume the carrier-identified neutral physical mode of WD-T38 is nonzero and
compactly supported in \([-c,c]\).

Then its zero extension cannot satisfy the correct compact-window Weil null
equation on any strict enlargement \((-a,a)\), \(a>c\), including the
threshold-corrected right-limit convention.

Equivalently,

~~~math
\boxed{
\texttt{AZ-FIN-WEIL-NULL-EXTENSION}
\text{ is discharged negatively under the WD-T38 hypotheses.}
}
~~~

**Standing:** INTERNAL-PROOF / CONDITIONAL on WD-T38 hypotheses.

**Verification:** P4-AUDIT-PASSED.

---

## 8. Scope of the discharge

WD-T40 excludes the **attained fixed-packet neutral persistence branch** under
the same carrier-identification hypotheses already present in WD-T38.

It does not discharge:

- AZ-NEXTJET-LOC;
- C-ACTUAL-KPH-FLOOR;
- WD-T39 noncompact/moving-background morphologies.

Therefore this is not by itself an RH proof.

It removes one Horizon-1 fixed-packet exit.

---

## 9. RPB-65 determination

~~~math
\boxed{
\textbf{RPB-65 — GAUSSIAN SUPPORT-GAP NULL-EXTENSION EXCLUSION PASSES PROMOTION AUDIT AND IS PROMOTED AS WD-T40.}
}
~~~

Canonical disposition:

~~~text
WD-T40:
    INTERNAL-PROOF / CONDITIONAL
    P4-AUDIT-PASSED

AZ-FIN-WEIL-NULL-EXTENSION:
    DISCHARGED NEGATIVELY UNDER WD-T38 HYPOTHESES

AZ-NEXTJET-LOC:
    OPEN

C-ACTUAL-KPH-FLOOR:
    OPEN

RH:
    NOT CLAIMED
~~~

## Next cursor

~~~text
RPB-66 / POST-PROMOTION NEUTRAL-BRANCH REFOLD
~~~

The next pass should perform cleanup only:

1. reconcile public/stable summaries with WD-T40;
2. mark RPB-57/58 as non-load-bearing historical candidate routes;
3. remove any live wording that still describes AZ-FIN-WEIL-NULL-EXTENSION as
   open;
4. do not reopen the neutral proof unless the new stable theorem itself is
   challenged.
