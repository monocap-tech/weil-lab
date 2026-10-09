# RPB108 DNE16 — Native two-high correlations and the optimized residual gate

Date: 2026-10-09 UTC. Independent continuation from eb5419b6b471ff4f95b08a3612519b2b9735775c. [Definitions](../docs/TERMINOLOGY_RPB108_DNE16_CORRELATED_SOURCE_GATE.md).

## New native arithmetic

At a=53/50, DNE16 constructs the complete projected source sigma=P_U L_Q p_star of each exact H2-compensated NF24 target and both projected measured-high sources K_j=P_U L_Q e_hj. Here U is the physical complement of all 56 retained modes and the two measured high modes. The joint 3-by3 Gram gives P2=||sigma||², Z=K^*sigma and H=K^*K. Every original archimedean, prime and signed pole cross-term is included.

| Paid native quantity | Even | Odd |
|---|---:|---:|
| Optimized gain fraction G/P2 | (0.00438429,0.00438434) | (0.0006648051,0.0006648055) |
| Gain in percent, approximate display | 0.438431% | 0.0664805% |
| Required gain fraction | (0.40869761,0.40869804) | (0.26145821,0.26145823) |
| Optimized J_min/S2 | (0.34853984,0.34854012) | (0.28009570,0.28009572) |
| Required upper bound J/S2 | 0.207 | 0.207 |
| Gate, including exact optimizer | **Fails** | **Fails** |

The joint native correlation is nonzero but much too small. This proves a stronger rejection than DNE15: even the best possible two-high variational trial cannot repair the scalar-floor estimate on either actual near-critical target. In particular no fixed two-by56 trial matrix can pass CC60's collective sufficient gate, since its evaluation on these retained directions would have to pass the failed directional test. This is a rejection of the estimator, not native negativity or a full-operator null.

For reference, approximate displays of the new native high-source Gram and correlations are:

| Entry | Even | Odd |
|---|---:|---:|
| H00 | 1.030924558449 | 1.024721403776 |
| H01=H10 | 0.768071095282 | 0.694625214162 |
| H11 | 1.369125995225 | 1.351294035028 |
| Z0 | 7.03244416e-19 | 2.35445647e-17 |
| Z1 | 1.37418207e-18 | 2.14922510e-17 |

These are displays, not point-exact inputs. Full outward intervals, including mixed-entry errors, are in the certificates. The result table is widened outward from the primary paid intervals.

## Native source construction and both projections

The copied NF24 target decodes to SHA256 6eee61fb4e58ac5be0e95f492f461b289da37ee13aeaa74bbf4acc06f6650c00. The same authenticated 56 rational retained coefficients and two high corrections used in DNE15 are used here. The native high form C2 is taken from the complete intervals in the copied CC60 validation at read-only Coupled head 795aa8849d07d99c7da880ca201dfda8aa011623. This is an authenticated input, not a new replay of the raw NF17/NF19 archives.

For each parity the three finite source inputs are the frozen target and its two normalized high Legendre modes. Write the full source as L_Q p=U_p-(p/2)log(a²-x²). DNE15's exact harmonic singular action, grouped regular convolution, both orientations of all six clipped prime powers {2,3,4,5,7,8}, and the correctly signed pole terms build each U_p. On each of seven half-interval panels the mixed source product is

    U_i U_j - (U_i p_j+U_j p_i)log(a²-x²)/2
              +p_i p_j log²(a²-x²)/4.

The source moment against each monomial is integrated with the same polynomial and stable log primitives. Dotting these moments with each normalized Legendre coefficient vector gives all 58 same-parity source coordinates. The truncated joint Gram is THEN projected by subtracting the products of every retained and measured-high coordinate. In particular the high sources K_j lose both their retained projection and their native C2 projection. Removing only the low projection would compute the wrong H and Z.

Projection uses coordinates of the same finite source approximation that is squared. It does not mix exact projection coefficients with an approximate source without paying their difference. The original projected source is enclosed afterwards by contraction of the complete source error. This also avoids requiring missing full native low-high matrix columns as inputs.

Sixty independent finite-form overlap checks run per parity: four computed high-source/high-mode pairings against CC60 C2, and 56 computed target/low-mode pairings against the NF24 native ledger. These checks pay the source approximation error. Both-high target coordinates are removed explicitly even though exact compensation makes them zero after transfer.

## Error ledger and exact compensation

The primary run uses 600-digit directed Decimal arithmetic and regular order N=360; the replay uses 650 digits and N=400. The regular/pole source operator error is

    eta_N=2a*(550/19)*(106/125)^N+3e-99.

The high inputs have physical norm one. The frozen target gets eta_N times its authenticated norm. DNE15's rational correction-to-exact-H2 ledger bounds the additional source transfer by 4e-58. That transfer is added to the target's source radius; the exact compensated energy interval is enlarged downwards by 1e-118. The ledger guards are executed again, rather than assuming a frozen correction is the exact minimizer.

