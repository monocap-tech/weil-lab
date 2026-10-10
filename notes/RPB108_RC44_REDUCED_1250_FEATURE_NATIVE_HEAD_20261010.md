# RPB108 RC44 — reduce the sufficient native head to 1250 features

2026-10-10. Parent RC43: `905b3875822005bcc207361bffe4b41973c1df94`.
Only `research/rpb108-route-consolidation` is written.

## Result

The original-form sufficient Chebyshev head drops from 8600 to **1250
native features**, preserving the whole infinite complementary floor

    H A_Q H >=(247/2500)I_H > (1/11)I_H.

The sharper direct budget gives a floor greater than 0.099598. The original
conditional head floor 1/4000 and source cross norm 1/300 would still pay
the Schur reserve 1223/8892000 on this new head.

The reduction follows from RC42/43's refreshed actual prime and negative
pole bounds, RC19's native digamma lower envelope, and RC22's contour
Chebyshev approximation. The sufficient feature count falls by 85.47
percent, a factor 172/25=6.88. A full dense square matrix at the new count
has 625/29584 of the old entry count, about 2.11 percent.

The 1250-feature canonical projection and full actual matrices are not
constructed. Existing certificates for the first eight features remain
applicable. This reduces the outstanding construction size; it does not
certify original positivity at B=1.10 or estimate the minimum necessary
head rank.

## Carrier and actual arithmetic inputs

The carrier D_B, B=11/10, inclusion i, weight log(e+|xi|), and Fourier
convention exp(-2pi i xi x) are unchanged. A_Q is the bounded canonical
operator of the original Weil form, retaining its unbounded physical
logarithmic principal part. Its original coefficients are pinned to CC27
blob `e9a44661f94ee6750fc5ad1fbf7dc719fa3ba482`.

RC43 proves for the entire physical prime operator

    ||K_prime||<=k_prime,phys,
    k_prime,phys=4.10314831633822... .

RC42 proves that the entire physical negative pole component has norm
at most 2(sinh B-B), with outward certificate value about 0.47129494.
The positive pole component can be dropped for a lower envelope; it
remains present in the actual form and all future source calculations.
The combined negative allowance is therefore

    k_actual=k_prime,phys+2||sinh(x/2)||_2^2
             =4.57444325658822... <183/40=:kappa.

These are **physical** operator bounds. The canonical bounds obtained
after inclusion are not substituted into the physical Fourier integrand.
The validator verifies their rho=252/257 conversion and both input hashes.

RC19 supplies the analytic original multiplier inequalities

    a_arch(xi)>=-31/5,
    a_arch(xi)>=log x-1/x, x=|xi|, whenever pi*x>=1/4.

The second estimate is derived from the digamma Euler series and full
sum/integral discrepancy bound, not an asymptotic approximation. RC21
already uses its stated wider range. No new external special-function
identity is imported here.

## Reduced cutoff with an exact high-frequency reserve

Set alpha=1/10 and T=exp(51/10). Fresh rational Taylor bounds prove

    160<T<165,  8/3<e<3.

For x>=T, the inherited multiplier inequality and
log(e+x)<=log x+3/x give

    a_arch(xi)-kappa-alpha log(e+x)
      >=(9/10)log x-kappa-(13/10)/x
      >(9/10)(51/10)-183/40-13/1600
      =11/1600>0.

This applies throughout the full high-frequency region. For x<=T,
e+T<eT since e>2, T>160, and e<3; hence log(e+x)<61/10. Therefore

    a_arch(xi)-kappa-alpha log(e+x)
      >=-31/5-183/40-61/100=-2277/200.

Splitting the physical Fourier integral and using the entire arithmetic
negative budget yields the original canonical inequality

    A_Q >=(1/10)I_D -(2277/200)J_T^*J_T
         >=(1/10)I_D -12 J_T^*J_T.

J_T restricts Fourier(i h) to (-T,T). The smooth-core inequality extends
to the full supported logarithmic carrier by inherited canonical form
continuity. Original positivity at 1.10 is not assumed.

## New sufficient head and the entire Fourier residual

Use the same native moments as RC22:

    ell_j(h)=integral_(-B)^B T_j(x/B)i h(x)dx,
    ell_j(h)=<r_j,h>_D.

