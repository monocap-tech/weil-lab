# RPB108 — NF43: a fifth original high source from the inverse witness

Date: 2026-10-09. Aperture a=53/50. Branch:
`research/rpb108-phase-geometry-localization`.
Recovered parent: `f2c49f8d2ff95374d3ee2c3b1836ec772e4817dc` (NF42).

The [additive terminology note](../docs/TERMINOLOGY_RPB108_INVERSE_WITNESS_NF43.md)
defines the new objects before their load-bearing use. Earlier reports,
definitions, source vectors and certificates remain unchanged.

NF43 adds one original high polynomial and its complete signed source
packet in each parity sector. It certifies a further positive inverse
response under the same remaining-background floor hypothesis. The odd
sector response is substantially larger than NF42's contribution. Both
joined lower certificates still fail; no negative original form is proved.

## Exact selection and physical custody

Let H4 consist of NF38's two original high polynomials and NF40's two
boundary polynomials. Rescale the first two by recorded rational upper
physical norms, preserving their physical span and the NF42 minorant A1.
With kappa=207/1000, set U4=(A-kappa I)H4, C4=H4*U4,
T4=U4*U4, W4=R*U4 and N4=C4+T4/kappa. The original signed packet gives

q=A1^-1 R h=R h/kappa-U4 N4^-1 W4* h/kappa^2,

where h is the unchanged NF38 witness and R its unchanged joined source
family. C4 and N4 are certified positive by rational congruence and
Gershgorin bounds; a rational approximate inverse is rigorously enclosed
through its residual row norm. Decimal arithmetic only selects rational
preconditioners and supplies no sign certificate.

The new fifth polynomial y restricts q to physical Legendre degrees
116..180 even or 117..179 odd, down-rounds coordinate midpoints to
denominator 10^100, projects exactly off the two restricted old high
polynomials, and divides by a rational upper physical norm. Its first two
boundary coordinates vanish. Thus its physical inner products with all
four old high columns are exactly zero, and its exact physical mass
squared lies in (99/100,1]. It belongs to the same original remaining
high space. It is a trial selected from q, not an asserted equality y=q.

The orthogonal inverse-witness shell square has a strictly positive
enclosure in each parity. The fixed JSON trials preserve the original
enclosed source coordinates, inverse coefficients, rounding, exact tail
Gram, projection coefficients, normalization and final rational y.

## Complete original source packet

The source of y uses the original exact endpoint logarithm, rational
degree-320 regular kernel, degree-40 signed pole approximation and all 13
original prime translation cells. Its native energy and seven native
crosses are enclosed with analytic source errors. Independently reversed
native source actions overlap every paid cross enclosure.

Physical projection removes the same native retained block as NF42.
Its midpoint-coordinate rounding error is paid outward, including the
rounding caused by rescaling the old source coordinates. NF43 encloses
the fifth projected source square and all seven complete signed source
covariances, against the four old high sources and the three unchanged
joined sources. Polynomial/logarithm moments retain all endpoint, regular,
prime, pole and mixed terms. No quadrature or sampling is used.

For source errors e_i,e_j and outward approximant norm bounds N_i,N_j,
the cross payment is e_i N_j+e_j N_i+e_i e_j; the square payment is
2 e_i N_i+e_i^2. All original intervals, reconstructed moments and
payments are preserved in the certificate. Carry-free integer convolution
is the same validated exact arithmetic as NF42.

## Conditional five-source inverse estimate

Put H5=(H4,y), U5=(A-kappa I)H5, C5=H5*U5,
T5=U5*U5 and W5=R*U5. The fifth native Schur defect and C5 are certified
positive. Under **A >= kappa I on the original remaining high space**,

A >= A2=kappa I+U5 C5^-1 U5* >= A1,

so the full signed matrix R*(A1^-1-A2^-1)R is an additional lower
contribution to the actual inverse improvement. The Woodbury formula is

R*A2^-1 R=R*R/kappa-W5(C5+T5/kappa)^-1 W5*/kappa^2.

The validator also computes the exact rational scalar-defect update after
eliminating the first four high columns. It verifies equality with the
direct five-column Woodbury difference and containment in the original
paid interval matrix. This is an independent algebra check, not a finite
abstract model asserted to be the original Weil operator.

