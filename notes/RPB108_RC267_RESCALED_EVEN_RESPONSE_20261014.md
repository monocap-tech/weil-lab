# RC267 — positive even-source gap from a rescaled response trial

Parent: `8b0d8a60fdb4a7d315cc249115c20fb07ee04d97` (RC266).
Branch: `research/rpb108-route-consolidation`.

RC267 certifies a positive signed gap for the current even P0-source test.
RC266's positive odd P1-source result is preserved unchanged. Both current
source tests therefore pass. The full rank-639 signed response criterion
and original full auxiliary norm gate remain unevaluated; Stage I stays open.

| Actual source bound | RC266 | RC267 |
| --- | ---: | ---: |
| Even original-action inverse upper | 0.104695285 | 0.087106566 |
| Even signed-gap lower | -0.016136089 | **+0.001452630** |
| Odd original-action inverse upper | 0.083217799 | 0.083217799 |
| Odd signed-gap lower | +0.013865017 | +0.013865017 |

Display upper/lower bounds are rounded outward. The certificate stores
exact rational enclosures. These are the same actual sources N0 P0 and
N0 P1 and the same chosen rational augmented operator. No new source is
introduced. The response space still has four trials per parity.

The selected even response polynomial changes from Z to (27/20)Z within
that same four-dimensional space. The chosen scale is one rational trial
candidate, compared with the previous valid response upper bound. No
continuous optimality or exhaustive scalar search is claimed. The odd trial
is unchanged. Physical source degree 1024 and prime output cutoff 2048 stay
fixed. The augmentation and the stronger RC266 contour comparison are unchanged.

## Affine physical source identity

Let f0=G0 P0 be the actual physical original source and let

    g = G0 P0-G Z = p+q+f,
    ||f||<=delta_old.

For t=27/20 the actual residual obeys the exact affine identity

    g_t = G0 P0-G(tZ) = t g+(1-t)f0.

This identity needs no commutation of G0 and G. The validator checks it
with exact noncommuting matrices, as well as the variational-center identity
for the rescaled trial. In D notation the physical residual is D times
N0 P0-N(tZ), with G=D N and G0=D N0.

The source f0 is materialized through degree 1024 and combined with the
pinned complete degree-1024 old residual polynomial. Its model errors are
included in norm. The high model remainder of the new source is computed
for the complete combined input Q_t=P0-tZ. Separate old/P0 tail norms are
not substituted for their correlated prime output.

## Put the auxiliary P0 source on the same prime model

RC231 supplies the P0 original-action model through degree 64. Its prime
translation/coefficient midpoints differ from the rounded parameters used
in RC250–262 for the old Q=P0-Z model. They are comparison models for the
same actual prime operator, and cannot be identified without a payment.

The new calculation uses RC250's exact chosen parameters for BOTH Q and
the auxiliary P0 source. For degrees through 64, the original P0 physical
coefficient is reconstructed from its D-action coefficient c and radius r:

    center=(H_n+s_mid)c,
    radius <= (H_n+s_upper)r+s_radius |c|.

The exact old prime coefficient is subtracted and the newly enclosed chosen-
parameter prime coefficient is added. All center rounding to the rational
10^-60 grid is added to the coefficient radius. This avoids unwieldy exact
denominators without discarding any uncertainty. Physical coefficient errors
are summed with masses 2B/(2n+1). The old P0 prime norm/projection tail is
independently reconstructed and must match RC231's pinned tail bound.

Above degree 64 the auxiliary source model uses the exact endpoint term

    (2n+1)/(n(n+1))

at matching even degrees, plus the chosen-parameter P0 prime coefficient.
The original regular-model tail above 64 is paid as a global physical error
using RC231's explicit physical norm bound. Its finite degree is 193; no
uncontrolled regular tail is inserted at high output degrees. The degree-40
pole model is already included in the low source block.

For constant P0, its prime output is piecewise constant on the same 15
segments. At a positive interior boundary b let jump be left value minus
right value. Parity and the Legendre primitive give, for even n>=2,

    prime_P0_coefficient(n)
      = sum_(seven positive boundaries) jump*(P_(n+1)(b)-P_(n-1)(b)).

The constant coefficient is the exact piecewise integral. The Legendre
recurrences use the inherited high-precision interval recipe, extended by
one recurrence step to degree 2049. The same 60-digit output intervals are
required in generation and replay.

The actual prime parameter error for this P0 model is separately paid.
For each pair, let de and dc be the saved distances of the chosen translation
and coefficient from their actual values. Since P0 has sup norm one and
zero derivative, its physical fault is bounded by

    sum_pairs 2*(dc*sqrt(2B)+(c_chosen+dc)*sqrt(2 de)).

The original regular-kernel and pole-Taylor faults remain included, as does
the discarded regular-model tail above degree 64. Together with the finite
coefficient errors these give a complete auxiliary-source norm error delta0.

## Complete correlated prime output for the new input

The new input is exactly

    Q_t=P0-tZ=t(P0-Z)+(1-t)P0.

The validator constructs its complete 15-segment polynomial prime output
using the unchanged seven chosen prime pairs. Its squared physical norm is
integrated exactly, retaining every input and cross-prime term. It reconstructs
the old Q model's full segment digest from this affine relation and checks
segment-by-segment linearity with the constant P0 model.

