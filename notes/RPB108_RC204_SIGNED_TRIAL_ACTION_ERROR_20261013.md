# RPB108 — RC204: exact signed trial-action-error optimization

Aperture B=11/10. Parent RC203, commit a390010cf32cb2f0d773c7f5b7c8d5ec37540880. The supported canonical operator M=D^-1 L, six response sources (P0,P2,f0,psi0,w14,v10), eight RC203 inverse-trial directions, and their complete physical action approximants are unchanged.

## Result

The **uniform squared trial-action-error factor**, certified against the same six-source D Gram lower, improves from **0.002504** (RC203's selected response-adapted error envelope) to

\[
\boxed{E_{\rm trial}\preceq0.002365\,G_{\rm source,lower}.}
\]

This is a reduction of 139/2504, approximately **5.55%**, in the certified upper factor. It does not claim a reduction in the actual errors, residual Gram, variational inverse enclosure, or original Weil response. **RC203's six-source inverse width 0.743003 remains the latest certified inverse width**, above the half-Gram threshold 0.5.

The calculation evaluates the sharp finite sign-envelope of the *eight inherited individual action-error norm bounds* on the fixed RC203 least-residual inverse coefficient matrix. It does not assume their errors are orthogonal, independent or aligned in the physical operator.

## Exact theorem and matrix test

Let S have actual D Gram G with RC203 rational Loewner lower G_L, let Y be RC203's exact 8-by-6 inverse trial coefficient matrix and e_i the certified absolute D-norm error on its i-th physical action. For every real x,

\[
\|\mathcal E Yx\|_D\le\sum_{i=0}^7 e_i|(Yx)_i|
=\max_{\sigma_i\in\{-1,1\}}\sigma^T\operatorname{diag}(e)Yx.
\]

A simultaneous sign reversal does not change the resulting square. Fix sigma_0=1; exactly 128 signed rank-one matrices remain. If for all of them

\[
z_\sigma z_\sigma^T\preceq\beta G_L,\qquad
z_\sigma=Y^T\operatorname{diag}(e)\sigma,
\]

then the claimed uniform action-error Gram bound holds for all real x. The real self-adjoint source and action maps and the separate real/imaginary decomposition extend it to complex x, without enumerating complex phases.

The input G_L is rational with large denominators. Set Q=10^20 and, entrywise, form the integer matrix
\[
g_{ij}=\lfloor Q(G_L)_{ij}\rfloor-6\mathbf1_{i=j}.
\]
The exact defect G_L-g/Q has every diagonal at least 6/Q and every off-diagonal magnitude below 1/Q. It is therefore strictly diagonally dominant and positive definite. Thus g/Q is a valid **smaller** Gram lower, not an optimistic rounding of the matrix.

All 48 products e_iY_ij have exact common denominator Z=10^70; write z_sigma=Z_sigma/Z with integer vectors Z_sigma. For beta=473/200000, each integer symmetric matrix

\[
473\, g Z^2-200000\, Q Z_\sigma Z_\sigma^T
\]

has all six leading principal minors strictly positive. Exact fraction-free Bareiss determinants certify **128 matrices and 768 positive minors**. At the immediately smaller millionth, beta=591/250000=0.002364, the sign mask 12 has a negative sixth leading minor. This only rejects that *sufficient* rounded-Gram test, not all possible physical bounds or a smaller factor against the true Gram.

The RC203 source file is checked against immutable Git blob 5d321b659367ba459682b557b12ef63451f63e49. Each matrix uses the original rational trial rows and paid column errors, not floating-point eigenvalues.

## Evidence boundary and next cursor

**Closed:** this fixed-trial, all-mixture, uniform marginal action-error envelope; its rigorous integer matrix controls and millionth-grid acceptance. **Open:** transporting the smaller envelope into a rebuilt joint variational/residual inverse enclosure, passing the six-source half-Gram gate, all additional native source/odd-parity coverage, original augmentation and Stage I.

**RC205 cursor:** keep the unchanged RC203 source/trial carriers and complete signed analytic tails, substitute the newly proved trial-error Gram majorant only where mathematically permitted, rerun the full inverse Loewner lower/upper and Young-parameter search. Never infer a 0.5 pass merely from the action-error improvement.

## Reproduction

```bash
python scripts/validate_rpb108_rc204_signed_error.py \
  --output certificates/rpb108_rc204_signed_error.json \
  certificates/rpb108_rc203_residual_enriched_six_source_inverse.json
python scripts/validate_rpb108_rc204_signed_error.py \
  --replay --output certificates/rpb108_rc204_signed_error.json \
  certificates/rpb108_rc203_residual_enriched_six_source_inverse.json
```

The proof uses exact integer arithmetic and rebuilds all 128 signed rank-one tests. No historical files or original Weil/Lean branches are changed.
