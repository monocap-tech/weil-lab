# Reflected packet bridge 108 — Native Source NF44

NF44 continues NF43 on the same original source front at aperture 53/50. Terminology is defined in `docs/TERMINOLOGY_RPB108_SIXTH_INVERSE_SOURCE_NF44.md`; prior milestone notes remain historical and unchanged.

## Construction and custody

The five original physical columns H5, joined three-polynomial family, retained projection and signed source family R are inherited without replacement. NF43's updated rational witness h5 selects q5=A2^-1 R h5 through the original five-column Woodbury packet. NF44 freezes a sixth rational physical polynomial separately for each parity on degrees116..180 even and117..179 odd. Exact projection removes the two original high tails and the NF43 fifth tail; the two boundary columns have zero coordinates on this shell. Thus y6 is exactly orthogonal to all five prior physical columns.

Midpoint selection is only trial selection. The native energy, eight native cross entries, complete projected-source square and eight signed source covariances are independently enclosed using the same endpoint logarithm, degree-320 regular kernel, degree-40 signed poles, 13 translation cells and analytic/error payments. Native crosses are checked in both action orders. Five authenticated NF43 files and original archive hashes guard custody.

Writing C6=H6*(A-kappa I)H6, T6=((A-kappa I)H6)*((A-kappa I)H6), W6=R*(A-kappa I)H6 and N6=C6+T6/kappa, the conditional inverse upper packet is

R*A3^-1 R = G/kappa - W6 N6^-1 W6*/kappa^2,

where kappa=207/1000 and G=R*R. Certified positivity of C6 and N6 and the original hypothesis A>=kappa I give A>=A3>=A2. The additional conditional response is R*(A2^-1-A3^-1)R. The same joined native Q gives lower certificate Q-R*A3^-1 R.

## Validation and result

The exact six-versus-five Woodbury response equals the scalar defect update at the rational midpoint packet, with positive scalar defect and denominator; this exact response lies inside the paid original interval matrix. The complete independent moment replay checks all sixth-source coordinates, native action in both orders, reverse source covariances, enlarged-packet assembly, matrix positivity, updated witnesses and sign tests. It also checks the five-source baseline against NF43 and retains packing, defect-response, full-block crossing and positive-whole-mass controls.

| Parity | Extra conditional response at NF43 witness | Six-source condensed margin | Necessary further response at updated witness |
|---|---:|---:|---:|
| Even | [4.813394471045e-25, 1.018865575474e-23] | [-8.688777243923e-23, -8.174675338534e-23] | > 8.175718291095e-23 |
| Odd | [2.631624815811e-22, 2.899621518445e-22] | [-1.998126769807e-22, -1.849061110464e-22] | > 1.850751993489e-22 |

Both leading two-coordinate blocks are certified positive. Both condensed margins and determinants remain negative, so the six-source lower minorants still fail to certify the joined sign. New rational witnesses are frozen from the six-source lower matrices. The additional response is positive at both NF43 witnesses. The odd margin improves markedly, while the even response remains small relative to its deficit. These numerical summaries are rounded for display; JSON certificates preserve exact rational endpoints.

Independent replay status: **PASS for both parities**, including the five-source NF43 baseline comparison and all inherited controls.

## Scope and next obligation

The floor A>=207/1000 I is an explicit inherited hypothesis, not newly proved. Failure of a lower estimator to certify positivity does not prove a negative original Weil form. Whole-domain positivity at53/50, RH, F4 and Lean closure are not claimed. The highest recorded whole-aperture certificate remains21/20.

The next source selection can use the updated six-source rational witness and the remaining inverse response. A complete original remaining-background transport and unconditional floor proof remain separate obligations.

## Reproduction

From the repository root, for each parity run `scripts/certify_native_sixth_inverse_source_nf44_106.py choose` with `--parity` and `--output`, then its `certify` mode with `--trial` and `--output`. The frozen trial files are retained, so certification does not require rerunning selection. Run `python scripts/validate_native_sixth_inverse_source_nf44_106.py --output notes/data/RPB108_NF44_INVERSE_WITNESS_VALIDATION_20261009.json` to independently replay both parities and inherited controls. The two parity replays use separate processes; no floating-point sign decision is used.
