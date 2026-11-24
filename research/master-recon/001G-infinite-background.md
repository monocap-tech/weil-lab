# MASTER-RECON-001G — Infinite-background adjudication: unconditional raw closed range

2026-11-24. INVESTIGATE; ADOPT 0. Paper derivation; no Lean compilation. Previous investigations remain stayed. This pass removes finite-off-axis assumptions from raw closed-range and right-continuity results, not from selected persistence rigidity.

## 1. Full and selected sampling estimates

Use the actual multiplicity-weighted raw Mellin analysis A=(A_+,A_-) with unitary signature decomposition of the reflection pairing, as in 001E. For a finite selected negative packet Pi, A_Pi=(A_+,A_-,Pi); omitted negative channels are deleted, as in 001F. Let X_t be the supported logarithmic Fourier space of 001E, with norm squared (2pi)^(-1) integral log(2+|xi|)|hat f(xi)|² dxi.

The full polarized explicit formula on smooth compact tests gives
$$
\|A_\Pi f\|^2=W(f,f)+2\|A_{-,\Pi}f\|^2+\|A_{-,\Pi^c}f\|^2.
$$
In particular ||A_+ f||² >= W(f,f), independently of the number of off-line zeros. The bounded physical pole and prime contributions and Gamma asymptotics yield
$$
\|A_+ f\|^2\ge \|f\|_{\log}^2-C_t\|f\|_2^2.
$$
No omitted negative evaluation bound is needed for this lower estimate.

For the upper estimate, use the classical Riemann–von Mangoldt formula with O(log T) remainder, giving O(log(2+|u|)) zeros counted with multiplicity in any unit-height interval (also negative heights by symmetry). In the Fourier ordinate variable all zeros lie in |Im z|<1/2. For F=hat f, subharmonic mean-value inequality on radius-one disks centered at each zero gives
$$
\sum_\rho m_\rho |F(\gamma_\rho)|^2
\le C\int_{-3/2}^{3/2}\int_{\mathbb R}\log(2+|u|)|F(u+iv)|^2du\,dv.
$$
Indeed the multiplicity-weighted overlap count of the disks at u+iv is O(log(2+|u|)); the Fourier sign / reflection permutation is immaterial to the complete sum but fixed in the native pairing. With f supported on [-t,t], F(u+iv)=hat{e^{v x} f}(u). Choose a smooth compact cutoff chi=1 on [-t,t]. Multiplication by chi(x)e^{v x} is bounded on X_t's Fourier norm uniformly over |v|<=3/2: the Fourier kernels are uniformly Schwartz, and with w(u)=log(2+|u|), w(u)^(1/2)<=C w(u-y)^(1/2) w(y)^(1/2); apply weighted convolution Young inequality. Hence
$$
\|Af\|^2\le B_t\|f\|_{\log}^2.
$$
The upper bound extends all evaluation maps by density; individual integral evaluations remain unchanged since they are L²-continuous on bounded support. The polarized full formula extends continuously to X_t, consistently on nested windows.

## 2. Unconditional positive-channel injectivity

Bui, Conrey and Young, *More than 41% of the zeros of the zeta function are on the critical line*, Acta Arith. 150 (2011), Theorem 1.1, proves liminf N_0^*(T)/N(T)>=0.4058 for simple critical-line zeros. Source https://arxiv.org/abs/1002.4127 (v2, first page checked). Only positivity of this lower bound is needed, not the numerical value or any newer claim. Riemann–von Mangoldt then gives at least c T log T distinct positive critical-line zeros for large T.

If A_+ f=0 for f in X_t, F=hat f vanishes at these distinct real ordinates (all such channels are positive). A nonzero entire F from supported L² f satisfies |F(z)|<=||f||_1 exp(t |Im z|); Jensen's formula centered at a fixed z0 with F(z0)!=0 bounds its zero count in radius R by O_f,t(R). This contradicts the superlinear distinct critical-line count. Thus A_+ f=0 implies F=0 and f=0. No zero-gap lower bound, RH, or finite-off-axis assumption.

## 3. Closed range uniformly over selected packets

X_t is a closed Hilbert space and embeds compactly into L² by the argument in 001E. If no lower constant b_t>0 exists for A_+, choose ||f_n||_log=1 with A_+ f_n->0. Extract a weak X_t / strong L² subsequence converging to f. Boundedness implies A_+ f=0, hence f=0. The lower estimate with L² defect then contradicts norm_log=1. Therefore
$$
b_t\|f\|_{\log}^2\le\|A_+ f\|^2\le\|A_\Pi f\|^2\le\|Af\|^2\le B_t\|f\|_{\log}^2.
$$
Constants do not depend on Pi. All these raw ranges on X_t are closed, with unique physical preimage, and equal the closures of smooth supported analysis ranges. This does NOT assert that the Green synthesis itself has closed range in its native energy metric.

