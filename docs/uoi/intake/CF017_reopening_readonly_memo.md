# Weil-Lab — CF017 Controlled Research Reopening

**Scope:** analytic/proof-preparation and read-only source audit. **No GitHub mutations, CI runs, Lean certificate claims, or accepted-frontier changes.** Current original HD/A frontier carried forward from the user's verified status: **692/968**.

## Highest-value immediate task

Formalize the **complex-polarized, phase-sensitive arithmetic discrepancy** and prove its **thin-packet local bound** on the actual logarithmic form carrier. This is a reusable control lemma for CF016's boundary screening problem, not a claim of global Weil positivity or RH.

### Exact objects

Use Fourier convention `F(ξ)=∫exp(-2πi xξ)f(x)dx` and `w(ξ)=log(e+|ξ|)`. Set

- `H_log(f)^2 = ∫w(ξ)|F(ξ)|^2 dξ`;
- `A_c={log n : Λ(n)>0, log n<2c}` and `κ_n=Λ(n)/sqrt(n)`;
- `C_fg(s)=∫f(x)conj(g(x-s))dx`, linear in `f`;
- `S_fg(s)=[C_fg(s)+C_fg(-s)]/2` (Hermitian-symmetric *as a pair*, not necessarily real);
- `D_c(f,g)=sum_{log n<2c} κ_n S_fg(log n) - ∫_0^{2c} e^{s/2} S_fg(s)ds`.

For supported tests `f,g`, the native pole-plus-prime mixed form satisfies the exact identity

`B_pole(f,g)+B_prime(f,g) = B_ref(f,g) - 2 D_c(f,g)`, 

where `B_ref(f,g)=2∫_0^{2c}exp(-s/2) S_fg(s)ds`, equivalently the positive-definite Fourier multiplier `1/(1/4+(2πξ)^2)`.

This is a **mixed Hermitian form identity**, not merely a real diagonal formula. The genuine pole is the two cross moments; do not replace it by `|M_-|²+|M_+|²`.

### CF017-A: uniform logarithmic thin-packet estimate

Suppose `f` is in the genuine logarithmic form domain, and `v∈L²` is supported in a measurable interval `I` of length `0<ell<=2c`. Write `S_c=sum_{log n<2c}κ_n`. For every `R>0`,

```
|D_c(f,v)| <= [S_c (sqrt(2 ell R) + 1/sqrt(log(e+R)))
                 + sqrt(ell (e^(2c)-1))] * ||f||_log * ||v||_2.
```

**Proof:** `|S_fv(s)| <= ||v||_2 [||f||_{L²(I+s)}+||f||_{L²(I-s)}]/2`. The prime sum is at most `S_c beta_f(ell)||v||_2`, where `beta_f(ell)=sup_{|J|<=ell}||f||_{L²(J)}`. Split `f=P_Rf+(1-P_R)f`. Fourier inversion/Plancherel give `||P_Rf||_{L²(J)}<=sqrt(2ell R)||f||_2`; high-frequency logarithmic energy gives `||(1-P_R)f||_2 <= ||f||_log/sqrt(log(e+R))`. For the continuous-reference integral, Cauchy-Schwarz in `s` and Tonelli give `∫_0^{2c}||f||_{L²(I±s)}² ds <= ell||f||_2²`, and `∫_0^{2c}e^s ds=e^(2c)-1`. Combine and use `||f||_2<=||f||_log`.

Taking `R=ell^(-1/2)` yields `|D_c(f,v)| = O_c(||f||_log ||v||_2 / sqrt(log(1/ell)))` as `ell→0`. The estimate retains all complex phases and requires no ordinary derivative of `f`.

If `k∈ker B_W` and `v=χ k` is a lawful smooth-cutoff endpoint packet, then `B_ref+ B_Gamma` against `(k,v)` equals `2D_c(k,v)`, and is bounded by this RHS. This is **a necessary boundary-screening inequality**, not contact exclusion.

### CF017-B: asymptotic sharpness in the one-prime window

Take `c=0.4`, `a=log 2`, `0<ell<min(2c-a,a,c)`. Let `v_ell=ell^(-1/2) 1_(c-ell,c)` and `f_ell=ell^(-1/2) 1_(c-a-ell,c-a)`. Both are supported in `[-c,c]` and belong to the logarithmic form domain. The only active prime power is `n=2`. Direct triangular-correlation integration gives

