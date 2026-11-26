# MASTER-RECON-001 — Neutral-shell reconciliation

**Opened:** 2026-11-24. **Status:** INVESTIGATE; ADOPT 0. Paper derivations, not Lean-certified results.

## Scope and stay

At the user's direction, independent expansion of the previous RH, Deninger–Connes, Weil-Lab, Return, CR-ALP, CR-INT and Bombieri investigations is stayed until completion of this reconciliation or an explicit writ of stay. Existing results may be recovered and audited for this investigation. This record does not itself cancel running CI or control other sessions.

Objective: pay the original MTP-2 obligation, bypass it by excluding the neutral space, or produce a rigorous falsifier or strictly narrower arithmetic obstruction. MTP-1 in the general infinite-exception case remains open. The archived finite-off-axis MTP-1 argument is not independently revalidated here.

## 001A — Neutral-shell inertia (abstract paper proof)

Let M be a finite-dimensional marked-signature Hilbert space and let ell be a bounded map from the native coefficient Hilbert space to M. Let G_t be closed nested gap subspaces with G_t contained in G_{c+} for t>c. Write

$$
\Gamma_+=\ell P_{G_{c+}}\ell^*,\qquad
\Gamma_t=\ell P_{G_t}\ell^*,\qquad D_t=\Gamma_+-\Gamma_t\succeq0.
$$

Assume MTP-1, i.e. $\Gamma_+\succeq I/2$, and norm convergence $D_t\to0$ as $t\downarrow c$. Set $E=\ker(\Gamma_+-I/2)$, $F=E^\perp$, and $K_t=P_E D_t|_E$. In the decomposition E+F, write

$$
\Gamma_+-I/2=\begin{pmatrix}0&0\\0&A\end{pmatrix},\qquad
D_t=\begin{pmatrix}K_t&B_t^*\\B_t&C_t\end{pmatrix}.
$$

If F is nonzero, choose $\alpha>0$ with $A\succeq\alpha I_F$. Put $\delta_t=\|D_t\|$; for $\delta_t<\alpha$, the complementary block $A-C_t$ is positive definite. The Schur complement is

$$
S_t=-K_t-B_t^*(A-C_t)^{-1}B_t.
$$

Positive semidefiniteness of D_t implies $K_t e=0\Rightarrow D_te=0\Rightarrow B_te=0$. Hence $\ker S_t=\ker K_t$. Inertia under invertible block congruence gives

$$
n_-(\Gamma_t-I/2)=\operatorname{rank}K_t,\qquad
\ker(\Gamma_t-I/2)=E\cap\ker D_t.
$$

Also $D_t^2\preceq\delta_t D_t$ implies $K_t^2+B_t^*B_t\preceq\delta_t K_t$. Therefore

$$
-\frac{\alpha}{\alpha-\delta_t}K_t\preceq S_t\preceq-K_t.
$$

If F is zero the inertia and kernel statements follow directly from $\Gamma_t-I/2=-D_t$. This argument preserves the exact activation kernel but does not prove its vanishing.

**Control:** a scalar nested compression can have $\Gamma_+=1/2$ and $\Gamma_{c+\varepsilon}=1/2-e^{-1/\varepsilon^2}$ for all sufficiently small positive epsilon. Realize this in L² by a vector with mass 1/2 in a retained sector, part of which has cumulative squared mass $e^{-1/\varepsilon^2}$ near the moving boundary; keep the other 1/2 outside the initial projection. Thus arbitrarily flat positive loss is compatible with projection nesting. This is not an actual-zeta counterexample.

## 001B — Exact arithmetic exterior response (paper derivation)

Use the ordinary Fourier convention $\hat f(\xi)=\int f(x)e^{-i\xi x}\,dx$ and inverse factor $1/(2\pi)$. For the stated full mixed-pole signed Weil convention the archimedean symbol is

$$
A(\xi)=\Re\psi(1/4+i\xi/2)-\log\pi
=-\gamma-\log\pi+\sum_{n\ge0}\left(\frac1{n+1}-\frac{2a_n}{a_n^2+\xi^2}\right),
\quad a_n=2n+1/2.
$$

Since $\mathcal F^{-1}[2a/(a^2+\xi^2)](x)=e^{-a|x|}$, off the diagonal the convolution kernel is $-J(|x-y|)$, where

$$
J(r)=\frac{e^{-r/2}}{1-e^{-2r}}
=\frac1{2r}+\frac14-\frac{r}{48}+O(r^2).
$$

The constant terms are supported on the diagonal and make no exterior contribution. For a compactly supported L² function the formula follows first on exterior test intervals at positive separation by absolute convergence, then on the whole open collar in the distributional sense. The truncated Carleman part has L² operator norm at most $\pi/2$ (using the full Carleman norm $\pi$), and the analytic remainder is Hilbert–Schmidt on bounded rectangles. This gives an L² exterior realization without assuming pointwise boundary traces.

