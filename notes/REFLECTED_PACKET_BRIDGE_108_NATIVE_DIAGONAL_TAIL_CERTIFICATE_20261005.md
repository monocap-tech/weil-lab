# RPB108: native diagonal tails give a sharper finite certificate

Base: research f52dc64cbe9109e1a9c17ab5282873f5e394c5ac.

## Result

The previous enormous cutoff was an artifact of approximating the entire physical inclusion before applying a generic bounded correction. The actual correction is a Fourier multiplier plus an exact rank-two pole form.

Using that structure gives the native tail bound
\[
\delta_T\le
\frac{S_a+(e+1/2)/T}{\log(e+T)},
\qquad
S_a=2\sum_{\log n\le2a}\frac{\Lambda(n)}{\sqrt n}.
\tag{1}
\]
The pole is retained exactly, with no tail error. Approximating only the low-frequency Fourier observation then gives a finite native operator with error
\[
\epsilon_{TN}\le\delta_T+
(10+S_a)\rho_{TN}(2+\rho_{TN}).
\tag{2}
\]
The finite perturbation rank is at most N+3.

There are explicit proved choices with error below 1/4:
a=1/4, T=16, N=191 (rank at most 194);
a=1/2, T=4096, N=98303 (rank at most 98306).

These are certificate sizes, not computed native matrix signs. The latter size is still large. No actual negative vector, endpoint or all-window positivity is asserted.

## Terminology before use

**Native diagonal tail:** the discarded high-frequency part of the actual bounded multiplier correction, estimated directly in the logarithmic form norm.

**Exact-pole retention:** leaving the actual rank-two pole form unchanged rather than approximating its physical inputs.

**Low-frequency certificate map:** a finite approximation of Fourier observation only on [-T,T].

These are additive refinements of the finite form certificate. Its same-vector source custody and zero-band limitations are unchanged.

## Sharpened archimedean correction

The previous Euler sum-integral proof bounded its error by
\[
\int_0^\infty\frac{du}{|u+z|^2}.
\]
For z=1/4+i pi xi and xi!=0 this is
\[
\frac1{\pi|\xi|}
\left(\frac\pi2-
\arctan\frac1{4\pi|\xi|}\right)
\le\frac1{2|\xi|}.
\]
Hence
\[
|\psi(z)-\log z|\le\frac1{2|\xi|}.
\]
With t=|xi| and q=1/(4pi), the logarithmic comparison is nonnegative:
\[
0\le\log(e+t)-\log\sqrt{q^2+t^2}
\le\log(1+e/t)\le e/t.
\]
Thus the actual multiplier correction
\[
d(\xi)=\Re\psi(1/4+i\pi\xi)-\log\pi-w(\xi)
\]
satisfies
\[
|d(\xi)|\le\min\{10,(e+1/2)/|\xi|\}.
\tag{3}
\]
The constant bound includes xi=0. No digamma derivative or unproved asymptotic expansion is needed.

## Diagonal multiplier tail on the actual carrier

The prime multiplier is
\[
p_a(\xi)=2\sum_{\log n\le2a}
\frac{\Lambda(n)}{\sqrt n}
\cos(2\pi\xi\log n),
\qquad |p_a|\le S_a.
\]
The actual native form on H=D_a is
\[
Q_a(f,g)=\langle f,g\rangle_H+
\int(d-p_a)\overline{\widehat f}\widehat g
+Q_{\rm pole}(f,g).
\tag{4}
\]
The pole form is exactly the existing cross-moment form.

On |xi|>T, weighted Cauchy-Schwarz gives a mixed-form operator bound
\[
\sup_{|\xi|>T}\frac{|d(\xi)-p_a(\xi)|}{w(\xi)}
\le\frac{S_a+(e+1/2)/T}{\log(e+T)}.
\]
This proves (1). Both slots share the same diagonal frequency cutoff; no cross-frequency inclusion-error estimate is necessary.

If 2a<log2, no native prime term occurs, so the tail is bounded by
(e+1/2)/(T log(e+T)), rather than a purely logarithmic bound.

## Finite low-frequency part, with the pole exact

Let L_T h=1_[-T,T] Fourier(h), valued in L2([-T,T]); its norm from H is at most one. Let B_TN be the Fourier Taylor map from the preceding note, restricted to that same interval. Its error now contains only the rectangle remainder:
\[
\|L_T-B_{TN}\|\le\rho_{TN}:=
\sqrt{4aT}e^{2\pi aT}
\frac{(2\pi aT)^{N+1}}{(N+1)!}.
\tag{5}
\]
No omitted high-frequency norm of physical h enters (5).

Put b_a=10+S_a. The exact low correction is L_T* M_(d-p_a) L_T, with multiplier norm at most b_a. Replace it by B_TN* M_(d-p_a) B_TN, and keep the logarithmic pole operator R_pole unchanged. Define
\[
\widetilde A_{TN}
=I+B_{TN}^*M_{d-p_a}B_{TN}+R_{\rm pole}.
\tag{6}
\]
Difference expansion bounds the low error by b_a rho(2+rho). Together with (1), this proves (2).

