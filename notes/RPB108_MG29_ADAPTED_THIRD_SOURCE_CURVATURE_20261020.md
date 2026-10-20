# MG29 — Original adapted third Fourier derivative and controlled 32-cell refinement

October 20, 2026. Stacked on verified MG28 [PR #277](https://github.com/monocap-tech/weil-lab/pull/277). This is the **next numerical source enclosure method**; do not promote it to spectral positivity, original 470D inverse, signed cap, or RH without the acceptance gates.

## Mathematical target

MG27 measured source curvature as the dominant trace-width cost, and MG28 used direct *adapted second Fourier derivatives* to shrink the 16-cell original [0,4] source bracket widths by 28–30%. The remaining drift budget was the sum of separate physical-source third derivative global norms. To preserve more cancellation, MG29 bounds the THIRD derivative directly for each original MG11 adapted 23-source combination

`h_j=f_j-a_j*s-c_j*f_pivot`, plus the true original sinh pole as its own source.

At each rational midpoint `xi_0`, compute the true rational interval

`T'''_h_j(xi_0)=T'''_f_j(xi_0)-a_j*T'''_s(xi_0)-c_j*T'''_pivot(xi_0)`

before taking absolute values. Every coefficient `a_j,c_j` is the *verified original endpoint-trace interval*, not a floating-point surrogate.

For all original sine and xcos supported physical sources, use the exact rational SI06/SM42/SM46 trigonometric antiderivatives `F3(q)=int x^3 sin(2*pi*q*x)` and `F4(q)=int x^4 cos(2*pi*q*x)`:

`T'''_sin(c)= -4*pi^3 [F3(c+xi)+F3(c-xi)]`

`T'''_xcos(c)= -4*pi^3 [F4(xi+c)+F4(xi-c)]`.

The pole `T_s=N(w)/(a²+w²)`, `w=2*pi*xi`, `a=1/2` is *analytically differentiated three times* with exact rational interval sin/cos/sinh/cosh and pi, and independently parity-checked at the origin. No finite differences or point-sampled FFT are used for proof.

## Whole-real frequency-cell rigorous bound

The actual FOURTH Fourier derivative globally obeys

`|T''''_g| <= (2*pi_upper)^4 int[-B,B] |x|^4|g(x)| dx`

for the original supported generator `g`. For `sin` and sinh pole, use `2B^5/5`; for `xcos`, `B^6/3` as exact physical moment caps.

On a cell of half-width `h`, for every real `xi` in the whole cell,

`|T'''_h_j(xi)| <= maxabs(T'''_h_j(xi_0)) + L4_h_j*h`.

Intersect this bound with MG28's global adapted third-derivative bound. Then refine the certified second-derivative envelope

`K29_j=min(K28_j, maxabs(T''_h_j(xi_0)) + min(L3_old_j,L3_direct_j)*h)`.

Consequently **every actual source Taylor radius satisfies `r29_j<=r28_j`**. This assertion is independently checked for every source/cell, not inferred from numerical trend.

## Scope and experiment

Use genuinely contiguous original physical-source Fourier frequency [0,4] on 16 and 32 exact rational equal-width cells. On *each* cell, preserve the identical original positive digamma + seven-prime interval multiplier and freeze MG26's accepted exact-rational sourcewise Young tau. Produce TWO original matrices in one calculation, one replaying MG28's direct second derivative and one with MG29's third refinement. Their difference is exclusively the certified source Taylor radius change.

The 16-cell MG28 replay must match its **separate accepted Actions #39438064440 artifact bit-for-bit on all three source moment TRACE widths**. A 32-cell MG28 replay is calculated side-by-side for a valid same-mesh improvement comparison. The original 24D prefix H/G/S lower and upper matrices then feed MG26's rigorous `H-H_prefix` physical source mass closure and MG24/SM41 high-tail source bounds, preserving all mixed sinh pole terms. For k=12,16, report complete real-frequency pole-corrected Gstar/Sstar bracket widths relative to MG28 same-mesh and the MG24 accepted original benchmark.

**Acceptance:** original rational midpoint third intervals and fourth drift, 16-cell independently accepted original MG28 replay, monotone source Taylor radii *for every cell*, strict exact lower/upper source and whole-frequency pole Loewner construction, and accurate independent GitHub Actions artifact. Positive source residual and signed 470-source cap are separate gates. If MG29's same-mesh width is not sharper, report no gain without inventing extra positivity.

Full original 470D strong inverse, signed odd 51/56 negative cap, independent Fourier/form/domain identification, even/Weil/CC27/RH remain **OPEN**.

**CI: PENDING**.
