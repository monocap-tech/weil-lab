# RPB108 CC4: exact original relative loss and the finite-contact dichotomy

2026-10-08 UTC / 2026-10-07 Pacific. Definitions: [CC4 registry](../docs/TERMINOLOGY_RPB108_ARITHMETIC_RELATIVE_LOSS.md).
Coupled base `f414e2464775300d93b4e31890ec715f2282f1bb`; recovered shared head `76a2ef43f9495d2a076fd1e0e472c7645e681f49` (NF63).
Aperture and Pre-Contact Shadow stay paused. The user redirected this step from the archive-blocked target matrix calculation to an analytic relative-loss principle.

## Outcome before interpretation

There is an exact ORIGINAL-form relative-loss identity on a protected nested Schur chart. Its accumulated log-determinant loss is additive and finite on every compact positive subinterval. At a hypothetical finite first contact, a locally protected chart exists and its loss necessarily diverges. Thus finite-aperture divergence is compatible with the current anchor, contact structure, continuity, bounded source norms and finite prime dictionary. Those facts do NOT rule it out.

The new identity makes the missing arithmetic estimate precise. An independently proved finite bound on the accumulated loss, with complement protection, would exclude contact. No such bound is established here. This is an exact conditional mechanism and a tested obstruction to its automatic closure, not an unconditional all-aperture positivity theorem.

## 1. Anchor and the carrier that makes loss monotone

The imported aperture-one certificate remains

    Q_1>=4e-32 physical mass, Q_1>=2e-34 E_log.

Its physical 112-vector corrected Schur certificate is not relabeled as an exact canonical matrix or replayed in CC4. In any fixed finite physical E contained in D_1, the exact completed graph, when its complement is protected, satisfies

    S_1(x)>=4e-32 ||W_1 x||_2^2>=4e-32 ||x||^2.

The stronger saved physical finite margin may be imported separately in its own coordinates. Only the displayed whole-domain bound is needed here.

Use physical support inclusion, NOT a moving dilation chart, for monotonicity. For s<t the exact original form on an old physical vector is unchanged: Q_t(h,k)=Q_s(h,k) for h,k in D_s. Every original divisor row and normalization is the same, and newly active prime terms have zero old/old overlap.

Fix a finite physical E contained in D_s, with physical orthonormal coefficient basis, and let F_a=D_a intersect E^perp_mass. These complements are nested. Assume their original forms C_a are coercive in the canonical norm, uniformly on the chart. The weak complement solve is therefore well-defined. Its graph satisfies

    W_a x=x-T_a x, Q(W_a x,F_a)=0,
    S_a(x)=min_{z in F_a} Q(x+z).

Consequently

    S_t<=S_s                                             (1)

in Loewner order. This is a whole minimization, not a trial upper bound presented as a lower bound. The fixed coefficient basis matters: arbitrary aperture-dependent changes of basis add coordinate losses and destroy this literal comparison.

This monotonicity is a consequence of exact unshifted support restriction. It is not an independent zeta-specific arithmetic inequality.

## 2. Exact shell reaction, with all inverse information retained

Choose a canonical Hilbert orthogonal complement Y of F_s inside F_t. Eliminate F_s first. For y in Y let V y=y-C_s^(-1)Q(F_s,y), interpreted as the original weak form solve. Define

    D_st(y,y')=Q(Vy,Vy'),
    H_st(x,y)=Q(W_s x,Vy)=Q(W_s x,y).

D_st is coercive because C_t is protected; canonical projection onto Y retains the lower norm bound. In the already completed coordinates the enlarged form on E+F_t is

    diag(C_s, [[S_s,H_st^*],[H_st,D_st]]).

The SECOND exact completion gives

    S_t=S_s-H_st^* D_st^(-1) H_st,
    W_t=W_s-V D_st^(-1)H_st.                           (2)

The actual inverse reaction in (2), rather than ||B||^2/c or an invented same-Gram inverse, is the loss. This is compatible with PS3 and with CC3's successful actual trial: a trial upper bound on the inverse may underestimate the exact Schur block, but is not this exact identity.

