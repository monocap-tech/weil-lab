# NF406 — Original fourth supported multiplier: certify the physical logarithmic endpoint and its exact power

**2026-10-30 PT | Canonical W-ODD-NEG OPEN.** Scope: unchanged original NF370 fourth source `u4=f_(T e4)-w4`, actual original signed seven-prime/digamma multiplier `m`, inherited finite-source strong realization, original support `I=[-B,B]`, `B=11/10`, and NF404 fixed dyadic pole centering `a=6677356497477490213/4611686018427387904`. The **complete original centered physical multiplier power is not measured.** Do not confuse source-only exact logs/point samples with a numerical interval certificate for `||1_I[m(D)u4-a sinh(x/2)]||²`.

## Previous → Current → Next

**Previous NF405:** SHA-pinned original digamma/prime action in physical x-space, compact `t∈[0,4B]`, keeping all seven original prime shifts and exact arch tail constant. A second representation extracted the source's true signed high-frequency boundary principal part at Lambda=2^24 and certified a whole-real signed-multiplier remainder <5.038e-17. Neither representation integrated the final positive supported physical norm.

**Current NF406:** Identify the **endpoint-singular contribution to the original complete physical response itself**, not a Fourier shadow. The actual original signed source endpoint is `v=u4(B)≈-1.167986449096830e-11` (NF374 4096-bit source native and original NF405 exact Fraction signed reconstruction). The archimedean kernel produces an unavoidable logarithmic boundary layer in the complete physical response. Certify its exact squared L² mass, remove it **as a function before integration**, and prove an exact strip-width budget. Separately reconstruct source u4 on actual physical support knots with the original NF369 SHA-pinned 242D projection, as an input to the future compact integral.

**Next NF407:** Integrate the **bounded, regularized** original arch response, all seven *signed* prime translates and dyadic pole subtraction on physical x intervals cut at the genuine prime support seams, and calculate the cross with the certified logarithmic function *before squaring/export*. A provisional point/mesh estimate cannot be promoted without an interval quadrature error envelope and a seam-dependent boundary analysis. If upper or lower does not settle NF404's original positive norm cap, explicitly retain the result as inconclusive.

## A. Rigorous original physical log boundary theorem

The exact NF405 signed multiplier arch action, with `u=u4` extended by zero off the interval, is

```
A u(x) = c_B u(x)
  -(1/2) ∫_0^(4B) K(t)[u(x+t/2)+u(x-t/2)-2u(x)]dt,
K(t)=exp(-t/4)/(1-exp(-t)).
```

For any fixed interior x, `t→0` has symmetric difference `t²u''(x)/4+O(t⁴)`, so the apparent `K(t)≈1/t` is cancelled locally. However **that cancellation is not uniform as x approaches B** when original u(B) is nonzero. Let `x=B-d`, `0<d<<B`. The right translation exits support at `t=2d`:

```
for 0<t<2d:   u(x+t/2)+u(x-t/2)-2u(x) = O(t²),
for 2d<t<B/2: right shift =0,
               u(x-t/2)-2u(x)=-u(B)+O(t+d).
```

Because `K(t)=1/t+O(1)` near 0, the nonuniform region contributes

```
A u(B-d)= +(u(B)/2) log(B/d) + O(1), d→0+.
```

The absolute remainder is bounded for `x` near B: the small t region integrates O(t), the crossed region subtracts exactly the `1/t` coefficient leaving O(1)+O(d/t), and large t is integrable because `t>0` and u has compact support. Original odd parity yields the opposite logarithm at -B. The seven genuine prime shifts `u(x±ln n)`, `n=2,3,4,5,7,8,9`, are **piecewise bounded** with support steps at `x=±B∓ln n`, but do not introduce further logs. The original dyadic `a*sinh(x/2)` is continuous and has no log.

Define the one specific source-anchored, physically odd logarithmic primitive:

```
q(x) = [u4(B)/2]*sgn(x)*log[B/(B-|x|)],  |x|<B.
g(x) = 1_I[m(D)u4(x)-a*sinh(x/2)].
h(x) = g(x)-q(x).
```

Then `h` is bounded in neighborhoods of both endpoints (though can have **finite jump seams** at original translated prime supports). This removes the only LOG endpoint singularity without changing `g`. It is NOT an assertion that the entire physical response or the entire norm is small.

## B. Exact original `q` energy and mandatory cross

Using `∫_0^B log²(B/d) dd=2B` gives the exact identity, no quadrature:

```
||q||²_(L²(I))
 = 2*(u4(B)^2/4) ∫_0^B log²[B/(B-x)]dx
 = B*u4(B)².
```

The original signed endpoint input `u4(B)` is source SHA-pinned to original NF374 native SHA256 `a725a6da6bf29ce21b1955df8f4d0b35b87ff8f003d09cdff13581d1b82f7559`, original NF405 endpoint source SHA256 `1945dc88d43fb329ff490e29cfc40b06bc6049ddd55186cc5f0f996a701001c3`, and original NF404 pole-centered source. Fully exact Fraction outward result:

```
1.50e-22 < ||q||² < 1.51e-22,
actual source interval centered near 1.500611579801204e-22.
```

This is about 13.7% of original NF404's source-selected centered power `E≈1.0950024763e-21`, but **not an independent additive contribution to total ||g||²**. In particular,

```
||g||² = ||h||² + 2<h,q> + ||q||².
```

The cross must be evaluated as a **signed physical** integral. From the accepted selected projection alone, `||g|| >= ||P_J g|| >3.3e-11`; independently `||q||<1.23e-11`, so `||h||>2.07e-11`. These are genuine original-source necessary lower bounds, not upper certificates, and prove that the regular component cannot simply be dropped. Both inequalities are checked **root-free in exact Fraction**.

CI [#41155918528](https://github.com/monocap-tech/weil-lab/actions/runs/41155918528) **SUCCESS**, script `scripts/local_replay/nf406_original_physical_endpoint_log_exact.py`, durable receipt `notes/data/provisional/NF406_original_physical_endpoint_log_exact.json`.

## C. Concrete support-boundary strips, original singular model only

For the two endpoint strips `I_delta=[-B,-B+delta]∪[B-delta,B]`, the q-only exact source energy is

```
||q||²_(I_delta)
 = [u4(B)² delta/2] * [L² + 2L +2],
L=log(B/delta).
```

Choose exact dyadic support widths `delta=B/2^k`, and invoke the **already certified original NF375** `log2<7/10`, so `L<7k/10`. Paying the worst original endpoint outward |u(B)|, exact Fraction calculations select the first dyadic `k=24` such that the q-only two-strip energy is **strictly below one thirty-second** of NF404's original exterior power budget `gamma²≈5.1296807868e-26`:

```
k=24,  delta=B/2^24 ≈6.556510925293e-8,
||q||²_two_endpoint_strips <1.421435e-27
                       <gamma²/32 ≈1.603025e-27.
```

This is an exact allocation of **q-only** explicit logarithmic energy, not a bound on `||g||²` in the strips. The regular `h` and signed `h,q` cross must also be enclosed before any strip is dropped. The more useful implementation is likely to integrate q **analytically with h** rather than create a tiny physical x mesh near the endpoints.

CI [#41155978570](https://github.com/monocap-tech/weil-lab/actions/runs/41155978570) **SUCCESS**, exact source-only replayer `scripts/local_replay/nf406_original_log_boundary_strip_exact.py`.

## D. Original source u4 physical sample oracle

The true unchanged original source is `u4 = F T e4 - (F-JX)(I+Y0)Te4`, where `X=D(D^T H D)^-1 D^T V`. The original large dyadic `Y0` can cause enormous cancellation in raw basis coefficients, so naively sampling `F Y0T` in double precision would not measure `u4`. Dedicated 4096-bit Arb implementation `scripts/verify_nf406_original_fourth_physical_source_samples.py` reconstructs the original full 242×242 physical Gram H, SHA-pinned original D frame, original four critical probes and native original NF369 quotient shear; evaluates **correlated u4, f_(Te4), w4** at eight rational support knots; checks odd parity, original NF374 exterior w4 endpoint and NF405 true signed u4(B) interval. It does not evaluate `m(D)u4` or its positive physical norm. Its CI execution status must be observed before any samples are accepted.

## NF406 decision and open obligations

**Accepted:** original `q` logarithmic singular source coefficient, physical norm and explicit q-only endpoint strip budget, under inherited original source-specific operator realization. Source-only exact CI 2 PASS.

**Not measured:** bounded regular physical `h=g-q`, signed `<h,q>`, their original complete norm, true physical J242-perpendicular fourth lowband upper, infinite exterior form inverse, general original operator domain, W-ODD-NEG, even/whole Weil and RH. There are no new signed source kernel cells and no main merge.

**Next bold NF407:** original source-correlated **regularized** compact physical integral with all signed arch/prime/pole terms, original genuine support seams and rigorous numerical error. Do not permit the q-only power bound to stand in for the full physical response.