The prime coefficient block is evaluated as follows:

- Degrees 0–64: direct exact polynomial integration on all segments.
- Even degrees 66–512: the inherited polynomial-resolvent Green boundary
  formula, with all seven positive boundaries and matching-parity reflection.
- Even degrees 514–2048: exact affine combination of RC262's pinned old Q
  coefficient intervals and the new chosen-parameter P0 coefficient intervals.

The boundary jumps are reconstructed exactly in Legendre coordinates. Fresh
independent projection checks at 66, 514, 1024 and 2048 must intersect. Degree
66 compares the Green formula with direct polynomial integration; the high
controls compare the reused affine block with a fresh Green evaluation.

Subtracting the lower bound on captured physical coefficient energy through
2048 from the exact full segment norm bounds the entire infinite prime tail.
For this input the resulting tail above 2048 is about 0.0002732882101.
There is no assumption that input errors or separate prime outputs are
orthogonal.

## New complete model tail and error payment

In degrees 1025–2048 the original model output is exactly endpoint(Q_t)
plus prime(Q_t), at matching parity. The regular model, pole model and
identity contribution have no output in this range. Each combined interval
is squared before summing, retaining endpoint/prime cancellation.

Beyond 2048 the inherited signed endpoint-moment proof is re-evaluated on
the new Q_t. It gives endpoint physical tail about 1.3773443064e-7. Its norm
is added to the complete prime-tail norm. The explicit combined output
1025–2048 is then added. Finally, the ideal-band augmentation tail above
1024 is scaled by t^2 and added in norm to this original model tail.

The complete omitted model energy above 1024 is about 0.0006422790566.
This is a new bound for the new trial, not a rescaling of the old remainder
bound. All infinitely many omitted degrees remain paid.

The complete finite and global physical error obeys

    delta_new <= t*delta_old+|1-t|*delta0.

The inherited old error includes the RC266 actual rational augmentation
comparison on Z, which scales by t on tZ. The auxiliary f0 source has no
augmentation term. Original model faults and all retained coefficient,
actual-s and center-rounding errors remain included. The complete new norm
allowance is approximately 2.3210356305e-7.

## Re-evaluate Fourier bounds and the variational center

For the full new retained source polynomial, every diagonal and cross term
through degree 1024 is recomputed with exact interval arithmetic at U,
3U/2, 8U/5 and 2U. The low principal-512 numerical control is the valid
Parseval enclosure [0,A512], explicitly labeled as such; it is not an old
numerical tail of the changed source.

The high-Legendre band compression norm bounds are unchanged geometric
operator bounds and apply to the new model remainder. RC265's coupled-shell
lemma uses its one common unknown omitted energy over the full interval
0<=||q_t||/sqrt(R_new)<=1. RC266's actual augmented lower form and complete
J-to-Fhat comparison remain valid for the same operator. The same 1639
rational tau candidates are considered, subject to positivity and inverse-
weight ordering.

The four even trial coefficients y are replaced by t y. The actual original
and rational augmentation form intervals from RC247 recompute the full
variational center

    C(tZ)=2 Re<Zt,N0 P0>_D-<Zt,N Zt>_D.

The old center is not reused for the changed trial. If B_joint is the
certified model inverse comparison and w0 is its maximum weight, then

    T_even <= C(tZ)_upper
               +(sqrt(B_joint)+delta_new sqrt(w0))^2.

All numerical decisions use rational intervals. The resulting inverse upper
0.08710656569949887 is below the actual original source-form lower near
0.08855919602877185, certifying signed-gap lower

    +0.0014526303292729818.

The certificate stores the exact rational values; these long decimals are
display approximations. The actual inverse/gap interval remains intersected
with the previous valid bounds. RC266's odd inverse and signed gap are
preserved unchanged by immutable pin.

N is the positive chosen augmentation of N0. The canonical metric is still
M=D^-1 L with Fourier weight log(e+|xi|); D has the harmonic diagonal H_n+s.
The n(n+1) factors above belong only to the separate Legendre boundary
identity. No augmented floor is asserted as an original Weil positive floor.

## Validation and scope

Generation and exact replay verify 236 inherited Git blob pins. Replay
reverses pin and summation orders, uses the inherited higher-precision
Legendre/Fourier settings, and must reproduce the entire saved rational
certificate. The fresh source/prime reconstruction, segment digest and
linearity checks, projection controls, and noncommuting rescaling/variational
identities are checked. The inherited contour, coupled-shell and global
error controls also remain in force.

From repository root:

    python scripts/validate_rpb108_rc267_rescaled_even_response.py --output certificates/rpb108_rc267_rescaled_even_response.json
    python scripts/validate_rpb108_rc267_rescaled_even_response.py --output certificates/rpb108_rc267_rescaled_even_response.json --replay

Both current P0/P1 source signed gaps are positive, without adding a source
or enlarging the response trial space. This does not establish positivity
of the full rank-639 signed response matrix or the original full auxiliary
norm below one. The separate eight-source canonical inverse width remains
485647/1000000. Stage I, RH, F4 and Lean remain open/false.

Next: extend signed-response certification beyond the current two-source
tests and complete the full auxiliary response criterion.
