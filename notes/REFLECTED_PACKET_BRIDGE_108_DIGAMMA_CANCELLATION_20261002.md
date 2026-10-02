# RPB-108 — actual centered digamma residual cancellation

Date: 2026-10-02 (America/Los_Angeles).
Recovered research head: `66ed85ef2dccd622e84a062489876e825912e248`.

## Actual source-line cancellation

The source line z(t)=1/4+i t/2 lies in the certified right half-plane.
Map the actual complex Euler HasSum through the continuous real-part map.
The certified reciprocal real-part formula identifies its terms as

    1/(n+1)-neutralGaussReciprocal(n,t),

with endpoint Re ψ(z(t))+γ. Subtract the t instance from the zero instance.
The regularizing terms and Euler constant cancel exactly, giving

    HasSum [reciprocal(n,t)-reciprocal(n,0)]
           [Re ψ(z(0))-Re ψ(z(t))].

At t=2πξ, embedding this real HasSum and using the certified actual
increment formula gives the increment series endpoint -C_0(ξ).
Thus the represented actual residual C_0+∑' increments is zero, and the
actual centered symbol C_N tends pointwise to zero at every frequency.
No representation, Gauss formula or growth premise enters this cancellation.

## Actual action consequence

The represented frequency residual pairing is zero on every Schwartz test.
The existing certified dominated-convergence transfer then proves that the
actual centered multiplier action tends to zero on each such test. This
transfer retains its full-symbol temperate-growth premise. No smooth
limiting-symbol CLM or operator norm convergence is asserted.

Next: consume the existing equality between represented residual pairings
and the actual exterior attachment defect. Exterior and whole source
attachment, central/boundary reconstruction and actual source-domain/
quadratic/polarization/normalized estimate witnesses remain open.
Canonical Weil, main and WD-T40 mathematical standing are unchanged.
Threshold bookkeeping is closed; logarithmic coercivity has not started.

## Certification

Certification: Lean 4.34.0 / pinned mathlib `5ed2965256430c3649e86755f9576b54eca72435`; 8,979 build jobs passed. All seven endpoint audits use only `propext`, `Classical.choice`, and `Quot.sound`; declaration gate passed. Validation head `55758c60bff80e626d63d461f150f0c7613d9449`, run `37067232863`, job `111038005004`, source blob `6f1ffdfdd94ab79ce0f08ed1afa6195150e4b81d`.

Validation-only workflow/cache changes are excluded from research promotion;
historical notes are immutable.
