# RPB108 — NF38: an independent second high direction and the joint functional test

2026-10-09 UTC. Phase Geometry parent NF37 is
`4368a1763f3d899281704347ebfebcd4c9779b27`. Coupled CC79 is read only
at `dd93e5cc7d003d44cdc240c5710f4c253dc1346f`. No other or paused branch
is modified. Definitions precede use in the additive
[NF38 terminology entry](../docs/TERMINOLOGY_RPB108_SECOND_HIGH_DIRECTION_NF38.md).

## Result

NF38 certifies the complete original response of a second, exactly
independent high direction in each parity, including the signed
covariance between the two high sources. It then allows **both high
functionals to vary jointly over every real two-by-three correction
matrix**. Neither parity passes the scalar-floor criterion: fixed
rational witnesses remain negative for that entire two-direction family.

| Certified quantity | Even | Odd |
| --- | --- | --- |
| Universal fixed-witness upper bound, all joint functionals | < -9.6002e-23 | < -1.6564e-21 |
| Joint ceiling condensed margin | (-1.00136e-22, -9.57466e-23) | (-1.66790e-21, -1.65628e-21) |
| Margin of the selected rational joint map | (-1.00136e-22, -9.57470e-23) | (-1.66790e-21, -1.65628e-21) |
| Determinant of the negative correction floor block H | (3.01368e-45, 3.01369e-45) | (2.11664e-38, 2.11665e-38) |
| Signed old–new projected source covariance | (-7.67716e-24, -7.67715e-24) | (-4.21863e-21, -4.21862e-21) |
| Selected negative witness's original native energy | (3.89440e-21, 3.89469e-21) | (9.32503e-19, 9.32505e-19) |

All displayed intervals strictly enclose the rational endpoints. The
selected native energy matrix and all selected floor diagonals are
positive in both parities, while the complete joined floor determinants
and mixed witnesses are negative. The rejection is a failure of this
named floor-certificate family, not a negative original Weil form.

The second direction improves the odd ceiling margin substantially,
from NF37's roughly -7.57e-21 to roughly -1.66e-21, but does not cross
zero. The even ceiling also improves and remains negative. Four
retained directions with all original F remain jointly certified;
NF38 adds no retained direction to that restriction.

## Exact selection of an independent direction

NF37 froze a rational family B=M35-z0 lambda0^T in each parity and
certified a rational negative witness h that survives every functional
along z0. NF38 constructs the complete original source of W=B h,
merging all overlapping Legendre coefficients exactly.

On the original high shell e112,e114,...,e180 even and
e113,e115,...,e179 odd, the reconstructed source coordinates are divided
by four and rounded downward at denominator 10^100. If r is that
rational polynomial, NF38 freezes

\[
z_1=r-\frac{\langle z_0,r\rangle}{\|z_0\|_2^2}z_0.
\]

Exact rational arithmetic certifies <z0,z1>=0 and ||z1||^2>0 in each
parity. The physical two-direction Gram has strictly positive determinant,
so this is a new direction rather than another functional along z0.
The retained components (x,w,u32) remain unchanged.

The source-shell square orthogonal to z0, with physical source-error
payment, is between 0.0018739 and 0.0020695 of the moved target's
complete projected source square even, and between 0.0121438 and
0.0121498 odd. Selection and these fractions do not prove a matrix sign.
Physical orthogonality does not imply source orthogonality.

## Complete original signed response

The producer reconstructs the three complete original sources of B and
the source of z1. The frozen old correction is included in every B
column. The native crosses beta1 and diagonal q1 use the correction's
original source coordinates, with physical norm error payments and
reverse pairing checks. The projected complete source crosses zeta1
and diagonal gamma1 retain both source errors and the retained midpoint
ball. The source square pays 2 eta1 sqrt(s_upper)+eta1^2.

The producer also reconstructs the old correction's source to certify
the signed native cross q01 and complete projected source covariance
gamma01 with z1. Their physical payments include both correction
errors. No source cross is discarded because the polynomials are
physically orthogonal.

The endpoint logarithms, rational regular kernel N320, degree40 pole
approximation and paid tail, original thirteen translation cells, and
outward polynomial/log/log-square moments at 500 decimal digits are
unchanged. Every archimedean, prime and pole source contribution and
their signed cross terms are included. There is no sampling or
quadrature sign proof.

## All two-direction correction functionals

Let Z=(z0,z1), and let C be any real two-by-three matrix. NF38 tests

\[
B_C=B-ZC.
\]

Both high functionals vary jointly. Since B already includes the frozen
old functional, a change of C can cancel it; this family includes the
original NF35 family and all NF36/NF37 functionals along z0.

