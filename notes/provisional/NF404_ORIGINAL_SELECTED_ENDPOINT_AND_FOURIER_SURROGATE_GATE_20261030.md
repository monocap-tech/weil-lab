# NF404 — Original 242D projection endpoint and the whole-line Fourier method boundary

**2026-10-30 PT.** Active original `W-ODD-NEG` OPEN. Scope: unchanged original J242, actual NF370 fourth source u4, all original seven signed prime powers, arch and the corrected original odd-pole restoration. **Do not conflate the projected selected vector with the full original multiplier response.**

## Previous → Current → Next

**Previous NF403:** Certified original J242 lowband complement **lower** >8.63e-14 and exact **conditional** sufficient upper target for `||1_I m(D)u4||²` within about 5.13e-26 above accepted selected projection squared norm. That original physical full-action scalar and full lowband complement upper remain UNCOMPUTED.

**Current NF404:** SHA-pinned recomputation of the original **physical** 242×242 Gram and archived dyadic D frame, with no signed-kernel reintegration. The input is the byte-identical NF401 accepted entire 242D transformed signed-plus-pole response column SHA256 `644337986f62a3f25bb6b2005efc82f517975c84629b32b5ae8d1e5b95614515` with all 242 outward source/rounding errors. Compute original raw selected coefficients `z=D(D^T H D)^-1 d`, check all 242 RAW original native signed/pole moment intervals, reconstruct original projected mass and evaluate the **real original selected projection's endpoint** and first derivative. This is the selected physical projection `j*=P_J(1_I m(D)u4)`, NOT `w=1_I m(D)u4` itself. Original 4096-bit Arb native endpoint computation and independent exact Fraction receipt **SUCCESS** in [Actions #41127177710](https://github.com/monocap-tech/weil-lab/actions/runs/41127177710).

Actual original selected source native endpoint:
```
j_*(B)  ≈ +0.8371177807578  (CERTIFIED nonzero)
j_*'(B) ≈ +0.8362471315245  (certified original selected derivative)
B = 11/10
```
The first native run reconstructed/overlapped all 242 accepted original raw selected moments and the full projected norm interval, independently checked Riesz trace/Cauchy inequalities and preserved source-native evidence `notes/data/provisional/NF404_original_selected_endpoint_native.json` and `NF404_original_selected_endpoint_acceptance.json`. First native endpoint SHA256 `a09b22f7f653e5eb2af516a6e6104d2d1e27b525c9cdc8bc0074c212b6982c94`.

**Derivative structural observation, original carrier:** For each original retained center `c`, the selected generators are contiguous prefixes
```
f_(c,k)(x) = x^k sin(2*pi*c*x) if k even,
           = x^k cos(2*pi*c*x) if k odd.
```
Writing `omega=2*pi*c`, for every retained `k`,
```
f_(c,k)'' =
  -omega² f_(c,k)
  + (-1)^k (2*k*omega) f_(c,k-1)       [k>=1]
  + k(k-1) f_(c,k-2)                   [k>=2].
```
The final pole generator `s=sinh(x/2)` obeys `s''=s/4`. Thus the original finite selected space is **invariant under the physical second derivative on the open support interval**. This allows an actual `||j_*''||_I` and endpoint `j_*''(B),j_*'''(B)` to be computed by original coefficient transport through the already authenticated physical Gram; no new signed integrals and no 242×242 derivative Gram rebuild. Do NOT differentiate the zero extension without paying its boundary distributions.

## Source-specific Fourier-tail method test and the information limit

The numerical second-derivative and Fourier tail source-native acceptance is a SEPARATE **ACCEPTED** execution gate, not inferred from the endpoint value alone. The original native job + independent root-free Fraction receipt Actions #41127751093 completed SUCCESS, true original native tail report SHA256 `f64016929e27c3fba0c4ca4ca72cea4d159a0559271f9747f39a593ef79b8df8`. The first attempt Actions #41127562921 failed only on an independent JSON key mismatch AFTER authentic native tail completion; the failure is retained without retroactive promotion. The new producer and independent root-free Fraction receipt compute a TRUE original source-specific lower on the full-line Fourier **highband of the zero-extended selected `j_*`**. The exact analytic proof is:

