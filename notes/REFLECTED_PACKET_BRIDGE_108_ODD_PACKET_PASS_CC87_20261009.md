# CC87: NF45 odd joined packet passes conditionally

CC parent: a793a8eb4703046ff06956416cb00a3fe378b228 (CC86). Read-only Native Source: 5f8a6c1e54a39236df253a5aae5f7be55fee74ed (NF45). Other branches are unchanged.

## Result

At aperture 53/50, NF45's seventh original high polynomial gives a positive definite lower matrix for the fixed three-direction odd joined packet. CC independently authenticates and checks the published interval matrix. This result is conditional on the inherited remaining-high floor A >= (207/1000) I and paid source/domain attachments. The even joined lower matrix still has two positive and one negative directions.

| Quantity | Even | Odd |
|---|---:|---:|
| Seventh-source response at NF44 witness | [-4.70855e-24,5.09105e-24] | [6.38295e-22,6.67556e-22] |
| Complete seven-source condensed margin | [-8.67466e-23,-8.15099e-23] | [4.44738e-22,4.60934e-22] |
| Full joined lower matrix positive under standing floor | No | Yes |
| Necessary additional credit at new witness | >8.152015474305e-23 | None for this packet sign |

These decimal intervals are outward summaries. JSON preserves exact rational enclosures. A failed lower certificate does not establish negativity of the original Weil form. The even gain interval straddles zero; its midpoint must not be used to claim certified improvement.

## Independent consumer checks

The validator authenticates both NF45 certificate hashes and the producer validation manifest. It checks the NF44 parent certificate and frozen trial hashes, exact preservation of all six-column physical/native/source Gram entries and both joined-cross families, physical orthogonality of the seventh polynomial to all six prior columns, physical squared mass in (99/100,1], and positive scalar defect. Published positive-inverse diagnostics are audited; their proofs are not reconstructed here.

It recomputes the signed matrix-update consistency, response at the exact NF44 updated witness, old and new witness values, leading determinant, complete determinant and condensed margin with independent rational interval arithmetic. The odd leading block, full determinant and condensed margin have strictly positive lower bounds. The even condensed margin, determinant and updated witness have strictly negative upper bounds. No assumption that a new condensed margin must be negative is inherited from the earlier consumer.

NF45 reports full native replay PASS, including original source coordinates, reverse covariances, both native action orders, analytic/source errors, seven-versus-six Woodbury algebra, selection and mutation controls. CC imports that report as authenticated producer evidence; it does not rerun those integrations or prove the standing floor.

## Coordinate coercivity consequence

For the odd matrix, write K=[[E,r],[r*,c]], beta=E^-1r and s=c-r*E^-1r. The identity

    x*Kx = (v+beta w)*E(v+beta w) + s w^2

holds for x=(v,w). Since E>0, its smallest eigenvalue is at least det(E)/trace(E). The inverse triangular map from (v+beta w,w) to (v,w) has squared operator norm at most its squared Frobenius norm 3+||beta||^2. Consequently

    K >= min(det(E)/trace(E),s) / (3+||beta||^2) I.

Use a determinant lower bound, trace upper bound, s lower bound and componentwise beta absolute upper bounds. The resulting exact rational epsilon is saved in the consumer JSON; its outward lower enclosure exceeds 1.6072e-46. This very conservative bound establishes retained-coordinate coercivity. It supplies neither a new physical whole-domain gap nor an estimate for unretained coordinates.

## Revised frontier

The odd fixed joined packet's conditional matrix-sign obligation is closed. Source-selection work now targets NF45's updated even witness and the seven-column minorant; CC82/CC84/CC86 remain the full-matrix acceptance and response-conditioning rules. There is no reason to demand another odd witness-deficit payment for the already positive packet, although later enlarged retained systems may need new sources and correlations.

The standing background floor is not proved by NF45 or CC87. Complete remaining-background transport remains an open attachment. The even joined sign, full simultaneous six-retained-direction result, the other 106 retained directions and collective coupling remain open. CC74 and CC78 restrictions and the whole-domain aperture 21/20 anchor remain preserved. Whole aperture 53/50, old-gap-independent all-cap continuation, RH, F4, full transport and Lean closure are not claimed.

## Reproduction

Run `python scripts/certify_cc87_seven_source_consumer.py notes/cc87-source notes/cc85-source --output notes/data/RPB108_CC87_SEVEN_SOURCE_CONSUMER_20261009.json`. Immutable imported NF45 notes, certificates and validation manifest are under `notes/cc87-source`. Certificate-level interval arithmetic decides the consumer sign checks.
