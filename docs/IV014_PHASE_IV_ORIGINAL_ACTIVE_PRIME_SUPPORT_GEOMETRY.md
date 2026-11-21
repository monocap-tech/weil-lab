# Weil-Lab — IV014
## True von-Mangoldt-active mixed support geometry and pole/Gamma residual gate

**Canonical iteration:** IV014, the independent Phase IV research line (not Phase III NF numerical production).
**Stack:** IV006 PR #766 → IV007 #767 → IV008 #769 → IV009 #771 → IV010 #773 → IV011 #774 → IV012 #778 → IV013 #779 → IV014 (this branch).
**Formal status:** ten new source-specific Lean theorem PROOF CANDIDATES, four upstream source axiom anchors, independent pinned Lean CI **PENDING**. Theorems here are not claimed kernel accepted without the successful real build and strict audit artifact.

### 1. A genuine loosening of IV013's geometric restriction

IV013 defined its prime-separated Schwartz physical test pair `s,t` by requiring no translated overlap at **every** integer n below the exact logarithmic cutoff N:

    t(x)=0 OR [s(x−log n)=0 AND s(x+log n)=0]  for every n<N and every x.

But the original mixed zeta prime side is NOT an unweighted integer sum:

    P_b(s,t) = Σ'_{n∈ℕ} Λ(n)/√n
        [ C_b(s,t)(log n) + C_b(s,t)(−log n) ].

The true `ArithmeticFunction.vonMangoldt n` can vanish. In particular, requiring geometric nonoverlap for all integers introduces **spurious restrictions** whenever the actual arithmetic coefficient is zero.

IV014 defines the genuinely source-active support condition

    ActivePrimeSeparated_N(s,t) :⇔
      ∀ n<N, Λ(n)≠0 →
        ∀ x, t(x)=0 OR
          [s(x−log n)=0 AND s(x+log n)=0].

It includes all actual nonzero von-Mangoldt prime-power contributions and deliberately makes **no restriction at zero-weighted integer frequencies**. There is no new prime oracle or edited coefficient.

IV013's stronger condition implies the new one by direct specialization. The reverse is not assumed.

### 2. Two independent EXACT source-side consequences

For an old Schwartz input s supported in `[-a,a]`, newly admitted t supported in `[-b,b]`, a≤b, take the genuine original correlation

    C_b(s,t)(τ) = ∫_{ℝ} t(x) conj(s(x−τ)) dx

from IV011. Under the active condition at n with Λ(n)≠0, both true samples vanish pointwise:

    C_b(s,t)(log n)=0,
    C_b(s,t)(−log n)=0.

For Λ(n)=0, the original sum vanishes from its literal **coefficient**, with no claim that the Schwartz correlation vanishes. Consequently, for a genuine IV011 source cutoff `∀n≥N, log n > a+b`:

    P_b(s,t)=0.

The new mathematical improvement over IV013 is that the strict separation assumptions are needed only for arithmetic-active n, not every n.

IV014 also derives a stronger conclusion for the **nonnegative physical overlap budget** from IV012:

    J(s,t;τ) := ∫ |t(x)| |s(x−τ)| dx.

At active n the entire absolute overlap is zero; inactive n contribute zero multiplied by original Λ(n). Thus

    E_prime,N(s,t)=
      Σ_{n<N} Λ(n)/√n [J(s,t;log n)+J(s,t;−log n)]
      =0.

This is stronger than relying on complex integral cancellation and makes IV012's absolute arithmetic envelope lose its whole prime component.

### 3. Finite physical interval-gap criterion

The new geometric theorem accepts *arbitrary Schwartz functions with interval source bounds*:

    support(s) ⊆ [cs−rs, cs+rs],
    support(t) ⊆ [ct−rt, ct+rt].

It uses a directly finite, checkable test on centers and radii for every arithmetic-active n<N:

    rs+rt < |ct−cs−log n|,
    rs+rt < |ct−cs+log n|.

These inequalities imply the whole pointwise active-prime separation condition. The proof is the precise translated-overlap obstruction: if a physical x lay simultaneously in t's interval and in either signed translated copy of s's interval, the corresponding center gap would be **at most** rs+rt, contradicting its strict separation.

**Important feasibility boundary:** this theorem permits nonzero Schwartz tests with sufficiently small supports, but it does not itself construct a nonzero Schwartz bump, certify a particular numerical interval/log bound, or prove that an arbitrary old frozen source family admits such a new test. Those are separate formal tasks.

An illustrative, **not Lean-certified**, geometric search near the original collars would take an old positive-collar narrow interval centered near 1.099 and a candidate new narrow interval near 0.2. Their center gap is near 0.899, away from the low-frequency active log 2≈0.693 and log 3≈1.099. A rigorous concrete bump witness and all relevant finite inequalities must be checked before this can be promoted into a constructed source theorem. Merely moving inside the same enclosing window is still an enlargement of the test CLASS beyond the original collars; it does not demonstrate positivity at larger window radii.

