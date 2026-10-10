# RPB108 CC115 — correct the signed-response floor binding; freeze the next exterior packet

Parent CC114: `5d625ef958501d7b8f84a295d279d86feef03f25`.
Read-only DNE48: `514386d14dcb1dc1bb2d469bc82a728d8de4b12d`.
Read-only Native NF58: `3a0233c71ba16eb2ca59947f32789ac5752485da`.
Definitions are registered in `docs/TERMINOLOGY_RPB108_CC115_EXTERIOR_COLUMN.md`.
All prior files remain historical and immutable.

**CC115 repairs a real floor-binding error in the CC113/CC114 647/1000 calculations.** Fresh reconstruction and entrywise replay certify the correct full44 response matrices in both parities, without certified finite inversion. Coverage remains88 retained directions plus the complete infinite F112 space, and the physical guard remains greater than1e-37. The original method conclusion survives: response is strictly stronger collectively than the plain criterion. The next45-column packets are frozen and preserve the old44 literally, but their new source computations did not finish; no90-direction upgrade is claimed.

## The error and its precise scope

CC112's `known_signed_response_cross_part` was formed at k0=603/1000. CC113's consumer reused this fixed part even when its command-line floor was changed to647/1000. It added the new G(v,Y) row correctly, but did not rebuild the other floor-dependent native terms. CC114 inherited the resulting647 rows. Their saved647 response credits, positive margins and numerical physical gaps therefore were not valid at their stated floor.

CC113's603/1000 response calculation has no such mismatch. Its certificate remains applicable because the certified original high floor647/1000 is at least603/1000. The source integrations, original packet Q/G, exact physical transport, retained ranks, high-floor validation, plain negative trial at647/1000, and original source/domain attachments are unaffected. DNE48's separate residual-response certificate is also unaffected by this CC error.

This note additively supersedes the CC113 and CC114647 response-credit guarantees and their numerical gap values. It does not rewrite their historical records or treat the old passing statuses as proof premises for the corrected matrices.

## Rebuild every signed row at the actual floor

For the exact physical identity

    Z44 = ZNative C + Y D + v t,

let BN/SN be the authenticated complete Native/high native/source pairings, QY/GY the high native/source Grams, and qv/gv the paid native/source v/Y rows. At the actual chosen k, the complete signed row matrix is

    W(k) = C*(SN-k BN) + D*(GY-k QY) + t*(gv-k qv).

Here the stars on C and D mean transpose, consistent with their saved column transport matrices. The formula retains every native term and every signed mixed entry. In particular, the correction to using the old k0 rows is

    W(k)-W(k0) = -(k-k0)[C*BN + D*QY + t*qv].

`cc115_response_transport.py` reconstructs the complete formula from its authenticated original inputs. The producer and replay both bind the saved signed rows to647/1000 explicitly. They authenticate CC112 transport against the unaffected CC113603 certificate and the v/Y source replay against that same valid source custody chain.

The corrected certificate freezes a rational H chosen by a decimal linear solve, and proves the entire44-column lower matrix

    Q-G/k + [WH+H*W*-H*NH]/k² > 0,
    N = GY/k-QY.

There is no certified finite inverse evaluation. The source/domain and residual-response identity are inherited; the signed-row reconstruction and positive rational congruences are fresh. Denominator positivity is replayed. The distinct entrywise arithmetic replay uses the frozen H and congruence, reassembles all credit entries as signed scalar sums, and reproduces or improves the producer's exact coefficient and physical floors. This shares interval primitives and proof code; it is not a new independent analytic source construction.

| Parity | Corrected coefficient floor, approximately | Corrected physical gap, approximately |
| --- | ---: | ---: |
| Even | 0.009175905019458589 | 2.293478437517513e-37 |
| Odd | 0.011771487983797823 | 2.9423981475675048e-33 |

The physical conversion remains min{d/[4(M+T/k²)],k/2}, with actual original packet mass and complete source trace. Both gaps exceed1e-37. Rank44 per parity and prior span inclusion follow from the unchanged exact physical transport and packet rank proof; no ranks from different frames are added.

At647/1000 the original plain even trial is still certified negative, while the corrected complete response matrix is positive. Thus the genuine same-floor collective separation is now supported by corrected data. DNE48 has independently adopted the equivalent response mechanism; no strict advantage over its new method or general total-cost dominance is asserted. The fixed-trial certificate still removes certified finite inversion from acceptance.

## Next exterior packet: prepared, not certified

The physical packets are stored as lossless deterministic gzip/base64 archives; their decoded bytes and original44 prefix remain authenticated. The new materializer freezes Z45=(T4*S,X[0:41]) in both parities. It verifies literal preservation of all44 physical columns and of the complete44x44 native prefix. X40 is the first of the twelve exterior retained directions per parity. An exact transport routine is prepared to verify its retained rank45 and recover its signed response row from the already-paid Native, Y and v data.

The planned new analytic work is44 source correlations against X40 and one new diagonal per parity; repeated old diagonals provide norm and compatibility controls. The producer includes original arch/pole actions, all six active prime powers in both orientations, endpoint logs and all56 retained projections. Primary settings are order360/precision760, replay400/800. The old44 source block will remain literal in the merged consumer. All new mixed response terms must be paid before any nested coverage upgrade.

Four source runs were launched. A compute-service interruption ended them during profile construction, before completed source Gram certificates or a complete first panel checkpoint. Their partial logs are not source evidence, and no fresh exterior source pairing is certified in this milestone. The prepared producer now saves each physical source profile separately with packet, column, helper, order, precision and producer hashes; completed panel checkpoints remain bound to the same computation. This supports faithful resume if the connection is interrupted again. This resume path has been added and compiled, but no successful resumed source integration is claimed here.

The exterior source validator and45-column response consumer are preparation scripts, not passing certificates. Their source files and frozen physical packets are published so the next step is concrete and reproducible. There are still24 uncovered retained directions.

## Reproduction of the completed correction

```sh
python scripts/certify_cc115_corrected_floor_response.py --output notes/data/RPB108_CC115_CORRECTED_647_RESPONSE_20261010.json
python scripts/certify_cc115_corrected_floor_response.py --replay notes/data/RPB108_CC115_CORRECTED_647_RESPONSE_20261010.json --output notes/data/RPB108_CC115_CORRECTED_647_REPLAY_20261010.json
```

Require authenticated source/transport hashes, explicit647 row binding, both full44 positive congruences, identical frozen trials and congruences, replay floor domination and both physical gaps above1e-37.

## Reproduction of the pending extension

Run each parity with the corresponding output names:

```sh
DNE16_ORDER=360 DNE16_PRECISION=760 python scripts/certify_cc115_exterior_source_star.py even --output notes/data/RPB108_CC115_EVEN_SOURCE_PRIMARY_20261010.json
DNE16_ORDER=400 DNE16_PRECISION=800 python scripts/certify_cc115_exterior_source_star.py even --output notes/data/RPB108_CC115_EVEN_SOURCE_REPLAY_20261010.json
```

Repeat for odd. Only after all four finish, run `validate_cc115_exterior_source_star.py` with an output named `notes/data/RPB108_CC115_EXTERIOR_SOURCE_AUDIT_20261010.json`, then the prepared `certify_cc115_exterior_response.py` producer and its `--replay` route. A failed or unresolved full45 gate is not a coverage upgrade. No pending output file is included as a completed certificate here.

Whole1.06, global first-contact exclusion, true infinite inverse evaluation, RH, F4 and Lean remain open. The highest whole-aperture anchor remains1.05. Only the CC branch is written.
