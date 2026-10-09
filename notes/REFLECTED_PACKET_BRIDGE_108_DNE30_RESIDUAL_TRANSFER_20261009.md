# RPB108 — DNE30: discharge NF42's floor and force its remaining response

Read [DNE30 terminology](../docs/TERMINOLOGY_RPB108_DNE30_RESIDUAL_TRANSFER.md) before the definitions below.
Parent DNE29: 30d1fae54150b1901bf8c83470b614a4d0d83397.
Read-only Phase NF42: f2c49f8d2ff95374d3ee2c3b1836ec772e4817dc.
Read-only Coupled CC81: 68d23fd4b746f9ae2496433d2ea34af38bd7b65d.
Only research/rpb108-direct-null-exclusion is written.

## Result and dependency

DNE17 discharges NF42's original high-floor hypothesis. DNE29's already certified positive Schur restriction also applies to NF42's same retained packet, despite their different finite high lifts. Consequently NF42's actual joined three-column Schur matrix is positive in both parities, and the actual residual response beyond its four-high-source minorant must exceed its negative model deficit.

This is a transfer and reconciliation of existing original certificates. The residual response lower bound depends on DNE29's positivity theorem; it is not an independently measured inverse response or a new retained-direction certificate.

| Derived quantity for NF42's frozen h | Even | Odd |
| --- | ---: | ---: |
| Actual joined Schur witness, strict lower h*L h | >9.21194e-22 | >2.10480e-19 |
| Necessary additional response after A1, refined screen | >9.39430e-23 | >1.45758e-21 |
| Forced actual residual h*T1 h, strict lower | >1.01513e-21 | >2.11937e-19 |
| Forced lower / necessary screen | >10.8058 | >145.4036 |
| Full scaled model-plus-residual margins | >0.2480,0.0980,0.4980 | >0.11998,0.19998,0.01998 |

The witness is the original NF38 frozen witness, with its third coefficient 1, and is not physically normalized. The refined screen intersects the original NF42 witness interval with a direct quadratic interval from its complete signed model matrix, so it is slightly stronger than CC81's displayed screen. These numbers bound the actual unknown residual; they do not evaluate it.

NF42's original four-high-source lower certificate remains negative, exactly as published. Its source-backed improvement becomes unconditional under DNE17. The actual original joined sign is positive by the independent DNE29 dependency. These statements are compatible: a negative lower estimator does not determine the sign of the actual form.

## The high operator and floor match

NF42's A is the original remaining high operator after physical projection off E112. DNE17's C is the original high restriction on F112=E112 orthogonal complement at the same aperture a=53/50. For finite original source columns and high form tests, both are defined by the same unshifted native Weil pairing. Equality of the closed restricted forms identifies their associated selfadjoint operators.

DNE17's complete prime Schur bound and inherited archimedean-minus-pole theorem give the original all-F112 inequality

    A>=11/25 I=0.44 I.

NF42 requires A>=207/1000 I=0.207 I. The hypothesis is therefore discharged with margin 233/1000. This uses an infinite-dimensional original form floor, not a compression to the four measured high polynomials. The NF42 field saying that its own turn did not newly prove that floor is preserved unchanged.

Under this discharged hypothesis, NF42's original source-backed minorant satisfies A>=A1>=0.207 I. Inverse order now applies unconditionally, so

    T1=R*(A1^-1-A^-1)R>=0.

NF42's previously conditional strictly positive source-backed witness credit from A0 to A1 is also unconditional. The new bounds below concern the additional response after A1, not that earlier credit.

## Exact invariance under changing finite high lifts

NF41 records the exact three base columns B used in NF42. DNE29 constructs T=B-Z Csel with NF38's two frozen high corrections Z and selected functionals Csel. Every correction coordinate is at least 112, so these shifts lie entirely in the original high form domain.

For fixed three-coordinate a, as f runs through the high form domain, f-Z Csel a runs through that same domain. Therefore

    inf_f Q(T a+f)=inf_f Q(B a+f).

Equivalently, with R_T=R-A Z Csel and the corresponding native Q_T,

    Q_T-R_T* A^-1 R_T=Q_B-R* A^-1 R=S.

The source/operator identities are valid because the finite polynomials have authenticated original physical L2 sources and A^-1 is bounded by the original high floor. No numerical approximation to the true inverse is used.

DNE29 pays the complete four-column low-plus-optimized source form at floor 0.44. Its three-column principal block supplies

    S>L=diag(ell_i/s_i^2),

with ell=(1/4,1/10,1/2) even and (3/25,1/5,1/50) odd. These are the three-column entries of DNE29's physical coarse diagonal, not its four-column source contraction credit. The same lower bound thus applies to the NF42 base packet.

The independent validator reconstructs every optimized coefficient from the base, both corrections and the selected functionals. It verifies unchanged retained coefficients, exact high support and equality of the NF38/NF42 frozen witness. Hash checks connect the full NF42 inputs to its original validation manifest, its NF41 parents and DNE29's imported exact polynomial records.