For S_s>0 put R_st=S_s^(-1/2)(S_s-S_t)S_s^(-1/2). Then R_st>=0, and strict positivity at t is exactly R_st<I. Thus

    Lambda(s,t)=-log det(I-R_st)
               =log det S_s-log det S_t.              (3)

All shell and old-complement mixed terms are retained. The finite retained space does not imply a finite shell or replace the infinite complement inverse by a finite matrix.

## 3. Accumulation without an unsupported derivative

For any partition s=a_0<...<a_m=t inside one chart,

    sum_j Lambda(a_j,a_(j+1))=Lambda(s,t).             (4)

The relative matrices at different steps need not commute. Determinants telescope nonetheless. If d=dim E, each relative ratio has eigenvalues in (0,1], so

    Lambda(s,t)/d <= ell(s,t) <= Lambda(s,t).

More importantly,

    S_t >= exp(-Lambda(s,t)) S_s.                     (5)

Indeed the product of the relative eigenvalues is at most their minimum. The total worst-direction step loss over ANY partition lies between Lambda(s,t)/d and Lambda(s,t), and (5) propagates a certified initial margin.

No global H1 bound, prime-translation derivative, or absolute continuity in aperture is used. In a protected chart S_a is continuous: the right limit follows by bounded weak compactness of complement minimizers, support closure, and lower semicontinuity of Q+beta mass with compact physical mass; the left limit follows from the existing smooth-core density, with a small finite E-projection correction. Uniform complement coercivity supplies the minimizer bounds. Thus S has bounded variation by (1), and its loss has the optional Stieltjes form

    Lambda(s,t)=integral_(s,t] tr[S_a^(-1)(-dS_a)].     (6)

