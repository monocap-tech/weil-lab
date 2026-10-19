# SM48 — Original 25-source signed-negative Jensen test of SM47 lower reference

**October 18, 2026 · Active W-ODD-NEG · Stacked on SM47 PR #229.**

## Question and mathematical status

SM47 proved a genuinely **one-sided** low [0,4096] lower bound \(L_{47}\preceq A_{\mathrm{low},25}\), for the 25 original physically supported odd SI10 source coordinates. SM47's \(17\) strictly positive windows do **not** reconstruct the true entire positive operator; missing positive spectral contributions were intentionally discarded. SM48 checks whether this particular rigorous lower reference is strong enough to absorb even a certified suboperator of the true original signed-negative spectrum.

This is a **method-sufficiency test**, not a purported contradiction to Weil positivity. It can fail even if the actual original full positive operator dominates the complete negative-frequency operator.

## Exact signed suboperator on the same 25 true physical sources

Let \(T(\xi)\) be the actual full 25-vector of supported odd sine Fourier transforms, including all 16 zero-extended \(\sin\) sources, 8 \(x\cos\) sources, and genuine \(\sinh(x/2)\) pole. The true odd frequency-negative part is

\[
K_{\mathrm{neg},25}
=2\int_0^\infty(\kappa-m(\xi))_+\,T(\xi)T(\xi)^T\,d\xi,
\qquad \kappa=10^{-3}.
\]

SM04 certifies **15 pairwise-disjoint complete REAL negative windows** \(I_j^-=[c_j-r,c_j+r]\), \(r=1/100\), where the *original* full signed seven-prime/digamma multiplier \(m(\xi)<-\delta\), \(\delta=2/5\). This follows from whole-real interval arithmetic, not samples. Let

\[
u_j^-=\frac1{2r}\int_{I_j^-}T(\xi)\,d\xi,\qquad
\gamma_- = 4r\delta=\frac2{125}.
\]

By Jensen,

\[
K_{\mathrm{neg},25}
\succeq\gamma_-\sum_{j=1}^{15}u_j^-{u_j^-}^T.
\]

At each original negative window center, take the exact rational SI06/SM42/SM46 Fourier midpoint enclosure, rational vector \(v_j^-\), actual local original supported second Fourier derivative upper \(K_{ij}\), true spatial third-moment bound and symmetric-band first derivative cancellation:

\[
|u^-_{ij}-v^-_{ij}|
\le r^{(0)}_{ij}+\frac{K_{ij}r^2}{6}.
\]

The new **full 25×25 rational negative Jensen matrix** \(N_{15}=\gamma_-\sum_j v_j^-{v_j^-}^T\) includes all 625 cross entries. With exact upward integer-square-root enclosures,

\[
K_{\mathrm{neg},25}\succeq N_{15}-\epsilon_N I_{25},\qquad
\epsilon_N=\gamma_-\sum_j
\bigl[2\sqrt{V_j^2R_j^2}+R_j^2\bigr].
\tag{SM48-N}
\]

This is a *lower*, not an upper, bound for the actual complete negative spectrum. It is enough to disqualify a candidate **positive lower reference** if that reference cannot dominate even \(N_{15}-\epsilon_NI\).

## Comparison with original SM47 all-low lower matrix

Reconstruct the same original SM47 full 25-source rational matrix, without averaging diagonal/cross terms away:

\[
L_{47}=\kappa H_q+P_{17}
-\Bigl[\epsilon_P+\kappa\bigl(\epsilon_H+2E/4096\bigr)\Bigr]I_{25}
\preceq A_{\mathrm{low},25},
\quad E=202/25.
\]

A purely rational witness vector \(z\in\mathbb Q^{25}\) with

\[
\boxed{
z^T(N_{15}-\epsilon_N I_{25}-L_{47})z>0
}
\tag{SM48-O}
\]

proves that **this SM47 lower reference cannot dominate even the 15-band original signed-negative suboperator**, so this reference alone cannot close W-ODD-NEG. It says **nothing** about the sign of the actual original signed Weil quadratic form, because \(L_{47}\) is only a lower bound on \(A_o\). Do not report this as an actual original signed negative direction or any proof of a nonzero original negative index.

The validator checks **all 25 individual coordinate source directions and all 600 normalized two-coordinate sign combinations**, with true exact rational quadratic inequalities. Candidate selection uses no floating spectrum. If no positive rational deficit is found, the proposed no-go assertion fails closed; a non-result cannot be upgraded to theorem.

## Signed exceptional pole retained

The real physical pole source \(s=\sinh(x/2)\) is the last of the actual 25 original source functions; its form vector is \(p_i=\langle g_i,s\rangle=H_{i,24}\). Original SM42 physical interval Gram gives \(q_i=H_{q,i,24}\) with exact upper error

\[
2pp^T\preceq 2qq^T+\epsilon_{\mathrm{pole}}I_{25}.
\]

Therefore \(L^\star_{47}=L_{47}-2qq^T-\epsilon_{\mathrm{pole}}I\) is a **certified lower reference** for original \(A_{\mathrm{low},25}-2ss^T\) in these source coordinates. A positive rational Rayleigh deficit against \(N_{15}-\epsilon_NI\) is additionally recorded; it remains a method obstruction only. This preserves the signed exceptional pole and complete source coupling without silently pretending the actual pole-subtracted operator has been upper bounded.

## Acceptance and next physical source obligation

Focused code must show: original full 15 negative whole-real windows, original full 17 positive windows, identical original SI10 physical 25 sources with all 625 cross entries, exact outward matrix/rank-one error fees, 625 exact rational source witness tests, **strict exact positive gap** for at least one witness against the non-pole lower reference (stronger than requiring failure only after pole correction), and explicit original odd O1/O2/even/Weil/CC27/RH = OPEN.

If this gate passes, SM48 is **negative evidence for the 17-window *lower reference*, not for original Weil positivity**. The next useful SM49 target is a source-adaptive **whole-positive response** in the negative-packet geometry (or direct original complete inverse/schur residual), with an exact matrix-weighted error rather than a global scalar fee. A higher-dimensional original source expansion must carry its own true physical Fourier identities and complete complement residual.

**Before GitHub Actions verification:** no SM48 quantitative acceptance or proof-reference obstruction is claimed. Original Fourier/closed-domain identification and external mathematical audit remain separate.