The complete native and source responses supply Q_Z, Gamma_Z and
the joined cross matrices BQ=Q(B,Z), BG=Gamma(B,Z). The old column's
crosses follow by exact bilinear expansion of NF36's paid responses
through the frozen lambda0. The newly integrated crosses supply the
second column. Define

\[
U_B=Q_B-\Gamma_B/\kappa,\quad
E=BQ-BG/\kappa,\quad H=Q_Z-\Gamma_Z/\kappa,
\qquad\kappa=207/1000.
\]

The full floor matrix is

\[
U_C=U_B-EC-C^TE^T+C^THC.
\]

Negative definiteness of the true H is tested through its first diagonal
and determinant using outward rational endpoints. Its adjugate formula
then encloses every entry of H^-1. Completion of squares gives

\[
V=U_B-EH^{-1}E^T,\qquad
U_C=V+(C-H^{-1}E^T)^TH(C-H^{-1}E^T)\preceq V.
\]

This ceiling applies to every real C in the two fixed directions. The
midpoint entries of H^-1 E^T select a rational C, rounded downward at
denominator 10^100. Its full native energy and complete source Gram
are updated separately before checking the complete joined sign.
The selection midpoint is not a sign certificate.

If the ceiling remains indefinite, a new rational h is frozen and
checked against the outward ceiling. With a=h^T U_B h, b=E^T h and
x=C h, its floor value obeys

\[
h^T U_C h=a-2b^Tx+x^THx
\le a-b^TH^{-1}b.
\]

A strictly negative outward upper endpoint of this last expression
rejects every real two-by-three C. The witness calculation is independent
of the interval arithmetic order used to eliminate the ceiling's
leading pair and does not assume independence of the uncertain source
entries. An intermediate certificate also tests the second functional
with the old one frozen; its scope is narrower than the joint test.

## Validation and reproducibility

The independent validator passes both parity certificates. It checks
the exact target merge, rational rounding and orthogonalization,
positive two-direction physical Gram, inherited NF37 matrix packets,
retained projection errors, native pairings and reverse checks, all
complete source-square/cross payments, and the old–new covariance.
It reconstructs the negative correction block and its inverse, the
joint ceiling, selected native/source matrices and the universal
witness upper bound. Separate LDL and symmetric-sum calculations
check the ceiling and selected signs through different arithmetic
orders.

Six new joint controls use a negative definite high block with a
nonzero signed cross, positive native energy and positive original
floor diagonals. The exact joint ceiling crosses positive/null/negative
at two scales; the optimal map attains it, and the null case has an
exact kernel. The validator also replays six one-direction controls
and three full-physical-mass shifts with exact positive ground levels.
These are genuine matrix controls, not actual Weil counterexamples.
Validation records four jointly certified retained directions with all
F and no six-direction certificate.

The original native archives and inherited source packets are hash
authenticated. The fixed selection files store the exact merged target,
both polynomials, orthogonalization coefficient, positive second mass,
paid shell coordinates and fractions. Response certificates store the
five new complete source products, native pairings, error payments,
joint high block and inverse, all joined crosses, complete ceiling,
rational selected map and full candidate sign.

With those original inputs staged, run for each parity
(PARITY lowercase, TAG uppercase):

```sh
python3 scripts/certify_native_second_high_direction_nf38_106.py choose --parity PARITY --output notes/data/RPB108_NF38_TAG_FIXED_SECOND_HIGH_DIRECTION_20261009.json
python3 scripts/certify_native_second_high_direction_nf38_106.py certify --trial notes/data/RPB108_NF38_TAG_FIXED_SECOND_HIGH_DIRECTION_20261009.json --output notes/data/RPB108_NF38_TAG_SECOND_HIGH_DIRECTION_CERTIFICATE_20261009.json
python3 scripts/validate_native_second_high_direction_nf38_106.py --output notes/data/RPB108_NF38_SECOND_HIGH_DIRECTION_VALIDATION_20261009.json
```

## Next frontier and preserved boundary

NF39 must enlarge or change the high correction span, or improve the
actual inverse-response estimate. Retuning either functional, including
both jointly, cannot pass this scalar-floor criterion inside the two
fixed directions. The joint universal witnesses identify the remaining
retained combinations for a further independent direction. The odd
margin improvement supplies a quantitative baseline, but does not
establish that another direction will suffice or that the entire shell
can pass.

NF38 does not certify an entire modified 54-column remaining graph.
The full remaining shared source Gram, its collective mixed covariance,
the full retained infinite-high sign, and whole-domain positivity at
53/50=1.06 remain open. The prior four-direction and separate
two-direction restrictions with all original F remain valid. Highest
internally certified whole-domain aperture stays 21/20=1.05. RH, F4,
full transport and Lean closure are unclaimed. Historical wording and
paused branches remain unchanged.
