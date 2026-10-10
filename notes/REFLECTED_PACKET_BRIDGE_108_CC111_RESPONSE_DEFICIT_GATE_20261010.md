# RPB108 — CC111: reduce the same-frame response test to three deficit coordinates

Parent: CC110, `9c66aec88a55cee9dfa6a9e1c699dc280e9ed799`.
Read-only DNE: `bb7220c07aa66c2fea00bbc36452a59130ee3fb1`.
Read-only Native: `29cd9381adeb08a9093b74e1ec487051d68e956b`.
Definitions: `docs/TERMINOLOGY_RPB108_CC111_RESPONSE_DEFICIT_GATE.md`.

CC111 produces a paid response acceptance gate in the actual original Z44 frame at k=603/1000. The plain deficit gate is rigorously negative definite in two even coordinates and one odd coordinate. This isolates the full collective test without discarding mixed correlations. Actual response crosses have not yet been computed in this frame, so no new positive directions are claimed. Coverage remains 85 plus all original F112, with the CC110 physical guard greater than 1e-38; 27 retained dimensions and whole original positivity at 1.06 remain open.

## Fresh frame recovery

CC111 freshly reruns the unchanged DNE44 physical materializer against the authenticated original DNE32 certificate and its dependencies already held in CC. Both output hashes agree exactly with the normalized packet hashes in the DNE44 complete source replays. Each raw packet has freshly checked exact retained rank 44. Every positive physical column is reconstructed from these raw columns and the exact B embedding and agrees exactly with the DNE44 certificate. Analytic basis and form-domain theorems remain inherited.

The Native NF55 response frame is distinct. Its complete native/source crosses cannot be relabeled as Z44 crosses. Current imported certified data contain Q44 and G44, but not the required Z44/Y native and source crosses for a paid high response family Y. This is a specific missing computation, rather than a failure of the source-response identity.

## Complete paid plain gate

Use the invertible frame J=(B,D) from CC110. Write

    J^t H J = [ A  E ; E^t  F ], H=kQ44-G44.

CC proves A positive with its frozen exact triangular congruence, constructs a rational approximate inverse, and bounds its residual to enclose A^-1. The residual row bounds are approximately 1.5789e-6 even and 2.4883e-9 odd, both strictly below one. It then pays every mixed term in

    S_plain = F-E^t A^-1 E.

Both negative gates are certified by fresh rational positive proofs of -S_plain. The numerical table is in these exact frozen embedding coordinates and comparison units; values are not physical eigenvalues.

| Parity | Positive block | Deficit gate | Paid upper threshold for isotropic deficit credit |
|---|---:|---:|---:|
| Even | 42 | 2 | 4.609137420596885 |
| Odd | 43 | 1 | 0.2782684789980162 |

The last column is a paid row-norm upper bound for -S_plain. A hypothetical correction with zero positive-block and mixed blocks and deficit block tI passes when t is strictly larger. The consumer verifies this with t equal to the exact bound plus 1e-12. This validates the acceptance calculation; it does not construct an original response credit. Exact matrices, inverse residuals, negative proofs and hypothetical positive controls are recorded in `notes/data/RPB108_CC111_RESPONSE_DEFICIT_GATE_20261010.json`.

## Actual response gate and rank obstruction

For a paid original high family Y, let N=G_Y/k-Q_Y and W=S_ZY-k Q_ZY. The form-unit response correction is Delta=k^-2 W N^-1 W^t, requiring the high-surplus and denominator positivity and a paid inverse. In comparison units K=k Delta. Transform K with J and retain every block. The full response certificate requires positivity of

    F+K_DD-(E+K_BD)^t(A+K_BB)^-1(E+K_BD).

Its positive block A+K_BB is positive in the exact model since K is positive semidefinite; interval arithmetic must still pay a positive proof and inverse. The correction changes this inverse and its mixed crosses. Therefore passing directional credits on the D columns or adding credit directly to S_plain is insufficient unless zero positive/mixed blocks have actually been proved.

The rank obstruction is exact. H has a negative subspace of dimension z. If a positive semidefinite correction has rank less than z, its kernel intersects that negative subspace nontrivially, leaving a negative vector. Thus an actual full-packet rescue needs response rank at least two even and one odd; at least as many independent paid high columns are necessary. Rank one cannot rescue the even packet. Larger rank is allowed and may be needed by the actual arithmetic.

The saved native D-column bounds also give necessary form-unit response credits: approximately 7.6437 and 4.4935 even, and 0.46147 odd. Exact conservative fractions are saved. These are necessary directional bounds, not sufficient collective thresholds and not physical gap estimates.

## Input cost and next computation

At the minimum possible high dimension, a dense full Z44 response needs 44r signed source crosses and r(r+1)/2 source high-high moments, plus the analogous native moments and exact physical high Gram. That is 91 source and 91 native moment slots for r=2 even, and 45 source and 45 native slots for r=1 odd. These counts describe a dense input layout before any exact identities or authenticated reuse; they are not lower bounds on independent integration work or runtime.

The reduced inverse is small only after paying the full positive-block inverse and all response crosses. No computational savings over plain remaining-source certification are established. The next substantive response step is to select original high vectors, certify their full Z44/Y native and source data, and evaluate the complete corrected gate above at the same 0.603 floor. A positive result would give the desired same-floor collective separation, since plain full-packet failure is already certified. A negative or unresolved sufficient response gate would not prove original form negativity.

No source integrations or true infinite-high inverse are evaluated in CC111. No Native or DNE branch receives writes. The highest whole-aperture anchor remains 21/20; whole 53/50, RH, F4 and Lean remain open.

## Reproduction

From the integration root:

```sh
python scripts/certify_cc111_response_deficit_gate.py --output notes/data/RPB108_CC111_RESPONSE_DEFICIT_GATE_20261010.json
```

Require exact raw packet hashes and positive physical reconstruction, both paid positive-block inverses, negative plain deficit gates and clearly marked hypothetical positive controls. Milestone custody records newly written artifact hashes. Prior immutable imported certificates and validators remain at their existing repository paths.
