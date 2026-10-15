# RC315 — Original signed Weil P0/P1 low-mode sign audit

**Parent:** RC314 merge `f63b5a6e85edb6d2fedf111a5a9f133db3c05c3e`.  
**Object:** the *original* CC27 signed Weil form at (B=11/10), identified with the completed native action at RC313.  
**Standing:** positive on the particular (P_0)/(P_1) subspace only; full Schur positivity, Stage I, F4, RH, and Lean are OPEN.

## What is actually tested

Let (u_n(x)=\sqrt{(2n+1)/(2B)}P_n(x/B)). These are physically (L^2[-B,B])-orthonormal, not (D)-normalized. RC312/313 give the original operator quadratic form

[
Q=J+W_B+c_RI-K_{\rm reg}+K_{\rm prime}+K_{\rm pole},
\qquad c_R=-\gamma-\log(2\pi\cdot 2B),
]
where (JP_n=H_nP_n), (W_B=\log 2-\tfrac12\log(1-t^2)), the prime term is the correctly signed *two* zero-extended translations per prime power, and the pole term has positive even and negative odd rank-one parts.

For the first two physical Legendre modes, all original-form terms have *independent explicit formulas*:

| Component | (u_0) | (u_1) |
|---|---|---|
| (J) | (0) | (1) |
| (\langle W_B\rangle) | (1) | (4/3) |
| prime autocorrelation at (\ell>0), (d=\ell/B) | (1-d/2) | (1-3d/2+d^3/4) |
| full prime term | (-2\sum_{n\in\{2,3,4,5,7,8,9\}}\frac{\Lambda(n)}{\sqrt n}C_{00}(\log n)) | same with (C_{11}) |
| pole term | (16\sinh^2(B/2)/B) | (-3[4\cosh(B/2)-8\sinh(B/2)/B]^2/B) |

For the regular convolution, each (r_k t^k) contributes (2r_k(2B)^{k+1}\int_0^1v^k C_{ii}(2Bv)dv). The RC46 degree-192 Taylor coefficients and its certified global uniform remainder are checked against their pinned Git blob. The remainder is paid using (|C_{ii}(t)|\le1).

Euler's constant is enclosed using (H_{128}-\log128-1/256<\gamma<H_{128}-\log128-1/256+1/(12\cdot128^2)). The code encloses logarithms with positive rational atanh series, pi with Machin's identity and alternating arctangent series, and hyperbolic moments with positive Taylor series. No floating-point quadrature or interpolation appears in the certificate.

## Result and limitation

The expected outward rational enclosures are approximately

[
\langle u_0,Qu_0\rangle\in(0.040254,0.040260),\qquad
\langle u_1,Qu_1\rangle\in(0.132385,0.132391).
]

Parity makes (langle u_0,Qu_1\rangle=0) exactly, so the original (2\times2) principal form is positive. This replaces the much wider low-head enclosures in RC46 *for these two specific entries*, without altering the original operator.

**Not proved:** positivity of any Schur complement, the larger (301/317)-dimensional original principal blocks, positivity after minimizing over the high modes, or the absence of negative/null spectrum. Even a positive (2\times2) principal block can have a negative Schur complement.

## Next frontier

RC316 should compute at least one nonzero **original signed** cross-block action (T=QN_0P) with rigorous finite and infinite tail payment. Then build an actual high response (Y), prove its signed action residual (R=T-CY) and Gram, and apply RC314's **minus-sign** correction. Avoid converting this preliminary low-sector test into a claim of Stage I closure.

## Reproduce

```bash
python scripts/validate_rpb108_rc315_low_mode_sign.py --output certificates/rpb108_rc315_low_mode_sign.json
python scripts/validate_rpb108_rc315_low_mode_sign.py --output certificates/rpb108_rc315_low_mode_sign.json --replay
```
