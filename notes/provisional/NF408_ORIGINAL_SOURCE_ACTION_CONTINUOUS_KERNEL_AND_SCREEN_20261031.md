# NF408 — Original source action: exact coefficient error and a cancellation-first continuous physical kernel

**2026-10-31 PT.** Canonical original `W-ODD-NEG` OPEN. This pass uses the same original NF370 fourth physical source, real full seven-prime signed digamma multiplier, J242, original NF404 dyadic pole centering `a=6677356497477490213/4611686018427387904`, original support I=[-11/10,11/10], and NF407 exact `g=z+q+r`. No new signed kernel sources/cells, no general operator-domain closure, no theorem or RH claim.

## Previous → Current → Next

**Previous NF407:** Certifies the exact physical log model `q` and all seven true signed original prime-discontinuity steps `r` plus their entire source-correlated original physical power `||q+r||²≈2.126406994276591e-21`. Original continuous remainder `z=g-q-r` remains unmeasured, even though full original centered power `||g||²` must meet the **conditional** upper cap `C≈1.0950537731e-21`. Original NF407 4096-bit 242+4 source coefficients now persist, and original NF406 eight physical sample checks are successful.

**Current NF408:** For the first time, compute the **original full signed physical action at a true interior point**, not a matched signed moment or Fourier tail. Separate source representation uncertainty from **actual physical quadrature uncertainty**, and derive a mathematically exact, source-preserving **cancellation-first physical formula for z itself**, with no endpoint log and no prime jumps left in the numerical integrands. A source-corrected original 16-cell positive L2 pilot uses the exact principal `||q+r||²` plus signed approximate `||z||²+2<z,q+r>`; only a rigorous quadrature enclosure can certify the result.

**Next NF409:** Turn source-corrected continuous `z` physical-cell quadrature into independently auditable interval enclosures, including the near-support endpoint `(u4(x)-u4(B))log(B/(B-x))`, corner transitions, and all original prime translations, and evaluate source-coupled `||z||²+2<z,p>`. No point pilot or noncertified 16-cell mesh can substitute for the inequality.

## A. Source-native 4096-bit uncertainty is already quantitatively negligible

NF407 original raw selected and critical physical coefficient carrier had raw coefficient magnitudes as large as ~1e142. The original 4096-bit native **Arb radius** inputs were NOT previously paid at the level of the complete physical signed multiplier action. NF408 independently computes, in **pure exact Fraction**, for the original dyadic native midpoints `u_mid`:

```
S = ||u4-u_mid||_L∞(I)               (strict source upper)
D = ||u4'-u_mid'||_L∞(I)             (strict source upper).
```

Each original selected generator `x^k sin/cos(2*pi*c*x)` is paid by `rad_i B^k` and `rad_i[k B^(k-1)+7|c|B^k]` (since `2pi<7`), the original odd pole `sinh(x/2)` by `rad_s` in both, and all **four original critical sine/pole probes** by their exact rational coefficients and original shared dyadic source-frame radii. No cancellations are assumed in these ERROR bounds. The native **midpoint values** themselves must still be summed correlated and never converted to float.

The complete original real signed `m` has `|m(xi)|<800` for |xi|<=1, proved from the exact quarter-digamma integral, `sum_{j>=0}(j+1/4)^-3<=72`, `pi²<10`, `|psi(1/4)-ln pi|<10`, and all seven prime powers `2 sum |Lambda(n)|/sqrt(n)<42`. The inherited accepted complete **signed** original highband estimate `|m(xi)|<=17+log|xi|` holds for |xi|>=1. Fourier integration by parts for the true supported C1 coefficient error, plus Plancherel and exact
```
int_1^infty (17+log t)^2/t² dt =325
```
give the source-native whole multiplier L2 error

```
||1_I m(D)(u4-u_mid)||_L2(I)
    < 3000*(S+D) <1e-745.
```

