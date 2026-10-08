# RPB108 CC2: actual completed-graph moments discharge a local update premise

2026-10-08 UTC. Definitions: [CC2 registry](../docs/TERMINOLOGY_RPB108_COUPLED_GRAPH_STEP.md).
Base `bbb2175f460bcc314a80468d1c5dfa6dacb6d9a0` (CC1). Aperture and Shadow are paused by user instruction; this work modifies only Coupled Continuation. No practical aperture breakthrough is claimed.

## 1. Recovered state and branch custody

Coupled head recovered at bbb2175f; Shadow at `345d4f7b6f1ad0e91be7771031a875391d633ca8` (PS2). Shared/Global recovered at `47e0ada898cdc2b9d57a209db683019a3a43f40e` (NF59). NF59 was read: fixed-width prime-only global smearing is ruled out by the actual PNT packet main-term mismatch. CC2 uses ORIGINAL unsmeared prime translations, so it neither needs that failed approximation nor changes its conclusion.

Final recovery found shared head `c862cf867ea30d6e8a192d424ffa259038b25884` (complete prime-8 attempt and scalability), and Shadow head `4debbf7e50dc625e0b8404c2ba4bb052542b6d2c` (PS3 inverse-information limit). Their decision/scalability and PS3 notes were read before publication. They supply no larger positive aperture, and do not invalidate this forced-graph estimate. Their complete repository state is reconciled additively into Coupled with explicit commit parents. Paused branch refs are not moved and no paused work is launched.

## 2. Coupled theorem and actual instantiated interval

On the entire original supported domain, for

    1 <= b <= 1+2^(-10^21),

the completed physical graph estimates proved below and the imported aperture-one certificate give

    Q_b(h) >= 2e-32 ||h||_2^2,
    Q_b(h) >= 7e-35 E_log(h),
    delta_b (on pulled H=D_1) >= 7e-35,
    lambda_min(b) >= 2e-32,
    g_b^2 <= 1-(7e-35)/C_(21/20)^2 <1.

C_(21/20) is the proved finite upper norm of complete original positive analysis on the larger canonical domain. PS1's weight equivalence supplies the same upper bound on the pulled domains for b>=1. It is not numerically evaluated. All original divisor rows, multiplicities and source normalizations are retained. The gain update is a consequence of this same coercivity margin, not an independent arithmetic advance.

This is an ANALYTIC continuation theorem with exact finite budget auditing and imported interval-sign hypotheses. It is not a new Lean-certified result. The interval is larger than PS1's by a factor 10^15 in its negative binary exponent, but remains astronomically small. Outcome B is strengthened by discharging the graph-moment premise; it is not promoted to the practically useful checkpoint A.

## 3. Anchor inputs audited and remaining independent hypotheses

The five compact native archive parts were restored. Their decoded SHA256 is exactly `c0898e2625a8ced3b17844e13238e001b3adeb3c12d6f6e5949fb79b401e5cd4`, matching the original corrected certificate. All 6,328 lower-triangle interval entries were checked for endpoint order and converted to a symmetric absolute row-sum majorant. Its maximum is below 11 (illustrative display 10.5831324), proving ||F_native||<11. This is an interval-derived rational bound, not a floating spectral estimate.

The unchanged original certificate supplies physical complement cp=93/100, exact corrected Schur lower margin tau=1/(320*10^27), and exact lift bound ||T||<8. Its saved lift-squared upper value, multiplied by cp^2, bounds the actual residual-map norm squared below 49. Thus ||B||<7 with the complete original source-error correction included. These corrected-sign and Gram bounds are imported; the enormous Gram archive and its pivots are not replayed here. PS2's independent archive/sign recheck remains preserved.

The full retained physical source map L:V->L2(-1,1) has the orthogonal decomposition Lx=F_native x+Bx. Hence

    ||L||^2 <=11^2+7^2<14^2.

The compact-native norm bound is the new independently recomputed input. No unproved eigenmode membership or global derivative regularity of completed vectors is used.

## 4. Physical graph and its FORCED source equation

Take the physical split V+F. The weak complement solution is well-defined because on F

    Q_1 >= cp physical mass,
    Q_1 >= c0 ||.||_H^2,  c0=cp/[10(cp+24)]=93/24930.

The second inequality uses the certificate's actual Gårding normalization Q_1>=E_log/10-24 mass. Define W x=x-Tx. Its physical V projection is x, and Q_1(Wx,v)=0 for v in F. The saved lift bound gives

    ||W x||_2^2=||x||_2^2+||Tx||_2^2<65||x||_2^2,
    ||W||_(V -> L2)<9.

For any canonical v, physical projection onto V is bounded on H and the remainder lies in F. Therefore

    Q_1(h,v)=sum_j Q_1(h,p_j) <p_j,v>_physical, h=W x.

