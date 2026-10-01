# Reflected-Packet Bridge

**Repository:** Weil-Lab

**Branch:** `research/reflected-packet-bridge`

**Current cursor:** RPB-108 / WD-T40 F-4
**Research standing:** experimental; WD-T40 mathematical standing unchanged, with final Lean assembly still blocked.

## Current standing

The live pointer was recovered from `fe92dffc4794a519a382a2533dc4313580fa443d`.
The former RPB-100 overview was stale and is superseded by this current view.
Historical pass notes remain immutable.

The Hermitian Gaussian cutoff bridge, frozen compact-test action,
Fourier/physical prime-shell identification, shell-corrected source-window
globalization, and strict-source/right-limit threshold action correction are
build-certified. Threshold bookkeeping is closed.

The latest threshold-action certificate is run `36871575764`, job
`110400389955`, module blob `2e1a1d755da1414651fe088cf42a787a3df213fa`.
See [threshold-action checkpoint](../notes/REFLECTED_PACKET_BRIDGE_108_SOURCE_THRESHOLD_ACTION_20261001.md).

The new continuation retains the actual source domain explicitly, proves
complex polarization on that domain, and constructs `q = r + p_h` with the
full compact weak identity from a represented core and central cancellation.
Exact-module validation passed in run `36876381132` (8,954 jobs). These constructions do not supply their
actual source witnesses. See [source-domain continuation](../notes/REFLECTED_PACKET_BRIDGE_108_SOURCE_FORM_DOMAIN_20261001.md).

| Obligation | Current state |
| --- | --- |
| F-1 physical Fourier carrier | Build-certified |
| Exact normalized multiplier and pole | Build-certified with imported symbol premise |
| F-3 support-gap Gaussian pairing | Build-certified for the specified residual carrier |
| Hermitian cutoff extension | Build-certified conditional on actual compact realization |
| Shell/globalization/threshold action corrections | Build-certified; bookkeeping closed |
| Scoped complex polarization | Build-certified |
| Residual construction from represented core | Build-certified |
| Actual source form-domain membership and form identification | Open |
| Actual core representative, regularity/growth and central cancellation | Open |
| F-4 logarithmic Gaussian coercivity | Not started |
| F-5 exponential weight, strip holomorphy, compact-support zero | Not started |
| F-6 final WD-T40 assembly | Not started |

## Next cursor

~~~text
RPB-108 / WD-T40 F-4 — ACTUAL SOURCE ATTACHMENT

1. Identify the finite-window source domain and attach WD-T38's retained membership hypothesis.
2. Attach the diagonal multiplier/pole form there; consume scoped polarization.
3. Establish the actual core representative with regularity and growth,
   and attach central cancellation of r + p_h.
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
