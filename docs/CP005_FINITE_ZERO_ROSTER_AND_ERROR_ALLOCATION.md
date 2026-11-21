# Weil-Lab — CP005
## Certified finite-zero roster adapter and an exact-error allocation for the original signed Weil compression

**Cross-projection CP### only:** stacked on CP004 PR #803 → CP003 #799 → CP002 #796 → CP001 #790. Preserve original Phase IV IV022 PR #800 (and its future IV### descendants), Phase III NF###, and PI### tracks without mutation. The CP004 companion original-source Lean PR #802 remains a separately pending original-source bridge.

**Status:** a new external finite-height Lean proof lead is identified, an exact rational smaller-height tail and robust error allocation are calculated, and a fail-closed data-adapter/receipt schema is added. **NOT** a direct build/audit of that external Lean proof inside Weil-Lab; **NOT** a complete enumerated and verified zero roster inside this branch; **NOT** the first full 3×3 arithmetic–spectral matrix comparison. No global Weil positivity/RH is claimed.

## 1. New external finite-height proof resource

**Source:** `smmercuri/zeta`, public GitHub repository, tag/release `v1-1e6` (commit prefix `c06b4e1`, inspect/record the complete immutable commit before importing any bytes). Its release states the theorem `Zeta.riemannHypothesisUpTo_1000449`, a Lean-kernel-checked RH-to-height 1,000,449 with only the standard axioms. The README reports **1,748,002** positive-height zeros certified up to the first Gram point `g≈1,000,449.797` above this target, with Turing completeness. The distinction between the integer theorem height and the actual Gram cutoff is important.

**Trust-layer distinctions in the upstream README:**
- `Zeta.*` kernel certificates use only `propext`, `Classical.choice`, `Quot.sound`; `Native.*` adds native trust. CP005 must NEVER silently substitute the latter.
- The published `1e6` release carries a Linux x86_64 prebuilt archive, whose import requires matching Lean toolchain/Mathlib and `module` syntax. Weil-Lab's existing IV### Lean imports are not presumed compatible.
- The README explicitly warns the default zero brackets are **maximized to tile the range**, intentionally compromising ordinate precision; a separate `1e4-prec` branch demonstrates narrower bisection enclosures. The `1e6` release's *count and RH-to-height theorem do not themselves certify that every exported ordinate bracket has width ≤2·10^-9*.
- Individual zero intervals need to be exported with their exact rational endpoints, a SHA-pinned source data archive, kernel/trust receipts, a proved correspondence between the listed intervals and original certified batch indices, and an exact count. A raw Odlyzko or LMFDB approximate text list is not a substitute.

Published proof baseline: Platt–Trudgian (2021) independently verifies RH up to height 3e12. This can be an additional finite-line-location cross-check but does NOT provide the CP005 required precise full list and Mellin-compression estimates.

### 1.5. Exact upstream source and *identified toolchain incompatibility*

GitHub API inspection of the immutable release resolves `v1-1e6` to commit **`c06b4e13d9c847e50a32c3d738271cbad62ae9f3`**. The release advertises the x86_64 prebuilt library with published SHA-256 **`f777b515af89a486654052f0052b8f6760e822c88c15e0be8af753c9542c2ea2`**; this is metadata, NOT a downloaded-and-rehashed certificate in CP005. The source `Zeta/Main.lean` explicitly contains the desired theorem `Zeta.riemannHypothesisUpTo_1000449` and the additional `Zeta.simpleZerosUpTo_1000449`, with source-level standard-axiom `#guard_msgs` assertions.

Importantly, `Zeta/Zeros/CountCertificates.lean` declares the original `certifiedZeroCount : CertifiedZeroCount` with a real Turing `count` proof and a `below` proof, sourced from the generated Gram-block and individual zero-interval bundles. `Zeta/Zeros/RiemannHypothesisUpTo/Basic.lean` contains the exact theorem
`
  riemannZeta.N_gramPoint_eq (Z : CertifiedZeroCount) :
    riemannZeta.N (gramPoint Z.minIdx) = Z.intervals.length
`
plus simplicity and no-off-line-zero consequences. This is the precise missing **zero-roster ↔ Turing completeness dictionary**, not merely a general finite-height RH assertion. It still must be applied to the *exported specific interval rows* with a verified hash/ordering map.

