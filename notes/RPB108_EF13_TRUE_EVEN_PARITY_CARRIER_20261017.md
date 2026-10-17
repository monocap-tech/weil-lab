# EF13 — Explicit *original* parity-even SI10 cofinite carrier

**Obligation:** W-EVEN-FORM (P2), not a replacement for P1 W-ODD-NEG.  
**Baseline:** original CC27 signed archimedean + all seven prime-power
frequencies, physically supported in \(I=[-11/10,11/10]\).
**Not asserted:** finite original signed PSD, complete even positivity,
original-zeta attachment or RH.

## Advance beyond EF12

EF12's exact Schur formula assumed an explicit carrier \(V\) and a
positive original signed complement lower bound. EF13 now **instantiates
these two geometric objects from SI10**, rather than leaving both as
free hypotheses. Nothing in EF13 evaluates the unsolved Schur block.

SI10's 973 unresolved positive-frequency dyadic leaves form 107
disjoint rational clusters \(J_j=[a_j,b_j]\), each with center
\(c_j=(a_j+b_j)/2>0\). The original signed multiplier satisfies
\(m(\xi)\ge\kappa=1/1000\) on every positive-frequency complement
and its reflected copy, including the infinite exterior.
Inside the cover the original signed deficit is bounded by the
outward rational heights from SI10/SM10. This is a bound on an
**error**, NOT a substitute \(K_{\mathrm{cap}}\) whose domination
is required for full positivity.

For each cluster define
\[
p_j=\min\{p\ge1:
 [\pi_{\rm up}B(b_j-a_j)]^p/p!<2^{-24}\}.
\]
The exact source replay verifies \(\sum_{j=1}^{107}p_j=890\).

Define the physical EVEN Taylor columns, for \(0\le k<p_j\):
\[
\boxed{
u^{(e)}_{jk}(x)=\mathbf1_I(x)
\frac{(2\pi x)^k}{k!}
\cos\left(2\pi c_j x+\frac{k\pi}{2}\right).
}
\]
Each is even: for even k it is an even monomial times an even cosine,
and for odd k an odd monomial times an odd sine.
The reflection of the original frequency interval is **automatically
encoded** by cosine parity, so it contributes no second independent
even column. The original negative odd pole
\(\sinh(x/2)\) does not occur in the even sector.
The original positive even pole
\(+2|\langle f,\cosh(x/2)\rangle|^2\)
is retained throughout \(q_e\) and can only help positivity.

Let \(V_e=\operatorname{span}\{u^{(e)}_{jk}\}\).
The 107 distinct nonzero frequencies give linearly independent
real exponential polynomials: expanding each into
\(e^{\pm2\pi ic_jx}\) with polynomial coefficients and applying
the standard uniqueness theorem for exponential polynomials shows
that a linear combination vanishing on the open interval has all
coefficients zero. Thus \(\dim V_e=890\).

The columns lie in the natural original signed form domain:
they are compactly supported piecewise \(C^1\) with bounded
variation, hence \(\widehat u(\xi)=O((1+|\xi|)^{-1})\)
for each fixed column. The original multiplier grows
at most logarithmically on the infinite exterior, so the positive
form-weighted Fourier integral is finite. This explains
form-domain inclusion analytically; a fully machine-checked
domain attachment is still outstanding.

## Original signed cofinite lower certificate

For \(f\in V_e^\perp\) with \(f\) even, Taylor approximation to
\(\cos(2\pi\xi x)\) around the same \(c_j\) gives a uniform error
\(\epsilon=2^{-24}\) over every whole original cluster and
therefore on every unresolved leaf. With Cauchy--Schwarz,

\[
|\widehat f(\xi)|^2
\le 2B\epsilon^2\|f\|_2^2\qquad
(\xi\text{ in the complete reflected cover}).
\]

Write the original SI10/SM10 exactly rational
full-reflection width \(W=973/32\),
and uncertain-cap mass
\(T=M_{\rm neg}+\kappa W<38\).

Plancherel, the original signed multiplier outside the
cover, the certified inside-cover lower, and the nonnegative even
pole yield

\[
\begin{split}
q_e(f,f)
&\ge\kappa\|f\|_2^2
-2B\epsilon^2(\kappa W+M_{\rm neg})\|f\|_2^2\\
&=\boxed{\gamma_e\|f\|_2^2},\\
\gamma_e&=\kappa-2B\,T\,2^{-48}>0.000999.
\end{split}
\]

This is an **actual signed ORIGINAL even-sector** cofinite coercivity
claim, inherited from SI10's whole-frequency analytic proof and
replayed with exact 24-bit rational inputs by EF13.

The contrast with EF10 matters: EF10 refuted domination by the
pessimistic conservative cap on ALL even vectors; it does not
contradict SI10/EF13 using its valid *small leakage* on the
orthogonal complement of an explicit source span.

## EF12 composition — exact remaining finite obligation

Now use the concrete \(V_e\) and
\(W_e=V_e^\perp\cap\mathcal D_e\).
Under original-form closure and domain hypotheses, SI10's
coercivity provides the Riesz complement inverse required by EF12.
The unsolved finite **890-dimensional** exceptional Schur test is

\[
S_e=A_e^{\rm signed}-B_e^{*}C_e^{-1}B_e
\succeq0.
\]

No unsupported numerical inverse is accepted. As EF12 showed,
an original-form forward solver with full complement energy-dual
residuals \(\rho_i\) suffices if it gives

\[
M_e-\left(\sum_{i=1}^{890}\rho_i^2\right)I_{890}\succeq0.
\]

**Next original obligations:** exact parity carrier normalized Gram /
coordinate transform; full signed 890×890 exceptional matrix entries;
original form-domain closure; original mixed forward residual lifts
and their infinite-complement dual norms; an exact Schur PSD.

**No EF06 false conservative-cap inversion should be resumed.**
