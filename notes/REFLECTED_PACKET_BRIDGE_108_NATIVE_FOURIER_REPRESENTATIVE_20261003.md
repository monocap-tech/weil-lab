# RPB-108 — actual native Fourier representative identified (2026-10-03)

Parent: `5647cf49c7b6abe2edd58fa0daf34444d01ec7dd`.
Cursor: WD-T38 actual source/quadratic/null attachment; F-4 pending.
Threshold bookkeeping is closed.

## Definition before use

`neutralNativeFourierDerivativeProduct a data v` is the actual function

    (2 pi I) * xi * (Fourier GreenSynthesis v)(xi).

Its input is the already constructed native physical Green synthesis with
the same actual `lp 2` shell coefficient vector and retained shell data.
It is the first-derivative frequency product; it is not the full Weil
spectral product.

## Proved witnesses

The product is locally integrable before its global L2 membership is
known: the actual L2 Fourier vector is locally integrable, and the linear
frequency factor is continuous.

Apply the parent's proved tempered-distribution frequency identity to each
Schwartz test. The actual distribution multiplication and actual L2
distribution integral give the concrete integral pairing

    integral u * Fourier GradientSynthesis
      = integral u * derivativeFrequencyProduct.

Use the pinned locally integrable compact-smooth test uniqueness theorem.
Every real compact smooth test is embedded into the already lawful complex
Schwartz test construction. This identifies, almost everywhere, the
actual function product with the actual L2 Fourier transform of the
constructed derivative synthesis.

Consequently `MemLp derivativeFrequencyProduct 2` follows by the actual
almost-everywhere identity and the derivative synthesis's L2 Fourier
membership. There is no imported representation equality and no added
spectral-domain premise.

## Scope and next attachment

The native derivative-frequency regularity witness is now genuinely
derived from the retained positive-window, shell-data/count inputs and
the constructed native coefficient vector. Finite logarithmic Fourier
energy and canonical supported form-domain attachment still need the
weight-domination argument. Spatial compact support is already attached.

Native background completion remains retained/written. The current WD-T38
physical carrier has not been identified with this native synthesis or
with the retained form-completion vector. Its actual source quadratic/null,
same-domain mixed/normalized, and enlarged frozen-action central
attachments remain open.

Current-mode membership
`MemLp (neutralWeilSpectralProduct carrier a) 2` is still not derived from
WD-T38 and is not assumed. Do not replace that full Weil spectral witness
with the different native derivative-frequency witness proved here.

Once actual central cancellation is attached, immediately consume
`neutralExteriorIntegralGrowthResidual_realizes_of_central` for the
certified locally integrable actual residual, boundary removal, and whole
compact weak realization. Exterior, digamma, boundary, and threshold work
remain closed. F-4 remains pending.

## Validation

Validation commit: `336fb2d506b5947e6c6141a13c15a94aaa01a23e`.
GitHub Actions run `37143038270`, job `111261239645`: full root build
passed (9,038 jobs). All four public theorem axiom audits passed with only
`propext`, `Classical.choice`, and `Quot.sound`; no project axiom or
unfinished-proof declaration was introduced.
