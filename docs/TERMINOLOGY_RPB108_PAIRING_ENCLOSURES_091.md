# RPB108 terminology: native/source enclosure comparison at 91/100

- **Source pairing enclosure P:** the independent exact supported integral evaluated with all source coefficient and moment interval widths retained.
- **Native energy enclosure Q:** the certified outward native matrix entry. Its interval width is retained in the corrected Schur test.
- **Actual source allowance eta_i:** the previously certified normalized row error. It remains unchanged and is distinct from either numerical enclosure width.
- **Interval gap:** max(0, P.lo-Q.hi, Q.lo-P.hi). The consistency audit requires this gap to be strictly below eta_i.
- **Enclosure comparison budget:** eta_i + width(P) + width(Q). The audit also verifies the maximal endpoint difference is below this budget. This is a numerical consistency guard, not an additional source-map error and not a replacement for the source approximation proof.
- **Residual correction:** the actual eta(2M+eta) remains computed from the original source map error and full residual trace. Native enclosure widths are already retained in Q and are not added to the source error.
- **Strict legacy checkpoint reuse:** the complete nine-panel checkpoint must retain its exact original constructor hash. The repaired script must match the entire original byte prefix through panel contractions, with all nonconstructor bindings verified by the original lossless decoder. Only the post-contraction comparison/reporting section changes.

Whole-domain positivity at 91/100 remains a claim only after complete repeated output, corrected sign and independent conversion validation.
