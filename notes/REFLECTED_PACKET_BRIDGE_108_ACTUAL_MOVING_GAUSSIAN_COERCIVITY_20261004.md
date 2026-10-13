# RPB108: actual moving-Gaussian logarithmic coercivity

Base: research 84015ec0f6ba107371ae9afbbd2a40649e36de11.

## Unconditional lower estimate

Fix 0<c<=a and let h be a complex L2 vector supported in [-c,c] with finite logarithmic Fourier energy. For R>=1 use the exact project moving Gaussian with normalization Ck=1/(2sqrt(pi)):
\[
K_R(x)=\frac{\sqrt R}{2\sqrt\pi}
 \exp(-Rx^2/4+iRx),\qquad g_R=K_R*h.
\]
Define
\[
\beta_R(\xi)=\exp(-(2\pi\xi-R)^2/R),\qquad
M_R=\int\beta_R(\xi)|\widehat h(\xi)|^2\,d\xi.
\]

There are explicit finite constants C'_a,D_a,c, depending only on the fixed windows and the certified native logarithmic error, such that the genuine full frozen action satisfies
\[
\Re\mathcal A_a(h;\overline{g_R})
 \ge(\log R-C'_a)M_R
 -D_{a,c}(1+\log R)e^{-R/4}\|h\|_2^2.
\tag{1}
\]
For log R>=C'_a this implies
\[
\Re\mathcal A_a(h;\overline{g_R})
 \ge(\log R-C'_a)\|g_R\|_2^2
 -D_{a,c}(1+\log R)e^{-R/4}\|h\|_2^2.
\tag{2}
\]

This is an actual F4 logarithmic Gaussian lower estimate proved independently of the obstructed central-null transport. It does not assert a residual upper estimate or FULL TRANSPORT CLOSED. The staged F4 entry prerequisites remain unclosed.

## Actual Gaussian frequency and admissibility

The physical project kernel is a Gaussian times the oscillatory phase exp(iRx), as documented in NeutralGaussianSchwartzSeed. The Gaussian Fourier integral gives exactly
\[
\widehat K_R(\xi)=\beta_R(\xi).
\]
It is a nonnegative real multiplier, centered at xi=R/(2pi), with frequency width of order sqrt(R). It is not an approximate identity as R tends to infinity.

Because h is compactly supported L1, g_R is Schwartz. For every derivative and polynomial weight, differentiate K_R under convolution and use its Schwartz bounds with y in the compact support of h. Hence conjugate(g_R) is a genuine Schwartz test for the tempered action.

The actual symbol premise was proved analytically in the previous record. Thus the action on this noncompact Schwartz test is defined directly, without extending a compact residual representation. Bilinear Plancherel and the same complex pole dictionary give
\[
\mathcal A_a(h;\overline{g_R})
 =\int m_a(\xi)\beta_R(\xi)|\widehat h(\xi)|^2\,d\xi
  +\overline{M_-(g_R)}M_+(h)
  +\overline{M_+(g_R)}M_-(h).
\tag{3}
\]
Here m_a is the actual threshold-corrected native symbol and M_\pm are the physical moments at s=+/-1/2.

The spectral integral is absolutely convergent: |m_a|<=w+C_a and 0<=beta_R<=1, while h has finite logarithmic energy. All pole moments exist; Gaussian decay also makes the filtered moments absolutely integrable. No assertion that m_a Fourier(h) is L2 is used.

Equation (3) is a direct action/form computation. It does not assert that g_R belongs to D_a: the filtered vector has whole-line support. The supported form operator A_a is not applied to g_R by fiat.

## Exact moving-Gaussian pole contribution

For real s, direct Gaussian integration yields
\[
\int K_R(x)e^{sx}\,dx
 =\exp(-R+s^2/R+2is).
\]
Fubini is justified by compact h and Gaussian decay, and hence
\[
M_s(g_R)=\exp(-R+s^2/R+2is)M_s(h).
\]
Put d_R=exp(-R+1/(4R)). At s=+/-1/2 the two factors are d_R exp(+/-i). Therefore the pole term in (3) is the real number
\[
2d_R\Re\left(e^i\overline{M_-(h)}M_+(h)\right).
\]
It has absolute value at most 2d_R|M_-(h)||M_+(h)|.

On [-c,c], Cauchy-Schwarz gives
\[
|M_\pm(h)|\le\sqrt{2c}\,e^{c/2}\|h\|_2.
\]
Consequently
\[
|\operatorname{pole\ term}|
 \le4c e^c e^{-R+1/(4R)}\|h\|_2^2.
\tag{4}
\]
This keeps the exact complex phase and Hermitian cross moments. No unconjugated product or even-real carrier shortcut is substituted.

## Logarithmic multiplier lower estimate

Let C_a>=0 be any certified error bound
\[
|m_a(\xi)-w(\xi)|\le C_a,\qquad
w(\xi)=\log(e+|\xi|).
\]
Set
\[
C'_a=C_a+\log(4\pi)+1.
\]
Split frequencies into H_R={|xi|>=R/(4pi)} and its complement L_R.

On H_R,
\[
m_a(\xi)\ge w(\xi)-C_a
 \ge\log R-\log(4\pi)-C_a
 \ge\log R-C'_a.
\]
On L_R, m_a>=-C_a and |2pi xi-R|>=R/2, so
\[
0\le\beta_R(\xi)\le e^{-R/4},
\quad
\int_{L_R}\beta_R|\widehat h|^2
 \le e^{-R/4}\|h\|_2^2.
\]
For L=log R-C'_a, it follows that
\[
\int m_a\beta_R|\widehat h|^2
 \ge L M_R-(|L|+C_a)e^{-R/4}\|h\|_2^2
 \ge L M_R-(\log R+C'_a+C_a)e^{-R/4}\|h\|_2^2.
\tag{5}
\]
These inequalities hold also when L is negative; no eventual positivity is silently used in (1).

For R>=1, the pole bound (4) is at most
\[
4c e^{c+1/4}e^{-R/4}\|h\|_2^2.
\]
Thus a permissible constant is
\[
D_{a,c}=1+C'_a+C_a+4c e^{c+1/4}.
\]
Combining (3)--(5) proves (1).

Plancherel gives ||g_R||_2^2=int beta_R^2|Fourier(h)|^2<=M_R. When L>=0, replacing M_R by this smaller squared norm proves (2). If h!=0 then M_R>0 because beta_R is strictly positive everywhere.

## What retaining the residual does and does not buy

This lower estimate uses the actual action itself. It neither discards the enlarged residual nor requires that action to vanish throughout a larger central window. The finite-selection and strict-margin obstructions are therefore respected.

To turn it into exponential control of M_R, one would still need an independent upper estimate for
\[
\mathcal A_a(h;\overline{g_R}).
\]
For example an independently proved upper bound of exponential order would combine with (1) to control moving Gaussian Fourier mass. That upper bound is not asserted here.

Endpoint nullity annihilates tests in the endpoint domain. The whole-line g_R is not such a test. The preceding obstruction proves that a nonzero endpoint vector cannot be made null on a larger window merely by inclusion. Therefore the previous strict-gap residual upper estimate cannot be imported for the genuine residual without its vanishing hypothesis.

The interface NeutralIntegralGrowthResidual explicitly demands a residual which vanishes on (-a,a) with c<a. A nonzero same-vector actual whole-action realization of that interface would imply the impossible central gate. Retaining a nonzero collar residual is lawful, but that residual does not meet the interface's vanishing field, so its Gaussian estimate is not available automatically.

No quantitative smallness of the genuine collar action, residual regularity, or F5 strip-holomorphy conclusion follows from the present lower bound alone. This is a substantive standalone coercivity theorem, not a completed transport package.

## Validation and cursor

Analytic proof from the exact project Gaussian, certified native logarithmic symbol bound, actual pole moments and the preceding analytic temperate-symbol dictionary. No new external arithmetic input. No Lean source/workflow changes or new CI claim. Existing certified code remains cb92c1b4dfca298cbc79d5b7d25598ea370236bf, Actions run 37236113125/job 111535430775.

At 84015ec, the actual normalized moving Gaussian K_R(x)=sqrt(R)/(2sqrt(pi)) exp(-R x^2/4+iRx) has Fourier multiplier beta_R(xi)=exp(-(2pi xi-R)^2/R). For every supported logarithmic h, its filtered mode g_R is Schwartz and the genuine frozen action on conjugate(g_R) equals the exact multiplier/pole pairing without a residual realization. The native log envelope, a split at |xi|=R/(4pi), and exact pole moments prove Re action >=(log R-C'_a) M_R-D_a,c(1+log R) exp(-R/4)||h||^2, M_R=int beta_R|Fourier h|^2. For large R this also controls (log R-C'_a)||g_R||^2. This is an unconditional analytic F4 Gaussian lower estimate on the actual carrier, independent of the obstructed same-vector central-null transport. The remaining issue is an independent upper estimate for the genuine nonzero residual action; endpoint nullity does not supply the old strict-gap exponential upper bound. No residual regularity/realization or F5 input is assumed. Lean unchanged; FULL TRANSPORT CLOSED and staged F4 entry remain open, though this standalone coercivity estimate is proved.
