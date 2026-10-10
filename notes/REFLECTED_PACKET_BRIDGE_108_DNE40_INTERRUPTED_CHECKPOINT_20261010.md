# RPB108 — DNE40 prepared source expansion; computation interrupted

Parent certified head: DNE39, `f15eea0a2d0a4b527bf62d73c17efd940b6eb12f`, on `research/rpb108-direct-null-exclusion`.

**Status: prepared and syntax-checked; source computation interrupted by workspace transport loss. No DNE40 source certificate, signed comparison, validation PASS, new positivity rank or new physical guard is claimed.** DNE39 remains the last certified mathematical result: original infinite F112 floor 289/500, 28 retained directions per parity plus all F112, total retained rank 56, common physical guard 1e-38. Whole aperture 1.06 positivity and RH remain open.

Terminology was registered before launching source computations in `docs/TERMINOLOGY_RPB108_DNE40_INCREMENTAL_JOINT_SOURCE.md`. The four prepared scripts are preserved here to enable recovery without changing historical certificates.

## Intended calculation

Use Z36=(T4 S,X[0:32]) from the unchanged DNE32 physical frame X=hatY U. Preserve every native mixed entry (Ps-As J)U32. Native normalization does not imply physical normalization.

Compute the whole original projected source Gram G36, including every infinite F112 tail, exact logarithmic endpoints, signed pole and all six prime powers in both orientations. Reuse DNE38's first 28 columns at matching order and precision: 406 upper-triangle integrals and existing retained coordinates remain unchanged. Compute all 260 new upper-triangle pairs and the 56 retained source coordinates for each of eight new columns. Reconstruct all 36 source columns to check identical old rounding ledgers; rebuild all physical error payments.

The producer uses analytic polynomial/log/log-squared cell integrals, exact signed packed convolution with a no-carry assertion, 250-digit coefficient grids and 100-digit stored outward grids. Primary order/precision is 360/600; replay 400/620. No quadrature supplies a certificate.

After source completion, test H40=(289/500)N36-G36. Rational congruences and outward Gershgorin margins certify positive prefixes. Paid exact rational negative trials certify failure of this sufficient uniform-floor bound, without proving original Weil negativity or a null vector. Audit exact retained rank and the physical square-completion guard, preserving all source correlations and physical masses. The true high inverse is not evaluated.

## Observed interruption and recovery

Four independent process runs were launched, one per parity and order. The last observed logs confirm all 36 source columns reconstructed: even primary 314.0 seconds, even replay 379.2 seconds, odd primary 311.0 seconds, odd replay 375.7 seconds. All four were active in moment/integral computation at the last process check. The workspace transport then disconnected. No completed cell-integral output or final source JSON was observed. Attempts to resume the process and workspace failed or timed out. Whether the jobs survived and whether their local outputs remain present is unknown.

Local workspace was `/workspace/scratch/4b99a57b283f/weil-lab`. Candidate outputs are `/tmp/dne40_even_360.json`, `/tmp/dne40_even_400.json`, `/tmp/dne40_odd_360.json`, `/tmp/dne40_odd_400.json`, with adjacent .log files. Existing session IDs were 54640, 30571, 62707, 30860 respectively. Recover and inspect these before restarting. Treat partial outputs as unvalidated.

## Reproduction and publication gate

Run `certify_dne40_joint_source_Gram.py PARITY --output SOURCE.json` for each parity at defaults, then with DNE16_ORDER=400 and DNE16_PRECISION=620 for replay. Original helper and DNE32/DNE38 inputs must be present at their recorded authenticated paths. Compress completed JSON with deterministic gzip (mtime=0) and base64 into new DNE40 notes/data source paths.

Run `certify_dne40_signed_comparison.py PRIMARY REPLAY --output COMPARISON.json` per parity with unchanged DNE39 high certificates present. Run `validate_dne40_signed_source.py EVEN_PRIMARY EVEN_REPLAY EVEN_COMPARISON ODD_PRIMARY ODD_REPLAY ODD_COMPARISON --output VALIDATION.json`. Require status PASS before any DNE40 mathematical claim. Record hashes, paid prefix ranks, failure controls, physical guards and custody. Publish final results additively, without rewriting this interruption record or older certificates.

The prepared four scripts passed Python syntax compilation before the disconnect. Their numerical results and enlarged source packets have not yet been validated.
