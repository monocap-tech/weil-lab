# NF407 — Original endpoint-log and seven-prime jumps: exact correlated principal and cancellation gate

**2026-10-30 PT. Canonical original `W-ODD-NEG` remains OPEN.** Original fourth physical source `u4`, original full signed seven-prime/archimedean multiplier, original support `I=[-B,B]`, `B=11/10`, original J242 and fixed original NF404 pole shear are UNCHANGED. No new signed kernel cells, no 242D source family expansion, no original general-domain promotion or RH closure.

## Previous cursor / current circle / next bold

**Previous NF406:** Accepted the true original 4096-bit physical source `u4=fTe4-(F-JX)(I+Y0)Te4` at eight rational support points; actual positive source can be O(1), e.g. `u4(B/2)≈3.66437836`, even though `u4(B)≈-1.16798644909683e-11`. Original NF406 endpoint-log model `q(x)=(u4(B)/2)sgn(x)log[B/(B-|x|)]` has accepted exact `||q||²=B u4(B)²≈1.500611579801204e-22`. NF406 exact rational logs partition the seven physical prime-shift supports into 16 open cells (17 knots). The complete centered physical scalar `||g||²` was not integrated.

**Current NF407:** Observe that the original physical **seven prime translations are discontinuous** at the 14 source-specific seams. Subtract their unique signed jump amplitudes as an explicit odd step function `r`, in addition to the original archimedean logarithm `q`. These two original source-determined functions `p=q+r` have an **exactly computable correlated L² norm**, while the remaining original function `z=g-p` is continuous inside I (and bounded at the endpoints) after support-boundary cancellation. This changes the actual physical quadrature from a log+14-jump source to a regularized source with all original signed discontinuities analytically accounted for. It is an actual original-object calculation, not a smooth numerical shadow and not the measured full `g`.

**Next NF408:** Evaluate the *remaining continuous* signed original physical `z(x)` on the NF406 16 original prime-support cells with correct source-correlated coefficients and guaranteed interval error. The remaining `||z||²+2<z,p>` is the only unmeasured scalar combination; its signed cross MUST be retained. No more new candidate sources or unaccounted Fourier quadrature.

## 1. The exact seven original prime jumps

The original physical prime action is

```
P u4(x) = - sum_{n in N7} c_n [u4(x+log n)+u4(x-log n)],
N7={2,3,4,5,7,8,9},
c_n=Lambda(n)/sqrt(n) >0.
```

Here `Lambda(n)` is the exact von Mangoldt coefficient: `log 2` for 2,4,8; `log 3` for 3,9; `log 5` for 5 and `log 7` for 7. The actual original source `u4` is odd and supported on `[-B,B]`, has continuous one-sided endpoints `u4(B)=v<0` and `u4(-B)=-v`; its zero extension has a jump at each endpoint. For `h_n=log n`, `0<h_n<2B`, put `x_n=|B-h_n|` in `(0,B)`. The translated signed physical term has exactly two **interior** jump locations `±x_n`, each with orientation-`x)-increasing jump `v c_n`. This holds for both `h_n<B` (right translation EXITS at `B-h_n`) and `h_n>B` (left translation ENTERS from `-B` at `h_n-B`). The positive/negative physical supports are not disjoint, and their genuine sign matters.

Subtract the step function

```
r(x) = v*sgn(x)*sum_{n in N7} c_n * 1_{|x|>x_n}.
```

Each constituent odd step has exactly the correct two jumps. The original `A u4` arch action is continuous inside I, with only the previously isolated boundary logarithms, so after additionally subtracting q, the function

```
z(x) = 1_I[m(D)u4(x)-a sinh(x/2)] - q(x)-r(x)
```

is an **interior-continuous, endpoint-bounded** original supported physical function. Prime shifts still contribute within each of the 16 original cells; they are not deleted, only their known jumps are subtracted, with all signs preserved. The underlying original physical object remains `g=z+q+r`.

## 2. Exact physical power and signed q-r correlation

For `p=q+r`, original `v`, original support B, and `d_n=B-x_n`, the whole original positive squared model norm follows from finite sums plus elementary primitives:

```
||q||² = B*v².
||r||² = 2*v² * sum_{n,m in N7} c_n*c_m * (B-max(x_n,x_m)).
<q,r> = v² * sum_{n in N7} c_n*d_n * (1+log(B/d_n)).
||p||² = ||q||²+||r||²+2<q,r>.
```

The log/q-r identity is the exact physical primitive `int_(x_n)^B log[B/(B-x)]dx=d_n[1+log(B/d_n)]`, not sampled quadrature. The complete `n=9` narrow overlap and almost-at-zero `n=3` step are INCLUDED. Source exact Fraction arithmetic uses NF406 128-term rational arctanh brackets for each original `log n`, outward integer-square-root enclosures for `sqrt n`, source-native `v` outward endpoints, and a 64-term scaled arctanh with remainder bound for the nested real `log(B/d_n)`. Outward decimal compaction is by exact floor/ceil only and the independent reader verifies `||p||²` interval = the exact positive-sum interval of its three components.

Source-certified approximate values (actual complete outward rational endpoints in the durable JSON):
```
||q||²     ≈ 1.500611579801204e-22
||r||²     ≈ 1.208713343019971e-21
<q,r>      ≈ 3.838162466382499e-22  (positive for the TRUE signed original v)
||q+r||²   ≈ 2.126406994276591e-21.
```

Exact rational source replay `scripts/local_replay/nf407_original_prime_jump_log_power_exact.py`, plus an independent standalone conditional-gate replayer; [Actions #41168113594](https://github.com/monocap-tech/weil-lab/actions/runs/41168113594) **SUCCESS**. Earlier workflow attempts failed successively on parser/rounding equality checks or a Git branch synchronization race; they are **not accepted runs** and must not be relabeled as such. The accepted source certificate persists in `notes/data/provisional/NF407_original_prime_jump_log_power_exact.json`.

## 3. Exact necessary cancellation IF the unchanged NF404 sufficient cap holds

The unchanged original NF404 pole-centered full physical scalar **sufficient** acceptance is:

```
||g||² <= C = E_selected_centered_lower+(sigma-H)^2
             ≈1.0950537731e-21  (still UNMEASURED).
