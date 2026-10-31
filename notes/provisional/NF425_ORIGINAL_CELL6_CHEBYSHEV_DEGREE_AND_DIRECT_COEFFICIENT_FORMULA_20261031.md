# Weil-Lab NF425 — A single certified Chebyshev degree suffices on complete original physical cell 6

**2026-10-31 PT.** `W-ODD-NEG` canonical active obligation OPEN; RH OPEN. Stacked on NF424 original-global-transfer branch (head `0bdedd947767ab3d7387c8aacc7d61d3663f180e`). Unchanged NF370 fourth source, NF407 exact 4096-bit source balls (242 selected + four critical, 32 critical sines, pole), NF406 seven original prime seams, NF422 physical arch transfer, NF423 true cell-6 third-derivative certificate, NF424 full source-correlated generating function and image tail.

## Previous cursor / current circle / next bold

- **Previous NF424:** source-exact physical generating function `G(x,lambda)` (full digamma response + two geometric endpoint image families) and strict original `sup_(J6)|z-z_2048|<10^-45` from original source coefficient balls and 2048 images per endpoint. Focused original preflight passed; actual finite expression not evaluated.
- **Current NF425:** Prove the *entire* original cell-6 fixed-branch finite function `z_2048` is holomorphic on one explicit complex Bernstein ellipse, bound it there using the *actual* source triangle and elementary digamma/cancellation estimates, and certify that a **single degree-2048 Chebyshev interpolant** exists with `sup_(J6)|z_true-P_2048|<2·10^-45`. This removes the question of how many independently certified centers or derivative tensors are mathematically needed. **No Chebyshev coefficients were computed.**
- **Next NF426:** Build and evaluate the actual **correlated Chebyshev coefficients** directly from generating functions/Bessel moments (with exact pole cancellation), enforce an outward radius per coefficient, and integrate the original signed `p z` and `z²` against the genuine NF410 full-cell moments. Only then promote cell-6 scalar information; afterward cells3/7 and remaining five, NF404 complete scalar.

## Exact original cell and analytic continuation (do not cross the physical prime seams)

The **true** physical open cell is

`J6=(log7-B,log8-B), B=11/10`.

The original NF406 exact knot brackets imply `J6 subset [.84,.98]`. Fix the **cell-6 analytic branch**, with n2,3,4,5,7 post-seam, n8,n9 neither. Outside J6 this analytic continuation is NOT the physical original piecewise function; restricting a polynomial to J6 is mandatory.

Use the convenient rational Chebyshev coordinates

`x=C+H*t, C=91/100, H=7/100, -1<=t<=1`.

For Bernstein ellipse `E_rho` with `rho=2` in t, the exact rational coordinate overbounds are

`329/400 <= Re x <= 399/400`, `|Im x|<=21/400`,

and `Re(B-x)>=41/400>1/10`. Thus both original physical image series converge normally on E2; the original endpoint logarithm `log[B/(B-x)]` has a holomorphic principal branch throughout this ellipse. All signed-prime *fixed-branch* original finite source translates are entire; physical branch switching is not being analytically crossed.

## Uniform conservative complex magnitude on E2

The original source midpoints are the exact NF407 242 selected + 4 critical dyadics. With the 32 original critical sines, the source is a real finite sum of `c_(f,k)*y^k sin(2*pi*f*y)` for even k and cos for odd k, plus `c_p sinh(y/2)`, with source-degree k<=13, original f<883, and exact source triangle

`sum |c_(f,k)| B^k + |c_p| < 10^160`.

The original total coefficient radius is strictly below `10^-700`. These overbounds are re-derived from the repository source, not from rounded values of the tiny observed `z`.

For each exponential source frequency `lambda0=±2*pi*i*f`, apply Cauchy's derivative estimate on the `|lambda-lambda0|<=1/8` disk. The digamma arguments `a±lambda/2`, `a=1/4`, have **real part >=3/16** and `|z-1|<4000`. From

`psi(z)=-gamma+sum_(m>=0)[1/(m+1)-1/(m+z)]`

one gets, by splitting at m=10000,

`|psi(z)| < 1 + 10000*(1+16/3) + 4000/9999 < 64000`.

The two image series each have `t>=41/200`; the geometric factor obeys `1/(1-e^(-t)) < 1+1/t <6`. For the source-frequency lambda disks, all image denominators have real part at least 3/16. The complex oscillatory exponential is bounded by

`|e^(lambda*x)| <= exp(7065*(21/400)+(1/8)*(11/10)) < 3^373`,

using `pi<4` and `e<3`. Consequently the finite combined original transfer satisfies the deliberately broad disk bound

`|G_2048(x,lambda)|<10^6*3^373` on each source-frequency disk.

Cauchy then gives `|partial_lambda^k G_2048|<=k!8^k*10^6*3^373` for k<=13; `13!8^13<10^24`. The true `sin` and `cos` source mode values are built from *both* ±imaginary lambda values, so the holomorphic x extension uses those paired exponentials, **not the nonholomorphic operation Im of a complex-x function**.

At original pole frequencies `lambda=±1/2`, `psi(1/4∓lambda/2)` has a simple pole, exactly canceled by its corresponding `m=0` image. **Do not evaluate those divergent pieces separately.** For `beta=a∓lambda/2`, the combined term is

