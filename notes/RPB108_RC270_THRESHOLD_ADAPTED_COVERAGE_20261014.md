# RPB108 — RC270: threshold-adapted canonical coverage

Parent RC269: `cbdb78b41af82ae8c06240286fea4d8918f58d44`.
Branch: `research/rpb108-route-consolidation`. Aperture B=11/10.

RC270 rebalances the original concentration inequality for two separate spectral
thresholds. It certifies **10 <= N_AQ(0.01) <= 608** and an original **nonpositive
spectral dimension at most 582**, including the kernel. These improve RC269's
609 ceilings. Neither result establishes positivity of the coupled exceptional
operator. Stage I, RH, F4 and Lean remain open.

| Requested threshold | Even rank | Odd rank | Total rank | Common original complement floor, approximately |
|---|---:|---:|---:|---:|
| Eigenvalues strictly below 0.01 | 236 | 372 | 608 | 0.01048954990635 |
| Eigenvalues at or below zero | 227 | 355 | 582 | 0.000198863505816 |

The two rows use different canonical moment spaces and different comparison
cutoffs. The 582 ceiling is not a bound on the number of eigenvalues below 0.01.
The reference floors, cutoffs and exact Fourier comparison kernels introduced here
do not alter the actual chosen rank-639 rational augmentation, its bandwidths or
its coefficient. All earlier action and positive-pivot certificates are preserved.

## Rebalancing the complete original form estimate

RC112 supplies the physical negative nonarchimedean allowance k separately on each
parity and the original archimedean envelopes

\[
 a_{arch}(\xi)\ge-31/5,\qquad
 a_{arch}(\xi)\ge\log|\xi|-1/|\xi|
 \quad(\pi|\xi|\ge1/4).
\]

The signed pole parity identity and the entire prime-operator bound remain those
of RC112. The new calculation changes only the concentration parameters. For
rational L>0, let T=exp L and choose certified T_lo<T<T_hi with T_lo>60. For
0<gamma<1 and |xi|>=T,

\[
 a_{arch}(\xi)-k-\gamma\log(e+|\xi|)
 \ge (1-\gamma)\log|\xi|-k-(1+3\gamma)/|\xi|.
\]

The right side increases with |xi|. Thus a sufficient high-frequency condition is

\[
 R=(1-\gamma)L-k-(1+3\gamma)/T_{lo}>0.
\]

Solving this scalar condition gives the admissible ceiling

\[
 \gamma_* = \frac{L-k-1/T_{lo}}{L+3/T_{lo}}.
\]

The validator chooses gamma=down_60(gamma_*)-10^-10 and checks R>0 exactly. It does
not assume the new gamma is one of the earlier fixed reference floors. In the low
band, log(e+|xi|)<L+1 for |xi|<=T. Consequently, with the upward-rounded penalty

\[
 p\ge31/5+k+\gamma(L+1),
\]

the complete original canonical form satisfies

\[
 \langle h,A_Qh\rangle_c
 \ge\gamma\|h\|_c^2-p\|J_T h\|_2^2
 \ge\gamma\|h\|_c^2-p\|J_U h\|_2^2,
 \qquad U=T_{hi}.
\]

The second inequality uses U>=T and p>0. The allowances are physical before
Fourier integration; no physical/canonical norm substitution is made inside the
multiplier. As in RC112, the estimate extends from the smooth supported core to
the full canonical carrier by form continuity. No new prime or special-function
estimate is asserted.

## Exact accepted parameter choices

| Threshold | Parity | L | First omitted matching degree m | Selected radius | Reference gamma, approximately |
|---|---|---:|---:|---:|---:|
| 0.01 | Even | 2083/500 | 472 | 36/25 | 0.0112372728363 |
| 0.01 | Odd | 1159/250 | 745 | 137/100 | 0.0111166871085 |
| 0 | Even | 2063/500 | 454 | 36/25 | 0.00160604556096 |
| 0 | Odd | 1147/250 | 711 | 69/50 | 0.000732606737192 |

The paired complement floors are approximately 0.01048954990635 and
0.01058760358317 for threshold 0.01; 0.000780616556651 and 0.000198863505816 for
threshold zero. All acceptance decisions use exact fractions recorded in the JSON.
Floating-point exploration proposed these four (L,m) pairs; it is not used in the
validator, nor claimed to prove optimality or minimal feature counts.

