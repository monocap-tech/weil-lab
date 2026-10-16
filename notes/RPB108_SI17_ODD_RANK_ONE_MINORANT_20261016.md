# RPB108 SI17 — an explicit rank-one odd physical concentration minorant for the original signed supported inverse

**Parent:** integrated SI16 \`3677bfbb681e39e270378a26c41c7bd42656c63f\`.  
**Front:** independent Structural Investigation, not a replacement of the more compact native RC334/RC335 signed Schur route.  
**Status:** a precise physically supported **rank-one positive lower-reference** and full operator-norm remainder, yielding a stronger upper bound for the original odd supported Birman–Schwinger response. **Not** an original trial inverse vector, full signed residual Gram, or positivity of the complete original Weil form.

## 1. Distinguishing three levels of information

The original CC27/RC312–313 signed Weil form was decomposed in SI11 as
\[
Q[f]=\mathfrak a[f]-\langle f,Kf\rangle,\quad
A\ge\kappa I,\quad \kappa=1/1000,
\]
where the positive supported operator \(A\) arises from \(a(\xi)=\max\{m(\xi),\kappa\}\), includes the positive even pole \(2|\cosh(x/2)\rangle\langle\cosh(x/2)|\), and the negative operator \(K\) includes the original odd pole \(2|s\rangle\langle s|\), \(s(x)=\sinh(x/2)\).

SI14 showed a **no-go for one specific scalar inverse chord using the coarse concentration bound \(T_J\preceq I\)**. SI16 used odd parity and the exact time–bandwidth trace to prove the stronger odd operator endpoint \(T_J\preceq0.017 I\), reducing the certified upper on the fixed original odd pole response from \(412.562\) to \(77.684\).

SI17 instead approximates **the physical operator \(T_J\)** by a single explicit original-frequency odd sine direction, with **a rigorous operator-norm error across every odd physical input**. This produces a **positive rank-one Loewner minorant** of the actual \(A_{\mathrm{odd}}\), not a false whole-line inverse.

## 2. Original signed positive continuum and physical odd concentration feature

Inherit and replay SI13's original all-point signed multiplier theorem for
\[
m(\xi)=\operatorname{Re}\psi(1/4+i\pi\xi)-\log\pi
-2\sum_{n\in\{2,3,4,5,7,8,9\}}
\frac{\Lambda(n)}{\sqrt n}\cos(2\pi\xi\log n),
\]
where the full seven signed prime-power coefficients use the original base-prime logarithms:
\[
m(\xi)>\frac75=1.4\quad
(\xi\in[0.22,0.38]\cup[-0.38,-0.22]).
\]
This statement is supplied by SI13's exact rational Euler digamma and signed cosine intervals, not pointwise sampling. Set
\[
c=\frac3{10},\quad r=\frac1{125},\quad
J_\pm=\pm[c-r,c+r]=\pm[0.292,0.308],
\quad \delta=\frac{1399}{1000}.
\]
Then \(a(\xi)\ge\kappa+\delta\) throughout \(J=J_+\cup J_-\).

On the original *odd physical* Hilbert space \(H_o\subset L^2([-B,B])\), \(B=11/10\), let \(h_\xi(x)=\sin(2\pi\xi x)\) and \(h=h_c\). Since the reflected frequency features coincide on odd inputs,
\[
\boxed{
T_{J,o}
=2\int_{c-r}^{c+r}|h_\xi\rangle\langle h_\xi|\,d\xi.
}
\]
This identity is on the **physically supported carrier**, with the entire reflected Fourier window and no improper frequency projection of the physical input.

## 3. New dimension-independent rank-one operator-norm enclosure

Set \(F(\xi)=|h_\xi\rangle\langle h_\xi|\). As a bounded-operator-valued twice-differentiable function,
\[
F''(\xi)=|h''_\xi\rangle\langle h_\xi|
+2|h'_\xi\rangle\langle h'_\xi|
+|h_\xi\rangle\langle h''_\xi|.
\]
The exact supported moment bounds
\[
\begin{split}
\|h_\xi\|_2^2&\le2B,\\
\|h'_\xi\|_2^2&\le(2\pi)^2\,\frac{2B^3}{3},\\
\|h''_\xi\|_2^2&\le(2\pi)^4\,\frac{2B^5}{5}
\end{split}
\]
and \(\sqrt5>2,\ \pi<22/7\) imply, **uniformly for all real frequencies**,
\[
\|F''(\xi)\|
\le\frac{10}{3}(2\pi)^2B^3
<C:=\frac{10}{3}\left(\frac{44}{7}\right)^2B^3.
\]
Taylor's theorem in operator norm and symmetry of \([-r,r]\) show the linear term cancels after integration, leaving a *cubic* (rather than quadratic) band-width remainder:
\[
\begin{aligned}
\left\|T_{J,o}-4r|h\rangle\langle h|\right\|
&\le
2\int_{-r}^r\frac{C}{2}t^2\,dt\\
&=\boxed{\frac{2Cr^3}{3}=:\varepsilon<\frac1{16000}.}
\end{aligned}
\]
This is a **whole-operator** certificate valid for all odd supported inputs, not a numerical fit to a few Fourier samples. In particular,
\[
\boxed{
A_o\succeq\kappa I+\delta T_{J,o}
\succeq\kappa' I+\gamma|h\rangle\langle h|,
}
\quad
\kappa'=\kappa-\delta\varepsilon>\frac9{10000},
\quad \gamma=4r\delta>0.
\]

## 4. Exact inversion of the *reference*, not of the original operator

The rank-one Sherman–Morrison formula is **exact for the physically supported reference operator**
\[
C_o=\kappa'I+\gamma|h\rangle\langle h|,
\]
whose inverse is
\[
C_o^{-1}=\frac1{\kappa'}I-
\frac{\gamma}{\kappa'(\kappa'+\gamma\|h\|_2^2)}
|h\rangle\langle h|.
\]
Original supported form order and inverse monotonicity give \(A_o^{-1}\preceq C_o^{-1}\).

Three exact-rational physical quantities pay the resulting upper bound:

* \(\|s\|_2^2=\sinh B-B<235648/10^6\), inherited with the original SI12 \(\sinh\)-Taylor outward enclosure.
* \(|\langle s,h\rangle|=|\widehat{Zs}(c)|>541/1000\), replayed with the exact SI13 original Fourier integral, rational Machin \(\pi\) and hyperbolic Taylor bounds.
* \(\|h\|_2^2=B-\sin(4\pi c B)/(4\pi c)
=B+\sin(8\pi/25)/(4\pi c)<133/100\). The last bound is certified by the alternating rational sine polynomial \(t-t^3/6+t^5/120\) and rigorous \(\pi\) enclosure, not a floating-point trigonometric evaluation.

Therefore
\[
\begin{aligned}
2\langle s,A_o^{-1}s\rangle
&\le2\left(
\frac{\|s\|_2^2}{\kappa'}
-\frac{\gamma|\langle s,h\rangle|^2}
{\kappa'(\kappa'+\gamma\|h\|_2^2)}
\right)\\
&<\boxed{42}.
\end{aligned}
\]
The exact rational regression enforces the strict bound. The displayed bound is about the *original odd inverse quadratic response* \(2\langle s,A_o^{-1}s\rangle\), **not a value the inverse actually attains**.

## 5. What SI17 does and does not resolve

This recovers a useful **support-preserving finite-dimensional positive reference**, including its complete operator-norm residual. It cuts the previous best certified odd-pole inverse upper by almost half (\(<78\) to \(<42\)) and provides the core construction for a multi-feature Woodbury model.

However, **42 is still far above the threshold 1** needed to certify the odd pole alone, and the full signed-frequency negative operator \(Z^*\mathcal F^{-1}r\mathcal FZ\) remains. SI17 does **not** compute a genuine vector \(A^{-1}s\), an original \(A\)-operator residual, any SI11 finite Birman–Schwinger matrix spectrum, original whole-form positivity, Stage I/F4, Lean formalization, or RH.

### SI18

Introduce a second or additional distinct **original signed-positive odd Fourier directions** and construct a small positive physical reference
\[
C_{o,N}=\kappa' I+\sum_{j=1}^N\gamma_j|h_{c_j}\rangle\langle h_{c_j}|
\]
with all concentration-operator Taylor remainders and cross-covariances rigorously paid. Certify the actual finite physical Gram \(\langle h_{c_i},h_{c_j}\rangle\), the \(\langle s,h_{c_j}\rangle\) overlaps and a **correct-sign Woodbury inverse upper**. Compare any improvement against SI17's certified \(<42\), as well as the still smaller native RC high Schur. If the increasingly complicated SI inverse route remains far from \(1\), stop optimizing it as a surrogate for the full RC problem.

## Reproduction

\`python scripts/validate_rpb108_si17_odd_rank_one_minorant.py\`

Exact Python \`Fraction\` inequalities and the original signed SI13 all-frequency window proof are replayed by GitHub Actions structural CI. Operator-order and Banach-space Taylor steps are analytic inputs and are not claimed to be Lean formalizations or independent peer review.
