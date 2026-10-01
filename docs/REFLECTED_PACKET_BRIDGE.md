# Reflected-Packet Bridge

**Repository:** Weil-Lab

**Branch:** `research/reflected-packet-bridge`

**Current cursor:** RPB-108 / WD-T40 F-4
**Research standing:** experimental; WD-T40 mathematical standing unchanged, with final Lean assembly still blocked.

## Current standing

This pass continues from `200e25ba4ce3d261841176b30372579bc5cf0782`.
The former RPB-100 overview was stale and is superseded by this current view.
Historical pass notes remain immutable.

The Hermitian Gaussian cutoff bridge, frozen compact-test action,
Fourier/physical prime-shell identification, shell-corrected source-window
globalization, and strict-source/right-limit threshold action correction are
build-certified. Threshold bookkeeping is closed.

The latest threshold-action certificate is run `36871575764`, job
`110400389955`, module blob `2e1a1d755da1414651fe088cf42a787a3df213fa`.
See [threshold-action checkpoint](../notes/REFLECTED_PACKET_BRIDGE_108_SOURCE_THRESHOLD_ACTION_20261001.md).

The previous continuation retains the actual source domain explicitly, proves
complex polarization on that domain, and constructs `q = r + p_h` with the
full compact weak identity from a represented core and central cancellation.
Exact-module validation passed in run `36876381132` (8,954 jobs). These constructions do not supply their
actual source witnesses. See [source-domain continuation](../notes/REFLECTED_PACKET_BRIDGE_108_SOURCE_FORM_DOMAIN_20261001.md).

The mixed-form continuation constructs the actual normalized multiplier-plus-pole
sesquilinear form on that retained domain. Mixed integrals genuinely converge
from the retained log energy and explicit upper symbol bound; Lp a.e. laws
and compact-window moment convergence justify its linear laws. The carrier
moments agree with the previously named pole coefficients. Scoped polarization
now applies to this concrete form, conditional on the retained source diagonal
identity. Exact-module validation passed in run `36896248362` (8,955 jobs),
with eight endpoint axiom closures restricted to the standard three axioms.
See [mixed-form continuation](../notes/REFLECTED_PACKET_BRIDGE_108_SOURCE_MIXED_FORM_20261001.md).

The source-diagonal continuation derives the absolute-symbol bound from retained
shifted lower/upper estimates and evaluates the concrete diagonal as the real
normalized multiplier energy plus `2 Re(conj(Mminus) Mplus)`. For the actual
carrier, this pole expression equals the real Hermitian pairing with the named
physical pole. The source comparison now consumes this explicit quadratic
formula on the retained domain. See [source-diagonal continuation](../notes/REFLECTED_PACKET_BRIDGE_108_SOURCE_DIAGONAL_20261001.md).

The current continuation establishes actual global L1/local integrability,
compact support and exponential-weighted norm integrability for the finite
prime translations. Their support-gap pairing is controlled by L1 mass.
The full residual's present pointwise growth fields require additional
regularity or an integral-growth bridge; compact L2 support does not supply
them. See [prime-regularity continuation](../notes/REFLECTED_PACKET_BRIDGE_108_PRIME_REGULARITY_20261001.md).

| Obligation | Current state |
| --- | --- |
| F-1 physical Fourier carrier | Build-certified |
| Exact normalized multiplier and pole | Build-certified with imported symbol premise |
| F-3 support-gap Gaussian pairing | Build-certified for the specified residual carrier |
| Hermitian cutoff extension | Build-certified conditional on actual compact realization |
| Shell/globalization/threshold action corrections | Build-certified; bookkeeping closed |
| Scoped complex polarization | Build-certified |
| Concrete retained-domain multiplier-plus-pole form | Build-certified with explicit domain/symbol inputs |
| Real source diagonal and derived shifted-comparison bound | Build-certified from retained inputs |
| Residual construction from represented core | Build-certified |
| Actual finite-prime local regularity and integral growth | Build-certified |
| Actual source form-domain membership and form identification | Open |
| Actual core representative, regularity/growth and central cancellation | Open |
| F-4 logarithmic Gaussian coercivity | Not started |
| F-5 exponential weight, strip holomorphy, compact-support zero | Not started |
| F-6 final WD-T40 assembly | Not started |

## Next cursor

~~~text
RPB-108 / WD-T40 F-4 — ACTUAL SOURCE ATTACHMENT

1. Identify the finite-window source domain and attach WD-T38's retained membership hypothesis.
2. Attach the explicit source quadratic identity and normalized shifted
   estimates there; the diagonal and mixed comparison bridges are constructed.
3. Establish the actual core representative with regularity and growth,
   and attach central cancellation of r + p_h. The finite-prime L1 component
   is constructed; the archimedean core and growth bridge remain open.
4. Consume the constructed compact weak realization in the certified
   Hermitian Gaussian bridge, then begin logarithmic coercivity.
~~~

Compact support and L2 membership do not stand in for these source inputs.
Defining a form-domain or core-representation structure does not discharge it.
No Gaussian construction or threshold investigation is to be restarted.

## Governance and custody

Mathematical standing, implementation, build certification and final Lean
certification remain separate. Validation-only workflow changes are excluded
from research promotion. `weil-lab/main` and canonical Weil are unchanged.

The current detailed control is [Lean Formalization Track](LEAN_FORMALIZATION_TRACK.md).
Provenance is in [Reflected-Packet Bridge Provenance](REFLECTED_PACKET_BRIDGE_PROVENANCE.md).
Definitions are in [Terminology](TERMINOLOGY.md) and its additive
[source-domain supplement](TERMINOLOGY_RPB108_SOURCE_DOMAIN.md).
The concrete mixed form is registered in the additive
[mixed-form supplement](TERMINOLOGY_RPB108_MIXED_FORM.md).
The explicit real diagonal and shifted-bound attachment are registered in the
[source-diagonal supplement](TERMINOLOGY_RPB108_SOURCE_DIAGONAL.md).

Finite-prime and integral-growth wording is registered in the additive
[prime-regularity supplement](TERMINOLOGY_RPB108_PRIME_REGULARITY.md).
