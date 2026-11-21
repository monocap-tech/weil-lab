# Weil-Lab — CP019
## True first Hardy-`Z` jet and original complex Euler–Maclaurin remainder derivative errors via Cauchy estimates

**Independent CP### cross-projection research, stacked on CP018 PR #839 → CP017 #838 → CP016 #837 → CP015 #836 → CP014 #831 → CP013 #829 → CP012 #827 → CP011 #825 → CP010 #822 → CP009 #819 → CP008 #817 → CP007 #815 → CP006 #810 → CP005 #807 → CP004 #803 → CP003 #799 → CP002 #796 → CP001 #790.** The original IV### Phase IV signed Weil prime/Arch/pole support-extension and NF### original physical numerical enclosure compilers are unchanged. The PI### normalized spectral comparison stays independently open.

**Proof level: original published source facts DIRECTLY checked + fully exact rational external arithmetic + FOUR NEW Lean v4.35 SOURCE CANDIDATE MODULES. NO NEW CP013–CP019 LEAN KERNEL ACCEPTANCE.** No narrow original Hardy-`Z` zero bracket has new kernel acceptance; no original signed Weil–full spectral 3×3 identity, global Weil positivity or RH.

## 1. Important corrected source understanding: theta' is ALREADY proved upstream

The original frozen upstream source `smmercuri/zeta@c06b4e13d9c847e50a32c3d738271cbad62ae9f3` has an accepted standalone source theorem:

```lean
-- in Zeta/Gram/Averaging.lean
theorem hasDerivAt_riemannSiegelTheta {T : ℝ} (hT : 0 < T) :
  HasDerivAt riemannSiegelTheta
    (1 / 2 * (Complex.digamma (1 / 4 + Complex.I * (T / 2))).re
      - 1 / 2 * Real.log Real.pi) T
```

This is a direct source bridge to the TRUE original phase derivative, **not a derivative inferred from its approximate theta value**. Original `Zeta/Gamma/TrigammaDecay.lean` additionally uses in its proof of `monotoneOn_re_digamma_quarter_vertical` the exact original complex digamma vertical-curve real derivative

[
\frac d{dt}\Re\psi(1/4+it/2)
=-\tfrac12\Im\psi'(1/4+it/2).
]

That identity is a local proof ingredient in the original source, not an already exported standalone theorem asserting (	heta'') in exactly CP018's interface. CP019 reuses the accepted θ' theorem and promotes a **new proof candidate**, rather than announcing θ' as newly discovered or newly accepted.

### New proof candidates in isolated original-v4.35 Lean

`CP019OriginalFirstJet.lean` builds on the real `hasDerivAt_riemannSiegelTheta`, original holomorphic `differentiableAt_riemannZeta`, and Mathlib's genuine real-to-complex `HasDerivAt.ofReal_comp` and `HasDerivAt.comp_ofReal` chain rules. Target is the true source Hardy-`Z` FIRST derivative on the entire (t>0) half-line:

[
\boxed{
Z'(t)=
\Re\left[e^{i\theta(t)}i
\left(\theta'(t)\zeta(1/2+it)+\zeta'(1/2+it)\right)\right].
}
]

This removes CP018's previous **abstract source-first-jet derivative identity** as a potentially independent analytical assumption once the module compiles. It does not yet give a numerical lower enclosure (Z'(149.5)\ge12/5).

`CP019ThetaSecond.lean` reuses and generalizes the real-digamma vertical derivative already worked out inside the accepted original `TrigammaDecay` source, combined with genuine `hasDerivAt_riemannSiegelTheta` and original filter-germ calculus. Its target:

[
\boxed{
\theta''(t)=-\tfrac14\Im\psi'(1/4+it/2)
}\quad(t>0),
]
with an explicit equality to CP018's `thetaSecondJet` definition, removing another source analytical derivative-identity input **conditional on NEW kernel acceptance**.

All six new source theorems in these two modules contain no introduced axiom or sorry. **They have not passed the original Lean 4.35 compiler and axiom audit**, so they must not be listed as newly certified.

## 2. A valid replacement for CP018's value-error derivative obstruction: move to a complex disk

The original source `Zeta/Zeros/HardyZ.lean` proves a Hardy-`Z` **REAL function-value** approximation error. Its derivative cannot be bounded by differentiating that error inequality. CP018 explicitly identified this loss of information.

