# RPB108 SI04 — Archimedean–prime Fourier safe band and trace-class localization of negative source

**Structural front:** SI04, independent of the RC324–328 native high-response certificates.  
**Parent:** merged RC328 \`c6a25abccb7ee8ec1b36c27016abbaebc571fbaf\`.  
**Sources:** original CC27 form identified in RC312–313; SI03's seven native prime coefficients and positive translation Dirichlet identity.  
**Standing:** an **all-input archimedean-plus-original-prime frequency localization theorem**, not full Weil positivity, an improved RC328 three-dimensional Schur certificate, or proof of RH.

## 1. Exact combined frequency multiplier

Set \(B=11/10\), \(I=[-B,B]\), \(Zf\) the zero extension of \(f\in L^2(I)\), and use
\(\widehat f(\xi)=\int_{\mathbb R} Zf(x)e^{-2\pi i x\xi}\,dx\).
The RC312 original archimedean multiplier is
\[
a_{\rm arch}(\xi)=\Re\psi(1/4+i\pi\xi)-\log\pi.
\]
The RC313 original paired prime translations have the **signed** multiplier
\(-2\sum_{n\in\mathcal A}c_n\cos(2\pi\xi\log n)\), with
\[
\mathcal A=\{2,3,4,5,7,8,9\},\qquad c_{p^k}=\frac{\log p}{\sqrt{p^k}}.
\]
Define
\[
\boxed{m(\xi):=a_{\rm arch}(\xi)
-2\sum_{n\in\mathcal A}c_n\cos(2\pi\xi\log n).}
\]
Then for every supported polynomial \(f\),
\[
Q_{\rm arch+prime}(f)=\int_{\mathbb R}m(\xi)|\widehat f(\xi)|^2\,d\xi.
\]
This identity is about the **entire signed original prime contribution**, not the positive Dirichlet part alone. The signed pole must still be added separately:
\[
Q_{\rm Weil}(f)=\int m|\widehat f|^2+
2|\langle c,f\rangle|^2-2|\langle s,f\rangle|^2,\quad
c(x)=\cosh(x/2),\ s(x)=\sinh(x/2).
\]

## 2. New all-degree safe-frequency theorem

**Claim.** For every real \(|\xi|\ge2048\),
\[
\boxed{m(\xi)>\frac{69}{700}>0.}
\]
This is a conservative *certified sufficient* cutoff; it is **not** the actual first sign-change frequency, and no optimality is claimed.

**Proof.** Euler's digamma series, applied at \(a=1/4\) and \(y=\pi|\xi|\), gives the exact, positive, increasing-in-\(y\) series
\[
\Re\psi(a+iy)-\psi(a)
=\sum_{k=0}^\infty g_y(k),\qquad
g_y(t)=\frac{y^2}{(t+a)((t+a)^2+y^2)}.
\]
For \(t\ge0\), \(g_y(t)\) decreases. Thus, for \(y\ge3(2048)\) (using \(\pi>3\)),
\[
\sum_{k\ge0}g_y(k)
\ge g_y(0)+g_y(1)+\int_2^\infty g_y(t)\,dt
= g_y(0)+g_y(1)+\frac12\log\left(1+\frac{y^2}{(9/4)^2}\right).
\]
Exact rational checks establish \(g_y(0)>399/100\) and \(g_y(1)>79/100\). Further,
\[
\frac12\log(1+y^2/(9/4)^2)
>\log(y/(9/4))
\ge\log(8192/3)
=13\log2-\log3>\frac{787}{100},
\]
using rigorously proved \(\log2>69/100\), \(\log3<11/10\).

The original quarter-digamma identity (RC312)
\[
\psi(1/4)=-\gamma-\frac\pi2-3\log2
\]
and the elementary certified bounds
\(\gamma<3/5,\ \pi<22/7,\ \log2<7/10,\ \log\pi<6/5\)
yield
\[
a_{\rm arch}(\xi)>
\frac{399}{100}+\frac{79}{100}+\frac{787}{100}
-\left(\frac35+\frac{11}{7}+\frac{21}{10}+\frac65\right)
=\frac{201}{28}=7.1785714\ldots.
\]
Rational \(\operatorname{atanh}\)-log enclosures and outward integer-square-root intervals for *all seven* original weights give
\[
2C:=2\sum_{n\in\mathcal A}c_n<\frac{177}{25}=7.08.
\]
Since \(-2\sum c_n\cos(\cdots)\ge-2C\) **pointwise** on all of \(\mathbb R\),
\[
m(\xi)>\frac{201}{28}-\frac{177}{25}
=\boxed{\frac{69}{700}}.
\]
The proof uses the proper **full pointwise** prime bound \(2C\), *not* SI03's smaller **supported-input operator** bound \(\|K_{\rm prime}\|<4.10315\). Substituting the latter pointwise would be invalid.

## 3. Entire negative part is contained in a finite Fourier band

Write \(m=m_+-m_-\) with \(m_\pm=\max(\pm m,0)\). SI04 implies
\[
\boxed{\operatorname{supp}m_-\subset(-2048,2048).}
\]
Moreover the digamma difference series gives \(a_{\rm arch}(\xi)\ge\psi(1/4)-\log\pi\), and therefore
\[
0\le m_-(\xi)\le
L:=\frac{383}{70}+\frac{177}{25}<13.
\]

Let the physical negative operator be
\[
K_-=Z^*\mathcal F^{-1}m_-\mathcal FZ
\]
on \(L^2(I)\). This is **positive trace-class**, not merely bounded or compact. Indeed write \(K_-=A^*A\), where
\(Af(\xi)=m_-(\xi)^{1/2}\widehat{Zf}(\xi)\) on \([-2048,2048]\).
Its integral kernel has Hilbert–Schmidt norm
\[
\|A\|_{\rm HS}^2
=\int_I\int_{-2048}^{2048}m_-(\xi)d\xi\,dx
=2B\int_{\mathbb R}m_-(\xi)d\xi.
\]
Thus
\[
\boxed{\operatorname{tr}K_-
=2B\int m_- \le 4B(2048)L
=\frac{45056}{5}L.}
\]
The unweighted band-limiting concentration operator
\(Q_{2048}=Z^*\mathcal F^{-1}\mathbf1_{[-2048,2048]}\mathcal FZ\)
has exact trace
\[
\boxed{\operatorname{tr}Q_{2048}=4B(2048)=\frac{45056}{5}=9011.2.}
\]

On the common polynomial core the **complete original signed form** consequently has the exact decomposition
\[
\boxed{
Q_{\rm Weil}(f)
=\underbrace{\int m_+|\widehat f|^2+
2|\langle c,f\rangle|^2}_{\text{nonnegative}}
-\underbrace{\bigl(\langle f,K_-f\rangle+
2|\langle s,f\rangle|^2\bigr)}_{\text{positive trace-class negative operator}}.
}
\]
The negative operator \(K_-+2|s\rangle\langle s|\) is positive trace-class on physical \(L^2(I)\); it remains trace-class when transported to the D carrier by the bounded physical embedding. This offers a **second, basis-independent localization mechanism** for the original form. The archimedean high-frequency growth supplies a nonnegative background; possible negativity is mediated by a finite Fourier band and the odd rank-one pole.

## 4. Why SI03's support gap cannot simply be pasted onto Fourier pieces

SI03's \(2.97185\) prime Dirichlet gap relies crucially on *compact physical support*: each cut-down translation decomposes into finite path graphs on \(I\). After applying a sharp Fourier projector, the resulting function is generally **not compactly supported** in \(I\). It would be incorrect to apply the SI03 finite-path gap separately to the positive/high or negative/low Fourier pieces.

The present theorem treats original primes **pointwise with \(2C\)** in the high band. SI03 instead treats primes **as cut-down physical operators with the stronger support-aware norm bound**. Developing a controlled bridge between those two decompositions (for example, time–frequency concentration estimates that retain support) is the SI05 research obligation.

## 5. Exact scope and next gate

- **Proved analytically:** all-input positive original archimedean-plus-prime multiplier for \(|\xi|\ge2048\); negative-part trace-class representation with explicit time–bandwidth trace bound; signed pole handled as an explicit rank-one negative perturbation.
- **Reproduced exactly:** logarithm and gamma enclosures, each original base-prime coefficient, cutoff margin \(69/700\), time-bandwidth trace \(45056/5\).
- **Not proved:** a positive lower bound for the full original Weil form; an effective small-dimensional projection of \(K_-\); a usable numerical rank/tail bound at the scale RC328 needs; actual 3D/317D Schur positivity; Stage I, F4, LF/Lean or RH.

**SI05:** investigate a *certified finite-rank approximation and tail norm* for \(K_-\) in the canonical D metric, or a frequency-localization inequality preserving the physical support-chain prime advantage. Test whether either can outperform the current RC328 inverse-response route before replacing it.

## Replay

\`\`\`bash
python scripts/validate_rpb108_si04_frequency_band.py
\`\`\`
