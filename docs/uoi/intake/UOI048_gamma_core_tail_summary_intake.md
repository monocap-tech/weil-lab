# Weil-Lab — UOI048: Gamma core–tail coupling intake (source-summary custody)

**2026-11-21 PT.** This file preserves the source *summary* supplied in conversation and the recovered exact-rational checker. The full mathematical derivation and exact original source-to-native attachment were **not** independently reconstructed in this repository recovery; this is NOT a kernel or complete analytic certification.

## Reported original restricted family and estimate

For a nested three-moment-neutral collar family, head `h` occupies collars `0,...,M-1`, tail `t` occupies collars `M,M+1,...`. The UOI048 report states the original mixed digamma estimate

```math
|\Gamma(h,t)| \le \frac{8^{-M}}{30000}\,\|h\|_2\|t\|_2,
\qquad \kappa_M < \frac{8^{-M}}{32970}.
```

At `M=10`, `kappa_10 < 2.83*10^(-14)`, and the recorded head margin is `alpha_10=14/25`. The positive infinite-tail margin `tau_10` and full-prime coupling upper bound `beta_10` are not certified.

The reported off-diagonal kernel, for `y>x`, is

```math
K_\Gamma(y-x)=-\frac{\exp(-(y-x)/2)}{1-\exp(-2(y-x))}.
```

Geometric expansion pairs exponential moments. The leading term vanishes when each collar test satisfies

```math
\int f_j(x)\,dx=\int f_j(x)e^{x/2}\,dx=\int f_j(x)e^{-x/2}\,dx=0.
```

The first surviving exponential order is `exp(-5(y-x)/2)`, as reported. The full original normalization, convergence, Fourier factors, and Gamma-completed domain remain independent proof obligations.

The UOI048 report also states that the cross-collar Gamma correction is Hilbert–Schmidt on the restricted family. This is **not** a claim of compactness for the complete prime operator.

## Terminal conditional target

With `beta_M` the Gamma-normalized original full-prime mixed head–tail norm and `tau_M` a positive infinite-tail Weil margin, the reported Schur sufficient condition is

```math
(\beta_M+\kappa_M)^2<\alpha_M\tau_M.
```

The condition is a sufficient quantitative criterion on the restricted family, **not** an equivalence theorem, support-independent positivity theorem, or RH proof.

## Recovered elementary verification

- `scripts/uoi/check_uoi048.py`: exact rational majorant, finite row/column checks, and Hilbert–Schmidt *bound arithmetic* only.
- `research/unified/receipts/UOI048_exact_constant_receipt.json`: arithmetic output with `verified_Lean_kernel=false` and `verified_original_native_form=false`.
- **Not recovered:** the complete original UOI048 analytic derivation and its source-verified collar family definition; geometric assumptions carried into UOI049 and UOI050 must be matched independently.
- **No new Lean acceptance:** this recovery does not compile the original digamma/source-domain lemmas.

This intake is included because UOI049 and UOI050 cite UOI048. It closes the omitted checker/receipt custody gap but explicitly leaves the analytic and formal proof gaps open.
