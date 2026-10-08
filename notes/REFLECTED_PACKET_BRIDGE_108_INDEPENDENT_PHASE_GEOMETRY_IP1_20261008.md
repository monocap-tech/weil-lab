# RPB108 — Independent phase-geometry / source-localization investigation (IP1)

Date: 2026-10-08. Independent exploratory branch based on Coupled CC30 `3d67de4ba4c44c6b4e164ee064663cc531a04527`. This is **not** a CC31 theorem, new aperture, Lean certificate, or reopening of paused Global/Aperture/Pre-Contact Shadow branches.

## 0. Audit and classification

**Status: analytic/conditional exploration.** The elementary Fourier, hyperbolic, matrix and finite-model identities below are derived explicitly. Their attachment to the full actual source on the canonical completion uses existing source decomposition, observability and arithmetic density hypotheses; a complete independent analytic/Lean verification is **not** claimed. No actual critical eigenvector, whole critical source covariance, or new original finite-cap source inverse is evaluated.

The local standing remains the internally certified whole-domain original positivity through `a=21/20` (CC18), even0/odd0. CC29 offers a weaker vanishing-modulus endpoint sufficiency criterion; CC30 classifies an every-height transverse sampling premise as Lindelof-strength. Neither result authorizes promoting the packet estimates below into an all-cap non-stalling theorem.

**Key result:** individual source-profile phase separation and moment cancellation can be quantified, but the full positive-source inverse can mediate off-diagonal coupling through omitted directions. The remaining interesting target is a WHOLE-COMPLEMENT positive-metric localization estimate plus defect-relative control on actual critical modes; ordinary packet correlations are insufficient.

## 1. Original source profiles and symmetry gate

Use the normalized full-divisor pair laws from CC20 (not raw double-counted forms), with every partner and multiplicity copy:
\[
 p_q(h)=\int h(x)e^{i\theta_q x}\cosh(\beta_q x)\,dx,\qquad
 n_q(h)=\int h(x)e^{i\theta_q x}\sinh(\beta_q x)\,dx.
\]
The original Q is P*P-N*N and `M_a=P_a^*P_a` acts on the canonical logarithmic carrier. The indices q may repeat at multiplicity. Reflection `beta -> -beta` makes p even and n odd. Therefore the negative-source range is inside the reflection-odd output sector, and `A_a=T_a T_a^*` annihilates the reflection-even output sector. Under RH the negative channel vanishes; this observation is not a proof of RH.

A unit circle governs ordinate phases `exp(i theta r)`, while the displacement `beta` gives the hyperbolic `sinh/cosh` factor. The critical spectral projection acts in the full negative SOURCE output space, not in physical frequency coordinate space.

## 2. Crowding and cluster moment filtration

On the fixed finite physical interval `[-B,B]`, set `phi_j(x)=exp(i theta_j x) sinh(beta_j x)`. The classical total zero counting forces close ordinates among ALL high zeros, but **does not** establish close OFF-CRITICAL pairs; their existence is unproved and could be false.

For two off-critical locations in the accepted displacement strip `|beta|<=kappa=3/8`, the mean-value estimate is
\[
\|\phi_1-\phi_2\|_{L^2(-B,B)}
\le \sqrt{2B}\,B\{\sinh(\kappa B)|\Delta\theta|
          +\cosh(\kappa B)|\Delta\beta|\}.
\]
For a cluster `|Delta theta_j|, |Delta beta_j|<=epsilon`, the two-variable Taylor expansion around its center has leading profiles `phi_0, partial_theta phi_0, partial_beta phi_0`. Any coefficient vector annihilating the three scalar moments has profile norm bounded by a cap-dependent `O(epsilon^2 sqrt(m)||alpha||)`, with actual orbit weights included in the weighted version. Higher moment cancellations yield further powers of epsilon. This controls raw source-profile SYNTHESIS, not the full critical inverse reaction.

