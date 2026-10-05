# RPB108: an explicit structural endpoint countermodel

Base: research 160792310b75223e59065b925ef02d2568a2f72f.

## The insufficiency theorem

The following structural package does not imply exclusion of finite positive endpoints:

- supported logarithmic Hilbert carriers with consistent physical inclusion;
- bounded positive and negative analyses, with positive analysis an isomorphism onto a closed range;
- an exact positive-minus-negative mixed identity;
- fixed-window identity-plus-compact forms and norm continuity after dilation;
- translation covariance and strict-enlargement weak-null rigidity;
- isolated null windows counted by negative-index growth;
- logarithmic moving-Gaussian lower coercivity.

An explicit comparison family satisfies all these properties and has a finite, attained positivity aperture with nonzero endpoint kernel.

This is a countermodel to the implication from the listed structural package. It is not the actual zeta form, a counterexample to RH, or a claim that all actual-zeta premises have been replicated.

## Terminology before use

**Structural comparison family:** an explicitly defined non-zeta family used only to test a proposed implication from specified structural properties.

**Structural endpoint countermodel:** such a family with a finite positive endpoint, disproving endpoint exclusion from those properties alone.

Use the same Fourier convention and carriers
\[
w(\xi)=\log(e+|\xi|),\qquad
D_a=\{h\in L^2:\operatorname{ess\,supp}h\subset[-a,a],E_{\log}(h)<\infty\}.
\]
Give D_a the logarithmic inner product. Define
\[
Q^{\rm mod}_a(f,g)=\int (w(\xi)-2)
\overline{\widehat f(\xi)}\widehat g(\xi)\,d\xi.
\tag{1}
\]

## Carrier and factorization are fully available

Take
\[
P_a h=\sqrt w\,\widehat h,\qquad N_a h=\sqrt2\,h.
\]
Both target spaces are ordinary L2 spaces. P_a is an isometry from D_a onto a closed range and has trivial kernel. N_a is bounded since w>=1. The identity
\[
Q^{\rm mod}_a(f,g)=\langle P_a f,P_a g\rangle-
\langle N_a f,N_a g\rangle
\]
is exact on both mixed slots.

The positive-energy quotient has no nonzero null class; its completion is D_a itself. The induced map T_a=N_a P_a^(-1) exists boundedly on the closed positive range. No constructor or completion is missing. Its unit contraction condition is nevertheless precisely Qmod_a>=0, and does not follow merely from its existence.

Physical inclusion preserves the original h, its Fourier transform and both analyses.

## Compactness, continuity and covariance

The physical inclusion J_a:D_a -> L2 is compact. Indeed the logarithmic unit ball has Fourier tail mass at most 1/w(T) outside [-T,T]. The low-frequency map from L2([-a,a]) to L2([-T,T]) is Hilbert-Schmidt, with kernel exp(-2pi i x xi). Thus J_a is a norm limit of compact low-frequency approximations.

Consequently the logarithmic Riesz operator for (1) is
\[
I-2J_a^*J_a,
\]
so both nullity and negative index are finite at each fixed a.

After physical dilation U_t f(x)=t^(-1/2)f(x/t), the form on D_1 has multiplier w(eta/t)-2. On compact positive t intervals, w(eta/t)-w(eta) is uniformly bounded. Pointwise continuity on bounded eta sets, and division by w(eta) in the tail, prove operator-norm continuity exactly as in the actual fixed-carrier construction. The correction remains compact.

The multiplier is independent of the physical support window. Restriction under support inclusion is exact, and simultaneous translation of both slots cancels the Fourier phases, giving translation covariance.

Strict-enlargement rigidity follows directly: a nonzero h supported in [-a,a] and weak-null on D_b with b>a would have all sufficiently small translates weak-null on an intermediate D_c. Distinct translates of a nonzero compactly supported function are linearly independent, contradicting finite nullity on D_c. No positivity is used.

Therefore the preceding block and index-count arguments apply to this family too.

## Explicit strict positive seed

For h supported in [-a,a], the already proved support uncertainty estimate is
\[
E_{\log}(h)\ge\tfrac12\log(e+1/(8a))\|h\|_2^2.
\]
For 0<a<=a0=e^(-8)/8 this gives Elog(h)>=4||h||_2^2. Hence
\[
Q^{\rm mod}_a(h)=E_{\log}(h)-2\|h\|_2^2
\ge\tfrac12 E_{\log}(h).
\tag{2}
\]
The comparison family has a direct strict positive seed.

## An actual negative vector for the comparison family

