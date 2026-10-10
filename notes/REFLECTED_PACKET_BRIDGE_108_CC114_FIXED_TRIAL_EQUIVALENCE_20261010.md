# RPB108 CC114 — fixed rational response and the updated DNE comparison

CC parent: CC113 `e6f57ad08a59000c79046b7cd48694b825d328ec`.
Read-only DNE48: `514386d14dcb1dc1bb2d469bc82a728d8de4b12d`.
Read-only Native NF58: `3a0233c71ba16eb2ca59947f32789ac5752485da`.
Definitions precede use in `docs/TERMINOLOGY_RPB108_CC114_FIXED_TRIAL_RESPONSE.md`.

**A fixed rational response trial reproduces CC113's complete 88-direction certificate without certifying a finite matrix inverse.** Both original 44-column matrices are positive at k=647/1000, with physical gaps above 1e-37 and the entire infinite F112 space included. No new source integrations are needed. Coverage stays 88, and 24 retained directions outside the packet remain open.

The method comparison has also changed: DNE48 has now adopted residual response and independently reached the same coverage. CC113's strict separation from the plain remaining-source criterion remains valid. No strict advantage over DNE48's new response method is established. With the same physical trial family, their formulas are algebraically equivalent after optimizing the rational trial.

## Exact equivalence on the original domain

Let L be the complete original high operator, L>=kI; f the complete packet high source; and Y the authenticated pure-high physical family. All operator-domain and source attachments are inherited from the CC113 dependency chain. Write

    Q = original packet native form,
    G = f*f,
    W = f*(L-k)Y,
    N = Y*L(L-k)Y/k.

CC113 authenticated all these signed matrices and proved N positive. For any exact rational matrix H with one row per trial column, set J=H/k and r=f-LYJ. The original residual identity and the floor imply

    f*L^-1 f = f*YJ + J*Y*f - J*Y*LYJ + r*L^-1 r
             <= f*YJ + J*Y*f - J*Y*LYJ + r*r/k.

Expanding every mixed term gives the finite lower bound

    S_H = Q-G/k + (WH+H*W*-H*NH)/k².

This is exactly DNE48's residual-response formula for the same physical Y. No finite inverse evaluation is required to accept S_H>0; even the positivity of N is unnecessary for this residual inequality itself. CC114 replays N positivity to authenticate the optimized comparison. Every mixed term remains in the full matrix.

When N>0, completion of the square gives

    W N^-1 W* - (WH+H*W*-H*NH)
      = (H-N^-1 W*)* N (H-N^-1 W*) >= 0.

Thus the optimized CC113 correction is the supremum of the fixed-trial corrections, attained at H=N^-1 W*. A numerical linear solve can propose H but supplies no sign evidence. A frozen rational H, paid with interval entries and a rational positive congruence, is sufficient. Negative or inaccurate trial credit is allowed; it merely weakens the bound. The saved exact scalar controls include the optimizer, imperfect, zero and negative-credit choices.

DNE48 uses three high trials; CC114 reuses CC113's eleven even and ten odd trials. Equal formulas do not imply equal bounds for distinct families. No claim that either family dominates the other is made.

## Fresh computation and arithmetic replay

The producer takes the authenticated CC113 complete signed response rows and original DNE44 packet Q/G, and the authenticated NF52 high native/source matrices. It reconstructs N, replays its rational positive certificate, and proposes H by a 160-digit decimal linear solve. It freezes H on denominator 10^100. Acceptance uses exact rational interval arithmetic, not the solve's precision or residual.

The producer forms WH and H*NH by matrix products. A separate replay uses the frozen H and congruence, reconstructing each credit entry directly as signed scalar sums over all trial indices. It proves the complete 44x44 lower matrices positive and reproduces or improves the producer's exact coefficient and physical floors. The two assembly paths share the existing interval primitives and proof routine; this is a distinct arithmetic replay, not an independently derived analytic source theorem or fresh source integration. Their last rational margins can differ because the entrywise assembly combines exact coefficients before interval multiplication. The replay checks floor domination rather than requiring byte equality of two differently associated interval expressions.

| Parity | Original packet columns | High trial columns | Physical gap lower, approximately |
| --- | ---: | ---: | ---: |
| Even | 44 | 11 | 2.582384837885281e-37 |
| Odd | 44 | 10 | 3.197279417949341e-33 |

Both exceed 1e-37. These slightly larger displayed bounds than CC113 reflect interval assembly and the chosen certificate; the exact fixed-trial matrix never exceeds the exact optimized matrix. The original packet mass, complete source trace, retained rank and span inclusion remain inherited from the authenticated CC113 full-packet certificate. The gap conversion is unchanged:

    min{d/[4(M+T/k²)],k/2}.

The producer completed in about 8.36 seconds on this run. This is local elapsed time, not a paired runtime benchmark or complexity claim. Both producer and replay evaluate **zero certified finite inverses**. A decimal solve used to select the trial remains part of proposal work.

## Recovered fronts and remaining work

DNE48 independently integrates 138 new even original high-trial source correlations in primary/replay archives and certifies its full even packet by frozen rational residual response. Its published source/response audits report 25,973 and 10,264 new exact checks. Those are recovered DNE reports, not fresh CC114 audit counts. Its common guard and retained coverage agree with CC113. Its complete trial-source archives and validators remain on the read-only DNE branch; the CC114 source snapshots preserve the explanatory note and published audit identities.

Native NF58 remains at an unresolved full joint lower matrix. Its frozen even target gains positively but spans zero; its previous odd target passes, followed by a new rejecting lower-bound witness. Those lower-bound statuses do not prove an original negative vector. NF58 is recovered for orientation only; no fresh NF58 analytic audit is claimed. Its original all-56-source frame differs from the computed Z44 packet. Neither its probe count nor its high trial count can be added to CC's retained rank.

The next coverage extension must address the twelve exterior retained columns per parity with their complete source correlations and mixed response entries. Rechecking old packet negativity or searching for another scalar floor is no longer the packet closure obligation. Fixed-trial residual certificates can reuse the paid high actions when those new correlations are supplied.

## Cost conclusion and limits

CC114 proves a concrete certificate simplification: a paid rational trial replaces certified finite inversion for this packet, preserving the result. It does not prove cheaper total computation than the plain remaining-source bound. Original source construction, all mixed correlations and dense positivity certification are still required. Nor does it prove strictness over DNE48's current criterion, which now uses the equivalent response mechanism.

Whole aperture 1.06, global first-contact exclusion, true infinite inverse evaluation, RH, F4 and Lean remain open. The highest whole-aperture anchor remains 1.05. No other branch is changed.

## Reproduction

From the repository root:

```sh
python scripts/certify_cc114_fixed_trial_response.py --output notes/data/RPB108_CC114_FIXED_TRIAL_RESPONSE_20261010.json
python scripts/certify_cc114_fixed_trial_response.py --replay notes/data/RPB108_CC114_FIXED_TRIAL_RESPONSE_20261010.json --output notes/data/RPB108_CC114_FIXED_TRIAL_REPLAY_20261010.json
```

Require both complete positive congruences, authenticated dependency hashes, replayed denominator positivity, identical frozen trials and congruences, replay floor domination and physical guard above 1e-37. No source integration is rerun by these commands.
