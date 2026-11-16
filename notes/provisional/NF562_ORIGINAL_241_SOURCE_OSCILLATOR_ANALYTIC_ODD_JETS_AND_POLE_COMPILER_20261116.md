# NF562 — Actual all-241 original oscillator analytic odd jets, closed parity forms, and source compiler recovery

**2026-11-16 PT. Draft stacked on NF561 PR #589.** New genuine-source Lean files and focused CI committed; their compiler acceptance PENDING. Full source generator independence, original weighted Gram positivity, signed Weil, W_ODD_NEG and RH **OPEN**.

## 1. Mathematical advance: no more generic anonymous oscillator family

NF561 proposed a source-ready higher-order Leibniz theorem. NF562 instantiates its result with every actual original oscillator index `i : Fin 241`, using the exact NF545 source declarations and the literal source generator `nf545OriginalSelectedRealGenerator ⟨i.val,...⟩`. New source module:

```
WeilDefect/Arithmetic/ActualZetaOriginalJ242ActualOscillatorOddDerivatives.lean
```

It defines:
- `neutralNF562OriginalOscillatorOrder i`: the unchanged monomial degree `k_i` from `nf545OriginalOscillatorNodeAt i`;
- `neutralNF562OriginalOscillatorOmega i = 2 * Real.pi * ((nf545OriginalOscillatorNodeAt i).1 : ℝ)`: **actual** angular frequency, no pi=1 or numerical approximation;
- `neutralNF562OriginalOscillatorTrig i`: the source's true sine iff k_i even and cosine iff k_i odd.

The explicit exact-source identity is

```
nf545OriginalSelectedRealGenerator ⟨i.val,...⟩
  = fun x => x^k_i * (if Even k_i then sin(ω_i*x) else cos(ω_i*x)).
```

It is a definitional unfolding of the already verified NF545 source, not a replacement generator. The new module proves candidate smoothness and source-indexed positive omega for **all 241 original indices**, with rational source-node positivity decidably checked from the exact data, and `Real.pi_pos` transferred multiplicatively.

For each original oscillator index `i<241` and odd derivative row `0≤n<242`, the new analytic theorem is

```
j_i^(2n+1)(0) =
  if k_i≤2n+1 then
    binomial(2n+1,k_i) * k_i! *
    [D^(2n+1-k_i) true_original_trig_i](0)
  else 0.
```

This uses the **actual** source analytic function on its left, and NF561's generic iterated Leibniz theorem on the right. A second theorem directly establishes the zero case for every original k_i>2n+1. No numeric Gram, assumed independence, source edit, or anonymous function family enters.

These are **committed Lean proof candidates**, not yet compiler-certified.

## 2. Closed mathematical parity formulas for both authentic oscillator types

New independent analytic module:

```
WeilDefect/Arithmetic/ActualZetaOriginalJ242MonomialTrigOddJets.lean
```

contains source-ready specialized theorems valid for any real omega and integers n,r with r≤n:

**Original even k=2r, sine:**

```
[D^(2n+1) (x^(2r) sin(ωx))](0)
 = binomial(2n+1,2r) * (2r)! * (-1)^(n-r) * ω^(2(n-r)+1).
```

**Original odd k=2r+1, cosine:**

```
[D^(2n+1) (x^(2r+1) cos(ωx))](0)
 = binomial(2n+1,2r+1) * (2r+1)! * (-1)^(n-r) * ω^(2(n-r)).
```

For n<r, the respective derivative is zero because the monomial degree exceeds the derivative order. These four generic analytic results are proved by combining the exact NF561 initial-point higher Leibniz selector with the scaled real sine/cosine derivative identities. The sign `(-1)^(n-r)` is equivalent to the audit's `(-1)^(n+floor(k/2))` because their exponents differ by `2r`.

The source-audited unified factorial form

```
D^(2n+1) j_(f,k)(0)
 = (-1)^(n+floor(k/2)) *
   (2n+1)!/(2n+1-k)! * ω_f^(2n+1-k)
```

for k≤2n+1 now has the full actual higher-derivative proof architecture. Converting the two generic parity theorems and the source-indexed conditional theorem to this *single* closed source-indexed statement, using exact binomial/factorial identities and Nat parity, is a remaining Lean proof obligation. Full source-left-kernel `ω p_a(ω²)` derivative correspondence and original Hermite independence are still OPEN in Lean.