Let R_1250 a=sum_(j=0)^1249 a_j r_j. Define P as the **canonical
orthogonal** projection onto its range and H=I-P. Distinct polynomial
degrees give independent moments on the smooth supported core, so this
native feature map has rank 1250. No conditioning estimate is inferred.

RC22's Laurent-contour approximation X_n on the radius-two contour gives

    ||J_T-X_n||<=2sqrt(BT)*4 exp(3z/4)2^(-n),
    z=2pi BT,  X_n H=0.

An exact rational exponential enclosure proves exp(693/1000)<2, hence
log2>693/1000. With n=1250, pi<22/7, and T<165,

    n log2-3z/4
      >1250(693/1000)-(3/4)(44/7)(11/10)165
      =297/28>10.

Also 2sqrt(BT)<27 and e>8/3. Consequently the entire low-band operator
error obeys

    ||J_T-X_n|| <108(3/8)^10=:delta
                =0.005939316004514694... <1/100.

All n moments vanish on H, so ||J_T H||<=delta. This controls the entire
infinite complement, not a sampled tail. It follows that

    H A_Q H >=[1/10-(2277/200)delta^2]I_H,

whose certified coefficient is 0.0995983887216621... . Coarsening to
the inherited acceptance floor gives

    H A_Q H >=(247/2500)I_H.

The feature-count reduction is a sufficient construction bound, not a
claim about the true minimal head or the spectra of the unknown matrices.

## Remaining actual gate on this head

For this new 1250-feature map define

    M=R_1250^*R_1250,
    A=R_1250^* A_Q R_1250,
    sigma=i^*R_B i R_1250,
    V_src=R_1250^*sigma=A-M,
    U=sigma^*sigma,
    Gamma=U-V_src^*M^(-1)V_src.

The sufficient acceptance conditions remain

    A >=(1/4000)M,
    Gamma <=(1/300)^2 M.

Together with the preserved whole complement floor, the exact bounded
Schur argument gives

    1/4000-(1/300)^2/(247/2500)=1223/8892000>0.

Neither actual condition is established. The source sigma includes the
entire archimedean remainder, all seven prime powers, both signed poles,
and their cross correlations. Separate component source bounds do not
certify Gamma. Positive diagonal head and tail blocks alone do not certify
the coupled operator; the exact validator retains that failure control.

## Reuse boundary and outstanding construction

The native r_j are fixed by their functionals and the same canonical
carrier; they do not depend on the chosen truncation count. RC39/40's
actual eight-feature Gram/inverse enclosure, RC41's moment reconstruction,
and RC42/43's actual low-eight pole/prime head entries therefore remain
valid for the corresponding principal block of this head.

Their low-eight projection is not P_1250, and the inverse of the principal
eight-feature Gram is not the leading block of M_1250^(-1). All new
feature correlations, whole-matrix inverse/solve control, and source
residuals need certification at the new count. Lowering the head count
does not prove that its unknown actual head floor or source cross norm
improves. The preceding 8600-feature theorem remains valid independently.

The remaining construction target is now 1250 features, including the
1242 features beyond the certified low-eight block. The archimedean
remainder still lacks an actual low-eight head attachment. Full mixed
source certification and the original head floor remain open.

## Validation and custody

Generation passes 20 exact rational checks. Replay uses an independent
positive atanh series for log2, a separate cutoff Taylor enclosure, and a
direct positive exp(10) partial sum for the coarsened kernel error. It
rechecks source hashes, physical/canonical budget conversions, high
reserve, contour exponent, rectangle-area factor, whole residual/floor,
Schur reserve, and count ratios.

Run:

    python scripts/validate_rpb108_rc44_reduced_native_head.py
    python scripts/validate_rpb108_rc44_reduced_native_head.py --replay certificates/rpb108_rc44_reduced_native_head.json

The contour expansion, Riesz-space, multiplier, and whole-complement
proofs are analytic arguments inherited and specialized above. Exact
finite checks verify their explicit budgets; they do not construct the
1250-feature projection or prove them in Lean.

No historical artifact or other branch is changed. No new original
whole-aperture positivity, RH/F4 theorem, or Lean closure is claimed.