On positive compact subintervals this is the continuous bounded-variation chain rule for log det. It need not have a density in da. Only if absolute continuity is separately proved may one write -tr(S_a^(-1)S_a')da.

For a merely norm-continuous moving-coordinate matrix, negative variation can be infinite even without contact. CC4 avoids that false implication by using (1). It does not substitute a full-domain logarithmic modulus for a differentiable loss rate.

## 4. Finite-aperture divergence: the exact conclusion

Suppose one chart extends to a finite A, its complement remains uniformly protected, and S_a>0 for a<A. Continuity then yields precisely:

    Lambda(s,A-)<infinity iff S_A>0;
    ker S_A nonzero iff Lambda(s,a)->infinity as a increases to A.

This follows because the bounded decreasing finite matrices have a limit, and their determinant tends to zero exactly when that limit has a kernel. In the finite-loss case (5) gives a positive endpoint Schur lower bound. Together with the protected complement and bounded graph/lift, square completion gives whole-domain physical and canonical positivity. A finite number of admissible chart changes adds only finite coordinate/comparison costs; no infinite reset is used to hide a divergent loss.

If the complement is NOT protected, finite Schur loss alone has no exclusion force. For example A_a=diag(1,A-a), retaining only the first coordinate, gives S_a=1 and Lambda=0 while the complement reaches zero. Every use of the principle must retain the complement gate. The certified aperture-one 112-complement is not asserted to stay positive at arbitrary larger apertures.

At an actual hypothetical first contact a_* the standing I+compact and physical compact-resolvent structure give a finite kernel K of dimension r and a positive gap above it. A LOCAL protected fixed chart can be chosen without assuming endpoint regularity: smooth functions supported strictly inside a_* are mass-dense; choose finitely many whose mass pairings detect all of K, and put them in E. They have common support inside some s<a_*. Then F_(a_*) intersects K only in zero. Positivity plus the canonical Fredholm gap makes C_(a_*) coercive on that closed complement; restriction gives the same protection below a_*. This is an existence chart, not a computed retained space or an assumption that the original E112 detects K.

In this chart ker S_(a_*) has dimension r, so its accumulated loss diverges. The contact theorem's exactly r negative full modes immediately to the right transfer by congruence to exactly r negative Schur directions while this complement stays protected. No contact is asserted to exist. The odd-order right-side TRIAL upper rates are not promoted to matching exact Schur rates or to a left-side asymptotic. Divergence requires no such rate.

The anchor starts the positive interval; it does not bound the subsequent logarithmic loss. A local contact chart may begin at s>1. Earlier compact positive portions admit finite protected-chart coverage, but their existence does not furnish an effective all-window arithmetic bound.

For a chart actually starting at one, an independent bound Lambda(1,b)<=M_B, C_b>=c_B in canonical norm, and ||W_b||_(coeff -> D_B)<=L_B would give the explicit consequence

    S_b>=m_B I, m_B=4e-32 exp(-M_B),
    Q_b>=delta_B E_log,
    delta_B=(1/2)min(m_B/L_B^2,c_B)>0,
    g_b^2<=1-delta_B/C_positive,B^2<1.

The simple factor 1/2 uses ||W_b x+z||^2<=2L_B^2||x||^2+2||z||^2. C_positive,B is the proved upper norm of COMPLETE original positive analysis, not an interior-source-surrogate norm. These are conditional consequences with independently bounded inputs, not new evaluated constants. A different starting chart uses its certified starting margin instead.

## 5. The arithmetic numerator and complete original source identity

Use the published NORMALIZED complete sources, with the historical partner-counting factor already absorbed:

    Q(h,k)=<P h,P k>-<N h,N k>.                      (7)

Every analytic multiplicity copy, ordinate, normalization and both mixed slots are retained. For every old graph and shell graph,

    H_st(x,y)=<P W_s x,P V y>-<N W_s x,N V y>,
    D_st(y,y')=<P V y,P V y'>-<N V y,N V y'>,
    S_s(x,x')=<P W_s x,P W_s x'>-<N W_s x,N W_s x'>.

Equations (2)–(3) are therefore exact arithmetic relative-loss identities for the ORIGINAL completed form. They do not invent a new source dictionary for the completed graph, omit the shell source, or assume Q(W_s x)=0. The graph solves a FORCED complement equation, as in CC2.

On any fixed finite larger aperture B the complete analysis is bounded on D_B. Protected complements keep W_a bounded in that norm. At contact the complete source energies on a limiting nonzero kernel direction converge to equal NONZERO finite values, by positive observability and the full-source convergence theorem. It is their signed difference that vanishes. Thus neither a divergent absolute source norm nor infinitely many newly active primes is required for divergent relative loss.

In the gain formulation, the original defect is 1-||N h||^2/||P h||^2. Contact collapses this defect while its denominator remains nonzero. Dividing a bounded absolute loss by that collapsing signed gap can accumulate infinite logarithmic loss. Bounded sampling, injectivity, strip width, continuity and finite prime total variation alone do not bound this ratio.

The missing ARITHMETIC NONDIVERGENCE theorem is an independent bound, on every finite endpoint, for (3) or (6), with complement protection. It must control the actual cross-prime/archimedean/pole shell reaction relative to S, rather than merely absolutely. Proving such a bound would exclude first contact and hence supply the open complete-gain theorem. The identity itself does not prove the bound. NF62's separated-prime budget failed the joint-bound comparison; NF63's positive cutoff background still requires its whole compact-gain estimate. Neither result is silently promoted here.

## 6. Genuine crossing operator and bounded absolute loss

Consider the actual differential form on nested H0^1(-a,a),

    q_a(h)=||h'||_2^2-||h||_2^2,
    P h=h', N h=h.

Its lowest physical eigenvalue is lambda_1(a)=(pi/(2a))^2-1, obtained by the first Dirichlet cosine. It is positive at a=1, zero at a_*=pi/2, and negative immediately afterward. The next level remains positive at contact. It has compact physical resolvent and a genuine one-dimensional first-contact cluster, not an arbitrarily assigned spectral label. Both source norms of the unit ground mode stay bounded near contact.

Choose a nonnegative normalized smooth retained v supported inside (-1,1). Its pairing with the contact ground mode is nonzero, so its complement is protected near contact. The exact scalar Schur block is

    S_a=1/<v,L_a^(-1)v>, a<a_*.

The ground resolvent term has nonzero weight and diverges as lambda_1(a)^(-1); the remaining spectrum stays separated. Hence S_a tends to zero, and the EXACT Schur loss diverges at this finite aperture. This operator passes the anchor/sign, nesting, source, compactness and cluster controls. It is NOT the zeta arithmetic and does not assert an actual zeta crossing. It refutes deriving nondivergence from those structural inputs alone.

The objection that this differential control has quadratic rather than logarithmic high-frequency growth can also be removed. On the EXACT canonical logarithmic carriers use the genuine form

    q_a(h)=E_log(h)-kappa||h||_2^2,
    P h=sqrt(w) Fourier(h), N h=sqrt(kappa)h.

Let ell_1 be the attained lowest level of E_log on D_1. Compact physical inclusion gives attainment, and ell_1>1 because w(xi)>1 almost everywhere away from zero, so every nonzero unit vector has energy strictly above one. Choose 1<kappa<ell_1. Then q_1 has a positive physical gap and a canonical gap by its Garding bound. Dilation of one fixed smooth compact unit bump to arbitrarily large supports makes its E_log energy tend to one by dominated convergence; therefore q is negative on a vector at some FINITE larger aperture. Its pulled canonical family is I plus compact and norm-continuous, with the same threshold-free logarithmic carrier construction. The first-contact argument supplies a finite attained kernel, and the locally protected Schur chart above forces divergent relative loss there. This is an analytic genuine logarithmic-operator control, not a computed zeta vector or an asserted full odd-order branch law. It shows that even the logarithmic coefficient and original-type full source identity do not supply the missing arithmetic nondivergence estimate.

Finite matrix controls likewise use A_t=[[sigma(1-t)+k^2,k],[k,1]], with complete source Grams P*P=[[sigma+k^2,k],[k,1]], N* N=diag(sigma t,0). Its exact graph is (1,-k), S_t=sigma(1-t), and its sources remain bounded. At t_j=1-2^(-j), each relative step loses half the gap, absolute losses sum to less than sigma, and Lambda(0,t_j)=j log 2 diverges. Taking sigma equal to the anchor lower bound merely changes the initial scale; it does not change the conclusion.

## 7. Positive-eigenmode and threshold controls

For a positive original physical level mu, the shifted form is Q_mu=Q-mu mass. Its complete negative source is (N h,sqrt(mu)h). ALL complement, shell and graph blocks must be recomputed for this shift. At a shifted contact,

    Q(h,k)=mu<h,k>_mass on its original eigenspace,

not zero. Shifted relative loss can diverge while the ORIGINAL form and its ORIGINAL relative loss remain positive and finite. The differential example with potential 1+mu reaches shifted contact at pi/(2sqrt(1+mu)), where the original ground level is mu>0. This prevents the contact-cluster theorem or a shifted unit-gain calculation from excluding original contact by relabeling.

At a finite B there are only finitely many original prime powers n<=exp(2B). Their weights remain Lambda(p^r)=log p, not r log p. At a_n=log n/2 the supported translation overlap is zero, including equality. In a nested step s<t the newly active terms are zero in the old/old slot and occur lawfully in old/shell and shell/shell slots. Their indirect inverse reaction must not be discarded. Thresholds create no form jump or loss atom when the chart is protected and positive. They do not guarantee a finite relative-loss density, and contact coinciding with a threshold is not ruled out.

No fixed-width smearing, prime continuum replacement, frozen source prefix, discarded pole, global H1 assumption or unproved aperture derivative is used. The full original source identity alone permits both the positive-eigenmode control and a genuine crossing; zeta-specific arithmetic exclusion still requires the new bound stated in section 5.

## Validation and standing

All 4,489 exact rational controls pass. The validator checks nested two-stage completions, noncommuting matrix determinant accumulation, positive mass shifts, source-energy residuals, finite absolute loss versus divergent logarithmic loss, complement-only contact, complete-source versus prefix errors, and the actual prime-8 dictionary/threshold ordering. In particular the full absolute prime-8 budget is checked below 13/2 (display 6.34260); the aperture-one five-term bound below 6 is NOT reused after activation of 8. Neither budget is substituted for the sharper joint prime norm. The differential/logarithmic crossing proofs and infinite-dimensional nested-chart theorem are analytic, not Lean-certified. Finite controls are not their proof.

The target's large source/Gram archives remain unreadable through the connector and are not used or replayed here. CC3's directional certificate, the aperture-one anchor, NF51–NF63 and all historical source custody remain unchanged. No new certified aperture, actual zeta contact or negative vector, arithmetic nondivergence bound, RH, F4, full transport or Lean closure is claimed.
