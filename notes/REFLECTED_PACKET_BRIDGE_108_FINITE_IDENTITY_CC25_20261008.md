# RPB108 CC25: exact local Weil identity excludes finite divisor alterations

Date: 2026-10-08 UTC. Coupled parent: 4c6b0e8caf1b67d666eaa61c2fdc223a0bbd3b8b.
Definitions: [finite identity rigidity](../docs/TERMINOLOGY_RPB108_FINITE_IDENTITY.md).

## Result and its significance

If two reflection-symmetric complete divisor dictionaries differ only at finitely many locations, and their original normalized mixed source forms equal the SAME native form on every supported smooth test in one nonempty open aperture, then their finite difference is zero.

Thus CC24's location perturbations cannot preserve the complete native Weil identity, even on a fixed small aperture. They are legitimate controls of averaged location estimates, not counterexamples to any implication from the exact full identity. This new analytic rigidity theorem makes that scope boundary explicit rather than leaving it as an unevaluated qualification.

The theorem does NOT establish the requested near-critical source-shell estimate. There is no known critical-line reference dictionary with the same actual native form to which we can apply it. Its inverse finite-moment problem is also not uniformly stable over coalescing locations. Neither the existence of an arithmetic strict budget nor logical independence from the full identities is proved.

## 1. Named original identities and lawful subtraction

ActualZetaSourceDecomposition.lean supplies the full-copy sampling and mixed summability on the Green dictionary; ActualZetaNativeWeilForm.lean supplies its exact mixed native arithmetic equality. The inherited supported canonical extension is analytic. No new statement about the independently named historical WD-T38 carrier or a full physical operator domain is used.

Fix a>0. Work with C_c^infinity(-a,a), a subspace of that canonical domain. Let the two source dictionaries be square summable there, and let their grouped signed multiplicity difference c_q have finite support. Reflection symmetry means c(beta,theta)=c(-beta,theta); ordinate sign partners and their multiplicities are also retained. Removed copies have negative coefficients. Combine coincident locations before calling the remaining rates distinct.

Subtracting the two complete mixed source equalities is lawful: the common infinite part cancels AFTER its convergent mixed pairing, and the remainder is finite. We do not sum a pointwise infinite zero kernel. The same native form includes the same prime coefficients and both signed poles; merely sharing the label 'explicit formula' would not be enough.

## 2. Exact finite difference kernel and normalization

The single-copy normalized positive-minus-negative mixed kernel is

    exp(i theta(y-x))
       [cosh(beta x)cosh(beta y)-sinh(beta x)sinh(beta y)]
      =exp(i theta(y-x))cosh(beta(y-x)).                    (1)

Hence the finite form difference is

    Delta Q(h,f)=integral integral conj(h(x)) f(y) K(y-x) dx dy,
    K(u)=sum_q c_q exp(i theta_q u)cosh(beta_q u).           (2)

There is no raw doubled-source factor in (1)-(2). Reflection partners DUPLICATE the cosh contribution rather than cancel it. Because c is beta-reflection invariant,

    K(u)=sum_j c_j exp(lambda_j u), lambda_j=beta_j+i theta_j, (3)

where the coefficients in (3) are exactly the signed multiplicities of the distinct reflected location atoms. Beta=0 fixed points contribute once per actual copy. Without reflection invariance, only the beta-even effective measure would be detected; an antisymmetric artificial change could be invisible. This is why the partner hypothesis is necessary, not cosmetic.

## 3. Equality on an open physical aperture forces K=0

Suppose Delta Q(h,f)=0 for EVERY h,f in C_c^infinity(-a,a). Choose smooth approximate delta bumps around any two interior points x0,y0, with integral one and support inside the aperture. Since the finite K is continuous, (2) tends to K(y0-x0). Therefore K(u)=0 for every u in (-2a,2a).

This uses a finite entire kernel only; there is no singular endpoint trace, zero-cutoff exchange or operator-supremum limit. The complex test space is the original one. If complete diagonal equality is supplied instead, complex polarization first gives the mixed equality.

The entire exponential polynomial K vanishes on an open real interval, hence every derivative at zero vanishes. For m distinct effective rates,

    0=K^(k)(0)=sum_{j=1}^m c_j lambda_j^k, 0<=k<m.        (4)

The Vandermonde matrix has determinant product_{i<j}(lambda_j-lambda_i), which is nonzero. Thus all c_j vanish. This proves the local exact rigidity claim. Positivity, a critical eigenvector, a source-shell inverse, a numerical old margin and RH are NOT assumptions of this rigidity theorem.

In particular, the CC24 added quartet has a nonzero finite K and already changes the complete native mixed pairing on every open aperture. Its scalar pair-correlation asymptotic can remain unchanged while this exact mixed identity changes. Those are different levels of source information.

## 4. Why rigidity is not the missing arithmetic estimate

