# SM46 — Source-affine physical Fourier cells and explicit coupled original 25×25 positive source matrix

**October 18, 2026 · canonical W-ODD-NEG · stacks on SM45 draft #227, whose final-head focused CI passed.**

## Rationale: account for source Fourier variation rather than charge it to error

SM45 passed the original true 25-source zero-extended physically supported odd source-window Fourier certificate with original signed seven-prime/digamma positive-frequency multiplier. On the SAME original 16 source-centered positive-frequency windows (measure **1029/64**), its original full source-coordinate 1/8-cell **physical Fourier integration error** dropped from **1268.842380325** to **130.916378**, and complete Loewner error (including original multiplier weight error **45.610847484**) dropped from **1314.453228** to **176.527225**. All 625 entries of the original rational SM44 positive source-window matrix remain unchanged. However even 176.5 is enormous relative to the original matrix diagonal range 0.3557–4.6538. A further global scalar Lipschitz refinement cannot by itself prove the complete original odd signed operator.

**SM46's new mathematical target is a SECOND-ORDER physical Fourier approximation**, integrating the first-order *source transform variation* into the rational matrix itself. This is different from reducing the magnitude of the error term for the same matrix.

## Original genuine odd source Fourier derivatives, fully audited by exact physical formulas

Let \(B=11/10\), and let \(T_g(\xi)=\int_{-B}^B g(x)\sin(2\pi\xi x)\,dx\) for one actual original SI10 supported odd source. The unchanged physical basis is sixteen \(\sin(2\pi c_jx)\), eight \(x\cos(2\pi c_jx)\), and the actual \(s(x)=\sinh(x/2)\).

Use original SM42 \(\pi\)-interval and rational period-reduced Taylor sine/cosine, together with exact trigonometric moments \(F_k(q)=\int_{-B}^Bx^k\{\cos,\sin\}(2\pi qx)dx\). With \(w=2\pi q\), the new **exact physical cubic sine moment** is
\[
\boxed{
F_3(q)=2\left(
-\frac{B^3\cos(wB)}{w}
+\frac{3B^2\sin(wB)}{w^2}
+\frac{6B\cos(wB)}{w^3}
-\frac{6\sin(wB)}{w^4}
\right),\quad F_3(0)=0.
}
\]
It is an antiderivative identity, not a sampled numeric approximation. Original actual sine-source first/second frequency derivatives are
\[
\begin{aligned}
T'_{\sin_c}(\xi)&=\pi\big(F_1(c-\xi)+F_1(c+\xi)\big),\\
T''_{\sin_c}(\xi)&=2\pi^2\big(F_2(c+\xi)-F_2(c-\xi)\big),\\
T'_{x\cos_c}(\xi)&=\pi\big(F_2(\xi+c)+F_2(\xi-c)\big),\\
T''_{x\cos_c}(\xi)&=-2\pi^2\big(F_3(\xi+c)+F_3(\xi-c)\big),\\
T'_s(\xi)&=2\pi T_{x s,\cos}(\xi)
\end{aligned}
\]
with the already-certified original SM42 true pole \(T_{xs,\cos}\). For the actual original \(\sinh(x/2)\) second derivative, use the inherited strict whole-support spatial-moment bound; no unsupported pole identity is inferred.

