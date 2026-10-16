# RPB108 SI25 — first orthogonal frequency-moment Bessel reference

**Parent:** SI24 merged, \`8af62a36ea1111e51f68c34060839bbf7e25094a\`, PR #119.  
**Track:** independent structural SI original signed physically supported odd operator; native RC high-Schur proceeds independently.  
**Standing:** conditional on exact-rational CI, a stronger eight-feature **one-pole inverse upper** from true frequency-orthogonal Bessel components. No full negative-frequency Birman–Schwinger matrix, full Weil positivity, Stage I, F4, Lean, or RH.

## 1. A new axis: certify orthogonal content of the continuous frequency band

SI24's six-feature positive Loewner minorant used mean-frequency Jensen vectors at centers \(0.30,0.76,1.20,1.65,0.25,0.35\), with original seven-prime signed multiplier inequalities valid on the corresponding entire neighborhoods. Its rigorously computed inverse upper comparison was
\[
2\langle s,A_o^{-1}s\rangle<2.169634.
\]
For the two *outer SI23 continuous-frequency bands* \(J_\pm=[0.22,0.28]\) and \([0.32,0.38]\), SI25 adds the **first orthogonal Legendre frequency moment**, not an extra midpoint sample or an arbitrary correlated column.

On any band \(J=[c-r,c+r]\), let \(u=(\xi-c)/r\), \(h_\xi(x)=\sin(2\pi\xi x)\), and normalized expectation \(E[F]=\frac12\int_{-1}^1F(u)\,du\). Then \(1\) and \(\sqrt3\,u\) are orthonormal in \(L^2([-1,1],du/2)\). Define the **true** physical supported vectors
\[
g_{0,c,r}(x)=E[h_{c+ru}(x)],\qquad
g_{1,c,r}(x)=3E[u\,h_{c+ru}(x)].
\]
Bessel/Parseval yields the exact positive operator inequality
\[
\boxed{
T_{J,o}=2\int_J|h_\xi\rangle\langle h_\xi|\,d\xi
\succeq4r\,|g_0\rangle\langle g_0|
+\frac{4r}{3}|g_1\rangle\langle g_1|.
}
\]
Indeed the first two orthogonal frequency coefficients are \(\sqrt2\,g_0\) and \(\sqrt{2/3}\,g_1\) in the Lebesgue \(u\)-measure, so both positive terms are exact; the omitted higher moments have **positive semidefinite** remainder. No adjustment to the original scalar floor is needed.

SI25 retains all six SI24 mean Jensen vectors, and adds \(g_1\) on \(c=1/4\) and \(c=7/20\), both radius \(r=3/100\), using SI13's entire signed original Fourier lower margin \(\delta=1399/1000\). The other four windows retain the individually certified SI21 margins. By disjointness of the six positive frequency bands and reflections:
\[
\boxed{
A_o\succeq C_8=\kappa I_o+
\sum_{j=1}^{6}4r_j\delta_j|g_{0,j}\rangle\langle g_{0,j}|
+\sum_{j=5}^{6}\frac{4r_j\delta_j}{3}|g_{1,j}\rangle\langle g_{1,j}|,
\quad\kappa=1/1000.
}
\]

## 2. Physically supported full eight-feature inverse certificate

Let \(G:\mathbb C^8\to H_o\) synthesize these **genuine functions**, \(\Gamma\) be the diagonal of the certified positive moment coefficients, \(H=G^*G\) its **full signed physical \(8\times8\) Gram**, and \(q=G^*s\) the original odd-pole overlaps. The supported operator inverse order and Woodbury law imply
\[
2\langle s,A_o^{-1}s\rangle\le
2\left(\frac{\|s\|_2^2}{\kappa}
-\frac{q^*(\Gamma^{-1}+H/\kappa)^{-1}q}{\kappa^2}\right).
\]
Select a rational trial dual witness \(z\) via midpoint linear solve; **certify** using all outward physical intervals and
\[
q^*M^{-1}q\ge2z^*q-z^*Mz,\quad M=\Gamma^{-1}+H/\kappa\succ0.
\]
This avoids treating the midpoint matrix as the actual original operator or dropping signed physical cross terms.

The degree-0 true averaged features use SI24's certified normalized single-panel Simpson error \(\tau_{0,j}=(2\pi r_j B)^4/180\). The two degree-1 **true** moment functions are enclosed by normalized composite Simpson on \(N=8\) frequency panels (all nine rational nodes), applied to \(f(u)=3u h_{c+ru}\). Its fourth derivative obeys
\[
\sup_{|u|\le1,|x|\le B}|\partial_u^4 f(u)|
\le3(4\beta^3+\beta^4),\quad\beta=2\pi rB,
\]
so the normalized integral error is
\[
\boxed{
\tau_{1}\le \frac{3(4\beta^3+\beta^4)}{180}
\left(\frac{2}{N}\right)^4.
}
\]
The validator uses the outward rational upper \(\pi\), never a floating-point pass criterion. It charges \((3/4)\tau_i\) on each original \(s\)-overlap and the conservative physical Gram product error \(4B(\tau_i+\tau_j)\), using pointwise \(|g_0|\le1\) and \(|g_1|\le3/2\). Every one of the **64 signed Gram entries** is included. Input support is never replaced by an unrestricted Fourier inverse.

**SI25 exact gate to be confirmed by Actions**:
\[
\boxed{2\langle s,A_o^{-1}s\rangle<\frac{13}{6}\approx2.166667.}
\]
A separate strict single-source reference test seeks a positive \(C_8-2|s\rangle\langle s|\) quadratic surplus \(>0.047\) **on the particular vector \(s\)**; that is not an operator spectral inequality.

## 3. Strategic interpretation

Pre-certificate floating-point physical quadrature suggests the six- to eight-feature nominal inverse upper moves only from approximately 2.14476 to 2.11840, a gain of 0.02636 (about **1.2%**). SI24's already rigorous displayed bound was 2.169634, not the nominal six-feature value, because rigorous overlap/quadrature interval slack is charged. SI25's certified upper must similarly include the full interval cost; no numeric improvement is asserted until the validator and CI succeed.

This comparison tests **diminishing returns** for adding first orthogonal frequency moments. Further isolated rank growth may be less valuable than replacing the sparse reference with more of the actual continuous positive operator or computing a correct-sign native supported inverse. The one-pole threshold \(1\) has **not** been achieved, and reaching it alone would still not certify SI11's full negative-frequency Birman–Schwinger norm.

**Next frontier SI26:** quantify second-moment marginal gain and/or derive a reusable analytic reference inverse residual on the full continuous interval, then compare against the native RC high-Schur cost before expanding a full SI11 matrix.

Replay: \`python scripts/validate_rpb108_si25_first_moment_bessel.py\`. All numerical acceptance inequalities use \`fractions.Fraction\` and prior signed continuous-frequency certification. The analytic Bessel identity is not a separate Lean formalization or external proof audit.