For original odd `j_*` smooth inside `I=[-B,B]`, the endpoint value is nonzero, and integration by parts twice gives, for `xi>0`,
```
hat(j*)(xi) = boundary_leading(xi)+remainder(xi)
|boundary_leading| = |j*(B) cos(2*pi*B*xi)|/(pi*xi)
|remainder| <= [2|j*'(B)|+||j*''||_L1(I)]/(4*pi²*xi²).
```
On the two symmetric frequency slabs `Lambda<=|xi|<=2Lambda`, `Lambda=2^24`, use `3<pi<4`,
```
||boundary_leading||² >= |j*(B)|² * (Lambda/2 - 1/(12B))/(32Lambda²)
||remainder||_(|xi|>=Lambda) < K/36 *sqrt(2/(3Lambda³)),
K=2|j*'(B)|+sqrt(2B)||j*''||_I .
```
Every quantity in this bound is original-source finite physical Gram or original endpoint data. The independent source verifier also checks **without square roots** the more conservative rational bound
```
||B_high j_*|| >
 |j_*(B)|_lower /36864
 - [2|j_*'(B)|_upper+(3/2)||j_*''||_upper] /(36*2^36).
```
This uses `Lambda=2^24`, `sqrt(65)<9`, `sqrt(2B)<3/2`; it is a strictly conservative lower, not a floating sample. Its numerical standing is now **ACCEPTED**: native original selected Fourier tail >2.55468e-5, and a separate independent root-free exact-rational lower >2.270827e-5 (hence strictly >2e-5). Certified original selected physical second derivative norm `||j_*''||≈0.1757165689` and endpoint derivative `j_*'(B)≈0.8362471315`. The full-line Fourier-primal sufficient METHOD STOP is accepted for the entire NF401 admissible physical-norm ball; this does NOT establish any actual original physical lowband mismatch.

**Source-certified tail >2e-5 (native lower ≈2.554680652e-5):** Every original selected j meeting NF401 necessary physical ball `||j-j_*||_I <=rho=H+tau<3.29e-13` obeys, by Plancherel,
```
||B_high j|| >= ||B_high j_*||-rho >1e-6-rho.
```
This would be a universal **METHOD STOP** for the NF386 whole-line positive Fourier-primal sufficient upper, since its whole-line tail of `j` alone then exceeds the physical fourth target `tau=2.8e-13` by over six orders of magnitude; and `||m(D)u4-j||_whole-line >=||B_high j||-H` also vastly exceeds `tau`. **This does NOT imply a positive physical lowband error**: NF402 proved support restriction and Fourier cutoff do not commute. Whole-line bandlimited `U_L` can have nontrivial exterior spatial leakage. Without a certified outside-support leakage upper or direct supported `||Q_J t_L||` upper, original physical lowband criterion, W-ODD-NEG and RH remain OPEN.

**Next NF405:** If the true source-specific full-line method STOP is certified, retire full-line Fourier-primal candidate integral for the whole NF401 admissible ball and prioritize **support-preserving positive residual computation** or the NF403 complete original supported full-multiplier-action scalar, with cancellation controlled to <1e-26. This is an explicit method selection, not a new positivity/negativity theorem, and no new source family/branch is opened.

## Custody and scope

The original physical selected projection endpoint is source-recovered and independently accepted. The derivative carrier invariance is an exact elementary analytic identity checked against original rank/prefix structure in the native producer. The dedicated Fourier-tail native and root-free independent CI **PASSED** in Actions #41127751093, authenticating the universal full-line surrogate METHOD STOP. Earlier independent-parser failure #41127562921 remains a documented historical failure. Original signed archive 30,371 cells, 4 original reflectors and all source SHA pins unchanged; zero fresh signed cells.

No original full-action supported scalar upper, original J-perpendicular lowband upper, infinite exterior form inverse or general operator-domain audit. No main merge. `W-ODD-NEG`, even/whole Weil, RH OPEN.


## New principal finding: remove the almost-pure original selected pole BEFORE the full norm integral

The fixed original pole `s=sinh(x/2)` is **already** one of the 242 accepted selected generators (original RAW index 241). Using the original NF401 actual outward selected norm and original pole *moment* `b_s=<w,s>` (not the signed odd pairing without pole correction), the physical squared norm of the pole is known analytically:

