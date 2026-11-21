# Weil-Lab — IV018
## Direct original three-cell signed coercivity: remove the mixed Schur premise by preserving the authentic n=9 prime term

**Canonical independent Phase IV head:** IV018; stacked on IV017 PR #785 → IV016 #784 → IV015 #783 → IV014 #781 → IV013 #779 → IV012 #778 → IV011 #774 → IV010 #773 → IV009 #771 → IV008 #769 → IV007 #767 → IV006 #766. Not Phase III NF### numerical matrix certification.

**Kernel status on source creation:** TWO new original Lean proof modules with TWENTY new theorem **CANDIDATES**, EIGHT genuine upstream axiom-audit declarations, pinned direct Lean/Mathlib workflow and exact-Fraction source preflight. No IV018 real compiler acceptance has yet been observed. The proposed unconditional one-quarter positivity for the restricted three-cell physical test class MUST NOT be reported as proved until both modules, all dependencies and all source-bound strict-axiom audits PASS the kernel.

## 1. Mathematical breakthrough relative to IV017: bypass the mixed Schur inequality

IV017 proposed a quantitatively new diagonal bound for Schwartz tests t concentrated in [0.199,0.201], but left a difficult original old/new mixed Schur inequality `|W(S,t)|² ≤ A D`. Such a mixed cross-term estimate generally does NOT follow from positive diagonals.

IV018 takes a different route: study the ORIGINAL SIGNED Weil quadratic value directly on the UNION of all old and new allowed physical supports, rather than trying to extend positivity one diagonal at a time.

The unchanged historical NF543 strict original collars are

    E_old =
      Ioo(-11/10, -11/10 + 1/500)
      ∪ Ioo(11/10 - 1/500, 11/10).

The newly admitted source interval is

    E_new = [199/1000,201/1000].

The actual enlarged source region is the THREE-CELL union

    E_3 = E_old ∪ E_new,

and all three cells lie within the SAME original physical cutoff window [-11/10,11/10]. No frozen source, divisor, pole, gammaBracket or coefficient is modified.

For EVERY genuine complex Schwartz physical function f supported in E_3, two authentic source bounds do not need to know whether f came from a finite old-plus-new combination. These are uniform over the whole three-cell support class.

## 2. Exact physical volume and Fourier uncertainty

The original two strict collars have total real Lebesgue measure exactly 1/250 (NF600). The new closed interval has measure 1/500. The three cells are disjoint, hence

    volume(E_3) = 1/250 + 1/500 = 3/500.

Actual Schwartz Cauchy–Schwarz and true source Plancherel give

    ‖f‖_(L¹)² ≤ (3/500) Mass(f),
    Mass(f) := ‖f.toLp 2 volume‖².

The true unitary Fourier pointwise L¹ bound gives

    |Fourier(f)(ξ)|² ≤ ‖f‖_(L¹)²,

and therefore the existing NF600 fixed real-frequency low band (-5,5), of length exactly 10, carries at most

    LowMass(f) ≤ (3/50) Mass(f).

This is sharper than naively paying the full original physical 2.2-length window. It exploits the authentic geometry of the THREE source cells, not a surrogate abstract matrix.

## 3. The actual original signed Gamma contribution

NF599 already proved genuine Gamma/digamma symbol bounds for the original zeta explicit formula:

    gammaBracket(r) > -28/5  for ALL real r;
    gammaBracket(r) >  11/10 for |r|≥30.

NF600 proved that |−2πξ|≥30 outside the fixed low band (-5,5). The original signed Archimedean diagonal is the full, unchanged real-frequency integral

    Arch(f) =
      ∫_{ℝ} gammaBracket(−2πξ) |Fourier(f)(ξ)|² dξ,

using the source-exact original correlation spectral identity, now generalized to any Schwartz test supported in the same authentic physical window by IV017's source candidate.

The symbol bounds give the exact signed inequality

    Arch(f) ≥ (11/10)Mass(f) − (67/10)LowMass(f).

Using LowMass≤(3/50)Mass:

    Arch(f) ≥ (11/10 − (67/10)*(3/50))Mass(f)
            = (349/500)Mass(f).

This is a SIGNED coercive estimate of the true Gamma integral, not IV012's absolute envelope.

