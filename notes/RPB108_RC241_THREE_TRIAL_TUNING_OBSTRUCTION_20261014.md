# RPB108 — RC241: uniform three-trial coefficient-tuning obstruction

Date: 2026-10-14 UTC. Aperture B=11/10. Parent RC240: `4bb28eccb6610bf8765b9382de9309abb2512b4a`. Branch: research/rpb108-route-consolidation.

RC241 proves that coefficient tuning alone cannot close the signed gate using the present RC240 three-trial upper-bound formula. The obstruction covers every coefficient vector, rather than only the finite candidate list. It also certifies a positive distance from each actual original-action source to the corresponding three-trial augmented-action range.

These are limitations of the fixed trial/action certification interface. The upper-bound formula floor is **not a lower bound for the true inverse response**, and its negative signed-enclosure ceiling is **not a negative original Weil direction**. All RC240 response enclosures are preserved. No new complete actions or response sources are claimed. Stage I, full signed positivity, original positivity, RH, F4 and Lean remain open.

## Uniform lower envelope of the upper-bound formula

For either parity, let o be the retained degree-64 center of O=N0 P_base and A the three retained centers of N P_base, N P_(base+2), N P_(base+4). Let W_lower be the actual D-weight lower diagonal, m_n(H_n+s_lower). Define the exact rational quantities

\[
K=A^*W_{\rm lower}A,\quad b=A^*W_{\rm lower}o,
\quad c=o^*W_{\rm lower}o.
\]

Let F and Y be the midpoint matrices of the pinned original-form and frequency-Gram intervals, G=F+lambda Y, and f=F e0. These midpoint matrices define a bound on the certification formula; they are not substituted for the actual operators.

For any coefficient vector y, the RC240 variational-center upper enclosure is at least

\[
C_{\rm mid}(y)=2\operatorname{Re}(y^*f)-y^*Gy.
\]

The paid full residual-energy upper bound is at least the retained-center energy c-2 Re(y*b)+y*Ky. This follows because its actual-metric center energy uses weights at least W_lower and its nonnegative fault norm is added before squaring. With the unchanged global positive augmented floor mu, the resulting inverse-response upper formula therefore satisfies

\[
U_{\rm cert}(y)\ge
\frac c\mu+2\operatorname{Re}(y^*h)+y^*Hy,
\quad H=K/\mu-G,\quad h=f-b/\mu.
\]

The validator proves H positive definite exactly. Completing the quadratic yields a uniform formula floor

\[
\boxed{U_{\rm cert}(y)\ge
U_*:=c/\mu-h^*H^{-1}h}
\]

for all real and complex coefficient vectors. It records the exact minimizing vector -H^-1 h and verifies the completion identity at independent exact vectors. This minimizes the optimistic quadratic lower envelope, not the actual upper formula and not the actual inverse response.

The correlated signed-gap lower enclosure also cannot escape the obstruction. Its interval quadratic lower endpoints are at most their midpoint quadratic, and its residual upper bound is at least the retained-center energy. Thus, for u=e0-y,

\[
L_{\Delta,\rm cert}(y)
\le u^*Fu+\lambda y^*Yy
-\mu^{-1}(c-2\operatorname{Re}(y^*b)+y^*Ky)
\le F_{00}-U_*.
\]

Both final ceilings are negative. Therefore neither the inverse-upper route nor the correlated signed-lower route can establish positivity by choosing different coefficients within this fixed interface. Existing RC240 intersections also have negative lower endpoints and do not change that conclusion.

| Method diagnostic | Even | Odd |
|---|---:|---:|
| Uniform floor of current inverse-upper formula, rounded downward | 11.748777900 | 13.032409625 |
| Upper ceiling of current correlated signed-lower formula, rounded upward | -11.660218704 | -12.935326810 |
| Actual original source form upper, rounded upward | 0.088559197 | 0.097082816 |

Even an arbitrarily dense coefficient search cannot overcome this gap. Merely decreasing the action fault radii while leaving these centers, midpoint form matrices and global mu unchanged cannot overcome it either: the optimistic lower envelope already discarded those nonnegative fault contributions. A different trial space, better inverse correction, or a materially changed action/form representation is needed. This does not obstruct other valid certification methods.

## Positive distance for the actual action range

The validator also establishes a distinct statement about the actual complete actions, with all errors paid. Let

\[
y_{\rm ls}=K^{-1}b,\qquad d^2=c-b^*K^{-1}b>0.
\]

Then the retained-center residual satisfies

\[
\|o-Ay\|_{D_{\rm lower}}^2
=d^2+(y-y_{\rm ls})^*K(y-y_{\rm ls}).
\]

Choose sigma^2=1/trace(K^-1). Exact positive-semidefiniteness verifies K>=sigma^2 I. The full action error map has norm at most delta=sqrt(sum_i E_i), where E_i are the three pinned complete N-action squared errors. This uses the triangle/Cauchy bounds for error columns, not orthogonality. Let epsilon0 bound the complete original source fault norm. For t=||y-y_ls||,

\[
\|O-NVy\|_D
\ge\sqrt{d^2+\sigma^2t^2}-\delta t
-\epsilon_0-\delta\|y_{\rm ls}\|.
\]

Because delta<sigma, the first two terms have global minimum d sqrt(1-delta^2/sigma^2). Paying all square-root rounding gives strictly positive uniform actual residual floors:

| Actual three-trial residual statement | Even | Odd |
|---|---:|---:|
| D-norm lower, rounded downward | 0.072175905 | 0.062443208 |
| Squared D-energy lower, rounded downward | 0.005209361 | 0.003899154 |

This proves that the three augmented trial actions cannot exactly represent the original-action source, even after their certified full-output uncertainty is included. It does not imply a negative signed gap: the actual inverse weighting of that residual remains different from the optimistic or conservative formula diagnostics.

## Prepared residual-shaped trial proposals

For each parity, the certificate records the physical Legendre coefficients of o-A y_ls, rounded to the 10^-60 rational grid, together with a paid D-energy rounding bound. These are concrete finite polynomials targeted at the residual that the current action span does not remove.

Their complete original and augmented actions have **not** been certified in this pass, and they are not counted as new action inputs. Their action certification is a proposed next step. Other options include a stronger complementary augmented-inverse estimate. The obstruction indicates why another scalar tuning sweep on the same three polynomials would be insufficient.

## Verification and scope

The validator checks 158 pinned input/helper blobs. Exact replay reverses retained degree summations and requires equality with the stored certificate. Independent controls verify quadratic completion and the analytic robust-residual minimum. Every needed positive-definite or positive-semidefinite matrix comparison is checked using exact rational arithmetic.

Publication adds the validator, certificate and this note to RC240 while preserving existing repository blobs. The previous inverse-response upper bounds remain 23.389542374 even and 29.021020187 odd when rounded upward. The separate canonical eight-source metric-inverse width remains 485647/1000000.

The uniform tuning obstruction concerns the fixed RC240 degree-64 centers and midpoint interval formulas with their inherited global mu. It is not an impossibility theorem for the original Weil positivity problem, the full 639-dimensional signed criterion, or a richer response method. Complete signed positivity still requires the full 248-dimensional even and 391-dimensional odd parameter spaces, or an equivalent uniform proof.

Next: certify the prepared residual-shaped polynomial actions or replace the global residual inverse correction with a stronger valid estimate. Keep the complete signed criterion as the completion requirement.
