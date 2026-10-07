# RPB108: exact strip matching and a subsequence endpoint criterion

Date: 2026-10-07 UTC. Recovered head e75bce077634fb903a1c0e5fa6cdaeb65ea7f430.
Definitions: [strip tests and normalized joint budgets](../docs/TERMINOLOGY_RPB108_ENDPOINT_STRIP_MATCHING.md).
Category: endpoint exclusion / critical joint cancellation. Analytic, not Lean-certified.

## Result

The EXACT actual full-native null equation, tested against a lawful boundary-strip indicator, yields at either endpoint

    J_R(epsilon)=(2L_epsilon/epsilon)
                         integral_0^epsilon h(a-v)dv+O_h(1),       (1)
    q_h(a+epsilon)/sqrt(L_epsilon)
      +(sqrt(L_epsilon)/epsilon) integral_0^epsilon h(a-v)dv
          =O_h(1/sqrt(L_epsilon)).                                (2)

The full exterior reciprocal budget therefore satisfies

    rho_R(epsilon)<=eta_R(epsilon)+O_h(1/sqrt(L_epsilon)).         (3)

The reflected equations retain the left endpoint. In particular, the NF25 derivative criterion strengthens to

    liminf_(epsilon->0) B_h(epsilon)=0
        iff B_h(epsilon)->0 iff h in H1, h'=g in SAME K_a.         (4)

Thus a SINGLE COMMON vanishing subsequence for the whole finite contact kernel suffices to exclude contact. This pass proves the joint matching and the subsequence implication. It does not prove that the actual kernel has that subsequence.

Unlike a generic regularity inference, (1)-(3) use the full mixed equation. They still apply to fixed physical eigenvalues after a scalar shift: the mass contribution is bounded in (1). Hence matching alone cannot distinguish zero from a rough positive eigenmode or prove endpoint exclusion.

## 1. The strip is a legal actual test

The zero-extended indicator chi of (a-epsilon,a) has Fourier transform bounded by min(epsilon,C/|xi|). Its logarithmic norm is finite. Its actual multiplier action is L2: the only near-boundary singularities below are logarithms. Thus it belongs to the canonical domain, and Q_a(h,chi)=0 is a lawful SAME-window mixed test for actual h in K.

NF25 already supplies, before any critical premise,

    |h(a-v)|<=C_h/sqrt(log(1/v)),

near the edge, and global boundedness and continuous zero endpoint values. All actual frozen prime translates of h and its physical pole are bounded. No positivity-preserving full-native semigroup or assumed boundary trace is used.

Put F(d)=integral_d^infinity k(s)ds, k(s)=exp(-s/2)/(1-exp(-2s)). Since k(s)=1/(2s)+k_reg(s), with bounded k_reg near zero,

    F(d)=-(1/2)log d+c_k+O(d).

In coordinates v=a-x, the exact native multiplier on chi is

    m0(D)chi(v)=m00+F(v)+F(epsilon-v), 0<v<epsilon,
    m0(D)chi(v)=-integral_(v-epsilon)^v k(s)ds,
                                                  epsilon<v<2a.

Only its pairing with the original supported h is used. For 0<v<epsilon, the first formula equals

    L_epsilon -(1/2)log[(v/epsilon)(1-v/epsilon)]+c+O(epsilon).

Pairing the logarithmic edge factor with h costs O_h(epsilon/sqrt(L_epsilon)), because its rescaled absolute integral is finite. The fixed c term has the same bound. All prime and pole pairings are O_h(epsilon), with threshold-equality translations retained. The regular-kernel part of the exterior pairing is also O_h(epsilon), since k(s)-1/(2s) is bounded on (0,2a]. Hence exact mixed nullity gives

    L_epsilon integral_0^epsilon f_R(v)dv
       -(1/2) integral_epsilon^(2a)
                     f_R(v) log[v/(v-epsilon)]dv=O_h(epsilon).   (5)

This is not a selected/background equation and not merely diagonal neutrality.

## 2. The logarithmic exterior weight reduces to the signed inverse moment

For v>=2epsilon,

    0<=log[v/(v-epsilon)]-epsilon/v<=epsilon^2/v^2.

On epsilon<v<2epsilon, the rescaled difference has a finite absolute integral. The boundary upper bound therefore yields

    integral_epsilon^(2a) |f_R(v)|
           |log[v/(v-epsilon)]-epsilon/v|dv
          =O_h(epsilon/sqrt(L_epsilon)).

To check the far estimate without assuming a uniform boundary bound at every v, split at sqrt(epsilon) and a fixed small delta. Up to sqrt(epsilon), log(1/v)>=L_epsilon/2. Above it use bounded h, giving O_h(epsilon^(3/2)), and the fixed outer part is O_h(epsilon^2). Combining with (5) proves (1). The SIGNED J_R(epsilon) exists at each finite cutoff; no improper limit or injectivity is inferred.

Define C_R(t)=integral_0^(2a) f_R(v)/(t+v)dv. At t=epsilon, the same boundary bound and split show

    C_R(epsilon)-J_R(epsilon)=O_h(1/sqrt(L_epsilon)).

The inner v<epsilon part has that bound directly. For v>=epsilon the kernel difference is epsilon/[v(v+epsilon)] and its absolute integral has the same bound. The exact exterior identity q_h(a+t)=-(1/2)C_R(t)+A_h(t), with bounded actual drive A_h, proves (2). This is genuine joint matching at the rough logarithmic scale; it does not assert either term separately tends to zero.

## 3. The entire exterior strip is controlled at the SAME scale

The elementary kernel identity gives

    integral_0^epsilon |C_R(t)-C_R(epsilon)|dt
      <=integral_0^(2a) |f_R(v)|
             [log(1+epsilon/v)-epsilon/(v+epsilon)]dv
       =O_h(epsilon/sqrt(L_epsilon)).

