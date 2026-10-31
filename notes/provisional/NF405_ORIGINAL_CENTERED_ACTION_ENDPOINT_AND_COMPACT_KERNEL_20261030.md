# NF405 — Original fourth centered physical action: endpoint extraction and compact translation kernel

**2026-10-30 Pacific.** Canonical `W-ODD-NEG` OPEN. Unchanged original 242 selected generators, original NF370 fourth direction `u4`, original NF404 fixed dyadic `a`, the full signed seven-prime/arch/pole-reconciled multiplier, physical support `I=[-11/10,11/10]`. **Standing:** exact-rational original-data highband and compact-operator identities **accepted** on source-only CI; the **actual positive centered physical integral has not been computed**. No original signed kernel cells added, no historical artifact overwritten, no theorem/RH promotion.

## Previous → Current → Next

**NF404 previous:** Original selected `j*=P_J[1_I m(D)u4]` certified physical norm ~0.702871967915, endpoint ~0.837117780758, and a source-specific zero-extended Fourier tail >2e-5 that stops only the **whole-line primal sufficient surrogate**, not actual supported physical lowband approximation. More decisively, original selected pole `s=sinh(x/2)` and fixed DYADIC
```
a=6677356497477490213/4611686018427387904
```
give exact original-source selected centered squared power
```
E=||P_J(1_I m(D)u4)-a s||_I²≈1.0950024763e-21,
```
with exact full outward interval and small allowed original exterior power `gamma²≈5.1296807868e-26`. A certified actual centered full-action power upper `<=E_lower+gamma²≈1.0950537731e-21` would discharge the **original fourth physical lowband sufficient criterion** under inherited source-specific strong action, but has not yet been obtained.

**NF405 current:** Two independent methods avoid falsely appealing to the earlier failed whole-line surrogate and quantify the one genuinely required source action: (1) extract the original *signed* physical source endpoint principal part from the original analytic high-frequency multiplier tail at the **existing cutoff**; and (2) rewrite the full original arch+seven-prime action as a **compact, cancellation-first physical translation integral** over a bounded interval, eliminating Fourier cutoffs altogether. They are alternative source-equivalent representations of the same (1_I m(D)u4-a s); do not add their errors or interpret them as two independent observations of the complement.

**Next NF406:** Actually enclose the compact supported **positive** norm using original u4 physical source coefficients, splitting the compact translation integrand at support-crossing lines `t=2(B±x)` and source prime shifts `x±log n=±B`. Evaluate the sum of the entire original arch physical kernel, all seven signed prime translations, and dyadic pole subtraction **before squaring**. A pilot without outward enclosures is only provisional. If a certified interval crosses the acceptance cap, report INCONCLUSIVE; if its lower exceeds the cap, STOP only the **particular NF403 strong-residual sufficient method**, never infer a negative Weil vector.

## A. Exact highband feasibility: source-tail horizon

The accepted original NF375 exact tail formula `calc(k,a1,a3,b,A,D,K)` is rerun with unchanged original `a1,a3,b`, original NF374 strict endpoint/curvature caps, `|m(xi)|<=17+log|xi|`, and both Fourier signs. The k=24 output **exactly reproduces** original certified `H24≈4.85120138558906e-14`, source-backed by NF375 Git blob `03c709571046d3f09307614aaded9749f5a15ba1`, source NF374 native SHA256 `a725a6da6bf29ce21b1955df8f4d0b35b87ff8f003d09cdff13581d1b82f7559`, NF401 242D source SHA256 `644337986f62a3f25bb6b2005efc82f517975c84629b32b5ae8d1e5b95614515`.

For a deliberately fixed half-budget `delta=gamma²/2`, if a *future true physical* norm upper for `g_{<=Lambda}=1_I B_<=Lambda[m(D)u4]-a s` is `||g_{<=Lambda}||²<=E_upper+delta`, exact triangle yields `||g||²< E_lower+gamma²` whenever
```
delta + 2 Rcap H_k + H_k² + (E_upper-E_lower) < gamma²
Rcap = 332/10^13 > sqrt(E_upper+delta).
```
All these are exact rational strict tests, not heuristic floating precision. Under the *unmodified*, non-source-cancelled NF375 norm bound, the **FIRST** dyadic cutoff that satisfies this half-budget is `k=39`, `Lambda=2^39=549755813888`. This certifies the inefficiency of **that declared bound-and-half-budget policy**; it is NOT a lower bound on other algorithms' required cutoffs or a proof that the physical integral is large.

