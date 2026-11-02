# Weil-Lab NF444 — Source-exact shared near-B resummation and J7/J8 contact

**2026-11-01 PT — ACCEPTED as an original-source mathematical representation, not as a signed integral.** Draft PR #465 stacked on original NF443 full signed physical J2 positive (PR #464). No main merge. Canonical W-ODD-NEG, NF410/NF404 global scalar, fourth J242 and RH OPEN.

## Previous cursor → current circle → next

**NF443 previous:** The true original physical J1,J2,J3 have complete STRICT POSITIVE signed contributions, J4,J5,J6 complete STRICT NEGATIVE. **Six of eight** original positive physical cells have actual continuous-source signed certificates. J7=(log8−B,log9−B) and J8=(log9−B,B) remain OPEN. Original NF433 J7 whole-panel Chebyshev 512 generator bound was ineffective; original NF441 J8 whole-panel uniform Bernstein/2048-image bound was a METHOD STOP because the principal q logarithm is unbounded and image exponential convergence ratio tends to one at x=B.

**NF444 current:** Recover a *common original source response* at J7/J8. The original NF424/NF443 image transfer contains its own source-exact cancellation of the explicit principal logarithm. **This removes the apparent endpoint singularity from the complete regular response z, not from p itself.** The residual numerical bound is still unacceptably loose to decide D7 or D8.

## Authentic source custody and distinct physical routes

