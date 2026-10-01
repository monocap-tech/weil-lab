# RPB-108 — strict-source threshold action correction

**Date:** 2026-10-01 (America/Los_Angeles)  
**Research base:** `4168cb16f82f1925b8b5b2ca95a6420f57295d4c`  
**Effective status:** **SOURCE STRICT-< / RIGHT-LIMIT <= THRESHOLD CORRECTION BUILD-CERTIFIED AT SYMBOL AND PHYSICAL ACTION LEVELS / STRICT-SOURCE FINITE-WINDOW PREMISE ADAPTS INTERNALLY TO THE SHELL-CORRECTED RIGHT-LIMIT PREMISE / SOURCE FORM-DOMAIN + POLARIZATION + ACTUAL RESIDUAL REPRESENTATION STILL OPEN / RPB-108 CONTINUES / COERCIVITY NOT STARTED**

## 1. Action-level threshold connection

The previous pass certified

~~~math
\Psi_a^{\le}=\Psi_a^{<}-\Theta_a.
~~~

This continuation defines the corresponding physical term
`rightLimitThresholdPrimePhysical` and proves

~~~lean
rightLimitThresholdPrime_pairing_integrable
rightLimitThresholdPrime_fourier_physical_pairing
~~~

for every Schwartz test.

The literal strict-source operator is now packaged by

~~~lean
strictSourceWeilMultiplierCore
strictSourceCompactAction
~~~

and Lean proves

~~~lean
frozenWeilCompactAction_eq_strictSource_sub_threshold
~~~

with exact identity

~~~math
E_a^{\le}(h;u)
=
E_a^{<}(h;u)
-
\int_{\mathbb R}u(x)\Theta_a^{\rm phys}h(x)\,dx.
~~~

## 2. Source-facing finite-window interface

The remaining finite-window source attachment can now be stated in the pinned
strict convention through

~~~lean
StrictSourceCorrectedWindowPremise
~~~

with both the equality-threshold correction and the previously certified
larger-window shell explicit.

The adapter

~~~lean
StrictSourceCorrectedWindowPremise.toRightLimit
~~~

produces the already-certified
`RightLimitWeilCorrectedSourceWindowPremise`, after which the existing
globalization and Hermitian Gaussian bridge apply.

No source/right-limit threshold convention remains hidden downstream.

## 3. Validation

The first rebased action run exposed missing measure namespace context.  The
second exposed only the need to expand `ContinuousLinearMap.sub_apply`
before rewriting the threshold pairing.  Neither repair changed a theorem
statement or hypothesis.

Final successful run:

~~~text
run: 36871575764
job: 110400389955
checked-out head: 3bf8577200c8ef4d1648c0613106aaf6d7706931
target: lake build WeilDefect.Morphology.NeutralWeilSourceThreshold
result: PASS (8953 jobs)
source blob: 2e1a1d755da1414651fe088cf42a787a3df213fa
declaration gate: PASS
~~~

The three inspected endpoints

~~~text
rightLimitThresholdPrime_fourier_physical_pairing
frozenWeilCompactAction_eq_strictSource_sub_threshold
StrictSourceCorrectedWindowPremise.toRightLimit
~~~

reported only `propext`, `Classical.choice`, and `Quot.sound`.

## 4. Determination

~~~math
\boxed{
\textbf{THE STRICT SOURCE PRIME CONVENTION IS NOW FULLY ATTACHED TO THE PROJECT RIGHT-LIMIT CONVENTION AT THE PHYSICAL ACTION LEVEL.}
}
~~~

## 5. Live continuation

~~~text
RPB-108 / WD-T40 F-4 — CONTINUES

NEXT:
  FINITE-WINDOW SOURCE FORM-DOMAIN
  + HERMITIAN POLARIZATION / COMPLEXIFICATION
  + ACTUAL RESIDUAL REPRESENTATION
    (local integrability + central vanishing + exponential growth)

LOGARITHMIC COERCIVITY: NOT STARTED
~~~
