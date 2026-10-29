# NF386 — Original Fourier-primal lowband upper entry

**Scope 2026-10-28 PT:** W-ODD-NEG remains OPEN. Stacked above NF385 PR #370. No actual original signed lowband upper, selected J242 trial vector, full exterior inverse or RH proof is created by this pass.

## Why this is not another finite signed witness

NF380–NF385 measure or limit finite exterior signed response, principally n512. Those results cannot give an upper on the original infinite exterior. NF374–NF375 instead already certify genuine whole-real signed high-frequency **UPPER** bounds for the exact original matched four directions `u_i=f_(T e_i)-w_i`, holding J242, NF369 Y0, NF370 dyadic T and the complete seven-prime signed multiplier fixed. Their missing term is a source-matched original **lowband upper**.

The old suggested method evaluated `H_i(L;j)=||P_I F^-1[1_(|xi|<=L) m(xi) uhat_i]-j||_(L2(I))` through a physical J242 projection or spatially correlated signed continuum cells, with explicit `j∈J242` still unconstructed. We obtain a **different sufficient upper route** from frequency-space Plancherel, which needs one scalar, nonnegative real-axis signed mismatch integral for any *frozen* explicit dyadic j, plus a high-frequency tail of that j. Neither a fresh 242x242 signed kernel nor a large simultaneous physical projection solve is logically required for this conservative route.

## Exact Fourier-primal inequality

Under the already inherited original supported Fourier/multiplier identification and same physical Fourier normalization, set `f_i,L(xi)=1_(|xi|<=L)m(xi) uhat_i(xi)`. Let `j∈J242` be a specifically frozen supported *odd* original selected-space trial, `j=J242 z` with explicit dyadic coefficients `z` and unchanged source SHA. Since `j` vanishes outside I when physically extended, Plancherel plus `||P_I g||<=||g||` implies

`H_i(L;j)^2 = ||P_I F^-1 f_i,L-j||² <= ||f_i,L-jhat||²_(L2(R))`

`= int_|xi|<=L |m(xi) uhat_i(xi)-jhat(xi)|² dxi + int_|xi|>L |jhat(xi)|² dxi.`  (A)

The integrand in the first term is **nonnegative and cancellation-aware**. A verified rational *upper* `U_i²` on the entire right side satisfying `U_i²<target_i(L)²` would prove the exact original lowband norm upper required in NF375, and `(high_i(L)+target_i(L))²<mu0*d_i/4` has already passed independently for the same original source and cutoff. This is sufficient to discharge direction i's **strong residual sufficient test**, conditional on the inherited strong operator realization. Four simultaneous passes would discharge only the NF370 four-plane trace test; other 238 selected directions, the full signed odd form and RH remain open. No such U_i² was calculated here.

Important: the full-line mismatch criterion is **strictly stronger than the physical interval criterion** and may fail even when the physical residual is small. A failed Fourier-primal trial is a METHOD STOP for that j and cutoff, not a negative original Weil vector.

## Explicit high-frequency j-tail cap, avoiding another signed calculation

For any odd supported j with twice differentiable interior and integrable j'' (finite linear combinations from J242 satisfy this), integration by parts twice gives for |xi|>L:

`|jhat(xi)| <= |j(B)|/(pi |xi|)+(2|j'(B)|+||j''||_1)/(4*pi²*xi²)`.

With exact rational conservative `pi>3`, define `a=|j(B)|/3`, `b=(2|j'(B)|+||j''||_1)/36`. Then the original full-line j-tail is rigorously bounded by

`int_|xi|>L |jhat|² < 2*(a²/L + a*b/L² + b²/(3 L³))`.  (B)

This requires only endpoint values and an L1 curvature bound on the **explicit original selected trial**; these are physical, not signed-kernel objects. For `L=2^24`, the unchanged original NF375 direction-four future lowband norm target is `tau=2.8e-13`. The **hypothetical design condition** `j(B)=0` and `2|j'(B)|+||j''||_1<=1/10` gives in exact rational arithmetic

`tail_j_squared < 2*(1/360)²/[3*(2^24)^3] < tau²/64`.

Thus an original selected trial meeting that condition would leave at least `63/64` of the squared Fourier-primal `tau²` budget for the nonnegative lowband mismatch integral. **No such original j was constructed or claimed to meet the endpoint condition in NF386.** The numerical threshold is a certified entry test for a *proposed* j, not an accepted original lowband upper.

More generally, for an actual candidate j compute exact rational outward bounds on its `j(B)`, `j'(B)`, and `||j''||_1` using the physical source frame and correlated polynomial/trig derivatives. Pay j-tail by (B), then rigorously integrate the **one nonnegative low-frequency original signed multiplier discrepancy** (A) in intervals. If the j-tail **lower** already reaches tau², that candidate cannot pass the Fourier-primal criterion (upper bounds alone do not establish impossibility). If its upper is large, optimization or direct physical restriction is needed rather than an invalid method stop.

## Verification and unaltered source

A stdlib `Fraction` checker at `scripts/local_replay/nf386_original_fourier_primal_lowband_entry.py` uses the **unchanged actual NF375 report Git blob SHA1 `03c709571046d3f09307614aaded9749f5a15ba1`**, original PR355 source SHA256 `abd37707d585dcd54b040f1ae865a7430a9c7cba85df31131661b2e72e560770`, original NF374 Arb native SHA256 `a725a6da6bf29ce21b1955df8f4d0b35b87ff8f003d09cdff13581d1b82f7559`, and verifies the 20 NF375 original high+future lowband budget comparisons, four original dyadic margins, exact j-tail prototype, and a **synthetic** 2D Hilbert fixture that cannot be mistaken for original Weil evidence. This program does **not** integrate the actual signed Fourier mismatch or create a z-vector. GitHub workflow execution and historical native pending statuses are separately reported.

**Previous NF385:** one n512 c-energy ray consumes <3.62835% of d4; unmeasured complement remains. **NF386 current:** constructive alternate original signed LOWBAND **UPPER** test with one scalar nonnegative Fourier integral and physically certified j tail. **Next:** freeze one actual J242 dyadic j and certify (A) at a selected original cutoff, or reject the Fourier-primal route if conservative off-support mismatch is prohibitive. Do not re-open broad harmonic scans or present the acceptance rule as a measured upper. Original n513, general domain, whole J242/odd/even/Weil and RH OPEN.
