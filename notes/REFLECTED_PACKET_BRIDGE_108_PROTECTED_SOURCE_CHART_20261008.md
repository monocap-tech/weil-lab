# RPB108 NF69: construct a protected source chart without source eigenvectors

2026-10-08 UTC / 2026-10-07 Pacific. Recovered Global `2f7a867881ae49e99f25d454e253c7d1a43496d4` (NF68); inspected Coupled `191b3c04dbddf9789c19cbb4ad7562deac2e9ec1` (CC8) read-only. Definitions: [protected source chart](../docs/TERMINOLOGY_RPB108_PROTECTED_SOURCE_CHART.md).

**Result.** An independently protected physical complement constructs a finite complete-source OUTPUT chart without finding source eigenvectors and without assuming whole original positivity. Its construction solves only the positive covariance on the protected physical complement. The finite source Schur gate has exactly the same negative index and nullity as the existing physical Schur gate.

This resolves NF68's analytic source-coordinate construction obstacle, not its arithmetic enclosure. It identifies why a change to source coordinates alone supplies no new exit: the actual complete reaction remains the unresolved whole physical Schur sign. The source chart has all mixed output blocks; it is NOT NF68's spectral projector with its off-diagonal deleted.

## 1. Independent source carrier and protected physical chart

Work on one fixed aperture D_a. Keep the full normalized original positive/negative analyses P,N, the SAME physical vector and Q=P*P-N*N. The actual positive-carrier equivalence gives bounded P,N and P bounded below on D_a, independently of unit domination; see [positive carrier equivalence](REFLECTED_PACKET_BRIDGE_108_POSITIVE_CARRIER_EQUIVALENCE_20261004.md). This is an ANALYTIC result with a nonconstructive fixed-window positive lower constant, not a new Lean theorem.

Let E be a d-dimensional physical retained chart, F its closed complement in the canonical carrier, and assume independently

    Q(f)>=c ||f||_D^2, c>0, on F.                 (1)

If the actual certificate is instead Q(f)>=c2 ||f||_2^2 on F, combine it with the independently established ORIGINAL Garding inequality

    Q(f)>=a0 ||f||_D^2-K0 ||f||_2^2, a0>0, K0>=0.

Multiplying the first inequality by K0/c2 and adding the second gives the exact compatible bound

    Q(f)>=cD ||f||_D^2,
    cD=a0 c2/(c2+K0)>0.                         (1a)

Thus use c=cD in (1)-(2), not c=c2. The historical canonical source Garding normalization has a0=1. This norm conversion uses positivity only on F, not on the whole domain, and introduces no whole-gap inverse. Numerical source bounds still require certified a0,K0 and M.

Because ||Pf||^2=Q(f)+||Nf||^2, the restricted positive covariance

    L_F=P_F*P_F >=c I_F                           (2)

is uniformly invertible. This inverse depends on the protected complement, not the smallest WHOLE Q eigenvalue. It stays protected when the retained original Schur gap closes. Whole-domain positivity is not a premise.

For each retained basis vector e_i, solve

    f_i=L_F^(-1)P_F*P e_i, h_i=e_i-f_i,
    u_i=P h_i, y_i=N h_i.                         (3)

Then <u_i,Pf>=0 for all f in F. Since P is a bounded isomorphism onto its closed range, P(F) is closed and codimension d in V=P(D_a). Consequently

    U=V intersect P(F)^perp=span(u_i), dim U=d,
    V=P(F) orthogonal-direct-sum U,
    Y=T(U)=span(y_i), dim Y=r<=d,
    T(Ph)=Nh.                                    (4)

The h_i are the positive-source-orthogonal physical lifts of the retained quotient. They need not be physically orthogonal to F and are not original Q-Schur graph lifts. Their construction does not use Q_F^(-1), the whole Q inverse, a hypothetical null vector or source eigenvectors. Multiplicity copies and every actual ordinate remain inside P and N.