### 4. Exact original pole/Gamma residual only

With original pole and Gamma terms unchanged, write

    R_b(s,t) = literalPole_b(s,t) + literalGamma_b(s,t).

The true original arithmetic Weil pairing now reduces exactly to

    W_b(s,t)=R_b(s,t),

in the arithmetic-active prime-separated class.

The IV012 full absolute envelope also reduces exactly to

    E_N(b;s,t) =
      E_pole(b;s,t)+E_Gamma(b;s,t),

and the true mixed norm is bounded by this pole-plus-Gamma residual:

    ‖W_b(s,t)‖ ≤ E_pole(b;s,t) + E_Gamma(b;s,t).

This is an exact and quantitatively sharper source-specific inequality in a restricted geometric class. The two genuine polar moments and the unchanged Gamma/digamma integral remain; they are not discarded or assigned a favorable sign.

### 5. Sharp conditional original one-new-source positivity

As in IV010–IV013, for an old finite original physical Schwartz combination `S=Σ_i u_i•s_i`, an additional test `t`, old signed energy A, and new diagonal D:

    Re W_b(S+v•t,S+v•t)
      = A+2Re(W_b(S,t)*v)+D|v|².

Under arithmetic-active separation of S,t, the mixed norm admits the original pole/Gamma budget bound. Thus **if**, in addition,

    A≥0,
    D≥0,
    [E_pole(b;S,t)+E_Gamma(b;S,t)]²≤A*D,

then the sharp original mixed Schur inequality follows, and the actual diagonal is nonnegative for all v∈ℂ.

The last two requirements (especially `D≥0` and the residual-square comparison) remain **UNPROVED new-support analytic obligations**. Prime-free geometry does not imply either.

### 6. Formal theorem and audit ledger

New Lean file:
`WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalActivePrimeSupportGeometry.lean`.

Ten new source-specific theorem candidates:

1. `neutralIV014ActiveSeparated_of_strong`
2. `neutralIV014ActiveCorrelation_vanish`
3. `neutralIV014ActivePhysicalOverlap_zero`
4. `neutralIV014ActiveFinitePrimeBudget_zero`
5. `neutralIV014ActiveMixedPrime_zero`
6. `neutralIV014ActiveMixed_eq_analytic`
7. `neutralIV014ActiveSeparated_of_intervalGap`
8. `neutralIV014ActiveArithmeticBudget_eq_residual`
9. `neutralIV014ActiveMixed_norm_le_residualBudget`
10. `neutralIV014ActiveOneNew_nonnegative_of_residual`

Strict source-bound audit:
`scripts/iv014_original_active_prime_geometry_audit.py`.

Independent workflow:
`.github/workflows/iv014-original-active-prime-support-geometry.yml`.

The workflow builds the full actual original Lean module, checks all ten new and four upstream original `#print axioms` declarations with only standard Lean axioms `propext`, `Classical.choice`, `Quot.sound`, rejects `sorryAx` and unauthorized source-level axioms, requires an actual compiled `.olean`, and SHA-256 binds the exact original dependency files and proof artifact.

### 7. Kernel recovery, as checked during IV014 creation

- IV006 genuine original window naturality and IV007 genuine finite mixed family naturality: **Lean + strict axiom PASS**.
- IV008 genuine original mixed Hermitian source: **Lean + strict axiom PASS** after the actual complex `star`/conjugation repair; run 44836233452.
- IV009 initial recovery compiled enough to reveal an exact genuine divisor-summability `starRingEnd`/conjugation expression mismatch. Its next source repair changed the source summability term definitionally; the corresponding obsolete rawTransform-token source-preflight assertion was also repaired. **The recent fresh runs were still queued/pending when IV014 was prepared.**
- IV010–IV013 real Lean acceptance depends on the successfully compiled IV009. Their own new declarations and source audits are **not** accepted merely because their source files exist.

Do not infer kernel success from a green upstream IV008 job, a source preflight, or a queued IV009/IV013/IV014 job.

### 8. Next — IV015

A mathematically meaningful further step would construct a NONZERO literal compactly supported complex Schwartz bump inside an explicit interval gap, with exact rational/real finite logarithmic inequalities against each relevant original active prime-power shift. The candidate support should be genuinely newly admitted beyond the old narrow original collars. Then study the **remaining exact two-pole-plus-Gamma residual** and its real new-support diagonal, rather than implying that zero prime terms imply positivity.

**What is not proved:** existence of a certified nonzero admissible new Schwartz witness, an unconditional new mixed Schur bound, a new-support diagonal sign, positivity at any enlarged radius, global Weil positivity or RH. Phase III original numerical certification remains a separate NF### track.
