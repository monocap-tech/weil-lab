# RPB108 PS2: localized continuation exposes the complement-sensitive gate

Base shadow head: `ea6431655705351b37e14a51945e5d630b7d94dc`.
Recovered shared head: `1b5db1dc92717e7e0dcd85341ac1494de97c0b70` (NF57).
Pre-publication shared recovery: `fba75ed4eda84f0c71286f314f85b0d29db0202a` (NF58), audited below and left on the existing front.
Definitions: [localized Schur interface](../docs/TERMINOLOGY_RPB108_PRECONTACT_SCHUR_INTERFACE.md).

## Result and stopping decision

The aperture-one source/native archives were restored and their decoded SHA256 hashes checked against the original corrected certificate. Its finite corrected Schur margin 1/(320*10^27)=3.125e-30 passes an independent 100-digit outward rational recheck, including odd-parity enclosure errors. Proposed 1e-28 and 1e-29 margins both have interval Schur pivots with NEGATIVE UPPER endpoints, not merely failed lower endpoints. The conservative comparison matrix's possible margin is consequently below 1e-29+nu, less than approximately 3.21 times the recorded margin. Large individual pivots do not justify a large spectral margin.

The localized continuation theorem below keeps the complete existing Gram. It isolates finite restriction, coupling and complement losses. The first two can exploit finite polynomial regularity, but scalar complement transport through the PS1 modulus reintroduces essentially the same tiny budget: about 2.21e-34. No useful enlarged aperture or new complete-range arithmetic gain bound results. This stops the proposed localization shortcut, rather than initiating a sequence of further conditional contact classifications.

No matched Gram was newly constructed. No actual physical eigenvalue, negative Weil vector or global positivity theorem was computed. The finite comparison matrix is a conservative lower certificate and must not be identified with the actual low physical spectrum.

## 1. Exact physical block continuation theorem

On the fixed mass carrier let V be the certified finite polynomial space and W its physical orthogonal complement. Every physical decomposition f=x+y remains on the same canonical form domain. The archived native source columns are physical L2, so their mixed residual B_a maps finite V boundedly into W. Write

    q_a(x+y)=<F_a x,x>+2 Re<B_a x,y>+q_(C_a)(y).

At the certified anchor suppose

    C_a>=c_a I,  F_a-c_a^(-1)B_a*B_a>=tau I_V,
    ||B_a||<=M.

At b suppose independently proved bounds are

    C_b>=c_b I, c_b>0,
    ||F_b-F_a||<=alpha,
    ||B_b-B_a||<=epsilon.

Completing the physical square in C_b gives the following sufficient finite margin:

    S_b>= [tau-alpha-(2M epsilon+epsilon^2)/c_b
                    -(1/c_b-1/c_a)_+ M^2] I_V.       (1)

Indeed B_b*B_b-B_a*B_a has norm <=2M epsilon+epsilon^2. Subtract c_b^(-1)B_b*B_b from F_b, compare with the anchor, and retain the possible increase of the inverse scalar complement. The true Schur complement F_b-B_b*C_b^(-1)B_b is at least this comparison, because C_b^(-1)<=c_b^(-1)I. A positive right-hand side and positive c_b give whole physical coercivity by the same two-variable mass conversion used in the original certificate. The native Garding estimate then gives canonical coercivity and hence strict complete-range source gain.

This is an analytic continuation theorem with quantitative hypotheses, not proof that its hypotheses hold at a useful b. It retains physical mass in the square and conversion. There is no replacement of C_b by the bounded canonical Riesz operator.

## 2. Where finite regularity helps

After mass dilation, the physical polynomial vectors in V stay fixed. The archimedean multiplier change has physical operator norm <=5|log(b/a)| by PS1's actual Euler-series derivative estimate; the pole change obeys its explicit physical bound.

For a zero-extended polynomial p on [-1,1], a displacement d satisfies the elementary physical estimate

    ||tau_d p-p||_2^2
       <=2||p||_infinity^2 |d|+||p'||_(L2(-1,1))^2 d^2,

when |d|<=2. Split off the two boundary strips and use Cauchy-Schwarz on the common interior. Translation to any original shift does not change this bound. Thus the complete prime action on each finite column has an explicit square-root displacement bound, including endpoint threshold activation; no H1 claim is made for the zero extension. Sum all actual prime powers with their existing coefficients and use the sum of squared column budgets to bound epsilon. Polynomial correlations also give finite restriction estimates directly. This avoids applying the slow global canonical modulus to the finite columns.

These estimates are potentially reproducible from the archived physical polynomial basis. They do not control C_b on the entire complement. V is not known to be the spectral near-null space, and the retained 112 vectors must not be relabeled as that projection.

## 3. Why the complement still consumes the margin

The exact original certificate gives c_1=93/100, tau=3.125e-30, and actual residual norm M<7 (the complete surrogate norm plus its actual source error). Its original lift bound 8 is retained. The source surrogate norm here bounds B_1; it is NOT the complete positive analysis norm ||P_1||.

Set c_b=c_1-zeta. Even with alpha=epsilon=0, (1) allocates the complement loss

    M^2 zeta/[c_1(c_1-zeta)].                         (2)

With the safe M=7 this equals tau at

    zeta_*=tau c_1^2/(49+tau c_1)
             approximately 5.51594387755e-32.         (3)

