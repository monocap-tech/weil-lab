# CC70 — finite collective positivity and the high-loading boundary

Definitions: docs/TERMINOLOGY_RPB108_RETAINED_HIGH_LOADING_CC70.md. Integration parent: CC69, 43661c39489f33f7fb0ad45c1573ff12a0973eeb. Read-only producer head: NF27, a446275d4ba9a6c71599c310c35e81d2e439de95.

## Native finite restriction

The unmodified NF27 producer was freshly replayed. Its complete certificate matches the producer certificate byte for byte. It uses authenticated original signed E112 source entries, rational congruence/Gershgorin positivity, a paid Neumann inverse enclosure, physical trace bounds, and a physical source-error ball for the tiny NF26 high correction. Decimal arithmetic selects rational preconditioners only.

For each unchanged retained seed x, W=E intersect x-perp has dimension 55. NF27 certifies the entire A_W as positive, not just selected coordinates. The physical native complement gaps exceed 5.80e-28 even and 6.16e-25 odd. Its complete finite retained reaction divided by the corrected energy lies in (0.0053911,0.0053913) even and (0.0085503,0.0085504) odd. Subtracting that reaction leaves positive energy. Thus the original form is positive on the finite span(v)+W in each parity. Exact parity gives a positive 112-dimensional finite lifted restriction, with polynomial support through degree 180.

The dimension 112 does not mean that the entire original form is positive. Infinite high elimination also changes both A_W and the mixed seed coupling. NF27's directional-score-minus-finite-reaction is expressly not a collective Schur bound.

## A quantitative joint gate

Let theta bound the floor-normalized collective source loading on W, p=||r||^2/(kappa q), and t=R/q. Eliminating W first gives a high form at least kappa(1-theta) and a corrected high source r-B A_W^-1 c. By the energy-normalized source bound,

    ||r-B A_W^-1 c|| <= sqrt(kappa q)*(sqrt(p)+sqrt(theta*t)).

Consequently the sufficient positivity test is

    (sqrt(p)+sqrt(theta*t))^2 < (1-theta)*(1-t),
    equivalently p+t+theta+2sqrt(p*t*theta) < 1.

The same proof after whitening by the true high form C replaces theta by nu and p by the true seed response ratio or any upper bound for it. The latter may be bounded by the already certified floor-based p. All displayed numerical targets below are hypothetical sufficient bounds, not established native loading estimates.

With the complete native upper bounds on p and t, theta<=1/100 even or theta<=4/25 odd would suffice. Exact rational square-root enclosures certify positive slack. Approximate limiting robust thresholds are 0.0150464 even and 0.1647264 odd; these display values are not proof inputs.

## Original arithmetic rejects direct norm assembly

We reconstruct the exact NF27 constrained inverse and its proof, then use all 56 original native pairings against the FIRST high mode e112 even or e113 odd. Their retained constrained quadratic reaction gives

    theta_even > 3.3322559080,
    theta_odd  > 3.1078539982.

These are lower bounds for complete collective loading, derived from one high coordinate. They already exceed one. Hence no completion of the missing source Gram can make the unchanged raw-W scalar-floor gate pass. This rejects this specific estimate, not the original form.

Using the authenticated native high diagonal as well, the high variational principle gives <z,C^-1 z>>=|<e_h,z>|^2/Q(e_h). Applied to the same complete constrained retained reaction, it yields

    nu_even > 0.1998651533,
    nu_odd  > 0.1896095485.

Even these true-response loading lower bounds exceed what the robust joint gate permits when it retains NF26's current floor-based seed-response upper bound and NF27's current finite-reaction upper bound. Exact rational comparisons reject that unchanged robust bound in both parities. This does not evaluate the true seed response: a substantially sharper seed bound, signed mixed cancellation, or different source-aware retained lifts can change the conclusion of a sufficient test.

Thus simply computing more raw-W source coordinates or replacing its floor norm by a true-response loading upper bound cannot close this particular robust gate with the current seed estimate. We need actual signed collective response information, stronger seed response control, or retained background lifts whose original finite form and residual sources are recertified together.

The exact collective interface remains M_W=A_W-B* C^-1 B and d=c-B* C^-1 r: certify M_W>0 and S_seed-d* M_W^-1 d>0. This is the load-bearing assembly goal; positivity of the native A_W alone does not meet it.

## Crossing and positive-level controls

For the exact three-by-three matrix with diagonal 1, seed-to-retained coupling 1/3, seed-to-high coupling 1/3, and retained-to-high coupling -s, the seed high Schur score is 8/9 and finite reaction is 1/9. Their difference stays 7/9 while the determinant is 1-2/9-s^2-2s/9. At s=7/9 it has a genuine null; at s=7/9 plus or minus 1/100 it has negative or positive whole sign. All two-block controls stay positive. This realizes exactly the robust sign boundary and shows why subtracting separate reaction estimates is insufficient.

The crossing matrix is positive semidefinite with rank two. Three genuine whole-mass shifts (1/1000,1/10,2) have those exact positive ground levels. The controls concern this specified three-block estimator packet, not complete Weil identities or actual Weil countermodels.

## Reproduction and scope

```sh
python3 scripts/certify_native_retained_coupling_nf27_106.py notes/data/RPB108_NF24_COMPENSATED_SOURCE_TARGETS_20261009.json notes/data/RPB108_NF26_SOURCE_INPUT_CC69_20261009.json INPUT_DIR/native112_N720_K620.json.gz --output /tmp/nf27_replay.json
python3 scripts/certify_retained_high_loading_cc70.py notes/data/RPB108_NF24_COMPENSATED_SOURCE_TARGETS_20261009.json notes/data/RPB108_NF26_SOURCE_INPUT_CC69_20261009.json /tmp/nf27_replay.json INPUT_DIR/native112_N720_K620.json.gz INPUT_DIR/native_boundary_columns_112_113.json.gz --output /tmp/cc70_loading.json
```

All five inputs are authenticated by SHA-256, including both decompressed original native archives. The constrained-inverse proof is independently reproduced and compared exactly to NF27. Complete rational intervals and hypothetical sufficient slacks are in the CC70 certificate; replay custody is separate.

Whole-domain anchor remains 21/20 with margin 1/(3*10^63). CC62's E2+F112 gap and NF26's two-seed Schur null exclusion remain. NF27 adds finite lifted positivity, not a new global null exclusion. Whole 53/50 positivity, collective infinite-high-corrected retained positivity, uniform defect-relative frame, all-cap old-gap-independent leakage, global actual null exclusion, RH/F4, full transport and Lean remain open. No nonimplication from complete original Weil identities is claimed. Historical wording and paused fronts are unchanged.