The finite perturbation lives in the span of the N+1 logarithmic moment representers and the two logarithmic pole-moment representers. It has rank at most N+3 and equals I on the orthogonal complement of that finite span.

Therefore the preceding whole-domain sign certificates and exact positive-high-complement Schur reduction apply verbatim with the new error. No background positivity is imported.

Finite Gram and native entries still need rigorous evaluation. The rank bound does not automatically make monomial coordinates well-conditioned or implement the matrix.

## Sufficient low-frequency degree

Write L=2pi aT and k=N+1. For a chosen rho0>0, the conditions
\[
k\ge2eL,\qquad
k\ge\frac{L+\log(\sqrt{4aT}/\rho_0)}{\log2},
\quad k\ge1
\tag{7}
\]
give rho_TN<=rho0, by k!>=(k/e)^k and (eL/k)^k<=2^(-k).

First choose T so that the explicit delta_T is at most half the desired error. Then choose rho0<=min{1,epsilon/(6b_a)}, and k by (7). Equation (2) gives the desired native error. All steps are explicit; the remaining task is the finite native arithmetic and its sign.

## Two rationally justified sufficient sizes

Use pi<4, e<3, log2>=2/3 and e+1/2<7/2. The log2 lower bound follows directly from integrating the geometric series for log((1+t)/(1-t)) at t=1/3.

### Prime-free window a=1/4

Here 2a=1/2<log2, so S_a=0. Choose T=16. Then
\[
\delta_T\le\frac{7/2}{16\log16}
\le\frac{21}{256}<\frac18.
\]
Take rho0=1/240 and k=192, so N=191. Since L=8pi<32 and e<3, k>=2eL. Also sqrt(4aT)/rho0=960 and log960<10 (because e>2), so the second bound in (7) is below 63. Thus rho<=1/240, and
\[
10\rho(2+\rho)\le30\rho\le\frac18.
\]
The total error is strictly below 1/4, with rank at most 194.

This example fixes an approximation size only; it does not certify the sign at a=1/4.

### Window a=1/2

Only n=2 occurs in the prime-power cutoff log n<=1, because 2<e<3. Hence S_a=sqrt(2) log2. Choose T=4096=2^12. Using sqrt(2)<17/12,
\[
\delta_T\le
\frac{\sqrt2\log2}{12\log2}
+\frac{7/2}{4096\cdot12\log2}
\le\frac{17}{144}+\frac7{65536}<\frac18.
\]
Since b_a<12, take rho0=1/288. Set k=98304 and N=98303. Now L=4096pi<16384, so k>=2eL. Also
sqrt(4aT)/rho0<128*288<65536, whose logarithm is below 16. Thus the second bound in (7) is below 24600. We obtain
\[
b_a\rho(2+\rho)\le36\rho\le\frac18.
\]
Again the total error is strictly below 1/4, with rank at most 98306.

This is far smaller than the generic construction's enormous sufficient cutoff, but a dense matrix of this size is not automatically practical. No timing, memory or numerical conditioning claim is made.

## Cursor consequence and validation

The generic cost obstruction is not an intrinsic obstruction: exact native diagonal structure already improves it, especially below the first prime threshold. The next computational step would still require stable finite coordinates and rigorous entry enclosures, not just the rank bound.

No finite sign, endpoint exclusion or Gaussian upper estimate follows solely from this approximation improvement. FULL TRANSPORT CLOSED remains open.

Analytic proof using the actual Euler multiplier, finite prime cutoff, exact pole form and elementary remainder bounds. No new external input, Lean source/workflow change or CI claim. Certified code remains cb92c1b4dfca298cbc79d5b7d25598ea370236bf, Actions run 37236113125/job 111535430775.

At f52dc64, a native diagonal-tail certificate replaces the impractical generic physical-inclusion approximation. The Euler sum-integral bound sharpens to |psi(1/4+i pi xi)-log(1/4+i pi xi)|<=1/(2|xi|), giving actual archimedean/log correction |d(xi)|<=min(10,(e+1/2)/|xi|). The finite prime multiplier has amplitude S_a=2 sum_(log n<=2a) Lambda(n)/sqrt(n). Direct diagonal truncation on the logarithmic carrier has error delta_T<=(S_a+(e+1/2)/T)/log(e+T). The actual pole rank-two form is retained exactly. Taylor approximation of only the low-frequency Fourier observation has error rho_TN, giving total native error delta_T+(10+S_a)rho_TN(2+rho_TN), with finite rank at most N+3. Previous sign and exact Schur certificates apply with this error. Explicit rational sufficient choices at error 1/4 are a=1/4,T=16,N=191 (rank<=194) and a=1/2,T=4096,N=98303 (rank<=98306), replacing the prior enormous sufficient cutoff. These are proved sizes, not evaluated Gram/native matrices or actual sign claims; the second size is still computationally large. Physical witness custody stays on the canonical logarithmic domain. No endpoint/RH conclusion or new Lean/CI result; FULL TRANSPORT CLOSED remains open.
