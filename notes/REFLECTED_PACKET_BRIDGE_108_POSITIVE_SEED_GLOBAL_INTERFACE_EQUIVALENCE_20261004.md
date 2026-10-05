# RPB108: direct positive seed and exact global interface equivalence

Base: research f677fb881610073a1aece1defe9abf8cac6b9558.

## What is proved

There is a direct, explicit sufficiently small positive native window using only the certified archimedean logarithmic error and compact support. It does not require the external Zhu short-window result.

Using that seed and the actual carrier theorems already proved, the following statements are equivalent:

1. For every a>0 and h in D_a, ||N_a h||<=||P_a h||.
2. For every a>0, the actual native weak-null space is zero.
3. Every actual endpoint weak-null vector has an eventual polynomial-times-exponential upper bound on the real genuine moving-Gaussian action.
4. For every a>0 there is eta_a>0 with Q_a(h)>=eta_a E_log(h) on D_a.
5. Every full-negative induced map T_a=N_a P_a^(-1) on the closed positive-analysis range is a contraction.

The third condition allows its rate, constant, polynomial exponent and starting R to depend on the vector and window. No uniform all-window estimate is needed for the equivalence.

These are equivalent assertions, not assertions established globally by this note. The result precisely locates the remaining input: the all-window endpoint-null Gaussian upper theorem has global full-source unit-domination strength.

## Terminology before use

**Positive seed window:** a fixed a_seed>0 on which the native quadratic controls the canonical logarithmic norm by a strictly positive constant.

**All-window full-source unit domination:** condition 1 for the complete normalized positive and negative actual analyses P,N, with raw multiplicity retained in their energy accounting.

**Endpoint weak-null vector:** h in D_a with Q_a(g,h)=0 for every g in that same D_a. A zero diagonal alone is not this definition.

**Endpoint-null Gaussian upper property:** condition 3, specified precisely below. It concerns the genuine action of the same physical vector and its moving Gaussian.

**Fixed-window strict logarithmic coercivity:** condition 4; eta_a may decrease as a grows. It supplies no uniform lower bound over all windows.

## Direct support uncertainty and a positive seed

Use Fourier convention exp(-2pi i x xi) and
\[
E_{\log}(h)=\int_{\mathbb R}\log(e+|\xi|)|\widehat h(\xi)|^2\,d\xi.
\]
For h supported in [-a,a], Cauchy-Schwarz gives
\[
|\widehat h(\xi)|^2\le\|h\|_1^2\le2a\|h\|_2^2.
\]
Put T=1/(8a). The Fourier mass in [-T,T] is at most
\[
(2T)(2a)\|h\|_2^2=\frac12\|h\|_2^2.
\]
Plancherel therefore gives
\[
E_{\log}(h)\ge\frac12\log(e+1/(8a))\|h\|_2^2.
\tag{6}
\]

Let C0>=0 be the certified global archimedean logarithmic error:
\[
|\operatorname{arch}(2\pi\xi)-\log(e+|\xi|)|\le C_0.
\]
For 2a<log 2 there is no nonzero prime term in the native cutoff. The n=1 coefficient, if included by notation, is zero. Thus the native form is the archimedean integral plus the two pole cross moments.

The exact pole dictionary and supported-moment estimate give
\[
|\overline{M_-(h)}M_+(h)+
 \overline{M_+(h)}M_-(h)|
 \le4a e^a\|h\|_2^2.
\]
Consequently
\[
Q_a(h)\ge E_{\log}(h)-(C_0+4a e^a)\|h\|_2^2.
\tag{7}
\]

Set K0=C0+4e and choose explicitly
\[
a_{\rm seed}
=\min\left\{\frac12,\frac{\log2}{4},
 \frac18 e^{-4K_0}\right\}>0.
\]
For every 0<a<=a_seed, the prime sum is absent, a<=1 and C0+4a e^a<=K0. Moreover
\[
\log(e+1/(8a))\ge4K_0.
\]
By (6), ||h||_2^2<=E_log(h)/(2K0). Equation (7) now proves
\[
Q_a(h)\ge\frac12 E_{\log}(h)
\qquad(0<a\le a_{\rm seed}).
\tag{8}
\]

This is deliberately a coarse seed, with no numerical claim about the maximal positive aperture. It is enough for first contact. It uses no positivity of an arbitrary background and no spectral physical operator domain.

## Existing actual carrier facts used in the equivalence

On D_a the already proved full source/native identity is
\[
Q_a(f,g)=\langle P_a f,P_a g\rangle-
          \langle N_a f,N_a g\rangle.
\tag{9}
\]
It is consistent under physical support inclusion. Actual sampling is bounded on the logarithmic domain, and P_a is bounded below with closed range. Thus T_a=N_a P_a^(-1) is a bounded map on that range regardless of whether it is a contraction.

The fixed-window Riesz operator is I+compact and self-adjoint. Pulling the forms back by physical dilation to D_1 gives an operator-norm-continuous family, including prime activation thresholds. These facts were proved in the actual first-contact record; their proofs do not depend on its external choice of starting positive window.

The strict-enlargement theorem says that a nonzero vector supported in [-a,a] cannot be full native weak-null on D_b for any b>a. It uses full-form translation covariance and finite fixed-window nullity, not background positivity.

The preceding Gaussian records prove the actual lower estimate and the implication that an eventual polynomial-times-exponential real-action upper bound forces h=0. All use the same physical vector. No raw synthesis preimage is added.

## Precise upper property

