# Weil-Lab — CP023
## Source-aware phase/ζ derivative error transport and conservative exact rational finite-approximant margins

**Branch:** independent CP### cross-projection, stacked on CP022 PR #844 → CP021 #843 → CP020 #842 → CP019 #840 → CP018 #839. **Original IV### support extension, NF### original physical numerical acceptance, and PI### independent pole/prime/Gamma work remain unchanged.** Neither global Weil positivity nor RH is claimed.

### 1. Live kernel status and trust boundary

The CP022 PR #844 head `7a0366469818ee683727ad7346b70951fb1896b7` had no completed CP021/CP022 original Lean 4.35 workflow, no compiled leaf `.olean` acceptance receipt and no new external original v4.35 standard-only `#print axioms` evidence on inspection. CP021 PR #843 inherited CP013/14 source-lineage runs were still QUEUED; source-only consistency is not kernel proof.

The current isolated container has no `lean`, `lake` or `elan` binary and no effective DNS to fetch the compiler. This CP023 cycle **does NOT claim actual original Lean4.35 compilation** and does not launch more CI into the NF/IV queue. The CP021 germ-then-Borwein opt-in kernel test remains the next concrete original compiler recovery obligation, exactly as in CP022.

### 2. Exact source mathematical identities, without differentiating a real-axis value-error inequality

The actual pinned original `Zeta.Zeros.HardyZ` and `Zeta.EulerMaclaurin.Continuation` give, on the actual positive-height line:

[
s_t=\tfrac12+it,\quad
Z(t)=\Re\bigl[e^{i\theta(t)}\zeta(s_t)\bigr],\quad
\zeta(s)=A_{6,256}(s)+R_{6,256}(s).
]

Define the **finite approximant projection** (Z_A(t)=\Re[e^{i\theta(t)}A_{6,256}(s_t)]) and **remainder projection** (Z_R(t)=\Re[e^{i\theta(t)}R_{6,256}(s_t)]).

Then (Z=Z_A+Z_R) as an exact mathematical function identity. With actual source-sound differentiability and holomorphic derivative transport (formal source proof candidates CP019–CP022; no new Lean kernel receipts), the chain rule gives:

[
\boxed{
Z_R'(t)=\Re\bigl[e^{i\theta(t)}i(\theta'(t)R(s_t)+R'(s_t))\bigr]
}
]

and

[
\boxed{
Z_R''(t)=\Re\bigl[e^{i\theta(t)}(
-\theta'(t)^2R(s_t)
-2\theta'(t)R'(s_t)
-R''(s_t)
+i\theta''(t)R(s_t))\bigr].
}
]

The second identity **retains the phase/ζ cancellation inside the complex expression**. For an upper bound on the smaller remainder portion, the triangle inequality suffices and yields rigorously valid but conservative scalar inequalities:

[
|Z_R'(t)|\le |\theta'(t)|\,|R(s_t)|+|R'(s_t)|,
]
[
|Z_R''(t)|\le
(\theta'(t)^2+|\theta''(t)|)|R(s_t)|
+2|\theta'(t)|\,|R'(s_t)|+|R''(s_t)|.
]

No derivative is obtained by applying a derivative operator to the original Hardy-`Z` real-axis value-error inequality. Instead, the *actual original holomorphic zeta remainder on a complex neighborhood* is what supports genuine Cauchy derivative estimates once its original-v4.35 source proof kernels are accepted.

### 3. New exact phase-aware numerical error budget

Assume **two NEW UNPROVED UNIFORM original phase bounds** on the entire target height interval (I=[149.5,150.05353]):

[
\boxed{|\theta'(t)|\le2,\qquad
|\theta''(t)|\le1\quad(\forall t\in I)}.
]

The exact original phase derivative formula (	heta'(t)=(\Re\psi(1/4+it/2)-\log\pi)/2) exists upstream and the exact trigamma second derivative has a NEW CP019 source candidate, but these **uniform numerical envelopes are not established in original Lean or validated ball arithmetic**. Exploratory high precision mpmath at (t=149.5,149.75,150.05353) gives roughly (	heta'(t)\approx1.585) and (	heta''(t)\approx0.00334); such point samples are NOT uniform bounds and are NOT used as premises of an accepted proof.

Assume in addition the previous **complex** original Euler–Maclaurin remainder Cauchy derivative targets, which have a mathematically exact Borwein rational argument and new CP019–CP022 Lean SOURCE candidates but **NO NEW LEAN KERNEL RECEIPT**:

[
|R|\le\frac3{10^{13}},\qquad
|R'|\le\frac{12}{10^{13}},\qquad
|R''|\le\frac{96}{10^{13}},\qquad
|R'''|\le\frac{1152}{10^{13}}.
]

Then, uniformly on (I), elementary complex norm/real-part inequalities imply:

[
\boxed{
|Z_R'(t)|\le2\frac3{10^{13}}+
\frac{12}{10^{13}}=
\frac{18}{10^{13}}=1.8\times10^{-12}
}.
]

For curvature:

[
\begin{aligned}
|Z_R''(t)| &\le (2^2+1)\frac3{10^{13}}
 +2\cdot2\frac{12}{10^{13}}
 +\frac{96}{10^{13}}\\
&=\boxed{
\frac{159}{10^{13}}=1.59\times10^{-11}
}.
\end{aligned}
]

These are **conditional, analytically justified sufficient bounds**, not actual accepted numerical error certificates for the original Hardy-`Z` and not full curvature bounds. The original phase envelopes and complex Cauchy source derivation require separate proof.

### 4. Precise two-scalar transfer to the remaining finite approximant

Once the original derivative identities and exact error assumptions are rigorously established, **it would be sufficient to certify only the FINITE original approximant**:

[
\boxed{
Z_A'(149.5)\ge\frac{12}{5}+\frac{18}{10^{13}}
}
]
and
[
\boxed{
\sup_{t\in I}|Z_A''(t)|
\le4-\frac{159}{10^{13}}.
}
]

Indeed, derivative decomposition and the triangle inequality immediately yield the original CP017 required (Z'(149.5)\ge12/5) and universal (|Z''(t)|\le4) for all (t\in I). This is an **exact support and phase-aware preservation law**, not a solution of those finite-approximant interval inequalities.

The finite approximant involves the original (255) nonzero (n^{-s}) source sum, pole correction, and finitely many Bernoulli/Pochhammer terms. Its derivatives and the original phase/digamma factors require genuine cancellation-aware **complex interval/ball enclosures** on the entire target interval. The uniform original phase derivative bounds are a distinct numerical verification task. No claim is made that the finite source approximant satisfies the two inequalities now.

The previous CP017 exact strict first-derivative positivity margin after the genuine original bounds is (4647/25000=0.18588), independent of this tiny remainder buffer. A genuine narrowed numerical root existence certificate in ((150.05352,150.05353)) is *still required* to attach the proposed root to the original source ordinal #53. All the original Weil Prime−Pole−Arch 3×3 and full spectral comparison remains separately open.

### 5. Concrete exact arithmetic verification and CI custody

New `scripts/cp023_original_phase_remainder_fraction_budget.py` computes these values with **only `fractions.Fraction`** and verifies exact Cauchy recursion order 0–3, exact first/second real phase-remainder envelopes, and deliberate false-tight-bound and weakened-phase-assumption negative controls. The exact arithmetic was independently executed in the local container, giving (E_1=9/5000000000000), (E_2=159/10000000000000).

The Python file additionally:
- Verifies the actual committed `CP018HardyJet.lean` exposes original phase ζ complex source jets, including `sourceFirstJet`, `sourceSecondJet`, `thetaPrimeJet`, `thetaSecondJet`, and two complex ζ derivatives;
- Verifies `CP021BorweinLeaf.lean` retains CP022's corrected (0≤t) source witness rather than the previous invalid `abs_of_nonneg ht.1`;
- Verifies `CP021GermLeaf.lean` still transports the **original** `riemannZeta_eq_approximant_add_remainder` through `Filter.EventuallyEq.iteratedDeriv_eq`;
- Rejects new source `sorry`, `axiom`, `constant`, `opaque` declarations in both leaves;
- Allows OPTIONAL `--numeric-screen` for sample (\theta',\theta'') values labeled strictly **NONRIGOROUS**, excluded from actual source receipts;
- FAILS CLOSED if `--receipt` is requested without BOTH exact `--self-test` and actual `--source-contract` controls. The receipt always says `CP023_PHASE_REMAINDER_EXACT_BUDGET_PASS_NOT_SOURCE_LEAN` and explicitly records the still-unproved original phase envelopes, complex Cauchy Lean kernels, finite approximant, Hardy-`Z` and Weil–spectral obligations.

The existing **opt-in only** `.github/workflows/cp021-original-independent-leaf-source-only-opt-in.yml` (label `cp021-leaf-source` or manual eligible dispatch) has one new exact phase-remainder budget/source-contract step and source-only JSON/log upload. It still downloads and checks the SEVEN true immutable original Zeta/Mathlib source SHAs through CP022's gate, imports only original upstream in the two compiler leaf modules, and **does not trigger on ordinary push/PR creation or synchronize events**.

**No CP023 workflow launched. No new original external v4.35 `.olean` exists. No additional auto-CI workload assigned to NF or IV.** No new Lean module is added in this cycle; CP023 deliberately prioritizes reducing the analytical uncertainty of eventual interval certification without generating more uncompiled Lean source debt.

### 6. Next independent obligations

**CP024:** Obtain actual kernel feedback from the ordered original `CP021GermLeaf` then `CP021BorweinLeaf` opt-in workflow when capacity permits, repair any actual compiler errors, and finally connect the accepted *complex ζ−finite approximant* error to validated **whole-interval** numerical bounds on the actual finite approximant and original phase (	heta',	heta''). A phase sample of (approx1.585) does **not** prove the required (|	heta'|le2), nor does the original closed-form derivative identity alone. Verify every interval enclosure using source-pinned exact ball/norm arithmetic, not just mpmath or numerical screening.

The original signed Weil/spectral normalized 3×3 equivalence, global support-independent positivity and RH remain independent and **OPEN**.
