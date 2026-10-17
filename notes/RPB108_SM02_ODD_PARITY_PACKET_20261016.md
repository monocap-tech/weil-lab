# RPB108 SM02 — odd-parity compression of the full original negative-frequency packet bridge

**Obligation:** W-ODD-NEG (original signed odd Weil form).  
**Parent:** SM01 merged; governance manifest active at research HEAD 64679855c6cf41fab673e32a628cc5f92ed587ce.  
**Standing:** analytic parity-compression theorem with a replayable exact-rational dimension/error regression, conditional on SI10–SI11 original signed-frequency cover and the SI29 pole result. **No full-negative-frequency finite eigenvalue or original odd positivity is certified.**

## 1. A concrete structural reduction, not a new frequency-band sweep

Let \(I=[-B,B]\), \(B=11/10\), \(H_o=L^2(I)_{\mathrm{odd}}\). The original multiplier \(m(\xi)\) is even. SI11's *actual signed* decomposition sets \(\kappa=10^{-3}\),
\[
a(\xi)=\max(m(\xi),\kappa),\quad r(\xi)=(\kappa-m(\xi))_+,\quad
Q_o=A_o-K_{{\rm freq},o}-2|s\rangle\langle s|,
\]
where \(A_o\succeq\kappa I\), \(K_{{\rm freq},o}=Z^*\mathcal F^{-1}r\mathcal F Z|_{H_o}\), \(s(x)=\sinh(x/2)\).
The exact cover has positive-frequency components \(J_j=[a_j,b_j]\), \(j=1,\ldots,107\), with reflected companions, width \(w_j=b_j-a_j\), center \(c_j\), and **full reflected** mass \(\int_{\mathbb R}r\le R=1204033883/32000000\). These constants refer to the *original seven signed prime powers* and physical zero extension, not a toy multiplier.

SI10–SI11 select a per-cluster Taylor order \(p_j(b)\) with the certified uniform remainder \(\varepsilon=2^{-b}\) for each supported plane wave in the cluster. Their full-space comparison uses \(\le 1+2\sum_jp_j\) physical directions.

The parity projection \(\Pi_o f(x)=(f(x)-f(-x))/2\) maps the two reflected bases into a **single** odd basis per center:
\[
q_{jk}(x)=\tfrac12\big[e^{2\pi i c_jx}x^k-
(-1)^ke^{-2\pi i c_jx}x^k\big],\qquad 0\le k<p_j.
\]
For even \(k\), this is \(i\,x^k\sin(2\pi c_jx)\); for odd \(k\), it is \(x^k\cos(2\pi c_jx)\). Both are odd on the physical support, and each is an odd projection of a valid SI10 modulated polynomial. Set
\[
W_{b,o}=\operatorname{span}\{q_{jk}:j\le107,\;k<p_j\}
+\operatorname{span}\{s\}\subset H_o,\quad
P_{b,o}=P_{W_{b,o}}.
\]
**Theorem SM02-A (parity halving).** The physical odd packet space satisfies
\[
\boxed{\dim W_{b,o}\le 1+\sum_jp_j(b)}
\]
rather than \(1+2\sum_jp_j(b)\). No rank independence assumption is needed: this is an upper bound. All per-cluster truncation orders, continuous signed-frequency cover, and pole vector are **unchanged**.

## 2. Original full-negative-frequency residual, preserved under parity compression

For \(\xi\in J_j\), apply the *orthogonal contraction* \(\Pi_o\) to SI10's plane-wave Taylor approximant about \(c_j\). Its error is still at most \(\sqrt{2B}\varepsilon\). On the odd carrier, the analysis functional depends only on this projected approximation. At \(-J_j\), reflection gives the same bound. Thus for every odd \(f\perp W_{b,o}\),
\[
|\widehat{Zf}(\xi)|\le\sqrt{2B}\varepsilon\|f\|_2\quad(\xi\in U).
\]
Writing \(K=K_{{\rm freq},o}\succeq0\), the actual positive representation
\[
K=\int_{\mathbb R} r(\xi)\,|h^o_\xi\rangle\langle h^o_\xi|\,d\xi,\quad
h^o_\xi=\Pi_o(e^{2\pi i\xi x}\mathbf1_I)
\]
with \(\|h^o_\xi\|\le\sqrt{2B}\), \(\|(I-P_{b,o})h^o_\xi\|\le\sqrt{2B}\varepsilon\), proves
\[
\boxed{\|K-P_{b,o}KP_{b,o}\|\le\eta_b=4BR\,2^{-b}},\qquad
\boxed{\|(I-P_{b,o})K(I-P_{b,o})\|\le2BR\,2^{-2b}}.
\]
The first uses the two-term rank-one decomposition with \((I-P)h\); the second uses its square. The pole \(2|s\rangle\langle s|\) is **exactly** inside \(W_{b,o}\) and contributes no approximation error.

This is a theorem about the *full original* negative-frequency operator and its physically supported odd compression. It does not estimate the unknown finite matrix eigenvalues.