For each pair, canonical W is the span of the actual canonical Riesz representatives
of the physical Chebyshev moments with matching degrees j<m. The even retained
degrees end at 470 or 452; the odd retained degrees end at 743 or 709. Distinct
polynomial functionals are independent, so these ranks are exact. Orthogonality in
the canonical metric to W annihilates the retained moments exactly. No approximate
Riesz vectors or unverified head Gram matrices enter this statement.

Use RC266–269's exact comparison-kernel contour argument, with b=(r-r^-1)/2:

\[
 \|J_U-X_m\|^2\le\delta^2,
 \qquad
 \delta^2\le
 \frac{4}{\pi_+ b(1-r^{-2})^2}
 \exp[-2(m\log r-2\pi_+BUb)].
\]

This is obtained by integrating the squared matching-parity Chebyshev tail over
the physical interval and frequency band. The same pi_upper defines both the
pointwise exponential envelope and its integral. The negative-one term in that
integral is dropped upward. The physical Hilbert–Schmidt bound is also a canonical
operator-norm bound since canonical-to-physical inclusion has norm at most one.
On W-perp, X_m h=0 exactly; hence

\[
 \langle h,A_Qh\rangle_c
 \ge\beta\|h\|_c^2,\qquad \beta=\gamma-p\delta^2.
\]

The validator checks beta>0.01 for the first pair and beta>0 for the second. It
searches only rational radii k/100, k=120,...,180, choosing the smallest certified
tail among admissible candidates. Skipped radii are recorded because their twice-gap
lies outside the exponential helper's proved domain (0,100). This proves a
sufficient certificate, with no claim that skipped or untested choices fail.

Cutoff exponentials are enclosed by computing exp(-L) with the same outward
rational exponential helper and inverting its positive interval. Logs of radii
use the inherited rational atanh expansion. Every cutoff, penalty, reserve, contour
tail, complement floor and threshold margin is enclosed in exact arithmetic.

## What the smaller spaces prove

The threshold-0.01 spaces have dimensions 236+372=608. Min-max bounds the original
strict-below-0.01 count by 608; the inherited five lower-count directions per parity
remain valid. The common shifted complement gap is now greater than
0.00048954990635, compared with RC269's approximately 0.00001193957912. This is a
larger certified separation at a slightly smaller head, not a computation of its
eigenvalues or inverse responses.

The threshold-zero spaces have dimensions 227+355=582. Their complement is strictly
positive, so the entire nonpositive spectral subspace, including zero eigenvectors,
has dimension at most 582. The spaces are nested inside the corresponding
threshold-0.01 spaces and inside RC269's W609. They need not be invariant spectral
spaces. No actual negative direction is produced.

Inside the inherited H1250, these yield strong compression dimensions 642 at
threshold 0.01 (389 even, 253 odd) and 668 at threshold zero (398 even, 270 odd).
Keeping E=H1250-perp and its old positive block D, minimization over E transfers
the original complement floor to the corresponding strong compression of
F=A_H-B D^-1 B*. At threshold 0.01, use the shifted effective operator with D-0.01
and subtract 0.01 from the floor. These are compression inequalities; original and
effective spectra are not identified.

One may instead eliminate each new W-perp directly. This gives a 608-source or
582-source canonical Schur operator and different complement inverse requirements.
The old inverse action degrees and residual budgets do not transfer automatically.
RC268's two positive pivots belong to its separate rank-639 signed reduction;
that remaining problem stays dimension 637. Subtracting those two pivots from
582 or 608 is not justified by this checkpoint.

The unresolved positivity obligation is still the full coupled Schur form:

\[
 F_W-F_{WS}F_S^{-1}F_{SW}\succ0.
\]

Its head metric, responses and cross terms are not evaluated here. The positive
complement is a rigorous dimension reduction, not Stage I closure. The separate
eight-source canonical inverse width 485647/1000000 remains unchanged.

## Reproduction

```bash
python scripts/validate_rpb108_rc270_threshold_adapted_coverage.py \
  --output certificates/rpb108_rc270_threshold_adapted_coverage.json
python scripts/validate_rpb108_rc270_threshold_adapted_coverage.py \
  --output certificates/rpb108_rc270_threshold_adapted_coverage.json --replay
```

The validator checks all 245 inherited note, certificate and helper Git blob pins.
Replay reverses pin and radius traversal, uses 440 exponential terms and 140-digit
internal arithmetic instead of 400 terms and 120 digits, and compares the complete
certificate exactly. The supplied analytic proof is not a Lean formalization.
Next: use the 582-source reduction for unshifted positivity or the 608-source
reduction for the 0.01 census, paying all head-metric, inverse and cross-term errors.
