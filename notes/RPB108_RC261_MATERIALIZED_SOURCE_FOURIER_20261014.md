# RC261 — degree-512 physical source and stable Fourier energy

Parent: `fdb624ba35037b8eb74347d0b86fffe0929080d6` (RC260).
Branch: `research/rpb108-route-consolidation`.

RC261 assembles the complete retained physical residual polynomial through
degree 512 and evaluates its outside-band Fourier energy with every mode
cross term. A stable diagonal-integral recurrence and RC259's off-diagonal
boundary identity replace the high-order inverse-power expansion for this
larger polynomial. The source and trial vectors, fixed Z, and actual rational
augmentation remain unchanged. Neither signed gap nor Stage I is closed.

| Certified upper bound | RC260 even | RC261 even | RC260 odd | RC261 odd |
| --- | ---: | ---: | ---: | ---: |
| Actual full-source outside Fourier energy | 0.008968308 | 0.007689894 | 0.010564676 | 0.007229871 |
| Actual original-action inverse response | 0.239383795 | 0.208890536 | 0.282920050 | 0.206396443 |

Display bounds are rounded outward. Exact rational enclosures are in the
certificate. Updated signed-gap lower bounds are approximately -0.120332
even and -0.109314 odd. The original source forms remain approximately
0.088559 and 0.097083; these are not tests against 0.5. The full signed
rank-639 response remains a separate unevaluated obligation.

## Complete physical source through 512

The actual physical source is g_e = D e = G0 Pbase - G Z, with
e = N0 Pbase - N Z and G = D N. N is the chosen positive augmented operator;
N0 is the original Weil operator. The canonical metric M = D^-1 L is separate.
The physical Legendre diagonal D is H_n+s, with harmonic H_n.

For degrees 0 through 256, use exactly RC257's polynomial coefficients
(H_n+s_mid)*e_center,n from the pinned RC251 residual and RC256 midpoint.
For degrees 257 through 512, use RC259's directly materialized physical
endpoint/prime/negative-augmentation centers. These are output coefficients,
not additional response trials. Their radii give a physical uncertainty
bound sum mass(n)*radius_n^2, added orthogonally to the inherited low block's
finite-coefficient and actual-s uncertainty.

The resulting retained uncertainty is below 2.511e-42 even and 2.737e-42
odd. RC260's complete model physical source bound beyond 512 supplies the
omitted block R. Its analytic infinite band tail remains fully paid; the
compressed-band projection defect is not reintroduced as an output error.
All original regular-kernel, prime-arithmetic, pole-Taylor and actual
rational-augmentation model faults remain paid globally after the model.

## Stable full Fourier Gram

Let j_n be a spherical Bessel function, z=2 pi B U, and define

    J_n(z) = integral_z^infinity j_n(t)^2 dt,
    W_nd(z) = j_n'(z)j_d(z)-j_n(z)j_d'(z).

For n != d of matching parity, RC259's boundary identity gives

    integral_z^infinity j_n(t)j_d(t) dt
      = -z^2 W_nd(z)/(n(n+1)-d(d+1)).

All pairs of distinct matching-parity retained degrees are evaluated. Their
coefficients include the Fourier parity signs and both symmetric cross
terms. The n(n+1) values belong to this Sturm--Liouville identity and are not
substituted for the harmonic D diagonal.

For diagonal terms, the spherical recurrences give

    d/dz [z*(j_n(z)^2+j_(n+1)(z)^2)]
      = (2n+1)*j_n(z)^2-(2n+3)*j_(n+1)(z)^2.

The boundary quantity tends to zero at infinity. Integration therefore gives
the positive recurrence

    (2n+3)*J_(n+1)(z)
      = (2n+1)*J_n(z)+z*(j_n(z)^2+j_(n+1)(z)^2).

No high-degree asymptotic expansion or unstable independent inverse-power
moments are used in these diagonal steps. The base is

    J_0(z) = 1/(2z) - Re(I_2(z))/2,
    I_2(z) = integral_z^infinity exp(2it)t^-2 dt.

One exact integration-by-parts enclosure for I_2 uses 500 terms in generation,
520 in replay. Its real and imaginary remainders are paid separately. The
phase exp(2iz) is enclosed using double-angle identities from the already
certified endpoint sine and cosine. Exact rational controls check the
diagonal derivative identity at six indices, including 512.

Initial endpoint values and derivatives come from RC260's high-precision
interval routine through 1024. They are then rounded outward to 150 decimal
digits for this quadratic calculation, 170 in replay. The same grids are
used for diagonal integrals. All finite sums use exact rational interval
endpoints between outward operations.

For physical polynomial p = sum a_n P_n, the complete outside energy is

    4B/pi * [sum_n a_n^2 J_n
      + 2 sum_(n>d) a_n a_d (-1)^((n-d)/2)
           * integral_z^infinity j_n j_d].

The original pinned pi lower-limit and prefactor error is paid globally
using the squared sum of absolute polynomial coefficients. The degree-256
principal block is accumulated separately and must intersect RC257's
independent inverse-power Fourier enclosure. This check passes for both
parities. Final outside-energy intervals have outward 24-decimal endpoints.

The degree-512 retained outside energies are about 0.002475299 even and
0.002017610 odd. These should not be compared as improvements over RC257's
degree-256 retained energies: the polynomials differ. The comparable actual
full-source bounds are the ones in the table above, after every omitted
output and model fault has been included.

## Actual full source and inverse response

The new polynomial has exact physical energy A and Fourier interval
[Y_lower,Y_upper]. Its omitted model output above 512 is physically
orthogonal. RC258's checked condition Y_upper*(A+R)<=A^2 yields

    ||P_out(p+q_model)||^2
      <= (sqrt(Y_upper)+sqrt((1-Y_upper/A)*R))^2.

The complete retained finite uncertainty and all global physical faults are
then added in norm. The actual total source energy S and outside energy X
are intersected with RC260. A reverse-triangle lower bound also encloses the
actual outside energy: approximately 5.56979e-5 even and 6.75451e-6 odd. These
are positive lower bounds, not proofs that a sufficient closure budget is
violated. The validator checks 0 <= X_lower <= X_upper <= S.

The same 1000 rational retained-band tau candidates minimize

    <e,N^-1 e>_D <= S/I + X_upper*(1/O-1/I),  I>O>0.

Add the resulting correction to the unchanged variational center upper,
intersect the inverse enclosure with RC260, and update the signed-gap lower
using the original source form lower. All inequalities concern the same
actual rational augmented operator; the ideal band operator does not replace
it. Source and four-trial spaces are unchanged.

## Validation and remaining work

Generation and exact replay verify 218 inherited blob pins. Replay uses the
longer base integral expansion, finer interval grids and RC260's longer
endpoint Taylor construction, reverses Fourier-term, coefficient-uncertainty
and pin summation order and tau candidates, and requires exact certificate
equality. The expensive earlier source and prime calculations are reused
from pinned certificates.

From repository root:

    python scripts/validate_rpb108_rc261_materialized_source_fourier.py --output certificates/rpb108_rc261_materialized_source_fourier.json
    python scripts/validate_rpb108_rc261_materialized_source_fourier.py --output certificates/rpb108_rc261_materialized_source_fourier.json --replay

The full signed rank-639 response and original full auxiliary norm gate are
unevaluated. The separate eight-source canonical inverse width remains
485647/1000000. Stage I, RH, F4 and Lean remain open/false.

Next: control remaining original prime output beyond 512 or use the complete
retained Fourier Gram for a sharper residual inverse calculation. Positive
closure of these two source tests would still leave the full signed gate.
