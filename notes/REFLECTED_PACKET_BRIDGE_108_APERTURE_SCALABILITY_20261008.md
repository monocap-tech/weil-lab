# RPB108: aperture-dependent criterion, recoverable complement, and uniform-method obstructions

2026-10-08 UTC. Recovered live head 401f6b3970280a79da974661cbb806b78b4ea1ca. Definitions: [prime-8 and scalability](../docs/TERMINOLOGY_RPB108_PRIME8_SCALABILITY_105.md). This note adds analytic sufficient results and finite exact method controls; it does not claim all-aperture positivity or Lean formalization. The aperture-one certificate 811b0826abf45d688d1e2da7900cda852103ddee and concurrent translated-contact Global/F4 results are preserved.

## 1. General prime geometry is finite and parameterizable

For any fixed finite a, finitely many prime powers have log(n)<2a. Use Lambda(p^r)=log(p), both orientations, and cuts 0,1,log(n)/(2a),1-log(n)/(2a). Away from coincidences, m active prime powers give at most 2m+1 source support panels. Order changes can occur at 2a=log(nm), even without an arithmetic activation. Equality events must be grouped as exact events rather than forced into strict ordering. Inactive endpoint points are measure-zero for L2 translations. Single-point activation does not create an overlap interval.

The prime operator has the universally sufficient finite bound B_abs(a)=2 sum_active Lambda(n)/sqrt(n). A weighted Schur certificate can improve it, but must include all shifted weight-cell events and supported directions. Its size is independent of source panel count: at 21/20 the source has thirteen panels whereas the depth-ten weight construction has 3277 cells and its refinement 4339 cells. The prime-power-8 amplitude is log(2)/sqrt(8), not log(8)/sqrt(8).

A necessary lower bound for ANY prime norm majorant follows by testing the normalized constant physical L2 function:

    B(a) >= 2 sum_active [Lambda(n)/sqrt(n)] [1-log(n)/(2a)].

The constant is an L2 operator test; it need not be in the form operator domain. Thus the arithmetic cost cannot be discarded by repartitioning. No asymptotic prime-number theorem is needed for this finite exact lower bound.

## 2. Complement coercivity can be recovered at every specified finite aperture

Use the existing actual multiplier bounds m0>=-27/5 and m0(xi)>=g(|xi|) for |xi|>=1, g(T)=log(T)-7/(216T^2). These are pinned in ENDPOINT_BRIDGE_AUDIT_20261005 and TWOBAND_COMPLEMENT_092_20261006 at the recovered head; the Fourier normalization remains unchanged.

For h orthogonal in physical L2 to E_k, the existing undamped Legendre/Bessel mass estimate is

    integral_|xi|<T |h_hat|^2 <= rho(a,k,T)||h||_2^2,
    rho = 4aT y^(2k)/[(2k+1)!!^2 (1-y^2/((2k+1)(2k+3)))],
    y=2a(22/7)T,

provided its geometric ratio is below one. This bound uses the all-real Bessel integral-representation bound, not the stronger positive-region damping argument. Physical basis completeness, Cauchy-Schwarz and integration give the displayed mass bound.

Choose T=k/(10a), requiring k>=10a so T>=1. Since y=22k/35, the ratio is below 121/1225. Also (2k+1)!!>=2^k k! and k!>=(k/e)^k, e<3. Therefore

    rho(a,k,k/(10a)) <= r_k=(245/552) k (33/35)^(2k).       (1)

This exact geometric envelope tends to zero and does not depend on a. A negative signed pole allowance valid without the small-aperture exponential guard is

    P(a,k)=4a exp(a) (a/2)^(2k)/(k!)^2.                  (2)

Indeed degree-(k-1) exponential Taylor polynomials pair to zero against h. Taylor remainder gives |M_pm(h)|<=sqrt(2a)exp(a/2)(a/2)^k/k! ||h||; the absolute Hermitian cross term is bounded by (2). The previously used 16a allowance is recovered whenever exp(a)<=4.

For ANY verified B(a)>=||P_prime||, the one-band step comparison gives

    c_*(a,k)=g(k/(10a))
              -[g(k/(10a))+27/5] r_k-B(a)-P(a,k),      (3)
    Q_a(h)>=c_*(a,k)||h||_2^2, h in F_k.

Here T>=1 ensures the coefficient of r_k is positive and the high multiplier bound applies. Replace exp(a), logarithms and pi guards by outward rational bounds to obtain an effective numerical lower bound. For every FIXED finite a and fixed finite B(a), (3) tends to +infinity as k tends to infinity: g grows like log k, r_k decays geometrically, and the pole allowance decays factorially. Thus increasing retained dimension can always repair this COMPLEMENT sufficient criterion. This proves complement recoverability, not positivity on E_k or positivity of its corrected coupling. It does not supply an efficient dimension bound or conditioning bound. Shifted Legendre coefficient L1 norms are P_n(3)=sum_j binom(n,j)binom(n+j,j); they grow with n and amplify constant-enclosure errors, as the existing Machin-80 rejection demonstrates. Full Schur margins and interval-elimination conditioning are separate quantities; the complement dimension criterion supplies no aperture-uniform lower bound on either. The crude B_abs is a permitted effective choice for each fixed a.

