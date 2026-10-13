# RC185: paid five-source focus polynomial and complete canonical action

Parent: RC184, `2d768e05d14b04040ba2195a6050c2d770b53840`.

RC185 constructs the concrete finite trial direction requested by RC184's failed five-source gate. Its complete actual canonical action is certified, including input truncation and infinite output tails. The enriched inverse has not yet been evaluated.

## Same actual residual, tighter single-vector error

Let S=(P0,P2,f0,psi0,w14), Y be RC184's selected least-residual trial matrix, and x=(-1/120,3/50,-14/25,-26/25,1). The actual residual is R185=(S-MS Y)x and its represented counterpart is Rhat185=(S-VY)x. All operators and norms retain their prior meanings.

RC184's simultaneous correlated error Gram gave ||R185-Rhat185||_D<=0.002844380568. For this particular vector, the independent complete column errors give the additional valid bound

\[
 \|R185-Rhat185\|_D\le\sum_i |(Yx)_i|\epsilon_i
 <0.000561940375.
\]

No orthogonality of column errors is assumed. Taking the smaller valid bound improves precision for this same residual; it does not alter the whole five-source error Gram or inverse enclosure. Combining it with RC184's nominal residual Gram lower proves ||R185||_D>0.005640725111, strengthening RC184's historical lower bound.

## Exact finite direction with complete input payment

The new q185 is the rational degree-256 even Legendre prefix of Rhat185, rounded to a 10^-40 coefficient grid. Native source/action coefficients through degree16382 are reconstructed using RC184's unchanged formulas and carriers. Rounding error and all finite coefficients above256 are paid in D energy. Above16382, RC184's whole residual tail Gram pays the infinite remainder.

The nominal residual approximation error is below0.001321351888. Including the tighter actual-to-nominal bound gives

\[
 \|R185-q185\|_D<0.001883292263,
 \qquad
 \frac{\|R185-q185\|_D}{\|R185\|_D}<0.333875.
\]

The finite direction has D energy enclosed near0.000036732201303. The 0.333875 figure is a single-residual approximation norm ratio, not a Stage I stopping condition. No additional acceptance threshold is selected here.

## Actual canonical action

M=D^-1 L with L=D+h+R-rI, r=789/125. For the exact polynomial q185, its identity action is exact. Its endpoint action Cq185 is computed with the exact Legendre logarithmic matrix through degree4094. The endpoint tail beyond4094 is bounded by the common eta D energy and a geometric denominator estimate using the input degree256. No support-invariance assertion or cutoff commutation is used.

The negative-r D^-1 correction is evaluated on all finite input coefficients. For D^-1 Rq185, the RC179 analytic kernel/Beta/log-moment method uses kernel degree192 and output degree768. Every parameter interval, kernel remainder, coefficient rounding term, and infinite endpoint-log output tail is paid. There is no regular input-tail error because q185 is an exact finite polynomial.

The combined certificate proves

\[
 \|Mq185-\widehat{Mq185}\|_D
 <8.962008\times10^{-6}.
\]

The actual canonical pairing is enclosed between0.000015890093284 and0.000015998725538. It also passes the adverse structural comparisons a||q185||_D^2<(q185,DMq185)<2||q185||_D^2 using a=32125/230953.

Since ||M||_D<=2 on the full canonical domain, transferring this represented action to the actual focus residual proves

\[
 \|MR185-\widehat{Mq185}\|_D<0.003775546533.
\]

This latter bound includes the input approximation error and is distinct from the much smaller action error on q185 itself.

## Verification and scope

The certificate hashes twenty inputs: RC184, its eighteen inputs in their recorded order, and RC170's regular-kernel constants. All RC184 input hashes are checked. Reconstruction checks the materialized w14 hash and the inherited Cpsi data just as RC184 does. Exact replay reverses finite coefficient sums, endpoint sums, and regular-kernel summation; the complete JSON must reproduce exactly.

Run:

```
python scripts/validate_rpb108_rc185_five_source_focus_action.py --output certificates/rpb108_rc185_five_source_focus_action.json
python scripts/validate_rpb108_rc185_five_source_focus_action.py --replay --output certificates/rpb108_rc185_five_source_focus_action.json
```

Next: orthogonalize q185 against the existing five-source trial family, retain the corresponding action transformation and all mixed errors, and evaluate the enriched inverse on the same five response sources. RC184 identified poor conditioning from retaining its older q alongside w14; q185 therefore needs a paid basis treatment rather than an unchecked extra row.

The accepted RC182 four-source result remains intact. RC184's five-source half-Gram gate remains failed at width5.513393 until an enriched enclosure is evaluated. Native v10,z_b6,t10 remain later coverage obligations. Stage I, whole-aperture original Weil positivity, RH, F4 and Lean remain open/unclaimed.
