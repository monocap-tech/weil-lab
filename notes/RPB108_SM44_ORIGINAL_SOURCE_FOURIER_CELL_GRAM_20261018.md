# SM44 — Exact original physical Fourier-cell Gram and complete rational 25×25 weighted source proxy

**October 18, 2026 · canonical W-ODD-NEG · stacked on SM43 draft PR #225 (recovered strict hybrid source-window gate, final-head CI pending).**

## The genuine remaining calculation after SM43A

SM43 and SM43A gave a true ORIGINAL seven-prime/digamma-positive, all-real signed-frequency interval enclosure on the source-centered union \(\mathcal W\) of **16 actual SI10 source windows** of total measure \(1029/64\), with the 25 genuine supported original odd sources (16 sin, 8 \(x\cos\), 1 true sinh pole). The strongest recovered SM43A uses the locally better of a signed original endpoint-affine positive-part weight and a step-constant positive weight. At mesh max 1/8, the recovered whole-source-matrix error to its formal weighted Fourier-cell Grams was **45.610847484** (initial 1/8 constant reference: 81.189344451), while the pure affine-only candidate FAILED the competitiveness gate (81.779824556). Even SM43A's improved exact real-weight error is much larger than the desired source stiffness threshold and, crucially, its cell Fourier Gram integrals \(C_I=2\int_I T(\xi)T(\xi)^T d\xi\) were *only defined*, not evaluated or enclosed.

**SM44 now does the new mathematical task:** evaluate an explicit **FULL 25×25 RATIONAL source Gram proxy \(P_{\mathcal W}\)**, with a rigorous whole-operator Loewner error from the **actual original weighted positive source stiffness** on exactly those genuine original frequency windows. This is NOT a claim about the remaining frequencies in \([0,4096]\), the full original 470-source operator, the true pole-conditioned Astar inverse, odd O1/O2, Weil/RH.

## 1. Analytic physical Fourier source intervals at every rational midpoint

The genuine original physically supported sine Fourier amplitudes (SM38 and SM42) are, with \(B=11/10\), \(\omega=2\pi\xi\), \(c\) each original SI10 rational center,
\[
\begin{aligned}
T_{\sin_c}(\xi)&=\tfrac12[F_0(c-\xi)-F_0(c+\xi)],\\
T_{x\cos_c}(\xi)&=\tfrac12[F_1(\xi+c)+F_1(\xi-c)],\\
T_s(\xi)&=\frac{2[(1/2)\cosh(B/2)\sin(\omega B)-\omega\sinh(B/2)\cos(\omega B)]}{(1/2)^2+\omega^2},
\end{aligned}
\]
where \(F_0(q)=2\sin(2\pi Bq)/(2\pi q)\), \(F_1(q)=2[\sin(2\pi Bq)-2\pi Bq\cos(2\pi Bq)]/(2\pi q)^2\), with the proper continuous \(q=0\) limits. These are exact **original physical Fourier identities** for the true supported source functions, no FFT truncation and no invented disjoint source support.

At the rational midpoint \(\xi_I=(a+b)/2\) of each TRUE original frequency cell \(I=[a,b]\), reuse SM42's **SI06 rational \(\pi\) interval, exact period-reduced rational sine/cos Taylor intervals and positive hyperbolic Taylor intervals**. Hence all 25 true \(T_j(\xi_I)\) lie in rigorous rational intervals. Choose rational midpoints \(v_{j,I}\) to denominator \(10^8\), and PAY the exact outward interval and quantization radius \(r_{j,I}\). The entire computed \(25\times25\) proxy uses only these rational physical midpoint amplitudes—not sampled digamma or float FFT values.

## 2. Valid complete source matrix Fourier-cell integration error

From the integral definition, for EVERY REAL \(\xi\) and each original supported selected physical source \(g_j\),
\[
T'_j(\xi)=2\pi\int_{-B}^B xg_j(x)\cos(2\pi\xi x)\,dx.
\]
Therefore each genuine original source has a rigorous full-real frequency-Lipschitz ceiling \(L_j\):
\[
|T'_j|\le
\begin{cases}
2\pi_{\rm up}B^2 & g_j=\sin(2\pi cx)\text{ or }s=\sinh(x/2),\\
\frac43\pi_{\rm up}B^3 & g_j=x\cos(2\pi cx).
\end{cases}
\]
The pole uses \( |\sinh(x/2)|<1\) for \(|x|\le B\). Thus on ALL actual real \(\xi\in I\),
\[
|T_j(\xi)-v_{j,I}|\le e_{j,I}:=r_{j,I}+\tfrac12L_j|I|.
\]
SM43 independently gives full-real original physical source sup \(|T_j(\xi)|\le s_{j,I}\). Set \(E_I=\sum_j e_{j,I}^2\), \(S_I=\sum_j s_{j,I}^2\). For EVERY coupled original source coefficient vector \(z\),
\[
\bigl|z^*(T(\xi)T(\xi)^T-v_Iv_I^T)z\bigr|
\le (2\sqrt{E_IS_I}+E_I)\|z\|_2^2.
\]
Every source cross interaction is paid. The square root is **rounded upward using exact integer square roots on Fractions**, not float.

