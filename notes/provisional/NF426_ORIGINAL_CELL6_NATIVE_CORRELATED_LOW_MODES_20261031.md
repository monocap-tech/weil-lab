# Weil-Lab NF426 — Native source-correlated Chebyshev low-mode evaluation, original cell 6

**2026-10-31 PT, original `W-ODD-NEG` OPEN.** Draft stacked [PR #432](https://github.com/monocap-tech/weil-lab/pull/432) on NF425 [PR #431](https://github.com/monocap-tech/weil-lab/pull/431). This stage implements, but does not yet assert success of, the first four native Chebyshev coefficients of the **complete original fixed cell-6 analytic branch**; 2,045 additional degree-2048 coefficients and the original signed integrals are not claimed.

## Previous cursor / current circle / next bold

- **Previous:** NF424 original global digamma + two endpoint-image source transfer, strict original full physical J6 model residual <10^-45. NF425 degree-2048 Chebyshev existence/uniform approximation bound <2·10^-45; **no numerical coefficients**.
- **Current NF426:** Native python-flint 0.8.0 `arb/acb` 2048-bit real/complex balls build original coefficient prefix n=0,1,2,3, with a rigorous finite-2048-image tail, exact source-dyadic radii, five physically post-seam original prime terms, original endpoint log and NF404 center. The remaining index-wide problem is explicitly OPEN until actual focused CI has passed and source-pinned intervals are retained.
- **Next:** Audit native overlap against NF416/NF419/NF421/NF423 at x=0.9, extend coefficient range to 0..2048 with measured complexity (possibly blockwise FFT/Bessel recurrences), and generate exact signed log/Chebyshev moments and true cell-6 pz/z² integral. Then original cells 3/7 and five remaining, whole NF410/NF404.

## Reorganization that preserves source correlation

Original odd source:

`u(y)=sum_(f,k) c_(f,k)*y^k*(sin(2*pi*f*y) if k even else cos(2*pi*f*y))+c_p*sinh(y/2)`.

All 242 selected plus four original critical generators, 32 critical sine frequencies, native raw dyadic midpoints and source error <10^-700 are preserved. Each term is a two-sided conjugate exponential pair with positive-frequency complex amplitude `alpha=c/(2i)` for even k and `alpha=c/2` for odd k.

Let `a_m=m+1/4`. For the original entire-source digamma/endpoint transfer from NF424, define the single correlated endpoint amplitude

`L_m = sum_(f,k,sign) alpha_(f,k,sign) exp(lambda*B) * sum_(j=0)^k binom(k,j)*B^(k-j)*j!/[2^j*(a_m-lambda/2)^(j+1)]`

with separate odd-pole treatment at m=0. Since the original full source is exactly ODD, its right-endpoint amplitude is `-L_m`, **not a separately fitted value**. Hence both original endpoint images together equal

`sum_(m=0)^2047 L_m/2 * exp(-2*a_m*B) * [exp(2*a_m*x)-exp(-2*a_m*x)]`.

The m=0 singular piece in the `c_p sinh(y/2)` mode is combined symbolically with the digamma pole, as follows. Write

`K_p=[psi(1)+psi(1/2)]/2-log(pi)-B`.

Its regularized full-line contribution to the true original source arch is

`c_p*(K_p*sinh(x/2)+x*cosh(x/2))`.

For m=0, only the **regular** pole component remains in the one-sided left amplitude:

`L_0^(p)=-c_p exp(-B/2)`.

For m>=1:

`L_m^(p)=(c_p/2)*[exp(B/2)/m-exp(-B/2)/(m+1/2)]`.

No division by zero, no independent digamma-/image-pole evaluation. These formulas preserve the physical n=8,9 neither branches and original signed n=2,3,4,5,7 source translations.

For Chebyshev `x=C+Ht`, `C=91/100,H=7/100`, set `b_0=1,b_n=2` for n>=1. Each image contributes the native interval coefficient

`(L_m/2)*b_n*I_n(2*a_m*H)*[exp(-2*a_m*(B-C))-(-1)^n exp(-2*a_m*(B+C))]`.

All endpoint-image source generators are summed into **one real Arb `L_m` before this Bessel map**, preserving cancellation instead of interval-expanding independent image modes.

The full-line source term `exp(lambda*x) D(lambda)` (NF424) contributes `partial_lambda^k[D(lambda) exp(lambda*C) b_n I_n(lambda*H)]`, implemented without numerical lambda differentiation: FLINT's rigorously enclosed polygamma derivatives `D^(r)`, and Chebyshev multiplication recurrence `t*T_0=T_1; t*T_n=(T_(n-1)+T_(n+1))/2` produce the exact coefficients of `x^j exp(lambda*x)`. Complex source components are reunited by conjugate symmetry **before taking the real interval**.

The five signed original prime branches are evaluated using `u(x-log n)+u(B)` exactly; original endpoint log has

`ell_0=log(B/Q), ell_n=2q^n/n (n>=1), Q=(B-C+sqrt((B-C)^2-H^2))/2, q=H/(B-C+sqrt((B-C)^2-H^2))<1/5`.

The original dyadic NF404 centering term is `-a sinh(x/2)`, with a held *exactly* at `6677356497477490213/4611686018427387904`.

## Native error and certification scope

Each retained native interval is widened by `4·10^-45`, sufficient for the original NF424 2048-image tail and coefficient dyadic uncertainty across the slightly larger rational interval `[.84,.98]` **for the fixed cell-6 analytic continuation only**. The Chebyshev coefficient functional has norm at most two in the sup norm. The original physical `z(x)` is identical to this analytic continuation on exactly `J6=(log7-B,log8-B)`; it is NOT identical outside J6 because prime support branches change.

The focused CI explicitly rejects a resulting coefficient interval width >=10^-25. **Even a complete passing 4-coefficient certificate is NOT a degree-three uniform approximation**. All uncomputed n>=4 coefficients remain nonzero/uncontrolled computationally (although the separate NF425 degree-2048 existence bound persists). An original pz/z² scalar must not be calculated from a truncated four-mode prefix.

## Repository evidence and gates

- Native script: `scripts/local_replay/nf426_original_cell6_correlated_chebyshev_prefix_native.py`.
- Focused CI: `.github/workflows/nf426-original-cell6-correlated-chebyshev-prefix.yml`; generated original source-pinned JSON retained as a workflow artifact **only upon passing**.
- Parent references: original NF407 source SHA in NF423 `0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce`, original NF406 seam SHA `c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675`.
- **Current acceptance:** executable native low-mode method pending focused CI; do not mark original coefficient prefix ACCEPTED on a failing or unfinished run.
- **Always OPEN:** remaining coefficients through n=2048, complete real cell6 polynomial interval table, signed cell6 `pz` and `z²`, other seven cells, complete NF410/NF404 scalar, original fourth exterior J242 upper, `W-ODD-NEG`, even/whole Weil, domain/infinite inverse and RH.

No historical source replacement or merge to main.
