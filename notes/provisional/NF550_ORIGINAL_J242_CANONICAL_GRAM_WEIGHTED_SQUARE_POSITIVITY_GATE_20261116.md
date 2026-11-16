# NF550 — True original J242 canonical Gram = real weighted squared source norm; semidefinite unconditional and strict positivity reduced to ONE local source-separation lemma

**2026-11-16 PT; stacked draft after NF549 #577. NEW Lean modules and their full dependent original chain are CI PENDING. This is NOT a claim of a compiled unconditional positive Gram, original signed Weil certificate or RH.**

## Original carrier custody (UNCHANGED)

- Original NF407 exact 242 selected source nodes from `notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json`, SHA256 `0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce`. Exact 67 rational frequency groups, 241 genuine contiguous source oscillator modes `x^k sin(2πfx)` for even k / `x^k cos(2πfx)` for odd k, plus original last `sinh(x/2)` pole, no reordering or surrogate vectors.
- Original NF494 U400 SHA256 `39cba367d70243c2d15e5a9323fc8097d58187923dcf0eca2b031136871f0181`. True B=11/10, δ=1/500 and two original strict terminal collars. All genuine positive/negative zeta divisor multiplicities unchanged.
- NF548 exact fixed C∞ real even nonnegative cutoff `χ_real(x)=u(2000(x−1099/1000))+u(2000(x+1099/1000))`, where `u` is Mathlib's canonical smooth bump with exact support `(-1,1)`. Its positive open source interval is exactly `I=(2197/2000,2199/2000)` and reflected negative interval. These are **strictly INSIDE** the original E; E itself is NOT replaced.
- True full physical selected L² source vectors `J_i = 1_{[-B,B]} j_i`, true bounded complex-linear `M_original(f)_i=⟪J_i,f⟫`, fixed Schwartz columns `b_i=χ j_i`, actual Gram `G = M_original ∘ B_χ`.

## Latest real CI receipts before NF550

