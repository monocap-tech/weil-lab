## Verified MG33 outcome — independent complete-frequency calculation

[Actions #39462301107](https://github.com/monocap-tech/weil-lab/actions/runs/39462301107) **PASSED** original true-source disjoint [0,4]/[4,8]/MG19 nonflat-source integrals, strict exact MG32 accepted baseline replay, the complete actual-source remainder bound and all independent no-promotion checks. The archived artifact is `mg33-original-disjoint-24D-joint-residual` ID `12284751583`, run head SHA `5cf18bd74f409d533ae9efa1f7af25d0e272ff21`.

**Only two of the original MG19 selected true nonflat panels** are >=8 and disjoint from the contiguous [0,8] band; the other 22 were rejected from extra coverage rather than double counted.

| Original cutoff | Rational trial | Original MG32 [0,4] total Rupper trace | MG33 [0,8] total | MG33 [0,8]+2 MG19 panels total | MG32 strict Gersh margin | MG33 hybrid Gersh margin |
|---|---|---:|---:|---:|---:|---:|
| 2^12 | scalar MG24 tI | 63.50474075 | 69.23276102 | 69.22139990 | -18.73756242 | -19.31983352 |
| 2^12 | nonscalar ridge | 69.62469569 | 75.61569860 | 75.59910283 | -23.06170028 | -23.37677764 |
| 2^16 | scalar MG24 tI | 63.50474524 | 69.23276596 | 69.22140483 | -18.73756206 | -19.31983327 |
| 2^16 | nonscalar ridge | 69.57093939 | 75.53990670 | 75.52307486 | -23.02927719 | -23.34535725 |

The new 32-cell positive band [4,8] has **worsened the complete-frequency upper trace** by approx. 5.73 in the original scalar case. Its conservative *complement upper trace also increases*: from 37.95740245 ([0,4] baseline) to 38.65965555 ([0,8]), even though the actual unmeasured original frequency set became strictly smaller. This is NOT a paradox: `Hmeasured_lower` may have large negative Loewner directions from MG15 sourcewise-Young error charges; subtracting that nonpositive lower estimate can increase the conservative complement upper. The actual source frequency mass on any physical band remains PSD. It also shows why adding more measured frequencies need NOT monotonically tighten a certificate.

Adding just the two extra MG19 sites to [0,8] slightly decreases its total scalar upper trace (~0.01136), yet the full Gershgorin margin deteriorates by another ~0.00013. Hence better upper TRACE != better source residual positivity in the original source coordinates.

**MG33 method disposition: VERIFIED NO-GO** for naive extra lowband coverage under the existing sourcewise affine Young H_lower + broad remaining physical source mass. No tested combination certifies a positive 24D source residual margin, let alone a 470D strong inverse or signed 51/56 cap.

**Next MG34 acceptance:** decompose exact marginal direct-band cost, change in omitted-frequency upper cost, and change in spectral Gershgorin margin on the SAME B; test PSD-safe mass crediting (never give negative source mass credit) before extending additional bands. Consider direct joint remainder covariance or source-specific certified PSD lower mass. Do not infer a negative direction of the true operator from the negative Gershgorin acceptance margins.

Canonical W-ODD-NEG, all-470 original strong inverse, signed odd 51/56 cap, independently audited Fourier/form-domain identification, even/Weil/CC27/RH remain **OPEN**.

---

# MG33 — Original disjoint joint Fourier residual across true frequency sectors

October 20, 2026, scoped and stacked on [MG32 PR #281](https://github.com/monocap-tech/weil-lab/pull/281). MG32 accepted the genuine original 24D joint Fourier residual formula and a direct covariance upper on positive [0,4], but with its coarse unmeasured-frequency complement yielded **no certified original source contraction**, and full-frequency upper trace 63.5–69.6. Approx. 60% of the scalar certified upper trace came from all omitted frequencies. MG31 previously proved 36/36 NEGATIVE rational Rayleigh witnesses for the prior *lower certificate matrices*, not the actual operator.

## Scope of true original source

Maintain precisely the original SI10 25 physical generator catalog, MG11 23 dual-boundary-adapted generators and one actual odd sinh pole (24D), the SM43 exact original signed digamma + seven-prime positive Fourier multiplier, the original true physical Gram, the complete rank-one pole coefficient interval b, and the existing SM41 high-frequency strong source tails.

The true original joint residual is

```
R=F-Astar F B,
r(xi)=t(xi)[I-a_o(xi)B+2e_p b^T B].
```

The Fourier integral includes both frequency signs with existing factor 2. Each new cell directly encloses the 24-dimensional **whole r(xi)** before squaring. This retains the true F / Ao FB / sinh-pole compensation terms within the measured band, rather than independently estimating H, G, S before forming their difference.

## Disjoint original frequency sectors and no double count

1. **Recompute accepted MG32 [0,4] baseline**, using its original 32 equal rational cells. Exact equality of the original 24D source-radius L1 sum to separately accepted MG29 Actions #39440914565 and original joint residual prefix/complement output to MG32 Actions #39459624082 is a hard acceptance gate.
2. Add contiguous [4,8] in **32 new rational cells**, with the same true original MG29 direct adapted third/Fourier fourth-derivative remainder and actual original signed whole-cell multiplier interval. This adds genuine full-source measured spectral mass.
3. Load the exact **24 original MG19 accepted selected nonflat frequency cells** from Actions #39363425186. Retain only cells with `left>=8`, disjoint from the measured [0,8] contiguous band. All such cells are in strictly increasing order with no overlap; cells with left below 8 are **not** claimed as new coverage. Re-evaluate their genuine original MG29 Fourier source intervals and directly measured joint residual covariance, rather than misusing their prior moment lower bounds as residual enclosures.

The resulting measured set `C=[0,8] union selected_MG19_above8` is a rigorously known union of pairwise disjoint positive-frequency intervals, together with the negative-frequency mirror.

## Entire-original-frequency closure

For each measured set `C`, the *actual physical source mass* satisfies
```
H=H_C+H_R, 0<=H_R<=Hup-HClo,
```
with `HClo` the SUM of independent, true, same-basis source mass Loewner lowers on disjoint [0,4], [4,8], and the selected MG19 cells. The remainder still includes all other real frequencies. The existing SM41 source high tail and global multiplier M_k bound yield
```
S_R <= M_k² (Hup-HClo) + tau2(k)I,
```
with exact original pole coefficient interval and all its uncertainty fees charged by the accepted MG32 nested Young source-residual upper. Nothing outside C is dropped, and no MG19 source moment matrix is copied into a logically unrelated residual quadratic.

Three complete-original-frequency candidates are independently valid for each rational B: (i) exact MG32 [0,4] baseline, (ii) measured contiguous [0,8], (iii) disjoint hybrid including accepted original MG19 sites above8. Retain the same original MG30 rational scalar and nonscalar B selected in MG32, cutoffs k=12,16.

**Report** separately: measured original residual covariance upper traces per sector, unmeasured original residual upper trace, total original source R*R upper trace, and the **strict Gershgorin lower margin** of `Hlo-Rupper`. A narrower upper trace than baseline is NOT a Loewner dominance claim; an original source contraction is accepted ONLY when that exact full-matrix lower margin is strictly positive. Even a positive 24D source residual is not a full 470D inverse because finite source invariance/complete odd complement are unproved.

## Gate and next obligation

- MG33 first Actions must independently confirm all original artifact IDs, exact MG32 original baseline reproduction, no-overlap of original source frequency cells, exact full-source Fourier/pole/multiplier Taylor enclosures, and whole-real-frequency complement.
- If new full-frequency residual margins are still nonpositive, compare *source mass gain* versus newly added **joint measured-band residual uncertainty**, rather than adding high-frequency cells indiscriminately.
- Canonical W-ODD-NEG, original all-470 inverse, signed odd 51/56 cap, original Fourier/form-domain identification, complete odd/even/Weil/CC27/RH all **OPEN**.

**Actions acceptance: PASSED; method no-go for tested bands.**
