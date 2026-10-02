# RPB-108 — normalized Laplace Fourier and Gauss reciprocal transfer

Date: 2026-10-01 (America/Los_Angeles).
Recovered research head: `279c732efb791a1553beae31c78ef8cd95a4fa0d`.

## Genuine half-line integral

For b>0, exp(-b|x|) is globally integrable. The complex oscillatory integrand
exp(-b|x|-itx) is also genuinely integrable. On the negative and positive
half-lines its coefficients have real parts b and -b respectively, so the
pinned library's convergent complex-exponential integral formulas apply.

The exact full-line integral is

\[
 \int_{\mathbb R}e^{-b|x|-itx}\,dx
 =(b-it)^{-1}+(b+it)^{-1}
 =\frac{2b}{b^2+t^2}.
\]

There is no totalized divergent integral or unstated convergence premise.

## Source/mathlib normalization

The Fourier transform uses exp(-2πixξ). Taking t=2πξ gives exactly the actual
mathlib Fourier transform of the physical Laplace kernel. Taking
b=2n+1/2 gives

\[
 \widehat{e^{-(2n+1/2)|x|}}(\xi)
 =\frac{n+1/4}{(n+1/4)^2+(\pi\xi)^2}.
\]

This is the actual real reciprocal term from the certified finite digamma
recurrence, not an analogy. Its negative matches the sign of the finite
terms subtracted from the shifted digamma tail.

## Remaining weak/operator transfer

Each scalar Fourier term is now attached. The finite physical sum must still
be passed through convolution with the rough compact carrier and identified
with its weak multiplier action. The shifted digamma tail must then be
controlled in the relevant exterior weak/operator limit.

The prior geometric pointwise kernel limit cannot substitute for that tail
control or for lawful integral interchange. Whole archimedean source attachment,
central cancellation, boundary reconstruction, compact weak realization and
source-domain/quadratic/normalized estimates remain open. Threshold bookkeeping
is closed; coercivity has not started. Canonical Weil and WD-T40 standing are
unchanged.

## Certification

Certification: Lean 4.34.0 / pinned mathlib `5ed2965256430c3649e86755f9576b54eca72435`;
8,964 build jobs passed. Five endpoints use only `propext`, `Classical.choice`,
and `Quot.sound`; declaration gate passed. Validation head
`bdad467cfd28555410444825f9642a629c88f2fa`, run `36944797734`,
job `110644359699`, source blob `63ed6b78651ff2ad5c9e4f78ede851d84b4ba70d`.
Validation-only workflow/cache changes are excluded from research promotion.
Prior checkpoint notes remain immutable.
