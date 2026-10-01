# Terminology registry — RPB-108 source domain and core representation

This additive companion to [Terminology](TERMINOLOGY.md) registers the names
used by `NeutralWeilSourceFormDomain.lean` before any claim of actual source
attachment.

## Retained source form domain

The retained source form domain is a complex submodule of physical L2 whose
members have finite logarithmically weighted Fourier energy. The attachment
`NeutralSourceFormDomainAttachment` requires explicit membership of the actual
carrier. It does not infer membership from compact support, L2 membership, or
smoothness of its ordinary Fourier transform. A diagonal source identity must
be established separately on that domain.

Complex polarization determines mixed terms on the domain itself. All four
polarization vectors remain in the domain by its submodule structure; this
does not extend the form to all L2 vectors or to arbitrary exterior tests.

## Core function representation

`NeutralWeilCoreFunctionRepresentation` is a locally integrable function `r`
with explicit exponential bounds that represents the fixed-cutoff tempered
multiplier core on all compact Schwartz tests. The function, its regularity,
and this exact representation remain source obligations. The mere existence
of a tempered multiplier does not supply them.

## Residual constructed from the core

`neutralWeilResidualFromCore` constructs `q = r + p_h` using the already
certified named pole. Its growth constant is the sum of the two constants and
its growth rate is the maximum of the two rates. Central a.e. cancellation is
required for this specific sum. Its full compact weak identity is derived
from the core representation and genuine product integrability.

**Registration:** RPB-108 continuation, October 1, 2026 (America/Los_Angeles).
