# RPB108: the full native physical eigenvalue and a one-scalar contact control

Date: 2026-10-06 (America/Los_Angeles). Recovered source `f0d6ef5967a2b32adc1c2acdb9b47a0e43282aab`.
Definitions: [native mass-contact registry](../docs/TERMINOLOGY_RPB108_NATIVE_MASS_CONTACT.md).
Global/F4 lane. This retains every prescribed prime and pole term; no aperture calculation.

## Actual result and comparison boundary

The full actual native form has an attained lowest physical eigenvalue at every a>0:
\[
\lambda_{ph}(a)=\min_{h\in D_a,\ \|h\|_2=1}Q_a(h).
\tag{1}
\]
It is continuous and strictly decreasing in a. Its eigenspace is finite-dimensional and nonzero. If its dimension is r, its global regularity flag satisfies
\[
\dim(K_a^{\lambda_{ph}(a)}\cap H^j(\mathbb R))\le\max(r-j,0).
\tag{2}
\]
In particular at least one lowest actual physical eigenvector is not globally H1, even at a strictly positive certified window. This does not concern actual native nullity unless lambda_ph(a)=0.

Take c=23/25. The independent whole-domain certificate implies
\[
\mu_c=\lambda_{ph}(c)\ge10^{-26}>0.
\tag{3}
\]
The mass-shift comparison family B_t^{mu_c}=Q_t-mu_c mass has strict coercivity on every t<c, a nonnegative attained kernel at c, and a negative vector at every t>c. All prescribed prime translations, their activation thresholds, and the original signed pole are unchanged. Only the additional scalar mass subtraction is tuned. This is an actual-operator comparison, not an actual-zeta contact or a claim of negativity for Q_t.

It improves the earlier archimedean-only obstruction: even retaining the exact prime and pole boundary terms does not make the structural endpoint package exclude contact when a scalar mass shift is allowed.

## Attainment in physical mass and finite eigenspace

At each fixed support the established logarithmic envelope, finite prime bound and pole bound give a finite M_a such that
\[
Q_a(h)\ge\|h\|_{log}^2-M_a\|h\|_2^2.
\tag{4}
\]
Thus the infimum in (1) is finite below; a nonzero smooth interior test makes it finite above. A minimizing mass-one sequence is bounded in D_a by (4). Pass weakly in D_a and strongly in physical L2 using the established compact inclusion. The limit retains mass one.

The form is its logarithmic Hilbert squared norm plus a correction whose pairing is bounded by a constant times the two physical L2 norms. The correction is therefore continuous along this strongly L2 convergent bounded sequence; the logarithmic norm is weakly lower semicontinuous. This attains (1), without a physical operator-domain assumption on the minimizing sequence.

B_a^{lambda_ph(a)} is nonnegative on the entire domain. Positivity polarizes its zero diagonal into full mixed nullity. Its logarithmic Riesz operator is I+compact, since the extra mass operator J_a*J_a is compact. Consequently its nonzero kernel is finite-dimensional. This is the physical eigenspace, not the effective-background kernel of a coercive covariance.

## Shifted strict-margin rigidity and strict decrease

For any fixed real mu, the full mixed form Q-mu mass has unchanged-support custody and simultaneous translation invariance. The additional physical L2 pairing is itself translation invariant. Its logarithmic Riesz operator is I+compact on each fixed supported domain.

The existing strict-margin proof therefore extends verbatim: if a nonzero vector supported in [-a,a] were full mixed-null for B_b^mu on a strictly larger b, its arbitrarily many small translates would lie in the finite kernel at an intermediate support. Distinct translates of a nonzero compact L2 vector are independent by the Fourier exponential-polynomial argument. This is impossible. This extension needs no boundary moment injection and holds for every fixed scalar mu.

Let 0<a<b and choose a mass-one minimizer h at a. Inclusion and exact native custody give lambda_ph(b)<=Q_b(h)=lambda_ph(a). If equality held, h would minimize on D_b. Nonnegativity of B_b^{lambda_ph(a)} would then make h full mixed-null on D_b, contradicting the strict margin. Hence
\[
\lambda_{ph}(b)<\lambda_{ph}(a).
\tag{5}
\]
This is an actual full-native spectral theorem. It supplies no quantitative crossing slope, asymptotic sign, or positive lower bound as a tends to infinity.

For t<c, (5) gives B_t^{mu_c}(h)>=(lambda_ph(t)-mu_c) mass. Combining with the shifted version of (4) gives strict logarithmic coercivity. At c the comparison is nonnegative with attained kernel. For t>c a physical minimizer has B_t^{mu_c}<0. Thus c is the exact first contact of this comparison family, not just a possible local zero.

## Continuity with the correct norm

Pull back by the existing physical-L2-unitary dilation U_a to one supported logarithmic Hilbert domain. The actual form operators A(a) are norm-continuous, including prime thresholds. Physical mass is unchanged under U_a, so the added mass Riesz operator is fixed and compact. The comparison operators A(a)-mu J*J are norm-continuous as well.

For physical mass-one minimizers in a compact positive aperture interval, uniform (4) and one fixed transported smooth trial give a uniform logarithmic norm bound. Thus
\[
|q_a(f,f)-q_b(f,f)|\le\|A(a)-A(b)\|\,\|f\|_{log}^2
\]
applied to minimizers on both sides proves continuity of lambda_ph. This step cannot use the logarithmic-norm spectral infimum as though it were the physical eigenvalue. Dilation compares families here and changes physical vectors; all strict-margin and packet inclusions preserve their physical vector instead.