Choose any nonzero smooth bump psi compactly supported in (-1,1), normalized to ||psi||_2=1. Put
\[
M_1=\int |\eta|\,|\widehat\psi(\eta)|^2\,d\eta<\infty.
\]
For h_a=U_a psi, the elementary bound log(e+s)<=1+s/e gives
\[
E_{\log}(h_a)
=\int w(\eta/a)|\widehat\psi(\eta)|^2\,d\eta
\le1+\frac{M_1}{ea}.
\]
Thus
\[
Q^{\rm mod}_a(h_a)\le-1+\frac{M_1}{ea}<0
\quad(a>M_1/e).
\tag{3}
\]
This is a constructed negative vector for the comparison family only.

Define Amod=sup{a:Qmod_a>=0}. Equations (2)-(3) show 0<Amod<infinity. Consistent restriction makes positivity downward closed. Norm continuity makes the finite endpoint nonnegative and attained. If its operator were strictly coercive, continuity would preserve positivity beyond Amod. Its lower bound is therefore zero, and the I+compact minimizing-sequence argument supplies a nonzero endpoint kernel vector.

There is consequently a finite positive endpoint despite the complete carrier and bounded factorization.

## The Gaussian lower mechanism also survives

For the same moving Gaussian use
\[
\beta_R(\xi)=\exp(-(2\pi\xi-R)^2/R),\qquad
M_R(h)=\int\beta_R|\widehat h|^2.
\]
Its genuine whole-line mixed action for (1) is
\[
A_R(h)=\int(w-2)\beta_R|\widehat h|^2.
\]
This integral is well-defined; no pole extension or generic distributional pairing is needed.

On |xi|>=R/(4pi), w-2>=log R-log(4pi)-2. On the complement, beta_R<=exp(-R/4) and w-2>=-1. For all sufficiently large R, with L_R=log R-log(4pi)-2>0,
\[
A_R(h)\ge L_R M_R(h)
-(L_R+1)e^{-R/4}\|h\|_2^2.
\tag{4}
\]
Thus the same logarithmic moving-Gaussian coercivity holds.

For a nonzero endpoint kernel vector, an eventual polynomial-times-exponential upper bound on A_R would imply exponential M_R decay by (4). The proved one-sided Gaussian decay theorem for nonzero compactly supported L2 vectors forbids this. Therefore the comparison endpoint does not satisfy the missing Gaussian upper condition.

The lower coercivity does not itself supply the upper condition or a contradiction.

## Exact scope of the obstruction

The comparison model omits the actual zeta-divisor sampling identity and the exact archimedean, prime and pole structure. It makes no claim about actual-zero multiplicities or their observational quotient. Those omitted features may supply independent rigidity; this theorem does not rule out such an argument.

What it rules out is endpoint exclusion using only the listed carrier, compactness, covariance, crossing and Gaussian-lower properties. They all coexist with a genuine finite endpoint in this explicit model. Further retyping of that package cannot turn its bounded factorization into a unit contraction at all windows.

The next endpoint-exclusion argument must use an additional property of the actual form and prove where that property enters. An endpoint-null Gaussian upper estimate would suffice, but its actual derivation remains missing.

## Validation and cursor

Self-contained analytic comparison, using only previously proved compact-support Fourier and Gaussian facts. No new external input, actual-zeta endpoint assertion, Lean source/workflow change or CI claim. Certified code remains cb92c1b4dfca298cbc79d5b7d25598ea370236bf, Actions run 37236113125/job 111535430775.

At 1607923, an explicit comparison family Qmod_a=Elog-2||h||_2^2 on the same supported logarithmic domains proves structural insufficiency. Its positive analysis sqrt(w) Fourier(h) is an isometry with closed range and trivial kernel; negative analysis sqrt(2)h factors boundedly through it. The family is support-consistent, translation invariant, fixed-window I+compact and norm-continuous after dilation. A direct uncertainty bound gives strict positivity for a<=e^(-8)/8, while a dilated smooth unit bump has negative energy for a> M1/e, with M1=integral |eta||Fourier(psi)(eta)|^2. Thus its positivity aperture is finite and attained with nonzero kernel. It obeys strict-enlargement rigidity, isolated null-window index jumps and the same moving-Gaussian logarithmic coercivity mechanism, yet full-source unit contraction fails beyond the endpoint and endpoint-null exponential Gaussian upper bounds fail. This comparison is not the actual zeta form and omits its arithmetic source identity, exact archimedean/pole and prime terms. It certifies that carrier completion, compactness, covariance, crossing counts and Gaussian lower coercivity alone cannot exclude endpoints. New input must exploit actual-zeta structure beyond that package. No actual endpoint/off-line zero, RH conclusion or new Lean/CI result; FULL TRANSPORT CLOSED remains open.