The actual source columns Lp_j are L2 and represent Q_1(p_j,v). Hermitian adjointness gives the forcing coefficient norm

    ||(Q_1(h,p_j))_j|| <=||L|| ||h||_2<14||h||_2.

Let ell_h be the polynomial with these coefficients. The full ORIGINAL native interior equation is

    m0(D)h=T_prime h-p_h+ell_h on (-1,1).

It is forced, not homogeneous. This avoids the unsupported CC1 shortcut of applying NF58's eigenvector estimate to a graph vector.

Use the EXISTING gapless exterior archimedean norm bound 4 and existing H^(-1/4) endpoint-removability argument, now with the additional L2 polynomial forcing in the interior. The exterior m0 action is unchanged; the interior norm is at most (6+12+14)||h||_2. The same proof glues these L2 representatives and removes the two endpoint-supported remainders. Thus

    ||m0(D)h||_2 <=(4+6+12+14)||h||_2=36||h||_2.

The already proved explicit |m0-w|<10 envelope gives

    ||h||_X1 <=46||h||_2 <=414||x||_2.            (G)

This is one forced-equation estimate for the completed graph, consumed immediately below. No earlier regularity classification is restarted, no homogeneous null equation is asserted, and no H1 conclusion or endpoint trace of h is used. The forced equation and bound apply to all 112 coefficient combinations, not only individual columns.

## 5. Diagonal and mixed perturbations have different tail powers

Write D=A(b)-A(1) in pulled canonical coordinates. Let epsilon=b-1, d_n=|min(log n,2)-min(log n/b,2)|. On the declared interval only 2,3,4,5,7 activate; their total coefficients c_n=2Lambda(n)/sqrt(n) are below 6 and d_n<2epsilon. Threshold exclusion is checked by a rational log(8)>2.02 and epsilon<=1/N^2, N=10^21.

PS1 bounds the archimedean-plus-pole physical operator change by v<=25epsilon on b<=21/20. Fix R>0 and use m=9, L=414. For h=W x, ||x||=1, Fourier splitting yields

    |<h,(tau_s-tau_t)h>|
       <=2pi R |s-t| m^2 +2 L^2/[log(e+R)]^2,
    ||(tau_s-tau_t)h||_2
       <=2pi R |s-t| m+2 L/[log(e+R)].

Compression to the support and averaging opposite shifts preserve these upper bounds. The second bounds the whole physical perturbation action, hence its bounded functional on F with H norm. The first bounds the finite graph diagonal. In particular the squared logarithmic moment gives a **squared tail denominator** for alpha, while eta has a single denominator and is subsequently squared in the Schur estimate. Replacing alpha by ||W||eta would discard the improvement.

Set epsilon<=2^-N, R=2^(N/2), N=10^21. From pi<4, log2>1/2,

    2pi R d_n <=16*2^(-N/2),
    log(e+R)>N/4.

The elementary induction 2^(N/2)>=N^2 for even N>=16 allows exact symbolic bounds without constructing huge integers. The resulting complete graph budgets are

    alpha <=[25m^2+96m^2+192L^2]/N^2,
    eta <=48L/N+[25m+96m]/N^2.

These include all original prime, archimedean and pole terms. The actual signed diagonal is enclosed in both directions; no arithmetic sign is inserted by a scalar-discrepancy argument.

## 6. Complement, completed Schur and physical/canonical conversions

The full PS1 modulus at this epsilon is

    omega <=48/N+121/N^2.

This is charged ONLY against c0=93/24930 on F. The complement lower bound is c=c0-omega>c0/2. Completing the square in the exact anchor graph then gives

    t=tau-alpha-eta^2/c >tau/2,
    q_b(Wx+z)>=t||x||_2^2+c||v||_H^2,
    v=z+C_b^(-1)H_b x,

where C_b is the F-Hilbert Riesz form, H_b represents the mixed perturbation, and ||H_b||<=eta. These are Hilbert form operators on F, not the full physical operator.

Since the physical finite/complement split is orthogonal,

    ||Wx+z||_2^2 <=||x||_2^2+(||v||_H+ell_b||x||_2)^2,
    ell_b=8+eta/c<81/10.

The exact two-variable conversion proves

    mu=t c/[t+c(1+ell_b^2)]>2e-32.

At all b in this interval, the native quarter-line lower envelope gives q_b>=E_log(U_b f)/10-25 mass, conservatively using prime loss <6, pole loss <13 and archimedean loss 6. Since E_log(U_b f)>=||f||_H^2-log(b)mass, the pulled inequality q_b>=||f||_H^2/10-26 mass follows. Blending with q_b>=mu mass gives

    delta_b >=mu/[10(mu+26)]>7e-35.