If `c_B||h||_D <= ||P h||` and `||h||_2<=e_B||h||_D` are the existing canonical positive observability and physical embedding bounds, the negative adjoint gives
\[
 \|T_s^* y\|\le (e_B/c_B)\|N_s^* y\|_{L^2\ {\rm profile}}.
\]
For `E_eta=1_[1-eta,1](T_s T_s^*)` with `0<eta<1`,
\[
 \|E_\eta y\|\le (1-\eta)^{-1/2}\|T_s^*y\|.
\]
Thus tightly clustered moment-cancelling negative-output directions are weakly represented in the near-unit critical output, conditional on the above actual source-carrier attachment and consistent multiplicity normalization. Coherent cluster directions need not be weak; finite rank alone supplies no defect factor.

## 3. Exact finite-packet physical Gram and phase sign

For two profiles, with `omega=theta_j-theta_i`,
\[
 K_{ij}=\int_{-B}^B e^{i\omega x}\sinh(\beta_i x)\sinh(\beta_j x)\,dx
  =\tfrac12[F_B(\beta_i+\beta_j,\omega)-F_B(\beta_i-\beta_j,\omega)],
\]
\[
 F_B(b,\omega)=2\,{\rm Re}\left(\frac{\sinh((b+i\omega)B)}{b+i\omega}\right),
\]
with continuous limiting values at removable singularities. Original orbit/multiplicity weights multiply the entries.

For `beta_i=beta_j=beta!=0`, `B=1`, `theta_j-theta_i=pi`:
\[
 d=\sinh(2\beta)/(2\beta)-1,\quad
 c=-2\beta\sinh(2\beta)/(4\beta^2+\pi^2)<0.
\]
At `beta=0.1`, `d=0.00668001270547`, `c=-0.00406345186734`. Therefore the coefficient DIFFERENCE (1,-1)/sqrt(2) has larger raw Gram energy than the sum; a priori identifying the coherent packet with equal positive coefficients is wrong. These are model profile parameters, not observed zeta zeros.

For any finite packet set C, the canonical positive inverse comparison has the form
\[
 A_C=N_C M_s^{-1}N_C^* \preceq (e_B/c_B)^2 K_C,
\]
where `K_C` is the weighted physical profile Gram and the domain/adjoints are those of the source-carrier specification. This is an UPPER comparison, not identity of physical and positive-source inverse metrics.

## 4. Ordinary interpacket frequency separation

For `omega=theta_j-theta_i!=0`, integrate the preceding physical Gram by parts. The boundary and derivative terms give
\[
 |K_{ij}|\le D_B/|\omega|,
 \quad D_B=2\sinh^2(\kappa B)+4B\kappa\sinh(\kappa B)\cosh(\kappa B).
\]
If two finite unweighted packets of sizes m,n have pairwise frequency separation at least Omega, then
\[
 \|K_{12}\|\le D_B\sqrt{mn}/\Omega.
\]
For weighted original partner copies, total weight factors replace m,n. This is physical profile locality, NOT a bound on the full inverse-weighted critical correlation or arbitrary zeta modes.

## 5. Smooth-modulated physical packets: available source localization

For fixed compact smooth f,g supported in (-B,B), define `h_R(x)=exp(-iRx)f(x)`, `k_S(x)=exp(-iSx)g(x)`. Repeated integration by parts, uniformly for `|beta|<=kappa`, gives for every n:
\[
 |p_q(h_R)|\le C_{B,f,n}(1+|\theta_q-R|)^{-n},
 \quad |n_q(h_R)|\le C_{B,f,n}|\beta_q|(1+|\theta_q-R|)^{-n}.
\]
The unconditional Riemann-von Mangoldt unit-height count `O(log(2+T))`, together with sufficiently high powers, gives for any desired `k>=1`
\[
 |\langle P h_R,P k_S\rangle|+|\langle N h_R,N k_S\rangle|
 \le C_{B,f,g,k}\frac{\log(e+|R|+|S|)}{(1+|R-S|)^k}.
\]
This is a **fixed-test, not whole-column**, bound. Its constant depends on f,g and k. The test family does not span an invariant subspace of `M_s` with certified uniform localization.

