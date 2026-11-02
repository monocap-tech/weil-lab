# Weil-Lab NF445 — Actual correlated image residual and exact Laplace kernel

**November 1, 2026 PT; original odd source.** NF445 advances the original NF444 *representation* obligation, not a full signed J7/J8 integral. Research draft [PR #466](https://github.com/monocap-tech/weil-lab/pull/466) stacked on NF444 [PR #465](https://github.com/monocap-tech/weil-lab/pull/465). **Source-native 4096-bit samples, endpoint derivatives and exact formal Laplace identities ACCEPTED. Quantitative all-image tail, J7/J8 signs and RH OPEN.** No main merge.

## Previous cursor → current circle → next bold

**NF444 previous:** Source-exact universal image coefficient \(T_m=v/a_m+R_m\), \(a_m=m+1/4\), \(v=u_4(B)<0\), \(B=11/10\). Its \(v/a_m\) image series sums in elementary functions and cancels the explicit original principal logarithm. The leftover \(\sum R_m\) is uniformly absolutely convergent through \(x=B\), but the crude independent-source triangle \(M\sim1.4181\times10^{144}\) leads to an unusable m≥2048 bound \(\sim3.4635\times10^{140}\). Actual original true J1,J2,J3 signed POSITIVE; J4,J5,J6 signed NEGATIVE; J7,J8 still OPEN.

**NF445 current:** Recover \(R_m\) itself as a **single correlated analytic continuation of the complete original 246-source linear form**, not a sum of absolute generator envelopes. Crucially, the continuation \(U_{\mathrm{ent}}(y)\) below is the *entire finite-generator extension* of the original compact-support source \(u_4\); for \(y>B\) it is **not** the physically extended compact-supported source. It is an exact identity of the authentic NF424/NF443 *archimedean transfer coefficients*. Do not confuse \(U_{\mathrm{ent}}\) outside support with the original physical response.

## Exact Laplace representation of the original native image coefficients

For every integer \(m\ge1\) set \(a_m=m+\tfrac14\). For one genuine original frequency/order generator \(c x^k\sin(2\pi f x)\) (even k) or \(c x^k\cos(2\pi f x)\) (odd k), write its source carrier as \(2\mathrm{Re}(\alpha x^k e^{\lambda x})\), with \(\lambda=2\pi if\), \(\alpha=-ic/2\) for sine and \(\alpha=c/2\) for cosine.

The actual NF443 source transfer uses exactly

\[
T_m^{f,k}=2\mathrm{Re}\left[
\alpha e^{\lambda B}
\sum_{j=0}^{k}
\frac{\binom{k}{j}j!B^{k-j}/2^j}
{(a_m-\lambda/2)^{j+1}}\right].
\]

This equals the Laplace integral of the *same original entire generator* because

\[
\int_0^\infty e^{-a_m t}
 (B+t/2)^k e^{\lambda(B+t/2)}\,dt
=e^{\lambda B}\sum_{j=0}^k
\frac{\binom{k}{j}j!B^{k-j}}
{2^j(a_m-\lambda/2)^{j+1}}.
\]

The authentic odd sinh source mode with coefficient \(c_{\rm pole}\) is not omitted: for m≥1 its exact integral is

\[
\frac{c_{\rm pole}}2
\left(\frac{e^{B/2}}{m}
-\frac{e^{-B/2}}{m+1/2}\right),
\]

exactly the original native image formula. At m=0 the sinh contribution is at its true removable/pole interface and **must stay separately joined in the original transfer**; none of these Laplace formulas is asserted there.

Therefore, as **exact source-linear identities**, for all m≥1,

\[
\boxed{T_m=\int_0^\infty e^{-a_m t}U_{\rm ent}(B+t/2)\,dt}
\]

and

\[
\boxed{R_m=\int_0^\infty e^{-a_m t}
  [U_{\rm ent}(B+t/2)-u_4(B)]\,dt.}
\]

Integration by parts gives a source-correlated derivative expansion

\[
T_m=\sum_{j=0}^{K-1}\frac{u_4^{(j)}(B)}
{2^j a_m^{j+1}}
+\frac1{(2a_m)^K}\int_0^\infty e^{-a_m t}
U_{\rm ent}^{(K)}(B+t/2)\,dt.
\]

This identity is exact for each finite K and m≥1. **Do not discard or estimate the last integral from only six numerical derivatives at B**. NF445 replay checks all original polynomial orders k≤13 against formal Laplace coefficient expansions through r≤13 over exact rational arithmetic; the odd sinh denominators are checked separately. None of these are a finite numerical tail certificate yet.

## One correlated integral replaces the entire m≥1 infinite residual image family

Define

\[
K_1(s)=\sum_{m=1}^\infty e^{-(m+1/4)s}
=\frac{e^{-5s/4}}{1-e^{-s}}\quad(s>0).
\]

The full original residual image contribution (with the NF444 source-linear leading \(v/a_m\) already removed) has **exactly**

\[
\boxed{
I_R(x)=\frac12\int_0^\infty
[U_{\rm ent}(B+t/2)-v]
\{K_1(t+2(B-x))-K_1(t+2(B+x))\}\,dt,
}
\]

for the fixed source branch and real 0≤x≤B, plus the separately finite m=0 residual native term. This sum/integral exchange is valid: near t=0 and x=B, the source difference is \(O(t)\), while \(K_1(t)=O(1/t)\); their product remains bounded. As t→∞, \(U_{\rm ent}(B+t/2)\) grows at most polynomially times \(e^{t/4}\) because the highest original generator degree is 13 and the sinh term has exponent 1/4, while \(K_1(t)\) decays \(e^{-5t/4}\). Thus the integrand is absolutely integrable including x=B.

**Improvement over NF444:** There is no arbitrary image cutoff and no \(1/[1-e^{-2(B-x)}]\) loss in this *identity*. All 246 original source coefficients enter before any absolute-value charge. It provides a plausible path to an independent weighted near-B Arb integral with whole-source error control.

**Important limitation:** This is a new **representation**, not an evaluated numerical bound. The source extension outside B can attain enormous values, and the full digamma/archimedean central contribution may cancel the image response. Moving the same large cancellation inside an integral does not automatically make rigorous numerical quadrature stable or yield a signed result.

## Genuine 4096-bit source-native evidence

The focused native calculation uses all original 242 selected+4 critical dyadic coefficients, all 32 source sines, 273 frequency/order groups, the identical original NF407 4096-bit source SHA256 \`0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce\` and NF406 seam SHA256 \`c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675\`. The original \(v=u_4(B)\) matches an **independent** evaluation using the existing source-native \(U\) evaluator and the original NF407 principal endpoint interval.

Rigorously enclosed source-correlated endpoint derivative midpoints (not substitutes for uniform derivative bounds):

| \(j\) | Original \(u_4^{(j)}(B)\) approx |
|---|---:|
| 0 | \(-1.1679864490968300\times10^{-11}\) |
| 1 | \(-1.3009713780539214\times10^{-7}\) |
| 2 | \(-2.832884296086389\times10^{-4}\) |
| 3 | \(-2.560062205184645\) |
| 4 | \(-1.722716415115091\times10^{4}\) |
| 5 | \(-9.301604045987576\times10^{7}\) |

Each native image coefficient and residual is an Arb ball with relative width below \(10^{-40}\). Exact outward rational interval endpoints, not these rounded display values, are archived in the GitHub Actions JSON.

| Image \(m\) | Genuine original \(T_m\), approx | Source-correlated \(R_m=T_m-v/a_m\), approx |
|---|---:|---:|
| 1 | \(-3.200641935054197\times10^{139}\) | nearly the same |
| 128 | \(-5.2366179683731215\times10^{25}\) | nearly the same |
| 256 | \(-2.417117643909355\times10^{7}\) | nearly the same |
| 512 | \(-3.041173333414664\times10^{-4}\) | \(-3.041173333186653\times10^{-4}\) |
| 1024 | \(-3.853564723407691\times10^{-10}\) | \(-3.853450690071191\times10^{-10}\) |
| 2048 | \(-2.938597435004671\times10^{-13}\) | \(-2.881573807561886\times10^{-13}\) |
| 4096 | \(-1.104049628670883\times10^{-14}\) | \(-8.189140902889897\times10^{-15}\) |
| 8192 | \(-2.6370311337991285\times10^{-15}\) | \(-1.2113099349870437\times10^{-15}\) |

The other sampled indices 2,4,8,16,32,64 are also in the original numerical artifact; all were certified but cannot substitute for every m. The **enormous low-index coefficients are genuine at the source level**, not a rounding malfunction. They show that merely making \(R_m\) correlated in source amplitudes is insufficient: cancellation with the original **central digamma/archimedean response** may also need to be preserved before quantitative near-B integration. At high m, \(a_m^2R_m\) starts approaching \(u_4'(B)/2\approx-6.50\times10^{-8}\), but a finite sample and formal asymptotic identity do not establish a uniform error at m≥8192.

[Focussed NF445 source-native CI #41387332302 — SUCCESS](https://github.com/monocap-tech/weil-lab/actions/runs/41387332302) independently verifies 4096-bit original U(B) overlap, all six derivative intervals, all 14 genuine T_m/R_m coefficient intervals, complete formal Laplace coefficient identities up to polynomial order 13, and original J7/J8/global status STOP. Original final native JSON SHA256 \`edfd1f0d2ae7c55aeb042b153a12ef2d8842553e09bf4f5078eb387a748ad7ba\`, source artifact #13115608336 ZIP digest \`c62a688929b4cabd4bf375307c6f964cb617bc64a3f246ce9653f46305e710af\`. Full original exact intervals retained until January 31, 2027. Permanent [NF445 digest/obligation custody](../data/provisional/NF445_original_correlated_residual_laplace_custody_index.json). Full raw JSON permanent repo archival DUE.

## Status and next NF446

**Accepted:** exact original generator-correlated Laplace identity of the whole m≥1 residual; exact resummed \(K_1\) single-integral architecture with removable x=B integrand; exact original polynomial and sinh verification; actual original source 4096-bit endpoint derivatives and 14 T_m/R_m interval observations.

**Not accepted:** any decision-quality *all-index* residual bound, any rigorous numerical value of the full \(I_R(x)\) across the endpoint collar, cancellation against central digamma, true signed J7/J8 integrals, original complete NF410/NF404 global signed scalar, principal E_p, original fourth J242 exterior upper, W-ODD-NEG, full even/whole Weil, operator domain and RH. Original signed physical cells remain **six/eight** (J1/J2/J3 positive; J4/J5/J6 negative).

**Next bold — NF446:** Preserve the *joint original digamma–image–physical-prime* source correlation, rather than attempting to bound the now-observed enormous low-m residual image family independently. Derive a finite-interval or weighted-kernel integral that pairs the universal \(K_1\) source carrier against the authentic NF424 digamma response, source subtraction at B and true J7/J8 prime routing. Demand an actual narrow continuous source enclosure or prove a quantitative information limit. No automatic increase in Chebyshev degree, images or Taylor jets. No main merge.
