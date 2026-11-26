# MASTER-RECON-001H — Infinite-background rigidity by analytic translation

2026-11-24. INVESTIGATE; ADOPT 0. Paper proof in the ordinary raw finite selected signature model of 001G. No Lean verification. Previous investigations remain stayed pending adjudication of the native historical marker.

## 1. Statement

Let X_t be the complex Hilbert space of zero-extended L² functions supported in [-t,t] with finite log Fourier norm, and A=(A_+,A_-) the bounded actual multiplicity-weighted raw Mellin analysis of 001G. Its reflection-pair signature decomposition is unitary. For any finite selected negative-coordinate packet Pi, use
$$
W_\Pi(f,h)=\langle A_+ f,A_+ h\rangle-\langle A_{-,\Pi}f,A_{-,\Pi}h\rangle.
$$
Pairings on different support windows are consistent. For this file take inner products linear in the first variable (conjugate the notation if using the native conjugate-linear-first convention). By 001G, for every fixed t>0, ||A_+f||²>=b_t||f||_log², b_t>0, and A:X_t->H is bounded. These estimates depend on the full polarized explicit formula, classical zero count and superlinear distinct critical-line zero count, not on finite off-axis exceptions.

**Theorem.** If k belongs to X_c and W_Pi(k,h)=0 for all h in X_{c+epsilon} for some epsilon>0, then k=0. No restriction on the cardinality of the omitted negative background.

## 2. Analytic translation of the positive form

Use tau_a f(x)=f(x-a) for real a. For an actual reflected pair rho_±=1/2±delta+i gamma, 0<delta<1/2, the Mellin evaluations transform by e^{i gamma a} diag(e^{delta a},e^{-delta a}). The equal multiplicities of reflected zeros allow a unitary Hadamard rotation, giving
$$
e^{i\gamma a}\begin{pmatrix}\cosh(\delta a)&\sinh(\delta a)\\\sinh(\delta a)&\cosh(\delta a)\end{pmatrix}.
$$
A critical-line coordinate only acquires a phase. Reflection duplication, if used in an implementation, must be attached by its normalized isometric identification; no arbitrary extra coefficient weights are allowed.

Fix t=c+epsilon/2 and restrict initially to real |a|<epsilon/4. For f,h in X_t define the positive form
$$
p_a(f,h)=\langle A_+\tau_{-a}f,A_+\tau_{-a}h\rangle.
$$
All shifted inputs lie in X_{c+epsilon}. Within a reflected pair the two phases cancel in the sesquilinear form. Write
$$
D_\delta(a)=\begin{pmatrix}\cosh(\delta a)&-\sinh(\delta a)\\-\sinh(\delta a)&\cosh(\delta a)\end{pmatrix},\qquad
E_+=\operatorname{diag}(1,0).
$$
For real a the coefficient matrix is D_delta(a) E_+ D_delta(a). Its analytic extension is that same product with complex a, NOT the product with a complex adjoint at complex a. All matrix entries and their power series are uniformly bounded and uniformly convergent on bounded complex parameter disks because |delta|<=1/2. The direct sum over all reflected pairs plus unchanged real-ordinate positive channels defines a norm-entire family B_+(a) on the full coefficient Hilbert space. Consequently the Riesz operator in fixed X_t,
$$
P(a)=A_t^* B_+(a) A_t,
$$
is norm-entire. Here A_t is the bounded full raw evaluation map on X_t, and the adjoint uses its log metric. For real a this operator represents exactly p_a. At a=0, 001G gives P(0)>=b_t I, so it is invertible. The Neumann series gives a norm-holomorphic inverse P(a)^(-1) in some complex disk around zero. No claim that complex translations of arbitrary compactly supported X_t functions exist is used in this construction.

## 3. The persistent mode has an analytic translation orbit

