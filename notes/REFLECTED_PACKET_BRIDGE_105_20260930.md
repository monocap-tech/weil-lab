# RPB-105 — WD-T40 F-4 residual and pole cutoff pairing convergence

**Date:** 2026-09-30  
**Branch:** research/reflected-packet-bridge  
**Status:** **COMPLETE / BUILD-CERTIFIED / RESIDUAL PAIRING CONVERGENCE CLOSED / POLE PAIRING CONVERGENCE CLOSED CONDITIONAL ON EXPLICIT POLE-GROWTH DATA / NO NEW ANALYTIC PREMISE / COERCIVITY NOT STARTED**

## 0. Objective

RPB-104 constructed the actual compactly supported Schwartz cutoff sequence for
the RPB-103 moving filtered mode.

RPB-105 discharges the two ordinary-integral convergence fields required by
RightLimitWeilGaussianCutoffPremise.

## 1. Whole-line residual pairing integrability

The prior F-3 layer had certified residual pairing integrability on the two
exterior half-lines.

RPB-105 adds

~~~lean
residualFilteredMode_integrable
~~~

which upgrades this to whole-line integrability using the already-certified
a.e. vanishing of the residual on the strict central interval.

No new residual bound is introduced.

## 2. General cutoff pairing limit

The new generic theorem

~~~lean
neutralGaussianSchwartzCutoff_pairing_tendsto
~~~

states that for a Schwartz function f and a measurable factor g, whenever

~~~math
x \mapsto f(x)g(x)
~~~

is integrable, the RPB-104 cutoff pairings converge to the uncut pairing.

The proof is direct dominated convergence:

- the cutoff scalar lies in [0,1];
- therefore the cutoff product is dominated by |f g|;
- for each fixed x, the expanding cutoff is eventually exactly 1;
- the dominator is integrable by hypothesis.

Thus the limit does not rely on an unproved continuity principle for ordinary
integration against exponentially growing factors.

## 3. Residual specialization

The theorem

~~~lean
movingGaussianFilteredModeCompactCutoff_residual_pairing_tendsto
~~~

applies the generic limit to the actual moving filtered mode and residual.

Its required integrability is discharged by the new whole-line residual
integrability theorem.

Therefore RPB-100 burden C is closed.

## 4. Pole specialization

The theorem

~~~lean
movingGaussianFilteredModeCompactCutoff_pole_pairing_tendsto
~~~

applies the same dominated-convergence bridge to any pole equipped with

~~~lean
NeutralPoleExponentialGrowthData pole.
~~~

The needed dominator is supplied by the RPB-100 theorem

~~~lean
poleFilteredMode_integrable.
~~~

Therefore burden D is closed at the exact level intended by RPB-100:
conditional only on the explicit source-faithful pole-growth carrier.

The remaining task is not convergence.  It is to instantiate that carrier for
the actual EXT-4 pole species.

## 5. Validation

The complete source passed under the pinned toolchain:

~~~text
run:  36801083567
job:  110175352895
head: 646adabb7d5423b4eafbd388150a6d0cd0cba2f8
blob: ea80c81d5d31768c68a6ea0ec69c68bed0cab806
~~~

Validation target:

~~~text
lake build WeilDefect.Morphology.NeutralGaussianCutoffPairing
~~~

The repository-wide rejection gate for axiom, sorry, and admit also passed.

## 6. RPB-105 determination

~~~math
\boxed{
\textbf{RPB-105 — BOTH ORDINARY-INTEGRAL CUTOFF LIMITS ARE NOW BUILD-CERTIFIED; THE ONLY REMAINING RPB-100 GAUSSIAN-ADMISSIBILITY BURDEN IS THE ACTUAL EXT-4 POLE-GROWTH INSTANTIATION.}
}
~~~

## 7. Remaining F-4 pre-coercivity burden

After RPB-105:

~~~text
A. actual moving filtered mode as SchwartzMap — CLOSED
B. compact Schwartz cutoff sequence + topology convergence — CLOSED
C. residual pairing convergence along cutoffs — CLOSED
D. pole pairing convergence along cutoffs — CLOSED conditional on E
E. actual EXT-4 pole exponential-growth instantiation — OPEN
~~~

Once E is supplied, the existing pieces can assemble the actual
RightLimitWeilGaussianCutoffPremise and hence derive the Gaussian weak identity
through the already-certified RPB-100 constructor.

## Next cursor

~~~text
RPB-106 / WD-T40 F-4 ACTUAL EXT-4 POLE EXPONENTIAL-GROWTH INSTANTIATION
~~~

Recover the concrete pole/evaluation species carried by EXT-4, expose its
finite exponential decomposition, and instantiate
NeutralPoleExponentialGrowthData.

Do not begin logarithmic coercivity until that source-faithful instantiation
and final cutoff-premise assembly are certified.
