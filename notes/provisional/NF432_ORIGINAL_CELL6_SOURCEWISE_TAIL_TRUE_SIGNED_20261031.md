# Weil-Lab NF432 — Original source-specific Chebyshev tail closes the original cell-6 continuous-response gap

**2026-10-31 PT.** Canonical `W-ODD-NEG` and RH OPEN. Stacked on [NF431 PR #440](https://github.com/monocap-tech/weil-lab/pull/440) with **original unchanged NF407 242 selected + four critical 4096-bit source** and exact original NF406 irrational physical prime seams, NF404 dyadic center, NF424 digamma+2048 per-side endpoint images, NF428 signed p moments and NF429 raw dx moments. No source swap, no main merge.

## Previous cursor / current circle / next

**Previous NF431:** 512 independently source-native Chebyshev series coefficient interval balls `a0..a511` certified, uniform full true original J6 response tail *unquantified*. Its exact original P511 finite-polynomial signed nonprincipal `4 ∫pP511+2∫P511²` is strictly negative, approximately `-4.239452110857815316795470074e-22`, but is **not** by itself the original continuous z integral. NF430 requires 1265 modes under the overly coarse common source triangle; 753 modes uncomputed.

**Current NF432:** Rather than certify 753 extra modes, exploit the actual NF407 frequency/order distribution. For each original merged source generator `(f,k,c)`, including exactly reconstructed four critical sources, use its **OWN** frequency `f`, polynomial order `k`, exact dyadic coefficient `c`, and choose the best rigorous Bernstein ellipse in `rho∈{2,3,4,5}`. Each ellipse separately encloses the same original fixed cell6 analytic branch; termwise Chebyshev coefficient tails can be summed at real `t∈[-1,1]`. Keep original physical restriction `J6=(log7-B,log8-B)`, B=11/10, five original signed post-seam prime powers 2,3,4,5,7; n8/n9 remain neither.

## Source-specific rigorous analytic envelope (not extrapolated observations)

Coordinates `x=C+Ht`, C=91/100, H=7/100. For every `rho∈{2,3,4,5}`, on Bernstein `E_rho`:

```
|Im x| ≤ v_rho = (7/100)*(rho-rho^-1)/2
Re x ≤ C+(7/100)*(rho+rho^-1)/2 ≤ 273/250=1.092 < B
Re(B-x) ≥ 1/125 >0.
```

The 2048-image original exponential source evaluator `G_2048(x,lambda)` is holomorphic for source frequencies on `|lambda-2*pi*i*f|≤1/8` and their original conjugates: the original digamma arguments have `Re(1/4±lambda/2)≥3/16`, original complete digamma source bound `|psi|<64000`; both geometric endpoint image families converge with factor `1+1/(2 delta)<64`, the original `lambda` disk edge `e^(B/8)<3`, and the unchanged source imaging denominator lower `3/16`. Direct triangle gives `|G_2048(x,lambda)|<10^6 exp(E(f,rho))` with

```
E(f,rho)=(2*(22/7)*f+1/8)*v_rho+1.
```

No round-off and no observed coefficient size is invoked. The radius1/8 Cauchy estimate gives the ORIGINAL `y^k sin/cos` generator arch transfer `|∂^k_lambda G|≤10^6 k!8^k exp(E)`. The original five signed post-seam `u4(x-log n)` translations obey `|x-log n|<3B`; their genuine positive Mangoldt weights sum `W<3`. After both ±frequency/conjugate-source branches, the combined ORIGINAL arch plus all five original signed prime translates for that generator is bounded on its ellipse by

```
M_(f,k,rho) <= 4*10^6 * abs(c) * k! * 8^k * exp(E(f,rho)).
```

The exact Chebyshev series bound `|a_n|≤2 M rho^-n` gives full **source generator** high-mode tail from n512:

```
tail_(f,k,rho) ≤ 16*10^6 * abs(c) * k!8^k
                  * 3^ceil(E(f,rho)) / rho^512
```

because `e<3` and `2/(1-rho^-1)≤4`. The code computes this bound with exact `Fraction` on the actual NF407 4096-bit dyadics and minimizes **per generator** across four independent ellipses before summing all merged source generators. Crucially it does NOT put the low-frequency extremely large source coefficients under the high-frequency exponential worst case. The exact `rho` selection applies to each additive analytic generator, so it preserves all original correlations rather than requiring coefficient-by-coefficient physical integration.

## Original pole, endpoint log and source uncertainty remain charged

The odd original `sinh(y/2)` source has `lambda=±1/2`. Its apparent `m0` digamma-image singularity is removable jointly; at `beta=0`, `psi(1+beta)+(exp(-2 beta d)-1)/beta` equals `psi(1)-2d`, with the remaining image sums bounded normally for `rho≤5`. Hence the complete odd-pole source response is holomorphic and uniformly <`10^6` times the original pole coefficient on `E5`. Include all five original prime shifts and the NF404 centered `sinh(x/2)` in a deliberately generous `4*10^7*(|pole|+2)/5^512` high-mode charge. Inherited original real endpoint coefficient `u4(B)` obeys the original exact raw source triangle <`10^160`, and the endpoint logarithmic Chebyshev parameter `q<1/5`, giving `raw*(1/5)^512/[512*(1-1/5)]`; constant `-u4(B)*W` gives NO high modes.

The original NF424 *real physical* J6 midpoint model error is retained independently, never transferred unsafely to a complex ellipse:

```
e_image = (36/2000)*10^160*(3/8)^480,
e_source = (10^12+20)*S0, S0<10^-700.
```

Thus `epsilon = exact_sum_min_source_tails + pole_tail + log_tail + e_image + e_source` rigorously bounds the true original physical continuous response against **the source-midpoint model's degree511 Chebyshev polynomial** on every x∈J6. Original NF428/NF431 outward coefficient balls enclose those midpoint-model coefficients and separately propagate their interval uncertainty into the polynomial signed-contraction receipts. They must not be silently dropped or double-claimed. No physical source evaluation at unverified centers is necessary.

## Actual numerical certificate and full original signed integral gate

Focused source-exact original [Actions #41252454230 SUCCESS](https://github.com/monocap-tech/weil-lab/actions/runs/41252454230) certifies the entire original frequency-wise series tail, with `epsilon≈6.687867e-23<1e-20` and exact rational output. Source-count 246 and source-frequency/order groups 273; selected ellipse counts: rho2=4, rho3=3, rho4=5, rho5=261. Source-frequency tail dominates, original pole/endpoint log residuals individually negligible but explicitly charged. The source calculation is a genuine whole-cell uniform analytic error certificate, **not** just numerical decay evidence. Artifact #13062275169, ZIP SHA256 b578ba350df704b48ebead950e3500be519acd1ae56b68134edca9e7c61ec3d6; generated JSON retention expiry 2027-01-29.

For full continuous signed acceptance (SEPARATE CI JOB, requiring the above), load immutable original NF428 low256 and signed p-moment, NF431 high256 and exact P511 signed receipt, NF429 all 2999 genuine dx Chebyshev moments, check their original NF407/NF406 SHA256, then use exact rational interval charges:

```
Pmax = sum_(n0..511) sup |a_n|,    m0 = ∫_J6 p(x) dx <0,
L = log(8/7).

|∫ p(z-P511)| <= epsilon*(-lower(m0)),
|∫(z²-P511²)| <= upper(L)*(2 epsilon*Pmax+epsilon²).

D_true = 4∫_J6 pz + 2∫_J6 z²
       ⊂ D_P511 +/- [4 epsilon*(-lower(m0))+
                      2 upper(L)*(2 epsilon*Pmax+epsilon²)].
```

The source P511 sign is negative. Promote true `D_true<0` ONLY if the new independently run and source-pinned exact Fraction signed upper <0. Source-tail PASS alone does **not** constitute signed cell acceptance.

**If sign passes:** closure of the original true continuous **cell-6 signed pz and z² integral only**, not of original global NF410/NF404 centered scalar (other seven cells plus principal/global terms), original fourth J242 exterior upper, W-ODD-NEG, even/whole Weil, infinite complement/domain/inverse, or RH. If it fails, retain only accepted sourcewise uniform tail and original P511 partial polynomial.

Source-exact tail validator: `scripts/local_replay/nf432_original_cell6_sourcewise_512_tail_exact.py`; true signed contraction: `scripts/local_replay/nf432_original_cell6_true_signed_from_P511_exact.py`; focused CI: `.github/workflows/nf432-original-cell6-sourcewise-tail.yml`. Retain original generated exact rational endpoints and artifact digests in custody after verification. No merge into main.


## Final original true J6 signed source-integral verification — ACCEPTED

**SUCCESS:** [Final focused two-job Actions #41252509627](https://github.com/monocap-tech/weil-lab/actions/runs/41252509627). Both the original source exact frequency-split complete Chebyshev high-mode tail and the separately artifact-SHA-pinned **true original physical cell6** pz/z² and signed contraction succeeded. All original NF407/NF406, NF404 pole-center, NF428/29/31 coefficient/moment source artifacts and original five post-seam/two neither prime flags rechecked. Original 512 accepted Chebyshev coefficient balls have the same old source, not newly substituted coefficients.

**Uniform true-z function tail:** exact rational original sourcewise plus pole/log plus source/image error `epsilon≈6.687866768763442757191439258369644e−23`, **strict <7e−23**, therefore <1e−20. Original 273 merged (f,k) groups choose independent rho2=4, rho3=3, rho4=5, rho5=261; no finite-mode extrapolation. A massive common `10^330` source upper has been replaced with truly source-varying exact input dyadics at each source frequency/degree.

**True continuous original cell-6 interval values:** all following displayed limits are conservative outward decimal brackets rounded from the exact rational interval endpoints; retained actual exact fraction balls are in CI artifact:

- Original `int_(J6) p(x) z(x) dx` lies in **[-282.72867005878475771818e−24, −282.72867005798736792259e−24]**.
- Original `int_(J6) z(x)^2 dx` lies in **[353.41066866265037184969e−24, 353.55880048511234775232e−24]**.
- Original complete true physical signed nonprincipal cell6 contribution `4int_(J6)pz + 2int_(J6)z²` lies in **[−424.09334290983828717334e−24, −423.79707926172477618576e−24]**. The **upper endpoint is rigorously <0**.

The exact signed high-mode error fee in the interval certificate is approx `1.48131824056755e−25`; the signed interval total width approx `2.96263648113511e−25`. The separate sourcewise pz fee and z² fee are both charged. The individual original `pz` and original `z²` integrals are accepted as true continuous object enclosures; their signed combination is also accepted.

**Artifact/verification custody:** Final source-tail JSON Actions artifact **#13061419183**, ZIP SHA256 `93786544bb3151ef6cb7984636fc34e7dfe610b8a4d01507324ecb5729f50380`, exact JSON SHA256 `8a1092cefad38cf6656cab5971f680a64abf24cb1b8b51e7185b8ca2ced631a4`. Final true signed original J6 JSON artifact **#13062040759**, ZIP SHA256 `118b70ded04aabe80935dd3a75cfc9c9054259ce04f29d87940d7254477ad052`, exact JSON SHA256 `79a7c5cae7ff5c74e68195b78d70bea92e80280a43ba15d255886a06c061e90c`. Artifacts expire 2027-01-29 absent separate permanent archival of raw generated full-fraction JSON. **Permanent compact source-hash, exact-proof-rule, and outward-rounded interval decision receipt:** `notes/data/provisional/NF432_original_true_cell6_signed_decision_custody_index.json`.

**NF432 closes:** genuine full continuous original positive support **cell 6** `pz`, `z²`, and `4pz+2z²` signed nonprincipal integral, with strictly negative certified upper, without remaining 753 coefficient evaluations. Prior original NF430 requirement of 1265 coefficient evaluations was a sufficient method-specific path, not a theorem-shaped necessity; the sourcewise tail supersedes its numerical dependency on cell6.

**NF432 does NOT close:** the **other SEVEN** original positive physical cells (3 and 7 prioritized, then remaining five), original full physical principal `E_p` plus 8-cell NF410/NF404 signed centered scalar threshold comparison, original fourth J242 exterior upper, W-ODD-NEG, even/whole Weil, infinite operator domain/inverse, RH. Cell 6 being a negative contribution does not by itself show that the total original signed quadratic is negative or that the Riemann Hypothesis follows. No main merge.

**Next NF433:** transfer the sourcewise, source-pinned and prime-branch-specific Chebyshev representation to original physical cells 3 and 7, preserving their own exact original NF406 seam branch selection and accepting them only after independent full true continuous signed pz/z² enclosures. Compare the 8-cell signed scalar against original NF404 cap only after ALL cells and global principal term are certified.