Y is a concrete finite output SUBSPACE specified by complete negative images of d physical vectors. Constructing it analytically does not mean its actual infinite coefficient vectors, basis Gram or numerical projection have been enclosed.

## 2. Quantitative protection of the entire output complement

Let ||P||<=M in the SAME canonical norm as (1), and put delta=c/M^2. Then 0<delta<=1 and

    ||T v||^2<= (1-delta)||v||^2, v in P(F).        (5)

Indeed Q(f)>=c||f||_D^2>=(c/M^2)||Pf||^2. If n is orthogonal to Y=T(U), then T*n is orthogonal to U and hence lies in P(F). Therefore T*n=T_F*n, where T_F=T restricted to P(F), and

    <(I-TT*)n,n> >=delta||n||^2, n in Y^perp.      (6)

This output protection uses the ADJOINT of the restricted contraction. It is not a claim that T maps P(F) into Y^perp, which need not hold. It is a compression estimate, not invariance of Y or Y^perp under TT*.

Thus the entire possibly infinite-dimensional output complement is protected, with rank at most d for the retained output chart. Neither compactness of T nor positivity of the entire form was assumed. If r=0, all of T is a contraction with a strict gap under (5), so whole positivity follows in that special case.

For the target a=21/20, CC8 retains a physical L2 complement lower c112=699/1000. Equation (1a) gives cD=a0(699/1000)/(699/1000+K0), and hence delta=cD/M^2 in the canonical source metric. This is a quantitative symbolic dictionary. Certified numerical a0,K0,M still have to be supplied before quoting a numerical delta; c112 is not itself the source-complement gap.

## 3. Correct finite source sign, with all mixed blocks

Write D_out=I-TT* on the COMPLETE negative source ambient. Let Pi project onto Y and use the orthogonal output decomposition Y direct-sum Y^perp:

    D_out=[[G,B],[B*,C_out]], C_out>=delta I,
    H_out=G-B C_out^(-1)B*.                       (7)

This is not generally the spectral decomposition in NF68. The old mixed output block B can be nonzero. Exact bounded square completion gives

    D_out congruent to diag(H_out,C_out).          (8)

Consequently whole ORIGINAL strict positivity/gain g_a<1 is equivalent to H_out>0. All original source rows and the WHOLE complementary output inverse remain in (7). A nonorthonormal basis y_i must retain its source Gram; replacing that Gram by I without whitening changes the form. If the y_i are dependent, first pass to an independent output basis or work on their actual quotient. Rank r is not presumed equal to d.

For example, D=[[1/4,1/2],[1/2,1/2]] has a protected low output 1/2 and positive retained diagonal 1/4, but H_out=-1/4. I-D is strictly positive, so this is a lawful source-defect algebra control. Dropping the mixed block would falsely certify the original whole sign.

## 4. Exact comparison with the physical completed Schur form

Let S_phys be the original physical Schur form on E obtained by eliminating the independently protected F. Physical square completion gives the full Q's negative index and nullity equal to those of S_phys.

Positive-source coordinates send Q to I_V-T*T by a bounded invertible change of variables. The nonpositive spectral directions of I_V-T*T and I_negative-TT* have identical multiplicity: for singular values at or above one, T and T* give inverse eigenmode correspondences up to the nonzero eigenvalue factor. Alternatively this follows by square completing the joint source block with identity diagonal in either order. No compact source analysis is used.

Equation (8) therefore yields

    n_minus(S_phys)=n_minus(H_out),
    nullity(S_phys)=nullity(H_out).                (9)

Both matrices are finite. If dim E=d and dim Y=r, their positive indices differ by d-r:

    n_plus(S_phys)=n_plus(H_out)+(d-r).            (10)

Thus S_phys>0 iff H_out>0; a genuine original contact or negative direction cannot disappear by changing between these charts. Finite Hermitian inertia also supplies a congruence to H_out plus d-r positive directions, although the two bases and numerical margins are generally different. Neither matrix is identified entrywise with the other.