```

Already `||p||²≈2.126406994e-21>C`. This **does not imply failure**, because `z` is unknown and the signed cross can be strongly negative. The exact source-bounded triangle and Pythagorean identity give the following strictly conditional requirements:

```
if ||g||²<=C:
   ||p||>4.61e-11, ||g||<3.31e-11,
   ||z||=||g-p||>1.30e-11,
   2<z,p> = ||g||²-||z||²-||p||² <= C-||p||²,
   <z,p> < -5.15e-22.
```

Both last conditions are checked using literal root-free exact `Fraction` inequalities on the original source certificates, never inferred from a measured `z`. This is a **real quantified necessary cancellation** for the fourth-source sufficient strong method: the continuous regularized original component cannot be ignored, estimated by positive-only triangle at this scale, or replaced by q+r. It must carry a negative physical correlation with the complete source singular model if the NF404 acceptance is to succeed.

## 4. True original 4096-bit physical coefficient custody

Original NF406 actual `u4` point profile [Actions #41156050309](https://github.com/monocap-tech/weil-lab/actions/runs/41156050309) **SUCCESS**; 242D original D/H/N SHA reassembled and original exact NF369 4x4 massive dyadic shear retained, and true source endpoint overlaps NF374/NF405 4096-bit input. Its rational-point source samples show `u4` O(1) in the interior; do not extrapolate endpoint smallness into full source action smallness. A separate NF407 original 4096-bit coefficient exporter reconstructs original 242 selected raw plus 4 original critical probe coefficients and their 8 correlated source samples. Its CI run status determines whether those coefficients may be promoted; it does **NOT** compute the compact physical multiplier action. Raw huge original shear/source coefficients cannot be converted to float or independently rounded before summing the entire source.

The numerical original `z` integrand still needs cancellation-first evaluation of the complete NF405 compact t-integral and all original seven prime translates, with the original q and r subtracted. A successful native coefficient export alone is **not** that numerical quadrature.

## Custody and STOP

- **Accepted** original q,r exact source power and signed cross; original 16-cell prime support partition; original NF406 4096-bit u4 rational point source.
- **Accepted conditional** necessary `||z||>1.30e-11` and `<z,p><-5.15e-22` IF the original NF404 target C is ever met.
- **Unmeasured** continuous original `||z||²`, signed `<z,p>`, original complete positive `||g||²`, fourth physical lowband/complement upper, general source-to-operator domain, infinite exterior inverse, W-ODD-NEG and RH.
- No fresh signed kernel cells, no historical source byte changes, no main merge; PR remains draft research.

**NF407 stopping point:** regularized physical scalar is `||g||²=||p||²+||z||²+2<z,p>` with explicit `||p||²` known. Do not promote or infer a new lowband sign until a true source-correlated interval bound for the *remaining continuous* `z` and its signed cross is available. Next bold NF408 is THIS actual integral, not another shadow.
