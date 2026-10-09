# CC62: original low-two/full-high leakage and an infinite restriction gap

Read [definitions](../docs/TERMINOLOGY_RPB108_LOW2_HIGH_LEAKAGE_CC62.md) first. This is a NEW original signed arithmetic certificate on a specified infinite-dimensional restriction at a=53/50. It does not certify the whole supported domain or the near-critical retained carrier.

## Native result

Let E2=span{e0,e1} and F112 be the physical complement of the entire original E112 carrier, with its canonical high form domain. The complete original Weil form obeys

    Q(h)>=1/100 ||h||_2²  for every h in E2+F112, at a=53/50.

The restriction contains EVERY canonical high mode, not just e112 through e115. It excludes the110 retained modes e2 through e111. In particular a complete original null cannot lie entirely in E2+F112; any null in the whole domain would have a nonzero component among the excluded retained modes. No assertion of orthogonality to E2 or identification of a critical eigenspace follows.

This fixed-restriction bound uses the actual source arithmetic and current high floor, without an old whole-aperture continuation gap. It is not uniform over aperture caps, over retained degree, or relative to the critical defect.

## NF23 recovered and replayed

Independent NF23 head612dd2696f8f9b423d1c898aaeda2b046fd93af0 closes the original arch-prime and arch-pole source cross integrals on e0/e1. Complete source-square intervals are

    .083661834381 < ||L e0||² < .083661834383,
    .338141181532 < ||L e1||² < .338141181534,
    <L e0,L e1>=0 by reflection.

These include the endpoint-log archimedean action, all six active prime powers in both orientations, both signed poles and every source-sector cross. NF23's older odd numerical NF22 diagnostic differed at about3e-12; NF23 explicitly labels it non-certifying. The new strict rational intervals, rather than that older diagnostic, supply this computation.

The NF23 producer was recovered with all three exact dependencies and ran UNMODIFIED. Its21 core fields, including all13 cell ledgers, match the published NF23 manifest EXACTLY. Both original NF22 exact producers also ran unmodified and reproduced their arch-square enclosures and Cauchy error bound. All four source-script SHA256 values match NF23's manifest. [Archived source manifest](data/RPB108_NF23_SOURCE_INPUT_CC62_20261009.json); [replay validation](data/RPB108_NF23_REPLAY_CC62_20261009.json). The archived manifest hash is134deb5db09b2bd720284c7f4e2a2fca5918982a307eb67267ecf3586e6810de. No floating-point quadrature contributes a bound.

## Complete retained projection and actual high leakage

For normalized e_j, j=0 or1, genuine physical source representation gives

    P_low,jj = ||P_F112 L e_j||²
             = ||L e_j||²-sum_(i in E112, same parity) |Q(e_i,e_j)|².

The sum removes ALL56 retained coordinates of that parity, not only the e_j diagonal. Other-parity coordinates vanish exactly by reflection. The complete source square is NF23's genuine original square; the112 retained projection records come from the authenticated NF17 original signed E112 source archive, raw SHA256 f69019a895cd675e304989cbb8209c90f033264e0aef589d4b1aa3be09cf4c81. All448 arch/prime/pole/full component intervals and the full-interval compatibility checks pass. Signed coefficients are squared with proper interval handling, including intervals crossing zero.

| Quantity (approximate display only) | Even e0 | Odd e1 |
|---|---:|---:|
| Original retained diagonal A_j=Q(e_j,e_j) | .0401520842754 | .1440116728563 |
| Entire retained source projection square | .0791524577056 | .3257399071152 |
| Complete F112 source square P_low,jj | .004509376677 | .012401274418 |
| P_low,jj/(kappa A_j) | .542547885 | .416004739 |

The exact outward bounds certify

    0<P_low,even < (543/1000) kappa A_even,
    0<P_low,odd  < (417/1000) kappa A_odd,
    kappa=207/1000.

This is UNCOMPENSATED low-two high leakage. It is not NF21's compensated56-column P2 or the complete58-column source Gram. The subtraction is well-conditioned enough here: the NF23 square widths about10^-12 are much smaller than the actual gate margins. CC58's cancellation warnings still apply to the much smaller near-critical retained directions.

## Full-high Schur and physical gap

On the entire F112, C_full>=kappa I. With B_low the genuine mixed source of E2 into F112, its true full inverse response satisfies

    G_low=B_low*C_full^{-1}B_low <=P_low/kappa.

Therefore its complete corrected retained signs obey

    A_even-G_even >(457/1000) A_even,
    A_odd-G_odd   >(583/1000) A_odd.

These inequalities upper-bound the COMPLETE infinite high response. They do not merely evaluate a finite measured high block.

For a complex low x in E2 and a canonical high y in F112, set u=A_low(x,x) and v=kappa||y||². Reflection diagonalizes the two parity source Grams. Since543/1000<9/16, the mixed pairing is bounded by

    |Q(x,y)| <=sqrt(P_low(x,x))||y|| <(3/4)sqrt(u v).

Hence

    Q(x+y)>=u+v-(3/2)sqrt(u v)>=(1/4)(u+v).

The native diagonal lower enclosures both exceed1/25, and kappa>1/25. Thus u+v>=(1/25)(||x||²+||y||²), giving Q(h)>=1/100||h||². Finite-polynomial operator-domain source representation and canonical high coercivity are existing dependencies; no general endpoint regularity or continuity route is restarted.

## Controls and limits

Three exact abstract crossing models have high c=1, mixed b=1/4, low a=b²+epsilon and corrected sign epsilon at epsilon=1/100,0,-1/100. Three genuine positive ground-level models use a=mu+b²/(1-mu), with mu=10^-40,1/100,1/20. Whole physical shifts create the null and retained-only shifts miss it. ALL these abstract controls FAIL the newly certified native leakage hypothesis P<kappa A. They are therefore excluded by the hypothesis, not contradictory to the restricted gap. They are not original Weil crossings or positive eigenlevels.

The remaining110 retained modes can couple to this certified infinite restriction. Positivity on this restriction and positivity of E112 separately do not settle their mixed complete Schur sign. The actual rational near-critical NF18/NF19 directions and full compensated collective Gram remain pending; a directional source test will be a probe rather than a whole-carrier certificate. CC59/CC60 correlation improvements and CC61 blind-direction stopping rules remain available if the physical sufficient estimator fails.

## Verification and standing

[Exact consumer](../scripts/certify_native_low2_high_leakage_cc62.py), [certificate](data/RPB108_LOW2_HIGH_LEAKAGE_CC62_CERTIFICATE_20261009.json), [custody](data/RPB108_LOW2_HIGH_LEAKAGE_CC62_CUSTODY_20261009.json). Reproduction inputs are the authenticated original E112 archive and archived NF23 source manifest; the consumer rejects incorrect hashes. Its published intervals round outward to10^-45. The native112 projection records and448 component checks, both full-high gates, physical-gap constants, three crossings and three positive-level controls pass.

Whole-domain positivity remains certified through21/20. Complete target53/50 positivity, cap-uniform old-gap-independent near-critical leakage, uniform defect-relative critical frame, actual whole-domain contact exclusion, RH/F4, full transport and Lean remain open. No complete-Weil-identity nonimplication is claimed. Preserve concurrent handoffs, historical wording and paused fronts.