This establishes a useful construction and a limit on what it buys. The source chart avoids solving the original source spectral problem. It does not turn the unresolved original arithmetic sign into an easier independent inequality. Its entries still require the whole P covariance and complete negative images in (3), plus the whole output reaction in (7). The existing physical Schur chart already has actual original source/panel machinery and a protected complement.

## 5. Stable positive-covariance construction, with complete residual

For a trial map ftilde:E->F in (3), set

    R=P_F*P|E-L_F ftilde,
    f_exact-ftilde=L_F^(-1)R.                     (11)

Because L_F>=c I in the specified carrier,

    (f_exact-ftilde)*(f_exact-ftilde)<=c^(-2)R*R.  (12)

The whole mixed residual Gram is required. A trial-space residual or one diagonal norm does not enclose all output columns. Bounded P and N then propagate (12) to errors of u_i and y_i, with their actual operator upper bounds. Gram conditioning and projection errors still have to be paid when turning approximate y_i into a certified Y chart; near rank loss, an unchecked numerical basis is not safe.

This analytic construction is stable relative to the independently known complement c. It introduces a complete POSITIVE covariance solve; CC8's original-Q complement solve is a different operator. They cannot be exchanged just because both are protected.

No actual full positive covariance, d negative image vectors, rank certificate, source Gram or output inverse is computed in this note. The nonconstructive positive-carrier theorem alone supplies existence, not those numerical enclosures.

## 6. Actual interface at a=21/20 and next cursor

CC8's pinned actual source reconstruction retains all six original prime powers, both signed pole slots, all retained projections, 13 translation panels and complete source errors. Its same completed direction has an independently certified lower >1.35e-32 (stored display 1.351579870198155e-32). This is ONE direction, not the whole 112-dimensional S_phys.

Equation (9) means that it is still necessary to obtain the entire original matrix sign or an independent whole reaction inequality. The source representation cannot promote that one directional result to H_out>0. The full physical Schur residual is a concrete existing target; constructing another uncomputed source basis does not satisfy it.

The next decisive input remains an evaluated WHOLE original inverse-reaction matrix or a genuine actual arithmetic bound on its critical correlations. For Global, the analytic critical-coordinate existence question is now settled by (3)-(6); source spectral eigenvectors are not prerequisites. Use the physical chart when its complete arithmetic entries are available. Any proposed source route must explain which independently estimable complete correlation it adds beyond the equivalent physical gate before spending another turn on coordinate changes.

No moving-window derivative, source-prefix limit, new aperture sequence or retired endpoint/regularity investigation is started. Prime-power activation equality keeps zero physical overlap; equations (3)-(9) alter no original arithmetic slot. A positive physical eigenlevel mu must use negative analysis (N,sqrt(mu)physical) and a recomputed output chart; its shifted unit mode is not an original null vector.

## 7. Validation and custody

591 exact rational checks pass across 72 coupled cases, including 24 each of output ranks 0,1,2; 44 are positive and 28 have original negative index. Separate exact positive/contact/crossing cases, a mixed-block deletion countercontrol, and the original positive level mu=11/100 also pass. The controls check P covariance orthogonality, complete output-complement protection, physical/source Schur inertia and whole mixed solve-error bounds. They are algebra controls, not actual zeta evaluations.

Script: [validate_native_protected_source_chart.py](../scripts/validate_native_protected_source_chart.py). It uses NF68's pinned exact matrix helpers. Infinite-dimensional range, adjoint and congruence arguments are analytic, not Lean-formalized or certified by the finite examples.

No actual critical source coordinates, new original gain bound, larger aperture, actual contact, arithmetic relative-loss nondivergence, RH, F4, full transport or Lean closure. NF68 and Coupled CC8 remain intact; coupled and paused refs are not written. Historical claims remain unchanged, with this note added.