## Domain promotion and the shifted regularity flag

A supported L2 solution of the shifted interior equation satisfies
\[
m_a(D)h+p_h=\mu h\quad\hbox{on }(-a,a).
\tag{6}
\]
The right side is L2. Off support the mass term vanishes, so the same actual archimedean Carleman estimate and finite prime-translation estimates apply unchanged. On the interior use mu h-p_h as the core L2 representative. Logarithmic growth still puts the possible endpoint defect in H^{-1/4}; the already proved cutoff removal excludes it. Hence the core is globally L2 and h promotes to D_a and full B_a^mu mixed-nullity. Constants increase by |mu|; no zero-shift promotion theorem is invoked with a changed equation silently.

If h is globally H1, its supported L2 derivative g satisfies the derivative of (6). Integration by parts gives M_-(g)=M_-(h)/2 and M_+(g)=-M_+(h)/2; the exact pole commutes with this differentiation. The constant mass term also commutes. Shifted promotion therefore puts g in K_a^mu. The finite-dimensional strict-descent proof now gives (2): equality of adjacent nonzero regularity subspaces would make differentiation an endomorphism and violate Fourier-polynomial independence.

The existing finite-logarithm and every-s<1/2 bootstrap also accommodates the added bounded scalar mass term. Nothing here supplies global H1 to the whole eigenspace, a dimension-one theorem, or a sign-preserving modulus inequality for the full prime/pole form.

## Fresh comparison packet: source custody is different

At c, preserve the actual full source analyses P,N. Their original identity is still Q=||P h||^2-||N h||^2. For mu_c>0 the comparison identity is instead
\[
B^{mu_c}(h)=\|Ph\|^2-\|(Nh,\sqrt{\mu_c}J h)\|^2.
\tag{7}
\]
The added mass channel is infinite-dimensional and artificial. It is not an actual divisor coordinate and does not establish actual WD-T10 domination or historical retained-packet attachment for Q.

Choose an orthonormal polynomial basis of physical L2(-b,b). Its mass observations separate every supported physical vector. On the finite-dimensional comparison kernel, finitely many of these rows already separate the kernel: the decreasing intersections of coordinate kernels stabilize, and their full intersection is zero. Call their weighted finite map R^mu. Nonnegative Fredholm stabilization makes G_c^mu=B_c^mu+(R_c^mu)*(R_c^mu) coercive; norm continuity keeps it coercive on some b>c. Fix b with no new prime threshold after c. The common-background square root, support filtration, reduced compensators and finite source defect now follow by the already proved algebra, for this explicitly different comparison selection.

Polynomial observation profiles are smooth on the fixed compact support, so the translated observation difference is O(s). The shifted multiplier retains the logarithmic envelope and the physical residual derivative proof above. Consequently the quadratic gain theorem has a lawful comparison extension:
\[
e_s^{mu_c}(h)=O(s^2)\quad\Longleftrightarrow\quad h\in H^1(\mathbb R),
\]
and then e_s^{mu_c}=o(s^2). Equation (2) supplies a nonzero comparison null vector for which limsup e_s^{mu_c}/s^2=infinity. All actual primes and the physical pole are present in that control. No actual negative-coordinate selection for this shifted kernel has been identified; it would be unlawful to rename R^mu as the actual selection R of F4.

## Exact obstruction and remaining theorem

Failed implication: prescribed prime/pole kernels + norm-continuous support family + strict initial comparison positivity + nonnegative Fredholm contact + finite smooth stabilization + derivative promotion + residual/gain algebra -> contact exclusion or a quadratic gain bound on the whole contact space.

The comparison above disproves this inference when scalar mass subtraction and its added source channel are allowed. It belongs to **endpoint exclusion**. Unlike the earlier archimedean control it retains all native prime and pole terms. Its precise deviation is the nonzero scalar mu_c and the corresponding artificial mass channel; it does not falsify an arithmetic theorem which uses the exact zero-shift source normalization.

The actual decisive target remains lambda_ph(a)>0 for every finite a, equivalently no actual nonnegative contact at mu=0 (the established global dichotomy and attained physical eigenvalue discharge the equivalence). A more local sufficient target is the actual quadratic gain bound on the full contact eigenspace. Neither is proved. A proof that only repeats the shifted-stable structural properties cannot supply the missing zero-shift normalization input. No enlarged full mixed-null transport is obtained; shifted strict-margin rigidity forbids it for the same nonzero comparison vector as well.

## Validation and custody

Pinned sources and repeated rational algebra controls are in notes/data/RPB108_NATIVE_MASS_CONTACT_20261006.json. The controls exhibit positive unshifted nested matrices, an endpoint contact after one scalar shift, a strictly negative enlarged trial and its exact inverse-residual gain. They are not actual arithmetic matrices or an eigenvalue computation. The attainment, continuity, margin rigidity and shifted promotion proofs are analytic, not Lean certified. No Lean/workflow change or new axiom/CI claim. Historical wording and certificates remain unchanged. Actual aperture frontier 23/25; F4 and FULL TRANSPORT CLOSED remain open.
