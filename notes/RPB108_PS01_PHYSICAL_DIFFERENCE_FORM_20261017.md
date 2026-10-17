# PS01 — physical difference-energy form of the original signed seven-prime Weil operator

**Research lane:** \`W-PHYSICAL-SHIFT\`, independent, exploratory, OPEN. **Canonical active obligation stays \`W-ODD-NEG\`.**
**Parent:** SI10 original signed Fourier multiplier; RC313/315 original prime translations; RC320 endpoint-cancelled translation sources; SM17 whole odd spectral gate.
**Scope:** algebraic/analytic change of coordinates for the *same* original supported form, plus a reproducible two-vector signed audit. No positivity theorem, finite Schur closure, or RH implication.

## 1. Why this is not an undiscovered prime-shift formula

RC315 already computes exact physical autocorrelations of P0/P1 for all seven prime-power shifts, and RC320 exploits cancellation of boundary jumps in the 14 shifted sources. Thus **prime shifts themselves are established repository machinery**. PS01 examines a different extension: rewrite *both* the archimedean and prime portions as a common physical difference-energy functional, and test whether that representation suggests a sharper coupled operator comparison. It must not restart or duplicate RC315/RC320 without a strictly new diagnostic.

## 2. Full signed supported form, conventions and domain

Put \`B=11/10\`, \`R=2B=11/5\`. For a real or complex physical input \`f\` on \`[-B,B]\`, let \`g=Zf\` be zero extension to the real line and use
\[
\widehat g(\xi)=\int_{\mathbb R}g(x)e^{-2\pi i\xi x}\,dx,\qquad
C_f(u)=\int_{\mathbb R}g(x)\overline{g(x+u)}\,dx .
\]
Let \(\tau_u g(x)=g(x+u)\) and \(D_f(u)=\|g-\tau_u g\|_2^2\).
Plancherel gives the **exact** identities
\[
\operatorname{Re}C_f(u)=\|f\|_2^2-\tfrac12D_f(u),\qquad
\int_{\mathbb R}\cos(2\pi \xi u)|\widehat g(\xi)|^2d\xi
=\operatorname{Re}C_f(u).
\]
For \(u\ge R\), disjoint supports give \(C_f(u)=0\) and \(D_f(u)=2\|f\|_2^2\).
The full original signed SI10 Fourier model is
\[
Q[f]=\int_{\mathbb R}m(\xi)|\widehat g(\xi)|^2d\xi
+2|\langle f,\cosh(x/2)\rangle|^2
-2|\langle f,\sinh(x/2)\rangle|^2 ,
\]
\[
m(\xi)=\operatorname{Re}\psi(\tfrac14+i\pi\xi)-\log\pi
-2\sum_{n\in N}\frac{\Lambda(n)}{\sqrt n}
 \cos(2\pi\xi\log n),\quad N=\{2,3,4,5,7,8,9\}.
\]
Here \(\Lambda(4)=\Lambda(8)=\log2\) and \(\Lambda(9)=\log3\), *not* \(\log n\).
No Fourier cutoff, periodic wraparound or replacement of the physical inverse is introduced.

The digamma integral difference for \(a=1/4\) is
\[
\operatorname{Re}\psi(a+i\pi\xi)-\psi(a)
=\int_0^\infty \frac{e^{-at}(1-\cos(\pi\xi t))}{1-e^{-t}}dt.
\]
Its integrand after spectral integration is nonnegative. Tonelli and \(u=t/2\) therefore give
\[
\int_{\mathbb R}(\operatorname{Re}\psi(\tfrac14+i\pi\xi)-\log\pi)
 |\widehat g(\xi)|^2d\xi
=[\psi(\tfrac14)-\log\pi]\|f\|_2^2
+\int_0^\infty k(u)D_f(u)\,du,
\quad
k(u)=\frac{e^{-u/2}}{1-e^{-2u}}.
\]
The full seven-prime part is *also* a difference energy:
\[
-2\sum_n w_n\operatorname{Re}C_f(\ell_n)
=-2\sum_n w_n\|f\|_2^2+\sum_nw_nD_f(\ell_n),
\quad w_n=\frac{\Lambda(n)}{\sqrt n}>0,\quad \ell_n=\log n.
\]
Hence on the original signed form domain (and initially on the supported smooth/piecewise-smooth form core),
\[
\boxed{\begin{aligned}
Q[f]={}&c_{\rm shift}\|f\|_2^2
+\int_0^\infty k(u)D_f(u)\,du
+\sum_{n\in N}w_nD_f(\log n)\\
&+2|\langle f,c\rangle|^2-2|\langle f,s\rangle|^2,\\
c_{\rm shift}={}&-\gamma-\frac{\pi}{2}-3\log2-\log\pi-2\sum_{n\in N}w_n,\\
c(x)={}&\cosh(x/2),\quad s(x)=\sinh(x/2).
\end{aligned}}
\]
The difference-energy terms have **positive coefficients**, but the scalar term is negative. This rewriting does not prove \`Q>=0\`: the issue is whether the complete difference energy and pole correction dominate its scalar deficit *jointly* on the physical subspace. In particular, one cannot lower-bound the individual prime autocorrelation terms independently and assume their mixed Schur costs disappear.

Finite form energy is equivalent to finiteness of the archimedean difference integral, because the additional seven shifts are bounded on \(L^2\). A precise closure/identification with the completed CC27 D-Riesz operator remains an explicit *transfer obligation*, not a result of algebra alone.

## 3. Built-in original signed P0/P1 cross-check

Let \(u_0=1/\sqrt R\) and \(u_1=\sqrt{3/R}\,x/B\) on \([-B,B]\). For \(0\le u\le R\), with \(y=u/R\), RC315's **true zero-extended** correlations are
\[
C_{00}(u)=1-y,\qquad C_{11}(u)=1-3y+2y^3.
\]
Thus
\[
D_{00}(u)=2y,\qquad D_{11}(u)=6y-4y^3
\]
for \(0\le u\le R\), and both equal \(2\) for \(u\ge R\). The archimedean term can be certified *independently of RC46's regular-kernel Taylor coefficients* by
\[
k(u)=\sum_{j\ge0}e^{-a_j u},\qquad a_j=2j+\tfrac12.
\]
Direct integration gives
\[
\int_0^\infty e^{-a u}D_{00}(u)du
=\frac{2}{R a^2}(1-e^{-aR}),
\]
\[
\int_0^\infty e^{-a u}D_{11}(u)du
=\frac6{R a^2}-\frac{24}{R^3a^4}
+\frac{6R(aR+2)^2}{(aR)^4}e^{-aR}.
\]
The PS01 validator uses rational intervals for \(e^{-aR}\), a rigorous monotone-integral series tail, and the existing outward-rational elementary constant bounds to reconstruct the **same full original signed two diagonals** as RC315. RC315's pinned evidence is required for comparison; the new archimedean series is *not* calculated from RC46's coefficients.

Expected earlier certificate: \(\langle u_0,Qu_0\rangle\approx0.04025418\), \(\langle u_1,Qu_1\rangle\approx0.13238566\). These are known old results and their reproduction is a calibration test, **not new two-direction positivity**.

## 4. New structural diagnostics, not yet new results

1. **Physical overlap stratification:** \(\ell_n=\log n<R\) for all seven terms, and \(R-\log9\approx0.0027754\). Quantify the seven overlap windows on supported inputs, including mixed terms; narrow overlap alone does *not* shrink the \(L^2\) translation operator norm.
2. **Boundary cancellation:** for zero-extended \(H^1\) inputs, \(\|\tau_{\ell+\delta}g-\tau_\ell g\|_2\le|\delta|\|g'\|_2\). Compare against RC320; look for operator-level reductions rather than rediscovering its P2-P0 instance.
3. **Parity/reflection:** derive explicit difference-plus-reflection blocks for even and odd functions. Test whether any common operator minorant controls both, without assuming an unproved sign for the reflected block.
4. **Carrier comparison:** keep RC314's 301-dimensional D-Riesz localization distinct from SI10's L2 Taylor localization (890 columns per parity). Seek a **verified** norm/domain-preserving intertwining map; dimensional comparison alone is not a compression theorem.
5. **Discriminator:** a successful method change must deliver a certified *new* bound on a whole operator, a coupled finite exceptional block, or its residual, beyond merely evaluating selected positive vectors.

## 5. Standing and custody

PS01 is a scoped parallel investigation. \`research/obligations.json\` retains canonical \`W-ODD-NEG\` and the original active frontier; no head-number competition or transfer of proof status is allowed. PS01 passes only the identity derivation and the P0/P1 calibration when its validator and scoped CI pass. W-ODD-NEG, W-EVEN-FORM, the 890-column original Schur blocks, the global Weil/RH bridge, and RH remain OPEN.

Reproduce:
\`python3 scripts/validate_rpb108_ps01_physical_difference_form.py\`.
