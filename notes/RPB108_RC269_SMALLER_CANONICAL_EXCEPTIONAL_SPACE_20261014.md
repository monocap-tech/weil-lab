# RPB108 — RC269: canonical exceptional coverage reduced to 609

Parent RC268: `e6ad8ec50be23a3d7beab1922f6b15ad80744c78`.
Branch: `research/rpb108-route-consolidation`. Aperture B=11/10.

RC269 certifies an explicit canonical moment space W of dimension 609 on whose
canonical orthogonal complement the complete original Weil form has a floor
strictly greater than 0.01. Thus the inherited original eigenvalue census improves
to **10 <= N_AQ(0.01) <= 609**, counting eigenvalues strictly below 0.01 with
multiplicity. The nonpositive spectral dimension, including nullity, is at most
609, improving RC268's 637 ceiling. Positivity of the remaining coupled block is
open. There is no Stage I, RH, F4 or Lean closure.

| Exact comparison | Even | Odd |
|---|---:|---:|
| First omitted matching Chebyshev degree m | 474 | 745 |
| Retained degrees | 0,2,...,472 | 1,3,...,743 |
| Canonical moment rank | 237 | 372 |
| Selected rational ellipse radius | 147/100 | 139/100 |
| Fourier tail squared upper, approximately | 2.902994e-6 | 7.513757e-6 |
| Original canonical complement floor, approximately | 0.0100119395791 | 0.0101766093641 |
| Strong dimensions inside inherited parity head 625 | 388 | 253 |

The JSON contains exact fractions; displayed decimals are explanatory only.
The chosen rational augmentation remains rank 639 with its existing kernel and
coefficient. The new smaller space uses an exact Fourier comparison kernel, not a
replacement of that augmentation. The two positive signed pivots from RC267–268
remain valid, and the old signed Schur problem remains dimension 637. They cannot
be subtracted from this independent 609-dimensional canonical reduction without
a further proof about the new effective operator.

## Original form and exact moment annihilation

Use RC112's complete original form inequality separately on each parity:

\[
 \langle h,A_Qh\rangle_c
 \ge \gamma_p\|h\|_c^2-p_p\|J_{T_p}h\|_2^2.
\]

All original archimedean, signed-pole and prime allowances are inherited from that
proof. The validator checks the same gamma and p against RC256 and checks that its
rational U is exactly RC112's certified upper endpoint for T. Consequently the
same inequality holds with J_U on the right, since U>=T and p>0. No new arithmetic
operator integrals or approximate original actions enter this step.

Let X_m be the exact Fourier kernel's Chebyshev expansion retaining degrees j<m.
Only degrees of the carrier parity contribute to its action. Define W_p using the
actual canonical Riesz representatives of the physical Chebyshev moment
functionals for those matching degrees. Distinct polynomial functionals are
independent on the smooth supported core, and hence have independent Riesz
representatives. Their parity follows from the reflection-invariant canonical
metric. This proves ranks 237 and 372; it is not a numerical conditioning claim.

For h canonically orthogonal to W_p, all retained physical moments vanish exactly,
so X_m h=0. These are canonical Riesz representatives, not physical Legendre
polynomials treated as canonical representatives. The span equals the corresponding
polynomial-moment span by the triangular Chebyshev change of basis. No moment
projection, approximate Riesz-vector or finite Taylor-kernel error is introduced.

## Integrated contour bound

For rational r>1 put b=(r-r^-1)/2. On the Laurent ellipse
t=(w+w^-1)/2, |w|=r, the exact Fourier kernel has modulus at most
exp(2*pi_upper*B*b*|xi|). Its Chebyshev coefficient of degree j is bounded by
2*r^-j times this envelope. Since m has the carrier parity, the matching tail obeys

\[
 |K_{tail}(x,\xi)|\le
 \frac{2r^{-m}}{1-r^{-2}}\exp(2\pi_+Bb|\xi|).
\]

For the parity carrier, the opposite kernel parity integrates to zero. Integrating
the squared matching kernel over x in [-B,B] and xi in [-U,U] gives

