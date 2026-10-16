# RC321 — Quartic boundary cancellation on the original signed Weil carrier

**Parent:** merged RC320 at \`6e4c2b358ec47f83f5c22f4cd790c462fd80c596\`.  
**Carrier:** original CC27 signed Weil quadratic form, imported on its completed $D$-energy space from RC313.  
**Scope:** the entire original high-source action of one candidate third even low direction is certified, using 256 exact rational-center Legendre projections and rigorously charged infinite tails. A full $P_0/P_2/P_4$ three-dimensional Schur positivity statement is **not** made; nor is any Stage I, F4, Lean or RH closure claim.

## A third boundary-compatible even direction

RC320's key was the quadratic difference $P_2-P_0$, whose zero extension belongs to $H^1(\mathbb R)$. RC321 extends this *structural*, not merely numerical, advantage to

$$
F_4(t):=P_4(t)-P_2(t)
=\frac78(t^2-1)(5t^2-1).
$$

Let $u_n=\sqrt{(2n+1)/(2B)}P_n(x/B)$, $B=11/10$, and $v_n=u_n/\sqrt{s+H_n}$. In physical normalization the candidate new low vector is

$$
f_4=u_4-\frac3{\sqrt5}u_2
=\frac3{\sqrt{2B}}\,F_4(x/B),
$$

and its $D$-normalized counterpart is $w_4=f_4/\sqrt{s+H_4}$. This is a legitimate new independent even low direction alongside $P_0,P_2$.

The physical source satisfies **exactly**

$$
\|f_4\|_{L^2}^2=\frac{14}{5},\qquad
\|f_4'\|_{L^2}^2=\frac{63}{B^2},\qquad
f_4(-B)=f_4(B)=0.
$$

As a result, its zero extension lies in $H^1(\mathbb R)$ and the rigorous source-shift bound is

$$
\|T_{\ell+\delta}f_4-T_\ell f_4\|_2
\le \frac{\sqrt{63}}B|\delta|<\frac8B|\delta|.
$$

No spurious $\sqrt{|\delta|}$ edge cost is needed. This improves over treating the $u_4$ and $u_2$ sources separately.

## A uniform even-degree mechanism, not just the quartic instance

For any even $d\ge2$, put $F_d=P_d-P_{d-2}$ and $f_d=\sqrt{(2d+1)/(2B)}F_d(x/B)$. The endpoint identity $P_j(\pm1)=(\pm1)^j$ implies $F_d(\pm1)=0$. Since these are finite polynomials, their zero extensions belong to $H^1(\mathbb R)$ automatically. Orthogonality and the Legendre derivative identities give the **general exact norms**

$
\|f_d\|_2^2=\frac{2(2d-1)}{2d-3},\qquad
\|f_d'\|_2^2=\frac{(2d-1)(2d+1)}{B^2}.
$

In particular the high-mode endpoint coefficients satisfy the exact rational cancellation

$
\boxed{
E_{n,d}-E_{n,d-2}
=
\frac{2(2d-1)(2n+1)}
{(n-d)(n+d+1)(n-d+2)(n+d-1)}
}\quad(n>d,\ n\equiv d\pmod2).
$

Consequently every adjacent-even difference has a first-order $H^1$ prime translation estimate and a cubic-decaying high endpoint coefficient. These are **analytic algebraic identities at all degrees**, not numerical extrapolations from RC321's $d=4$ calculation.

This does **not** imply that a family of all adjacent-even differences automatically has a positive Schur matrix: the low signed Gram and its entire high cross-covariance still require independent certification.

## Complete native signed prime source

Retain **all seven original CC27 prime powers** and both zero-extended shifts (14 translations). In the dimensionless coordinate $t=x/B$, each translated polynomial is

$$
-\frac{\Lambda(m)}{\sqrt m}
F_4\bigl(t\pm \log(m)/B\bigr)
$$

on its true clipped support and zero outside. Their sum has 15 exact support segments, each a quartic rational-center polynomial. The validator integrates the *square of the full signed sum*, including every overlap/interference term, to obtain the complete physical prime mass.

For the even Legendre output $n=0,2,\ldots,510$, write

$$
A_n^{(4-2)}
=-(2n+1)\sum_m\frac{\Lambda(m)}{\sqrt m}
\int_{-1}^{1-\log(m)/B}
P_n(t)F_4\bigl(t+\log(m)/B\bigr)\,dt.
$$

The moments are reduced to at most five successive applications of the tridiagonal Legendre multiplication identity

$$
tP_k(t)=\frac{k+1}{2k+1}P_{k+1}(t)
+\frac{k}{2k+1}P_{k-1}(t),
$$

followed by exact rational evaluation of the Legendre antiderivative at a rational-center displacement. The calculation supports $n=0,2,4$ without artificial negative-degree integrals.

Two independent **self-adjointness consistency checks** reproduce the $P_0/P_4$ and $P_2/P_4$ original signed prime mixed entries from separately computed RC318 and RC319 coefficient arrays.

With the entire physical signed source norm and all 256 even projection coefficients paid in rational arithmetic, Parseval yields an outward rigorous **whole-infinite $n\ge512$ tail** rather than extrapolating from sample decay. The uncertain true prime logarithms, square-root weights and translating support boundaries are paid globally by the compact-support $H^1$ norm above.

## Exact cancellation of the original endpoint asymptotic

The canonical original logarithmic endpoint coefficients obey

$$
E_{n,d}=\frac{2n+1}{(n-d)(n+d+1)}
\quad(n>d,\ n\equiv d\pmod2).
$$

Therefore for the independent quartic direction

$$
\boxed{
E_{n,4}-E_{n,2}
=\frac{14(2n+1)}
{(n-4)(n+5)(n-2)(n+3)}
}\qquad(n\ge244,\ n\text{ even}).
$$

The nominal leading $1/n$ endpoint tail **cancels algebraically**, leaving order $n^{-3}$. All remaining high endpoint energy above degree 510 is paid analytically using an exact all-degree telescoping identity from RC318.

The pinned 192-degree RC46 regular-kernel Taylor polynomial, acting on a quartic source, produces a polynomial of degree at most 197. Every high projection $n\ge244$ of that regular polynomial therefore vanishes exactly, and the full regular-kernel analytic error is paid by operator norm. The signed even-pole high tail is independently bounded geometrically.

## What this checkpoint does—and does not—show

RC321 merges the finite degree-244-through-510 **original signed endpoint+prime combined** source energy and the complete infinite complementary source norm, charging the global displacement/weight error once. It is an actual full-high $D$ response bound for the **new independent** low vector $w_4$. The full third-column source, not just a few principal matrix elements, is brought into the same canonical representation as RC318 and RC320.

The validated outward rational enclosure has the following scale:

| Quantity | Guaranteed upper bound |
|---|---:|
| Complete original signed prime-source physical $n\ge512$ Parseval tail, squared | $<3.863092\times10^{-7}$ |
| Pinned-logarithm signed translation/weight physical $L^2$ uncertainty | $\le10^{-25}$ |
| Full original combined finite high $D$-energy, degrees 244–510 | $<7.314163\times10^{-8}$ |
| Full original $D$-high response norm $\|Tw_4\|_D$ | $<2.816560\times10^{-4}$ |
| **Full original high-response energy $\|Tw_4\|_D^2$** | **$<7.933010\times10^{-8}$** |

The $D$-high response bound is calculated for the original signed *combined* polynomial direction and covers **all** even high coordinates, not merely degrees through 510. Its raw bound is substantially smaller than RC319's separate $P_2$ response, although RC320's quadratic difference has a still smaller high output.

However, a small high response is **not yet** a certificate of a positive $3\times3$ Schur form. That requires the full **original signed low $P_0/P_2/P_4$ matrix**, its cross-covariance with the existing positive two-dimensional block, and a strict Loewner/Schur determinant.

**RC322 next:** compute the original signed low matrix involving $P_4$, then combine that low Gram with the complete certified $w_4$ high response and RC320's two-dimensional Schur block; explicitly pay the off-diagonals and test a true positive three-dimensional determinant. The remaining even and odd dimensions remain open.

## Reproduce

\`\`\`bash
python scripts/validate_rpb108_rc321_p4_boundary_native.py --output certificates/rpb108_rc321_p4_boundary_native.json
python scripts/validate_rpb108_rc321_p4_boundary_native.py --output certificates/rpb108_rc321_p4_boundary_native.json --replay
\`\`\`

This checkpoint neither settles the full rank-317 Schur positivity condition nor the Riemann hypothesis.
