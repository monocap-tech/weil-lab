# EF22 — Exact original seven-prime arithmetic energy cancellation on the fixed EF21 cofinite test

**2026-10-31; active canonical W-EVEN-FORM, OPEN.** Parent EF21 [draft PR #400](https://github.com/monocap-tech/weil-lab/pull/400) exact physical fixed cosine-bell source and O(r) localization-method STOP; expanded [Actions #41218819802](https://github.com/monocap-tech/weil-lab/actions/runs/41218819802) **SUCCESS** with original source and governance checks. Original arch pseudolocality and source/form-domain bridge separate from CI, whole even/odd/Weil/RH remain OPEN.

## 1. Source-specific arithmetic cancellation, not replacement by a positive cap

EF21 fixes one *genuine original* even cofinite test f=F_h psi, with the original 107 SI10 rational centers c_j, 469 orders, real even selfadjoint bounded h=1/2048 shift filter, and the compact cosine-six bell psi centered at ±a, a=B-ln2+469h, B=11/10, radius r=1/65536. All 1,878 bell translates are physically supported in I and pairwise disjoint. f is exactly orthogonal to all 469 original parity-even source columns. Its exact physical squared L2 norm is (231r/1024)*sum_{k=-469}^{469} A_k²>=231r/512. This is not a normalized inverse-Schur bound.

On the actual original signed pole-free Fourier multiplier, the full ORIGINAL prime contribution is

q_prime(f,f) = -sum_{n in {2,3,4,5,7,8,9}} w_n[<f,T_{ln n}f>+<f,T_{-ln n}f>],
w_n=(ln p_n)/sqrt(n)>0.

For the fixed bell grid, **every** pair of translated support components lies at centers s*a-k*h with s=±1, -469<=k<=469. The difference between two centers is either an integer multiple d*h with |d|<=938 (same lobe sign) or ±2a+d*h with |d|<=938 (opposite lobe signs). Both are strict literal physical support intervals, not sampled Fourier heuristic.

The original ln2 interval gives ln(2)>938h+2r, so ALL seven n fail same-lobe overlap. For opposite-lobe center differences, the only potential matches lie near ln(n) - (2a+d*h), with n in the authentic original n-set and d=-938,...,+938. The exact source checker inspects **7*1877=13,139** original ln(n)/ln2 Fraction interval comparisons and certifies a strict positive margin to each after deducting 2r. The other sign -2a+d*h is impossible by positivity/size bounds. Consequently, f and every shifted T_{±ln n}f have DISJOINT support for all seven original n.

Therefore we have the **exact original-object identity**

  q_prime(f,f)=0,

without assuming prime weights small, replacing m with an upper cap, invoking a truncated positive surrogate, or running an enormous signed frequency mesh. Writing the original pole-free signed form as q0=q_arch+q_prime, its cofinite energy for this PARTICULAR exact f is

  **E=q0(f,f)=q_arch(f,f)=∫_R arch(xi)|fhat(xi)|² dxi**.

This is the major EF22 simplification: the original signed seven-prime part of the **energy denominator** is eliminated by a genuine physical support/separation identity, not estimated. The original archimedean logarithmic symbol is retained with its actual sign, and its energy upper interval is still needed.

The actual original even positive pole can be restored independently. Since cosh(x/2) is a common real eigenfunction of all even shifts on the full real line, and every shifted bump is still supported in I, the physical overlap obeys

  <cosh(x/2),f> = Lambda_h <cosh(x/2),psi>,
  Lambda_h=prod_j [2cosh(h/2)-2cos(2*pi*h*c_j)]^{p_j} > 0.

Thus the true original even pole contribution is exactly +2 Lambda_h²|<cosh,psi>|². No numeric Lambda or positivity promotion is inferred.

## 2. The original signed mixed numerator remains nonzero and reduces to finite boundary sums

EF20 showed (conditional on the original arch pseudolocality/form-domain argument) that the true fixed-h mixed map is nonzero for SOME compact even psi, but that does not certify the sign of the SPECIFIC EF21 cosine bell.

Let e(x)=1_I cos(2*pi*(37/64)x) be the first actual SI10 even source. Its untruncated full-real cosine is an EXACT native exceptional mode. Since f is even and orthogonal to that cosine on I, it is also orthogonal to cos(2*pi*c0*(x±ln n)) on I for each n: the sine cross vanishes by parity. For the actual shifted physically truncated source e(x±ln n), the original prime mixed integral is therefore entirely a **physical cutoff correction**, not a global cosine term:

  q_prime(e,f)=sum_n w_n sum_{σ=±1}
    ∫_{|x+σln n|>B} f(x) cos(2*pi*c0*(x+σln n)) dx.

This exact identity eliminates all infinite-frequency prime quadrature from M. The remaining region is a finite sum over the 1,878 actual bell translates. Each bell is either entirely outside, entirely inside, or partially clipped by one of the original physical source endpoints. Because h>2r, each cutoff intersects at most one translate per sign-lobe, giving at most 7*2*2*2=56 partial possibilities a priori. A NEW exact rational original-ln(n) center/end-point test sharpens this drastically: **EXACTLY TWO** original bells are partially clipped, both belonging to the original **n=2 source term**: (sigma=+1, positive bell near +a, k=+469 at physical +B), and its even mirror (sigma=-1, negative bell near -a, k=-469 at -B). All original n=3,4,5,7,8,9 have **ZERO** partially clipped bells; all their contributions are complete/zero bell integrals. Every full bell piece reduces to H_r(c0)*cos(2*pi*c0*shifted center). Thus the entire authentic seven-prime mixed calculation is finite elementary trigonometric sums with **only two half-bell exceptions**. These sums, their conditioning, and the full original mixed sign have NOT yet been evaluated or enclosed.

The archimedean contribution to M still requires the original signed archimedean Fourier/physical evaluation, but only **one** full-frequency mixed integral remains instead of a seven-prime plus arch mixture. The arch energy E similarly requires one full-frequency scalar integral and a certified UPPER bound.

## 3. A first genuine numerical ORIGINAL signed mixed source component: n=2

The two partially clipped bells have a stronger consequence than merely reducing the number of residual integrals. For n=2, sigma=+, all 939 bell translates on the NEGATIVE-center lattice lie completely inside the original e(x+ln2) support, and their full-cosine integral is zero EXACTLY by the original SI10 c0=37/64 FIR root. Every positive-center lattice translate is completely excluded, except the unique extreme k=+469 bell centered at the true endpoint x0=B-ln2; precisely its t<0 half lies inside original shifted e. The sigma=- source translate is its exact parity mirror with k=-469. Both extreme source FIR coefficients are exactly +1; the two source-sign and bell-1/2 coefficients combine to ONE half-bell integral, not two.

Thus the *authentic signed n=2 original pole-free mixed contribution* is exactly

q_prime,n2(e,f) = -w2 * ∫_{-r}^{0} cos^6(pi*t/(2r)) cos(2*pi*c0*(B+t)) dt,

where w2=ln2/sqrt2, c0=37/64, B=11/10, r=1/65536. This is NOT the whole original mixed M (which also contains n=3,4,5,7,8,9 and archimedean terms).

Since the EXACT original rational cosine interval at phase 407*pi/320 has cos_hi<0, and |cos(omega(B+t))-cos(omega B)|<=omega_hi*r with omega_hi=2*pi_hi*c0, we have cos_hi+omega_hi*r<0. The exact half-bell mass is 5r/16. Hence a **strict, original source-specific positive interval**:

0 < (ln2/sqrt2)_lower *[-cos_hi - omega_hi*r]*(5r/16)
  <= q_prime,n2(e,f)
  <= (ln2/sqrt2)_upper *[-cos_lo + omega_hi*r]*(5r/16).

The new source checker requires the LOWER endpoint to exceed 15/10^7=0.0000015, using inherited SI06/14 original Fraction enclosures. The exact source CI will print the actual lower/upper decimal summaries. **This is a real quantitative signed ORIGINAL n=2 mixed contribution, not a point-jump-to-L2 inference, not a normalized inverse-Schur bound, and not evidence that the full M is positive.**

## 4. Audit, stopping condition, next accepted original data



This is a strong exact cancellation for the original object. It must not be mistaken for q_prime(e,f)=0 or an original positivity theorem. The genuine original pole-free Schur variational quotient remains

  |M_arch+M_prime|² / E_arch,

and no positive numerical lower is established without a common certified interval M and finite positive upper E. EF21's shrinking-radius normalized O(r) method STOP remains; making r smaller does not repair signed Schur conditioning.

**Source verification acceptance:** Replay exact SI10 original 973/107 cover, native physical bell support and 469 source degrees, 13,139 rigorous original log-lattice nonoverlaps, no swapped weights, exact q_prime(f,f)=0 and prime mixed cutoff identity. The finite log rational checks certify supports and algebra; any independent operator/domain audit remains open. CI can accept source-specific arithmetic cancellation, not complete original arch quantification.

**EF23 next:** Evaluate the original finite boundary/cutoff prime numerator with rigorously outward exact trig/sinh intervals and source FIR coefficient control; separately certify a source-conditioned original arch M and E upper. If 469-factor conditioning prevents reliable mixed sign, STOP the universal FIR and pivot to genuinely finite lower-moment exact complementary test; do not manufacture numerical Schur bounds from nonzero jumps. All prior original evidence preserved, no main merge.
