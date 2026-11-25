# Weil-Lab — CF020: adjacent-interface and dyadic prime-silent boundary coercivity

Date: 2026-11-21. **Analytic derivation, local numerical controls only. No GitHub write, no Lean build, no Actions.** Original HD/A frontier unchanged **692/968**. No RH or first-contact exclusion claim.

## A. Exact original-form source and normalization

Read-only checked source branch: `research/iv023-original-four-cell-schwartz-partition-and-prime-transfer`.

- `WeilDefect/Arithmetic/ActualZetaNativeLogBounds.lean`, blob `f8728d020bff9d0427ae6e4969da355f37182224`: `neutralActualZetaArchimedean_log_bound` proves the uniform bound on the genuine archimedean multiplier minus the canonical weight.
- `WeilDefect/Arithmetic/LogarithmicForm.lean`, blob `ae932d4f3f7e4d6d06dbd778a5708927172238dc`: `logarithmicFourierWeight ξ=log(exp(1)+|ξ|)`.
- `WeilDefect/Morphology/NeutralLogPoleSourceAttachment.lean`, blob `331ad94a02336a124eb6c17e3ee94480694a8c5c`: the pole mixed form is exactly the sum of two Hermitian *cross* moments.
- `WeilDefect/Arithmetic/ActualZetaNativeWeilForm.lean`, blob `961b6742782fa3f808ac9b70cfadfc0790c8fc32`: true Gamma-minus-prime plus signed pole native mixed form.

Let `D` be the compactly supported logarithmic Fourier form domain; `||f||log²=∫ log(exp(1)+|ξ|)|Ff(ξ)|² dξ`, with `Ff(ξ)=∫exp(-2πiξx)f(x)dx`. Then `||f||2≤||f||log`. Let `B_W` denote the true original complex Hermitian form. The reference identity from CF015 and CF019 is `B_W=B_ref-2D_arith`, with `B_ref=B_Gamma+B_continuum+pole` and positive convolution-reference kernel `exp(-|x-y|/2)`.

For disjoint physical supports, `B_ref(u,v)=-∫∫ conj(u(x))v(y) q(|x-y|)dxdy` with

`q(s)=exp(-5s/2)/(1-exp(-2s))=exp(-3s/2)/(2sinh(s))`.

The resulting integral is absolutely convergent for ordered touching supports by the Hilbert–Carleman estimate below; the identity follows first for positive-gap smooth tests and extends by boundedness and density.

## B. CF020-A: exact gap-free Carleman bound

For every `s>0`, `0<q(s)≤1/(2s)`. Indeed `exp(-3s/2)≤1` and `sinh(s)≥s`.

If `supp(u)⊂(-∞,b]` and `supp(v)⊂[b,∞)`, write `r=b-x≥0`, `t=y-b≥0` to get

`|B_ref(u,v)| ≤ 1/2 ∫_0∞∫_0∞ |u(b-r)| |v(b+t)|/(r+t) dr dt`.

The Hilbert–Carleman operator `Cf(r)=∫_0∞f(t)/(r+t)dt` has `L²` norm `π`. An elementary Schur proof uses positive weight `h(r)=r^{-1/2}` and the identity `∫_0∞ h(t)/(r+t)dt = π h(r)`; apply weighted Schur on each slot. Hence

`|B_ref(u,v)|≤(π/2)||u||₂||v||₂`.

This is uniform at zero interface gap, allows arbitrary complex phases and disjoint logarithmic form-domain functions, and is sharp in the scale-invariant `L²` limit (truncated `s^{-1/2}` Mellin profiles at shrinking scales). It does not imply positivity of the full form.

## C. CF020-B: original logarithmic-norm adjacent decoupling

If `v` lies on the right and occupies width `ell`, the prior proven CF018 Fourier-capacity inequality gives

`||v||₂≤α(ell)||v||log`, `α(ell)=sqrt(2/log(exp(1)+1/(4ell)))`.

Therefore

`|B_ref(u,v)| ≤ (π/2)α(ell)||u||log||v||log`.

With CF018's phase-sensitive mixed discrepancy inequality `|D_arith(u,v)|≤A_c(ell)||u||log||v||log` and `A_c(ell)=O_c(1/log(1/ell))`, we get the full-form bound

