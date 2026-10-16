# RPB108 SI14 — multi-window odd supported inverse bounds and a scalar-chord no-go

**Parent:** merged RC334, commit \`af3e0d994e15155e70f8120115896773a64473b0\`; SI13 already integrated at PR #107.  
**Front:** independent Structural Investigation. Original CC27/RC312–313 signed archimedean + seven-prime frequency multiplier and the SI11/12/13 physically supported positive inverse \(A^{-1}\).  
**Status:** exact signed frequency interval and Fourier-mass certificates, an improved actual *supported odd inverse upper bound*, and a **proof-strategy obstruction** for positive-window scalar-chord certificates. **No genuine odd inverse vector, residual Gram, full finite Birman–Schwinger matrix, Stage I closure or RH proof.**

## 1. The inherited full original decomposition

On \(I=[-B,B]\), \(B=11/10\), let \(Zf\) denote zero extension and use \(\widehat{Zf}(\xi)=\int_I f(x)e^{-2\pi i x\xi}\,dx\). From SI11,
\[
m(\xi)=\Re\psi(1/4+i\pi\xi)-\log\pi
-2\sum_{n\in\{2,3,4,5,7,8,9\}}
\frac{\Lambda(n)}{\sqrt n}\cos(2\pi\xi\log n),
\]
with base-prime weights for powers. Put \(\kappa=1/1000\) and
\[
a(\xi)=\max(m(\xi),\kappa),\quad
A=Z^*\mathcal F^{-1}a\mathcal F Z
+2|\cosh(x/2)\rangle\langle\cosh(x/2)|,
\]
understood as the *physically supported* positive selfadjoint form operator. The original negative odd pole vector is \(s(x)=\sinh(x/2)\); its standalone Birman–Schwinger value is \(2\langle s,A^{-1}s\rangle\). The complete signed negative-frequency operator remains separately present in the full BS matrix.

SI13 used \(J_1=\pm[0.22,0.38]\), a rigorous original \(m>1.4\) on \(J_1\), and an original supported Fourier mass \(\int_{J_1}|\widehat{Zs}|^2>0.0288\) to improve the scalar-only odd inverse upper bound from approximately 471.295 to <413.753. SI14 asks if **aggregating other disjoint positive windows** can get near the necessary BS target 1.

## 2. Complete *signed* multiwindow certificate

Choose the three pairwise disjoint rational positive-frequency windows, together with their reflections:
\[
J_1^+=[11/50,19/50],\qquad
J_2^+=[73/100,79/100],\qquad
J_3^+=[219/100,223/100],
\quad J=\bigcup_{j=1}^3(J_j^+\cup-J_j^+).
\]
The exact SI14 Fraction validator partitions **each window** into 128 dyadic-rational cells, bounds the *whole* original signed prime cosine response using SI06's rigorous rational phase/log/sqrt enclosures and the globally certified \(|p'(\xi)|<69\), and pays the monotone Euler-digamma tail on every cell. It establishes
\[
\boxed{m(\xi)>\kappa+1=1.001\qquad(\xi\in J).}
\]
No finite sampling inference is used for a continuum sign claim. Parity gives the reflected-frequency statement.

Define the physically supported positive contraction
\[
T_J=Z^*\mathcal F^{-1}\mathbf1_J\mathcal FZ,\quad0\preceq T_J\preceq I.
\]
Its positivity and support preservation are exact even though physical Fourier cutoff itself would not preserve compact support. The original positive form satisfies
\[
A\succeq\kappa I+T_J,\qquad
A^{-1}\preceq(\kappa I+T_J)^{-1}
\preceq\frac1\kappa I-\frac1{\kappa(\kappa+1)}T_J.
\]
The last inequality is a scalar *convex-chord majorant* on the spectral interval \([0,1]\), not a claim that restriction commutes with inversion.

## 3. Certify the original ODD Fourier energy across all three bands

The physical odd pole \(s(x)=\sinh(x/2)\) has the exact Fourier amplitude
\[
|\widehat{Zs}(\xi)|
=\frac{2\left|
\frac12\cosh(B/2)\sin(2\pi B\xi)
-(2\pi\xi)\sinh(B/2)\cos(2\pi B\xi)
\right|}{\frac14+(2\pi\xi)^2}.
\]
The validator evaluates the three rational band centers \(\xi_1=3/10,\;\xi_2=76/100,\;\xi_3=221/100\) using outward **rational** sine/cosine Taylor enclosures, Machin bounds for \(\pi\), rational hyperbolic Taylor enclosures and rigorous original phase reduction modulo \(2\pi\). It certifies the center amplitude lower thresholds \(0.54, 0.16, 0.07\), respectively.

The supported first-moment derivative inequality from SI13 holds on the entire line:
\[
\left|\frac d{d\xi}\widehat{Zs}(\xi)\right|
\le2\pi\int_I|x\,s(x)|dx<3.
\]
Thus throughout each *complete* window, the respective lower amplitude bounds are \(>0.30,\ >0.07,\ >0.01\). Parseval and reflection give the explicit combined original physical odd Fourier mass
\[
\boxed{\int_J|\widehat{Zs}(\xi)|^2d\xi>
2(0.16)(0.30)^2+
2(0.06)(0.07)^2+
2(0.04)(0.01)^2.}
\]
All lower bounds are rational and strict; the exact sum is consumed by the verifier.

The resulting **actual supported odd inverse upper** is
\[
\boxed{
2\langle s,A^{-1}s\rangle
<
\frac{2(\sinh B-B)}{\kappa}
-\frac{2}{\kappa(\kappa+1)}
\int_J|\widehat{Zs}(\xi)|^2.
}
\]
This is a new rigorously supported comparator, not a calculated inverse vector, and the printed strict numeric margin is read from successful GitHub Actions replay.

## 4. New analytic obstruction: positive-window scalar chords cannot finish the odd pole

The obstacle is **more fundamental than the efficiency of searching for windows**.

Independently of the positive windows, SI14 certifies an original **negative** signed multiplier interval
\[
J_{\rm bad}=\pm[7/100,13/100],
\qquad
\boxed{m(\xi)<0<\kappa\quad(\xi\in J_{\rm bad}).}
\]
For this upper sign test, use monotonicity of \(\Re\psi(1/4+i\pi\xi)\) in \(|\xi|\), the exact 128-term **upper** Euler/digamma bound (with integral tail from index 127), the full signed seven-prime rational cosine **upper** at \(0.1\), and the all-frequency prime Lipschitz penalty \(69(0.13-0.07)/2\). The validator asserts the entire worst-case upper is negative, not just the midpoint.

The same original analytic Fourier formula and rigorous derivative bound show
\[
|\widehat{Zs}(0.1)|>0.26,\qquad
|\widehat{Zs}(\xi)|>0.26-3(0.03)=0.17
\quad(\xi\in[0.07,0.13]).
\]
By reflection,
\[
\boxed{
E_{\rm forbidden}
=\int_{J_{\rm bad}}|\widehat{Zs}(\xi)|^2d\xi
>2(0.06)(0.17)^2=0.003468.
}
\]
For **any** symmetric set \(J\) confined to frequencies where \(m(\xi)\ge\kappa+\delta\) for a single chosen \(\delta>0\), \(J\cap J_{\rm bad}=\varnothing\), and its scalar-chord *upper certificate*
\[
U_{\rm chord}(J,\delta)=
\frac{2\|s\|^2}{\kappa}
-\frac{2\delta}{\kappa(\kappa+\delta)}
\int_J|\widehat{Zs}(\xi)|^2d\xi
\]
necessarily satisfies
\[
\boxed{
U_{\rm chord}(J,\delta)
\ge\frac{2}{\kappa}\int_{J_{\rm bad}}|\widehat{Zs}|^2
>6.936>1.
}
\]
The proof uses only Parseval and \(\delta/(\kappa+\delta)<1\). No possible choice or number of disjoint **positive frequency windows**, **within this scalar-chord comparison class**, can certify the odd BS threshold \(\le1\).

**Crucial distinction:** \(U_{\rm chord}>1\) is a **floor on the certificate's UPPER BOUND**. It is absolutely **not** a lower bound on the *true* value \(2\langle s,A^{-1}s\rangle\), and does not exhibit a negative Weil direction or preclude a more sophisticated supported inverse estimate. In particular, the actual physically supported operator couples frequencies; its inverse cannot be evaluated pointwise.

## 5. Decision: end the window-only optimization loop

SI14 has a two-part result: a certified improvement from aggregating three disjoint genuine positive windows, and a **rigorous method-class no-go** explaining why indefinitely adding windows cannot prove odd-pole stability through this scalar chord mechanism. This is a valid **structural efficiency conclusion**.

**SI15 target:** construct a genuine *odd* supported trial inverse \(y\approx A^{-1}s\), and certify the **correct-sign positive residual term**
\[
2\langle s,A^{-1}s\rangle
=4\langle s,y\rangle-2\langle y,Ay\rangle
+2\langle s-Ay,A^{-1}(s-Ay)\rangle
\le4\langle s,y\rangle-2\langle y,Ay\rangle+
\frac{2}{\kappa}\|s-Ay\|^2.
\]
The trial response must lie in \(\operatorname{Dom}A\), and the error must be an original **supported** operator residual with all Fourier and rank-one terms included; a purely numerical Fourier reciprocal or a projected algebraic residual is invalid. Benchmark the computational cost against RC334's native signed high-inverse path, which remains primary.

No whole Weil positivity, complete odd-pole Birman–Schwinger eigenvalue, original source residual Gram, Stage I closure, F4, LF/Lean, or RH is claimed.

## Replay

\`python scripts/validate_rpb108_si14_odd_multiband_nogo.py\`

The validator inherits the original signed SI06/12/13 digamma/prime data and uses \`Fraction\` for all finite acceptance checks, plus exact rational Fourier-moment formulas. It is not a Lean proof or independent peer review.
