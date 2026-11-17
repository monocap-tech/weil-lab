# NF569 — From the genuine J242 real odd-jet left kernel to global complex source independence and strict canonical finite Gram

Draft stacked on **NF568 PR #600**. All new NF569 Lean proofs are committed candidates; **not compiler-certified**.

## 1. Actual CI boundary

At entry to NF569, NF566 run 44004240240, NF567 run 44005817998, and NF568 runs 44006908433 / 44007069874 all still reported queued jobs. There were no completed new logs available to address inherited analytic or physical errors. The latest confirmed frequency-polynomial proof remains NF565 job 133769466691 SUCCESS; the exact 58,564 source coefficient audit 133769466750 also SUCCESS. NF565 oscillator and weighted-square jobs failed earlier; repairs from NF566 are not yet accepted. NF542–NF549, generic NF553–NF556 and genuine NF557–NF560 had been accepted in earlier focused dependency builds.

The research action here therefore advances the exact remaining terminal mathematical implications while isolating checkable new pieces from the stalled source compiler queue. No failed or pending dependency is relabeled as passing.

## 2. Independent finite-dimensional square matrix theorem

New module: `ActualZetaOriginalJ242SquareKernelTransport.lean`.

For any real square matrix A indexed by Fin N, define L(a)_j = Σ_n a_n A_nj. This is a linear endomorphism. If the left kernel is zero, L is injective, hence surjective by finite-dimensionality. Given Ab=0, for any i choose a with L(a)=e_i, where e_i is the actual coordinate vector. The exact finite sum interchange is

    b_i = Σ_j L(a)_j b_j = Σ_n a_n (Σ_j A_nj b_j) = 0.

Thus b=0. The proof uses neither symmetry nor a determinant or numerical conditioning estimate. No source results are imported.

## 3. Independently derive the right kernel from the literal real source combination

New module: `ActualZetaOriginalJ242GlobalCombinationJets.lean`.

Let j_i be the actual `nf545OriginalSelectedRealGenerator i`. Every such function is smooth at every finite order, by its original sine/cosine-monomial or genuine sinh(x/2) formula. For b : Fin 242 → ℝ define U_b(x)=Σ_i b_i j_i(x).

Using actual higher-order finite-sum differentiation we implement

    D_x^(2n+1) U_b(0) = Σ_j A_nj b_j,

with A literally the original NF560 analytic odd-jet matrix. Hence U_b identically zero implies Ab=0. This proof does not import pending NF566 closed jet formulas, the NF568 left-kernel proof, or NF550 physical Gram.

For complex d, define V_d(x)=Σ_i d_i (j_i(x):ℂ). Explicit induction over finite sums shows Re V_d=U_Re(d) and Im V_d=U_Im(d), since the genuine j_i are real. No complex derivative transfer or hidden real-valued coefficient assumption.

## 4. Assemble the terminal original global independence candidate

New module: `ActualZetaOriginalJ242GlobalIndependence.lean`.

Apply the generic square theorem to the actual NF560 matrix and the NF568 source-specific candidate left-kernel theorem. This gives Ab=0 ⇒ b=0. With the actual real combination derivative identity we obtain U_b≡0 ⇒ b=0. Real and imaginary splitting then gives V_d≡0 ⇒ d=0 for complex d.

The final theorem has no source-independence premise, but depends on the still-pending NF566–NF568 source proof chain. **Not LEAN PASS.**

## 5. Connect directly to the canonical physical Gram, without changing it

New module: `ActualZetaOriginalJ242CanonicalGramPositivity.lean`.

The NF569 untruncated complex combination is definitionally the NF550 combination, since the NF546 complex generator is the exact real original generator embedded in ℂ. The terminal module supplies the exact NF551 proposition `NeutralNF551OriginalJ242GlobalIndependence`, calls genuine original collar separation, then calls the NF551 conditional Gram positivity theorem to produce a candidate with no separation or independence premise:

    ∀ d : Fin 242 → ℂ, d ≠ 0 →
       0 < Re(Σ_i conj(d_i) (Gχ d)_i).

Here Gχ is the unchanged `neutralNF548CanonicalOriginalWeightedGram`, with the fixed original NF548 even two-collar cutoff, not a surrogate or auxiliary Gram. No assertion of full Weil positivity, uniform energy estimate, signed scalar certificate, or RH follows.

The strict finite Gram theorem remains **compiler pending**, both because the original NF550/NF551 physical and analytic modules remain unaccepted and because NF566–NF568 authentic source independence is not yet accepted.

## 6. Verification

Two focused jobs only in the new NF569 workflow, with per-ref concurrency cancellation on reruns: an independent generic square/actual combination jets compilation and a dependent full original complex independence/canonical Gram compilation. Earlier audit and broad diagnostics are already queued; they are not duplicated in the NF569-specific workflow. No proof holes intentionally inserted. No Lean executable is locally available in this workflow; actual acceptance must be read from the CI result. 

## 7. Next NF570

Prioritize compiler recovery, not further long speculative dependency stacks. When new CI logs are available, recover the earliest failing actual import, independently confirm the generic square theorem and source-combination jet identities, and attempt the full original global independence / Gram endpoint. If queues remain blocked, inspect workflow scheduling and the earliest concrete source errors rather than declare proof completion. Correction real-data conjugation-equivariance, NF528 full source divisor graph convergence, NF527 complete cofinite 1/10 gamma+prime both-poles coercivity, NF539 signed Weil source identification, W_ODD_NEG and RH remain OPEN.