`e^(lambda*x)/2 * [psi(1+beta)+(exp(-2*beta*d)-1)/beta]`

with `d=B-x` on the left or `d=B+x` on the right. Its beta=0 quotient is exactly `-2d`, and on the small pole disk its magnitude also satisfies the above conservative bound. This explicitly establishes holomorphy of the complete odd pole contribution.

The five post-seam original source translates have `|x-log n|<3B` on the ellipse (using log7<2); `3^13<10^7` absorbs the shifted monomials. The original endpoint log has magnitude <100 on the right-half-plane enclosure, and the signed prime weights total <3. The exact original NF404 dyadic center is <2. Combining all terms, an intentionally huge but rigorous analytic triangle envelope is

**`sup_(x in E2)|z_2048(x)|<M=10^400`.**

The script checks the explicit rational exponents, source degree/frequency limits, digamma bound, image denominator/geometric bounds, `13!8^13`, and final integer inequality `10^190·3^373<10^400`. The complex-analysis identities above, rather than a merely sampled ellipse grid, are the mathematical premises of this bound.

## Explicit one-polynomial interpolation acceptance

For a holomorphic function bounded by M on Bernstein E2, the degree-N Chebyshev-node interpolation error satisfies the standard conservative bound

`||z_2048-P_N||_(Linf([.84,.98])) <= 4*M*2^(-N)/(2-1)`.

With N=2048 and M=10^400, exact integer comparison certifies

`4*10^400 / 2^2048 < 10^-200`.

NF424's independently source-certified real original cell-6 model error is <10^-45. Therefore the **mathematically defined** Chebyshev interpolant at 2049 nodes has the rigorous *existential* bound

**`sup_(x in J6)|z_true(x)-P_2048(x)| < 2·10^-45`.**

A numerical implementation has NOT yet evaluated those 2049 polynomial coefficients or created a signed cell-6 integral; the statement does NOT provide a usable interval table of actual values. Its force is that there is now one source-correlated **fixed finite polynomial degree** with an audited margin, instead of NF423's 667657 separately certified derivative centers.

## More efficient actual coefficient construction — no physical x integral

Every finite image term is an exponential `e^(mu*x)` times a source-dependent constant; lambda derivatives of the complete digamma term give exponential-polynomials of degree <=13. On `x=C+H*t` the exact Chebyshev expansion is

`e^(mu*x)=e^(mu*C)*(I_0(mu*H)+2*sum_(k>=1) I_k(mu*H)*T_k(t))`.

Thus the full original `x^j e^(lambda*x)` coefficients can be constructed by **lambda differentiation** of `e^(lambda*C)*I_k(lambda*H)`. The source sin/cos and every original signed prime translate use the same paired ±frequency generator; the two physical endpoint image families use `mu=±2(m+1/4)`; the original centered pole uses `mu=±1/2`. Coefficients are to be summed with **correlated Arb intervals and exact source radii**, not independently rounded source-term residuals. This Bessel construction is a formula, not an executed numerical coefficient certificate.

The source endpoint logarithm also has exact Chebyshev coefficients. Let

`A=B-C=19/100`, `Q=(A+sqrt(A²-H²))/2=(19+2sqrt78)/200`,
`q=H/(A+sqrt(A²-H²))=7/(19+2sqrt78)<1/5`.

Then

`log(B/(B-x))=log(B/Q)+2*sum_(k>=1)(q^k/k)*T_k(t)`.

The independent exact-rational tail beyond degree 2048 is smaller than `10^-1400`. No physical x/t integration or numerical differentiation of the endpoint log is necessary.

**Design-only future coefficient-radius gate:** if all 2049 actual Chebyshev coefficients receive outward certified radius at most `10^-25`, the additional complete cell uniform uncertainty is at most `2049*10^-25<10^-21`, far smaller than NF409's provisional cell-integration L² tolerance 9·10^-17. This per-coefficient target has NOT been achieved by the present pass.

Finally `p=q+r` on J6 is the exact original endpoint logarithm plus the **five active original signed constant jumps**. Once actual coefficient balls exist, signed `integral_(J6) pP` follows from exact log/Chebyshev moments, and `integral_(J6) P²` from the identity `T_j T_k=(T_(j+k)+T_|j-k|)/2`, with genuine outward irrational knot brackets. The current NF410 polynomial moments only cover low degrees; the exact moment recurrence must be extended and certified before the signed integral can be called completed.

## Verification and disposition

- Exact original-source/rational Bernstein geometry/degree/log-tail replay: `scripts/local_replay/nf425_original_cell6_chebyshev_existence_exact.py`.
- Focused runner: `.github/workflows/nf425-cell6-chebyshev-existence.yml`.
- Classification: **original-cell6 global analytic degree/existence/remainder ACCEPTED if focused replay passes; numerical original finite polynomial coefficients, signs, `p z` and `z²` integral remain OPEN.** CI verifies the declared source pins and rational inequalities; it is not a 4096-bit evaluation of the finite original response.
- Other original cells 3/7 and five remaining, whole NF410/NF404 scalar, fourth J242 complement upper, original infinite inverse/domain, `W-ODD-NEG`, even and whole Weil, RH **OPEN**. No source replacement or main merge.
