# RPB108: direct Gaussian far-field estimate and boundary-collar localization

Base: research abde309157af63cbd93f6ffb78f54e7e3743a5d2.

## The direct estimate

Fix a>0 and d>0. Let h be supported in [-a,a] with finite logarithmic Fourier energy E_log(h), and let
\[
g_R=K_R*h,\qquad
K_R(x)=\frac{\sqrt R}{2\sqrt\pi}e^{-Rx^2/4+iRx},
\quad R\ge1.
\]
Choose a real smooth cutoff chi_out with 0<=chi_out<=1, equal to one on [-a-d/2,a+d/2] and supported in (-a-d,a+d). Define
\[
u_R^{\rm far}=(1-\chi_{\rm out})\overline{g_R}.
\]
For the genuine fixed-cutoff native action,
\[
|\mathcal A_a(h;u_R^{\rm far})|
 \le C_{a,d}R^{3/2}e^{-Rd^2/64}E_{\log}(h).
\tag{1}
\]
The constant is finite and also depends on the chosen fixed cutoff. It is independent of h and R.

This proves actual exponential control at every fixed positive separation from the physical support. No residual function, central-gap realization, H1 regularity of h or physical spectral operator domain is assumed.

## Terminology and test admissibility

**Separated far-field action:** the genuine fixed-cutoff action against u_far above. It is a test localization, not a change of source vector or multiplier cutoff.

**Boundary-collar action:** the action against (chi_out-chi_in) conjugate(g_R), where chi_in is a compact endpoint-interior cutoff defined below.

**Pole-admissible Gaussian cutoff test:** a Schwartz function obtained by multiplying conjugate(g_R) by one of the cutoffs here, for which the exponential pole product is proved absolutely integrable.

The multiplier core is a tempered functional. The pole contains exp(x/2) and exp(-x/2); it is not silently treated as a tempered functional defined on every Schwartz function. Gaussian decay proves weighted pole integrability for each whole-line test used here. Compact tests retain the previously certified integrability.

## A logarithmic action bound

Let w(xi)=log(e+|xi|), and let C_a>=0 satisfy the already proved native symbol envelope |m_a-w|<=C_a. For a Schwartz test u, the actual multiplier transpose identity gives
\[
\mathcal A_a^{\rm core}(h;u)
 =\int m_a(\xi)\widehat h(\xi)\widehat u(-\xi)\,d\xi.
\]
Since w>=1 and w is even,
\[
|\mathcal A_a^{\rm core}(h;u)|
 \le(1+C_a)\sqrt{E_{\log}(h)}\sqrt{E_{\log}(u)}.
\tag{2}
\]
This is weighted Cauchy-Schwarz, using |m_a|<= (1+C_a)w. It does not require m_a Fourier(h) to be L2.

There is an absolute finite constant C_F with
\[
E_{\log}(u)\le C_F\|u\|_{H^1(\mathbb R)}^2.
\tag{3}
\]
Indeed w(xi)<=C(1+xi^2), and Fourier differentiation and Plancherel apply to the smooth test u. H1 is used for this test only.

The actual physical pole is
\[
p_h(x)=M_-(h)e^{x/2}+M_+(h)e^{-x/2}.
\]
Its moments satisfy |M_pm(h)|<=sqrt(2a)e^(a/2)||h||_2. Hence
\[
|p_h(x)|\le2\sqrt{2a}e^{a/2}\|h\|_2 e^{|x|/2}.
\tag{4}
\]
A weighted L1 bound for u therefore controls the pole action directly.

## Gaussian tail and derivative bounds

From the exact kernel and
\[
K_R'(v)=(iR-Rv/2)K_R(v),
\]
there is an absolute C such that, for R>=1,
\[
|K_R(v)|\le C\sqrt R e^{-Rv^2/8},\qquad
|K_R'(v)|\le C R^{3/2}e^{-Rv^2/8}.
\]
For the second bound, absorb (1+|v|) into exp(Rv^2/8), uniformly for R>=1.

Put t=|x|-a for |x|>=a. Since |x-y|>=t on the support of h, convolution and ||h||_1<=sqrt(2a)||h||_2 give
\[
|g_R(x)|\le C_a\sqrt R\|h\|_2 e^{-Rt^2/8},\qquad
|g_R'(x)|\le C_a R^{3/2}\|h\|_2 e^{-Rt^2/8}.
\tag{5}
\]

Both u_far and its derivative vanish for |x|<a+d/2. On their remaining support t>=d/2, and
\[
e^{-Rt^2/8}\le e^{-Rd^2/64}e^{-Rt^2/16}.
\tag{6}
\]
The derivative of the fixed cutoff is bounded. Equations (5)--(6), integrated in L2, yield
\[
\|u_R^{\rm far}\|_{H^1}
 \le C_{a,d}R^{3/2}e^{-Rd^2/64}\|h\|_2.
\tag{7}
\]
One may bound the remaining Gaussian integrals by their R=1 values; no optimal power of R is needed.

Likewise,
\[
\int|u_R^{\rm far}(x)|e^{|x|/2}\,dx
 \le C_{a,d}\sqrt R e^{-Rd^2/64}\|h\|_2.
\tag{8}
\]
The remaining integral is bounded by a constant times
\[
\int_{d/2}^\infty e^{-t^2/16+t/2}\,dt<\infty.
\]
This proves genuine weighted pole integrability, as well as its estimate.

Combining (2), (3), (7) and (4), (8), then using ||h||_2<=sqrt(E_log(h)) and sqrt(R)<=R^(3/2), proves (1). The far test is Schwartz because g_R is Schwartz and 1-chi_out has bounded derivatives of all orders.