```
||s||_I² = sinh(11/10)-11/10 ≈ 0.23564747012417677938478.
```

An independent pure-`Fraction` replay of **100 terms** of `sinh(11/10)`, with exact geometric upper on the omitted positive Taylor tail, proves the original pole squared norm bracket to width <1e-200. Choose once the exact **dyadic** scalar

```
a = 26709425989909960852 / 18446744073709551616
  = 6677356497477490213 / 4611686018427387904
  ≈ 1.4479208842050587194034.
```

The original true `<w,s>/||s||²` lies within `2^-64` of this fixed dyadic `a`, as proven with the outward original 242D source-native pole moment and exact pole-norm enclosures. The identity

```
R_a² = ||P_J w-a s||_I²
     = ||P_J w||_I² -2a<w,s>+a²||s||_I²
```

is exact **for this fixed original source**. The [source-only, exact-rational Actions #41128201628](https://github.com/monocap-tech/weil-lab/actions/runs/41128201628) **SUCCESS** and durable result `notes/data/provisional/NF404_original_selected_pole_shear_exact.json` strictly certify

```
1.09e-21 < R_a² < 1.10e-21,
true source interval approximately R_a²≈1.0950024763e-21,
||P_J w||² ≈0.494... BEFORE pole-centering.
```

**This is the original-object simplification.** Since `s∈J`, the true original exterior response is **exactly invariant**:

```
Q_J(w-a s)=Q_J w.
```

By orthogonal Pythagoras,

```
||Q_J w||² = ||w-a s||² - R_a².
```

The untouched NF403 original fourth lowband sufficient power budget is `gamma²=(sigma-H)^2≈5.1296807868e-26`; using the entire exact source-certified lower bound `R_a,lo²`, we now have the **much better conditioned sufficient scalar acceptance**:

```
||1_I [m(D)u4-a sinh(x/2)]||²
       <= R_a,lo² + gamma²
       ≈ 1.0950537731e-21.                (NF404 centered gate)
```

Compared with the NF403 full scalar `||w||²≈0.494` that required a nearly 26-decimal cancellation, this positive centered physical scalar is expected **at the 1e-21 scale** if the original fourth residual can meet its budget; to decide the `≈5e-26` allowance now requires about **5e-5 relative resolution**, not ~1e-25. This is a >20-order improvement in conditioning of the next numerical physical scalar, not a numerical evaluation of that scalar. The actual centered integral is **UNMEASURED**, so there is still NO original physical `J242^perp` upper or lowband certificate.

The exact pole subtraction is intentionally applied to the ORIGINAL complete signed-multiplier physical response after the accepted odd-pole restoration. It does **not** delete or assume away the original pole term in Wodd, and introduces no new physical test function outside the existing original 242-dimensional selected space. The fixed `a` is dyadic; it can be certified directly in any future physical quadrature without having to represent a transcendental source-dependent pole coefficient. This is why NF405 should use the **centered positive support-restricted integral**, not the old uncentered global scalar or the definitively stopped whole-line Fourier surrogate.

## Final NF404 custody and disposition

- Original selected endpoint/native 4096-bit Arb #41127177710 **SUCCESS**; endpoint value `+0.837117780757802...` (not the full response boundary value), first derivative `+0.836247131524514...`.
- Original source true `j_*` Fourier tail #41127751093 **SUCCESS**, native >`2.55468e-5`, independently checked root-free exact lower >`2e-5` and full-line Fourier-primal **METHOD STOP** for *every* candidate satisfying NF401 necessary physical ball. First attempt #41127562921 **FAILURE** (receipt key only) retained.
- Original selected pole-centered 242D exact Fraction #41128201628 **SUCCESS**: **strict** original `||P_J w-a s||²∈(1.09e-21,1.10e-21)` and dyadic fixed pole coefficient `a`, new source-exact centered positive scalar acceptance target `≈1.0950537731e-21`.
- The **actual original centered physical scalar has not been integrated**; original fourth lowband/complement upper, whole infinite exterior inverse, general operator-domain transfer, even/whole Weil, RH OPEN. New signed cells 0; historical archives unchanged and research PR unmerged.
