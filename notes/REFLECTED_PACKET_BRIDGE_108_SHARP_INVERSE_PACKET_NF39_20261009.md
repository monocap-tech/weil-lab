# RPB108 — NF39: sharp inverse envelope and the missing arithmetic improvement

2026-10-09 UTC. Phase Geometry parent NF38 is
`d84bc1079b44bb6d8d724945354c7334c29e6eaf`. This additive checkpoint
modifies only the Phase Geometry branch. Read definitions first in the
[NF39 terminology entry](../docs/TERMINOLOGY_RPB108_SHARP_INVERSE_PACKET_NF39.md).

## Result

NF38's joint correction ceiling is **exactly the sharp inverse envelope
obtainable from the named aggregated two-direction moment packet and
the background lower bound**. Rewriting the correction calculation as
an inverse bound does not improve it.

NF39 proves sharpness by constructing exact rational abstract Hilbert
models inside every interval of that packet. Two positive high
backgrounds preserve exactly the same native and source moments but
give opposite joined Schur signs. Their retained native energy matrices
are positive. The negative model attains NF38's ceiling; the positive
model changes the background off the two known high directions.

| Exact rational model diagnostic, approximate display | Even | Odd |
| --- | ---: | ---: |
| Last Schur LDL pivot, minimal background | -9.79276e-23 | -1.66209e-21 |
| Last Schur LDL pivot, changed background | +4.37623e-22 | +3.00106e-19 |

The decimals in this model table are approximate displays, not interval
certificates. Exact rational pivots, positive seven-vector Grams, high
operators and inverses are stored in the machine-readable certificates.
All source/native moments agree exactly between the two models and lie
inside the original paid intervals. These are **abstract realizations
of the aggregated packet**, not models of the complete original Weil
identities, endpoint functions, translation cells or polynomial
coordinates. No actual original-form negativity is established.

The independent validator passes both certificates, the inherited NF38
response replay, six genuine full-block crossing controls, and three
whole-physical-mass shifts with exact positive ground levels. Four
retained directions with all original F remain jointly certified.
The actual original inverse and the six-direction join remain open.

## The packet and the positive high-column surplus

Let A be the positive high background used by the existing Schur
reduction, A>=kappa I with kappa=207/1000. Let Z=(z0,z1) be NF38's
two exact high polynomials and r=(r0,r1,r2) the three joined physical
high sources. The aggregated packet consists of

\[
M=Z^*Z,\quad Q_Z=Z^*AZ,\quad G_Z=(AZ)^*AZ,
\]

\[
B=r^*Z,\quad S=r^*AZ,\quad G=r^*r,\quad Q=Q_B.
\]

The stars are physical high-space adjoints. The native and complete
source quantities carry NF38's original physical error payments. The
two polynomials are physically orthogonal, so M is an exact positive
diagonal rational matrix.

Put V=AZ-kappa Z and C=QZ-kappa M. NF39 certifies C>0 through outward
rational diagonal and determinant tests in both parities. For every
high form-domain vector f, positivity of A-kappa I and completion of
squares against the two Z columns gives

\[
\langle f,(A-\kappa I)f\rangle
\ge \langle V^*f,C^{-1}V^*f\rangle.
\]

Consequently

\[
A\ge A_0:=\kappa I+VC^{-1}V^*,\qquad A^{-1}\le A_0^{-1}.
\]

Moreover, V^*Z=C, so A0 Z=AZ exactly. The minorant preserves both
known high columns, not merely their energies.

## Why this is exactly NF38's ceiling

Woodbury inversion gives

\[
A_0^{-1}=\kappa^{-1}I-
\kappa^{-1}V(\kappa C+V^*V)^{-1}V^*.
\]

The required moments are already in the packet:

\[
V^*V=G_Z-2\kappa Q_Z+\kappa^2M,\quad
r^*V=S-\kappa B,
\]

\[
\kappa C+V^*V=G_Z-\kappa Q_Z=-\kappa H,
\quad E=B-S/\kappa.
\]

Thus the inverse-envelope Schur matrix is

\[
Q-r^*A_0^{-1}r
=Q-G/\kappa-EH^{-1}E^T=V_{38}.
\]

This is NF38's true joint functional ceiling. The identity holds for
the true correlated data within the outward enclosures. It does not
assume that independent midpoint choices identify the actual operator.

The mathematical argument applies to the positive high block already
used in the source/Schur reduction; it provides no global spectral
classification or whole-domain continuation theorem.

## Exact moment-preserving models

For the sharpness check, NF39 chooses rational values within every
paid native/source interval, taking a symmetric intersection midpoint
for symmetric matrices. It then forms the exact physical Gram of
seven formal vectors

