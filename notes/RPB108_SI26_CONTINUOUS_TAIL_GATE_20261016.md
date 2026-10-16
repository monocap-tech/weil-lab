# RPB108 SI26 — closing the *entire* remaining outer-band moment family (reference-only)

**Parent:** SI25 merged as \`7f4cce289abc72c32fa1bbf6380fd09460196b4d\` (PR #120).  
**Track:** independent structural SI original signed, physically supported odd Hilbert space. Native RC high-Schur is independent.  
**Scope:** a conditional-on-CI *no-go* for **the specific C23 supported positive lower-reference strategy when changing only higher orthogonal moments on the two SI23 outer bands**. This is not a nonpositivity theorem about the original Weil form, an original \(A_o^{-1}\) lower bound, Stage I, F4, Lean, or RH.

## 1. The proper comparison is not an eighth-vs-tenth column computation

SI23 introduced the genuine **continuous** signed-original positive reference \(C_{23}\):
\[
C_{23}=C_4+\delta T_{E,o},\qquad
E=[0.22,0.28]\cup[0.32,0.38],\quad \delta=1399/1000.
\]
The original signed multiplier satisfies \(m(\xi)>\kappa+\delta=1.4\) on the *entire reflected* SI13 band \(\pm[0.22,0.38]\), and all four SI21 windows remain separately certified. Thus \(A_o\succeq C_{23}\) on the actual odd physical carrier \(L^2([-11/10,11/10])_{\rm odd}\).

SI25's finite **eight-feature** reference \(C_8\preceq C_{23}\) includes all six mean Jensen modes and the first two frequency-orthogonal Legendre modes, one for each outer band. The gap \(R=C_{23}-C_8\) consists of **all higher Legendre moments of those two bands, together**, not simply the next degree-two term. SI26 estimates the **entire** gap without computing further Gram columns.

## 2. Exact whole-operator Bessel tail bound

For \(J=[c-r,c+r]\), \(r=3/100\), set \(u=(\xi-c)/r\) and \(h(u,x)=\sin(2\pi(c+ru)x)\), \(x\in[-B,B]\), \(B=11/10\). Let \(P_1\) be the orthogonal projector in the **frequency variable \(u\)** onto \(\operatorname{span}\{1,u\}\). On the actual physical odd Hilbert space, Bessel/Parseval identifies
\[
R_J=T_{J,o}-4r|g_0\rangle\langle g_0|
-\tfrac{4r}{3}|g_1\rangle\langle g_1|\succeq0.
\]
The true moment vectors \(g_0=E[h]\), \(g_1=3E[uh]\) are as in SI25; no truncation of their definitions occurs.

Because \(P_1\) is the best \(L^2([-1,1],du)\) degree-one approximation,
\[
\int_{-1}^1\!\!\|h(u,\cdot)-P_1h(u,\cdot)\|_{L^2([-B,B])}^2du
\le\int_{-B}^B\!\!\int_{-1}^1
\frac{(2\pi r)^4 x^4 u^4}{4}\,du\,dx
=\frac{(2\pi r)^4 B^5}{25}.
\]
The inequality is the global Taylor remainder after \(h(0,x)+u\partial_u h(0,x)\), bounded at **every** \(x,u\) by \((2\pi r)^2x^2u^2/2\). In particular, the omitted operator is PSD and trace class with
\[
0\preceq R_J,\qquad
\|R_J\|_{\rm op}\le\operatorname{Tr}R_J
\le\frac{2r(2\pi r)^4B^5}{25}.
\]
No infinity-of-sampled-frequencies or unbounded Fourier reciprocal has been substituted for the original supported integral.

With the original positive signed factor \(\delta\) on each of two outer bands, the **complete** weighted tail satisfies
\[
\boxed{
0\preceq C_{23}-C_8\preceq\varepsilon I_o,
\qquad
\varepsilon=\frac{4\delta r(2\pi_{\rm hi}r)^4B^5}{25}
<1.4\cdot10^{-5}.
}
\]
The \(\pi_{\rm hi}\) bound is SI06's exact rational interval. The estimate pays *all* Legendre degrees \(2,3,\ldots\), without any missing band, residual, or operator-norm error.

## 3. Two-sided inverse bounds on the **reference**, not on the original \(A_o\)

SI25 established a correct-sign original-supported inverse **upper comparison**
\[
2\langle s,A_o^{-1}s\rangle\le2\langle s,C_8^{-1}s\rangle
<2.160880.
\]
SI26 adds the missing **lower** enclosure on \(2\langle s,C_8^{-1}s\rangle\), **not** on \(2\langle s,A_o^{-1}s\rangle\). Use SI25's exact eight true physical Gram and source intervals, with all signed off-diagonal entries and the complete rigorously charged Simpson errors. Put \(H=G^*G\), \(q=G^*s\), \(\Gamma=\operatorname{diag}(\gamma_i)>0\), \(M=\Gamma^{-1}+H/\kappa\succ0\). Woodbury is an *identity* for the finite reference:
\[
2\langle s,C_8^{-1}s\rangle
=2\left(\frac{\|s\|^2}{\kappa}-\frac{q^*M^{-1}q}{\kappa^2}\right).
\]
For an exact rational \(z\) selected through a rational midpoint solve, the exact residual identity
\[
q^*M^{-1}q
=2z^*q-z^*Mz + (q-Mz)^*M^{-1}(q-Mz)
\]
implies, **since \(M\succeq\Gamma^{-1}\)**,
\[
\boxed{
q^*M^{-1}q\le
2z^*q-z^*Mz+
\gamma_{\max}\|q-Mz\|^2.
}
\]
All positive and negative coefficients use their correct outward endpoint and *each* residual component uses its complete interval. Coupled with SI25's lower correction and SI12's true supported norm \(\|s\|^2=\sinh B-B\), this proves a true **two-sided** interval for the actual finite-rank reference pole response. The accepting gate targets
\[
\boxed{2\langle s,C_8^{-1}s\rangle>2.}
\]

Because \(C_8\preceq C_{23}\preceq C_8+\varepsilon I_o\) and \(C_8\succeq\kappa I_o\), the spectral calculus gives
\[
(C_8+\varepsilon I_o)^{-1}
\succeq(1-\varepsilon/\kappa)C_8^{-1}.
\]
Consequently,
\[
\boxed{
2\langle s,C_{23}^{-1}s\rangle
\ge(1-\varepsilon/\kappa)\,2\langle s,C_8^{-1}s\rangle
>1.97.
}
\]
Also, every higher-frequency moment combined can improve the **reference** pole inverse response by at most
\[
\boxed{
0\le2\langle s,C_8^{-1}s\rangle
-2\langle s,C_{23}^{-1}s\rangle
\le(\varepsilon/\kappa)\,2\langle s,C_8^{-1}s\rangle
<0.03.
}
\]

**These strict numerical gates require the full validator and final-head CI.** In particular the result does not say the actual signed Weil operator has a bad direction: \(A_o\) may contain arbitrarily important additional original positive-frequency information beyond the chosen windows.

## 4. Decision for the research program

If these tests pass, **the entire higher-moment family on just the two outer bands is exhausted as a method of reaching the one-pole BS threshold of 1.** It does not matter how many extra moments, finer Taylor panels, or more precise arithmetic one adds there: the original *continuous* outer-band lower reference \(C_{23}\) itself fails its one-pole inverse threshold by a wide margin.

The proper **SI27 frontier** is to locate **new independent original signed positive frequency mass outside the existing six windows**, or compute a supported physical inverse against more of the *actual* full operator, and then explicitly test genuine negative-frequency BS couplings. Do not spend another large Gram/CI pass merely adding moments of these two outer bands. Compare with the RC native high-Schur route.

Reproduce: \`python scripts/validate_rpb108_si26_continuous_tail_gate.py\`. Only exact rational \`Fraction\` inequalities accept; the Loewner/Bessel and residual identities are analytic arguments rather than a standalone Lean formalization. No RH conclusion.