The reported exact-rational native source radii actually imply an error around 1e-759. This is a true **accepted original full signed-multiplier input-radius error** (not a physical quadrature or full norm bound). [Actions #41218596474](https://github.com/monocap-tech/weil-lab/actions/runs/41218596474) **SUCCESS**. Script `scripts/local_replay/nf408_original_source_midpoint_action_error_exact.py`; persisted source `notes/data/provisional/NF408_original_source_midpoint_action_error_exact.json`.

## B. True original physical-action numeric pilot at x=B/2

`scripts/local_replay/nf408_original_compact_physical_action_pilot.py` recovers all 242 original raw selected and 4 original critical coefficient midpoints as 205-220 decimal digit numbers, preserves the **correct plus sign** on original raw selected `+JXM` in `u4=F(T-M)+JXM`, groups analytic polynomials on their genuine frequencies, and evaluates the TRUE original source `u4(x)` **before** the original signed multiplier. The arch real quarter-digamma physical kernel uses the exact compact physical difference formula, splits the t-integral at both genuine original support crossings `t1=2(B-x)`, `t2=2(B+x)`, retains all seven signed prime shifts, then subtracts original fixed dyadic pole. No original rank-one pole has been incorrectly omitted from the signed Weil-to-multiplier projection; the source-specific strong transfer remains the inherited assumption.

At x=11/20 (B/2), the original native source control `u4(x)≈3.664378361751959864...` agrees with source-native NF406 data. Distinct Gauss meshes (n14 with max t step .05 at 205 decimal digits; n20 with step .025 at 220 digits) yield:

```
Original arch action Au4(x)          ≈ -1.83625526628157244
Original seven prime action P u4(x) ≈ +2.23947122555252626
Original complete m(D)u4(x)         ≈ +0.403215959270953825
Original centered g(x)              ≈ -9.04577689395736e-12
Original endpoint q(x)              ≈ -4.04793257061845e-12
Original all seven jump r(x)        ≈ -2.55876547026586e-11
Original continuous z(x)=g-q-r      ≈ +2.05898103793197e-11.
```

The two approximations for original g,z differ by ~4.34258608359372e-16 absolute, and do show **numerical signed cancellation** of the expected orientation at this one point. But: the pilot uses approximate double-derived Gauss nodes/weights, excludes a very short t interval without yet a valid norm bound, and does not propagate all arithmetic rounding. The `~4.34e-16` difference is a convergence diagnostic, **NOT a rigorous error bound**. This point alone does not determine `||g||²`, the original lowband upper, or Weil/RH. [Actions #41218405130](https://github.com/monocap-tech/weil-lab/actions/runs/41218405130) **SUCCESS**; initial source pilot runs #41218256737 and #41218324582 failed on a numpy float repr parser and remain historical failures.

## C. New EXACT continuous-source physical operator formula — no endpoint subtraction after quadrature

The previous NF405 compact physical arch kernel is
```
A u(x) =c0*u(x) + ∫_0^(4B) K(t)[u(x)-(u(x+t/2)+u(x-t/2))/2]dt,
c0=psi(1/4)-ln pi,
K(t)=e^(-t/4)/(1-e^(-t)).
```
The full supported u4 is extended by zero. For x>=0 put
```
d=B-x,   t1=2d,   t2=2(B+x),
J(t)=∫_t^infty K(s)ds
    =2[atanh(e^(-t/4))+atan(e^(-t/4))],
L=ln(B/d).
```
Because both translated copies leave support at t>t2, and the right translation alone leaves at t>t1, **the exact original arch action** can be retyped into two finite, source-correlated integrals and an explicit tail constant:

```
A u(x) = [c0 + (J(t1)+J(t2))/2]*u(x)
       + I0(x)+I1(x),
I0(x)=∫_0^t1 K(t) [u(x)-(u(x+t/2)+u(x-t/2))/2]dt,
I1(x)=1/2∫_t1^t2 K(t) [u(x)-u(x-t/2)]dt.
```

Subtract the **actual** NF406 q(x)=(v/2)L, v=u4(B), and retype with `Phi(d)=J(2d)-L` to obtain the desired original bounded arch part:

```
A u4(x)-q(x)
 = [c0 + (J(t2)+Phi(d))/2]*u4(x)
   + [L/2]*(u4(x)-v) +I0(x)+I1(x).
```

Crucially, **evaluate Phi without subtracting two divergent logarithms**:

```
Phi(d)=ln[(d/B)*coth(d/4)] +2*atan(e^(-d/2)),
lim_(d->0+) Phi(d)=ln(4/B)+pi/2.
```

Thus `Phi` is endpoint bounded, and `(u4(x)-v)L→0` as x→B. Also `I0` shrinks smoothly and `I1` remains bounded because `u4(B)-u4(B-t/2)=O(t)` makes K(t)~1/t integrable at t=0. THIS is a legitimate source-preserving **continuous physical integrand**, not a postprocessed plot of a shadow. The earlier isolated log is paid exactly, and no enormous log cancellation is attempted numerically.

## D. New exact prime-jump cancellation directly inside each translated term

For each genuine original prime power n=2,3,4,5,7,8,9, write `h=ln n`, `c_n=Lambda(n)/sqrt(n)`, `x_n=|B-h|`. For x in (0,B), the original `-c_n[u4(x+h)+u4(x-h)]` and original known signed step `r_n(x)=v*c_n 1_(x>x_n)` combine EXACTLY as:

```
if h<B and 0<x<x_n:
      P_n u4 -r_n = -c_n[u4(x+h)+u4(x-h)].
if h>B and 0<x<x_n:
      P_n u4 -r_n = 0.
for either h<B or h>B and x>x_n:
      P_n u4 -r_n = -c_n[u4(x-h)+u4(B)].
```

At h<B, the left seam limit is `-c_n[v+u4(B-2h)]`, exactly matching the right expression. At h>B, the post-seam expression begins at `-c_n[u4(-B)+v]=0`, exactly matching the zero pre-seam branch. **All seven source-original translated prime jumps are therefore removed algebraically before numerical integration, with all seven continuous remainders retained.**

Together the final true original `z(x)=[A u4(x)-q(x)] +Σ_n[P_n u4(x)-r_n(x)]-a*sinh(x/2)` is evaluated directly and can be reflected oddly to x<0. This formula has exactly the same source, signed symbol, original center, and support as NF407 g=z+q+r, but is now a continuous source action suitable for interval quadrature. Pure exact-Fraction branch and algebra verification `scripts/local_replay/nf408_original_continuous_action_exact.py`, source CI [Actions #41219140490](https://github.com/monocap-tech/weil-lab/actions/runs/41219140490) **check run status before promoting**.

## E. Whole original 16-cell numerical L2 screen and standing

The source-matched original physical x-domain has exactly eight positive open cells and their eight odd reflections. NF408 has launched a *separately typed exploratory* 16-cell pilot. It uses true original 242+4 source coefficient midpoints, complete physical arch+seven-prime source action, and the known exact source principal `||p||²`, with

```
||g||² = ||p||² +||z||²+2<z,p>,
p=q+r.
```

Two outer Gauss resolutions (2 and 4 nodes per positive support cell) are computed with 205-digit source coefficients, 14-point piecewise inner t quadrature, and the actual rational-attested original 16-cell seam order. Critically, even if both approximate full norms lie on one side of the NF404 upper threshold, neither is a certificate: the x/nested-t quadrature errors, small-t near-boundary layer, and actual Gauss nodes/weights have no verified interval bound. The full scalar must be marked **UNCOMPUTED AS A RIGOROUS UPPER** until these are supplied. Workflow [Actions #41218841422](https://github.com/monocap-tech/weil-lab/actions/runs/41218841422) status must be checked before any pilot numbers are quoted.

## Mathematical stop conditions

Source **ACCEPTED**: native original physical 242+4 coeff radii lead to complete signed multiplier L2 source-input error <1e-745 (exact).
Source **PROVISIONAL NUMERICAL**: genuine original complete multiplier physical action sampled at x=B/2, two-resolution discrepancy ~4.34e-16, no rigorous pointwise L2 certificate.
Source **ANALYTIC EXACT**: stable continuous original arch source after endpoint log subtract-before-quadrature and continuous original seven-prime translations after signed jumps subtract-before-quadrature. Formal exact regression is not a numerical norm proof.
Original **FULL CENTERED NORM UPPER STILL OPEN**: need certified x/t integrals and signed q+r cross, original lowband Q_J upper, original general operator domain, full exterior inverse, W-ODD-NEG, even/whole Weil and RH.
**Next bold NF409:** implement original continuous z(x) certified interval quadrature on the original eight positive physical cells using exact Phi(d), stable signed prime branches, and pay all source/inner/outer errors. Compare full original norm to NF404 true source-centered acceptance cap; do not use an unsigned triangle bound to avoid the known necessary negative cross.