For real |a|<epsilon/4, set f_a=tau_a k in X_t. For every h in X_t, tau_-a h belongs to X_{c+epsilon}; persistence gives
$$
0=W_\Pi(k,\tau_{-a}h)=p_a(f_a,h)-\langle A_{-,\Pi} k,A_{-,\Pi}\tau_{-a}h\rangle.
$$
Thus
$$
P(a)f_a=r(a).
$$
The right-hand-side vector represents the displayed finite negative-channel pairing. It is norm-holomorphic near zero after extending the real-parameter formula: each selected channel is a fixed linear combination of the two raw Mellin evaluations at its actual reflected pair, multiplied by scalar exponentials of a; in the conjugate slot on the real axis, extend the conjugated scalar coefficients by their conjugate-coefficient power series, not by taking complex conjugates of the complex variable. There are only finitely many such coordinates and their Riesz representers in X_t are fixed. Equivalently, use the analytic finite negative form matrix and the fact that the corresponding finite raw evaluations of f_a are entire scalar functions of a.

It follows that for real a near 0,
$$
f_a=P(a)^{-1}r(a).
$$
The right side is a holomorphic X_t-valued function of complex a near zero. Therefore the translation orbit of k has a genuine local holomorphic extension U(a) in the fixed supported log space.

## 4. Compact support contradicts holomorphic translation

For each real xi, the Fourier evaluation functional f->hat f(xi) is bounded on X_t since supported L² embeds in L¹. For real a,
$$
\widehat{U(a)}(\xi)=e^{-i\xi a}\hat k(\xi).
$$
Both sides are holomorphic in the complex parameter disk, so the scalar identity theorem extends this equality to complex a in that disk. Choose b>0 so ±ib lie in the disk. Since U(ib),U(-ib) belong to X_t⊂L², Plancherel gives
$$
\int_{\mathbb R}e^{2b|\xi|}|\hat k(\xi)|^2d\xi<\infty.
$$
Indeed the two imaginary translations control the two frequency half-lines. Fourier inversion and Cauchy-Schwarz show that k has a holomorphic representative on the strip |Im z|<b: on smaller substrips the inverse Fourier integral is absolutely convergent, including its differentiated integrals. The representative is zero a.e. on the exterior real intervals by compact support, hence zero there by continuity and identically zero by the identity theorem. Thus k=0. QED.

The proof uses bounded displacement delta rather than unbounded height gamma, and finite selected negativity rather than finite omitted negativity. It does not rely on pointwise convergence of the omitted covariance or any infinite differential annihilator.

## 5. Raw selected MTP-2 adjudication

For u in E=ker(Gamma_Pi,c-I/2), set v=P_Gc ell*u. By 001G there is unique k_u in X_c with A_Pi k_u=J_Pi v and A_-,Pi k_u=-u/2. Persistence v in G_t for t>c is exactly W_Pi(k_u,h)=0 on X_t. The theorem gives u=0. Hence for every t>c,
$$
E\cap\ker(\Gamma_{\Pi,c}-\Gamma_{\Pi,t})=\{0\}.
$$
If Gamma_Pi,c>=I/2, right norm continuity (001G) and the abstract inertia theorem (001A) give n_-(Gamma_Pi,t-I/2)=dim E for all sufficiently close t>c. Thus nonzero neutral persistence is impossible for the ordinary raw finite selected marker, even with infinite omitted negative background.

At an actual selected first contact (positivity below c and negative tests in every larger window), 001G forces E nonzero. Thus raw selected MTP-2 fails at such a contact, conditional on its existence. This is entirely consistent with a hypothetical failure of RH. It neither establishes off-line zeros nor rules out first contact. Under the ordinary raw formulation, initial positivity and the full Weil criterion imply RH failure would produce at least one finite selected packet with first contact (the convergent negative sum already has a finite negative witness). Therefore a universal MTP-2 at all such contacts is tantamount to excluding the contacts, not a usable nonzero continuation principle.

## 6. Scope and remaining adjudication

The raw physical theorem and raw selected-marker implication are paper proved under the established 001G estimates. No formal compilation or independent novelty review. The native ordinary Picard-to-gap identity and raw Mellin pairing were derived in 001F, but exact signed-column metric normalization and any historical indefinite-background restored marker / order of limits remain to be audited. Do not claim equivalence to an arbitrary historical construction. The original goal of falsifying nontrivial persistence is achieved for the ordinary raw selected mechanism. Native attachment and a decision on closing the reconciliation remain; RH and neutral-space exclusion remain open. No previous investigation is released by this commit.
