# SM50A — Entire original negative-frequency source2 UPPER, refined physical Fourier mean-square

**October 18–19, 2026 · Same W-ODD-NEG obligation as SM50 draft PR #232.** This is a same-thread refinement of SM50's first complete-negative acceptance; it does not branch the research objective.

## Why SM50 baseline was inconclusive

The first original SM50 Actions **39194179750 passed** all original 973-leaf coverage checks. Its true original positive LOW source2 lower, with the full 25×25 source error paid, was approximately **0.095124**, whereas the entire original negative-frequency upper charged by whole-leaf sinc supremum was **0.859214**, plus the original sinh pole penalty approximately **0.000127**. The rigorous signed *lower* was approximately **−0.764217**. This proves neither positivity nor negativity of the actual form. It identifies a loose negative-upper integration method, not an original non-RH witness.

## New whole-real signed and physical source refinement

Start from **all 973 original SI10 signed-negative dyadic leaves**, true weight \(w_{\rm old}=h_I+\kappa\), original all-seven-prime/digamma \(m\) and full signed negative-frequency support subset of [0,896]. Split each parent into **four exact rational subcells**, 3,892 in total, never dropping any part of the support.

For every real subcell \(J=[a,b]\), \(c=(a+b)/2\), \(r=(b-a)/2\), use the inherited original SM39 *arbitrary rational left* archimedean lower, SI06 exact seven-prime midpoint interval and true derivative 69:

\[
m(\xi)\ge m^-_J:=
\operatorname{arch}_{\rm lo}(a)
+\operatorname{prime}_{\rm lo}(c)-69r,\quad\forall\xi\in J.
\]

Therefore the actual complete negative multiplier is dominated throughout by

\[
0\le(\kappa-m(\xi))_+
\le w_J:=\min\left\{w_{\rm old},
\operatorname{ceil}_{10^{-6}}\big[(\kappa-m^-_J)_+\big]\right\}.
\]

Both arguments of the minimum are *independent certified original whole-real upper bounds*. No floor is imposed for zero cells because the source2 scalar form does not need strictly positive Hankel covariance pivots.

