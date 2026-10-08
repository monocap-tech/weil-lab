# RPB108 NF68: finite critical reaction with the entire incoming shell retained

2026-10-08 UTC / 2026-10-07 Pacific. Recovered Global `d6d5d5dcbb999924db59d9bdc66c6ce800280ab2` (NF67); inspected Coupled `191b3c04dbddf9789c19cbb4ad7562deac2e9ec1` (CC8) read-only. Definitions precede use in [critical-reaction registry](../docs/TERMINOLOGY_RPB108_CRITICAL_OUTPUT_REACTION.md).

**Result.** Under NF67's independently protected finite critical OUTPUT space and a strict WHOLE low-output incoming bound, the remaining ORIGINAL continuation gate is exactly a finite matrix:

    Hcrit = Gcrit - L (I_W-B_low)^(-1) L*,
    g_t<1 iff Hcrit>0.

The inverse still acts on the ENTIRE, possibly infinite-dimensional source-orthogonal incoming shell W. This is not retained physical-block positivity or a source-prefix truncation. Its entries have an exact original mixed-form dictionary and admit an upper enclosure from a complete residual solve. No actual zeta overlap matrix has been evaluated here. This advances the specification of the arithmetic gate; it does not discharge it.

## 1. Hypotheses and exact elimination

Adopt NF67's complete normalized ORIGINAL P,N on a fixed finite aperture cap, with Q(h,k)=<Ph,Pk>-<Nh,Nk>. All partner normalizations, actual ordinates and multiplicities are unchanged. Assume g_s<1 and use its exact shell W=V_t intersect V_s^perp, K=T_t|W, A_s=T_s T_s*, D=I-A_s.

Choose 0<eta<1 and E=E_s((1-eta,1]). A protected codimension-d physical complement, as in NF67, independently proves rank E<=d when eta<c/C_P^2. It is not assumed to persist beyond its certified chart. Put

    Y=range E, G=D|Y, L=EK,
    B_low=K*(I-E)D^(-1)(I-E)K,
    C_W=I_W-B_low.

G is strictly positive on Y because the OLD original gain is below one. Assume an independently proved WHOLE bound B_low<=b I_W with b<1. The crude sufficient bound eta^(-1)|| (I-E)K ||^2<=b is available only when actually established. Merely testing finite incoming vectors supplies neither this hypothesis nor its strictness.

NF67 gives B=K*D^(-1)K=B_low+L*G^(-1)L. Hence

    J=I_W-B=C_W-L*G^(-1)L.                    (1)

Consider the bounded self-adjoint block on W direct-sum Y with diagonal C_W,G and off-diagonals -L*,-L. Exact square completion in either order gives congruences to

    diag(C_W, Hcrit), Hcrit=G-L C_W^(-1)L*,
    diag(J, G).                                (2)

Both eliminating blocks are uniformly positive. Thus J is uniformly positive iff Hcrit is uniformly positive. Since Y is FINITE dimensional, Hcrit>0 is a finite matrix sign and is automatically uniform. By NF67, this is exactly g_t<1. The case Y={0} simply reduces to C_W>0.

Similarly J>=0 iff Hcrit>=0; their kernel dimensions and negative indices agree. The original source-coordinate form on V_s direct-sum W is congruent to diag(I-T_s*T_s,J). Consequently Hcrit's negative index and nullity are also those of the ORIGINAL Q_t. This is a conditional exact count, not proof that actual zeta has a negative vector or contact.

The matrix is finite because the output is protected, NOT because the whole incoming source shell is finite. All of W remains in C_W^(-1). A bare bound L L*<G does not suffice when the low channel consumes budget: for scalar G=1/2, L L*=1/4, C_W=1/4, the raw inequality holds but Hcrit=-1/2.

## 2. Relative reaction and quantitative continuation

Define the finite relative reaction

    Rcrit=G^(-1/2) L C_W^(-1)L* G^(-1/2)>=0.

Hcrit>0 iff ||Rcrit||<1. If independently ||Rcrit||<=r^2<1 and B_low<=b I with b<1, then

    J >= (1-b)(1-r^2) I_W.                     (3)

Indeed J=C_W^(1/2)[I-R*R]C_W^(1/2) with
R=G^(-1/2)L C_W^(-1/2), whose squared norm is ||Rcrit||.
Thus the FULL incoming cost obeys ||B||<=1-(1-b)(1-r^2)<1, giving NF67's quantitative original-gain consequence. This is sharper in structure than independently bounding the critical term and adding its norm to b: it retains low/critical correlation via the exact low-shell completion.

The relative matrix may reach one at a finite aperture. Bounded absolute sources or a finite output dimension does not rule this out. No accumulated relative-loss nondivergence is inferred.

## 3. Exact ORIGINAL mixed arithmetic dictionary

Let A_Y=A_s|Y; it is invertible because A_Y>(1-eta)I. Define the old physical lift

    Z n=P_s^(-1) T_s* A_Y^(-1)n, n in Y.         (4)

The inverse P_s^(-1) is only used on V_s. Polar/spectral invariance gives

    N Z n=n,
    P Z n=T_s* A_Y^(-1)n,
    Q(Zn,Zm)=< (A_Y^(-1)-I)n,m>.                (5)

