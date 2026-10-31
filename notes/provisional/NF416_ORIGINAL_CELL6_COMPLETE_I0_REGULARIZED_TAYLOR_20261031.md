# NF416 VERIFIED ACCEPTANCE — first complete original z pointwise source enclosure

**Focused original native run [#41228999730](https://github.com/monocap-tech/weil-lab/actions/runs/41228999730) SUCCESS**, SHA-pinned source receipt `notes/data/provisional/NF416_original_cell6_full_I0_and_z_point_native.json`. It certifies the **entire** unchanged original 246-generator symmetric I0 at x=9/10, t∈[0,2/5], not merely the near-zero truncation. Original physically supported x-t/2 and x+t/2 branches both retained, and full original seven-prime NF414 and I1 NF415 parents are preserved.

The certified **complete** original cell-6 pointwise values (approximations of rigorous outward exact rational intervals) are:

```
I0(9/10) ≈ -0.294411377127259627297474239170374...
z(9/10)  ≈ +0.00000000004202421814328318159234807...
          ≈ +4.202421814328318159234807e-11
```

The true complete z pointwise interval width is **<10^-55** after all original source-native coefficients, tiny-t source/H tails, 38 rational regular-t source/K panels, and source second-derivative coefficient radii. It is strictly POSITIVE at this one x. This does **NOT** settle full original cell6, the other hotspot cells, signed p/z cross, centered original NF404 scalar, W-ODD-NEG or RH. The original NF415 partial z−I0 was not a complete z; NF416 now fills exactly its missing term.

Native source result uses x=9/10; tiny interval [0,1/50] via analytic H(t)=tK(t) and source Taylor degree530, remaining [1/50,2/5] via 38 exact rational panels and source degree300/K degree160, outward 1024bit Arb. The entire original NF407 highest selected frequency is accounted for and source coefficient errors are paid by the genuine second-derivative S2 rather than a divergent S0/t bound. Independently exact Fraction reread of these source/error receipts is separately tracked and must not be relabeled successful until its CI is checked.

**Next NF417:** Replicate this genuine complete source-correlated original z(x) pointwise enclosure on cells 3 and 7, then lift points to one-sided full-cell enclosures of z and the NF410 signed moments. NF404 C decision remains dependent on all eight physical original cells and signed cross and selected projection; no RH promotion.

---

# NF416 — Complete original cell-6 I0 by analytic removal of t=0 and 246-source correlated Taylor panels

**2026-10-31 PT — original NF370 fourth u4 unchanged, original 242 selected+4 critical source, B=11/10, seven signed real prime powers, NF404 centered pole. Canonical W-ODD-NEG and RH remain OPEN.**

## Previous cursor

NF413 source-native true ||u4''||L²(-B,B)<256. NF414 original cell-6 at x=9/10 finite arch + seven signed translated prime regularized terms exact. NF415 source-correlated original I1(9/10) for t∈[2/5,4] *certified* interval width <10^-70 and z(9/10)-I0(9/10) ∈[0.2944113771692838454407574207627221719871, 0.2944113771692838454407574207627221719872]. The remaining original I0 on [0,2/5] was OPEN.

## Current NF416 method — original complete I0

For original x=9/10, t1=2(B-x)=2/5, physical I0 is

I0(x)=∫_0^(2/5) K(t) {u4(x) - [u4(x+t/2)+u4(x-t/2)]/2}dt,
K(t)=e^(-t/4)/(1-e^(-t)).

At t=0, K(t) has a pole but the *original source-centered second difference* is O(t²). Replace K with H(t)/t, H(t)=t e^(-t/4)/(1-e^(-t)). H is analytic in |t|<2π and H(0)=1. This is an analytic removal of the only original t=0 singularity; do not sample or numerically truncate that singularity.

### First exact segment [0,1/50]

Compute the complete true NF407 source Taylor coefficients a_n = u4^(n)(x)/n! at the original rational x, combining ALL 242 selected polynomial-trigonometric generators, all four critical sine blocks, and the original odd pole *before* numerical integration. The symmetric original difference has the exact series

D_tu4(x) = -Σ_(even n>=2) a_n (t/2)^n.

Compute the exact rational Taylor coefficients h_j of H(t) about zero through degree 60 by formal series division of exp(-t/4) and (1−exp(-t))/t. Integrate every resulting polynomial term exactly on [0,1/50]:

I0^(tiny) ≈ -Σ_(n even>=2, j<=60) a_n h_j 2^(−n) τ^(n+j)/(n+j), τ=1/50,

with source degree 530. All source a_n are outward native Arb 1024-bit on the full original 246-source sum. No Gauss nodes.

For all actual original source frequencies f≤882.9140625, the translated source phase has |ω*t/2|<62 on 0≤t≤τ, and original polynomial degrees≤13. With source-exact raw triangle Uraw=Σ|a_(f,k)| B^k+|b|<10^160, an **exact Fraction** uniform tail is

R_s = 8*3^62*Uraw * 62^(530−13+1)/(530−13+1)! <10^-60.

The real t-dependent source tail vanishes at least like (t/τ)^531, so division by t at the removable endpoint is safe. On complex |t|≤1, |H(t)|<6: |exp(−t/4)|<3/2 and |(1−exp(−t))/t|>1/4 from e<11/4. The degree-60 H tail at t≤τ is R_H≤6τ^61/(1−τ)<10^-100. The original NF413 curvature bound implies |D_tu4(x)/t|<6 on 0≤t≤τ. Therefore an exact integrated tiny-segment error is

E_small=6 R_s/(531)+6 τ R_H <10^-60.

### Remaining exact original segment [1/50, 2/5]

This interval has no kernel pole. Partition into 38 exact rational panels of width 1/100 and half-width ρ_t=1/200. At each rational center t_j, form BOTH original source Taylor jets u4(x+t_j/2+δ/2) and u4(x−t_j/2−δ/2) with original full 242+4 source coefficients combined first. Preserve their original symmetric difference *before* multiplication by K; do not substitute the I1 one-sided difference.

Use source degree 300 and K centered Taylor degree 160. Integrate the product exactly by symmetric polynomial moment ∫_-ρ^ρ δ^n dδ=0 for odd n, 2ρ^(n+1)/(n+1) for even n. All coefficient calculations use native outward Arb 1024bit and all original source radii are paid separately.

On each original panel, 7|f|ρ_t/2<16 for every actual original frequency and degrees≤13, so

R_source ≤3^16 Uraw * 16^(300−13+1)/(300−13+1)! <10^-42.

For all t_j≥1/40 and complex |δ|≤t_j/2, Re(t_j+δ)≥1/80; |K|<81 and ρ/(t_j/2)≤2/5. Hence the degree-160 kernel Taylor tail is bounded exactly by

R_K ≤81 (2/5)^161/(1−2/5) <10^-60.

The original source has |u4|<513 throughout its physical support from NF411 endpoint value/slope and NF413 curvature, hence symmetric |D_tu4|<1030. Real K(t)<2/t≤100 for t≥1/50. A conservative integrated original large-panel error is

E_large=(2/5−1/50)[100 R_source +R_K(1030+R_source)] <10^-39.

Finally, unlike an invalid ∫S0/t charge, original native source-coefficient uncertainty is paid through the original full second-derivative uniform radius S2 from NF413:

|δD_t|≤S2*t²/8, so |δI0|≤S2*(2/5)^2/8.

All three error terms are **exact rational source-pinned and positive**. The entire original I0 is a single 1024-bit outward Arb sum of the integrated tiny and 38 regular panels plus these exact tails/radii. No original t integral is omitted.

## Acceptance / STOP contract

The focused native receipt may certify complete original I0(9/10) only if all real-source and exact-Fraction error bounds pass and the final outward rational interval width is <10^-12. The true complete original z(9/10) may then be enclosed by exact rational outward addition of three **independently source-radii-paid** originals: NF414 finite full signed source; NF415 I1; NF416 complete I0. This is a *single original physical point*, not a cell-sup enclosure or signed NF404 norm.

Accepted status requires inspection of the actual focused GitHub Actions run; a committed script or queued CI does not confer native mathematical acceptance.

**OPEN even if focused passes:** true continuous original z on entire original cell6 and other original physical cells 3,7, and remaining 5; NF410 signed z/p correlations, NF404 whole original centered scalar C, fourth J242 lowband/complement, original domain/inverse, W-ODD-NEG, even/whole Weil and RH. No source change, new signed cells, main merge or theorem promotion.

Script: scripts/local_replay/nf416_original_cell6_full_I0_regularized_taylor.py.
Workflow: .github/workflows/nf416-original-cell6-regularized-I0.yml.
Receipt on verified native success: notes/data/provisional/NF416_original_cell6_full_I0_and_z_point_native.json.
