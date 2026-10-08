# RPB108 — Independent phase geometry IP3: old-packet annihilation and outgoing-shell Gram certificate

Date 2026-10-08. Independent continuation of IP2 (latest initial head `4e225b006c75486e8c9743dc709bf31ea6b3155c`), read-only actual Coupled CC20 and CC31. **Result A:** exact quotient/shell operator identities and finite packet Gram + full-dual residual certificate. **Result C:** a packet trial confined to the old support has exactly zero CC20 forced pairing and cannot approximate the full inverse representer in the positive-source metric. No new actual arithmetic suppression, aperture, RH/F4, or Lean proof is claimed. Most of the quotient identities were ALREADY present in CC20; the explicit packet certificate and stopping rule clarify their proper use rather than claiming a new source-shell theorem.

## 1. Setup and completely forced quotient orthogonality

For 0<s<t<=B, let H_s=D_s be closed in H_t=D_t under the inherited isometric canonical inclusion i. Use complete normalized ORIGINAL P_t and N_t, all multiplicities/reflections/prime powers/poles, and M_t=P_t*P_t with M_t>=m_B I>0. The old source observability is protected independent of signed source defect.

Take an old critical generalized lift h_i in D_s, with lambda_i=1-delta_i>0. Its complete forced functional is
\[
J_i(f)=Q(h_i,f)-\delta_i\langle P h_i,P f\rangle,\quad J_i\circ i=0.
\]
Let j_i be its canonical Riesz representer in D_t, so j_i \perp iD_s in the CANONICAL metric. Let u_i=M_t^{-1}j_i. For all v in D_s,
\[
\langle P_tu_i,P_si v\rangle =J_i(iv)=0.
\]
Thus u_i belongs to the POSITIVE-metric-orthogonal outgoing shell
\[
Z_{st}=\{u\in D_t:\langle P_tu,P_s v\rangle=0\ \forall v\in D_s\}
       =P_t^{-1}(V_t\ominus V_s).
\]
The full dual norm obeys
\[
\boxed{\|J_i\|_{P_t^*}^2=\langle j_i,M_t^{-1}j_i\rangle
   =\|P_tu_i\|^2,\quad u_i\in Z_{st}.}
\]
For ANY old-support trial z=iv in iD_s, the positive-metric orthogonality is exact:
\[
\|P_t(u_i-z)\|^2=\|P_tu_i\|^2+\|P_s v\|^2.
\]
Equivalently, `||j_i-M_t z||_{M_t^{-1}}^2 = ||j_i||_{M_t^{-1}}^2+||P_t z||^2`. A trial confined to the old domain makes the exact inverse residual WORSE; no amount of modulating its frequency changes `J_i(z)=0`. The finite packet variational lower test restricted to D_s has optimum 0 at z=0. This is NOT a proof that the coarse upper estimate from IP2 never happens to improve numerically; it is a precise orthogonality obstruction to approximating the actual Riesz solution.

## 2. Exact quotient Schur and support-aware shell lift

Split the canonical H_t orthogonally as H_s \oplus W_0, with W_0=H_s^{\perp H_t}. Relative to this splitting,
\[
M_t=\begin{pmatrix}A&B\\B^*&C\end{pmatrix},\quad
j_i=(0,\xi_i).
\]
Here A>=m_B I. The quotient positive metric is
\[
S=C-B^*A^{-1}B\succeq m_B I,
\]
and the exact full dual norm is
\[
\boxed{\langle j_i,M_t^{-1}j_i\rangle
   =\langle\xi_i,S^{-1}\xi_i\rangle.}
\]
The minimizer over old corrections for an incoming canonical vector w in W_0 is `(-A^{-1}Bw,w)`; this identifies the quotient metric with the physical source shell `V_t\ominus V_s`.

In original CC20 notation, the positive-metric projection is
\[
R_s=i M_s^{-1}i^*M_t,\quad M_s=i^*M_t i.
\]
For ANY supported test f in D_t, define `z_f=(I-R_s)f`. Then `z_f\in Z_{st}`,
\[
 J_i(z_f)=J_i(f),\qquad
 \|P_tz_f\|=\inf_{v\in D_s}\|P_t(f-iv)\|.
\]
It is FALSE to replace `z_f` with a physical indicator of the exterior strip: the positive projection can have old-window corrections, and the canonical logarithmic Hilbert metric is nonlocal. The exact projection above was inherited from CC20, not newly discovered by IP3.

## 3. Finite outward packet Gram: a rigorous lower AND conditional upper certificate

