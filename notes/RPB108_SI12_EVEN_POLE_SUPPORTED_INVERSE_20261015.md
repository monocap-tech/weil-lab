# RPB108 SI12 — physically supported even-pole inverse response and the odd-sector obstruction

**Parent:** SI11 integrated at \`c5f2550213e5c153f03d59e1b199f1fb09d4be5b\`.  
**Front:** independent structural investigation; parallel RC332 native signed high-Schur analysis preserved.  
**Standing:** certified **upper bounds for actual original supported positive-inverse matrix elements** derived by Loewner operator comparison, exact supported rank-one resolvent decomposition, and parity splitting. These are **not** an evaluated original inverse vector \(A^{-1}u\), an original \(A\)-residual Gram, the 1,631-feature Birman–Schwinger spectrum, full Weil positivity, Stage I, F4, Lean or RH.

## 1. Correct original operator and parity

SI11 decomposes the original CC27/RC312–313 complete signed Weil form on physical \(H=L^2([-B,B])\), \(B=11/10\), as \(Q=A-K\), where
\[
\begin{split}
A &= A_0+2|c\rangle\langle c|,\qquad
A_0=Z^*\mathcal F^{-1}a(\xi)\mathcal F Z,\quad a(\xi)=\max(m(\xi),\kappa),\\
K &= Z^*\mathcal F^{-1}r(\xi)\mathcal F Z+2|s\rangle\langle s|,\qquad
r(\xi)=(\kappa-m(\xi))_+,\quad\kappa=1/1000,\\
c(x)&=\cosh(x/2),\qquad s(x)=\sinh(x/2).
\end{split}
\]
Here \(A_0\) denotes the **selfadjoint operator associated with the supported positive closed form**; in general it is not the restriction of an unrestricted whole-line inverse. Its inverse exists as a bounded operator because \(A_0\ge\kappa I\). The original signed multiplier \(m\) is even in frequency, so both \(A_0\) and \(K\) preserve even/odd parity, \(c\) is even, and \(s\) is odd.

Consequently, **every exact supported inverse covariance between an even physical feature and an odd physical feature vanishes**:
\[
\boxed{\langle u_{\rm even},A^{-1}u_{\rm odd}\rangle=0.}
\]
This splits SI11's supported Birman–Schwinger matrix into even and odd blocks in a parity-respecting basis, reducing cross-covariance accounting without changing either proof obligation.

## 2. Exact Sherman–Morrison law on the *supported* inverse

Let \(R_0=A_0^{-1}\), and let \(\tau=\langle c,R_0c\rangle\). Then the bounded rank-one resolvent identity gives
\[
\boxed{
A^{-1}=R_0-\frac{2\,|R_0c\rangle\langle R_0c|}{1+2\tau}.
}
\]
This identity holds **exactly for the original physically supported inverse**; it is not obtained by commuting compression and Fourier inversion.

In particular,
\[
\boxed{\langle c,A^{-1}c\rangle=\frac{\tau}{1+2\tau},\qquad
\tau=\langle c,A_0^{-1}c\rangle.}
\]
For any even input \(u\),
\[
\boxed{
\langle u,A^{-1}u\rangle
=\langle u,R_0u\rangle
-\frac{2|\langle u,R_0c\rangle|^2}{1+2\tau}.
}
\]
The subtracted correction has the **correct sign**; dropping it gives a conservative upper bound, not equality. For all odd \(u\), the rank-one correction is exactly zero. Thus the original positive even pole can improve the *even* inverse response but **does not directly control the negative odd-pole direction**.

## 3. First explicit rigorous supported inverse-column upper bound

Because \(A_0\ge\kappa I\),
\[
A=A_0+2cc^*\succeq C:=\kappa I+2cc^*,
\quad\Rightarrow\quad
\boxed{A^{-1}\preceq C^{-1}.}
\]
Here \(C\) is a bounded **physical supported** reference and can be inverted *exactly*:
\[
\boxed{
C^{-1}=\kappa^{-1}I-
\frac{2}{\kappa(\kappa+2\|c\|_2^2)}|c\rangle\langle c|.
}
\]

The original exact physical norms are
\[
\|c\|_2^2=B+\sinh B,\qquad
\|s\|_2^2=\sinh B-B.
\]
For the normalized physical constant \(u_0(x)=(2B)^{-1/2}\),
\[
|\langle u_0,c\rangle|^2=\frac4B(\cosh B-1).
\]
Therefore we have an **actual original supported inverse matrix-element inequality**:
\[
\boxed{
\langle u_0,A^{-1}u_0\rangle
\le\frac1\kappa
\left[
1-\frac{2(4/B)(\cosh B-1)}
{\kappa+2(B+\sinh B)}
\right]
<\frac{213}{100}=2.13.
}
\]
The all-direction floor alone gives \(1000\), so the original positive pole reduces the certified upper bound for this **one even column** by more than a factor of 469. This is a Loewner *upper certificate*, not a computed exact value.

For the normalized original even pole vector \(e_c=c/\|c\|_2\), similarly,
\[
\boxed{
\langle e_c,A^{-1}e_c\rangle
\le\frac{1}{\kappa+2(B+\sinh B)}
<\frac{206}{1000}=0.206.
}
\]
The exact \(\sinh,\cosh\) enclosures (positive rational Taylor sums plus explicit geometric remainder bounds) and the strict rational inequalities are replayed by the standard-library validator. No numerical floating-point sampling is used to certify the displayed thresholds.

### Why this is a genuinely supported result but not yet SI11's residual certificate

These are rigorous upper bounds on matrix elements of the **actual original supported** inverse \(A^{-1}\). They arise from the form order \(A\succeq C\) and the *exact supported reference inverse* \(C^{-1}\).

They do **not** supply an approximation \(Y\approx A^{-1}U\) with a validated original residual \(R=U-AY\). In particular, \(Y=C^{-1}U\) solves the *reference* problem \(CY=U\), not \(AY=U\), and the unknown residual \((A-C)Y\) must not be asserted zero. SI11's positive residual Gram obligation remains.

The bound can be used as one diagonal entry of a **certified Loewner matrix upper comparator** for a parity-respecting SI11 feature basis \(U\):
\[
\boxed{
U^*A^{-1}U
\preceq\kappa^{-1}I-
\frac{2}{\kappa(\kappa+2\|c\|_2^2)}
(U^*c)(U^*c)^*.
}
\]
If the SI11 span is enlarged by the single exact physical even feature \(c\), its rank increases by *at most one*; SI11's existing negative-operator Taylor approximation error remains valid (orthogonal projection onto a larger physical span does not worsen each plane-wave best-approximation error). This is a precise **one-column inverse preconditioner**, not an entire finite-matrix positivity certificate.

## 4. The odd-sector scalar-floor no-go

The negative odd pole belongs to \(K\), as \(2|s\rangle\langle s|\). Its stand-alone Birman–Schwinger operator has sole nonzero eigenvalue
\[
\lambda_{\rm odd,pole}=2\langle s,A^{-1}s\rangle.
\]
From the crude supported reference bound \(A^{-1}\preceq C^{-1}\), because \(s\perp c\),
\[
\boxed{2\langle s,A^{-1}s\rangle
\le\frac{2\|s\|_2^2}{\kappa}
=\frac{2(\sinh B-B)}{\kappa}\approx471.295.}
\]
This is far above the positivity threshold \(1\). **It does not show the actual odd pole is destabilizing**, only that the even-pole rank-one preconditioner and the scalar \(\kappa\) floor cannot certify its absorption. SI03's prime-energy absorption is on a *different positive decomposition* and cannot be inserted into \(A^{-1}\) without an exact operator interface.

Because odd/even parity decouple, this obstruction cannot be cured by off-diagonal even–odd covariance. The next meaningful supported inverse response must therefore involve a genuinely **odd physical source** and a strictly stronger positive reference than \(\kappa I\) in that sector.

## 5. SI13 next gate

For the original odd source \(s\), construct a rigorous *supported* positive comparison \(A_{\rm odd}\succeq C_{\rm odd}\succ\kappa I\) in a useful direction, or certify a genuine odd trial response \(Y\) with full **positive** residual Gram
\[
G_{\rm odd}=U_{\rm odd}^*Y+Y^*U_{\rm odd}-Y^*A_{\rm odd}Y
+R^*A_{\rm odd}^{-1}R.
\]
Do not replace the supported \(A_{\rm odd}^{-1}\) with unrestricted \(1/a(\xi)\), assume prime/pole sign cancellation carries through inversion, or claim that the observed ~471 scalar upper bound is an actual eigenvalue. Compare the computational expense against the smaller native RC332 signed Schur path.

**SI12 does not certify full original Weil positivity, the full 1,631-feature Birman–Schwinger eigenvalue gate, Stage I, F4, LF/Lean, or RH.**

## Reproduction

\`python scripts/validate_rpb108_si12_even_supported_inverse.py\`.

The exact-rational regression certifies all hyperbolic norm enclosures and strict inverse upper-threshold inequalities; the operator inequalities use the rank-one resolvent theorem and inverse monotonicity, not independent numerical verification of the full original integral operator.
