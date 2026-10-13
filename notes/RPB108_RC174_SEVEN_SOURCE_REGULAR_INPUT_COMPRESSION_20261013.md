# RPB108 — RC174: seven-source regular input compression

Aperture 11/10. Parent RC173: `0f30fec20153a724c55b4b8d3c6555b448222c54`.
Only `research/rpb108-route-consolidation` is written. Historical checkpoints, source frames and Lean remain unchanged.

RC174 pays the regular component's infinite input tails on the full seven-source family. The tail-only D-action relative norm upper is 0.000085465. Combining that with RC170's Poisson operator error gives a represented finite-input regular-map relative norm upper of 0.000128810. Both bounds hold uniformly over real and complex mixtures, in conditioned or original native coordinates.

The remaining regular action can therefore use finite polynomial inputs without assuming the analytic tails vanish. The output arithmetic and carrier coefficients of those finite-input actions have not yet been evaluated for the full family.

## High-input-mode operator theorem

Let q be supported on [-B,B] and orthogonal in physical L2 to every polynomial of degree <=N. Put n=N+1. The real-axis integral Taylor remainder for exp(-2 pi i x xi) has modulus at most (2 pi B |xi|)^n/n!: its integral representation uses only unit-modulus exponentials. All lower Taylor terms annihilate against q. Hence

\[
|\widehat q(\xi)|\le\sqrt{2B}\,\|q\|_2
\frac{(2\pi B|\xi|)^n}{n!}.
\]

For m(xi)=log(1+e/abs(xi)) and I2=integral_0^infty m^2=e pi^2/3, split Fourier space at U>0. The low-band term is at most 4B I2 times the square of this uniform remainder times ||q||_2^2. In the high band, log(1+x)<=x gives m<=e/U; Plancherel pays the remaining term. Restricting output to [-B,B] can only lower its norm. Therefore

\[
\|Rq\|_2^2\le\left[
4BI_2\left(\frac{(2\pi BU)^n}{n!}\right)^2
 +\frac{e^2}{U^2}\right]\|q\|_2^2.
\]

Choose U=n/(6 pi_upper B). Then 2 pi B U<=n/3. Monotone integral comparison for log(k) gives n!>=(n/e)^n; the paid e<11/4 bound gives remainder <=(11/12)^n. The validator accepts the minimum of this new squared bound and r^2, where r=789/125 and the inherited supported-source norm bound is checked exactly. Denote the resulting squared factor by phi_N^2.

This theorem holds for all supported physical inputs after applying I-Pi_N, including arbitrary complex source mixtures. It does not require individual high-degree response columns. It does not claim a sharp operator norm or an optimal frequency split.

## Seven-source correlated tail payment

Take N=16382, matching the already paid finite source prefix. RC159 supplies the signed tail polynomials of every conditioned source in the common eta carrier; RC168 supplies positive, full infinite eta moments. RC174 convolves products by degree before applying their signed moment intervals. Weighted Loewner conversion gives a full PSD upper Gamma_tail for the actual omitted source D Gram. The exact native-to-conditioned coefficient identity is verified.

Every omitted degree is at least 16384, so its physical Gram is at most Gamma_tail/(H16384+s_lower). For the regular output, D^-1 converts physical squared error to D energy at cost at most 1/s_lower. The full correlated input-tail action error is thus bounded by

\[
E_{tail}^*D E_{tail}\preceq
\frac{\phi_{16382}^2}{s_{lower}(H_{16384}+s_{lower})}
\Gamma_{tail}.
\]

The accepted relative D-norm upper is 0.000085465. This is smaller than simply discarding the same source D tail under a generic bounded action norm.

Let Rhat be RC170's represented positive Poisson operator, with physical L2 norm error epsilon. The complete represented approximation is D^-1 Rhat Pi_N S. Its error splits into D^-1 R(I-Pi_N)S and D^-1(R-Rhat)Pi_N S. The latter error Gram is at most epsilon^2 G_upper/s_lower^2. This uses physical/D equivalence and the orthogonal D projection; it is a full mixture bound, not an independent-column diagonal estimate.

Young's matrix inequality pays their mixed output error. Among the fixed positive parameter grid, tau=1/2 selects the best tested relative bound. Exact rational PSD accepts total relative energy and its outward square root 0.000128810. The native bounds are exact inverse-source congruences and have the same relative norm upper. NumPy supplies a search hint only; every grid acceptance and preceding-grid rejection is rational.

Although Rhat is positive selfadjoint, Rhat Pi_N is an action approximation and its self-adjointness is not assumed. Subsequent signed mixed pairings must retain the error payment. The endpoint action C, identity source and -r D^-1 source term are not compressed or discarded by this theorem.

## Concrete finite source f0

RC126/129's actual f0 has eta coefficients at every even degree 2..988. RC174 directly encloses the physical squared norm of each discarded finite tail, paying the actual s interval. Multiplying by phi_M^2/s_lower gives the absolute D-energy error of omitting that input from the regular action.

| Requested regular input-tail D-norm budget | Smallest even input degree for this sufficient bound | Accepted component error, outward |
|---|---:|---:|
| 10^-4 | 172 | 0.000099858 |
| 10^-5 | 492 | 0.000009960 |
| 10^-6 | 936 | 0.000000982 |

All even cutoffs from 0 through 988 are tested. Each predecessor fails this bound at the stated target; that is not a lower bound on actual action error or proof that smaller inputs cannot work with a sharper estimate. These are component targets, not a selected Stage I tolerance.

For example, at input degree 256 the new component norm upper is 0.000042877, versus 0.001234035 from the generic r-only estimate. The full f0 action must still pay the Poisson evaluation and output carrier error, along with its other canonical action terms. The compressed input contains 86 nonzero even Legendre terms at degree 172, rather than the original 494 through degree 988.

## Remaining action contract

The next concrete operation is evaluation of finite-polynomial regular outputs with full arithmetic, coefficient and output-tail errors. The original seven-source infinite inputs now have a quantified regular-component reduction; the special f0 budget also supplies a smaller actual finite input. This does not realize all required regular output coefficients or execute full-family canonical inversion.

RC173's two-source inverse and warm start remain intact. Stage I's final numerical tolerance and full source coverage remain open. Original Weil/augmented actions, the original signed response below one, whole-aperture positivity, Global/F4, RH and Lean closure are unchanged.

## Reproduction

Run `scripts/validate_rpb108_rc174_regular_source_tail_compression.py --output certificates/rpb108_rc174_regular_source_tail_compression.json` with RC173, RC169, RC168, RC159, RC170, RC121 and RC129 certificates in that order. Repeat with `--replay`. Replay reverses signed moment and source-tail accumulation and candidate traversal, comparing the complete rational certificate. Dependency hashes, the exact source-tail transform, both coordinate systems' PSD bounds and each minimal component cutoff are checked.
