# RPB108 NF10 — Fresh original physical infinite-complement certificate at a=53/50

Date 2026-10-08. Independent research branch research/rpb108-phase-geometry-localization. Parent NF9/IP9, active Coupled CC38 read-only; Global NF71 and Pre-Contact Shadow PS3 remain paused. This note is a **new complete physical-complement estimate for the original actual Weil form**, not whole-domain positivity at a=53/50. The entire retained 112-vector native matrix, full source Gram, and corrected even/odd Schur signs still need independent construction.

## Result

Set a=53/50 and let E112 be the span of the first 112 normalized physical Legendre modes in L2(-a,a). On its physical orthogonal complement F112, the complete ORIGINAL unshifted native Weil quadratic form, with the actual prime powers 2,3,4,5,7,8 and both signed pole orientations, has the fresh certified lower bound

\[
\boxed{Q_a(h)\ge \frac{17}{100}\,\|h\|_{L^2(-a,a)}^2
\qquad(h\perp_{L^2}E_{112}\text{ in the canonical supported form domain}).}
\]

The strict unrounded lower was >0.172351243732, and 17/100 is rounded down with a genuine rational margin. It does NOT reuse CC18's c=699/1000: that value was valid at a=21/20, not a=53/50.

This is a positivity result on the infinite codimension-112 physical complement only. No positivity is claimed for the full original domain, the first 112 retained modes, their mixed coupling, or the new aperture overall.

## 1. New complete six-prime weighted Schur bound

The original physical prime translation operator is the selfadjoint finite sum

\[
{\cal P}_a f(x)=
 \sum_{n\in\{2,3,4,5,7,8\}}
 \frac{\Lambda(n)}{\sqrt n}\,[f(x+\log n)+f(x-\log n)],
\]

with zero extension outside [-a,a]. For a=53/50 define the strictly positive even rational weight

\[
w(x)=\frac58+\frac38(x/a)^2.
\]

Using the Schur test on the positive symmetric absolute-translation kernel, it is enough to enclose, for EVERY x in [-a,a],

\[
\frac{\sum_n \frac{\Lambda(n)}{\sqrt n}
     [1_{|x+\log n|<a}w(x+\log n)+1_{|x-\log n|<a}w(x-\log n)]}{w(x)}.
\]

A new complete exact-rational physical-cell cover partitions [-a,a] into 6000 closed cells and applies rigorous atanh logarithm intervals, rational square-root lower bounds, interval lower w(x) and interval upper translated w(y). Every cell that intersects a prime support boundary **includes** the potentially active shift. This covers BOTH orientations of ALL six original prime powers; no endpoint interpolation or floating sample is used as a proof premise.

The maximum certified upper endpoint on the first cover is <2.565346230069. A separate non-nested 6133-cell cover gives <2.565401883261. Both independently pass the stricter check <257/100, hence the convenient unconditional original operator estimate

\[
\boxed{\|{\cal P}_a\|_{L^2\to L^2}<\frac{13}{5}=2.6.}
\tag{NF10.1}
\]

This is an absolute prime-operator norm bound used ONLY for the complement lower. It is not a defect-relative arithmetic correlation estimate.

## 2. Repaired depth-6 high-frequency Bessel mass at a=1.06

The original CC18 complement used Legendre degrees >=112, and cutoffs 15,16,17. The latter fails its positive-region condition at 53/50: (2a pi 17)^2>112*113. Instead choose the independently checked cutoff triplet

\[
\boxed{T_0=14,\quad T_1=15,\quad T_2=16.}
\]

The upper cutoff satisfies (2a pi 16)^2<112*113 using an exact Machin/atan interval for pi. The existing proved degree-n Bessel logarithmic-derivative comparison is applied in the same analytic scope as the old prime-8 preflight. NF10 reconstructs its six-iteration derivative coefficients independently:

\[
c_0(n)=\frac1{2n+3},\qquad
c_j^{(r+1)}(n)=
  \frac{\sum_{p+q=j-1}c_p^{(r)}(n)c_q^{(r)}(n)}
       {2n+2j+3}\quad (j\ge1),
\]

with the precise finite convolution/denominator implementation in the producer. Every coefficient is positive and decreases when n increases, by induction on the positive rational recurrence. Hence the complete rate denominator for all n>=112 and T<=16 can be bounded below using n=112 and T=16. The exact finite 64-coefficient audit gives