## 4. Retaining BOTH true original poles

The original half-pole source moments M_±(f) at ±1/2 satisfy the existing window-specific real bound

    |M_±(f)| ≤ 2‖f‖₁

for every function supported inside the original physical window. Hence BOTH genuine pole residues cost at most

    |Pole(f,f)| ≤ 8‖f‖₁² ≤ (24/500)Mass(f)
              = (6/125)Mass(f).

The *analytic* (pole + Gamma) part of the ORIGINAL signed Weil diagonal on E_3 is therefore bounded below by

    Re[originalPole(f,f) + originalGamma(f,f)]
      ≥ (349/500 − 6/125)Mass(f)
      = (13/20)Mass(f).

This calculation does not claim that the original prime sum is zero. That would be FALSE for general old-collar Schwartz tests, because a genuine n=9 prime-power cross-collar translation can survive.

## 5. The genuine original n=9 prime, not a discarded term

NF600 proved from the unchanged source support and the *actual original von Mangoldt series*:

1. For any old `S` supported in E_old, every active original logarithmic prime translate except n=9 has zero original physical correlation.
2. At n=9, both genuine signed ±log9 old-collar correlations are bounded individually by Mass(S)/2.
3. The actual von Mangoldt coefficient satisfies `Λ(9)/sqrt(9) ≤ 2/5`, so the full original prime term satisfies

    |Re P_original(S,S)| ≤ (2/5)Mass(S).

These are actual NF600 source theorems, **not** an invented prime cutoff.

For any genuinely newly admitted t supported in E_new, any old S and every v∈ℂ, IV018 targets the much stronger exact source identity

    P_original(S+v•t,S+v•t) = P_original(S,S).

The proof uses the IV016 exact numerical gap around c=1/5 and its self-prime clearance, and proves pointwise for every active m<10:

    C_original(S+v•t,S+v•t)(+log m)
      = C_original(S,S)(+log m),

    C_original(S+v•t,S+v•t)(−log m)
      = C_original(S,S)(−log m).

All old-new, new-old and new-new REAL complex translated products vanish by physical support; no accidental sesquilinearity is assumed. Inactive indices have their ACTUAL Λ=0 coefficient. Every n≥10 is eliminated by the rigorously pinned original log(10)>11/5 support cutoff.

Importantly, the mixed, new-new and old-old original sources have different arithmetic behavior:
- old-old n=9 may survive and is paid as NF600 source;
- old-new and new-old are exactly separated at all active prime powers;
- new-new is exactly separated at all active prime powers.

Physical old/new support disjointness also gives

    Mass(S+v•t) = Mass(S) + Mass(v•t) ≥ Mass(S).

Consequently the authentic complete original prime term of the enlarged test obeys

    |Re P_original(S+v•t,S+v•t)|
      ≤ (2/5)Mass(S)
      ≤ (2/5)Mass(S+v•t).

The new prime-bound proof is NOT an assumption; it is the main separate IV018 source-specific kernel proof CANDIDATE, relying on actual NF600 accepted old n=9 theorems and IV015/IV016 geometric certificates.

## 6. FULL original one-quarter coercivity on the expanded three-cell family — KERNEL CANDIDATE

Let `f=S+v•t`, where S is any original two-collar Schwartz function, t is any Schwartz function supported in E_new and v is ANY complex coefficient. The genuine original signed arithmetic zeta EF is

    Re W_original(f,f)
      = Re originalPole(f,f)
        − Re originalPrime(f,f)
        + Re originalArch(f,f).

The true exact source bounds give

    Re W_original(f,f)
      ≥ (13/20)Mass(f) − (2/5)Mass(f)
      = (1/4)Mass(f).

The principal NEW theorem candidate is:

    neutralIV018OriginalOldPlusNew_oneQuarter_coercive:
      (1/4)*‖S+v•t‖_(L²)²
        ≤ Re W_original(S+v•t,S+v•t).

The original two strict collars, new interval and SAME 11/10 physical window appear in this theorem; there is NO hypothesis on original mixed Schur, separate old/new diagonal signs, or any version of RH.

The next theorem applies the statement to a true finite family of old source vectors:

    S = Σ_i u_i • s_i,

