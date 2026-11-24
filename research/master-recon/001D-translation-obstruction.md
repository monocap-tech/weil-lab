# MASTER-RECON-001D — Translation obstruction to neutral persistence

2026-11-24. INVESTIGATE; ADOPT 0. Paper proof, no Lean compilation. Previous investigations remain under stay. This result is a falsification of nonzero *physical* two-sided collar persistence, not an RH proof.

## 1. Native physical convention

Use the uncompressed full signed Weil distribution in the convention of 001B: ordinary Fourier multiplier A(xi)=Re psi(1/4+i xi/2)-log pi, prime convolution with both shifts ±log n and weights -Lambda(n)/sqrt(n), and mixed pole convolution kernel 2cosh((x-y)/2). Each contribution commutes with translations and convolution by compactly supported smooth functions, interpreted as distributions; the prime measure is locally finite, and the input is compactly supported. On a fixed finite window only finitely many prime terms occur. No global L² boundedness of the pole or prime distributions is needed.

## 2. Finite smooth null dimension

Fix t>0. The complete form on C_c^infty(-t,t) is
$$
W_t(f,f)=\frac1{2\pi}\int A(\xi)|\widehat f(\xi)|^2\,d\xi+\langle f,B_tf\rangle.
$$
The finite prime-shift operator and the pole kernel restricted to the bounded square define a bounded self-adjoint B_t. Digamma asymptotics and continuity give A(xi)>=log(2+|xi|)-C_A. Thus for some C_t>0,
$$
W_t(f,f)\ge\frac1{2\pi}\int\log(2+|\xi|)|\widehat f(\xi)|^2\,d\xi-C_t\|f\|_2^2.
$$
Let R>0 satisfy log(2+R)>2C_t. Each normalized smooth supported null vector (indeed any smooth f of nonpositive form value) has Fourier mass on [-R,R] at least 1/2. For an orthonormal family f_1,...,f_m of such vectors, Bessel on L²(-t,t) against exp(i xi x) gives sum_j |hat f_j(xi)|² <=2t. Integrating,
$$
m/2\le 2tR/\pi,\qquad m\le4tR/\pi.
$$
In particular the linear space of smooth supported distributional null vectors on (-t,t) is finite dimensional: if it had arbitrarily many independent vectors, Gram-Schmidt would give arbitrarily long such orthonormal families. No positivity of W_t is assumed.

## 3. No nonzero two-sided persistent physical mode

**Theorem.** Let k be a compactly supported L² function with supp k contained in [-c,c], c>0. If for some epsilon>0,
$$
\mathcal W k=0\quad\text{in }\mathcal D'(-c-\varepsilon,c+\varepsilon),
$$
then k=0.

**Proof.** Suppose k is nonzero. Choose a smooth compactly supported approximate identity of radius less than epsilon/8 such that its convolution g with k is nonzero (L² convergence of approximate identities). Distributional convolution commutes with W, so Wg vanishes on the window of radius c+epsilon-epsilon/8. Set t=c+epsilon/2. For each |a|<epsilon/8 the translate tau_a g is smooth and supported strictly in (-t,t), and W(tau_a g)=tau_a Wg vanishes there. Its form value is zero by testing with itself. The translations are linearly independent for distinct a: a finite linear dependence gives hat g(xi) sum_j b_j exp(-ia_j xi)=0; hat g is continuous and nonzero on some open interval, so uniqueness of exponential polynomials gives every b_j=0. Arbitrarily many independent translates contradict Section 2. QED.

This bypasses regularity of individual prime-shadow germs, inverse estimates and first-contact assumptions. It also avoids assuming k is in the closed form domain: the mollified vectors are genuine original smooth compactly supported tests. The proof depends on the complete mixed-pole convolution convention; using a nontranslation-invariant regularized carrier directly would not justify it.

## 4. Boundary distribution payment and exterior Gram

For a compactly supported L² k, Wk belongs to H^{-sigma}_loc for every sigma>0: the Gamma multiplier has at most logarithmic growth; prime terms are locally finite L² translates; pole output is locally smooth. Thus if Wk vanishes on the interior and both open exterior collars, any remaining distribution supported at ±c on the larger interval must vanish. A distribution supported at finitely many points is a finite sum of delta derivatives, none of whose nonzero combinations belongs locally to H^{-sigma} for 0<sigma<1/2 (localize around each point and use the polynomial Fourier transform). Hence the full enlarged-window distributional vanishing hypothesis of Section 3 holds.

Consequently for every epsilon>0 the two-sided exterior map of 001B is injective on the physical interior-null L² space. For a finite-dimensional selected neutral realization K:E->L²(-c,c) with W(Ku)=0 distributionally on (-c,c), the Gram of 001B has exactly
$$
\ker\mathfrak G_\varepsilon=\ker\mathcal K.
$$
If the native realization is injective (e.g. if the archived identity N_c^* k_u=-u is attached with its original domains), the Gram is positive definite on any nonzero E. This is the opposite of the proposed MTP-2 vanishing on a nontrivial physical neutral space.

## 5. Logical consequence and limits

The original source attachment remains OPEN. If it is proved, so that ker K_{c+epsilon}=ker arithmetic Gram with an injective physical realization, then under the finite-dimensional MTP-1 and convergence hypotheses of 001A,
$$
n_-(\Gamma_{c+\varepsilon}-I/2)=\dim E
$$
for all sufficiently small positive epsilon. Thus every nonzero marked neutral direction activates, and MTP-2 is equivalent to E=0 under those hypotheses. This does not establish that E=0, nor does it establish that there are actual off-line zeros, or prove RH. In particular a localized null vector may exist with immediate exterior activation, exactly compatible with first contact. No inference from impossibility of persistence to impossibility of a neutral mode is permitted.

Prior 001C shadow-jump result remains valid in its stated convention but is no longer needed to prove non-persistence. The next gate must audit native coefficient-to-physical attachment and decide whether the MTP-2 strategy should be retired or bypassed through a new strictness theorem. No release of stay and no formal certification claimed.