- NF542 [#43900908980](https://github.com/monocap-tech/weil-lab/actions/runs/43900908980): LEAN PASS.
- NF543 [#43900906815](https://github.com/monocap-tech/weil-lab/actions/runs/43900906815): LEAN PASS.
- NF544 original physical 242 Gram inverse [#43942319623](https://github.com/monocap-tech/weil-lab/actions/runs/43942319623): **LEAN PASS**.
- NF545, NF547, NF548: SHA-pinned independent original SOURCE AUDIT PASS in recent runs.
- NF545 actual 241-node source expansion Lean earlier hit the default recursion depth; NF549 replaced it with structurally verified `List.length_flatMap` plus already-proved exact 241 multiplicity sum. Current fresh NF549 compiler jobs (e.g. [#43947651373](https://github.com/monocap-tech/weil-lab/actions/runs/43947651373)) had NOT returned accepted Lean results as of this pass.
- Thus NOTHING in NF545 selected-functions, NF546 physical moments, NF547 actual χj, NF548 canonical cutoff, NF549 actual L² pairing or NF550 new statements is labeled LEAN PASS prematurely.

## 1. NEW a.e. physical synthesis

New module `WeilDefect/Arithmetic/ActualZetaOriginalCanonicalGramWeightedSquare.lean` introduces the unchanged source combination

```
S_d(x) = ∑_{j<242} d_j · j_j(x)
W_d(x) = ∑_{j<242} d_j · 1_{[-B,B]}(x) · j_j(x).
```

The actual (L²)-synthesis from NF549, `V(d)=Σd_j[J_j]_{L²}`, has the honest a.e. representative `W_d`: the Lean proof combines genuine `Lp.coeFn_smul`, `Lp.coeFn_fun_finsetSum`, `eventuallyEq_sum`, and the NF546 source-specific `J_j` a.e. equality. No pointwise evaluation of an arbitrary physical L² class is silently asserted. The same original J242 full aperture is preserved.

## 2. ACTUAL fixed original squared norm, not a formal Gram symbol

NF549's conditional-compiler physical Gram identity is

```
∑ conj(d_i) (G d)_i = ⟪V(d), [Bχ d]_{L²}⟫.
```

By the genuine original NF547 source Schwartz synthesis identity `Bχ(d)(x)=χ(x) S_d(x)`, the two genuine physical a.e. representatives and support `supp(χ)⊂E⊂[-B,B]`, the new NF550 proof gives

```
  ∑_{i<242} conj(d_i) (Gd)_i
    = ∫_ℝ χ(x) · |S_d(x)|² dx                         (ℂ integral).
```

The right integrand is REAL and NONNEGATIVE because this is the actual original real χ. The next theorem converts it exactly into the genuine real integral

```
  Re ∑ conj(d_i)(Gd)_i
    = ∫_ℝ χ_real(x) |S_d(x)|² dx ≥ 0.
```

**This is a source-specific canonical Gram positive-SEMIDEFINITE identity, not yet strict positive definiteness.** Unlike earlier abstract finite-rank lemmas, it fixes ALL original data, moment maps, χ, Schwartz columns, and full untruncated source functions.

## 3. Source-specific strict positivity is reduced to one point in original E

The original full 242 selected source combination is continuous (a finite sum of exact oscillator/pole functions). The scalar real weight `x ↦ χ_real(x) |S_d(x)|²` is continuous, compactly supported, integrable and nonnegative. Hence if there is even ONE point x where χ_real(x)>0 and S_d(x)≠0, the integral is STRICTLY POSITIVE; the proof uses the pinned measure `IsOpen.measure_pos` and `integral_pos_of_integrable_nonneg_nonzero` result rather than sampling or quadrature.

NF550 submits exact Lean implications:

```
∀ d x, 0<χ_real(x) ∧ S_d(x)≠0 ⇒ Re(d*Gd)>0.
∀ d x, x∈(2197/2000,2199/2000) ∧ S_d(x)≠0 ⇒ Re(d*Gd)>0.
```

Therefore the **only last finite-Gram algebraic hypothesis** is

```
CollarSeparatesJ242 :=
  ∀ d : Fin 242→ℂ, d ≠ 0 →
    ∃ x∈(2197/2000,2199/2000),  S_d(x) ≠ 0.
```

This exact local condition follows analytically from NF545's characteristic-root proof: the 67 distinct rational frequencies give 134 distinct imaginary roots, the genuine sinh pole gives ±1/2, and after combining polynomial exponents the 136 roots are pairwise distinct. A nonzero exponential polynomial cannot vanish identically on an interval; the even/odd selected monomial coefficients then separately vanish. Thus no nonzero original d can vanish on the fixed open collar interval. **THIS local analytic source-separation theorem is NOT YET Lean-formalized.**

## 4. One-source terminal correction once local separation is proved

`WeilDefect/Arithmetic/ActualZetaOriginalCanonicalGramSeparationGate.lean` defines the proposition `NeutralNF550OriginalCollarSeparatesJ242` with exact source S_d and the fixed original collar subinterval. Under this **one source-specific uniqueness hypothesis**, it constructs:

1. Injectivity and strict positivity of **the actual canonical original 242 Gram**, not an assumed arbitrary positive Gram.
2. An exact 242-dimensional Schwartz correction right inverse R for genuine full-window physical moments M_original, supported only in ORIGINAL E.
3. A corrected strict original collar Schwartz representative admitting the genuine log Hilbert carrier and matching all 242 authentic moments exactly. No abstract M, arbitrary b_j, arbitrary χ or independently assumed Gram inverse remains.

These are PENDING compiler acceptance. Their separation premise is an analytic-source dependency, not a fabricated assumption concealed inside an unconditional theorem. They do NOT establish convergence of original singular `ell_U` in full true-divisor source graph.

## 5. Strict verification

New independent `.github/workflows/nf550-original-canonical-weighted-square.yml` checks the original NF407+NF500 SHA-native exact 242 signature with Python, and performs pinned Lean builds in order: NF545 source functions → NF546 genuine selected L² moments → NF547 χj Schwartz → NF548 actual canonical even χ → NF548 Gram inverse → NF549 source physical integral → NF550 weighted squared norm/semidefiniteness and local separation endpoint. Proof-placeholder rejector included.

**CI standing on creation: queued/pending.**

## 6. NEXT — NF551

First take actual compiler logs to repair every outstanding NF545→NF550 module and get real green receipts. Then formalize the ORIGINAL 136-root exponential-polynomial unique continuation for exact original J242 functions on the fixed open E interior. This one specific mathematical theorem, rather than any further anonymous coercivity/Gram hypothesis, will make the original 242 Gram unconditionally strictly positive in Lean.

Separately still open: exact NF528 original inward affine-mollified `g_s` and all-multiplicity P/N graph convergence to original `ell_U`; true NF527 gamma+prime n=9+both poles coercivity (Q≥1/10‖f‖²); NF539 complete signed source identity; original signed odd/even decision and RH.

**Do not claim full even/odd Weil positivity or RH.**
