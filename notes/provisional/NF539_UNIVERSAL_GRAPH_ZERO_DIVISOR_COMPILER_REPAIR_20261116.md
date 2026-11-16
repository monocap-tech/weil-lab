# NF539 — universal full source graph → genuine zeta divisor, focused Lean compiler repair

**November 16, 2026 PT. Draft PR #567.** Original NF494 U400 SHA256 `39cba367d70243c2d15e5a9323fc8097d58187923dcf0eca2b031136871f0181` unchanged. The original 242 selected moments and exact true-zero multiplicity copies are untouched.

## Actual NF538 compilation receipts

[Focused NF538 CI #43816639413](https://github.com/monocap-tech/weil-lab/actions/runs/43816639413) completed **FAILURE**, but it passed the prior source-graph closure, generic literal zeta EF, and automatic full-divisor summability modules before the independent universal graph identity failed in `ActualZetaFullGraphRawDivisorQuadratic.lean` on exactly two local Lean elaboration errors:

- **Line 31:** `(sqrt(2)⁻¹)*(sqrt(2)⁻¹)=(sqrt(2)*sqrt(2))⁻¹` was not closed by `simp only [inv_pow,pow_two]`. NF539 uses `simp only [mul_inv_rev]`.
- **Line 122:** `re_inner_eq_norm_add_mul_self_sub_norm_sub_mul_self_div_four` lacked an explicit complex scalar field and the typeclass search got stuck. NF539 provides `(𝕜 := ℂ)`.

No theorem statement, authentic normalization, original source or divisor indexing was altered. The new dedicated [NF539 CI run #43832483415](https://github.com/monocap-tech/weil-lab/actions/runs/43832483415) must be checked to determine actual acceptance. **The universal full graph Lean theorem is NOT yet accepted.**

## Exact universal algebra

For each existing authentic `h : NeutralActualZetaSourceDomain a`, the original source graph already contains both `P,N ∈ ℓ²(Σρ Fin(mρ))`, with exactly the original pair:
$$
P_q=(A_q+B_q)/\sqrt2,\quad N_q=(A_q-B_q)/\sqrt2,\quad
A_q=F_h(\bar z_q),\ B_q=F_h(z_q).
$$
Thus `A,B ∈ ℓ²`, and their mixed product is absolutely summable without RH or Green density. There is a SECOND multiplication by `1/sqrt2` in the authentic `neutralActualZetaSourceQuadratic`, giving
$$
Q(h)=\frac12(\|P\|_2^2-\|N\|_2^2)
=\operatorname{Re}\sum_{q\in D_\zeta}\overline{F_h(\bar z_q)}F_h(z_q).
$$
When the physical autocorrelation of the SAME `h` is `C²`, the imported complete authentic zeta EF implies `Q(h)=Re literatureRHS(C_h)`. The zero-side identity is unrestricted within the actual existing source graph, but the `C²` hypothesis is not universally automatic, and there is **no claim** every physical test or the singular original `ell_U` is already in that graph.

## Fresh finite-rational checks

NF539 reran original exact Fraction scripts:
- NF526 `verify_nf526_original_prime_support_exact.py`: PASS, only original prime-power `n=9` on the true (B=11/10,\delta=1/500) support.
- NF527 `verify_nf527_collared_arch_coercivity_exact.py`: PASS, bounds `133/250` arch gain, prime absolute <`2/5`, pole absolute <`4/125`; strict original smooth-test margin `1/10` **conditionally on inherited analytical identities**.
- NF528 `verify_nf528_collar_preserving_geometry_and_normalization_exact.py`: PASS, ten exact finite true-partner P/N normalization rows.

This is not a new U400 source replay, nor compiled infinite-dimensional arithmetic coercivity.

## Remaining proof obligations and no-transfer

- NF529 source graph closure: previous dedicated **LEAN PASS**.
- NF532 generic physical window correlation true zeta EF: previous **LEAN PASS**.
- NF533 automatic actual divisor summability: repaired in NF535, **LEAN PASS** in NF535 CI.
- NF534 a.e. smooth convolution, NF535 original collar physical L², NF536 odd samples/general non-Green source graph lift, NF537 raw-to-PN ℓ² transport: **not yet Lean-certified**. NF538 previously fixed two NF534 elaboration errors but those remain CI-pending.
- NF539 universal graph-to-zero-series: mathematical two-by-two algebra established, new standalone Lean target corrected, **CI PENDING**.
- Original (C_c^\infty(E)) logarithmic Hilbert carrier admission, authentic NF527 two-collar gamma/prime9/pole one-tenth coercivity, original NF524/NF528 singular carrier full graph convergence and original physical nonzero premise: **OPEN as Lean obligations**.
- Global odd/even coercivity, W_ODD_NEG and RH: **OPEN**.

**NF539 status:** compiler repair and independent exact arithmetic replay, formal universal identity acceptance pending.