\[
 \|J_U-X_m\|_{HS}^2
 \le \frac{4}{\pi_+ b(1-r^{-2})^2}
       \exp[-2(m\log r-2\pi_+BUb)].
\]

Here the negative-one term in the frequency integral is discarded upward. The
same pi_upper is used in the exponential envelope and its integral; the denominator
is not independently substituted into an expression using exact pi. This is the
RC266 integrated contour argument applied to a new exact comparison length.
The canonical-to-physical inclusion has norm at most one, so this also bounds the
squared operator norm on the canonical carrier. On W_p-perp it therefore bounds
the squared norm of J_U itself.

The validator encloses log r by the inherited positive atanh series and computes
the exponential with outward rational arithmetic. For each fixed m it checks the
finite radius grid k/100, k=120,...,180. Candidates outside the exponential helper's
proved domain 0<2*gap<100 are recorded and skipped (none even; nine odd). The
smallest certified upper bound among admissible candidates is selected with a
deterministic rational tie break. This is not a claim of optimal radius over all
real numbers, minimal m, or minimal possible exceptional dimension.

Writing the selected squared tail upper as delta_p^2 gives

\[
 \langle h,A_Qh\rangle_c\ge
 \beta_p\|h\|_c^2,\qquad
 \beta_p=\gamma_p-p_p\delta_p^2>1/100,
 \quad h\perp_c W_p.
\]

The JSON records downward-rounded beta and beta-1/100. Min-max then bounds the
strict below-0.01 spectral dimension by codim(W_p-perp)=dim W_p. In particular the
nonpositive spectral dimension, including the kernel, has the same upper bound.
RC112's five lower-count directions per parity are preserved. The space W need
not be invariant, and this argument does not identify the low eigenvectors.

## Effective strong compression and remaining obligation

The new W lies inside RC112's W639 and hence inside the inherited H1250. Set
S=H1250 orthogonal minus W in the canonical metric. Its dimension is now
1250-609=641, with parity dimensions 388 and 253. Keep the old infinite complement
E=H1250-perp and its positive block D and certified inverse machinery. For the
original effective operator F=A_H-B D^-1 B*, minimizing the original form over E
shows

\[
 P_S F P_S\succeq\beta P_S,\qquad \beta=\min_p\beta_p.
\]

For the shifted effective operator at t=0.01, the corresponding compression has
floor beta-t>0, by minimizing the shifted form with D-t. These are compression
bounds, not assertions that original and effective eigenvalues coincide.

On W plus S the exact remaining positivity condition is the coupled Schur form
F_W-F_WS F_S^-1 F_SW>0. Alternatively one can eliminate W-perp directly, obtaining
a different 609-dimensional canonical effective operator with complement floor
beta. Its head metric, complement inverse responses and cross terms have not been
computed here. Old inverse degrees, tolerances and action budgets do not
automatically transfer to this larger infinite complement. A strong complement
and positive finite compressions alone cannot certify coupled positivity; an exact
two-by-two control in the validator illustrates this limitation.

## Reproduction and preservation

```bash
python scripts/validate_rpb108_rc269_smaller_canonical_exceptional_space.py \
  --output certificates/rpb108_rc269_smaller_canonical_exceptional_space.json
python scripts/validate_rpb108_rc269_smaller_canonical_exceptional_space.py \
  --output certificates/rpb108_rc269_smaller_canonical_exceptional_space.json --replay
```

All 242 inherited note, certificate and helper Git blob pins are checked. Replay
reverses dependency and radius traversal and uses 440 exponential terms with a
140-digit internal grid in place of 400 terms and 120 digits, then compares the
complete certificate exactly. The result is an exact-arithmetic certificate with
the analytic proof supplied here, not a Lean formalization. No earlier file, actual
augmentation, response source or existing positive-pivot certificate is changed.

Next: use the enlarged 641-dimensional strong compression or construct the new
609-source canonical Schur responses, retaining all metric, inverse, cross-term
and residual error payments.
