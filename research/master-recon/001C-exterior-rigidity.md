# MASTER-RECON-001C — Exterior arithmetic rigidity

2026-11-24. INVESTIGATE; ADOPT 0. Paper derivations in the Fourier and mixed-pole convention of 001B. Previous investigations remain stayed. Native marked-signature attachment remains open.

## 1. Exact pole/Gamma cancellation

For w>0 the kernel of 001B satisfies
$$
L(w)=2\cosh(w/2)-\frac{e^{-w/2}}{1-e^{-2w}}
=e^{w/2}-\frac{e^{-5w/2}}{1-e^{-2w}}.
$$
The lowest Gamma exponential cancels one pole exponential, without a pole-null assumption. For h in L²(0,2c) put
$$
M_+=\int_0^{2c}e^{r/2}h(r)dr,\quad
M_n=\int_0^{2c}e^{-(2n+1/2)r}h(r)dr\quad(n\ge1).
$$
The exterior nonprime response is
$$
H(s)=e^{s/2}M_+-\sum_{n\ge1}e^{-(2n+1/2)s}M_n,\qquad s>0.
$$
Persistence requires H(s)=S(s) a.e. on (0,epsilon), where S is the actual weighted prime-shadow sum of zero-extended h from 001B, retaining log m < 2c+epsilon and both collar realizations separately.

## 2. Exterior moment rigidity

If H vanishes on a set of positive measure in a positive interval, real analyticity gives H=0 throughout s>0. Multiply by exp(-s/2) and let s tend to infinity to obtain M_+=0; uniqueness of the convergent power series in exp(-2s) then gives M_n=0 for n>=1. Let a=exp(-4c)>0, x=exp(-2r). The moment equations are
$$
0=\tfrac12\int_a^1 x^{n-3/4}h(-\tfrac12\log x)dx,\qquad n\ge1.
$$
The span of x^n (n>=1) is uniformly dense in C([a,1]), since f/x can be uniformly approximated by polynomials. The integrable moment density is therefore zero, so h=0 a.e. This proves that any nonzero persistent mode has a prime-shadow sum nonzero a.e. on its collar. This does not exclude an actual nonzero shadow.

## 3. Cauchy jump and local support reconstruction

Put z=exp(2s), a=exp(-4c), v(x)=x^{1/4}h(-log(x)/2)/2 on [a,1], and
$$
C_v(z)=\int_a^1\frac{v(x)}{z-x}dx,\qquad z\in\mathbb C\setminus[a,1].
$$
The substitution and geometric series, or direct kernel substitution, give
$$
H(s)=z^{1/4}M_+-z^{-1/4}C_v(z).
$$
Use the principal positive-real branch of the powers near [a,1]. On the exterior interval the prime shadow determines the germ
$$
C_v(z)=z^{1/2}M_+-z^{1/4}S(\tfrac12\log z).
$$
Since v is L² on [a,1], Cauchy boundary values in L² locally (or distributionally) satisfy C_v(x+i0)-C_v(x-i0)=-2pi i v(x). Consequently the analytic continuations of the shadow germ from the exterior along the upper and lower sides of the slit, written in s coordinates, satisfy
$$
S^\uparrow(-r)-S^\downarrow(-r)=\pi i h(r),\qquad 0<r<2c
$$
a.e. Here the two branches refer to the Cauchy representation; no analytic continuation of arbitrary individual translated L² germs is assumed. The unknown M_+ contributes no jump.

**Local theorem:** If the exterior shadow germ admits a real-analytic extension through s=0 to (-eta,eta), then h=0 a.e. on (0,min(eta,2c)), or on a smaller positive interval if the chosen holomorphic neighborhood is smaller. Proof: its holomorphic extension near 0 agrees by the identity theorem with the upper and lower Cauchy branches reached from positive s. Their jumps vanish on a small negative segment, hence the corresponding h vanishes. More generally agreement of both continuations across any open subinterval of the slit implies h=0 on the corresponding physical interval. A single analytic continuation on a neighborhood of the entire real segment [-2c,epsilon'] (epsilon'>0) implies h=0 everywhere by the same jump argument. In particular a finite exponential polynomial shadow is impossible for a nonzero persistent mode.

**Critical-support corollary:** Suppose a nonzero physical neutral mode at c lies in the native form domain, its zero extension has unchanged form value, and all smaller supports have strict positivity on the corresponding native form domains. If the two exterior prime-shadow germs both extend real-analytically through their boundary coordinate s=0, the local theorem gives zero neighborhoods at both ends of [-c,c]. The mode then lies in a strictly smaller support form domain (assuming native domain compatibility), contradicting strict positivity. Thus at least one of the weighted prime-shadow germs fails analytic extension through s=0. If parity is independently established, the reflected germs have the same property. The conclusion is conditional on the physical first-contact hypotheses and not on an assumed unproved neutral realization.

## 4. Scope correction and next gate

Analyticity strictly *inside* a positive collar is automatic under persistence, and is not enough for anti-locality. Analytic extension through the boundary, with agreement of both slit continuations, is the relevant hypothesis. It forces local support loss, not necessarily global vanishing without further continuation. No theorem forcing that extension for actual neutral modes has been established. Nor does failure of persistence for a nonzero mode alone prove RH.

Next: determine whether the original interior neutral equation enforces matching jumps or boundary nonanalyticity at the actual prime-shadow locations. In particular, a first-contact persistent mode requires nonanalyticity of the weighted shadow across at least one support edge, and the two-sided continuation jumps reconstruct its physical values. Preserve native domain, coefficient metric, signs, multiplicities and threshold terms. No promotion of MTP-2 or RH. No Lean compilation performed.