**Hard current dependency mismatch:** Original Weil-Lab IV022 has `leanprover/lean4:v4.34.0` and Mathlib `v4.34.0`. External `smmercuri/zeta@v1-1e6` has **Lean v4.35.0 / Mathlib v4.35.0** and a separately pinned `PrimeNumberTheoremAnd` dependency. Consequently **do not add a direct Lake `require Zeta` to the existing Phase IV branch** or import its public `.olean` with the wrong toolchain. For CP006, use a separate pinned v4.35 formal adapter and explicit mathematical statement export, or an independently proved compatibility port. Avoid silently upgrading canonical Phase IV.

## 2. Replace CP004's T=2^20 with a certifiably reachable boundary

Set the **finite spectral cutoff at the first certified Gram point** `g` *above* 1,000,449, with all 1,748,002 positive-height zeros counted below it, and rigorously prove `g>1,000,000`. Do NOT equate the integer height 1,000,449 with this Gram point. Rather than trying to guess the exact number `N_+(1,000,000)`, include all certified intervals through `g`. Since `g>10^6`, the remaining zero tail is a subset of the tail above `T_0=10^6`, for which the previous CP003 unconditional zero-count argument applies.

Define `h0=1/2000`, `r∈{1/1000,1/500}`, `M(h)=32/h+4+h`, and the exact rational constant
`
 K0 = 2/(10^6)^3 * ((8/7)*21 + 8/49).
 E_tail(r) = K0*(9/4)*(2*M(h0)^2/h0+M(r)^2/r).
`
The use of `21` is conservative: `log(2·10^6)<21` because `e>2` and `2^21>2·10^6`; `log 2<1` also follows from `e>2`. The HSW count `N_abs(U)≤U log U` remains unconditional and requires neither full RH nor a missing-zero hypothesis at unbounded height.

**New exact Fraction calculation:**
`
 E_tail(1/1000) < 0.001894 < 1/500;
 E_tail(1/500)  < 0.001796 < 1/500.
`
Both are strictly below 0.002. This is an explicit tail **bound conditional on CP003's bump derivative/mass estimates and the full zero-side form normalization**, not a certified finite sum of roots.

## 3. Error transfer from independently proved zero brackets to cosine moments

Use CP004's real-even profile transform
`
 Phi(y)= ∫_-1^1 phi(u)cos(yu)du,
 J_ij(gamma)= 2*h_i*h_j*Phi(h_i*gamma)*Phi(h_j*gamma)*cos((c_i-c_j)*gamma),
 (h_i)=(h0,h0,r), (c_i)=(-1099/1000,+1099/1000,1/5).
`
`0<=phi<=1` immediately implies `|Phi|<=2` and `|Phi'|<=∫_-1^1 |u|du=1`. For every positive zero ordinate `gamma`, exact product differentiation gives
`
 |J'_ij(gamma)| <= 4*h_i*h_j*(h_i+h_j) + 8*h_i*h_j*|c_i-c_j|.
`
The normalized physical masses satisfy `m_i=h_i*a2` with `a2>24/25` as established by CP003's rational bump mass preflight. Using `sqrt(h_i h_j) <= (h_i+h_j)/2`, one obtains the rational **row-sum** operator perturbation upper bound, provided every certified ordinate bracket has a midpoint `gammahat_k` with half-width at most `delta=10^-9`:
`
 E_loc(r) = N*delta* max_(i=0,1,2) sum_(j=0,1,2)
    (25/24)*(h_i+h_j) *
            (2*(h_i+h_j)+4*|c_i-c_j|),
 N=1,748,002.
`
The spectral matrix is real symmetric. The spectral norm is no more than its maximum absolute row sum, so `E_loc` is a true **operator**, not merely entrywise, allowance. The full normalized approximation error includes this ordinate-localization term and a separate rigorous cosine/profile quadrature term.

**Exact rational error allocation at the certified Gram point**, assuming an independent normalized quadrature/rounding enclosure `E_quad<=1/50000` (currently OPEN):
`
 r=1/1000: E_tail + E_loc + E_quad < 0.001944 < 1/500;
 r=1/500:  E_tail + E_loc + E_quad < 0.001856 < 1/500.
`
The CP005 executable actually checks the STRICT rational inequality `E_tail(r)+E_loc(r)+1/50000<1/500`, rather than accepting these rounded decimals as evidence.

