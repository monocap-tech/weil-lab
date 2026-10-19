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

## Verified first complete original signed-source execution

**GitHub Actions [39191354830](https://github.com/monocap-tech/weil-lab/actions/runs/39191354830) completed SUCCESS at source head d881aa1477509bd6c63b9d79ea19f8bc57ccc556.** All exact-rational source, matrix, signed real-window and scope checks passed (not merely Python syntax). The new record:

| Certified source matrix/object | Outward full-coupling scalar fee |
| --- | ---: |
| SM47 complete original positive low [0,4096] 25-source lower | \(132769427841/500000000000000\), approximately \(0.000265538856\) |
| NEW original true 15-band negative source-mean lower | \(59935997/1000000000000\), approximately \(0.000059935997\) |
| Actual original sinh-pole rank-one upper comparison error | \(80001/1000000000000\), approximately \(0.000000080001\) |

**Decisive witness without subtracting the pole:** Original supported SI10 source *coordinate index 2* (zero-based, a genuine selected sine cluster) has, with **the complete original signed negative 15-band lower** and **the entire SM47 positive-low reference**,

\[
\begin{aligned}
\langle e_2,(N_{15}-\epsilon_N I)e_2\rangle
&\gtrsim 0.019501318476,\\
\langle e_2,L_{47}e_2\rangle
&\lesssim 0.002168100628,\\
\langle e_2,(N_{15}-\epsilon_N I-L_{47})e_2\rangle
&> 17/1000.
\end{aligned}
\]

These decimal signs summarize exact independently outward-rounded rational enclosures; the actual certifier compares exact Fractions and proves the strict \(17/1000\) gap. The strongest among the 625 checked normalized one/two-source vectors is also \(e_2\), with measured exact comparison approximately **0.01733321784822** per coefficient norm squared.

The pole-aware lower-reference diagnostic has an even larger maximal normalized deficit, approximately **0.33072387141209** at \(z=e_{16}-e_{24}\) (where source 24 is the actual sinh pole). This value still concerns **only the lower reference**; it is **not** a negative eigenvalue or a Rayleigh witness for the true whole original signed Weil operator.

**What changed structurally:** the SM47 proof-reference deficiency already occurs *before* pole subtraction. Thus it cannot be fixed merely by certifying exceptional-pole compensation. What must improve is captured **original positive spectral mass on the negative-packet source geometry** or the full source-conditioned original positive inverse. All 25 genuine source Fourier cross couplings were present; this is not a diagonal truncation.

**Custody:** The focused source head d881 CI passed. Subsequent strengthening at heads 1ac4a520, 36b6eceb and 812d5a4e makes the original source-coordinate provenance explicit and fail-closes on rigorous \(17/1000\) and \(33/100\) bounds. Final-head workflow must be checked independently. This is not peer review or Lean formalization.

**No automatic mathematical promotion:** Entire original W-ODD-NEG O1/O2, actual full original negative cap/inverse, 470 source strong residual, even E1–E4, signed Weil, CC27 and RH all remain OPEN.
