# DNE51: exhaust the old even trial space and prepare a genuine extension

Parent: DNE50 `3c61708f807b42ddffcff7d0a8516ea6a9e45cf1`.
Branch: `research/rpb108-direct-null-exclusion`.
Definitions were registered before computation in
`docs/TERMINOLOGY_RPB108_DNE51_RESPONSE_EXTENSION.md`.

The independent audit passes **18,277 exact rational checks**. The original
positivity state remains **109 retained directions plus the entire infinite
F112 space**, with three retained directions uncovered, at a=53/50. The
actual high floor remains 647/1000 and DNE50's common physical guard 1e-39
remains valid. No new original positivity or source integration is claimed.

## A route-wide even obstruction

Use the complete original source Grams from DNE50, with its explicit
native-to-source map, and the existing three even physical high trials Y.
For a scalar comparison parameter t define

    E(t)=B-t*M, W(t)=D-t*A,
    H_J(t)=t*N-G+E(t)*J+J^*E(t)^*-J^*W(t)*J.

When W(t)>0, completing the square gives

    H_J(t)=H_opt(t)-(J-W(t)^(-1)E(t)^*)^*
                          W(t)(J-W(t)^(-1)E(t)^*),
    H_opt(t)=t*N-G+E(t)W(t)^(-1)E(t)^*.

Therefore a negative quadratic trial of H_opt excludes **every coefficient
matrix J in this fixed trial space**, rather than merely DNE50's saved J.
The finite 3-by-3 comparison inverse here is not the original infinite high
inverse. W positivity and the trial enclosures are certified by exact
outward interval arithmetic.

| Scalar parameter t | Certified optimal even trial upper, approximate | Role |
| --- | ---: | --- |
| 647/1000 | -0.0282698542471 | Current original high floor |
| 669/1000 | -0.0122866524029 | Optimistic parameter above the inherited shell ceiling |
| 69/100 | -0.0000264025447544 | Strict necessary threshold for this trial comparison |
| 691/1000 | Full 56-column paid budget positive | Hypothetical sufficient parameter only |

At t=691/1000 a rational 3-by-56 J and a full rational interval congruence
certify H_J>0. Thus the fixed even trial comparison's transition is bracketed
between **0.690 and 0.691**. Neither endpoint has been proved to be a lower
floor for the original high operator. The bracket is a statement about
the comparison's required scalar input, not about the actual operator.

For any fixed J, H_J(t)/t equals the finite native residual expression minus
the exact residual-source Gram divided by t. The residual Gram is positive
semidefinite, so this expression increases with t. The obstruction at .690
therefore also excludes every smaller positive scalar parameter. DNE47's
fixed-F112 positive-region shell/global-prime-norm mechanism has ceiling
approximately .668418601929; even its optimistic best input cannot close
this complete even comparison using the old trial space.

This does not bound the actual high floor from above, exclude another high
floor theorem, or identify an original negative or null direction.

## Packet-tail recycling cannot enlarge the even trial space

All 56 retained even packet columns have physical high parts lying exactly
in the existing three-dimensional Y span. The certificate saves a rational
56-by-3 chart. The independent auditor reconstructs each full physical
high tail from DNE49's exact packet and checks every coefficient identity.
This reflects the original construction X=(W-T4*K)*U, where raw W lies
in the retained space and the high part comes from the tested T4 columns.

Consequently selecting additional high tails of this same retained packet,
or recombining them, supplies no new physical trial directions. Such a
selection cannot repair the all-J obstruction above.

## Genuine trial extension and exact source manifest

The proposed extension changes the physical trial space:

| Parity | Existing high trials | New exact trials | Total trial rank | New upper source correlations |
| --- | ---: | --- | ---: | ---: |
| Even | 3 | Physical Legendre e112,e114,e116 | 6 | 183 |
| Odd | 0 | Normalized high parts of tested packet columns 1,2,3 | 3 | 174 |

Both full physical trial Grams have independently checked positive rational
congruences. Every vector lies exactly in F112 with the correct parity.
The three even low high modes are independent of the inherited Y span.
The odd tails have rational normalizations paid against their exact masses.
No source-action approximation is used to prove these geometric claims.

Preserve DNE50's even 59-by-59 and odd 56-by-56 complete source matrices
literally. Append three sources in each parity. The certificate enumerates
all 183 even and 174 odd missing upper pairs, with no duplicates or omitted
old/new or new/new entries. Total next source cost: **357 correlations**
per primary or replay run. This is an entry count, not a runtime prediction.

The old trial geometry, complete source correlations, and original high
floor are reusable. The newly proposed physical trial vectors have **no
certified original source actions, native pairings, or response credit yet**.
Their usefulness is not established by their physical independence.

## Next computation

Integrate the six new original actions with the same complete endpoint-log,
regular-kernel, signed-pole, and six-prime-power engine as DNE50. Use separate
N360/P600 and N400/P620 runs; retain all old paid prefixes unchanged. Pay
analytic source error, polynomial/log rounding, every full physical Gram,
and all 56 same-parity retained projections.

For each new action retain source coordinates through degree180. These
pay original pairings against the entire retained packet and all trial
vectors. The even full M becomes 56-by-6 and A becomes 6-by-6; the odd M is
56-by-3 and A is 3-by-3. In addition to the 357 projected-source correlations,
the new native pairings comprise 168 new M entries per parity and 15 even
plus 6 odd new upper A entries. Preserve the already paid even M and A
blocks. Independently audit all pairings before forming E, W and credits.

Attempt the complete 56-by-56 response budget in each parity at the actual
floor .647. All mixed terms must be paid; credits on the three unresolved
comparison diagonals alone do not establish positivity. The new frame may
still fail, in which case its failure remains a comparison result.

## Reproduction and verification

```sh
python scripts/certify_dne51_response_extension.py --output notes/data/RPB108_DNE51_RESPONSE_EXTENSION_20261010.json.gz.b64
python scripts/validate_dne51_response_extension.py notes/data/RPB108_DNE51_RESPONSE_EXTENSION_20261010.json.gz.b64 --output notes/data/RPB108_DNE51_RESPONSE_EXTENSION_VALIDATION_20261010.json
```

Both scripts compile and the producer and auditor finished. There are no
unfinished computational jobs. The auditor uses unrounded rational interval
algebra, independently checks finite inverse trials by both adjugate and
LDL calculations, verifies full congruences and physical coefficient charts,
and checks positive-Schur and mixed-coupling countercontrols. Inherited
audits are authenticated by their decoded hashes; their old counts are
not counted as new checks. Custody records hashes of stored bytes separately.

Historical DNE50 artifacts remain unchanged. Whole-aperture positivity at
1.06, global first-contact exclusion, RH and Lean remain open.
