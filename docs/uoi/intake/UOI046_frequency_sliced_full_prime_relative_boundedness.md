# Weil-Lab — UOI046: frequency-sliced Bessel control of the complete prime form

**Research standing (2026-11-21):** Analytic theorem **conditional on the established arithmetic Brun–Titchmarsh short-interval upper bound**, the elementary Chebyshev upper bound, and UOI045's *analytic* signed-Gamma collar estimates. All of these are standard/unconditional mathematical results, but their particular attachment to the original literal Weil form has **not** been checked by Lean. Reproducible stage-ten finite checks merely corroborate the definitions; they do **not** verify the infinite-stage analytic proof. No new CI submission or NF count change. Formalization obligations belong solely in GitHub issue #898.

Original source ref for the definitions: `614ba879f7389fdb620c474adaee273b00eac71c`; source files include `ActualZetaOriginalCollarPrimeBound.lean`, `ActualZetaOriginalCollarGammaLower.lean`, `ActualZetaPhaseIVOriginalNarrowSignedGamma.lean`, and `Def_Zeta23_ExplicitFormula.lean`. The old fixed-collar source→native identification remains insufficient for the new supports (F01/F08).

## 1. Exact restricted family and main theorem

Set `q=8`, `t=log q`, `δ=1/1000`, `c_j=(j+1/2)t`, `δ_j=δ q^{-j}`, `I_j=(c_j−δ_j,c_j+δ_j)`. As before `S_m` consists of complex smooth compact tests `f=Σ_{j<m} f_j`, `supp f_j⊂I_j`, whose three **separate local moments** vanish:

`∫ f_j=∫exp(x/2) f_j=∫exp(−x/2) f_j=0`.

Write the **complete literal original two-sided von Mangoldt prime diagonal**

`P(f)=Σ_{n≥2} Λ(n)/√n [C_f(log n)+C_f(−log n)]`,

with `C_f(s)=∫ f(x) conj(f(x−s))dx`. For finite `m` only finitely many `n` occur. Let `Gamma(f)` denote the original signed digamma Fourier quadratic. Since poles vanish separately, `W_lit(f)=Gamma(f)−P(f)` on `S_m`.

**UOI046 theorem (analytically proved, not kernel-certified).** There is a **finite absolute constant** `C_*` independent of `m` such that

> `|P(f)| ≤ C_* Gamma(f)` for every `m≥2`, every `f∈S_m`.

In particular the UOI043 monotone generalized Rayleigh ratios obey

> `0 < rho_infty := sup_m sup_{0≠f∈S_m} P(f)/Gamma(f) ≤ C_* < ∞`.

Consequently the original full prime Hermitian form has a unique continuous extension to the Gamma Hilbert completion `H_infty` of the algebraic union `S_infty`. There exists a **bounded self-adjoint** `A_infty` on `H_infty` representing that prime form; each compact finite-stage `A_m` is its genuine form compression. The limiting supremum is the **top of the spectrum** `sup σ(A_infty)`; attainment or compactness of `A_infty` is **not** established.

**Nothing here implies `rho_infty≤1`, a positive whole-form margin, positivity on all Schwartz functions, or RH.** `C_*` may be much larger than one.

## 2. Exact arithmetic translation blocks and orthogonality

For `j<k`, let `d=k−j`, `N=8^d`, `a_jk=δ_j+δ_k` and

`A_jk={n≥2: Λ(n)>0, |log n−d log8|<a_jk}`.

Define the full-line translation sum (no sharp output restriction)

`V_jk g(x)=Σ_{n∈A_jk} κ_n g(x+log n)`, `κ_n=Λ(n)/√n`.

The source convention and no same-collar prime shifts imply

`P(f)=2 Re Σ_{j<k} <f_j,V_jk f_k>`, with `<h,g>=∫conj(h)g`.

Distinct integer logarithms in the admissible window are separated by much more than `2δ_k`: for `N≥8`, all `n≤2N` have spacing at least `log(1+1/(2N))>1/(2N+1)>2δ_k`. Hence **all translates of any `g` supported in `I_k` are pairwise disjoint** on the whole line, giving the exact identity

`||V_jk g||_2² = b_jk² ||g||_2²`, where `b_jk²=Σ_{n∈A_jk} Λ(n)²/n`.

