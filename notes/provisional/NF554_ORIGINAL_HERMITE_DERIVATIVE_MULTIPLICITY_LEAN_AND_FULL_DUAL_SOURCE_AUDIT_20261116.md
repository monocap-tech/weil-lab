# NF554 — Hermite-jet root multiplicity in Lean, original 242 odd-source dual coefficient bridge, and NF547 smoothness recovery

**2026-11-16 PT. Draft stacked on NF553 PR #581. Original SHA custody unchanged. No source-independent RH claim.**

## 1. Accepted and failed compiler observations

- NF542–NF545 **LEAN PASS** (historical verified).
- NF546 genuine original 242 full-window physical L² moments, including the actual index-241 sinh pole, **LEAN PASS** on NF552 PR #580 commit `78c761ee4e021a9a5a50e761905e8b2c99c644d0`, run `43958541249`.
- NF552 original complete 242×242 odd-jet modular determinant / 68-node Hermite-product audit **PASS**, run `43958541368`, job `133619443020`.
- NF553 standalone `ActualZetaOriginalJ242HermiteDegreeObstruction.lean` **LEAN PASS** on NF553 PR #581, run `43961169992`, job `133628641547`. This proves the degree-242 divisor obstruction and positivity/separation of real squared nodes.
- NF553 source signed-determinant audit **PASS**, run `43961169992`, job `133628641424`; confirms original -1 determinant sign analytically via source order and genuine pole.
- NF547 genuine original smooth weighted-column compilation is now the first observed failure. The NF553 `dsimp` repair progressed to **three** failures at lines 32/34/36 of `ActualZetaOriginalJ242WeightedCollarGram.lean`: `fun_prop` could prove real sine/cosine/sinh smoothness, but could not infer `ContDiff ℝ ∞` of the **real-to-complex cast**. Precise CI: run `43961171234`, job `133628646051`. The other NF548–NF551 runs inherited this failure.
- NF554 now separates the real smooth original generator proof from the real-to-complex conversion: first prove `ContDiff ℝ ∞ j_i`, then compose with the genuine bounded real-linear map `Complex.ofRealCLM` via `Complex.ofRealCLM.contDiff.comp`. This is a targeted **candidate** compiler repair, not an accepted proof.

## 2. Mathlib already supplies the generic Hermite root-multiplicity theorem

NF553's dual original source argument was:
```
p(t) = Σ_(0<=n<242) (-1)^n a_n t^n,
deg p <= 241.
```
The original odd-derivative left kernel `a^T A = 0` implies `p(-1/4)=0`, and for each original positive frequency `ω_f=2π f`:
```
(d/dω)^k [ω p(ω²)]_(ω=ω_f) = 0,    0 <= k < m_f.
```
To infer that the squared node `t_f=ω_f²` is a root of `p` of multiplicity at least `m_f`, factor the nonzero map `ω↦ω²` locally and use polynomial differentiation / root multiplicity in characteristic zero.

Rather than implement the general Hermite root-multiplicity fact from scratch, Mathlib has an established theorem:
```
Polynomial.lt_rootMultiplicity_of_isRoot_iterate_derivative
```
Under `p≠0` over characteristic zero, if all formal derivatives of orders `0,...,m-1` vanish at `t`, then `rootMultiplicity t p >= m`.

NF554 creates the standalone candidate Lean module:
```
WeilDefect/Arithmetic/ActualZetaOriginalJ242HermiteDerivativeMultiplicity.lean
```
with two named theorems:

- `neutralNF554HermiteRootMultiplicity_of_vanishingJets`: vanishing of formal derivatives `k<m` implies `m ≤ rootMultiplicity t p`, for any real polynomial `p≠0`.
- `neutralNF554HermiteRootMultiplicity_contra`: if all these derivatives vanish but `rootMultiplicity t p < m`, the polynomial must be zero.

The module depends **only on Mathlib**. It asserts neither original source independence nor canonical Gram positivity; source-specific chain transfer is still OPEN until actual Lean compilation of the derivative formula.

## 3. Stronger original source coefficient audit: 58,564 exact cases

The exact original `j_{f,k}=x^k sin(ω_fx)` (even k), `x^k cos(ω_fx)` (odd k) have odd derivatives at zero:
```
j_{f,k}^(2n+1)(0)
 = 0                                     if k>2n+1;
 = (-1)^(n+floor(k/2)) (2n+1)!/(2n+1-k)! ω_f^(2n+1-k)
                                         otherwise.
```
This identity is an algebraic consequence of the authentic sine/cosine Taylor coefficients; it does not use numerical π.

For the dual polynomial `p`,
```
∑_n a_n j_(f,k)^(2n+1)(0)
 = (-1)^floor(k/2) (d/dω)^k [ω p(ω²)]_(ω=ω_f).
```
The genuine last pole obeys
```
∑_n a_n (sinh(x/2))^(2n+1)(0)
 = 1/2 p(-1/4).
```

The new exact original-source auditor `scripts/local_replay/verify_nf554_original_dual_odd_jet_coefficient_bridge.py` checks all **241×242=58,322** oscillator index/odd-derivative combinations, comparing independently assembled sine/cosine Taylor coefficients to the dual-polynomial derivative factorial/sign/exponent. It checks all **242** true sinh-pole coefficients, for a total **58,564 exact symbolic comparisons**. No `π=1` specialization or approximation is required for the coefficient identity.

Each comparison uses exact integer factorials and symbolic exponents; all original 67 frequency blocks, 241 ordered monomial indices and the final true pole are pinned by exact source SHA and Lean table. This replaces a generic benchmark with a source-specific symbolic identity audit, but **is not itself a Lean theorem**. CI is pending.

## 4. Exact remaining logical bridge

Having proved the above derivative identity on paper, the formal endgame for original finite source independence is:

1. Build the `p(t)` polynomial from `a : Fin 242 → ℝ`, prove `natDegree p < 242` and injection of its coefficients.
2. Prove in Lean that `(d/dω)^k[ωp(ω²)]` vanishing at nonzero `ω_f` implies `p`'s first `m_f` formal derivatives vanish at `t_f=ω_f²` (triangular chain-rule coefficient has nonzero diagonal `ω_f(2ω_f)^k`).
3. Invoke NF554's generic root-multiplicity theorem to obtain multiplicities `m_f`; add genuine pole `-1/4` with multiplicity one.
4. Prove `H(t)=(t+1/4)∏_f(t-4π²f²)^{m_f}` divides `p` (distinct original real nodes); then use NF553's compiler-accepted `deg H=242 > deg p` obstruction.
5. Establish invertibility of the actual original square odd-jet matrix over ℝ and complex independence by splitting coefficients into real and imaginary parts.
6. Apply NF551 real-analytic local-global identity and NF550 weighted-square theorem to get **unconditional original canonical 242 Gram positivity in Lean**.

No off-source or numerical surrogates and no source-specific axiom should enter any of these transfers.

## 5. Non-transfer

The original NF528 inward/affine mollification and complete positive/negative divisor-source graph convergence, NF527 full gamma+prime n9+both poles 1/10 coercivity, NF539 signed Weil source identity, W_ODD_NEG, and RH remain **OPEN**. An unconditional original finite Gram inverse would only close the 242 physical moment correction gate, not the global Weil proof.

## 6. NF555 target

Obtain actual NF554 standalone Hermite multiplicity Lean acceptance and NF547 smoothness repair, then unblock NF548–NF551 in order. Formalize the source derivative-to-polynomial triangular jet bridge; after that the global-independence assumption can be removed without a generic 242×242 determinant theorem.