`|B_W(u,v)| ≤ η_c(ell)||u||log||v||log`,
`η_c(ell)=(π/2)α(ell)+2A_c(ell)=O_c(1/sqrt(log(1/ell)))`.

Independently of CF018's sharper discrepancy bound, one can check the coarser unconditional fixed-`c` estimate from the exact Fourier multiplier:

`|D_arith(u,v)|≤[S_c+2(exp(c)-1)]||u||₂||v||₂`,

where `S_c=∑_{log n<2c} Λ(n)/sqrt(n)`. This gives a separation-free complete-form bound with explicit coefficient `[π/2+2S_c+4(exp(c)-1)]α(ell)` in the original logarithmic norm. Thus the qualitative vanishing does not rely on a sharp CF017 estimate.

If **both** adjacent supports have widths ≤`ell`, then the reference bound becomes `|B_ref(u,v)|≤π/log(exp(1)+1/(4ell))||u||log||v||log`.

## D. CF020-C: universal prime-silent local Gårding bound

Let `C_Γ≥0` be any constant satisfying the verified original symbol inequality

`|g(2πξ)-w(ξ)|≤C_Γ`, with `g(t)=Re digamma(1/4+it/2)-log(π)`.

Consider `v` supported in **any** interval of length at most `a_0`, with `a_0<log 2`. Every prime-power autocorrelation of `v` vanishes. Translation invariance of the true full form (including both cross-pole moments) allows centering that interval.

Cauchy–Schwarz on centered support gives `|M_±(v)|²≤2sinh(a_0/2)||v||₂²`, so

`|P_pole(v)|≤4sinh(a_0/2)||v||₂²`.

Therefore, with `M_* = C_Γ+4sinh(a_0/2)`, **independently of the original global window radius**,

`Q_W(v)≥||v||log² - M_*||v||₂²`.

Combining with interval Fourier capacity gives

`Q_W(v)≥[1-M_* α(ell)²]||v||log²` for packet width `ell≤a_0`.

Thus every packet of sufficiently small width enjoys `Q_W(v)≥(1/2)||v||log²`, with an admissible width controlled by a *fixed* `M_*`, not by the total support radius. This is a genuine support-independent local microcoercivity theorem; it is **not** a support-independent positivity theorem for general supported tests.

## E. CF020-D: dyadic shell screening theorem

Take a boundary collar `I=(b-a,b)` of length `0<a<a_0<log2`, and set the dyadic shells

`I_j=(b-a 2^{-j}, b-a 2^{-(j+1)})`, `j=0,1,2,...`,

with widths `δ_j=a 2^{-(j+1)}`. Let `u_j∈D` be arbitrary complex supported logarithmic vectors with `supp(u_j)⊂cl(I_j)`. For the theorem below, take any *finite* subfamily; no unproved infinite splitting of an arbitrary vector is assumed.

All prime mixed correlations between the shells vanish (every two points lie within one interval of length `<log2`). The exact full-form off-diagonal physical kernel simplifies to

`B_W(u_j,u_k)=∫∫conj(u_j(x))u_k(y)[exp(|x-y|/2)-q(|x-y|)]dxdy`, `j≠k`.

For adjacent `k=j+1`, the Carleman bound gives

`|∫∫conj(u_j)u_k q|≤(π/2)||u_j||₂||u_k||₂`.

For `k≥j+2`, the minimum gap is at least `a 2^{-(j+2)}`, and `q(s)≤1/(2s)` with Cauchy–Schwarz gives

`|∫∫conj(u_j)u_k q|≤2^{-(k-j)/2}||u_j||₂||u_k||₂`.

The sum of absolute row coefficients in this symmetric matrix is bounded by

`R=2[(π/2)+∑_{m=2}∞2^{-m/2}]=π+2+sqrt(2)`.

Meanwhile the smooth term is bounded by

`|∑_{j≠k}∫∫conj(u_j)u_k exp(|x-y|/2)| ≤ exp(a/2) a ∑_j||u_j||₂²`

using `∑δ_j=a` and Cauchy–Schwarz on `∑||u_j||_1`.

