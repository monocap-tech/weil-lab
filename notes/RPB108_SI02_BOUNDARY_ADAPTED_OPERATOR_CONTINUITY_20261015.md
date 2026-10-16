# RPB108 SI02 — collective boundary-adapted energy and compact translation continuity

**Research front:** structural investigation, separate from the RC Schur-inverse chain.  
**Parent:** merged RC323 \`15665091da594ffa73cdfa63f62bcc133939c779\`.  
**Source dependencies:** RC313 original CC27 form; RC314 D carrier; RC320–321 boundary differences; RC323 scalar high-floor no-go.  
**Standing:** exact analytic lemmas and finite rational regression, **not** a full source/Schur positivity certificate. Stage I, F4, RH and Lean remain open.

## Definitions and convention

Let \(I=[-B,B]\), \(B=11/10\). Define physical orthonormal Legendre modes
\[
u_n(x)=\sqrt{\frac{2n+1}{2B}}P_n(x/B),\qquad
d_n=H_n+s>0,\quad H_0=0,\ s>0.
\]
The canonical completed carrier is
\[
\mathcal H_D=\left\{f=\sum_{n\ge0}\alpha_n u_n:
\sum_{n\ge0}d_n|\alpha_n|^2<\infty\right\}.
\]
The embedding \(J:\mathcal H_D\to L^2(I)\) is compact: in the Legendre coordinates its singular values are \(d_n^{-1/2}\to0\).

## SI02-A — exact collective identities for the adapted even family

Set \(F_{2k}=P_{2k}-P_{2k-2}\), \(k\ge1\), and for finitely supported \(c\)
\[
q_c(x)=\sum_{k=1}^N c_kF_{2k}(x/B),\qquad c_0=c_{N+1}=0,
\quad a_n=\frac{2B}{2n+1}(H_n+s).
\]
There are two *simultaneous exact* identities:
\[
\boxed{\|q_c\|_D^2=\sum_{j=0}^N a_{2j}|c_j-c_{j+1}|^2}
\quad\text{and}\quad
\boxed{\|q_c'\|_{L^2(I)}^2=\frac{2}{B}\sum_{k=1}^N(4k-1)|c_k|^2.}
\]
The first is Legendre orthogonality after coefficient telescoping. The second follows from the *all-degree polynomial identity*
\[
\boxed{F_d'(t)=(2d-1)P_{d-1}(t)}
\]
and derivative orthogonality. Hence the canonical D Gram is a weighted discrete Dirichlet form (tridiagonal) while the zero-extension \(H^1\) gradient Gram is **diagonal** in the same coordinates.

The odd family \(F_{2k+1}=P_{2k+1}-P_{2k-1}\) has the same construction, with
\[
\|q_{\rm odd}'\|_2^2=\frac2B\sum_{k\ge1}(4k+1)|c_k|^2.
\]
Every \(F_d\) vanishes at \(\pm1\); its zero extension lies in \(H^1(\mathbb R)\). The translation estimate is therefore *collective*, with no separately charged boundary jumps:
\[
\boxed{\|\tau_{\ell+\delta}\widetilde q_c-\tau_\ell\widetilde q_c\|_{L^2(\mathbb R)}
\le |\delta|\left(\frac{2}{B}\sum_{k=1}^N(4k-1)|c_k|^2\right)^{1/2}.}
\]

## SI02-B — why an unweighted coefficient proof cannot be uniform

The adapted family is **not a Riesz sequence** in \(\mathcal H_D\) for the ordinary unweighted \(\ell^2\) coefficient norm. Taking \(c_k=1\) for \(1\le k\le N\) gives
\[
\sum_{k=1}^NF_{2k}=P_{2N}-P_0,\qquad
\left\|\sum_{k=1}^NF_{2k}\right\|_D^2=a_{2N}+a_0=O(1),
\]
while \(\sum_{k=1}^N|c_k|^2=N\to\infty\). Therefore there is no fixed lower Riesz bound for that coefficient norm.

Nor is the collective \(H^1\) translation estimate Lipschitz with a constant controlled only by the D norm. For a *single* \(F_d\),
\[
\frac{\|[F_d(\cdot/B)]'\|_2^2}{\|F_d(\cdot/B)\|_D^2}
=\frac{2(2d-1)/B}{a_d+a_{d-2}}
\sim \frac{2d^2}{B^2\log d}\longrightarrow\infty.
\]
Thus a single dimension-independent estimate
\(\|\tau_\delta Zf-Zf\|_2\le C|\delta|\|f\|_D\)
**cannot** hold on the entire boundary-vanishing polynomial core. An attempted uniform H1/D bound is a dead end; the discrete gradient metric must be retained.

## SI02-C — a *different* uniform result: norm continuity via compact embedding

For a polynomial \(p\in H^1(I)\), with zero extension \(Zp\), distributional differentiation gives the endpoint-aware translation inequality
\[
\boxed{\|\tau_\delta Zp-Zp\|_{L^2(\mathbb R)}
\le |\delta|\|p'\|_{L^2(I)}
+\sqrt{|\delta|}(|p(-B)|+|p(B)|).}
\]
The two boundary jumps must be retained unless \(p\) vanishes there.

Let \(\Pi_K\) be the physical Legendre degree-\(K\) projection, and define
\[
A_K^2=\sum_{n=0}^K\frac{2n+1}{2B\,d_n},\qquad
V_K^2=\sum_{n=1}^K\frac{(2n+1)n(n+1)}{2B^2\,d_n}.
\]
Cauchy-Schwarz and \(\|u_n'\|_2^2=(2n+1)n(n+1)/(2B^2)\) give
\[
|(\Pi_K f)(\pm B)|\le A_K\|f\|_D,\quad
\|(\Pi_K f)'\|_2\le V_K\|f\|_D.
\]
The omitted physical high tail satisfies
\(\|(I-\Pi_K)f\|_2\le d_{K+1}^{-1/2}\|f\|_D\).

Let \(S_\ell=\mathbf1_I\tau_\ell ZJ:\mathcal H_D\to L^2(I)\) denote an original *zero-extended, clipped* translation. Both zero-extension/translation and clipping are contractions on physical \(L^2\). Splitting \(f=\Pi_Kf+(I-\Pi_K)f\) therefore proves the explicit all-input operator inequality
\[
\boxed{
\|S_{\ell+\delta}-S_\ell\|_{\mathcal H_D\to L^2(I)}
\le |\delta|V_K+2\sqrt{|\delta|}A_K+\frac{2}{\sqrt{H_{K+1}+s}}
\qquad(K\ge0).
}
\]
This holds simultaneously for every polynomial, every degree, and all inputs in the completed carrier. Taking first \(\delta\to0\) for fixed \(K\), then \(K\to\infty\), gives
\[
\boxed{\lim_{\delta\to0}\|S_{\ell+\delta}-S_\ell\|_{\mathcal H_D\to L^2(I)}=0.}
\]

Since \(d_n\to\infty\), this operator-norm continuity holds despite the absence of a globally D-Lipschitz translation estimate. It is also a direct consequence of compact \(J\) and strong continuity of physical translations, but the formula above provides an explicit **degree-independent, finite-split bound**.

For any finite original seven-prime source with parameter intervals \((c_m,\ell_m)\), the triangle inequality now gives a dimension-independent continuity modulus for its entire signed paired-translation operator (and, after bounded \(D^{-1}\) conversion, its D-Riesz action). This is a **norm-continuity and uncertainty-control result**, not a positive lower bound.

## SI02-D — the near/far obstruction is sharp in degree

RC321's original endpoint difference on \(n>d\) with equal parity is
\[
E_{n,d}-E_{n,d-2}
=\frac{2(2d-1)(2n+1)}
{(n-d)(n+d+1)(n-d+2)(n+d-1)}.
\]
At the first neighboring output \(n=d+2\), the expression is
\[
\boxed{\frac14-\frac{2}{4d^2+8d+3}\to\frac14}.
\]
Thus the \(O(n^{-3})\) decay is **fixed-input far-tail decay**, not a uniform diagonal-band estimate. For \(n\ge2d\ge4\), one has the elementary explicit bound
\[
0<E_{n,d}-E_{n,d-2}\le\frac{48d}{n^3}.
\]
**Implication:** a structural argument needs a local/near-diagonal component and a distinct far-field component. It cannot conclude uniform coercivity by treating all cross interactions as a small error.

## Interpretation and next gate

- **New usable positive result:** all-degree, same-basis *diagonal* derivative energy and norm continuity of the complete original translated source action on the D carrier.
- **New negative result:** no dimension-free D-Lipschitz \(H^1\) estimate from these differences; no unweighted-\(\ell^2\) Riesz lower bound; near-diagonal endpoint coupling persists.
- **Quantitative limitation:** the explicit modulus involves \(2/\sqrt{H_{K+1}+s}\), which decreases only logarithmically. By itself it is far too coarse to meet current tight RC323/RC324 Schur margins. We do **not** claim a completed uniform prime-certification budget from it.
- **Research priority SI03:** retain the diagonal derivative penalty and weighted D-difference metric, and seek a *mode-localized* bound for the actual signed Schur covariance. Do not reuse RC323's falsified scalar-floor-only criterion. Independently inspect the odd rank-one negative-pole sector.
- This note neither proves positive \(Q\) on all boundary-vanishing inputs nor closes Stage I, F4, RH or Lean.

## Reproduction

Run \`python scripts/validate_rpb108_si02_boundary_structure.py\`. The standard-library Fraction checks cover representative finite Legendre identities, derivative orthogonality, telescoped D energy and the exact near/far endpoint inequalities. Finite regression is **not** the proof of the all-degree claims; the derivations above are.