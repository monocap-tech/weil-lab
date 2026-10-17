# RPB108 EF01 — original even-sector parity compression and inverse gate

**Obligation:** W-EVEN-FORM; explicitly scoped local work, while canonical W-ODD-NEG remains active.
**Parent:** research/rpb108-route-consolidation at 8e39fd4f12d6f3c504d9d4f23ff95948b5608782.
**Standing:** analytic parity and supported-inverse reduction depending on certified SI10–SI11 original signed cover, plus exact-rational rank/error regression. The finite original even gate remains **OPEN**; no whole-even, whole-Weil, global-bridge or RH proof.

## 1. The original even form

On H_e = L²([-B,B])_even, B=11/10, with physical zero extension Z, write
\[
Q_e(f)=\int_{\mathbb R}m(\xi)|\widehat{Zf}(\xi)|^2\,d\xi
       +2|\langle f,c\rangle|^2,\qquad c(x)=\cosh(x/2),
\]
where the **original signed** multiplier is
\[
m(\xi)=\Re\psi(1/4+i\pi\xi)-\log\pi-
 2\sum_{n\in\{2,3,4,5,7,8,9\}}\frac{\Lambda(n)}{\sqrt n}
 \cos(2\pi\xi\log n).
\]
The negative odd pole s=sinh(x/2) vanishes by parity; the positive even pole stays.

For κ=1/1000 let a=max(m,κ), r=(κ-m)_+, and
\[
A_{0,e}=Z^*\mathcal F^{-1}a\mathcal F Z|_{H_e}\succeq\kappa I,\quad
K_e=Z^*\mathcal F^{-1}r\mathcal F Z|_{H_e}\succeq0,\quad
A_e=A_{0,e}+2|c\rangle\langle c|.
\]
Thus Q_e=A_e-K_e on the **physically supported** form domain. Neither operator inversion nor the form is replaced by an unrestricted Fourier reciprocal. SI10/11 give original signed cover constants
\[
W=973/32,\quad M=1203060883/32000000,\quad
R=M+\kappa W=1204033883/32000000<38,\quad\int r\le R.
\]

## 2. Even parity-halved packet

Use SI10's 107 positive-frequency uncertainty clusters J_j, centers c_j,
and original Taylor orders p_j(b). The even projection of reflected physical
modulated columns is
\[
q^e_{jk}(x)=\Pi_e(e^{2\pi i c_jx}x^k)
=\tfrac12(e^{2\pi i c_jx}+(-1)^k e^{-2\pi i c_jx})x^k,
\quad 0\le k<p_j(b).
\]
For even k it equals x^k cos(2πc_jx); for odd k it is
i x^k sin(2πc_jx). Both are even, and reflected pairs produce only
one even column each; no linear independence is assumed.

Let W_{b,e}=span{q^e_jk} within H_e and let P_{b,e} be its orthogonal
projection. Then
\[
\boxed{\dim W_{b,e}\le\sum_{j=1}^{107}p_j(b).}
\]
Unlike the odd case there is **no extra negative-pole vector**.
An even f orthogonal to W_{b,e} is orthogonal to SI10's complete reflected
Taylor span; it is automatically orthogonal to the odd pole s.
Hence the *complete original signed* SI10 cofinite estimate holds:
\[
\boxed{Q_e(f)\ge
[\kappa-2B(\kappa W+M)2^{-2b}]\|f\|_2^2.}
\]
For b=9 the even exceptional codimension is at most **469** and
the original entire even form satisfies Q_e(f)>0.00068||f||² on
its orthogonal complement. Under the standard closed-form realization,
the even negative index is at most 469. This **does not** prove
positivity on the omitted finite block or its cross-couplings.

## 3. Full original negative-frequency approximation

