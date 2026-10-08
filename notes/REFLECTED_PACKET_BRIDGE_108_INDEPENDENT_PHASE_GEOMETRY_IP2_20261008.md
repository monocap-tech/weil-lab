# RPB108 — Independent phase geometry IP2: whole-column leakage, exact packet Schur bound and signed countercontrol

Date: 2026-10-08. Parent: IP1 commit \`48d83c40c6fb4b3739de6e95f2e3b6659dfd0fb7\`. Source custody: Coupled CC31 \`00dfd25de49cb62c05caba8b365d7efaa7ea91ee\`, Global NF71, Shadow PS3. This is an independent mathematical checkpoint, **not** CC32, another certified aperture, a Lean proof, or a new integration research frontier.

## Result and scope

**A (exact structural identities):** There is a legitimate finite-dimensional smooth frequency-packet projection on the canonical supported Hilbert carrier. Its WHOLE-complement positive-source leakage is exactly the positive-operator variance, and the full positive inverse on that packet admits a rigorous Schur enclosure. A whole-dual-residual variational bound is valid for any actual CC20 forced row, with no unproved physical L2 source representative.

**C (decisive information limit):** Perfect positive-source frequency-packet localization is insufficient to bound the original negative-source shell reaction. An exact complete finite source model has \`M=P*P=I\` and zero positive-metric leakage but old strictly positive gain and a genuine negative direction in the enlarged signed form. The model is NOT zeta's divisor and does NOT preserve the native Weil explicit formula.

The actual packet localization and critical-row defect-scale estimates required below are **not computed** for zeta. Their availability is a new arithmetic question. Retain CC31's cap-uniform critical rank, CC29's weaker vanishing-modulus sufficiency, and the original whole-domain positivity anchor through \`a=21/20\`.

## 1. Legitimate packet projections under compact physical support

Fix finite B and the established canonical complex Hilbert carrier H_B=D_B of functions supported in [-B,B], with logarithmic Fourier norm. Let \`chi\` be a nonzero C_c^infinity(-B,B) and choose finitely many distinct real R_j. The functions
\[
v_j(x)=\chi(x)e^{iR_jx}
\]
are in H_B. Gram-Schmidt in the ORIGINAL canonical inner product produces an orthonormal finite frame U:C^k -> H_B, and \`Pi=UU*\` is a legitimate canonical orthogonal packet projection. Distinct exponentials times nonzero chi are linearly independent: an exponential polynomial vanishing on the open set where chi !=0 vanishes identically.

An exact HARD frequency band projector does not leave H_B invariant. Indeed, if h has compact physical support, \`Fourier h(z)\` extends to an entire function of z. If its real Fourier support is also compact, the entire function vanishes on an open real ray, hence h=0. Any frequency-local construction must admit tails; do not present \`1_{|xi-R|<W}\` as a projection from H_B onto a nonzero subspace of functions with the SAME physical support.

## 2. Exact WHOLE-column variance certificate

Let M=P_B*P_B be the established bounded positive self-adjoint Riesz operator on H_B, and assume the inherited positive observability \`M>=m_B I\`, m_B>0. Write \`Pi=UU*\` and \`L=(I-Pi) M Pi\`. Then
\[
 L*L=\Pi M(I-\Pi)M\Pi
     =\Pi M^2\Pi-(\Pi M\Pi)^2,
\]
so
\[
 \|L\|^2=\|\Pi M^2\Pi-(\Pi M\Pi)^2\|.                 (1)
\]
For a unit one-packet vector u this reads
\[
 \|(I-\Pi)Mu\|^2=\|Mu\|^2-|\langle Mu,u\rangle|^2.
\]
This requires the FULL canonical dual action \`Mu\`; sampling only \`<Pu,Pv_j>\` on selected packets determines \`Pi M Pi\`, but not \`Pi M^2Pi\`. No actual zeta variance values are claimed.

Set A=\Pi M\Pi on ran Pi, C=(I-\Pi)M(I-\Pi) on ran(I-Pi), and R=(I-\Pi)M\Pi. Then C>=m_B I, and the exact packet Schur block for M is
\[
 S=A-R*C^{-1}R>0.
\]
For every packet row j in ran Pi,
\[
 \langle j,M^{-1}j\rangle=\langle j,S^{-1}j\rangle.
\]
If \`||R||<=epsilon_B<m_B\`, Loewner order gives
\[
 S \succeq A-(\epsilon_B^2/m_B)I,\qquad
 \langle j,M^{-1}j\rangle
 \le\langle j,(A-\epsilon_B^2/m_B I)^{-1}j\rangle.     (2)
\]
The strict inequality eps<m is a convenient sufficient condition for invertibility of the displayed LOWER matrix; the actual positive M needs no such hypothesis.

For any canonical dual representer j, including one outside the packet, and ANY finite packet trial z in ran Pi,
\[
 \langle j,M^{-1}j\rangle
 =2{\rm Re}\langle j,z\rangle-\langle z,Mz\rangle
   +\langle j-Mz,M^{-1}(j-Mz)\rangle
\]
and therefore
\[
 \langle j,M^{-1}j\rangle
 \le 2{\rm Re}\langle j,z\rangle-\langle z,Mz\rangle
       +m_B^{-1}\|j-Mz\|^2.                            (3)
\]
This is a valid WHOLE-domain residual payment. The norm of \`j-Mz\` includes all omitted canonical directions. It is not a finite sampled residual, nor an assertion that \`j\` has a physical L2 source.

## 3. Complete exact negative-source countercontrol

Take the complex physical/canonical carrier H=C^2, positive source P=I, old support subspace V_s=span(e_1), enlarged support V_t=C^2, and the original-style complete negative analysis N=(3/4,3/4):C^2->C. Both source channels are bounded and P*P=I. Use packet projection Pi onto e_1. Consequently
\[
 M=I,\quad (I-\Pi)M\Pi=0.
\]
The old signed form has gap \`1-(3/4)^2=7/16>0\`, hence strict old positivity. The complete source-shell operator has incoming K=3/4, and its exact relative cost is
\[
 K^*(I-A_s)^{-1}K=(9/16)/(7/16)=9/7>1.
\]
The entire enlarged original-style signed form has matrix
\[
 Q=I-N*N=
 \begin{pmatrix}7/16&-9/16\\-9/16&7/16\end{pmatrix},
\quad \det Q=-1/8<0.
\]
Its eigenvalues are 1 and -1/8; a genuinely negative full direction is (1,1). Thus **even epsilon_B=0 cannot imply any gap-independent strict shell cost** without additional information about N and its mixed cross block. This is an exact generic source model, not an alternative zeta divisor or a counterexample to the complete native Weil identity.

The CC31 protected critical rank in this control is one. It does not exclude the failure: low-dimensional critical modes still need arithmetic defect-dependent suppression.

## 4. A quantitative packet estimate with all missing obligations visible

Let j_i denote the canonical Riesz representer of CC20's original forced row J_i, with eigenvalue lambda_i and defect delta_i. Its needed positive-dual covariance is
\[
 \langle j_i,M_t^{-1}j_i\rangle
 \le b_B\lambda_i\omega_B(\delta_i),\quad \omega_B(x)\longrightarrow0.
\]
This scalar condition, plus CC31's cap-uniform critical rank, would imply CC29's collective endpoint target with a factor depending only on the cap. It is an open arithmetic hypothesis.

Equations (2)-(3) suggest a valid packet-based certification pipeline:

1. Specify Pi with actual canonical/support custody and a WHOLE-complement leakage enclosure \`epsilon_B\`.
2. Construct packet trials z_i and certify \`||j_i-M_t z_i||\` against the ENTIRE D_t dual, not a finite collection of samples.
3. Show that the complete upper bound (3), or the packet Schur bound (2) together with the off-packet row norms, is \`O(lambda_i omega_B(delta_i))\` uniformly on the required cap and old-positive windows.
4. Preserve the unchanged full negative-source mixed rows, including every divisor partner and multiplicity copy, and the genuine crossing/positive-level controls.

A finite packet frame without item (2) is not a certificate. Small \`||(I-Pi)M Pi||\` without items (2)-(3) cannot determine the signed source reaction, as Section 3 proves.

## 5. Relation to CC29–CC31, and exit status

CC29's endpoint criterion only requires a cap-uniform vanishing modulus of the full critical shell covariance as the OLD source defect tends to zero; this is weaker than a global strict \`q<1\` on each shell. CC31 proves that the number of near-unit critical output modes is bounded by a finite d_B on any fixed cap, and that scalar whole-forced-row estimates suffice up to a factor d_B. IP2 therefore prioritizes the scalar critical residual, not an unweighted frame bound on every raw zero frequency.

The metric localization problem is strictly weaker than RH and might have standalone results, but by itself it has no way to discriminate original negative-source contact. We do not claim that actual zeta's M commutator is small for these packet projections, that critical rows are packet localized, or that new cap-effective constants exist. The fixed-test phase decay in IP1 does not verify a whole-column operator norm.

No new aperture, RH/F4, full transport, Lean theorem, actual critical covariance, or global non-stalling follows. Coupled remains sole active integration; Global NF71, Aperture and Shadow PS3 remain paused. Continue only if a new ACTUAL arithmetic estimate for j_i and its complete residual is available; otherwise classify packet localization as a structural tool, not an RH breakthrough.
