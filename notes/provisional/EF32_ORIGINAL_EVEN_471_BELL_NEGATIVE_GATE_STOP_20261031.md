# EF32 — Certified original even first-source diagonal and 471-bell sufficient-negative-gate METHOD STOP

**2026-10-31.** Canonical `W-EVEN-FORM` OPEN. Parent [EF31 draft PR #426](https://github.com/monocap-tech/weil-lab/pull/426), exact native last-head [Actions #41237653010](https://github.com/monocap-tech/weil-lab/actions/runs/41237653010) SUCCESS; EF30 original sampled moment rank470/nullity1 [Actions #41236609475](https://github.com/monocap-tech/weil-lab/actions/runs/41236609475) SUCCESS. This pass retains the TRUE SI10 original 469 even exceptional rows, original positive even pole, complete original seven prime-power and archimedean signed form, and the original EF28 471 disjoint C5 even bells with physical Gram d I. Odd `W-ODD-NEG` paused/OPEN; whole Weil and RH OPEN.

## NEW full original first-source diagonal, with analytic scalar tail

Take the unchanged original first protected source

`e(x)=1_[-B,B](x) cos(omega x)`, `B=11/10`, `omega=2*pi*(37/64)`.

The genuine pole-free original diagonal is `A=q0(e,e)=A_prime+A_arch`; genuine even sector attaches `2*u^2` with `u=<cosh(x/2),e>`. Original EF29 already supplied a 340-digit outward interval `A_prime≈0.30039538744`, including ALL seven prime powers on the diagonal, **including n8 and n9** even though their EF28 mixed bell channels vanish. EF32 independently computes and certifies the previously uncomputed **entire original digamma first-source diagonal** `A_arch`, not an arch norm upper.

Use the exact original quarter-digamma identity under the physical Fourier convention:

`a_arch(xi)=-gamma-ln(pi)+sum_(n>=0)[1/(n+1) -(n+1/4)/((n+1/4)^2+(pi*xi)^2)]`.

For `lambda_n=2n+1/2`, the inverse physical Fourier transform of the rational summand is `exp(-lambda_n |x|)`. Define the original compact-source autocorrelation, for `0<=t<=2B`:

`C(t)=(S0-t/2)cos(omega*t) - cos(2*omega*B)sin(omega*t)/(2*omega)`, with `S0=C(0)=||e||^2=B+sin(2*omega*B)/(2*omega)`.

Let `F_n=2 int_0^(2B) e^(-lambda_n*t) C(t)dt`; the script uses the exact closed rational/exponential/sine/cosine endpoint formula (via `J=(1-e^(-(lambda-i omega)2B))/(lambda-i omega)` and `K=(1-e^(-(lambda-i omega)2B)(1+2B(lambda-i omega)))/(lambda-i omega)^2`), with SI06/EF24 native exact outward 10^340 integer interval arithmetic. Thus

`A_arch=(-gamma-ln(pi))*S0+sum_(n>=0)[S0/(n+1)-F_n]`.

The Euler constant uses the rigorous integer-harmonic bounds `H_M-ln M-1/(2M) < gamma < H_M-ln M-1/(2(M+1))` with M=1024 and original source log2; ln(pi) uses the original rational SI06 logarithm interval and original PI enclosure. For `lambda_n*2B>=250`, the exponential endpoint is bounded in `[0,10^-100]` using an exact positive finite Taylor lower certificate `exp(250)>10^100`, *not* dropped without payment.

**Complete infinite-series tail:** the original C(t) extended by zero for t>2B satisfies C(2B)=0 and `|C'(t)|<=L=S0*omega+1`: specifically original S0>B is source-checked, so `0<=S0-t/2<=S0` for 0<=t<=2B. Then

`|F_n-S0/(n+1/4)| <= L/(2(n+1/4)^2)`

and

`|S0/(n+1)-F_n| <= (3*S0/4+L/2)/(n+1/4)^2`.

For n>=N=256, the entire omitted tail is strictly less than `(3*S0/4+L/2)/(N-1)<1/40`. Every bound is outward rational and includes actual original source cutoff, original true digamma, and high-frequency content.

## Native original certificate — accepted scoped CI

**[Actions #41238414693](https://github.com/monocap-tech/weil-lab/actions/runs/41238414693) SUCCESS**, same true source strengthened original autocorrelation-bound assertion; artifact ID `13056218000`, SHA256 `1a0e8363a04ae9e0f099618448ea2a8dfe4f098dad6585114044b406ce619274`, 403486-byte ZIP, retains the **all-471 native EF29 source replay** and EF32 scalar rational result.

Outward values (decimal display rounded; authoritative integers are in the artifact):

| Original quantity | Certified enclosure / upper |
| --- | ---: |
| Full original digamma diagonal `A_arch` | `[-0.76712234087,-0.73831578350]` |
| Original seven-prime diagonal `A_prime` | approximately `+0.30039538744`, outward |
| True even-pole charge `2u²` | approximately `+0.49772423011`, outward |
| **Original complete even first-source diagonal `A_even`** | **`[+0.030997276682,+0.059803834050]`** |
| Full original EF29 reduced signed vector max absolute coordinate | `<0.000115902` |
| Full original EF29 reduced signed vector squared Euclidean norm | **`<3.174615×10^-6`** |
| Prior EF28 sufficient-negativity threshold lower `34*d*A_even`, `d=231/8388608` | **`>2.9021812×10^-5`** |

This gives TWO distinct statements on the **true original source**:

1. `q_even(e,e)=A_even>0.030997`: an actual strictly positive **one-dimensional direction**, under the inherited source/domain attachment. This is NOT even-sector positivity.
2. For the original 471-dimensional EF28 bell span constrained to be exactly source- and pole-neutral by the true 470 rows, its unique normalized direction w (EF30/EF31) obeys `delta²=|gtilde*w|²/||w||² <=||gtilde||² <3.174615e-6 < 34*d*A_even`. The **existing EF28/EF31 sufficient negative-even criterion** `delta²>34*d*A_even` is therefore provably **IMPOSSIBLE** with its fixed `E<=34*d*||w||²` upper-energy budget, even with the mathematically exact kernel vector and zero projection numerical error. This is a rigorous *method-specific STOP*, not an observed floating loss of precision.

Crucially, failure of a SUFFICIENT negative witness condition is NOT a positive-semidefiniteness proof, nor does it exclude a genuine negative even vector even in this restricted span. The actual true energy of the kernel direction `q0(f,f)` may be much smaller than `34*d*||w||²`; the true normalized correction `delta²/(q0(f,f)/(d||w||²)*d)` and full infinite-complement Schur response remain unmeasured. We did **not** compute actual `delta` or a certified numerical kernel orientation, and we do not claim this upper-energy stop is a mathematical obstruction to all detector choices.

## Decision / next research junction

EF31's exact Chebyshev kernel direction remains a valid structural certificate, but **computing its numerically delicate coefficients solely to retry the unchanged 34d sufficient-negative gate has zero mathematical value**. EF32 avoids the conditioning trap by an exact, correlation-preserving full original `||gtilde||` upper and an independently certified original first-source diagonal.

**EF33 acceptance preflight:** attack the TRUE even-sector sign with (a) an *actual kernel-specific* original cofinite energy evaluation/strict upper sufficient to reduce the normalized scalar denominator below the new source threshold, or (b) a different original-source/coupled-positive Schur strategy, preserving the entire 469-dimensional finite source, genuine pole and infinite remainder. Since `delta²<=3.175e-6` and `A_even>0.030997`, a negative witness via this kernel can only be decided if its TRUE energy satisfies a much sharper quantitative inequality than the inherited 34d bound; no certificate may replace the true denominator by the certified lower floor to infer negativity. If the fixed detector is ruled out, record its correct method-class scope and pivot. Do not reopen paused odd automatically.

**Standing:** native source verified scalar original digamma diagonal and all-471 signed vector upper; exact algebra/analytic tails documented, pending independent physical form/core and digamma audit. Original corrected complete 469D even Schur, odd and whole Weil, RH remain OPEN. GitHub-first additive custody, no `main` merge.
