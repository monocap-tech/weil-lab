# RPB108 RC95 — All four known weak modes pass the corrected Schur test

Date: 2026-10-11. Branch: `research/rpb108-route-consolidation`.
Predecessor: RC94, commit `52ae3e4a9446a4b38c9bbb1d7c93287aa5db2d4b`.
Aperture: B=1.10, physical interval length R=2.20.

RC95 closes the full known even two-mode corrected Schur block. RC94's odd result is retained. Parity orthogonality then certifies positivity of the corrected form on the entire four-dimensional span of the fixed RC63 weak vectors.

This is the first pass in this sequence where all four known weak modes, including both same-parity cross entries, satisfy the rank-1250-complement Schur condition. It does not certify that these are all dangerous modes, control the remaining strong block, or pay the weak/strong inverse allowance. Whole-aperture positivity, RH and Global/F4 remain open.

The improvement comes from a structural source-tail theorem: remove the exact common prime-jump profile, bound the continuous remainder by its signed weighted derivative Gram, and transport that tail through the rank-1250 canonical complement. There is no dense 1,250-feature Weil-head evaluation and no new list of original-source pairings against all 1,250 features.

## Exact acceptance

Let Q_e,lower be the unchanged RC94 signed original Weil lower on the two known even vectors. Let G_e be the RC95 upper for their actual rank-1250 coupling covariance. Exact rational arithmetic proves

    G_e <= lambda_e Q_e,lower,
    lambda_e = 36109321197/549755813888
             approximately 0.0656824726266 < alpha = 247/2500 = 0.0988.

Consequently

    Q_e,actual − alpha^(-1) Gamma_1250,e
      >= Q_e,lower − alpha^(-1) G_e
      >= (1−lambda_e/alpha) Q_e,lower > 0.

The retained fraction of the even head lower is approximately 0.33519764548. The corrected even lower has approximately

| Entry | Value |
| --- | ---: |
| weak_0 diagonal | 3.549809923e−18 |
| weak_0 / weak_1 cross | −2.133520549e−16 |
| weak_1 diagonal | 7.993228988e−14 |

Its positive leading entry and positive determinant are checked exactly. Displayed decimals are explanatory; they are not evidence for acceptance.

A separate exact rational bisection against the actual canonical Gram upper proves a corrected even canonical floor at least

`835477998907/274877906944000000000000000000` (approximately 3.03945125382e-18).

RC94's corrected odd canonical floor, approximately 8.567545016e−18, is retained. The full known four-mode corrected span therefore has canonical floor at least the smaller value above. Mixed-parity head and coupling entries vanish because the original paired translations, even Fourier multipliers, signed pole and complete polynomial Riesz head preserve parity.

The new even source upper also improves the RC94 even upper in the whole Loewner order. This is an improvement of actual-source upper certificates, not a lower bound on actual coupling.

## Define and remove the prime-jump profile

Write t=x/B in [−1,1], and y=(t+1)/2 in [0,1]. For each active prime power n=p^k define

    ell_n=log(n)/B,  c_n=1−ell_n,
    w_n=−log(p)/sqrt(n).

For an even trial V, its endpoint traces agree: V(−1)=V(1)=e. The exact paired prime translations have jumps e w_n at t=−c_n and −e w_n at t=c_n. Thus the common even jump profile is defined by

    J(t)=sum_n w_n [1_(t>−c_n) − 1_(t>c_n)].

For either known even source F_nom=q+K_nom V, define g=F_nom−e J. The jump subtraction makes g continuous at every internal translation boundary. Within each open support segment, g'=F_nom'. There are seven active prime powers, fourteen translation boundaries and fifteen segments. Their ordering is checked with directed intervals.

The two exact endpoint values are approximately 3.996929917e−9 and 1.308554162e−6. The jump-tail covariance is therefore the single scalar jump-profile tail norm times the endpoint outer product e e^T. It has rank one. Treating fourteen jumps as unrelated source errors would discard this correlation.

The source's logarithmic coefficients vanish at their singular endpoints. In the defining polynomial/log representation, L(y) is divisible by y and M(y) is its reflected partner, divisible by 1−y. Their derivatives have only integrable logarithmic singularities. Therefore g has finite weighted derivative energy; no divergent endpoint derivative estimate is used.

## Weighted Legendre tail theorem

