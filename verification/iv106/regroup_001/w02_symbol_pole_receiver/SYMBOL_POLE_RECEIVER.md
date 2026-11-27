# IV106 W02 — Literal-symbol / positive-pole dual receiver
Status: conditional analytic advancement, not a native theorem or numerical Schur certificate. Independent of the active E18X run 45951142451; no E19V release, no bank enlargement. Owner-ratified W02 amendment d4e482f2f616112dca11f6d8fd803a3dffb5a80c governs. Parent 28018381670158ceed55520c48e32324b26c779b contains mixed-metric receiver.

## Exact source reconciliation
E17B already proves (at source level) the explicit loss 20 and the numerical inverse bound 21, including nonnegativity of the pole term on the actual signed-difference kernel. Do not report that existing fact as a new theorem. The advance here is a symbol-sensitive, rank-one-aware inverse-energy majorant that improves the 21 bound uniformly for the same raw residual and admits a direct matrix certificate.
- C3C c613964eb4c2f1dd44196b3deb609ea07e3ca9ae verification/iv106/iv106_c3c/ActualZetaIV106C3ActualConstraints.lean blob 25d13ea5fb5fce899121fd61ab5ae54a5b954002, neutralIV106C3Constraints_zero_iff: one signed pole difference, equal moments, all 665 cell rows and both k-row families.
- E11 c9c5f6cf9f04f33a14722cd07e1a7e3edf56795d verification/iv106/iv106_e11/ActualZetaIV106E11ClosedKernelMargin.lean blob 0e441edc678a5c41bb58b11bde6b16bbf59bc48b: c=5003/5000 closed mass estimate.
- E17A 0c93c44d5965d9890ea2745c4bdd0ccf6abaf1c1 verification/iv106/iv106_e17a/ActualZetaIV106E17AExplicitShift.lean blob ca8e33baee614db82dd70e448def9572c2e27919: S+20>=w.
- E17B 6d1c092ad7a969663895fbea2391188cbf0d23e8 verification/iv106/iv106_e17b/ActualZetaIV106E17BExplicitReserve.lean blob 941e20215fbdeb15036b3c2442fb733c2ac94033: explicit_garding, Margin, Inverse21, Enclosure21, Interval21.
- Base 018f7e59f4129ce521cd3ae86d1afd59d3b64b5f WeilDefect/Arithmetic/ActualZetaCanonicalNativeEnergy.lean blob bda93aa61bc6580197649833f30394aae943d910; ActualZetaNativeFormOperator.lean blob 93beff3a82207f44fd5a431987c39f1aeb7e0092: literal quadratic multiplier plus 2 Re(conj(m-)m+), supported Hilbert attachment. WeilDefect/Morphology/NeutralLogHilbertCarrier.lean blob 679d58b8f0cfa6b4f7d28c48ce844a41cdce2844: reconstruction and Fourier identity.
- E12/E15/E16 and E19L/M are pinned in parent mixed-metric report; E19MRawFourier blob b13e9a2ed55f778ba98cd11de1d786a1e05f067f at 98174cc17783bd3096652f1a2aa3560677c712b9. All actual theorem attachments remain conditional on source acceptance; no historical native status inferred from files.
 
## Derivation
Let a=11/10, k=34, K the exact E12 kernel, J_K its isometric inclusion into ambient L2(dxi). Use inner product conjugate-linear in the first slot. Set x=J_K d, w=log(e+|xi|), S=rightLimitCompactWeilSymbolMathlib a. On K, m+=m-=m(d) by the signed row, not m=0. The exact actual energy is E(d)=integral (S/w)|x|^2+2|m(d)|^2. E11 gives E(d)>=c integral |x|^2/w. Let p be the ambient Riesz vector representing m on K, e.g. reconstruction adjoint of the physical moment representative (average of the two representatives is also valid). Existence follows from bounded compact-window physical moments and contractive U. No specific sign convention for moment exponent is added.
 
Choose a single scalar lambda=c/(c+20)=5003/105003. It lies in (0,1), (1-lambda)c=20lambda. The convex energy combination gives
 E(d)>= integral q |x|^2 + 2lambda |<p,x>|^2,
 q=lambda(S+20)/w>=lambda.
 q is measurable and bounded above using the original symbol envelope. Let B=M_q+2lambda p<p, .> on ambient L2. B is bounded, self-adjoint and B>=lambda I. This is a lower form on K, not a replacement operator or a claim of equality with C. C=I_K^* A I_K, where A is the actual operator on H, I_K:K->H, J:H->ambient L2 and J_K=J I_K. Thus C>=J_K^*B J_K as forms. The raw residual g satisfies r=J_K^*g, d=C^{-1}r. From E(d)=Re<x,g> and weighted Cauchy-Schwarz (or variational completion), E(d)<=<g,B^{-1}g>, a real nonnegative number. This follows even without computing C^{-1} numerically.
 
Write T=M_{1/q}, v(g)=<p,Tg>, h=<p,Tp>+1/(2lambda)>0. Then
 <g,B^{-1}g> = <g,Tg> - |v(g)|^2/h.
 Proof: B^{-1}g=Tg - Tp v(g)/h, checked by multiplying B; h real. Alternatively, for arbitrary z in C,
 E(d) <= integral |g-zp|^2/q + |z|^2/(2lambda),
 by Cauchy-Schwarz on (sqrt(q)x,sqrt(2lambda)<p,x>), with conjugate conventions; minimizing the right side gives z=v(g)/h. No inverse computation in the actual kernel. Since q>=lambda and the subtracted term is nonnegative,
 0<= <g,B^{-1}g> <= lambda^{-1}||g||^2 = (105003/5003)||g||^2 < 21||g||^2 for g != 0.
 Strict gain versus 21 is small from the rational scalar alone; the pointwise symbol and pole subtraction may be much larger. No actual quantitative gain inferred without residual data.
 
## Matrix form usable with certified inputs
For the 734 raw residual columns g_i (E19L/M row and exterior corrections preserved) define
 R_ij=<g_i,Tg_j> - conj(v_i)v_j/h, v_i=<p,Tg_i>.
 R is PSD, and the quadratic error of each actual synthesized trial is bounded above by cvec^* R cvec for ALL complex coefficients, including redundant coordinates. Sufficient terminal test is L0-R>=0 as a Hermitian matrix, L0 a lower enclosure of actual trial energy. Alternative directed interval method: choose any fixed complex z_i (not necessarily optimum), h_i=g_i-z_i p. Then the PSD upper certificate
 Rtilde_ij=<h_i,T h_j> + conj(z_i) z_j/(2lambda)
 dominates R by the exact completed square. This avoids certified subtraction of an uncertain rank-one Gram. A whole-bank choice of z_i is linear in coefficients and preserves Loewner ordering. Neither entrywise choice of lambda nor componentwise signed interval subtraction is sufficient. Error in g_i must include actual IV105C columns and exterior/row synthesis; physical errors can also use parent mass-only bound if needed. Old 700-coordinate proxy remains insufficient.
 
## Next mathematical test
Use fixed lambda and optimize z_i with the literal common moment representative only when the full raw residual input is authenticated. A lower certified q envelope can be used in the positive integral of Rtilde (requires q_lower>=positive constant); retain the exact rank-one penalty. Evaluate the full complex quadratic Gram comparison, not individual residual norms. This method cannot be evaluated on the existing E19U single pole-row approximation as if it were a 734-column action matrix. Pending E18X run is not consumed; no numerical/native work claimed. Proof is self-reviewed analytic, not independent native admission. 