## 4. Right-support continuity for ordinary selected markers

Fix Pi and define R_Pi,t=A_Pi X_t, G_Pi,t=R_Pi,t^perp in the selected coefficient Hilbert space. On a common larger support T, injectivity implies that a vector belonging to every R_Pi,t with t>c and t<T has the same unique physical preimage in X_T; it is supported in the intersection [-c,c]. Thus
$$
\bigcap_{t>c}R_{\Pi,t}=R_{\Pi,c},\qquad
\overline{\bigcup_{t>c}G_{\Pi,t}}=G_{\Pi,c}.
$$
Decreasing-gap projections converge strongly from the right (as t decreases, the G spaces increase). With ell the finite selected coordinate projection, compression gives
$$
\lim_{t\downarrow c}\|\Gamma_{\Pi,t}-\Gamma_{\Pi,c}\|=0,\quad
\Gamma_{\Pi,t}=\ell P_{G_{\Pi,t}}\ell^*.
$$
At a genuine selected first contact with W_Pi nonnegative on smaller windows, inward approximation shows W_Pi,c>=0; since W_Pi(f,f)=||A_Pi f||²-2||ell A_Pi f||², this is equivalent to Gamma_Pi,c>=I/2 by orthogonal projection duality. Hence Gamma_Pi,+ = Gamma_Pi,c >= I/2. This pays the right-jump half-bound for the ordinary raw finite selected marker at its own first contact, even with infinite omitted background. It does not prove a half-bound at arbitrary support. Native ordinary Picard marker transfer requires the exact signed-column metric and test-class audit of 001F; alternative indefinite restoration/limit constructions are not automatically identified.

If a selected form has negative directions in every larger window, finite dimension and right continuity force E=ker(Gamma_Pi,c-I/2) nonzero. A selected first contact is guaranteed for at least one finite packet if the full Weil criterion yields a negative smooth test: full negative sum converges by the sampling bound, so a sufficiently large finite selected sum already yields negativity. Initial full positivity implies selected positivity. No assertion that an arbitrary packet has a first contact is made.

## 5. Unconditional physical neutral attachment, infinite-background obstruction remaining

For u in E, v=P_Gc ell*u and J_Pi=I-2ell*ell, the identity J_Pi v=-P_Rc ell*u gives unique k_u in X_c with A_Pi k_u=J_Pi v and selected analysis -u/2. Thus k_u is nonzero iff u is nonzero and W_Pi(k_u,h)=0 for all h in X_c. For t>c,
$$
v\in G_{\Pi,t}\iff W_\Pi(k_u,h)=0\quad\forall h\in X_t.
$$
This is exact for the raw selected model, with no finite-exception hypothesis. Equivalently the full physical distribution W k_u is forced on the larger window by minus the omitted negative covariance; define that covariance through its bounded pairing on X_t, not by presuming pointwise convergence. The infinite forcing need not have finite exponential span. 001D/001F therefore do not yet exclude this case. No theorem asserting analytic regularity, finite annihilation, or exact persistence of the infinite background is supplied.

A corollary for the complete raw model: its closed range holds unconditionally too, and for any half-threshold vector (now the full negative space may be infinite-dimensional) the same projection construction produces a physical null mode; 001D excludes nonzero persistence. Do not infer norm continuity of the compression to the full infinite negative space or existence of a half-threshold vector from absence of a uniform margin.

## 6. Disposition

The finite-background annihilator mechanism cannot simply be taken to an infinite limit. This pass instead eliminates raw range escape and the ordinary finite selected right jump using established actual zeta arithmetic (simple critical-line density and local total count) plus logarithmic physical coercivity. No RH, selected infinite-background persistence rigidity, native indefinite-restored endpoint identification, or Lean verification is claimed. Historical general MTP-1 is only paid for the ordinary raw selected marker with the stated first-contact hypotheses, not every historical construction. Novelty has not been checked comprehensively.

Next: audit whether the infinite omitted forcing can have the exact larger-window support identity with a compactly supported selected null mode, now with physical attainment available; otherwise adjudicate the reconciliation by its proven finite-background falsification and explicit unresolved infinite case. No stay released.
