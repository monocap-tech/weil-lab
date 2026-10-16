# RPB108 SI13 — a genuine odd-sector supported inverse improvement from positive signed Fourier windows

**Parent:** merged SI12 at \`340bcf39f97b50eb6e1ac41f6b3543455c579806\`.  
**Track:** Structural Investigation, independent of the RC333 native signed degree-254 covariance PR.  
**Standing:** certified strict **upper improvement for an original odd supported inverse quadratic response**, using an explicit *positive-frequency multiplier window and physical time-limited compression*. This is **not** the calculation of the actual vector \(A^{-1}s\), an original \(A\)-residual Gram, the complete Birman–Schwinger finite matrix, a full signed Weil positivity proof, Stage I, F4, Lean, or RH.

## 1. Original supported decomposition, parity, and the real obligation

In SI11–12, on \(H=L^2(I)\), \(I=[-B,B]\), \(B=11/10\), we used the original CC27 / RC312–313 *signed* archimedean-plus-seven-prime multiplier
\[
m(\xi)=\operatorname{Re}\psi(1/4+i\pi\xi)-\log\pi
-2\sum_{n\in\{2,3,4,5,7,8,9\}}
\frac{\Lambda(n)}{\sqrt n}\cos(2\pi\xi\log n).
\]
With \(\kappa=1/1000\), define \(a(\xi)=\max(m(\xi),\kappa)\), \(r=(\kappa-m)_+\), and let \(A\) be the selfadjoint operator associated with the positive physical supported quadratic form
\[
\mathfrak a[f]
=\int a(\xi)|\widehat{Zf}(\xi)|^2d\xi
+2|\langle c,f\rangle|^2,\qquad
c(x)=\cosh(x/2).
\]
Then \(A\ge\kappa I\). The original negative operator is \(K=Z^*\mathcal F^{-1}r\mathcal F Z+2|s\rangle\langle s|\), where \(s(x)=\sinh(x/2)\) is odd.

SI12's even-pole rank-one reference improved even supported inverse matrix elements but did not improve the crude odd upper
\[
2\langle s,A^{-1}s\rangle\le 2\|s\|^2/\kappa
=\frac{2(\sinh B-B)}{\kappa}\approx471.29494.
\]
SI13 finds an independent, **strictly stronger odd-sector reference** without importing the SI03 prime Dirichlet gap into the wrong operator.

## 2. New all-point positive Fourier window, including all original prime phases

Define the symmetric rational frequency window
\[
J_+=[11/50,19/50]=[0.22,0.38],\qquad J_-=-J_+,\qquad J=J_+\cup J_-.
\]
SI13's exact rational verifier proves
\[
\boxed{m(\xi)>\frac75=1.4>\kappa+1\quad(\xi\in J).}
\]
The first successful Actions replay showed a minimum outward rational bound of approximately **1.4000438497**; the CI validator now explicitly asserts the exact rational inequality \(m>7/5\) across the entire band.

The proof is *continuous-frequency*, not a finite sampling extrapolation. Partition \(J_+\) into 128 rational equal-width intervals \([l_i,r_i]\). On each interval, the original quarter-digamma Euler series with the validated 128-term positive partial sum and monotone integral-tail lower bound gives a lower bound \(A(l_i)\) on the archimedean multiplier. SI06's full **original signed** seven-prime rational phase/cosine code bounds the prime multiplier at the midpoint \(x_i\). Using the certified \(|p'(\xi)|<69\) derivative, the all-point lower bound is
\[
\boxed{m(\xi)\ge A(l_i)+p_{\rm lower}(x_i)-\frac{69}{2}(r_i-l_i)>7/5}
\]
throughout each entire interval. Evenness covers \(J_-\). No negative odd-pole contribution is dropped; it is kept for the inverse-response comparison.

## 3. The physically supported positive reference is NOT a Fourier inverse

Let \(\mathcal F\) use the original \(e^{-2\pi i x\xi}\) convention, and let \(Z:L^2(I)\to L^2(\mathbb R)\) be zero extension. Define the physically supported *positive contraction*
\[
T_J:=Z^*\mathcal F^{-1}\mathbf1_J\mathcal F Z,\quad 0\preceq T_J\preceq I.
\]
Because \(a(\xi)\ge\kappa+\mathbf1_J(\xi)\) pointwise and the even positive pole is nonnegative,
\[
\boxed{A\succeq \kappa I+T_J}
\]
on the original positive supported form domain. **This is an operator lower reference bound**, not the false equality \(A^{-1}=Z^*\mathcal F^{-1}a^{-1}\mathcal FZ\).

Order reversal for positive inverses gives
\[
A^{-1}\preceq(\kappa I+T_J)^{-1}.
\]
Since \(T_J\) is a positive contraction, the scalar *convex-chord* bound valid for every \(0\le t\le1\),
\[
\frac1{\kappa+t}
\le\frac1{\kappa}-\frac{t}{\kappa(\kappa+1)}
\]
extends by continuous spectral functional calculus, yielding the exact **supported odd inverse bound**
\[
\boxed{
\langle s,A^{-1}s\rangle
\le\frac{\|s\|_2^2}{\kappa}
-\frac{1}{\kappa(\kappa+1)}
\int_J|\widehat{Zs}(\xi)|^2d\xi.
}
\]
This is stronger than SI12's odd scalar upper whenever the odd Fourier mass on \(J\) is positive.

## 4. Exact certified nonzero odd Fourier mass on the positive window

For \(s(x)=\sinh(x/2)\), the original two-sided Fourier transform is odd and purely imaginary. At the rational central frequency \(\xi_0=3/10\) define \(k=2\pi\xi_0=3\pi/5\). Then \(kB=33\pi/50=\pi/2+4\pi/25\) and direct elementary integration gives
\[
\left|\widehat{Zs}(\xi_0)\right|
=
\frac{2\left[
\frac12\cosh(B/2)\cos(4\pi/25)
+k\sinh(B/2)\sin(4\pi/25)
\right]}{1/4+k^2}.
\]
Using SI06's exact rational Machin enclosure of \(\pi\), SI12's rational \(\sinh,\cosh\) Taylor enclosures, and the valid lower bounds \(\cos t\ge1-t^2/2,\;\sin t\ge t-t^3/6\) for \(0\le t\le4\pi/25\), the verifier establishes
\[
\boxed{|\widehat{Zs}(3/10)|>0.54.}
\]
An elementary supported first-moment bound gives
\[
\left|\frac{d}{d\xi}\widehat{Zs}(\xi)\right|
\le2\pi\int_{-B}^B|x\sinh(x/2)|dx
=2\pi\left(4B\cosh(B/2)-8\sinh(B/2)\right)<3.
\]
Every \(\xi\in J_+\) lies within \(0.08\) of \(0.3\), so
\[
|\widehat{Zs}(\xi)|>0.54-3(0.08)=0.30.
\]
By the odd physical source's conjugation symmetry, \(|\widehat{Zs}(-\xi)|=|\widehat{Zs}(\xi)|\). Thus the **entire actual signed positive window** has a rigorously nonzero supported odd Fourier mass:
\[
\boxed{
\int_J|\widehat{Zs}(\xi)|^2\,d\xi
>2(0.38-0.22)(0.30)^2
=\frac{36}{1250}=0.0288.
}
\]
There is no sampling-based lower bound, no unsound phase interpolation, and no uncharged support loss.

## 5. New certified strictly improved supported odd response

Insert the previous mass lower into the positive contraction comparison:
\[
\boxed{
2\langle s,A^{-1}s\rangle
<
\frac{2(\sinh B-B)}{\kappa}
-\frac{2}{\kappa(\kappa+1)}
\left(\frac{36}{1250}\right)
<414.
}
\]
The strict value \(414\) is certified by rational enclosures, and is genuinely better than SI12's \(\approx471.3\) upper.

The initial successful CI replay returned a new odd-pole inverse upper bound of approximately **413.752482705896**, with a certified improvement greater than **57.54** over the scalar-only bound. This is *strict positive progress on the actual odd-sector supported inverse response*, not an extrapolation from an even positive pole. It does not by itself discharge the relevant pole's Birman–Schwinger threshold \(\le1\): the estimate is deliberately coarse, and a true inverse response may be much smaller. The \(414\) upper is **not** an actual eigenvalue, lower bound, or indication of a negative Weil direction.

The same construction can incorporate *several disjoint certified positive windows*; then their physically supported contraction remains \(0\preceq T_J\preceq I\), so the inverse comparison rewards the **combined odd Fourier mass** without paying new signed prime uncertainty.

## 6. Decision and SI14 frontier

The decisive structural observation is that positive Fourier windows can be turned into **true positive supported operator references** and can yield certified actual odd inverse-response upper bounds. This creates an analytic bridge between SI06/07 frequency positivity and SI11's supported inverse test that was missing in SI12.

However, no original trial vector \(y\approx A^{-1}s\) was computed; no exact original odd inverse response or residual Gram was certified; no full 1,631-feature Birman–Schwinger matrix spectral condition has been checked. The present rank-one comparison is not competitive with native RC signed high response.

**SI14:** aggregate multiple certified disjoint positive Fourier windows to increase odd Fourier mass and sharpen the supported inverse bound. Compare the resulting limit to the \(\le1\) odd-pole target. If this remains too large, proceed to genuine supported trial inverse responses with a rigorously positive residual Gram, rather than indefinitely sharpening a one-column inverse comparator. Preserve independent RC custody.

**No full original Weil positivity, Stage I closure, F4, Lean proof, or RH result is claimed.**

## Replay

\`python scripts/validate_rpb108_si13_odd_fourier_reference.py\`

Validator uses only rational SI06 original signed prime intervals, rational digamma series, exact original Fourier formula for the compactly supported odd pole, elementary operator spectral comparison, and exact original hyperbolic-function enclosures. The mathematical operator-order argument is analytic; the CI regression is not independent peer review or Lean formalization.
