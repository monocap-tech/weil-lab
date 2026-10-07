# RPB108: the actual Pick model has no infinity atom; cyclic completion retains a source gauge

2026-10-07. Recovered global/live head 43e88c0cc3c0042bbecafaafad277fe230e64aa7. Definitions: [Pick cyclic completion](../docs/TERMINOLOGY_RPB108_PICK_CYCLIC_COMPLETION.md). Analytic continuation of NF45, conditional on a hypothetical nonzero actual nonnegative contact kernel.

## Result and exact scope

The actual normalized jump tests satisfy

    ||k_(iy)||_D^2=O(log(y)/y), y->infty.

Consequently the Pick representation has zero linear coefficient at infinity. Its representing measure consists exactly of the real generator-zero atoms already attached in NF45. The actual real-zero division vectors are an orthogonal basis of the JUMP-GENERATED energy carrier:

    H_jump=H_div,
    [k_w]=sum_(Phi(t)=0) [u_t]/[Phi'(t)(w-t)].

The series converges in the Q quotient norm. Its native-energy Parseval identity is exact. This is a spectral completeness theorem on a specified actual carrier; generation of the ENTIRE native quotient is not established here.

Crucially, a Q expansion is not unchanged complete-zeta-source reconstruction. A lawful physical lift uses Pi=I-P_K and retains Gamma(P_K k_w). That finite kernel correction remains observable and can carry the unresolved terminal trace. The actual shifted positive eigenspace has the same cyclic theorem for Q_mu; its source pairings retain the mu mass residual.

## 1. Endpoint asymptotics give the large-imaginary generator value

Choose the top physical generator phase so its profile is Phi. Let r=dim K, and let c_L!=0 be the averaged LEFT endpoint trace of D^(r-1)h_*. The actual balanced traces and primitive formulas from the derivative-chain theorem give

    Phi(iy)=c_L exp(ay)/[y^r sqrt(log y)] (1+o(1)).       (1)

For r>=2, the left primitive asymptotic is

    h_*(-a+v)=c_L v^(r-1)/[(r-1)! sqrt(log(1/v))]
                      +o(v^(r-1)/sqrt(log(1/v))).

Substitute v=u/y in the Laplace integral. On each bounded u interval the normalized integrand converges to c_L exp(-u)u^(r-1)/(r-1)!. Its integral is c_L. The endpoint asymptotic supplies a polynomial/logarithmic bound for 0<v<delta. On u<=sqrt(y), the ratio sqrt(log y)/sqrt(log(y/u)) is bounded, and the exponential tail controls increasing u. On u>sqrt(y), Cauchy-Schwarz against the supported L2 generator gives an exponentially small remainder, even after multiplying by y^r sqrt(log y). The fixed interior part has the stronger exp(-delta y) factor. These estimates justify the limit without a sign assumption on the whole generator.

For r=1 the terminal trace is averaged rather than pointwise. Its proved strong scaled L2 trace gives the required convergence against exp(-u) on every bounded u interval. The accepted bound |h_*(-a+v)|<=C/sqrt(log(1/v)) near the boundary gives the same tail domination. Thus (1) also holds in the rough one-vector case, without upgrading its trace to a pointwise limit.

In particular |Phi(iy)| grows exponentially and is bounded below by a positive multiple of exp(ay)y^(-r)(log y)^(-1/2) for all sufficiently large y. The endpoint coefficient is nonzero because the chain's terminal trace is nonzero and left/right traces are balanced. No aperture certificate is used in this argument.

## 2. Exact global resolvent formula for the normalized jump

Set v_y(x)=exp(yx)1_(x<0) on the WHOLE line, and let R_y be convolution by v_y. With the angular Fourier convention,

    F_vy(eta)=1/(y+i eta),
    F_(R_y h_*)(eta)=Phi(eta)/(y+i eta).

The normalized jump test has the exact global identity

    k_(iy)=v_y-R_y h_*/Phi(iy).                      (2)

For x<-a, R_y h_*(x)=exp(yx)Phi(iy), so the two terms cancel exactly. For x>a both terms vanish. Inside the window, (2) is precisely the compact Volterra/jump formula from NF45. Thus the estimates below use full-line Fourier norms for auxiliary functions but do not replace k_(iy) by an enlarged-support test.

Use the full-line logarithmic norm with weight W(eta)=log(e+|eta|), equivalent to the canonical norm when restricted to D_a. The auxiliary v_y and R_y h_* are measured only in this full-line norm; they are not declared supported tests. Scaling eta=yu gives, for y>=2,

    ||v_y||_log^2 <= C log(e+y)/y,
    ||R_y h_*||_log <= ||h_*||_D/y.

The first inequality follows from integrability of (1+u^2)^(-1) and log(e+|u|)/(1+u^2); the second is the pointwise multiplier bound |y+i eta|^(-1)<=1/y. Combining (1)-(2) yields

    ||k_(iy)||_D^2
      <=2C log(e+y)/y + 2||h_*||_D^2/[y^2|Phi(iy)|^2]
      =O(log y/y).                                  (3)

Full native form continuity on the fixed supported logarithmic domain implies Q(k_(iy),k_(iy)) obeys the same bound. Every prime and the pole are retained in that continuity estimate. Individual auxiliary terms in (2) need not be evaluated in Q outside its supported carrier.

## 3. Herglotz representation; all transfer hypotheses checked

External framework: Mitja Nedic, *Characterizations of Herglotz-Nevanlinna Functions Using Positive Semi-Definite Functions and the Nevanlinna Kernel in Several Variables*, Complex Analysis and Operator Theory 15, 109 (2021), DOI [10.1007/s11785-021-01155-x](https://link.springer.com/article/10.1007/s11785-021-01155-x), Theorem 2.1 at n=1 and the following infinity-coefficient formula. Only the classical one-variable representation is imported.

In a convention absorbing the factor pi into the measure, write

    M(w)=A+b w+integral_R [1/(t-w)-t/(1+t^2)]dnu(t),
    A real, b>=0, integral_R dnu(t)/(1+t^2)<infty.

The hypotheses are supplied by NF45: M is holomorphic in the upper half-plane and Im M>=0. Its meromorphic real-symmetric continuation has only simple real generator-zero poles. The infinity formula and the exact Gram diagonal give

    b=lim_(y->infty) Im M(iy)/y
     =lim_(y->infty) Q(k_(iy),k_(iy))=0.             (4)

The representing measure has no mass on an interval of real analytic continuation: integrating the imaginary part over compact subintervals and using the Poisson kernel recovers that measure, while real analyticity makes the limit zero there. Generator zeros are locally finite, so this removes all continuous and singular-continuous parts. The local residue calculation from NF45 fixes the remaining weights:

    nu=sum_t c_t delta_t,
    c_t=d_t/|Phi'(t)|^2>0,
    sum_t c_t/(1+t^2)<infty.                         (5)

This uses the elementary one-variable inversion consequence of the displayed representation; no zeta measure is substituted for nu. Differencing the representation now gives the locally convergent exact Gram expansion

    Q(k_w,k_v)=sum_t c_t/[(w-t)(bar v-t)].           (6)

There is no extra positive rank-one constant kernel from a linear term. The omitted possibility b>0 would have contributed exactly such a direction.

## 4. Cyclic completeness in the actual energy quotient

The nonnegative Q quotient is completed to H_Q. For a fixed generator zero t, NF45's form-valued limit

    (w-t)k_w -> u_t/Phi'(t)

puts [u_t] in H_jump. Its Q norm is d_t>0 and different t vectors are Q-orthogonal. Taking the conjugate parameter to t in (6), equivalently taking the residue in NF45's Gram identity, gives

    Q(k_w,u_t)=d_t/[Phi'(t)(w-t)].                 (7)

Conjugation in the second argument is retained. Equations (6)-(7) give

    Q(k_w,k_w)=sum_t |Q(k_w,u_t)|^2/d_t.

Subtracting the finite orthogonal projection and passing through increasing finite sets proves its remainder norm tends to zero. Therefore

    [k_w]=sum_t [u_t]/[Phi'(t)(w-t)] in H_Q,
    H_jump=H_div.                                   (8)

No unproved total-domain cyclicity is hidden in this argument. H_jump=H_Q would need an additional generation theorem. An invisible positive direct summand can be added to an abstract realization without changing M or (6); the finite checker records this precise response-level control. It is not an actual zeta counterexample.

## 5. The complete source graph requires a kernel correction

At nonnegative contact, the logarithmic Riesz operator of Q is I+compact and K is its finite kernel. On the physical L2-orthogonal complement to K, Q controls the full logarithmic norm. One direct proof by contradiction: take f_n perpendicular to K with ||f_n||_D=1 and Q(f_n)->0. Compact physical inclusion and weak D convergence, together with positivity, show every limit is null and perpendicular to K, hence zero. The physical norms then tend to zero, contradicting the established Garding bound Q(f_n)>=c||f_n||_D^2-C||f_n||_2^2. Thus the gauge Pi=I-P_K is a bounded realization of H_Q into D_a.

Apply this gauge to (8). For every fixed nonreal w,

    Pi k_w=sum_t Pi u_t/[Phi'(t)(w-t)] in D_a,
    Gamma(Pi k_w)=sum_t Gamma(Pi u_t)/[Phi'(t)(w-t)]
                                      in complete source norm.    (9)

The second convergence uses bounded complete actual analysis on D_a. Full original source custody is

    Gamma(k_w)=Gamma(P_K k_w)
                 +sum_t Gamma(Pi u_t)/[Phi'(t)(w-t)].             (10)

Complete analysis observes every nonzero vector of K, so it does not descend unchanged to D_a/K. Dropping Gamma(P_K k_w) is not justified by Q(P_K k_w)=0. The real-zero division tests are globally H^r, but their physical projections P_K u_t need not be zero. Subtracting those projections can introduce the rough terminal kernel direction. A smooth ungauged division vector therefore does not authorize declaring the source lift's endpoint trace zero.

The finite signed-observation control has Q=diag(0,1,1,1) and injective analysis Gamma(a,b,c,d)=(a,b,c,d;a), with positive entries before the semicolon and negative entry after it. It realizes the same quotient seminorm while visibly observing its null direction. An extra positive coordinate can be invisible to the chosen jump response. This audits (10) and the whole-carrier generation gap, not actual arithmetic contact.

## 6. Controls and consequence for the research path

| Control | Outcome |
|---|---|
| Actual rough lowest positive eigenspace | Use Q_mu throughout: the endpoint Laplace asymptotic, b=0, atom weights and jump-carrier basis all hold. Actual unshifted source Gram retains mu physical mass. No exclusion follows from this cyclic theorem alone. |
| Compact-good-row logarithmic control | Lacks the exact generator/jump equation; no model attachment is inferred. It still blocks a generic sign argument from positive Gram or compact rows. |
| Fixed finite actual restoration | Changes sharp/log by o(1). The full equation used here cannot be kept after altering source rows without rechecking it. |
| Two-row comparison contact | Does not automatically inherit derivative skew or actual jump custody. No artificial rows are used in (1)-(10). |
| Positive invisible direct summand | Preserves the entire chosen Pick function but enlarges the ambient positive carrier. Shows why response completeness must be scoped to H_jump. |
| Injective signed analysis on a semidefinite carrier | Observes its null direction despite zero Q norm. Demonstrates the exact need to retain the physical/source gauge correction. |

The internal model graph shortens: the infinity direction is excluded, the atomic measure is fully attached, and jump-carrier completeness is proved. The final arithmetic graph does not yet shorten. Whole-native generation remains open, and even proving it would not independently force the signed sharp-head coefficient to vanish; the shifted control shares that structure. The next useful question is an actual source-compatible lifting or range relation that constrains the kernel correction in (10), with the mu residual retained.

No bounded/sublogarithmic sharp subsequence is constructed. The implication from actual unshifted source-range nullity to such a subsequence remains unproved. Endpoint exclusion, F4, full transport and Lean closure remain open. Concurrent aperture work is preserved.

## Verification

The companion rational checker verifies finite atom Gram/Parseval identities, residue coefficients, the resolvent cancellation multiplier, and the invisible-summand/source-gauge controls. It does not certify the analytic endpoint/Laplace limit, Herglotz theorem or infinite completion argument. The dependency manifest pins all actual inputs and names the exact external theorem. No Lean proof or axiom is added.
