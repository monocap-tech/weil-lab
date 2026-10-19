# MG08 — Actual original-source SI29 residual feasibility pilot

**October 19, 2026. Numerical diagnostic only. Whole original odd/even/Weil/CC27/RH OPEN.**

## Objective

MG07 PR #255 defines a rigorous **conditional complete-470-source** preconditioned residual gate based on the *genuine* physical SI29 14-feature positive operator lower reference B14. MG08 measures the first physically attached residual overlaps on the existing **original SM36 true 25-source pilot**, instead of adding more finite matrix identities without real source evaluations. MG08 never claims original 470-source positivity.

SM36's already passing sampled pilot has the original seven-prime/digamma multiplier, the genuinely supported 25 SI10 source functions and original sinh pole, all original 107 negative moment blocks / 890 columns, 4096 and 8192 physical samples. MG08 reuses exactly that physical source selection and signed Fourier multiplier, but calculates the entire **strong sampled physical-space residual** rather than the trivially vanishing coefficient-space Ritz defect.

## Computation

For the sampled physical basis V with physical Gram H, sampled original positive Fourier stiffness Ao and actual odd-pole overlap b, construct sampled Astar stiffness S=Ao-2bb^T and trial coefficient map C=S^-1 H. The trial solution in the actual supported physical grid is Z=VC. Independently compute sampled physical Astar(Z) by the FFT frequency multiplier max(kappa,m(xi)), restricted back to the true support, **then** subtract 2 s <s,Z>. Define

  R_sampled = V - Astar_sampled(Z).

Sampled Galerkin orthogonality checks V^T R_sampled dx ≈ 0, but **nonzero complete strong residual** R_sampled is measured in sampled L2. It is not a certified original strong residual: the log-growing archimedean high-frequency tail is truncated and the Fourier-grid quadrature is not outward bounded.

MG08 evaluates each of the **true analytic original SI29 feature functions** on this physical grid, rather than using the rational Simpson proxy as the mathematical function. For c,r,δ and degree=0:

  g_c,r(x) = sin(2 pi c x) sinc(2 r x),

where numpy.sinc(z)=sin(pi z)/(pi z). For first normalized orthogonal moment degree=1:

  g1_c,r(x) = 3 cos(2 pi c x) [sin(u)/u² - cos(u)/u], u=2 pi r x,

with a stable exact Taylor at small u. All **12 degree-0 and 2 degree-1 SI29 features** are included. Retain gamma=4rδ/(3 if degree1 else 1) and the true supported odd pole s(x)=sinh(x/2).

Compute sampled D=R^T R, F=G14^T R, physical full 14x14 feature Gram, q=G14^T s and z=R^T C14^-1 s, all with physical dx integration. The complete sampled inverse-reference residual matrix is calculated by exact-shape Woodbury:

  DB = kappa^-1 D - kappa^-2 F^T M^-1 F + (2/alpha) z z^T,

M=Gamma^-1 + kappa^-1 G14^T G14 and alpha=1-2 <s,C14^-1 s>. A separate sampled computation of B14^-1 R checks the full matrix, including negative positive-feature correction and positive pole correction, to high floating precision. This is **numerical internal consistency only**, not rigorous original interval enclosure.

The same sampled Galerkin Z is passed through all genuine SM10 **107 full negative physical moment blocks / 890 Taylor columns**, including eta. Compare for rational trial t values the generalized eigenvalue of the original SM35 scalar penalty

  (1+t)Ncap + (1+1/t)(Hminus/kstar²) D

versus MG07's operator-reference penalty

  (1+t)Ncap + (1+1/t)(Hminus/kstar) DB.

These are **sampled, exploratory** matrices with original source geometry. Numerical spectral values above or below 51/56 can neither accept nor reject the original 470D proof.

## Method gates

1. Require the actual 25 original physical sources, 14 SI29 analytic true feature functions (12 means + 2 moments), 107 original negative source blocks and 890 original negative cap columns, the true pole subtraction and no silently dropped source cross.
2. Verify nonzero physically sampled strong residual, small source-space Galerkin weak residual, positive sampled reference pole alpha, numerical full-matrix Woodbury cross-check and finite eigenvalues. Compare **4096 vs 8192** physical grids at the same ×4 padding; these grids have Nyquist frequencies above the ~883 largest selected source frequency.
3. Record reference-weighted residual spectral inflation, the cap contribution and whether the two sampled objectives are improved on identical source columns. No scalar trace alone establishes Loewner dominance.
4. If reference preconditioning yields meaningful numerical improvement, the next gate is **certified entire-frequency source residual and SI29 feature Gram enclosures on a single true original source block**. If not, test stronger negative-frequency-weighted resolvent or alternative trial spaces before the full 470D cost.
5. The original **unbounded** positive Fourier multiplier, frequency quadrature error, high logarithmic tail, dense 470-source conditioning, and complete 470x470 positive/negative coupled matrices remain unresolved.

Reproduction: `OPENBLAS_NUM_THREADS=2 OMP_NUM_THREADS=2 python scripts/mg08_original_14feature_strong_residual_pilot.py`.