and proves the candidate bound simultaneously for every complex old coefficient vector u and every new coefficient v.

The final source theorem candidate constructs an ACTUAL nonzero complex Schwartz bump t centered at c=1/5, with t(c)=1 while every old original collar test vanishes at c, and quantifies this same 1/4 original Weil inequality uniformly for all such u,v.

**This is a potential genuine source-support extension with a quantitative margin that bypasses the mixed Schur obstacle.** Its certification is entirely contingent on actual Lean kernel acceptance. It is not global Weil positivity because E_3 is only a specially chosen finite union of tiny physical support cells, not the space of all admissible Weil tests.

## 7. Audit ledger

The new FIRST module `WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalThreeCellSignedEnvelope.lean` contains ten original-source candidates:

1. `neutralIV018OldNew_disjoint`.
2. `neutralIV018ThreeCell_volume`.
3. `neutralIV018ThreeCell_supported_window`.
4. `neutralIV018ThreeCell_L1_bound`.
5. `neutralIV018ThreeCell_L1_sq`.
6. `neutralIV018ThreeCell_lowMass`.
7. `neutralIV018ThreeCell_signedGamma_lower`.
8. `neutralIV018ThreeCell_poleReal_lower`.
9. `neutralIV018ThreeCell_analyticReal_lower`.
10. `neutralIV018ThreeCell_oneQuarter_of_primeBound` — explicitly conditional on its genuine prime bound.

The new SECOND module `WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalThreeCellPrime9Transfer.lean` contains ten original-source candidates:

1. `neutralIV018OldPlusNew_supportedThreeCell`.
2. `neutralIV018OldPlusNew_mass_add`.
3. `neutralIV018OldMass_le_expandedMass`.
4. `neutralIV018ExpandedCorrelation_eq_old_of_threeZeros`.
5. `neutralIV018ExpandedActiveCorrelation_eq_old`.
6. `neutralIV018ExpandedPrime_eq_old`.
7. `neutralIV018ExpandedPrime_real_bound`.
8. `neutralIV018OriginalOldPlusNew_oneQuarter_coercive`.
9. `neutralIV018OriginalFiniteOldPlusNew_oneQuarter`.
10. `neutralIV018ExistsGenuineNewThreeCellPositiveDirection`.

**Twenty NEW original-source Lean theorem candidates**, plus EIGHT real source axiom anchors, across two modules.

Independent auditor:
`scripts/iv018_original_three_cell_coercivity_audit.py`.
It checks every exact Fraction rational identity for original volume, original signed Gamma, BOTH poles, NF600 n=9 prime cost and final 1/4 coefficient, with no floating-point trust, and verifies exact source dependencies and 28 strict `#print axioms` target names.

Dedicated pinned Lean/Mathlib kernel workflow:
`.github/workflows/iv018-original-three-cell-signed-coercivity.yml`.

A verified PASS requires both ORIGINAL .olean objects, all 20 new and eight upstream exact source-bound standard-axiom receipts (only `propext`, `Classical.choice`, `Quot.sound`), no `sorryAx`, and SHA-256-bound original source dependencies/toolchain/Lean objects. In particular, source preflight or a green exact-rational ledger is **NOT** evidence that the IV018 one-quarter theorem has been accepted by Lean.

## 8. Current distinction and next stage

- IV006–IV008 genuine original Lean source kernel/axiom audits: accepted as previously recorded.
- IV009's source recovery was still in progress on the last live Actions check; IV015 and IV016 were queued. IV017 and IV018 source candidates have no terminal kernel PASS at creation.
- The full original three-cell source-specific coercivity is therefore **UNVERIFIED BY LEAN**. It must be treated as a proposed theorem until the full dependency chain and strict original source kernel audits succeed.
- It is not a complete Phase III physical numerical enclosure, a general global Weil support theorem, or RH.

**Next IV019:** recover actual IV009–IV018 Lean compiler results and repair any original source elaboration/axiom errors; then investigate extension from one chosen new narrow cell to multiple admissible cells without allowing new prime-power overlap modes. Growth of the support set may cause additional active von-Mangoldt translations and destroy the 1/4 margin — this is a genuine arithmetic-geometric threshold that must be certified, not assumed.
