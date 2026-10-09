# RPB108 — NF42: original boundary defect-source response

Date: 2026-10-09. Aperture a=53/50. Branch:
`research/rpb108-phase-geometry-localization`.
Parent: `4d2a5d7d3857854677a223ca38d03b13358f40e9` (NF41).

The [additive NF42 terminology note](../docs/TERMINOLOGY_RPB108_BOUNDARY_RESPONSE_NF42.md)
fixes the definitions before use. Earlier reports and wording are unchanged.

NF42 constructs the **boundary defect-source covariance packet** required
by NF41. It uses those original signed moments to enclose a **conditional
joined inverse improvement certificate** through the **four-high-source
minorant**. The floor hypothesis remains explicit.

## Original physical source moments

Keep the frozen Z=(z0,z1), R=(r0,r1,r2) and boundary
Y=(e112,e114) even or (e113,e115) odd. A denotes the original remaining
high background, after physical projection off the native retained block.
Each AY source is reconstructed with its exact endpoint logarithm,
rational degree-320 regular kernel, degree-40 pole approximation and all
13 original prime translation cells. Its retained coordinates are the
original signed native archive intervals. The source errors include the
uniform analytic error and the physical error of that retained projection.

The new original source packet consists of three symmetric boundary
source Gram entries, four boundary/old-high-source covariances and six
boundary/joined-source crosses per parity. Each is a polynomial/logarithm
moment integral with an outward physical error payment. For approximants
s_i,s_j with source errors e_i,e_j, the cross payment is
`e_i ||s_j|| + e_j ||s_i|| + e_i e_j`; the square payment is
`2 e_i ||s_i|| + e_i²`. All upper norms are outward enclosures, not sampled
norms. The JSON certificates preserve the reconstructed moments, payments,
original paid intervals, source errors and retained coordinate intervals.

## Actual defect-source response estimate

Put kappa=207/1000, C=Z*AZ-kappa Z*Z, V=AZ-kappa Z,
A0=kappa I+V C^-1 V*. NF40 already certified the positive compression
D_Y=Y*(A-A0)Y. NF42 supplies the actual defect-source columns
F=(A-A0)Y=AY-kappa Y-V C^-1 P*, where P=Y*V.

From the new original source packet and inherited signed moments,
compute F*F, F*R and F*V with all errors paid. With
N=C+V*V/kappa and W=R*V, Woodbury gives

\[
g=F^*A_0^{-1}R=\kappa^{-1}F^*R-
\kappa^{-2}F^*V N^{-1}W^*,
\]

\[
M_F=F^*A_0^{-1}F=\kappa^{-1}F^*F-
\kappa^{-2}F^*V N^{-1}V^*F.
\]

The outward denominator D_Y+M_F is certified positive definite. Under
**A >= kappa I on the original remaining high space**, positivity of
D=A-A0 implies D >= F D_Y^-1 F*. Therefore

\[
R^*(A_0^{-1}-A^{-1})R\succeq
\Delta=g^*(D_Y+M_F)^{-1}g.
\]

NF42 encloses this full signed 3 by 3 matrix contribution and adds it to
the original NF38/NF39 joined Schur lower matrix. A strictly positive
frozen-witness value of Delta certifies a genuine response improvement
under the hypothesis and excludes zero-response models matching this
expanded source packet. This does not by itself prove positivity of the
whole joined Schur matrix, a new background floor, or whole-domain Weil
positivity.

## Certified outcome

For the already frozen, unnormalized NF38 witness h (third coordinate 1),
the source-backed Woodbury improvement has these outward display bounds:

| Conditional quantity | Even | Odd |
| --- | ---: | ---: |
| h*Delta h | [1.68013122983, 1.78712561456] × 10⁻²⁴ | [1.98181339342, 1.98435969486] × 10⁻²² |
| Necessary further improvement relative to A1, strict lower bound | 9.39362146648 × 10⁻²³ | 1.45753955024 × 10⁻²¹ |