But the original published **ZETA Euler–Maclaurin remainder** is substantially stronger as a complex-analytic object. Actual source:
- `Zeta/EulerMaclaurin/Continuation.lean` proves `Complex.differentiableOn_eulerMaclaurinRemainderIoi_cpow`, the **HOLOMORPHY** of the improper remainder on a complex half-plane, and provides `zetaRemainder`, the original full approximant remainder, and the original `riemannZeta_eq_approximant_add_remainder`.
- `Zeta/EulerMaclaurin/ErrorBound.lean` proves original `norm_zetaRemainder_le` with the **complex** Borwein majorant `zetaRemainderBound` on (\Re(s)>-(2M+1)), not merely on critical-line real ordinates.
- `Mathlib/Analysis/Complex/Liouville.lean` at the original pinned v4.35.0 publishes the genuine `Complex.norm_iteratedDeriv_le_of_forall_mem_sphere_norm_le`, i.e. Cauchy:

[
 \|R_M^{(k)}(s_0)\|
 \le \frac{k!}{r^k}\max_{|s-s_0|=r}\|R_M(s)\|.
]

This transfers a **COMPLEX UNIFORM VALUE** bound into derivatives through the holomorphic Cauchy integral theorem, which is valid. It does NOT differentiate the real Hardy-`Z` value-error inequality and does not assume source phase first/second derivatives came from a numerical screen.

## 3. A concrete exact M=6, N=256, radius=1/4 derivative budget for EVERY target height

Let (t\in[a,b]), (a=149.5), (b=150.05353). Center each complex Cauchy circle at (s_t=1/2+it) with `r=1/4`. If (|z-s_t|=r), then exact triangle/real-part inequalities give

[
\Re z\ge\frac14,
\quad
\|z\|\le\frac12+t+\frac14
\le150.80353<151.
]

Choose original Euler–Maclaurin order (M=6) and cutoff (N=256). The original proven `zetaRemainderBound` is

[
B_{M,N}(z)=
\frac{|z+(2M+1)|}{\Re z+(2M+1)}
\left|
\frac{B_{2M+2}}{(2M+2)!}
 (z)_{2M+1}N^{-z-(2M+1)}
\right|.
]

At (M=6), we have (|B_{14}|=7/6) EXACTLY (the script independently reconstructs all Bernoulli numbers through rational recurrence). All points on the entire moving family of complex circles satisfy

[
\frac{|z+13|}{\Re z+13}
\le\frac{164}{13+1/4}=\frac{656}{53},
\quad
\left|(z)_{13}\right|
=\prod_{j=0}^{12}|z+j|
\le\prod_{j=0}^{12}(151+j),
\quad
\big|256^{-z-13}\big|\le256^{-13}.
]

Thus the **mathematically derived explicit source Borwein upper bound** is

[
\begin{aligned}
\|R_6(z,256)\|
&\le \frac{656}{53}
 \frac{7}{6\cdot14!}
 \frac{\prod_{j=0}^{12}(151+j)}{256^{13}}\\
&=\boxed{
\frac{181596617021805363}{
633825300114114700748351602688
}}\\
&\approx2.865089433777896\times10^{-13}
\quad<\boxed{3\times10^{-13}}.
\end{aligned}
]

Every finite scalar calculation above is independently verified with stdlib exact `fractions.Fraction`, exact product/factorials and exact Bernoulli recursion. The real/complex norm estimates are standard mathematical inequalities **derived from the actual published formula**. However, the complete universal original `zetaRemainderBound≤3×10^-13` **has not yet been attached as an unconditional NEW Lean theorem**: the source-level all-circle finite Borwein inequality must still be discharged. Do not replace that gap with raw source SHA or one numeric sample.

Cauchy's genuine published theorem would then yield, simultaneously for EVERY height in the interval:

| Complex zeta remainder derivative order (k) | Uniform source-derived upper target, if the envelope is Lean attached |
|---:|---:|
| 0 | (displaystyle3\times10^{-13}) |
| 1 | (displaystyle1.2\times10^{-12}) |
| 2 | (displaystyle9.6\times10^{-12}) |
| 3 | (displaystyle1.152\times10^{-10}) |