## 3. Exact integration of the rational signed positive-part weight

For each original real cell, use exactly SM43A's *CERTIFIED locally optimal* choice:
- original constant reference \(w_I=(\ell_I+u_I)/2\), or
- \(w_I(\xi)=\max(\kappa,q_I(\xi))\), with \(q_I\) the rational signed original \(m\)-endpoint-midpoint affine interpolant.

The latter has at most ONE **exact rational reference crossing** and its scalar integral \(J_I=\int_Iw_I(\xi)d\xi\) is evaluated in closed rational arithmetic by splitting there when needed; all actual unknown true \(m=\kappa\) crossings remain covered by the SM43A rational error, not assumed to be identical to the reference crossing. Round \(J_I\) to an explicit denominator \(10^8\), pay \(|J_I-\widetilde J_I|\) separately.

Construct the ACTUAL EXPLICIT FULL 25×25 **rational** matrix
\[
\boxed{\mathsf P_{\mathcal W}
=2\sum_{I\subset\mathcal W}\widetilde J_I v_Iv_I^T.}
\]
Its entries are all rational; every source cross retained, not just diagonals. The complete \(\mathsf B_{\mathcal W}\) with original weighted Fourier cell Gram and SM43A's chosen reference has rigorous source-matrix error
\[
\boxed{
-\epsilon_{\rm Fourier}I_{25}
\preceq \mathsf B_{\mathcal W}-\mathsf P_{\mathcal W}
\preceq \epsilon_{\rm Fourier}I_{25}
}
\]
with exact rational upper
\[
\epsilon_{\rm Fourier}=
\sum_I\big[
  2J_I(2\sqrt{E_IS_I}+E_I)
  +2|J_I-\widetilde J_I|\sum_j v_{j,I}^2
\big].
\]

SM43A already certifies a true original seven-prime/digamma whole-real **positive multiplier** error \(\epsilon_{\rm weight}\) between \(\mathsf A_{o,\mathcal W}\) and \(\mathsf B_{\mathcal W}\), including all \(\kappa\) crossings. Therefore the NEW fully numeric-usable-rational but potentially very conservative operator enclosure is
\[
\boxed{
-(\epsilon_{\rm weight}+\epsilon_{\rm Fourier})I_{25}
\preceq\mathsf A_{o,\mathcal W}-\mathsf P_{\mathcal W}
\preceq(\epsilon_{\rm weight}+\epsilon_{\rm Fourier})I_{25}.
}
\]
This is a **real original complete 25×25 source-window weighted positive stiffness enclosure**, not merely an intermediate reference integral. It is entirely original physical source geometry + full signed seven-prime/digamma and has no numerical Gauss / unbounded-tail assumptions on the covered windows.

SM44 checks the strict error contraction from maximum mesh widths \(1/4\to1/8\) on the **identical source window union**, reporting \(\epsilon_{\rm weight}\), \(\epsilon_{\rm Fourier}\), total and the actual complete 25×25 rational proxy. If the scalar Fourier error is still larger than source conditioning tolerances, the next optimization is a true original source-centered *higher-order analytic T derivative* or matrix-weighted/preconditioned cell error, not arbitrary more FFT padding.

## 4. Strict acceptance boundaries / next frontier

This fully certified new stiffness enclosure covers only \(\mathcal W\) of measure \(1029/64\), NOT all original positive LOW \([0,4096]\) or the original high-log positive tail beyond 4096. SM41's exact source high log upper remains separate, SM42's exact supported physical Gram/pole remains separate, and SM40's full original signed-negative upper remains separately certified. A source-window positive stiffness enclosure with large error is **not** a full original \(A_o\) positive matrix, rank-one \(A_*\) inverse, true strong resolvent, all-470 complete odd sign, even E1-E4, whole signed Weil, CC27 or RH proof.

**SM45 direction:** inspect the actually measured complete physical Fourier source-cell integration error (as distinct from the 45.6 original multiplier error) and improve dominant source-conditioned frequency cells, plus extend **ALL missing intervals** of the true original positive LOW \([0,4096]\) without dropping the actual original physical source cross, then combine SM41 high tail and SM42 pole. No auto promotion. Full original Fourier/closed-domain analytic audit remains an independent requirement.

Replay: \`python3 scripts/validate_rpb108_sm44_physical_fourier_cell_gram.py\`. JSON outputs a complete original 25×25 rational proxy and independent outward rational source error budgets, all explicitly scoped.