The improvement is strictly positive in both sectors. Its size is about
1.8% even and 12% odd of NF39's necessary witness threshold. Thus NF41's
zero-response possibility is excluded under the floor hypothesis, but
this particular four-high-source minorant still does not certify the
joined Schur sign. Both improved lower matrices have positive leading
2 by 2 blocks and rigorously negative determinants and condensed margins.
The upper endpoint of the improved frozen-witness value is also negative.
These are failures of the computed lower certificate, not negative
original Weil-form values.

More precisely, writing T1=R*(A1^-1-A^-1)R, the actual joined Schur matrix
is Q-R*A1^-1R+T1. Strict positivity of the joined Schur matrix requires h*T1 h greater than minus the
upper endpoint of the certified A1 witness value. The displayed necessary
further improvements are rounded downward from those exact bounds.
They are necessary witness conditions, not a sufficient whole-matrix test.

The next arithmetic step is to choose and freeze an additional original
high polynomial from the remaining inverse-coupled witness, physically
orthogonal to the four current high directions, then certify its native
block and complete signed source covariances. The new bound leaves a quantified response deficit for this next
source certificate to address.

## Independent algebra and arithmetic checks

Let H=(Z,Y), U=(A-kappa I)H and C4=H*U. The original source/native
moments give C4>0 via C>0 and the positive boundary Schur compression.
The direct four-high-source minorant is

\[
A_1=\kappa I+U C_4^{-1}U^*.
\]

It equals A0+F D_Y^-1 F*. The validator uses exact rational four-column
Woodbury algebra, independently of the sequential interval response
formula, to verify this identity and the resulting joined inverse matrix.
The chosen rational algebra lies inside the original outward response
intervals. No finite abstract model is presented as an original Weil
operator.

Moment products use **carry-free integer convolution**. Integer centers
and radii give coefficient bounds through
`|a|*radius(b) + radius(a)*|b| + radius(a)*radius(b)`; exact convolution
is followed by outward division by the 500-digit grid. Binary packing
uses a bit width strictly above the largest possible coefficient, so
there is no cross-coefficient carry. Signed offsets are subtracted with
exact prefix sums. This replaces only polynomial product arithmetic,
not the source kernel, moment formulas, endpoint constants or physical
error bounds.

The validator checks signed integer products against direct sums,
exhaustively checks interval endpoint vertices in small controls, and
recomputes one boundary source square per parity with the inherited
interval product algorithm. It also replays every new source covariance
in reverse order, all payments and the full response matrix. No numerical
quadrature or sampling enters the proof.

## Reproducibility

With the authenticated native archives, run from the repository root:

```sh
python scripts/certify_native_boundary_response_nf42_106.py --parity even --output notes/data/RPB108_NF42_EVEN_BOUNDARY_RESPONSE_CERTIFICATE_20261009.json
python scripts/certify_native_boundary_response_nf42_106.py --parity odd --output notes/data/RPB108_NF42_ODD_BOUNDARY_RESPONSE_CERTIFICATE_20261009.json
python scripts/validate_native_boundary_response_nf42_106.py --output notes/data/RPB108_NF42_BOUNDARY_RESPONSE_VALIDATION_20261009.json
```

NF41's two certificates and validation manifest are authenticated before
new work. Original native archives and prior source inputs retain their
inherited hash checks. The defect-source controls include positive
boundary defects with zero uncoupled response, nonzero physical coupling
with zero response, and a positive source-coupled response bounded below
by the exact Woodbury contribution. The six inherited full-block crossing
controls and three positive whole-physical-mass controls also pass.

Validation: **PASS**. Both parity covariance replays, the inherited
product reference squares, the exact joint/sequential inverse identity,
and all controls passed.

## Scope

The new response estimate is conditional on the stated original remaining
high floor. That floor is not newly established here. Complete remaining
background transport and whole-domain positivity at 53/50 remain open.
The highest internally certified whole-domain aperture remains 21/20.
RH, F4 and Lean closure are not claimed. Only Phase Geometry is written;
Coupled, DNE and the paused branches are unchanged.