**Corollary SM02-B (true original odd complement).** For odd \(f\perp W_{b,o}\), orthogonality to every odd projection implies orthogonality to the original SI10 full packet basis and to \(s\). Therefore SI10's original-form complement positivity applies with the same strict rational \(L^2\) floor and the reduced odd codimension. In particular, with \(b=9\), a physical odd subspace of codimension at most **470** contains *every possible nonpositive odd direction modulo the usual form-domain qualification* (the original full-space SI10 bound is 939). The compressed finite block and its cross terms remain open; this is not full odd positivity.

## 3. Correct complete-pole finite Birman–Schwinger gate with the better error denominator

Let \(U_b:\mathbb C^{d_b}\to H_o\) be **orthonormal** synthesis onto \(W_{b,o}\), \(d_b\le1+\sum_jp_j\), and \(t_b=U_b^*s\). Define
\[
D_b=U_b^*K_{{\rm freq},o}U_b,\quad
M_b=D_b+2|t_b\rangle\langle t_b|\succeq0,\quad
G_b=U_b^*A_o^{-1}U_b.
\]
Crucially \(D_b\) contains the *entire original signed negative-frequency multiplier* through \(K_{{\rm freq},o}\), not one sampled negative band. The full pole-frequency cross coupling is retained by \(M_b^{1/2}G_bM_b^{1/2}\). Since \(A_o\succeq\kappa I\), the **sufficient** gate
\[
\boxed{
\lambda_{\max}\big(M_b^{1/2}G_bM_b^{1/2}\big)
+\frac{\eta_b}{\kappa}\le1
\ \Longrightarrow\ Q_o\succeq0 .
}
\]
This uses the original positive operator \(A_o\) *before* rank-one pole absorption. Consequently the full negative-frequency residual is divided by \(\kappa\), **not** \((1-L)\kappa\) with \(L=0.966379\). SM01's post-pole denominator would enlarge this coarse error by about \(1/(1-L)\), nearly 30-fold. Both approaches are valid sufficient conditions, but retaining the pole in the **finite matrix** is better conditioned for the approximation error.

For a trial inverse response \(Y:\mathbb C^{d_b}\to\operatorname{Dom}A_o\), set \(E_b=U_b-A_oY\). The exact correct-sign physical inverse identity gives
\[
G_b=U_b^*Y+Y^*U_b-Y^*A_oY+E_b^*A_o^{-1}E_b
\preceq U_b^*Y+Y^*U_b-Y^*A_oY+\kappa^{-1}E_b^*E_b.
\]
A valid future check must certify an **upper** Loewner enclosure for \(G_b\), preserve all cross-Gram entries in \(M_b\), and prove the finite eigenvalue is beneath \(1-\eta_b/\kappa\). No unrestricted whole-line reciprocal and no independent/uncoupled pole test may replace it.

## 4. Quantitative new rank frontier (all counts upper bounds)

| \(b\) | Old full SI11 rank bound | New odd rank bound | \(\eta_b/\kappa\) upper from exact SI11 budget |
|---:|---:|---:|---:|
| 9 | 939 | 470 | 323.349 |
| 10 | 1003 | 502 | 161.675 |
| 12 | 1121 | 561 | 40.419 |
| 16 | 1367 | 684 | 2.527 |
| 20 | 1561 | 781 | 0.157886 |
| 21 | 1631 | 816 | 0.078943 |
| 24 | 1781 | 891 | 0.009868 |
| 32 | 2151 | 1076 | 0.000038547 |

The \(b=24\) and \(b=32\) gates now ask for a positive operator finite block with at most **891** or **1076** odd physical directions, rather than **1781** or **2151** full-space directions. The numbers are dimension **ceilings**, not eigenvalue certificates and not matrix computations already performed. At \(b=9\), SI10 complements are positive on a much smaller **odd** exceptional space, although \(\eta_9/\kappa\) is too large to use the coarse full operator perturbation gate.

The independent RC314 route already localizes a possible-negative sector to dimension 301 in a *different weighted native carrier*. Do not conflate that localization with this physically orthonormal SI11/SM02 negative-frequency matrix; reconciliation may yield a better route but requires an explicit transport theorem.

## 5. Next obligation-facing action

**W-ODD-NEG stays OPEN.** After SM02, the next valuable action is to build/estimate one **original signed finite odd packet column**, with the complete pole-frequency cross response and rigorous supported \(A_o^{-1}\) bound. Compare the \(b=20,24,32\) odd-basis cost against RC's native 301-dimensional localization. If the 14-feature \(C_{14}\) reference cannot capture the negative packet, show a *method-class obstruction* before scaling it; failure of a lower reference is **not** failure of the original \(A_o\).

**Reproduction:** `python scripts/validate_rpb108_sm02_odd_packet_parity.py`. It reconstructs SI10's signed rational cover, verifies parity counts and both exact residual budgets, and checks a correct-sign coupled algebraic regression. Rational assertions do **not** independently establish the analytic Fourier/parity theorem, original form positivity, Stage I, LF or RH.