The remaining assumptions in the formal Cauchy theorem are independent of its exact rational arithmetic:

**Analytical regularity:** original improper Euler–Maclaurin remainder's holomorphy on the closed complex disk. CP019 now supplies `CP019HolomorphicRemainder.lean`, whose proof source uses the actual original `Complex.differentiableOn_eulerMaclaurinRemainderIoi_cpow`, the finite entire Bernoulli/Pochhammer term and `Mathlib.DifferentiableOn.diffContOnCl_ball`. Thus the exact source `DiffContOnCl` condition is **discharged as a no-sorry Lean source proof candidate**, no longer a required additional numerical assumption when CP019 compiles.

**All-circle numerical inequality:** (\forall z\in\mathrm{sphere}(s_t,r), B_{6,256}(z)\le3\times10^{-13}) remains an **EXPLICIT missing new Lean proof** in the stronger final Cauchy theorem. The proof needs source `ascPochhammer` product norms, complex norm geometry, the original (B_{14}), complex `cpow` modulus and the exact rational inequality. Its mathematical reasoning and exact external arithmetic have passed, but no actual original compiler receipt exists.

The four new Lean source modules give **17** new theorem targets in total:
1. `CP019OriginalFirstJet.lean`: 3 original first-jet identities.
2. `CP019ThetaSecond.lean`: 3 original trigamma second-phase identities.
3. `CP019HolomorphicRemainder.lean`: 3 original source Euler–Maclaurin holomorphy and disk-restriction identities.
4. `CP019CauchyRemainder.lean`: 8 exact source remainder value/Cauchy/finite-product lemmas, including the stronger `original_zeta_EM_cauchy_of_Borwein_circle_only` and order-three derivative bound, **conditional only on the remaining all-circle Borwein envelope**.

No derivative data from an independent Hardy-`Z` numerical screen is added as a Lean axiom.

## 4. Independent actual numerical comparison (NONRIGOROUS, not a proof)

As a feasibility cross-check, I implemented the original `zetaApproximant` formula at (M=6,N=256) in high-precision mpmath, and computed independent complex derivatives of `riemannZeta - zetaApproximant` for (k=0,1,2,3) at three heights. Example magnitudes:

| (t) | (k=0) residual | (k=1) | (k=2) | (k=3) |
|---:|---:|---:|---:|---:|
| 149.5 | (7.88\times10^{-16}) | (4.37\times10^{-15}) | (2.42\times10^{-14}) | (1.34\times10^{-13}) |
| 149.75 | (8.05\times10^{-16}) | (4.46\times10^{-15}) | (2.47\times10^{-14}) | (1.37\times10^{-13}) |
| 150.05353 | (8.27\times10^{-16}) | (4.58\times10^{-15}) | (2.54\times10^{-14}) | (1.41\times10^{-13}) |

All sampled magnitudes are smaller than the separate rational Cauchy targets, but this mpmath calculation is **NONRIGOROUS**: it is not certified ball arithmetic, a universal source remainder proof, a new narrow zero sign enclosure or original derivative anchor. The rigorous route is the analytically valid Cauchy transfer from the genuine complex source theorem, plus the missing complete Lean circle envelope.

## 5. Original immutable seven-source provenance

I directly re-fetched and verified **all 7 exact Git blob hashes** against genuine source theorem signatures:

| Original file | Frozen Git blob | Original accepted source capability |
|---|---|---|
| `Zeta/Gram/Averaging.lean` | `6a30171433903a57736de2ab83b120ef660e08bd` | TRUE `hasDerivAt_riemannSiegelTheta` |
| `Zeta/Gamma/TrigammaDecay.lean` | `60b6e9a4645d06988d2ca2d293b141195382d37c` | TRUE digamma vertical derivative in `monotoneOn_re_digamma_quarter_vertical` proof |
| `Zeta/EulerMaclaurin/Continuation.lean` | `1bb01e946fa7e344497eaf7694fbecff0a714d09` | TRUE complex remainder holomorphy, original zeta EM identity |
| `Zeta/EulerMaclaurin/ErrorBound.lean` | `01184af0dbfd1369e14725e02e990b016bedfe6f` | TRUE complex original `norm_zetaRemainder_le` and `zetaRemainderBound` |
| `Zeta/Zeros/HardyZ.lean` | `9975442b0c14011c35f4624197d0bf26169c7665` | TRUE Hardy-`Z` definition and value-error, NOT derivative error |
| `mathlib4@v4.35.0` `Mathlib/Analysis/Complex/Liouville.lean` | `70382d63ec267d2704790b1d77692e1f5cd5faed` | TRUE n-th Cauchy derivative estimate `norm_iteratedDeriv_le_of_forall_mem_sphere_norm_le` |
| `mathlib4@v4.35.0` `Mathlib/Analysis/Complex/RealDeriv.lean` | `d7223234773ef2f7caec59a941211806412083fa` | TRUE complex-to-real derivative chain rules |