```
D_c(f_ell,v_ell)
 = log(2)/(2 sqrt(2)) - [8 sqrt(2)/ell] sinh(ell/4)^2
 -> log(2)/(2 sqrt(2)) > 0.
```

Meanwhile `||f_ell||_log² = log(1/ell)+O(1)` and `||v_ell||_2=1`. Thus the **order** `1/sqrt(log(1/ell))` cannot be improved uniformly for the normalized `||f||_log*||v||_2` bound. This shows why an arbitrarily narrow packet may retain a nontrivial prime-phase response when another packet is located at its genuine arithmetic translate.

### Required source dependencies

1. `WeilDefect/Arithmetic/ActualZetaNativeWeilForm.lean`: native mixed form and original prime sign/source normalization.
2. `WeilDefect/Morphology/NeutralLogPoleSourceAttachment.lean`: exact two cross-pole mixed moments.
3. `WeilDefect/Morphology/NeutralLogHilbertCarrier.lean`: supported log-energy carrier and form-domain identification.
4. `WeilDefect/Arithmetic/LogarithmicForm.lean`: certified weight `log(exp(1)+abs ξ)` and its Plancherel convention.
5. IV030 phase-dependence control: preserve Hermitian mixed pairing; no graph-only substitution.

### Lean proof decomposition (proposal, not a certified file)

1. Define the mixed autocorrelation and Hermitian symmetric shift pair `S_fg`.
2. Prove the pole-to-continuous-reference integral identity, both mixed slots, with exact Fourier factors.
3. Define `D_c` as a bounded mixed form and prove the native identity by algebraic substitution.
4. Prove the finite-band local interval mass estimate and logarithmic-frequency tail estimate.
5. Combine with translated-interval Cauchy-Schwarz to prove `CF017-A`.
6. Add the explicit two-rectangle sharpness family as an *analytic* test; if formalized, keep separate from the general theorem.

**Acceptance criteria:** exact signs/factors at `n=2`, real/imaginary polarization, endpoint threshold convention (`log n<2c`), smooth-density compatibility, no new axioms, no `sorry`, genuine Lean kernel compilation, and strict `#print axioms` audits. None is represented as completed Lean certification here.

### Local validation completed (read-only)

`cf017_discrepancy_validation.py` checks the pole/prime/reference identities for four complex test pairs on a piecewise-constant three-cell basis, Hermitian symmetry, the Stieltjes integration-by-parts representation, and recurrence of the one-prime phase. All tests passed, with identity residuals below `3e-7` (typically approximately `1e-12` or smaller). The explicit sharpness family was independently evaluated for collar widths `.100, .050, .020, .010, .005` and converged toward `log(2)/(2sqrt(2))`.

These are **numerical identity checks, not kernel certificates, certified intervals, or proof of inequalities**.

### Controlled submission preflight — BLOCKED

Read-only GitHub comparison found that the `research/nf753-original-indexzero-096-103-kernel-five-run-custody` and `research/nf756-scope-legacy-numerical-pr-trigger-fanout-wave-two` lineages **diverge** (`ahead_by=13`, `behind_by=8` on the NF756 side). The repository's `main` branch is at SHA `a117b3cf39d52643a2f33826fcbf8725cb5f86cf` (dated November 10, 2026) and cannot by itself be assumed to include the newer workflow repairs. This is **not proof of an unsafe branch**, but it fails the requested repaired-lineage attestation.

Before creating a CF PR: select a branch containing both accepted mathematical source ancestry and all required source-scoped workflow repairs; verify its ancestry by commit comparison; statically evaluate the complete `.github/workflows` set for the exact proposed changed-file list and count every `pull_request` match; inspect any unconditional wildcard triggers and reusable-workflow expansion; confirm that the expected fan-out is explicitly bounded; only then stage a small isolated research PR. No Actions or GitHub write occurred in this pass.

The initial analytic + local Python work requires **no GitHub Actions**. A later Lean kernel acceptance does require controlled CI only after those gates pass.

## Why this matters

The result replaces CF016's derivative-dependent prime-counting estimate with a logarithmic-form-domain bound that is both phase-sensitive and essentially sharp. It provides a falsifiable exact inequality for CF's boundary-screening program without assuming RH. It also gives a precise compatibility candidate for IV's phase-sensitive arithmetic projection, while making no unsupported equivalence claim.