Choose finitely many smooth f_a in C_c^infinity(-t,t) with support not necessarily inside (-s,s), and set z_a=(I-R_s)f_a. Let E be their span in Z_st and retain any exact linear dependence by using a pseudoinverse. Define
\[
\Gamma_{ab}=\langle P_tz_a,P_tz_b\rangle,\quad
v_a=J_i(z_a)=J_i(f_a).
\]
Then, with complex inner-product convention consistently adopted, the finite-shell restricted dual norm is `L_E=v^*\Gamma^\dagger v`. The finite optimal positive-metric packet trial `u_E\in E` satisfies `J_i(e)=\langle P_tu_E,P_te\rangle` for all e in E, and `||P_tu_E||^2=L_E`. The FULL forced-row norm has an exact orthogonal energy split:
\[
\boxed{
\|J_i\|_{P_t^*}^2
=L_E+\|j_i-M_tu_E\|_{M_t^{-1}}^2.
}
\]
Thus the genuinely useful validated enclosure is
\[
\boxed{
L_E\le \langle j_i,M_t^{-1}j_i\rangle
 \le L_E+m_B^{-1}\|j_i-M_tu_E\|_{D_t}^2. }
\]
It is obligatory to certify the residual over ALL of D_t, including exterior and old corrections. Finite packet tests alone supply only the LEFT inequality. A large L_E disproves a proposed small scalar bound; a small L_E never establishes it without the whole complementary tail.

The normalized CC31 sufficiency gate would require
\[
L_{E,i}+m_B^{-1}\|j_i-M_tu_{E,i}\|_{D_t}^2
 \le b_B\lambda_i\omega_B(\delta_i),\quad \omega_B(x)\to0,
\]
uniformly over old strictly source-positive s and nearby t in each finite cap. No such estimate is currently proved for actual zeta.

## 4. Exact source controls

**Positive-metric nontrivial model.** On H_t=C^2, let old H_s=span(e1), M=[[2,1],[1,2]], j=e2. Then `u=M^-1j=(-1/3,2/3)` lies in outgoing positive-orthogonal shell span((-1/2,1)), even though it has a nonzero OLD CANONICAL coordinate. The quotient Schur is 3/2, and the exact norm is 2/3. For old trial z=a e1, `||P(u-z)||^2=2/3+2|a|^2`. The finite new packet f=e2 orthogonalizes to (-1/2,1), and the one-packet Gram already captures the full 2/3 norm.

**Genuine signed reaction in a complete finite source control.** On H_t=C^2 with P=I, N=(3/4,3/4), old H_s=span(e1), the old source eigenvalue is lambda=9/16, defect delta=7/16. The actual forced functional formed from its old lift is `J(f)=-(9/16) f_2`. Its full dual norm is `81/256`, and division by lambda gives incoming critical covariance 9/16, old-defect-relative shell cost 9/7>1. The forced solution is entirely outgoing and the enlarged original-style Q has a negative direction. Thus outgoing-shell identification alone does NOT supply defect-relative decay.

**Omitted-shell tail model.** On C^3 with
\[
M=\begin{pmatrix}1&0&1/2\\0&1&1/2\\1/2&1/2&1\end{pmatrix},
\quad j=(0,1,1),\quad H_s={\rm span}(e1),
\]
the packet E=span(e2) is already outgoing. Its restricted Gram norm is 1; the full inverse norm is 3/2; the exact complementary tail is 1/2. With `m_B=1/4`, the conservative bound is `1<=3/2<=2`. An incomplete packet certificate can therefore underestimate the true covariance despite correct normalization and exact full positive metric.

All models are finite exact controls, NOT modifications of the actual zeta divisor or alternative assignments satisfying the same native explicit formula. No evidence for actual contact is claimed.

## 5. Decision and custody

**Positive advance:** a mathematically sound finite outward-shell packet certificate and a clear whole-residual upper-bound procedure, with exact quotient geometry. **Negative decision:** the old-window smooth modulations considered in IP1/IP2 are invisible to the CC20 forced row, even though they provide perfectly valid ordinary Fourier localization estimates. Sampling ever more old packets is not progress on the defect-relative residual.

This checkpoint does not derive an arithmetic upper bound on any actual critical row. The next feasible independent experiment is to construct smooth OUTWARD test packets crossing the old support boundary, source-orthogonalize using `R_s`, and compute their *native mixed* forced pairings with the actual old generalized lift. Such a computation still requires actual critical h_i data and a complete dual tail bound before it becomes a certificate.

Source custody: CC20's forced-row kernel/quotient identities, CC27's native exterior forcing, CC29's vanishing-modulus endpoint test, CC31's finite cap-uniform critical rank. Coupled remains the sole active integration frontier; Global NF71, Aperture and Shadow PS3 remain paused. No new aperture beyond 21/20, RH/F4, transport or Lean closure.

## 6. Reproducible finite control validation

The reproducible [IP3 exact rational validator](../scripts/validate_native_phase_packet_ip3.py) has been executed and passes **24 exact rational assertions**. It checks a nontrivial positive metric, forced-row/old-support orthogonality, exact outgoing quotient Gram, exact original-style 9/7 crossing cost, omitted-shell tail and a conservative whole-dual residual enclosure. These checks do not certify the actual zeta forced row or any infinite-dimensional theorem in Lean.
