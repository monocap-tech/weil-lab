# MG67 — Exact rational original-source coefficient-orthant copositivity census

**Status: mathematical construction and independent implementation committed; GitHub Actions independent acceptance pending.** Parent MG66 [original physical 3D error covariance independent full replay Actions #40022012105](https://github.com/monocap-tech/weil-lab/actions/runs/40022012105) PASSED for six actual original source 3-planes, exactly 24 physical sign-adjusted 3×3 source matrices. Only 7 of 24 matrices were globally SPD; zero full three-dimensional source restrictions passed all four sign cases. This does not prove an actual strong-action source negative eigenmode or rank at most two.

## New structural distinction: source coefficient sign cone versus entire R³

Original MG66 uses the genuine SI10/MG11 23-adapted plus actual sinh-pole source, original signed seven-prime/digamma multiplier, verified 55-cell physical original source Fourier intervals and unchanged true corrected strong action. It independently certifies the source mean center Q and the source-specific interval error covariance R on six rational original 3-planes, with the TRUE physical mean perturbation satisfying

    ||Delta C z||² <= |z|^T R |z|

for every real source coefficient z. The true original center mean energy is ||C z||²=z^T Q z. On a fixed sign orthant z=D x with x>=0 and D=diag(±1,±1,±1),

    ||C z||² - ||Delta C z||²
    >= x^T (D Q D - R) x.

MG66 required **Q-D R D positive definite on ALL real R³**, which is stronger than needed on the particular sign cone for D. The mathematically appropriate sufficient criterion is **strict copositivity of B_D=D Q D-R**, that is

    inf_{x>=0, ||x||_1=1} x^T B_D x > 0

for each of the four sign orthants modulo the global sign. A positive rational lower m>0 for every cone implies a uniform original 3D source action gap for every real vector, with ||z||_1²>=||z||_2². Retaining MG66's true physical source norm bound, exact source coefficient-Euclidean restricted coercivity follows from

    kappa >= m² / [2 (tr(Q)+tr(R)) tr(W^T W)] > 0.

This is ONLY an original restricted 3D physical source theorem when all four sign cones pass. It cannot be promoted to a global 24D rank-three Loewner source bound, residual contraction or RH.

## Exact finite three-variable copositivity decision, without floating eigenvalues

Each exact parent MG66 3×3 source matrix Q and R has enormous integer/rational entries because physical Taylor bounds were kept exact. For x>=0, products x_i x_j are nonnegative. Thus for each exact B_D we can *rigorously* replace its entries by directed rational lower and upper bounds with denominator 10^14:

    floor(10^14 B_ij)/10^14 <= B_ij <= ceil(10^14 B_ij)/10^14.

Let B_lower and B_upper be these rational matrices. For every x>=0, this induces exact inequalities

    x^T B_lower x <= x^T B_D x <= x^T B_upper x.

The producer computes exact rational global minima of both bounding quadratic forms on the **compact nonnegative 2-simplex**, not their possibly misleading global real-eigenvalues. For a symmetric rational 3×3 A, every simplex global minimum occurs at a vertex, a stationary point along one of its three edges, or an interior KKT stationary point. If the interior KKT system is singular, any interior stationary extremum belongs to a flat affine stationary family meeting the simplex boundary at the same value, already checked. No floating-point minimizer is used for acceptance.

A **positive lower-simplex minimum** certifies strict source-cone positivity for the true original physical error envelope. A **negative upper-simplex minimum** yields an explicit rational nonnegative source coefficient vector for which EVEN the upper bound is negative, thereby giving a rigorous failure witness for this *conservative source uncertainty inequality*. Such a witness DOES NOT yield a physical negative-energy mode, since the envelope R may be loose or correlated in inaccessible ways. If zero falls between minima, leave that source sign cone explicitly unresolved.

## Provisional arithmetic findings, separately reproduced before Actions

On the original independently verified MG66 physical Q/R archive, local exact rational producer and a separately implemented exact barycentric minimizer agreed:

| Third original source | Original MG66 globally SPD cases | MG67 strictly copositive sign cones | Explicit failing error-envelope cone witnesses |
|---|---:|---:|---:|
| e0 | 2/4 | 3/4 | 1 |
| e1 | 1/4 | 3/4 | 1 |
| e2 | 1/4 | 3/4 | 1 |
| e11 | 1/4 | 3/4 | 1 |
| e20 | 1/4 | 3/4 | 1 |
| e23 | 1/4 | 3/4 | 1 |
| **Total** | **7/24** | **18/24** | **6** |

Thus correct geometric sign-cone restriction recovers eleven additional positive cases of the existing physical uncertainty model, but there remains a **negative original conservative-error envelope witness in one sign orthant for each sampled 3-plane**. NONE of the six fixed source configurations has a strict true 3D source positivity certificate under this exact radius-covariance model. This finite failure is not a universal source-rank limit.

## Independent acceptance

The separately authored MG67 verifier does NOT import the MG67 producer. It reconstructs the exact signed error forms from the previously independently physically accepted MG66 Q/R source matrices and independently computes their directed 10^14 rational enclosures. Instead of the producer's 4×4 rational KKT Gaussian elimination, the verifier minimizes each quadratic via exact reduction to x2=1-x0-x1, closed-form interior stationary point, all edge stationarity and vertices. It checks all 24 lower and upper minima, their explicit rational witnesses, validates negative upper witnesses against the **original full-precision** B_D matrix, and enforces full four-sign acceptance before any 3D theorem.

**Next frontier MG68:** The six actual sign-orthant failure directions are specific, exact and source-coordinate dependent. Optimize genuine source basis and physical Fourier cell selection for these failing orthants, or derive tighter original physical error correlations than the independent component-radius model before spending further iterations on global 24D source coercivity. Any improved physical error bound must have its own independently regenerated original Fourier proof. Scalar trace improvement alone is not a sufficient gate.

All original 24D strong-action source coercivity/residual contraction, 470D inverse, odd signed 51/56 spectral cap, independent original Fourier/form/domain identification, even/Weil/CC27/RH remain OPEN.