The actual divisor already satisfies the actual native equality. To use Section 3 to exclude its off-line locations, one would need a DIFFERENT divisor, known to be on the critical line, with precisely the same native mixed form and only finite difference. Neither existence nor equality of such a reference is established. Projecting actual locations onto the critical line changes (2); there is no premise making the resulting K zero. A generic positive reference form is also not the same arithmetic form.

Even a hypothetical assertion that only finitely many zeros are off line does not create that reference equality. The finite difference from a critical-line projection is then detectable, rather than contradictory. Exact detection is not proof that the detected native form has positive sign.

The requested target remains J M_t^(-1)J*<=q Lambda G on the actual old critical modes, plus a low-output budget ell with q+ell<1. Section 3 has no G, no old critical equation and no estimate on those combined rows. The uniqueness of finite coefficients from all mixed tests does not supply the needed quantitative defect cancellation.

We therefore narrow the earlier negative conclusions carefully: diagonal bounds, strip/density statistics and the inspected scalar correlation asymptotics do not suffice for their proposed transfers; the full exact native identity forbids our finite alteration models. None of these statements proves that ALL possible arguments from the full identity fail. The original full-identity implication asked by the user remains unresolved at this checkpoint.

## 5. Quantitative instability even for a fixed number of finite atoms

For a simple stability control put four critical-line effective atoms at theta=+/-1 and +/-(1+epsilon), with coefficients +1,+1,-1,-1, 0<epsilon<=1. This is a legal balanced finite signed difference preserving both partner symmetries. Its kernel is

    K_epsilon(u)=2cos(u)-2cos((1+epsilon)u).

The mean value theorem gives |K_epsilon(u)|<=2epsilon|u|. Thus on (-a,a),

    |Delta Q(h,f)|<=8a^2 epsilon ||h||_2 ||f||_2.           (5)

The coefficient supremum remains one, even while the whole finite difference form tends to zero on the fixed aperture. Its first four derivative moments are

    (0,0,4epsilon+2epsilon^2,0).

Their supremum is at most 6epsilon. Hence any inverse-Vandermonde coefficient estimate in these supremum norms has a constant at least 1/(6epsilon). There is no bound uniform over these finite location changes based only on cap, number of atoms and bounded displacement/height. This does not assert that the actual zeta divisor can be altered arbitrarily or has arbitrarily close distinct zeros.

This stability control concerns coefficient reconstruction, not the shell estimate itself. It proves that the finite-rigidity proof cannot be promoted to a uniform quantitative theorem merely by assigning a cap-only inverse constant to its Vandermonde matrix. A genuinely new estimate on the actual critical correlations could still avoid that inverse problem entirely.

## 6. Positive-level mass cannot be hidden as a finite alteration

For Q-mu||h||_2^2 with mu>0, the complete extra negative channel is sqrt(mu) times the ENTIRE physical vector. It is not a finitely altered zero-source dictionary.

Every finite kernel (3) depends on finitely many linear exponential moments of a test. Choose more linearly independent smooth disjoint bumps than there are such moments. A nonzero linear combination h annihilates every moment, so Delta Q(h,h)=0. Its mass mu||h||_2^2 is strictly positive. Therefore no finite exponential kernel can equal the nonzero physical mass form on the whole supported smooth domain. This is a finite-rank argument, not an assumption about canonical compactness or endpoint regularity.

The inherited full positive-level test remains original P=I, N=(9/25,12/25), mu=16/25, original budget 9/34 and shifted whole budget one. All physical mass rows are retained. Rigidity does not relabel that shifted null vector as an original null vector or exclude a genuine crossing. The genuine differential and logarithmic crossing discriminators remain inherited; their native forms are not the SAME original arithmetic form presumed in Section 3.

## 7. Validation and present exit status

23,330 exact checks pass: 838 new (72 complex rational Vandermonde recovery/determinant checks across 18 cases, 258 reflection/normalization checks, 160 coalescing-location stability checks and 348 full-mass rank checks) plus 22,492 inherited CC24 checks, including complete physical pulse, genuine crossing and full positive-level controls. The finite complex matrices retain all reflected/sign atoms and mixed coefficients. The functional local-kernel argument and infinite-background cancellation are analytic; finite tests do not prove them in Lean or evaluate actual critical source modes.

The exact finite-alteration loophole is now closed for the complete original native identity. Stop using CC24-style modified divisors as possible full-identity counterexamples. Their averaged-statistic limitation remains valid in its stated scope.

The all-cap old-gap-independent arithmetic relative bound is still neither proved nor disproved for actual zeta. A next successful pass needs a NEW actual estimate for the joint forced rows, not another normalization, scalar statistic, finite alteration or qualitative uniqueness argument. Original whole-domain positivity remains internally certified through 21/20, even0/odd0, joined physical margin 1/(3*10^63). RH/F4, retained attachment, reusable continuation, accumulated finite-cap relative loss and Lean remain open. Global stays paused at NF71; Aperture and Pre-Contact Shadow remain paused. No new aperture.