For actual supported odd sine e2 with genuine frequency center \(1845/128\), the exact original SI06/SM42 Fourier antiderivatives and first/second frequency derivatives give interval enclosures for \(T(c)\), \(T'(c)\), \(T''(c)\). Select rational midpoint coefficients \(v,d\), and prove

\[
T(\xi)=v+d(\xi-c)+\rho(\xi),\qquad
|\rho(\xi)|\le R:=r_0+r_1r+\tfrac12 K_Jr^2,
\]
\[
K_J=\min\bigl\{K_{\rm global},
|T''(c)|_{\rm upper}+M_3r\bigr\}.
\]

The symmetric subcell integral eliminates the affine cross exactly. Writing \(M_2=v^2+d^2r^2/3\), Cauchy and original exact upward integer-isqrt enclosures yield

\[
\int_J |T(\xi)|^2 d\xi
\le |J|\left(M_2+2R\sqrt{M_2}+R^2\right).
\]

The inherited SM43 original whole-cell sinc supremum independently yields
\(\int_J|T|^2\le|J|s_J^2\). Choose the **minimum of these two rigorously certified whole-cell integrals** with exact Fraction arithmetic. Thus the new original entire signed-negative source2 upper is

\[
\boxed{
U_{50A,2}:=
2\sum_{J\in\mathrm{3892}}
w_J|J|\min\left\{s_J^2,
M_{2,J}+2R_J\sqrt{M_{2,J}}+R_J^2\right\}.
}
\]

All original negative support and signed weights remain. The independently verified source2 positive LOW lower from SM49 and original true sinh pole upper remain unchanged. The resulting signed quadratic lower is \(L^{\rm full25}_{+,2}-U_{50A,2}-\Pi_2\). As before, genuine original source2 sign can be certified **only if this exact signed lower is strictly positive**. A negative lower remains inconclusive.

## Verification / scope

The focused SM50A validator reconstructs all 973 original parents, 3,892 real signed subcells and original true supported sine source integrals with rational SI06/SM39/SM42 formulas. It must strictly reduce the entire-negative source2 upper compared to SM50's 973-cell envelope and preserve all signed/physical one-dimensional claims and complete original source matrix status.

If still too conservative, investigate source-targeted signed multiplier interpolation or capture more original positive continuum; do not convert a lower/upper certificate gap into a claim of actual negativity.

Complete original 25×25 signed odd PSD/inertia, 470-source conditioned Astar inverse and strong residual, W-ODD-NEG O1/O2, even E1–E4, original Weil positivity, CC27 and RH remain **OPEN**. Inherited Fourier/form-domain identities and external mathematical audit remain separate from Actions.


## Focused SM50A numerical certificate — accepted on original 3892 real subcells

**October 18 local / October 19 UTC · GitHub Actions [39198050550](https://github.com/monocap-tech/weil-lab/actions/runs/39198050550) SUCCESS** on source commit \`e71881b4eb3a66a403a4f296fdf78d6aead73c75\`. Both exact-rational original source computation and fail-closed numerical/obligation checks passed. The initial two source runs, 39194778387 and 39194832919, had finished all computations and written artifacts, but failed from an output-only Python \`json.dumps(..., flush=True)\` typo; this was corrected to \`print(..., flush=True)\`. No mathematical acceptance check had failed. The corrected focused run passed.

| Original entire negative spectrum, same physical e₂ | Outward bound |
| --- | ---: |
| Original SM50 973-parent complete negative upper | \`214803569513/250000000000\` = **0.859214278052** |
| Original SM50A 3892-subcell improved signed *weight only* + sinc | \`76189799421/125000000000\` = **0.609518395368** |
| Original SM50A 3892-subcell signed weight + true Fourier affine-square | \`144542118733/250000000000\` = **0.578168474932** |
| Same original SM49 complete 25-source-error positive LOW e₂ lower | \`47561993717/500000000000\` = **0.095123987434** |
| Genuine SM42 exceptional-pole penalty upper | \`126906031/1000000000000\` = **0.000126906031** |
| First original SM50 signed lower | \`-764217196649/1000000000000\` = **−0.764217196649** |
| New entire-negative original SM50A signed lower | \`-483171393529/1000000000000\` = **−0.483171393529** |

*These are outward rational enclosures, not floating-source FFT approximations.* All **973** original parent negative leaves and **107** original source clusters remain included, partitioned into **3,892** true whole-real subcells. The improved sign-cell upper is strict on 3,892 subcells. Full physical sine Fourier affine mean-square rather than the whole-cell sinc supremum was chosen on **2,549** subcells, and local second derivative estimates improved on **2,549** subcells. The final original full-negative scalar cap is **32.7096% smaller** than the first SM50 cap; a strengthened exact gate \(10U_{50A}<7U_{50}\) (more than 30% gain), plus at least 2,500 source-affine cells, is now in the validator and workflow. The first pass preceded this strengthened gate; its final PR-head Actions must be checked independently.

**Scope is crucial:** The certified bound of **−0.483171393529 is a LOWER bound on the true original signed odd form along this single source**. It is still negative and therefore gives *no* negativity or positivity conclusion about the actual signed form. In particular, it is **not** an original off-line zero, evidence against RH, a negative odd spectral index, or full signed Weil positivity.

## Structural lesson and next true-operator strategy

Most of the improved bound comes from **signed-weight localization** (0.859214→0.609518); physical source-integral sharpening contributes an additional 0.031350. Another indiscriminate refinement of the negative leaf integration is unlikely to be the highest-value *first* next move.

For the *same* original scalar source \(g_2\), the exact pointwise identity holds everywhere:

\[
\underbrace{\max\{\kappa,m(\xi)\}}_{\text{original positive}}
-\underbrace{(\kappa-m(\xi))_+}_{\text{original negative}}
=m(\xi).
\]

The next original-source investigation should exploit this exact signed cancellation directly on the source's Fourier-dominant frequency band, rather than separately estimate a small positive LOWER and a large negative UPPER before subtraction. A rigorous source-targeted signed real-frequency cell integral can use:
- original whole-real signed *lower* \(m_{\rm lo}(I)\) from rational arch-left and seven-prime second-derivative/interpolation bounds;
- if \(m_{\rm lo}(I)\ge0\), a certified LOWER on \(\int_I|T_2|^2\), e.g. Jensen with rigorous physical Fourier mean interval;
- if \(m_{\rm lo}(I)<0\), a certified UPPER on \(\int_I|T_2|^2\), e.g. SM50A affine-square with full remainder;
- remaining outer negative frequencies bounded ABOVE from the exhaustive original negative-cover cap; outside original high-frequency sign-safe domain the signed contribution is nonnegative.

The weighted signed sum must retain **every real frequency** without double counting. This is a **proposed next gate**, not a claimed new signed-form certificate. In parallel or afterwards, the complete original 25×25 signed matrix, 470 physical source residual, exceptional-pole Schur, and orthogonal complement remain independent acceptance obligations.
