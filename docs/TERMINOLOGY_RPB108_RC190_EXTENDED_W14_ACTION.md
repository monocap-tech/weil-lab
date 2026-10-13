# RC190 terminology: refined complete native w14 action

Historical wording remains unchanged. Native w14 is still the exact stored g polynomial on even degrees0..4094 plus the eta-weighted fifteen-moment tail on even degrees>=4096. Its native moment scale is977132. The supported canonical M=D^-1 L, D norm, and native seven-source frame retain their definitions.

- **p190**: an exact rational finite approximation of w14 on even degrees0..32766, with nonnegative coefficients at scale2^32. The discrepancy from both its native finite polynomial and its native analytic prefix is paid in D energy.
- **Q190(p190)**: a represented complete Cp190 action, C=D^-1 h. It has32768 even finite coefficients through65534, stored at scale10^30, and25 retained analytic output moments beyond65534. Its output moment scale32766*32767 is not the native w14 moment scale977132.
- **Centered Cw190 trial**: Q190(p190)+(1/2)t190, with t190 the unchanged native w14 source restricted to even degrees>=32768. Its entire input tail is paid using0<=C<=I, without cutoff commutation.
- **Finite regular input alpha190**: the exact native g polynomial through degree512. This is distinct from the quantized endpoint input p190. The complete native regular-input remainder includes g above512 and the full native analytic tail.
- **Extended regular output**: a degree-1536 finite representation of D^-1 R alpha190, using the inherited degree-192 analytic kernel and exact Beta/log-moment formulas, with its complete endpoint-log output tail paid.
- **Private regular interval precision**:600-digit directed Decimal contexts and600-digit upward rational square-root bounds used only in this new construction. Historical helper modules and checkpoint artifacts are not modified.
- **Complete RC190 canonical w14 action trial**: native w14 plus the centered Cw190 trial, the retained RC183 negative-r finite correction and exact negative-r native analytic tail, and the new extended regular polynomial. The separate endpoint, regular, and finite negative-r rounding errors are all paid.

The endpoint arithmetic is exact fixed-point integer arithmetic with proved overflow guards. The regular calculation uses directed Decimal intervals, not unverified floating-point sampling. This checkpoint does not evaluate a new five-source inverse width or close Stage I.