The finite exact control script checks the envelope and double-factorial inequalities at 28 parameter pairs, with two norm-lower controls. These 58 checks are controls only; the analytic inequalities and limit proof above, not the finite sample, establish (1)-(3) for the stated parameters.

## 3. The current 112-vector damped comparison has an exact ceiling

For its positive-Bessel outer cutoff,

    T_max < sqrt(k(k+1))/(2pi a).

The three-band lower bound is at most g(T_max)-B(a), hence below log(T_max)-B(a), because every mass penalty and absolute pole charge is nonnegative. At a=21/20, k=112, B=1063939/500000, an independent outward interval gives

    produced complement lower bound < 0.708399.

The actual fresh bound 699/1000 is close to that ceiling. Reusing 93/100 is impossible for THIS comparison and THESE prime bounds, regardless of further damping iterations. This is not an upper bound on actual Q|F_k and does not prove 112 vectors insufficient for a full corrected certificate.

To reach a desired c with this positive-Bessel method it is necessary that

    sqrt(k(k+1)) > 2pi a exp(B(a)+c).

This exposes a potentially expensive retained-dimension dependence on the prime majorant. With fixed k=112, at a=18 every permitted outer cutoff is already below one, so this high-symbol comparison cannot even invoke its published |xi|>=1 bound. Neither this failure nor the ceiling is a negative Weil-form witness.

## 4. Present polynomial kernel architecture cannot cover all apertures

Both current native and source remainder formulas use the geometric ratio

    L/6 = d/3 = 2a/3 < 1, L=4a.

At a>=3/2 their stated positive remainder estimate is invalid: at equality the denominator vanishes, above equality its sign is wrong. Increasing orders does not repair this proof. Even replacing the coarse six by the exact nearest singularity cannot make the SINGLE origin expansion all-aperture: z/(1-exp(-z)) has nonremovable poles at z=+/-2pi i, so its Maclaurin series has radius 2pi. The origin kernel argument reaches 4a. For a>pi/2 that expansion cannot converge on the whole required real interval. This is a complex-plane expansion obstruction, not a real-axis singularity of Q.

A scalable source construction therefore needs kernel-distance subdivision, expansions at multiple real centers, or another certified representation. Merely adding prime support panels does not subdivide the kernel-distance argument used in the archimedean integrals. Such a replacement is a specified remaining task; this note does not supply its native/source reconstruction and full error proof.

At 21/20 there is no radius obstruction: 2a/3=7/10. Fresh orders 400/400 (native) and 100/130 (source) repair the inherited budgets. The source polynomial ceiling increases from 9/4 to 23/10, above its exact ceiling 457/200. Taylor's integral remainder for exp(-x), x>=0, bounds the exponential remainder by x^(N+1)/(N+1)! even though d/2=21/20>1; no invalid globally decreasing factorial-series premise is used.

## 5. Parameterized complete corrected Schur criterion

At a given a, assume: lawful actual canonical form and physical decomposition E_k+F_k; c>0 verified on F_k; complete native Q_E; complete actual source map on E_k with residual surrogate Gram R and full allowance eta; M>=||B_tilde||; and

    Q_E-c^-1[R+eta(2M+eta)I] >= tau I, tau>0.          (4)

The correction follows from ||B-B_tilde||<=eta and norm expansion, giving B*B<=R+eta(2M+eta)I. Complete mixed terms and physical projections are mandatory. The positive complement operator C exists by the closed form representation; its inverse has norm <=1/c. Completing the square gives Q>=tau||e||^2+c||z||^2 with z=f+C^-1Be. If L>=||C^-1B||, then

    mu=tau c/[tau+c(1+L^2)] >0,
    Q>=mu||h||_2^2.                                 (5)

The two-variable comparison matrix has determinant mu^2 and nonnegative diagonals. A valid lift bound is L^2>=c^-2[tr(R)+delta], delta=eta(2M+eta), with outward trace from the COMPLETE surrogate Gram. If the actual Garding inequality is Q>=Elog/10-D(a)||h||^2, then

    Q>=mu/[10(mu+D(a))] Elog.                        (6)

At the prime-8 target D(a)=26, using strict prime loss<7, pole loss<13 and archimedean loss six. This criterion is sufficient and aperture-dependent. It is conditional on (4); it does not prove that some chosen k and source budget satisfy (4) at every a. Complement recoverability alone cannot close this condition.

## 6. Continuation and monotonicity audit

