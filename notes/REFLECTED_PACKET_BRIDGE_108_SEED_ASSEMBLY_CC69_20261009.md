# CC69 — native seed positivity and the mixed assembly boundary

Terminology: docs/TERMINOLOGY_RPB108_SEED_ASSEMBLY_CC69.md. Producer source head: 14ba1d21bd15656be6a1c1ce60f217cb703d93cc (NF26). Integration parent: 07f837876b47fcfb5fdad2ea041876af1f497cea (CC68).

NF26 uses genuinely additional original high modes: 33 even modes e116 through e180 and 32 odd modes e117 through e179. Its frozen rational trials retain the original NF18 seed directions. The complete original archimedean, prime and pole sources are reconstructed on all thirteen translation cells, including endpoint logarithms. Regular-kernel and pole errors are paid in physical norm; tiny corrected energies inherit authenticated native energies and paid small-correction pairings. Diagnostic coefficients select a trial only.

The fresh unmodified producer replay is recorded in the custody certificate. Complete source ratios P_v/(kappa Q(v)) lie in (0.9612,0.9619) even and (0.7612,0.7613) odd. The original directional Schur values have lower bounds greater than 3.32e-36 and 7.56e-32 respectively. Exact reflection parity gives zero mixed coefficient between these two seeds. Hence their two-dimensional retained Schur restriction is positive, including arbitrary collective combinations of these two fixed seeds. This is a real native gain beyond CC68: corrections outside H2 are not subject to its same-H2 estimator invariance.

We independently reconstruct the paid low-coordinate correction and consume CC62's original e0/e1 complete source bounds. For v=p-y,

    B = Q(e_j,p)-Q(e_j,y)-<r_ej,C^-1 r_v>.

The norm-only estimate gives |B|<=1.355804e-18 even and <=1.213947e-16 odd. The diagonal lower-bound budgets allow approximately 2.471393e-19 and 7.975891e-17. Exact rational comparisons show that the inverse-response norm term alone exceeds each budget. Thus this estimator cannot certify the four-direction union of the seed restriction with the low-two restriction. This result does not evaluate or reject the actual signed B.

The minimal additional scalar correlation sufficient for each same-parity assembly is an original signed enclosure of <r_ej,C^-1 r_v> tight enough that the resulting |B|^2 is below A_lower D_lower. A sharper joint block response bound or stronger diagonal lower bounds can also suffice. For the full retained space, the corresponding requirement is a positive lower bound for the collective Schur matrix, including all remaining same-parity retained couplings; two seed gates do not supply it.

The consumer checks three genuine two-by-two mixed crossings (positive, zero, negative ground level with fixed positive diagonals) and three positive whole-mass ground levels. These exact controls show why separate positive directional gates cannot establish assembly, and why zero must be distinguished from a positive level. They are elementary estimator controls, not models of all original Weil arithmetic.

Highest whole-domain anchor remains 21/20 with margin 1/(3*10^63). CC62's original E2+F112 gap remains 1/100. NF26 additionally excludes a null vector whose retained component lies in the two-seed span: minimizing over the coercive high form would give positive seed Schur energy, and a zero retained component is excluded by high coercivity. The two null exclusions do not imply exclusion on the sum of those retained subspaces. Whole 53/50 positivity, all-cap old-gap-independent leakage, the uniform defect-relative frame on actual critical eigenvectors, collective retained null exclusion, RH/F4, full transport and Lean remain open. No logical nonimplication from complete original Weil identities is claimed. Paused fronts and historical wording remain unchanged.

Reproduction from the repository root:

```sh
python3 scripts/certify_native_high_correction_nf26_106.py notes/data/RPB108_NF24_COMPENSATED_SOURCE_TARGETS_20261009.json notes/data/RPB108_NF26_FIXED_TRIAL_CC69_20261009.json notes/data/RPB108_NF24_COMPENSATED_SOURCE_CERTIFICATE_20261009.json --output /tmp/cc69_native_replay.json
python3 scripts/certify_seed_assembly_cc69.py /tmp/cc69_native_replay.json notes/data/RPB108_NF24_COMPENSATED_SOURCE_TARGETS_20261009.json notes/data/RPB108_LOW2_HIGH_LEAKAGE_CC62_CERTIFICATE_20261009.json --output /tmp/cc69_assembly_replay.json
```

The native replay output equals notes/data/RPB108_NF26_SOURCE_INPUT_CC69_20261009.json byte for byte; the consumer output equals the published CC69 assembly certificate.