## 3. Newly confirmed upstream compiler failure and repair

NF561's source dual/pole job (run #43976006178, job #133680034237) **FAILED at the NF559 finite genuine pole dual algebra**, AFTER advancing past source-exact NF557 and NF558 coefficient injectivity. The precise error is:

```
ActualZetaOriginalJ242OriginalPoleDual.lean:38:10
rw [pow_mul] failed because no occurrence of an exponent of form m*n
```

The current goal contained `((1/2)^2)^n`. NF562 corrects this to `rw [← pow_mul, pow_add]`, orienting the already-known real power identity from the nested form to `(1/2)^(2*n)`. No source or mathematical premise changes. **Fresh compiler acceptance pending.**

The NF561 exact source SHA/58,564 symbolic coefficient replay job **PASS** (job #133680034560).

The NF561 independent generic scaled sin/cos and initial-point monomial Leibniz Lean job and physical Gram NF546→NF551 compiler job were still IN PROGRESS at the most recent check. Do not describe them as PASS. NF547–NF548 previously passed in genuine dependent builds, but NF549→NF551 must pass their current actual compiler chain. Earlier NF549 `set_option` parser failure was repaired in NF561 and awaits that independent job.

The NF560 actual sinh-pole all-odd-derivative source module also depends on the finite NF559 negative pole dual algebra; its full acceptance is still blocked or pending. It must not be inferred from source coefficient audits.

## 4. Source fidelity and verification

Source custody unchanged:
- 67 original distinct positive rational oscillator frequency groups;
- 241 original fixed monomial order/frequency oscillator indices;
- true separate index-241 generator `sinh(x/2)`;
- B=11/10 and collar δ=1/500; unchanged canonical even strict collar cutoff;
- exact original NF407 and NF500 SHA-pinned source replay; NF554 all-entry 58,564 symbolic oscillator/pole coefficient audit **PASS**.

New pinned `.github/workflows/nf562-original-actual-oscillator-odd-jets.yml` has four separate checks:

1. NF561 generic initial-point Leibniz and scaled trigonometric derivatives, followed by NF562 parity-specialized all-order source functions and **actual 241-index** source derivatives/positive frequencies.
2. NF557→NF560 exact original dual polynomial, pole algebra repaired this stage, and genuine analytic sinh derivatives.
3. Genuine original NF546→NF551 physical Gram/cutoff/integral/signed-square/local-global compiler chain.
4. Unmodified SHA-pinned original 58,564-entry coefficient replay.

All **NF562 new Lean compiler results are PENDING**. No new axiom, sorry or admit introduced.

## 5. Remaining chain to unconditional original finite Gram

The accepted generic NF553–NF556 math gives the degree bound contradiction, root multiplicity from vanishing derivatives and exact quadratic root-multiplicity transport. Need still:

1. Generic NF561 Leibniz and NF562 authentic oscillator source-indexed analytic jets **Lean PASS**.
2. Uniform source-indexed signed factorial formula and genuine analytic source-odd-jet left-kernel ↔ `F_a^{(k)}(ω_f)=0` derivative identity in Lean.
3. Genuine negative pole (NF560) and 67 source positive squared nodes with total multiplicity 242, simultaneous polynomial root multiplicity/divisibility in Lean.
4. Show real square source odd-jet matrix invertible from trivial left kernel, extend to original complex coefficients and global independence.
5. Combine NF551 real-analytic collar uniqueness with NF550 physical weighted Gram to prove **unconditional** original canonical Gram strict positivity; separate reality/conjugation-equivariance of correction still needed.

None of (2)–(5) has been achieved in Lean at NF562.

Full NF528 genuine source all-divisor graph convergence, NF527 complete gamma+prime n=9+both poles 1/10 coercivity, NF539 signed Weil identity, W_ODD_NEG and RH remain **OPEN**.

## NF563

Obtain actual NF562 Lean compiler diagnostics, repair genuine source-indexed analytic jet compilation and NF559 negative pole algebra, and address NF549–NF551 remaining physical-chain errors. Then formalize the unified exact signed source factorial formula and the source derivative-to-dual polynomial step. Avoid new numerical Gram detours.
