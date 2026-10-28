# Weil-Lab NF373 — original matched exterior endpoint-jet extraction

**Research standing:** ORIGINAL-CARRIER NATIVE COMPUTATION AUTHORED; until focused CI and independent replay pass, numerical outputs remain **PENDING/UNACCEPTED**. This is an additive GitHub-native follow-up to NF372, not a substitute for the original infinite Schur and not an RH proof. The original `J242`, four PR348 source functions, original NF369 exact dyadic `Y0`, and NF370 preconditioner `T` are unchanged.

## Previous cursor → current gate → next

NF372 established that the **raw source** high-frequency signed multiplier tails are below a quarter of the four NF370 strong-residual budgets at `Lambda=2^24`. It also stopped the naive absolute-second-derivative bound for the **full** matched trial. The remaining high-tail obligation is **not** the raw source; it is the physically correlated correction

\[
 w_i = (I-P_J)F\,(I_4+Y_0)T e_i.
\]

The endpoint of `w_i` cannot be deduced from the very small inherited physical quotient Gram: point trace is not continuous in the logarithmic-energy topology. The next valid step is to compute the original selected-space projection, then evaluate the actual four boundary jets before another high-band integral.

## Finite original-object projection, no 242-dimensional *energy* inverse

Let `g_a` be the **unchanged 241 selected polynomial-trigonometric odd generators** from the SHA-pinned PR350 original physical rank inventory, plus the original supported `sinh(x/2)` as the 242nd. Let `F_k` be the unchanged four 32-sine-plus-sinh functions from PR355. On `I=[-11/10,11/10]`, define the **physical** Gram and overlaps

\[
 H_{ab}=\langle g_a,g_b\rangle_{L^2(I)},\qquad
 V_{ak}=\langle g_a,F_k\rangle_{L^2(I)}.
\]

The physical projection coefficients are `X=H^{-1}V`. We need not invert an ill-conditioned raw `H` directly: take a **fixed midpoint/dyadic physical frame** `D` from the original selected Gram, independently certify `N=D^T H D` is within row distance `<0.01` from the identity, then compute

\[
 X = D\,(D^T H D)^{-1} D^T V.
\]

Its normal-equation residual `HX−V` is checked with outward Arb intervals. Independently compare the recomputed original quotient Gram `F^*F−V^*X` against the **archived NF369 native interval quotient Gram** entry-by-entry: any empty intersection is a hard STOP, not a new mathematical result.

Write the previously accepted exact dyadic `M=(I_4+Y0)T`. Then

\[
 w_i(B) = \sum_k F_k(B) M_{ki}-\sum_a g_a(B)(XM)_{ai},
\]
\[
 w_i'(B) = \sum_k F'_k(B) M_{ki}-\sum_a g_a'(B)(XM)_{ai},\qquad B=11/10.
\]

The generated native interval report must output **all four** endpoint jets with outward enclosures, including direction 4. The physical projection and source transformations use the original rational coefficients throughout; no new witness, selected-space enlargement or additional sign assumption is allowed.

For raw generators `g_{c,k}(x)=x^k sin(2πcx)` with even `k` or `x^k cos(2πcx)` with odd `k`, the derivatives are elementary and evaluable in Arb at the original rational `B`. The supported sinh has derivative `(1/2)cosh(B/2)`. Do not replace it with a sampled quadrature proxy or omit the pole from the selected projection.

## Trust and acceptance boundary

- Script `scripts/verify_nf373_original_exterior_endpoint_jets.py` reads the repository's restored exact PR350 rank JSON, and PR355/NF369 **field slices** that were extracted after SHA checking the complete original ZIP/JSON at NF372. It checks the exact historical SHA256 values for those three input JSONs.
- Native original projection is computed fresh by `python-flint==0.8.0` at 4096-bit precision in the focused GitHub CI; an independent original ZIP/JSON/Arb full parent replay is **not** performed here.
- CI must check the original physical Gram normalization, native NF369 quotient interval overlap and all four outward endpoint enclosures. A failure is a STOP or verification issue, **not** a signed Weil negative witness.
- This pass **does not** upper-bound the high-frequency multiplier action on `w_i`, its full second-derivative L1 norm, the matched low-band residual, `R^*C^{-1}R`, the other 238 selected directions, general operator-domain closure, W-ODD-NEG, even/whole Weil or RH.

**Immediate next after a successful endpoint report:** use the exact resulting boundary jets to build a cancellation-aware estimate of `m(D) w_i` on `|ξ|>2^24`; only then calculate correlated selected-space lowband residuals. If one jet shows no feasible margin, STOP/retype this **method** before another source/precision campaign.

**GitHub custody:** default, without per-pass authorization. Attach producer, this note, focused CI and pinned inputs on a new stacked draft continuation of PR #357; do not overwrite NF356–NF372 historical evidence.
