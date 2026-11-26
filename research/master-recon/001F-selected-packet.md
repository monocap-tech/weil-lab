# MASTER-RECON-001F — Selected-packet adjudication

2026-11-24. INVESTIGATE; ADOPT 0. Paper proof. Previous investigations stay in force. This addresses the finite omitted background and the ordinary selected Picard marker; no promotion of the infinite background or RH.

## 1. Native correction to 001E

Archived PAP-ARITH-0 gives Q_W=Q_Pi-||N_{Pi^c}^*g||². The ordinary native selected form retains all positive channels and only selected negative channels. Thus if A=(A_+,A_-,Pi,A_-,Pi^c) is raw analysis, A_Pi=(A_+,A_-,Pi) and
$$
W_\Pi=W+\langle A_{-,\Pi^c}f,A_{-,\Pi^c}h\rangle.
$$
The coefficient is ONE, not the coefficient TWO in the sign-reversal model of 001E. Both are finite exponential-output perturbations when the omitted background is finite. Do not conflate ordinary selected marker with indefinite restored-background resolvents before their prescribed limits.

## 2. Finite-background persistence obstruction

Theorem: Let k in L² be supported in [-c,c]. Suppose Wk belongs, on (-c-epsilon,c+epsilon), to a fixed finite-dimensional space V spanned by finitely many complex exponentials. Then k=0. In particular no nonzero selected physical mode with finite omitted negative channels persists across a two-sided collar.

Proof: Choose nonzero constant coefficient differential operator D=p(partial_x) annihilating V, e.g. p(z)=product(z-lambda) over the exponents. Convolve k with a smooth compactly supported approximate identity of radius less than epsilon/4, choosing it so g is nonzero if k is nonzero. On the window shrunk by the mollifier radius Wg belongs to V (convolution multiplies each exponential by a scalar). D commutes with W on compactly supported smooth functions as W is a convolution distribution. Thus W(Dg)=0 on a larger interval than the support of Dg. By 001D, Dg=0. Fourier transform gives p(i xi) hat g(xi)=0, so g=0 by continuity and the finiteness of the roots, contradiction. The omitted negative correction has output in V since every omitted channel is a linear combination of the actual two reflected exponentials. QED.

The same argument handles any finite exponential-polynomial forcing by using root multiplicities. No claim about an infinite background is made.

## 3. Closed selected raw range

Assume finite off-line zeros. Use X_t from 001E. Deleting finitely many L²-bounded evaluations preserves its two-sided estimates with an L² defect:
$$
\|f\|_{\log}^2-C_t\|f\|_2^2\le \|A_\Pi f\|^2\le B_t\|f\|_{\log}^2.
$$
If A_Pi f=0, the selected form pairs f to zero against all tests on every larger window; hence Wf is a finite exponential forcing there. Section 2 gives f=0. The weak X_t / strong L² compactness argument of 001E removes the defect and proves closed range R_Pi,t=A_Pi X_t. Ranges are consistent and their right intersection is R_Pi,c, by injectivity on the larger window and support. Thus G_Pi,t=R_Pi,t^perp has right limit G_Pi,c, with norm convergence after compression to finite selected space.

## 4. Exact Picard-to-gap identity

For bounded native synthesis S=[P M] from positive plus selected coefficient spaces to the Green carrier, let ell extract the selected coordinates. With eta>0, Woodbury (or direct multiplication) gives
$$
(I+M^*(PP^*+\eta I)^{-1}M)^{-1}
=I-M^*(SS^*+\eta I)^{-1}M
=\ell\,\eta(S^*S+\eta I)^{-1}\ell^*.
$$
The spectral theorem yields strong convergence of eta(S*S+eta I)^(-1) to P_ker S; finite-dimensional compression gives norm convergence. Thus the ordinary native Picard endpoint is exactly ell P_ker S ell*. This holds even if S has nonclosed range; no Green inverse is assumed. It does not justify arbitrary exchange of background restoration and Picard limits.

## 5. Native source pairing recovered

The archived Lean definitions in Pasted text(4).txt give sourceLoad=(0,2f), sourceLift=orthogonal projection of sourceLoad onto the energySubspace, energyVector(g)=(g',g/2), rawColumn=sqrt(m) sourceEmbed(actualGreenSource), and actualGreenSource(rho)(x)=exp((bar rho-1/2)x). For smooth supported g, energyVector(g) lies in energySubspace. Therefore with the conjugate-linear-first inner product
$$
\langle rawColumn_\rho,energyVector(g)\rangle
=\sqrt{m_\rho}\int\overline{actualGreenSource_\rho(x)}g(x)dx
=\sqrt{m_\rho}\int e^{(\rho-1/2)x}g(x)dx.
$$
This is precisely the raw Mellin evaluation. In particular no unproved assertion that a Green adjoint is an ordinary L² adjoint is needed. If the signed columns are the corresponding normalized sums/differences (including any reflected duplicate normalization), their adjoint evaluations follow by linearity. Density of the original supported energy vectors in the native carrier implies ker S is the annihilator of these test evaluations, hence G_Pi,t after the exact coefficient metric identification. The archive records full-positive and selected-negative columns and preservation of their original normalization, but the full signed-column definitions were not independently fetched here. This final identification to the historical implementation is conditional on those normalization and test-class checks; the raw selected theorem itself is proved in the explicit-formula signature convention.

## 6. Selected neutral reconstruction

For the raw selected model use J_Pi=I-2 ell*ell on H_+⊕H_-,Pi. For u in E=ker(Gamma_c-I/2), v=P_Gc ell*u has selected coordinate u/2, so J_Pi v=v-ell*u=-P_Rc ell*u. Closed range yields unique k in X_c with A_Pi k=J_Pi v and selected analysis -u/2. The relation v in G_t for t>c is exactly W_Pi k=0 on (-t,t). By Section 2 this forces k=0 and u=0. Hence
$$
E\cap\ker(\Gamma_c-\Gamma_t)=\{0\},\qquad t>c.
$$
If Gamma_c>=I/2, 001A gives n_-(Gamma_t-I/2)=dim E for small positive t-c. Thus raw finite-exception selected MTP-2 iff E=0, with native Picard identification conditional as above. At a selected first contact with genuine right negativity, finite dimension and right norm continuity force E nonzero; MTP-2 then fails, not a contradiction to hypothetical off-line zeros.

## 7. Adjudication and unresolved infinite case

Finite omitted exponential background is not an escape from 001D. The full physical and raw finite-exception selected persistence mechanisms are negatively resolved. No actual nonzero neutral vector has been exhibited; neutral-space exclusion is unresolved.

For infinitely many omitted negative channels, the correction no longer lies in a fixed finite exponential space and the annihilating polynomial argument is unavailable. A new tail-to-exact-rigidity theorem or genuinely different argument would be required. Finite tail restoration at every fixed Picard scale does not justify it: archived finite-restoration results explicitly allow the cutoff to depend on regularization and do not commute the endpoint limits. Native signed-column normalization and the exact historical marker identification still need direct source checking. No Lean compilation, independent literature novelty check or RH claim. No release of stay.

Next gate, if continued: identify whether the infinite background can be eliminated by a uniform source-exact argument or whether the remaining reconciliation should be stayed. In particular do not infer MTP-2 from coercivity or from finite-rank approximations converging in norm.