This is a scale for the sufficient majorant, not a necessary restriction on the actual aperture. It nevertheless shows that using the current certificate with independent absolute losses needs extraordinarily precise complement preservation.

To see what PS1 provides, the certificate's physical Garding estimate on H is

    ||f||_H^2<=10[q_1(f)+24||f||_2^2].

On W, q_1>=c_1 physical mass. If omega=||A(b)-A(1)|| is bounded and 10omega<1, then

    q_b>= (1-10omega)q_1-240omega physical mass,
    C_b>= [c_1-249.3omega] I.                         (4)

Substitution of (4) into (3) leaves omega below approximately 2.21257275473e-34 EVEN BEFORE finite restriction and coupling errors. That is the same scale as PS1's canonical margin, not a practical escape from its logarithmic continuity budget. NF57's new smearing theorem has a sharp logarithmic rate for that particular approximation; it does not prove optimality of every aperture modulus, but supplies no fast generic replacement here.

## 4. Exact countercontrol: finite blocks alone do not continue positivity

Take one physical finite direction and one physical complement direction, mass matrix I, and

    F=M^2/c+tau, B=M, C(zeta)=c-zeta,
    q_zeta=[[F,M],[M,c-zeta]].

F and B are constant and perfectly observable throughout. The complement stays strictly positive at zeta_* from (3), but the exact Schur complement is

    tau-M^2 zeta/[c(c-zeta)].

It vanishes at zeta_* and becomes negative above it. Thus even exact finite-block invariance, exact coupling invariance and a substantial positive complement do not preserve the tiny full margin. The loss term cannot be omitted. This is a finite rational countercontrol to the block shortcut, not an actual prime/source model.

For any physical positive-level comparison, shifting by mu contributes -mu physical mass to both diagonal blocks, and the original source identity remains Q=||P||^2-||N||^2. The known actual positive-eigenmode control therefore continues to reject dropping that residual. No pairwise source contraction or finite negative prefix replaces the full actual range.

## 5. Margin audit and its precise scope

Both complete archived Gram and compact native matrix were restored from the shadow branch. The original corrected certificate pins their decoded hashes to `92d8c188...` and `c0898e26...`. The original actual-source correction delta is retained exactly. The matrix tested is

    G=Q-(100/93)[R_surrogate+delta I].

All 112 coordinates remain. The recheck splits the two parity blocks only after budgeting the COMPLETE opposite-parity enclosure by its symmetric row-sum norm nu, approximately 5.10e-40. Successful positive blocks for G-tau I-nu I certify the full G>=tau I; opposite-parity terms are not silently set to zero.

At tau=1e-28, the even block fails at pivot index 33 (zero-based). Its upper endpoint is below -0.01209. Previous interval pivots are strictly positive, so elimination gives a negative restriction for G-(tau+nu)I. Consequently this comparison matrix cannot have a lower margin tau+nu; this is stronger than merely failing an algorithm. It is NOT a negative actual native physical test or an upper bound for the true operator's lowest eigenvalue. G is the conservative comparison used by this specific certificate.

The original tau passes with 112 strictly positive interval pivots at a fresh 100-digit grid. At tau=1e-29 the even block fails at index 37 with upper endpoint below -0.9804. The same argument gives the stronger comparison-margin ceiling 1e-29+nu. A failed candidate without a negative upper endpoint would be inconclusive and must be labeled accordingly. No floating-point eigenvalue estimate is used in any certificate.

## 6. Concurrent custody and smallest genuinely new task

NF57 on the existing shared branch was read: it preserves the actual complete prime dictionary and derives an explicit canonical smearing error and an actual one-prime sharpness control. No new smeared positivity or global gain bound was supplied. Its result is audited rather than merged into or redirected by PS2. PS1's two-sided spectral theorem, physical mass and NF49/NF50 limit restrictions remain unchanged.

The pre-publication recovery also read [NF58](https://github.com/monocap-tech/weil-lab/commit/fba75ed4eda84f0c71286f314f85b0d29db0202a). It proves a faster-than-every-fixed-inverse-log-power smearing error on bounded-level ORIGINAL eigenvectors, with constants depending on aperture, level bound and chosen moment order. Its sign-transfer theorem needs an independent WHOLE-domain smeared lower bound. This is a relevant alternative to the slow unrestricted-domain error; it is not contradicted by PS2's comparison-margin audit. No numerical moment constants, positive smeared certificate or new aperture are supplied there. Fixed-aperture eigenvector estimates must not be treated as already uniform along varying pre-contact apertures, and smearing an atom at its support threshold must still be charged. This changes the available approximation interface, without solving its arithmetic sign premise.

The smallest useful next proof for THIS localized route is now precise: control the ORIGINAL complement-sensitive quantity B_b*C_b^(-1)B_b relative to its anchor, with signed or correlated information strong enough to leave a finite positive Schur margin at a materially larger b. An arithmetic estimate for that coupled quantity, or a stronger actual restriction/coupling certificate, could improve (1). Independent absolute block budgets inherited from the same slow global modulus do not. NF58 separately supplies a sign-transfer route if an independent complete smeared lower bound can be proved; extending its moment recurrence or restating its transfer does not count as that bound.

Stop condition reached for this attempt: no useful larger interval and no distinguishing arithmetic information. PS2 publishes the block theorem, conservative-margin audit and countercontrol; it does not continue generic geometry indefinitely. Actual global positivity, RH, F4, full transport and new Lean closure remain open.