Define h^e_ξ=Π_e(e^{2πiξx} 1_I). The original continuous negative
operator is
\[
K_e=\int_{\mathbb R} r(\xi)|h^e_\xi\rangle\langle h^e_\xi|\,d\xi.
\]
The SI10 Taylor remainder survives even projection with
||(I-P_{b,e})h^e_ξ|| ≤ √(2B) 2^{-b} throughout the certified cover.
Together with ||h^e_ξ||≤√(2B), this yields
\[
\boxed{\|K_e-P_{b,e}K_eP_{b,e}\|\le\eta_b=4BR\,2^{-b}},
\quad
\boxed{\|(I-P_{b,e})K_e(I-P_{b,e})\|\le2BR\,2^{-2b}}.
\]
All reflected bands, the full signed negative multiplier, and
the complete infinite continuum residual are retained.

| Taylor bits b | SI11 full rank bound | even rank ceiling | η_b/κ upper |
|---:|---:|---:|---:|
| 9 | 939 | 469 | <323.349 |
| 10 | 1003 | 501 | <161.675 |
| 12 | 1121 | 560 | <40.419 |
| 16 | 1367 | 683 | <2.527 |
| 20 | 1561 | 780 | <0.157886 |
| 21 | 1631 | 815 | <0.078943 |
| 24 | 1781 | 890 | <0.009868 |
| 32 | 2151 | 1075 | <0.000038547 |

The small-b coarse inverse-norm gate is vacuous, even while the
SI10 *quadratic* complement estimate is positive. RC314's tighter
301-dimensional localization is in a **different** native metric;
no unproved transport between these carriers is assumed.

## 4. Exact positive-even-pole correction and remaining finite gate

Set R_e f = sqrt(r) Fourier(Zf), so K_e=R_e* R_e.
Original even positivity is equivalent to the exact operator gate
\[
\boxed{R_e A_e^{-1}R_e^*\preceq I.}
\]
The supported positive-pole inverse has a favorable rank-one update:
\[
A_e^{-1}=A_{0,e}^{-1}-
\frac{2}{1+2\langle c,A_{0,e}^{-1}c\rangle}
|A_{0,e}^{-1}c\rangle\langle A_{0,e}^{-1}c|.
\]
For orthonormal synthesis U_b onto W_{b,e}, put
M_b=U_b* K_e U_b, G_b=U_b* A_e^{-1} U_b,
G_{0,b}=U_b* A_{0,e}^{-1} U_b and v_b=U_b* A_{0,e}^{-1}c.
Then exactly
\[
G_b=G_{0,b}-
\frac{2}{1+2\langle c,A_{0,e}^{-1}c\rangle}v_bv_b^*.
\]
The pole correction **lowers** the supported inverse Gram.
Deleting it is a conservative sufficient bound, not an equality.
A finite *sufficient* certification target is
\[
\boxed{\lambda_{\max}(M_b^{1/2}G_bM_b^{1/2})+\eta_b/\kappa\le1
\quad\Longrightarrow\quad Q_e\succeq0.}
\]
At b=24 this is at most **890 even** directions, with relative
all-negative-frequency remainder <0.009868. Neither this finite
eigenvalue nor the true supported inverse Gram has yet been certified.
For any trial inverse Y, the residual E=U_b-A_eY contributes the
**positive** error term E* A_e^{-1} E and cannot be discarded.

## 5. Standing and next action

**W-EVEN-FORM OPEN.** This pass establishes the even parity-compressed
cofinite theorem (469 exceptions at b=9), preserves the rigorous
infinite negative-frequency error, and exhibits the correct original
supported even-pole finite inverse criterion. It does **not**
discharge the finite low/cross Schur certificate, full even positivity,
whole Weil positivity, the global bridge or RH.

**Next action:** construct one genuinely supported even finite inverse
Gram/cross certificate and bound its complete residual, retaining
the favorable pole coupling; compare with native RC's partially
positive original P0/P2 Schur and high-complement route.
Do not replace a missing matrix eigenvalue with another reformulation.

Replay: python3 scripts/validate_rpb108_ef01_even_parity.py.
Exact regression arithmetic is **not** independent mathematical
review and does not calculate the missing eigenvalue.