The UOI045 scalar comparison used `b_jk` directly; its Gamma-normalized largest eigenvalue diverges. Here we preserve frequency information in the pairings rather than replacing them with `b_jk ||f_j||||f_k||` immediately.

## 3. The low-frequency packet bound from the zero mean

A global elementary Chebyshev upper bound `ψ(x)=Σ_{n≤x}Λ(n)≤C_ψ x` (for some fixed absolute `C_ψ`) gives, since `A_jk⊂(N/2,2N)`, 

`Σ_{n∈A_jk}κ_n ≤ 2√2 C_ψ √N`.

The local mean-zero condition gives for every frequency ξ,

`|hat f_k(ξ)| ≤ 2π |ξ| δ_k sqrt(2δ_k) ||f_k||_2`.

The Fourier multiplier of `V_jk` is the **exact finite original arithmetic phase sum** `M_jk(ξ)=Σ_n κ_n exp(2πi ξ log n)` (no absolute value is inserted in the identity). For `Pi_R`, the full-line projection to Fourier frequencies `|ξ|≤R`, the preceding bounds imply

`||Pi_R V_jk f_k||_2 ≤ 8π sqrt(2/3) C_ψ sqrt(N) δ_k^(3/2) R^(3/2) ||f_k||_2`.

Choose the **scale-matched cutoff** `R_d=√N=8^(d/2)`. Since `δ_k=δ 8^{−k}`,

> `||Pi_{R_d} V_jk f_k||_2 ≤ C_0 δ^(3/2) 8^(−3j/2) 8^(−d/4) ||f_k||_2`, with `C_0=8π sqrt(2/3) C_ψ`.

