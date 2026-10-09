# RPB108 — NF36: collective high correction of the mixed floor witnesses

2026-10-09 UTC. Phase Geometry parent NF35 is
`e8073998dbfaf313180efcbbacf824da5f9cc0d5`. Coupled CC78 was read only
at `14dcfae9c91304f2fc8677586605f795f0d06c6e`. No other or paused branch
is modified. Definitions precede use in the additive
[NF36 terminology entry](../docs/TERMINOLOGY_RPB108_COLLECTIVE_CORRECTION_NF36.md).

## Result

NF36 certifies the complete original response of one fixed mixed-source
high correction in each parity. Both corrected joined floor families
fail for **every real scalar strength**. This is a uniform obstruction
to these two fixed rank-one families, not a negative original-form result.
The prior four retained directions with all original F remain certified;
NF36 adds no retained direction to that joint restriction.

Let nu(tau) denote the condensed floor margin after eliminating the
unchanged positive leading pair. Exact rational certificates give:

| Certified quantity | Even | Odd |
| --- | --- | --- |
| Upper bound on nu(tau), all real tau | < -9.8539e-23 | < -7.5211e-21 |
| Selected rational peak candidate, approximate display | 0.5141452343694218 | 0.05248448063673713 |
| Margin at that exact candidate | (-1.13609e-22, -1.08947e-22) | (-7.58595e-21, -7.56304e-21) |
| Floor determinant at that candidate | (-8.21852e-95, -8.10589e-95) | (-4.51578e-86, -4.50650e-86) |
| Original native energy determinant at that candidate | (1.60725e-92, 1.60733e-92) | (2.26406e-82, 2.26407e-82) |

All displayed intervals strictly enclose the rational endpoints. Peak
decimals are diagnostic displays; the certificates store the exact
denominator-10^50 scalars. All seven frozen candidates and the additional
peak candidate have positive native energy matrices and negative joined
floor margins in both parities. The selected candidate packets also
retain exact rational mixed witnesses with negative floor value and
strictly positive original native energy.

## Targeting the certified mixed obstruction

NF35 completed the signed three-direction source Gram in each parity.
Every diagonal score and the native energy matrix were positive, but the
joined floor matrix was indefinite. Its exact rational mixed witnesses
f=(f0,f1,1) supply the targets W=f0 v+f1 t+u34. The fixed sources of W
are reconstructed after merging all overlapping Legendre coefficients
exactly. No eigenvector or true inverse-response identity is assumed.

The shell includes every same-parity high mode from e112 through e180
even and e113 through e179 odd. Its source-square fraction lies in
(0.0429681,0.0435770) even and (0.4218116,0.4218240) odd, with physical
source-error payment. Dividing the midpoint source coordinates by four
and rounding downward to denominator 10^100 freezes a polynomial z.
Selection does not establish any matrix sign.

The joined rank-one map is (v,t,u34-tau z). It uses the coordinate
functional ell(c)=c2, which takes value one on the mixed target f.
Thus the correction changes the full joined family using the mixed
source; it does not optimize the old u34 diagonal separately. All three
retained components (x,w,u32) remain exactly the same. This checkpoint
tests the joined three-direction family, not an entire newly modified
54-column remaining graph.

## Complete original correction response

The original source of the small polynomial z supplies all signed native
couplings beta_i=Q(M35_i,z) and qz=Q(z,z). A reusable exact monomial
functional encloses the normalized Legendre source coordinates. The
native bilinear error is the correction source error multiplied by the
other physical vector's norm upper bound. Reverse old-source pairings
agree after the same physical payment. Unit-mass approximation errors
are not used to establish tiny native energies directly.

Projecting the correction source onto F gives three new complete signed
covariances zeta_i and its complete square gamma_z. The residual error
eta_z pays the uniform source replacement and the retained midpoint
ball; projection contraction pays the source error once. Every cross
payment includes both physical source errors, using reconstructed norm
upper bounds from the inherited true diagonals plus their reconstruction
errors. The correction square pays
2 eta_z sqrt(s_upper)+eta_z^2.

All original archimedean, prime and pole terms and their crosses are
included. The exact endpoint logarithms, regular kernel N320, degree40
pole approximation and paid tail, thirteen original translation cells,
and outward polynomial/log/log-square moments at 500 decimal digits
remain unchanged. There is no quadrature or source-sampling proof input.