Source inspection was direct via connected GitHub files; source SHA checks are genuine. A source-file hash does not certify that the new local Lean source proof compiles.

## 6. Custody, compiler gating and next mathematical obligation

New `scripts/cp019_original_cauchy_exact_fraction_preflight.py` tests the full **exact rational** M6N256 envelope independently, incl. Bernoulli recurrence B14=7/6, norm-factor geometry, product, exact Cauchy caps and deliberate failed overly-small error caps. It checks the seven exact immutable source signatures. Return status: `CP019_SEVEN_PINNED_SOURCES_AND_EXACT_CAUCHY_BUDGET_PASS_NOT_KERNEL`.

New `scripts/cp019_original_lean_source_and_cauchy_axiom_audit.py` is fail-closed: actual source-bound original v4.35 compilation of **FOUR** new CP019 `.olean` and eleven CP013–CP018 dependencies, plus **17 actual** printed standard-only axiom receipts; no `sorryAx`/nonstandard axioms. Any eventual success status states **CP019_ORIGINAL_HARDYZ_FIRST_THETA_SECOND_JET_AND_CAUCHY_CONDITIONAL_KERNEL_PASS_ONLY**, explicitly preserving the remaining original all-circle Borwein envelope and Hardy-`Z` numeric derivative/curvature/narrow zero as OPEN.

Two workflows, opt-in only via PR labels `cp019-cauchy-source` / `cp019-cauchy-lean` or eligible manual dispatch. No normal push or PR-created/synchronize jobs; no extra background CI load on the IV###/NF### queue. At PR creation no new original Lean kernel acceptance or original v4.35 build receipts are asserted.

**Next CP020:**
1. Discharge the ONLY remaining **all-circle Borwein numerical envelope** in the new Cauchy estimate: kernel proof that `zetaRemainderBound z 6 256 ≤3/10^13` on every radius-1/4 complex circle about (1/2+it), uniformly (149.5\le t\le150.05353). Use original `norm_zetaRemainder_le`, `ascPochhammer_succ_eval`, complex norm/rpow and exact Bernoulli B14 + rational product. The original remainder holomorphy has its own new CP019 source theorem candidate.
2. Kernel-certify derivative transport `iteratedDeriv k (riemannZeta - zetaApproximant)=iteratedDeriv k zetaRemainder` for (k\le3), relying on original complex analytic identity and Mathlib genuine `Filter.EventuallyEq.iteratedDeriv` and `iteratedDeriv_add`.
3. With the complex first/second ζ derivative remainder now controlled at (lesssim10^{-10}), derive a **separate genuine source phase/Gamma derivative remainder** and an actual validated interval enclosure of the finite approximant across eight cells, including the correlated rotated complex bracket for (Z'').
4. Close the original (Z'(149.5)\ge12/5) and (|Z''|\le4) on the entire interval using actual source ball arithmetic, then finally the missing CP010 genuinely certified root in ((150.05352,150.05353)). This is distinct from CP016 source-defined intrinsic ordinal #53 proof candidate.
5. Recover **real** pending CP013–CP019 original Lean 4.35 compiler results and repair concrete type errors, rather than silently promoting no-sorry source candidates to accepted proofs.

**Preservation law:** a function-value bound on one real line does not transport derivatives; a UNIFORM HOLOMORPHIC complex-neighborhood bound DOES, via original Cauchy integral theory. That is a genuine source analytic preservation mechanism, not the original signed Weil ↔ full spectral normalized equality, which remains INDEPENDENTLY OPEN. NO global Weil positivity or RH claim.