Source-exact script `scripts/local_replay/nf405_original_centered_source_tail_horizon.py`; focused CI [Actions #41154901413](https://github.com/monocap-tech/weil-lab/actions/runs/41154901413) **SUCCESS**.

## B. SOURCE-MATCHED endpoint extraction recovers original Lambda=2^24

For the actual unchanged original odd supported `u4=f_(Te4)-w4`, define `B=11/10` and `T_u(xi)=int_{-B}^B u4(x) sin(2*pi*xi*x) dx` (the sine amplitude used in original NF375). Exact integration by parts twice gives
```
T_u(xi)= -u4(B)*cos(2*pi*B*xi)/(pi*xi) + R_u(xi).
```
The original 32 sine source functions vanish at `B` because `2*pi*(5n/11)*(11/10)=pi*n`. Hence **the genuine original signed endpoint**, not an absolute-value proxy, is
```
u4(B)= b*sinh(B/2) -w4(B).
```
NF374 original native signed `w4(B)` and exact original signed pole coefficient `b` now certify `u4(B)≈-1.167986449096830e-11` (both exact outward endpoints preserved). The Fourier leading term uses this **ONE actual signed endpoint**; its original complete seven-prime/digamma symbol `m(xi)` remains untouched.

The NF375 original sine first/cubic moments, source sinh derivative, and NF374 actual original matched w4 endpoint derivative/curvature pay every remainder in the WHOLE frequency interval `|xi|>2^24`:
```
||m R_u||_high <= (|A1| sqrt(J4)+A3 sqrt(J8))/6
                + |b|sqrt(J4)/12
                + (D4+K4)sqrt(J4)/18
                = H_rem.
```
Here `Jq=2 int_Lambda^infty (17+log xi)^2/xi^q dxi` with exact rational outward square-root enclosures and the original same 4096-bit strict NF374 caps. Every original positive/negative real-frequency side is paid and every term is nonnegative; this is **NOT** subtracting two unrelated certified upper bounds. Native original endpoint and source SHA are independently validated by the exact-rational replayer.

Results at the **UNCHANGED** `Lambda=2^24`:
```
original full signed highband H24 ≈ 4.85120138558906e-14
original signed-endpoint-extracted remainder H_rem < 5.038e-17
actual source endpoint u4(B) ≈ -1.167986449096830e-11
original remaining centered-norm cross fee <3.345e-27
half original exterior budget gamma²/2 ≈2.565e-26.
```

Thus the *original* `k=24` cutoff **already meets** the exact half-budget remainder fee `delta+2 Rcap H_rem+H_rem²+(E_upper-E_lower)<gamma²` **provided the endpoint principal-part function is retained and actually evaluated in the future physical centered integrand**. It cannot be thrown away as an error (its Fourier L² may be ~4.7e-14). Define its exact physical value as an L² function on the original support:
```
P_Lambda(x) = -(2*u4(B)/pi)
  * int_{Lambda}^infty m(xi)*cos(2*pi*B*xi)*sin(2*pi*x*xi)/xi dxi.
```
One source-matched sufficient positive physical target is then
```
|| 1_I B_<=Lambda[m(D)u4] + 1_I P_Lambda-a*s ||²
      <= E_upper+gamma²/2.               (UNMEASURED)
```
The signed leading tail and original lowband are **summed before squaring**. Their residual difference from actual original complete centered `g` has norm `<=H_rem`. This is a **rigorous future acceptance contract**, not a completed scalar or a lowband positivity certificate.

Exact source replayer `scripts/local_replay/nf405_original_endpoint_extracted_tail.py`. [Actions #41155027585](https://github.com/monocap-tech/weil-lab/actions/runs/41155027585) **SUCCESS**; source exact result `notes/data/provisional/NF405_original_endpoint_extracted_tail_exact.json`.

## C. An even shorter ORIGINAL object-level route: compact physical digamma action

The unchanged original true REAL signed Fourier multiplier is exactly
```
m(xi) = Re psi(1/4+i*pi*xi) -log(pi)
        -2 sum_(n in {2,3,4,5,7,8,9})
               LambdaMangoldt(n)/sqrt(n) * cos(2*pi*xi*log(n)).
```

The convergent quarter-digamma difference formula is
```
Re psi(1/4+i*pi*xi)-psi(1/4)
  = int_0^infty K(t)*(1-cos(pi*xi*t)) dt,
K(t)=exp(-t/4)/(1-exp(-t)).
```
Under the inherited original source-specific strong realization (log multiplier on supported piecewise smooth u4), Fourier translation gives
```
Arch(D) u4(x) =
  (psi(1/4)-log pi) u4(x)
  -(1/2) int_0^infty K(t)
             [u4(x+t/2)+u4(x-t/2)-2*u4(x)] dt.
```
The original `u4` is zero-extended off `I`. For `x∈I` and `t>4B=22/5`, both shifted values vanish. The remaining scalar tail is EXACT:
```
J_B = int_(4B)^infty K(t) dt
    = 4 sum_(j>=0) exp(-(4j+1)B)/(4j+1)
    = 2[atanh(exp(-B))+atan(exp(-B))].
```

Therefore, for almost every `x∈I`, the ORIGINAL WHOLE SIGNED physical response—not a shadow of a selected trial—is
```
1_I m(D)u4(x) =
  [psi(1/4)-log(pi)+J_B] u4(x)
  - (1/2) int_0^(22/5) K(t)
        [u4(x+t/2)+u4(x-t/2)-2*u4(x)] dt
  - sum_(n=2,3,4,5,7,8,9)
        LambdaMangoldt(n)/sqrt(n)
        [u4(x+log(n))+u4(x-log(n))].
```
The original `psi(1/4)=-EulerGamma-pi/2-3*log 2`. All seven original prime powers, exact signed weights, and the original **arch** are retained. There is **no Fourier cutoff** in this representation. The dyadic original selected pole coefficient `a` is subtracted only at the **end** before the original positive physical square.

The apparent `1/t` singularity at `t=0` is cancelled *symbolically*:
```
u4(x+t/2)+u4(x-t/2)-2*u4(x)
       = (t²/4)u4''(x)+O(t⁴)
```
for any interior x, so the entire kernel integrand is `O(t)` near zero. Across physical support boundaries, split the compact region at `t=2(B±x)`; the log boundary layer can be treated with explicit endpoint majorants. Prime translate support changes at `x±log n=±B`; all genuine original `log n<2B` (verified by finite exact Taylor `exp(11/5)>9`), and the terms for `n=9` have a narrow but nonzero overlap. Source-form identity requires only the finite explicit original u4 graph-domain hypothesis, not closure of the general original domain.

Consequently the **actual unmeasured** NF404 centered norm is a positive integral over the **fixed original physical interval** of the square of this compact source-coupled expression, rather than a 2^39-range frequency quadrature. The old whole-line primal surrogate STOP is irrelevant to this support-preserving formula.

Pure `Fraction` regression `scripts/local_replay/nf405_original_compact_physical_kernel.py` checks the exact series identity for `J_B`, the even difference cancellation coefficients, original seven-prime support geometry, original NF404/NF401 SHA-pins and closure flags. It is an algebraic reproducibility check accompanying the mathematical Fourier/digamma proof above; **it does NOT numerically evaluate `psi`, the t-integral or the final physical norm.** Independent CI result must pass before source-exact custody can be promoted.

## Mathematical STOP and acceptance distinctions

- **ACCEPTED** original NF404 pole-centered selected power and its needed upper threshold, but no actual full original centered power.
- **ACCEPTED** original NF375 source-normalized high tail horizon; naive half-budget route would require `2^39` under the declared policy only.
- **ACCEPTED** original signed-endpoint extraction: explicit leading source highband function + `H_rem<5.038e-17` at cutoff `2^24`; original lowband-plus-leading physical norm remains **UNMEASURED**.
- **ANALYTIC EXACT** original compact translation-kernel identity: 0<t<22/5 and all seven prime-power shifts; compact scalar integral remains **UNCOMPUTED**.
- Original source-specific strong action identification inherited but general original domain audit **OPEN**.
- Exact NF403 fourth lowband/exterior sufficient test **OPEN**; `W-ODD-NEG`, full 242 direction, even/whole Weil and RH all **OPEN**.

**Next bold:** build a cancellation-first rigorous original physical `u4` evaluator, splitting t/x at actual source support seams, and establish an outward positive norm interval for the unmodified `||1_I[m(D)u4-a s]||²`. No further speculative harmonic scan or uniform 2^39 Fourier mesh.