Let `α_a²=2/log(exp(1)+1/(2a))`. Since `δ_j≤a/2`, interval capacity gives `||u_j||₂²≤α_a²||u_j||log²`. Combining the estimates,

`|∑_{j≠k}B_W(u_j,u_k)| ≤ α_a² [π+2+sqrt(2)+a exp(a/2)] ∑_j||u_j||log²`.

And the universal local Gårding bound from part D supplies the diagonal terms. Consequently:

**CF020 dyadic block-coercivity**

`Q_W(∑_j u_j) ≥ {1 - α_a² [M_* + π+2+sqrt(2)+a exp(a/2)]} ∑_j ||u_j||log²`.

The bracket tends to `1` as `a↓0`, **uniformly in the total support window**, and is at least `1/2` for sufficiently small `a`. The theorem is established for finite sums of individually admissible shell vectors. Extending to arbitrary sharp-cut decompositions requires a separate logarithmic multiplier/stable decomposition lemma.

## F. Neutral-mode screening consequence and current stop

Suppose `k` is a genuine full-form neutral vector at a nonnegative window, with a lawful non-overlapping split `k=u+v` across an interface, where `v` occupies a terminal collar of width `ell`. Exact mixed nullity gives `Q_W(v)=-B_W(u,v)`. For narrow enough `ell`, parts C and D imply

`||v||log ≤ 2η_c(ell)||u||log` provided `v≠0`.

Thus **uncontrolled order-one operator coupling across a lawful sharp interface is excluded**; a neutral mode, if one exists, must have unusually small logarithmic endpoint energy relative to the interior (at most `O_c(1/sqrt(log(1/ell)))` in this particular estimate). This does **not** logically exclude CF018’s strong-coupling alternative for a very small `v`: both alternatives may hold simultaneously. This is compatible with CF012 endpoint-support saturation, which demands nonzero mass in every collar but gives no matching positive lower-rate bound.

Crucial domain gate: the sharp cutoff `u=1_{(-∞,b)}k`, `v=1_{(b,∞)}k` has not been independently attached in Lean to the original logarithmic carrier. Such cutoffs are expected to be bounded by the weighted-Hilbert-transform theory for the `A₂` weight `w(ξ)=log(e+|ξ|)`, but this must be proved or replaced by a lawful smooth decomposition with a controlled overlap. Do not apply the split consequence to every null vector without this gate.

The dyadic shell estimate cannot be summed over an arbitrary neutral `k` without proving an appropriate square-summable decomposition of its logarithmic form energy. Do not infer global contact exclusion or positivity from the finite-block theorem.

## G. Reproducibility and verification

Execute: `python /mnt/data/cf020_adjacent_dyadic_validator.py`.

The script checks: pointwise `K_Γ-G=q`; the global inequality `q≤1/(2s)`; near-sharp Carleman trial profiles; geometric dyadic cross-coupling coefficients; the direct original prime-silent kernel identity `2cosh(s/2)-K_Γ(s)=exp(s/2)-q(s)`; and complex-phase off-diagonal upper bounds. All numerical quadrature is exploratory, not interval-certified. No primary source or accepted artifact is changed.

**Next formal tasks (controlled CI only once workflow branch gate is cleared):**
1. Prove one-sided Carleman bilinear inequality and `q≤1/(2s)` in a small standalone Mathlib module, with genuine complex polarization.
2. Attach the exact kernel reduction to the native Weil form and prove the support-width `<log2` prime silence, preserving strict activation conventions and native pole signs.
3. Prove interval Fourier capacity and universal local Gårding in the current `neutralLogHilbertCarrier`.
4. Prove finite dyadic shell estimates, then separately investigate the *logarithmic sharp-cutoff multiplier* and square-summable dyadic decomposition.
5. Compare the prime-silent microscopic result with IV030 phase-sensitive remote graph: local off-diagonal suppression does **not** erase remote prime-shift phases. No cross-projection equivalence is claimed.

**GitHub Actions:** not needed for the present analytic/local validation. No PR or heavy CI should run until the chosen branch demonstrably contains repaired source-scoped triggers, appropriate pinning/manifest preflight order and bounded PR fan-out. Keep NF750–NF753 accepted certificates and strict axiom-audit custody unchanged. Original HD/A frontier **692/968**.
