# RPB108 CC9: an actual mixed two-retained completed-Schur block

2026-10-08 UTC / 2026-10-07 Pacific. Coupled base `191b3c04dbddf9789c19cbb4ad7562deac2e9ec1`; shared NF67 `d6d5d5dcbb999924db59d9bdc66c6ce800280ab2` and publication recheck NF68 `2f7a867881ae49e99f25d454e253c7d1a43496d4` recovered and reconciled additively. Definitions: [CC9 registry](../docs/TERMINOLOGY_RPB108_TWO_RETAINED_BLOCK.md). Aperture and Pre-Contact Shadow remain paused.

## Objective

CC3/CC8 certified one completed coefficient direction. Repeated improvement on that direction alone does not determine a whole Schur block. CC9 keeps the original physical E112/F112 decomposition and adds an independent retained direction: a DEFINED rational constant u. The retained plane V=span(h,u) is not required to be orthogonal. Two original complement trials, degrees 112 and 114, supply ONE linear lift on the whole retained plane, including all mixed products.

This step tests a full 2x2 LOWER Schur matrix. Positive diagonal tests alone are insufficient. If its determinant is positive, all combinations in that plane are certified, with the original infinite complement still eliminated. No sign for the other 110 retained coordinates is inferred.

## 1. Four complete original sources

The original constructor reconstructs FOUR sources at a=21/20: the saved witness's even part, the rational constant, and the rational degree-112 and degree-114 complement polynomials. All source normalizations are explicit. The constant and trials are defined with exact rational midpoint factors; no approximate orthogonality is used for membership in E112/F112.

The witness normalization substitution is bounded as in CC3/CC8. Its actual odd coefficients remain in its full native energy and physical mass. Reflection makes their cross products with the three even sources exactly zero. For the retained source Gram h diagonal only, their extra source energy is enclosed by 64 times their exact odd coefficient mass, using the saved ACTUAL source-map norm <8. This is not deletion of the odd source or use of a surrogate norm without its complete allowance.

Every source retains the original endpoint-log singular part, six prime powers 2,3,4,5,7,8, both orientations and both signed pole slots. The same 13 translation panels, exponential order 140, 180 Bernoulli pairs, gamma order 56 and exact outward logarithm/polynomial moment machinery apply. Integration degree is 1228. ALL source-pair products, including witness/constant and every constant/trial action product, are integrated and projected off physical degrees 0..111.

There are 112 independent retained-source/native pairing overlap checks: 56 for the witness and 56 for the constant. New native witness/constant coupling is checked against BOTH source constructions and the independently saved native matrix. Four trial/retained symmetry checks and one trial/trial symmetry check also retain the original mixed form.

The compact native matrix is decoded and its uncompressed SHA256 checked. The full binary source/Gram archives remain unreplayed. Four newly reconstructed sources do not constitute the missing full 112-source family.

## 2. Whole matrix credit, not independent scalar repairs

Let B_V be the actual two-column projected source map, and Z the two-trial complement map. Enclose

    AV=Q restricted to V,
    GR=B_V^* B_V,
    QZ=Z^*CZ, GZ=(CZ)^*(CZ),
    BZ=Z^*B_V, VZ=(CZ)^*B_V.

Every quantity comes from the SAME original operator. No QZ-squared surrogate is assigned to GZ. Keep the original c112=699/1000; no larger polynomial-prefix complement is substituted.

Set J=GZ/c-QZ and a=VZ/c-BZ. Choose one rational two-column trial map T from the midpoint systems J T=a, then evaluate its complete matrix credit outward:

    Credit=a^*T+T^*a-T^*JT,
    Lower=AV-GR/c+Credit.                            (1)

For each retained coefficient vector x, use the ACTUAL trial ZTx and residual B_Vx-CZTx. Original inverse square completion gives

    <B_Vx,C^(-1)B_Vx>
      <=2<B_Vx,ZTx>-<ZTx,CZTx>
         +||B_Vx-CZTx||^2/c.

Expanding this one residual yields EXACTLY (1), including every cross-column term. Hence the exact original completed Schur restricted to V satisfies

    S_V>=Lower.                                     (2)

The midpoint solves are proposals only; no optimality claim substitutes for the outward matrix test. A positive diagonal for h and a positive diagonal for u would NOT prove (2) positive on their combinations. The full determinant is required and evaluated.

## 3. Actual result

The full lower block PASSES. The actual lower matrix is enclosed near

    [[ 1.373694800363044e-32, -1.437676369714094e-18 ],
     [-1.437676369714094e-18,  0.03678446793895774   ]].

Its rational determinant lower endpoint is strictly greater than 5e-34 (display 5.032394100746392e-34). Thus the nonzero mixed coupling is paid; this is more than two separate scalar positive tests. ALL combinations in V have positive ORIGINAL completed Schur energy.

The witness diagonal is sharper than CC8's >1.35e-32 bound because CC9 newly reconstructs the full retained source Gram rather than importing its old scalar sufficient-estimator baseline. The actual odd-source energy remains bounded and included. This does not alter CC8's historical certificate.