## Exact same-vector endpoint localization

Now suppose h is an actual endpoint weak-null vector at a:
\[
Q_a(v,h)=0\qquad(v\in D_a).
\tag{9}
\]
Fix 0<epsilon<a. Choose a real chi_in in C_c^\infty(-a,a), with 0<=chi_in<=1 and equal to one on [-a+epsilon,a-epsilon].

The test chi_in conjugate(g_R) is compact and its conjugate chi_in g_R belongs to D_a. The already proved native/compact-action dictionary and (9) give
\[
\mathcal A_a(h;\chi_{\rm in}\overline{g_R})=0.
\tag{10}
\]
Only this endpoint-interior term is killed. No larger central window is introduced.

Define
\[
C_R=\mathcal A_a\bigl(h;
 (\chi_{\rm out}-\chi_{\rm in})\overline{g_R}\bigr),\qquad
F_R=\mathcal A_a(h;u_R^{\rm far}).
\]
The collar test is compact, smooth and supported within [-a-d,a+d], and it vanishes on [-a+epsilon,a-epsilon]. It is not asserted to be an endpoint-domain test, because it can extend beyond [-a,a].

The partition of the test and additivity give exactly
\[
\mathcal A_a(h;\overline{g_R})=C_R+F_R.
\tag{11}
\]
All pole integrals are absolutely convergent by compactness or the proved Gaussian bounds, so this is genuine integral additivity. The physical h, its actual samples and the multiplier cutoff a are unchanged.

## The collar inherits the coercivity signal

The earlier actual moving-Gaussian estimate gives
\[
\Re\mathcal A_a(h;\overline{g_R})
 \ge(\log R-C'_a)M_R
 -D_a(1+\log R)e^{-R/4}\|h\|_2^2,
\]
where M_R=int exp(-(2pi xi-R)^2/R)|Fourier(h)|^2 and the supported window is c=a. Using (1) and (11),
\[
\Re C_R\ge(\log R-C'_a)M_R
 -D_a(1+\log R)e^{-R/4}\|h\|_2^2
 -C_{a,d}R^{3/2}e^{-Rd^2/64}E_{\log}(h).
\tag{12}
\]

Thus the Gaussian lower signal is carried by the genuine compact boundary-collar action, up to explicit exponential errors. No pointwise residual representative is needed.

If h!=0, the one-sided Gaussian theorem proves that C_R cannot satisfy any eventual estimate
\[
\Re C_R\le C(1+R)^p e^{-\delta R},
\qquad\delta>0,\ p\ge0,
\tag{13}
\]
for all sufficiently large real R. Indeed (13) plus (1) and (11) would give the forbidden eventual polynomial-times-exponential upper bound for the whole genuine action, forcing h=0.

This applies to every fixed choice of epsilon,d and cutoffs as above, however thin the collars are. No uniform constant as epsilon or d tends to zero is claimed. Nor is any lower estimate at every R claimed beyond (12); failure of (13) means arbitrarily large R violate it.

## The independent input is now localized

The separated far field is controlled, and endpoint-interior cancellation is lawful. Their combination leaves the compact collar action C_R. The remaining Gaussian null-exclusion route must derive an upper estimate for that genuine collar interaction, or use a different exclusion argument.

For a hypothetical nonzero endpoint mode, (13) is impossible. Therefore proving it from independent actual endpoint premises would exclude the mode; it is not a universal tail estimate available from compact support alone.

The canonical aperture theorem shows any finite first-contact mode reaches both support endpoints. The collar obstruction is consistent with that saturation: there is no fixed support gap to which the historical residual vanishing estimate could apply.

Nothing here asserts an actual endpoint mode exists, that the collar has a locally integrable residual representative, or that endpoint nullity alone supplies (13). No full-source unit domination, selected-background domination or RH conclusion follows.

## Validation and cursor

Analytic proof using explicit Gaussian kernel and first derivative bounds, supported L1/L2 control, the actual logarithmic symbol envelope, the compact-action dictionary and the previous one-sided Gaussian theorem. No new external input, Lean source/workflow change or CI claim. Certified code remains cb92c1b4dfca298cbc79d5b7d25598ea370236bf; Actions run 37236113125/job 111535430775.

At abde309, the genuine moving-Gaussian action splits into an endpoint-interior term, a compact boundary-collar action and a separated far-field action. For every supported logarithmic h and every fixed exterior separation d>0, direct kernel/derivative Gaussian bounds, the native log-symbol Cauchy-Schwarz estimate and separately verified weighted pole integrability prove |far_R|<=C_a,d R^(3/2) exp(-R d^2/64) E_log(h), without a residual representation or physical operator-domain membership. Endpoint weak-nullity kills only the compact interior test, giving exact same-vector action=collar+far. The actual coercivity bound transfers to the collar with only explicit exponential errors. For any nonzero endpoint-null vector, every fixed sufficiently thin collar consequently fails every eventual polynomial-times-exponential real-part upper bound; such a bound would force h=0 by the one-sided Gaussian theorem. This localizes the independent null-exclusion input to genuine boundary-collar cancellation/smallness, not remote tails, raw multiplicity, graph completion or a representation wrapper. Whole-line tests here have explicit weighted pole integrability; the exponentially growing pole is not treated as a generic tempered functional on all Schwartz tests. No actual endpoint existence, residual regularity, global unit bound or RH conclusion is asserted; Lean/CI unchanged and FULL TRANSPORT CLOSED remains open.
