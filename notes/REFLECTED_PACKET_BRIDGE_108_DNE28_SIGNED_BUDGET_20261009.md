# RPB108 — DNE28: stronger signed four-column source budgets

Read the additive [DNE28 terminology](../docs/TERMINOLOGY_RPB108_DNE28_SIGNED_BUDGET.md) before the definitions below.
Parent DNE27: 3b5c5cb3a6db62c0fc7745820dc42a0d3d195c16.
Read-only Phase NF41: 4d2a5d7d3857854677a223ca38d03b13358f40e9.
Read-only Coupled CC79: dd93e5cc7d003d44cdc240c5710f4c253dc1346f.
Only research/rpb108-direct-null-exclusion is written.

## Result

The unchanged original DNE23 four-column frames admit much stronger complete source contraction credits. The improvement uses the complete signed native and source matrices directly, with a coherent payment for the uncomputed low-source row.

| Paid quantity | Even | Odd |
| --- | ---: | ---: |
| Frozen rational source Young parameter tau | 381/1000 | 173/500 |
| DNE27 four-column credit | 0.00316 | 0.00962 |
| DNE28 four-column credit c | 4/125 = 0.032 | 41/500 = 0.082 |
| Credit improvement | >10.12 times | >8.52 times |
| Scaled native lower Q4 | >0.04 I | >0.14 I |
| Physical diagonal lower ell | (10^-6,0.2,0.2,0.2) | (10^-6,0.07,0.07,0.07) |
| Full-high physical gap, strict lower | >1.96059e-35 | >6.86207e-32 |

The common reported physical guard is now

    Q(h)>=1.9*10^-35 ||h||^2, h in Z8+F112.

This is 4.75 times DNE27's reported guard 4*10^-36. Eight retained directions remain jointly certified and 104 remain outside their span. No direction is added. The increased source credits are conditional budgets for a remaining test, not a passing remaining Gram or whole-domain positivity certificate.

## Coherent majorant pays every missing low-source cross

Let r0 be the original complete low source, with ||r0||^2<=P0, and let R3 be the three original source columns from NF32. For every complex low coefficient a and three-coordinate z, Young's exact square identity gives

    ||a r0+R3 z||^2
      <=(1+1/tau)P0 |a|^2+(1+tau)z*Gamma3 z.

Thus Gamma4<=D_tau=diag((1+1/tau)P0,(1+tau)Gamma3). The difference before replacing the low norm by P0 is ||a r0-tau R3 z||^2/tau. This treats the unknown low row as one coherent source family. The zero border of D_tau does not assign zero values to the original low-source crosses. Complete signed entries of Gamma3 are retained.

The original native Q4 is fully enclosed: CC62 supplies its low diagonal, DNE23 supplies all three original low/lift pairings, and NF32 supplies its signed three-column block. The producer intersects the two authenticated symmetric enclosures for each three-block entry, checking overlap, then applies DNE23's exact rational congruence scales.

The frozen rational choices above give

    H=S[(kappa-c)Q4-D_tau]S>0, kappa=11/25.

All four outward interval LDL pivot lower endpoints are positive in each parity. Therefore the entire original four-column source satisfies

    Gamma4<=D_tau<(kappa-c)Q4.

This direct comparison preserves information discarded by DNE27's diagonal lower form and absolute native row comparison. It does not reuse a three-column credit as a four-column credit: the low source and its full native border are paid in the same matrix inequality.

A floating midpoint calculation was used only to select candidate rational tau and c. These constants are frozen before certification. Every load-bearing comparison is exact rational and outward; no claim of optimality over tau, source completions or continuous parameters is made.

## Physical gap with all original high vectors

A separate signed matrix comparison pays

    S[Q4-D_tau/kappa]S>diag(ell).

This is not inferred from the scalar credit. Its four outward LDL pivots are checked independently. Since Gamma4<=D_tau, it also bounds the original coarse source matrix Q4-Gamma4/kappa.

DNE27's authenticated inverse-completed physical column bounds b_i are reused without weakening their source or norm payments. The same original high floor C>=kappa I gives, by square completion and weighted Cauchy,

    physical_gap >= [sum_i (s_i b_i)^2/ell_i+1/kappa]^-1,
    s_0=1.

