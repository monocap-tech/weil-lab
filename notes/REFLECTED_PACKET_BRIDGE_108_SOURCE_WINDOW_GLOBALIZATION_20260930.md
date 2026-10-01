# RPB-108 — shell-corrected source-window globalization

**Date:** 2026-09-30 (America/Los_Angeles)  
**Research base:** `dc2903952b6f3cc66231b199b6060c9528e819e2`  
**Effective status:** **SHELL-CORRECTED SOURCE-WINDOW GLOBALIZATION BUILD-CERTIFIED / FREE SUPPORT GLOBALIZATION REJECTED / ALL-COMPACT WEAK WITNESS DERIVED FROM CORRECTED FINITE-WINDOW PREMISE / EXTERNAL SOURCE FORM-DOMAIN + THRESHOLD-CORRECTED LOCAL RESIDUAL ATTACHMENT STILL OPEN / RPB-108 CONTINUES / COERCIVITY NOT STARTED**

## 1. Scope correction

The first attempted globalization route was too strong.

For a compact test whose support is contained in a larger window
`(-b,b)`, the already-certified compression theorem does **not** permit one
to replace the larger-window action `E_b` by the frozen base action `E_a`
unless that test was already supported in the old window `(-a,a)`.

The lawful arbitrary-test relation is instead

~~~math
E_a(h;u)
=
E_b(h;u)
+
\int_{\mathbb R}u(x)P_{a,b}h(x)\,dx.
~~~

The finite shell is therefore load-bearing outside the old window.

The invalid free-globalization draft was never promoted to the research
branch.

## 2. Certified implementation

New module:

~~~text
WeilDefect/Morphology/NeutralWeilSourceWindowAttachment.lean
~~~

Certified declarations:

~~~text
compactSchwartz_support_in_symmetric_window
frozenWeilCompactAction_eq_larger_add_shell
RightLimitWeilCorrectedSourceWindowPremise
rightLimitWeilWeakRealizationPremise_of_correctedSourceWindows
rightLimitWeilGaussianHermitian_of_correctedSourceWindows
~~~

Every compact Schwartz test is first placed inside some sufficiently large
symmetric source window.

The corrected finite-window premise then asks for the selected frozen
residual to satisfy

~~~math
\int u q_a
=
E_b(h;u)
+
\int uP_{a,b}h
~~~

on that source window.  The certified radius-correction and
Fourier/physical-shell theorems identify the right-hand side with the frozen
base action `E_a(h;u)`.

Consequently:

~~~lean
rightLimitWeilWeakRealizationPremise_of_correctedSourceWindows
~~~

derives the existing all-compact-test
`RightLimitWeilWeakRealizationPremise` at the frozen base radius.

The downstream theorem

~~~lean
rightLimitWeilGaussianHermitian_of_correctedSourceWindows
~~~

then feeds that derived witness directly into the already-certified
Hermitian Gaussian cutoff bridge.  No new Gaussian identity is imported.

## 3. Source boundary

This pass does **not** prove the new source-window premise.

The remaining external/source reconstruction task is now finite-window and
explicit:

1. put the actual compact L2 carrier and the required real/complex test
   components in the source form domain;
2. polarize/complexify the source quadratic identity on that finite window;
3. retain the source-to-mathlib Fourier normalization;
4. reconcile the source strict prime cutoff with the project's
   equality-threshold right-limit convention;
5. identify the supplied residual with the resulting shell-corrected frozen
   action, including its local integrability, central vanishing, and
   exponential-growth fields.

The source's strict compact-window formula is therefore not silently promoted
to the project's right-limit `<=` symbol.

## 4. Validation history

The first PR run

~~~text
run: 36823900387
~~~

was green but built the inherited unrelated target
`WeilDefect.Examples.WeakCriticalFallthrough`.  It is **not** a certificate
for this module.

The workflow target was then corrected explicitly.

The first genuine target run reached the new module and exposed only an
elaboration issue in the compact-support bounding lemma: membership in the
closed interval needed to be destructured before `linarith`.  No theorem
statement or hypothesis changed.

Final successful direct validation:

~~~text
repository: monocap-tech/weil-lab
validation branch: validation/rpb108-source-window-globalization
PR: 26
run: 36824968898
job: 110248500881
checked-out HEAD: af0060d6acef81062a01eb06087dd3566bc800bb
Lean: leanprover/lean4:v4.34.0
mathlib: 5ed2965256430c3649e86755f9576b54eca72435
actual target: lake build WeilDefect.Morphology.NeutralWeilSourceWindowAttachment
result: PASS (8952 build-graph jobs)
source blob: 5be297c758f1f169be2f4eadf00996beeae3a6e4
declaration rejection gate: PASS
~~~

The four inspected endpoint closures reported only:

~~~text
propext
Classical.choice
Quot.sound
~~~

No `sorryAx` or project axiom appears in those inspected dependency
closures.  Explicit source hypotheses remain theorem parameters.

## 5. Determination

~~~math
\boxed{
\textbf{THE ALL-COMPACT FROZEN EXT-4 WITNESS NO LONGER HAS TO BE IMPORTED DIRECTLY.  IT IS AN INTERNAL CONSEQUENCE OF A SHELL-CORRECTED FINITE-WINDOW SOURCE PREMISE.}
}
~~~

The rejected free-globalization attempt is itself informative: the finite
prime shell is exactly the custody needed when a test leaves the old support
window.

## 6. Live continuation

~~~text
RPB-108 / WD-T40 F-4 — CONTINUES

ALL-COMPACT WITNESS FROM CORRECTED SOURCE WINDOWS: CERTIFIED
HERMITIAN GAUSSIAN CONSEQUENCE FROM THAT WITNESS: CERTIFIED CONDITIONAL

NEXT:
SOURCE QUADRATIC FORM-DOMAIN
+ POLARIZATION/COMPLEXIFICATION ON EACH FINITE WINDOW
+ STRICT-CUTOFF / RIGHT-LIMIT THRESHOLD CORRECTION
+ ACTUAL RESIDUAL ATTACHMENT TO THE SHELL-CORRECTED LOCAL IDENTITY

LOGARITHMIC COERCIVITY: NOT STARTED
~~~
