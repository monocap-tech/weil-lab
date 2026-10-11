# RPB108 RC101 — Odd three-mode jump-aware Schur certificate

Date: 2026-10-11. Branch: `research/rpb108-route-consolidation`.
Predecessor: RC100, commit `977f192222b7ca634a59b1fe34c478b5175c75ce`.
Aperture B=1.10; R=2B=11/5. Actual sufficient canonical Riesz head rank 1250.

RC101 certifies corrected original Weil positivity on the full odd three-dimensional span, including both weak/control cross terms. Retaining RC100’s even three-dimensional certificate and exact parity orthogonality gives a positive six-dimensional corrected span. The original operator’s nonpositive spectral-dimension upper drops from 1245 to 1244. Complete weak-mode coverage and whole-aperture positivity remain open.

## The odd source and its shared jumps

RC101 uses the unchanged RC63 odd weak_0, weak_1 and positive_control vectors, the matching RC67 64-mode Riesz trials, and the complete original signed Weil remainder. There are six signed derivative Gram entries to certify. No even derivative entry is substituted for an odd one.

For each trial V_j, parity gives V_j(-1)=-e_j and V_j(1)=e_j. For each active prime power n=p^k, set

    c_n = 1-log(n)/B,    w_n = -log(p)/sqrt(n),
    J_o(t) = sum_n w_n [1_(t>-c_n)+1_(t>c_n)-1].

At either prime support boundary the actual odd source has jump -e_j w_n: entering at -c_n uses V_j(-1), and exiting at c_n subtracts V_j(1). Thus the nominal original source has the decomposition

    F_j = g_j - e_j J_o.

The remainder g_j is continuous across all prime support boundaries. Its derivative on every open segment agrees with F_j'. The shared sign in front of J_o disappears in its rank-one covariance; retaining it correctly is necessary for the decomposition.

For either sign of c_n, the n-th step profile equals sign(t) times 1_(|t|>|c_n|). Generation computes its full physical norm by walking all fourteen ordered knots, including both exterior intervals. Independent replay instead uses the overlap kernel

    integral_-B^B J_o(x/B)^2 dx
      = 2B sum_(n,m) w_n w_m [1-max(|c_n|,|c_m|)].

All knot orders and signs of c_n are checked with directed intervals. The odd Legendre coefficients, for odd degree d<1250, are generated as

    h_d = 2B sum_n w_n [P_(d-1)(c_n)-P_(d+1)(c_n)]/(2d+1).

Replay uses the independent derivative identity

    h_d = 2B sum_n w_n (1-c_n^2) P_d'(c_n)/[d(d+1)].

The use of c_n instead of |c_n| is valid because d-1 and d+1 are even. All even coefficients vanish by parity. Full norm minus the sum of 625 odd coefficient energies certifies the infinite physical tail j_tail beyond the degree cutoff. This is a Parseval calculation for one shared scalar jump profile, not a dense original Weil head evaluation.

## The signed three-input derivative Gram

In y=(t+1)/2 coordinates the polynomial/logarithmic archimedean source form is

    A_j(y)+L_j(y) log(y)+M_j(y) log(1-y),
    M_j = -reflect(L_j).

The differentiated non-logarithmic part is A_j'+L_j/y-M_j/(1-y). Odd parity makes its last two terms L_j/y+reflect(L_j/y). Each logarithmic coefficient vanishes at its singular endpoint, so the weighted energy is finite.

The signed odd pole source is -2 t_j sinh(Bt/2), where t_j is the physical pairing of V_j with exp(Bt/2). Its y derivative is -R t_j cosh(Bt/2). The validator includes the even Taylor polynomial through degree 80 and bounds the uniform omitted derivative by

    eta_j = R |t_j| 2(B/2)^81/81!.

The first omitted cosh degree is 82; the displayed geometric bound deliberately overestimates that tail. Positive-series interval pole pairings are independently recomputed on replay.

All six entries of

    D_nom,ij = integral_0^1 y(1-y) F_i'(y) F_j'(y) dy

are integrated with directed 800-digit arithmetic. They include the full polynomial input, finite archimedean approximation, all fourteen prime translations and signed pole polynomial before taking a matrix upper. Generation uses grouped log products and incomplete primitive differences; replay uses nine ordered log products, reflected log(1-y) primitives and affine prime integration on all fifteen segments.

For nu=1/65536, a weighted row bound produces D_nom,upper. The exact common omitted-pole allowance is

    D = (1+nu) D_nom,upper
        +(1+1/nu) diag(eta_j^2/2).

Indeed integral_0^1 y(1-y)dy=1/6 and there are three inputs, so Cauchy gives a factor 3/6=1/2 on the diagonal allowance. This is a common Gram inequality for every combination, not three unrelated diagonal estimates.

## Tail, source transfer and signed head

The weighted Legendre derivative theorem gives

    C = R D/[1250*1251],
    J_tail = j_tail e e*,
    N(s) = tau1250^2 [(1+s) C+(1+1/s) J_tail].

The subtraction by physical polynomials of degree below 1250 maps into the actual sufficient canonical head H1250. RC95's accepted tau1250 bounds the canonical adjoint on its orthogonal complement. Consequently N(s) is a common upper for the nominal projected source Gram on that complement.

As in RC100, RC81's raw nominal residual intervals are contracted onto all three actual target vectors before interval-to-matrix inflation. With rho=252/257, trial physical Gram T_trial and original approximation errors delta_L, delta_K,

    Ep = rho^2 [(1+nu) E_nom,upper
                  +(1+1/nu) delta_L^2 T_trial],
    E = rho(1+nu) k1250,odd^2 Ep
        +(1+1/nu) delta_K^2 tau1250^2 T_trial,
    Gamma1250 <= G(s,t)=(1+t)N(s)+(1+1/t)E.

