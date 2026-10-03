# RPB-108 — actual native Fourier derivative bridge (2026-10-03)

Parent: `36fa17302379e6f515ef78239bf8404df487f446`.
Cursor: WD-T38 actual source/quadratic/null attachment; F-4 pending.
Threshold bookkeeping is closed.

## Attached actual derivative representation

`NeutralNativeFourierDerivative.lean` uses the existing actual
`conjugateSchwartz` construction to convert the first-antilinear L2
weak derivative identity into Mathlib's bilinear distribution test
convention. Conjugation commutes with the actual Schwartz derivative;
the conjugated test's L2 inner product is its unconjugated integral
pairing against the actual physical L2 vector.

These identities and the already certified native weak derivative prove

    derivative (Lp.toTemperedDistribution GreenSynthesis)
      = Lp.toTemperedDistribution GradientSynthesis.

Both L2 vectors were constructed before this attachment. No equality
with an unspecified representative is assumed.

## Actual Fourier multiplier witness

The one-dimensional derivative is the directional derivative in direction
1. The pinned tempered-distribution Fourier derivative theorem, together
with the pinned compatibility of the actual L2 and distribution Fourier
transforms, therefore proves

    TD(Fourier GradientSynthesis)
      = (2 pi I) * frequency * TD(Fourier GreenSynthesis).

The multiplication on the right is the actual tempered-distribution
`smulLeftCLM` with the real coordinate embedded in complex scalars.
The L2 vector on the left is the actual Fourier transform of the
previously constructed derivative synthesis. This proves an actual
distributional frequency-multiplier representation for the same native
vector and coefficients, under the retained shell-data/count inputs.

## Scope and next mathematical obligation

This equality is not yet a pointwise almost-everywhere frequency-product
identity. Identifying the locally integrable coordinate product with the
L2 distribution representative, then deriving its L2 membership and finite
logarithmic Fourier energy, remains necessary before canonical supported
logarithmic form-domain membership is claimed. The spatial support and
actual L2 weak derivative witnesses are already attached in the parent.

Native background completion remains retained/written. The current WD-T38
carrier is not identified with the native synthesis or that completion
vector. Its actual source quadratic/null law, same-domain mixed/normalized
attachment, and enlarged frozen-action central cancellation remain open.

Current-mode membership
`MemLp (neutralWeilSpectralProduct carrier a) 2` is not derived from WD-T38
and is not assumed. The native Fourier derivative representation does not
supply identification of the independently parameterized current carrier.

Once actual central cancellation is attached, immediately consume
`neutralExteriorIntegralGrowthResidual_realizes_of_central` for the
certified locally integrable residual, boundary removal, and whole compact
weak realization. Exterior, digamma, boundary, and threshold work remain
closed. F-4 remains pending.

## Validation

Validation commit: `16a101a5c5d06cea6c65bdc57dfabcc2c5af1a12`.
GitHub Actions run `37141841223`, job `111257733982`:
root build passed (9037 jobs). All four public theorem audits use only
`propext, Classical.choice, Quot.sound`, with no `sorryAx`.
The unfinished/project-axiom declaration gate passed.
Research workflow and historical notes are preserved.
