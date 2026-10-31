# NF415 — Original cell-6 I1 source-correlated analytic Taylor integration; pointwise tiny-t theorem

**2026-10-31 PT. Canonical W-ODD-NEG, unchanged NF370 u4; NF407 native 242 selected + four critical; NF404 center and seven signed prime powers unchanged.**

## Previous / current / next

**NF413:** A complete original 246-source analytic 4096-bit physical curvature Gram certifies ||u4''||L2(-B,B)<256. The small-t contribution was certified in L2 only.

**NF414:** Original source-native 4096-bit finite regularized arch and all true signed seven-prime continuous remainders on genuine original physical hotspot cells 3,6,7 at rational x=7/20,9/10,26/25; source coefficients and branch conditions rigorously paid. The actual I0, I1 and full z(x) were not integrated.

**NF415 accepted analytic:** Let d=B-x and t1=2d. Original near-zero I0 has D_tu4(x)=u4(x)-[u4(x+t/2)+u4(x-t/2)]/2. The exact triangular kernel and Cauchy–Schwarz on the same support yield

|D_t u4(x)| ≤ t^(3/2)/(4√3) ||u4''||L2(-B,B),

and K(t)=exp(-t/4)/(1-exp(-t))<2/t gives

|∫_0^min(h,t1) K(t) D_tu4(x)dt| < 256 h^(3/2)/(3√3)<50 h^(3/2),

using exact integer test 256²=65536<67500=3*(3*50)². With h=10^-12, the original I0 tiny-t contribution is pointwise <5e-17 uniformly in x∈(0,B). This is NOT a claim that the rest of I0, I1, or z is certified.

## First ACb native diagnostic: exact method stop

The original I1 at x=9/10 (physical cell 6) runs over exact t∈[2/5,4]:

I1(9/10)=1/2∫_(2/5)^4 K(t)[u4(9/10)-u4(9/10-t/2)]dt.

Native FLINT acb.integral directly applied to the entire exact dyadic 242+4 source returned a FINITE but UNRESOLVED ball of order ±2.18×10^142; original source cancellation was lost on complex validation boxes. Correct focused #41227573428 SUCCESS **as a typed method STOP**; detailed receipt notes/data/provisional/NF415_original_cell6_I1_validated_acb.json. The passing workflow explicitly requires width <1e-13 to accept the I1 enclosure and did not promote it. Earlier failed workflow attempts were native-script argparse errors, not mathematical successes. Increasing Gauss nodes/precision without changing interval dependency does not solve the cancellation problem.

## New original source-correlated analytic Taylor method (pending focused native acceptance)

To avoid this exact dependency trap, the new script forms the complete 242+4 original source as exactly dyadic merged rational physical polynomial-trig coefficients by frequency/degree and odd sinh pole. It computes the *entire source Taylor jet at each rational panel center*, combining all frequency families and all original selected/critical source correlations BEFORE integrating, rather than asking an interval evaluator to box an enormous raw expression.

We fix x=9/10, original I1 limits [2/5,4], and subdivide into 360 exact rational panels of width 1/100, centers t_j=2/5+(2j+1)/200, half-width ρ_t=1/200. The original physical source argument s=x-t/2 has exact center s_j=x-t_j/2 and half-width ρ_s=1/400.

For original source
u4(s)=Σ_(f,k) a_(f,k)s^k φ_k(2π f s)+b sinh(s/2),
φ_even=sin, φ_odd=cos,

use the exact identity
u4(s)=Im[Σ_f (Σ_k a_(f,k) i^(k mod2) s^k) exp(i2π f s)]+b sinh(s/2).

Expand the full source around each real rational s_j to Taylor degree N_s=160, by exactly rational polynomial shift/binomials, outward 1024-bit Arb/acb frequency exponentials and the explicit entire exponential Taylor recurrence. Both original selected and critical coefficients enter every coefficient of this complete source jet. The original translated source u4(x-t/2) is then the same polynomial with Taylor coefficient n multiplied by (-1/2)^n; the original u4(x) constant is also source correlated.

Expand K(t)=exp(-t/4)/(1-exp(-t)) independently around t_j using an exact exponential series quotient recurrence to Taylor degree N_K=48. Integrate the complete *product polynomial* exactly over each symmetric rational panel; odd powers integrate to zero and even powers have exact weights 2ρ_t^(n+1)/(n+1). All numerical polynomial coefficients are outward Arb, never unverified Gauss weights.

### Fully explicit analytic uniform remainder

For every original physical generator, k≤13, |s_j|+ρ_s≤B. The original max frequency obeys 2π|f|ρ_s<7|f|ρ_s<2. Let the source-exact rational coefficient triangle Uraw=Σ_(f,k)|a_(f,k)|B^k+|b|, checked against Uraw<10^160. For the complete Taylor source remainder, on each real panel,

R_source ≤ 8 Uraw * 2^(N_s-13+1)/(N_s-13+1)!
        = 8 Uraw * 2^148/148! <1e-42

(the numeric inequality is enforced by exact Fraction on native execution). The same very generous bound includes the odd sinh pole Taylor tail. The source is huge in raw coordinates, but the degree-160 local remainder kills that scale factorially; the actual polynomial coefficients themselves keep every source correlation.

For the kernel on any complex disk |t-t_j|≤R_j=t_j/2, Re(t)≥t_j/2≥1/5. Thus |K(t)|≤6 (since |e^-t|≤e^-1/5≤5/6), while |δt|/R_j≤1/40. By Cauchy, its degree-48 Taylor remainder on each real panel is

R_K < 7 / 40^49 < 1e-70.

Original NF413 curvature plus NF411 |u4(B)|<1e-9 and |u4'(B)|<1e-6 yield |u4(s)|<513 throughout [-B,B] by the endpoint integral formula and sqrt((2B)^3/3)<2. Hence |D(t)|=|(u4(x)-u4(x-t/2))/2|<520. Also 0<K(t)<2/t≤5 on entire true I1 interval [2/5,4]. A fully rational error for EACH panel is bounded by

width*( (5/2)*R_source + R_K*(520+R_source/2) ).

Sum over all 360 panels (total length 18/5). Original native coefficient uncertainty is charged separately as <5*S0 for I1, since every physical u4 value error ≤S0 and ∫_(2/5)^4 K(t)dt<2ln10<5.

The final result can be accepted only if the outward native source-correlated panel sum plus both exact analytic remainders and native coefficient radius produces a width <1e-12. A CPU SUCCESS or a midpoint integral is not itself the acceptance condition.

## Status and stopping point

- **ACCEPTED analytic:** pointwise original t<h error <50h^(3/2), so <5e-17 at h=10^-12.
- **ACCEPTED method STOP:** naïve complex-ball direct I1 of full raw 246-source is unresolving despite a finite ball. Its bound has width order 1e142; prior run #41227573428 valid only as source-scope diagnostic.
- **New correlated Taylor original I1:** full original source code/workflow and explicit rational error contract attached; actual native producer/CI must succeed before numerical I1 certificate is accepted.
- **OPEN:** remaining original I0 above h, original I1 in cells 3,7, complete z at ANY hotspot point or on any cell, signed NF410 z/p cross, full NF404 centered scalar C, original fourth J242-perp, operator domain/inverse, W-ODD-NEG, even/whole Weil/RH.

No new source family, signed cells, historical overwrite, main merge or RH claim.

Code: scripts/local_replay/nf415_original_cell6_I1_correlated_taylor_native.py
Focused CI: .github/workflows/nf415-original-correlated-taylor-I1.yml
Expected accepted receipt only if successful: notes/data/provisional/NF415_original_cell6_I1_correlated_taylor_native.json