The bounds in the result table follow. Both exceed DNE27's corresponding bounds. This pays the nonorthogonal physical frame and every original infinite high correction. It does not equate coordinate energy with physical mass or evaluate the actual infinite inverse. Exact reflection parity combines the sectors.

As a separate native comparison, S Q4 S>q I is paid at q=1/25 even and 7/50 odd. All three matrix comparisons have strictly positive rational pivots.

## Larger conditional remaining allowance

DNE25's source transport theorem now uses c=0.032 even and c=0.082 odd on this same frame. After exact native energy orthogonalization, the complete inequality

    c B_Y-Gamma_Y>0

would imply whole 1.06 positivity. This condition itself forces B_Y>0 because Gamma_Y is a Gram. It still requires the full signed remaining source Gram, rather than diagonal or selected-window information.

For a frozen rational remainder, the inherited alternative is r+kappa epsilon<c, where r bounds the full normalized remaining source Gram and epsilon pays the native border dual square. One conservative allocation is:

| Allowance | Even | Odd |
| --- | ---: | ---: |
| r=c/2 | 0.016 | 0.041 |
| epsilon=c/(4 kappa) | 1/55 | 41/880 |
| Unused credit c-r-kappa epsilon | 0.008 | 0.0205 |

These are allowances only. No remaining energy orthogonalization, native border dual square or complete remaining source Gram is computed here. DNE24's exact 104-dimensional null reduction is unchanged.

## Independent verification and custody

Primary and replay consumers use outward interval decimal grids of 80 and 100 digits. Each passes 30 explicitly counted certificate assertions, with additional interval ordering, overlap and division guards. Replay matrix boxes lie inside the primary boxes; the frozen credits, physical diagonals and resulting physical gaps agree exactly. The high-completed masses remain the paid DNE27 inputs in both runs.

The validator imports no producer code. It independently reconstructs the input matrices and source majorants with exact fractions, checks outward containment, and tests all symmetric matrix-box vertices. Each of the six four-by-four boxes has 1024 vertices: source credit, native identity and physical diagonal comparisons in each parity. Every vertex has four strictly positive exact leading determinants. Matrix convexity therefore certifies every interior matrix, without treating uncertain entries as statistically independent.

Validation passes 25,532 rational checks, including 24,576 vertex leading-minor checks, 162 exact coherent source Young controls with nonzero signed low-source crosses, and 486 physical completion controls. Three genuine full-block positive/null/negative crossings and three whole-physical-mass positive-level controls also pass. These controls are abstract examples, not original Weil countermodels. Python syntax checks pass.

All five load-bearing input hashes are pinned and their local bytes match the corresponding files at the DNE27 parent. No new original source integration or source producer replay is claimed. This is an outward computational matrix certificate combined with the inherited original-source, high-floor and closed-form arguments; it is not a Lean proof.

## Current-head interface and limits

Phase has advanced from NF40 to NF41. NF41 certifies signed boundary/source crosses and excludes NF40's specific zero-coupling extension. A different fixed-cross extension still has zero joined inverse improvement, so the actual defect-source response coupling remains its frontier. DNE28 records this update but does not import that separate packet into the unchanged DNE23 frame or claim an actual response gain from it. Coupled remains CC79; both source branches are read only.

Whole 1.06 positivity, the complete remaining 104-dimensional reaction, exact unit-response exclusion, all-aperture continuation, RH/F4/full transport and Lean remain open. Historical documents are preserved additively.

## Reproduction

```sh
python3 scripts/certify_dne28_signed_budget.py notes/data/RPB108_DNE23_EIGHT_DIRECTION_CERTIFICATE_20261009.json notes/data/RPB108_DNE18_CC62_INPUT_20261009.json notes/data/RPB108_DNE22_NF32_EVEN_INPUT_20261009.json notes/data/RPB108_DNE22_NF32_ODD_INPUT_20261009.json notes/data/RPB108_DNE27_COHERENT_BUDGET_CERTIFICATE_20261009.json --output /tmp/dne28.json
```

Replay with --digits 100 and a second output path. The independent validator accepts the same five inputs followed by primary, replay and validation output paths. Custody records source/output hashes and pinned heads.