For a zero-extended function k supported on [-c,c], reflect $h(r)=k(c-r)$ on (0,2c). Denote zero extension by a tilde. In the full mixed-pole convention the pole kernel is $2\cosh((x-y)/2)$. The prime weights are $d_n=\Lambda(n)/\sqrt n$ with both translation signs. For $0<s<\varepsilon$ the right exterior response is

$$
(\mathcal M^+_{c,\varepsilon}h)(s)=
\int_0^{2c}\left[2\cosh((s+r)/2)-J(s+r)\right]h(r)\,dr
-\sum_{\substack{n\ge2\\ \log n<2c+\varepsilon}}d_n\widetilde h(\log n-s).
$$

**Threshold correction:** the interior cutoff $\log n<2c$ does not suffice on the exterior collar: a prime power at $\log n=2c$ contributes $h(2c-s)$. The stated exterior cutoff includes it, and zero extension handles all partial overlaps. Forward shifts vanish on the right exterior. No parity reduction is presumed.

The archived finite-exception investigation supplies a candidate native linear neutral realization $\mathcal K:E\to L^2(-c,c)$ with $k_u=\mathcal Ku$ and coefficient relation $\Phi(u)=(P_c^*k_u,-N_c^*k_u)$; the native typing and normalization still require audit. Define $R_+ k(r)=k(c-r)$, $R_- k(r)=k(-c+r)$ and the two-sided bounded residual

$$
T_\varepsilon u=(\mathcal M^+_{c,\varepsilon} R_+\mathcal Ku,
\mathcal M^+_{c,\varepsilon} R_-\mathcal Ku),\qquad
\mathfrak G_\varepsilon=T_\varepsilon^*T_\varepsilon.
$$

The left expression uses reflection symmetry of the stated complete signed operator. This Gram measures the squared L² norm of the two exterior outputs in the stated convention.

## Native attachment gate (OPEN)

Put $J_Eu=P_{G_{c+}}\ell^*u$. Projection nesting gives exactly

$$
\langle u,K_tu\rangle=\|(I-P_{G_t})J_Eu\|^2,\qquad
\ker K_t=\{u:J_Eu\in G_t\}.
$$

The missing native statement is

$$
J_Eu\in G_t\iff \mathcal W\widetilde k_u=0\text{ on }(-t,t).
$$

If this statement, native interior neutrality and the preceding analytic hypotheses hold, then $\ker K_{c+\varepsilon}=\ker\mathfrak G_\varepsilon$, and for small epsilon

$$
n_-(\Gamma_{c+\varepsilon}-I/2)=\operatorname{rank}\mathfrak G_\varepsilon.
$$

This is a conditional rank/kernel identity, not equality of the two Grams or their metrics. Source attachment must verify actual divisor, multiplicities, signs, the selected/background coefficient decomposition, coefficient inner product, physical carrier and distributional pairing. The archived physical null identity cannot be treated as an independently certified theorem here. In particular an adjoint involving a regularized carrier need not automatically coincide with raw L² analysis.

## Ledger and next gate

| Item | Status |
| --- | --- |
| Abstract inertia, kernel, relative Schur estimates | Paper proved under explicit assumptions |
| Exterior kernel and threshold correction | Derived in stated convention |
| Native coefficient-to-physical identity | OPEN |
| Historical finite-off-axis MTP-1 | Reported in archive; audit required |
| Exact exterior Gram vanishing or strict positivity on actual neutral space | OPEN |
| General infinite-exception MTP-1 | OPEN |
| MTP-2 / RH | OPEN |

001C: exterior arithmetic rigidity on actual interior neutral modes, with native attachment in parallel only as part of this reconciliation. Test exact exponential-resolvent expansion, actual finite prime shadows and the interior equation together. Do not substitute arbitrary boundary germs, generic unique continuation, or decay to all polynomial orders for exact persistence. If proving immediate activation, recognize that it falsifies persistence for a nonzero neutral mode; it does not by itself exclude such a mode or prove RH.

## Historical provenance

September archived research gates AZ-FIN-MTP2-BOUNDARY-0, AZ-FIN-NEUTRAL-EXPLICIT-FORMULA-0, AZ-FIN-PRIME-SHADOW-0 and AZ-FIN-SHADOW-ALIGNMENT-0 (2026-09-21) motivate the finite-exception physical realization and shadow equation. MASTER-RECON-001A/B are the 2026-11-24 reconciliation paper derivations. This file is a research ledger, not a formal proof certificate or a claim of novelty over the literature.