## A full signed residual bound

NF42 encloses the exact model quantity K1=Q_B-R*A1^-1R. Its status as a lower certificate for S does not make it the actual Schur matrix. The identity

    S=K1+T1

and the inherited S>L imply

    T1>L-K1.

To express a single rational matrix lower bound, scale by S_c=diag(s_i), intersect symmetric entry enclosures and form midpoint M. Let epsilon be the maximum row sum of the entry radii. Symmetry and the weighted product inequality give

    M-epsilon I<=S_c K1 S_c<=M+epsilon I.

Define D=diag(ell)-M-epsilon I. Then S_c T1 S_c>D. This D is a signed lower bound; it has negative diagonal entries in both sectors and is deliberately not called a positive semidefinite response matrix. T1 itself remains positive semidefinite by inverse order.

Adding the model's lower envelope to this forced residual floor gives

    (M-epsilon I)+D=diag(ell)-2 epsilon I>0.

All three exact margins are positive in both sectors. This is a complete mixed-coefficient acceptance in NF42's model coordinates, rather than a witness-only sign test. Its dependency on DNE29 remains explicit, so it does not create a second independent proof of the original positive restriction.

## Quantified frozen-witness consequence

For the already frozen NF42 witness h, let a=h*L h and let [wlo,whi] enclose h*K1 h. The signed-matrix interval and the published NF42 witness interval overlap; their intersection is used. The upper endpoint remains negative.

    h*T1 h>a-whi,
    necessary additional-response screen=-whi.

The strict lower bounds in the result table follow. The actual residual exceeds its necessary witness screen by the separately certified positive amount a. The full signed matrix bound, not merely this witness comparison, establishes the packet acceptance.

These response quantities do not certify the remaining 104-dimensional source Gram, a physical high floor beyond DNE17, or an all-aperture estimate. They identify how DNE's existing result constrains the actual residual operator that CC81 leaves unknown.

## Verification and custody

Primary and replay consumers respectively use the paid DNE29 primary and source-replay lower forms. Each passes 61 explicitly counted rational assertions. Their numerical rows are byte-identical; the output metadata records which dependency was used. The original NF42 native/source integrations and DNE17's expensive word/gate validator are not rerun.

The independent validator imports no producer code and passes 2,760 rational checks. In each parity it tests all 64 vertices of the symmetric three-by-three model box, checking every principal minor of both envelope differences for nonnegativity. This pays the model envelopes throughout the boxes by convexity. It checks the signed residual floor, its indefinite status, all acceptance margins, exact frame reconstruction, witness interval intersection and forced response values.

Six exact full-block controls cross positive/null/negative at two scales while their native retained and high blocks remain positive. Changing finite high lifts preserves their Schur matrices exactly. Three positive whole-physical-mass shifts preserve the true null's shifted eigenlevel and show why a retained-only shift misses it. Three controls also confirm that a positive finite high compression cannot establish a uniform high floor. These are abstract controls, not original Weil countermodels. Syntax checks pass.

The two complete NF42 certificates are preserved as deterministic gzip/base64 imports; their decoded hashes agree with the original NF42 validation manifest. The manifest itself is preserved unchanged. Inherited DNE files remain immutable dependencies. All output and import hashes are recorded in custody.

## Scope and next remaining calculation

The same six retained directions of NF42 are already contained in DNE's eight-dimensional Z8. No positive retained direction is added. DNE29's common physical guard 2.4*10^-35 on Z8+F112 is unchanged. The remaining dimension is still 104.

This resolves NF42's conditional floor for the actual original operator and transfers the actual joined sign from DNE. It does not improve NF42's computed four-high lower model, measure T1, construct the optimized native energy orthogonal remainder or certify its complete source Gram. The remaining DNE test is still c B_Y-Gamma_Y>0 on the optimized remainder, with c=0.11 even and 0.14 odd. An actual full remaining response or source bound is still required for whole 1.06 positivity.

Phase and Coupled are read only at their pinned heads. Their historical packet outcomes are not rewritten. Whole 1.06 positivity, exact unit-response exclusion on the 104-dimensional remainder, all-aperture continuation, RH/F4/full transport and Lean remain open. The transfer is an argument from inherited original closed-form/source theorems plus exact arithmetic, not Lean closure.

## Reproduction

```sh
python3 scripts/certify_dne30_residual_transfer.py notes/data/RPB108_DNE30_MANIFEST_20261009.json --output /tmp/dne30.json
python3 scripts/certify_dne30_residual_transfer.py notes/data/RPB108_DNE30_MANIFEST_20261009.json --replay-bounds --output /tmp/dne30_replay.json
python3 scripts/validate_dne30_residual_transfer.py notes/data/RPB108_DNE30_MANIFEST_20261009.json /tmp/dne30.json /tmp/dne30_replay.json /tmp/dne30_validation.json
```

The manifest supplies pinned original dependencies and encoded imports. Custody preserves raw/decoded hashes and the write/read branch heads.
