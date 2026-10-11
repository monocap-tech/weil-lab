# RPB108 RC100 — Common even three-mode jump-aware Schur certificate

Date: 2026-10-11. Branch: `research/rpb108-route-consolidation`.
Predecessor: RC99, commit `cd467decb81216cdb1e64fd8945a72064a1ba492`.
Aperture B=1.10. Actual sufficient canonical Riesz head rank 1250.

RC100 certifies corrected original Weil positivity on the entire even three-dimensional span, including both added-control cross terms. Combined with the retained RC94 odd pair and parity orthogonality, the certified corrected span grows from four to five dimensions. The original operator’s nonpositive spectral-dimension upper drops from 1246 to 1245. This is not complete weak-mode coverage or whole-aperture positivity.

RC100 extends the structural source-tail method to the two known even weak vectors and the fixed even positive control. It certifies three new signed weighted derivative entries: the two mixed control entries and the control diagonal. The three old weak-pair derivative entries are retained exactly from RC95. It does not evaluate a dense 1250-feature Weil head or infer projected covariance signs from physical Gram signs.

## Common three-input tail theorem

For the three nominal original sources F_j=q_j+K_nom V_j on the unchanged 64-mode Riesz trials, all even endpoint traces agree within each trial: V_j(-1)=V_j(1)=e_j. The exact common prime jump profile is the same J certified in RC95. Thus

    F_j = g_j + e_j J,

where g_j is continuous across every prime translation support boundary. Its derivative on each open segment is F_j'. The logarithmic coefficients vanish at their singular endpoints, so the weighted derivative energy is finite.

For physical Legendre projection P_<m, weighted derivative Bessel control gives the matrix inequality

    Gram((I−P_<m)g) <= R/[m(m+1)] D,
    D_ij = integral_0^1 y(1−y) g_i'(y) g_j'(y) dy.

This holds for every real combination of the three sources. The new entries are signed integrals of the complete nominal source derivatives, including the polynomial input, logarithmic archimedean part, all prime translations and signed pole. All source correlations are retained before interval-to-matrix bounds.

RC95's scalar physical jump-tail upper j_tail is unchanged because the prime profile and cutoff are unchanged. The new three-input covariance is

    J_tail = j_tail e e*.

It has rank at most one. Only its endpoint amplitude vector grows from two coordinates to three. No new degree-1250 jump-profile integration or coefficient list is needed.

## New derivative integrations and pole allowance

The derivative source is represented by a polynomial and two logarithmic terms. Exact divisibility gives the endpoint quotients L/y and M/(1−y). Prime derivatives are integrated on the same fifteen exact support segments used by RC95.

Generation integrates the three new symmetric entries at 800-digit directed precision. It uses six full-interval logarithmic moment families and incomplete polynomial/log primitives for the signed prime cross terms. Existing pi enclosures remain valid; no floating quadrature or eigenvalue is accepted.

The pole derivative is included as an 80-degree polynomial with certified uniform remainder eta_j. Since integral_0^1 y(1−y)dy=1/6, for any three-input combination its weighted error squared is bounded by

    (3/6) sum_j |a_j|² eta_j².

The diagonal pole-error attachment therefore uses eta_j²/2, rather than the two-input eta_j²/3. The Young attachment uses nu=1/65536. This dimension change is required for a genuine common three-input Gram upper.

The weighted interval scales are (10000,100,1). Their first-to-second ratio remains the RC95 weak-pair ratio. Signed midpoint matrices are enlarged by paid weighted row radii; all final matrix tests are exact rational arithmetic.

## Canonical source transfer at the actual sufficient head

Let tau1250 be RC95's canonical-complement embedding/adjoint bound. For m=1250 define

    C = R D/[1250*1251],
    N(s) = tau1250² [(1+s) C + (1+1/s) J_tail].

The polynomial physical subtraction maps into the actual H1250. Consequently N(s) bounds the common nominal projected source Gram on that complete head's complement, not a smaller projection.

The actual-source transfer is rebuilt on all three inputs. Contract RC81's raw nominal Legendre operator-residual intervals onto the three targets before weighted row inflation. With trial physical Gram T_trial,

    Ep = rho² [(1+nu) E_nom,upper
                + (1+1/nu) delta_L² T_trial],
    rho=252/257.

Using RC89's archimedean, prime and pole transfer bounds scaled by tau1250/tau38,

    E = rho(1+nu) k1250² Ep
        + (1+1/nu) delta_K² tau1250² T_trial.

Thus for every positive s,t,

    Gamma1250 <= G(s,t)=(1+t)N(s)+(1+1/t)E.

This is a common Loewner upper. It retains mixed correlations without assigning the upper's off-diagonal signs to actual projected entries. The smaller physical subtraction degree used in RC99 no longer determines the nominal tail: the continuous weighted derivative theorem controls the infinite tail beyond 1250 directly.

