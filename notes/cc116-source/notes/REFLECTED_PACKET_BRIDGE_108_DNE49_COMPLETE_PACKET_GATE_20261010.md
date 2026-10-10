# DNE49: complete retained packet and paid remaining trial pairings

## Result and scope

On the unchanged research branch, DNE49 extends the exact DNE48 packet to Z56=(T4*S,X[0:52]) in both parities. The original finite native matrices are positive by new paid rational 56-by-56 congruences. Independent exact chart checks prove rank 56 per parity after projection onto E112, hence a complete 112-dimensional retained coordinate chart. The 36 previously missing entries of the even trial-native coupling M are now paid using already certified DNE48 whole-action coordinates.

The independent audit passes **28,004 exact rational checks**. No new source integration was performed. The all-high certified rank stays **88**, with **24** uncovered retained directions. The original infinite F112 floor remains 647/1000, and the inherited common physical all-high guard remains 1e-37. Neither whole-aperture positivity nor RH is proved.

Mathematical parent: `514386d14dcb1dc1bb2d469bc82a728d8de4b12d` (DNE48). The live head and immutable parent custody were verified before continuation. All historical certificate files remain unchanged.

## Exact packet and finite native energy

The four scaled tested columns T4*S, the frozen projection J, and the full rational triangular U are unchanged from DNE32. All 52 normalized remainders are expanded exactly as

    X=(W-T4*K)*U, K=S*J.

The native border is the paid nonzero matrix

    (P_s-A_s*J)*U.

It is never replaced by zero. The upper-left 44-by-44 native block and first 44 polynomials coincide with the previous packet. The complete original native matrix uses A_s, this border, and the complete DNE32 congruence C52. A rational 56-by-56 congruence then proves strict positive Gershgorin margins independently for each parity. Decimal arithmetic selects the candidate congruence; exact outward interval arithmetic alone establishes positivity.

| Parity | Finite native coefficient floor, approximate | Retained chart rank | New source columns |
|---|---:|---:|---:|
| Even | 0.0123119954329451 | 56 | 12 |
| Odd | 0.015044535333378887 | 56 | 12 |

These floors concern the original finite native form before the inverse-response subtraction. They do not establish positivity of the enlarged packet coupled to F112.

The chart audit checks the exact nonsingular first-four-coordinate T4 minor, every entry of W's literal 52-by-52 identity minor, exact orthogonality of all four retained T4 projections against W, every lower-triangular zero and diagonal pivot of U, and nonzero scales. Therefore [T4*S,(W-T4*K)*U] is an invertible retained chart. Native positivity and retained chart rank are distinct claims, and both are checked.

## Paid remaining trial-native coupling

DNE48 supplies three exact physical high vectors Y0,Y1,Y2 and their whole-action coordinates at all 91 even indices 0,2,...,180. Every new X column has support inside these coordinates. For each of the twelve new native columns and each high trial, DNE49 evaluates

    M_ij=<X_i,L_original Y_j>=<P_F L_original X_i,Y_j>.

The exact interval dot product is enlarged by gamma_j times the certified physical norm upper of X_i, where gamma_j is DNE48's whole-source L2 error for Y_j. This pays the complete operator-action approximation. The first 44 rows agree exactly with the previously stored DNE48 unrounded trial-native pairing intervals. The new 12-by-3 block has maximum interval width approximately 2.184523436452555e-12. There is no sampled quadrature, reintegration of the old prefix, or evaluation of the actual infinite inverse.

The existing A, D and residual W=D-k*A are unchanged. The new M rows are now available for the eventual E=B-k*M once new B is integrated. Computing M alone does not supply B or G.

## Exact source ordering and missing correlations

The certificate contains full exact native columns once, plus source labels, trial columns and explicit native-to-source maps. This avoids duplicating large polynomial archives.

| Parity | Source order | Native-to-source map | Reused source size | Total source size | Missing upper entries |
|---|---|---|---:|---:|---:|
| Even | Z44, Y0,Y1,Y2, X40,...,X51 | 0:44 then 47:59 | 47 | 59 | 642 |
| Odd | Z44, X40,...,X51 | 0:56 | 44 | 56 | 606 |

The even native matrix is 56-by-56 even though its source matrix will be 59-by-59. Y0,Y1,Y2 are high trial columns, not retained dimensions. Source arrays must be extracted with the saved maps rather than by taking a leading 56-by-56 block.

Each missing pair (i,j), i<=j, is enumerated exactly; j is at least the corresponding reused source size. The 642 even entries split into 528 old-native/new-native, 36 trial/new-native, and 78 new/new. The odd 606 entries split into 528 old/new and 78 new/new. Total remaining source correlations: **1248**. The audit checks exact set equality and uniqueness of these manifests.

The next load-bearing step is to integrate these whole-source correlations with independent primary/replay enclosures, retaining the same source definition, endpoint logs, signed poles, all six active prime powers in both orientations, polynomial/log rounding, analytic remainder payments, and the subtraction of all 56 same-parity retained source coordinates. Copy the old even DNE48 47-by-47 and odd DNE44 44-by-44 paid prefixes unchanged. Then form the complete G and B, extend the DNE48 residual-response budget, and attempt full even/odd positivity. A failed sufficient budget would not show negativity of the original form.

## Verification and reproducibility

The producer reconstructs the full native packet and proposes congruences. The independent auditor reconstructs physical coefficients directly from W, K and U, rather than trusting the producer's materializer. It uses separate unrounded rational interval algebra for the native border and congruence, independently expands the four-by-four determinant by permutations, checks every paid M entry, and validates all source index maps and manifests. Inherited validation records and decoded certificate hashes authenticate dependencies. DNE48's stored artifact and helper hashes were checked against immutable parent custody; additional materialization helpers were compared with immutable parent file contents.

Reproduce from the repository root:

```sh
python scripts/certify_dne49_complete_packet_gate.py --output notes/data/RPB108_DNE49_COMPLETE_PACKET_GATE_20261010.json.gz.b64
python scripts/validate_dne49_complete_packet_gate.py notes/data/RPB108_DNE49_COMPLETE_PACKET_GATE_20261010.json.gz.b64 --output notes/data/RPB108_DNE49_COMPLETE_PACKET_VALIDATION_20261010.json
```

Both scripts compile. The final producer and independent audit completed; no computational jobs remain running. The initial internal triangular-minor assumption was replaced with a general exact determinant before successful certification. The published audit checks the general determinant independently. Certificate hashes refer to decoded JSON bytes; custody hashes refer to stored file bytes.
