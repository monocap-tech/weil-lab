# NF467 — Original J7 macroscopic mean as a source-linear functional

**2026-11-07. Standing: ACCEPTED exact operator reduction; original source-native numerical mean NOT CERTIFIED.** Parent NF466 PR #494 (focused algebra CI #42405913415 SUCCESS). Canonical W-ODD-NEG OPEN.

## Original source and exact panel

Original NF407 SHA256 `0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce`; NF406 physical seams SHA256 `c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675`. Let B=11/10, I=[26/25,53/50], L=1/50, and U the unchanged original 246-source odd compact carrier. NF446 gives the **complete joint** arch response J_U(x), with its pole cancellation already performed.

Write the exact physical regular response on this fixed original J7 cell in the form

[
z(x)=\mathcal J_U(x)-\sum_{n\in S_7}w_n[U(x-\log n)+v]-H_{404}(x),
\quad S_7=\{2,3,4,5,7,8\},\quad v=U(B),
]
where w_n are the **original** NF405 regular prime-power coefficients (do not silently replace them by a different principal-jump convention), and H_404 is the unchanged original dyadic/sinh centering. This equation is the NF446 original physical-cell convention; any future evaluator must import its precise weights and centering from native source, not substitute illustrative constants.

Define A_I f=(1/L)int_I f(x)dx. Then the exact desired mean is

[
\boxed{
\bar z=A_I\mathcal J_U
-\sum_{n\in S_7}w_n\left[
\frac{\mathcal U(b-\log n)-\mathcal U(a-\log n)}L+v\right]
-A_I H_{404},
}
]
where a=26/25, b=53/50 and \mathcal U is **any antiderivative of the original physical U** on [-B,B]. The original U consists of finitely many polynomial-exponential/sine/hyperbolic generators, so each translated primitive difference can be evaluated sourcewise using the original coefficient intervals. No prime-translation x-quadrature is necessary. All arguments x-log n stay on the physical support on genuine J7; this is a support condition inherited from NF406, not from rational panel endpoints.

The only unresolved component of the mean is the **joint compact arch source functional** A_I J_U (plus direct source-native primitive evaluation of the finite prime/centering terms). In particular, computing independent digamma and exterior image terms is invalid due to NF445 catastrophic cancellation. Keep the five terms of NF446 J_U together with shared U and v source coefficients before interval evaluation.

## Linear source adjoint formulation

If the original source is U=sum_j c_j phi_j, including the pole/critical generators with their original correlation and finite-source radii, the NF446 compact identity is linear in U. Consequently
[
A_I\mathcal J_U=\sum_j c_j\, A_I\mathcal J_{\phi_j},
]
provided the original source linear combination is retained **jointly** (not separate absolute envelopes of huge exterior image terms). The 273 original frequency/order groups may be used as the evaluation basis, but they do not authorize a new 273-free-coefficient surrogate. The mean is a single scalar linear functional of the **same** original coefficient vector. This makes an adjoint/weighted-panel integration viable: compute the compact kernel panel-integrated once per original grouped generator, then contract with the original coefficients with outward error.

### Acceptance and error ledger

An accepted numeric interval for zbar requires separately auditable enclosures for: (1) all 273 grouped original joint compact arch panel integrals; (2) original 246-source coefficient radii propagated in the same contraction; (3) the six original prime-power shifted primitive differences and their exact weights; (4) unchanged NF404 centering; (5) joint removable t=0 and moving-boundary a(x),b(x) numerical integration errors. It must reproduce independent original point/mean overlap where available. This pass computes **none** of those numerical intervals and therefore does not claim a source-certified zbar.

**Closed:** exact original J7 mean decomposition into a compact joint arch linear functional and six finite source-primitive shifts. **OPEN:** numerical A_I J_U, native coefficient contraction, actual zbar, covariance, variance, signed D_I, whole D7/D8, NF404, W-ODD-NEG and RH.

**Next bold NF468:** implement one source-native joint compact arch panel integration with rigorous interval error and coefficient contraction; prioritize a single grouped source contribution and prove an aggregate error budget before claiming the complete original mean.
