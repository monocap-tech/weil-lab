# NF530 — dependency-correct Lean builds and genuine smooth-correlation EF port

**2026-11-15 PT. Research draft, not accepted mathematical certificate.** Stacked on NF529 #557. The original NF494 full U400/H400 checksum `39cba367d70243c2d15e5a9323fc8097d58187923dcf0eca2b031136871f0181` remains unchanged; no original-source 400-coefficient replay in this NF.

## NF529 failure diagnosis

Focused GitHub Actions run [43781024141](https://github.com/monocap-tech/weil-lab/actions/runs/43781024141) finished **FAILURE BEFORE THEOREM TYPECHECKING**. The first line of `ActualZetaSourceQuadraticClosure.lean` failed with `unknown module prefix 'WeilDefect'`, because the workflow ran `lake env lean <source.lean>` without first building the repository-local `.olean` dependencies. That is an infrastructure error; no positivity or closure theorem was refuted or accepted. NF530 changes the dedicated workflow to `lake build WeilDefect.Arithmetic.ActualZetaSourceQuadraticClosure` to follow the actual import DAG.

## New generic full-multiplicity literal EF theorem target

New module: `WeilDefect/Arithmetic/ActualZetaSmoothLiteralFormula.lean`. It is the first direct *generic physical-window correlation* imported zeta EF lemma on this branch, with NO Green-synthesis restriction. For arbitrary `f g : RealComplexL2` and fixed `a`, it takes precisely:
(1) `ContDiff ℝ 2` of their authentic correlation;
(2) compact support is automatically obtained from already proved `neutralWindowCorrelation_hasCompactSupport`;
(3) the only other outstanding premise is `Summable` of the actual all-copy divisor series `conj(F_f(conj z_q)) F_g(z_q)`.
It proves that same **complete actual zeta-divisor copy series** equals `Zeta23.EF.literatureRHS (neutralWindowCorrelation a f g)`, preserving exact von Mangoldt, gamma-bracket and pole contributions. Proof references only existing `neutralWindowCorrelation_rawTransform`, `neutralActualZetaDivisor_tsum_literature`, and genuine imported `Zeta23.WeilEF.EF_lit_zeta`.

This lemma is now a Lean proof **candidate**, NOT yet accepted; the new dedicated workflow builds this module too. Only C² regularity and complete divisor-sum summability remain to be specialized for strict smooth collar tests. Compact support is discharged generically by existing Lean code.

## Quantitative full-source graph closure

The existing signed source quadratic with the authentic additional 1/sqrt(2) normalization satisfies, analytically on full Hilbert source graph H:
`|Q(h)-Q(k)| <= 1/2 (||h||_H+||k||_H)||h-k||_H`.
This makes the condition `Q>=c||physical||_2²` closed in source graph norm. The existing NF529 four-theorem Lean closure module is now built by Lake instead of invoked without its imports. Passing these lemmas alone does **not** prove NF527 two-collar positivity or original endpoint smooth graph membership.

## Actual local replay performed in NF530

Three previous exact Fraction executables were rerun locally and produced PASS:
- NF526: true original endpoint geometry admits only the prime-power n=9;
- NF527: 20-term gamma gain at |t|=30 >67/10, arch lower 133/250, full positive signed margin 1/10;
- NF528: eight strict collar-contraction margins and ten conjugate-partner P/N exact rational algebra rows.

These finite checks did not recompute original NF494 U400; do not certify complete infinite-dimensional signed forms or Lean theorem compilation. Local receipts are separate from GitHub CI.

## Strict NF530 stopping points

The dedicated [NF530 CI run](https://github.com/monocap-tech/weil-lab/actions/runs/43781700861) has been initiated; **its success must be checked**, not inferred. The imported EF is genuine, but compact C∞ collar correlation admissibility, source divisor uniform decay for the collar-only smoothing, and the gamma/primes/poles 1/10 coercivity inequality have not yet been Lean compiled. Original ell_U zero-side sign >3.2e-33 remains **analytic conditional** on inherited NF523–NF528 premises, not newly source-certified by this PR. Green observability, global odd/even positivity, W_ODD_NEG and RH remain OPEN.

**NF531:** Investigate and fix *actual* Lean errors, if any, from the dependency-correct build; compile smooth collar admissibility and universal 1/10 source lower bound separately, then the original graph-closed transfer.