\[
(z_0,z_1,V_0,V_1,r_0,r_1,r_2).
\]

Its blocks are M, C, B, V^*V, S-kappa B and G. Exact rational LDL
factorization gives seven strictly positive pivots in each parity.
This defines a finite-dimensional real Hilbert space with that Gram;
no approximate eigenvalue test or irrational coordinate selection is
needed.

In this space define A0 by the minorant above. Let P be physical
orthogonal projection off span(Z), and define

\[
A_\delta=A_0+\delta P,\qquad \delta\ge0.
\]

Both backgrounds obey A_delta>=kappa I and A_delta Z=AZ. Therefore
M, QZ, GZ, B, S, G and Q are exactly unchanged. NF39 freezes delta=0
and delta=1. It stores exact rational matrices for both operators and
their inverses, checks both inverse products equal the identity, and
computes the complete joined Schur matrices. The delta=0 matrix has
a positive leading pair and negative final pivot. The delta=1 matrix
has three positive pivots. Positivity of the full abstract joined-plus-
high block follows from its positive high background and positive Schur
matrix; the negative model has an explicit negative full-block witness.

This proves that the named aggregated moments and lower floor do not
determine the actual inverse-response sign. It does not prove that all
currently known source information, or the complete Weil identities,
cannot determine it. The original functional shapes and other native
coordinates are additional information excluded from this model test.

## The precise additional quantity needed

For the actual high background define the inverse improvement matrix

\[
T=r^*(A_0^{-1}-A^{-1})r\succeq0.
\]

The exact original joined Schur matrix is V38+T. The condition

\[
\boxed{V_{38}+T\succ0}
\]

is necessary and sufficient for this three-direction restriction with
all original high directions, given the standing positive background.
Merely knowing T>=0 is insufficient: the negative matching model has
T=0. A quantitative signed lower matrix bound on T can settle the join.

Along NF38's fixed rational universal witnesses h, positivity requires
T(h,h)>-h^T V38 h. The paid ceiling moments give the following necessary
strict lower bounds:

| Necessary actual inverse improvement on the fixed witness | Even | Odd |
| --- | ---: | ---: |
| T(h,h) | > 9.5771e-23 | > 1.6564e-21 |

These inequalities are checked against exact rational endpoints. The
witnesses have h2=1 and are not normalized physical unit vectors; these
numbers are not spectral gaps. Passing one witness threshold alone is
not sufficient for full matrix positivity. The full signed condition
V38+T>0 remains the acceptance target.

## Validation and reproduction

The validator replays NF38's exact selections, native/source payments,
high cross covariance and joined tests using authenticated original
inputs. It verifies every exact model moment against its paid interval,
positive physical Gram and surplus, projection identities, high-column
attachment, self-adjointness, exact inverse products, source/native
moment equality, and both Schur signs. It also verifies an explicit
negative full-block witness and the exact envelope/ceiling identity.

Six genuine full-block controls cross positive/null/negative at two
scales while the native retained matrix and high background stay
positive. In the null case an exact five-coordinate kernel proves
that shifts by .001, .1 and 2 times the whole physical identity have
those exact positive ground levels. The shift acts on retained and
high coordinates. These controls are not actual Weil countermodels.

With the inherited source and native inputs staged, run:

```sh
python3 scripts/certify_native_sharp_inverse_packet_nf39_106.py --parity even --output notes/data/RPB108_NF39_EVEN_SHARP_INVERSE_PACKET_CERTIFICATE_20261009.json
python3 scripts/certify_native_sharp_inverse_packet_nf39_106.py --parity odd --output notes/data/RPB108_NF39_ODD_SHARP_INVERSE_PACKET_CERTIFICATE_20261009.json
python3 scripts/validate_native_sharp_inverse_packet_nf39_106.py --output notes/data/RPB108_NF39_SHARP_INVERSE_PACKET_VALIDATION_20261009.json
```

## Next frontier and preserved boundary

NF40 must add actual arithmetic information that lowers the inverse
envelope: new high columns enlarge the known span, while a direct
inverse-improvement estimate controls T beyond that span. Repackaging
the same aggregated NF38 data or reoptimizing its correction functionals
cannot strengthen this sharp bound. The matching positive model
demonstrates that a positive inverse improvement is possible; it does
not certify it for the original Weil background.

The full residual source Gram, collective retained/infinite-high sign,
uniform all-cap response criterion and whole-domain aperture 53/50=1.06
remain open. Four retained directions with all F and the separate
two-direction restriction remain certified. Highest internally certified
whole-domain aperture stays 21/20=1.05. RH, F4, full transport and Lean
closure are unclaimed; paused branches and historical wording remain
unchanged.
