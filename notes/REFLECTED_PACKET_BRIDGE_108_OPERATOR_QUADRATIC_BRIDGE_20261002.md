# RPB-108 — physical operator/quadratic bridge

Continues from `41e3532aa83905dac6255b5cf5dbd9f3f799becc`.

`NeutralOperatorQuadraticBridge` identifies the physical L2 core pairing
with the exact normalized spectral multiplier pairing by Plancherel.
Genuine L2 Hermitian integrability and a.e. spectral representative laws
justify the physical pairing. On the carrier column, every test vector in
the concrete source form domain now has its multiplier pairing identified
with the physical operator core. Combining the certified real diagonal
with the existing Hermitian pole identity gives the concrete carrier
quadratic energy as the real physical core pairing plus the real pole pairing.
The chosen physical carrier representative also has a genuinely convergent
core pairing.

Actual spectral operator-domain membership remains an explicit open input.
The bridge adds no positive comparison, central cancellation or imported
source quadratic identity premise. It identifies the constructed form and
constructed operator core, not a separately imported source form or the
abstract endpoint-null extension. That source attachment, polarization
attachment, central cancellation and actual whole-source realization remain
open. Threshold bookkeeping is closed; logarithmic coercivity has not started.

## Certified endpoints

- `l2HermitianPairing_integrable`
- `neutralWeilOperatorDomainCore_hermitian_pairing`
- `sourceDomainMultiplierPairing_operatorCore`
- `neutralWeilOperatorDomainCore_carrier_pairing_integrable`
- `sourceDomainQuadratic_operatorCore`

Certification: Lean 4.34.0 / pinned mathlib `5ed2965256430c3649e86755f9576b54eca72435`; 8,987 build jobs passed. All five endpoint audits use only `propext`, `Classical.choice`, and `Quot.sound`; declaration gate passed. Validation head `f202f6ddc684478102061f9b1cfc0f2e8ff4f741`, run `37077578096`, job `111070781347`, source blob `89e41c3a3bf68c4685d461a1d989a0532a020f32`.

~~~text
RPB-108 / WD-T40 F-4 — CONTINUES
PHYSICAL CORE ↔ EXACT SPECTRAL CARRIER COLUMN: IDENTIFIED
CONCRETE QUADRATIC ↔ PHYSICAL CORE + POLE ENERGY: IDENTIFIED
PHYSICAL CARRIER CORE PAIRING: GENUINELY INTEGRABLE
ACTUAL SPECTRAL OPERATOR MEMBERSHIP: OPEN
IMPORTED SOURCE / ENDPOINT-NULL ATTACHMENT: OPEN
CENTRAL CANCELLATION + WHOLE SOURCE REALIZATION: OPEN
THRESHOLD BOOKKEEPING: CLOSED
LOGARITHMIC COERCIVITY: NOT STARTED
~~~

The exact normalized Fourier transform is the existing L2 isometry. Its inner-product preservation supplies the physical/spectral equality; the product's toLp representative is used only through its a.e. equality. The actual carrier h is likewise substituted only a.e. The concrete diagonal and previously certified Hermitian pole term then give physical core-plus-pole energy with no hidden scaling constant.

This identifies the concrete form on the operator-domain carrier column. It neither identifies a separately imported source form on all vectors nor proves that the abstract endpoint-null operator is this physical multiplier-plus-pole operator. Those are the remaining source attachment obligations, not consequences of naming the concrete quadratic.

Terminology: [physical operator/quadratic bridge](../docs/TERMINOLOGY_RPB108_OPERATOR_QUADRATIC_BRIDGE.md).
Validation-only workflow is excluded from research promotion; historical notes remain unchanged.
