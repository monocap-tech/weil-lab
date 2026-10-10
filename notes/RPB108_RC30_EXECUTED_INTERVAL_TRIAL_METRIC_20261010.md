# RPB108 RC30 — executed interval enclosure of complete physical trial metric

2026-10-10. Branch research/rpb108-route-consolidation.
Recovered parent d423f360b413109cc45b98c1c7fc4cbd7985eab7 (RC29).

## Result

The COMPLETE physical logarithmic metric on the first eight unnormalized
Legendre trial modes at B=11/10 is now enclosed. A rational symmetric
center matrix Ghat is stored with mass matrix D and certified error

    -E D <= G_true-Ghat <= E D,
    E=5082896500000003/11000000000000000000 <1/2000.

This is the physical trial metric, not the original signed Weil head,
and not the Gram matrix of canonical Riesz representatives.

## Executed construction

Run python scripts/validate_rpb108_rc30_interval_metric.py.
Executed successfully at 220 decimal digits, on all 1000 RC29 atoms.
All 20 upper-triangle same-parity entries are enclosed; the remaining
16 upper-triangle entries vanish exactly by parity.
RC29 overlap polynomials and Cauchy integral recurrence are used exactly.

The arithmetic uses directed Decimal contexts for basic operations.
Monotone exp, ln and sqrt endpoint values are rounded to nearest and
then widened by one representable neighbor on each side.
The computational assumption is Python Decimal's documented correctly
rounded exp/ln/sqrt behavior:
https://docs.python.org/3/library/decimal.html
This is numerical interval certification, not a Lean verification.

Arctangent is enclosed by the half-angle identity, repeated three times,
followed by 180 alternating-series terms and a rigorous next-term
remainder interval. For arguments greater than one the identity
atan(x)=pi/2-atan(1/x) is used first. Pi is enclosed through Machin's
identity using the same bounded series. Every operation carries its
rounding interval through the cancellation-prone moment recurrence.

The script asserts that every final mixture-entry interval has width
below 1e-30 before rounding outward to rational endpoints on the
1e-20 grid. The rational midpoint matrix of these intervals is used
as Qhat_trial. Parity zeros are exact.

For entry midpoint error epsilon_entry, the mass-normalized matrix
error is bounded by 8 epsilon_entry/min_i D_ii. Here min_i D_ii=11/75;
the resulting transport allowance is 3/11000000000000000000.
This is an operator error, not an unscaled entrywise assertion.

Add RC25's exact singular and endpoint matrices and RC26's scalar
midpoint. The final allowance is the sum of:
- RC29 whole-operator mixture error 109/500000;
- scalar half-width 488163/(2*10^9);
- interval entry transport allowance above.

The certificate includes exact rational Ghat, D, all evaluated mixture
entry intervals, and evidence flags. Approximate diagonal centers are

    2.3938091164, 0.8901121819, 0.5783122746, 0.4403786853,
    0.3614524320, 0.3098089256, 0.2731007010, 0.2454990847.

These decimal displays are not used as proof data. The canonical Fourier
weight independently gives G_true>=D. No original signed Weil
positivity follows from positivity of its supporting metric.

## Evidence boundary and next step

The complete low-mode physical metric is evaluated and enclosed.
No matrix inverse or trial Riesz coefficients have yet been computed.
The resulting polynomial trials would still require whole physical
source residual bounds from RC24; a finite solve alone does not
certify those residuals or the actual canonical inverse.

Next: solve against concrete low-mode functionals, certify the finite
solve, and compute whole-space weak residuals. The separate 8600-feature
native head/source obligations remain open. No original aperture
extension, RH/F4 theorem, or Lean closure is claimed.
