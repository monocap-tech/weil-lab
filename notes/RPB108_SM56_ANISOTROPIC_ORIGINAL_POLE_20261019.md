# SM56 — Exact source-anisotropic Loewner errors for the original signed odd pole Schur

**October 19, 2026 · Original active W-ODD-NEG · stacked on SM55 draft PR #238.**

## Verified starting point and mathematical question

SM55 final-head Actions 39266782935 **PASSED** its exact-rational signed three-source certificate and fail-closed original obligation checks. The strongest original signed physical SI10 source triple is the genuine supported sine source 2, same-center xcos source 17, and sinh-pole source 24. The complete true odd signed form is bounded below on this *trial subspace* by the passing SM55 242-positive-window full 3x3 matrix whose original effective pole Schur margin is approximately **-0.058442558309409**. That lower remains inconclusive about the true negative index and whole original Weil positivity. All original negative frequency and exceptional-pole rank-one operator contributions are already paid in its unchanged baseline.

SM55 and SM54 charged each source positive-frequency Fourier mean approximation error with **one scalar epsilon multiplied by I3**. This is mathematically correct but may be overly conservative, especially for the pole source whose Fourier mean Taylor remainder is not equal to the sine/xcos remainders. SM56 develops a new certified error geometry on the same **242 original whole-real sign-positive disjoint windows**, so any improvement comes from accurately pricing errors rather than adding frequency windows.

## New complete 3x3 componentwise theorem

On each positive window I, the original SI06/SM39/SM40 whole-real signed multiplier lower gives gamma_I=2|I|delta_I>0. The true physical Fourier *frequency mean* u has exact rational midpoint vector v (sine2, xcos17, sinh24) and componentwise original SM42/SM46 second frequency Taylor bounds:

|u_i-v_i| <= r_i = r_i^(midpoint) + K_i |I|^2/24.

The original frequency-linear Taylor derivative integrates to zero on every symmetric real cell. For all i,j, with e=u-v,

|u_i u_j-v_i v_j| <= d_ij := |v_i| r_j + |v_j| r_i + r_i r_j.

The real symmetric error matrix E=uu^T-vv^T has exact entrywise absolute bounds |E_ij|<=d_ij. For any real coefficient z, 2|z_i z_j|<=z_i^2+z_j^2, hence

z^T E z >= -sum_i (sum_j d_ij) z_i^2.

Therefore the **full source-coupled valid Loewner bound** is

gamma_I u u^T >= gamma_I v v^T - diag_i( ceil_1e-12(gamma_I sum_j d_ij)).

This is a theorem for every original source coefficient vector z in the complete **three-dimensional** physical trial span. It is NOT a componentwise scalar-positivity inference or a claim about 25/470 entire source indices. It uses the true original physical sinh pole Fourier value and correct GLOBAL curvature bound, never substituting a fictional local pole curvature estimate.

For comparison the SM55 scalar bound is also independently valid on the same cell:

gamma_I u u^T >= gamma_I vv^T - ceil_1e-12(gamma_I epsMean) I3.

**Both formulas are valid.** Neither matrix dominates the other in every physical source direction automatically. The improvement criterion must therefore be the **full exact 3x3 Schur margin**, not merely which pole diagonal fee is smaller.

## Exact replay and adaptive selection

The exact full original signed SM55 242-prefix 3x3 matrix is pinned from passing Actions 39265951866 in the certificate file. The SM56 validator reruns SM55's signed whole-real hierarchical original candidate selection, checks all disjointness and multiplier sign conditions, replays the full scalar signed 3x3 matrix exactly and asserts **equality of all 9 rational entries** against the pinned passing certificate. It then revisits all 242 selected real signed positive cells and independently recomputes the three original physical Fourier midpoint interval and true componentwise mean error radii.

Each cell produces (a) the passing old scalar-error 3x3 lower increment and (b) the new fully valid anisotropic-error 3x3 lower increment. For comparison the validator computes:

- Full scalar-error original complete signed 3x3 lower, exactly equal to SM55 passing Actions;
- Full anisotropic-error original complete signed 3x3 lower;
- An adaptive mixture choosing, for each of the **same disjoint windows**, whichever of the two separately valid lower increments gives the better exact coupled pole Schur margin at that stage.

