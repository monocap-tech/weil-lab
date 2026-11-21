# Weil-Lab — IV030
## Phase fidelity is an independent obstruction: the ORIGINAL prime form is not a function of support graph and \(L^2\) mass

**Project custody.** IV030 continues the separately maintained Phase IV original signed Weil support-extension certification and cross-projection compatibility investigation. It does not interrupt Phase III NF###. The mathematical source considered below is the ACTUAL original Zeta23 von-Mangoldt prime term, not an artificial Gram/spectral replacement. This is a standalone explicit mathematical construction with exact-rational checks, **not a newly kernel-accepted Lean proof**, not global Weil positivity and not RH.

**Actual compiler boundary:** repaired IV009 workflow [44850887402](https://github.com/monocap-tech/weil-lab/actions/runs/44850887402) remained QUEUED when checked for IV030; IV018 [44850967574](https://github.com/monocap-tech/weil-lab/actions/runs/44850967574) remained PENDING; IV019–IV024 previously checked jobs remained QUEUED. GitHub's repository-wide queue was 2240 at IV030's initial inspection. No full IV023 four-cell original signed Weil \(1/16\) Lean kernel PASS or source-bound axiom receipt was obtained. The IV025 generated Lake-manifest preflight repairs, IV027 corrected graph signs, IV028 corrected real GitHub compiler-error parser and IV029 input-order dictionary remain on the existing recovery descendant branch; individual earlier PR heads have not received those patches.

### 1. What IV024–IV029 proved only as an independent geometry/complex-algebra test

The genuine original two strict NF543 collars are

    L = (-11/10, -549/500),
    R = ( 549/500, 11/10).

They sit near \(-1.1\) and \(+1.1\), and their only possible old-old arithmetic-active \(\pm\log(n)\) interactions for \(n<10\) occur at \(n=9\).

The actual original complex correlation definition, verified against \`ActualZetaCorrelationTransform.lean\` and the source IV011 Schwartz-integral dictionary, is

    C(s,t;τ) = ∫_ℝ t(x) conj(s(x-τ)) dx,

so its FIRST argument is conjugate-linear and its SECOND is linear. The ORIGINAL signed prime contribution (from \`ActualZetaOriginalCollarPrimeBound.lean\`) is

    P(f,f) = ∑_{n≥0} [Λ(n)/√n]
                       [C(f,f;+log n)+C(f,f;-log n)].

The NF600 original theorem source reduces this to exactly \(n=9\) for test functions supported in L∪R. Its true original coefficient is

    κ = Λ(9)/√9 = (log3)/3,    0<κ<2/5.

That last inequality is also checked independently with positive rational 96-term log enclosures. It is a genuine numerical constant of the original arithmetic source, not a new selected scalar.

### 2. Three genuine compactly supported smooth Schwartz tests, identical geometry and mass

Let the rational closed interval

    A = [-1099/1000, -5494/5000] = [-1.099,-1.0988]

lie strictly inside the left original collar L. The rigorous exact positive-rational log(9) bracket satisfies

    1.098 < -1.099 + log 9,
    -1.0988 + log 9 < 1.1.

Consequently \(A+\log9\) lies strictly inside R. There exists a nonzero REAL nonnegative \(C^\infty\) compactly supported function \(\phi\) with support contained in the interior of A (standard smooth bump construction); \(\phi\), regarded as a complex function, is Schwartz. Define

    δ := log9,
    ψ(x) := φ(x−δ).

Then ψ is a real compactly supported Schwartz function with support inside the unchanged original right collar. Their supports are disjoint and related by the ACTUAL exact arithmetic shift, not an approximate rational shift. Write

    J := ∫_ℝ φ(x)^2 dx = ∫_ℝ ψ(x)^2 dx > 0.

The same exact rational log brackets certify that for every actual original active prime-power index n in {2,3,4,5,7,8}, neither ±log n can shift the support of φ into that of ψ, and no ±log n can correlate a bump with itself. The n9 *same-cell* terms likewise vanish; the two ±log9 cross-orientations survive.

For any complex \(\beta\), set \(f_\beta=\phi+\beta\psi\). By the literal original second-unshifted/first-shifted source definition,

    C(f_beta,f_beta;+δ) = beta·J,
    C(f_beta,f_beta;−δ) = conj(beta)·J,

so the authentic old-original \(n=9\) prime sum is

    P_original(f_beta,f_beta)
      = κ [beta J + conj(beta) J]
      = 2 κ J Re(beta).

Choose exactly \(\beta=1,-1,i\). Because all \(|\beta|=1\), the three tests have EXACTLY the same support \(\mathrm{supp}\phi\cup\mathrm{supp}\psi\), the same old-collar signed graph (the two n9 edges), and the same genuine physical \(L^2\) mass:

    Mass(f_beta) = ||φ||² + |beta|²||ψ||² = 2J.

However their original genuine prime contributions are, respectively,

    P_original(f_1,f_1)    = +2κJ,
    P_original(f_{−1},f_{−1}) = −2κJ,
    P_original(f_i,f_i)    = 0.

The \(\beta=i\) case has two NONZERO individual imaginary signed correlations that cancel; its n9 geometric edges do not disappear. The \(\beta=-1\) case changes the sign of the original prime term without changing support, mass or prime graph.

### 3. An exact two-dimensional original PRIME matrix, not a new spectral Weil realization

On the selected span of the genuine Schwartz functions \(\phi,\psi\), let \(f=a\phi+b\psi\). Because the supports are disjoint,

    Mass(f) = J (|a|²+|b|²),
    P_original(f,f) = κJ [conj(a)b + conj(b)a].

In the ordered physical source basis \((\phi,\psi)\), the exact PRIME quadratic block is

           [ 0   κJ ]
    P  =   [        ].
           [ κJ  0  ]

After individually normalizing the bumps by \(1/\sqrt J\), this finite PRIME block has eigenvalues \(\pm\kappa\) and signature (1,1). This is **not** an independent spectral model and it is not the matrix of the entire Weil form: it excludes both original poles and the complete signed Gamma/digamma contribution, which must be retained before drawing conclusions about original Weil positivity. No negative FULL Weil direction or RH counterexample has been constructed.

The historical NF600 *absolute prime allowance* is consistent with this example because \(|P(f_\beta,f_\beta)|/Mass(f_\beta)≤κ<2/5\) in the displayed unit-phase family. Absolute bounds do not recover the missing phase.

### 4. New genuinely falsifiable compatibility obstruction IV030-N

**NO-GO statement:** There cannot exist a universal rule \(F\) such that for every complex Schwartz f supported in these original frozen collars,

    P_original(f,f) = F(Graph_Λ(supp f), Mass(f)),

even if F is given both directed signed shift orientations and the exact width/measure of the support. The three concrete genuine smooth tests above have the same graph, identical full supports and identical mass but three different values of the actual original prime quadratic term.

**Missing invariant:** the complex *off-diagonal amplitude and relative phase* of the physical mixed correlation, i.e. \(C(\phi,\psi;\tau)\) and its exact adjoint, not merely whether that coupling is geometrically possible. A projection comparison preserving only source support capacity, graph orientation and \(L^2\) norm is too weak to reconstruct the genuine original arithmetic pairing.

This NO-GO is relative to that proposed graph+mass-only reconstruction, NOT a no-go theorem against every possible spectral realization. A future independent spectral or arithmetic construction might still match the complete original Weil form if it preserves the complex sesquilinear mixed entries together with the original full signed pole and Gamma corrections.

**Falsification/independent checks:** An alleged target T that maps these three equal-mass/source-graph tests to the SAME prime quadratic value cannot preserve the original prime form. An exact target must distinguish +1, -1, and i relative phase, retain the first-slot conjugation, and preserve signed translations under argument swap. Conversely, simply presenting a target with the right 2×2 matrix above proves only the behavior of this PRIME restriction, not independent realization of full W.

### 5. Exact rational executable audit and provenance

\`scripts/iv030_original_prime_phase_no_go.py\` is a reproducible pure-stdlib Python \`Fraction\` sentry, **executed locally before commit**. Its exact checks include:

- the 96-term atanh-series rational log(9) and log(3) brackets, with rigorous nonnegative tail;
- strict containment of rational A in the unchanged original left collar and of A+log9 in the unchanged original right collar;
- absence of any other true von-Mangoldt-active prime-power interactions at either sign, plus self-separation;
- \(\kappa=\log3/3>0\) and \(\kappa<2/5\), consistent with the NF600 historical source;
- exact rational-complex phase coefficients \(+2,-2,0\) multiplying the symbolic positive \(\kappa J\);
- common mass \(2J\) and common source supports for the three unit-modulus phase choices.

The exact bump's positive \(J\) is kept symbolic: the script does not falsely compute an integral of an unspecified smooth function, and its step-free analytic construction is not an accepted Lean theorem. The actual finite 96-term logarithm bounds and complex-rational phase algebra were executed locally, and the exact Git blob hash of the committed script is checked against that executed local Python source.

**This script is NONKERNEL.** The genuine original \`NF600Prime_single\` and the actual original Schwartz-correlation dictionary are separately sourced, but the new three-test construction is not yet formalized and audited in Lean. The test does NOT establish that either the original full Weil form or the independent spectral target has a particular sign.

### 6. IV031 gate

**Primary:** recover actual compiled corrected IV009 Lean object and standard-axiom proof from the real queued job, or its first genuinely executed source error, without increasing the PR/push workflow fan-out. Then propagate IV025–IV029 source-specific custody corrections deliberately.

**Parallel separate cross-projection research:** test whether any genuinely independent proposed arithmetic/spectral model carries the three phase-distinguishable prime-pairing values under an explicit source/domain map, including both poles and the complete signed Gamma term. The selected finite prime block provides a falsifiable calibration object—not a spectral realization of the entire original Weil form.

Phase III NF### numerical original signed source certification is unaffected. No global Weil positivity, RH or external spectral equivalence is asserted.