For b>=1, E_log(U_b f)<=||f||_H^2, so this is also the displayed native logarithmic bound. The physical eigenvalue lower bound is mu; no Rayleigh upper value is substituted. The resolvent remains J[A(b)+beta J*J]^(-1)J*, preserving physical mass.

## 7. Complete source gain

The full original identity Q_b=||P_b h||^2-||N_b h||^2 and proved upper bound ||P_b U_b||<=C_(21/20) imply the stated complete-range gain bound. Positive-range observability and closedness are the existing fixed-domain results; no new numerical observability constant is claimed. This is one coherent update of aperture, physical positivity and original gain.

## 8. Prime-8 behavior

The bound stays below a_8=log(8)/2. It recomputes the complete active dictionary at the actual interval and does not propagate eleven panels or dimension adequacy across 8. CC1's separate failure at prime 8 remains: the coarse archimedean budget alone exceeds the available canonical complement bound there. CC2 fixes graph control, not that threshold-complement estimate. No certificate at 21/20 is inferred.

The recovered direct 21/20 attempt already supplies a fresh physical complement 699/1000 and complete target native/source/Gram data. Its exact negative corrected-comparison witness has POSITIVE actual native energy. That failure does not refute original positivity. The witness's required scalar ratio is approximately 0.708374555, above 0.699. The complement-only 113-vector probe cannot be inserted into the 112-vector Gram. These are imported target data, not computations rerun here.

## 9. Countercontrols

The original positive eigenmode mass residual mu||h||_2^2 remains in all comparisons. Replacing Q by Q-mu mass changes its forcing, graph, complement and source-negative channel explicitly; it cannot be identified with this unshifted update.

PS2's fixed-F/fixed-B counterexample is also respected. On its completed graph, complement loss contributes alpha=zeta T^2 and eta=zeta T. Hence the new finite margin is exactly tau-M^2 zeta/[cp(cp-zeta)], reaching zero at PS2's same crossing. CC2 succeeds because it bounds the ACTUAL graph perturbation, not because complement losses disappear.

NF49's rough mixed compensation and NF50's nonuniform height limits are unused and remain intact. Bound (G) is logarithmic and permits rough zero extensions. NF56's signed discrepancy remains indefinite. NF57's full-domain sharp logarithmic rate is not improved or contradicted: sharper tail powers are proved only on the finite completed graph. NF59's fixed-width prime-only smearing is never introduced.

## 10. Could this stall?

Yes. There is no uniform lower graph margin or step size at a finite limiting aperture. PS1's generic crossing still permits arbitrarily many positive updates approaching contact. CC2 does not prove non-stalling or global positivity.

## 11. Resistance relative to PS1 and CC1

The missing ACTUAL graph-moment premise is now discharged with a quantitative forcing certificate. Its diagonal tail uses the squared moment, reducing the represented continuation exponent from 10^36 to 10^21. This is a real improvement in the sufficient bound, but both intervals are impractical. Resistance decreases for rigorous local attachment; it remains high for useful continuation and unchanged for non-stalling. No global exit is claimed.

## 12. Smallest next task and stopping decision

Do not iterate the generic moment recurrence simply to optimize an astronomically small exponent. Compute or bound the **signed completed-graph change** W*[A(b)-A(1)]W, together with its corrected mixed action, at ONE practical target. An approximate complement solve plus its full residual certificate, as in CC1, can make this finite task reviewable. For continuation from the anchor reaching prime 8, separately sharpen the complement protection before charging that graph margin. The current absolute one-moment budget does not supply this signed arithmetic information.

The final target residue makes the smallest arithmetic experiment more specific: use the failed 21/20 witness to certify ONE actual complement trial lift and its complete physical residual, with the fresh target complement 699/1000. Test whether the resulting directional inverse slack is strictly positive and large enough to repair that comparison direction. Such a direction alone would not certify the whole target block or a continuation interval; both would still require their complete enclosures. PS3 proves the old Gram plus scalar complement cannot supply this slack by themselves, even if the complement spectrum is known. The needed new data are the actual inverse alignment/residual, not more precision in the same Gram. No new full target Gram should be built merely to repeat its already decided sign.

Validation: the compact native archive is decoded and hash-checked, all 6,328 interval entries contribute to the norm upper bound, and all displayed finite step budgets, conversions, threshold inequalities and PS2 crossing controls are checked with exact rationals. The forcing/distribution/Fourier and full-domain implications are written analytic proofs, not mechanically or Lean certified. The original complete Gram and corrected pivots are imported rather than reconstructed; no fresh target Gram is built. Published claims preserve that boundary. Global exclusion, RH, F4, full transport and Lean closure remain open.
