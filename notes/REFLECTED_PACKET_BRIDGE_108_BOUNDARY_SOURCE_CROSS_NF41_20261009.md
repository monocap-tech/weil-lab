# RPB108 — NF41: signed boundary source coupling and the defect-source frontier

Date: 2026-10-09. Aperture a=53/50. Branch:
`research/rpb108-phase-geometry-localization`.
Parent: `090e389c030c9b488de00d1e44a6b1b6bd43f96c` (NF40).

Read [the additive terminology note](../docs/TERMINOLOGY_RPB108_BOUNDARY_SOURCE_CROSS_NF41.md)
before the definitions below. Historical wording is unchanged.

NF41 certifies the **signed boundary/source cross matrix** J=Y*R for
both parity sectors. It establishes nonzero **projected boundary inverse
coupling**, excluding NF40's specific model supported on span(Ytilde).
It then constructs a **fixed-cross zero-response extension** that retains
these newly certified crosses. The remaining arithmetic object is the
**defect-source columns** F=(A-A0)Y and their signed response coupling.

## New original arithmetic source certificate

Keep NF37's three frozen selected polynomials and their projected complete
physical source columns R, as used by NF38–NF40. The boundary columns are
Y=(e112,e114) even and Y=(e113,e115) odd. They are physically orthonormal
and outside the retained native block; the retained source subtraction
therefore contributes zero to Y*R.

For each of the three frozen polynomials, reconstruct its complete
archimedean, prime and pole source on the original 13 translation cells.
Use the rational degree-320 regular kernel, the degree-40 pole polynomial,
and the exact endpoint logarithmic moments, on the inherited 500-digit
outward grid. Each of the two boundary Legendre pairings is enlarged by
eta times an upper bound for the exact polynomial physical norm.
An independent reverse source pairing checks original symmetry with
the same physical error payment. No quadrature or sampled transforms
enter the certificate.

These are six signed original cross intervals per parity, rather than
unsigned absolute-value replacements. Their exact endpoints and source
payments are recorded in the parity JSON certificates. The frozen
polynomial coefficients are recorded explicitly and authenticated through
the inherited chain; no new direction or functional is selected here.

## What the new coupling proves

Write kappa=207/1000, C=Z*AZ-kappa M, V=AZ-kappa Z,
A0=kappa I+V C^-1 V*, T_V=V*V, W=R*V, and N=C+T_V/kappa.
The outward 2 by 2 inverse of N is positive definite. With X=Y*Z,
P=Y*V, B=R*Z and J=Y*R, the physical inverse coupling is

\[
H=\widetilde Y^*A_0^{-1}R
 =\kappa^{-1}(J-XM^{-1}B^*)
 -\kappa^{-2}(P-XM^{-1}C)N^{-1}W^*.
\]

The producer encloses H with all original native/source errors paid.
For the already frozen NF38 witness h, the outward lower bound on
||Hh||^2 is strictly positive in both sectors. NF40's specific extension
required H=0 and is therefore excluded by this new original arithmetic
data. H is coupling of physical boundary vectors to inverse sources;
it is not yet coupling of defect-source columns to inverse sources.

The following display encloses the squared coupling for that frozen,
unnormalized witness (its third joined coordinate is 1). These are
coupling norms, not inverse-response improvements:

| Quantity | Even | Odd |
| --- | ---: | ---: |
| ||Hh||², outward displayed enclosure | [2.25720093567, 2.89364726211] × 10⁻²⁵ | [2.52357001799, 2.52818641764] × 10⁻²² |

## Why the fixed crosses still do not force improvement

Select rational moments inside the authenticated packet and the new J
intervals. The extended nine-vector Gram of (Z,V,R,Y) is exactly positive
definite. The J values are now fixed to the new interval midpoints and
are no longer freely chosen to enforce H=0.

Instead put S=(Z,A0^-1 R), let P_S be its physical orthogonal projector,
and define Yhat=(I-P_S)Y. Exact rational Gram calculations certify the
five-dimensional S Gram and the two-dimensional L=Yhat*Yhat as positive
definite. Keep the chosen positive boundary compression
D_Y=QY-kappa I-P C^-1P*. Set