The final result chooses the greatest **certified exact rational Schur margin** among these independently valid entire physical source lower matrices, retaining SM55 as a fallback. A gain from the new error geometry is accepted **only if this exact full coupled Schur strictly improves**, never from uncharged errors or isolated diagonal positivity.

The Sylvester conditions remain full positive leading 2x2 coupled block and strictly positive entire 3x3 determinant. A negative determinant of a lower matrix cannot prove actual odd negativity.

## Research status and complete-operator boundary

Initial focused CI is pending. If anisotropic errors recover further pole margin, this provides a new direction for source-aware matrix certificates on the complete 25-support source space. Whether or not it improves, **the actual original negative index, the orthogonal remainder, 470 original Astar inverse/strong residual and complete W-ODD-NEG O1/O2 remain OPEN**; the even operator, Weil positivity, CC27 and RH also remain OPEN. Independent original physical Fourier/domain mathematical audit remains outstanding.

The next substantive route after this trial-space diagnostics is a complete-operator bound on the orthogonal remainder and true spectral inertia; trial-space error optimization cannot itself replace those acceptance gates.


## Exact finite-dimensional negative-index ceiling

The complete true original signed odd three-source form Q satisfies Q >= L, with L a rigorously computed full symmetric 3x3 lower. Its first two leading Sylvester minors are strictly positive. The inertia decomposition over its 2x2 positive leading block and its exact real Schur S=det L/det L_2 gives:

- If S>0, L is strictly positive definite and Q is strictly positive on this exact physical **three-dimensional** span.
- If S=0, L is positive semidefinite and Q has **negative index zero** on this three-dimensional span (a possible zero direction remains).
- If S<0, L has precisely two positive and one negative eigenvalues, and the min-max/inertia comparison Q >= L proves **negative index of Q on this three-dimensional trial space is at most one**. It does NOT prove a true negative direction exists.

This is a mathematically justified finite-dimensional index CEILING, not a complete-operator original odd negative-index theorem. The orthogonal complement and all original 25 supported/470-source directions must be classified independently to accept canonical W-ODD-NEG O1/O2. The validator and Actions explicitly prevent any promotion from this 3D ceiling to the complete operator.


## First original focused certificate — Actions 39270413282 SUCCESS

The complete original source Fourier and all-cross rational validator **passed** its first focused GitHub Actions run 39270413282 on the initial SM56 source head, before later documentation and the explicit three-dimensional index-ceiling acceptance was committed. It exactly reconstructed the complete nine-entry rational SM55 signed 3x3 lower matrix from original Actions 39265951866, and rechecked all 242 original signed-positive disjoint real cells.

| Whole-source SM56 comparison | Exact verified result |
| --- | ---: |
| SM55 original scalar-error effective pole Schur lower | -0.05844255830940901 |
| Uniformly switched all 242 cells to anisotropic fees | -0.05844493343464814 |
| **Exact per-cell choice between TWO valid full-source lower bounds** | **-0.058397346915907374** |
| Strict certified improved complete signed 3x3 Schur margin | **>0.000045211393** |
| Cells using source-componentwise fees | **84** |
| Cells retaining existing scalar original fee | **158** |
| Cells whose individual pole component fee was smaller anisotropically | **84** |
| Cells whose pole component fee was larger anisotropically | **158** |
| Total original 242-cell pole scalar approximation fee | 0.000888965145 |
| Total original 242-cell pole anisotropic approximation fee | 0.000891564161 |

This proves an important *limited* structural observation: **anisotropic error fees are not uniformly better**, even for the pole coordinate, but exact source-targeted error selection can strengthen the *entire* original 3x3 signed lower. This is a sound mathematical improvement after retaining every original real signed frequency source cell, previous negative upper, original exceptional rank-one pole, and all mixed physical source terms.

The resulting lower's original signed Sylvester third determinant remains strictly negative, so **three-source PD is still NOT established**. The original odd form may or may not have any actual negative vector in this span. The lower's strictly positive leading original sine/xcos 2x2 minor does, by finite-dimensional inertia monotonicity, imply **actual original signed negative index at most one on this 3-dimensional physical span**, not on the complete odd operator.

First substantive Actions passed; subsequent code added explicit scoped negative-index checking and this research note. Final PR-head Actions and independent original Fourier/domain premise audit remain separately pending. No complete operator positive or negative index theorem has been promoted.