The complete corrected matrices use bilinear expansion. Their leading
pair blocks are preserved exactly. For i=0,1,

\[
Q_{\tau,i2}=Q_{35,i2}-\tau\beta_i,\qquad
\Gamma_{\tau,i2}=\Gamma_{35,i2}-\tau\zeta_i,
\]

and

\[
Q_{\tau,22}=Q_{35,22}-2\tau\beta_2+\tau^2q_z,
\qquad
\Gamma_{\tau,22}=\Gamma_{35,22}-2\tau\zeta_2+\tau^2\gamma_z.
\]

Every entry retains its physical error enclosure before testing
U_tau=Q_tau-Gamma_tau/kappa, kappa=207/1000. Native positivity is a
separate matrix test.

## A rigorous scalar-family test

The rational strengths {1/4,1/2,3/4,1,5/4,3/2,2} are fixed in the
selection files before the response proof. Since the leading pair A is
unchanged, its elimination gives the exact real quadratic

\[
\nu(\tau)=\nu_0-2\alpha\tau+\delta\tau^2.
\]

The paid response moments enclose nu0, alpha and delta. If delta has
strictly negative upper endpoint, its midpoint peak selects one further
rational tau, rounded downward to denominator 10^50, before that
candidate is tested. Its sign uses the complete outward three-by-three
matrix, not a midpoint maximum.

The rational upper bound

\[
\nu_{0,\rm upper}+
\frac{|\alpha|_{\rm upper}^2}{-\delta_{\rm upper}}
\]

bounds the true condensed margin for every real tau. A negative upper
bound rejects the entire scalar family using this fixed z, not all
possible high corrections or sharper inverse estimates.

## Validation and reproduction

The independent arithmetic validator passes both parity packets. It
replays the exact mixed-target merge, rational selection, source-error
payments, native response pairings, complete source-square and cross
payments, every candidate matrix and the all-real-scalar upper bound.
It checks the condensed quadratic against direct elimination and a
separately ordered LDL calculation, and verifies the selected rational
negative floor witnesses against positive original native energies.

Controls include six exact positive/null/negative mixed-crossing cases
at two scales, three positive full-physical-mass shifts with exact ground
levels, and three concave scalar families whose exact peak crosses zero.
These are matrix controls, not claimed Weil counterexamples. Validation
records four jointly certified retained directions with all F, and no
six-direction certificate.

The original native archives, inherited NF24–NF34 inputs, both NF35
source Grams and their validator packet are hash authenticated. The
fixed correction files retain exact mixed coefficients, merged polynomial
coefficients, selected source coordinates, paid shell fractions and
frozen scalar candidates. Certificates retain all native and complete
source responses, every candidate sign, the quadratic and the complete
selected matrix. With those original inputs staged, run for each parity
(PARITY lowercase, TAG uppercase):

```sh
python3 scripts/certify_native_collective_correction_nf36_106.py choose --parity PARITY --output notes/data/RPB108_NF36_TAG_FIXED_COLLECTIVE_CORRECTION_20261009.json
python3 scripts/certify_native_collective_correction_nf36_106.py certify --trial notes/data/RPB108_NF36_TAG_FIXED_COLLECTIVE_CORRECTION_20261009.json --output notes/data/RPB108_NF36_TAG_COLLECTIVE_CORRECTION_CERTIFICATE_20261009.json
python3 scripts/validate_native_collective_correction_nf36_106.py --output notes/data/RPB108_NF36_COLLECTIVE_CORRECTION_VALIDATION_20261009.json
```

## Next frontier and preserved boundary

NF37 must change the correction direction or use a correction with more
than one independent high component. Retuning the scalar of either NF36
polynomial cannot pass this floor criterion. The signed response moments
and uniform family obstruction supply a certified baseline for testing
a broader shell or a correction of multiple joined columns. A stronger
actual inverse-response bound is also a distinct open route; the scalar
floor obstruction does not rule it out.

The complete remaining shared-frame Gram, its full mixed covariance,
the full retained infinite-high sign and whole aperture 53/50 remain
open. The prior four-direction and separate two-direction restrictions
with all original F remain valid. Highest internally certified whole-domain
aperture stays 21/20=1.05. RH, F4 and Lean are unclaimed. Historical
wording and paused branches remain unchanged.