Physical support inclusion gives lambda_min(b)<=lambda_min(a) for b>a. Certified positivity propagates downward. It supplies no upward positivity implication and no monotonic lower bound on corrected finite Schur matrices with changing physical bases, panels and arithmetic terms.

The existing ENDPOINT_BRIDGE_AUDIT already records actual norm continuity of the logarithmic-carrier operator A(a), including arithmetic activations. Preserve and reuse it; do not reclaim it as a new theorem. Under mass-unitary dilation U_a, Elog(U_a f)>=Elog(f)/max(1,a). Thus a strict logarithmic physical-window bound kappa gives A(a)>=alpha I, alpha=kappa/max(1,a). IF an effective modulus proves ||A(b)-A(a)||<alpha/2, then A(b)>=alpha/2 I. Existence of some neighborhood follows from the pinned norm continuity, but a quantified enlargement requires that modulus. No uniform radius or summable sequence of certified continuation steps has been proved.

The L2 prime translation summands themselves are NOT norm-continuous at a support threshold: a newly supported partial translation on every positive-width overlap has L2 norm one, although its finite-column source action tends to zero. This prevents substituting naive physical operator-norm continuity for the pinned logarithmic-carrier continuity. It does not contradict that existing result.

A genuine all-aperture theorem still needs (4) for all a, or a continuation/first-contact exclusion theorem strong enough to reach arbitrary apertures. The current numerical architecture has rigorous complement recovery and conditional complete-certificate and local-continuation criteria, but is obstructed as an unchanged all-aperture polynomial implementation. Global endpoint exclusion, F4, full transport and Lean closure remain open.

## 7. Recovered concurrent NF57 approximation theorem

Before publication, the concurrent Global/F4 head advanced to 1b5db1dc92717e7e0dcd85341ac1494de97c0b70. Its new PRIME_SMEARING_20261008 theorem is relevant and is preserved: for every fixed finite a, averaging EVERY active arithmetic atom over a physical shift width delta<=exp(-4), while retaining the exact archimedean and pole forms, gives

    |Q_a-Q_(a,delta)| <= [4 S_a/log(1/delta)] Elog,
    S_a=2 sum_(log n<=2a) Lambda(n)/sqrt(n).

It proves matching logarithmic order for the error norm in the actual one-prime window; a uniform power-of-delta rate is false for that smearing. The equality atom is included for approximation, even though its original physical overlap is measure-zero. Its averaged contribution is covered by the error estimate.

The exact six-power target sum also satisfies S_(21/20)<13/2. Thus delta=2^(-j), j>=6, gives the inherited conservative target error <39/j in logarithmic energy. An independently PROVED smeared coercivity kappa_delta>39/j would transfer positivity, with the subtraction retained. No such smeared sign or original source-gain estimate is supplied by the approximation theorem.

This adds a genuine reusable parameterized arithmetic approximation; it does not solve (4), change the native/source origin-expansion radius, or yield all-aperture positivity. Its rate is expensive relative to the published tiny margins: to charge at most half of the already certified aperture-one logarithmic floor 2e-34 using the target budget 39/j, the sufficient integer j must exceed 39*10^34. This is a consequence of these conservative ERROR AND GAP bounds, not a necessary lower bound for every possible certificate or evidence that the true gap is that small. The existence of an effective approximation must not be confused with an efficient all-aperture positivity algorithm.

NF57 controls prime smearing at a FIXED aperture. It is not itself a complete effective modulus for changing aperture and the entire canonical operator. The strict local continuation result remains conditional on an adequate full-operator modulus, and global exclusion/F4 remain open.

## 8. Publication recovery: NF58 and NF59

The fresh publication parent 47e0ada898cdc2b9d57a209db683019a3a43f40e also preserves NF58 (fba75ed4eda84f0c71286f314f85b0d29db0202a) and NF59. [NF58](REFLECTED_PACKET_BRIDGE_108_SMEARED_SIGN_TRANSFER_20261008.md) obtains faster-than-every-fixed-inverse-log-power prime-smearing error on bounded-level ORIGINAL eigenvectors and a conditional whole-form sign transfer. It supplies no independent smeared lower bound. Thus the worst-domain error cost in section 7 is not the only possible sign-transfer budget.

[NF59](REFLECTED_PACKET_BRIDGE_108_SMEARING_MAIN_TERM_20261008.md) proves analytically from the prime number theorem that EVERY fixed positive prime-only averaging width produces negative smeared packets at sufficiently large apertures. Its exponential moment alpha_delta=sinh(delta/2)/(delta/2)>1 mismatches the unchanged pole main term. This rigorously excludes that fixed-width all-aperture approximation route, not positivity of the ORIGINAL form. Adaptive widths remain open; scaling both pole slots cancels the leading mismatch but requires its full additional error and supplies no sign. No finite negative original vector or Lean conclusion is inferred.

These independently recovered results are preserved unchanged. They sharpen the scalability decision without changing the direct prime-8 certificate data or its failed sufficient inequality.
