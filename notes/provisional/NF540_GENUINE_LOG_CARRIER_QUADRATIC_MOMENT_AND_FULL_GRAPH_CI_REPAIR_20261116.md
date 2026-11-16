# NF540 — Exact genuine logarithmic Hilbert carrier gate and targeted universal-graph compiler repairs

**2026-11-16 PT. Draft PR #568; NEW LEAN ACCEPTANCE PENDING.** Inherited NF539 universal graph identity is mathematically supported and now patched again for compiler elaboration. The original NF494 U400 SHA256 \`39cba367d70243c2d15e5a9323fc8097d58187923dcf0eca2b031136871f0181\` and all original 242 selected source directions remain unchanged. The all-multiplicity actual zeta divisor remains the exact same object. No global RH, W_ODD_NEG or original singular carrier certificate is claimed.

## 1. Actual NF539 CI verdict: two script errors, not an arithmetic contradiction

The focused original NF539 run [#43832483415](https://github.com/monocap-tech/weil-lab/actions/runs/43832483415) **COMPLETED FAILURE**. The prior NF529 full graph closure, NF532 generic authentic zeta EF, and NF533 automatic literal actual multiplicity summability compilation targets passed. The independent NF538/NF539 universal full source graph module then failed at:

- \`ActualZetaFullGraphRawDivisorQuadratic.lean:32:10\`: \`simp only [mul_inv_rev]\` made no progress proving the exact \(\sqrt2\)-inverse multiplication identity. NF540 now uses \`rw [pow_two]\` followed by \`(mul_inv_rev _ _).symm\` directly.
- \`ActualZetaFullGraphRawDivisorQuadratic.lean:132:6\`: \`rw [h]\` could not identify \`RCLike.re (inner ℂ ...)\` syntactically with the \`Complex.re\` projection in the target. NF540 explicitly \`change\`s the goal to \`RCLike.re\` before \`rw [h]\`.

Both changes preserve the exact \(\tfrac12\) second source factor, the existing P/N source vectors, the unchanged actual divisor and the theorem statements. Recompilation in the inherited focused workflow is pending; do not promote universal \`Q=Re Σ\` to Lean PASS without a genuine check receipt.

## 2. Mathematical advance: original log-energy source admission reduces to one standard quadratic Fourier moment

The genuine \`NeutralLogHilbertCarrier a\` is NOT just a supported \(L^2\) vector. Its original physical spectral energy is
\[
\int_{\mathbb R} \log(e+|\xi|)\,|\widehat f(\xi)|^2\,d\xi<\infty.
\]
A plain physical \(L^2\) embedding as in NF535 is insufficient.

The NEW \`ActualZetaLogCarrierQuadraticMoment.lean\` makes the elementary but essential explicit bound **using the actual unchanged spectral weight**:
\[
\boxed{1\le w(\xi)=\log(e+|\xi|)
 \le e+1+\xi^2}.
\]
The upper inequality follows from \(\log x\le x\) for \(x\ge0\) and \(|\xi|\le1+\xi^2\); no zero data, RH or Green representation is involved.

For any **same original physical** \(f\in L^2(\mathbb R)\) with finite polynomial Fourier moment
\[
 M_2(f)=\int_{\mathbb R}(e+1+\xi^2)|\widehat f(\xi)|^2\,d\xi<\infty,
\]
the pointwise comparison gives the exact logarithmic energy admissibility
\[
\int_{\mathbb R}\log(e+|\xi|)|\widehat f(\xi)|^2\,d\xi<\infty.
\]
When the SAME \(f\) is a.e. supported in \([-a,a]\), the existing \`neutralCanonicalLogFormDomain a\` and \`neutralCanonicalToLogHilbert\` constructions therefore give a **source-exact** \(k\in\mathrm{NeutralLogHilbertCarrier}(a)\) with
\[
\boxed{\mathrm{neutralLogPhysical}(k)=f\quad \text{as original } L^2 \text{ vectors}.}
\]
This is a strong admissibility reduction: **the only new regularity input needed for this gate is a quadratic Fourier moment**, not an independently estimated full logarithmic graph norm or Green-source approximation.

The three new Lean target declarations are:
- \`neutralLogarithmicFourierWeight_le_quadraticMoment\`;
- \`neutralFiniteLogFourierEnergy_of_quadraticMoment\`;
- \`neutralPhysicalL2_hasOriginalLogHilbertCarrier_of_quadraticMoment\`.

All are written without \`sorry\`, \`axiom\` or \`admit\` but **are not claimed compiled**. An independent, smaller \`.github/workflows/nf540-log-carrier-moment.yml\` builds this module without depending on the NF534–NF537 unfinished smooth-test modules, so its verdict can be accepted separately. Initial NF540 dedicated CI: [#43834206106](https://github.com/monocap-tech/weil-lab/actions/runs/43834206106), QUEUED at writing.

## 3. What is still unproved

The moment hypothesis is a *sufficient condition*, not its discharge for the actual original collar. For the original smooth strict-collar approximants, the next regularity theorem must use their actual physical a.e. representatives, with compact support and enough derivatives, to prove the Fourier second moment (for instance via the \(L^2\)-Fourier derivative relation and Plancherel). The user-visible claim must NOT conflate C² almost everywhere with a pointwise smooth representative, and the singular original endpoint-log \(\ell_U\) is **not** automatically H¹. This NF540 step does not address its full original two-source graph limit.

The other outstanding obligations remain:
- NF539 exact universal full source-graph \`Q=Re Σ_actual\` Lean certification: compiler patch written; focused verdict pending.
- NF534 almost-everywhere regularized physical correlation and NF535 smooth collar L² embedding: independent Lean compiler errors/skip remain unresolved.
- NF536/NF537 real-odd all-divisor source sample ℓ² and P/N full-graph lift: Lean compilation pending.
- NF527 genuine true-gamma/digamma, only actual \(n=9\) prime and original pole term sharp \(Q\ge 0.1\|f\|_2^2\) for strict collars: **analytic exact-rational sufficient gate**, not Lean proof.
- NF524/NF528 complete actual full two-source approximation and original U400-specific endpoint nonzero carrier sign: analytic, Lean OPEN.
- Global odd/even positivity, W_ODD_NEG, Riemann hypothesis: OPEN.

**NF540 disposition: independent exact logarithmic-domain admission criterion and further universal-identity compiler repairs, new Lean verdicts PENDING.**