If ghat_ij is the projected truncated source pairing and epsilon_i bounds the projected source error, its native error radius is

    epsilon_i sqrt(ghat_jj^upper)
      +epsilon_j sqrt(ghat_ii^upper)+epsilon_i epsilon_j.

This is applied to all six independent joint entries. Interval arithmetic encloses all coefficients, signed mixed products, projections, C2 products, determinant, inverse expression, rational-trial evaluation and final subtraction. Decimal ln/sqrt endpoints are widened by a representable neighbor; pi and gamma retain DNE15's rational Machin and Euler-Maclaurin certificates. No Gaussian sample is substituted for the source integral.

## Optimized and fixed rational gates

With the inherited kappa=207/1000 define W0=C2(C2-kappa I) and V=W0+H. Native C2 spectral lower bounds 2.8 even and 2.89 odd imply W0>0 and V>0. The two-by-two determinant is also checked positive in each paid interval computation. CC59's gain is

    G=Z^*V^-1 Z,
    J_min=P2-G,
    T_rest<=J_min/kappa.

The inverse is evaluated by its explicit symmetric two-by-two determinant formula with all entries enclosed. For an exact rational two-vector y, CC60's identity is

    J(y)=P2-2y^*Z+y^*Vy
        =||sigma-Ky||²+y^*W0y >=J_min.

Each output also freezes a rational y from the midpoint inverse trial, with denominator dividing 10^60, and encloses J(y) using the native joint Gram and C2 intervals. This is valid for every exact rational y because the entire native joint Gram was already enclosed; it does not depend on treating a numerical optimizer as exact. The certificate records the actual rational values.

Both paid lower bounds J_min>kappa S2 are strict. Since J(y)>=J_min for every trial, further tuning of y within this same two-source variational family cannot close these targets. The frozen rational trials also fail, and closely attain the optimized values. No inverse-rounding error is blamed for failure.

CC59's least-compatible high completion attains this upper response bound. Therefore improving the sufficient response estimate requires more native high-form information than this floor and these two source correlations. It does not require the actual native high form to equal that least completion, and it gives no logical nonimplication from all Weil identities.

## Verification and reproduction

All four native source runs executed successfully. Higher-order replay tightens the optimized J_min/S2 brackets to (0.348539977410,0.348539977774) even and (0.280095711505,0.280095711513) odd. The gain fractions narrow to (0.004384313215,0.004384313270) even and (0.00066480531819,0.00066480531855) odd. These displays are widened outward from the paid replay intervals.

The exact Fraction algebra validator passes 640 assertions covering joint projection, polarization, the explicit inverse, the variational identity and its nonnegative gap. A separate rational certificate validator passes 206 checks, including all primary/replay joint-Gram overlaps, both DNE15 exact-target overlaps, positive high-Gram determinant guards and the strict optimized gate failures. Across the four native runs, all 240 finite-form/source compatibility checks pass. Python compilation checks pass. No Lean or GitHub Actions run is claimed.

Reproduce from the published producer, the DNE15 encoded target, copied CC60 input and an output path:

    python scripts/certify_dne16_correlated_source.py even \
      notes/data/RPB108_DNE15_NF24_TARGETS_20261009.json.gz.b64 \
      even_certificate.json \
      notes/data/RPB108_DNE16_CC60_NATIVE_INPUT_20261009.json

Use odd for the odd parity. Environment variables DNE16_PRECISION and DNE16_ORDER select the replay settings 650 and 400. The standalone rational certificate validator takes directories containing DNE16 primary/replay outputs and DNE15 replay outputs, named even_certificate.json, odd_certificate.json and their *_replay_certificate.json counterparts.

## Scope and next frontier

The next useful original-arithmetic step is a stronger source-aligned effective high-form bound, more measured high modes with their complete projected sources, or an enclosure of the actual inverse-weighted reaction. The measured correlations quantify why optimizing the same rank-two correction is exhausted.

A concrete alternative target is to certify an original F112 floor above 0.35008: DNE15's paid ratios would then close BOTH coarse directional tests directly. This is a proposed arithmetic bound, not a bound proved here, and it would still leave the full 56-dimensional matrix gate to be established. Any refined directional proof must ultimately establish T_rest<S2 rather than infer a sign from the estimator's failure.

These are complete native source integrals and paid directional correlations at the original near-critical energy scale. They do not evaluate the true infinite inverse, prove native negativity, exclude actual nulls, certify the whole 1.06 aperture, establish an old-gap-independent critical-space lower frame, or settle RH/F4, transport or Lean. DNE14's constant-line result and DNE15's coarse-gate rejection remain unchanged. No other branch is written.