## Certified outcome

The following displays round lower endpoints downward and upper endpoints
upward. Witness values use the original unnormalized NF38 witness.

| Quantity | Even | Odd |
| --- | ---: | ---: |
| Extra h*R*(A1^-1-A2^-1)R h | [2.28765, 11.43355] × 10^-24 | [1.04637, 1.07109] × 10^-21 |
| Five-source joined condensed margin | [-9.21239, -8.70829] × 10^-23 | [-4.74470, -4.60740] × 10^-22 |
| Necessary further response at the updated witness, strict lower bound | 8.70942 × 10^-23 | 4.60898 × 10^-22 |

The additional frozen-witness response is strictly positive in both
sectors. The odd lower bound exceeds five times the upper endpoint of
NF42's response contribution at that same original witness.

Both five-source joined lower matrices have positive leading 2 by 2
blocks and rigorously negative determinants and condensed margins. Their
original frozen-witness values also have negative upper endpoints. These
are failures of Q-R*A2^-1R, not negative original Weil-form values.

For each parity, NF43 additionally freezes a rational witness selected
from the new condensed lower matrix. If the actual joined Schur matrix
Q-R*A^-1R is strictly positive, that updated witness must receive an
extra response from R*(A2^-1-A^-1)R exceeding the displayed necessary
threshold. The thresholds are necessary witness conditions, not
sufficient whole-matrix tests. The updated witness differs from NF38's
original witness; their response deficits must not be conflated.

## Reproducibility and validation

Run with the authenticated native archives and earlier NF inputs:

```sh
python scripts/certify_native_inverse_witness_nf43_106.py choose --parity even --output notes/data/RPB108_NF43_EVEN_FIXED_INVERSE_WITNESS_20261009.json
python scripts/certify_native_inverse_witness_nf43_106.py choose --parity odd --output notes/data/RPB108_NF43_ODD_FIXED_INVERSE_WITNESS_20261009.json
python scripts/certify_native_inverse_witness_nf43_106.py certify --trial notes/data/RPB108_NF43_EVEN_FIXED_INVERSE_WITNESS_20261009.json --output notes/data/RPB108_NF43_EVEN_INVERSE_WITNESS_CERTIFICATE_20261009.json
python scripts/certify_native_inverse_witness_nf43_106.py certify --trial notes/data/RPB108_NF43_ODD_FIXED_INVERSE_WITNESS_20261009.json --output notes/data/RPB108_NF43_ODD_INVERSE_WITNESS_CERTIFICATE_20261009.json
python scripts/validate_native_inverse_witness_nf43_106.py --output notes/data/RPB108_NF43_INVERSE_WITNESS_VALIDATION_20261009.json
```

The recovered 147 repository inputs match the live NF42 tree with no
mismatches. NF42's independent validation passed again and its parsed
manifest is identical to the archived manifest. NF43 pins both NF42
source certificates, authenticates their inherited inputs, and pins each
fixed trial before source certification.

NF43 independent validation: **PASS**. It checks exact physical selection
and rejects a nonorthogonal mutation; independently checks inverse-witness
source coordinates; reconstructs the fifth source, its square and all
reverse signed source covariances; replays all error payments, inverse
proofs and sign outcomes; and checks the exact scalar/direct Woodbury
identity. It also reruns NF42's packing and defect-response controls and
the inherited genuine full-block crossings and positive whole-mass
controls.

## Next frontier and scope

The next source step should use the updated five-source witness, not the
old NF38 witness: reconstruct A2^-1 R h_new, project its shell component
off all five existing high polynomials, then freeze and certify the next
original source packet. The new thresholds quantify what any sufficient
response must overcome. An alternative is an original remaining-background
estimate strong enough to pay these full matrix deficits directly.

The background floor remains an explicit hypothesis and is not newly
proved here. Complete remaining-background transport and whole-domain
positivity at a=53/50 remain open; the highest internally certified
whole-domain aperture remains 21/20. RH, F4 and Lean closure are not
claimed. Only this Native Source/NF checkpoint on the existing branch is
written; Coupled, DNE and other branch refs are unchanged.
