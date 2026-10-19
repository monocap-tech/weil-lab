# MG12 — Original double-boundary Gram and certified low-band envelope

October 19, 2026. Stacked on passing MG11 #260. W-ODD-NEG, complete even/Weil/CC27/RH, and independent analytic Fourier/domain audit remain OPEN.

## Verified method-gate outcome — October 19, 2026

The first dedicated whole calculation **PASSED** GitHub Actions [39343097995](https://github.com/monocap-tech/weil-lab/actions/runs/39343097995), with exact original physical 23-source eigenvalue lower floor **0.020429750736**, independently reproduced MG11 nonpole pivot index 23, and first strict positive low-band certificate among tested dyadic cutoffs at **2^16**.

At cutoff **2^20**, the conservative entire original positive-energy-scaled strong action upper is **82018597753.99704**. This is a ratio of rigorous COARSE bounds, NOT the actual source strong Galerkin residual norm or a negative-eigenvalue assertion.

**MG12 decision: ACCEPT physical Gram/domain-relative basis transform, REJECT this coarse whole-low-band scalar strong-action bound as quantitatively viable for the MG07 51/56 source-470 residual gate.** The next method investigation should estimate the actual low-frequency coupled (A_*^2) and (A_*) source forms/real-source residual with certified adaptive frequency integration, physical cross terms and the SI29 preconditioner, rather than further increase endpoint derivative peeling alone.

## First genuinely transformed physical inner product

MG11 proved that the exact original supported odd physical source endpoint values b_i=f_i(B) and endpoint derivatives d_i=f_i'(B) have rank two. With pivot q=23 and the original sinh pole s at index 24, define Delta=b_s*d_q-b_q*d_s, a_i=(b_i*d_q-b_q*d_i)/Delta and c_i=(b_s*d_i-b_i*d_s)/Delta. The 23 true physical functions h_i=f_i-a_i*s-c_i*f_q vanish at both endpoints together with their first derivatives. The coefficients are exact analytic values, enclosed by SM42 rational intervals rather than replaced by sample values.

MG12 independently reconstructs ALL 625 original physical 25-source Gram intervals using SM42. It performs the complete physical congruence H23=T^* H25 T with exact-rational outward intervals for the 529 transformed entries, including all two-pivot physical cross terms. The transformed matrix is positive definite structurally because SM42 certified H25>0 and T contains identity rows on the 23 unconstrained original source coefficients. In addition the validator attempts a direct exact-rational preconditioned-Gershgorin certificate, obtaining an explicit coefficient-eigenvalue floor ell_H. Numerical Cholesky proposes a preconditioner ONLY; the proof uses exact rational intervals. All genuine transformed physical odd sinh pole overlaps g_i=<s,h_i> and original pole norm are enclosed.

## Real, conservative low-frequency source operator inequality

With Lambda=2^k, MG11's third-derivative complete 23D endpoint cancellation gives, on the ENTIRE high real Fourier tail, an L2 error tau0=2*sum(D3'_i)^2/(6^6*5*Lambda^5) times I23, and an original strong positive action error tauA=2*sum(D3'_i)^2/(6^6*Lambda^5) * [M^2/5+2*M/25+2/125] times I23, M=17+k*347/500. Both derive from exact source derivative upper bounds, not numerical FFT data.

SM42's inherited original multiplier bound kappa<=a_o(xi)<=M on the low band |xi|<=Lambda, together with Parseval, establishes the true coupled low-band Loewner source sandwich:

  kappa * (H23 - tau0 I23) <= Ao_low <= M * H23.

It also proves S_low=integral_low a_o(xi)^2 hhat hhat* <= M^2 H23 and, combining MG11's high strong tail, FULL original pole-free strong action:

  ||Ao h_z||^2 <= M^2 z^T H23 z + tauA ||z||^2.

The true original positive Astar=Ao-2|s><s| is retained, not discarded. With all pole overlaps g_i=<s,h_i>, Young's inequality gives

  ||Astar h_z||^2 <= 2 M^2 z^T H23 z + 2 tauA ||z||^2 + 8||s||^2 (g^T z)^2.

The SI29 reference Astar>=kappa_star I gives the **separate energy lower** T* Astar T >=kappa_star H23. Thus a rigorous but likely hugely conservative complete 23D strong-action-to-energy upper ratio is measurable.

## Acceptance and nonclaims

At dyadic cutoffs k=12,16,20,24,30, MG12 reports the complete transformed physical Gram's positive definite proof and actual coefficient-norm lower, all low-band and strong-tail bounds, exact pole payment, and whether each coarse low-band strict PSD gate closes. These inequalities do NOT establish the original Galerkin residual R=J-Astar Z is small. The full original 470-source residual, 14-feature reference correlations, 890-column negative cap, signed odd O1/O2, even sector, Weil positivity and RH remain unproved.

If the 23D physical Gram passes but the strong-action-to-energy ratio remains enormous, the next gate should improve certified COUPLED LOW-FREQUENCY STIFFNESS and approximate the actual continuous Galerkin response, not repeat endpoint peeling.

Reproduce: python scripts/validate_rpb108_mg12_double_trace_gram_lowband.py.