112 independent retained/native overlaps and six source/native symmetry audits pass. Twelve additional actual trial/action overlaps agree with CC8's independently repeated integrals. The source L2 errors are approximately 1.14670e-55, 3.65008e-58, 2.03191e-49 and 6.90009e-48 for witness, constant, degree 112 and degree 114 respectively. The certificate stores the complete mixed matrices and the SINGLE two-column rational lift.

## 4. Coercivity consequence if the mixed block passes

Let d be a positive lower determinant endpoint and t an upper trace endpoint of Lower. Since Lower is a positive 2x2 matrix, its smallest Euclidean-coordinate eigenvalue is at least d/t. The retained physical mass Gram has largest eigenvalue at most its trace, m_h+m_u, even though h and u are not orthogonal. Thus

    S_V>=tau physical retained mass,
    tau=d/[t(m_h+m_u)]>0.                           (3)

This is a lower bound, not an identification of a Rayleigh upper value with a spectral gap. The original complete 112-source bound and protected complement give

    ||Wv||_2^2<133||v||_2^2, v in V.

For a vector in the ENTIRE slice D_slice=V+F112, write it uniquely as Wv+z, z in F112. Exact square completion gives

    Q(Wv+z)=S_V(v)+Q(z),
    Q>=mu mass on D_slice,
    mu=min(tau/(2*133),c/2)>0.                      (4)

Using the imported original target Garding inequality Q>=E_log/10-26 mass, blend (4) to get

    Q>=mu/[10(mu+26)] E_log on D_slice.             (5)

D_slice has codimension 110 in the supported canonical domain: two independent original retained directions plus the whole F112 complement. This is an infinite-dimensional coercivity certificate on that slice, conditional on a passed block. It is NOT whole-domain positivity at 21/20. At most 110 original nonpositive spectral directions can remain, by min-max and the known compact-resolvent structure. This improves the protected-codimension bound; it does not say those directions exist.

The actual block passes, so the exact rational conversion gives

    tau>3.5e-33 on the retained plane,
    mu>1.3e-35 physical mass on the WHOLE infinite slice,
    canonical margin>5e-38 E_log on that slice.

Conservative displays are tau=3.532123325583611e-33, mu=1.327865911873538e-35 and canonical margin=5.107176584128992e-38. All constants come from lower determinant/upper trace, full retained mass and the original protected graph/complement bounds, not from finite trial Rayleigh upper levels.

## 5. NF67/NF68 interface and inference boundary

NF67 supplies the exact COMPLETE-source incoming-shell cost K^*(I-A_old)^(-1)K and a critical-output leakage target. It is read and preserved. CC9's four physical source reconstructions are ORIGINAL operator sources, not a selection of divisor rows, and are not identified with that source-orthogonal incoming shell. No numerical bound on NF67's leakage is claimed.

A passed slice supplies an improved protected-codimension input for NF67's critical-output dimension argument. Turning it into a whole incoming-shell cost still requires the complete original positive-source norm bound and actual critical correlations; neither is supplied by a positive 2x2 restriction alone. The original exact aperture Schur reaction and relative-loss nondivergence obligation remain open.

NF67's strict continuation criterion also requires an independently ORIGINAL-positive starting chart. CC9 does not establish that condition on the whole 21/20 domain. Its improved slice can be used as a protected-complement input when that additional condition is available; no unproved whole original gain below one is assumed here.

NF68 is also read and preserved. Its finite critical-output reaction Hcrit=Gcrit-L C_W^(-1)L^* acts on actual critical source-output coordinates and requires C_W>0 on the ENTIRE incoming source-orthogonal shell. A residual upper certificate must include all critical columns and the whole incoming residual Gram. CC9's physical two-retained matrix is not Hcrit; its complement trials do not supply NF68's incoming trial map, critical coordinates, complete residual, or whole low incoming gain bound. The improved protected slice is an input for further critical-dimension analysis, not a passed NF68 continuation gate.

All original prime thresholds preserve zero overlap at equality. Both signed poles and the complete original source identity remain intact. No positive eigenlevel is shifted to zero or relabeled original contact. These are the original unshifted coefficients and the same protected complement.

## 6. Validation and custody

Exact genuine mixed-matrix controls verify the full residual Gram identity and inverse upper bound, keeping all lift columns together. A positive-diagonal/negative-determinant control rejects separate scalar sign inference. Independent overlaps with CC8's trial/action and saved-witness cross quantities verify the repeated operator construction.

Twelve genuine coupled matrix-credit cases and twelve independent actual CC8 overlap audits pass. The determinant and physical/canonical conversion thresholds are checked by exact rational arithmetic. Analytic inverse-square, full-domain completion and min-max arguments are not Lean-certified.

No full target Schur sign, new whole aperture, original negative vector/contact, arithmetic nondivergence, global source gain, RH/F4, full transport or Lean result is claimed. Historical CC8 and concurrent NF67/NF68 blobs remain unchanged. Paused refs are untouched.