For v<epsilon the bracket has a finite rescaled integral and |f_R|<=C_h/sqrt(L_epsilon). For v>=epsilon the bracket is at most epsilon^2/(2v^2), and the previous split applies. Bounded A_h contributes only O_h(epsilon). Thus

    integral_0^epsilon |q_h(a+t)|dt
       <=epsilon |q_h(a+epsilon)|+O_h(epsilon).

Dividing by epsilon sqrt(L_epsilon), and applying (2) and the absolute value of the strip mean, proves (3). Cauchy-Schwarz gives eta_R<=sqrt(B_(h,R)); the same holds on the left.

The crucial gain over NF25 is that this estimate uses B at one scale. It does not require a vanishing upper envelope over all smaller scales. The exact null equation supplies the signed Carleman cancellation that generic boundary upper regularity lacked.

## 4. Subsequence derivative promotion and the contact consequence

Repeat the established reciprocal argument with smooth f physically orthogonal to the whole K BEFORE Fredholm inversion. Its inverse u has the logarithmic interior upper bound and exterior O(sqrt(log)) action. For the mollified derivative, the two retained boundary terms are bounded by

    C_f*(eta_R+eta_L+rho_R+rho_L)
       <=C_(f,h)*(sqrt(B_h(epsilon))+1/sqrt(L_epsilon)).

The interior pairing tends to -<h,f'>. If B_h tends to zero along a sequence, both exterior terms vanish along that SAME sequence, proving <h,f'>=0 for every such f. Finite-codimension identification and the continuous primitive give the global h'=g in K and H1, exactly as audited in NF25. Conversely H1 gives B_h->0. This proves (4), including the passage from liminf to a full limit ON THE ACTUAL KERNEL.

For a physical orthonormal basis of finite K, B_K is basis-independent and nonnegative. If liminf B_K=0, select a common vanishing sequence; each basis vector then satisfies (4). Differentiation is an endomorphism of K and compact-support Fourier-polynomial independence forces K=0.

Consequently any nonzero hypothetical actual K satisfies

    0<liminf_(epsilon->0) B_K(epsilon)
       <=limsup_(epsilon->0) B_K(epsilon)<infinity.               (6)

The lower bound is qualitative, depending on the fixed kernel/window. It is not an explicit arithmetic constant or assertion that K exists. For an individual non-H1 null vector, (4) likewise forces a positive liminf; a nonzero H1 vector in a higher-dimensional kernel is not ruled out individually.

## 5. Controls and the remaining actual theorem

For a fixed eigenspace q_h=mu h, the strip mass term contributes at most |mu|epsilon||h||_infinity to (5), leaving (1)-(3) unchanged in scope. Applying the shifted reciprocal argument proves (4) there too. The already constructed rough ACTUAL positive eigenmode therefore has positive liminf B_h, strengthening the previous limsup statement. An actual smooth-forcing rough inverse is another control for the failure of generic boundary upper bounds to give vanishing mass, but is not a null vector.

The leading profile f(v)=c/sqrt(log(1/v)) is consistent with (1): J(epsilon) has leading 2c sqrt(L_epsilon), while (2L_epsilon/epsilon)integral_0^epsilon f has the same leading term. Thus joint matching does not cancel the rough physical profile itself. No single signed inverse moment is declared injective.

Smallest remaining endpoint theorem for this route: at every hypothetical actual NONNEGATIVE first contact, establish liminf B_K(epsilon)=0. Equivalently, provide a common sequence of strips whose total normalized kernel mass vanishes. This condition fails in the mass-shifted rough positive-eigenvalue contact control; the actual unshifted arithmetic/source constraints must supply the distinction. First-contact nonnegativity alone supplies no such estimate here.

The attempted direct inference full-native strip matching -> vanishing normalized mass fails at the rough leading profile and shifted actual control. What IS closed is the joint estimate and the subsequence derivative implication. No new transverse bound, aperture certificate, historical attachment or enlarged same-vector transport is required for those proofs. The accepted beta<=3/8 bound remains in force but does not enter the physical strip singularity.

## Custody and validation

Pinned sources at recovered e75bce077634fb903a1c0e5fa6cdaeb65ea7f430:
- ENDPOINT_MASS_PROMOTION_20261007: 6bae812597a46f52e110ecea4a150cfa7c369d80.
- CRITICAL_RECIPROCAL_PROMOTION_20261007: 9983be22ab58e926b5e15127f8feaf53d43329e0.
- CRITICAL_MASS_SHIFT_CONTACT_20261007: 228069a79d0a987ef3651a926b0aaf797dd7541b.
- CRITICAL_EIGENMODE_TARGET_20261007: 3354b89638b643d5b21c4c428f069f738ccf59f5.
- ACTUAL_ROUGH_FORCED_INVERSE_20261007: 525ced5f03a8fc5dee543ada83d74a5fed8d74b0.

No new external theorem imported. NF25 retains its versioned logarithmic-boundary theorem and domain/semigroup custody. Analytic audit: canonical indicator domain and multiplier domain; correct 1/(2s) normalization; both indicator action regions; regular-kernel, threshold-prime and positive pole retention; signed inverse truncation; absolute near/far kernel bounds; whole-strip residual control; common-sequence reciprocal estimate; endpoint removal and whole-kernel derivative chain. The companion rational checks verify logarithmic series remainders and normalized control brackets, not actual zeros, kernel existence or the infinite-dimensional theorem. No Lean build, axiom audit or F4 claim. Historical wording/certificates and concurrent aperture work preserved; canonical cursor updated additively. Endpoint exclusion, retained attachment and full transport remain open.