Let L_n(y)=P_n(2y−1). The identities

    −[y(1−y)L_n']'=n(n+1)L_n,
    integral_0^1 L_n² dy=1/(2n+1)

give weighted derivative orthogonality. For the continuous piecewise-smooth g constructed above, integration by parts has no internal jump term. Endpoint boundary terms vanish because y(1−y)L_n' vanishes and g has finite endpoint traces. Bessel's inequality for the derivative family yields

    sum_n n(n+1)(2n+1)|integral g L_n dy|²
      <= integral_0^1 y(1−y)|g_y'|² dy.

Hence, for the physical Legendre projection P_<m,

    ||(I−P_<m)g||²_physical
      <= R/[m(m+1)] integral_0^1 y(1−y)|g_y'|² dy.

The same argument for every real linear combination of the two weak inputs is a matrix Loewner inequality. At m=1250 it controls the full infinite physical tail without evaluating each source coefficient in that tail.

## Signed derivative Gram

RC95 builds the complete original nominal source directly on the unchanged RC67 trials and fixed RC63 weak combinations. It differentiates the polynomial/log representation algebraically. For F=A+L log(y)+M log(1−y), the nonlogarithmic derivative part is

    A' + L/y − M/(1−y).

The endpoint quotients use the defining divisibility and reflection formulas, rather than division by a numerically small endpoint value.

The weighted Gram includes q', the archimedean derivative, all prime derivative pieces, the signed pole derivative and every cross term. The full-interval logarithmic products use six exact moment families. Prime/archimedean cross terms use incomplete polynomial/log primitives on the fifteen exact support segments. Correlations are retained before interval row bounds.

The pole derivative is included as an 80-degree Taylor polynomial. Its remainder is bounded by the geometric exponential-series tail, 2(B/2)^81/81!, times R and the certified trial exponential moment. The resulting weighted error covariance is paid explicitly with a Young allowance. Positive Rodrigues moments certify the pole amplitudes; no floating quadrature or sampling is used.

The weighted derivative Gram upper is approximately

| Entry | Value |
| --- | ---: |
| weak_0 diagonal | 8.568164023e−14 |
| cross | 4.012902904e−13 |
| weak_1 diagonal | 4.571355214e−10 |

All three signed entries are enclosed by directed arithmetic. The weighted symmetric interval scales are (100,1). The derivative Gram upper and its pole-error attachment are exact PSD matrices.

## Scalar jump kernel and canonical transport

The jump profile's physical tail norm is computed as its full piecewise-constant norm minus its capture by the physical Legendre polynomials below degree 1250. This is a scalar profile calculation shared by both weak inputs, not a Weil-head matrix.

For each even degree n>=2,

    <J,P_n>_physical
      = −2B sum_k w_k [P_(n−1)(c_k)−P_(n+1)(c_k)]/(2n+1).

The degree-zero pairing is 2B sum_k w_k c_k. Legendre recurrence and Parseval give the full infinite residual, including all degrees beyond the cutoff. Replay obtains the pairings instead from

    [P_(n−1)(c)−P_(n+1)(c)]/(2n+1)
      = (1−c²)P_n'(c)/[n(n+1)],

and obtains the full norm from the step-overlap kernel B[1−max(c,d)]. The directed physical jump-tail norm squared is approximately 0.00091652139638. Its rank-one covariance preserves both endpoint amplitudes and their cross term.

The canonical complement H1250=i*P_<1250 is the same complete sufficient head whose inherited Weil complement floor is 247/2500. A Fourier/Legendre concentration staircase, with frequency spacing 1/2, closes after 268 layers at frequency 134 and proves the canonical-complement embedding norm upper approximately 0.45112852565. The infinite Legendre tail is explicit. Rational logarithm replay and the factorial identity check the staircase independently.

Let D be the weighted derivative Gram upper, J_tail the rank-one physical jump-tail covariance, and E the transferred actual original-source error. Then

    C=R D/[1250*1251],
    N(s)=tau1250² [(1+s)C+(1+1/s)J_tail],
    G(s,t)=(1+t)N(s)+(1+1/t)E.

The inherited RC94 source-error upper scales by tau1250²/tau128², because each archimedean/prime/pole transfer contains one complement embedding factor. No duplicate factor is introduced. The accepted rational parameters are s=1 and t=2.

The polynomial projection in the tail theorem maps exactly into the actual Riesz head. Thus G is an upper for the actual canonical rank-1250 source coupling. The inherited complement floor is applied to that same rank. No smaller-head Weil floor is assumed.

## What is now closed, and what remains

Closed: the corrected original Weil form is positive on the four fixed RC63 weak modes and all their combinations. RC95 supplies the even block; RC94 supplies the odd block; parity supplies their orthogonal direct sum. This is an internal exact interval certificate, not a Lean formalization.

Still open: identifying every potentially dangerous direction in the complete head, certifying the corrected strong block, and bounding its cross interaction with the known weak span. If T=A−alpha^(-1)Gamma is the full corrected head and H1250=W+S, a complete proof still needs

    T_SS > 0,
    T_WW − T_WS T_SS^(-1) T_SW > 0.

RC95 proves T_WW>0 for the known four-dimensional W. It does not evaluate T_WS or establish complete weak-mode coverage. A positive principal block does not imply a positive full matrix.

The next priority should therefore shift from refining these four already-certified modes to coverage/index control and the strong/cross-block theorem. Global first-contact exclusion remains a separate route.

## Verification and deliverables

Inputs, in order: RC94, RC63, RC67, RC59, RC56, RC43, RC46 and RC68. SHA-256 digests and source/trial/native/precision crosslinks are checked. Exact parity, endpoint trace identities and inherited odd acceptance are checked.

Directed interval arithmetic uses 800-digit working contexts to pay recurrence dependency amplification at degree 1250. Existing pi enclosures remain valid; the degree-1250 jump calculation depends on newly enclosed prime logarithms and square roots. No machine-float eigenvalue is accepted. All final PSD, determinant, relative-source and canonical corrected-floor checks use Fraction arithmetic.

Independent replay uses nine ordered log products, reflected incomplete log(1−y) moments, affine prime derivative integration, a positive pole-moment recurrence, differentiated Legendre jump pairings and the step-overlap norm kernel. Finer replay derivative and jump-tail intervals must lie inside the saved generation intervals. Replay then rechecks the complete source attachment and both known weak corrected certificates.

- `scripts/validate_rpb108_rc95_jump_aware_even_source_tail.py`
- `certificates/rpb108_rc95_jump_aware_even_source_tail.json`
- `notes/RPB108_RC95_ALL_KNOWN_WEAK_SCHUR_BLOCKS_AND_JUMP_AWARE_SOURCE_TAIL_20261011.md`

No Lean files or other research fronts are changed. No complete-head positivity, RH or Global/F4 claim is made.