For every a>0 and every h in D_a satisfying the endpoint weak-null equation, require the existence of delta>0, C>=0, p>=0 and R0>=1 such that
\[
\Re\mathcal A_a(h;\overline{K_R*h})
 \le C(1+R)^p e^{-\delta R}
\qquad(R\ge R_0),
\tag{10}
\]
where K_R is the exact normalized project moving Gaussian.

Here g_R=K_R*h is a whole-line Schwartz test for the tempered action, not a vector asserted to belong to D_a. Nullity on D_a does not by itself evaluate this test to zero. Condition (10) is the missing independent input, not a restatement of that invalid inference.

## Proof of the equivalences

**1 iff 5.** On the closed range of P_a, every k has the unique same-vector form k=P_a h. Therefore ||T_a k||<=||k|| is exactly ||N_a h||<=||P_a h||. No off-range observations are introduced. Zero extension by orthogonal projection is also contractive precisely in this case.

**1 implies 2.** By (9), condition 1 makes Q nonnegative on every supported domain. If h is endpoint-null at a, then Q_a(h,h)=0. For any b>a, support inclusion preserves the vector and gives Q_b(h,h)=0. Positivity of the Hermitian form Q_b implies Q_b(g,h)=0 for every g in D_b, either by form Cauchy-Schwarz or by varying both real and imaginary multiples of g. The strict-enlargement theorem then gives h=0.

**2 implies 1.** If condition 1 fails, (9) supplies an actual supported logarithmic vector with strictly negative native energy at some a1. Equation (8) implies a1>a_seed. Pull the actual forms back to D_1 along the compact positive interval [a_seed,a1]. Norm continuity, strict initial positivity and negativity at a1 give a first contact with lower spectral bound zero. Since the contact operator is nonnegative and I+compact, zero is attained by a nonzero kernel vector: for a unit minimizing sequence f_j, A f_j tends to zero; compactness of (A-I) gives a strongly convergent subsequence of f_j with unit limit in the kernel. Its physical dilation is a nonzero actual endpoint weak-null vector. This contradicts condition 2. No negative vector is asserted to exist in applying this contrapositive.

**2 iff 3.** Under condition 2, every endpoint-null vector is zero, so (10) holds with C=0, delta=1 and p=0. Conversely, (10) and the already proved actual Gaussian lower bound imply exponential M_R decay. The one-sided Gaussian theorem forces that same h to be zero. This proves condition 2. In particular, no uniform choices of the parameters in (10) are necessary.

**1 implies 4.** The first implication above already gives kernel zero. At a fixed a, A_a is nonnegative and I+compact. If its quadratic had no positive lower bound on the logarithmic unit sphere, a unit minimizing sequence would again satisfy A_a f_j->0. Compactness would produce a unit kernel vector, contradiction. Therefore Q_a>=eta_a E_log for some eta_a>0.

**4 implies 1.** Condition 4 gives Q_a>=0. The actual identity (9) yields full-source unit domination.

This proves all five equivalent without assuming any one of them globally.

## What the theorem rules out procedurally

The remaining all-window estimate cannot be classified as a routine observation-quotient correction. The quotient/completion and bounded factorization are already available; proving (10) for every endpoint null vector would settle the global unit bound by the equivalence.

It remains legitimate to derive (10) from a genuinely independent analytic argument and thereby exclude endpoint nullity. The theorem does not prove that no such argument exists. It proves that simply assuming (10), or putting it in a representation record, imports exactly the unresolved global null-exclusion content.

At a single named window, an upper property need only exclude that window's kernel. The global equivalence requires quantification over all windows. A finite numerical window audit cannot be substituted for it.

The theorem concerns full P,N. A selected-background B differs from N, and unit gain on a selected vector requires separate removed-energy custody. Neither the full translation theorem nor this equivalence is silently transferred to a selected-only form.

No claim of RH, existence of an actual off-line zero, existence of an endpoint mode, or FULL TRANSPORT CLOSED is made.

## Validation and cursor

Analytic proof. The new seed uses only explicit support/Fourier mass bounds, the existing native archimedean envelope and exact pole moments. The equivalence uses the previously proved actual carrier, first-contact, strict-enlargement and one-sided Gaussian theorems. This removes the external short-window positivity input from the first-contact existence argument at the expense of a much smaller, nonoptimal seed. Historical claims about the 0.8 window are unchanged.

No Lean source or workflow changes and no new CI result. Certified code remains cb92c1b4dfca298cbc79d5b7d25598ea370236bf; Actions run 37236113125/job 111535430775.

At f677fb8, a direct support/Fourier estimate proves an explicit sufficiently small native positive seed without the external Zhu short-window input: E_log(h)>=0.5 log(e+1/(8a))||h||_2^2 and, below the first prime threshold, Q_a(h)>=0.5 E_log(h) for a<=a_seed determined by the native archimedean logarithmic error. Combined with the already proved norm-continuous I+compact family, first-contact construction, strict-enlargement null obstruction and one-sided Gaussian decay theorem, this yields an exact all-window equivalence: full-negative unit domination ||N_a h||<=||P_a h|| for every a,h; absence of nonzero endpoint weak-null vectors; existence of an eventual polynomial-times-exponential upper bound on the genuine Gaussian action of every endpoint-null vector; and fixed-window strict logarithmic coercivity for every a. The positive-carrier contraction formulation is equivalent too. Constants may depend on the window/vector; no uniform all-window constant is asserted. Thus the remaining endpoint-null Gaussian upper theorem has global full-source unit-bound strength, not carrier-retyping strength. No equivalent condition is proved globally, no selected-background equivalence or RH conclusion is asserted, and Lean/CI are unchanged. FULL TRANSPORT CLOSED remains open.