The transfer uses the odd pole factor from RC89. Signed physical derivative correlations inform a common upper; they do not fix signs of actual canonical projected covariance entries.

The actual original odd head lower is rebuilt from RC97's matching signed trial head centers, trial radii and the newly balanced common Ep. The paid additional entry radii are

    sqrt(Ep_ii) s_j + sqrt(Ep_jj) s_i,
    kappa_odd sqrt(Ep_ii Ep_jj).

Canonical error contributes -Ep_ii/rho to the lower diagonal and an absolute sqrt(Ep_ii Ep_jj)/rho to mixed entries. Here s_j bounds the actual source norm and kappa_odd is RC66's complete physical odd operator bound. The weighted row scales are (8000,100,1), also used for residual and derivative upper inflation.

Exact rational pivots certify Q_lower>0. The acceptance test is

    G(s,t) <= lambda Q_lower,    lambda < alpha=247/2500.

It then follows on the full odd three-dimensional span that

    Q_actual-Gamma1250/alpha
      >= Q_lower-G(s,t)/alpha
      >= (1-lambda/alpha) Q_lower > 0.

This tests correlation in the full matrix. The finite Young grid {1/4,1/2,1,2,4} supplies sufficient certificates; rejection by this grid would not prove actual nonpositivity.

## Exact acceptance and spectral consequence

The accepted Young parameters are s=1 and t=1. Exact rational matrix tests give

    lambda = 63733457079/1099511627776
           approximately 0.05796524153902 < alpha = 247/2500 = 0.0988.

The retained fraction of the signed original head lower is

    1-lambda/alpha = 28061432340793/67894843015168,

approximately 0.4133072718722. Both the signed three-mode head lower and its corrected lower have strictly positive exact pivots.

The six signed weighted derivative entry enclosures have approximate centers:

| Entry | Center, display |
| --- | ---: |
| weak_0 diagonal | 3.1847985171e-12 |
| weak_0 / weak_1 | -7.3116677151e-11 |
| weak_0 / control | 2.0774220854e-08 |
| weak_1 diagonal | 2.2251659382e-08 |
| weak_1 / control | -1.6665985931e-06 |
| control diagonal | 4.1208327209e-04 |

The odd jump physical tail norm squared is at most approximately 0.0008593882059139. The common actual control coupling upper is approximately 2.564562747949e-09, compared with RC98’s 1.1250255198e-8. This compares sufficient upper certificates; it supplies no lower bound on actual coupling.

An exact lower bisection against rho times the physical native Gram certifies the odd corrected canonical floor at least

    566901718717/1073741824000000000000000000,

approximately 5.279683682295e-16. The actual canonical Gram is bounded above by this comparison Gram. The accepted PSD inequality therefore proves a lower bound in the actual canonical norm.

RC100’s retained even floor is smaller. By parity the full six-dimensional corrected span has canonical floor at least

    343413578179/274877906944000000000000000000,

approximately 1.249331319483e-18. The three actual vectors within each parity are independent because their positive head lower is positive definite. Opposite parities are orthogonal for the actual metric, original Weil form and projected coupling covariance: the original operator, the sufficient head and its complement preserve parity.

Schur completion with the inherited positive infinite complement gives a positive subspace of codimension 1250-6=1244. Any nonpositive original spectral subspace intersects this positive subspace only at zero, so its projection to the remaining head coordinates is injective. Hence its dimension is at most 1244, by the RC96 codimension argument. RC77 compactness makes these the finite exceptional spectral modes below the essential spectrum at 1. This bound is not an assertion that all 1244 remaining dimensions are dangerous or that they require dense evaluation.

## Verification and remaining frontier

The sixteen direct inputs are RC100, RC99, RC95, RC97, RC98, RC63, RC67, RC59, RC56, RC43, RC46, RC68, RC81, RC83, RC89 and RC66. SHA-256 digests, predecessor crosslinks, unchanged fixed coefficient vectors and exact trial parity are checked. RC100’s complete input digest list is checked against all fifteen remaining files.

Generation certifies six new derivative entries and a new odd jump profile. Independent replay recomputes all six entries using nine ordered log products, reflected incomplete primitives and affine prime overlaps, and the odd jump profile using its step-overlap kernel and derivative Legendre identity. Replay uses finer outward intervals for the derivative entries and jump tail; those intervals must lie inside the generation enclosures. It then reconstructs the head, transfer, common source upper, exact relative matrix test and canonical floor, and requires exact equality with the saved certificate.

The local derivative checkpoint and logs are intermediate files, not repository deliverables. The certificate is an internal directed-interval/exact-rational proof, not a Lean formalization. No dense 1250-feature original Weil head is evaluated.

The immediate known-control cross problem is now closed in both parities. The next theorem-facing obligation is coverage: prove a positive lower bound on the remaining strong head and control its interaction with the certified six-dimensional span, or prove an index/exclusion or first-contact theorem that replaces this completion. The present six vectors are not proved to exhaust all potentially nonpositive modes. Their positivity alone does not settle the full original form, Global/F4 or RH.

- `scripts/validate_rpb108_rc101_odd_three_mode_jump_tail.py`
- `certificates/rpb108_rc101_odd_three_mode_jump_tail.json`
- `notes/RPB108_RC101_ODD_THREE_MODE_JUMP_AWARE_SCHUR_20261011.md`