## Common signed original head lower

RC97 supplies the signed original trial head centers and paid trial/source metric radii on the matching 64-mode trials. RC100 attaches its newly balanced common actual Riesz-error upper to all six head entries.

For actual source norm upper s_j and full physical original remainder norm kappa_even, the additional entry allowances are

    sqrt(Ep_ii) s_j + sqrt(Ep_jj) s_i,
    kappa_even sqrt(Ep_ii Ep_jj),
    sqrt(Ep_ii Ep_jj)/rho for canonical off-diagonal error.

The canonical diagonal correction lies between -Ep_ii/rho and zero. The same source-cancellation identity as RC92 is used; no broad 32-mode head is paired with a 64-mode error.

Weighted row subtraction with scales (10000,100,1) gives a genuine actual original head lower Q_lower. Exact positive pivots decide whether it is positive definite. If so, exact rational relative bisection tests

    G(s,t) <= lambda Q_lower.

The accepted complement floor is alpha=247/2500 on the complete rank-1250 head. A value lambda<alpha proves

    Q_actual − Gamma1250/alpha
      >= Q_lower − G(s,t)/alpha
      >= (1−lambda/alpha) Q_lower > 0.

The tested grid has s,t in {1/4,1/2,1,2,4}; it finds a sufficient rational certificate, not a necessary condition for actual positivity.

## Exact acceptance and canonical floor

The accepted parameters are s=1 and t=2. Exact rational PSD tests prove

    lambda = 45141495983/549755813888
           approximately 0.0821119028533 < alpha = 247/2500 = 0.0988.

The retained fraction 1−lambda/alpha is 5733986518209/33947421507584 (approximately 0.168907865857). The signed original three-mode lower and the corrected three-mode lower both have strictly positive exact pivots.

The three new weighted derivative entry enclosures have approximate centers:

| Entry | Center, display |
| --- | ---: |
| weak_0 / control | -3.433569959e-10 |
| weak_1 / control | 1.002228111e-8 |
| control diagonal | 4.072454859e-6 |

The common actual control coupling upper is approximately 1.085842424e-11, compared with RC98's directional upper 7.717510980e-11. This comparison is an improvement of upper certificates, not a lower bound on actual coupling. The matrix acceptance retains the mixed entries rather than using that diagonal improvement alone.

An exact rational lower bisection against rho times the physical native Gram proves the even three-mode corrected canonical floor at least

    343413578179/274877906944000000000000000000,

approximately 1.24933131948e-18. The actual canonical Gram is no larger than this comparison Gram, so the accepted PSD inequality supplies a canonical norm floor. RC94's odd two-mode corrected floor exceeds this value. Parity therefore supplies the same lower floor on the full certified five-dimensional span.

Its compression with the inherited positive infinite complement is positive by Schur completion. This positive subspace has codimension 1250−5=1245. Any original nonpositive spectral subspace intersects it only at zero, so projection onto the remaining head coordinates is injective. This gives the updated index upper 1245, by the RC96 codimension argument. It does not count the remaining modes as dangerous or eliminate a negative/null direction outside the certified subspace.

The odd positive control remains individually certified from RC98, but its mixed interaction with the odd weak pair is still open. The odd source needs its own jump profile and common weighted derivative Gram; the even profile cannot be reused by changing a label. No corrected six-dimensional positivity claim is made.

## Verification and scope

Inputs: RC99, RC95, RC97, RC98, RC63, RC67, RC59, RC56, RC43, RC46, RC68, RC81, RC83, RC89 and RC66. Byte SHA-256 digests, unchanged coefficient vectors and predecessor source/trial/projection crosslinks are checked.

The three original RC95 derivative entries and its jump-tail and canonical-transport certificates are inherited exactly. The three new derivative entries are independently reintegrated on replay using nine ordered logarithmic products, reflected incomplete log(1−y) primitives and affine prime integration. Finer replay intervals must lie inside the saved generation intervals. Replay then rebuilds the common source transfer, signed head, exact relative test and any accepted canonical floor.

The final generation uses an explicit local derivative checkpoint. The checkpoint and progress logs are intermediate files, not additional repository deliverables.

This is an internal exact interval/rational certificate, not a Lean formalization. The odd three-mode extension, complete weak-mode coverage, corrected strong block, remaining weak/strong interaction and Global/F4 remain open. No whole-aperture positivity or RH claim is made.

- `scripts/validate_rpb108_rc100_even_three_mode_jump_tail.py`
- `certificates/rpb108_rc100_even_three_mode_jump_tail.json`
- `notes/RPB108_RC100_EVEN_THREE_MODE_JUMP_AWARE_SCHUR_20261011.md`