\[
\operatorname{rate}_{112,16}>80,\qquad
\operatorname{rate}_{n,T}>75
\quad(n\ge112,\ T\le16).
\]

The producer uses **75** conservatively in all 48 individually enclosed degrees 112 through 159. The damping exponent is bounded below by its first 12 positive terms with an outward rational rounding, and exp(exponent) is bounded below by 155 strictly positive Taylor terms. Every resulting mass term is rounded outward at 10^-18. The remaining degrees >=160 are controlled by the old rigorously valid undamped geometric Bessel tail, re-evaluated at a=53/50. This supplies the certified complete frequency-mass bounds:

| T | Upper bound on physical mass below T for the high Legendre complement |
| --- | ---: |
| 14 | 8.2489334 × 10^-10 |
| 15 | 3.185918500315 × 10^-6 |
| 16 | 0.001714180415762022 |

These are physical high-complement mass bounds, not zero-frequency counts and not truncated finite-source Gram entries.

## 3. Complete native archimedean plus signed-pole margin

Reapply the original rigorous high-frequency archimedean lower multiplier

\[
b(T)=\log T-\frac{7}{216T^2},
\]

and the inherited low-band native absolute loss 27/5, with exact interval arithmetic:

\[
\begin{aligned}
\mathrm{Arch}_a \ge
&\ b(16)_{\rm lower}
-[b(14)_{\rm upper}+27/5]\,\rho_{14}\\
&-[b(15)_{\rm upper}-b(14)_{\rm lower}]\,\rho_{15}\\
&-[b(16)_{\rm upper}-b(15)_{\rm lower}]\,\rho_{16}.
\end{aligned}
\]

All coefficients multiplying positive mass uppers are rounded in the safe direction. The result is

\[
\boxed{\mathrm{Arch}_a>2.772351243732>277/100.}
\tag{NF10.2}
\]

For degree cutoff k=112 the original **two-cross-pole** absolute bound remains

\[
\mathrm{Pole}_a\le
 16a\frac{(a/2)^{224}}{(112!)^2},
\]

which is extraordinarily small and is paid positively rather than changing its original signed conventions.

Subtract the FULL original prime norm upper and the exact signed-pole absolute allowance from the archimedean lower:

\[
\boxed{
Q_a|_{F112}\succeq
  (\mathrm{Arch}_a-\|{\cal P}_a\|-\mathrm{Pole}_a)I
  >0.172351243732\,I
  >\frac{17}{100}I.
}
\tag{NF10.3}
\]

Thus the desired positive physical complement at 53/50 is certified as a distinct new target result.

## 4. Validation and precise remaining work

- [Fresh NF10 producer](../scripts/certify_native_prime8_complement_nf10_106.py): fully self-contained exact rational prime covering, Machin pi bounds, sixfold Bessel coefficient recursion, all 48 masses, geometric tail, archimedean margin and complete pole payment.
- [Independent NF10 consumer](../scripts/validate_native_prime8_complement_nf10_106.py): separate 6133-cell prime cover, coefficient monotonicity across degrees 112..159, three target cutoffs, and replay of the 17/100 physical margin.
- [Compact manifest](data/RPB108_NF10_COMPLEMENT106_CERTIFICATE_20261008.json): separately rounded rational upper and lower endpoints. The finite checks were executed on the local mathematical implementation. No claim is made that the GitHub code was executed in a CI runner, and no Lean proof is present.

The physical complement constant from NF10 is smaller than CC18's old c=699/1000. A smaller c makes the inverse reaction allowance larger. Therefore NF10's successful complement certificate does **not** guarantee that the inherited 112-vector finite retained sign will close at 53/50; in particular the target weak odd/even chart could require a sharper complement bound, better source cancellation, or a redesigned retained space.

**NF11 gate:** Rebuild the complete target-specific native retained 112-vector matrix at 53/50 and independently evaluate signed finite trials. Then reconstruct corrected source/action Grams for the even and odd weak charts, with all true source errors and c>=17/100 paid. If the conservative Schur signs fail, treat this as an inconclusive certificate, not actual Weil negativity. A fresh stronger complement estimate may be essential for numerical closure.

**Standing:** This is new certified source-level positivity only on F112 at a=53/50. The highest whole-domain certified aperture remains a=21/20 (CC18). CC38 remains active Coupled analytic source, Global NF71 and Pre-Contact Shadow PS3 paused; non-stalling, RH/F4/full transport and Lean closure remain open.