Exact original whole-real **third** frequency derivative bounds follow directly from
\[
|T'''_g(\xi)|\le(2\pi_{\rm up})^3\int_{-B}^B|x|^3|g(x)|\,dx.
\]
Since \(|\sin|\le1\), \(|\sinh(x/2)|<1\), \(|x\cos|\le|x|\), the true supported source-specific rational upper is \((2\pi_{\rm up})^3B^4/2\) for sin and pole, or \((2\pi_{\rm up})^3(2B^5/5)\) for xcos. This locally improves the true second-derivative envelope via
\[
K_{j,I}=\min\{K_{j,\rm global}^{SM45},
|T_j''(\xi_I)|_{\rm up}+M_{3,j}|I|/2\}.
\]
All frequency points in the source cell are included.

## The true original affine physical-source approximation

For any original rational real frequency cell \(I=[a,b]\), midpoint \(\xi_I\), and \(h=b-a\), compute exactly-rational-enclosed \(T_j(\xi_I)\) and \(T_j'(\xi_I)\) and select rational centers \(v_{j,I},d_{j,I}\). The true original supported Fourier amplitudes obey
\[
\boxed{
T_j(\xi)=v_{j,I}+d_{j,I}(\xi-\xi_I)+r_{j,I}(\xi),\qquad
|r_{j,I}(\xi)|
\le r^{(0)}_{j,I}+\tfrac h2r^{(1)}_{j,I}
+\tfrac18K_{j,I}h^2.
}
\]
The radius of both genuine original midpoint physical source intervals and the Taylor second-derivative allowance is paid for every real \(\xi\in I\), not sampled at Gauss nodes.

SM43A's true original positive scalar reference \(w_I(\xi)\) is unchanged: either the verified original constant cell weight or \(\max\{\kappa,q_I(\xi)\}\) where \(q_I\) is its exact rational endpoint-signed multiplier interpolant. Its actual unknown original \(m(\xi)=\kappa\) crossings remain covered by SM43A's already-certified whole-real multiplier error; the *reference* has at most one rational crossing and its moments
\[
J_{k,I}=\int_I w_I(\xi)(\xi-\xi_I)^k\,d\xi,\qquad k=0,1,2,
\]
are integrated by exact rational polynomials, splitting at the reference kink as required. All three moments are outward-error-paid when quantized.

The **full coupled 25×25 original source-affine rational matrix** is
\[
\boxed{
P_{46}=2\sum_I\left(
\widetilde J_{0,I}v_Iv_I^T+
\widetilde J_{1,I}(v_Id_I^T+d_Iv_I^T)+
\widetilde J_{2,I}d_Id_I^T
\right).
}
\]
It includes every odd source cross and true pole interaction; no diagonal-only or sample spectral proof.

For \(E_I=\sum_j(r^{(0)}+r^{(1)}h/2+K_jh^2/8)^2\), entire original source sup \(S_I=\sum_j s_{j,I}^2\), and affine source sup \(V_I=\sum_j(|v_j|+|d_j|h/2)^2\), the full rank-one form difference is bounded by
\[
\|T(\xi)T(\xi)^T-V(\xi)V(\xi)^T\|
\le \sqrt{E_I}\bigl(\sqrt{S_I}+\sqrt{V_I}\bigr).
\]
All roots have exact integer-isqrt upward rational enclosures, so the Fourier error is
\[
\epsilon_{I,\mathrm{aff}}\le
2J_{0,I}\sqrt{E_I}(\sqrt{S_I}+\sqrt{V_I})+
2|\delta J_0|\|v\|^2+
4|\delta J_1|\|v\|\|d\|+
2|\delta J_2|\|d\|^2.
\]
A stronger strictly **fail-closed cellwise comparator** retains the original SM45 midpoint reference and its independently already-certified exact source error when \(\epsilon_{\rm aff}\ge\epsilon_{\rm SM45,cell}\). This guarantees SM46's whole coupled source Fourier error **cannot increase** from SM45 before outward rounding. The original SM43A scalar multiplier error remains **identical**.

**Meaningful acceptance requirement:** at the SAME original 1/8 frequency mesh and same original source-window union, require the full certified source Fourier error to drop **at least 5% versus SM45**. Also prove strict 1/4→1/8 mesh error contraction. If the exact-replay fails that threshold, do NOT relax it or claim the affine scheme passed.

## Scope/next dependency

This would produce a complete original physical 25×25 rational source-window positive stiffness enclosure—**not** the complete low-frequency positive operator. The unchanged true source-window union has measure \(1029/64\) and leaves most of the true original real \([0,4096]\) low band unprocessed at this precision. The original SM41 full positive digamma logarithmic high tail, SM42 physical full Gram and pole, and SM40 complete negative-frequency upper are separate valid pieces; they do not automatically compose without the complete true original Astar inverse/strong resolvent. All original 470 supported higher-degree physical generators and a complete O1/O2 signed odd operator test remain unfinished, as do original even E1-E4, whole Weil positivity, native CC27 transfer and RH.

**SM47:** inspect measured cellwise constant-versus-affine selection and remaining full 25×25 errors. If source window error is still excessive, target matrix/source-scaled Loewner and exact analytic higher-order source transforms. Independently extend true original positive low integration over **ALL real frequencies** \([0,4096]\) and develop all 470 original higher-k source derivatives before attempting the complete corrected Schur. Preserve the canonical W-ODD-NEG acceptance gates and independent original Fourier/form-domain audit.

Replay \`python3 scripts/validate_rpb108_sm46_affine_physical_fourier_source.py\`, generating an explicit rational 25×25 matrix and exact Loewner budget in \`artifacts/sm46_original_source_affine_physical_fourier.json\`.
