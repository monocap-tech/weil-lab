# Weil-Lab — NF common-form identification square (read-only)

Date: 2026-10-27. Repo: `monocap-tech/weil-lab`. Inspected research head `3a06261ae27c46f73c3687c974d7b23624ab0dd5` (PR #355) and main RH interface appendix. This is an analytic dependency audit, not a new formal theorem, CI acceptance, or repository mutation.

## A. Canonical domain and original odd form at B=11/10

Let `H=L²([-B,B])`, with zero extension `Z:H→L²(R)`, and

`D_B={f∈H: E_log(f)=∫ log(e+|ξ|)|F(Zf)(ξ)|²dξ <∞}`.

In the original Fourier convention `Ff(ξ)=∫ f(x)exp(-2πiξx)dx` let

`m_B(ξ)=Re ψ(1/4+iπξ)-log π-2 Σ_{n∈{2,3,4,5,7,8,9}} Λ(n)/√n cos(2πξ log n)`.

Since `log 9<2B<log 10` and Λ(n)=0 for non-prime powers, this is the whole actual frozen-prime sum at B, with no equality-threshold term. The native canonical quadratic is

`q_B(f)=∫m_B(ξ)|F(Zf)(ξ)|²dξ + 2 Re(conj M_-(f)*M_+(f))`, with `M_±(f)=∫_{-B}^B f(x)exp(±x/2)dx`, respecting the project's Hermitian conventions.

For odd `f`, `M_+(f)=〈f,s〉`, `M_-(f)=-〈f,s〉`, `s(x)=sinh(x/2)`. Hence

`q_B(f)=∫m_B(ξ)|F(Zf)(ξ)|²dξ - 2|〈f,s〉|²`.

Original SI10/SM41 define `κ=1/1000`, `a_o=max(κ,m_B)`, and `k_-=(κ-m_B)_+`. Pointwise `a_o-k_-=m_B`. Thus on the same odd supported logarithmic form domain,

`q_B|odd = a_o - 2|s〉〈s| - k_- = w_o`.

This is *form equality*, not identification of a whole-line strong Fourier multiplier with a compressed physical operator on an unproved operator domain. Polarization gives the mixed identity.

## B. Closed-form realization (analytic reduction)

The certified actual symbol logarithmic-envelope theorem supplies `|m_B-w|≤C_B`, `w=log(e+|ξ|)≥1`. The pole bilinear is bounded in physical L², so `q_B-E_log` extends to a bounded Hermitian physical L² bilinear form. Thus `q_B+c||·||²` has a norm equivalent to `E_log` for a sufficiently large finite `c`, and is a closed semibounded form on `D_B`. Reflection commutes with the multiplier and pole kernel, so the odd restriction is closed. The associated selfadjoint odd form operator is unique by the first representation theorem.

The *operator-domain* characterization must remain form-theoretic:

`Dom(W_o)={u∈D_B^odd: ∃g∈H_odd, w_o(u,v)=〈g,v〉 for every v∈D_B^odd}`.

No equality of this set with the domain of the uncompressed whole-line multiplier is claimed. Membership of each supported polynomial-trigonometric source follows from its `O(|ξ|^{-1})` Fourier tail and `∫_1^∞log(t)t^{-2}dt<∞`. Hence the physical `J_242` projection preserves the form domain and maps the odd smooth core densely onto `(I-P_J)D_B^odd` in form norm.

## C. Source/native square: two available paths

Existing certified Lean results:
* `ActualZetaCanonicalNativeEnergy`: concrete native quadratic on all supported-logarithmic vectors;
* `ActualZetaNativeFormOperator`: bounded native form operator in the *logarithmic carrier* norm, not automatically an L² strong operator;
* `ActualZetaGreenGraphMixed`: normalized actual-divisor P-minus-N source covariance equals native form on the Green graph closure.

Existing analytic result (not newly Lean-certified): `REFLECTED_PACKET_BRIDGE_108_LOG_SAMPLING_GRAPH_DENSITY_20261004.md` proves full actual divisor sampling bounded by log energy and claims the source graph equals Green closure, yielding all-domain source/native equality. The global source/raw normalization is critical: raw full-divisor partner zero form = **2 ×** canonical native form, while normalized P-minus-N source covariance = canonical native form.

**Independent proposed shorter extension route:**
1. For any `f,g∈C_c^∞((-B,B))`, build their compact mixed correlation `K_fg(t)=∫f(x)overline{g(x-t)}dx`. It is `C_c^∞`, so it is eligible for the *generic* repository theorem `Zeta23.WeilEF.EF_lit_zeta (hs:ZetaSeam)` (which accepts any compact `C²` test), not only the constructed Green correlation.
2. Prove the direct Fourier product identity for this same `K_fg`, and apply the actual explicit formula plus native prime, digamma, and pole dictionaries. Preserve partner-conjugation, copy multiplicities, Fourier `2π` normalization, and raw-factor-two. Conclude normalized source/native equality on all compactly supported smooth pairs. This is **not** yet a newly compiled Lean composition.
3. The existing unit-window zero-count/reproducing-kernel bound controls all raw actual samples by `E_log` for any supported vector; hence normalized P/N mixed source covariance is continuous on `D_B×D_B`. The native form is also continuous by the bounded log-symbol ratio and pole bound.
4. Inward dilation and compact mollification give `C_c^∞((-B,B))` density in `D_B` (and its odd restriction) in logarithmic form norm. Passing both variables to the limit gives the identity on the entire supported log carrier, without first showing Green-graph closure equals the entire source graph.

The new route replaces one dependency (the full Green-graph density step) with explicit arbitrary-test correlation/Fourier normalizations and the generic EF proof. Audit those identities and the `ZetaSeam` dependency before formal promotion. No assertion that this route was newly proved in Lean or independently CI-replayed.

## D. Separate transfer obligations remain OPEN

* Historical WD-T38 abstract witness: actual same physical vector, source map, selected coefficients, `P/C/k` identity and endpoint weak-null attachment. The carrier theorem alone does not construct this witness.
* WD-T40: conditional strict-null-extension exclusion on the RPB branch. Main branch appendix still calls the neutral interface OPEN; reconcile custody and theorem scope, not by overwriting main.
* `AZ-NEXTJET-LOC`: negative defect near-field arithmetic; not solved by source/native form equality.
* Direct approach: full signed odd/even positivity, including **upper** control of the infinite-dimensional Schur correction, remains OPEN. Domain/form equality cannot imply a sign.
* Original L² strong-operator action and inverse residual estimates: require the form-derived operator domain or separate strong-domain proof. An isometric form identity does not automatically transport arbitrary strong-multiplier actions.
* Full source domination / F4 / RH: OPEN.

## E. Cursor and recommendation

The *common form* is already expressible by the same symbol and pole on the same supported logarithmic physical domain. Treat its analytic equality as a **compositional audit/normalization port**, not a novel positivity theorem. Highest-value near-term formal task: prove the direct arbitrary-smooth-correlation source/native lemma and transfer by log-form density, with exact factor-two audit. Preserve the original signed Schur remainder as a distinct quantitative problem. No automatic reopening of NEXTJET or null-extension.

### Source links

- https://github.com/monocap-tech/weil-lab/blob/research/original-exterior-scalar-floor-stop/notes/RPB108_SI10_COMPLEMENT_POSITIVITY_20261015.md
- https://github.com/monocap-tech/weil-lab/blob/research/original-exterior-scalar-floor-stop/notes/RPB108_SM41_ORIGINAL_POSITIVE_LOG_TAIL_20261018.md
- https://github.com/monocap-tech/weil-lab/blob/research/original-exterior-scalar-floor-stop/notes/REFLECTED_PACKET_BRIDGE_108_ACTUAL_CANONICAL_NATIVE_ENERGY_20261004.md
- https://github.com/monocap-tech/weil-lab/blob/research/original-exterior-scalar-floor-stop/notes/REFLECTED_PACKET_BRIDGE_108_LOG_SAMPLING_GRAPH_DENSITY_20261004.md
- https://github.com/monocap-tech/weil-lab/blob/research/rpb108-direct-null-exclusion/notes/REFLECTED_PACKET_BRIDGE_65_20260929.md
- https://github.com/monocap-tech/weil-lab/blob/main/docs/RH_INTERFACE_APPENDIX.md