For w in W put k=P_t^(-1)w. Source orthogonality gives <PZn,Pk>=0, so the exact mixed original source identity implies

    <n,Lw>=<n,Nk>=-Q(Zn,k).                    (6)

In a critical eigenbasis with A_s n_i=lambda_i n_i, lambda_i>1-eta, the old representer is Z n_i=lambda_i^(-1)P_s^(-1)T_s*n_i. This division by lambda_i must not be omitted. The old physical Gram is (1-lambda_i)/lambda_i, while G's source-coordinate defect is 1-lambda_i; they are distinct metrics.

Thus the finite reaction's quadratic is the WHOLE dual mixed-form supremum

    <L C_W^(-1)L*n,n>
      =sup_(w in W) [2 Re<n,Lw>-<C_W w,w>]
      =sup_(k=P_t^(-1)w,w in W)
           [-2 Re Q(Zn,k)-||Pk||^2+<B_low w,w>]. (7)

Every arithmetic slot in the original Q is retained by this identity, including the logarithmic background, all active prime powers with Lambda(p^r)=log p and both orientations, and both signed poles. At prime-power activation equality physical overlap remains zero. Equation (6) does not set the mixed arithmetic form to zero; it translates its precise nonzero reaction into source coordinates. The incoming k need not be confined to the outer physical strip. Any arithmetic calculation replacing it by that strip changes the question.

Equations (4)-(7) are analytic identities under NF67's published complete range/observability assumptions. They are not new Lean results or an evaluated zeta correlation bound.

## 4. Complete residual UPPER enclosure

A finite reaction matrix can be certified without treating a trial solve as the exact entire inverse. Let U:Y->W be ANY bounded trial solve for C_W^(-1)L*. Put

    Eres=L*-C_W U,
    Jtrial=L U+U*L*-U*C_W U.

Exact completion yields

    L C_W^(-1)L*=Jtrial+Eres* C_W^(-1)Eres,
    Jtrial <= reaction <= Jtrial+(1-b)^(-1)Eres*Eres. (8)

Thus an independent WHOLE residual enclosure Eres*Eres<=Rbar makes

    Hcrit >= G-Jtrial-(1-b)^(-1)Rbar.            (9)

Positive definiteness of this finite LOWER matrix certifies the original gain gate. A positive G-Jtrial alone is an UPPER estimate for Hcrit and proves no sign. The trial solve must act on ALL critical columns and its residual Gram must include all mixed columns and the full incoming norm. One direction, a frozen source height, or a residual calculated in a trial subspace is insufficient.

CC8 has actual original complement solves for one physical retained direction and pays its full residual; it does not supply U, Eres, the critical source eigenspace, or the whole low-shell bound in (8). No equivalence between those different solve spaces is asserted. Its single-direction improvement and its unresolved whole matrix gate remain intact.

## 5. Contact, crossing and positive-level controls

If Hcrit y=0 with y nonzero, set

    w=C_W^(-1)L*y,
    n=D^(-1)K w,
    p=T_s*n+w in V_t, h=P_t^(-1)p.              (10)

Then G y=Lw, so E n=y. The low component of n is its exact low-defect inverse reaction; C_W w=L*y implies K*n=w. Hence A_t n=n, T_t p=n and T_t*n=p. Consequently h is a NONZERO original full mixed-null vector. Conversely every original null vector yields such a y. This is an exact conditional reconstruction, not an assertion that the actual matrix is singular.

For a positive physical eigenlevel mu, the negative analysis is (N,sqrt(mu)physical). The old A_s, its spectral E, L, C_W and G must all be recomputed in this extended output ambient. A unit relative reaction in that shifted problem is compatible with Q(h)=mu||h||_2^2>0 in the original problem. Reusing the shifted matrix as original Hcrit is forbidden.

Finite exact controls cover genuinely coupled noncommuting low/critical reactions, complete original-source block inertia, both square completions, original mixed representers, exact nonzero-source contact, negative crossings, and the positive level mu=11/100. They validate algebra only. NF67 and the genuine crossing controls already show that no abstract source identity alone supplies the missing arithmetic suppression.

## 6. Validation, scope and next cursor

[scripts/validate_native_critical_output_reaction.py](../scripts/validate_native_critical_output_reaction.py) uses only exact rational arithmetic. 486 checks pass across 48 coupled cases: 16 strictly positive, 30 with negative index and 2 with exact nullity. The analytic infinite-dimensional congruence and range arguments are proved above, not by those samples and not Lean-formalized.

The next substantive ORIGINAL arithmetic input is now a concrete finite relative matrix enclosure, using (6)-(9), together with an independently protected output space and a WHOLE low-shell bound. Neither finite output dimension nor the dictionary itself estimates those entries. If actual source spectral coordinates are unavailable, that is a remaining construction obligation; they must not be replaced by selected divisor rows or a physical retained block.

No evaluated actual overlap, new zeta gain bound, larger certified aperture, actual contact, original negative vector, relative-loss nondivergence, RH, F4, full transport or Lean closure. NF65-NF67, Coupled CC8, paused Aperture/Shadow refs and historical artifacts are preserved. No earlier endpoint regularity, compactness, Abel transfer or terminal classification is restarted.