If the upstream certified intervals are wider than 2×10^-9 (as is likely for the default maximized-interval setting), **the manifest is NOT READY**. The proper next work is to generate and certify *refined* brackets linked to the upstream kernel/Turing count—not to round the published intervals to narrower bounds.

## 4. Fail-closed CP005 adapter, without invented root data

New script `scripts/cp005_formal_zero_roster_adapter.py` supports:

- `--self-test`: independent pure-Fraction verification of both E_tail/E_loc budgets and several synthetic gate failures.
- `--roster FILE --manifest MANIFEST`: stream a file of rational ordinate brackets (CSV lines `lower,upper`) and check exact row count `N=1748002`, positivity, strict ordering, actual half-width ≤1e−9, finite-range placement below the stated Gram-point interval, and SHA-256 digests.
- Require a pinned upstream `v1-1e6` tag, claimed kernel `Zeta.riemannHypothesisUpTo_1000449`, explicit no-native axiom trust, and independent external proof-attachment metadata. The actual source materials must be fetched, verified and imported separately. Merely writing metadata or checking a hash cannot verify a theorem.

The adapter **never prints LEAN_PASS or CERTIFIED_SPECTRAL_COMPARISON**. Even with well-formed complete-length data it emits `STRUCTURAL_PREFLIGHT_ONLY`, pending live verification of the upstream Lean axiom receipt, the claimed correspondence from individual interval IDs to certified zeros, and the *entire original arithmetic and spectral mixed dictionary*. If data or manifest is absent, its result is `NOT_READY`. Synthetic negative controls are explicitly labeled.

No fake 1,748,002-row file is committed.

## 5. Required full original source interface

The CP004 original Lean bridge PR #802, based on the IV022 original-source branch, introduces **candidate** wrappers for:
`neutralCP004OriginalCorrelationIntegral`,
`neutralCP004OriginalPrimeFiniteTen`,
`neutralCP004OriginalPrimeSingleN9_of_otherTermsZero`,
`neutralCP004OriginalPrimeZero_of_allTermsZero`.
The actual CP001 analytic bump function `phi((x-c)/h)` is NOT yet constructed as a source-bound `𝓢(ℝ,ℂ)` term in Lean; existing Mathlib smooth bumps are not definitionally this exact explicit `phi`. Establishing explicit `phi` smoothness, original window membership, the exact n9 overlap and all 288 real gap cases, and the mass/derivative enclosures is a genuine new formalization obligation, not something CP005 can infer from the prior generic wrappers.

Other unresolved requirements: complete normalized original pole-prime-Gamma 3×3 interval enclosures; the **full complex mixed pairing** equality `A=Z_infinity` including reflection and original 1/(2π) normalization; outward verified evaluation of all five `J` cosine moments; all-source coordinate/axiom custody.

**Do not transfer** results from PI003's norm-one mixed trace p=3 shell into the full diagonal Weil matrix: the norm-one trace-test domain/missing diagonal remains an independent interface obstruction.

## 6. Falsification and next CP006

- A SOURCE-proved unexpected non-n9 signed active prime term in the frozen bump family falsifies the CP002/CP003 arithmetic entry table.
- A root roster whose exact Turing count, Gram endpoint, or individual bracket proof fails **blocks the spectral comparison**, even when its raw zero locations appear plausible.
- If the same fully certified arithmetic 3×3 and finite zero-side 3×3 have a discrepancy exceeding the independently certified total operator error, CP-C1's *stated normalization/source dictionary* is falsified. It does NOT establish RH false.
- **CP006:** bridge the actual external `v1-1e6` standard-axiom theorem to pinned original Weil-Lab source, independently certify *high-precision* root intervals and cosine integrals, finish an original `phi` Schwartz carrier, and execute CP004's necessary interval comparison against a real certificate manifest.

**External primary sources:** https://github.com/smmercuri/zeta ; https://github.com/smmercuri/zeta/releases/tag/v1-1e6 ; https://arxiv.org/abs/2004.09765 ; https://arxiv.org/abs/2107.06506 .