No new source selection, no changed frequency order and no replacement principal response: original NF407 242 selected +4 critical dyadic coefficients, all 32 critical sine frequencies, 273 distinct frequency/order groups, exact NF404 centered source and odd sinh removable pole, and NF406 physical support seams. Original source JSON SHA256 \`0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce\`; original seams JSON SHA256 \`c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675\`.

On J7 regular NF405 minus shifts **2,3,4,5,7,8** and plus none, independent principal NF407 r-jumps **2,3,4,5,7,8**. On J8 both add **n9**, plus still none. This must not be conflated with earlier J1/J2 branches.

## Source-original image coefficient identity

The true native transfer, not a stand-in discretization, uses image index \(m\geq0\), \(a_m=m+\tfrac14\), with source-correlated transfer coefficient \(T_m\). Each original (frequency \(f\), polynomial order \(k\), source coefficient \(c\)) contributes

\[
2\operatorname{Re}\left[
e^{2\pi i f B}\sum_{j=0}^k
\frac{\alpha_{f,k}\binom{k}{j}j!B^{k-j}/2^j}
{(a_m-\pi i f)^{j+1}}
\right],\quad |2\alpha_{f,k}|=|c|.
\]

The original odd sinh pole contributes, for \(m\geq1\),

\[
\frac{c_{\rm pole}}{2}
\left(\frac{e^{B/2}}{m}-\frac{e^{-B/2}}{m+1/2}\right).
\]

The original \(m=0\) removable-pole formula is separately finite and retained **unchanged**.

The coefficient of \(a_m^{-1}\) in the *complete source-linear* \(T_m\) is exactly

\[
v=u_4(B)
\]

(the same original endpoint evaluator used in the explicit principal piece). This is an equality of source-linear amplitudes for the unchanged original dyadic source, not a fit to numerical mode values.

Define the exact remainder \(R_m=T_m-v/a_m\). For \(m\geq1\), using \(a_m\geq5/4\), \(|(a_m-\pi i f)^{-1}|\leq1/a_m\), \(\pi<22/7\), \(e^{B/2}<2\), and \(e^{-B/2}<1\),

\[
|R_m|\leq\frac{M}{(m+1/4)^2}.
\]

Here the original full-source outward rational \(M\) is computed directly as

\[
\begin{aligned}
M_0={}&|c_{\rm pole}|+\sum_{(f,k)} |c_{f,k}|
\left[\frac{22}{7}fB^k+
\sum_{j=1}^k\frac{\binom{k}{j}j!B^{k-j}}{2^j}\right],\\
M={}&M_0+10^{12}S_0,
\end{aligned}
\]

where \(S_0\) is the **original actual 4096-bit source dyadic interval-radius charge**. The error overcharge follows from \(k\leq13\), \(f<883\), \(13\cdot13!<10^{11}\). The pole remainder is bounded by \((7/16)|c_{\rm pole}|/a_m^2\), strictly inside the pole overcharge \(|c_{\rm pole}|\).

The resulting authentic original bound is approximately

\[
M\simeq1.41812105824581\cdot10^{144}.
\]

That constant is real, rigorous and **not sign-decision-quality**.

## Exact image resummation and principal logarithm cancellation

For \(d>0\), define

\[
\begin{aligned}
\mathcal H(d)
&=\sum_{m=0}^{\infty}\frac{e^{-2(m+1/4)d}}{m+1/4}\\
&=\log\coth(d/4)+2\arctan(e^{-d/2}).
\end{aligned}
\]

This is an exact elementary identity: put \(y=e^{-d/2}\), then the original series becomes \(4\sum_{m\ge0}y^{4m+1}/(4m+1)\). Its derivative in \(y\) is \(4/(1-y^4)\), the derivative of \(\log((1+y)/(1-y))+2\arctan y\); both vanish at \(y=0\). NF444 also checks the first 128 odd formal power-series coefficients exactly over \(\mathbb Q\), including the cancellation of all \(y^{4m+3}\) powers.

For the original transfer on positive x, write \(d=B-x\). The infinite image contribution is exactly

\[
I(x)=\frac v2[\mathcal H(B-x)-\mathcal H(B+x)]
+\frac12\sum_{m=0}^{\infty}R_m
\left(e^{-2a_m(B-x)}-e^{-2a_m(B+x)}\right).
\]

The original NF407 centered response *also contains* \(-\tfrac v2\log(B/(B-x))\). Thus the potentially divergent expression in the complete z is

\[
\frac v2\left[\mathcal H(d)-\log(B/d)-\mathcal H(B+x)\right],
\]

and since

\[
\mathcal H(d)+\log d\longrightarrow\log4+\pi/2
\qquad(d\downarrow0),
\]

the source-exact boundary limit is

\[
\boxed{\frac v2\bigl[\log(4/B)+\pi/2-\mathcal H(2B)\bigr].}
\]

All other native original fixed-cell terms (entire source response, shifted interior u4 terms, and already-joined removable sinh pole) have finite boundary limits. The \(m=0\) residual is a single finite term; the \(m\geq1\) residual series converges **uniformly up to x=B**, since \(\sum a_m^{-2}<\infty\).

For every \(N\geq1\) and real \(0\leq x\leq B\), the remaining full-source image tail obeys

\[
\left|\frac12\sum_{m=N}^{\infty}R_m
(e^{-2a_m(B-x)}-e^{-2a_m(B+x)})\right|
\leq\frac{M}{2(N-3/4)}.
\]

This formula no longer contains the factor \(1/(1-e^{-2(B-x)})\) that made the old whole-cell J8 2048-image approach stop. In particular the complete original fixed-source z has a **finite continuous one-sided value at x=B**. It does **not** follow that z analytically extends across B or that a 512-mode unweighted Chebyshev approximation is adequate there.

At N=2048 the honest residual sourcewise absolute bound is ~\(3.46347797837541\times10^{140}\), **orders of magnitude too loose** compared with original true signed contributions of order \(10^{-23}\). No zero-error or positivity certificate follows.

## Actual J7/J8 contact at n=9

At \(x_*=\log9-B\), the n9 regular NF405 minus-translate switches on. Because the original u4 source is odd,

\[
\Delta z_{\rm regular}=-w_9 u_4(-B)=+w_9v.
\]

At that same genuine prime-support seam the original principal \(r\) gains \(+w_9v\), so in \(z\)'s subtraction of the principal response,

\[
\Delta z_{\rm principal}=-w_9v.
\]

**Their sum is exactly zero.** J7 and J8 are two physical support descriptions of the same continuous z; no new independent response variable or arbitrary jump is permitted. This exact equality holds for every source coefficient in its native interval, not merely at the midpoint.

The original J8 principal \(p(x)\propto \log(B/(B-x))\) remains unbounded at B, but logarithms are L1; with complete z bounded to the endpoint, the original \(pz\) and \(z^2\) are **integrable** on J8. This proves existence of the physical integrals, **not their numerical signs**.

## Status / next NF445

The source-exact CI replay checks actual source and seam SHA, the original native transfer code conventions (including m=0 special pole handling, true endpoint U(B) and explicit original principal log), exact odd-series coefficients, original J7/J8 branch and jump identities, source-radius M, and the O(m^-2) tail formula. [Focused NF444 Actions #41385705229 — SUCCESS](https://github.com/monocap-tech/weil-lab/actions/runs/41385705229).

**Closed mathematical obligations:**
- Source-universal analytic extraction of near-B singular image term and its exact cancellation against the original principal logarithm.
- Existence and continuity of the complete original J8 response at +B as a one-sided finite limit.
- Exact physical J7/J8 seam contact (n9 activation canceled by principal r).
- Existence of the original J8 \(pz\) and \(z^2\) integrals as finite quantities.

**Still OPEN:**
- A **quantitatively useful** original source-correlated bound for residual \(R_m\), replacing the loose absolute M~10^144 triangle; possible exact Arb source-group residual evaluations and higher-order pole subtraction.
- Full original true signed D7 and D8, the independent original NF410 p0/true signed moment contracts and summability of a near-B collar.
- Original principal E_p global evaluation, full NF410/NF404 signed scalar, fourth J242 exterior upper, W-ODD-NEG, even/whole Weil/infinite inverse/domain, RH.

**Next bold NF445:** compute actual **correlated** source \(R_m\) and perhaps one or more exact asymptotic 1/a_m^j coefficients, before increasing J7/J8 Chebyshev degree or inserting arbitrarily tiny endpoint collars. The certificate architecture—not merely the sampling resolution—must become quantitative. No main merge.