\[
D_-=\widehat Y L^{-1}D_Y L^{-1}\widehat Y^*,
\qquad A_-=A_0+D_-.
\]

This gives D_->=0, D_-Z=0, Y*D_-Y=D_Y, and
D_-A0^-1 R=0. Thus A_->=kappa I, A_-Z=AZ, Y*A_-Y=QY, and

\[
A_-^{-1}R=A_0^{-1}R.
\]

Every NF39 aggregate moment, NF40's chosen boundary energy block, and
NF41's chosen signed J matrix match exactly. Nevertheless the joined
inverse improvement is zero on all three source columns and the abstract
joined Schur matrix is exactly NF39's negative minimal-background ceiling.

This model is an enclosure-compatible finite Hilbert realization only.
It does not match complete original Weil identities, all polynomial
coordinates, boundary source covariance data, or the actual unknown
exact moments. Actual original Weil negativity is not claimed. The result
shows that the currently enclosed packet, even with J fixed, cannot
certify the needed improvement without additional source information.
NF41 does not claim an opposite-sign model for this expanded packet.

## Concrete next arithmetic estimate

Under the NF39 background-floor hypothesis, D=A-A0 is positive
semidefinite. Reconstruct F=DY=AY-A0Y with its physical errors and
certify its signed crosses. Since D_Y=Y*DY>0,

\[
D\succeq F D_Y^{-1}F^*,\qquad
A\succeq A_0+F D_Y^{-1}F^*.
\]

Woodbury then yields the sufficient joined response bound

\[
R^*(A_0^{-1}-A^{-1})R\succeq
R^*A_0^{-1}F\,(D_Y+F^*A_0^{-1}F)^{-1}\,F^*A_0^{-1}R.
\]

This is the next quantitative target. Unlike H, it involves the actual
signed defect-source response coupling F*A0^-1R. A positive witness
value must pay NF39's necessary response threshold; certifying the whole
joined Schur matrix requires its full signed matrix contribution.
The hypothesis and all source errors must remain explicit. The formula
is a sufficient certificate route, not a completed actual response bound.

## Reproducibility and validation

From the repository root with the authenticated native archives:

```sh
python scripts/certify_native_boundary_source_cross_nf41_106.py --parity even --output notes/data/RPB108_NF41_EVEN_BOUNDARY_SOURCE_CROSS_CERTIFICATE_20261009.json
python scripts/certify_native_boundary_source_cross_nf41_106.py --parity odd --output notes/data/RPB108_NF41_ODD_BOUNDARY_SOURCE_CROSS_CERTIFICATE_20261009.json
python scripts/validate_native_boundary_source_cross_nf41_106.py --output notes/data/RPB108_NF41_BOUNDARY_SOURCE_CROSS_VALIDATION_20261009.json
```

The validator authenticates NF40's certificates and manifest, replays
NF40's native defect and exact extension, recomputes all six new forward
and reverse source pairings in each parity, and reconstructs the new
projector and PSD factor without calling the producer's model routine.
It verifies all named moment identities, fixed new signed crosses,
positive Hilbert Grams and the exactly zero response.

Controls include three cases with both nonzero physical boundary inverse
coupling and positive boundary defect but zero inverse improvement;
adding a defect coupled to the inverse source gives a positive response.
The defect-source Woodbury lower bound is independently checked against
the exact inverse, including positivity of the leftover defect.
The six inherited full-block crossings and three positive whole-physical-
mass controls are also replayed.

Validation: **PASS**. Both parity source replays, exact model identities,
and the independent exact/outward inverse-coupling checks passed.

The actual inverse improvement, complete remaining background transport,
and whole-domain Schur sign at 53/50 remain open. The certified whole-domain
aperture remains 21/20. RH, F4 and Lean closure are not claimed. Only the
Phase Geometry branch is written; the other fronts are unchanged.