Using the CC22 inherited cumulative transverse moment `Z_2(T)\ll T(\log\log T)^2/\log T`, a dyadic average in `R in [T,2T]` gives a *candidate analytic corollary*, subject to the exact CC22 count and source normalizations:
\[
 T^{-1}\int_T^{2T}\|Nh_R\|^2dR
 \ll_{B,f}(\log\log T)^2/\log T.
\]
Since the original native logarithmic multiplier yields `Q(h_R,h_R)=||f||_2^2\log T+O_{B,f}(1)` for fixed f as T grows, the corresponding averaged negative/positive source-energy ratio is `O((loglog T)^2/(log T)^2)`. Neither averaging nor fixed f establishes an every-height local count or an adaptive critical-mode bound. **Do not cite this analytic deduction as a replayed numerical certificate**.

## 6. Precise full-inverse obstruction and a smaller next gate

For any bounded self-adjoint `M\succeq m I` and orthogonal projection `Pi` in the SAME canonical Hilbert space,
\[
 [M^{-1},Pi]=-M^{-1}[M,Pi]M^{-1},
 \quad \|\Pi M^{-1}(I-\Pi)\|\le m^{-2}\|\Pi M(I-\Pi)\|.
\]
A test on two selected packet vectors does **not** bound this whole-column coupling.

Exact finite control:
\[
 M=\begin{pmatrix}1&0&1/2\\0&1&1/2\\1/2&1/2&1\end{pmatrix},
 \qquad
 M^{-1}=\begin{pmatrix}3/2&1/2&-1\\1/2&3/2&-1\\-1&-1&2\end{pmatrix}.
\]
`M` has eigenvalues `1,1+1/sqrt(2),1-1/sqrt(2)`, hence is uniformly positive. Even though `M_12=0`, `(M^-1)_12=1/2`. The third unobserved direction mediates the interaction. This is a generic positive-metric control, **not** actual zeta arithmetic.

The exact original identity is `M=Q+N^*N` in the canonical form representation; the native prime-archimedean-pole equality fixes Q. It does not by itself give the `whole-complement` operator norm of `(I-Pi)M Pi`, nor the defect-weighted critical covariance. The next genuinely weaker-than-RH research gate is:

(1) Specify a canonical frequency-packet projection Pi with rigorous operator-domain and physical embedding control.
(2) Prove a COMPLETE, cap-effective bound `||(I-Pi)M Pi||` against every complementary direction, not only selected smooth packets.
(3) Prove a separate approximation/selection estimate attaching the ACTUAL critical source rows to that packet space, with source-defect-scale error rather than old-gap division.
(4) Check genuine crossing, full positive-level mass and CC25 full-identity custody; avoid promoting finite altered zero sets to models of the SAME Weil formula.

## 7. Jurisdiction and handoff

This branch is an independent analytic investigation only, not a new active RPB108 integration frontier. Coupled remains the sole active integration thread. The paused Global/F4, Aperture and Pre-Contact Shadow notes can cite these formulas as exploratory dependencies, not as certified new aperture or independent non-stalling hypotheses.

**Certified standing unaffected:** whole-domain original positivity through `21/20`, no new aperture; no actual whole critical source covariance `J M_t^-1 J^*` or CC29 vanishing-modulus bound evaluated; no RH/F4, transport or Lean closure. Results in Sections 2–6 are conditional elementary analytic derivations and finite illustrative models; prior assistant explanations were not independently sourced, built or formally checked.

**Stopping rule:** If packet localization remains only a fixed-test bound or its transfer requires an uncontrolled `1/min(delta_i)`, classify the transfer as insufficient and stop. Do not replace the RH-equivalent global shell gate with yet another notation for the same missing correlation.

## Subsequent checkpoint

[IP2 — whole-column packet variance and positive-inverse countercontrol](REFLECTED_PACKET_BRIDGE_108_INDEPENDENT_PHASE_GEOMETRY_IP2_20261008.md) makes the canonical packet projection explicit, gives the exact positive-inverse Schur/residual comparison, and proves that even **perfect** positive-metric localization cannot alone exclude negative original-style shell reaction. IP1's fixed-test estimates remain exploratory, with no new original zeta bound or RH conclusion.