The geometric matrix `8^(−3j/2)8^(−(k−j)/4)` has bounded `l²→l²` norm (at most `1/(8^(1/4)−1)` by Young's convolution estimate). Thus summing the **low-frequency** portions of all original prime pairings costs at most

> `C_0 δ^(3/2)/(8^(1/4)−1) ||f||_2² ≤ [C_0 δ^(3/2)/(G(8^(1/4)−1))] Gamma(f)`.

This low-band screening uses only the first of the three local moments; the other two remove both original poles.

## 4. Short-interval arithmetic Bessel column bound

The key new *arithmetic* estimate is

> **Lemma:** There is a constant `C_A<∞`, independent of `k`, such that `Σ_{0≤j<k} b_jk² ≤ C_A(k+1)` for all `k≥1`.

Proof sketch with complete regimes (all implicit constants absolute and finite):

* The admissible interval lies in `(N/2,2N)` and has length `h=O(δ_j N)`, while `log(2N)=O(d)`.
* For `j≤k/3` and sufficiently large `k`, `h≥N^(1/6)`. The classical **Brun–Titchmarsh short-interval prime upper bound** `π(x+h)−π(x)≤2h/log h` then gives the ordinary-prime part of `b_jk²` as `O(δ_j d)`; the total composite prime-power part is `O((d+1)^3 8^(−d/2))`, since there are at most `O(√N log N)` relevant nonprime prime powers up to `2N`.
* For `j>k/3`, bound **all integers** in the interval by `O(δ_j N+1)`. This gives `b_jk²=O(δ_j d²+d² 8^(−d))`. Summing those bounds over `j>k/3` is `O(k²8^(−k/3)+1)=O(1)`.
* Finally `Σ_{j≤k/3} δ_j d ≤ k Σ_{j≥0}δ8^(−j)=O(k)`, and the higher-prime-power error in the early region is summable because `d≥2k/3`. Any finitely many smaller `k` are absorbed into the same `C_A`.

This **is not** the false scalar-envelope spectral norm bound from UOI045. Its claim is a *square-column* estimate on the actual original coefficients: the earlier normalized scalar first row can still have nondecaying entries, while the Fourier slices in §5 prevent all those interactions from saturating on one low-frequency hub.

Reference for the short-interval bound: Montgomery–Vaughan form cited in `https://math.mit.edu/~drew/PrimeGapsOberwolfach3.pdf` and `https://dms.umontreal.ca/~andrew/PDF/Pretentious010611.pdf`. This inequality is classical and unconditional; a Lean proof or accepted import in the project's pinned toolchain has **not** been checked.

## 5. High-frequency Bessel summation: one Gamma unit pays for all remote collars

Split each pair exactly by the same Fourier projection:

`<f_j,V_jk f_k> = <Pi_(≤R_d) f_j, Pi_(≤R_d)V_jk f_k> + <Pi_(>R_d)f_j, Pi_(>R_d)V_jk f_k>`.

Apply Cauchy–Schwarz across **all ordered edges** `j<k` to the high part:

`|Σ_{j<k} high_jk| ≤ [Σ_j Σ_{d≥1} ||Pi_(>8^(d/2)) f_j||_2²]^(1/2) [Σ_k ||f_k||_2² Σ_{j<k}b_jk²]^(1/2)`.

For the first factor, exchanging the sum and Fourier integral counts at most `(2/log8) log_+|ξ|` thresholds:

`Σ_{d≥1} ||Pi_(>8^(d/2))h||² ≤ (2/log8) ∫ log_+|ξ| |hat h(ξ)|²dξ ≤ (2/log8)L(h)`.

UOI045's **exact** spatial-log-energy decomposition and strict cross collar error `<1/1000 ||f||²` give

`Σ_j L(f_j) ≤ L(f)+ (1/1000)||f||² ≤ Gamma(f)+(28/5+1/1000)||f||²`.

The inherited `Gamma(f)≥G||f||²` therefore bounds the first factor by

`[ (2/log8)(1+(28/5+1/1000)/G) Gamma(f)]^(1/2)`.

For the second factor, the arithmetic lemma gives `≤[C_A Σ_k(k+1)||f_k||²]^(1/2)`. UOI045's all-stage spatial Gamma estimate supplies `Gamma(f)≥Σ_k g_k||f_k||²`, with `g_k=859/1000+3k/5≥3(k+1)/5`; hence the second factor is at most `[5C_A Gamma(f)/3]^(1/2)`.

Combining high and low parts and the factor **two** for the original `±log n` correlations yields the promised **all-stage relative bound**

> `|P(f)| ≤ C_* Gamma(f)` with, for instance,
>
> `C_* = 2 C_0 δ^(3/2)/[G(8^(1/4)−1)] + 2 sqrt( (10 C_A/(3 log8)) * (1+(28/5+1/1000)/G) )`.

All constants are finite and independent of `m`. This is a constructive mathematical bound once `C_ψ` and `C_A` are fixed; it is **not** optimized, and we do **not** assert `C_*<1`.

## 6. Operator completion and exact inclusion law

The bounded real Hermitian quadratic P on the dense linear union `S_infty` satisfies `|P(f)|≤C_*||f||_Gamma²`. By polarization its mixed form extends continuously to `H_infty×H_infty` and is represented uniquely by a **bounded self-adjoint** operator `A_infty`. Since literal `P` and `Gamma` are unchanged by zero extension, for the canonical form isometries `J_m:H_m→H_infty`,

> `A_m=J_m* A_infty J_m`, `rho_m=lambda_max(A_m)`, and `sup_m rho_m=sup σ(A_infty)≤C_*`.

The infinite operator need not be compact despite individual `A_m` being compact. Nor does its largest spectral value have to be an eigenvalue. The remaining research question is the **sign threshold** `sup σ(A_infty)≤1`, which this method does not settle.

**Compatibility:** any external spectral construction claiming a surjective Gamma/complete-prime form equivalence on this completed nested system must preserve the bounded operator up to unitary conjugacy, not merely a few finite-prime scalar coefficients. A non-surjective embedding preserves form values only on its image; it does not imply equality of full target spectra.

## 7. Verification boundary and formalization handoff

The companion `check_uoi046.py` recomputes stage-ten squared-column bounds from **unchanged** UOI044 exact rational majorant entries and verifies the zero-mean scaling exponent and geometric series. The finite check does **not** prove Brun–Titchmarsh, any Gamma integral, the infinite arithmetic lemma, or the all-stage operator theorem.

**Ledger #898:** record as a single addendum under **F04** (exact two-sided full-prime translations and orthogonality), **F10** (source Gamma/log-energy comparison), **F25** (infinite nested support and Fourier threshold counting), **F26** (Brun–Titchmarsh column-summation, relative form boundedness and completed self-adjoint operator), **F34** (form-preserving compatibility); **F01/F08** still required for complete original→native/source proof. All are *analytic targets*, not independently verified Lean declarations. No new CI activity.
