# RPB-108 — concrete retained-domain multiplier-plus-pole form

Date: 2026-10-01 (UTC). Recovered research head:
`275f0a21f90fbb4b939b4b621efe09a62e5fc288`.

## Scope

This continuation replaces the abstract candidate multiplier/pole form with
an integral-valued sesquilinear form on the retained source domain. It does
not reopen threshold bookkeeping or claim WD-T40/RH closure.

The normalized symbol is exactly `rightLimitCompactWeilSymbolMathlib a`,
including its existing fixed-cutoff normalization. The first Fourier slot is
conjugated. The pole term is

\[
\overline{M_{-1/2}(f)}M_{1/2}(g)+
\overline{M_{1/2}(f)}M_{-1/2}(g).
\]

Moments are integrated over the retained window `[-a,a]`. For the actual
carrier, compact support proves equality with its already named moments
over `[-c,c]` whenever `c ≤ a`. This identity does not change prime cutoffs.

## Genuine convergence and representative custody

`integrable_mixedMultiplier` proves absolute integrability of the mixed
complex expression from both diagonal absolute-symbol energies. Its bound
is `|m| ‖F‖ ‖G‖ ≤ |m| ‖F‖² + |m| ‖G‖²`.

`NeutralSourceFormDomainAttachment.absoluteSymbolEnergy` transfers the
retained logarithmic energy using the explicit upper bound
`|m(ξ)| ≤ C logarithmicFourierWeight(ξ)`. This bound remains imported EXT5
input; no new digamma-asymptotic theorem or compact-L2 bootstrap is asserted.
Symbol measurability follows from the existing temperate-growth premise.

`mixedMultiplier_integrable` applies that transfer to each domain member.
Additivity uses genuinely convergent integral addition; scalar laws use
integral linearity. Fourier and Lp a.e. representative identities ensure
these laws hold for equivalence classes rather than chosen pointwise lifts.

`sourceWindowMoment` is a complex-linear map on L2, with genuine restricted
integrability from local L2 integrability and the bounded compact interval.
It is not a global exponential-moment theorem for arbitrary L2 functions.

## Concrete comparison, not actual source identification

`sourceDomainMultiplierForm` and `sourceDomainPoleForm` construct the two
sesquilinear pieces. `sourceDomainWeilForm` adds them, and its evaluation
theorem exposes the exact integrals and cross terms.

`sourceDomainWeilForm_eq_of_diagonal` consumes the previously certified
complex polarization on this specific form and this same retained domain.
Equality of the historical source diagonal with this concrete diagonal is
still an explicit retained source obligation. No exterior or arbitrary rough
ambient test is admitted by polarization.

## Open residue and next cursor

1. Attach WD-T38's retained source-domain membership and its source diagonal
   identity to the concrete L2 carrier and constructed form.
2. Establish the actual function representing the multiplier core, with
   local integrability, exponential growth, and central cancellation of
   `r + p_h`. Logarithmic quadratic energy alone is not operator regularity.
3. Consume the already constructed full residual weak realization in the
   certified Hermitian bridge, then start logarithmic Gaussian coercivity.

Threshold bookkeeping remains closed. Coercivity has not started. The
previous source-domain checkpoint remains immutable.

## Certification

Exact-module validation passed in run `36896248362`, job `110483849939`.
Checked-out head: `d6a1a42985a22c229422d242bb5e0fb9f2dc6298`.
Source blob: `f2ce89e5e020f09de54d1864da928bd99a841cbd`.
Lean 4.34.0; mathlib `5ed2965256430c3649e86755f9576b54eca72435`.
All 8,955 build jobs passed. Eight audited endpoint axiom closures contain
only `propext`, `Classical.choice`, and `Quot.sound`; no `sorryAx`.
The project unfinished/project-axiom declaration gate passed.

Research promotion carries the identical source blob and root import, with
this new checkpoint, additive terminology and current-control updates.
Validation-only workflow changes are excluded; the original workflow blob
remains `f194e9564577d3b79831b7abfb91b5933f3af98f`.
Canonical Weil and `main` are unchanged. This is a conditional construction
certificate, not actual source-witness supply or final WD-T40 certification.
